# SQL Injection Examples

## Overview

SQL injection attacks occur when untrusted user input is improperly handled in database queries, allowing attackers to manipulate query logic, access unauthorized data, or modify database contents. This document provides concrete examples and prevention strategies.

## Types of SQL Injection

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

**Secure Approach:**
```python
# SECURE: Parameterized query
def get_user_products(user_id):
    query = "SELECT * FROM products WHERE user_id = %s"
    return db.execute(query, (user_id,))
```

### Boolean-Based Blind Injection

**Bad Example (Vulnerable Code):**
```php
// VULNERABLE: Unvalidated input in query
$productId = $_GET['id'];
$query = "SELECT name FROM products WHERE id = $productId";
$result = mysqli_query($conn, $query);
```

**Attack:**
```
Input: 1' AND '1'='1
Resulting Query: SELECT name FROM products WHERE id = 1' AND '1'='1

Input: 1' AND '1'='2
Resulting Query: SELECT name FROM products WHERE id = 1' AND '1'='2
```

**Why It's Bad:**
- Different responses reveal information
- Attacker can extract data bit by bit
- No input validation

**Secure Approach:**
```php
// SECURE: Prepared statement
$productId = $_GET['id'];
$stmt = $conn->prepare("SELECT name FROM products WHERE id = ?");
$stmt->bind_param("i", $productId);
$stmt->execute();
```

### Time-Based Blind Injection

**Bad Example (Vulnerable Code):**
```java
// VULNERABLE: Dynamic query building
public User getUser(String username) {
    String query = "SELECT * FROM users WHERE username = '" + username + "'";
    return executeQuery(query);
}
```

**Attack:**
```
Input: admin' OR IF(1=1, SLEEP(5), 0)--
Result: Query delays 5 seconds if condition true

Input: admin' OR IF((SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a', SLEEP(5), 0)--
Result: Extracts password character by character via timing
```

**Why It's Bad:**
- Allows data extraction without visible output
- Difficult to detect
- Can bypass security controls

**Secure Approach:**
```java
// SECURE: PreparedStatement
public User getUser(String username) {
    String query = "SELECT * FROM users WHERE username = ?";
    PreparedStatement stmt = conn.prepareStatement(query);
    stmt.setString(1, username);
    return executeQuery(stmt);
}
```

### Stacked Queries Injection

**Bad Example (Vulnerable Code):**
```csharp
// VULNERABLE: Multiple statements allowed
public void UpdateUser(string userId, string newName) {
    string query = $"UPDATE users SET name = '{newName}' WHERE id = {userId}";
    ExecuteQuery(query); // Allows multiple statements
}
```

**Attack:**
```
Input: test'; DROP TABLE users;--
Resulting Query: 
UPDATE users SET name = 'test'; DROP TABLE users;--' WHERE id = ...
```

**Why It's Bad:**
- Executes additional malicious statements
- Can destroy entire tables
- Permanent data loss

**Secure Approach:**
```csharp
// SECURE: Parameterized + disable multiple statements
public void UpdateUser(string userId, string newName) {
    string query = "UPDATE users SET name = @name WHERE id = @id";
    SqlCommand cmd = new SqlCommand(query, conn);
    cmd.Parameters.AddWithValue("@name", newName);
    cmd.Parameters.AddWithValue("@id", userId);
    cmd.ExecuteNonQuery();
}
```

## Real-World Attack Scenarios

### Scenario 1: Authentication Bypass

**Vulnerable Code:**
```python
def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = db.execute(query).fetchone()
    return user is not None
```

**Attack:**
```
Username: admin' --
Password: anything
Resulting Query: SELECT * FROM users WHERE username='admin' --' AND password='anything'
Result: Logs in as admin without password
```

**Alternative Attack:**
```
Username: admin' OR '1'='1' --
Password: ignored
Resulting Query: SELECT * FROM users WHERE username='admin' OR '1'='1' --' AND password='...'
Result: Returns all users, logs in as first user (often admin)
```

**Secure Implementation:**
```python
def login(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    # Hash password before comparison
    hashed_pw = hash_password(password)
    user = db.execute(query, (username, hashed_pw)).fetchone()
    return user is not None
```

### Scenario 2: Data Exfiltration

**Vulnerable Code:**
```javascript
// Node.js vulnerable code
app.get('/product', (req, res) => {
    const id = req.query.id;
    const query = `SELECT * FROM products WHERE id = ${id}`;
    db.query(query, (err, results) => {
        res.json(results);
    });
});
```

**Attack Sequence:**
```
1. Discover table names:
   Input: 1 UNION SELECT table_name, null FROM information_schema.tables--

2. Discover columns:
   Input: 1 UNION SELECT column_name, null FROM information_schema.columns 
          WHERE table_name='users'--

3. Extract data:
   Input: 1 UNION SELECT username, password FROM users--
```

**Secure Implementation:**
```javascript
// Node.js secure code with parameterized query
app.get('/product', (req, res) => {
    const id = req.query.id;
    const query = 'SELECT * FROM products WHERE id = ?';
    db.query(query, [id], (err, results) => {
        res.json(results);
    });
});
```

### Scenario 3: Privilege Escalation

**Vulnerable Code:**
```ruby
# Ruby on Rails vulnerable (raw SQL)
def update_role
  @user = User.find(params[:id])
  ActiveRecord::Base.connection.execute(
    "UPDATE users SET role = '#{params[:role]}' WHERE id = #{@user.id}"
  )
end
```

**Attack:**
```
Input role: admin' WHERE id=1; UPDATE users SET role='admin' WHERE id=2;--
Result: Changes role for user 2 to admin
```

**Secure Implementation:**
```ruby
# Ruby on Rails secure (ActiveRecord)
def update_role
  @user = User.find(params[:id])
  @user.update(role: params[:role])  # Uses parameterized queries
end
```

## Prevention Strategies

### Input Validation

```python
def validate_user_id(user_input):
    # Whitelist approach: only allow integers
    try:
        user_id = int(user_input)
        if user_id < 0:
            raise ValueError("ID must be positive")
        return user_id
    except ValueError:
        raise InvalidInputError("Invalid user ID format")
```

### Parameterized Queries (All Languages)

```python
# Python (psycopg2)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Java (JDBC)
PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
stmt.setInt(1, userId);

# PHP (PDO)
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $userId]);

# Node.js (mysql2)
connection.execute('SELECT * FROM users WHERE id = ?', [userId]);

# C# (ADO.NET)
cmd.CommandText = "SELECT * FROM users WHERE id = @id";
cmd.Parameters.AddWithValue("@id", userId);
```

### Stored Procedures

```sql
-- Create stored procedure
CREATE PROCEDURE GetUserProducts(IN user_id INT)
BEGIN
    SELECT * FROM products WHERE user_id = user_id;
END;

-- Call from application (still use parameters!)
CALL GetUserProducts(?);
```

### ORM Usage

```python
# Django ORM - automatically parameterized
products = Product.objects.filter(user_id=user_id)

# SQLAlchemy - uses bind parameters
products = session.query(Product).filter(Product.user_id == user_id).all()

# Hibernate (Java) - HQL with parameters
Query query = session.createQuery("FROM Product WHERE userId = :userId");
query.setParameter("userId", userId);
```

## Detection Patterns

### Code Review Red Flags

1. **String Concatenation in Queries:**
   ```python
   # BAD
   query = "SELECT * FROM users WHERE id = " + user_id
   query = f"SELECT * FROM users WHERE id = {user_id}"
   query = "SELECT * FROM users WHERE id = %s" % user_id
   ```

2. **Unvalidated Input:**
   ```python
   # BAD
   user_input = request.GET['id']
   query = f"SELECT * FROM table WHERE id = {user_input}"
   ```

3. **Dynamic Table/Column Names:**
   ```python
   # BAD (even with parameters elsewhere)
   query = f"SELECT * FROM {table_name} WHERE id = %s"
   ```

### Runtime Detection

```python
def detect_sql_injection_attempt(input_string):
    suspicious_patterns = [
        r"(\bOR\b|\bAND\b)\s+['\"]?\d+['\"]?\s*=\s*['\"]?\d+",
        r"UNION\s+(ALL\s+)?SELECT",
        r"--\s*$",
        r";\s*(DROP|DELETE|UPDATE|INSERT)",
        r"EXEC(\UTE)?\s*\(",
        r"SLEEP\s*\(",
        r"BENCHMARK\s*\(",
        r"information_schema",
        r"/\*.*\*/",  # Comments
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            log_security_event(f"Potential SQL injection: {input_string}")
            return True
    
    return False
```

## Testing Checklist

- [ ] Test all input fields with `'` character
- [ ] Test with `1 OR 1=1` patterns
- [ ] Test UNION-based attacks
- [ ] Test comment sequences (`--`, `/* */`)
- [ ] Test stacked queries with `;`
- [ ] Test time-based attacks with `SLEEP()`
- [ ] Verify error messages don't leak schema info
- [ ] Test authentication bypass attempts
- [ ] Verify all queries use parameterization
- [ ] Test with URL-encoded injection payloads
- [ ] Test second-order injection scenarios
- [ ] Verify stored procedures use parameters
- [ ] Check ORM queries for raw SQL escapes

## Related Documents

- [[security_mistakes]] - General security vulnerabilities
- [[unsafe_code]] - Unsafe coding patterns
- [[xss_examples]] - Cross-site scripting examples
- [[prompt_injection_examples]] - AI-specific injection attacks
