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
# 安全漏洞
本文檔整合了軟體開發中常見的安全漏洞，包括注入攻擊、不安全程式碼實務和安全性錯誤。
---

## SQL注入
當資料庫查詢中不受信任的使用者輸入處理不當時，就會發生 SQL 注入攻擊，使攻擊者能夠操縱查詢邏輯、存取未經授權的資料或修改資料庫內容。
### 經典的基於 UNION 的注入
**錯誤範例（易受攻擊的程式碼）：**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**攻擊：**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**為什麼不好：**
- 公開其他表中的數據
- 繞過預期的查詢邏輯
- 可以提取敏感資訊
**更好的方法：**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### 預防策略
1. **使用參數化查詢**：切勿將使用者輸入連接到 SQL 中
2. **輸入驗證**：驗證並清理所有使用者輸入
3. **最小權限**：資料庫帳戶應具有最小權限
4. **ORM 用法**：使用處理轉義的物件關係映射器
5. **Web應用程式防火牆**：部署WAF以偵測注入嘗試
---

## 跨站腳本 (XSS)
當攻擊者將惡意腳本注入其他使用者檢視的網頁時，就會發生跨站腳本 (XSS) 攻擊。
### 反射 XSS
**錯誤範例（易受攻擊的程式碼）：**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**攻擊：**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**為什麼不好：**
- 用户输入直接渲染，无需编码
- 攻击者可以制作恶意 URL
- 可能发生会话劫持、凭证盗窃
**更好的方法：**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### 儲存型 XSS
**錯誤的例子：**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### 預防策略
1. **輸出編碼**：根據上下文（HTML、JS、URL、CSS）對資料進行編碼
2. **輸入驗證**：拒絕或淨化惡意輸入
3. **內容安全策略**：使用CSP標頭限制腳本來源
4. **HTTPOnly Cookies**：防止 JavaScript 存取會話 cookie
5. **現代框架**：使用預設自動轉義的React、Vue、Angular
---

## 記憶體安全問題
### 緩衝區溢出
**壞例子（C）：**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**問題：**
- 可以覆蓋相鄰的內存
- 可能允許程式碼執行攻擊
- 導致未定義的行為
**更好的方法：**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### 釋放後使用
**錯誤範例 (C++)：**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**更好的方法：**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### 預防策略
1. **使用安全語言**：優先選擇 Rust、Go、Java、Python，而不是 C/C++
2. **智慧指標**：在C++中使用RAII模式
3. **邊界檢查**：始終驗證陣列索引
4. **靜態分析**：使用Valgrind、AddressSanitizer等工具
5. **記憶體安全API**：使用更安全的標準函式庫函數
---

## 身份驗證錯誤
### 弱密碼策略
**錯誤的例子：**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**問題：**
- 容易受到暴力攻擊
- 常見密碼容易被猜到
- 違反安全最佳實踐
**更好的方法：**```python
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

### 儲存明文密碼
**錯誤的例子：**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**更好的方法：**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### 預防策略
1. **強雜湊**：使用 bcrypt、Argon2 或 scrypt 作為密碼
2. **多重身份驗證**：需要額外驗證
3. **速率限制**：防止暴力攻擊
4. **帳號鎖定**：嘗試失敗後暫時鎖定
5. **安全性會話管理**：使用安全性的、僅限 HTTP 的 cookie
---

## 其他安全錯誤
### 硬編碼的秘密
**錯誤的例子：**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**更好的方法：**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### 不安全的直接物件引用
**錯誤的例子：**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**更好的方法：**```python
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

### 丟失率限制
**錯誤的例子：**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**更好的方法：**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## 相關主題
- **AI/LLM 失敗**：請參閱`ai_llm_failures.md`以了解提示注入和 AI 特定的安全問題
- **不安全的程式碼模式**：請參閱程式碼範例以了解記憶體安全性和未定義的行為
- **身份驗證最佳實踐**：實施正確的身份驗證流程和會話管理
- **代碼品質**：請參閱`code_quality_issues.md`以了解安全編碼實踐
---

## 其他安全漏洞
### 指令注入
**它是什麼：** 透過未經淨化的使用者輸入執行任意系統命令。
**錯誤範例（易受攻擊的程式碼）：**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**攻擊：**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**為什麼不好：**
- 攻擊者可以執行任何系統指令
- 整個系統受到損害的可能性
- 資料破壞、可能安裝惡意軟體
**更好的方法：**```python
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

### 路徑遍歷
**它是什麼：** 使用 ../ 序列存取預期目錄之外的檔案。
**錯誤的例子：**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**攻擊：**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**更好的方法：**```python
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

### 伺服器端請求偽造 (SSRF)
**它是什麼：** 讓伺服器向非預期的目的地發出請求。
**錯誤的例子：**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**攻擊：**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**更好的方法：**```python
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

## 密碼錯誤
### 弱哈希演算法
**錯誤的例子：**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**為什麼不好：**
- MD5 和 SHA1 的密碼被破壞
- 計算速度快（支援暴力破解）
- 展示了碰撞攻擊
**更好的方法：**```python
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

### 硬編碼加密金鑰
**錯誤的例子：**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**更好的方法：**```python
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

### 使用 ECB 模式
**錯誤的例子：**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**為什麼不好：**
- 相同的明文區塊產生相同的密文
- 資料中的模式是可見的
——著名的「歐洲央行企鵝」示範了這個問題
**更好的方法：**```python
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

## API 安全性問題
### 缺少輸入驗證
**錯誤的例子：**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**更好的方法：**```python
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

### 不安全的 API 驗證
**錯誤的例子：**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**更好的方法：**```python
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

### API 缺少速率限制
**錯誤的例子：**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**更好的方法：**```python
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

## 安全標頭和配置
### 缺少安全標頭
**錯誤的例子：**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**更好的方法：**```python
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

### 不安全的 CORS 配置
**錯誤的例子：**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**更好的方法：**```python
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

## 案例研究
### 案例研究 1：Equifax 資料外洩 (2017)
**事件：** 攻擊者利用 Apache Struts 漏洞存取 1.47 億人的個人資料。
**根本原因：**
- 未修補的軟體 (CVE-2017-5638)
- 內容類型標頭沒有輸入驗證
- 網路分段不足
**影響：**
- 14億美元的成本
- 暴露的個人資料（SSN、出生日期、地址）
- 嚴重的聲譽損害
**課程：** 保持依賴關係更新；實施縱深防禦。
### 個案研究 2：目標違反 (2013)
**事件：** 攻擊者竊取了 4000 萬張信用卡號碼。
**根本原因：**
- 第三方供應商憑證遭到洩露
- 供應商與支付系統之間沒有網路分段
- 忽略安全警報
**影響：**
- 2.02 億美元的成本
- 執行長和資訊長被解僱
- 需要檢修支付系統
**課程：** 分段網路；監控第三方存取；回應警報。
### 案例研究 3：SolarWinds 供應鏈攻擊 (2020)
**事件：** 插入軟體更新中的惡意程式碼影響了 18,000 多個組織。
**根本原因：**
- 受損的建構系統
- 使用有效憑證簽署惡意更新
- 進入網路後橫向移動
**影響：**
- 政府機關受到損害
- 財富 500 強企業受到影響
- 持續調查和補救
**課程：** 安全建置管道；驗證軟體完整性；零信任架構。
---

## 安全測試策略
### 靜態應用程式安全測試 (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### 動態應用程式安全測試 (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### 依賴關係掃描
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### 滲透測試清單
- [ ] SQL注入測試
- [ ] XSS 測試（反射、儲存、基於 DOM）
- [ ] CSRF 令牌驗證
- [ ] 驗證繞過嘗試
- [ ] 授權檢查（垂直/水平權限提升）
- [ ] 限速驗證
- [ ] 安全標頭的存在
- [ ] SSL/TLS 配置
- [ ] 會議管理審查
- [ ] 錯誤處理（無資訊外洩）
---

## 安全資源
### OWASP 前 10 名 (2021)
1. 存取控制被破壞
2. 加密失敗
3、注射
4. 不安全的設計
5. 安全設定錯誤
6. 易受攻擊和過時的組件
7. 身份驗證失敗
8. 軟體和資料完整性故障
9. 安全日誌記錄和監控故障
10. 伺服器端請求偽造
### 推薦工具
- **靜態分析**：SonarQube、Semgrep、CodeQL
- **依賴關係掃描**：Dependabot、Renovate、Snyk
- **動態測試**：OWASP ZAP、Burp Suite
- **秘密檢測**：GitLeaks、TruffleHog
- **容器安全**：Trivy、Clair、Anchore