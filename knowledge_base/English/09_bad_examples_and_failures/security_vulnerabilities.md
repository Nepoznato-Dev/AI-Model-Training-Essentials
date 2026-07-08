# Security Vulnerabilities

This document consolidates common security vulnerabilities in software development, including injection attacks, unsafe code practices, and security mistakes.

---

## SQL Injection

SQL injection attacks occur when untrusted user input is improperly handled in database queries, allowing attackers to manipulate query logic, access unauthorized data, or modify database contents.

### Classic UNION-Based Injection

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: String concatenation with user input
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = " + user_id
    return db.execute(query)
```

**Attack:**
```
Input: 1 UNION SELECT username, password, email FROM users--
Resulting Query:
SELECT * FROM products WHERE user_id = 1 UNION SELECT username, password, email FROM users--
```

**Why It's Bad:**
- Exposes data from other tables
- Bypasses intended query logic
- Can extract sensitive information

**Better Approach:**
```python
# SAFE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = ?"
    return db.execute(query, (user_id,))
```

### Prevention Strategies

1. **Use Parameterized Queries**: Never concatenate user input into SQL
2. **Input Validation**: Validate and sanitize all user input
3. **Least Privilege**: Database accounts should have minimal permissions
4. **ORM Usage**: Use Object-Relational Mappers that handle escaping
5. **Web Application Firewalls**: Deploy WAFs to detect injection attempts

---

## Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) attacks occur when attackers inject malicious scripts into web pages viewed by other users.

### Reflected XSS

**Bad Example (Vulnerable Code):**
```php
// VULNERABLE: Unsanitized user input in output
<?php
$searchTerm = $_GET['q'];
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

**Attack:**
```
URL: https://example.com/search?q=<script>alert('XSS')</script>
Result: Script executes in victim's browser
```

**Why It's Bad:**
- User input directly rendered without encoding
- Attacker can craft malicious URLs
- Session hijacking, credential theft possible

**Better Approach:**
```php
// SAFE: Proper output encoding
<?php
$searchTerm = htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8');
echo "<div>Search results for: " . $searchTerm . "</div>";
?>
```

### Stored XSS

**Bad Example:**
```javascript
// VULNERABLE: User comment stored and displayed without sanitization
app.post('/comment', (req, res) => {
    db.saveComment(req.body.comment);  // Malicious script stored
});

app.get('/comments', (req, res) => {
    const comments = db.getComments();
    res.send(`<div>${comments}</div>`);  // Script executes for all viewers
});
```

### Prevention Strategies

1. **Output Encoding**: Encode data based on context (HTML, JS, URL, CSS)
2. **Input Validation**: Reject or sanitize malicious input
3. **Content Security Policy**: Use CSP headers to restrict script sources
4. **HTTPOnly Cookies**: Prevent JavaScript access to session cookies
5. **Modern Frameworks**: Use React, Vue, Angular which auto-escape by default

---

## Memory Safety Issues

### Buffer Overflows

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

**Better Approach:**
```c
char buffer[10];
strncpy(buffer, user_input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
```

### Use-After-Free

**Bad Example (C++):**
```cpp
int* ptr = new int(42);
delete ptr;
*ptr = 10;  // Undefined behavior - accessing freed memory
```

**Better Approach:**
```cpp
std::unique_ptr<int> ptr = std::make_unique<int>(42);
// Memory automatically managed, no manual delete needed
```

### Prevention Strategies

1. **Use Safe Languages**: Prefer Rust, Go, Java, Python over C/C++
2. **Smart Pointers**: Use RAII patterns in C++
3. **Bounds Checking**: Always validate array indices
4. **Static Analysis**: Use tools like Valgrind, AddressSanitizer
5. **Memory-Safe APIs**: Use safer standard library functions

---

## Authentication Mistakes

### Weak Password Policies

**Bad Example:**
```python
# Allows trivial passwords
def register_user(username, password):
    if len(password) >= 4:  # Minimum 4 characters!
        create_user(username, password)
```

**Problems:**
- Susceptible to brute force attacks
- Common passwords easily guessed
- Violates security best practices

**Better Approach:**
```python
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

### Storing Plaintext Passwords

**Bad Example:**
```python
# NEVER store passwords in plaintext
def login(username, password):
    user = db.query("SELECT * FROM users WHERE username = ?", username)
    if user and user.password == password:  # Plaintext comparison!
        return create_session(user)
```

**Better Approach:**
```python
import bcrypt

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.insert_user(username, hashed)

def login(username, password):
    user = db.get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.hashed_password):
        return create_session(user)
```

### Prevention Strategies

1. **Strong Hashing**: Use bcrypt, Argon2, or scrypt for passwords
2. **Multi-Factor Authentication**: Require additional verification
3. **Rate Limiting**: Prevent brute force attacks
4. **Account Lockout**: Temporarily lock after failed attempts
5. **Secure Session Management**: Use secure, HTTP-only cookies

---

## Other Security Mistakes

### Hardcoded Secrets

**Bad Example:**
```python
# NEVER hardcode secrets in source code
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
```

**Better Approach:**
```python
import os

# Load from environment variables
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
```

### Insecure Direct Object References

**Bad Example:**
```python
# VULNERABLE: No authorization check
def get_document(doc_id):
    return db.query("SELECT * FROM documents WHERE id = ?", doc_id)
# Any user can access any document by guessing IDs
```

**Better Approach:**
```python
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

### Missing Rate Limiting

**Bad Example:**
```python
# No rate limiting - vulnerable to abuse
@app.route('/api/login', methods=['POST'])
def login():
    # Can be called unlimited times
    return attempt_login(request.json)
```

**Better Approach:**
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return attempt_login(request.json)
```

---

## Related Topics

- **AI/LLM Failures**: See `01_ai_llm_failures.md` for prompt injection and AI-specific security issues
- **Unsafe Code Patterns**: See code examples for memory safety and undefined behavior
- **Authentication Best Practices**: Implement proper auth flows and session management
