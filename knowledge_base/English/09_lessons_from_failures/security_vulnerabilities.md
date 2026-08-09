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

# Security Vulnerabilities

This document consolidates common security vulnerabilities in software development, including injection attacks, unsafe code practices, and security mistakes.

---

## SQL Injection

SQL injection attacks occur when untrusted user input is improperly handled in database queries, allowing attackers to manipulate query logic, access unauthorized data, or modify database contents.

### Classic UNION-Based Injection

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Attack:**
```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Why It's Bad:**
- Exposes data from other tables
- Bypasses intended query logic
- Can extract sensitive information

**Better Approach:**
```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Prevention Strategies

1. **Use Parameterized Queries**: Never concatenate user input into SQL
2. **Input Validation**: Validate and sanitize all user input
3. **Least Privilege**: Database accounts should have minimal permissions
4. **ORM Usage**: Use Object-Relational Mappers that handle escaping
5. **Web Application Firewalls**: Deploy WAFs to detect injection attempts

---

## Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) attacks occur when attackers inject malicious scripts into web pages viewed by other users.

### Reflected XSS

**Bad Example (Vulnerable Code):**
```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Attack:**
```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Why It's Bad:**
- User input directly rendered without encoding
- Attacker can craft malicious URLs
- Session hijacking, credential theft possible

**Better Approach:**
```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Stored XSS

**Bad Example:**
```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Prevention Strategies

1. **Output Encoding**: Encode data based on context (HTML, JS, URL, CSS)
2. **Input Validation**: Reject or sanitize malicious input
3. **Content Security Policy**: Use CSP headers to restrict script sources
4. **HTTPOnly Cookies**: Prevent JavaScript access to session cookies
5. **Modern Frameworks**: Use React, Vue, Angular which auto-escape by default

---

## Memory Safety Issues

### Buffer Overflows

**Bad Example (C):**
```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problems:**
- Can overwrite adjacent memory
- May allow code execution attacks
- Causes undefined behavior

**Better Approach:**
```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Use-After-Free

**Bad Example (C++):**
```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Better Approach:**
```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Prevention Strategies

1. **Use Safe Languages**: Prefer Rust, Go, Java, Python over C/C++
2. **Smart Pointers**: Use RAII patterns in C++
3. **Bounds Checking**: Always validate array indices
4. **Static Analysis**: Use tools like Valgrind, AddressSanitizer
5. **Memory-Safe APIs**: Use safer standard library functions

---

## Authentication Mistakes

### Weak Password Policies

**Bad Example:**
```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problems:**
- Susceptible to brute force attacks
- Common passwords easily guessed
- Violates security best practices

**Better Approach:**
```python
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

### Storing Plaintext Passwords

**Bad Example:**
```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Better Approach:**
```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Prevention Strategies

1. **Strong Hashing**: Use bcrypt, Argon2, or scrypt for passwords
2. **Multi-Factor Authentication**: Require additional verification
3. **Rate Limiting**: Prevent brute force attacks
4. **Account Lockout**: Temporarily lock after failed attempts
5. **Secure Session Management**: Use secure, HTTP-only cookies

---

## Other Security Mistakes

### Hardcoded Secrets

**Bad Example:**
```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Better Approach:**
```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Insecure Direct Object References

**Bad Example:**
```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Better Approach:**
```python
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

### Missing Rate Limiting

**Bad Example:**
```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Better Approach:**
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Related Topics

- **AI/LLM Failures**: See `ai_llm_failures.md` for prompt injection and AI-specific security issues
- **Unsafe Code Patterns**: See code examples for memory safety and undefined behavior
- **Authentication Best Practices**: Implement proper auth flows and session management
- **Code Quality**: See `code_quality_issues.md` for secure coding practices

---

## Additional Security Vulnerabilities

### Command Injection

**What It Is:** Executing arbitrary system commands through unsanitized user input.

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Attack:**
```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Why It's Bad:**
- Attacker can execute any system command
- Potential for complete system compromise
- Data destruction, malware installation possible

**Better Approach:**
```python
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

**What It Is:** Accessing files outside intended directories using ../ sequences.

**Bad Example:**
```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Attack:**
```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Better Approach:**
```python
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

**What It Is:** Making the server make requests to unintended destinations.

**Bad Example:**
```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Attack:**
```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Better Approach:**
```python
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

## Cryptographic Mistakes

### Weak Hashing Algorithms

**Bad Example:**
```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Why It's Bad:**
- MD5 and SHA1 are cryptographically broken
- Fast to compute (enables brute force)
- Collision attacks demonstrated

**Better Approach:**
```python
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

### Hardcoded Encryption Keys

**Bad Example:**
```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Better Approach:**
```python
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

### Using ECB Mode

**Bad Example:**
```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Why It's Bad:**
- Identical plaintext blocks produce identical ciphertext
- Patterns in data are visible
- Famous "ECB penguin" demonstrates the problem

**Better Approach:**
```python
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

## API Security Issues

### Missing Input Validation

**Bad Example:**
```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Better Approach:**
```python
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

### Insecure API Authentication

**Bad Example:**
```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Better Approach:**
```python
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

### Missing Rate Limiting on APIs

**Bad Example:**
```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Better Approach:**
```python
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

## Security Headers and Configuration

### Missing Security Headers

**Bad Example:**
```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Better Approach:**
```python
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

### Insecure CORS Configuration

**Bad Example:**
```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Better Approach:**
```python
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

## Case Studies

### Case Study 1: Equifax Data Breach (2017)

**Incident:** Attackers exploited Apache Struts vulnerability to access personal data of 147 million people.

**Root Cause:**
- Unpatched software (CVE-2017-5638)
- No input validation on content-type header
- Insufficient network segmentation

**Impact:**
- $1.4 billion in costs
- Personal data exposed (SSN, birth dates, addresses)
- Massive reputational damage

**Lesson:** Keep dependencies updated; implement defense in depth.

### Case Study 2: Target Breach (2013)

**Incident:** Attackers stole 40 million credit card numbers.

**Root Cause:**
- Third-party vendor credentials compromised
- No network segmentation between vendor and payment systems
- Ignored security alerts

**Impact:**
- $202 million in costs
- CEO and CIO fired
- Payment system overhaul required

**Lesson:** Segment networks; monitor third-party access; respond to alerts.

### Case Study 3: SolarWinds Supply Chain Attack (2020)

**Incident:** Malicious code inserted into software updates affected 18,000+ organizations.

**Root Cause:**
- Compromised build system
- Signed malicious updates with valid certificates
- Lateral movement once inside networks

**Impact:**
- Government agencies compromised
- Fortune 500 companies affected
- Ongoing investigation and remediation

**Lesson:** Secure build pipelines; verify software integrity; zero-trust architecture.

---

## Security Testing Strategies

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

### Dependency Scanning

```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Penetration Testing Checklist

- [ ] SQL injection testing
- [ ] XSS testing (reflected, stored, DOM-based)
- [ ] CSRF token validation
- [ ] Authentication bypass attempts
- [ ] Authorization checks (vertical/horizontal privilege escalation)
- [ ] Rate limiting verification
- [ ] Security headers presence
- [ ] SSL/TLS configuration
- [ ] Session management review
- [ ] Error handling (no information leakage)

---

## Security Resources

### OWASP Top 10 (2021)
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery

### Recommended Tools
- **Static Analysis**: SonarQube, Semgrep, CodeQL
- **Dependency Scanning**: Dependabot, Renovate, Snyk
- **Dynamic Testing**: OWASP ZAP, Burp Suite
- **Secret Detection**: GitLeaks, TruffleHog
- **Container Security**: Trivy, Clair, Anchore
