---
# فراداده
عنوان: "آسیب پذیری های امنیتی"
توضیحات: "آسیب پذیری های امنیتی رایج"
دسته بندی: "درس هایی از شکست"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "درس هایی از تیم پایگاه دانش شکست ها"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [امنیت، آسیب‌پذیری، درس‌هایی از شکست]
سطح سختی: "پیشرفته"
پیش نیاز: []
تخمینی_زمان_خواندن: "34 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
# آسیب پذیری های امنیتی
این سند آسیب‌پذیری‌های امنیتی رایج در توسعه نرم‌افزار، از جمله حملات تزریق، شیوه‌های کد ناامن و اشتباهات امنیتی را ادغام می‌کند.
---

## تزریق SQL
حملات تزریق SQL زمانی اتفاق می‌افتد که ورودی نامعتبر کاربر به‌درستی در پرس‌و‌جوهای پایگاه داده به کار گرفته می‌شود و به مهاجمان اجازه می‌دهد تا منطق پرس و جو را دستکاری کنند، به داده‌های غیرمجاز دسترسی داشته باشند یا محتوای پایگاه داده را تغییر دهند.
### تزریق کلاسیک مبتنی بر UNION
**نمونه بد (کد آسیب پذیر):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**حمله:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**چرا بد است:**
- داده های جداول دیگر را در معرض دید قرار می دهد
- منطق پرس و جو مورد نظر را دور می زند
- می تواند اطلاعات حساس را استخراج کند
**رویکرد بهتر:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### استراتژی های پیشگیری
1. **از پرس و جوهای پارامتری استفاده کنید**: هرگز ورودی کاربر را به SQL الحاق نکنید
2. **Input Validation**: تمام ورودی های کاربر را اعتبارسنجی و پاکسازی کنید
3. **حداقل امتیاز**: حساب های پایگاه داده باید حداقل مجوزها را داشته باشند
4. **استفاده از ORM**: از نگاشتهای شیء-رابطه ای استفاده کنید که فرار را کنترل می کنند
5. **فایروال های برنامه کاربردی وب**: WAF ها را برای شناسایی تلاش های تزریق مستقر کنید.
---

## اسکریپت بین سایتی (XSS)
حملات Cross-Site Scripting (XSS) زمانی اتفاق می‌افتند که مهاجمان اسکریپت‌های مخرب را به صفحات وب که توسط سایر کاربران مشاهده می‌شوند تزریق می‌کنند.
### XSS منعکس شده است
**نمونه بد (کد آسیب پذیر):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**حمله:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**چرا بد است:**
- ورودی کاربر به طور مستقیم بدون رمزگذاری ارائه می شود
- مهاجم می تواند URL های مخرب ایجاد کند
- ربودن جلسه، سرقت مدارک ممکن است
**رویکرد بهتر:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS ذخیره شده است
**مثال بد:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### استراتژی های پیشگیری
1. **کدگذاری خروجی**: کدگذاری داده ها بر اساس زمینه (HTML، JS، URL، CSS)
2. **Input Validation**: ورودی مخرب را رد یا پاکسازی کنید
3. **سیاست امنیتی محتوا**: از هدرهای CSP برای محدود کردن منابع اسکریپت استفاده کنید
4. **HTTPOnly Cookies**: جلوگیری از دسترسی جاوا اسکریپت به کوکی های جلسه
5. **فریم‌ورک‌های مدرن**: از React، Vue، Angular استفاده کنید که به‌طور پیش‌فرض به صورت خودکار فرار می‌کنند.
---

## مسائل ایمنی حافظه
### سرریز بافر
**مثال بد (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**مشکلات:**
- می تواند حافظه مجاور را بازنویسی کند
- ممکن است به حملات اجرای کد اجازه دهد
- باعث رفتار نامشخص می شود
**رویکرد بهتر:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### استفاده-پس از-رایگان
**مثال بد (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**رویکرد بهتر:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### استراتژی های پیشگیری
1. **از زبان های ایمن استفاده کنید**: Rust، Go، Java، Python را به C/C++ ترجیح دهید
2. **نشانگرهای هوشمند**: از الگوهای RAII در C++ استفاده کنید
3. **بررسی کرانه ها**: همیشه شاخص های آرایه را تأیید کنید
4. **تحلیل استاتیک**: از ابزارهایی مانند Valgrind، AddressSanitizer استفاده کنید
5. **Memory-Safe APIs**: از توابع استاندارد کتابخانه ایمن تر استفاده کنید
---

## اشتباهات احراز هویت
### سیاست های رمز عبور ضعیف
**مثال بد:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**مشکلات:**
- مستعد حملات brute force
- رمزهای عبور رایج به راحتی قابل حدس زدن هستند
- بهترین شیوه های امنیتی را نقض می کند
**رویکرد بهتر:**```python
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

### ذخیره رمزهای عبور متن ساده
**مثال بد:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**رویکرد بهتر:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### استراتژی های پیشگیری
1. **هشینگ قوی**: برای رمزهای عبور از bcrypt، Argon2 یا scrypt استفاده کنید
2. ** احراز هویت چند عاملی **: نیاز به تأیید اضافی
3. **Rate Limiting**: از حملات brute force جلوگیری کنید
4. **Account Lockout**: به طور موقت پس از تلاش های ناموفق قفل می شود
5. **مدیریت جلسه امن**: از کوکی های امن و فقط HTTP استفاده کنید
---

## دیگر اشتباهات امنیتی
### اسرار کدگذاری شده
**مثال بد:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**رویکرد بهتر:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### ارجاعات مستقیم شیء ناامن
**مثال بد:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**رویکرد بهتر:**```python
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

### محدودیت نرخ از دست رفته
**مثال بد:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**رویکرد بهتر:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## موضوعات مرتبط
- **مشکلات AI/LLM**: برای تزریق سریع و مسائل امنیتی خاص هوش مصنوعی به`ai_llm_failures.md`مراجعه کنید
- **الگوهای کد ناامن**: برای ایمنی حافظه و رفتار تعریف نشده به نمونه های کد مراجعه کنید
- **بهترین روشهای احراز هویت**: اجرای جریانهای احراز هویت مناسب و مدیریت جلسه
- **کیفیت کد**: برای شیوه های کدگذاری ایمن به`code_quality_issues.md`مراجعه کنید
---

## آسیب پذیری های امنیتی اضافی
### فرمان تزریق
**چیست:** اجرای دستورات سیستم دلخواه از طریق ورودی غیرعفونی شده کاربر.
**نمونه بد (کد آسیب پذیر):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**حمله:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**چرا بد است:**
- مهاجم می تواند هر فرمان سیستمی را اجرا کند
- امکان به خطر افتادن کامل سیستم
- تخریب داده ها، نصب بدافزار امکان پذیر است
**رویکرد بهتر:**```python
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

### پیمایش مسیر
**چیست:** دسترسی به فایل های خارج از دایرکتوری های مورد نظر با استفاده از دنباله های ../.
**مثال بد:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**حمله:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**رویکرد بهتر:**```python
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

### جعل درخواست سمت سرور (SSRF)
**چیست:** ایجاد درخواست از سرور برای مقاصد ناخواسته.
**مثال بد:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**حمله:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**رویکرد بهتر:**```python
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

## اشتباهات رمزنگاری
### الگوریتم های هش ضعیف
**مثال بد:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**چرا بد است:**
- MD5 و SHA1 از نظر رمزنگاری شکسته شده اند
- محاسبه سریع (فشار بی رحم را فعال می کند)
- حملات برخورد نشان داده شده است
**رویکرد بهتر:**```python
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

### کلیدهای رمزگذاری سخت
**مثال بد:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**رویکرد بهتر:**```python
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

### با استفاده از حالت ECB
**مثال بد:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**چرا بد است:**
- بلوک های متن ساده یکسان متن رمزی یکسانی تولید می کنند
- الگوهای موجود در داده ها قابل مشاهده است
- معروف "پنگوئن ECB" مشکل را نشان می دهد
**رویکرد بهتر:**```python
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

## مشکلات امنیتی API
### اعتبار سنجی ورودی وجود ندارد
**مثال بد:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**رویکرد بهتر:**```python
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

### احراز هویت ناامن API
**مثال بد:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**رویکرد بهتر:**```python
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

### محدودیت نرخ از دست رفته در APIها
**مثال بد:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**رویکرد بهتر:**```python
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

## سرصفحه ها و پیکربندی امنیتی
### سرصفحه های امنیتی از دست رفته است
**مثال بد:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**رویکرد بهتر:**```python
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

### پیکربندی CORS ناامن
**مثال بد:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**رویکرد بهتر:**```python
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

## مطالعات موردی
### مطالعه موردی 1: نقض داده های Equifax (2017)
**حادثه:** مهاجمان از آسیب پذیری Apache Struts برای دسترسی به اطلاعات شخصی 147 میلیون نفر سوء استفاده کردند.
**علت اصلی:**
- نرم افزار بدون وصله (CVE-2017-5638)
- بدون تایید ورودی در هدر نوع محتوا
- تقسیم بندی شبکه ناکافی
**تاثیر:**
- 1.4 میلیارد دلار هزینه
- اطلاعات شخصی افشا شده (SSN، تاریخ تولد، آدرس)
- صدمه شدید به شهرت
**درس:** وابستگی ها را به روز نگه دارید. دفاع را عمیقاً اجرا کنید
### مطالعه موردی 2: نقض هدف (2013)
**حادثه:** مهاجمان 40 میلیون شماره کارت اعتباری را سرقت کردند.
**علت اصلی:**
- اعتبار فروشنده شخص ثالث به خطر افتاده است
- عدم تقسیم بندی شبکه بین فروشنده و سیستم های پرداخت
- هشدارهای امنیتی نادیده گرفته شده است
**تاثیر:**
202 میلیون دلار هزینه
- مدیرعامل و مدیر ارشد اجرایی اخراج شدند
- تعمیرات اساسی سیستم پرداخت مورد نیاز است
**درس:** شبکه های بخش. نظارت بر دسترسی شخص ثالث؛ به هشدارها پاسخ دهید
### مطالعه موردی 3: حمله زنجیره تامین SolarWinds (2020)
**حادثه:** کد مخرب درج شده در به روز رسانی نرم افزار بیش از 18000 سازمان را تحت تأثیر قرار داد.
**علت اصلی:**
- سیستم ساخت به خطر افتاده
- به روز رسانی های مخرب با گواهی های معتبر امضا شده است
- حرکت جانبی یک بار در داخل شبکه ها
**تاثیر:**
- سازمان های دولتی به خطر افتادند
- فورچون 500 شرکت تحت تاثیر قرار گرفت
- بررسی و اصلاح در حال انجام
**درس:** ساخت خطوط لوله ایمن. بررسی یکپارچگی نرم افزار؛ معماری بدون اعتماد
---

## استراتژی های تست امنیت
### تست امنیت برنامه استاتیک (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### تست امنیت برنامه پویا (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### اسکن وابستگی
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### چک لیست تست نفوذ
- [ ] تست تزریق SQL
- [ ] تست XSS (بازتاب شده، ذخیره شده، مبتنی بر DOM)
- [ ] اعتبار سنجی رمز CSRF
- [ ] تلاش های دور زدن احراز هویت
- [ ] بررسی های مجوز (تشدید امتیازات عمودی/افقی)
- [ ] راستی‌آزمایی محدودکننده نرخ
- [ ] وجود سرصفحه های امنیتی
- [ ] پیکربندی SSL/TLS
- [ ] بررسی مدیریت جلسه
- [ ] رسیدگی به خطا (بدون نشت اطلاعات)
---

## منابع امنیتی
### 10 برتر OWASP (2021)
1. کنترل دسترسی شکسته
2. خرابی های رمزنگاری
3. تزریق
4. طراحی ناامن
5. پیکربندی اشتباه امنیتی
6. مولفه های آسیب پذیر و قدیمی
7. شناسایی و تأیید اعتبار
8. نرم افزار و یکپارچگی داده ها خراب است
9. ثبت نام امنیتی و خرابی های نظارت
10. جعل درخواست سمت سرور
### ابزارهای توصیه شده
- **تحلیل استاتیک**: SonarQube، Semgrep، CodeQL
- **اسکن وابستگی**: Dependabot، Renovate، Snyk
- **تست دینامیک**: OWASP ZAP، Burp Suite
- **تشخیص محرمانه**: GitLeaks، TruffleHog
- ** امنیت کانتینر **: Trivy، Clair، Anchore