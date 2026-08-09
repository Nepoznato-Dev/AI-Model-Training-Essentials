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

# Güvenlik Açıkları
Bu belge, enjeksiyon saldırıları, güvenli olmayan kod uygulamaları ve güvenlik hataları dahil olmak üzere yazılım geliştirmedeki yaygın güvenlik açıklarını birleştirir.
---

## SQL Enjeksiyonu
SQL enjeksiyon saldırıları, güvenilmeyen kullanıcı girişinin veritabanı sorgularında uygunsuz şekilde işlenmesiyle meydana gelir ve saldırganların sorgu mantığını değiştirmesine, yetkisiz verilere erişmesine veya veritabanı içeriğini değiştirmesine olanak tanır.
### Klasik UNION Tabanlı Enjeksiyon
**Kötü Örnek (Hassas Kod):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Saldırı:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Neden Kötü:**
- Diğer tablolardaki verileri ortaya çıkarır
- Amaçlanan sorgu mantığını atlar
- Hassas bilgileri çıkarabilir
**Daha İyi Yaklaşım:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Önleme Stratejileri
1. **Parametreli Sorguları Kullanın**: Kullanıcı girişini hiçbir zaman SQL'de birleştirmeyin
2. **Giriş Doğrulaması**: Tüm kullanıcı girişlerini doğrulayın ve temizleyin
3. **En Az Ayrıcalık**: Veritabanı hesapları minimum izinlere sahip olmalıdır
4. **ORM Kullanımı**: Kaçmayı yöneten Nesne İlişkisel Eşleyicileri kullanın
5. **Web Uygulaması Güvenlik Duvarları**: Ekleme girişimlerini tespit etmek için WAF'ları dağıtın
---

## Siteler Arası Komut Dosyası Çalıştırma (XSS)
Siteler Arası Komut Dosyası Çalıştırma (XSS) saldırıları, saldırganların diğer kullanıcılar tarafından görüntülenen web sayfalarına kötü amaçlı komut dosyaları yerleştirmesiyle meydana gelir.
### Yansıyan XSS
**Kötü Örnek (Hassas Kod):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Saldırı:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Neden Kötü:**
- Kullanıcı girişi kodlama olmadan doğrudan işlenir
- Saldırgan kötü amaçlı URL'ler oluşturabilir
- Oturumun ele geçirilmesi, kimlik bilgilerinin çalınması mümkün
**Daha İyi Yaklaşım:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Saklanan XSS
**Kötü Örnek:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Önleme Stratejileri
1. **Çıktı Kodlaması**: Verileri bağlama göre kodlayın (HTML, JS, URL, CSS)
2. **Giriş Doğrulaması**: Kötü niyetli girişi reddedin veya temizleyin
3. **İçerik Güvenliği Politikası**: Komut dosyası kaynaklarını kısıtlamak için CSP başlıklarını kullanın
4. **Yalnızca HTTP Çerezleri**: JavaScript'in oturum çerezlerine erişimini engelleyin
5. **Modern Çerçeveler**: Varsayılan olarak otomatik çıkış yapan React, Vue, Angular'ı kullanın
---

## Bellek Güvenliği Sorunları
### Arabellek Taşmaları
**Kötü Örnek (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Sorunlar:**
- Bitişik belleğin üzerine yazabilir
- Kod yürütme saldırılarına izin verebilir
- Tanımlanamayan davranışa neden olur
**Daha İyi Yaklaşım:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Ücretsiz Sonra Kullan
**Kötü Örnek (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Daha İyi Yaklaşım:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Önleme Stratejileri
1. **Güvenli Diller Kullanın**: C/C++ yerine Rust, Go, Java ve Python'u tercih edin
2. **Akıllı İşaretçiler**: C++'da RAII modellerini kullanın
3. **Sınır Kontrolü**: Dizi indekslerini her zaman doğrulayın
4. **Statik Analiz**: Valgrind, AdresSanitizer gibi araçları kullanın
5. **Bellek açısından Güvenli API'ler**: Daha güvenli standart kitaplık işlevlerini kullanın
---

## Kimlik Doğrulama Hataları
### Zayıf Şifre Politikaları
**Kötü Örnek:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Sorunlar:**
- Kaba kuvvet saldırılarına karşı duyarlı
- Yaygın olarak kullanılan şifreler kolayca tahmin edilebilir
- En iyi güvenlik uygulamalarını ihlal ediyor
**Daha İyi Yaklaşım:**```python
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

### Düz Metin Parolalarını Saklama
**Kötü Örnek:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Daha İyi Yaklaşım:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Önleme Stratejileri
1. **Güçlü Karma**: Parolalar için bcrypt, Argon2 veya scrypt kullanın
2. **Çok Faktörlü Kimlik Doğrulama**: Ek doğrulama gerektirir
3. **Hız Sınırlama**: Kaba kuvvet saldırılarını önleyin
4. **Hesap Kilitleme**: Başarısız denemelerden sonra geçici olarak kilitlenir
5. **Güvenli Oturum Yönetimi**: Güvenli, yalnızca HTTP çerezlerini kullanın
---

## Diğer Güvenlik Hataları
### Sabit Kodlanmış Sırlar
**Kötü Örnek:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Daha İyi Yaklaşım:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Güvenli Olmayan Doğrudan Nesne Referansları
**Kötü Örnek:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Daha İyi Yaklaşım:**```python
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

### Eksik Hız Sınırlaması
**Kötü Örnek:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Daha İyi Yaklaşım:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## İlgili Konular
- **AI/LLM Hataları**: Hızlı enjeksiyon ve yapay zekaya özgü güvenlik sorunları için `ai_llm_failures.md`'ye bakın
- **Güvenli Olmayan Kod Kalıpları**: Bellek güvenliği ve tanımsız davranış için kod örneklerine bakın
- **Kimlik Doğrulama İçin En İyi Uygulamalar**: Uygun kimlik doğrulama akışlarını ve oturum yönetimini uygulayın
- **Kod Kalitesi**: Güvenli kodlama uygulamaları için `code_quality_issues.md`'ye bakın
---

## Ek Güvenlik Açıkları
### Komut Ekleme
**Nedir:** Temizlenmemiş kullanıcı girişi aracılığıyla rastgele sistem komutlarının yürütülmesi.
**Kötü Örnek (Hassas Kod):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Saldırı:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Neden Kötü:**
- Saldırgan herhangi bir sistem komutunu çalıştırabilir
- Sistemin tamamen tehlikeye girme potansiyeli
- Veri imhası, kötü amaçlı yazılım kurulumu mümkün
**Daha İyi Yaklaşım:**```python
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

### Yol Geçişi
**Nedir:** ../ dizilerini kullanarak amaçlanan dizinlerin dışındaki dosyalara erişme.
**Kötü Örnek:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Saldırı:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Daha İyi Yaklaşım:**```python
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

### Sunucu Tarafı İstek Sahteciliği (SSRF)
**Nedir:** Sunucunun istenmeyen hedeflere istekte bulunmasını sağlamak.
**Kötü Örnek:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Saldırı:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Daha İyi Yaklaşım:**```python
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

## Şifreleme Hataları
### Zayıf Karma Algoritmalar
**Kötü Örnek:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Neden Kötü:**
- MD5 ve SHA1 kriptografik olarak bozuk
- Hızlı hesaplama (kaba kuvvete olanak sağlar)
- Çarpışma saldırıları gösterildi
**Daha İyi Yaklaşım:**```python
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

### Sabit Kodlanmış Şifreleme Anahtarları
**Kötü Örnek:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Daha İyi Yaklaşım:**```python
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

### ECB Modunu Kullanma
**Kötü Örnek:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Neden Kötü:**
- Aynı düz metin blokları aynı şifreli metni üretir
- Verilerdeki modeller görülebilir
- Ünlü "ECB pengueni" sorunu gösteriyor
**Daha İyi Yaklaşım:**```python
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

## API Güvenlik Sorunları
### Eksik Giriş Doğrulaması
**Kötü Örnek:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Daha İyi Yaklaşım:**```python
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

### Güvenli Olmayan API Kimlik Doğrulaması
**Kötü Örnek:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Daha İyi Yaklaşım:**```python
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

### API'lerde Eksik Hız Sınırlaması
**Kötü Örnek:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Daha İyi Yaklaşım:**```python
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

## Güvenlik Başlıkları ve Yapılandırması
### Eksik Güvenlik Başlıkları
**Kötü Örnek:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Daha İyi Yaklaşım:**```python
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

### Güvenli Olmayan CORS Yapılandırması
**Kötü Örnek:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Daha İyi Yaklaşım:**```python
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

## Vaka Çalışmaları
### Örnek Olay 1: Equifax Veri İhlali (2017)
**Olay:** Saldırganlar Apache Struts güvenlik açığından yararlanarak 147 milyon kişinin kişisel verilerine erişti.
**Temel Neden:**
- Yama uygulanmamış yazılım (CVE-2017-5638)
- İçerik türü başlığında giriş doğrulaması yok
- Yetersiz ağ bölümlemesi
**Etki:**
- 1,4 milyar dolar maliyet
- Açığa çıkan kişisel veriler (SSN, doğum tarihleri, adresler)
- Büyük itibar kaybı
**Ders:** Bağımlılıkları güncel tutun; Savunmayı derinlemesine uygulayın.
### Örnek Olay 2: Hedef İhlali (2013)
**Olay:** Saldırganlar 40 milyon kredi kartı numarasını çaldı.
**Temel Neden:**
- Üçüncü taraf satıcı kimlik bilgileri tehlikeye girdi
- Satıcı ve ödeme sistemleri arasında ağ segmentasyonu yok
- Göz ardı edilen güvenlik uyarıları
**Etki:**
- 202 milyon dolar maliyet
- CEO ve CIO kovuldu
- Ödeme sisteminin revizyonu gerekiyor
**Ders:** Segment ağları; üçüncü taraf erişimini izlemek; uyarılara yanıt verin.
### Örnek Olay 3: SolarWinds Tedarik Zinciri Saldırısı (2020)
**Olay:** Yazılım güncellemelerine eklenen kötü amaçlı kod 18.000'den fazla kuruluşu etkiledi.
**Temel Neden:**
- Güvenliği ihlal edilmiş yapı sistemi
- Geçerli sertifikalarla imzalanmış kötü amaçlı güncellemeler
- Ağların içine girdikten sonra yanal hareket
**Etki:**
- Devlet kurumları tehlikeye girdi
- Fortune 500 şirketleri etkilendi
- Devam eden soruşturma ve iyileştirme
**Ders:** Güvenli derleme ardışık düzenleri; yazılım bütünlüğünü doğrulayın; sıfır güven mimarisi.
---

## Güvenlik Test Stratejileri
### Statik Uygulama Güvenliği Testi (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Dinamik Uygulama Güvenliği Testi (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Bağımlılık Taraması
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Sızma Testi Kontrol Listesi
- [ ] SQL enjeksiyon testi
- [ ] XSS testi (yansıyan, depolanan, DOM tabanlı)
- [ ] CSRF belirteci doğrulaması
- [ ] Kimlik doğrulamayı atlama girişimleri
- [ ] Yetkilendirme kontrolleri (dikey/yatay ayrıcalık yükseltme)
- [ ] Hız sınırlama doğrulaması
- [ ] Güvenlik başlıklarının varlığı
- [ ] SSL/TLS yapılandırması
- [ ] Oturum yönetimi incelemesi
- [ ] Hata yönetimi (bilgi sızıntısı yok)
---

## Güvenlik Kaynakları
### OWASP İlk 10 (2021)
1. Bozuk Erişim Kontrolü
2. Şifreleme Hataları
3. Enjeksiyon
4. Güvenli Olmayan Tasarım
5. Güvenlik Yanlış Yapılandırması
6. Savunmasız ve Güncel Olmayan Bileşenler
7. Tanımlama ve Kimlik Doğrulama Hataları
8. Yazılım ve Veri Bütünlüğü Arızaları
9. Güvenlik Günlüğü ve İzleme Arızaları
10. Sunucu Tarafı İstek Sahteciliği
### Önerilen Araçlar
- **Statik Analiz**: SonarQube, Semgrep, CodeQL
- **Bağımlılık Taraması**: Dependabot, Renovate, Snyk
- **Dinamik Test**: OWASP ZAP, Burp Suite
- **Gizli Tespit**: GitLeaks, TruffleHog
- **Konteyner Güvenliği**: Trivy, Clair, Anchore