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
#الثغرات الأمنية
تعمل هذه الوثيقة على دمج الثغرات الأمنية الشائعة في تطوير البرمجيات، بما في ذلك هجمات الحقن وممارسات التعليمات البرمجية غير الآمنة والأخطاء الأمنية.
---

## حقن SQL
تحدث هجمات حقن SQL عندما تتم معالجة مدخلات المستخدم غير الموثوق بها بشكل غير صحيح في استعلامات قاعدة البيانات، مما يسمح للمهاجمين بالتلاعب بمنطق الاستعلام، أو الوصول إلى البيانات غير المصرح بها، أو تعديل محتويات قاعدة البيانات.
### الحقن الكلاسيكي المعتمد على UNION
**مثال سيء (رمز الضعف):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**هجوم:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**لماذا هو سيء:**
- يعرض البيانات من الجداول الأخرى
- يتجاوز منطق الاستعلام المقصود
- يمكن استخراج المعلومات الحساسة
** نهج أفضل: **```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### استراتيجيات الوقاية
1. **استخدام الاستعلامات ذات المعلمات**: لا تقم أبدًا بتسلسل إدخال المستخدم في SQL
2. **التحقق من صحة الإدخال**: التحقق من صحة جميع مدخلات المستخدم وتعقيمها
3. **الامتياز الأقل**: يجب أن تتمتع حسابات قاعدة البيانات بالحد الأدنى من الأذونات
4. **استخدام ORM**: استخدم مصممي الخرائط المرتبطين بالكائنات الذين يتعاملون مع الهروب
5. **جدران حماية تطبيقات الويب**: انشر WAFs لاكتشاف محاولات الحقن
---

## البرمجة النصية عبر المواقع (XSS)
تحدث هجمات البرمجة النصية عبر المواقع (XSS) عندما يقوم المهاجمون بإدخال نصوص برمجية ضارة في صفحات الويب التي يشاهدها المستخدمون الآخرون.
### XSS المنعكس
**مثال سيء (رمز الضعف):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**هجوم:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**لماذا هو سيء:**
- يتم تقديم إدخال المستخدم مباشرة بدون تشفير
- يمكن للمهاجم إنشاء عناوين URL ضارة
- اختطاف الجلسة، وسرقة بيانات الاعتماد ممكنة
** نهج أفضل: **```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS المخزنة
**مثال سيء:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### استراتيجيات الوقاية
1. **ترميز الإخراج**: تشفير البيانات بناءً على السياق (HTML، JS، URL، CSS)
2. **التحقق من صحة الإدخال**: رفض المدخلات الضارة أو تنظيفها
3. **سياسة أمان المحتوى**: استخدم رؤوس CSP لتقييد مصادر البرامج النصية
4. ** ملفات تعريف الارتباط الخاصة بـ HTTP فقط **: منع وصول JavaScript إلى ملفات تعريف الارتباط الخاصة بالجلسة
5. **الأطر الحديثة**: استخدم React وVue وAngular التي يتم الهروب منها تلقائيًا بشكل افتراضي
---

## مشكلات تتعلق بسلامة الذاكرة
### تجاوز سعة المخزن المؤقت
**مثال سيء (ج):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**المشاكل:**
- يمكن الكتابة فوق الذاكرة المجاورة
- قد يسمح بهجمات تنفيذ التعليمات البرمجية
- يسبب سلوكًا غير محدد
** نهج أفضل: **```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### الاستخدام بعد ذلك مجانًا
**مثال سيء (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

** نهج أفضل: **```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### استراتيجيات الوقاية
1. **استخدام اللغات الآمنة**: تفضل Rust وGo وJava وPython على C/C++
2. **المؤشرات الذكية**: استخدم أنماط RAII في لغة C++
3. **فحص الحدود**: التحقق دائمًا من صحة مؤشرات المصفوفة
4. **التحليل الثابت**: استخدم أدوات مثل Valgrind وAddressSanitizer
5. **واجهات برمجة التطبيقات الآمنة للذاكرة**: استخدم وظائف المكتبة القياسية الأكثر أمانًا
---

## أخطاء في المصادقة
### سياسات كلمات المرور الضعيفة
**مثال سيء:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**المشاكل:**
- عرضة لهجمات القوة الغاشمة
- كلمات المرور الشائعة يمكن تخمينها بسهولة
- ينتهك أفضل الممارسات الأمنية
** نهج أفضل: **```python
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

### تخزين كلمات مرور النص العادي
**مثال سيء:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

** نهج أفضل: **```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### استراتيجيات الوقاية
1. **التجزئة القوية**: استخدم bcrypt أو Argon2 أو scrypt لكلمات المرور
2. **المصادقة المتعددة العوامل**: تتطلب عملية تحقق إضافية
3. ** تحديد المعدل **: منع هجمات القوة الغاشمة
4. **تأمين الحساب**: قفل مؤقت بعد المحاولات الفاشلة
5. **إدارة الجلسة الآمنة**: استخدم ملفات تعريف الارتباط الآمنة المخصصة لـ HTTP فقط
---

## أخطاء أمنية أخرى
### الأسرار المشفرة
**مثال سيء:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

** نهج أفضل: **```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### مراجع الكائنات المباشرة غير الآمنة
**مثال سيء:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

** نهج أفضل: **```python
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

### الحد من المعدل المفقود
**مثال سيء:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

** نهج أفضل: **```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## موضوعات ذات صلة
- **فشل AI/LLM**: راجع`ai_llm_failures.md`للتعرف على المشكلات الأمنية الخاصة بالذكاء الاصطناعي والحقن الفوري
- **أنماط التعليمات البرمجية غير الآمنة**: راجع أمثلة التعليمات البرمجية لسلامة الذاكرة والسلوك غير المحدد
- **أفضل ممارسات المصادقة**: تنفيذ تدفقات المصادقة المناسبة وإدارة الجلسة
- **جودة الكود**: راجع`code_quality_issues.md`للتعرف على ممارسات البرمجة الآمنة
---

## ثغرات أمنية إضافية
### حقن الأوامر
**ما هو:** تنفيذ أوامر النظام التعسفية من خلال إدخال المستخدم غير المعقم.
**مثال سيء (رمز الضعف):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**هجوم:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**لماذا هو سيء:**
- يمكن للمهاجم تنفيذ أي أمر من أوامر النظام
- إمكانية اختراق النظام بالكامل
- تدمير البيانات، وإمكانية تثبيت البرامج الضارة
** نهج أفضل: **```python
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

### اجتياز المسار
**ما هو:** الوصول إلى الملفات خارج الدلائل المقصودة باستخدام ../ التسلسلات.
**مثال سيء:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**هجوم:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

** نهج أفضل: **```python
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

### تزوير الطلب من جانب الخادم (SSRF)
**ما هو:** جعل الخادم يقدم طلبات إلى وجهات غير مقصودة.
**مثال سيء:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**هجوم:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

** نهج أفضل: **```python
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

## أخطاء التشفير
### خوارزميات التجزئة الضعيفة
**مثال سيء:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**لماذا هو سيء:**
- تم كسر تشفير MD5 وSHA1
- سريع في الحساب (يتيح القوة الغاشمة)
- أظهرت هجمات الاصطدام
** نهج أفضل: **```python
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

### مفاتيح التشفير المشفرة
**مثال سيء:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

** نهج أفضل: **```python
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

### استخدام وضع البنك المركزي الأوروبي
**مثال سيء:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**لماذا هو سيء:**
- تنتج كتل النص العادي المتطابقة نصًا مشفرًا متطابقًا
- الأنماط في البيانات مرئية
- "بطريق البنك المركزي الأوروبي" الشهير يوضح المشكلة
** نهج أفضل: **```python
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

## مشكلات أمان واجهة برمجة التطبيقات
### التحقق من صحة الإدخال مفقود
**مثال سيء:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

** نهج أفضل: **```python
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

### مصادقة واجهة برمجة التطبيقات غير الآمنة
**مثال سيء:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

** نهج أفضل: **```python
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

### تحديد المعدل المفقود على واجهات برمجة التطبيقات
**مثال سيء:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

** نهج أفضل: **```python
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

## رؤوس الأمان والتكوين
### رؤوس الأمان المفقودة
**مثال سيء:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

** نهج أفضل: **```python
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

### تكوين CORS غير آمن
**مثال سيء:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

** نهج أفضل: **```python
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

## دراسات الحالة
### دراسة الحالة 1: خرق بيانات Equifax (2017)
**الحادثة:** استغل المهاجمون ثغرة Apache Struts للوصول إلى البيانات الشخصية لـ 147 مليون شخص.
**السبب الجذري:**
- برنامج غير مُصحح (CVE-2017-5638)
- لا يوجد التحقق من صحة الإدخال في رأس نوع المحتوى
- تجزئة الشبكة غير كافية
**التأثير:**
- 1.4 مليار دولار تكاليف
- البيانات الشخصية المكشوفة (رقم الضمان الاجتماعي وتواريخ الميلاد والعناوين)
- ضرر كبير بالسمعة
**الدرس:** حافظ على تحديث التبعيات؛ تنفيذ الدفاع في العمق.
### دراسة الحالة 2: خرق الهدف (2013)
**الحادث:** سرق المهاجمون 40 مليون رقم بطاقة ائتمان.
**السبب الجذري:**
- اختراق بيانات اعتماد بائع الطرف الثالث
- لا يوجد تجزئة للشبكة بين البائع وأنظمة الدفع
- تجاهل التنبيهات الأمنية
**التأثير:**
- 202 مليون دولار تكاليف
- تم طرد الرئيس التنفيذي ورئيس قسم المعلومات
- يلزم إجراء إصلاح شامل لنظام الدفع
**الدرس:** الشبكات المقطعية؛ مراقبة وصول الطرف الثالث؛ الرد على التنبيهات.
### دراسة الحالة 3: هجوم سلسلة توريد SolarWinds (2020)
**الحادث:** أثرت تعليمات برمجية ضارة تم إدخالها في تحديثات البرامج على أكثر من 18000 مؤسسة.
**السبب الجذري:**
- نظام البناء المخترق
- تحديثات ضارة موقعة بشهادات صالحة
- الحركة الجانبية مرة واحدة داخل الشبكات
**التأثير:**
- الوكالات الحكومية للخطر
- تأثرت شركات فورتشن 500
- التحقيق المستمر والعلاج
**الدرس:** بناء خطوط أنابيب آمنة؛ التحقق من سلامة البرمجيات؛ بنية الثقة الصفرية.
---

## استراتيجيات اختبار الأمان
### اختبار أمان التطبيقات الثابتة (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### اختبار أمان التطبيقات الديناميكية (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### فحص التبعية
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### قائمة التحقق من اختبار الاختراق
- [ ] اختبار حقن SQL
- [ ] اختبار XSS (المنعكس والمخزن والمعتمد على DOM)
- [ ] التحقق من صحة رمز CSRF
- [ ] محاولات تجاوز المصادقة
- [ ] فحص التفويض (تصعيد الامتيازات عموديًا/أفقيًا)
- [ ] التحقق من الحد من المعدل
- [ ] وجود رؤوس الأمان
- [ ] تكوين SSL/TLS
- [ ] مراجعة إدارة الجلسة
- [ ] معالجة الأخطاء (عدم تسرب المعلومات)
---

## الموارد الأمنية
### أفضل 10 OWASP (2021)
1. التحكم في الوصول مكسور
2. فشل التشفير
3. الحقن
4. التصميم غير الآمن
5. التكوين الخاطئ للأمان
6. المكونات الضعيفة والقديمة
7. فشل تحديد الهوية والمصادقة
8. فشل سلامة البرامج والبيانات
9. فشل التسجيل والمراقبة الأمنية
10. تزوير الطلب من جانب الخادم
### الأدوات الموصى بها
- **التحليل الثابت**: SonarQube، Semgrep، CodeQL
- **مسح التبعية**: Dependabot، Renovate، Snyk
- **الاختبار الديناميكي**: OWASP ZAP، Burp Suite
- **الكشف السري**: GitLeaks، TruffleHog
- **أمن الحاويات**: تريفي، كلير، أنكور