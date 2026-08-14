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
# Failles de sécurité
Ce document consolide les vulnérabilités de sécurité courantes dans le développement de logiciels, notamment les attaques par injection, les pratiques de code non sécurisées et les erreurs de sécurité.
---

##Injection SQL
Les attaques par injection SQL se produisent lorsque des entrées utilisateur non fiables sont traitées de manière incorrecte dans les requêtes de base de données, permettant aux attaquants de manipuler la logique des requêtes, d'accéder à des données non autorisées ou de modifier le contenu de la base de données.
### Injection classique basée sur UNION
**Mauvais exemple (code vulnérable) :**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Attaque:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Pourquoi c'est mauvais :**
- Expose les données d'autres tables
- Contourne la logique de requête prévue
- Peut extraire des informations sensibles
**Meilleure approche :**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Stratégies de prévention
1. **Utilisez des requêtes paramétrées** : ne concaténez jamais les entrées utilisateur dans SQL
2. **Validation des entrées** : validez et désinfectez toutes les entrées utilisateur
3. **Moyen privilège** : les comptes de base de données doivent avoir des autorisations minimales
4. **Utilisation ORM** : utilisez des mappeurs objet-relationnels qui gèrent l'échappement
5. **Pare-feu d'application Web** : déployez des WAF pour détecter les tentatives d'injection
---

## Scripts intersites (XSS)
Les attaques XSS (Cross-Site Scripting) se produisent lorsque des attaquants injectent des scripts malveillants dans des pages Web consultées par d'autres utilisateurs.
### XSS réfléchi
**Mauvais exemple (code vulnérable) :**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Attaque:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Pourquoi c'est mauvais :**
- Entrée utilisateur directement rendue sans encodage
- L'attaquant peut créer des URL malveillantes
- Détournement de session, vol d'identifiants possible
**Meilleure approche :**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS stocké
**Mauvais exemple :**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Stratégies de prévention
1. **Output Encoding** : encodez les données en fonction du contexte (HTML, JS, URL, CSS)
2. **Validation des entrées** : rejeter ou nettoyer les entrées malveillantes
3. **Politique de sécurité du contenu** : utilisez les en-têtes CSP pour restreindre les sources de script
4. **Cookies HTTPOnly** : Empêcher l'accès JavaScript aux cookies de session
5. **Frameworks modernes** : utilisez React, Vue, Angular qui s'échappent automatiquement par défaut
---

## Problèmes de sécurité de la mémoire
### Débordements de tampon
**Mauvais exemple (C) :**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problèmes :**
- Peut écraser la mémoire adjacente
- Peut permettre des attaques par exécution de code
- Provoque un comportement indéfini
**Meilleure approche :**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Utilisation après libération
**Mauvais exemple (C++) :**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Meilleure approche :**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Stratégies de prévention
1. **Utilisez des langages sécurisés** : préférez Rust, Go, Java, Python à C/C++
2. **Pointeurs intelligents** : utilisez les modèles RAII en C++
3. **Vérification des limites** : validez toujours les indices de tableau
4. **Analyse statique** : utilisez des outils comme Valgrind, AddressSanitizer
5. **API Memory-Safe** : utilisez des fonctions de bibliothèque standard plus sûres
---

## Erreurs d'authentification
### Politiques de mot de passe faibles
**Mauvais exemple :**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problèmes :**
- Sensible aux attaques par force brute
- Mots de passe courants faciles à deviner
- Viole les meilleures pratiques de sécurité
**Meilleure approche :**```python
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

### Stockage des mots de passe en texte brut
**Mauvais exemple :**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Meilleure approche :**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Stratégies de prévention
1. **Strong Hashing** : utilisez bcrypt, Argon2 ou scrypt pour les mots de passe
2. **Authentification multifacteur** : nécessite une vérification supplémentaire
3. **Limitation de débit** : évitez les attaques par force brute
4. **Verrouillage du compte** : verrouillage temporaire après des tentatives infructueuses
5. **Gestion sécurisée des sessions** : utilisez des cookies sécurisés HTTP uniquement
---

## Autres erreurs de sécurité
### Secrets codés en dur
**Mauvais exemple :**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Meilleure approche :**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Références d'objets directs non sécurisés
**Mauvais exemple :**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Meilleure approche :**```python
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

### Limitation du débit manquant
**Mauvais exemple :**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Meilleure approche :**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Sujets connexes
- **Échecs AI/LLM** : voir`ai_llm_failures.md`pour une injection rapide et des problèmes de sécurité spécifiques à l'IA.
- **Modèles de code non sécurisés** : consultez des exemples de code pour la sécurité de la mémoire et les comportements non définis.
- **Meilleures pratiques d'authentification** : mettre en œuvre des flux d'authentification et une gestion de session appropriés
- **Qualité du code** : voir`code_quality_issues.md`pour les pratiques de codage sécurisées
---

## Failles de sécurité supplémentaires
### Injection de commandes
**Qu'est-ce que c'est :** Exécution de commandes système arbitraires via une entrée utilisateur non vérifiée.
**Mauvais exemple (code vulnérable) :**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Attaque:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Pourquoi c'est mauvais :**
- L'attaquant peut exécuter n'importe quelle commande système
- Potentiel de compromission complète du système
- Destruction des données, installation de logiciels malveillants possible
**Meilleure approche :**```python
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

### Traversée du chemin
**Qu'est-ce que c'est :** Accès aux fichiers en dehors des répertoires prévus à l'aide des séquences ../.
**Mauvais exemple :**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Attaque:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Meilleure approche :**```python
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

### Contrefaçon de requête côté serveur (SSRF)
**Qu'est-ce que c'est :** Faire en sorte que le serveur envoie des requêtes vers des destinations inattendues.
**Mauvais exemple :**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Attaque:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Meilleure approche :**```python
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

## Erreurs cryptographiques
### Algorithmes de hachage faibles
**Mauvais exemple :**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Pourquoi c'est mauvais :**
- MD5 et SHA1 sont cryptographiquement cassés
- Rapide à calculer (permet la force brute)
- Attaques de collision démontrées
**Meilleure approche :**```python
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

### Clés de chiffrement codées en dur
**Mauvais exemple :**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Meilleure approche :**```python
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

### Utilisation du mode BCE
**Mauvais exemple :**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Pourquoi c'est mauvais :**
- Des blocs de texte en clair identiques produisent un texte chiffré identique
- Les modèles dans les données sont visibles
- Le célèbre "pingouin de la BCE" démontre le problème
**Meilleure approche :**```python
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

## Problèmes de sécurité des API
### Validation d'entrée manquante
**Mauvais exemple :**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Meilleure approche :**```python
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

### Authentification API non sécurisée
**Mauvais exemple :**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Meilleure approche :**```python
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

### Limitation de débit manquante sur les API
**Mauvais exemple :**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Meilleure approche :**```python
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

## En-têtes et configuration de sécurité
### En-têtes de sécurité manquants
**Mauvais exemple :**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Meilleure approche :**```python
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

### Configuration CORS non sécurisée
**Mauvais exemple :**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Meilleure approche :**```python
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

## Études de cas
### Étude de cas 1 : Violation de données d'Equifax (2017)
**Incident :** Les attaquants ont exploité la vulnérabilité d'Apache Struts pour accéder aux données personnelles de 147 millions de personnes.
**Cause fondamentale :**
- Logiciel non corrigé (CVE-2017-5638)
- Aucune validation d'entrée sur l'en-tête de type de contenu
- Segmentation insuffisante du réseau
**Impact :**
- 1,4 milliard de dollars de coûts
- Données personnelles exposées (SSN, dates de naissance, adresses)
- Dommages massifs à la réputation
**Leçon :** Gardez les dépendances à jour ; mettre en œuvre une défense en profondeur.
### Étude de cas 2 : Violation de l'objectif (2013)
**Incident :** Les attaquants ont volé 40 millions de numéros de cartes de crédit.
**Cause fondamentale :**
- Les informations d'identification d'un fournisseur tiers ont été compromises
- Aucune segmentation du réseau entre les fournisseurs et les systèmes de paiement
- Alertes de sécurité ignorées
**Impact :**
- 202 millions de dollars de coûts
- Le PDG et le CIO licenciés
- Refonte du système de paiement requise
**Leçon :** Réseaux de segments ; surveiller l'accès des tiers ; répondre aux alertes.
### Étude de cas 3 : Attaque de la chaîne d'approvisionnement de SolarWinds (2020)
**Incident :** Un code malveillant inséré dans des mises à jour logicielles a affecté plus de 18 000 organisations.
**Cause fondamentale :**
- Système de construction compromis
- Mises à jour malveillantes signées avec des certificats valides
- Mouvement latéral une fois à l'intérieur des réseaux
**Impact :**
- Les agences gouvernementales compromises
- Entreprises Fortune 500 touchées
- Enquête et remédiation en cours
**Leçon :** Pipelines de build sécurisés ; vérifier l'intégrité du logiciel ; architecture zéro confiance.
---

## Stratégies de tests de sécurité
### Tests de sécurité des applications statiques (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Tests dynamiques de sécurité des applications (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Analyse des dépendances
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Liste de contrôle des tests d'intrusion
- [ ] Tests d'injection SQL
- [ ] Tests XSS (réfléchis, stockés, basés sur DOM)
- [ ] Validation du jeton CSRF
- [ ] Tentatives de contournement d'authentification
- [ ] Vérifications d'autorisation (élévation de privilèges verticale/horizontale)
- [ ] Vérification de la limitation du débit
- [ ] Présence des en-têtes de sécurité
- [ ] Configuration SSL/TLS
- [ ] Revue de la gestion des sessions
- [ ] Gestion des erreurs (pas de fuite d'informations)
---

## Ressources de sécurité
### OWASP Top 10 (2021)
1. Contrôle d'accès brisé
2. Échecs cryptographiques
3. Injection
4. Conception non sécurisée
5. Mauvaise configuration de la sécurité
6. Composants vulnérables et obsolètes
7. Échecs d’identification et d’authentification
8. Défaillances des logiciels et de l'intégrité des données
9. Échecs de journalisation et de surveillance de sécurité
10. Contrefaçon de requête côté serveur
### Outils recommandés
- **Analyse statique** : SonarQube, Semgrep, CodeQL
- **Analyse des dépendances** : Dependabot, Renovate, Snyk
- **Tests dynamiques** : OWASP ZAP, Burp Suite
- **Détection secrète** : GitLeaks, TruffleHog
- **Sécurité des conteneurs** : Trivy, Clair, Anchore