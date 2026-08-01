<!-- 
This file was automatically translated from English to Korean.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 로컬 AI 아키텍처

대규모 언어 모델을 완전히 온디바이스에서 실행하기 위한 실용 가이드입니다. 하드웨어 고려 사항, 추론 엔진, 메모리 최적화, 엣지 배포를 위한 시스템 설계를 다룹니다.

---

## 왜 AI를 로컬에서 실행할까?

- **Privacy**: 데이터가 기기 밖으로 나가지 않습니다.
- **Cost**: 토큰당 API 비용이 들지 않습니다.
- **Latency**: 네트워크에 의존하지 않아 지연 시간이 예측 가능합니다.
- **Offline availability**: 인터넷 없이도 동작합니다.
- **Control**: 모델 버전, 커스터마이징, fine-tuning을 완전히 통제할 수 있습니다.

---

## 하드웨어 요구 사항

### GPU 메모리 (VRAM)
가장 중요한 자원입니다. 메모리에서의 모델 크기 ≈ **parameters × bytes per parameter**입니다.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**실전 가이드라인:**
- 8GB VRAM → 4-bit 기준 최대 7B 모델
- 12GB VRAM → 4-bit 기준 최대 13B 모델
- 24GB VRAM → 4-bit 기준 최대 70B 모델(또는 8-bit 기준 13B)
- Apple Silicon(통합 메모리)은 64GB+ 시스템에서 70B 모델까지 실행할 수 있습니다.

### RAM (System Memory)
- CPU 추론을 위해서는 모델을 메모리에 올릴 수 있을 만큼 충분한 시스템 RAM이 필요합니다(VRAM 수치와 비슷한 수준).
- GPU 추론에서는 모델을 VRAM으로 오프로딩하기 전에 메모리에 적재해야 하므로 시스템 RAM도 중요합니다.

### Storage
- 양자화된 모델 가중치는 수 GB 정도의 공간을 차지합니다(예: 4-bit 7B ≈ 디스크에서 4 GB). 여러 모델을 위해 최소 20–50 GB의 여유 공간을 확보하세요.

### CPU
- 프롬프트 처리(prefill)와 CPU 오프로딩에는 최신 멀티코어 CPU가 도움이 됩니다.
- Apple M-series 칩은 통합 메모리와 Neural Engine 덕분에 LLM 실행 성능이 매우 뛰어납니다.

---

## 양자화

양자화는 가중치의 수치 정밀도를 낮춰, 약간의 정확도 손실만으로 메모리 사용량을 크게 줄이고 속도를 높이는 방법입니다.

### 널리 쓰이는 형식

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp 형식, CPU/GPU 하이브리드에 최적화 | 로컬 추론에 가장 적합 |
| **GPTQ** | 4–8 | GPU 전용, CUDA에서 효율적 | NVIDIA GPU에 가장 적합 |
| **AWQ** | 4 | activation-aware 방식, GPU 전용 | GPU 배치 추론에 적합 |
| **ONNX** | variable | 표준화된 크로스플랫폼 형식 | 프로덕션 서빙 |

### 양자화 수준 선택
- **Q8_0** (8-bit): 품질 손실이 거의 없지만 크기가 가장 큽니다.
- **Q6_K** (6-bit): 품질이 좋고 압축률도 준수합니다.
- **Q5_K_M** (5-bit): 흔히 쓰이는 균형점입니다.
- **Q4_K_M** (4-bit): 가장 작고, 대부분의 작업에서 수용 가능한 품질을 제공합니다.
- **IQ4_XS** / **IQ3_XS**: 4/3-bit에서 더 나은 perplexity를 제공하는 개선된 양자화 방식입니다.

**실전 요령:** 품질과 크기의 균형을 위해 Q4_K_M을 우선 고려하세요. VRAM에 여유가 있다면 Q5나 Q6를 사용하세요.

---

## 로컬 추론 엔진

### llama.cpp
- C++로 작성되었습니다.
- GGUF 형식을 지원합니다.
- CPU와 GPU(CUDA, Metal, OpenCL 경유)에 최적화되어 있습니다.
- 특히 CPU에서 매우 빠릅니다.
- 명령줄, 서버 모드, Python 바인딩을 제공합니다.

**예시 명령어:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32는 32개 레이어를 GPU로 오프로딩한다는 뜻입니다.)

Ollama
llama.cpp를 간단한 CLI와 REST API로 감싼 도구입니다.

모델을 자동으로 다운로드하고 관리합니다.

프로토타이핑과 데스크톱 앱에 매우 적합합니다.

시스템 프롬프트를 위한 사용자 정의 Modelfiles를 지원합니다.

사용 방법:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Windows, macOS, Linux용 그래픽 데스크톱 앱입니다.

원클릭 다운로드와 채팅 인터페이스를 제공합니다.

OpenAI 호환 API를 제공하는 내장 로컬 서버가 있습니다.

비기술 사용자와 빠른 테스트에 적합합니다.

Hugging Face Transformers + bitsandbytes
HF 모델을 위한 표준 Python 라이브러리입니다.

`load_in_4bit=True`와 함께 bitsandbytes를 사용하면 4-bit 양자화를 적용할 수 있습니다.

fine-tuning에는 더 유연하지만, 추론 속도는 llama.cpp보다 느립니다.

ExLlamaV2
GPTQ와 AWQ를 위한 매우 빠른 GPU 추론 엔진입니다.

NVIDIA GPU에서 최고의 성능을 발휘합니다.

배치 생성도 지원합니다.

mlx (Apple)
Apple의 M-series 칩을 위한 프레임워크입니다.

Apple Silicon에 매우 최적화되어 있습니다.

Python API를 제공합니다.

메모리 관리
컨텍스트 윈도우와 KV 캐시
KV cache는 컨텍스트의 모든 레이어와 모든 토큰에 대한 key-value 쌍을 저장합니다. 컨텍스트 길이가 길어질수록 선형적으로 증가합니다.

메모리 비용 ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

32-layer 모델에서 KV heads가 8개이고 head dim이 128이라면, 토큰 하나당 비용은 약 ~32 × 8 × 128 × 2 bytes = 65 KB입니다. 128k tokens라면 cache만으로 약 8 GB가 필요합니다.

오프로딩 전략
레이어 오프로딩: 일부 레이어는 GPU에, 나머지는 CPU에 배치합니다. 순수 CPU보다 빠르고 필요한 VRAM도 더 적습니다.

토큰 스트리밍: 한 번에 모두 처리하지 않고 토큰을 점진적으로 처리합니다.

프롬프트 캐싱
유사한 프롬프트 사이에서 KV cache를 재사용해 prefill 단계를 다시 계산하는 비용을 줄입니다. 일부 프레임워크는 이를 지원합니다(예: vLLM, `--prompt-cache`를 사용하는 llama.cpp).

메모리 매핑 파일
모델 가중치를 전부 RAM에 올리지 않고 디스크에서 직접 읽습니다. 메모리가 제한된 시스템에서 대형 모델을 다룰 때 유용하며, llama.cpp는 기본적으로 memory-mapping을 사용합니다.

배포 아키텍처
단일 기기 모드
하나의 모델을 하나의 기기(노트북, 스마트폰, 엣지 디바이스)에서 실행하는 방식입니다. 개인 비서, 메모 앱, 코드 완성 등에 활용됩니다.

하이브리드 엣지-클라우드
로컬 모델이 일반적인 질의를 처리하고, 복잡한 질문은 클라우드 모델로 넘깁니다. 대부분의 경우에는 속도와 프라이버시를, 예외적인 경우에는 높은 성능을 얻을 수 있어 양쪽의 장점을 모두 살릴 수 있습니다.

분산 추론(Multi-GPU)
더 큰 모델은 여러 GPU에 레이어를 나눠 배치하거나(tensor parallelism), 컨텍스트를 여러 장치에 나눌 수 있습니다(pipeline parallelism). llama.cpp에서는 `-ngl`, ExLlamaV2에서는 `--num-gpu-layers`를 사용합니다.

모바일 배포
Android: JNI bindings 또는 ML Kit를 통해 llama.cpp를 사용할 수 있습니다.

iOS: Swift bindings 또는 mlx를 통해 llama.cpp를 사용할 수 있습니다.

Web: WebLLM(WebGPU에서 ONNX runtime으로 실행) 또는 transformers.js를 사용할 수 있습니다.

성능 최적화
Flash Attention
attention 계산을 더 빠르게 하고 메모리 사용량도 줄여 줍니다. llama.cpp, ExLlamaV2, 최신 transformers 라이브러리에서 사용할 수 있습니다.

배치 추론
여러 프롬프트를 하나의 forward pass로 함께 처리합니다. 처리량이 크게 증가하며 llama-batch 또는 vLLM을 사용할 수 있습니다.

조기 종료 / 토큰 예산 관리
최대 token budget을 설정해 생성이 무한정 길어지는 것을 막습니다.

추측적 디코딩
작고 빠른 모델(draft model)이 토큰을 먼저 예측하고, 큰 모델이 이를 병렬로 검증하는 방식입니다. 2–3배의 속도 향상을 얻을 수 있습니다.

실전 설정 가이드
1. Ollama 설치
bash
curl -fsSL https://ollama.com/install.sh | sh
2. 모델 가져오기
bash
ollama pull phi3:3.8b-q4_K_M
3. API로 실행
bash
ollama serve
그다음 `http://localhost:11434/api/generate`로 요청을 보내면 됩니다.

4. Python 연동
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Alternative) llama.cpp 직접 사용
bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
모니터링과 가시성
Linux에서는 `nvidia-smi`, macOS에서는 Activity Monitor로 GPU 사용률을 추적하세요.

메모리 사용량(RAM과 VRAM)을 추적하세요.

초당 토큰 수(throughput)를 추적하세요.

첫 토큰이 출력되기까지 걸리는 시간(latency)을 추적하세요.

llama.cpp 또는 Ollama의 내장 로깅을 활용하세요.

한계와 트레이드오프
품질 격차: 소형 로컬 모델(3.8B–7B)은 복잡한 추론에서 일반적으로 대형 클라우드 모델(GPT-4, Claude 3.5)보다 성능이 낮습니다.

지식 cutoff: 모델의 지식은 학습 시점에 고정되므로, 최신 정보가 필요하면 RAG를 사용해 보완해야 합니다.

다국어 성능: 작은 모델은 다국어 처리 능력이 상대적으로 떨어질 수 있습니다.

도구 사용: 소형 모델에서는 agentic workflow(function calling)의 신뢰성이 낮을 수 있습니다.

그럼에도 일상적인 많은 작업(요약, Q&A, 코드 완성, 분류)에서는 로컬 모델이 이미 충분히 실용적이며 빠르게 개선되고 있습니다.

텍스트

---

## 파일 4: `security_best_practices.md`

```markdown
# 보안 모범 사례

애플리케이션, 인프라, 데이터를 개발 단계부터 프로덕션까지 안전하게 보호하기 위한 실용 가이드입니다.

---

## OWASP Top 10 (2021) — 개요

1. **Broken Access Control**: 사용자가 접근해서는 안 되는 리소스에 접근할 수 있는 문제입니다.
2. **Cryptographic Failures**: 암호화가 약하거나 아예 적용되지 않은 상태입니다.
3. **Injection**: SQL, NoSQL, OS command, LDAP injection과 같은 주입 공격입니다.
4. **Insecure Design**: 아키텍처 수준의 설계 결함입니다.
5. **Security Misconfiguration**: 기본 비밀번호, 열린 포트, 과도하게 자세한 오류 메시지 같은 설정 문제입니다.
6. **Vulnerable and Outdated Components**: 의존성에 알려진 CVE가 존재하는 상태입니다.
7. **Identification and Authentication Failures**: 취약한 비밀번호나 잘못된 세션 관리 같은 인증 실패입니다.
8. **Software and Data Integrity Failures**: 공급망 공격, 서명되지 않은 업데이트 같은 무결성 문제입니다.
9. **Security Logging and Monitoring Failures**: 침해를 탐지하지 못하는 로깅·모니터링 문제입니다.
10. **Server-Side Request Forgery (SSRF)**: 서버를 악용해 내부 시스템으로 요청을 보내게 만드는 취약점입니다.

---

## 입력 검증과 출력 인코딩

### 검증 규칙
- **Whitelist > Blacklist**: 알려진 나쁜 패턴을 막는 것보다 허용할 패턴을 먼저 정의하세요(예: email 검사용 regex).
- **Length limits**: buffer overflow와 DoS를 막기 위해 최대 길이를 강제하세요.
- **Type checking**: 정수는 정수인지, 불리언은 불리언인지 확인하세요.
- **Use well-tested libraries**: email, URL, date validation에는 표준 라이브러리를 사용하세요(예: Python의 `email-validator`, Node의 `validator.js`).

### 출력 인코딩
- **HTML encoding**: XSS를 막기 위해 `<`, `>`, `&`, `"`, `'`를 인코딩하세요.
- **SQL parameterisation**: 사용자 입력을 SQL 쿼리에 직접 이어 붙이지 마세요. parameterised queries(prepared statements)나 ORM을 사용하세요.
- **Shell escaping**: 사용자 입력으로 shell 명령을 구성하는 일은 피하고, 불가피하다면 `shlex.quote()` 같은 방법을 사용하세요.

---

## 인증과 권한 부여

### 비밀번호 관리
- **Hashing**: 비밀번호는 **Argon2id**(권장), **bcrypt**, **scrypt**, **PBKDF2** 같은 강력하고 느린 해시 알고리즘으로 저장하세요.
- **Salting**: 사용자마다 고유한 salt를 추가하세요.
- **Minimum length**: 최소 12–16자를 강제하세요.
- **MFA (Multi-Factor Authentication)**: 민감한 작업에는 두 번째 인증 수단(TOTP, SMS, hardware key)을 요구하세요.
- **Rate limiting**: 로그인 엔드포인트에서 brute-force 시도를 막으세요(예: IP/사용자당 5분에 5회).

### 세션 관리
- session token에는 secure, HTTP-only, SameSite cookie를 사용하세요.
- 적절한 만료 시간을 설정하세요.
- 로그아웃 시와 비밀번호 변경 시 세션을 무효화하세요.
- URL에 session ID를 노출하지 마세요.

### OAuth2 / OIDC
- 검증된 라이브러리를 사용하세요(예: Authlib, PyJWT, Passport.js, Spring Security).
- ID token은 signature, issuer, audience, expiration을 철저히 검증하세요.
- CSRF 방지를 위해 state parameter를 사용하세요.
- client secret은 안전하게 보호하세요.

### JWT (JSON Web Tokens)
- **Sign**: 더 강한 보안을 위해 RS256 또는 ES256(비대칭 방식)을 사용하세요. 공유 비밀을 잘 관리할 수 있다면 HS256(대칭 방식)도 사용할 수 있습니다.
- **Validate**: signature, issuer (`iss`), audience (`aud`), expiration (`exp`)을 항상 검증하세요.
- **Keep short expiration**: access token은 15–60분 정도의 짧은 만료 시간을 두고, 더 긴 세션에는 refresh token을 사용하세요.
- **Store securely**: JWT를 localStorage에 저장하지 마세요(XSS에 취약함). 대신 HTTP-only cookie를 사용하세요.

---

## API 보안

### 인증
- 공개 엔드포인트를 제외한 모든 API 호출은 항상 인증하세요.
- basic auth보다 API key나 OAuth2 token을 우선 사용하세요. basic auth는 매 요청마다 자격 증명을 전송합니다.

### 속도 제한과 스로틀링
- abuse와 DoS를 방지하기 위해 사용자별·IP별 rate limit을 적용하세요.
- `Retry-After` 헤더와 함께 `429 Too Many Requests`를 반환하세요.

### CORS (Cross-Origin Resource Sharing)
- 허용할 origin만 명시적으로 열어 두세요(프로덕션에서는 절대 `*` 사용 금지).
- 서버 측에서 `Origin` 헤더를 검증하세요.

### 입력 검증
- header와 body를 포함한 모든 요청 파라미터를 검증하세요.
- 예상하지 못한 필드는 거부하세요(JSON Schema의 `"strict": true` 또는 `additionalProperties: false`).

### HTTPS / TLS
- 프로덕션에서는 HTTPS를 강제하세요.
- HSTS (HTTP Strict Transport Security)를 사용해 브라우저가 HTTPS만 사용하도록 하세요.
- TLS 1.2 또는 1.3을 사용하고 TLS 1.0/1.1은 비활성화하세요.

---

## 비밀정보 관리

### 비밀정보를 하드코딩하지 말 것
- secrets(API keys, passwords, database URLs)를 source control에 커밋하지 마세요.
- environment variables 또는 secret management 도구를 사용하세요.

### 도구
- **HashiCorp Vault**: 엔터프라이즈급 동적 secret 관리 도구입니다.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: 클라우드 네이티브 secret 관리 서비스입니다.
- **SOPS**: 파일 안의 secrets를 암호화하고 KMS 또는 GPG와 함께 커밋할 수 있게 해줍니다.
- **Docker secrets**: Swarm mode용 기능입니다. Kubernetes secrets는 base64 인코딩일 뿐이므로 주의해서 사용하고, 필요하다면 external Secrets Store CSI driver를 검토하세요.

### Rotation
- secrets와 service account를 정기적으로 교체하세요.
- 가능하다면 rotation을 자동화하세요.

---

## 의존성 관리

### 취약점 스캔
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot`(GitHub), `Renovate`, `Trivy`.

### 패치 관리
- 의존성은 패치된 버전으로 계속 업데이트하세요.
- minor/patch 업데이트를 위한 자동 pull request를 설정하세요.
- breaking change 여부를 changelog로 검토하세요.

### 공급망 무결성
- 재현 가능한 빌드를 위해 `package-lock.json`, `Cargo.lock`, `go.sum` 같은 package lockfile을 사용하세요.
- 다운로드한 의존성의 checksum을 검증하세요.
- 공식 registry를 우선 사용하고 검증된 게시자만 신뢰하세요.

---

## 인프라 보안

### 방화벽
- 반드시 필요한 포트(예: 80, 443)를 제외한 모든 inbound port를 차단하세요.
- SSH 접근은 특정 IP 범위로 제한하거나 VPN/bastion host를 사용하세요.
- 세밀한 제어를 위해 security groups(AWS) 또는 NSGs(Azure)를 사용하세요.

### OS 하드닝
- `sudo apt upgrade`, `yum update` 등으로 보안 업데이트를 정기적으로 적용하세요.
- 불필요한 서비스와 기본 계정을 비활성화하세요.
- SSH에 대한 brute-force 시도를 막기 위해 fail2ban을 사용하세요.
- SSH 보안을 강화하세요: root login 비활성화, key-based auth 사용, 기본 포트 변경(선택 사항).

### 네트워크 분리
- database와 cache는 인터넷 접근이 없는 private subnet에 두세요.
- public-facing 서비스에는 DMZ를 사용하세요.
- 네트워크 접근에도 least privilege 원칙을 적용하세요.

### 인프라 내 비밀정보
- 암호화되지 않았다면 CI/CD environment variables에 secrets를 저장하지 마세요.
- 장기적으로 살아 있는 key 대신 클라우드 제공자의 IAM role을 EC2/VM instance에 부여하세요.

---

## 로깅과 모니터링

### 무엇을 기록할 것인가
- 인증 이벤트(success/failure)
- 접근 제어 결정(authorisation failure)
- 관리자 작업(사용자 생성, 삭제, 권한 변경)
- database schema 변경
- 시스템 오류와 exception
- API 요청과 응답(민감한 데이터는 마스킹)

### 무엇을 기록하지 말아야 하는가
- 비밀번호, secrets, tokens, PII(Personal Identifiable Information)는 해시 처리 또는 마스킹 없이 기록하지 마세요.
- 전체 신용카드 번호를 기록하지 마세요.

### 경보 설정
- 다음 상황에 대한 알림을 설정하세요.
  - 여러 차례의 로그인 실패(brute force 가능성)
  - 비정상적인 접근 패턴(예: 새로운 위치, 이상한 시간대)
  - 새로운 관리자 계정 생성
  - 높은 오류율 또는 지연 시간 급증
- 고급 상관 분석을 위해 SIEM(Security Information and Event Management)을 사용할 수 있습니다.

### 로그 보존
- 규제 요구 사항에 따라 최소 30–90일 동안 로그를 보관하세요.
- ELK Stack, Splunk, Datadog 같은 중앙 집중식 위변조 방지 시스템에 로그를 저장하세요.

---

## Secure Development Lifecycle (SDL)

1. **Training**: 개발자가 흔한 취약점을 이해하도록 교육하세요.
2. **Threat modelling**: 설계 초기 단계에서 잠재적 위협을 식별하세요.
3. **Secure coding standards**: linter와 code review checklist를 통해 강제하세요.
4. **SAST** (Static Application Security Testing): SonarQube, CodeQL 같은 도구로 source code의 취약점을 스캔하세요.
5. **DAST** (Dynamic Application Security Testing): OWASP ZAP, Burp Suite 같은 도구로 실행 중인 애플리케이션을 스캔하세요.
6. **SCA** (Software Composition Analysis): 의존성을 스캔하세요.
7. **Penetration testing**: 정기적인 윤리적 해킹 점검을 수행하세요.
8. **Bug bounty**: 외부 연구자들이 책임 있게 취약점을 찾도록 장려하세요.
9. **Incident response plan**: 침해가 탐지되었을 때를 위한 명확한 대응 계획을 마련하세요.

---

## Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — 당황하지 말되 빠르게 행동하세요.
2. **Isolate** 영향을 받은 시스템을 격리하세요(필요하다면 네트워크에서 분리).
3. **Preserve evidence**: 로그, 메모리 덤프, 디스크 이미지를 확보하세요.
4. **Identify** 범위를 파악하세요. 어떤 시스템과 어떤 데이터가 영향을 받았는지 확인하세요.
5. **Rotate** 유출된 모든 자격 증명과 secrets를 교체하세요.
6. **Patch** 취약점을 수정하세요.
7. **Notify** 필요한 경우 법적 기한 안에 영향받은 사용자와 규제 기관에 통지하세요.
