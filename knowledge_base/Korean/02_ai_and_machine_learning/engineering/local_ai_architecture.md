<!--
---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# 로컬 AI 아키텍처
하드웨어 고려 사항, 추론 엔진, 메모리 최적화, 엣지 배포를 위한 시스템 설계 등 대규모 언어 모델을 전체 기기에서 실행하기 위한 실용적인 가이드입니다.
---

## AI를 로컬에서 실행하는 이유는 무엇입니까?
- **개인정보 보호**: 데이터가 장치 외부로 유출되지 않습니다.
- **비용**: 토큰당 API 수수료가 없습니다.
- **지연 시간**: 예측 가능하고 네트워크가 필요 없는 추론입니다.
- **오프라인 가용성**: 인터넷 없이 작동합니다.
- **제어**: 모델 버전, 사용자 정의 및 미세 조정을 완벽하게 제어합니다.
---

## 하드웨어 요구 사항
### GPU 메모리(VRAM)
가장 중요한 리소스입니다. 메모리 내 모델 크기 ≒ **매개변수 × 매개변수당 바이트 수**.
| 정밀 | 매개변수당 바이트 | 3.8B 모델 | 7B 모델 | 13B 모델 | 70B 모델 |
|------------|---------|------------|----------|------------|------------|
| FP32 | 4 | ~15GB | ~28GB | ~52GB | ~280GB |
| FP16 | 2 | ~7.6GB | ~14GB | ~26GB | ~140GB |
| INT8(8비트) | 1 | ~3.8GB | ~7GB | ~13GB | ~70GB |
| INT4(4비트) | 0.5 | ~1.9GB | ~3.5GB | ~6.5GB | ~35GB |
**실용 지침:**
- 8GB VRAM → 4비트에서 최대 7B 모델.
- 12GB VRAM → 4비트에서 최대 13B 모델.
- 24GB VRAM → 4비트에서 최대 70B 모델(또는 8비트에서 13B).
- Apple Silicon(통합 메모리)은 64GB 이상의 시스템에서 70B 모델을 실행할 수 있습니다.
### RAM(시스템 메모리)
- CPU 추론을 위해서는 모델을 로드하기에 충분한 시스템 RAM이 필요합니다(VRAM 수치와 유사).
- GPU 추론의 경우 시스템 RAM은 VRAM으로 오프로드하기 전에 모델을 메모리에 로드하는 데 중요합니다.
### 스토리지
- 정량화된 모델 가중치는 몇 GB를 차지합니다(예: 디스크의 4비트 7B ≒ 4GB). 여러 모델에 대해 최소 20~50GB의 여유 공간을 확보하세요.
### CPU
- 신속한 처리(사전 채우기) 및 CPU 오프로딩을 위해 최신 멀티 코어 CPU가 도움이 됩니다.
- Apple M 시리즈 칩은 통합 메모리 및 Neural Engine으로 인해 LLM에 대한 성능이 뛰어납니다.
---

## 양자화
양자화는 가중치의 수치적 정밀도를 감소시키고, 메모리를 극적으로 줄이며, 작은 정확도 비용으로 속도를 높입니다.
### 인기 있는 형식
| 형식 | 비트 | 설명 | 일반적인 용도 |
|---------|------|-------------|-------------|
| **GGUF** | 4~8 | CPU/GPU 하이브리드에 최적화된 llama.cpp 형식 | 로컬 추론에 가장 적합 |
| **GPTQ** | 4~8 | GPU 전용, CUDA에서 효율적 | NVIDIA GPU에 가장 적합 |
| **AWQ** | 4 | 활성화 인식, GPU 전용 | GPU의 일괄 추론에 적합 |
| **ONNX** | 변수 | 표준화된 크로스 플랫폼 | 생산 서빙 |
### 양자화 레벨 선택
- **Q8_0** (8비트): 품질 손실이 최소화되고 크기가 가장 큽니다.
- **Q6_K**(6비트): 좋은 품질, 적절한 압축.
- **Q5_K_M**(5비트): 일반적인 최적 지점.
- **Q4_K_M**(4비트): 대부분의 작업에 허용되는 최소 품질입니다.
- **IQ4_XS** / **IQ3_XS**: 4/3 비트에서 더 나은 혼란으로 양자화가 향상되었습니다.
**경험 법칙:** 품질과 크기의 균형을 잘 맞추려면 Q4_K_M을 사용하세요. 추가 VRAM이 있는 경우 Q5 또는 Q6을 사용하십시오.
---

## 추론 엔진(로컬)
### 라마.cpp
- C++로 작성되었습니다.
- GGUF 형식을 지원합니다.
- CPU 및 GPU에 최적화되었습니다(CUDA, Metal, OpenCL을 통해).
- 특히 CPU에서 매우 빠릅니다.
- 명령줄, 서버 모드 및 Python 바인딩.
**예제 명령:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### 올라마
- 간단한 CLI 및 REST API로 llama.cpp를 래핑합니다.
- 모델을 자동으로 다운로드하고 관리합니다.
- 프로토타이핑 및 데스크톱 앱에 적합합니다.
- 시스템 프롬프트에 대한 사용자 정의 모델 파일을 지원합니다.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM 스튜디오
- Windows, macOS, Linux용 그래픽 데스크톱 앱.
- 원클릭 다운로드 및 채팅 인터페이스.
- OpenAI 호환 API가 내장된 로컬 서버.
- 기술적인 지식이 없는 사용자 및 빠른 테스트에 적합합니다.
### 허깅 페이스 트랜스포머 + 비트샌드바이트
- HF 모델용 표준 Python 라이브러리입니다.
- 4비트 양자화에는 `bitsandbytes`를 사용합니다(`load_in_4bit=True`).
- 미세 조정에는 더 유연하지만 추론에는 llama.cpp보다 느립니다.
### ExLlamaV2
- GPTQ 및 AWQ에 대한 매우 빠른 GPU 추론.
- NVIDIA GPU에서 최고의 성능을 발휘합니다.
- 일괄 생성을 지원합니다.
### mlx(애플)
- M 시리즈 칩을 위한 Apple의 프레임워크입니다.
- Apple Silicon에 최적화되어 있습니다.
- 파이썬 API.
---

## 메모리 관리
### 컨텍스트 창 및 KV 캐시
KV 캐시는 모든 레이어와 컨텍스트의 모든 토큰에 대한 키-값 쌍을 저장합니다. 컨텍스트 길이에 따라 선형적으로 증가합니다.
메모리 비용 ≒ 2 × 레이어 × (KV 헤드 × 헤드 딤) × 토큰 × 값당 바이트
8KV 헤드와 128헤드 딤이 있는 32레이어 모델의 경우 각 토큰의 비용은 ~32 × 8 × 128 × 2바이트 = 토큰당 65KB입니다. 128k 토큰의 경우 캐시에만 ~8GB가 소요됩니다.
### 오프로드 전략
- **레이어 오프로딩**: 일부 레이어는 GPU에 배치하고 다른 레이어는 CPU에 배치합니다. 순수 CPU보다 빠르며 VRAM 요구 사항이 낮습니다.
- **토큰 스트리밍**: 토큰을 한꺼번에 처리하지 않고 점진적으로 처리합니다.
### 프롬프트 캐싱
사전 채우기 단계를 다시 계산하지 않으려면 유사한 프롬프트에서 KV 캐시를 재사용하십시오. 일부 프레임워크에서는 이를 지원합니다(예: vLLM, `--prompt-cache`가 포함된 llama.cpp).
### 메모리 매핑된 파일
모델 가중치를 RAM에 완전히 로드하지 않고 디스크에서 직접 로드합니다(메모리가 제한된 시스템의 대규모 모델에 유용함). llama.cpp는 기본적으로 메모리 매핑을 사용합니다.
---

## 배포 아키텍처
### 단일 장치 모드
하나의 모델은 하나의 컴퓨터(노트북, 스마트폰, 엣지 장치)에서 실행됩니다. 개인 비서, 메모 작성 앱, 코드 완성에 사용됩니다.
### 하이브리드 엣지-클라우드
로컬 모델은 일반적인 쿼리를 처리합니다. 복잡한 질문에는 클라우드 모델로 대체합니다. 이는 대부분의 경우 속도/비공개, 극단적인 경우에 대한 기능이라는 두 가지 장점을 모두 제공합니다.
### 분산 추론(다중 GPU)
더 큰 모델의 경우 여러 GPU에 걸쳐 레이어를 분할하거나(텐서 병렬 처리) 여러 장치에 걸쳐 컨텍스트를 분할합니다(파이프라인 병렬 처리). `-ngl`와 함께 llama.cpp를 사용하거나 `--num-gpu-layers`와 함께 ExLlamaV2를 사용하세요.
### 모바일 배포
- **Android**: JNI 바인딩 또는 ML Kit를 통해 llama.cpp를 사용합니다.
- **iOS**: Swift 바인딩 또는 mlx를 통해 llama.cpp를 사용합니다.
- **웹**: WebLLM(ONNX 런타임을 통해 WebGPU에서 실행) 또는 Transformers.js를 사용합니다.
---

## 성능 최적화
### 플래시 주의
주의 계산 속도를 높이고 메모리 사용량을 줄입니다. llama.cpp, ExLlamaV2 및 최신 변환기 라이브러리에서 사용할 수 있습니다.
### 일괄 추론
단일 전달 단계에서 여러 프롬프트를 처리합니다. 처리량을 획기적으로 증가시킵니다.`llama-batch`또는 vLLM을 사용하세요.
### 조기 중단 / 토큰 예산 책정
무제한 생성을 방지하려면 최대 토큰 예산을 설정하세요.
### 추측적 디코딩
작고 빠른 모델(초안)을 사용하여 토큰을 예측한 다음 대규모 모델로 병렬로 검증합니다. 2~3배의 속도 향상을 얻을 수 있습니다.
---

## 실제 설정 가이드
### 1. 올라마 설치하기
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. 모델 가져오기
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. API로 실행
```bash
ollama serve
```

그런 다음`http://localhost:11434/api/generate`에 요청을 보냅니다.
### 4. 파이썬 통합
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (대체) llama.cpp를 직접 사용
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## 모니터링 및 관찰 가능성
- GPU 활용도를 추적합니다(Linux에서는 `nvidia-smi`, macOS에서는 Activity Monitor).
- 메모리 사용량(RAM 및 VRAM)을 추적합니다.
- 초당 토큰을 추적합니다(처리량).
- 첫 번째 토큰까지의 시간(대기 시간)을 추적합니다.
- llama.cpp 또는 Ollama의 내장 로깅을 사용하세요.
---

## 제한 사항 및 장단점
- **품질 격차**: 소규모 로컬 모델(3.8B~7B)은 일반적으로 복잡한 추론에서 대규모 클라우드 모델(GPT-4, Claude 3.5)보다 성능이 낮습니다.
- **지식 차단**: 모델 지식은 훈련 시간에 동결됩니다. RAG를 사용하여 현재 정보를 주입합니다.
- **다국어**: 소형 모델의 경우 다국어 기능이 떨어질 수 있습니다.
- **도구 사용**: 에이전트 워크플로(함수 호출)는 소규모 모델에서는 안정성이 떨어질 수 있습니다.
많은 일상 작업(요약, Q&A, 코드 완성, 분류)에서는 로컬 모델이 이미 충분하며 빠르게 개선되고 있습니다.