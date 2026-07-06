# Security Mistakes

Security mistakes are errors in software design, implementation, or operation that create vulnerabilities. These mistakes can lead to data breaches, unauthorized access, and system compromise.

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

**Better:**
```python
import re

def is_strong_password(password):
    """Enforce strong password requirements."""
    if len(password) < 12:
        return False, "Password must be at least 12 characters"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain lowercase letter"
    
    if not re.search(r'\d', password):
        return False, "Password must contain a number"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain special character"
    
    # Check against common password list
    if password.lower() in COMMON_PASSWORDS:
        return False, "Password is too common"
    
    return True, "Password meets requirements"
```

---

### Storing Passwords Insecurely

**Bad Example:**
```python
# Plaintext storage
users = {
    "alice": "password123",
    "bob": "qwerty456"
}

# Or reversible encryption
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
encrypted_password = cipher.encrypt(password.encode())
# Can be decrypted with the key!
```

**Problems:**
- Database breach exposes all passwords
- Insider threat can read passwords
- Users reuse passwords across sites

**Better:**
```python
import bcrypt
import argon2

def hash_password(password):
    """Hash password with Argon2 (recommended)."""
    ph = argon2.PasswordHasher(
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32
    )
    return ph.hash(password)

def verify_password(password, hashed):
    """Verify password against hash."""
    ph = argon2.PasswordHasher()
    try:
        ph.verify(hashed, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
```

---

### Session Management Failures

**Bad Example:**
```python
# Predictable session IDs
def create_session(user_id):
    session_id = f"session_{user_id}_{timestamp}"
    return session_id

# No expiration
sessions[session_id] = user_data  # Lives forever

# Session fixation vulnerability
def login(username, password):
    session_id = request.cookies.get('session_id')  # Use provided ID
    if authenticate(username, password):
        sessions[session_id] = username  # Attack controls session_id!
```

**Problems:**
- Session hijacking possible
- Sessions never expire
- Session fixation attacks

**Better:**
```python
import secrets
from datetime import datetime, timedelta

def create_session(user_id):
    """Create secure session with proper expiration."""
    session_id = secrets.token_urlsafe(32)
    
    sessions[session_id] = {
        'user_id': user_id,
        'created_at': datetime.now(),
        'expires_at': datetime.now() + timedelta(hours=24),
        'ip_address': request.remote_addr,
        'user_agent': request.user_agent.string
    }
    
    return session_id

def validate_session(session_id):
    """Validate session with security checks."""
    session = sessions.get(session_id)
    
    if not session:
        return None
    
    if datetime.now() > session['expires_at']:
        del sessions[session_id]  # Expired
        return None
    
    # Regenerate session ID periodically
    if datetime.now() - session['created_at'] > timedelta(hours=1):
        new_session_id = create_session(session['user_id'])
        del sessions[session_id]
        return new_session_id
    
    return session['user_id']
```

---

## Authorization Mistakes

### Broken Access Control

**Bad Example:**
```python
# Trusting client-provided IDs
def get_order(order_id):
    order = db.query("SELECT * FROM orders WHERE id = ?", order_id)
    return order
# Any user can access any order by changing order_id

# Or worse
def delete_user(user_id):
    if user_id != 1:  # "Protect" admin
        db.delete("users", user_id)
# Attacker can delete any user except admin
```

**Problems:**
- Horizontal privilege escalation
- Vertical privilege escalation
- Data breach

**Better:**
```python
def get_order(order_id, current_user):
    """Ensure user owns the order."""
    order = db.query(
        "SELECT * FROM orders WHERE id = ? AND user_id = ?",
        order_id,
        current_user.id
    )
    
    if not order:
        raise PermissionError("Order not found")
    
    return order

def delete_user(target_user_id, current_user):
    """Check admin privileges."""
    if not current_user.is_admin:
        raise PermissionError("Admin access required")
    
    if target_user_id == current_user.id:
        raise ValueError("Cannot delete yourself")
    
    db.delete("users", target_user_id)
```

---

### Insecure Direct Object References (IDOR)

**Bad Example:**
```python
# API endpoint
GET /api/users/{{user_id}}/documents

# Implementation
def get_user_documents(user_id):
    return db.documents.find({"owner_id": user_id})
# User changes user_id parameter to access others' documents
```

**Better:**
```python
def get_user_documents(requested_user_id, current_user):
    """Only allow access to own documents."""
    if requested_user_id != current_user.id and not current_user.is_admin:
        raise PermissionError("Access denied")
    
    return db.documents.find({"owner_id": requested_user_id})
```

---

## Input Validation Mistakes

### Trusting Client-Side Validation

**Bad Example:**
```javascript
// Frontend validation only
<input type="number" min="0" max="10000" />
<button onclick="transfer()">Transfer</button>

<script>
function transfer() {
    if (amount <= 10000) {  // Easily bypassed
        submit_transfer(amount);
    }
}
</script>
```

**Problems:**
- Client validation easily bypassed
- No server-side protection
- Allows arbitrary values

**Better:**
```python
def transfer_funds(from_account, to_account, amount, current_user):
    """Server-side validation."""
    # Verify ownership
    if from_account.owner_id != current_user.id:
        raise PermissionError("Account access denied")
    
    # Validate amount
    if not isinstance(amount, (int, float)):
        raise ValidationError("Amount must be numeric")
    
    if amount <= 0:
        raise ValidationError("Amount must be positive")
    
    if amount > MAX_TRANSFER_LIMIT:
        raise ValidationError(f"Exceeds transfer limit of {MAX_TRANSFER_LIMIT}")
    
    # Check balance
    if from_account.balance < amount:
        raise ValidationError("Insufficient funds")
    
    # Perform transfer atomically
    with db.transaction():
        from_account.balance -= amount
        to_account.balance += amount
        db.save(from_account)
        db.save(to_account)
```

---

### XSS (Cross-Site Scripting) Vulnerabilities

**Bad Example:**
```python
# Rendering user input without escaping
def display_comment(comment):
    return f"<div class='comment'>{comment}</div>"

# User submits: <script>steal_cookies()</script>
# Script executes in other users' browsers
```

**Problems:**
- Session hijacking
- Malware distribution
- Defacement

**Better:**
```python
import html

def display_comment(comment):
    """Escape HTML entities."""
    safe_comment = html.escape(comment)
    return f"<div class='comment'>{safe_comment}</div>"

# Or use template engine with auto-escaping
# Jinja2, React, etc. auto-escape by default
```

---

## Data Protection Mistakes

### Exposing Sensitive Data

**Bad Example:**
```python
# API returns everything
def get_user_profile(user_id):
    user = db.users.find_one({"id": user_id})
    return jsonify(user)
# Returns: password_hash, ssn, credit_card, internal_notes...

# Error messages leak information
except DatabaseError as e:
    return {"error": str(e)}
# Returns: "Connection failed: password authentication failed for user 'admin'"
```

**Better:**
```python
def get_user_profile(user_id, current_user):
    """Return only necessary fields."""
    if user_id != current_user.id and not current_user.is_admin:
        raise PermissionError("Access denied")
    
    user = db.users.find_one({"id": user_id})
    
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at.isoformat()
        # Explicitly exclude sensitive fields
    })

# Generic error messages
except DatabaseError:
    logger.error("Database error occurred")
    return {"error": "An error occurred processing your request"}
```

---

### Missing Encryption

**Bad Example:**
```python
# HTTP instead of HTTPS
server = HTTPServer(('0.0.0.0', 80), handler)

# Unencrypted database connection
conn = psycopg2.connect(
    host="db.example.com",
    user="app",
    password="secret",
    database="production"
    # No SSL!
)

# Sensitive data stored unencrypted
user.ssn = "123-45-6789"  # Stored as-is in database
```

**Better:**
```python
# Force HTTPS
@app.before_request
def enforce_https():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"), 301)

# Encrypted database connection
conn = psycopg2.connect(
    host="db.example.com",
    user="app",
    password="secret",
    database="production",
    sslmode="require"
)

# Encrypt sensitive fields at rest
from cryptography.fernet import Fernet

cipher = Fernet(encryption_key)
user.ssn_encrypted = cipher.encrypt(ssn.encode())
```

---

## Configuration Mistakes

### Default Credentials

**Bad Example:**
```python
# Shipping with default credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Or documented defaults
DATABASE_URL = "postgres://postgres:postgres@localhost/db"
```

**Problems:**
- Well-known defaults easily exploited
- Automated attacks target defaults
- Often unchanged in production

**Better:**
```python
import os
import secrets

def initialize_system():
    """Force credential setup on first run."""
    if not os.path.exists('.initialized'):
        admin_password = secrets.token_urlsafe(32)
        print(f"Initial admin password: {admin_password}")
        print("CHANGE THIS IMMEDIATELY!")
        os.environ['ADMIN_PASSWORD'] = admin_password
        
        with open('.initialized', 'w') as f:
            f.write('true')

# Always require environment variables
def get_admin_password():
    password = os.getenv('ADMIN_PASSWORD')
    if not password:
        raise ConfigurationError("ADMIN_PASSWORD must be set")
    if password == 'admin123':
        raise ConfigurationError("Default password not allowed")
    return password
```

---

### Verbose Error Messages in Production

**Bad Example:**
```python
# Debug mode in production
app.config['DEBUG'] = True

# Full stack traces to users
@app.errorhandler(Exception)
def handle_error(e):
    return f"<pre>{traceback.format_exc()}</pre>", 500
# Exposes: file paths, code logic, library versions
```

**Better:**
```python
# Debug disabled in production
app.config['DEBUG'] = os.getenv('ENV') != 'production'

@app.errorhandler(Exception)
def handle_error(e):
    logger.exception("Unhandled exception")
    
    if app.config['DEBUG']:
        return f"<pre>{traceback.format_exc()}</pre>", 500
    
    return render_template('error.html'), 500
```

---

## Security Checklist

```markdown
## Application Security Checklist

### Authentication
- [ ] Strong password requirements enforced
- [ ] Passwords hashed with Argon2/bcrypt
- [ ] Multi-factor authentication available
- [ ] Account lockout after failed attempts
- [ ] Secure session management

### Authorization
- [ ] Server-side access control on all endpoints
- [ ] Principle of least privilege applied
- [ ] IDOR vulnerabilities prevented
- [ ] Admin functions properly protected

### Input Validation
- [ ] All input validated server-side
- [ ] Output properly escaped
- [ ] SQL injection prevented (parameterized queries)
- [ ] File uploads validated and sanitized

### Data Protection
- [ ] HTTPS enforced everywhere
- [ ] Sensitive data encrypted at rest
- [ ] Minimal data exposure in APIs
- [ ] Secure deletion of sensitive data

### Configuration
- [ ] No default credentials
- [ ] Debug mode disabled in production
- [ ] Security headers configured
- [ ] Dependencies up to date

### Monitoring
- [ ] Security events logged
- [ ] Anomaly detection implemented
- [ ] Incident response plan documented
- [ ] Regular security audits scheduled
```

---

## Related Documents

- [[unsafe_code]] - Writing insecure code
- [[prompt_injection]] - AI-specific security issues
- [[bad_api_design]] - API security considerations
- [[09_bad_examples_and_failures]] - General anti-patterns
