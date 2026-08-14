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
# سیکیورٹی کے خطرات
یہ دستاویز سافٹ ویئر ڈیولپمنٹ میں سیکیورٹی کے عمومی کمزوریوں کو مضبوط کرتی ہے، بشمول انجیکشن حملے، کوڈ کے غیر محفوظ طریقے، اور سیکیورٹی کی غلطیاں۔
---

## ایس کیو ایل انجیکشن
ایس کیو ایل انجیکشن حملے اس وقت ہوتے ہیں جب ڈیٹا بیس کے سوالات میں ناقابل اعتماد صارف ان پٹ کو غلط طریقے سے ہینڈل کیا جاتا ہے، جس سے حملہ آور استفسار کی منطق میں ہیرا پھیری کرنے، غیر مجاز ڈیٹا تک رسائی، یا ڈیٹا بیس کے مواد میں ترمیم کرنے کی اجازت دیتے ہیں۔
### کلاسک یونین پر مبنی انجکشن
**بری مثال (خطرناک کوڈ):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**حملہ:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**یہ برا کیوں ہے:**
- دوسرے جدولوں سے ڈیٹا کو بے نقاب کرتا ہے۔
- مطلوبہ استفسار کی منطق کو نظرانداز کرتا ہے۔
- حساس معلومات نکال سکتے ہیں۔
**بہتر نقطہ نظر:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### روک تھام کی حکمت عملی
1. **پیرامیٹرائزڈ سوالات کا استعمال کریں**: کبھی بھی صارف کے ان پٹ کو SQL میں مت جوڑیں۔
2. **ان پٹ کی توثیق**: صارف کے تمام ان پٹ کی توثیق اور صفائی کریں۔
3. **کم سے کم استحقاق**: ڈیٹا بیس اکاؤنٹس کو کم سے کم اجازتیں ہونی چاہئیں
4. **ORM کا استعمال**: آبجیکٹ-ریلیشنل میپرز کا استعمال کریں جو فرار کو سنبھالتے ہیں
5. **ویب ایپلیکیشن فائر والز**: انجیکشن کی کوششوں کا پتہ لگانے کے لیے WAFs کو تعینات کریں
---

## کراس سائٹ اسکرپٹنگ (XSS)
کراس سائٹ اسکرپٹنگ (XSS) حملے اس وقت ہوتے ہیں جب حملہ آور دوسرے صارفین کے ذریعے دیکھے جانے والے ویب صفحات میں بدنیتی پر مبنی اسکرپٹ داخل کرتے ہیں۔
### عکاسی شدہ XSS
**بری مثال (خطرناک کوڈ):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**حملہ:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**یہ برا کیوں ہے:**
- صارف کا ان پٹ بغیر انکوڈنگ کے براہ راست پیش کیا گیا۔
- حملہ آور بدنیتی پر مبنی یو آر ایل تیار کر سکتا ہے۔
- سیشن ہائی جیکنگ، اسناد کی چوری ممکن ہے۔
**بہتر نقطہ نظر:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### ذخیرہ شدہ XSS
**بری مثال:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### روک تھام کی حکمت عملی
1. **آؤٹ پٹ انکوڈنگ**: سیاق و سباق کی بنیاد پر ڈیٹا کو انکوڈ کریں (HTML, JS, URL, CSS)
2. **ان پٹ کی توثیق**: نقصان دہ ان پٹ کو مسترد یا صاف کریں۔
3. **مواد کی حفاظت کی پالیسی**: سکرپٹ کے ذرائع کو محدود کرنے کے لیے CSP ہیڈر استعمال کریں۔
4. **HTTPOonly Cookies**: سیشن کوکیز تک جاوا اسکرپٹ کی رسائی کو روکیں۔
5. **جدید فریم ورک**: React، Vue، Angular کا استعمال کریں جو خود بخود بچ جائیں
---

## میموری کی حفاظت کے مسائل
### بفر اوور فلو
**بری مثال (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**مسائل:**
- ملحقہ میموری کو اوور رائٹ کر سکتے ہیں۔
- کوڈ پر عمل درآمد کے حملوں کی اجازت دے سکتا ہے۔
- غیر متعینہ سلوک کا سبب بنتا ہے۔
**بہتر نقطہ نظر:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### استعمال کے بعد مفت
**بری مثال (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**بہتر نقطہ نظر:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### روک تھام کی حکمت عملی
1. **محفوظ زبانیں استعمال کریں**: C/C++ پر Rust, Go, Java, Python کو ترجیح دیں
2. **سمارٹ پوائنٹرز**: C++ میں RAII پیٹرن استعمال کریں۔
3. **باؤنڈز چیکنگ**: ہمیشہ سرنی انڈیکس کی توثیق کریں۔
4. **جامد تجزیہ**: ویلگرائنڈ، ایڈریس سینیٹائزر جیسے ٹولز استعمال کریں۔
5. **میموری سیف APIs**: محفوظ معیاری لائبریری فنکشنز استعمال کریں۔
---

## توثیق کی غلطیاں
### کمزور پاس ورڈ پالیسیاں
**بری مثال:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**مسائل:**
- وحشیانہ طاقت کے حملوں کے لیے حساس
- عام پاس ورڈز کا آسانی سے اندازہ لگایا جاتا ہے۔
- سیکیورٹی کے بہترین طریقوں کی خلاف ورزی کرتا ہے۔
**بہتر نقطہ نظر:**```python
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

### سادہ متن کے پاس ورڈز کو اسٹور کرنا
**بری مثال:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**بہتر نقطہ نظر:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### روک تھام کی حکمت عملی
1. **مضبوط ہیشنگ**: پاس ورڈز کے لیے bcrypt، Argon2، یا سکرپٹ کا استعمال کریں
2. **ملٹی فیکٹر توثیق**: اضافی تصدیق کی ضرورت ہے۔
3. **ریٹ کی حد بندی**: وحشیانہ طاقت کے حملوں کو روکیں۔
4. **اکاؤنٹ لاک آؤٹ**: ناکام کوششوں کے بعد عارضی طور پر لاک
5. **سیکیور سیشن مینجمنٹ**: محفوظ، صرف HTTP کوکیز استعمال کریں۔
---

## سیکیورٹی کی دیگر غلطیاں
### ہارڈ کوڈ شدہ راز
**بری مثال:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**بہتر نقطہ نظر:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### غیر محفوظ براہ راست آبجیکٹ حوالہ جات
**بری مثال:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**بہتر نقطہ نظر:**```python
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

### لاپتہ شرح کی حد
**بری مثال:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**بہتر نقطہ نظر:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## متعلقہ موضوعات
- **AI/LLM ناکامیاں**: فوری انجیکشن اور AI سے متعلق مخصوص سیکیورٹی مسائل کے لیے`ai_llm_failures.md`دیکھیں
- **غیر محفوظ کوڈ پیٹرنز**: میموری کی حفاظت اور غیر متعینہ رویے کے لیے کوڈ کی مثالیں دیکھیں
- **تصدیق کے بہترین طریقے**: درست توثیق کے بہاؤ اور سیشن کے انتظام کو نافذ کریں
- **کوڈ کوالٹی**: کوڈنگ کے محفوظ طریقوں کے لیے`code_quality_issues.md`دیکھیں
---

## اضافی حفاظتی خطرات
### کمانڈ انجیکشن
**یہ کیا ہے:** غیر سینیٹائزڈ یوزر ان پٹ کے ذریعے صوابدیدی نظام کے احکامات پر عمل درآمد۔
**بری مثال (خطرناک کوڈ):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**حملہ:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**یہ برا کیوں ہے:**
- حملہ آور کسی بھی سسٹم کمانڈ کو چلا سکتا ہے۔
- مکمل نظام سے سمجھوتہ کرنے کا امکان
- ڈیٹا کی تباہی، میلویئر کی تنصیب ممکن ہے۔
**بہتر نقطہ نظر:**```python
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

### راستہ عبور کرنا
**یہ کیا ہے:** ../ sequences کا استعمال کرتے ہوئے مطلوبہ ڈائریکٹریوں سے باہر فائلوں تک رسائی۔
**بری مثال:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**حملہ:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**بہتر نقطہ نظر:**```python
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

### سرور سائیڈ درخواست جعلسازی (SSRF)
**یہ کیا ہے:** سرور کو غیر ارادی منزلوں کے لیے درخواستیں کرنا۔
**بری مثال:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**حملہ:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**بہتر نقطہ نظر:**```python
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

## کرپٹوگرافک غلطیاں
### کمزور ہیشنگ الگورتھم
**بری مثال:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**یہ برا کیوں ہے:**
- MD5 اور SHA1 خفیہ طور پر ٹوٹے ہوئے ہیں۔
- حساب کرنے میں تیز (بروٹ فورس کو قابل بناتا ہے)
- تصادم حملوں کا مظاہرہ کیا
**بہتر نقطہ نظر:**```python
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

### ہارڈ کوڈ شدہ انکرپشن کیز
**بری مثال:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**بہتر نقطہ نظر:**```python
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

### ECB موڈ استعمال کرنا
**بری مثال:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**یہ برا کیوں ہے:**
- ایک جیسے سادہ متن کے بلاکس ایک جیسی سائفر ٹیکسٹ تیار کرتے ہیں۔
- ڈیٹا میں پیٹرن نظر آتے ہیں۔
- مشہور "ECB پینگوئن" مسئلہ کو ظاہر کرتا ہے۔
**بہتر نقطہ نظر:**```python
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

## API سیکیورٹی کے مسائل
### ان پٹ کی توثیق غائب ہے۔
**بری مثال:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**بہتر نقطہ نظر:**```python
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

### غیر محفوظ API کی توثیق
**بری مثال:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**بہتر نقطہ نظر:**```python
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

### APIs پر شرح کی حد غائب ہے۔
**بری مثال:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**بہتر نقطہ نظر:**```python
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

## سیکیورٹی ہیڈرز اور کنفیگریشن
### سیکیورٹی ہیڈرز غائب ہیں۔
**بری مثال:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**بہتر نقطہ نظر:**```python
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

### غیر محفوظ CORS کنفیگریشن
**بری مثال:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**بہتر نقطہ نظر:**```python
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

## کیس اسٹڈیز
### کیس اسٹڈی 1: Equifax ڈیٹا کی خلاف ورزی (2017)
**واقعہ:** حملہ آوروں نے 147 ملین لوگوں کے ذاتی ڈیٹا تک رسائی کے لیے اپاچی سٹرٹس کے خطرے سے فائدہ اٹھایا۔
**جڑ کی وجہ:**
- بغیر پیچ شدہ سافٹ ویئر (CVE-2017-5638)
- مواد کی قسم کے ہیڈر پر کوئی ان پٹ کی توثیق نہیں ہے۔
- ناکافی نیٹ ورک سیگمنٹیشن
**اثر:**
- $1.4 بلین لاگت
- ذاتی ڈیٹا بے نقاب (SSN، تاریخ پیدائش، پتے)
- بڑے پیمانے پر ساکھ کو نقصان
** سبق:** انحصار کو اپ ڈیٹ رکھیں؛ گہرائی میں دفاع کو لاگو کریں.
### کیس اسٹڈی 2: ٹارگٹ بریچ (2013)
**واقعہ:** حملہ آوروں نے 40 ملین کریڈٹ کارڈ نمبر چرا لیے۔
**جڑ کی وجہ:**
- فریق ثالث وینڈر کی اسناد سے سمجھوتہ کیا گیا۔
- وینڈر اور ادائیگی کے نظام کے درمیان نیٹ ورک کی تقسیم نہیں ہے۔
- نظر انداز سیکورٹی الرٹس
**اثر:**
- لاگت میں $202 ملین
- سی ای او اور سی آئی او کو برطرف کر دیا گیا۔
- ادائیگی کے نظام کی بحالی کی ضرورت ہے۔
**سبق:** سیگمنٹ نیٹ ورکس؛ تیسری پارٹی کی رسائی کی نگرانی؛ انتباہات کا جواب دیں.
### کیس اسٹڈی 3: سولر ونڈز سپلائی چین اٹیک (2020)
**واقعہ:** سافٹ ویئر اپ ڈیٹس میں داخل کردہ بدنیتی پر مبنی کوڈ نے 18,000+ تنظیموں کو متاثر کیا۔
**جڑ کی وجہ:**
- سمجھوتہ شدہ تعمیراتی نظام
- درست سرٹیفکیٹ کے ساتھ بدنیتی پر مبنی اپ ڈیٹس پر دستخط کیے گئے۔
- نیٹ ورک کے اندر ایک بار پس منظر کی حرکت
**اثر:**
- سرکاری ایجنسیوں نے سمجھوتہ کیا۔
- فارچیون 500 کمپنیاں متاثر ہوئیں
- جاری تحقیقات اور تدارک
**سبق:** محفوظ تعمیراتی پائپ لائنز؛ سافٹ ویئر کی سالمیت کی تصدیق؛ زیرو ٹرسٹ فن تعمیر۔
---

## سیکیورٹی ٹیسٹنگ کی حکمت عملی
### جامد ایپلیکیشن سیکیورٹی ٹیسٹنگ (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### ڈائنامک ایپلیکیشن سیکیورٹی ٹیسٹنگ (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### انحصار اسکیننگ
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### دخول ٹیسٹنگ چیک لسٹ
- ایس کیو ایل انجیکشن ٹیسٹنگ
- [ ] XSS ٹیسٹنگ (عکاس شدہ، ذخیرہ شدہ، DOM پر مبنی)
- [ ] CSRF ٹوکن کی توثیق
- [ ] توثیق بائی پاس کی کوششیں۔
- [ ] اجازت کی جانچ پڑتال (عمودی/افقی استحقاق میں اضافہ)
- [ ] شرح کو محدود کرنے کی تصدیق
- [ ] سیکورٹی ہیڈر کی موجودگی
- [ ] SSL/TLS کنفیگریشن
- [ ] سیشن مینجمنٹ کا جائزہ
- [ ] نقص کو سنبھالنا (معلومات کا رساو نہیں)
---

## سیکیورٹی وسائل
### OWASP ٹاپ 10 (2021)
1. ٹوٹا ہوا رسائی کنٹرول
2. خفیہ نگاری کی ناکامیاں
3. انجکشن
4. غیر محفوظ ڈیزائن
5. سیکورٹی کی غلط ترتیب
6. کمزور اور پرانے اجزاء
7. شناخت اور تصدیق میں ناکامیاں
8. سافٹ ویئر اور ڈیٹا انٹیگریٹی کی ناکامیاں
9. سیکورٹی لاگنگ اور مانیٹرنگ کی ناکامیاں
10. سرور سائیڈ درخواست جعلسازی
### تجویز کردہ ٹولز
- **جامد تجزیہ**: سونار کیوب، سیمگریپ، کوڈ کیو ایل
- **انحصار اسکیننگ**: انحصار بوٹ، تجدید کاری، Snyk
- **متحرک جانچ**: OWASP ZAP، Burp Suite
- **خفیہ کھوج**: گٹ لیکس، ٹرفل ہاگ
- **کنٹینر سیکیورٹی**: ٹریوی، کلیر، اینکر