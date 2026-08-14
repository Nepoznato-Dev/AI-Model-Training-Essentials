<!--
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

-->
# নিরাপত্তা দুর্বলতা
এই দস্তাবেজটি সফ্টওয়্যার বিকাশে সাধারণ নিরাপত্তা দুর্বলতাগুলিকে একীভূত করে, যার মধ্যে ইনজেকশন আক্রমণ, অনিরাপদ কোড অনুশীলন এবং নিরাপত্তা ভুল রয়েছে৷
---

## এসকিউএল ইনজেকশন
SQL ইনজেকশন আক্রমণ ঘটে যখন অবিশ্বস্ত ব্যবহারকারীর ইনপুট ডাটাবেস কোয়েরিতে ভুলভাবে পরিচালনা করা হয়, আক্রমণকারীদের ক্যোয়ারী লজিক ম্যানিপুলেট করতে, অননুমোদিত ডেটা অ্যাক্সেস করতে বা ডাটাবেসের বিষয়বস্তু পরিবর্তন করতে দেয়।
### ক্লাসিক UNION-ভিত্তিক ইনজেকশন
**খারাপ উদাহরণ (ভালনারেবল কোড):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**আক্রমণ:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**কেন এটা খারাপ:**
- অন্যান্য টেবিল থেকে ডেটা প্রকাশ করে
- উদ্দিষ্ট ক্যোয়ারী লজিক বাইপাস করে
- সংবেদনশীল তথ্য বের করতে পারেন
**উত্তম পদ্ধতি:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### প্রতিরোধের কৌশল
1. **প্যারামিটারাইজড কোয়েরি ব্যবহার করুন**: কখনই এসকিউএল-এ ব্যবহারকারীর ইনপুট সংযুক্ত করবেন না
2. **ইনপুট বৈধকরণ**: সমস্ত ব্যবহারকারীর ইনপুট যাচাই ও স্যানিটাইজ করুন
3. **ন্যূনতম বিশেষাধিকার**: ডাটাবেস অ্যাকাউন্টের সর্বনিম্ন অনুমতি থাকা উচিত
4. **ORM ব্যবহার**: অবজেক্ট-রিলেশনাল ম্যাপারগুলি ব্যবহার করুন যা পলায়ন পরিচালনা করে
5. **ওয়েব অ্যাপ্লিকেশন ফায়ারওয়াল**: ইনজেকশন প্রচেষ্টা শনাক্ত করতে WAF স্থাপন করুন
---

## ক্রস-সাইট স্ক্রিপ্টিং (XSS)
ক্রস-সাইট স্ক্রিপ্টিং (এক্সএসএস) আক্রমণ ঘটে যখন আক্রমণকারীরা অন্য ব্যবহারকারীদের দ্বারা দেখা ওয়েব পৃষ্ঠাগুলিতে দূষিত স্ক্রিপ্ট ইনজেকশন করে।
### প্রতিফলিত XSS
**খারাপ উদাহরণ (ভালনারেবল কোড):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**আক্রমণ:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**কেন এটা খারাপ:**
- ব্যবহারকারীর ইনপুট এনকোডিং ছাড়াই সরাসরি রেন্ডার করা হয়েছে
- আক্রমণকারী দূষিত URL তৈরি করতে পারে
- সেশন হাইজ্যাকিং, শংসাপত্র চুরি সম্ভব
**উত্তম পদ্ধতি:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### সংরক্ষিত XSS
**খারাপ উদাহরণ:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### প্রতিরোধের কৌশল
1. **আউটপুট এনকোডিং**: প্রসঙ্গের উপর ভিত্তি করে ডেটা এনকোড করুন (HTML, JS, URL, CSS)
2. **ইনপুট বৈধকরণ**: দূষিত ইনপুট প্রত্যাখ্যান বা স্যানিটাইজ করুন
3. **কন্টেন্ট সিকিউরিটি পলিসি**: স্ক্রিপ্ট সোর্স সীমিত করতে CSP হেডার ব্যবহার করুন
4. **HTTPOonly Cookies**: সেশন কুকিতে JavaScript অ্যাক্সেস প্রতিরোধ করুন
5. **আধুনিক ফ্রেমওয়ার্ক**: রিঅ্যাক্ট, ভিউ, অ্যাঙ্গুলার ব্যবহার করুন যা ডিফল্টরূপে স্বয়ংক্রিয়ভাবে পালাতে পারে
---

## মেমরির নিরাপত্তা সংক্রান্ত সমস্যা
### বাফার ওভারফ্লো
**খারাপ উদাহরণ (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**সমস্যা:**
- সংলগ্ন মেমরি ওভাররাইট করতে পারেন
- কোড এক্সিকিউশন আক্রমণের অনুমতি দিতে পারে
- অনির্ধারিত আচরণের কারণ
**উত্তম পদ্ধতি:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### ব্যবহার-পর-বিনামূল্যে
**খারাপ উদাহরণ (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**উত্তম পদ্ধতি:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### প্রতিরোধের কৌশল
1. **নিরাপদ ভাষা ব্যবহার করুন**: C/C++ এর চেয়ে মরিচা, গো, জাভা, পাইথন পছন্দ করুন
2. **স্মার্ট পয়েন্টার**: C++ এ RAII প্যাটার্ন ব্যবহার করুন
3. **বাউন্ড চেকিং**: সর্বদা অ্যারে সূচক যাচাই করুন
4. **স্ট্যাটিক অ্যানালাইসিস**: ভ্যালগ্রিন্ড, অ্যাড্রেস স্যানিটাইজারের মতো টুল ব্যবহার করুন
5. **মেমরি-সেফ APIs**: নিরাপদ স্ট্যান্ডার্ড লাইব্রেরি ফাংশন ব্যবহার করুন
---

## প্রমাণীকরণের ভুল
### দুর্বল পাসওয়ার্ড নীতি
**খারাপ উদাহরণ:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**সমস্যা:**
- নৃশংস শক্তি আক্রমণের জন্য সংবেদনশীল
- সাধারণ পাসওয়ার্ড সহজেই অনুমান করা যায়
- নিরাপত্তার সর্বোত্তম অনুশীলন লঙ্ঘন করে
**উত্তম পদ্ধতি:**```python
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

### প্লেইনটেক্সট পাসওয়ার্ড সংরক্ষণ করা
**খারাপ উদাহরণ:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**উত্তম পদ্ধতি:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### প্রতিরোধের কৌশল
1. **স্ট্রং হ্যাশিং**: পাসওয়ার্ডের জন্য bcrypt, Argon2 বা স্ক্রিপ্ট ব্যবহার করুন
2. **মাল্টি-ফ্যাক্টর প্রমাণীকরণ**: অতিরিক্ত যাচাইকরণ প্রয়োজন
3. **হার সীমাবদ্ধতা**: নৃশংস বল আক্রমণ প্রতিরোধ করুন
4. **অ্যাকাউন্ট লকআউট**: ব্যর্থ প্রচেষ্টার পরে সাময়িকভাবে লক করুন
5. **নিরাপদ সেশন ম্যানেজমেন্ট**: নিরাপদ, শুধুমাত্র HTTP কুকিজ ব্যবহার করুন
---

## অন্যান্য নিরাপত্তা ভুল
### হার্ডকোডেড সিক্রেটস
**খারাপ উদাহরণ:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**উত্তম পদ্ধতি:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### অনিরাপদ প্রত্যক্ষ অবজেক্ট রেফারেন্স
**খারাপ উদাহরণ:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**উত্তম পদ্ধতি:**```python
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

### হারের সীমা অনুপস্থিত
**খারাপ উদাহরণ:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**উত্তম পদ্ধতি:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## সম্পর্কিত বিষয়
- **AI/LLM ব্যর্থতা**: প্রম্পট ইনজেকশন এবং এআই-নির্দিষ্ট নিরাপত্তা সংক্রান্ত সমস্যার জন্য`ai_llm_failures.md`দেখুন
- **অনিরাপদ কোড প্যাটার্নস**: মেমরি নিরাপত্তা এবং অনির্ধারিত আচরণের জন্য কোড উদাহরণ দেখুন
- **প্রমাণিকরণের সর্বোত্তম অভ্যাস**: যথাযথ প্রমাণীকরণ প্রবাহ এবং সেশন ব্যবস্থাপনা প্রয়োগ করুন
- **কোডের গুণমান**: নিরাপদ কোডিং অনুশীলনের জন্য`code_quality_issues.md`দেখুন
---

## অতিরিক্ত নিরাপত্তা দুর্বলতা
### কমান্ড ইনজেকশন
**এটি কী:** অসংযত ব্যবহারকারী ইনপুটের মাধ্যমে নির্বিচারে সিস্টেম কমান্ড কার্যকর করা।
**খারাপ উদাহরণ (ভালনারেবল কোড):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**আক্রমণ:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**কেন এটা খারাপ:**
- আক্রমণকারী যেকোনো সিস্টেম কমান্ড চালাতে পারে
- সম্পূর্ণ সিস্টেম আপস জন্য সম্ভাব্য
- ডেটা ধ্বংস, ম্যালওয়্যার ইনস্টলেশন সম্ভব
**উত্তম পদ্ধতি:**```python
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

### পাথ ট্রাভার্সাল
**এটা কী:** ../ সিকোয়েন্স ব্যবহার করে উদ্দেশ্যপ্রণোদিত ডিরেক্টরির বাইরে ফাইল অ্যাক্সেস করা।
**খারাপ উদাহরণ:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**আক্রমণ:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**উত্তম পদ্ধতি:**```python
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

### সার্ভার-সাইড অনুরোধ জালিয়াতি (SSRF)
**এটি কী:** সার্ভারকে অনাকাঙ্ক্ষিত গন্তব্যে অনুরোধ করা।
**খারাপ উদাহরণ:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**আক্রমণ:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**উত্তম পদ্ধতি:**```python
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

## ক্রিপ্টোগ্রাফিক ভুল
### দুর্বল হ্যাশিং অ্যালগরিদম
**খারাপ উদাহরণ:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**কেন এটা খারাপ:**
- MD5 এবং SHA1 ক্রিপ্টোগ্রাফিকভাবে ভাঙা
- গণনা করতে দ্রুত (ব্রুট ফোর্স সক্ষম করে)
- সংঘর্ষ আক্রমণ প্রদর্শিত
**উত্তম পদ্ধতি:**```python
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

### হার্ডকোডেড এনক্রিপশন কী
**খারাপ উদাহরণ:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**উত্তম পদ্ধতি:**```python
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

### ECB মোড ব্যবহার করা
**খারাপ উদাহরণ:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**কেন এটা খারাপ:**
- অভিন্ন প্লেইনটেক্সট ব্লক একই সাইফারটেক্সট তৈরি করে
- ডেটাতে নিদর্শনগুলি দৃশ্যমান
- বিখ্যাত "ECB পেঙ্গুইন" সমস্যাটি দেখায়
**উত্তম পদ্ধতি:**```python
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

## API নিরাপত্তা সমস্যা
### ইনপুট বৈধতা অনুপস্থিত
**খারাপ উদাহরণ:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**উত্তম পদ্ধতি:**```python
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

### অনিরাপদ API প্রমাণীকরণ
**খারাপ উদাহরণ:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**উত্তম পদ্ধতি:**```python
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

### API-এ হারের সীমা অনুপস্থিত
**খারাপ উদাহরণ:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**উত্তম পদ্ধতি:**```python
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

## নিরাপত্তা শিরোনাম এবং কনফিগারেশন
### নিরাপত্তা শিরোনাম অনুপস্থিত
**খারাপ উদাহরণ:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**উত্তম পদ্ধতি:**```python
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

### অনিরাপদ CORS কনফিগারেশন
**খারাপ উদাহরণ:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**উত্তম পদ্ধতি:**```python
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

## কেস স্টাডিজ
### কেস স্টাডি 1: ইকুইফ্যাক্স ডেটা লঙ্ঘন (2017)
**ঘটনা:** আক্রমণকারীরা 147 মিলিয়ন মানুষের ব্যক্তিগত ডেটা অ্যাক্সেস করার জন্য Apache Struts দুর্বলতাকে কাজে লাগিয়েছে।
**মূল কারণ:**
- আনপ্যাচড সফ্টওয়্যার (CVE-2017-5638)
- বিষয়বস্তু-টাইপ হেডারে কোন ইনপুট বৈধতা নেই
- অপর্যাপ্ত নেটওয়ার্ক বিভাজন
**প্রভাব:**
- $1.4 বিলিয়ন খরচ
- ব্যক্তিগত তথ্য প্রকাশ করা হয়েছে (SSN, জন্ম তারিখ, ঠিকানা)
- ব্যাপক খ্যাতি ক্ষতি
**পাঠ:** নির্ভরতা আপডেট রাখুন; গভীরভাবে প্রতিরক্ষা বাস্তবায়ন।
### কেস স্টাডি 2: লক্ষ্য লঙ্ঘন (2013)
**ঘটনা:** হামলাকারীরা ৪ কোটি ক্রেডিট কার্ড নম্বর চুরি করেছে।
**মূল কারণ:**
- তৃতীয় পক্ষের বিক্রেতার শংসাপত্রগুলি আপস করা হয়েছে৷
- বিক্রেতা এবং পেমেন্ট সিস্টেমের মধ্যে কোন নেটওয়ার্ক বিভাজন নেই
- নিরাপত্তা সতর্কতা উপেক্ষা করা হয়েছে
**প্রভাব:**
- $202 মিলিয়ন খরচ
- CEO এবং CIO বরখাস্ত
- পেমেন্ট সিস্টেম ওভারহল প্রয়োজন
**পাঠ:** সেগমেন্ট নেটওয়ার্ক; তৃতীয় পক্ষের অ্যাক্সেস নিরীক্ষণ; সতর্কতা সাড়া
### কেস স্টাডি 3: সোলারউইন্ডস সাপ্লাই চেইন অ্যাটাক (2020)
**ঘটনা:** সফ্টওয়্যার আপডেটে ক্ষতিকারক কোড ঢোকানো হয়েছে যা 18,000+ প্রতিষ্ঠানকে প্রভাবিত করেছে।
**মূল কারণ:**
- আপস বিল্ড সিস্টেম
- বৈধ শংসাপত্র সহ দূষিত আপডেট স্বাক্ষরিত
- নেটওয়ার্কের ভিতরে একবার পার্শ্বীয় আন্দোলন
**প্রভাব:**
- সরকারী সংস্থা আপস করেছে
- ফরচুন 500 কোম্পানি প্রভাবিত
- চলমান তদন্ত এবং প্রতিকার
**পাঠ:** নিরাপদ বিল্ড পাইপলাইন; সফ্টওয়্যার অখণ্ডতা যাচাই; জিরো-ট্রাস্ট আর্কিটেকচার।
---

## নিরাপত্তা পরীক্ষার কৌশল
### স্ট্যাটিক অ্যাপ্লিকেশন সিকিউরিটি টেস্টিং (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### ডায়নামিক অ্যাপ্লিকেশন সিকিউরিটি টেস্টিং (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### নির্ভরতা স্ক্যানিং
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### পেনিট্রেশন টেস্টিং চেকলিস্ট
- [ ] এসকিউএল ইনজেকশন পরীক্ষা
- [ ] XSS পরীক্ষা (প্রতিফলিত, সঞ্চিত, DOM-ভিত্তিক)
- [ ] CSRF টোকেন বৈধতা
- [ ] প্রমাণীকরণ বাইপাস প্রচেষ্টা
- [ ] অনুমোদন চেক (উল্লম্ব/অনুভূমিক বিশেষাধিকার বৃদ্ধি)
- [ ] হার সীমিত যাচাইকরণ
- [ ] নিরাপত্তা শিরোনাম উপস্থিতি
- [ ] SSL/TLS কনফিগারেশন
- [ ] সেশন ব্যবস্থাপনা পর্যালোচনা
- [ ] ত্রুটি পরিচালনা (কোন তথ্য ফাঁস নয়)
---

## নিরাপত্তা সম্পদ
### OWASP শীর্ষ 10 (2021)
1. ভাঙ্গা অ্যাক্সেস কন্ট্রোল
2. ক্রিপ্টোগ্রাফিক ব্যর্থতা
3. ইনজেকশন
4. অনিরাপদ ডিজাইন
5. নিরাপত্তা ভুল কনফিগারেশন
6. দুর্বল এবং পুরানো উপাদান
7. সনাক্তকরণ এবং প্রমাণীকরণ ব্যর্থতা
8. সফ্টওয়্যার এবং ডেটা ইন্টিগ্রিটি ব্যর্থতা৷
9. নিরাপত্তা লগিং এবং মনিটরিং ব্যর্থতা
10. সার্ভার-সাইড অনুরোধ জালিয়াতি
### প্রস্তাবিত সরঞ্জাম
- **স্ট্যাটিক বিশ্লেষণ**: সোনারকিউব, সেমগ্রেপ, কোডকিউএল
- **নির্ভরতা স্ক্যানিং**: ডিপেন্ডাবোট, রিনোভেট, Snyk
- **ডাইনামিক টেস্টিং**: OWASP ZAP, Burp Suite
- **সিক্রেট ডিটেকশন**: গিটলিকস, ট্রাফলহগ
- **কন্টেইনার নিরাপত্তা**: ট্রিভি, ক্লেয়ার, অ্যাঙ্কর