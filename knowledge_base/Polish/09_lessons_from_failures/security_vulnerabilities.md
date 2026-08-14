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
# Luki w zabezpieczeniach
W tym dokumencie przedstawiono typowe luki w zabezpieczeniach występujące podczas tworzenia oprogramowania, w tym ataki polegające na wstrzykiwaniu oprogramowania, praktyki związane z niebezpiecznym kodem i błędy bezpieczeństwa.
---

## Wstrzyknięcie SQL
Ataki polegające na wstrzykiwaniu kodu SQL mają miejsce, gdy dane wejściowe niezaufanego użytkownika są niewłaściwie obsługiwane w zapytaniach do bazy danych, co umożliwia atakującym manipulowanie logiką zapytań, uzyskiwanie dostępu do nieautoryzowanych danych lub modyfikowanie zawartości bazy danych.
### Klasyczny wtrysk oparty na UNION
**Zły przykład (kod luki):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Atak:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Dlaczego to jest złe:**
- Udostępnia dane z innych tabel
- Pomija zamierzoną logikę zapytań
- Potrafi wyodrębnić poufne informacje
**Lepsze podejście:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Strategie zapobiegawcze
1. **Użyj zapytań sparametryzowanych**: Nigdy nie łącz danych wejściowych użytkownika z SQL
2. **Weryfikacja danych wejściowych**: Sprawdź i oczyść wszystkie dane wejściowe użytkownika
3. **Najmniejsze uprawnienia**: Konta bazy danych powinny mieć minimalne uprawnienia
4. **Użycie ORM**: Użyj maperów obiektowo-relacyjnych, które obsługują ucieczkę
5. **Zapory sieciowe aplikacji internetowych**: wdrażaj zabezpieczenia WAF w celu wykrywania prób wstrzyknięć
---

## Skrypty między witrynami (XSS)
Ataki typu Cross-Site Scripting (XSS) mają miejsce, gdy napastnicy wstrzykiwają złośliwe skrypty na strony internetowe przeglądane przez innych użytkowników.
### Odbicie XSS
**Zły przykład (kod luki):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Atak:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Dlaczego to jest złe:**
- Dane wejściowe użytkownika renderowane bezpośrednio bez kodowania
- Osoba atakująca może stworzyć złośliwe adresy URL
- Możliwość przejęcia sesji i kradzieży danych uwierzytelniających
**Lepsze podejście:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Przechowywane XSS
**Zły przykład:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Strategie zapobiegawcze
1. **Kodowanie wyjściowe**: Koduj dane w oparciu o kontekst (HTML, JS, URL, CSS)
2. **Weryfikacja danych wejściowych**: Odrzuć lub usuń złośliwe dane wejściowe
3. **Polityka bezpieczeństwa treści**: Użyj nagłówków CSP, aby ograniczyć źródła skryptów
4. **HTTPOnly Cookies**: Zapobiegaj dostępowi JavaScript do plików cookie sesji
5. **Nowoczesne frameworki**: Używaj React, Vue, Angular, które domyślnie automatycznie uciekają
---

## Problemy z bezpieczeństwem pamięci
### Przepełnienia bufora
**Zły przykład (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problemy:**
- Może zastąpić sąsiednią pamięć
- Może umożliwiać ataki polegające na wykonaniu kodu
- Powoduje niezdefiniowane zachowanie
**Lepsze podejście:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Do wykorzystania po bezpłatnym
**Zły przykład (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Lepsze podejście:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Strategie zapobiegawcze
1. **Używaj bezpiecznych języków**: Preferuj Rust, Go, Java i Python zamiast C/C++
2. **Inteligentne wskaźniki**: Używaj wzorców RAII w C++
3. **Sprawdzanie granic**: Zawsze sprawdzaj indeksy tablicy
4. **Analiza statyczna**: Użyj narzędzi takich jak Valgrind, AddressSanitizer
5. **Bezpieczne dla pamięci interfejsy API**: Używaj bezpieczniejszych standardowych funkcji bibliotecznych
---

## Błędy uwierzytelniania
### Słabe zasady dotyczące haseł
**Zły przykład:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problemy:**
- Podatny na ataki siłowe
- Wspólne hasła łatwe do odgadnięcia
- Narusza najlepsze praktyki bezpieczeństwa
**Lepsze podejście:**```python
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

### Przechowywanie haseł w postaci zwykłego tekstu
**Zły przykład:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Lepsze podejście:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Strategie zapobiegawcze
1. **Silne haszowanie**: Użyj bcrypt, Argon2 lub scrypt do haseł
2. **Uwierzytelnianie wieloskładnikowe**: Wymagaj dodatkowej weryfikacji
3. **Ograniczenie szybkości**: Zapobiegaj atakom brutalnej siły
4. **Blokada konta**: Tymczasowa blokada po nieudanych próbach
5. **Bezpieczne zarządzanie sesją**: Używaj bezpiecznych plików cookie obsługujących wyłącznie protokół HTTP
---

## Inne błędy bezpieczeństwa
### Zakodowane na stałe sekrety
**Zły przykład:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Lepsze podejście:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Niebezpieczne bezpośrednie odniesienia do obiektów
**Zły przykład:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Lepsze podejście:**```python
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

### Brakujące ograniczenie szybkości
**Zły przykład:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Lepsze podejście:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Powiązane tematy
- **Awarie AI/LLM**: Zobacz `ai_llm_failures.md`, aby uzyskać informacje na temat szybkiego wstrzykiwania i problemów związanych z bezpieczeństwem specyficznych dla sztucznej inteligencji
- **Niebezpieczne wzorce kodu**: Zobacz przykłady kodu dotyczące bezpieczeństwa pamięci i niezdefiniowanego zachowania
- **Najlepsze praktyki dotyczące uwierzytelniania**: Wprowadź odpowiednie przepływy uwierzytelniania i zarządzanie sesjami
- **Jakość kodu**: Zobacz `code_quality_issues.md`, aby zapoznać się z praktykami bezpiecznego kodowania
---

## Dodatkowe luki w zabezpieczeniach
### Wstrzykiwanie poleceń
**Co to jest:** Wykonywanie dowolnych poleceń systemowych na podstawie nieoczyszczonych danych wejściowych użytkownika.
**Zły przykład (kod luki):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Atak:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Dlaczego to jest złe:**
- Atakujący może wykonać dowolne polecenie systemowe
— Możliwość całkowitego naruszenia bezpieczeństwa systemu
- Zniszczenie danych, możliwa instalacja złośliwego oprogramowania
**Lepsze podejście:**```python
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

### Przechodzenie ścieżki
**Co to jest:** Dostęp do plików poza zamierzonymi katalogami przy użyciu sekwencji ../.
**Zły przykład:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Atak:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Lepsze podejście:**```python
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

### Fałszowanie żądań po stronie serwera (SSRF)
**Co to jest:** Wysyłanie przez serwer żądań do niezamierzonych miejsc docelowych.
**Zły przykład:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Atak:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Lepsze podejście:**```python
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

## Błędy kryptograficzne
### Słabe algorytmy mieszające
**Zły przykład:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Dlaczego to jest złe:**
- MD5 i SHA1 są łamane kryptograficznie
- Szybkie obliczenia (umożliwia brutalną siłę)
- Pokazano ataki kolizyjne
**Lepsze podejście:**```python
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

### Zakodowane na stałe klucze szyfrujące
**Zły przykład:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Lepsze podejście:**```python
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

### Korzystanie z trybu EBC
**Zły przykład:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Dlaczego to jest złe:**
- Identyczne bloki tekstu jawnego dają identyczny tekst zaszyfrowany
- Widoczne są wzorce w danych
- Słynny „pingwin EBC” demonstruje problem
**Lepsze podejście:**```python
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

## Problemy z bezpieczeństwem API
### Brak weryfikacji danych wejściowych
**Zły przykład:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Lepsze podejście:**```python
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

### Niebezpieczne uwierzytelnianie API
**Zły przykład:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Lepsze podejście:**```python
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

### Brakujące ograniczenie szybkości w interfejsach API
**Zły przykład:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Lepsze podejście:**```python
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

## Nagłówki zabezpieczeń i konfiguracja
### Brakujące nagłówki zabezpieczeń
**Zły przykład:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Lepsze podejście:**```python
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

### Niebezpieczna konfiguracja CORS
**Zły przykład:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Lepsze podejście:**```python
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

## Studia przypadków
### Studium przypadku 1: Naruszenie danych Equifax (2017)
**Incydent:** osoby atakujące wykorzystały lukę w zabezpieczeniach Apache Struts, aby uzyskać dostęp do danych osobowych 147 milionów osób.
**Główna przyczyna:**
- Niezałatane oprogramowanie (CVE-2017-5638)
- Brak sprawdzania poprawności danych wejściowych w nagłówku typu zawartości
- Niewystarczająca segmentacja sieci
**Wpływ:**
- 1,4 miliarda dolarów kosztów
- Dane osobowe ujawnione (SSN, daty urodzenia, adresy)
- Ogromne szkody dla reputacji
**Lekcja:** Aktualizuj zależności; wdrożyć głęboką obronę.
### Studium przypadku 2: Naruszenie celu (2013)
**Incydent:** atakujący ukradli 40 milionów numerów kart kredytowych.
**Główna przyczyna:**
— Naruszono dane uwierzytelniające dostawców zewnętrznych
- Brak segmentacji sieci pomiędzy dostawcami i systemami płatności
- Ignorowano alerty bezpieczeństwa
**Wpływ:**
- Koszty wynoszące 202 miliony dolarów
- Zwolniono dyrektora generalnego i CIO
- Wymagana zmiana systemu płatności
**Lekcja:** Sieci segmentowe; monitorować dostęp osób trzecich; reagować na alerty.
### Studium przypadku 3: Atak na łańcuch dostaw SolarWinds (2020)
**Incydent:** złośliwy kod wprowadzony do aktualizacji oprogramowania dotknął ponad 18 000 organizacji.
**Główna przyczyna:**
- Naruszony system kompilacji
- Podpisane złośliwe aktualizacje z ważnymi certyfikatami
- Ruch boczny wewnątrz sieci
**Wpływ:**
- Agencje rządowe zagrożone
- Dotknięte firmy z listy Fortune 500
- Trwające dochodzenie i środki zaradcze
**Lekcja:** Bezpieczne budowanie potoków; zweryfikować integralność oprogramowania; architekturę zerowego zaufania.
---

## Strategie testowania bezpieczeństwa
### Statyczne testowanie bezpieczeństwa aplikacji (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Dynamiczne testowanie bezpieczeństwa aplikacji (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Skanowanie zależności
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Lista kontrolna testów penetracyjnych
- [ ] Testowanie wtrysku SQL
- [ ] Testowanie XSS (odzwierciedlone, zapisane, oparte na DOM)
- [ ] Walidacja tokena CSRF
- [ ] Próby obejścia uwierzytelnienia
- [ ] Kontrole autoryzacji (eskalacja uprawnień w pionie/poziomie)
- [ ] Weryfikacja ograniczenia szybkości
- [ ] Obecność nagłówków zabezpieczeń
- [ ] Konfiguracja SSL/TLS
- [ ] Przegląd zarządzania sesją
- [ ] Obsługa błędów (brak wycieku informacji)
---

## Zasoby dotyczące bezpieczeństwa
### OWASP Top 10 (2021)
1. Zepsuta kontrola dostępu
2. Awarie kryptograficzne
3. Wstrzyknięcie
4. Niebezpieczny projekt
5. Błędna konfiguracja zabezpieczeń
6. Wrażliwe i nieaktualne komponenty
7. Błędy identyfikacji i uwierzytelnienia
8. Awarie oprogramowania i integralności danych
9. Błędy w logowaniu i monitorowaniu zabezpieczeń
10. Fałszowanie żądań po stronie serwera
### Polecane narzędzia
- **Analiza statyczna**: SonarQube, Semgrep, CodeQL
- **Skanowanie zależności**: Depabot, Renovate, Snyk
- **Testowanie dynamiczne**: OWASP ZAP, Burp Suite
- **Wykrywanie sekretów**: GitLeaks, TruffleHog
- **Bezpieczeństwo kontenera**: Trivy, Clair, Anchore