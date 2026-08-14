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
# Mga Kahinaan sa Seguridad
Pinagsasama-sama ng dokumentong ito ang mga karaniwang kahinaan sa seguridad sa pagbuo ng software, kabilang ang mga pag-atake sa pag-iniksyon, hindi ligtas na mga kasanayan sa code, at mga pagkakamali sa seguridad.
---

## SQL Injection
Nangyayari ang mga pag-atake ng SQL injection kapag ang hindi pinagkakatiwalaang input ng user ay hindi wastong pinangangasiwaan sa mga query sa database, na nagpapahintulot sa mga umaatake na manipulahin ang lohika ng query, i-access ang hindi awtorisadong data, o baguhin ang mga nilalaman ng database.
### Classic UNION-Based Injection
**Maling Halimbawa (Vulnerable Code):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Atake:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Bakit Masama:**
- Inilalantad ang data mula sa iba pang mga talahanayan
- Mga bypass na nilalayong lohika ng query
- Maaaring kunin ang sensitibong impormasyon
**Mas mahusay na Diskarte:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Mga Istratehiya sa Pag-iwas
1. **Gumamit ng Mga Parameterized na Query**: Huwag kailanman pagsamahin ang input ng user sa SQL
2. **Input Validation**: I-validate at i-sanitize ang lahat ng input ng user
3. **Least Privilege**: Ang mga database account ay dapat na may kaunting mga pahintulot
4. **ORM Usage**: Gumamit ng Object-Relational Mappers na humahawak ng escaping
5. **Web Application Firewalls**: I-deploy ang mga WAF upang matukoy ang mga pagtatangkang mag-iniksyon
---

## Cross-Site Scripting (XSS)
Nagaganap ang mga pag-atake ng Cross-Site Scripting (XSS) kapag ang mga umaatake ay nag-inject ng mga nakakahamak na script sa mga web page na tiningnan ng ibang mga user.
### Sinasalamin ang XSS
**Maling Halimbawa (Vulnerable Code):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Atake:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Bakit Masama:**
- Direktang nai-render ang input ng user nang walang pag-encode
- Maaaring gumawa ang attacker ng mga nakakahamak na URL
- Pag-hijack ng session, posibleng pagnanakaw ng kredensyal
**Mas mahusay na Diskarte:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Nakaimbak na XSS
**Masama Halimbawa:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Mga Istratehiya sa Pag-iwas
1. **Output Encoding**: I-encode ang data batay sa konteksto (HTML, JS, URL, CSS)
2. **Input Validation**: Tanggihan o i-sanitize ang malisyosong input
3. **Patakaran sa Seguridad ng Nilalaman**: Gumamit ng mga header ng CSP upang paghigpitan ang mga source ng script
4. **HTTOnly Cookies**: Pigilan ang JavaScript na access sa session cookies
5. **Modern Frameworks**: Gumamit ng React, Vue, Angular na auto-escape bilang default
---

## Mga Isyu sa Kaligtasan ng Memory
### Umaapaw ang Buffer
**Maling Halimbawa (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Mga Problema:**
- Maaaring i-overwrite ang katabing memory
- Maaaring payagan ang mga pag-atake sa pagpapatupad ng code
- Nagdudulot ng hindi natukoy na pag-uugali
**Mas mahusay na Diskarte:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Gamitin-Pagkatapos-Libre
**Masamang Halimbawa (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Mas mahusay na Diskarte:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Mga Istratehiya sa Pag-iwas
1. **Gumamit ng Mga Ligtas na Wika**: Mas gusto ang Rust, Go, Java, Python kaysa sa C/C++
2. **Smart Pointer**: Gumamit ng mga pattern ng RAII sa C++
3. **Bounds Checking**: Palaging i-validate ang mga indeks ng array
4. **Static Analysis**: Gumamit ng mga tool tulad ng Valgrind, AddressSanitizer
5. **Memory-Safe API**: Gumamit ng mas ligtas na karaniwang mga function ng library
---

## Mga Pagkakamali sa Pagpapatunay
### Mahina ang Mga Patakaran sa Password
**Masama Halimbawa:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Mga Problema:**
- Madaling kapitan sa mga pag-atake ng malupit na puwersa
- Ang mga karaniwang password ay madaling mahulaan
- Lumalabag sa pinakamahuhusay na kagawian sa seguridad
**Mas mahusay na Diskarte:**```python
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

### Pag-iimbak ng Mga Plaintext na Password
**Masama Halimbawa:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Mas mahusay na Diskarte:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Mga Istratehiya sa Pag-iwas
1. **Strong Hashing**: Gumamit ng bcrypt, Argon2, o scrypt para sa mga password
2. **Multi-Factor Authentication**: Nangangailangan ng karagdagang pag-verify
3. **Paglilimita sa Rate**: Pigilan ang mga malupit na pag-atake
4. **Account Lockout**: Pansamantalang i-lock pagkatapos ng mga nabigong pagtatangka
5. **Secure Session Management**: Gumamit ng secure, HTTP-only na cookies
---

## Iba pang Mga Pagkakamali sa Seguridad
### Mga Lihim na Naka-hardcode
**Masama Halimbawa:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Mas mahusay na Diskarte:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Mga Di-Secure na Direktang Mga Sanggunian sa Bagay
**Masama Halimbawa:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Mas mahusay na Diskarte:**```python
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

### Nawawalang Paglilimita sa Rate
**Masama Halimbawa:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Mas mahusay na Diskarte:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Mga Kaugnay na Paksa
- **AI/LLM Failures**: Tingnan ang`ai_llm_failures.md`para sa agarang pag-iniksyon at mga isyu sa seguridad na partikular sa AI
- **Mga Pattern ng Hindi Ligtas na Code**: Tingnan ang mga halimbawa ng code para sa kaligtasan ng memorya at hindi natukoy na gawi
- **Pinakamahuhusay na Kasanayan sa Pagpapatotoo**: Ipatupad ang mga wastong daloy ng auth at pamamahala ng session
- **Marka ng Code**: Tingnan ang`code_quality_issues.md`para sa mga secure na kasanayan sa coding
---

## Karagdagang Mga Kahinaan sa Seguridad
### Command Injection
**Ano Ito:** Pagpapatupad ng mga arbitraryong utos ng system sa pamamagitan ng hindi nalinis na input ng user.
**Maling Halimbawa (Vulnerable Code):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Atake:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Bakit Masama:**
- Maaaring isagawa ng attacker ang anumang utos ng system
- Potensyal para sa kumpletong kompromiso ng system
- Pagkasira ng data, posibleng pag-install ng malware
**Mas mahusay na Diskarte:**```python
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

### Path Traversal
**Ano Ito:** Pag-access sa mga file sa labas ng mga inilaan na direktoryo gamit ang ../ sequences.
**Masama Halimbawa:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Atake:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Mas mahusay na Diskarte:**```python
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

### Server-Side Request Forgery (SSRF)
**Ano Ito:** Paggawa ng mga kahilingan sa server sa mga hindi nilalayong destinasyon.
**Masama Halimbawa:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Atake:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Mas mahusay na Diskarte:**```python
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

## Mga Pagkakamali sa Cryptographic
### Mahinang Hashing Algorithm
**Masama Halimbawa:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Bakit Masama:**
- MD5 at SHA1 ay cryptographically sira
- Mabilis na magcompute (nagpapagana ng brute force)
- Nagpakita ng mga pag-atake ng banggaan
**Mas mahusay na Diskarte:**```python
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

### Mga Hardcode na Encryption Key
**Masama Halimbawa:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Mas mahusay na Diskarte:**```python
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

### Gamit ang ECB Mode
**Masama Halimbawa:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Bakit Masama:**
- Ang magkaparehong plaintext block ay gumagawa ng magkaparehong ciphertext
- Nakikita ang mga pattern sa data
- Ang sikat na "ECB penguin" ay nagpapakita ng problema
**Mas mahusay na Diskarte:**```python
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

## Mga Isyu sa Seguridad ng API
### Nawawalang Input Validation
**Masama Halimbawa:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Mas mahusay na Diskarte:**```python
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

### Hindi Secure na Pagpapatotoo ng API
**Masama Halimbawa:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Mas mahusay na Diskarte:**```python
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

### Nawawalang Paglilimita sa Rate sa mga API
**Masama Halimbawa:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Mas mahusay na Diskarte:**```python
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

## Mga Header at Configuration ng Seguridad
### Nawawalang Security Header
**Masama Halimbawa:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Mas mahusay na Diskarte:**```python
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

### Hindi Secure na Configuration ng CORS
**Masama Halimbawa:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Mas mahusay na Diskarte:**```python
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

## Pag-aaral ng Kaso
### Pag-aaral ng Kaso 1: Equifax Data Breach (2017)
**Insidente:** Sinamantala ng mga attacker ang kahinaan ng Apache Struts upang ma-access ang personal na data ng 147 milyong tao.
**Ugat Dahilan:**
- Unpatched software (CVE-2017-5638)
- Walang pagpapatunay ng input sa header ng uri ng nilalaman
- Hindi sapat na segmentasyon ng network
**Epekto:**
- $1.4 bilyon sa mga gastos
- Nalantad ang personal na data (SSN, mga petsa ng kapanganakan, mga address)
- Napakalaking pinsala sa reputasyon
**Aralin:** Panatilihing na-update ang mga dependency; ipatupad ang depensa nang malalim.
### Pag-aaral ng Kaso 2: Target na Paglabag (2013)
**Insidente:** Ninakaw ng mga umaatake ang 40 milyong numero ng credit card.
**Ugat Dahilan:**
- Nakompromiso ang mga kredensyal ng third-party na vendor
- Walang network segmentation sa pagitan ng vendor at mga sistema ng pagbabayad
- Binalewala ang mga alerto sa seguridad
**Epekto:**
- $202 milyon sa mga gastos
- Ang CEO at CIO ay tinanggal
- Kinakailangan ang pagsasaayos ng sistema ng pagbabayad
**Aralin:** Mga network ng segment; subaybayan ang pag-access ng third-party; tumugon sa mga alerto.
### Pag-aaral ng Kaso 3: SolarWinds Supply Chain Attack (2020)
**Insidente:** Ang nakakahamak na code na inilagay sa mga update sa software ay nakaapekto sa 18,000+ organisasyon.
**Ugat Dahilan:**
- Nakompromiso ang build system
- Nilagdaan ang mga nakakahamak na update na may wastong mga sertipiko
- Lateral na paggalaw minsan sa loob ng mga network
**Epekto:**
- Nakompromiso ang mga ahensya ng gobyerno
- Fortune 500 kumpanya na apektado
- Patuloy na pagsisiyasat at remediation
**Aralin:** Secure build pipelines; i-verify ang integridad ng software; arkitektura na walang tiwala.
---

## Mga Istratehiya sa Pagsubok sa Seguridad
### Static Application Security Testing (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Dynamic Application Security Testing (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Pag-scan ng Dependency
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Checklist ng Pagsubok sa Pagpasok
- [ ] Pagsubok ng SQL injection
- [ ] Pagsubok sa XSS (naipakita, inimbak, batay sa DOM)
- [ ] CSRF token validation
- [ ] Mga pagtatangka sa pag-bypass sa pagpapatotoo
- [ ] Mga pagsusuri sa awtorisasyon (vertical/horizontal privilege escalation)
- [ ] Pagpapatunay na naglilimita sa rate
- [ ] Presensya ng mga header ng seguridad
- [ ] SSL/TLS configuration
- [ ] Pagsusuri sa pamamahala ng session
- [ ] Error sa paghawak (walang pagtagas ng impormasyon)
---

## Mga Mapagkukunan ng Seguridad
### Nangungunang 10 ng OWASP (2021)
1. Sirang Access Control
2. Mga Pagkabigo sa Cryptographic
3. Iniksyon
4. Insecure na Disenyo
5. Maling configuration ng Seguridad
6. Mga Mahina at Lumang Bahagi
7. Mga Pagkabigo sa Pagkilala at Pagpapatunay
8. Mga Pagkabigo sa Integridad ng Software at Data
9. Mga Pagkabigo sa Pag-log at Pagsubaybay sa Seguridad
10. Pamemeke ng Kahilingan sa Gilid ng Server
### Mga Inirerekomendang Tool
- **Static Analysis**: SonarQube, Semgrep, CodeQL
- **Pag-scan ng Dependency**: Dependabot, Renovate, Snyk
- **Dynamic na Pagsusuri**: OWASP ZAP, Burp Suite
- **Secret Detection**: GitLeaks, TruffleHog
- **Seguridad ng Container**: Trivy, Clair, Anchore