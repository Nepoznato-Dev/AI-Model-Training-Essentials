# Локальная архитектура AI

Практическое руководство по запуску large language models полностью на устройстве — аппаратные требования, inference engines, оптимизация памяти и проектирование систем для edge deployment.

---

## Зачем запускать AI локально?

- **Приватность**: Данные не покидают устройство.
- **Стоимость**: Нет оплаты API за каждый token.
- **Задержка**: Предсказуемый inference без зависимости от сети.
- **Доступность офлайн**: Работает без интернета.
- **Контроль**: Полный контроль над версией модели, кастомизацией и fine-tuning.

---

## Требования к оборудованию

### Память GPU (VRAM)
Самый критичный ресурс. Размер модели в памяти ≈ **parameters × bytes per parameter**.

| Точность | Байт на параметр | Модель 3.8B | Модель 7B | Модель 13B | Модель 70B |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Практические рекомендации:**
- 8GB VRAM → до 7B-моделей в 4-bit.
- 12GB VRAM → до 13B-моделей в 4-bit.
- 24GB VRAM → до 70B-моделей в 4-bit (или 13B в 8-bit).
- Apple Silicon (unified memory) может запускать 70B-модели на системах с 64GB+.

### RAM (System Memory)
- Для CPU inference нужна достаточная системная RAM, чтобы загрузить модель (ориентируйтесь примерно на те же значения, что и для VRAM).
- Для GPU inference системная RAM важна для загрузки модели в память перед выгрузкой в VRAM.

### Storage
- Квантованные веса модели занимают несколько GB (например, 4-bit 7B ≈ 4 GB на диске). Для нескольких моделей стоит иметь как минимум 20–50 GB свободного места.

### CPU
- Для prompt processing (prefill) и CPU-offloading полезен современный многоядерный CPU.
- Чипы Apple M-series отлично подходят для LLM благодаря unified memory и Neural Engine.

---

## Quantisation

Quantisation уменьшает числовую точность весов, что резко снижает расход памяти и повышает скорость ценой небольшой потери качества.

### Популярные форматы

| Формат | Биты | Описание | Типичное применение |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | Формат llama.cpp, оптимизированный для гибридного CPU/GPU | Лучший выбор для локального inference |
| **GPTQ** | 4–8 | Только для GPU, эффективен на CUDA | Лучший выбор для NVIDIA GPU |
| **AWQ** | 4 | Учитывает активации, только для GPU | Подходит для batch inference на GPU |
| **ONNX** | variable | Стандартизированный, кроссплатформенный | Production serving |

### Выбор уровня квантования
- **Q8_0** (8-bit): минимальная потеря качества, самый большой размер.
- **Q6_K** (6-bit): хорошее качество, достойное сжатие.
- **Q5_K_M** (5-bit): распространённая золотая середина.
- **Q4_K_M** (4-bit): самый маленький размер, приемлемое качество для большинства задач.
- **IQ4_XS** / **IQ3_XS**: Улучшенное квантование с лучшей perplexity при 4/3 bits.

**Общее правило:** Используйте Q4_K_M для хорошего баланса между качеством и размером. Если VRAM с запасом, выбирайте Q5 или Q6.

---

## Inference Engines (Local)

### llama.cpp
- Написан на C++.
- Поддерживает формат GGUF.
- Оптимизирован для CPU и GPU (через CUDA, Metal, OpenCL).
- Очень быстрый, особенно на CPU.
- Command-line интерфейс, server mode и Python bindings.

**Example command:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)

Ollama
Оборачивает llama.cpp простым CLI и REST API.

Автоматически скачивает модели и управляет ими.

Отлично подходит для прототипирования и desktop-приложений.

Поддерживает пользовательские Modelfiles для system prompts.

Пример использования:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Графическое desktop-приложение для Windows, macOS и Linux.

Скачивание в один клик и интерфейс чата.

Встроенный локальный сервер с OpenAI-compatible API.

Хорошо подходит для нетехнических пользователей и быстрого тестирования.

Hugging Face Transformers + bitsandbytes
Стандартная Python-библиотека для HF-моделей.

Используйте bitsandbytes для 4-bit quantisation (load_in_4bit=True).

Она гибче для fine-tuning, но для inference медленнее, чем llama.cpp.

ExLlamaV2
Очень быстрый GPU inference для GPTQ и AWQ.

Лучшая производительность на NVIDIA GPU.

Поддерживает batched generation.

mlx (Apple)
Фреймворк Apple для чипов M-series.

Сильно оптимизирован для Apple Silicon.

Python API.

Управление памятью
Контекстное окно и KV cache
KV cache хранит пары ключ-значение для каждого слоя и каждого token в контексте. Он растёт линейно вместе с длиной контекста.

Затраты памяти ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

Для модели с 32 слоями, 8 KV heads и 128 head dim каждый token стоит ~32 × 8 × 128 × 2 bytes = 65 KB на token. Для 128k tokens это ~8 GB только на cache.

Стратегии offloading
Layer offloading: Часть слоёв размещается на GPU, остальные — на CPU. Это быстрее, чем чистый CPU, и требует меньше VRAM.

Token streaming: Обрабатывайте tokens постепенно, а не все сразу.

Кэширование prompt'ов
Переиспользуйте KV cache для похожих prompt'ов, чтобы не пересчитывать фазу prefill. Некоторые фреймворки это поддерживают (например, vLLM, llama.cpp с --prompt-cache).

Файлы с memory mapping
Загружайте веса модели прямо с диска, не помещая их целиком в RAM (полезно для огромных моделей на системах с ограниченной памятью). llama.cpp по умолчанию использует memory mapping.

Архитектуры развёртывания
Режим одного устройства
Одна модель работает на одной машине (ноутбук, смартфон, edge device). Подходит для персональных ассистентов, приложений для заметок и code completion.

Гибрид Edge-Cloud
Локальная модель обрабатывает типовые запросы, а для сложных вопросов используется cloud model. Это даёт лучшее из двух миров — скорость и приватность в большинстве случаев, возможности облака для пограничных сценариев.

Распределённый inference (Multi-GPU)
Для более крупных моделей распределяйте слои между несколькими GPU (tensor parallelism) или делите контекст между устройствами (pipeline parallelism). Используйте llama.cpp с -ngl или ExLlamaV2 с --num-gpu-layers.

Мобильное развёртывание
Android: Use llama.cpp via JNI bindings or ML Kit.

iOS: Use llama.cpp via Swift bindings or mlx.

Web: Use WebLLM (runs on WebGPU via ONNX runtime) or transformers.js.

Оптимизация производительности
Flash Attention
Ускоряет вычисление attention и снижает потребление памяти. Доступен в llama.cpp, ExLlamaV2 и современных библиотеках transformers.

Batch inference
Обрабатывайте несколько prompt'ов за один forward pass. Это резко повышает throughput. Используйте llama-batch или vLLM.

Early Stopping / Token Budgeting
Задавайте максимальный бюджет tokens, чтобы предотвратить неограниченную генерацию.

Speculative Decoding
Используйте маленькую быструю draft-модель для предсказания tokens, а затем параллельно проверяйте их большой моделью. Это может дать ускорение в 2–3×.

Практическое руководство по настройке
1. Установите Ollama
bash
curl -fsSL https://ollama.com/install.sh | sh
2. Загрузите модель
bash
ollama pull phi3:3.8b-q4_K_M
3. Запустите через API
bash
ollama serve
Затем отправляйте запросы на http://localhost:11434/api/generate.

4. Интеграция с Python
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Альтернатива) Используйте llama.cpp напрямую
bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
Мониторинг и наблюдаемость
Отслеживайте загрузку GPU (nvidia-smi на Linux, Activity Monitor на macOS).

Отслеживайте использование памяти (RAM и VRAM).

Отслеживайте tokens per second (throughput).

Отслеживайте time to first token (latency).

Используйте встроенное логирование из llama.cpp или Ollama.

Ограничения и компромиссы
Разрыв в качестве: Небольшие локальные модели (3.8B–7B) обычно уступают крупным облачным моделям (GPT-4, Claude 3.5) в сложных задачах рассуждения.

Knowledge cutoff: Знания модели зафиксированы на момент обучения; используйте RAG, чтобы добавлять актуальную информацию.

Мультиязычность: У небольших моделей мультиязычные возможности могут быть слабее.

Использование инструментов: Agentic workflows (function calling) могут быть менее надёжны на маленьких моделях.

Для многих повседневных задач (summarisation, Q&A, code completion, classification) локальных моделей уже достаточно, и они быстро улучшаются.

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
