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

# Athari za Usalama
Hati hii inaunganisha udhaifu wa kawaida wa kiusalama katika uundaji wa programu, ikiwa ni pamoja na mashambulizi ya sindano, mbinu zisizo salama za kanuni na makosa ya usalama.
---

## Sindano ya SQL
Mashambulizi ya sindano ya SQL hutokea wakati ingizo la mtumiaji asiyeaminika linaposhughulikiwa isivyo sahihi katika hoja za hifadhidata, kuruhusu washambuliaji kudhibiti mantiki ya hoja, kufikia data ambayo haijaidhinishwa, au kurekebisha maudhui ya hifadhidata.
### Sindano ya Kimsingi ya MUUNGANO
**Mfano Mbaya (Msimbo Hatarini):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Shambulio:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Kwa nini ni mbaya:**
- Huonyesha data kutoka kwa jedwali zingine
- Bypasses lengo query mantiki
- Inaweza kutoa taarifa nyeti
**Njia Bora:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Mikakati ya Kuzuia
1. **Tumia Hoji Zilizowekwa Vigezo**: Usiwahi kuunganisha ingizo la mtumiaji kwenye SQL
2. **Uthibitishaji wa Ingizo**: Thibitisha na usafishe ingizo zote za mtumiaji
3. **Mapendeleo Kidogo**: Akaunti za hifadhidata zinapaswa kuwa na ruhusa ndogo
4. **Matumizi ya ORM**: Tumia Ramani za Kitu-Mahusiano zinazoshughulikia kutoroka
5. **Ngome za Kulinda za Maombi ya Wavuti**: Tumia WAF ili kugundua majaribio ya kudunga
---

## Uandikaji wa Tovuti Mtambuka (XSS)
Mashambulizi ya Cross-Site Scripting (XSS) hutokea wakati wavamizi wanapoingiza hati hasidi kwenye kurasa za wavuti zinazotazamwa na watumiaji wengine.
### Iliakisiwa XSS
**Mfano Mbaya (Msimbo Hatarini):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Shambulio:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Kwa nini ni mbaya:**
- Ingizo la mtumiaji limetolewa moja kwa moja bila usimbaji
- Mshambulizi anaweza kutengeneza URL hasidi
- Utekaji nyara wa kikao, wizi wa sifa unawezekana
**Njia Bora:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Iliyohifadhiwa XSS
**Mfano Mbaya:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Mikakati ya Kuzuia
1. **Usimbaji wa Pato**: Weka msimbo data kulingana na muktadha (HTML, JS, URL, CSS)
2. **Uthibitishaji wa Ingizo**: Kataa au safisha ingizo hasidi
3. **Sera ya Usalama ya Maudhui**: Tumia vichwa vya CSP ili kuzuia vyanzo vya hati
4. **Vidakuzi vya HTTPPekee**: Zuia ufikiaji wa JavaScript kwa vidakuzi vya kipindi
5. **Mifumo ya Kisasa**: Tumia React, Vue, Angular ambayo hutoroka kiotomatiki kwa chaguomsingi
---

## Masuala ya Usalama wa Kumbukumbu
### Bafa Inafurika
**Mfano Mbaya (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Matatizo:**
- Inaweza kubatilisha kumbukumbu iliyo karibu
- Inaweza kuruhusu mashambulizi ya utekelezaji wa kanuni
- Husababisha tabia isiyobainishwa
**Njia Bora:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Tumia-Baada ya-Bure
**Mfano Mbaya (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Njia Bora:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Mikakati ya Kuzuia
1. **Tumia Lugha Salama**: Pendelea Kutu, Go, Java, Chatu kuliko C/C++
2. **Viashirio Mahiri**: Tumia ruwaza za RAII katika C++
3. **Kukagua Mipaka**: Thibitisha fahirisi za safu kila wakati
4. **Uchambuzi Tuli**: Tumia zana kama vile Valgrind, AddressSanitizer
5. **API za Kumbukumbu-Salama**: Tumia vipengele vya kawaida vya maktaba vilivyo salama zaidi
---

## Makosa ya Uthibitishaji
### Sera za Nenosiri dhaifu
**Mfano Mbaya:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Matatizo:**
- Inaweza kushambuliwa kwa nguvu ya kikatili
- Nywila za kawaida zinakisiwa kwa urahisi
- Inakiuka mbinu bora za usalama
**Njia Bora:**```python
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

### Kuhifadhi Manenosiri Matini
**Mfano Mbaya:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Njia Bora:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Mikakati ya Kuzuia
1. **Hashing Yenye Nguvu**: Tumia bcrypt, Argon2, au scrypt kwa manenosiri
2. **Uthibitishaji wa Mambo Mengi**: Inahitaji uthibitishaji wa ziada
3. **Kupunguza Viwango**: Zuia mashambulizi ya nguvu ya kinyama
4. **Kufungia Akaunti**: Funga kwa muda baada ya majaribio yasiyofaulu
5. **Udhibiti Salama wa Kipindi**: Tumia vidakuzi salama, vya HTTP pekee
---

## Makosa Mengine ya Usalama
### Siri Zenye Msimbo Ngumu
**Mfano Mbaya:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Njia Bora:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Marejeleo ya Kitu cha Moja kwa Moja kisicho salama
**Mfano Mbaya:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Njia Bora:**```python
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

### Kikomo cha Kiwango Kinachokosekana
**Mfano Mbaya:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Njia Bora:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Mada Zinazohusiana
**AI/LLM Imeshindwa**: Tazama`ai_llm_failures.md`kwa sindano ya papo hapo na masuala ya usalama mahususi ya AI
- **Miundo ya Misimbo Isiyo Salama**: Tazama mifano ya msimbo kwa usalama wa kumbukumbu na tabia isiyobainishwa
- **Mbinu Bora za Uthibitishaji**: Tekeleza mtiririko sahihi wa uthibitishaji na usimamizi wa kipindi
- **Ubora wa Msimbo**: Angalia`code_quality_issues.md`kwa mbinu salama za usimbaji
---

## Athari za Ziada za Usalama
### Sindano ya Amri
**Ilivyo:** Kutekeleza amri kiholela za mfumo kupitia uingizaji wa mtumiaji ambao haujaidhinishwa.
**Mfano Mbaya (Msimbo Hatarini):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Shambulio:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Kwa nini ni mbaya:**
- Mshambulizi anaweza kutekeleza amri yoyote ya mfumo
- Uwezo wa maelewano kamili ya mfumo
- Uharibifu wa data, usakinishaji wa programu hasidi unawezekana
**Njia Bora:**```python
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

### Upitishaji wa Njia
**Ni Nini:** Kupata faili nje ya saraka zilizokusudiwa kwa kutumia ../ mifuatano.
**Mfano Mbaya:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Shambulio:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Njia Bora:**```python
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

### Kughushi Ombi la Upande wa Seva (SSRF)
**Ilivyo:** Kufanya seva kufanya maombi kwa maeneo yasiyotarajiwa.
**Mfano Mbaya:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Shambulio:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Njia Bora:**```python
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

## Makosa ya Cryptographic
### Kanuni za Hashing dhaifu
**Mfano Mbaya:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Kwa nini ni mbaya:**
- MD5 na SHA1 zimevunjwa kificho
- Haraka kuhesabu (huwezesha nguvu ya kikatili)
- Mashambulizi ya mgongano yameonyeshwa
**Njia Bora:**```python
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

### Vifunguo vya Usimbaji Fiche Vigumu
**Mfano Mbaya:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Njia Bora:**```python
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

### Kwa kutumia Modi ya ECB
**Mfano Mbaya:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Kwa nini ni mbaya:**
- Vitalu vya maandishi wazi vinavyofanana hutoa maandishi ya siri yanayofanana
- Sampuli katika data zinaonekana
- Maarufu "ECB penguin" inaonyesha shida
**Njia Bora:**```python
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

## Masuala ya Usalama ya API
### Uthibitishaji wa Ingizo haupo
**Mfano Mbaya:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Njia Bora:**```python
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

### Uthibitishaji wa API isiyo salama
**Mfano Mbaya:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Njia Bora:**```python
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

### Kikomo cha Kiwango Kinachokosekana kwenye API
**Mfano Mbaya:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Njia Bora:**```python
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

## Vichwa vya Usalama na Usanidi
### Vijajuu vya Usalama Havipo
**Mfano Mbaya:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Njia Bora:**```python
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

### Usanidi wa CORS usio salama
**Mfano Mbaya:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Njia Bora:**```python
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

## Uchunguzi
### Uchunguzi Kifani 1: Uvunjaji Data wa Equifax (2017)
**Tukio:** Wavamizi walitumia hatari ya Apache Struts kufikia data ya kibinafsi ya watu milioni 147.
**Chanzo Cha msingi:**
- Programu ambayo haijachapishwa (CVE-2017-5638)
- Hakuna uthibitishaji wa ingizo kwenye kichwa cha aina ya yaliyomo
- Upungufu wa sehemu za mtandao
**Athari:**
- $1.4 bilioni kwa gharama
- Data ya kibinafsi imefichuliwa (SSN, tarehe za kuzaliwa, anwani)
- Uharibifu mkubwa wa sifa
**Somo:** Weka vitegemezi vilivyosasishwa; kutekeleza ulinzi kwa kina.
### Uchunguzi kifani 2: Ukiukaji Lengwa (2013)
**Tukio:** Wavamizi waliiba nambari milioni 40 za kadi za mkopo.
**Chanzo Cha msingi:**
- Kitambulisho cha mchuuzi wa mtu wa tatu kimeathiriwa
- Hakuna mgawanyiko wa mtandao kati ya muuzaji na mifumo ya malipo
- Arifa za usalama zilizopuuzwa
**Athari:**
- $202 milioni kwa gharama
- Mkurugenzi Mtendaji na CIO wafutwa kazi
- Urekebishaji wa mfumo wa malipo unahitajika
**Somo:** Mitandao ya sehemu; kufuatilia upatikanaji wa mtu wa tatu; kujibu arifa.
### Uchunguzi Kifani 3: Mashambulizi ya Msururu wa Ugavi wa SolarWinds (2020)
**Tukio:** Msimbo hasidi uliowekwa kwenye masasisho ya programu uliathiri mashirika 18,000+.
**Chanzo Cha msingi:**
- Mfumo wa ujenzi ulioathiriwa
- Sasisho hasidi zilizosainiwa na vyeti halali
- Harakati za baadaye mara moja ndani ya mitandao
**Athari:**
- Mashirika ya serikali kuathirika
- Bahati 500 makampuni walioathirika
- Uchunguzi unaoendelea na urekebishaji
**Somo:** Kulinda mabomba ya kujenga; thibitisha uadilifu wa programu; usanifu wa zero-trust.
---

## Mikakati ya Upimaji Usalama
### Jaribio la Usalama la Programu Isiyobadilika (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Jaribio la Usalama wa Programu Inayobadilika (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Uchanganuzi wa Kutegemea
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Orodha ya Kujaribu Kupenya
- [ ] Upimaji wa sindano ya SQL
- [ ] Upimaji wa XSS (ulioonyeshwa, kuhifadhiwa, kulingana na DOM)
- [ ] Uthibitishaji wa tokeni ya CSRF
- [ ] Majaribio ya kukwepa ya uthibitishaji
- [ ] Ukaguzi wa uidhinishaji (kupanda kwa upendeleo kwa wima/mlalo)
- [ ] Uthibitishaji unaopunguza viwango
- [ ] Uwepo wa vichwa vya usalama
- [ ] usanidi wa SSL/TLS
- [ ] Mapitio ya usimamizi wa kikao
- [ ] Ushughulikiaji wa hitilafu (hakuna uvujaji wa habari)
---

## Nyenzo za Usalama
### OWASP 10 Bora (2021)
1. Udhibiti Uliovunjwa wa Ufikiaji
2. Kushindwa kwa Cryptographic
3. Sindano
4. Usanifu usio salama
5. Mipangilio Mibaya ya Usalama
6. Vipengele Vinavyoweza Kuathirika na Vilivyopitwa na Wakati
7. Kushindwa kwa Utambulisho na Uthibitishaji
8. Kushindwa kwa Uadilifu wa Programu na Data
9. Usalama wa Kuingia na Kushindwa kwa Ufuatiliaji
10. Kughushi Ombi la Upande wa Seva
### Zana Zinazopendekezwa
- **Uchambuzi Tuli**: SonarQube, Semgrep, CodeQL
- **Uchanganuzi wa Utegemezi**: Dependabot, Rekebisha, Snyk
- **Jaribio la Nguvu**: OWASP ZAP, Burp Suite
- ** Ugunduzi wa Siri **: GitLeaks, TruffleHog
- ** Usalama wa chombo **: Trivy, Clair, Anchore