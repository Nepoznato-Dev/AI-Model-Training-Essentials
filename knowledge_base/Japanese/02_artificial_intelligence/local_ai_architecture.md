<!-- 
This file was automatically translated from English to Japanese.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local AI アーキテクチャ

A practical ガイド to runnでg large 言語 models entirely on-device — hardware considerations, でference engでes, memory optimisation, と system design のために edge デプロイ.

---

# # Why Run AI Locally?

- **Privacy**: No データ leaves その device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, ネットワーク-free でference.
- **Offlでe availability**: Works とout でternet.
- **Control**: Full control over model version, customisation, と fでe-tunでg.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size で memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| でT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| でT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical ガイドlでes:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ システム.

# ## RAM (System Memory)
- For CPU でference, you need enough system RAM to load その model (similar to VRAM numbers).
- For GPU でference, system RAM matters のために loadでg その model でto memory beのためにe のfloadでg to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free のために multiple models.

# ## CPU
- For prompt processでg (prefill) と CPU-のfloadでg, a modern multi-core CPU helps.
- Apple M-series chips have excellent perのためにmance のために LLMs due to その unified memory と Neural Engでe.

---

# # Quantisation

Quantisation reduces その numerical precision の weights, dramatically cuttでg memory と でcreasでg speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp のためにmat, optimised のために CPU/GPU hybrid | Best のために local でference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best のために NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good のために batch でference on GPUs |
| **ONNX** | variable | Stとardised, cross-platのためにm | Production servでg |

# ## Choosでg a Quantisation Level
- **Q8_0** (8-bit): mでimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality のために most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation と better perplexity at 4/3 bits.

**Rule の thumb:** Use Q4_K_M のために a good balance の quality と size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Engでes (Local)

# ## llama.cpp
- Written で C++.
- Supports GGUF のためにmat.
- Optimised のために CPU と GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Commと-lでe, server mode, と Python bでdでgs.

**Example commと:**
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
# セキュリティ ベストプラクティス

A practical ガイド to securでg applications, でfrastructure, と データ — from 開発 to production.

---

# # OWASP Top 10 (2021) — 概要

1. **Broken Access Control**: Users can access resources そのy shouldn't.
2. **Cryptographic Failures**: Weak or missでg encryption.
3. **Injection**: SQL, NoSQL, OS commと, or LDAP でjection.
4. **Insecure Design**: Architectural f法律s.
5. **セキュリティ Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable と Outdated Components**: Known CVEs で dependencies.
7. **Identification と Auそのntication Failures**: Weak passwords, session mis管理.
8. **Sのtware と データ Integrity Failures**: Supply chaで attacks, unsigned updates.
9. **セキュリティ Loggでg と Monitorでg Failures**: No detection の breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse の server to make requests to でternal システム.

---

# # Input Validation と Output Encodでg

# ## Validation Rules
- **Whitelist > Blacklist**: Defでe allowed patterns (e.g., regex のために email) raそのr than blockでg known bad patterns.
- **Length limits**: Enのためにce maximum lengths to prevent buffer overflows と DoS.
- **Type checkでg**: Ensure でtegers are でtegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, と date validation, use stとard libraries (e.g., `email-validator` で Python, `validator.js` で Node).

# ## Output Encodでg
- **HTML encodでg**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user でput でto SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escapでg**: Avoid buildでg shell commとs from user でput; if unavoidable, use `shlex.quote()` or similar.

---

# # Auそのntication と Authorisation

# ## Password 管理
- **Hashでg**: Store passwords と a strong, slow hashでg algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Saltでg**: Add a unique per-user salt.
- **Mでimum length**: Enのためにce at least 12–16 characters.
- **MFA (Multi-Factor Auそのntication)**: Require a second factor (TOTP, SMS, hardware key) のために sensitive operations.
- **Rate limitでg**: Prevent brute-のためにce attempts on logで endpoでts (e.g., 5 attempts per 5 mでutes per IP/user).

# ## Session 管理
- Use secure, HTTP-only, SameSite cookies のために session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout と on password change.
- Avoid exposでg session IDs で URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Sprでg セキュリティ).
- Validate ID tokens thoroughly (sig自然, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON ウェブ Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) のために better セキュリティ; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify sig自然, issuer (`iss`), audience (`aud`), と expiration (`exp`).
- **Keep short expiration**: 15–60 mでutes のために access tokens; use refresh tokens のために longer sessions.
- **Store securely**: Never store JWTs で localStorage (vulnerable to XSS); use HTTP-only cookies でstead.

---

# # API セキュリティ

# ## Auそのntication
- Always auそのnticate API calls (except public endpoでts).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limitでg と Throttlでg
- Apply per-user と per-IP rate limits to prevent abuse と DoS.
- Return `429 Too Many Requests` と a `Retry-After` header.

# ## CORS (Cross-Origで Resource Sharでg)
- Allow only specific origでs (never `*` で production).
- Validate `Origで` header on その server side.

# ## Input Validation
- Validate all request parameters, でcludでg headers と body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` で JSON Schema).

# ## HTTPS / TLS
- Enのためにce HTTPS で production.
- Use HSTS (HTTP Strict Transport セキュリティ) to のためにce browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets 管理

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, データbase URLs) to source control.
- Use environment variables or secret 管理 tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets で files と commit そのm (と KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use と care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets と service accounts.
- Automate rotation where possible.

---

# # Dependency 管理

# ## Vulnerability Scannでg
- **Python**: `安全なty`, `pip-audit`, `bとit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patchでg
- Keep dependencies updated to patched versions.
- Set up automated pull requests のために mでor/patch updates.
- Review changelogs のために breakでg changes.

# ## Supply Chaで Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums の downloaded dependencies.
- Prefer のficial registries と trust only verified publishers.

---

# # Infrastructure セキュリティ

# ## Firewalls
- Block all でbound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use セキュリティ groups (AWS) or NSGs (Azure) のために fでe-graでed control.

# ## OS Hardenでg
- Apply セキュリティ updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services と default accounts.
- Use fail2ban to block brute-のためにce attempts on SSH.
- Harden SSH: disable root logで, use key-based auth, change default port (optional).

# ## ネットワーク Segmentation
- Place データbases と caches で private subnets と no でternet access.
- Use a DMZ のために public-facでg services.
- Apply その prでciple の least privilege to ネットワーク access.

# ## Secrets で Infrastructure
- Never store secrets で CI/CD environment variables unless encrypted.
- Use その cloud provider's IAM roles のために EC2/VM でstances でstead の long-lived keys.

---

# # Loggでg と Monitorでg

# ## What to Log
- Auそのntication イベント (success/failure).
- Access control decisions (authorisation failures).
- Admで actions (user creation, deletion, permission changes).
- データbase schema changes.
- System errors と exceptions.
- API requests と responses (redact sensitive データ).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Inのためにmation) unless hashed/redacted.
- Full credit card numbers.

# ## Alertでg
- Set up alerts のために:
  - Multiple failed logでs (potential brute のためにce).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admで accounts created.
  - High error rates or latency spikes.
- Use a SIEM (セキュリティ Inのためにmation と Event 管理) のために 上級 correlation.

# ## Log Retention
- Retaで logs のために at least 30–90 days dependでg on regulatory requirements.
- Store logs で a centralised, tamper-evident system (e.g., ELK Stack, Splunk, データdog).

---

# # Secure 開発 Lifecycle (SDL)

1. **Traででg**: Ensure developers understと common vulnerabilities.
2. **Threat modellでg**: Identify potential threats early で design.
3. **Secure codでg stとards**: Enのためにce via lでters と code review checklists.
4. **SAST** (Static Application セキュリティ Testでg): Scan source code のために vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application セキュリティ Testでg): Scan runnでg applications (OWASP ZAP, Burp Suite).
6. **SCA** (Sのtware Composition Analysis): Scan dependencies.
7. **Penetration testでg**: Regular ethical hackでg exercises.
8. **Bug bounty**: Encourage external researchers to fでd vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan のために when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** その affected システム (disconnect from ネットワーク if needed).
3. **Preserve evidence**: Capture logs, memory dumps, と disk images.
4. **Identify** その scope: which システム, which データ.
5. **Rotate** all compromised credentials と secrets.
6. **Patch** その vulnerability.
7. **Notify** affected users と regulatory bodies if required (とで 法的 timeframes).
8. **Conduct a post-mortem** to understと root cause と improve processes.