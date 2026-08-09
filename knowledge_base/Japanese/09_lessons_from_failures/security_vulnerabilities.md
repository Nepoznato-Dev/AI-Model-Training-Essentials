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

# セキュリティの脆弱性
このドキュメントには、インジェクション攻撃、安全でないコードの実践、セキュリティ上の間違いなど、ソフトウェア開発における一般的なセキュリティ脆弱性がまとめられています。
---

## SQL インジェクション
SQL インジェクション攻撃は、信頼できないユーザー入力がデータベース クエリで不適切に処理された場合に発生し、攻撃者がクエリ ロジックを操作したり、未承認のデータにアクセスしたり、データベースの内容を変更したりすることを可能にします。
### 古典的な UNION ベースのインジェクション
**悪い例 (脆弱なコード):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**攻撃：**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**なぜ悪いのか:**
- 他のテーブルからのデータを公開します
- 意図したクエリロジックをバイパスします
- 機密情報を抽出できる
**より良いアプローチ:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### 予防戦略
1. **パラメータ化されたクエリを使用**: ユーザー入力を SQL に連結しないでください。
2. **入力検証**: すべてのユーザー入力を検証し、サニタイズします。
3. **最低権限**: データベース アカウントには最小限の権限が必要です
4. **ORM の使用法**: エスケープを処理するオブジェクト リレーショナル マッパーを使用する
5. **Web アプリケーション ファイアウォール**: WAF を導入してインジェクション試行を検出します
---

## クロスサイト スクリプティング (XSS)
クロスサイト スクリプティング (XSS) 攻撃は、攻撃者が他のユーザーが閲覧している Web ページに悪意のあるスクリプトを挿入するときに発生します。
### 反映された XSS
**悪い例 (脆弱なコード):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**攻撃：**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**なぜ悪いのか:**
- ユーザー入力はエンコードせずに直接レンダリングされます
- 攻撃者は悪意のある URL を作成できる
- セッションハイジャック、資格情報の盗難の可能性
**より良いアプローチ:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### 保存された XSS
**悪い例:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### 予防戦略
1. **出力エンコーディング**: コンテキスト (HTML、JS、URL、CSS) に基づいてデータをエンコードします。
2. **入力検証**: 悪意のある入力を拒否またはサニタイズします。
3. **コンテンツ セキュリティ ポリシー**: CSP ヘッダーを使用してスクリプト ソースを制限する
4. **HTTPOnly Cookies**: JavaScript によるセッション Cookie へのアクセスを防止します。
5. **最新のフレームワーク**: デフォルトで自動エスケープする React、Vue、Angular を使用します。
---

## メモリの安全性の問題
### バッファオーバーフロー
**悪い例 (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**問題:**
- 隣接するメモリを上書き可能
- コード実行攻撃を許可する可能性があります
- 未定義の動作を引き起こす
**より良いアプローチ:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### 無償使用後の使用
**悪い例 (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**より良いアプローチ:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### 予防戦略
1. **安全な言語を使用**: C/C++ よりも Rust、Go、Java、Python を優先します
2. **スマート ポインター**: C++ で RAII パターンを使用する
3. **境界チェック**: 配列インデックスを常に検証します。
4. **静的分析**: Valgrind、AddressSanitizer などのツールを使用する
5. **メモリセーフ API**: より安全な標準ライブラリ関数を使用する
---

## 認証ミス
### 弱いパスワード ポリシー
**悪い例:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**問題:**
- ブルートフォース攻撃を受けやすい
- 一般的なパスワードは推測されやすい
- セキュリティのベストプラクティスに違反します
**より良いアプローチ:**```python
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

### 平文パスワードの保存
**悪い例:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**より良いアプローチ:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### 予防戦略
1. **強力なハッシュ**: パスワードに bcrypt、Argon2、または scrypt を使用します。
2. **多要素認証**: 追加の検証が必要です
3. **レート制限**: ブルートフォース攻撃を防止します
4. **アカウントのロックアウト**: 試行が失敗した後に一時的にロックします
5. **安全なセッション管理**: 安全な HTTP 専用 Cookie を使用する
---

## その他のセキュリティ上の間違い
### ハードコードされたシークレット
**悪い例:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**より良いアプローチ:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### 安全でない直接オブジェクト参照
**悪い例:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**より良いアプローチ:**```python
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

### レート制限がありません
**悪い例:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**より良いアプローチ:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## 関連トピック
- **AI/LLM エラー**: プロンプト インジェクションと AI 固有のセキュリティ問題については、`ai_llm_failures.md` を参照してください。
- **安全でないコード パターン**: メモリの安全性と未定義の動作については、コード例を参照してください。
- **認証のベスト プラクティス**: 適切な認証フローとセッション管理を実装する
- **コード品質**: 安全なコーディングの実践については、`code_quality_issues.md` を参照してください。
---

## 追加のセキュリティ脆弱性
### コマンドインジェクション
**概要:** サニタイズされていないユーザー入力を通じて任意のシステム コマンドを実行します。
**悪い例 (脆弱なコード):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**攻撃：**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**なぜ悪いのか:**
- 攻撃者はあらゆるシステムコマンドを実行できる
- 完全なシステム侵害の可能性
- データ破壊、マルウェアインストールの可能性
**より良いアプローチ:**```python
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

### パストラバーサル
**概要:** ../ シーケンスを使用して、意図したディレクトリの外にあるファイルにアクセスします。
**悪い例:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**攻撃：**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**より良いアプローチ:**```python
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

### サーバーサイドリクエストフォージェリ (SSRF)
**概要:** サーバーに意図しない宛先にリクエストを送信させます。
**悪い例:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**攻撃：**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**より良いアプローチ:**```python
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

## 暗号化の間違い
### 弱いハッシュアルゴリズム
**悪い例:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**なぜ悪いのか:**
- MD5 と SHA1 は暗号化が破られています
- 高速な計算 (ブルート フォースが可能)
- 衝突攻撃のデモンストレーション
**より良いアプローチ:**```python
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

### ハードコードされた暗号化キー
**悪い例:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**より良いアプローチ:**```python
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

### ECB モードの使用
**悪い例:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**なぜ悪いのか:**
- 同一の平文ブロックは同一の暗号文を生成します
- データのパターンが見える
- 有名な「ECBペンギン」が問題を実証
**より良いアプローチ:**```python
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

## API セキュリティの問題
### 入力検証がありません
**悪い例:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**より良いアプローチ:**```python
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

### 安全でない API 認証
**悪い例:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**より良いアプローチ:**```python
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

### API にレート制限がない
**悪い例:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**より良いアプローチ:**```python
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

## セキュリティヘッダーと設定
### セキュリティヘッダーがありません
**悪い例:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**より良いアプローチ:**```python
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

### 安全でない CORS 構成
**悪い例:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**より良いアプローチ:**```python
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

## ケーススタディ
### ケーススタディ 1: Equifax データ侵害 (2017)
**事件:** 攻撃者は Apache Struts の脆弱性を悪用し、1 億 4,700 万人の個人データにアクセスしました。
**根本原因:**
- パッチが適用されていないソフトウェア (CVE-2017-5638)
- コンテンツタイプヘッダーの入力検証はありません
- ネットワークのセグメンテーションが不十分である
**影響:**
- コストは14億ドル
- 個人データの漏洩 (SSN、生年月日、住所)
・甚大な風評被害
**教訓:** 依存関係を常に最新の状態に保ってください。多層防御を実装します。
### ケーススタディ 2: ターゲット違反 (2013 年)
**事件:** 攻撃者は 4,000 万件のクレジット カード番号を盗みました。
**根本原因:**
- サードパーティベンダーの認証情報が侵害された
- ベンダーと決済システムの間でネットワークを分割しない
- 無視されたセキュリティ警告
**影響:**
- 費用は2億200万ドル
- CEO と CIO を解雇
- 決済システムの見直しが必要
**レッスン:** ネットワークをセグメント化する。サードパーティのアクセスを監視します。アラートに応答します。
### ケーススタディ 3: SolarWinds サプライ チェーン攻撃 (2020)
**インシデント:** ソフトウェア更新プログラムに挿入された悪意のあるコードは、18,000 以上の組織に影響を与えました。
**根本原因:**
- 侵害されたビルドシステム
- 有効な証明書を使用して署名された悪意のあるアップデート
- ネットワーク内に入った後の横方向の移動
**影響:**
- 政府機関が侵害された
- 影響を受けるフォーチュン 500 企業
- 継続的な調査と修復
**レッスン:** 安全なビルド パイプライン。ソフトウェアの整合性を検証します。ゼロトラストアーキテクチャ。
---

## セキュリティテスト戦略
### 静的アプリケーション セキュリティ テスト (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### 動的アプリケーション セキュリティ テスト (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### 依存関係のスキャン
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### 侵入テストのチェックリスト
- [ ] SQL インジェクション テスト
- [ ] XSS テスト (反映、保存、DOM ベース)
- [ ] CSRFトークンの検証
- [ ] 認証バイパス試行
- [ ] 権限チェック (垂直/水平権限昇格)
- [ ] レート制限の検証
- [ ] セキュリティヘッダーの存在
- [ ] SSL/TLS 設定
- [ ] セッション管理のレビュー
- [ ] エラー処理（情報漏洩なし）
---

## セキュリティ リソース
### OWASP トップ 10 (2021)
1. 壊れたアクセス制御
2. 暗号化の失敗
3. 注射
4. 安全でない設計
5. セキュリティの設定ミス
6. 脆弱なコンポーネントと古いコンポーネント
7. 識別と認証の失敗
8. ソフトウェアおよびデータの整合性障害
9. セキュリティのログ記録と監視の失敗
10. サーバー側のリクエストフォージェリ
### 推奨ツール
- **静的分析**: SonarQube、Semgrep、CodeQL
- **依存関係スキャン**: dependabot、Renovate、Snyk
- **動的テスト**: OWASP ZAP、Burp Suite
- **秘密検出**: GitLeaks、TruffleHog
- **コンテナセキュリティ**: Trivy、Clair、Anchore