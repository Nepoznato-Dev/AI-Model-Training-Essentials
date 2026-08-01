<!-- 
This file was automatically translated from English to German.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Lokale KI-Architektur

Ein praktischer Leitfaden zum vollständigen Betrieb großer Sprachmodelle auf dem eigenen Gerät – mit Schwerpunkt auf Hardwareanforderungen, Inferenz-Engines, Speicheroptimierung und Systemdesign für Edge-Bereitstellung.

---

## Warum KI lokal ausführen?

- **Datenschutz**: Keine Daten verlassen das Gerät.
- **Kosten**: Keine API-Gebühren pro Token.
- **Latenz**: Vorhersagbare Inferenz ohne Netzwerkabhängigkeit.
- **Offline-Verfügbarkeit**: Funktioniert auch ohne Internet.
- **Kontrolle**: Volle Kontrolle über Modellversion, Anpassung und Fine-Tuning.

---

## Hardwareanforderungen

### GPU-Speicher (VRAM)
Das ist die kritischste Ressource. Die Modellgröße im Speicher lässt sich grob abschätzen als **Parameter × Bytes pro Parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Praktische Richtwerte:**
- 8 GB VRAM → bis zu 7B-Modelle in 4-Bit
- 12 GB VRAM → bis zu 13B-Modelle in 4-Bit
- 24 GB VRAM → bis zu 70B-Modelle in 4-Bit (oder 13B in 8-Bit)
- Apple Silicon mit Unified Memory kann auf Systemen mit 64 GB+ auch 70B-Modelle ausführen

### RAM (Arbeitsspeicher)
- Für CPU-Inferenz benötigen Sie genügend Arbeitsspeicher, um das Modell vollständig zu laden (ähnlich wie bei den VRAM-Werten).
- Für GPU-Inferenz ist System-RAM wichtig, um das Modell zunächst in den Speicher zu laden, bevor es in den VRAM ausgelagert wird.

### Speicherplatz
- Quantisierte Modellgewichte belegen einige GB (z. B. 4-Bit-7B ≈ 4 GB auf der Festplatte). Für mehrere Modelle sollten mindestens 20–50 GB frei sein.

### CPU
- Für die Prompt-Verarbeitung (Prefill) und CPU-Offloading hilft eine moderne Multi-Core-CPU.
- Apple-M-Series-Chips liefern dank Unified Memory und Neural Engine sehr gute Leistung für LLMs.

---

## Quantisierung

Quantisierung verringert die numerische Präzision der Gewichte und spart dadurch erheblich Speicher, während die Geschwindigkeit steigt und die Genauigkeit nur leicht sinkt.

### Gängige Formate

| Format | Bits | Beschreibung | Typische Nutzung |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp-Format, optimiert für CPU/GPU-Hybridbetrieb | Am besten für lokale Inferenz |
| **GPTQ** | 4–8 | Nur für GPU, effizient auf CUDA | Am besten für NVIDIA-GPUs |
| **AWQ** | 4 | Aktivierungsbewusst, nur für GPU | Gut für Batch-Inferenz auf GPUs |
| **ONNX** | variable | Standardisiert, plattformübergreifend | Produktives Serving |

### Wahl des Quantisierungsgrads
- **Q8_0** (8-bit): minimaler Qualitätsverlust, größte Größe.
- **Q6_K** (6-bit): gute Qualität, ordentliche Kompression.
- **Q5_K_M** (5-bit): häufig der beste Kompromiss.
- **Q4_K_M** (4-bit): kleinste Größe bei für viele Aufgaben noch akzeptabler Qualität.
- **IQ4_XS** / **IQ3_XS**: Verbesserte Quantisierung mit besserer Perplexity bei 4 bzw. 3 Bit.

**Faustregel:** Verwenden Sie Q4_K_M als guten Kompromiss zwischen Qualität und Größe. Wenn Sie zusätzlichen VRAM haben, sind Q5 oder Q6 oft die bessere Wahl.

---

## Lokale Inferenz-Engines

### llama.cpp
- In C++ geschrieben.
- Unterstützt das GGUF-Format.
- Für CPU und GPU optimiert (via CUDA, Metal, OpenCL).
- Sehr schnell, besonders auf der CPU.
- Bietet Kommandozeilenbetrieb, Servermodus und Python-Bindings.

**Beispielbefehl:**
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
# Sicherheit Best Practices

A practical Leitfaden to securing applications, infrastructure, und Daten — from Entwicklung to production.

---

## OWASP Top 10 (2021) — Übersicht

1. **Broken Access Control**: Users can access resources they shouldn't.
2. **Cryptographic Failures**: Weak or missing encryption.
3. **Injection**: SQL, NoSQL, OS command, or LDAP injection.
4. **Insecure Design**: Architectural flaws.
5. **Sicherheit Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable und Outdated Components**: Known CVEs in dependencies.
7. **Identification und Authentication Failures**: Weak passwords, session mismanagement.
8. **Software und Daten Integrity Failures**: Supply chain attacks, unsigned updates.
9. **Sicherheit Logging und Monitoring Failures**: No detection von breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse von server to make requests to internal Systeme.

---

## Input Validation und Output Encoding

### Validation Rules
- **Whitelist > Blacklist**: Define allowed patterns (e.g., regex für email) rather than blocking known bad patterns.
- **Length limits**: Enforce maximum lengths to prevent buffer overflows und DoS.
- **Type checking**: Ensure integers are integers, booleans are booleans.
- **Use well-tested libraries**: für email, URL, und date validation, use standard libraries (e.g., `email-validator` in Python, `validator.js` in Node).

### Output Encoding
- **HTML encoding**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user input into SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escaping**: Avoid building shell Befehle from user input; if unavoidable, use `shlex.quote()` or similar.

---

## Authentication und Authorisation

### Password Verwaltung
- **Hashing**: Store passwords mit a strong, slow hashing algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Salting**: Add a unique per-user salt.
- **Minimum length**: Enforce at least 12–16 characters.
- **MFA (Multi-Factor Authentication)**: Require a second factor (TOTP, SMS, hardware key) für sensitive operations.
- **Rate limiting**: Prevent brute-force attempts on login endpoints (e.g., 5 attempts per 5 minutes per IP/user).

### Session Verwaltung
- Use secure, HTTP-only, SameSite cookies für session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout und on password change.
- Avoid exposing session IDs in URLs.

### OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spring Sicherheit).
- Validate ID tokens thoroughly (signature, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

### JWT (JSON Web Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) für better Sicherheit; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify signature, issuer (`iss`), audience (`aud`), und expiration (`exp`).
- **Keep short expiration**: 15–60 minutes für access tokens; use refresh tokens für longer sessions.
- **Store securely**: Never store JWTs in localStorage (vulnerable to XSS); use HTTP-only cookies instead.

---

## API Sicherheit

### Authentication
- Always authenticate API calls (except public endpoints).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

### Rate Limiting und Throttling
- Apply per-user und per-IP rate limits to prevent abuse und DoS.
- Return `429 Too Many Requests` mit a `Retry-After` header.

### CORS (Cross-Origin Resource Sharing)
- Allow only specific origins (never `*` in production).
- Validate `Origin` header on der Serverseite.

### Input Validation
- Validate all request parameters, including headers und body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` in JSON Schema).

### HTTPS / TLS
- Enforce HTTPS in production.
- Use HSTS (HTTP Strict Transport Sicherheit) to force browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

## Secrets Verwaltung

### Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, Datenbank URLs) to source control.
- Use environment variables or secret Verwaltung tools.

### Tools
- **HashiCorp Vault**: Enterprise-grade, dynamic secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native.
- **SOPS**: Encrypt secrets in files und commit them (mit KMS or GPG).
- **Docker secrets**: für Swarm mode; Kubernetes secrets (base64-encoded, but use mit care; consider external Secrets Store CSI driver).

### Rotation
- Regularly rotate secrets und service accounts.
- Automate rotation where possible.

---

## Dependency Verwaltung

### Vulnerability Scanning
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Patching
- Keep dependencies updated to patched versions.
- Set up automated pull requests für minor/patch updates.
- Review changelogs für breaking changes.

### Supply Chain Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums von downloaded dependencies.
- Prefer official registries und trust only verified publishers.

---

## Infrastructure Sicherheit

### Firewalls
- Block all inbound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use Sicherheit groups (AWS) or NSGs (Azure) für fine-grained control.

### OS Hardening
- Apply Sicherheit updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services und default accounts.
- Use fail2ban to block brute-force attempts on SSH.
- Harden SSH: disable root login, use key-based auth, change default port (optional).

### Netzwerk Segmentation
- Place databases und caches in private subnets mit no internet access.
- Use a DMZ für public-facing services.
- Apply das Prinzip von least privilege to Netzwerk access.

### Secrets in Infrastructure
- Never store secrets in CI/CD environment variables unless encrypted.
- Use des Cloud-Anbieters's IAM roles für EC2/VM instances instead von long-lived keys.

---

## Logging und Monitoring

### What to Log
- Authentication Ereignisse (success/failure).
- Access control decisions (authorisation failures).
- Admin actions (user creation, deletion, permission changes).
- Datenbank schema changes.
- System errors und exceptions.
- API requests und responses (redact sensitive Daten).

### What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Information) unless hashed/redacted.
- Full credit card numbers.

### Alerting
- Set up alerts für:
  - Multiple failed logins (potential brute force).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admin accounts created.
  - High error rates or latency spikes.
- Use a SIEM (Sicherheit Information und Event Verwaltung) für Fortgeschritten correlation.

### Log Retention
- Retain logs für at least 30–90 days depending on regulatory requirements.
- Store logs in a centralised, tamper-evident system (e.g., ELK Stack, Splunk, Datadog).

---

## Secure Entwicklung Lifecycle (SDL)

1. **Training**: Ensure developers understand common vulnerabilities.
2. **Threat modelling**: Identify potential threats early in design.
3. **Secure coding standards**: Enforce via linters und code review checklists.
4. **SAST** (Static Application Sicherheit Testen): Scan source code für vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Sicherheit Testen): Scan running applications (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): Scan dependencies.
7. **Penetration Testen**: Regular ethical hacking exercises.
8. **Bug bounty**: Encourage external researchers to find vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan für when a breach is detected.

---

## Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** das betroffene System (disconnect from Netzwerk if needed).
3. **Preserve evidence**: Capture logs, memory dumps, und disk images.
4. **Identify** den Umfang: which Systeme, which Daten.
5. **Rotate** all compromised credentials und secrets.
6. **Patch** die Schwachstelle.
7. **Notify** affected users und regulatory bodies if required (within Rechtlich timeframes).
8. **Conduct a post-mortem** to understand root cause und improve processes.
