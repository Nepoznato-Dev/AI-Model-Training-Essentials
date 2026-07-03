# Архитектура локального AI

Практическое руководство по запуску больших языковых моделей полностью на устройстве — аппаратные требования, inference-движки, оптимизация памяти и проектирование систем для edge deployment.

---

## Зачем запускать AI локально?

- **Privacy**: данные не покидают устройство.
- **Cost**: никаких API-платежей за token.
- **Latency**: предсказуемый inference без зависимости от сети.
- **Offline availability**: работает без интернета.
- **Control**: полный контроль над версией модели, кастомизацией и fine-tuning.

---

## Аппаратные требования

### Память GPU (VRAM)
Самый критичный ресурс. Размер модели в памяти ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Практические рекомендации:**
- 8GB VRAM → до 7B-моделей в 4-bit.
- 12GB VRAM → до 13B-моделей в 4-bit.
- 24GB VRAM → до 70B-моделей в 4-bit (или 13B в 8-bit).
- Apple Silicon (unified memory) может запускать 70B-модели на системах с 64GB+ памяти.

### RAM (System Memory)
- Для CPU inference требуется достаточно системной RAM, чтобы загрузить модель (примерно на том же уровне, что и VRAM).
- Для GPU inference системная RAM важна для загрузки модели в память перед выгрузкой в VRAM.

### Storage
- Квантованные веса модели занимают несколько GB (например, 4-bit 7B ≈ 4 GB на диске). Для нескольких моделей стоит иметь как минимум 20–50 GB свободного места.

### CPU
- Для обработки prompt на этапе prefill и CPU-offloading полезен современный многоядерный CPU.
- Чипы Apple M-series отлично подходят для LLMs благодаря unified memory и Neural Engine.

---

## Квантование

Квантование уменьшает числовую точность весов, резко снижая потребление памяти и повышая скорость ценой небольшой потери точности.

### Популярные форматы

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | формат llama.cpp, оптимизированный для гибридного CPU/GPU | Лучший вариант для локального inference |
| **GPTQ** | 4–8 | только для GPU, эффективен на CUDA | Лучший вариант для NVIDIA GPUs |
| **AWQ** | 4 | учитывает активации, только для GPU | Хорошо подходит для batch inference на GPU |
| **ONNX** | variable | стандартизованный, кроссплатформенный | Production serving |

### Выбор уровня квантования
- **Q8_0** (8-bit): минимальная потеря качества, самый большой размер.
- **Q6_K** (6-bit): хорошее качество, достойное сжатие.
- **Q5_K_M** (5-bit): распространённый оптимальный баланс.
- **Q4_K_M** (4-bit): минимальный размер и приемлемое качество для большинства задач.
- **IQ4_XS** / **IQ3_XS**: улучшенное квантование с лучшей perplexity при 4/3 битах.

**Общее правило:** используйте Q4_K_M как хороший баланс качества и размера. Если VRAM с запасом, выбирайте Q5 или Q6.

---

## Inference-движки (локальные)

### llama.cpp
- Написан на C++.
- Поддерживает формат GGUF.
- Оптимизирован для CPU и GPU (через CUDA, Metal, OpenCL).
- Очень быстрый, особенно на CPU.
- Имеет command-line интерфейс, server mode и Python bindings.

**Example command:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 выгружает 32 слоя на GPU)

Ollama
Предоставляет оболочку над llama.cpp с простым CLI и REST API.

Автоматически загружает модели и управляет ими.

Отлично подходит для прототипирования и desktop-приложений.

Поддерживает пользовательские Modelfiles для system prompts.

Usage:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Графическое desktop-приложение для Windows, macOS и Linux.

Загрузка моделей и чат-интерфейс в один клик.

Встроенный локальный сервер с OpenAI-compatible API.

Хорошо подходит для нетехнических пользователей и быстрого тестирования.

Hugging Face Transformers + bitsandbytes
Стандартная Python-библиотека для HF-моделей.

Используйте bitsandbytes для 4-bit квантования (load_in_4bit=True).

Более гибка для fine-tuning, но для inference медленнее, чем llama.cpp.

ExLlamaV2
Очень быстрый GPU inference для GPTQ и AWQ.

Лучшая производительность на NVIDIA GPUs.

Поддерживает batched generation.

mlx (Apple)
Фреймворк Apple для чипов M-series.

Сильно оптимизирован для Apple Silicon.

Python API.

Управление памятью
Context Window and KV Cache
KV cache хранит пары key-value для каждого слоя и каждого token в контексте. Он растёт линейно вместе с длиной контекста.

Memory cost ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

Для 32-слойной модели с 8 KV heads и 128 head dim каждый token стоит ~32 × 8 × 128 × 2 bytes = 65 KB на token. Для 128k tokens это ~8 GB только на cache.

Offloading Strategies
Layer offloading: часть слоёв размещается на GPU, остальные на CPU. Быстрее, чем чистый CPU, и требует меньше VRAM.

Token streaming: tokens обрабатываются постепенно, а не все сразу.

Prompt Caching
Повторно используйте KV caches для схожих prompts, чтобы не пересчитывать фазу prefill. Некоторые фреймворки это поддерживают (например, vLLM, llama.cpp с --prompt-cache).

Memory-Mapped Files
Загружайте веса модели напрямую с диска, не помещая их полностью в RAM (это полезно для огромных моделей на системах с ограниченной памятью). llama.cpp по умолчанию использует memory-mapping.

Deployment Architectures
Single-Device Mode
Одна модель работает на одной машине (ноутбук, смартфон, edge device). Используется для персональных ассистентов, приложений для заметок, code completion.

Hybrid Edge-Cloud
Локальная модель обрабатывает обычные запросы; для сложных вопросов используется cloud fallback. Это сочетает преимущества обоих подходов — скорость и приватность для большинства случаев, возможности облака для сложных сценариев.

Distributed Inference (Multi-GPU)
Для более крупных моделей слои распределяются по нескольким GPU (tensor parallelism) или контекст делится между устройствами (pipeline parallelism). Используйте llama.cpp с -ngl или ExLlamaV2 с --num-gpu-layers.

Mobile Deployment
Android: используйте llama.cpp через JNI bindings или ML Kit.

iOS: используйте llama.cpp через Swift bindings или mlx.

Web: используйте WebLLM (работает на WebGPU через ONNX runtime) или transformers.js.

Performance Optimisation
Flash Attention
Ускоряет вычисление attention и уменьшает потребление памяти. Доступен в llama.cpp, ExLlamaV2 и современных библиотеках transformers.

Batch Inference
Обрабатывайте несколько prompts за один forward pass. Это резко повышает throughput. Используйте llama-batch или vLLM.

Early Stopping / Token Budgeting
Задавайте максимальный budget по tokens, чтобы избежать неограниченной генерации.

Speculative Decoding
Используйте маленькую быструю модель (draft) для предсказания tokens, а затем параллельно проверяйте их большой моделью. Это может дать ускорение в 2–3×.

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
Затем отправляйте запросы на http://localhost:11434/api/generate.

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
Мониторинг и наблюдаемость
Отслеживайте загрузку GPU (nvidia-smi в Linux, Activity Monitor в macOS).

Отслеживайте использование памяти (RAM и VRAM).

Отслеживайте tokens per second (throughput).

Отслеживайте time to first token (latency).

Используйте встроенное логирование llama.cpp или Ollama.

Ограничения и компромиссы
Разрыв в качестве: небольшие локальные модели (3.8B–7B) обычно уступают крупным облачным моделям (GPT-4, Claude 3.5) в сложных задачах на рассуждение.

Knowledge cutoff: знания модели зафиксированы на момент обучения; используйте RAG для добавления актуальной информации.

Multilingual: у меньших моделей может быть слабее поддержка многих языков.

Tool use: agentic workflows (function calling) на небольших моделях могут работать менее надёжно.

Для многих повседневных задач (summarisation, Q&A, code completion, classification) локальных моделей уже достаточно, и они быстро улучшаются.

text

---

## File 4: `security_best_practices.md`

```markdown
# Лучшие практики безопасности

Практическое руководство по защите приложений, инфраструктуры и данных — от разработки до production.

---

## OWASP Top 10 (2021) — Обзор

1. **Broken Access Control**: пользователи могут получать доступ к ресурсам, к которым не должны иметь доступа.
2. **Cryptographic Failures**: слабое или отсутствующее шифрование.
3. **Injection**: SQL, NoSQL, OS command или LDAP injection.
4. **Insecure Design**: архитектурные недостатки.
5. **Security Misconfiguration**: пароли по умолчанию, открытые порты, слишком подробные сообщения об ошибках.
6. **Vulnerable and Outdated Components**: известные CVE в зависимостях.
7. **Identification and Authentication Failures**: слабые пароли, ошибки управления сессиями.
8. **Software and Data Integrity Failures**: атаки на supply chain, неподписанные обновления.
9. **Security Logging and Monitoring Failures**: отсутствие обнаружения инцидентов.
10. **Server-Side Request Forgery (SSRF)**: злоупотребление сервером для отправки запросов во внутренние системы.

---

## Проверка входных данных и кодирование вывода

### Правила валидации
- **Whitelist > Blacklist**: задавайте допустимые шаблоны (например, regex для email), а не блокируйте только известные плохие варианты.
- **Length limits**: ограничивайте максимальную длину, чтобы предотвращать buffer overflow и DoS.
- **Type checking**: проверяйте, что integers действительно integers, а booleans — booleans.
- **Use well-tested libraries**: для проверки email, URL и дат используйте стандартные библиотеки (например, `email-validator` в Python, `validator.js` в Node).

### Кодирование вывода
- **HTML encoding**: кодируйте `<`, `>`, `&`, `"`, `'`, чтобы предотвратить XSS.
- **SQL parameterisation**: никогда не конкатенируйте пользовательский ввод в SQL-запросы. Используйте parameterised queries (prepared statements) или ORM.
- **Shell escaping**: избегайте построения shell-команд из пользовательского ввода; если это неизбежно, используйте `shlex.quote()` или аналогичный механизм.

---

## Authentication и Authorisation

### Управление паролями
- **Hashing**: храните пароли с использованием сильного и медленного алгоритма хеширования: **Argon2id** (предпочтительно), **bcrypt**, **scrypt** или **PBKDF2**.
- **Salting**: добавляйте уникальную salt для каждого пользователя.
- **Minimum length**: требуйте минимум 12–16 символов.
- **MFA (Multi-Factor Authentication)**: требуйте второй фактор (TOTP, SMS, hardware key) для чувствительных операций.
- **Rate limiting**: предотвращайте brute-force атаки на endpoints входа (например, 5 попыток за 5 минут на IP/пользователя).

### Управление сессиями
- Используйте безопасные HTTP-only cookies с SameSite для session tokens.
- Устанавливайте корректные сроки действия.
- Инвалидируйте сессии при logout и при смене пароля.
- Не раскрывайте session IDs в URL.

### OAuth2 / OIDC
- Используйте зрелые библиотеки (например, Authlib, PyJWT, Passport.js, Spring Security).
- Тщательно валидируйте ID tokens (signature, issuer, audience, expiration).
- Используйте параметры state для предотвращения CSRF.
- Держите client secrets в тайне.

### JWT (JSON Web Tokens)
- **Sign**: используйте RS256 или ES256 (асимметричные) для лучшей безопасности; HS256 (симметричный) допустим, если shared secrets хорошо управляются.
- **Validate**: всегда проверяйте signature, issuer (`iss`), audience (`aud`) и expiration (`exp`).
- **Keep short expiration**: 15–60 минут для access tokens; для более длинных сессий используйте refresh tokens.
- **Store securely**: никогда не храните JWT в localStorage (уязвимо к XSS); вместо этого используйте HTTP-only cookies.

---

## Безопасность API

### Authentication
- Всегда аутентифицируйте API-вызовы (кроме публичных endpoints).
- Предпочитайте API keys или OAuth2 tokens вместо basic auth (который отправляет credentials в каждом запросе).

### Rate Limiting и Throttling
- Применяйте ограничения по пользователю и по IP, чтобы предотвращать злоупотребления и DoS.
- Возвращайте `429 Too Many Requests` с заголовком `Retry-After`.

### CORS (Cross-Origin Resource Sharing)
- Разрешайте только конкретные origins (никогда не `*` в production).
- Валидируйте заголовок `Origin` на стороне сервера.

### Input Validation
- Проверяйте все параметры запроса, включая headers и body.
- Отклоняйте неожиданные поля (`"strict": true` или `additionalProperties: false` в JSON Schema).

### HTTPS / TLS
- В production принудительно используйте HTTPS.
- Используйте HSTS (HTTP Strict Transport Security), чтобы заставить браузеры работать только через HTTPS.
- Используйте TLS 1.2 или 1.3 (отключите TLS 1.0/1.1).

---

## Управление секретами

### Never Hardcode Secrets
- Не коммитьте secrets (API keys, passwords, database URLs) в source control.
- Используйте environment variables или инструменты управления секретами.

### Tools
- **HashiCorp Vault**: enterprise-grade решение с динамическими secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: cloud-native варианты.
- **SOPS**: шифрует secrets в файлах и позволяет коммитить их (с KMS или GPG).
- **Docker secrets**: для режима Swarm; Kubernetes secrets (закодированы в base64, поэтому используйте осторожно; можно рассмотреть внешний Secrets Store CSI driver).

### Rotation
- Регулярно ротируйте secrets и service accounts.
- По возможности автоматизируйте rotation.

---

## Управление зависимостями

### Сканирование уязвимостей
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Patching
- Поддерживайте зависимости в обновлённом состоянии с установленными исправлениями.
- Настройте автоматические pull request для minor/patch обновлений.
- Проверяйте changelog на breaking changes.

### Supply Chain Integrity
- Используйте lockfiles пакетов (`package-lock.json`, `Cargo.lock`, `go.sum`) для воспроизводимых сборок.
- Проверяйте checksums скачанных зависимостей.
- Предпочитайте официальные registries и доверяйте только проверенным publishers.

---

## Безопасность инфраструктуры

### Firewalls
- Блокируйте все входящие порты, кроме явно необходимых (например, 80, 443).
- Ограничивайте доступ по SSH конкретными диапазонами IP (или используйте VPN/bastion host).
- Используйте security groups (AWS) или NSGs (Azure) для точного контроля доступа.

### OS Hardening
- Регулярно устанавливайте security updates (`sudo apt upgrade`, `yum update`).
- Отключайте ненужные службы и учётные записи по умолчанию.
- Используйте fail2ban для блокировки brute-force попыток по SSH.
- Усиливайте SSH: отключайте root login, используйте key-based auth, при необходимости меняйте порт по умолчанию.

### Network Segmentation
- Размещайте databases и caches в приватных подсетях без доступа в интернет.
- Используйте DMZ для публичных сервисов.
- Применяйте принцип наименьших привилегий к сетевому доступу.

### Secrets in Infrastructure
- Никогда не храните secrets в переменных окружения CI/CD без шифрования.
- Используйте IAM roles облачного провайдера для EC2/VM instances вместо долгоживущих ключей.

---

## Logging и Monitoring

### Что логировать
- События аутентификации (успех/ошибка).
- Решения контроля доступа (ошибки authorisation).
- Действия администраторов (создание пользователей, удаление, изменение прав).
- Изменения схемы database.
- Системные ошибки и exceptions.
- API requests и responses (с маскированием чувствительных данных).

### Что не логировать
- Пароли, secrets, tokens, PII (Personal Identifiable Information), если они не захешированы/не замаскированы.
- Полные номера банковских карт.

### Alerting
- Настройте оповещения для:
  - множественных неудачных попыток входа (возможный brute force).
  - необычных паттернов доступа (например, из новых локаций или в необычное время).
  - создания новых admin accounts.
  - высокого уровня ошибок или скачков latency.
- Используйте SIEM (Security Information and Event Management) для продвинутой корреляции.

### Хранение логов
- Храните логи не менее 30–90 дней в зависимости от регуляторных требований.
- Держите логи в централизованной tamper-evident системе (например, ELK Stack, Splunk, Datadog).

---

## Secure Development Lifecycle (SDL)

1. **Training**: убедитесь, что разработчики понимают распространённые уязвимости.
2. **Threat modelling**: выявляйте потенциальные угрозы на раннем этапе проектирования.
3. **Secure coding standards**: обеспечивайте соблюдение через linters и checklists code review.
4. **SAST** (Static Application Security Testing): сканируйте source code на уязвимости (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): сканируйте работающие приложения (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): сканируйте зависимости.
7. **Penetration testing**: регулярно проводите этичные проверки на проникновение.
8. **Bug bounty**: поощряйте внешних исследователей ответственно находить уязвимости.
9. **Incident response plan**: подготовьте чёткий план действий на случай обнаружения инцидента.

---

## Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — но действуйте быстро.
2. **Isolate** затронутые системы (при необходимости отключите их от сети).
3. **Preserve evidence**: сохраните логи, дампы памяти и образы дисков.
4. **Identify** масштаб: какие системы и какие данные затронуты.
5. **Rotate** все скомпрометированные credentials и secrets.
6. **Patch** уязвимость.
7. **Notify** затронутых пользователей и регуляторов, если это требуется (в установленные законом сроки).
8. **Conduct a post-mortem** для понимания первопричины и улучшения процессов.
