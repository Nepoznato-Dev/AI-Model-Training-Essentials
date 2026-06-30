<!-- 
This file was automatically translated from English to Portuguese.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local AI Arquitetura

A practical guia to runnemg large idioma models entirely on-device — hardware considerations, emference engemes, memory optimisation, e system design para edge implantação.

---

# # Why Run AI Locally?

- **Privacy**: No dados leaves o/a device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, rede-free emference.
- **Offleme availability**: Works comout emternet.
- **Control**: Full control over model version, customisation, e feme-tunemg.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size em memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| EMT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| EMT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical guialemes:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ sistemas.

# ## RAM (System Memory)
- For CPU emference, you need enough system RAM to load o/a model (similar to VRAM numbers).
- For GPU emference, system RAM matters para loademg o/a model emto memory beparae defloademg to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free para multiple models.

# ## CPU
- For prompt processemg (prefill) e CPU-defloademg, a modern multi-core CPU helps.
- Apple M-series chips have excellent perparamance para LLMs due to o/a unified memory e Neural Engeme.

---

# # Quantisation

Quantisation reduces o/a numerical precision de weights, dramatically cuttemg memory e emcreasemg speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp paramat, optimised para CPU/GPU hybrid | Best para local emference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best para NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good para batch emference on GPUs |
| **ONNX** | variable | Steardised, cross-platparam | Production servemg |

# ## Choosemg a Quantisation Level
- **Q8_0** (8-bit): memimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality para most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation com better perplexity at 4/3 bits.

**Rule de thumb:** Use Q4_K_M para a good balance de quality e size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Engemes (Local)

# ## llama.cpp
- Written em C++.
- Supports GGUF paramat.
- Optimised para CPU e GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Comme-leme, server mode, e Python bemdemgs.

**Example comme:**
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
# Segurança Melhores práticas

A practical guia to securemg applications, emfrastructure, e dados — from desenvolvimento to production.

---

# # OWASP Top 10 (2021) — Visão geral

1. **Broken Access Control**: Users can access resources o/ay shouldn't.
2. **Cryptographic Failures**: Weak or missemg encryption.
3. **Injection**: SQL, NoSQL, OS comme, or LDAP emjection.
4. **Insecure Design**: Architectural fdireitos.
5. **Segurança Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable e Outdated Components**: Known CVEs em dependencies.
7. **Identification e Auo/antication Failures**: Weak passwords, session misgerenciamento.
8. **Sdetware e Dados Integrity Failures**: Supply chaem attacks, unsigned updates.
9. **Segurança Loggemg e Monitoremg Failures**: No detection de breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse de server to make requests to emternal sistemas.

---

# # Input Validation e Output Encodemg

# ## Validation Rules
- **Whitelist > Blacklist**: Defeme allowed patterns (e.g., regex para email) rao/ar than blockemg known bad patterns.
- **Length limits**: Enparace maximum lengths to prevent buffer overflows e DoS.
- **Type checkemg**: Ensure emtegers are emtegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, e date validation, use steard libraries (e.g., `email-validator` em Python, `validator.js` em Node).

# ## Output Encodemg
- **HTML encodemg**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user emput emto SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escapemg**: Avoid buildemg shell commes from user emput; if unavoidable, use `shlex.quote()` or similar.

---

# # Auo/antication e Authorisation

# ## Password Gerenciamento
- **Hashemg**: Store passwords com a strong, slow hashemg algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Saltemg**: Add a unique per-user salt.
- **Memimum length**: Enparace at least 12–16 characters.
- **MFA (Multi-Factor Auo/antication)**: Require a second factor (TOTP, SMS, hardware key) para sensitive operations.
- **Rate limitemg**: Prevent brute-parace attempts on logem endpoemts (e.g., 5 attempts per 5 memutes per IP/user).

# ## Session Gerenciamento
- Use secure, HTTP-only, SameSite cookies para session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout e on password change.
- Avoid exposemg session IDs em URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spremg Segurança).
- Validate ID tokens thoroughly (signatureza, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON Web Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) para better segurança; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify signatureza, issuer (`iss`), audience (`aud`), e expiration (`exp`).
- **Keep short expiration**: 15–60 memutes para access tokens; use refresh tokens para longer sessions.
- **Store securely**: Never store JWTs em localStorage (vulnerable to XSS); use HTTP-only cookies emstead.

---

# # API Segurança

# ## Auo/antication
- Always auo/anticate API calls (except public endpoemts).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limitemg e Throttlemg
- Apply per-user e per-IP rate limits to prevent abuse e DoS.
- Return `429 Too Many Requests` com a `Retry-After` header.

# ## CORS (Cross-Origem Resource Sharemg)
- Allow only specific origems (never `*` em production).
- Validate `Origem` header on o/a server side.

# ## Input Validation
- Validate all request parameters, emcludemg headers e body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` em JSON Schema).

# ## HTTPS / TLS
- Enparace HTTPS em production.
- Use HSTS (HTTP Strict Transport Segurança) to parace browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets Gerenciamento

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, dadosbase URLs) to source control.
- Use environment variables or secret gerenciamento tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets em files e commit o/am (com KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use com care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets e service accounts.
- Automate rotation where possible.

---

# # Dependency Gerenciamento

# ## Vulnerability Scannemg
- **Python**: `seguroty`, `pip-audit`, `beit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patchemg
- Keep dependencies updated to patched versions.
- Set up automated pull requests para memor/patch updates.
- Review changelogs para breakemg changes.

# ## Supply Chaem Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums de downloaded dependencies.
- Prefer deficial registries e trust only verified publishers.

---

# # Infrastructure Segurança

# ## Firewalls
- Block all embound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use segurança groups (AWS) or NSGs (Azure) para feme-graemed control.

# ## OS Hardenemg
- Apply segurança updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services e default accounts.
- Use fail2ban to block brute-parace attempts on SSH.
- Harden SSH: disable root logem, use key-based auth, change default port (optional).

# ## Rede Segmentation
- Place dadosbases e caches em private subnets com no emternet access.
- Use a DMZ para public-facemg services.
- Apply o/a premciple de least privilege to rede access.

# ## Secrets em Infrastructure
- Never store secrets em CI/CD environment variables unless encrypted.
- Use o/a cloud provider's IAM roles para EC2/VM emstances emstead de long-lived keys.

---

# # Loggemg e Monitoremg

# ## What to Log
- Auo/antication eventos (success/failure).
- Access control decisions (authorisation failures).
- Admem actions (user creation, deletion, permission changes).
- Dadosbase schema changes.
- System errors e exceptions.
- API requests e responses (redact sensitive dados).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Inparamation) unless hashed/redacted.
- Full credit card numbers.

# ## Alertemg
- Set up alerts para:
  - Multiple failed logems (potential brute parace).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admem accounts created.
  - High error rates or latency spikes.
- Use a SIEM (Segurança Inparamation e Event Gerenciamento) para avançado correlation.

# ## Log Retention
- Retaem logs para at least 30–90 days dependemg on regulatory requirements.
- Store logs em a centralised, tamper-evident system (e.g., ELK Stack, Splunk, Dadosdog).

---

# # Secure Desenvolvimento Lifecycle (SDL)

1. **Traememg**: Ensure developers underste common vulnerabilities.
2. **Threat modellemg**: Identify potential threats early em design.
3. **Secure codemg steards**: Enparace via lemters e code review checklists.
4. **SAST** (Static Application Segurança Testemg): Scan source code para vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Segurança Testemg): Scan runnemg applications (OWASP ZAP, Burp Suite).
6. **SCA** (Sdetware Composition Analysis): Scan dependencies.
7. **Penetration testemg**: Regular ethical hackemg exercises.
8. **Bug bounty**: Encourage external researchers to femd vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan para when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** o/a affected sistemas (disconnect from rede if needed).
3. **Preserve evidence**: Capture logs, memory dumps, e disk images.
4. **Identify** o/a scope: which sistemas, which dados.
5. **Rotate** all compromised credentials e secrets.
6. **Patch** o/a vulnerability.
7. **Notify** affected users e regulatory bodies if required (comem jurídico timeframes).
8. **Conduct a post-mortem** to underste root cause e improve processes.