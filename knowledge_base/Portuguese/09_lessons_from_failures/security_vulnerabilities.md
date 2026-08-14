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
# Vulnerabilidades de segurança
Este documento consolida vulnerabilidades de segurança comuns no desenvolvimento de software, incluindo ataques de injeção, práticas de código inseguras e erros de segurança.
---

## Injeção SQL
Os ataques de injeção de SQL ocorrem quando entradas de usuários não confiáveis ​​são tratadas incorretamente em consultas de banco de dados, permitindo que invasores manipulem a lógica de consulta, acessem dados não autorizados ou modifiquem o conteúdo do banco de dados.
### Injeção clássica baseada em UNION
**Mau exemplo (código vulnerável):**```python
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

**Por que é ruim:**
- Expõe dados de outras tabelas
- Ignora a lógica de consulta pretendida
- Pode extrair informações confidenciais
**Melhor abordagem:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Estratégias de Prevenção
1. **Use consultas parametrizadas**: nunca concatene a entrada do usuário no SQL
2. **Validação de entrada**: valide e limpe todas as entradas do usuário
3. **Privilégio mínimo**: contas de banco de dados devem ter permissões mínimas
4. **Uso de ORM**: Use mapeadores objeto-relacionais que lidam com escape
5. **Firewalls de aplicativos da Web**: implante WAFs para detectar tentativas de injeção
---

## Scripting entre sites (XSS)
Os ataques Cross-Site Scripting (XSS) ocorrem quando os invasores injetam scripts maliciosos em páginas da web visualizadas por outros usuários.
### XSS refletido
**Mau exemplo (código vulnerável):**```php
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

**Por que é ruim:**
- Entrada do usuário renderizada diretamente sem codificação
- O invasor pode criar URLs maliciosos
- Sequestro de sessão, possível roubo de credenciais
**Melhor abordagem:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS armazenado
**Mau exemplo:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Estratégias de Prevenção
1. **Codificação de saída**: Codifique dados com base no contexto (HTML, JS, URL, CSS)
2. **Validação de entrada**: Rejeite ou limpe entradas maliciosas
3. **Política de segurança de conteúdo**: use cabeçalhos CSP para restringir fontes de script
4. **Cookies HTTPOnly**: Impede o acesso JavaScript aos cookies de sessão
5. **Frameworks Modernos**: Use React, Vue, Angular que escapam automaticamente por padrão
---

## Problemas de segurança de memória
### Estouro de buffer
**Mau Exemplo (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problemas:**
- Pode substituir a memória adjacente
- Pode permitir ataques de execução de código
- Causa comportamento indefinido
**Melhor abordagem:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Use-após-livre
**Exemplo ruim (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Melhor abordagem:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Estratégias de Prevenção
1. **Use linguagens seguras**: prefira Rust, Go, Java, Python a C/C++
2. **Ponteiros Inteligentes**: Use padrões RAII em C++
3. **Verificação de limites**: Sempre valide índices de array
4. **Análise Estática**: Use ferramentas como Valgrind, AddressSanitizer
5. **APIs Memory-Safe**: Use funções de biblioteca padrão mais seguras
---

## Erros de autenticação
### Políticas de senha fraca
**Mau exemplo:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problemas:**
- Suscetível a ataques de força bruta
- Senhas comuns facilmente adivinhadas
- Viola as melhores práticas de segurança
**Melhor abordagem:**```python
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

### Armazenando senhas em texto simples
**Mau exemplo:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Melhor abordagem:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Estratégias de Prevenção
1. **Hashing forte**: Use bcrypt, Argon2 ou scrypt para senhas
2. **Autenticação multifator**: requer verificação adicional
3. **Limitação de Taxa**: Evite ataques de força bruta
4. **Bloqueio de conta**: bloqueio temporário após tentativas fracassadas
5. **Gerenciamento seguro de sessões**: use cookies seguros somente HTTP
---

## Outros erros de segurança
### Segredos codificados
**Mau exemplo:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Melhor abordagem:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Referências diretas a objetos inseguros
**Mau exemplo:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Melhor abordagem:**```python
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

### Limitação de taxa ausente
**Mau exemplo:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Melhor abordagem:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Tópicos Relacionados
- **Falhas de AI/LLM**: consulte`ai_llm_failures.md`para injeção imediata e problemas de segurança específicos de IA
- **Padrões de código inseguros**: veja exemplos de código para segurança de memória e comportamento indefinido
- **Práticas recomendadas de autenticação**: implemente fluxos de autenticação e gerenciamento de sessões adequados
- **Qualidade do código**: consulte`code_quality_issues.md`para práticas de codificação seguras
---

## Vulnerabilidades de segurança adicionais
### Injeção de comando
**O que é:** Execução de comandos arbitrários do sistema por meio de entrada não higienizada do usuário.
**Mau exemplo (código vulnerável):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Ataque:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Por que é ruim:**
- O invasor pode executar qualquer comando do sistema
- Potencial para comprometimento completo do sistema
- Destruição de dados, possível instalação de malware
**Melhor abordagem:**```python
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

### Travessia de caminho
**O que é:** Acessar arquivos fora dos diretórios pretendidos usando sequências ../.
**Mau exemplo:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Ataque:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Melhor abordagem:**```python
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

### Falsificação de solicitação do lado do servidor (SSRF)
**O que é:** Fazer com que o servidor faça solicitações para destinos não intencionais.
**Mau exemplo:**```python
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

**Melhor abordagem:**```python
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

## Erros criptográficos
### Algoritmos de hash fracos
**Mau exemplo:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Por que é ruim:**
- MD5 e SHA1 estão criptograficamente quebrados
- Rápido para calcular (permite força bruta)
- Ataques de colisão demonstrados
**Melhor abordagem:**```python
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

### Chaves de criptografia codificadas
**Mau exemplo:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Melhor abordagem:**```python
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

### Usando o modo BCE
**Mau exemplo:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Por que é ruim:**
- Blocos de texto simples idênticos produzem texto cifrado idêntico
- Os padrões nos dados são visíveis
- O famoso “pinguim do BCE” demonstra o problema
**Melhor abordagem:**```python
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

## Problemas de segurança da API
### Validação de entrada ausente
**Mau exemplo:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Melhor abordagem:**```python
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

### Autenticação de API insegura
**Mau exemplo:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Melhor abordagem:**```python
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

### Limitação de taxa ausente em APIs
**Mau exemplo:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Melhor abordagem:**```python
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

## Cabeçalhos e configuração de segurança
### Cabeçalhos de segurança ausentes
**Mau exemplo:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Melhor abordagem:**```python
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

### Configuração CORS insegura
**Mau exemplo:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Melhor abordagem:**```python
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

## Estudos de caso
### Estudo de caso 1: Violação de dados Equifax (2017)
**Incidente:** Os invasores exploraram a vulnerabilidade do Apache Struts para acessar dados pessoais de 147 milhões de pessoas.
**Causa raiz:**
- Software sem patch (CVE-2017-5638)
- Nenhuma validação de entrada no cabeçalho do tipo de conteúdo
- Segmentação de rede insuficiente
**Impacto:**
- US$ 1,4 bilhão em custos
- Dados pessoais expostos (SSN, datas de nascimento, endereços)
- Danos massivos à reputação
**Lição:** Mantenha as dependências atualizadas; implementar a defesa em profundidade.
### Estudo de caso 2: violação da meta (2013)
**Incidente:** Os invasores roubaram 40 milhões de números de cartão de crédito.
**Causa raiz:**
- Credenciais de fornecedores terceirizados comprometidas
- Sem segmentação de rede entre fornecedores e sistemas de pagamento
- Alertas de segurança ignorados
**Impacto:**
- US$ 202 milhões em custos
- CEO e CIO demitidos
- Revisão do sistema de pagamento necessária
**Lição:** Segmentar redes; monitorar o acesso de terceiros; responder a alertas.
### Estudo de caso 3: Ataque à cadeia de suprimentos da SolarWinds (2020)
**Incidente:** Código malicioso inserido em atualizações de software afetou mais de 18 mil organizações.
**Causa raiz:**
- Sistema de compilação comprometido
- Atualizações maliciosas assinadas com certificados válidos
- Movimento lateral uma vez dentro das redes
**Impacto:**
- Agências governamentais comprometidas
- Empresas Fortune 500 afetadas
- Investigação e remediação contínuas
**Lição:** Pipelines de construção seguros; verificar a integridade do software; arquitetura de confiança zero.
---

## Estratégias de testes de segurança
### Teste estático de segurança de aplicativos (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Teste Dinâmico de Segurança de Aplicativos (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Verificação de Dependências
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Lista de verificação de teste de penetração
- [] teste de injeção SQL
- [] Teste XSS (refletido, armazenado, baseado em DOM)
- [] Validação de token CSRF
- [] Tentativas de ignorar autenticação
- [] Verificações de autorização (escalonamento de privilégios vertical/horizontal)
- [] Verificação de limite de taxa
- [] Presença de cabeçalhos de segurança
- [] configuração SSL/TLS
- [] Revisão de gerenciamento de sessão
- [] Tratamento de erros (sem vazamento de informações)
---

## Recursos de segurança
### Top 10 do OWASP (2021)
1. Controle de acesso quebrado
2. Falhas criptográficas
3. Injeção
4. Design inseguro
5. Configuração incorreta de segurança
6. Componentes vulneráveis e desatualizados
7. Falhas de identificação e autenticação
8. Falhas de software e integridade de dados
9. Falhas de registro e monitoramento de segurança
10. Falsificação de solicitação do lado do servidor
### Ferramentas recomendadas
- **Análise Estática**: SonarQube, Semgrep, CodeQL
- **Verificação de dependências**: Dependabot, Renovate, Snyk
- **Teste Dinâmico**: OWASP ZAP, Burp Suite
- **Detecção de segredos**: GitLeaks, TruffleHog
- **Segurança de contêineres**: Trivy, Clair, Anchore