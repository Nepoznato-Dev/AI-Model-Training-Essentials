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
# Vulnerabilidades de seguridad
Este documento consolida las vulnerabilidades de seguridad comunes en el desarrollo de software, incluidos ataques de inyección, prácticas de código inseguro y errores de seguridad.
---

## Inyección SQL
Los ataques de inyección SQL ocurren cuando la entrada de un usuario que no es de confianza se maneja incorrectamente en las consultas de la base de datos, lo que permite a los atacantes manipular la lógica de la consulta, acceder a datos no autorizados o modificar el contenido de la base de datos.
### Inyección clásica basada en UNION
**Mal ejemplo (código vulnerable):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Ataque:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Por qué es malo:**
- Expone datos de otras tablas.
- Omite la lógica de consulta prevista
- Puede extraer información confidencial
**Mejor enfoque:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Estrategias de prevención
1. **Utilice consultas parametrizadas**: nunca concatene la entrada del usuario en SQL
2. **Validación de entradas**: valida y desinfecta todas las entradas del usuario
3. **Mínimo privilegio**: las cuentas de bases de datos deben tener permisos mínimos
4. **Uso de ORM**: use asignadores relacionales de objetos que manejen el escape
5. **Firewalls de aplicaciones web**: implemente WAF para detectar intentos de inyección
---

## Secuencias de comandos entre sitios (XSS)
Los ataques de secuencias de comandos entre sitios (XSS) ocurren cuando los atacantes inyectan secuencias de comandos maliciosas en páginas web vistas por otros usuarios.
### XSS reflejado
**Mal ejemplo (código vulnerable):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Ataque:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Por qué es malo:**
- Entrada del usuario renderizada directamente sin codificación
- El atacante puede crear URL maliciosas
- Secuestro de sesión, posible robo de credenciales
**Mejor enfoque:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS almacenado
**Mal ejemplo:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Estrategias de prevención
1. **Codificación de salida**: codifica datos según el contexto (HTML, JS, URL, CSS)
2. **Validación de entrada**: Rechazar o desinfectar entradas maliciosas
3. **Política de seguridad de contenido**: use encabezados CSP para restringir las fuentes de secuencias de comandos
4. **Cookies HTTPOnly**: impiden el acceso de JavaScript a las cookies de sesión
5. **Marcos modernos**: use React, Vue, Angular, que escapan automáticamente de forma predeterminada
---

## Problemas de seguridad de la memoria
### Desbordamientos del búfer
**Mal ejemplo (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problemas:**
- Puede sobrescribir la memoria adyacente
- Puede permitir ataques de ejecución de código.
- Provoca un comportamiento indefinido.
**Mejor enfoque:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Uso después de la liberación
**Mal ejemplo (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Mejor enfoque:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Estrategias de prevención
1. **Utilice lenguajes seguros**: prefiera Rust, Go, Java, Python a C/C++
2. **Punteros inteligentes**: utilice patrones RAII en C++
3. **Comprobación de límites**: valide siempre los índices de la matriz
4. **Análisis estático**: utilice herramientas como Valgrind, AddressSanitizer
5. **API seguras para la memoria**: utilice funciones de biblioteca estándar más seguras
---

## Errores de autenticación
### Políticas de contraseñas débiles
**Mal ejemplo:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problemas:**
- Susceptible a ataques de fuerza bruta
- Contraseñas comunes que se adivinan fácilmente
- Viola las mejores prácticas de seguridad.
**Mejor enfoque:**```python
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

### Almacenamiento de contraseñas en texto plano
**Mal ejemplo:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Mejor enfoque:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Estrategias de prevención
1. **Hashing fuerte**: utilice bcrypt, Argon2 o scrypt para las contraseñas
2. **Autenticación multifactor**: requiere verificación adicional
3. **Limitación de velocidad**: evita ataques de fuerza bruta
4. **Bloqueo de cuenta**: bloqueo temporal después de intentos fallidos
5. **Administración segura de sesiones**: utilice cookies seguras solo HTTP
---

## Otros errores de seguridad
### Secretos codificados
**Mal ejemplo:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Mejor enfoque:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Referencias directas a objetos inseguros
**Mal ejemplo:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Mejor enfoque:**```python
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

### Falta límite de tasa
**Mal ejemplo:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Mejor enfoque:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Temas relacionados
- **Errores de AI/LLM**: Consulte`ai_llm_failures.md`para conocer la inyección rápida y problemas de seguridad específicos de AI
- **Patrones de código inseguro**: vea ejemplos de código para seguridad de la memoria y comportamiento indefinido
- **Mejores prácticas de autenticación**: implementar flujos de autenticación y gestión de sesiones adecuados
- **Calidad del código**: consulte`code_quality_issues.md`para conocer prácticas de codificación segura
---

## Vulnerabilidades de seguridad adicionales
### Inyección de comandos
**Qué es:** Ejecutar comandos arbitrarios del sistema a través de entradas no saneadas del usuario.
**Mal ejemplo (código vulnerable):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Ataque:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Por qué es malo:**
- El atacante puede ejecutar cualquier comando del sistema.
- Potencial de compromiso completo del sistema
- Destrucción de datos, posible instalación de malware.
**Mejor enfoque:**```python
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

### Recorrido de ruta
**Qué es:** Acceder a archivos fuera de los directorios previstos mediante secuencias ../.
**Mal ejemplo:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Ataque:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Mejor enfoque:**```python
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

### Falsificación de solicitudes del lado del servidor (SSRF)
**Qué es:** Hacer que el servidor realice solicitudes a destinos no deseados.
**Mal ejemplo:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Ataque:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Mejor enfoque:**```python
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

## Errores criptográficos
### Algoritmos de hash débiles
**Mal ejemplo:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Por qué es malo:**
- MD5 y SHA1 están criptográficamente rotos
- Rápido de calcular (permite la fuerza bruta)
- Ataques de colisión demostrados.
**Mejor enfoque:**```python
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

### Claves de cifrado codificadas
**Mal ejemplo:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Mejor enfoque:**```python
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

### Usando el modo BCE
**Mal ejemplo:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Por qué es malo:**
- Los bloques de texto plano idénticos producen texto cifrado idéntico
- Los patrones en los datos son visibles.
- El famoso "pingüino del BCE" demuestra el problema
**Mejor enfoque:**```python
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

## Problemas de seguridad de API
### Falta validación de entrada
**Mal ejemplo:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Mejor enfoque:**```python
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

### Autenticación API insegura
**Mal ejemplo:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Mejor enfoque:**```python
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

### Falta limitación de tasa en las API
**Mal ejemplo:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Mejor enfoque:**```python
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

## Encabezados de seguridad y configuración
### Faltan encabezados de seguridad
**Mal ejemplo:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Mejor enfoque:**```python
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

### Configuración CORS insegura
**Mal ejemplo:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Mejor enfoque:**```python
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

## Estudios de caso
### Estudio de caso 1: Violación de datos de Equifax (2017)
**Incidente:** Los atacantes aprovecharon la vulnerabilidad de Apache Struts para acceder a los datos personales de 147 millones de personas.
**Causa raíz:**
- Software sin parches (CVE-2017-5638)
- No hay validación de entrada en el encabezado de tipo de contenido
- Segmentación de red insuficiente
**Impacto:**
- 1.400 millones de dólares en costes
- Datos personales expuestos (NSS, fechas de nacimiento, direcciones)
- Daño masivo a la reputación
**Lección:** Mantener las dependencias actualizadas; implementar la defensa en profundidad.
### Estudio de caso 2: Incumplimiento del objetivo (2013)
**Incidente:** Los atacantes robaron 40 millones de números de tarjetas de crédito.
**Causa raíz:**
- Credenciales de proveedores externos comprometidas
- No hay segmentación de red entre proveedores y sistemas de pago.
- Alertas de seguridad ignoradas
**Impacto:**
- $202 millones en costos
- CEO y CIO despedidos
- Se requiere una revisión del sistema de pago
**Lección:** Segmentar redes; monitorear el acceso de terceros; responder a las alertas.
### Estudio de caso 3: Ataque a la cadena de suministro de SolarWinds (2020)
**Incidente:** El código malicioso insertado en las actualizaciones de software afectó a más de 18 000 organizaciones.
**Causa raíz:**
- Sistema de construcción comprometido
- Actualizaciones maliciosas firmadas con certificados válidos
- Movimiento lateral una vez dentro de las redes.
**Impacto:**
- Agencias gubernamentales comprometidas
- Empresas Fortune 500 afectadas
- Investigación y remediación en curso
**Lección:** Canalizaciones de construcción seguras; verificar la integridad del software; Arquitectura de confianza cero.
---

## Estrategias de prueba de seguridad
### Pruebas de seguridad de aplicaciones estáticas (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Pruebas dinámicas de seguridad de aplicaciones (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Escaneo de dependencias
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Lista de verificación de pruebas de penetración
- [] Pruebas de inyección SQL
- [] Pruebas XSS (reflejadas, almacenadas, basadas en DOM)
- [] Validación del token CSRF
- [] Intentos de omisión de autenticación
- [] Verificaciones de autorización (escalada de privilegios vertical/horizontal)
- [] Verificación de limitación de velocidad
- [] Presencia de encabezados de seguridad
- [] Configuración SSL/TLS
- [] Revisión de gestión de sesiones
- [] Manejo de errores (sin fuga de información)
---

## Recursos de seguridad
### Top 10 de OWASP (2021)
1. Control de acceso roto
2. Fallos criptográficos
3. Inyección
4. Diseño inseguro
5. Mala configuración de seguridad
6. Componentes vulnerables y obsoletos
7. Fallos de identificación y autenticación
8. Fallos de integridad del software y de los datos
9. Fallas de monitoreo y registro de seguridad
10. Falsificación de solicitudes del lado del servidor
### Herramientas recomendadas
- **Análisis estático**: SonarQube, Semgrep, CodeQL
- **Escaneo de dependencias**: Dependabot, Renovate, Snyk
- **Pruebas dinámicas**: OWASP ZAP, Burp Suite
- **Detección secreta**: GitLeaks, TruffleHog
- **Seguridad de contenedores**: Trivy, Clair, Anchore