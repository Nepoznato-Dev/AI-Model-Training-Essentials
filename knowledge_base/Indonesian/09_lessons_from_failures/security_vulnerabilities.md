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
# Kerentanan Keamanan
Dokumen ini mengkonsolidasikan kerentanan keamanan umum dalam pengembangan perangkat lunak, termasuk serangan injeksi, praktik kode yang tidak aman, dan kesalahan keamanan.
---

## Injeksi SQL
Serangan injeksi SQL terjadi ketika input pengguna yang tidak dipercaya tidak ditangani dengan benar dalam kueri database, sehingga memungkinkan penyerang memanipulasi logika kueri, mengakses data yang tidak sah, atau mengubah konten database.
### Injeksi Klasik Berbasis UNION
**Contoh Buruk (Kode Rentan):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Menyerang:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Mengapa Ini Buruk:**
- Mengekspos data dari tabel lain
- Melewati logika kueri yang dimaksudkan
- Dapat mengekstrak informasi sensitif
**Pendekatan yang Lebih Baik:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Strategi Pencegahan
1. **Gunakan Kueri Parameterisasi**: Jangan pernah menggabungkan input pengguna ke dalam SQL
2. **Validasi Input**: Memvalidasi dan membersihkan semua input pengguna
3. **Hak Istimewa Terkecil**: Akun database harus memiliki izin minimal
4. **Penggunaan ORM**: Gunakan Pemeta Relasional Objek yang menangani pelolosan
5. **Firewall Aplikasi Web**: Menerapkan WAF untuk mendeteksi upaya injeksi
---

## Pembuatan Skrip Lintas Situs (XSS)
Serangan Cross-Site Scripting (XSS) terjadi ketika penyerang menyuntikkan skrip berbahaya ke halaman web yang dilihat oleh pengguna lain.
### Mencerminkan XSS
**Contoh Buruk (Kode Rentan):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Menyerang:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Mengapa Ini Buruk:**
- Input pengguna langsung diberikan tanpa pengkodean
- Penyerang dapat membuat URL berbahaya
- Pembajakan sesi, kemungkinan pencurian kredensial
**Pendekatan yang Lebih Baik:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS Tersimpan
**Contoh Buruk:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Strategi Pencegahan
1. **Pengkodean Keluaran**: Mengkodekan data berdasarkan konteks (HTML, JS, URL, CSS)
2. **Validasi Input**: Menolak atau membersihkan input berbahaya
3. **Kebijakan Keamanan Konten**: Gunakan header CSP untuk membatasi sumber skrip
4. **HTTPOnly Cookies**: Mencegah akses JavaScript ke cookie sesi
5. **Kerangka Kerja Modern**: Gunakan React, Vue, Angular yang otomatis lolos secara default
---

## Masalah Keamanan Memori
### Buffer Melimpah
**Contoh Buruk (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Masalah:**
- Dapat menimpa memori yang berdekatan
- Mungkin mengizinkan serangan eksekusi kode
- Menyebabkan perilaku tidak terdefinisi
**Pendekatan yang Lebih Baik:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Gunakan-Setelah-Gratis
**Contoh Buruk (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Pendekatan yang Lebih Baik:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Strategi Pencegahan
1. **Gunakan Bahasa Aman**: Lebih suka Rust, Go, Java, Python daripada C/C++
2. **Smart Pointer**: Gunakan pola RAII di C++
3. **Pemeriksaan Batas**: Selalu validasi indeks array
4. **Analisis Statis**: Gunakan alat seperti Valgrind, AddressSanitizer
5. **API Aman Memori**: Gunakan fungsi perpustakaan standar yang lebih aman
---

## Kesalahan Otentikasi
### Kebijakan Kata Sandi Lemah
**Contoh Buruk:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Masalah:**
- Rentan terhadap serangan brute force
- Kata sandi umum mudah ditebak
- Melanggar praktik terbaik keamanan
**Pendekatan yang Lebih Baik:**```python
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

### Menyimpan Kata Sandi Teks Biasa
**Contoh Buruk:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Pendekatan yang Lebih Baik:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Strategi Pencegahan
1. **Hashing Kuat**: Gunakan bcrypt, Argon2, atau scrypt untuk kata sandi
2. **Otentikasi Multi-Faktor**: Memerlukan verifikasi tambahan
3. **Pembatasan Kecepatan**: Mencegah serangan brute force
4. **Penguncian Akun**: Mengunci sementara setelah upaya gagal
5. **Manajemen Sesi Aman**: Gunakan cookie aman khusus HTTP
---

## Kesalahan Keamanan Lainnya
### Rahasia yang di-hardcode
**Contoh Buruk:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Pendekatan yang Lebih Baik:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Referensi Objek Langsung Tidak Aman
**Contoh Buruk:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Pendekatan yang Lebih Baik:**```python
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

### Batasan Tarif Tidak Ada
**Contoh Buruk:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Pendekatan yang Lebih Baik:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Topik Terkait
- **Kegagalan AI/LLM**: Lihat`ai_llm_failures.md`untuk injeksi cepat dan masalah keamanan khusus AI
- **Pola Kode Tidak Aman**: Lihat contoh kode untuk keamanan memori dan perilaku tidak terdefinisi
- **Praktik Terbaik Otentikasi**: Menerapkan alur autentikasi dan manajemen sesi yang tepat
- **Kualitas Kode**: Lihat`code_quality_issues.md`untuk praktik pengkodean yang aman
---

## Kerentanan Keamanan Tambahan
### Perintah Injeksi
**Apa Artinya:** Menjalankan perintah sistem sewenang-wenang melalui masukan pengguna yang tidak bersih.
**Contoh Buruk (Kode Rentan):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Menyerang:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Mengapa Ini Buruk:**
- Penyerang dapat menjalankan perintah sistem apa pun
- Potensi kompromi sistem yang lengkap
- Penghancuran data, kemungkinan pemasangan malware
**Pendekatan yang Lebih Baik:**```python
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

### Penjelajahan Jalur
**Apa Artinya:** Mengakses file di luar direktori yang dituju menggunakan urutan ../.
**Contoh Buruk:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Menyerang:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Pendekatan yang Lebih Baik:**```python
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

### Pemalsuan Permintaan Sisi Server (SSRF)
**Apa Artinya:** Membuat server membuat permintaan ke tujuan yang tidak diinginkan.
**Contoh Buruk:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Menyerang:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Pendekatan yang Lebih Baik:**```python
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

## Kesalahan Kriptografi
### Algoritma Hashing Lemah
**Contoh Buruk:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Mengapa Ini Buruk:**
- MD5 dan SHA1 rusak secara kriptografis
- Cepat untuk menghitung (mengaktifkan kekerasan)
- Serangan tabrakan ditunjukkan
**Pendekatan yang Lebih Baik:**```python
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

### Kunci Enkripsi Hardcode
**Contoh Buruk:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Pendekatan yang Lebih Baik:**```python
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

### Menggunakan Mode ECB
**Contoh Buruk:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Mengapa Ini Buruk:**
- Blok teks biasa yang identik menghasilkan teks tersandi yang identik
- Pola dalam data terlihat
- "Penguin ECB" yang terkenal menunjukkan masalahnya
**Pendekatan yang Lebih Baik:**```python
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

## Masalah Keamanan API
### Validasi Masukan Tidak Ada
**Contoh Buruk:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Pendekatan yang Lebih Baik:**```python
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

### Otentikasi API tidak aman
**Contoh Buruk:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Pendekatan yang Lebih Baik:**```python
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

### Batasan Tarif pada API Tidak Ada
**Contoh Buruk:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Pendekatan yang Lebih Baik:**```python
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

## Header dan Konfigurasi Keamanan
### Header Keamanan Tidak Ada
**Contoh Buruk:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Pendekatan yang Lebih Baik:**```python
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

### Konfigurasi CORS Tidak Aman
**Contoh Buruk:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Pendekatan yang Lebih Baik:**```python
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

## Studi Kasus
### Studi Kasus 1: Pelanggaran Data Equifax (2017)
**Insiden:** Penyerang mengeksploitasi kerentanan Apache Struts untuk mengakses data pribadi 147 juta orang.
**Akar Penyebab:**
- Perangkat lunak yang belum ditambal (CVE-2017-5638)
- Tidak ada validasi input pada header tipe konten
- Segmentasi jaringan tidak memadai
**Dampak:**
- Biaya $1,4 miliar
- Data pribadi terekspos (SSN, tanggal lahir, alamat)
- Kerusakan reputasi besar-besaran
**Pelajaran:** Terus perbarui dependensi; melaksanakan pertahanan secara mendalam.
### Studi Kasus 2: Pelanggaran Target (2013)
**Insiden:** Penyerang mencuri 40 juta nomor kartu kredit.
**Akar Penyebab:**
- Kredensial vendor pihak ketiga dikompromikan
- Tidak ada segmentasi jaringan antara vendor dan sistem pembayaran
- Peringatan keamanan diabaikan
**Dampak:**
- Biaya $202 juta
- CEO dan CIO dipecat
- Diperlukan perombakan sistem pembayaran
**Pelajaran:** Segmentasikan jaringan; memantau akses pihak ketiga; merespons peringatan.
### Studi Kasus 3: Serangan Rantai Pasokan SolarWinds (2020)
**Insiden:** Kode berbahaya yang dimasukkan ke dalam pembaruan perangkat lunak memengaruhi 18.000+ organisasi.
**Akar Penyebab:**
- Sistem pembangunan yang dikompromikan
- Menandatangani pembaruan berbahaya dengan sertifikat yang valid
- Gerakan lateral saat berada di dalam jaringan
**Dampak:**
- Instansi pemerintah berkompromi
- Perusahaan Fortune 500 terkena dampaknya
- Investigasi dan remediasi yang sedang berlangsung
**Pelajaran:** Mengamankan pipeline build; memverifikasi integritas perangkat lunak; arsitektur tanpa kepercayaan.
---

## Strategi Pengujian Keamanan
### Pengujian Keamanan Aplikasi Statis (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Pengujian Keamanan Aplikasi Dinamis (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Pemindaian Ketergantungan
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Daftar Periksa Pengujian Penetrasi
- [ ] Pengujian injeksi SQL
- [ ] Pengujian XSS (dicerminkan, disimpan, berbasis DOM)
- [ ] Validasi token CSRF
- [ ] Upaya bypass autentikasi
- [ ] Pemeriksaan otorisasi (eskalasi hak istimewa vertikal/horizontal)
- [ ] Verifikasi pembatasan nilai
- [ ] Kehadiran header keamanan
- [ ] Konfigurasi SSL/TLS
- [ ] Tinjauan manajemen sesi
- [ ] Penanganan kesalahan (tidak ada kebocoran informasi)
---

## Sumber Daya Keamanan
### OWASP 10 Teratas (2021)
1. Kontrol Akses Rusak
2. Kegagalan Kriptografi
3. Injeksi
4. Desain Tidak Aman
5. Kesalahan Konfigurasi Keamanan
6. Komponen Rentan dan Kedaluwarsa
7. Kegagalan Identifikasi dan Otentikasi
8. Kegagalan Integritas Perangkat Lunak dan Data
9. Kegagalan Pencatatan dan Pemantauan Keamanan
10. Pemalsuan Permintaan Sisi Server
### Alat yang Direkomendasikan
- **Analisis Statis**: SonarQube, Semgrep, CodeQL
- **Pemindaian Ketergantungan**: Dependabot, Renovasi, Snyk
- **Pengujian Dinamis**: OWASP ZAP, Burp Suite
- **Deteksi Rahasia**: GitLeaks, TruffleHog
- **Keamanan Kontainer**: Trivy, Clair, Anchore