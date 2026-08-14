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
# सुरक्षा कमजोरियाँ
यह दस्तावेज़ सॉफ्टवेयर विकास में सामान्य सुरक्षा कमजोरियों को समेकित करता है, जिसमें इंजेक्शन हमले, असुरक्षित कोड प्रथाएं और सुरक्षा गलतियाँ शामिल हैं।
---

## एसक्यूएल इंजेक्शन
SQL इंजेक्शन हमले तब होते हैं जब डेटाबेस प्रश्नों में अविश्वसनीय उपयोगकर्ता इनपुट को अनुचित तरीके से संभाला जाता है, जिससे हमलावरों को क्वेरी तर्क में हेरफेर करने, अनधिकृत डेटा तक पहुंचने या डेटाबेस सामग्री को संशोधित करने की अनुमति मिलती है।
### क्लासिक यूनियन-आधारित इंजेक्शन
**खराब उदाहरण (असुरक्षित कोड):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**आक्रमण करना:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**यह बुरा क्यों है:**
- अन्य तालिकाओं से डेटा प्रदर्शित करता है
- इच्छित क्वेरी तर्क को बायपास करता है
- संवेदनशील जानकारी निकाल सकते हैं
**बेहतर दृष्टिकोण:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### रोकथाम रणनीतियाँ
1. **पैरामीटरयुक्त क्वेरीज़ का उपयोग करें**: कभी भी उपयोगकर्ता इनपुट को SQL में संयोजित न करें
2. **इनपुट सत्यापन**: सभी उपयोगकर्ता इनपुट को मान्य और स्वच्छ करें
3. **न्यूनतम विशेषाधिकार**: डेटाबेस खातों के पास न्यूनतम अनुमतियाँ होनी चाहिए
4. **ओआरएम उपयोग**: ऑब्जेक्ट-रिलेशनल मैपर्स का उपयोग करें जो भागने को संभालते हैं
5. **वेब एप्लिकेशन फ़ायरवॉल**: इंजेक्शन प्रयासों का पता लगाने के लिए WAF तैनात करें
---

## क्रॉस-साइट स्क्रिप्टिंग (XSS)
क्रॉस-साइट स्क्रिप्टिंग (XSS) हमले तब होते हैं जब हमलावर अन्य उपयोगकर्ताओं द्वारा देखे गए वेब पेजों में दुर्भावनापूर्ण स्क्रिप्ट इंजेक्ट करते हैं।
### प्रतिबिंबित XSS
**खराब उदाहरण (असुरक्षित कोड):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**आक्रमण करना:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**यह बुरा क्यों है:**
- उपयोगकर्ता इनपुट एन्कोडिंग के बिना सीधे प्रस्तुत किया गया
- हमलावर दुर्भावनापूर्ण यूआरएल तैयार कर सकता है
- सत्र अपहरण, क्रेडेंशियल चोरी संभव
**बेहतर दृष्टिकोण:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### संग्रहित XSS
**खराब उदाहरण:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### रोकथाम रणनीतियाँ
1. **आउटपुट एनकोडिंग**: संदर्भ के आधार पर डेटा एनकोड करें (HTML, JS, URL, CSS)
2. **इनपुट सत्यापन**: दुर्भावनापूर्ण इनपुट को अस्वीकार या साफ़ करें
3. **सामग्री सुरक्षा नीति**: स्क्रिप्ट स्रोतों को प्रतिबंधित करने के लिए सीएसपी हेडर का उपयोग करें
4. **HTTPonly कुकीज़**: सत्र कुकीज़ तक जावास्क्रिप्ट पहुंच को रोकें
5. **आधुनिक फ्रेमवर्क**: रिएक्ट, व्यू, एंगुलर का उपयोग करें जो डिफ़ॉल्ट रूप से स्वचालित रूप से बच जाता है
---

## मेमोरी सुरक्षा मुद्दे
### बफ़र ओवरफ़्लो
**खराब उदाहरण (सी):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**समस्याएँ:**
- आसन्न स्मृति को अधिलेखित कर सकते हैं
- कोड निष्पादन हमलों की अनुमति दे सकता है
- अपरिभाषित व्यवहार का कारण बनता है
**बेहतर दृष्टिकोण:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### उपयोग के बाद निःशुल्क
**खराब उदाहरण (सी++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**बेहतर दृष्टिकोण:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### रोकथाम रणनीतियाँ
1. **सुरक्षित भाषाओं का उपयोग करें**: C/C++ की तुलना में रस्ट, गो, जावा, पायथन को प्राथमिकता दें
2. **स्मार्ट पॉइंटर्स**: C++ में RAII पैटर्न का उपयोग करें
3. **बाउंड चेकिंग**: हमेशा सरणी सूचकांकों को मान्य करें
4. **स्थैतिक विश्लेषण**: वेलग्रिंड, एड्रेस सैनिटाइज़र जैसे टूल का उपयोग करें
5. **मेमोरी-सुरक्षित एपीआई**: सुरक्षित मानक लाइब्रेरी फ़ंक्शन का उपयोग करें
---

## प्रमाणीकरण गलतियाँ
### कमजोर पासवर्ड नीतियाँ
**खराब उदाहरण:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**समस्याएँ:**
- क्रूर बल के हमलों के प्रति संवेदनशील
- सामान्य पासवर्ड का आसानी से अनुमान लगाया जा सकता है
- सुरक्षा सर्वोत्तम प्रथाओं का उल्लंघन करता है
**बेहतर दृष्टिकोण:**```python
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

### प्लेनटेक्स्ट पासवर्ड संग्रहीत करना
**खराब उदाहरण:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**बेहतर दृष्टिकोण:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### रोकथाम रणनीतियाँ
1. **मजबूत हैशिंग**: पासवर्ड के लिए bcrypt, Argon2, या scrypt का उपयोग करें
2. **मल्टी-फैक्टर प्रमाणीकरण**: अतिरिक्त सत्यापन की आवश्यकता है
3. **दर सीमित करना**: क्रूर बल के हमलों को रोकें
4. **खाता लॉकआउट**: विफल प्रयासों के बाद अस्थायी रूप से लॉक करें
5. **सुरक्षित सत्र प्रबंधन**: सुरक्षित, HTTP-केवल कुकीज़ का उपयोग करें
---

## अन्य सुरक्षा गलतियाँ
### हार्डकोडेड रहस्य
**खराब उदाहरण:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**बेहतर दृष्टिकोण:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### असुरक्षित प्रत्यक्ष वस्तु संदर्भ
**खराब उदाहरण:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**बेहतर दृष्टिकोण:**```python
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

### गुम दर सीमा
**खराब उदाहरण:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**बेहतर दृष्टिकोण:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## संबंधित विषय
- **एआई/एलएलएम विफलताएं**: त्वरित इंजेक्शन और एआई-विशिष्ट सुरक्षा समस्याओं के लिए`ai_llm_failures.md`देखें
- **असुरक्षित कोड पैटर्न**: मेमोरी सुरक्षा और अपरिभाषित व्यवहार के लिए कोड उदाहरण देखें
- **प्रमाणीकरण सर्वोत्तम अभ्यास**: उचित प्रमाणीकरण प्रवाह और सत्र प्रबंधन लागू करें
- **कोड गुणवत्ता**: सुरक्षित कोडिंग प्रथाओं के लिए`code_quality_issues.md`देखें
---

## अतिरिक्त सुरक्षा कमजोरियाँ
### कमांड इंजेक्शन
**यह क्या है:** अस्वच्छ उपयोगकर्ता इनपुट के माध्यम से मनमाने ढंग से सिस्टम कमांड निष्पादित करना।
**खराब उदाहरण (असुरक्षित कोड):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**आक्रमण करना:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**यह बुरा क्यों है:**
- हमलावर किसी भी सिस्टम कमांड को निष्पादित कर सकता है
- संपूर्ण सिस्टम समझौता की संभावना
- डेटा विनाश, मैलवेयर इंस्टॉलेशन संभव
**बेहतर दृष्टिकोण:**```python
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

### पथ परिभ्रमण
**यह क्या है:** ../ अनुक्रमों का उपयोग करके इच्छित निर्देशिकाओं के बाहर फ़ाइलों तक पहुँचना।
**खराब उदाहरण:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**आक्रमण करना:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**बेहतर दृष्टिकोण:**```python
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

### सर्वर-साइड अनुरोध जालसाजी (एसएसआरएफ)
**यह क्या है:** सर्वर से अनपेक्षित गंतव्यों के लिए अनुरोध करना।
**खराब उदाहरण:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**आक्रमण करना:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**बेहतर दृष्टिकोण:**```python
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

## क्रिप्टोग्राफ़िक गलतियाँ
### कमजोर हैशिंग एल्गोरिदम
**खराब उदाहरण:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**यह बुरा क्यों है:**
- MD5 और SHA1 क्रिप्टोग्राफ़िक रूप से टूटे हुए हैं
- गणना करने में तेज़ (क्रूर बल को सक्षम बनाता है)
- टकराव के हमलों का प्रदर्शन किया गया
**बेहतर दृष्टिकोण:**```python
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

### हार्डकोडेड एन्क्रिप्शन कुंजियाँ
**खराब उदाहरण:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**बेहतर दृष्टिकोण:**```python
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

### ईसीबी मोड का उपयोग करना
**खराब उदाहरण:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**यह बुरा क्यों है:**
- समान प्लेनटेक्स्ट ब्लॉक समान सिफरटेक्स्ट उत्पन्न करते हैं
- डेटा में पैटर्न दिखाई दे रहे हैं
- प्रसिद्ध "ईसीबी पेंगुइन" समस्या को प्रदर्शित करता है
**बेहतर दृष्टिकोण:**```python
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

## एपीआई सुरक्षा मुद्दे
### गुम इनपुट सत्यापन
**खराब उदाहरण:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**बेहतर दृष्टिकोण:**```python
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

### असुरक्षित एपीआई प्रमाणीकरण
**खराब उदाहरण:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**बेहतर दृष्टिकोण:**```python
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

### एपीआई पर दर सीमा का अभाव
**खराब उदाहरण:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**बेहतर दृष्टिकोण:**```python
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

## सुरक्षा शीर्षलेख और कॉन्फ़िगरेशन
### गुम सुरक्षा शीर्षलेख
**खराब उदाहरण:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**बेहतर दृष्टिकोण:**```python
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

### असुरक्षित सीओआरएस कॉन्फ़िगरेशन
**खराब उदाहरण:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**बेहतर दृष्टिकोण:**```python
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

## मामले का अध्ययन
### केस स्टडी 1: इक्विफैक्स डेटा ब्रीच (2017)
**घटना:** हमलावरों ने 147 मिलियन लोगों के व्यक्तिगत डेटा तक पहुंचने के लिए अपाचे स्ट्रट्स की भेद्यता का फायदा उठाया।
**मूल कारण:**
- अनपैच्ड सॉफ़्टवेयर (CVE-2017-5638)
- सामग्री-प्रकार हेडर पर कोई इनपुट सत्यापन नहीं
- अपर्याप्त नेटवर्क विभाजन
**प्रभाव:**
- लागत $1.4 बिलियन
- व्यक्तिगत डेटा उजागर (एसएसएन, जन्मतिथि, पते)
- बड़े पैमाने पर प्रतिष्ठा की क्षति
**पाठ:** निर्भरताएँ अद्यतन रखें; रक्षा को गहराई से लागू करें।
### केस स्टडी 2: लक्ष्य उल्लंघन (2013)
**घटना:** हमलावरों ने 40 मिलियन क्रेडिट कार्ड नंबर चुरा लिए।
**मूल कारण:**
- तृतीय-पक्ष विक्रेता क्रेडेंशियल्स से समझौता किया गया
- विक्रेता और भुगतान प्रणालियों के बीच कोई नेटवर्क विभाजन नहीं
- सुरक्षा अलर्ट को नजरअंदाज किया गया
**प्रभाव:**
- लागत $202 मिलियन
- सीईओ और सीआईओ को निकाल दिया गया
- भुगतान प्रणाली में आमूल-चूल परिवर्तन की आवश्यकता
**पाठ:** खंड नेटवर्क; तीसरे पक्ष की पहुंच की निगरानी करें; अलर्ट का जवाब दें.
### केस स्टडी 3: सोलरविंड्स सप्लाई चेन अटैक (2020)
**घटना:** सॉफ़्टवेयर अपडेट में डाले गए दुर्भावनापूर्ण कोड ने 18,000+ संगठनों को प्रभावित किया।
**मूल कारण:**
- समझौता निर्माण प्रणाली
- वैध प्रमाणपत्रों के साथ हस्ताक्षरित दुर्भावनापूर्ण अद्यतन
- नेटवर्क के अंदर एक बार पार्श्व आंदोलन
**प्रभाव:**
- सरकारी एजेंसियों ने समझौता किया
- फॉर्च्यून 500 कंपनियां प्रभावित
-जारी जांच और निवारण
**पाठ:** पाइपलाइनों का सुरक्षित निर्माण; सॉफ़्टवेयर अखंडता सत्यापित करें; शून्य-विश्वास वास्तुकला।
---

## सुरक्षा परीक्षण रणनीतियाँ
### स्थैतिक अनुप्रयोग सुरक्षा परीक्षण (एसएएसटी)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### डायनामिक एप्लिकेशन सुरक्षा परीक्षण (डीएएसटी)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### निर्भरता स्कैनिंग
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### प्रवेश परीक्षण चेकलिस्ट
- [ ] एसक्यूएल इंजेक्शन परीक्षण
- [ ] XSS परीक्षण (प्रतिबिंबित, संग्रहीत, DOM-आधारित)
- [ ] सीएसआरएफ टोकन सत्यापन
- [ ] प्रमाणीकरण बायपास प्रयास
- [ ] प्राधिकरण जांच (ऊर्ध्वाधर/क्षैतिज विशेषाधिकार वृद्धि)
- [ ] दर सीमित सत्यापन
- [ ] सुरक्षा हेडर उपस्थिति
- [ ] एसएसएल/टीएलएस कॉन्फ़िगरेशन
- [ ] सत्र प्रबंधन समीक्षा
- [ ] त्रुटि प्रबंधन (कोई जानकारी लीक नहीं)
---

## सुरक्षा संसाधन
### OWASP टॉप 10 (2021)
1. टूटा हुआ अभिगम नियंत्रण
2. क्रिप्टोग्राफ़िक विफलताएँ
3. इंजेक्शन
4. असुरक्षित डिज़ाइन
5. सुरक्षा ग़लतफ़हमी
6. कमजोर और पुराने घटक
7. पहचान और प्रमाणीकरण विफलताएँ
8. सॉफ़्टवेयर और डेटा अखंडता विफलताएँ
9. सुरक्षा लॉगिंग और निगरानी विफलताएँ
10. सर्वर-साइड अनुरोध जालसाजी
### अनुशंसित उपकरण
- **स्टेटिक विश्लेषण**: सोनारक्यूब, सेमग्रेप, कोडक्यूएल
- **निर्भरता स्कैनिंग**: डिपेंडाबॉट, रेनोवेट, स्निक
- **गतिशील परीक्षण**: ओडब्ल्यूएएसपी जैप, बर्प सुइट
- **गुप्त जांच**: गिटलीक्स, ट्रफलहॉग
- **कंटेनर सुरक्षा**: ट्रिवी, क्लेयर, एंकर