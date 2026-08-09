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

# Sicherheitslücken
Dieses Dokument konsolidiert häufige Sicherheitslücken in der Softwareentwicklung, darunter Injektionsangriffe, unsichere Codepraktiken und Sicherheitsfehler.
---

## SQL-Injection
SQL-Injection-Angriffe treten auf, wenn nicht vertrauenswürdige Benutzereingaben in Datenbankabfragen nicht ordnungsgemäß verarbeitet werden, wodurch Angreifer die Abfragelogik manipulieren, auf nicht autorisierte Daten zugreifen oder Datenbankinhalte ändern können.
### Klassische UNION-basierte Injektion
**Schlechtes Beispiel (anfälliger Code):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Angriff:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Warum es schlecht ist:**
– Macht Daten aus anderen Tabellen verfügbar
– Umgeht die beabsichtigte Abfragelogik
- Kann vertrauliche Informationen extrahieren
**Besserer Ansatz:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Präventionsstrategien
1. **Verwenden Sie parametrisierte Abfragen**: Verketten Sie niemals Benutzereingaben in SQL
2. **Eingabevalidierung**: Validieren und bereinigen Sie alle Benutzereingaben
3. **Geringste Rechte**: Datenbankkonten sollten über minimale Berechtigungen verfügen
4. **ORM-Nutzung**: Verwenden Sie objektrelationale Mapper, die das Escapen handhaben
5. **Webanwendungs-Firewalls**: Stellen Sie WAFs bereit, um Einschleusungsversuche zu erkennen
---

## Cross-Site-Scripting (XSS)
Cross-Site-Scripting-Angriffe (XSS) treten auf, wenn Angreifer schädliche Skripts in Webseiten einschleusen, die von anderen Benutzern angezeigt werden.
### Reflektiertes XSS
**Schlechtes Beispiel (anfälliger Code):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Angriff:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Warum es schlecht ist:**
- Benutzereingaben werden direkt ohne Codierung gerendert
– Angreifer können bösartige URLs erstellen
- Session-Hijacking, Zugangsdatendiebstahl möglich
**Besserer Ansatz:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Gespeichertes XSS
**Schlechtes Beispiel:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Präventionsstrategien
1. **Ausgabekodierung**: Daten basierend auf dem Kontext kodieren (HTML, JS, URL, CSS)
2. **Eingabevalidierung**: Schädliche Eingaben ablehnen oder bereinigen
3. **Inhaltssicherheitsrichtlinie**: Verwenden Sie CSP-Header, um Skriptquellen einzuschränken
4. **Nur HTTP-Cookies**: Verhindern Sie den JavaScript-Zugriff auf Sitzungscookies
5. **Moderne Frameworks**: Verwenden Sie React, Vue, Angular, die standardmäßig automatisch maskiert werden
---

## Probleme mit der Speichersicherheit
### Pufferüberläufe
**Schlechtes Beispiel (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Probleme:**
- Kann angrenzenden Speicher überschreiben
– Kann Codeausführungsangriffe ermöglichen
- Verursacht undefiniertes Verhalten
**Besserer Ansatz:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Kostenlose Nutzung nach dem Gebrauch
**Schlechtes Beispiel (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Besserer Ansatz:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Präventionsstrategien
1. **Sichere Sprachen verwenden**: Bevorzugen Sie Rust, Go, Java, Python gegenüber C/C++
2. **Intelligente Zeiger**: Verwenden Sie RAII-Muster in C++
3. **Grenzprüfung**: Array-Indizes immer validieren
4. **Statische Analyse**: Verwenden Sie Tools wie Valgrind, AddressSanitizer
5. **Speichersichere APIs**: Verwenden Sie sicherere Standardbibliotheksfunktionen
---

## Authentifizierungsfehler
### Richtlinien für schwache Passwörter
**Schlechtes Beispiel:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Probleme:**
- Anfällig für Brute-Force-Angriffe
- Gängige Passwörter sind leicht zu erraten
– Verstößt gegen bewährte Sicherheitspraktiken
**Besserer Ansatz:**```python
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

### Speichern von Klartext-Passwörtern
**Schlechtes Beispiel:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Besserer Ansatz:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Präventionsstrategien
1. **Starkes Hashing**: Verwenden Sie bcrypt, Argon2 oder scrypt für Passwörter
2. **Multi-Faktor-Authentifizierung**: Erfordert eine zusätzliche Überprüfung
3. **Ratenbegrenzung**: Verhindern Sie Brute-Force-Angriffe
4. **Kontosperrung**: Vorübergehende Sperrung nach fehlgeschlagenen Versuchen
5. **Sichere Sitzungsverwaltung**: Verwenden Sie sichere, reine HTTP-Cookies
---

## Andere Sicherheitsfehler
### Hartcodierte Geheimnisse
**Schlechtes Beispiel:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Besserer Ansatz:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Unsichere direkte Objektreferenzen
**Schlechtes Beispiel:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Besserer Ansatz:**```python
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

### Fehlende Ratenbegrenzung
**Schlechtes Beispiel:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Besserer Ansatz:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Verwandte Themen
- **KI/LLM-Fehler**: Informationen zu sofortiger Injektion und KI-spezifischen Sicherheitsproblemen finden Sie unter `ai_llm_failures.md`
- **Unsichere Codemuster**: Siehe Codebeispiele für Speichersicherheit und undefiniertes Verhalten
- **Best Practices für die Authentifizierung**: Implementieren Sie ordnungsgemäße Authentifizierungsabläufe und Sitzungsverwaltung
- **Codequalität**: Informationen zu sicheren Codierungspraktiken finden Sie unter `code_quality_issues.md`
---

## Zusätzliche Sicherheitslücken
### Befehlsinjektion
**Was es ist:** Ausführen beliebiger Systembefehle durch unbereinigte Benutzereingaben.
**Schlechtes Beispiel (anfälliger Code):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Angriff:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Warum es schlecht ist:**
- Angreifer kann jeden Systembefehl ausführen
- Möglichkeit einer vollständigen Systemkompromittierung
- Datenvernichtung, Malware-Installation möglich
**Besserer Ansatz:**```python
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

### Pfaddurchquerung
**Was es ist:** Zugriff auf Dateien außerhalb vorgesehener Verzeichnisse mithilfe von ../-Sequenzen.
**Schlechtes Beispiel:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Angriff:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Besserer Ansatz:**```python
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

### Serverseitige Anforderungsfälschung (SSRF)
**Was es ist:** Den Server dazu veranlassen, Anfragen an unbeabsichtigte Ziele zu stellen.
**Schlechtes Beispiel:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Angriff:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Besserer Ansatz:**```python
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

## Kryptografische Fehler
### Schwache Hashing-Algorithmen
**Schlechtes Beispiel:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Warum es schlecht ist:**
- MD5 und SHA1 sind kryptografisch fehlerhaft
- Schnelle Berechnung (ermöglicht Brute Force)
- Kollisionsangriffe nachgewiesen
**Besserer Ansatz:**```python
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

### Hartcodierte Verschlüsselungsschlüssel
**Schlechtes Beispiel:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Besserer Ansatz:**```python
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

### Verwenden des ECB-Modus
**Schlechtes Beispiel:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Warum es schlecht ist:**
- Identische Klartextblöcke erzeugen identischen Chiffretext
- Muster in den Daten sind sichtbar
– Der berühmte „EZB-Pinguin“ veranschaulicht das Problem
**Besserer Ansatz:**```python
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

## API-Sicherheitsprobleme
### Fehlende Eingabevalidierung
**Schlechtes Beispiel:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Besserer Ansatz:**```python
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

### Unsichere API-Authentifizierung
**Schlechtes Beispiel:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Besserer Ansatz:**```python
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

### Fehlende Ratenbegrenzung für APIs
**Schlechtes Beispiel:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Besserer Ansatz:**```python
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

## Sicherheitsheader und Konfiguration
### Fehlende Sicherheitsheader
**Schlechtes Beispiel:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Besserer Ansatz:**```python
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

### Unsichere CORS-Konfiguration
**Schlechtes Beispiel:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Besserer Ansatz:**```python
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

## Fallstudien
### Fallstudie 1: Datenschutzverletzung bei Equifax (2017)
**Vorfall:** Angreifer nutzten die Schwachstelle von Apache Struts aus, um auf persönliche Daten von 147 Millionen Menschen zuzugreifen.
**Grundursache:**
– Ungepatchte Software (CVE-2017-5638)
– Keine Eingabevalidierung für den Inhaltstyp-Header
- Unzureichende Netzwerksegmentierung
**Auswirkung:**
- Kosten in Höhe von 1,4 Milliarden US-Dollar
- Persönliche Daten offengelegt (SSN, Geburtsdaten, Adressen)
- Massiver Reputationsschaden
**Lektion:** Abhängigkeiten auf dem neuesten Stand halten; Verteidigung in die Tiefe implementieren.
### Fallstudie 2: Zielverletzung (2013)
**Vorfall:** Angreifer haben 40 Millionen Kreditkartennummern gestohlen.
**Grundursache:**
– Anmeldeinformationen von Drittanbietern wurden kompromittiert
- Keine Netzwerksegmentierung zwischen Anbieter und Zahlungssystemen
- Sicherheitswarnungen ignoriert
**Auswirkung:**
- Kosten in Höhe von 202 Millionen US-Dollar
- CEO und CIO entlassen
- Überarbeitung des Zahlungssystems erforderlich
**Lektion:** Netzwerke segmentieren; den Zugriff Dritter überwachen; auf Warnungen reagieren.
### Fallstudie 3: Angriff auf die Lieferkette von SolarWinds (2020)
**Vorfall:** Schadcode, der in Software-Updates eingefügt wurde, betraf über 18.000 Organisationen.
**Grundursache:**
- Kompromittiertes Build-System
– Signierte bösartige Updates mit gültigen Zertifikaten
- Seitliche Bewegung innerhalb von Netzwerken
**Auswirkung:**
- Regierungsbehörden kompromittiert
– Fortune-500-Unternehmen betroffen
- Laufende Untersuchung und Abhilfe
**Lektion:** Sichere Build-Pipelines; Überprüfung der Softwareintegrität; Zero-Trust-Architektur.
---

## Strategien für Sicherheitstests
### Statische Anwendungssicherheitstests (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Dynamische Anwendungssicherheitstests (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Abhängigkeitsscan
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Checkliste für Penetrationstests
- [ ] SQL-Injection-Tests
- [ ] XSS-Tests (reflektiert, gespeichert, DOM-basiert)
- [ ] CSRF-Token-Validierung
- [ ] Authentifizierungsumgehungsversuche
- [ ] Berechtigungsprüfungen (vertikale/horizontale Rechteausweitung)
- [ ] Überprüfung der Ratenbegrenzung
- [ ] Vorhandensein von Sicherheitsheadern
- [ ] SSL/TLS-Konfiguration
- [ ] Überprüfung der Sitzungsverwaltung
- [ ] Fehlerbehandlung (kein Informationsverlust)
---

## Sicherheitsressourcen
### OWASP Top 10 (2021)
1. Defekte Zugangskontrolle
2. Kryptografische Fehler
3. Injektion
4. Unsicheres Design
5. Fehlkonfiguration der Sicherheit
6. Anfällige und veraltete Komponenten
7. Identifikations- und Authentifizierungsfehler
8. Software- und Datenintegritätsfehler
9. Fehler bei der Sicherheitsprotokollierung und -überwachung
10. Serverseitige Anforderungsfälschung
### Empfohlene Werkzeuge
- **Statische Analyse**: SonarQube, Semgrep, CodeQL
- **Abhängigkeitsscan**: Dependabot, Renovate, Snyk
- **Dynamische Tests**: OWASP ZAP, Burp Suite
- **Geheime Entdeckung**: GitLeaks, TruffleHog
- **Containersicherheit**: Trivy, Clair, Anchore