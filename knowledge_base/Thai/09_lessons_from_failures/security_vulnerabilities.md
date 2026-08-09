---
# Metadata
title: "Security Vulnerabilities"
description: "Common security vulnerabilities"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# ช่องโหว่ด้านความปลอดภัย
เอกสารนี้รวบรวมช่องโหว่ด้านความปลอดภัยทั่วไปในการพัฒนาซอฟต์แวร์ รวมถึงการโจมตีแบบฉีด แนวทางปฏิบัติด้านโค้ดที่ไม่ปลอดภัย และข้อผิดพลาดด้านความปลอดภัย
---

## การฉีด SQL
การโจมตีแบบแทรก SQL เกิดขึ้นเมื่ออินพุตของผู้ใช้ที่ไม่น่าเชื่อถือได้รับการจัดการอย่างไม่เหมาะสมในการสืบค้นฐานข้อมูล ทำให้ผู้โจมตีสามารถจัดการตรรกะการสืบค้น เข้าถึงข้อมูลที่ไม่ได้รับอนุญาต หรือแก้ไขเนื้อหาฐานข้อมูล
### การฉีดแบบคลาสสิกที่ใช้ UNION
**ตัวอย่างที่ไม่ดี (โค้ดที่มีช่องโหว่):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**จู่โจม:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**ทำไมมันแย่:**
- เปิดเผยข้อมูลจากตารางอื่น
- ข้ามตรรกะการสืบค้นที่ตั้งใจไว้
- สามารถดึงข้อมูลที่ละเอียดอ่อนได้
**แนวทางที่ดีกว่า:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### กลยุทธ์การป้องกัน
1. **ใช้การสืบค้นแบบกำหนดพารามิเตอร์**: อย่าเชื่อมอินพุตของผู้ใช้เข้ากับ SQL
2. **การตรวจสอบอินพุต**: ตรวจสอบและฆ่าเชื้ออินพุตของผู้ใช้ทั้งหมด
3. **สิทธิ์ขั้นต่ำ**: บัญชีฐานข้อมูลควรมีสิทธิ์ขั้นต่ำ
4. **การใช้งาน ORM**: ใช้ตัวแมปเชิงวัตถุที่จัดการการหลบหนี
5. **ไฟร์วอลล์แอปพลิเคชันเว็บ**: ปรับใช้ WAF เพื่อตรวจจับความพยายามในการแทรก
---

## การเขียนสคริปต์ข้ามไซต์ (XSS)
การโจมตีด้วยสคริปต์ข้ามไซต์ (XSS) เกิดขึ้นเมื่อผู้โจมตีแทรกสคริปต์ที่เป็นอันตรายลงในหน้าเว็บที่ผู้ใช้รายอื่นดู
### XSS สะท้อน
**ตัวอย่างที่ไม่ดี (โค้ดที่มีช่องโหว่):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**จู่โจม:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**ทำไมมันแย่:**
- การป้อนข้อมูลของผู้ใช้แสดงผลโดยตรงโดยไม่ต้องเข้ารหัส
- ผู้โจมตีสามารถสร้าง URL ที่เป็นอันตรายได้
- การไฮแจ็กเซสชัน การขโมยข้อมูลประจำตัวเป็นไปได้
**แนวทางที่ดีกว่า:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS ที่เก็บไว้
**ตัวอย่างที่ไม่ดี:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### กลยุทธ์การป้องกัน
1. **การเข้ารหัสเอาต์พุต**: เข้ารหัสข้อมูลตามบริบท (HTML, JS, URL, CSS)
2. **การตรวจสอบอินพุต**: ปฏิเสธหรือกำจัดอินพุตที่เป็นอันตราย
3. **นโยบายความปลอดภัยของเนื้อหา**: ใช้ส่วนหัว CSP เพื่อจำกัดแหล่งที่มาของสคริปต์
4. **คุกกี้ HTTPOnly**: ป้องกันการเข้าถึง JavaScript ในคุกกี้เซสชัน
5. **Modern Frameworks**: ใช้ React, Vue, Angular ซึ่งจะหลีกอัตโนมัติตามค่าเริ่มต้น
---

## ปัญหาความปลอดภัยของหน่วยความจำ
### บัฟเฟอร์ล้น
**ตัวอย่างที่ไม่ดี (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**ปัญหา:**
- สามารถเขียนทับหน่วยความจำที่อยู่ติดกัน
- อาจอนุญาตให้มีการโจมตีการเรียกใช้โค้ด
- ทำให้เกิดพฤติกรรมที่ไม่ได้กำหนดไว้
**แนวทางที่ดีกว่า:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### ใช้หลังฟรี
**ตัวอย่างที่ไม่ดี (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**แนวทางที่ดีกว่า:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### กลยุทธ์การป้องกัน
1. **ใช้ภาษาที่ปลอดภัย**: ชอบ Rust, Go, Java, Python มากกว่า C/C++
2. **ตัวชี้อัจฉริยะ**: ใช้รูปแบบ RAII ในภาษา C++
3. **การตรวจสอบขอบเขต**: ตรวจสอบดัชนีอาร์เรย์เสมอ
4. **การวิเคราะห์แบบคงที่**: ใช้เครื่องมือเช่น Valgrind, AddressSanitizer
5. **Memory-Safe APIs**: ใช้ฟังก์ชันไลบรารีมาตรฐานที่ปลอดภัยยิ่งขึ้น
---

## ข้อผิดพลาดในการตรวจสอบสิทธิ์
### นโยบายรหัสผ่านที่อ่อนแอ
**ตัวอย่างที่ไม่ดี:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**ปัญหา:**
- ไวต่อการโจมตีด้วยกำลังดุร้าย
- รหัสผ่านทั่วไปเดาได้ง่าย
- ละเมิดแนวทางปฏิบัติด้านความปลอดภัยที่ดีที่สุด
**แนวทางที่ดีกว่า:**```python
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

### การจัดเก็บรหัสผ่านข้อความธรรมดา
**ตัวอย่างที่ไม่ดี:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**แนวทางที่ดีกว่า:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### กลยุทธ์การป้องกัน
1. **การแฮชที่แข็งแกร่ง**: ใช้ bcrypt, Argon2 หรือ scrypt สำหรับรหัสผ่าน
2. **การตรวจสอบสิทธิ์แบบหลายปัจจัย**: ต้องมีการตรวจสอบเพิ่มเติม
3. **การจำกัดอัตรา**: ป้องกันการโจมตีด้วยกำลังดุร้าย
4. **การล็อคบัญชี**: ล็อคชั่วคราวหลังจากพยายามล้มเหลว
5. **การจัดการเซสชันที่ปลอดภัย**: ใช้คุกกี้ HTTP ที่ปลอดภัยเท่านั้น
---

## ข้อผิดพลาดด้านความปลอดภัยอื่น ๆ
### ความลับฮาร์ดโค้ด
**ตัวอย่างที่ไม่ดี:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**แนวทางที่ดีกว่า:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### การอ้างอิงวัตถุโดยตรงที่ไม่ปลอดภัย
**ตัวอย่างที่ไม่ดี:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**แนวทางที่ดีกว่า:**```python
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

### การจำกัดอัตราที่ขาดหายไป
**ตัวอย่างที่ไม่ดี:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**แนวทางที่ดีกว่า:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## หัวข้อที่เกี่ยวข้อง
- **ความล้มเหลวของ AI/LLM**: ดู`ai_llm_failures.md`สำหรับการฉีดที่รวดเร็วและปัญหาด้านความปลอดภัยเฉพาะของ AI
- **รูปแบบโค้ดที่ไม่ปลอดภัย**: ดูตัวอย่างโค้ดเพื่อความปลอดภัยของหน่วยความจำและลักษณะการทำงานที่ไม่ได้กำหนด
- **แนวทางปฏิบัติที่ดีที่สุดในการรับรองความถูกต้อง**: ใช้ขั้นตอนการรับรองความถูกต้องและการจัดการเซสชันที่เหมาะสม
- **คุณภาพโค้ด**: ดู`code_quality_issues.md`สำหรับแนวทางปฏิบัติในการเขียนโค้ดที่ปลอดภัย
---

## ช่องโหว่ด้านความปลอดภัยเพิ่มเติม
### คำสั่งฉีด
**มันคืออะไร:** การดำเนินการคำสั่งของระบบตามอำเภอใจผ่านการป้อนข้อมูลของผู้ใช้ที่ไม่สะอาด
**ตัวอย่างที่ไม่ดี (โค้ดที่มีช่องโหว่):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**จู่โจม:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**ทำไมมันแย่:**
- ผู้โจมตีสามารถดำเนินการคำสั่งระบบใดก็ได้
- ศักยภาพในการประนีประนอมระบบโดยสมบูรณ์
- การทำลายข้อมูล, การติดตั้งมัลแวร์เป็นไปได้
**แนวทางที่ดีกว่า:**```python
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

### การข้ามเส้นทาง
**มันคืออะไร:** การเข้าถึงไฟล์นอกไดเร็กทอรีที่ต้องการโดยใช้ ../ ซีเควนซ์
**ตัวอย่างที่ไม่ดี:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**จู่โจม:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**แนวทางที่ดีกว่า:**```python
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

### การปลอมแปลงคำขอฝั่งเซิร์ฟเวอร์ (SSRF)
**มันคืออะไร:** การทำให้เซิร์ฟเวอร์ส่งคำขอไปยังปลายทางที่ไม่ได้ตั้งใจ
**ตัวอย่างที่ไม่ดี:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**จู่โจม:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**แนวทางที่ดีกว่า:**```python
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

## ข้อผิดพลาดในการเข้ารหัส
### อัลกอริธึมการแฮชที่อ่อนแอ
**ตัวอย่างที่ไม่ดี:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**ทำไมมันแย่:**
- MD5 และ SHA1 ใช้งานไม่ได้ด้วยการเข้ารหัส
- รวดเร็วในการคำนวณ (เปิดใช้งานกำลังเดรัจฉาน)
- แสดงให้เห็นการโจมตีแบบชนกัน
**แนวทางที่ดีกว่า:**```python
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

### คีย์การเข้ารหัสแบบฮาร์ดโค้ด
**ตัวอย่างที่ไม่ดี:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**แนวทางที่ดีกว่า:**```python
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

### การใช้โหมด ECB
**ตัวอย่างที่ไม่ดี:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**ทำไมมันแย่:**
- บล็อกข้อความธรรมดาที่เหมือนกันจะสร้างข้อความเข้ารหัสที่เหมือนกัน
- มองเห็นรูปแบบข้อมูลได้
- “นกเพนกวิน ECB” ชื่อดัง สาธิตปัญหา
**แนวทางที่ดีกว่า:**```python
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

## ปัญหาด้านความปลอดภัยของ API
### ขาดการตรวจสอบอินพุต
**ตัวอย่างที่ไม่ดี:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**แนวทางที่ดีกว่า:**```python
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

### การตรวจสอบสิทธิ์ API ที่ไม่ปลอดภัย
**ตัวอย่างที่ไม่ดี:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**แนวทางที่ดีกว่า:**```python
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

### การจำกัดอัตราที่ขาดหายไปใน API
**ตัวอย่างที่ไม่ดี:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**แนวทางที่ดีกว่า:**```python
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

## ส่วนหัวและการกำหนดค่าความปลอดภัย
### ส่วนหัวการรักษาความปลอดภัยหายไป
**ตัวอย่างที่ไม่ดี:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**แนวทางที่ดีกว่า:**```python
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

### การกำหนดค่า CORS ที่ไม่ปลอดภัย
**ตัวอย่างที่ไม่ดี:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**แนวทางที่ดีกว่า:**```python
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

## กรณีศึกษา
### กรณีศึกษา 1: การละเมิดข้อมูล Equifax (2017)
**เหตุการณ์:** ผู้โจมตีใช้ประโยชน์จากช่องโหว่ของ Apache Struts เพื่อเข้าถึงข้อมูลส่วนบุคคลของผู้คน 147 ล้านคน
**สาเหตุที่แท้จริง:**
- ซอฟต์แวร์ที่ไม่ได้รับการติดตั้ง (CVE-2017-5638)
- ไม่มีการตรวจสอบอินพุตบนส่วนหัวของประเภทเนื้อหา
- การแบ่งส่วนเครือข่ายไม่เพียงพอ
**ผลกระทบ:**
- ค่าใช้จ่าย 1.4 พันล้านดอลลาร์
- ข้อมูลส่วนบุคคลที่ถูกเปิดเผย (SSN, วันเกิด, ที่อยู่)
- ความเสียหายทางชื่อเสียงครั้งใหญ่
**บทเรียน:** อัปเดตการอ้างอิงอยู่เสมอ ดำเนินการป้องกันในเชิงลึก
### กรณีศึกษา 2: การละเมิดเป้าหมาย (2013)
**เหตุการณ์:** ผู้โจมตีขโมยหมายเลขบัตรเครดิต 40 ล้านหมายเลข
**สาเหตุที่แท้จริง:**
- ข้อมูลประจำตัวของผู้ขายบุคคลที่สามถูกบุกรุก
- ไม่มีการแบ่งส่วนเครือข่ายระหว่างผู้ขายและระบบการชำระเงิน
- ละเว้นการแจ้งเตือนความปลอดภัย
**ผลกระทบ:**
- ค่าใช้จ่าย 202 ล้านเหรียญสหรัฐ
- CEO และ CIO ไล่ออก
- จำเป็นต้องยกเครื่องระบบการชำระเงิน
**บทเรียน:** เครือข่ายเซ็กเมนต์ ตรวจสอบการเข้าถึงของบุคคลที่สาม ตอบสนองต่อการแจ้งเตือน
### กรณีศึกษา 3: การโจมตีห่วงโซ่อุปทานของ SolarWinds (2020)
**เหตุการณ์:** รหัสที่เป็นอันตรายที่แทรกลงในการอัปเดตซอฟต์แวร์ส่งผลกระทบต่อองค์กรมากกว่า 18,000 แห่ง
**สาเหตุที่แท้จริง:**
- ระบบการสร้างที่ถูกบุกรุก
- ลงนามการอัปเดตที่เป็นอันตรายด้วยใบรับรองที่ถูกต้อง
- การเคลื่อนไหวด้านข้างเมื่ออยู่ภายในเครือข่าย
**ผลกระทบ:**
-หน่วยงานของรัฐถูกบุกรุก
- บริษัทใน Fortune 500 ได้รับผลกระทบ
- การสอบสวนและการแก้ไขอย่างต่อเนื่อง
**บทเรียน:** ไปป์ไลน์การสร้างที่ปลอดภัย ตรวจสอบความสมบูรณ์ของซอฟต์แวร์ สถาปัตยกรรมแบบ Zero Trust
---

## กลยุทธ์การทดสอบความปลอดภัย
### การทดสอบความปลอดภัยของแอปพลิเคชันแบบคงที่ (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### การทดสอบความปลอดภัยของแอปพลิเคชันแบบไดนามิก (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### การสแกนการพึ่งพา
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### รายการตรวจสอบการทดสอบการเจาะ
- [ ] การทดสอบการฉีด SQL
- [ ] การทดสอบ XSS (สะท้อนกลับ จัดเก็บ ตาม DOM)
- [ ] การตรวจสอบโทเค็น CSRF
- [ ] ความพยายามบายพาสการรับรองความถูกต้อง
- [ ] การตรวจสอบการอนุญาต (การยกระดับสิทธิ์ในแนวตั้ง/แนวนอน)
- [ ] การตรวจสอบการจำกัดอัตรา
- [ ] การมีอยู่ของส่วนหัวความปลอดภัย
- [ ] การกำหนดค่า SSL/TLS
- [ ] การตรวจสอบการจัดการเซสชั่น
- [ ] การจัดการข้อผิดพลาด (ไม่มีข้อมูลรั่วไหล)
---

## แหล่งข้อมูลด้านความปลอดภัย
### OWASP 10 อันดับแรก (2021)
1. การควบคุมการเข้าถึงที่เสียหาย
2. ความล้มเหลวในการเข้ารหัส
3. การฉีด
4. การออกแบบที่ไม่ปลอดภัย
5. การกำหนดค่าความปลอดภัยไม่ถูกต้อง
6. ส่วนประกอบที่มีช่องโหว่และล้าสมัย
7. ความล้มเหลวในการระบุตัวตนและการรับรองความถูกต้อง
8. ความล้มเหลวด้านความสมบูรณ์ของซอฟต์แวร์และข้อมูล
9. การบันทึกความปลอดภัยและความล้มเหลวในการตรวจสอบ
10. การปลอมแปลงคำขอฝั่งเซิร์ฟเวอร์
### เครื่องมือแนะนำ
- **การวิเคราะห์แบบคงที่**: SonarQube, Semgrep, CodeQL
- **การสแกนการพึ่งพา**: Dependabot, Renovate, Snyk
- **การทดสอบแบบไดนามิก**: OWASP ZAP, Burp Suite
- **การตรวจจับความลับ**: GitLeaks, TruffleHog
- **ความปลอดภัยของตู้คอนเทนเนอร์**: ทริวี่, แคลร์, แองเคอร์