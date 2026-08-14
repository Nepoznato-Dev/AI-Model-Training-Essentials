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
#Lỗ hổng bảo mật
Tài liệu này tổng hợp các lỗ hổng bảo mật phổ biến trong phát triển phần mềm, bao gồm các cuộc tấn công tiêm nhiễm, thực hành mã không an toàn và các lỗi bảo mật.
---

## Chèn SQL
Các cuộc tấn công tiêm nhiễm SQL xảy ra khi đầu vào của người dùng không đáng tin cậy được xử lý không đúng cách trong các truy vấn cơ sở dữ liệu, cho phép kẻ tấn công thao túng logic truy vấn, truy cập dữ liệu trái phép hoặc sửa đổi nội dung cơ sở dữ liệu.
### Tiêm dựa trên UNION cổ điển
**Ví dụ xấu (Mã dễ bị tổn thương):**```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Tấn công:**```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Tại sao nó xấu:**
- Hiển thị dữ liệu từ các bảng khác
- Bỏ qua logic truy vấn dự định
- Có thể trích xuất thông tin nhạy cảm
**Cách tiếp cận tốt hơn:**```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Chiến lược phòng ngừa
1. **Sử dụng truy vấn được tham số hóa**: Không bao giờ nối dữ liệu đầu vào của người dùng vào SQL
2. **Xác thực đầu vào**: Xác thực và vệ sinh tất cả đầu vào của người dùng
3. **Đặc quyền tối thiểu**: Tài khoản cơ sở dữ liệu phải có quyền tối thiểu
4. **Cách sử dụng ORM**: Sử dụng Trình ánh xạ quan hệ đối tượng để xử lý việc thoát
5. **Tường lửa ứng dụng web**: Triển khai WAF để phát hiện các nỗ lực tiêm nhiễm
---

## Tập lệnh chéo trang (XSS)
Các cuộc tấn công Cross-Site Scripting (XSS) xảy ra khi kẻ tấn công đưa các tập lệnh độc hại vào các trang web được người dùng khác xem.
### XSS được phản ánh
**Ví dụ xấu (Mã dễ bị tổn thương):**```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Tấn công:**```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Tại sao nó xấu:**
- Đầu vào của người dùng được hiển thị trực tiếp mà không cần mã hóa
- Kẻ tấn công có thể tạo các URL độc hại
- Có thể chiếm quyền điều khiển phiên, đánh cắp thông tin xác thực
**Cách tiếp cận tốt hơn:**```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### XSS được lưu trữ
**Ví dụ tồi:**```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Chiến lược phòng ngừa
1. **Mã hóa đầu ra**: Mã hóa dữ liệu dựa trên ngữ cảnh (HTML, JS, URL, CSS)
2. **Xác thực đầu vào**: Từ chối hoặc loại bỏ đầu vào độc hại
3. **Chính sách bảo mật nội dung**: Sử dụng tiêu đề CSP để hạn chế nguồn tập lệnh
4. **Cookie chỉ HTTP**: Ngăn chặn quyền truy cập của JavaScript vào cookie phiên
5. **Các khung hiện đại**: Sử dụng React, Vue, Angular tự động thoát theo mặc định
---

## Vấn đề về an toàn bộ nhớ
### Tràn bộ đệm
**Ví dụ xấu (C):**```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Vấn đề:**
- Có thể ghi đè lên bộ nhớ lân cận
- Có thể cho phép tấn công thực thi mã
- Gây ra hành vi không xác định
**Cách tiếp cận tốt hơn:**```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Dùng-Sau-Miễn phí
**Ví dụ tồi (C++):**```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Cách tiếp cận tốt hơn:**```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Chiến lược phòng ngừa
1. **Sử dụng ngôn ngữ an toàn**: Thích Rust, Go, Java, Python hơn C/C++
2. **Con trỏ thông minh**: Sử dụng mẫu RAII trong C++
3. **Kiểm tra giới hạn**: Luôn xác thực các chỉ số mảng
4. **Phân tích tĩnh**: Sử dụng các công cụ như Valgrind, addressSanitizer
5. **API an toàn bộ nhớ**: Sử dụng các chức năng thư viện tiêu chuẩn an toàn hơn
---

## Lỗi xác thực
### Chính sách mật khẩu yếu
**Ví dụ tồi:**```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Vấn đề:**
- Dễ bị tấn công vũ phu
- Mật khẩu thông dụng dễ đoán
- Vi phạm các biện pháp bảo mật tốt nhất
**Cách tiếp cận tốt hơn:**```python
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

### Lưu trữ mật khẩu văn bản gốc
**Ví dụ tồi:**```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Cách tiếp cận tốt hơn:**```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Chiến lược phòng ngừa
1. **Băm mạnh**: Sử dụng bcrypt, Argon2 hoặc tiền điện tử cho mật khẩu
2. **Xác thực đa yếu tố**: Yêu cầu xác minh bổ sung
3. **Giới hạn tỷ lệ**: Ngăn chặn các cuộc tấn công vũ phu
4. **Khóa tài khoản**: Khóa tạm thời sau khi thử không thành công
5. **Quản lý phiên an toàn**: Sử dụng cookie an toàn, chỉ HTTP
---

## Các lỗi bảo mật khác
### Bí mật được mã hóa cứng
**Ví dụ tồi:**```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Cách tiếp cận tốt hơn:**```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Tham chiếu đối tượng trực tiếp không an toàn
**Ví dụ tồi:**```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Cách tiếp cận tốt hơn:**```python
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

### Thiếu giới hạn tỷ lệ
**Ví dụ tồi:**```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Cách tiếp cận tốt hơn:**```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Chủ đề liên quan
- **Lỗi AI/LLM**: Xem`ai_llm_failures.md`để biết các vấn đề về tiêm nhanh và bảo mật dành riêng cho AI
- **Mẫu mã không an toàn**: Xem ví dụ mã về an toàn bộ nhớ và hành vi không xác định
- **Các phương pháp xác thực tốt nhất**: Triển khai các luồng xác thực và quản lý phiên thích hợp
- **Chất lượng mã**: Xem`code_quality_issues.md`để biết các phương pháp mã hóa an toàn
---

## Các lỗ hổng bảo mật bổ sung
### Lệnh tiêm
**Nó là gì:** Thực thi các lệnh hệ thống tùy ý thông qua đầu vào của người dùng chưa được dọn dẹp.
**Ví dụ xấu (Mã dễ bị tổn thương):**```python
# VULNERABLE: User input passed to shell
def get_file_info(filename):
    os.system(f"ls -la {filename}")  # Command injection possible!
```

**Tấn công:**```
Input: file.txt; rm -rf /
Executed: ls -la file.txt; rm -rf /
```

**Tại sao nó xấu:**
- Kẻ tấn công có thể thực thi bất kỳ lệnh hệ thống nào
- Khả năng xâm phạm toàn bộ hệ thống
- Có thể hủy dữ liệu, cài đặt phần mềm độc hại
**Cách tiếp cận tốt hơn:**```python
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

### Truyền tải đường dẫn
**Nó là gì:** Truy cập các tệp bên ngoài các thư mục dự định bằng cách sử dụng chuỗi ../.
**Ví dụ tồi:**```python
# VULNERABLE: No path validation
def serve_file(filename):
    filepath = f"/var/www/files/{filename}"
    return open(filepath).read()
```

**Tấn công:**```
Input: ../../etc/passwd
Result: Reads /etc/passwd (system file)
```

**Cách tiếp cận tốt hơn:**```python
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

### Giả mạo yêu cầu phía máy chủ (SSRF)
**Nó là gì:** Khiến máy chủ đưa ra yêu cầu đến các đích đến ngoài ý muốn.
**Ví dụ tồi:**```python
# VULNERABLE: User controls URL fetched by server
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)  # Can access internal services!
    return response.text
```

**Tấn công:**```
Input: http://localhost:6379/  (Redis admin interface)
Input: http://169.254.169.254/latest/meta-data/  (AWS metadata)
```

**Cách tiếp cận tốt hơn:**```python
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

## Lỗi mật mã
### Thuật toán băm yếu
**Ví dụ tồi:**```python
import hashlib

# NEVER use MD5 or SHA1 for security purposes
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # BROKEN!
```

**Tại sao nó xấu:**
- MD5 và SHA1 bị phá mã hóa
- Tính toán nhanh (cho phép sử dụng vũ lực)
- Các cuộc tấn công va chạm đã được chứng minh
**Cách tiếp cận tốt hơn:**```python
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

### Khóa mã hóa được mã hóa cứng
**Ví dụ tồi:**```python
# NEVER hardcode encryption keys
ENCRYPTION_KEY = b'0123456789abcdef'  # Visible in source code!

def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(data))
```

**Cách tiếp cận tốt hơn:**```python
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

### Sử dụng Chế độ ECB
**Ví dụ tồi:**```python
# ECB mode reveals patterns in plaintext
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
```

**Tại sao nó xấu:**
- Các khối bản rõ giống nhau tạo ra bản mã giống hệt nhau
- Các mẫu trong dữ liệu có thể nhìn thấy được
- “Chim cánh cụt ECB” nổi tiếng chứng minh vấn đề
**Cách tiếp cận tốt hơn:**```python
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

## Vấn đề bảo mật API
### Thiếu xác thực đầu vào
**Ví dụ tồi:**```python
@app.route('/api/user/<user_id>')
def get_user(user_id):
    # user_id could be anything - SQL injection, XSS, etc.
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Cách tiếp cận tốt hơn:**```python
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

### Xác thực API không an toàn
**Ví dụ tồi:**```python
# Sending credentials in URL parameters
GET /api/data?api_key=sk-12345&user=admin

# Problems:
# - Logged in server logs
# - Visible in browser history
# - Sent in Referer header
```

**Cách tiếp cận tốt hơn:**```python
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

### Thiếu giới hạn tỷ lệ trên API
**Ví dụ tồi:**```python
# API endpoint with no rate limiting
@app.route('/api/search')
def search():
    results = perform_search(request.args.get('q'))
    return jsonify(results)
# Can be abused for scraping, DoS, resource exhaustion
```

**Cách tiếp cận tốt hơn:**```python
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

## Tiêu đề và cấu hình bảo mật
### Thiếu tiêu đề bảo mật
**Ví dụ tồi:**```python
# No security headers configured
@app.route('/')
def index():
    return render_template('index.html')
```

**Cách tiếp cận tốt hơn:**```python
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

### Cấu hình CORS không an toàn
**Ví dụ tồi:**```python
# Allow all origins - DANGEROUS!
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Too permissive!
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
```

**Cách tiếp cận tốt hơn:**```python
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

## Nghiên cứu trường hợp
### Nghiên cứu điển hình 1: Vi phạm dữ liệu Equifax (2017)
**Sự cố:** Kẻ tấn công khai thác lỗ hổng Apache Struts để truy cập dữ liệu cá nhân của 147 triệu người.
**Nguyên nhân cốt lõi:**
- Phần mềm chưa được vá (CVE-2017-5638)
- Không có xác thực đầu vào trên tiêu đề loại nội dung
- Phân đoạn mạng không đầy đủ
**Tác động:**
- Chi phí 1,4 tỷ USD
- Dữ liệu cá nhân bị lộ (SSN, ngày sinh, địa chỉ)
- Thiệt hại danh tiếng lớn
**Bài học:** Luôn cập nhật các phần phụ thuộc; triển khai phòng thủ theo chiều sâu.
### Nghiên cứu điển hình 2: Vi phạm mục tiêu (2013)
**Sự cố:** Kẻ tấn công đã đánh cắp 40 triệu số thẻ tín dụng.
**Nguyên nhân cốt lõi:**
- Thông tin xác thực của nhà cung cấp bên thứ ba bị xâm phạm
- Không có sự phân chia mạng giữa nhà cung cấp và hệ thống thanh toán
- Bỏ qua cảnh báo bảo mật
**Tác động:**
- Chi phí 202 triệu USD
- CEO và CIO bị sa thải
- Yêu cầu đại tu hệ thống thanh toán
**Bài học:** Mạng phân đoạn; giám sát quyền truy cập của bên thứ ba; trả lời các cảnh báo.
### Nghiên cứu điển hình 3: Tấn công chuỗi cung ứng SolarWinds (2020)
**Sự cố:** Mã độc được chèn vào các bản cập nhật phần mềm đã ảnh hưởng đến hơn 18.000 tổ chức.
**Nguyên nhân cốt lõi:**
- Hệ thống xây dựng bị xâm phạm
- Đã ký các bản cập nhật độc hại với chứng chỉ hợp lệ
- Chuyển động bên một lần trong mạng
**Tác động:**
- Cơ quan nhà nước bị xâm phạm
- Các công ty Fortune 500 bị ảnh hưởng
- Đang tiếp tục điều tra và khắc phục
**Bài học:** Bảo mật quy trình xây dựng; xác minh tính toàn vẹn của phần mềm; kiến trúc không tin cậy.
---

## Chiến lược kiểm tra bảo mật
### Kiểm tra bảo mật ứng dụng tĩnh (SAST)
```yaml
# GitHub Actions example
- name: Run SAST
  uses: github/super-linter/slim@v5
  env:
    VALIDATE_PYTHON_BLACK: true
    VALIDATE_PYTHON_FLAKE8: true
    PYTHON_BLACK_CONFIG_FILE: pyproject.toml
```

### Kiểm tra bảo mật ứng dụng động (DAST)
```bash
# OWASP ZAP scan
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://your-app.com
```

### Quét phụ thuộc
```bash
# Python
pip-audit

# Node.js
npm audit

# General
snyk test
```

### Danh sách kiểm tra thâm nhập
- [] Kiểm tra tiêm SQL
- [ ] Kiểm tra XSS (được phản ánh, được lưu trữ, dựa trên DOM)
- [] Xác thực mã thông báo CSRF
- [ ] Các nỗ lực bỏ qua xác thực
- [ ] Kiểm tra ủy quyền (leo thang đặc quyền dọc/ngang)
- [ ] Xác minh giới hạn tỷ lệ
- [] Sự hiện diện của tiêu đề bảo mật
- [ ] Cấu hình SSL/TLS
- [ ] Đánh giá quản lý phiên
- [ ] Xử lý lỗi (không rò rỉ thông tin)
---

## Tài nguyên bảo mật
### Top 10 OWASP (2021)
1. Kiểm soát truy cập bị hỏng
2. Lỗi mật mã
3. Tiêm
4. Thiết kế không an toàn
5. Cấu hình bảo mật sai
6. Các thành phần dễ bị tổn thương và lỗi thời
7. Lỗi nhận dạng và xác thực
8. Lỗi về tính toàn vẹn của phần mềm và dữ liệu
9. Lỗi ghi nhật ký và giám sát bảo mật
10. Giả mạo yêu cầu phía máy chủ
### Công cụ được đề xuất
- **Phân tích tĩnh**: SonarQube, Semgrep, CodeQL
- **Quét phụ thuộc**: Dependabot, Renovate, Snyk
- **Kiểm tra động**: OWASP ZAP, Burp Suite
- **Phát hiện bí mật**: GitLeaks, TruffleHog
- **Bảo mật vùng chứa**: Trivy, Clair, Anchore