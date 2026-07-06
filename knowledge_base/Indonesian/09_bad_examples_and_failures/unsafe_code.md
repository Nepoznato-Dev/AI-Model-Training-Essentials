# Unsafe Code

Unsafe code refers to programming practices that can lead to security vulnerabilities, crashes, data corruption, or undefined behavior. Writing safe code is essential for building reliable and secure software.

---

## Categories of Unsafe Code

### Memory Safety Issues

#### Buffer Overflows

**Bad Example (C):**
```c
char buffer[10];
strcpy(buffer, user_input);  // No bounds checking!
// If user_input > 9 chars, overflow occurs
```

**Problems:**
- Can overwrite adjacent memory
- May allow code execution attacks
- Causes undefined behavior

**Better:**
```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

---

#### Use After Free

**Bad Example (C):**
```c
char *data = malloc(100);
free(data);
// ... later ...
strcpy(data, "new value");  // Writing to freed memory!
```

**Problems:**
- Memory may be reallocated for other purposes
- Causes heap corruption
- Security vulnerability (use-after-free exploits)

**Better:**
```c
char *data = malloc(100);
// ... use data ...
free(data);
data = NULL;  // Prevent accidental reuse
```

---

#### Race Conditions

**Bad Example:**
```python
# Global counter accessed by multiple threads
counter = 0

def increment():
    global counter
    temp = counter
    time.sleep(0.001)  # Simulate work
    counter = temp + 1
# Multiple threads calling increment() lose updates
```

**Problems:**
- Non-deterministic behavior
- Data corruption
- Lost updates

**Better:**
```python
import threading

class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    @property
    def value(self):
        with self._lock:
            return self._value
```

---

### Input Validation Failures

#### SQL Injection

**Bad Example:**
```python
def get_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return db.execute(query)
# Vulnerable to: username = "' OR '1'='1"
```

**Problems:**
- Allows arbitrary SQL execution
- Data breach risk
- Potential data destruction

**Better:**
```python
def get_user(username):
    query = "SELECT * FROM users WHERE username = ?"
    return db.execute(query, (username,))  # Parameterized query
```

---

#### Command Injection

**Bad Example:**
```python
def backup_file(filename):
    os.system(f"cp {filename} /backup/")
# Vulnerable to: filename = "data.txt; rm -rf /"
```

**Problems:**
- Arbitrary command execution
- Complete system compromise

**Better:**
```python
import subprocess

def backup_file(filename):
    subprocess.run(["cp", filename, "/backup/"], check=True)
```

---

#### Path Traversal

**Bad Example:**
```python
def read_user_file(filename):
    with open(f"/data/users/{filename}", "r") as f:
        return f.read()
# Vulnerable to: filename = "../../../etc/passwd"
```

**Problems:**
- Access files outside intended directory
- Information disclosure

**Better:**
```python
from pathlib import Path

def read_user_file(filename):
    base_dir = Path("/data/users").resolve()
    requested_path = (base_dir / filename).resolve()
    
    # Verify path is within base directory
    if not str(requested_path).startswith(str(base_dir)):
        raise ValueError("Invalid file path")
    
    with open(requested_path, "r") as f:
        return f.read()
```

---

### Resource Management Issues

#### Resource Leaks

**Bad Example:**
```python
def process_file(path):
    f = open(path, 'r')
    data = f.read()
    # Forgot to close file
    return process(data)
# File handle leaked on exception
```

**Problems:**
- Exhausts file descriptors
- Memory leaks
- Database connection pool depletion

**Better:**
```python
def process_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return process(data)
# File automatically closed
```

---

#### Unbounded Resource Consumption

**Bad Example:**
```python
cache = {}

def cache_result(key, value):
    cache[key] = value  # Grows forever!
# Memory exhaustion over time
```

**Better:**
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_operation(key):
    return expensive_computation(key)
```

Or implement explicit limits:
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.cache = OrderedDict()
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
```

---

### Error Handling Issues

#### Silent Failures

**Bad Example:**
```python
def save_data(data):
    try:
        db.save(data)
    except Exception:
        pass  # Silently ignore errors
# Data loss goes unnoticed
```

**Problems:**
- Errors go undetected
- Data corruption
- Debugging nightmare

**Better:**
```python
def save_data(data):
    try:
        db.save(data)
        logger.info("Data saved successfully")
    except DatabaseError as e:
        logger.error(f"Database error: {e}")
        alert_team("CRITICAL", "Data save failed")
        raise
```

---

#### Catching Too Broad Exceptions

**Bad Example:**
```python
def process_request(request):
    try:
        validate(request)
        process(request.data)
        send_response()
    except Exception:
        return {"error": "Something went wrong"}
# Catches KeyboardInterrupt, SystemExit, etc.
```

**Problems:**
- Hides programming errors
- Prevents graceful shutdown
- Makes debugging difficult

**Better:**
```python
def process_request(request):
    try:
        validate(request)
        process(request.data)
        send_response()
    except ValidationError as e:
        return {"error": f"Invalid request: {e}"}, 400
    except ProcessingError as e:
        logger.error(f"Processing failed: {e}")
        return {"error": "Processing failed"}, 500
```

---

### Cryptographic Weaknesses

#### Weak Random Number Generation

**Bad Example:**
```python
import random

def generate_token():
    return random.randint(100000, 999999)
# Uses predictable PRNG, not cryptographically secure
```

**Problems:**
- Predictable output
- Session hijacking possible
- Token forgery

**Better:**
```python
import secrets

def generate_token():
    return secrets.token_urlsafe(32)
# Cryptographically secure random bytes
```

---

#### Hardcoded Secrets

**Bad Example:**
```python
DATABASE_PASSWORD = "super_secret_123"
API_KEY = "sk-1234567890abcdef"

def connect():
    return db.connect(password=DATABASE_PASSWORD)
```

**Problems:**
- Secrets in version control
- No rotation mechanism
- Exposed in binaries

**Better:**
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file (not committed)

def get_database_password():
    password = os.getenv("DATABASE_PASSWORD")
    if not password:
        raise ConfigurationError("DATABASE_PASSWORD not set")
    return password
```

---

#### Insecure Hashing

**Bad Example:**
```python
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
# MD5 is cryptographically broken
```

**Problems:**
- Fast to brute force
- Rainbow table attacks
- Collision vulnerabilities

**Better:**
```python
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
```

---

## Safe Coding Practices

### Defense in Depth

```python
def process_user_upload(file, user):
    # Layer 1: Authentication
    if not user.is_authenticated:
        raise UnauthorizedError()
    
    # Layer 2: Authorization
    if not user.has_permission('upload'):
        raise PermissionError()
    
    # Layer 3: Input validation
    if not is_safe_filename(file.name):
        raise ValidationError("Invalid filename")
    
    # Layer 4: Size limit
    if file.size > MAX_UPLOAD_SIZE:
        raise ValidationError("File too large")
    
    # Layer 5: Content validation
    if not validate_file_content(file.content):
        raise ValidationError("Invalid file content")
    
    # Layer 6: Secure storage
    safe_path = generate_safe_storage_path()
    store_securely(file.content, safe_path)
    
    # Layer 7: Logging
    logger.info(f"User {user.id} uploaded file {file.name}")
    
    return {"success": True, "path": safe_path}
```

### Principle of Least Privilege

```python
# Bad: Running with excessive permissions
def read_config():
    return open("/etc/app/config.yaml").read()

# Good: Minimal required permissions
def read_config():
    config_path = Path.home() / ".myapp" / "config.yaml"
    return config_path.read_text()
```

### Fail Secure

```python
# Bad: Fails open
def check_access(user, resource):
    try:
        return database.has_permission(user, resource)
    except Exception:
        return True  # Grant access on error!

# Good: Fails closed
def check_access(user, resource):
    try:
        return database.has_permission(user, resource)
    except Exception as e:
        logger.error(f"Access check failed: {e}")
        return False  # Deny access on error
```

---

## Security Checklist

```markdown
## Code Security Checklist

### Input Handling
- [ ] All input validated and sanitized
- [ ] Parameterized queries for database access
- [ ] No command injection vulnerabilities
- [ ] Path traversal prevented

### Memory Safety
- [ ] Bounds checking on arrays/buffers
- [ ] No use-after-free possibilities
- [ ] Proper initialization of variables
- [ ] Null pointer checks where needed

### Resource Management
- [ ] Resources properly released (files, connections)
- [ ] Limits on resource consumption
- [ ] Timeout handling implemented
- [ ] Connection pooling used appropriately

### Cryptography
- [ ] Secure random number generation
- [ ] Strong hashing algorithms (bcrypt, argon2)
- [ ] No hardcoded secrets
- [ ] Keys stored securely

### Error Handling
- [ ] No silent failures
- [ ] Appropriate exception types caught
- [ ] Errors logged without sensitive data
- [ ] Fail-secure defaults

### Concurrency
- [ ] Race conditions prevented
- [ ] Proper locking mechanisms
- [ ] Deadlock avoidance
- [ ] Thread-safe data structures
```

---

## Related Documents

- [[security_mistakes]] - Common security errors
- [[prompt_injection]] - AI-specific security issues
- [[bad_api_design]] - API security considerations
- [[09_bad_examples_and_failures]] - General anti-patterns
