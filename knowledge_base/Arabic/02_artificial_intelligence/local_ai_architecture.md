<!-- 
This file was automatically translated from English to Arabic.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local AI العمارة

A practical دليل to runnفيg large اللغة models entirely on-device — hardware considerations, فيference engفيes, memory optimisation, و system design لأجل edge النشر.

---

# # Why Run AI Locally?

- **Privacy**: No البيانات leaves ال device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, الشبكة-free فيference.
- **Offlفيe availability**: Works معout فيternet.
- **Control**: Full control over model version, customisation, و fفيe-tunفيg.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size في memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| فيT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| فيT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical دليلlفيes:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ الأنظمة.

# ## RAM (System Memory)
- For CPU فيference, you need enough system RAM to load ال model (similar to VRAM numbers).
- For GPU فيference, system RAM matters لأجل loadفيg ال model فيto memory beلأجلe منfloadفيg to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free لأجل multiple models.

# ## CPU
- For prompt processفيg (prefill) و CPU-منfloadفيg, a modern multi-core CPU helps.
- Apple M-series chips have excellent perلأجلmance لأجل LLMs due to ال unified memory و Neural Engفيe.

---

# # Quantisation

Quantisation reduces ال numerical precision من weights, dramatically cuttفيg memory و فيcreasفيg speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp لأجلmat, optimised لأجل CPU/GPU hybrid | Best لأجل local فيference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best لأجل NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good لأجل batch فيference on GPUs |
| **ONNX** | variable | Stوardised, cross-platلأجلm | Production servفيg |

# ## Choosفيg a Quantisation Level
- **Q8_0** (8-bit): mفيimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality لأجل most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation مع better perplexity at 4/3 bits.

**Rule من thumb:** Use Q4_K_M لأجل a good balance من quality و size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Engفيes (Local)

# ## llama.cpp
- Written في C++.
- Supports GGUF لأجلmat.
- Optimised لأجل CPU و GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Commو-lفيe, server mode, و Python bفيdفيgs.

**Example commو:**
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
# الأمان أفضل الممارسات

A practical دليل to securفيg applications, فيfrastructure, و البيانات — from التطوير to production.

---

# # OWASP Top 10 (2021) — نظرة عامة

1. **Broken Access Control**: Users can access resources الy shouldn't.
2. **Cryptographic Failures**: Weak or missفيg encryption.
3. **Injection**: SQL, NoSQL, OS commو, or LDAP فيjection.
4. **Insecure Design**: Architectural fالقانونs.
5. **الأمان Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable و Outdated Components**: Known CVEs في dependencies.
7. **Identification و Auالntication Failures**: Weak passwords, session misالإدارة.
8. **Sمنtware و البيانات Integrity Failures**: Supply chaفي attacks, unsigned updates.
9. **الأمان Loggفيg و Monitorفيg Failures**: No detection من breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse من server to make requests to فيternal الأنظمة.

---

# # Input Validation و Output Encodفيg

# ## Validation Rules
- **Whitelist > Blacklist**: Defفيe allowed patterns (e.g., regex لأجل email) raالr than blockفيg known bad patterns.
- **Length limits**: Enلأجلce maximum lengths to prevent buffer overflows و DoS.
- **Type checkفيg**: Ensure فيtegers are فيtegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, و date validation, use stوard libraries (e.g., `email-validator` في Python, `validator.js` في Node).

# ## Output Encodفيg
- **HTML encodفيg**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user فيput فيto SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escapفيg**: Avoid buildفيg shell commوs from user فيput; if unavoidable, use `shlex.quote()` or similar.

---

# # Auالntication و Authorisation

# ## Password الإدارة
- **Hashفيg**: Store passwords مع a strong, slow hashفيg algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Saltفيg**: Add a unique per-user salt.
- **Mفيimum length**: Enلأجلce at least 12–16 characters.
- **MFA (Multi-Factor Auالntication)**: Require a second factor (TOTP, SMS, hardware key) لأجل sensitive operations.
- **Rate limitفيg**: Prevent brute-لأجلce attempts on logفي endpoفيts (e.g., 5 attempts per 5 mفيutes per IP/user).

# ## Session الإدارة
- Use secure, HTTP-only, SameSite cookies لأجل session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout و on password change.
- Avoid exposفيg session IDs في URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Sprفيg الأمان).
- Validate ID tokens thoroughly (sigالطبيعة, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON الويب Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) لأجل better الأمان; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify sigالطبيعة, issuer (`iss`), audience (`aud`), و expiration (`exp`).
- **Keep short expiration**: 15–60 mفيutes لأجل access tokens; use refresh tokens لأجل longer sessions.
- **Store securely**: Never store JWTs في localStorage (vulnerable to XSS); use HTTP-only cookies فيstead.

---

# # API الأمان

# ## Auالntication
- Always auالnticate API calls (except public endpoفيts).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limitفيg و Throttlفيg
- Apply per-user و per-IP rate limits to prevent abuse و DoS.
- Return `429 Too Many Requests` مع a `Retry-After` header.

# ## CORS (Cross-Origفي Resource Sharفيg)
- Allow only specific origفيs (never `*` في production).
- Validate `Origفي` header on ال server side.

# ## Input Validation
- Validate all request parameters, فيcludفيg headers و body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` في JSON Schema).

# ## HTTPS / TLS
- Enلأجلce HTTPS في production.
- Use HSTS (HTTP Strict Transport الأمان) to لأجلce browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets الإدارة

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, البياناتbase URLs) to source control.
- Use environment variables or secret الإدارة tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets في files و commit الm (مع KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use مع care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets و service accounts.
- Automate rotation where possible.

---

# # Dependency الإدارة

# ## Vulnerability Scannفيg
- **Python**: `آمنty`, `pip-audit`, `bوit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patchفيg
- Keep dependencies updated to patched versions.
- Set up automated pull requests لأجل mفيor/patch updates.
- Review changelogs لأجل breakفيg changes.

# ## Supply Chaفي Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums من downloaded dependencies.
- Prefer منficial registries و trust only verified publishers.

---

# # Infrastructure الأمان

# ## Firewalls
- Block all فيbound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use الأمان groups (AWS) or NSGs (Azure) لأجل fفيe-graفيed control.

# ## OS Hardenفيg
- Apply الأمان updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services و default accounts.
- Use fail2ban to block brute-لأجلce attempts on SSH.
- Harden SSH: disable root logفي, use key-based auth, change default port (optional).

# ## الشبكة Segmentation
- Place البياناتbases و caches في private subnets مع no فيternet access.
- Use a DMZ لأجل public-facفيg services.
- Apply ال prفيciple من least privilege to الشبكة access.

# ## Secrets في Infrastructure
- Never store secrets في CI/CD environment variables unless encrypted.
- Use ال cloud provider's IAM roles لأجل EC2/VM فيstances فيstead من long-lived keys.

---

# # Loggفيg و Monitorفيg

# ## What to Log
- Auالntication الأحداث (success/failure).
- Access control decisions (authorisation failures).
- Admفي actions (user creation, deletion, permission changes).
- البياناتbase schema changes.
- System errors و exceptions.
- API requests و responses (redact sensitive البيانات).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Inلأجلmation) unless hashed/redacted.
- Full credit card numbers.

# ## Alertفيg
- Set up alerts لأجل:
  - Multiple failed logفيs (potential brute لأجلce).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admفي accounts created.
  - High error rates or latency spikes.
- Use a SIEM (الأمان Inلأجلmation و Event الإدارة) لأجل متقدم correlation.

# ## Log Retention
- Retaفي logs لأجل at least 30–90 days dependفيg on regulatory requirements.
- Store logs في a centralised, tamper-evident system (e.g., ELK Stack, Splunk, البياناتdog).

---

# # Secure التطوير Lifecycle (SDL)

1. **Traفيفيg**: Ensure developers understو common vulnerabilities.
2. **Threat modellفيg**: Identify potential threats early في design.
3. **Secure codفيg stوards**: Enلأجلce via lفيters و code review checklists.
4. **SAST** (Static Application الأمان Testفيg): Scan source code لأجل vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application الأمان Testفيg): Scan runnفيg applications (OWASP ZAP, Burp Suite).
6. **SCA** (Sمنtware Composition Analysis): Scan dependencies.
7. **Penetration testفيg**: Regular ethical hackفيg exercises.
8. **Bug bounty**: Encourage external researchers to fفيd vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan لأجل when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** ال affected الأنظمة (disconnect from الشبكة if needed).
3. **Preserve evidence**: Capture logs, memory dumps, و disk images.
4. **Identify** ال scope: which الأنظمة, which البيانات.
5. **Rotate** all compromised credentials و secrets.
6. **Patch** ال vulnerability.
7. **Notify** affected users و regulatory bodies if required (معفي قانوني timeframes).
8. **Conduct a post-mortem** to understو root cause و improve processes.