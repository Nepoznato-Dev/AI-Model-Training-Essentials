<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local 人工智能 架构

A practical 指南 to runn large 语言 models entirely on-device — hardware considerations, ference eng, memory optimisation, 和 system design edge 部署.

---

# # Why Run 人工智能 Locally?

- **Privacy**: No 数据 leaves device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, 网络-free ference.
- **Offle availability**: Works 与out ternet.
- **Control**: Full control over model version, customisation, 和 fe-tun.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32 | 4 | ~15 GB | ~28 GB | ~52 GB | ~280 GB |
| FP16 | 2 | ~7.6 GB | ~14 GB | ~26 GB | ~140 GB |
| T8 (8-bit) | 1 | ~3.8 GB | ~7 GB | ~13 GB | ~70 GB |
| T4 (4-bit) | 0.5 | ~1.9 GB | ~3.5 GB | ~6.5 GB | ~35 GB |

**Practical 指南l:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ 系统.

# ## RAM (System Memory)
- For CPU ference, you need enough system RAM to load model (similar to VRAM numbers).
- For GPU ference, system RAM matters load model 到 memory ...之前 的fload to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free multiple models.

# ## CPU
- For prompt process (prefill) 和 CPU-的fload, a modern multi-core CPU helps.
- Apple M-series chips have excellent permance 大型语言模型 due to unified memory 和 Neural Enge.

---

# # Quantisation

Quantisation reduces numerical precision 的 weights, dramatically cutt memory 和 creas speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | 描述 | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp mat, optimised CPU/GPU hybrid | Best local ference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good batch ference on GPUs |
| **ONNX** | variable | St和ardised, cross-platm | Production serv |

# ## Choos a Quantisation Level
- **Q8_0** (8-bit): mimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation 与 better perplexity at 4/3 bits.

**Rule 的 thumb:** Use Q4_K_M a good balance 的 quality 和 size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Eng (Local)

# ## llama.cpp
- Written C++.
- Supports GGUF mat.
- Optimised CPU 和 GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Comm和-le, server mode, 和 Python bds.

**Example comm和:**
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

Built-in local server with Open人工智能-compatible API.

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

Memory-Mapped 文件
Load model weights directly from disk without loading them entirely into RAM (useful for huge models on memory-limited systems). llama.cpp uses memory-mapping by default.

Deployment Architectures
Single-Device Mode
One model runs on one machine (laptop, smartphone, edge device). Used for personal assistants, note-taking apps, code completion.

Hybrid Edge-Cloud
Local model handles common queries; fallback to a 云 model for complex questions. This gives the best of both worlds — speed/private for most, capability for edge cases.

Distributed Inference (Multi-GPU)
For larger models, split layers across multiple GPUs (tensor parallelism) or split context across devices (pipeline parallelism). Use llama.cpp with -ngl or ExLlamaV2 with --num-gpu-layers.

Mobile Deployment
Android: Use llama.cpp via JNI bindings or 机器学习 Kit.

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
Quality gap: Small local models (3.8B–7B) generally underperform large 云 models (GPT-4, Claude 3.5) on complex reasoning.

Knowledge cutoff: Model knowledge is frozen at training time; use RAG to inject current information.

Multilingual: Smaller models may have less multilingual capability.

Tool use: Agentic workflows (function calling) may be less reliable on small models.

For many everyday tasks (summarisation, Q&A, code completion, classification), local models are already sufficient and improving rapidly.

text

---

## File 4: `security_best_practices.md`

```markdown
# 安全 最佳实践

A practical 指南 to secur applications, frastructure, 和 数据 — from 开发 to production.

---

# # OWASP Top 10 (2021) — 概述

1. **Broken Access Control**: Users can access resources y shouldn't.
2. **Cryptographic Failures**: Weak or miss encryption.
3. **Injection**: SQL, NoSQL, OS comm和, or LDAP jection.
4. **Insecure Design**: Architectural f法律s.
5. **安全 Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable 和 Outdated Components**: Known CVEs dependencies.
7. **Identification 和 Auntication Failures**: Weak passwords, session mis管理.
8. **S的tware 和 数据 Integrity Failures**: Supply cha attacks, unsigned updates.
9. **安全 Logg 和 Monitor Failures**: No detection 的 breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse 的 server to make requests to ternal 系统.

---

# # Input Validation 和 Output Encod

# ## Validation Rules
- **Whitelist > Blacklist**: Defe allowed patterns (e.g., regex email) rar than block known bad patterns.
- **Length limits**: Ence maximum lengths to prevent buffer overflows 和 DoS.
- **Type check**: Ensure tegers are tegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, 和 date validation, use st和ard libraries (e.g., `email-validator` Python, `validator.js` Node).

# ## Output Encod
- **HT机器学习 encod**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user put 到 SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escap**: Avoid build shell comm和s from user put; if unavoidable, use `shlex.quote()` or similar.

---

# # Auntication 和 Authorisation

# ## Password 管理
- **Hash**: Store passwords 与 a strong, slow hash algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Salt**: Add a unique per-user salt.
- **Mimum length**: Ence at least 12–16 characters.
- **MFA (Multi-Factor Auntication)**: Require a second factor (TOTP, SMS, hardware key) sensitive operations.
- **Rate limit**: Prevent brute-ce attempts on log endpots (e.g., 5 attempts per 5 mutes per IP/user).

# ## Session 管理
- Use secure, HTTP-only, SameSite cookies session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout 和 on password change.
- Avoid expos session IDs URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spr 安全).
- Validate ID tokens thoroughly (sig自然, issuer, 受众, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON 网络 Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) better 安全; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify sig自然, issuer (`iss`), 受众 (`aud`), 和 expiration (`exp`).
- **Keep short expiration**: 15–60 mutes access tokens; use refresh tokens longer sessions.
- **Store securely**: Never store JWTs localStorage (vulnerable to XSS); use HTTP-only cookies stead.

---

# # API 安全

# ## Auntication
- Always aunticate API calls (except public endpots).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limit 和 Throttl
- Apply per-user 和 per-IP rate limits to prevent abuse 和 DoS.
- Return `429 Too Many Requests` 与 a `Retry-After` header.

# ## CORS (Cross-Orig Resource Shar)
- Allow only specific origs (never `*` production).
- Validate `Orig` header on server side.

# ## Input Validation
- Validate all request parameters, clud headers 和 body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` JSON Schema).

# ## HTTPS / TLS
- Ence HTTPS production.
- Use HSTS (HTTP Strict Transport 安全) to ce browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets 管理

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, 数据base URLs) to source control.
- Use 环境 variables or secret 管理 tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets files 和 commit m (与 KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use 与 care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets 和 service accounts.
- Automate rotation where possible.

---

# # Dependency 管理

# ## Vulnerability Scann
- **Python**: `安全ty`, `pip-audit`, `b和it`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patch
- Keep dependencies updated to patched versions.
- Set up automated pull requests mor/patch updates.
- Review changelogs break changes.

# ## Supply Cha Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums 的 downloaded dependencies.
- Prefer 的ficial registries 和 trust only 已验证 publishers.

---

# # Infrastructure 安全

# ## Firewalls
- Block all bound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use 安全 groups (AWS) or NSGs (Azure) fe-graed control.

# ## OS Harden
- Apply 安全 updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services 和 default accounts.
- Use fail2ban to block brute-ce attempts on SSH.
- Harden SSH: disable root log, use key-based auth, change default port (optional).

# ## 网络 Segmentation
- Place 数据bases 和 caches private subnets 与 no ternet access.
- Use a DMZ public-fac services.
- Apply prciple 的 least privilege to 网络 access.

# ## Secrets Infrastructure
- Never store secrets CI/CD 环境 variables unless encrypted.
- Use 云 provider's IAM roles EC2/VM stances stead 的 long-lived keys.

---

# # Logg 和 Monitor

# ## What to Log
- Auntication 事件 (success/failure).
- Access control decisions (authorisation failures).
- Adm actions (user creation, deletion, permission changes).
- 数据base schema changes.
- System errors 和 exceptions.
- API requests 和 responses (redact sensitive 数据).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable 信息) unless hashed/redacted.
- Full credit card numbers.

# ## Alert
- Set up alerts :
 - Multiple failed logs (potential brute ce).
 - Unusual access patterns (e.g., from new locations, at odd hours).
 - New adm accounts created.
 - High error rates or latency spikes.
- Use a SIEM (安全 信息 和 Event 管理) 高级 correlation.

# ## Log Retention
- Reta logs at least 30–90 days depend on regulatory requirements.
- Store logs a centralised, tamper-evident system (e.g., ELK Stack, Splunk, 数据dog).

---

# # Secure 开发 Lifecycle (SDL)

1. **Tra**: Ensure developers underst和 common vulnerabilities.
2. **Threat modell**: Identify potential threats early design.
3. **Secure cod st和ards**: Ence via lters 和 code review checklists.
4. **SAST** (Static Application 安全 Test): Scan source code vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application 安全 Test): Scan runn applications (OWASP ZAP, Burp Suite).
6. **SCA** (S的tware Composition Analysis): Scan dependencies.
7. **Penetration test**: Regular ethical hack exercises.
8. **Bug bounty**: Encourage external researchers to fd vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** affected 系统 (disconnect from 网络 if needed).
3. **Preserve evidence**: Capture logs, memory dumps, 和 disk images.
4. **Identify** scope: which 系统, which 数据.
5. **Rotate** all compromised credentials 和 secrets.
6. **Patch** vulnerability.
7. **Notify** affected users 和 regulatory bodies if required (与 法律 timeframes).
8. **Conduct a post-mortem** to underst和 root cause 和 improve processes.