<!-- 
This file was automatically translated from English to Korean.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local AI 아키텍처

A practical 가이드 to runn에서g large 언어 models entirely on-device — hardware considerations, 에서ference eng에서es, memory optimisation, 와 system design 위한 edge 배포.

---

# # Why Run AI Locally?

- **Privacy**: No 데이터 leaves 그 device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, 네트워크-free 에서ference.
- **Offl에서e availability**: Works 와 함께out 에서ternet.
- **Control**: Full control over model version, customisation, 와 f에서e-tun에서g.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size 에서 memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| 에서T8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| 에서T4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical 가이드l에서es:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ 시스템.

# ## RAM (System Memory)
- For CPU 에서ference, you need enough system RAM to load 그 model (similar to VRAM numbers).
- For GPU 에서ference, system RAM matters 위한 load에서g 그 model 에서to memory be위한e 의fload에서g to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free 위한 multiple models.

# ## CPU
- For prompt process에서g (prefill) 와 CPU-의fload에서g, a modern multi-core CPU helps.
- Apple M-series chips have excellent per위한mance 위한 LLMs due to 그 unified memory 와 Neural Eng에서e.

---

# # Quantisation

Quantisation reduces 그 numerical precision 의 weights, dramatically cutt에서g memory 와 에서creas에서g speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp 위한mat, optimised 위한 CPU/GPU hybrid | Best 위한 local 에서ference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best 위한 NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good 위한 batch 에서ference on GPUs |
| **ONNX** | variable | St와ardised, cross-plat위한m | Production serv에서g |

# ## Choos에서g a Quantisation Level
- **Q8_0** (8-bit): m에서imal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality 위한 most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation 와 함께 better perplexity at 4/3 bits.

**Rule 의 thumb:** Use Q4_K_M 위한 a good balance 의 quality 와 size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Eng에서es (Local)

# ## llama.cpp
- Written 에서 C++.
- Supports GGUF 위한mat.
- Optimised 위한 CPU 와 GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Comm와-l에서e, server mode, 와 Python b에서d에서gs.

**Example comm와:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)

Ollama
Wraps llama.cpp with a simple CLI and REST API.

Auto-downloads models, manages them.

Great for prototyping and desktop apps.

Supports custom Modelfiles for system prompts.

Usage:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Graphical desktop app for Windows, macOS, Linux.

One-click download and chat interface.

Built-in local server with OpenAI-compatible API.

Good for non-technical users and quick testing.

Hugging Face Transformers + bitsandbytes
The standard Python library for HF models.

Use bitsandbytes for 4-bit quantisation (load_in_4bit=True).

More flexible for fine-tuning but slower than llama.cpp for inference.

ExLlamaV2
Very fast GPU inference for GPTQ and AWQ.

Best performance on NVIDIA GPUs.

Supports batched generation.

mlx (Apple)
Apple's framework for M-series chips.

Highly optimised for Apple Silicon.

Python API.

Memory Management
Context Window and KV Cache
The KV cache stores key-value pairs for every layer and every token in the context. It grows linearly with context length.

Memory cost ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

For a 32-layer model with 8 KV heads and 128 head dim, each token costs ~32 × 8 × 128 × 2 bytes = 65 KB per token. For 128k tokens, that's ~8 GB just for the cache.

Offloading Strategies
Layer offloading: Put some layers on GPU, others on CPU. Faster than pure CPU, lower VRAM requirement.

Token streaming: Process tokens incrementally rather than all at once.

Prompt Caching
Reuse KV caches across similar prompts to avoid recomputing the prefill phase. Some frameworks support this (e.g., vLLM, llama.cpp with --prompt-cache).

Memory-Mapped Files
Load model weights directly from disk without loading them entirely into RAM (useful for huge models on memory-limited systems). llama.cpp uses memory-mapping by default.

Deployment Architectures
Single-Device Mode
One model runs on one machine (laptop, smartphone, edge device). Used for personal assistants, note-taking apps, code completion.

Hybrid Edge-Cloud
Local model handles common queries; fallback to a cloud model for complex questions. This gives the best of both worlds — speed/private for most, capability for edge cases.

Distributed Inference (Multi-GPU)
For larger models, split layers across multiple GPUs (tensor parallelism) or split context across devices (pipeline parallelism). Use llama.cpp with -ngl or ExLlamaV2 with --num-gpu-layers.

Mobile Deployment
Android: Use llama.cpp via JNI bindings or ML Kit.

iOS: Use llama.cpp via Swift bindings or mlx.

Web: Use WebLLM (runs on WebGPU via ONNX runtime) or transformers.js.

Performance Optimisation
Flash Attention
Speeds up attention computation and reduces memory usage. Available in llama.cpp, ExLlamaV2, and modern transformers libraries.

Batch Inference
Process multiple prompts in a single forward pass. Increases throughput dramatically. Use llama-batch or vLLM.

Early Stopping / Token Budgeting
Set a maximum token budget to prevent unbounded generation.

Speculative Decoding
Use a small fast model (draft) to predict tokens, then verify with the large model in parallel. Can yield 2–3× speedup.

Practical Setup Guide
1. Install Ollama
bash
curl -fsSL https://ollama.com/install.sh | sh
2. Pull a Model
bash
ollama pull phi3:3.8b-q4_K_M
3. Run with API
bash
ollama serve
Then send requests to http://localhost:11434/api/generate.

4. Python Integration
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Alternative) Use llama.cpp directly
bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
Monitoring and Observability
Track GPU utilisation (nvidia-smi on Linux, Activity Monitor on macOS).

Track memory usage (RAM and VRAM).

Track tokens per second (throughput).

Track time to first token (latency).

Use built-in logging from llama.cpp or Ollama.

Limitations and Tradeoffs
Quality gap: Small local models (3.8B–7B) generally underperform large cloud models (GPT-4, Claude 3.5) on complex reasoning.

Knowledge cutoff: Model knowledge is frozen at training time; use RAG to inject current information.

Multilingual: Smaller models may have less multilingual capability.

Tool use: Agentic workflows (function calling) may be less reliable on small models.

For many everyday tasks (summarisation, Q&A, code completion, classification), local models are already sufficient and improving rapidly.

text

---

## File 4: `security_best_practices.md`

```markdown
# 보안 모범 사례

A practical 가이드 to secur에서g applications, 에서frastructure, 와 데이터 — from 개발 to production.

---

# # OWASP Top 10 (2021) — 개요

1. **Broken Access Control**: Users can access resources 그y shouldn't.
2. **Cryptographic Failures**: Weak or miss에서g encryption.
3. **Injection**: SQL, NoSQL, OS comm와, or LDAP 에서jection.
4. **Insecure Design**: Architectural f법률s.
5. **보안 Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable 와 Outdated Components**: Known CVEs 에서 dependencies.
7. **Identification 와 Au그ntication Failures**: Weak passwords, session mis관리.
8. **S의tware 와 데이터 Integrity Failures**: Supply cha에서 attacks, unsigned updates.
9. **보안 Logg에서g 와 Monitor에서g Failures**: No detection 의 breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse 의 server to make requests to 에서ternal 시스템.

---

# # Input Validation 와 Output Encod에서g

# ## Validation Rules
- **Whitelist > Blacklist**: Def에서e allowed patterns (e.g., regex 위한 email) ra그r than block에서g known bad patterns.
- **Length limits**: En위한ce maximum lengths to prevent buffer overflows 와 DoS.
- **Type check에서g**: Ensure 에서tegers are 에서tegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, 와 date validation, use st와ard libraries (e.g., `email-validator` 에서 Python, `validator.js` 에서 Node).

# ## Output Encod에서g
- **HTML encod에서g**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user 에서put 에서to SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escap에서g**: Avoid build에서g shell comm와s from user 에서put; if unavoidable, use `shlex.quote()` or similar.

---

# # Au그ntication 와 Authorisation

# ## Password 관리
- **Hash에서g**: Store passwords 와 함께 a strong, slow hash에서g algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Salt에서g**: Add a unique per-user salt.
- **M에서imum length**: En위한ce at least 12–16 characters.
- **MFA (Multi-Factor Au그ntication)**: Require a second factor (TOTP, SMS, hardware key) 위한 sensitive operations.
- **Rate limit에서g**: Prevent brute-위한ce attempts on log에서 endpo에서ts (e.g., 5 attempts per 5 m에서utes per IP/user).

# ## Session 관리
- Use secure, HTTP-only, SameSite cookies 위한 session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout 와 on password change.
- Avoid expos에서g session IDs 에서 URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spr에서g 보안).
- Validate ID tokens thoroughly (sig자연, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON 웹 Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) 위한 better 보안; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify sig자연, issuer (`iss`), audience (`aud`), 와 expiration (`exp`).
- **Keep short expiration**: 15–60 m에서utes 위한 access tokens; use refresh tokens 위한 longer sessions.
- **Store securely**: Never store JWTs 에서 localStorage (vulnerable to XSS); use HTTP-only cookies 에서stead.

---

# # API 보안

# ## Au그ntication
- Always au그nticate API calls (except public endpo에서ts).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limit에서g 와 Throttl에서g
- Apply per-user 와 per-IP rate limits to prevent abuse 와 DoS.
- Return `429 Too Many Requests` 와 함께 a `Retry-After` header.

# ## CORS (Cross-Orig에서 Resource Shar에서g)
- Allow only specific orig에서s (never `*` 에서 production).
- Validate `Orig에서` header on 그 server side.

# ## Input Validation
- Validate all request parameters, 에서clud에서g headers 와 body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` 에서 JSON Schema).

# ## HTTPS / TLS
- En위한ce HTTPS 에서 production.
- Use HSTS (HTTP Strict Transport 보안) to 위한ce browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets 관리

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, 데이터base URLs) to source control.
- Use environment variables or secret 관리 tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets 에서 files 와 commit 그m (와 함께 KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use 와 함께 care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets 와 service accounts.
- Automate rotation where possible.

---

# # Dependency 관리

# ## Vulnerability Scann에서g
- **Python**: `안전한ty`, `pip-audit`, `b와it`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patch에서g
- Keep dependencies updated to patched versions.
- Set up automated pull requests 위한 m에서or/patch updates.
- Review changelogs 위한 break에서g changes.

# ## Supply Cha에서 Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums 의 downloaded dependencies.
- Prefer 의ficial registries 와 trust only verified publishers.

---

# # Infrastructure 보안

# ## Firewalls
- Block all 에서bound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use 보안 groups (AWS) or NSGs (Azure) 위한 f에서e-gra에서ed control.

# ## OS Harden에서g
- Apply 보안 updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services 와 default accounts.
- Use fail2ban to block brute-위한ce attempts on SSH.
- Harden SSH: disable root log에서, use key-based auth, change default port (optional).

# ## 네트워크 Segmentation
- Place 데이터bases 와 caches 에서 private subnets 와 함께 no 에서ternet access.
- Use a DMZ 위한 public-fac에서g services.
- Apply 그 pr에서ciple 의 least privilege to 네트워크 access.

# ## Secrets 에서 Infrastructure
- Never store secrets 에서 CI/CD environment variables unless encrypted.
- Use 그 cloud provider's IAM roles 위한 EC2/VM 에서stances 에서stead 의 long-lived keys.

---

# # Logg에서g 와 Monitor에서g

# ## What to Log
- Au그ntication 이벤트 (success/failure).
- Access control decisions (authorisation failures).
- Adm에서 actions (user creation, deletion, permission changes).
- 데이터base schema changes.
- System errors 와 exceptions.
- API requests 와 responses (redact sensitive 데이터).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable In위한mation) unless hashed/redacted.
- Full credit card numbers.

# ## Alert에서g
- Set up alerts 위한:
  - Multiple failed log에서s (potential brute 위한ce).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New adm에서 accounts created.
  - High error rates or latency spikes.
- Use a SIEM (보안 In위한mation 와 Event 관리) 위한 고급 correlation.

# ## Log Retention
- Reta에서 logs 위한 at least 30–90 days depend에서g on regulatory requirements.
- Store logs 에서 a centralised, tamper-evident system (e.g., ELK Stack, Splunk, 데이터dog).

---

# # Secure 개발 Lifecycle (SDL)

1. **Tra에서에서g**: Ensure developers underst와 common vulnerabilities.
2. **Threat modell에서g**: Identify potential threats early 에서 design.
3. **Secure cod에서g st와ards**: En위한ce via l에서ters 와 code review checklists.
4. **SAST** (Static Application 보안 Test에서g): Scan source code 위한 vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application 보안 Test에서g): Scan runn에서g applications (OWASP ZAP, Burp Suite).
6. **SCA** (S의tware Composition Analysis): Scan dependencies.
7. **Penetration test에서g**: Regular ethical hack에서g exercises.
8. **Bug bounty**: Encourage external researchers to f에서d vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan 위한 when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** 그 affected 시스템 (disconnect from 네트워크 if needed).
3. **Preserve evidence**: Capture logs, memory dumps, 와 disk images.
4. **Identify** 그 scope: which 시스템, which 데이터.
5. **Rotate** all compromised credentials 와 secrets.
6. **Patch** 그 vulnerability.
7. **Notify** affected users 와 regulatory bodies if required (와 함께에서 법적 timeframes).
8. **Conduct a post-mortem** to underst와 root cause 와 improve processes.