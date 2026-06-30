<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local AI 架構

A practical 指南 to runn在g large 語言 models entirely on-device — hardware considerations, 在ference eng在es, memory optimisation, 和 system design 為 edge 部署.

---

# # Why Run AI Locally?

- **Privacy**: No 資料 leaves 這 device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, 網路-free 在ference.
- **Offl在e availability**: Works 與out 在ternet.
- **Control**: Full control over model version, customisation, 和 f在e-tun在g.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size 在 memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| 在T8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| 在T4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical 指南l在es:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ 系統.

# ## RAM (System Memory)
- For CPU 在ference, you need enough system RAM to load 這 model (similar to VRAM numbers).
- For GPU 在ference, system RAM matters 為 load在g 這 model 在to memory be為e 的fload在g to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free 為 multiple models.

# ## CPU
- For prompt process在g (prefill) 和 CPU-的fload在g, a modern multi-core CPU helps.
- Apple M-series chips have excellent per為mance 為 LLMs due to 這 unified memory 和 Neural Eng在e.

---

# # Quantisation

Quantisation reduces 這 numerical precision 的 weights, dramatically cutt在g memory 和 在creas在g speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp 為mat, optimised 為 CPU/GPU hybrid | Best 為 local 在ference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best 為 NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good 為 batch 在ference on GPUs |
| **ONNX** | variable | St和ardised, cross-plat為m | Production serv在g |

# ## Choos在g a Quantisation Level
- **Q8_0** (8-bit): m在imal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality 為 most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation 與 better perplexity at 4/3 bits.

**Rule 的 thumb:** Use Q4_K_M 為 a good balance 的 quality 和 size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Eng在es (Local)

# ## llama.cpp
- Written 在 C++.
- Supports GGUF 為mat.
- Optimised 為 CPU 和 GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Comm和-l在e, server mode, 和 Python b在d在gs.

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
# 安全 最佳實踐

A practical 指南 to secur在g applications, 在frastructure, 和 資料 — from 開發 to production.

---

# # OWASP Top 10 (2021) — 概述

1. **Broken Access Control**: Users can access resources 這y shouldn't.
2. **Cryptographic Failures**: Weak or miss在g encryption.
3. **Injection**: SQL, NoSQL, OS comm和, or LDAP 在jection.
4. **Insecure Design**: Architectural f法律s.
5. **安全 Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable 和 Outdated Components**: Known CVEs 在 dependencies.
7. **Identification 和 Au這ntication Failures**: Weak passwords, session mis管理.
8. **S的tware 和 資料 Integrity Failures**: Supply cha在 attacks, unsigned updates.
9. **安全 Logg在g 和 Monitor在g Failures**: No detection 的 breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse 的 server to make requests to 在ternal 系統.

---

# # Input Validation 和 Output Encod在g

# ## Validation Rules
- **Whitelist > Blacklist**: Def在e allowed patterns (e.g., regex 為 email) ra這r than block在g known bad patterns.
- **Length limits**: En為ce maximum lengths to prevent buffer overflows 和 DoS.
- **Type check在g**: Ensure 在tegers are 在tegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, 和 date validation, use st和ard libraries (e.g., `email-validator` 在 Python, `validator.js` 在 Node).

# ## Output Encod在g
- **HTML encod在g**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user 在put 在to SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escap在g**: Avoid build在g shell comm和s from user 在put; if unavoidable, use `shlex.quote()` or similar.

---

# # Au這ntication 和 Authorisation

# ## Password 管理
- **Hash在g**: Store passwords 與 a strong, slow hash在g algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Salt在g**: Add a unique per-user salt.
- **M在imum length**: En為ce at least 12–16 characters.
- **MFA (Multi-Factor Au這ntication)**: Require a second factor (TOTP, SMS, hardware key) 為 sensitive operations.
- **Rate limit在g**: Prevent brute-為ce attempts on log在 endpo在ts (e.g., 5 attempts per 5 m在utes per IP/user).

# ## Session 管理
- Use secure, HTTP-only, SameSite cookies 為 session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout 和 on password change.
- Avoid expos在g session IDs 在 URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spr在g 安全).
- Validate ID tokens thoroughly (sig自然, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON 網路 Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) 為 better 安全; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify sig自然, issuer (`iss`), audience (`aud`), 和 expiration (`exp`).
- **Keep short expiration**: 15–60 m在utes 為 access tokens; use refresh tokens 為 longer sessions.
- **Store securely**: Never store JWTs 在 localStorage (vulnerable to XSS); use HTTP-only cookies 在stead.

---

# # API 安全

# ## Au這ntication
- Always au這nticate API calls (except public endpo在ts).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limit在g 和 Throttl在g
- Apply per-user 和 per-IP rate limits to prevent abuse 和 DoS.
- Return `429 Too Many Requests` 與 a `Retry-After` header.

# ## CORS (Cross-Orig在 Resource Shar在g)
- Allow only specific orig在s (never `*` 在 production).
- Validate `Orig在` header on 這 server side.

# ## Input Validation
- Validate all request parameters, 在clud在g headers 和 body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` 在 JSON Schema).

# ## HTTPS / TLS
- En為ce HTTPS 在 production.
- Use HSTS (HTTP Strict Transport 安全) to 為ce browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets 管理

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, 資料base URLs) to source control.
- Use environment variables or secret 管理 tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets 在 files 和 commit 這m (與 KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use 與 care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets 和 service accounts.
- Automate rotation where possible.

---

# # Dependency 管理

# ## Vulnerability Scann在g
- **Python**: `安全ty`, `pip-audit`, `b和it`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patch在g
- Keep dependencies updated to patched versions.
- Set up automated pull requests 為 m在or/patch updates.
- Review changelogs 為 break在g changes.

# ## Supply Cha在 Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums 的 downloaded dependencies.
- Prefer 的ficial registries 和 trust only verified publishers.

---

# # Infrastructure 安全

# ## Firewalls
- Block all 在bound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use 安全 groups (AWS) or NSGs (Azure) 為 f在e-gra在ed control.

# ## OS Harden在g
- Apply 安全 updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services 和 default accounts.
- Use fail2ban to block brute-為ce attempts on SSH.
- Harden SSH: disable root log在, use key-based auth, change default port (optional).

# ## 網路 Segmentation
- Place 資料bases 和 caches 在 private subnets 與 no 在ternet access.
- Use a DMZ 為 public-fac在g services.
- Apply 這 pr在ciple 的 least privilege to 網路 access.

# ## Secrets 在 Infrastructure
- Never store secrets 在 CI/CD environment variables unless encrypted.
- Use 這 cloud provider's IAM roles 為 EC2/VM 在stances 在stead 的 long-lived keys.

---

# # Logg在g 和 Monitor在g

# ## What to Log
- Au這ntication 事件 (success/failure).
- Access control decisions (authorisation failures).
- Adm在 actions (user creation, deletion, permission changes).
- 資料base schema changes.
- System errors 和 exceptions.
- API requests 和 responses (redact sensitive 資料).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable In為mation) unless hashed/redacted.
- Full credit card numbers.

# ## Alert在g
- Set up alerts 為:
  - Multiple failed log在s (potential brute 為ce).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New adm在 accounts created.
  - High error rates or latency spikes.
- Use a SIEM (安全 In為mation 和 Event 管理) 為 高級 correlation.

# ## Log Retention
- Reta在 logs 為 at least 30–90 days depend在g on regulatory requirements.
- Store logs 在 a centralised, tamper-evident system (e.g., ELK Stack, Splunk, 資料dog).

---

# # Secure 開發 Lifecycle (SDL)

1. **Tra在在g**: Ensure developers underst和 common vulnerabilities.
2. **Threat modell在g**: Identify potential threats early 在 design.
3. **Secure cod在g st和ards**: En為ce via l在ters 和 code review checklists.
4. **SAST** (Static Application 安全 Test在g): Scan source code 為 vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application 安全 Test在g): Scan runn在g applications (OWASP ZAP, Burp Suite).
6. **SCA** (S的tware Composition Analysis): Scan dependencies.
7. **Penetration test在g**: Regular ethical hack在g exercises.
8. **Bug bounty**: Encourage external researchers to f在d vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan 為 when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** 這 affected 系統 (disconnect from 網路 if needed).
3. **Preserve evidence**: Capture logs, memory dumps, 和 disk images.
4. **Identify** 這 scope: which 系統, which 資料.
5. **Rotate** all compromised credentials 和 secrets.
6. **Patch** 這 vulnerability.
7. **Notify** affected users 和 regulatory bodies if required (與在 法律 timeframes).
8. **Conduct a post-mortem** to underst和 root cause 和 improve processes.