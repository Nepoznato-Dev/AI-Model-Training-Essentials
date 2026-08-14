---
# Metadata
title: "Security Vulnerabilities"
description: "Common security vulnerabilities"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [security, vulnerabilities, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "34 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Уязвимости безопасности
В этом документе собраны общие уязвимости безопасности при разработке программного обеспечения, включая атаки путем внедрения, небезопасные методы написания кода и ошибки безопасности.
---

## SQL-инъекция
Атаки с помощью SQL-инъекций происходят, когда ненадежный пользовательский ввод неправильно обрабатывается в запросах к базе данных, что позволяет злоумышленникам манипулировать логикой запроса, получать доступ к неавторизованным данным или изменять содержимое базы данных.
### Классическая инъекция на основе UNION
**Плохой пример (уязвимый код):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Атака:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Почему это плохо:**
- Предоставляет данные из других таблиц
- Обходит предполагаемую логику запроса.
- Может извлекать конфиденциальную информацию
**Лучший подход:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Стратегии профилактики
1. **Используйте параметризованные запросы**: никогда не объединяйте пользовательский ввод в SQL.
2. **Проверка ввода**: проверка и очистка всех вводимых пользователем данных.
3. **Наименьшие права**: учетные записи базы данных должны иметь минимальные разрешения.
4. **Использование ORM**: используйте объектно-реляционные преобразователи, которые обрабатывают экранирование.
5. **Брандмауэры веб-приложений**: разверните WAF для обнаружения попыток внедрения.
---

## Межсайтовый скриптинг (XSS)
Атаки с использованием межсайтовых сценариев (XSS) происходят, когда злоумышленники внедряют вредоносные сценарии в веб-страницы, просматриваемые другими пользователями.
### Отраженный XSS
**Плохой пример (уязвимый код):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Атака:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Почему это плохо:**
- Пользовательский ввод отображается напрямую без кодирования.
- Злоумышленник может создавать вредоносные URL-адреса.
- Перехват сеанса, возможна кража учетных данных
**Лучший подход:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Сохраненный XSS
**Плохой пример:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Стратегии профилактики
1. **Кодирование вывода**: кодируйте данные на основе контекста (HTML, JS, URL, CSS).
2. **Проверка ввода**: отклонение или очистка вредоносного ввода.
3. **Политика безопасности контента**: используйте заголовки CSP для ограничения источников сценариев.
4. **HTTPOnly Cookies**: запретить доступ JavaScript к файлам cookie сеанса.
5. **Современные фреймворки**: используйте React, Vue, Angular, которые по умолчанию автоматически экранируются.
---

## Проблемы безопасности памяти
### Переполнение буфера
**Плохой пример (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Проблемы:**
- Может перезаписывать соседнюю память
- Может допускать атаки на выполнение кода.
- Вызывает неопределенное поведение
**Лучший подход:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Использование после бесплатного использования
**Плохой пример (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Лучший подход:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Стратегии профилактики
1. **Используйте безопасные языки**: предпочитайте Rust, Go, Java, Python C/C++.
2. **Умные указатели**: используйте шаблоны RAII в C++.
3. **Проверка границ**: всегда проверяйте индексы массива.
4. **Статический анализ**: используйте такие инструменты, как Valgrind, AddressSanitizer.
5. **API, безопасные для памяти**: используйте более безопасные функции стандартной библиотеки.
---

## Ошибки аутентификации
### Слабые политики паролей
**Плохой пример:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Проблемы:**
- Подвержен атакам методом грубой силы.
- Общие пароли легко угадываются
- Нарушает лучшие практики безопасности.
**Лучший подход:**```python
import re

def is_strong_password(password):
    """Enforce strong password requirements."""
    if len(password) < 12:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*]', password):
        return False
    return True
```

### Хранение паролей в виде открытого текста
**Плохой пример:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Лучший подход:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Стратегии профилактики
1. **Сильное хеширование**: используйте bcrypt, Argon2 или scrypt для паролей.
2. **Многофакторная аутентификация**: требуется дополнительная проверка.
3. **Ограничение скорости**: предотвращение атак методом перебора.
4. **Блокировка учетной записи**: временная блокировка после неудачных попыток.
5. **Безопасное управление сеансами**: используйте безопасные файлы cookie только для HTTP.
---

## Другие ошибки безопасности
### Жестко закодированные секреты
**Плохой пример:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Лучший подход:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Небезопасные прямые ссылки на объекты
**Плохой пример:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Лучший подход:**```python
def get_document(doc_id, current_user):
    doc = db.query(
        "SELECT * FROM documents WHERE id = ? AND owner_id = ?",
        doc_id,
        current_user.id
    )
    if not doc:
        raise PermissionError("Document not found")
    return doc
```

### Отсутствует ограничение скорости
**Плохой пример:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Лучший подход:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Похожие темы
- **Ошибки AI/LLM**: см.`ai_llm_failures.md`для быстрого внедрения и проблем безопасности, связанных с AI.
- **Небезопасные шаблоны кода**: см. примеры кода для обеспечения безопасности памяти и неопределенного поведения.
– **Рекомендации по аутентификации**: внедрение правильных потоков аутентификации и управления сеансами.
- **Качество кода**: см.`code_quality_issues.md`для получения информации о методах безопасного кодирования.
---

## Дополнительные уязвимости безопасности
### Внедрение команд
**Что это такое:** Выполнение произвольных системных команд посредством несанкционированного пользовательского ввода.
**Плохой пример (уязвимый код):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Атака:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Почему это плохо:**
- Злоумышленник может выполнить любую системную команду
- Возможность полного компрометации системы.
- Уничтожение данных, возможна установка вредоносного ПО
**Лучший подход:**```python
# SAFE: Use subprocess with list arguments
import subprocess

def get_file_info(filename):
    result = subprocess.run(
        ["ls", "-la", filename],
        capture_output=True,
        text=True,
        check=False
    )
    return result.stdout
```

### Обход пути
**Что это такое:** Доступ к файлам за пределами предполагаемых каталогов с помощью последовательностей ../.
**Плохой пример:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Атака:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Лучший подход:**```python
import os
from pathlib import Path

def serve_file(filename):
    base_dir = Path("/var/www/files").resolve()
    requested_path = (base_dir / filename).resolve()
    
    # Ensure path is within base directory
    if not str(requested_path).startswith(str(base_dir)):
        raise PermissionError("Access denied")
    
    return requested_path.read_text()
```

### Подделка запросов на стороне сервера (SSRF)
**Что это такое:** сервер отправляет запросы к непредусмотренным местам назначения.
**Плохой пример:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Атака:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Лучший подход:**```python
from urllib.parse import urlparse
import ipaddress

def is_safe_url(url):
    parsed = urlparse(url)
    
    # Only allow HTTP/HTTPS
    if parsed.scheme not in ['http', 'https']:
        return False
    
    # Resolve hostname and check IP
    try:
        ip = socket.gethostbyname(parsed.hostname)
        ip_obj = ipaddress.ip_address(ip)
        
        # Block private/internal IPs
        if ip_obj.is_private or ip_obj.is_loopback:
            return False
        
        return True
    except:
        return False

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    if not is_safe_url(url):
        return "Invalid URL", 400
    response = requests.get(url)
    return response.text
```

---

## Криптографические ошибки
### Слабые алгоритмы хеширования
**Плохой пример:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Почему это плохо:**
- MD5 и SHA1 криптографически взломаны.
- Быстро вычислять (включает грубую силу)
- Продемонстрированы столкновения
**Лучший подход:**```python
import bcrypt
import argon2

# Use password-specific hashing functions
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

# Or use Argon2 (winner of Password Hashing Competition)
def hash_password_argon2(password):
    ph = argon2.PasswordHasher()
    return ph.hash(password)
```

### Жестко запрограммированные ключи шифрования
**Плохой пример:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Лучший подход:**```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# Derive key from password + salt
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())

# Store salt with encrypted data, derive key at runtime
salt = os.urandom(16)
key = derive_key(user_password, salt)
```

### Использование режима ECB
**Плохой пример:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Почему это плохо:**
- Идентичные блоки открытого текста создают идентичный зашифрованный текст.
- Видны закономерности в данных
- Знаменитый «пингвин ЕЦБ» демонстрирует проблему
**Лучший подход:**```python
# Use authenticated encryption modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_authenticated(data, key):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    return nonce + ciphertext  # Store nonce with ciphertext

def decrypt_authenticated(ciphertext, key):
    aesgcm = AESGCM(key)
    nonce = ciphertext[:12]
    data = ciphertext[12:]
    return aesgcm.decrypt(nonce, data, None)
```

---

## Проблемы безопасности API
### Отсутствует проверка ввода
**Плохой пример:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Лучший подход:**```python
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Integer(required=True, validate=validate.Range(min=1))
    email = fields.Email(required=True)
    username = fields.String(
        required=True,
        validate=[
            validate.Length(min=3, max=50),
            validate.Regexp(r'^[a-zA-Z0-9_]+$')
        ]
    )

@app.route('/api/user/<int:user_id>')  # Type constraint in route
def get_user(user_id):
    schema = UserSchema()
    validated = schema.load({'id': user_id})
    return db.get_user(validated['id'])
```

### Небезопасная аутентификация API
**Плохой пример:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Лучший подход:**```python
# Use Authorization header
import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
}
response = requests.get('/api/data', headers=headers)

# Or use API key in header
headers = {
    'X-API-Key': os.environ.get('API_KEY')
}
```

### Отсутствует ограничение скорости в API
**Плохой пример:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Лучший подход:**```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@app.route('/api/search')
@limiter.limit("10 per minute")
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)

# Different limits for different endpoints
@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")  # Stricter for login
def login():
    ...
```

---

## Заголовки безопасности и конфигурация
### Отсутствуют заголовки безопасности
**Плохой пример:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Лучший подход:**```python
from flask_talisman import Talisman

app = Flask(__name__)

# Configure security headers
Talisman(app, 
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
        'style-src': "'self'"
    },
    force_https=True,
    strict_transport_security=True,
    strict_transport_security_max_age=31536000
)

# Or manually add headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response
```

### Небезопасная конфигурация CORS
**Плохой пример:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Лучший подход:**```python
from flask_cors import CORS

# Configure specific allowed origins
CORS(app, 
    resources={
        r"/api/*": {
            "origins": ["https://trusted-domain.com"],
            "methods": ["GET", "POST"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    }
)
```

---

## Тематические исследования
### Пример 1: Утечка данных Equifax (2017 г.)
**Инцидент:** Злоумышленники воспользовались уязвимостью Apache Struts для доступа к личным данным 147 миллионов человек.
**Основная причина:**
- Непропатченное программное обеспечение (CVE-2017-5638).
- Нет проверки ввода в заголовке типа контента.
- Недостаточная сегментация сети
**Влияние:**
- Затраты в размере $1,4 млрд.
- Раскрыты персональные данные (SSN, даты рождения, адреса)
- Огромный репутационный ущерб.
**Урок:** постоянно обновляйте зависимости; реализовать глубокоэшелонированную оборону.
### Пример 2: Нарушение цели (2013 г.)
**Инцидент:** Злоумышленники украли 40 миллионов номеров кредитных карт.
**Основная причина:**
- Учетные данные стороннего поставщика скомпрометированы.
- Нет сегментации сети между вендорами и платежными системами.
- Игнорируются предупреждения безопасности
**Влияние:**
- 202 миллиона долларов затрат
- Генеральный директор и директор по информационным технологиям уволены
- Требуется капитальный ремонт платежной системы
**Урок:** сегментируйте сети; контролировать доступ третьих лиц; реагировать на оповещения.
### Пример 3: Атака на цепочку поставок SolarWinds (2020 г.)
**Инцидент:** Вредоносный код, добавленный в обновления программного обеспечения, затронул более 18 000 организаций.
**Основная причина:**
- Скомпрометированная система сборки
- Подписанные вредоносные обновления действительными сертификатами.
- Боковое перемещение внутри сетей
**Влияние:**
- Государственные учреждения скомпрометированы
- Пострадали компании из списка Fortune 500
- Текущее расследование и исправление ситуации.
**Урок:** Безопасные конвейеры сборки; проверить целостность программного обеспечения; архитектура нулевого доверия.
---

## Стратегии тестирования безопасности
### Статическое тестирование безопасности приложений (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Динамическое тестирование безопасности приложений (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Сканирование зависимостей
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Контрольный список тестирования на проникновение
- [ ] Тестирование SQL-инъекций
- [ ] XSS-тестирование (отраженное, сохраненное, на основе DOM)
- [ ] Проверка токена CSRF
- [ ] Попытки обхода аутентификации
- [ ] Проверки авторизации (вертикальное/горизонтальное повышение привилегий)
- [ ] Проверка ограничения скорости
- [ ] Наличие заголовков безопасности
- [ ] Конфигурация SSL/TLS
- [ ] Обзор управления сеансом
- [ ] Обработка ошибок (без утечки информации)
---

## Ресурсы по безопасности
### Топ-10 OWASP (2021 г.)
1. Нарушенный контроль доступа
2. Криптографические сбои
3. Инъекция
4. Небезопасный дизайн
5. Неправильная настройка безопасности
6. Уязвимые и устаревшие компоненты
7. Сбои идентификации и аутентификации
8. Нарушения целостности программного обеспечения и данных
9. Сбои ведения журнала безопасности и мониторинга
10. Подделка запросов на стороне сервера
### Рекомендуемые инструменты
- **Статический анализ**: SonarQube, Semgrep, CodeQL.
- **Сканирование зависимостей**: Dependabot, Renovate, Snyk.
- **Динамическое тестирование**: OWASP ZAP, Burp Suite.
- **Секретное обнаружение**: GitLeaks, TruffleHog.
- **Охрана контейнеров**: Триви, Клэр, Анкор.