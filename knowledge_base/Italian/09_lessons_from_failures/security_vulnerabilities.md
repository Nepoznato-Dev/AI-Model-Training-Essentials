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
# Vulnerabilità della sicurezza
Questo documento consolida le vulnerabilità di sicurezza comuni nello sviluppo del software, inclusi attacchi di tipo injection, pratiche di codice non sicure ed errori di sicurezza.
---

##Iniezione SQL
Gli attacchi SQL injection si verificano quando l'input di un utente non attendibile viene gestito in modo improprio nelle query del database, consentendo agli aggressori di manipolare la logica delle query, accedere a dati non autorizzati o modificare i contenuti del database.
### Iniezione classica basata su UNION
**Esempio errato (codice vulnerabile):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Attacco:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Perché non va bene:**
- Espone i dati da altre tabelle
- Ignora la logica di query prevista
- Può estrarre informazioni sensibili
**Approccio migliore:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Strategie di prevenzione
1. **Utilizza query con parametri**: non concatenare mai l'input dell'utente in SQL
2. **Convalida input**: convalida e disinfetta tutti gli input dell'utente
3. **Privilegio minimo**: gli account database devono avere autorizzazioni minime
4. **Utilizzo ORM**: utilizzare mapping relazionali a oggetti che gestiscono l'escape
5. **Web Application Firewall**: distribuisci WAF per rilevare i tentativi di injection
---

## Scripting tra siti (XSS)
Gli attacchi Cross-Site Scripting (XSS) si verificano quando gli aggressori inseriscono script dannosi nelle pagine Web visualizzate da altri utenti.
### XSS riflesso
**Esempio errato (codice vulnerabile):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Attacco:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Perché non va bene:**
- Input dell'utente reso direttamente senza codifica
- L'aggressore può creare URL dannosi
- Dirottamento della sessione, possibile furto di credenziali
**Approccio migliore:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS memorizzato
**Cattivo esempio:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Strategie di prevenzione
1. **Codifica output**: codifica i dati in base al contesto (HTML, JS, URL, CSS)
2. **Convalida input**: rifiuta o disinfetta input dannosi
3. **Politica di sicurezza dei contenuti**: utilizza le intestazioni CSP per limitare le origini degli script
4. **Cookie solo HTTP**: impedisce l'accesso JavaScript ai cookie di sessione
5. **Framework moderni**: utilizza React, Vue, Angular con escape automatico per impostazione predefinita
---

## Problemi di sicurezza della memoria
### Overflow del buffer
**Cattivo esempio (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problemi:**
- Può sovrascrivere la memoria adiacente
- Può consentire attacchi di esecuzione di codice
- Causa un comportamento indefinito
**Approccio migliore:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Usa-dopo-gratuito
**Esempio errato (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Approccio migliore:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Strategie di prevenzione
1. **Utilizza linguaggi sicuri**: preferisci Rust, Go, Java, Python rispetto a C/C++
2. **Puntatori intelligenti**: utilizza modelli RAII in C++
3. **Controllo dei limiti**: convalida sempre gli indici dell'array
4. **Analisi statica**: utilizza strumenti come Valgrind, AddressSanitizer
5. **API memory-safe**: utilizza funzioni della libreria standard più sicure
---

## Errori di autenticazione
### Politiche relative alle password deboli
**Cattivo esempio:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problemi:**
- Sensibile agli attacchi di forza bruta
- Password comuni facilmente indovinabili
- Viola le migliori pratiche di sicurezza
**Approccio migliore:**```python
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

### Memorizzazione di password in testo normale
**Cattivo esempio:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Approccio migliore:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Strategie di prevenzione
1. **Hashing forte**: utilizza bcrypt, Argon2 o scrypt per le password
2. **Autenticazione a più fattori**: richiede una verifica aggiuntiva
3. **Limitazione della velocità**: previene gli attacchi di forza bruta
4. **Blocco account**: blocco temporaneo dopo tentativi falliti
5. **Gestione sicura delle sessioni**: utilizza cookie sicuri, solo HTTP
---

## Altri errori di sicurezza
### Segreti codificati
**Cattivo esempio:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Approccio migliore:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Riferimenti a oggetti diretti non sicuri
**Cattivo esempio:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Approccio migliore:**```python
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

### Limitazione della velocità mancante
**Cattivo esempio:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Approccio migliore:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Argomenti correlati
- **Errori AI/LLM**: vedere`ai_llm_failures.md`per l'inserimento tempestivo e problemi di sicurezza specifici dell'IA
- **Modelli di codice non sicuri**: vedere esempi di codice per la sicurezza della memoria e il comportamento indefinito
- **Best practice per l'autenticazione**: implementare flussi di autenticazione e gestione delle sessioni adeguati
- **Qualità del codice**: vedere`code_quality_issues.md`per pratiche di codifica sicure
---

## Ulteriori vulnerabilità di sicurezza
### Iniezione di comando
**Che cos'è:** Esecuzione di comandi di sistema arbitrari tramite input dell'utente non disinfettato.
**Esempio errato (codice vulnerabile):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Attacco:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Perché non va bene:**
- L'attaccante può eseguire qualsiasi comando di sistema
- Potenziale di compromissione completa del sistema
- Distruzione dei dati, possibile installazione di malware
**Approccio migliore:**```python
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

### Attraversamento del percorso
**Che cos'è:** Accesso ai file al di fuori delle directory previste utilizzando sequenze ../.
**Cattivo esempio:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Attacco:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Approccio migliore:**```python
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

### Falsificazione delle richieste lato server (SSRF)
**Che cos'è:** Fa sì che il server effettui richieste verso destinazioni non previste.
**Cattivo esempio:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Attacco:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Approccio migliore:**```python
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

## Errori crittografici
### Algoritmi di hashing deboli
**Cattivo esempio:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Perché non va bene:**
- MD5 e SHA1 sono crittograficamente danneggiati
- Veloce da calcolare (abilita la forza bruta)
- Dimostrazione degli attacchi di collisione
**Approccio migliore:**```python
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

### Chiavi di crittografia codificate
**Cattivo esempio:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Approccio migliore:**```python
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

### Utilizzo della modalità BCE
**Cattivo esempio:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Perché non va bene:**
- Blocchi di testo in chiaro identici producono testo cifrato identico
- I modelli nei dati sono visibili
- Il famoso "pinguino della BCE" dimostra il problema
**Approccio migliore:**```python
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

## Problemi di sicurezza dell'API
### Convalida dell'input mancante
**Cattivo esempio:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Approccio migliore:**```python
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

### Autenticazione API non sicura
**Cattivo esempio:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Approccio migliore:**```python
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

### Limitazione della velocità mancante sulle API
**Cattivo esempio:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Approccio migliore:**```python
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

## Intestazioni e configurazione di sicurezza
### Intestazioni di sicurezza mancanti
**Cattivo esempio:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Approccio migliore:**```python
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

### Configurazione CORS non sicura
**Cattivo esempio:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Approccio migliore:**```python
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

## Casi di studio
### Caso di studio 1: violazione dei dati di Equifax (2017)
**Incidente:** gli aggressori hanno sfruttato la vulnerabilità di Apache Struts per accedere ai dati personali di 147 milioni di persone.
**Causa principale:**
- Software senza patch (CVE-2017-5638)
- Nessuna convalida dell'input sull'intestazione del tipo di contenuto
- Segmentazione della rete insufficiente
**Impatto:**
- 1,4 miliardi di dollari di costi
- Dati personali esposti (SSN, date di nascita, indirizzi)
- Enormi danni alla reputazione
**Lezione:** Mantieni aggiornate le dipendenze; implementare la difesa in profondità.
### Caso di studio 2: violazione degli obiettivi (2013)
**Incidente:** gli aggressori hanno rubato 40 milioni di numeri di carte di credito.
**Causa principale:**
- Credenziali del fornitore di terze parti compromesse
- Nessuna segmentazione della rete tra venditore e sistemi di pagamento
- Avvisi di sicurezza ignorati
**Impatto:**
- 202 milioni di dollari di costi
- CEO e CIO licenziati
- Necessaria una revisione del sistema di pagamento
**Lezione:** Reti di segmenti; monitorare l'accesso di terzi; rispondere agli avvisi.
### Caso di studio 3: attacco alla catena di fornitura SolarWinds (2020)
**Incidente:** Il codice dannoso inserito negli aggiornamenti software ha colpito oltre 18.000 organizzazioni.
**Causa principale:**
- Sistema di build compromesso
- Aggiornamenti dannosi firmati con certificati validi
- Movimento laterale una volta all'interno delle reti
**Impatto:**
- Agenzie governative compromesse
- Colpite le aziende Fortune 500
- Indagini e azioni correttive in corso
**Lezione:** Pipeline di build sicure; verificare l'integrità del software; architettura Zero Trust.
---

## Strategie di test di sicurezza
### Test statici di sicurezza delle applicazioni (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Test dinamici di sicurezza delle applicazioni (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Scansione delle dipendenze
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Lista di controllo per i test di penetrazione
- [] Test di iniezione SQL
- [] Test XSS (riflesso, archiviato, basato su DOM)
- [ ] Convalida del token CSRF
- [ ] Tentativi di bypass dell'autenticazione
- [ ] Controlli di autorizzazione (escalation dei privilegi verticale/orizzontale)
- [ ] Verifica della limitazione della velocità
- [ ] Presenza intestazioni di sicurezza
- [ ] Configurazione SSL/TLS
- [ ] Revisione della gestione della sessione
- [ ] Gestione degli errori (nessuna perdita di informazioni)
---

## Risorse per la sicurezza
### OWASP Top 10 (2021)
1. Controllo degli accessi interrotto
2. Errori crittografici
3. Iniezione
4. Design insicuro
5. Errata configurazione della sicurezza
6. Componenti vulnerabili e obsoleti
7. Errori di identificazione e autenticazione
8. Errori di integrità del software e dei dati
9. Errori di registrazione e monitoraggio della sicurezza
10. Falsificazione delle richieste lato server
### Strumenti consigliati
- **Analisi statica**: SonarQube, Semgrep, CodeQL
- **Scansione delle dipendenze**: Dependabot, Renovate, Snyk
- **Test dinamici**: OWASP ZAP, Burp Suite
- **Rilevamento segreti**: GitLeaks, TruffleHog
- **Sicurezza dei container**: Trivy, Clair, Anchore