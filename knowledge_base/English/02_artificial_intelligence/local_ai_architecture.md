# Local AI Architecture

A practical guide to running large language models entirely on-device — hardware considerations, inference engines, memory optimisation, and system design for edge deployment.

---

## Why Run AI Locally?

- **Privacy**: No data leaves the device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, network-free inference.
- **Offline availability**: Works without internet.
- **Control**: Full control over model version, customisation, and fine-tuning.

---

## Hardware Requirements

### GPU Memory (VRAM)
The most critical resource. Model size in memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical guidelines:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ systems.

### RAM (System Memory)
- For CPU inference, you need enough system RAM to load the model (similar to VRAM numbers).
- For GPU inference, system RAM matters for loading the model into memory before offloading to VRAM.

### Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free for multiple models.

### CPU
- For prompt processing (prefill) and CPU-offloading, a modern multi-core CPU helps.
- Apple M-series chips have excellent performance for LLMs due to the unified memory and Neural Engine.

---

## Quantisation

Quantisation reduces the numerical precision of weights, dramatically cutting memory and increasing speed at a small accuracy cost.

### Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp format, optimised for CPU/GPU hybrid | Best for local inference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best for NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good for batch inference on GPUs |
| **ONNX** | variable | Standardised, cross-platform | Production serving |

### Choosing a Quantisation Level
- **Q8_0** (8-bit): minimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality for most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation with better perplexity at 4/3 bits.

**Rule of thumb:** Use Q4_K_M for a good balance of quality and size. If you have extra VRAM, use Q5 or Q6.

---

## Inference Engines (Local)

### llama.cpp
- Written in C++.
- Supports GGUF format.
- Optimised for CPU and GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Command-line, server mode, and Python bindings.

**Example command:**
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
# Security Best Practices

A practical guide to securing applications, infrastructure, and data — from development to production.

---

## OWASP Top 10 (2021) — Overview

1. **Broken Access Control**: Users can access resources they shouldn't.
2. **Cryptographic Failures**: Weak or missing encryption.
3. **Injection**: SQL, NoSQL, OS command, or LDAP injection.
4. **Insecure Design**: Architectural flaws.
5. **Security Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable and Outdated Components**: Known CVEs in dependencies.
7. **Identification and Authentication Failures**: Weak passwords, session mismanagement.
8. **Software and Data Integrity Failures**: Supply chain attacks, unsigned updates.
9. **Security Logging and Monitoring Failures**: No detection of breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse of server to make requests to internal systems.

---

## Input Validation and Output Encoding

### Validation Rules
- **Whitelist > Blacklist**: Define allowed patterns (e.g., regex for email) rather than blocking known bad patterns.
- **Length limits**: Enforce maximum lengths to prevent buffer overflows and DoS.
- **Type checking**: Ensure integers are integers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, and date validation, use standard libraries (e.g., `email-validator` in Python, `validator.js` in Node).

### Output Encoding
- **HTML encoding**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user input into SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escaping**: Avoid building shell commands from user input; if unavoidable, use `shlex.quote()` or similar.

---

## Authentication and Authorisation

### Password Management
- **Hashing**: Store passwords with a strong, slow hashing algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Salting**: Add a unique per-user salt.
- **Minimum length**: Enforce at least 12–16 characters.
- **MFA (Multi-Factor Authentication)**: Require a second factor (TOTP, SMS, hardware key) for sensitive operations.
- **Rate limiting**: Prevent brute-force attempts on login endpoints (e.g., 5 attempts per 5 minutes per IP/user).

### Session Management
- Use secure, HTTP-only, SameSite cookies for session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout and on password change.
- Avoid exposing session IDs in URLs.

### OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spring Security).
- Validate ID tokens thoroughly (signature, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

### JWT (JSON Web Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) for better security; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify signature, issuer (`iss`), audience (`aud`), and expiration (`exp`).
- **Keep short expiration**: 15–60 minutes for access tokens; use refresh tokens for longer sessions.
- **Store securely**: Never store JWTs in localStorage (vulnerable to XSS); use HTTP-only cookies instead.

---

## API Security

### Authentication
- Always authenticate API calls (except public endpoints).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

### Rate Limiting and Throttling
- Apply per-user and per-IP rate limits to prevent abuse and DoS.
- Return `429 Too Many Requests` with a `Retry-After` header.

### CORS (Cross-Origin Resource Sharing)
- Allow only specific origins (never `*` in production).
- Validate `Origin` header on the server side.

### Input Validation
- Validate all request parameters, including headers and body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` in JSON Schema).

### HTTPS / TLS
- Enforce HTTPS in production.
- Use HSTS (HTTP Strict Transport Security) to force browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

## Secrets Management

### Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, database URLs) to source control.
- Use environment variables or secret management tools.

### Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets in files and commit them (with KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use with care; consider external Secrets Store CSI driver).

### Rotation
- Regularly rotate secrets and service accounts.
- Automate rotation where possible.

---

## Dependency Management

### Vulnerability Scanning
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Patching
- Keep dependencies updated to patched versions.
- Set up automated pull requests for minor/patch updates.
- Review changelogs for breaking changes.

### Supply Chain Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums of downloaded dependencies.
- Prefer official registries and trust only verified publishers.

---

## Infrastructure Security

### Firewalls
- Block all inbound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use security groups (AWS) or NSGs (Azure) for fine-grained control.

### OS Hardening
- Apply security updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services and default accounts.
- Use fail2ban to block brute-force attempts on SSH.
- Harden SSH: disable root login, use key-based auth, change default port (optional).

### Network Segmentation
- Place databases and caches in private subnets with no internet access.
- Use a DMZ for public-facing services.
- Apply the principle of least privilege to network access.

### Secrets in Infrastructure
- Never store secrets in CI/CD environment variables unless encrypted.
- Use the cloud provider's IAM roles for EC2/VM instances instead of long-lived keys.

---

## Logging and Monitoring

### What to Log
- Authentication events (success/failure).
- Access control decisions (authorisation failures).
- Admin actions (user creation, deletion, permission changes).
- Database schema changes.
- System errors and exceptions.
- API requests and responses (redact sensitive data).

### What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Information) unless hashed/redacted.
- Full credit card numbers.

### Alerting
- Set up alerts for:
  - Multiple failed logins (potential brute force).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admin accounts created.
  - High error rates or latency spikes.
- Use a SIEM (Security Information and Event Management) for advanced correlation.

### Log Retention
- Retain logs for at least 30–90 days depending on regulatory requirements.
- Store logs in a centralised, tamper-evident system (e.g., ELK Stack, Splunk, Datadog).

---

## Secure Development Lifecycle (SDL)

1. **Training**: Ensure developers understand common vulnerabilities.
2. **Threat modelling**: Identify potential threats early in design.
3. **Secure coding standards**: Enforce via linters and code review checklists.
4. **SAST** (Static Application Security Testing): Scan source code for vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): Scan running applications (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): Scan dependencies.
7. **Penetration testing**: Regular ethical hacking exercises.
8. **Bug bounty**: Encourage external researchers to find vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan for when a breach is detected.

---

## Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** the affected systems (disconnect from network if needed).
3. **Preserve evidence**: Capture logs, memory dumps, and disk images.
4. **Identify** the scope: which systems, which data.
5. **Rotate** all compromised credentials and secrets.
6. **Patch** the vulnerability.
7. **Notify** affected users and regulatory bodies if required (within legal timeframes).
8. **Conduct a post-mortem** to understand root cause and improve processes.