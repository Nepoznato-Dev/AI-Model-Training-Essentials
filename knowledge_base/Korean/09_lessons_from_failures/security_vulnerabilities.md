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
# 보안 취약점
이 문서에는 주입 공격, 안전하지 않은 코드 관행, 보안 실수 등 소프트웨어 개발 시 일반적인 보안 취약점이 통합되어 있습니다.
---

## SQL 주입
SQL 주입 공격은 신뢰할 수 없는 사용자 입력이 데이터베이스 쿼리에서 부적절하게 처리될 때 발생하며, 이로 인해 공격자가 쿼리 논리를 조작하거나, 승인되지 않은 데이터에 액세스하거나, 데이터베이스 콘텐츠를 수정할 수 있습니다.
### 전형적인 UNION 기반 주입
**나쁜 예(취약한 코드):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**공격:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**나쁜 이유:**
- 다른 테이블의 데이터를 노출합니다.
- 의도된 쿼리 로직을 우회합니다.
- 민감한 정보 추출 가능
**더 나은 접근 방식:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### 예방 전략
1. **매개변수화된 쿼리 사용**: 사용자 입력을 SQL에 연결하지 마세요.
2. **입력 유효성 검사**: 모든 사용자 입력의 유효성을 검사하고 삭제합니다.
3. **최소 권한**: 데이터베이스 계정에는 최소한의 권한이 있어야 합니다.
4. **ORM 사용법**: 이스케이프를 처리하는 객체 관계형 매퍼를 사용하세요.
5. **웹 애플리케이션 방화벽**: WAF를 배포하여 주입 시도를 감지합니다.
---

## 교차 사이트 스크립팅(XSS)
XSS(교차 사이트 스크립팅) 공격은 공격자가 다른 사용자가 보는 웹 페이지에 악성 스크립트를 삽입할 때 발생합니다.
### 반영된 XSS
**나쁜 예(취약한 코드):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**공격:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**나쁜 이유:**
- 인코딩 없이 직접 렌더링되는 사용자 입력
- 공격자가 악성 URL을 만들 수 있음
- 세션 하이재킹, 자격 증명 도용 가능
**더 나은 접근 방식:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### 저장된 XSS
**나쁜 예:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### 예방 전략
1. **출력 인코딩**: 컨텍스트(HTML, JS, URL, CSS)를 기반으로 데이터를 인코딩합니다.
2. **입력 유효성 검사**: 악의적인 입력을 거부하거나 삭제합니다.
3. **콘텐츠 보안 정책**: CSP 헤더를 사용하여 스크립트 소스 제한
4. **HTTPOnly 쿠키**: 세션 쿠키에 대한 JavaScript 액세스 방지
5. **최신 프레임워크**: 기본적으로 자동 이스케이프되는 React, Vue, Angular 사용
---

## 메모리 안전 문제
### 버퍼 오버플로
**나쁜 예(C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**문제:**
- 인접 메모리 덮어쓰기 가능
- 코드 실행 공격을 허용할 수 있음
- 정의되지 않은 동작이 발생합니다.
**더 나은 접근 방식:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### 사용 후 무료
**나쁜 예(C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**더 나은 접근 방식:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### 예방 전략
1. **안전한 언어 사용**: C/C++보다 Rust, Go, Java, Python을 선호하세요.
2. **스마트 포인터**: C++에서 RAII 패턴 사용
3. **경계 검사**: 항상 배열 인덱스의 유효성을 검사합니다.
4. **정적 분석**: Valgrind, AddressSanitizer와 같은 도구 사용
5. **메모리 안전 API**: 보다 안전한 표준 라이브러리 함수 사용
---

## 인증 실수
### 취약한 비밀번호 정책
**나쁜 예:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**문제:**
- 무차별 공격에 취약
- 쉽게 추측할 수 있는 일반적인 비밀번호
- 보안 모범 사례를 위반합니다.
**더 나은 접근 방식:**```python
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

### 일반 텍스트 비밀번호 저장
**나쁜 예:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**더 나은 접근 방식:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### 예방 전략
1. **강력한 해싱**: 비밀번호에 bcrypt, Argon2 또는 scrypt를 사용하세요.
2. **다단계 인증**: 추가 확인 필요
3. **속도 제한**: 무차별 대입 공격 방지
4. **계정 잠금**: 시도 실패 후 일시적으로 잠깁니다.
5. **보안 세션 관리**: 안전한 HTTP 전용 쿠키 사용
---

## 기타 보안 실수
### 하드코딩된 비밀
**나쁜 예:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**더 나은 접근 방식:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### 안전하지 않은 직접 개체 참조
**나쁜 예:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**더 나은 접근 방식:**```python
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

### 속도 제한 누락
**나쁜 예:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**더 나은 접근 방식:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## 관련 주제
- **AI/LLM 오류**: 프롬프트 삽입 및 AI 관련 보안 문제는 `ai_llm_failures.md`를 참조하세요.
- **안전하지 않은 코드 패턴**: 메모리 안전 및 정의되지 않은 동작에 대한 코드 예제를 참조하세요.
- **인증 모범 사례**: 적절한 인증 흐름 및 세션 관리 구현
- **코드 품질**: 보안 코딩 방법은 `code_quality_issues.md`를 참조하세요.
---

## 추가 보안 취약점
### 명령 주입
**정의:** 삭제되지 않은 사용자 입력을 통해 임의의 시스템 명령을 실행합니다.
**나쁜 예(취약한 코드):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**공격:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**나쁜 이유:**
- 공격자는 모든 시스템 명령을 실행할 수 있습니다.
- 시스템 전체가 손상될 가능성
- 데이터 파기, 악성코드 설치 가능
**더 나은 접근 방식:**```python
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

### 경로 순회
**정의:** ../ 시퀀스를 사용하여 의도한 디렉터리 외부의 파일에 액세스합니다.
**나쁜 예:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**공격:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**더 나은 접근 방식:**```python
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

### 서버측 요청 위조(SSRF)
**정의:** 서버가 의도하지 않은 대상에 요청을 하도록 만드는 것입니다.
**나쁜 예:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**공격:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**더 나은 접근 방식:**```python
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

## 암호화 실수
### 약한 해싱 알고리즘
**나쁜 예:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**나쁜 이유:**
- MD5 및 SHA1이 암호화되어 손상되었습니다.
- 빠른 계산(무차별 대입 가능)
- 충돌 공격 시연
**더 나은 접근 방식:**```python
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

### 하드코딩된 암호화 키
**나쁜 예:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**더 나은 접근 방식:**```python
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

### ECB 모드 사용
**나쁜 예:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**나쁜 이유:**
- 동일한 평문 블록은 동일한 암호문을 생성합니다.
- 데이터의 패턴이 보입니다.
- 유명한 "ECB 펭귄"이 문제를 보여줍니다.
**더 나은 접근 방식:**```python
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

## API 보안 문제
### 입력 유효성 검사 누락
**나쁜 예:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**더 나은 접근 방식:**```python
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

### 안전하지 않은 API 인증
**나쁜 예:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**더 나은 접근 방식:**```python
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

### API 속도 제한 누락
**나쁜 예:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**더 나은 접근 방식:**```python
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

## 보안 헤더 및 구성
### 보안 헤더 누락
**나쁜 예:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**더 나은 접근 방식:**```python
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

### 안전하지 않은 CORS 구성
**나쁜 예:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**더 나은 접근 방식:**```python
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

## 사례 연구
### 사례 연구 1: Equifax 데이터 유출(2017)
**사건:** 공격자들은 Apache Struts 취약점을 악용하여 1억 4,700만 명의 개인 데이터에 접근했습니다.
**근본 원인:**
- 패치되지 않은 소프트웨어(CVE-2017-5638)
- 콘텐츠 유형 헤더에 대한 입력 유효성 검사가 없습니다.
- 네트워크 세분화가 부족함
**영향:**
- 비용 14억 달러
- 개인정보 노출(SSN, 생년월일, 주소)
- 막대한 명예훼손
**강의:** 종속성을 계속 업데이트하세요. 심층 방어를 구현합니다.
### 사례 연구 2: 표적 침해(2013)
**사건:** 공격자들은 4천만 개의 신용카드 번호를 훔쳤습니다.
**근본 원인:**
- 타사 공급업체 자격 증명이 손상되었습니다.
- 벤더와 결제 시스템 간 네트워크 분할이 없습니다.
- 무시된 보안 경고
**영향:**
- 비용 2억 2백만 달러
- CEO 및 CIO 해고
- 결제시스템 전면 개편 필요
**강의:** 세그먼트 네트워크; 제3자 액세스를 모니터링합니다. 경고에 응답합니다.
### 사례 연구 3: SolarWinds 공급망 공격(2020)
**사건:** 소프트웨어 업데이트에 삽입된 악성 코드가 18,000개 이상의 조직에 영향을 미쳤습니다.
**근본 원인:**
- 손상된 빌드 시스템
- 유효한 인증서로 서명된 악성 업데이트
- 네트워크 내부에서 측면 이동
**영향:**
- 정부 기관이 손상됨
- Fortune 500대 기업이 영향을 받음
- 지속적인 조사 및 해결
**강의:** 보안 빌드 파이프라인; 소프트웨어 무결성을 확인합니다. 제로 트러스트 아키텍처.
---

## 보안 테스트 전략
### 정적 애플리케이션 보안 테스트(SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### 동적 애플리케이션 보안 테스트(DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### 종속성 검색
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### 침투 테스트 체크리스트
- [ ] SQL 주입 테스트
- [ ] XSS 테스트(반영, 저장, DOM 기반)
- [ ] CSRF 토큰 검증
- [ ] 인증 우회 시도
- [ ] 권한 확인(수직/수평 권한 상승)
- [ ] 속도 제한 확인
- [ ] 보안 헤더 존재
- [ ] SSL/TLS 구성
- [ ] 세션 관리 검토
- [ ] 오류 처리(정보 유출 없음)
---

## 보안 리소스
### OWASP 상위 10(2021)
1. 손상된 접근 통제
2. 암호화 실패
3. 주입
4. 안전하지 않은 디자인
5. 잘못된 보안 구성
6. 취약하고 오래된 구성요소
7. 식별 및 인증 실패
8. 소프트웨어 및 데이터 무결성 오류
9. 보안 로깅 및 모니터링 실패
10. 서버측 요청 위조
### 권장 도구
- **정적 분석**: SonarQube, Semgrep, CodeQL
- **종속성 검색**: dependencyabot, Renovate, Snyk
- **동적 테스트**: OWASP ZAP, Burp Suite
- **비밀 탐지**: GitLeaks, TruffleHog
- **컨테이너 보안**: Trivy, Clair, Anchore