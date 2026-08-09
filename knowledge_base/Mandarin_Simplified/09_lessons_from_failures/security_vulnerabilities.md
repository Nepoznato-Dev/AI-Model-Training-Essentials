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

# 安全漏洞
本文档整合了软件开发中的常见安全漏洞，包括注入攻击、不安全代码实践和安全错误。
---

## SQL注入
当数据库查询中不受信任的用户输入处理不当时，就会发生 SQL 注入攻击，从而使攻击者能够操纵查询逻辑、访问未经授权的数据或修改数据库内容。
### 经典的基于 UNION 的注入
**错误示例（易受攻击的代码）：**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**攻击：**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**为什么不好：**
- 公开其他表中的数据
- 绕过预期的查询逻辑
- 可以提取敏感信息
**更好的方法：**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### 预防策略
1. **使用参数化查询**：切勿将用户输入连接到 SQL 中
2. **输入验证**：验证并清理所有用户输入
3. **最小权限**：数据库帐户应具有最小权限
4. **ORM 用法**：使用处理转义的对象关系映射器
5. **Web应用程序防火墙**：部署WAF以检测注入尝试
---

## 跨站脚本 (XSS)
当攻击者将恶意脚本注入其他用户查看的网页时，就会发生跨站脚本 (XSS) 攻击。
### 反射 XSS
**错误示例（易受攻击的代码）：**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**攻击：**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**为什么不好：**
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

### 存储型 XSS
**错误的例子：**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### 预防策略
1. **输出编码**：根据上下文（HTML、JS、URL、CSS）对数据进行编码
2. **输入验证**：拒绝或净化恶意输入
3. **内容安全策略**：使用CSP标头限制脚本来源
4. **HTTPOnly Cookies**：防止 JavaScript 访问会话 cookie
5. **现代框架**：使用默认自动转义的React、Vue、Angular
---

## 内存安全问题
### 缓冲区溢出
**坏例子（C）：**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**问题：**
- 可以覆盖相邻的内存
- 可能允许代码执行攻击
- 导致未定义的行为
**更好的方法：**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### 释放后使用
**错误示例 (C++)：**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**更好的方法：**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### 预防策略
1. **使用安全语言**：优先选择 Rust、Go、Java、Python，而不是 C/C++
2. **智能指针**：在C++中使用RAII模式
3. **边界检查**：始终验证数组索引
4. **静态分析**：使用Valgrind、AddressSanitizer等工具
5. **内存安全API**：使用更安全的标准库函数
---

## 身份验证错误
### 弱密码策略
**错误的例子：**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**问题：**
- 容易受到暴力攻击
- 常见密码容易被猜到
- 违反安全最佳实践
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

### 存储明文密码
**错误的例子：**```python
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

### 预防策略
1. **强哈希**：使用 bcrypt、Argon2 或 scrypt 作为密码
2. **多重身份验证**：需要额外验证
3. **速率限制**：防止暴力攻击
4. **账户锁定**：尝试失败后暂时锁定
5. **安全会话管理**：使用安全的、仅限 HTTP 的 cookie
---

## 其他安全错误
### 硬编码的秘密
**错误的例子：**```python
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

### 不安全的直接对象引用
**错误的例子：**```python
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

### 丢失率限制
**错误的例子：**```python
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

## 相关主题
- **AI/LLM 失败**：请参阅`ai_llm_failures.md`了解提示注入和 AI 特定的安全问题
- **不安全的代码模式**：请参阅代码示例以了解内存安全和未定义的行为
- **身份验证最佳实践**：实施正确的身份验证流程和会话管理
- **代码质量**：请参阅`code_quality_issues.md`了解安全编码实践
---

## 其他安全漏洞
### 命令注入
**它是什么：** 通过未经净化的用户输入执行任意系统命令。
**错误示例（易受攻击的代码）：**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**攻击：**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**为什么不好：**
- 攻击者可以执行任何系统命令
- 整个系统受到损害的可能性
- 数据破坏、可能安装恶意软件
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

### 路径遍历
**它是什么：** 使用 ../ 序列访问预期目录之外的文件。
**错误的例子：**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**攻击：**```
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

### 服务器端请求伪造 (SSRF)
**它是什么：** 让服务器向非预期的目的地发出请求。
**错误的例子：**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**攻击：**```
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

## 密码错误
### 弱哈希算法
**错误的例子：**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**为什么不好：**
- MD5 和 SHA1 的密码被破坏
- 计算速度快（支持暴力破解）
- 展示了碰撞攻击
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

### 硬编码加密密钥
**错误的例子：**```python
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
**错误的例子：**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**为什么不好：**
- 相同的明文块产生相同的密文
- 数据中的模式是可见的
——著名的“欧洲央行企鹅”演示了这个问题
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

## API 安全问题
### 缺少输入验证
**错误的例子：**```python
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

### 不安全的 API 身份验证
**错误的例子：**```python
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
**错误的例子：**```python
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

## 安全标头和配置
### 缺少安全标头
**错误的例子：**```python
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
**错误的例子：**```python
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
### 案例研究 1：Equifax 数据泄露 (2017)
**事件：** 攻击者利用 Apache Struts 漏洞访问 1.47 亿人的个人数据。
**根本原因：**
- 未修补的软件 (CVE-2017-5638)
- 内容类型标头没有输入验证
- 网络分段不足
**影响：**
- 14亿美元的成本
- 暴露的个人数据（SSN、出生日期、地址）
- 严重的声誉损害
**课程：** 保持依赖关系更新；实施纵深防御。
### 案例研究 2：目标违反 (2013)
**事件：** 攻击者窃取了 4000 万张信用卡号码。
**根本原因：**
- 第三方供应商凭证遭到泄露
- 供应商和支付系统之间没有网络分段
- 忽略安全警报
**影响：**
- 2.02 亿美元的成本
- 首席执行官和首席信息官被解雇
- 需要检修支付系统
**课程：** 分段网络；监控第三方访问；响应警报。
### 案例研究 3：SolarWinds 供应链攻击 (2020)
**事件：** 插入软件更新中的恶意代码影响了 18,000 多个组织。
**根本原因：**
- 受损的构建系统
- 使用有效证书签署恶意更新
- 进入网络后横向移动
**影响：**
- 政府机构受到损害
- 财富 500 强企业受到影响
- 持续调查和补救
**课程：** 安全构建管道；验证软件完整性；零信任架构。
---

## 安全测试策略
### 静态应用程序安全测试 (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### 动态应用程序安全测试 (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### 依赖关系扫描
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### 渗透测试清单
- [ ] SQL注入测试
- [ ] XSS 测试（反射、存储、基于 DOM）
- [ ] CSRF 令牌验证
- [ ] 验证绕过尝试
- [ ] 授权检查（垂直/水平权限提升）
- [ ] 限速验证
- [ ] 安全标头的存在
- [ ] SSL/TLS 配置
- [ ] 会议管理审查
- [ ] 错误处理（无信息泄露）
---

## 安全资源
### OWASP 前 10 名 (2021)
1. 访问控制被破坏
2. 加密失败
3、注射
4. 不安全的设计
5. 安全配置错误
6. 易受攻击和过时的组件
7. 身份验证失败
8. 软件和数据完整性故障
9. 安全日志记录和监控故障
10. 服务器端请求伪造
### 推荐工具
- **静态分析**：SonarQube、Semgrep、CodeQL
- **依赖关系扫描**：Dependabot、Renovate、Snyk
- **动态测试**：OWASP ZAP、Burp Suite
- **秘密检测**：GitLeaks、TruffleHog
- **容器安全**：Trivy、Clair、Anchore