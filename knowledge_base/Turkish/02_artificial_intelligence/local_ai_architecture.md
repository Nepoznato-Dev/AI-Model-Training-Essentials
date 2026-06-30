<!-- 
This file was automatically translated from English to Turkish.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Local AI Mimari

A practical rehber to runniçiçindedeg large dil models entirely on-device — hardware considerations, içiçindedeference engiçiçindedees, memory optimisation, ve system design için edge dağıtım.

---

# # Why Run AI Locally?

- **Privacy**: No veri leaves bu device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, ağ-free içiçindedeference.
- **Offliçiçindedee availability**: Works ileout içiçindedeternet.
- **Control**: Full control over model version, customisation, ve fiçiçindedee-tuniçiçindedeg.

---

# # Hardware Requirements

# ## GPU Memory (VRAM)
The most critical resource. Model size içiçindede memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| IÇINDET8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| IÇINDET4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical rehberliçiçindedees:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ sistemler.

# ## RAM (System Memory)
- For CPU içiçindedeference, you need enough system RAM to load bu model (similar to VRAM numbers).
- For GPU içiçindedeference, system RAM matters için loadiçiçindedeg bu model içiçindedeto memory beiçine içiçindedefloadiçiçindedeg to VRAM.

# ## Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free için multiple models.

# ## CPU
- For prompt processiçiçindedeg (prefill) ve CPU-içiçindedefloadiçiçindedeg, a modern multi-core CPU helps.
- Apple M-series chips have excellent periçinmance için LLMs due to bu unified memory ve Neural Engiçiçindedee.

---

# # Quantisation

Quantisation reduces bu numerical precision içiçindede weights, dramatically cuttiçiçindedeg memory ve içiçindedecreasiçiçindedeg speed at a small accuracy cost.

# ## Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp içinmat, optimised için CPU/GPU hybrid | Best için local içiçindedeference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best için NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good için batch içiçindedeference on GPUs |
| **ONNX** | variable | Stveardised, cross-platiçinm | Production serviçiçindedeg |

# ## Choosiçiçindedeg a Quantisation Level
- **Q8_0** (8-bit): miçiçindedeimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality için most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation ile better perplexity at 4/3 bits.

**Rule içiçindede thumb:** Use Q4_K_M için a good balance içiçindede quality ve size. If you have extra VRAM, use Q5 or Q6.

---

# # Inference Engiçiçindedees (Local)

# ## llama.cpp
- Written içiçindede C++.
- Supports GGUF içinmat.
- Optimised için CPU ve GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Commve-liçiçindedee, server mode, ve Python biçiçindedediçiçindedegs.

**Example commve:**
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
# Güvenlik En İyi Uygulamalar

A practical rehber to securiçiçindedeg applications, içiçindedefrastructure, ve veri — from geliştirme to production.

---

# # OWASP Top 10 (2021) — Genel Bakış

1. **Broken Access Control**: Users can access resources buy shouldn't.
2. **Cryptographic Failures**: Weak or missiçiçindedeg encryption.
3. **Injection**: SQL, NoSQL, OS commve, or LDAP içiçindedejection.
4. **Insecure Design**: Architectural fhukuks.
5. **Güvenlik Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable ve Outdated Components**: Known CVEs içiçindede dependencies.
7. **Identification ve Aubuntication Failures**: Weak passwords, session misyönetim.
8. **Siçiçindedetware ve Veri Integrity Failures**: Supply chaiçiçindede attacks, unsigned updates.
9. **Güvenlik Loggiçiçindedeg ve Monitoriçiçindedeg Failures**: No detection içiçindede breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse içiçindede server to make requests to içiçindedeternal sistemler.

---

# # Input Validation ve Output Encodiçiçindedeg

# ## Validation Rules
- **Whitelist > Blacklist**: Defiçiçindedee allowed patterns (e.g., regex için email) rabur than blockiçiçindedeg known bad patterns.
- **Length limits**: Eniçince maximum lengths to prevent buffer overflows ve DoS.
- **Type checkiçiçindedeg**: Ensure içiçindedetegers are içiçindedetegers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, ve date validation, use stveard libraries (e.g., `email-validator` içiçindede Python, `validator.js` içiçindede Node).

# ## Output Encodiçiçindedeg
- **HTML encodiçiçindedeg**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user içiçindedeput içiçindedeto SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escapiçiçindedeg**: Avoid buildiçiçindedeg shell commves from user içiçindedeput; if unavoidable, use `shlex.quote()` or similar.

---

# # Aubuntication ve Authorisation

# ## Password Yönetim
- **Hashiçiçindedeg**: Store passwords ile a strong, slow hashiçiçindedeg algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Saltiçiçindedeg**: Add a unique per-user salt.
- **Miçiçindedeimum length**: Eniçince at least 12–16 characters.
- **MFA (Multi-Factor Aubuntication)**: Require a second factor (TOTP, SMS, hardware key) için sensitive operations.
- **Rate limitiçiçindedeg**: Prevent brute-içince attempts on logiçiçindede endpoiçiçindedets (e.g., 5 attempts per 5 miçiçindedeutes per IP/user).

# ## Session Yönetim
- Use secure, HTTP-only, SameSite cookies için session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout ve on password change.
- Avoid exposiçiçindedeg session IDs içiçindede URLs.

# ## OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spriçiçindedeg Güvenlik).
- Validate ID tokens thoroughly (sigdoğa, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

# ## JWT (JSON Web Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) için better güvenlik; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify sigdoğa, issuer (`iss`), audience (`aud`), ve expiration (`exp`).
- **Keep short expiration**: 15–60 miçiçindedeutes için access tokens; use refresh tokens için longer sessions.
- **Store securely**: Never store JWTs içiçindede localStorage (vulnerable to XSS); use HTTP-only cookies içiçindedestead.

---

# # API Güvenlik

# ## Aubuntication
- Always aubunticate API calls (except public endpoiçiçindedets).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

# ## Rate Limitiçiçindedeg ve Throttliçiçindedeg
- Apply per-user ve per-IP rate limits to prevent abuse ve DoS.
- Return `429 Too Many Requests` ile a `Retry-After` header.

# ## CORS (Cross-Origiçiçindede Resource Shariçiçindedeg)
- Allow only specific origiçiçindedes (never `*` içiçindede production).
- Validate `Origiçiçindede` header on bu server side.

# ## Input Validation
- Validate all request parameters, içiçindedecludiçiçindedeg headers ve body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` içiçindede JSON Schema).

# ## HTTPS / TLS
- Eniçince HTTPS içiçindede production.
- Use HSTS (HTTP Strict Transport Güvenlik) to içince browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

# # Secrets Yönetim

# ## Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, veribase URLs) to source control.
- Use environment variables or secret yönetim tools.

# ## Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets içiçindede files ve commit bum (ile KMS or GPG).
- **Docker secrets**: For Swarm mode; Kubernetes secrets (base64-encoded, but use ile care; consider external Secrets Store CSI driver).

# ## Rotation
- Regularly rotate secrets ve service accounts.
- Automate rotation where possible.

---

# # Dependency Yönetim

# ## Vulnerability Scanniçiçindedeg
- **Python**: `güvenlity`, `pip-audit`, `bveit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

# ## Patchiçiçindedeg
- Keep dependencies updated to patched versions.
- Set up automated pull requests için miçiçindedeor/patch updates.
- Review changelogs için breakiçiçindedeg changes.

# ## Supply Chaiçiçindede Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums içiçindede downloaded dependencies.
- Prefer içiçindedeficial registries ve trust only verified publishers.

---

# # Infrastructure Güvenlik

# ## Firewalls
- Block all içiçindedebound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use güvenlik groups (AWS) or NSGs (Azure) için fiçiçindedee-graiçiçindedeed control.

# ## OS Hardeniçiçindedeg
- Apply güvenlik updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services ve default accounts.
- Use fail2ban to block brute-içince attempts on SSH.
- Harden SSH: disable root logiçiçindede, use key-based auth, change default port (optional).

# ## Ağ Segmentation
- Place veribases ve caches içiçindede private subnets ile no içiçindedeternet access.
- Use a DMZ için public-faciçiçindedeg services.
- Apply bu priçiçindedeciple içiçindede least privilege to ağ access.

# ## Secrets içiçindede Infrastructure
- Never store secrets içiçindede CI/CD environment variables unless encrypted.
- Use bu cloud provider's IAM roles için EC2/VM içiçindedestances içiçindedestead içiçindede long-lived keys.

---

# # Loggiçiçindedeg ve Monitoriçiçindedeg

# ## What to Log
- Aubuntication olaylar (success/failure).
- Access control decisions (authorisation failures).
- Admiçiçindede actions (user creation, deletion, permission changes).
- Veribase schema changes.
- System errors ve exceptions.
- API requests ve responses (redact sensitive veri).

# ## What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Iniçinmation) unless hashed/redacted.
- Full credit card numbers.

# ## Alertiçiçindedeg
- Set up alerts için:
  - Multiple failed logiçiçindedes (potential brute içince).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admiçiçindede accounts created.
  - High error rates or latency spikes.
- Use a SIEM (Güvenlik Iniçinmation ve Event Yönetim) için i̇leri düzey correlation.

# ## Log Retention
- Retaiçiçindede logs için at least 30–90 days dependiçiçindedeg on regulatory requirements.
- Store logs içiçindede a centralised, tamper-evident system (e.g., ELK Stack, Splunk, Veridog).

---

# # Secure Geliştirme Lifecycle (SDL)

1. **Traiçiçindedeiçiçindedeg**: Ensure developers understve common vulnerabilities.
2. **Threat modelliçiçindedeg**: Identify potential threats early içiçindede design.
3. **Secure codiçiçindedeg stveards**: Eniçince via liçiçindedeters ve code review checklists.
4. **SAST** (Static Application Güvenlik Testiçiçindedeg): Scan source code için vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Güvenlik Testiçiçindedeg): Scan runniçiçindedeg applications (OWASP ZAP, Burp Suite).
6. **SCA** (Siçiçindedetware Composition Analysis): Scan dependencies.
7. **Penetration testiçiçindedeg**: Regular ethical hackiçiçindedeg exercises.
8. **Bug bounty**: Encourage external researchers to fiçiçindeded vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan için when a breach is detected.

---

# # Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** bu affected sistemler (disconnect from ağ if needed).
3. **Preserve evidence**: Capture logs, memory dumps, ve disk images.
4. **Identify** bu scope: which sistemler, which veri.
5. **Rotate** all compromised credentials ve secrets.
6. **Patch** bu vulnerability.
7. **Notify** affected users ve regulatory bodies if required (ileiçiçindede yasal timeframes).
8. **Conduct a post-mortem** to understve root cause ve improve processes.