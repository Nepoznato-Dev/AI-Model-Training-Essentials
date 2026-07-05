# Bad Examples and Failures

## Overview

This document provides concrete examples of bad code practices, common failures, and anti-patterns in programming. By studying these negative examples, developers can learn what to avoid and understand the consequences of poor coding decisions.

## When to Reference This Document

- Conducting code reviews to identify problematic patterns
- Training junior developers on what not to do
- Debugging issues caused by common mistakes
- Refactoring legacy code with known anti-patterns
- Creating test cases for edge cases and error conditions
- Building awareness of technical debt indicators

## Anti-Patterns

### God Object / God Class

**Problem**: A single class that knows too much or does too much, violating the Single Responsibility Principle.

**Bad Example**:
```python
class UserManager:
    def __init__(self):
        self.db_connection = Database()
        self.email_service = EmailService()
        self.cache = RedisCache()
        self.logger = Logger()
        self.auth = AuthenticationService()
    
    def register_user(self, username, email, password):
        # Validate input
        if not username or not email or not password:
            raise ValueError("All fields required")
        
        # Hash password
        hashed = hashlib.sha256(password.encode()).hexdigest()
        
        # Check if user exists
        existing = self.db_connection.query("SELECT * FROM users WHERE email=?", email)
        if existing:
            raise Exception("User already exists")
        
        # Insert into database
        self.db_connection.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            username, email, hashed
        )
        
        # Send welcome email
        self.email_service.send(
            to=email,
            subject="Welcome!",
            body=f"Hello {username}, welcome to our platform!"
        )
        
        # Cache user data
        self.cache.set(f"user:{email}", {"username": username})
        
        # Log the action
        self.logger.info(f"User registered: {email}")
        
        # Generate auth token
        token = self.auth.generate_token(email)
        
        return {"user_id": 123, "token": token}
    
    def get_user_reports(self, user_id):
        # Generate complex reports
        # ... 200 more lines of reporting logic
        pass
    
    def send_newsletter(self, content):
        # Email marketing logic
        # ... 150 more lines of newsletter logic
        pass
    
    def cleanup_old_users(self):
        # Maintenance tasks
        # ... 100 more lines of cleanup logic
        pass
```

**Why It's Bad**:
- Violates Single Responsibility Principle
- Difficult to test (too many dependencies)
- Hard to maintain and extend
- Creates tight coupling between unrelated features
- Becomes a bottleneck for team collaboration

**Solution**: Split into focused classes:
- `UserRepository` - Data access
- `UserValidator` - Input validation
- `EmailNotifier` - Email sending
- `UserAuthService` - Authentication
- `UserCacheService` - Caching operations

### Spaghetti Code

**Problem**: Code with no clear structure, excessive nesting, and tangled control flow.

**Bad Example**:
```python
def process_order(order, user, inventory):
    if order is not None:
        if user is not None:
            if user.is_active:
                if order.items:
                    total = 0
                    for item in order.items:
                        if item in inventory:
                            if inventory[item] > 0:
                                if item.price > 0:
                                    if user.has_permission('purchase'):
                                        if order.total <= user.credit_limit:
                                            if validate_address(user.address):
                                                if check_fraud_score(user) < 0.5:
                                                    # Finally process the order
                                                    total += item.price * item.quantity
                                                    inventory[item] -= item.quantity
                                                    # ... more nested logic
                                                else:
                                                    return {"error": "Fraud detected"}
                                            else:
                                                return {"error": "Invalid address"}
                                        else:
                                            return {"error": "Credit limit exceeded"}
                                    else:
                                        return {"error": "No permission"}
                                else:
                                    return {"error": "Invalid price"}
                            else:
                                return {"error": "Out of stock"}
                        else:
                            return {"error": "Item not found"}
                    return {"success": True, "total": total}
                else:
                    return {"error": "Empty order"}
            else:
                return {"error": "User inactive"}
        else:
            return {"error": "No user"}
    else:
        return {"error": "No order"}
```

**Why It's Bad**:
- Extremely hard to read and follow
- Difficult to modify without breaking something
- High cognitive load for developers
- Testing is nearly impossible
- Violates flat is better than nested principle

**Solution**: Use early returns and extract methods:
```python
def process_order(order, user, inventory):
    if not order:
        return {"error": "No order"}
    
    if not user or not user.is_active:
        return {"error": "Invalid user"}
    
    if not order.items:
        return {"error": "Empty order"}
    
    if not user.has_permission('purchase'):
        return {"error": "No permission"}
    
    if not validate_address(user.address):
        return {"error": "Invalid address"}
    
    if check_fraud_score(user) >= 0.5:
        return {"error": "Fraud detected"}
    
    if order.total > user.credit_limit:
        return {"error": "Credit limit exceeded"}
    
    total, error = calculate_total_and_update_inventory(order.items, inventory)
    if error:
        return {"error": error}
    
    return {"success": True, "total": total}
```

### Magic Numbers and Strings

**Problem**: Hardcoded values scattered throughout code without explanation.

**Bad Example**:
```python
def calculate_price(base_price, quantity, user_type):
    if user_type == 1:
        discount = 0.15
    elif user_type == 2:
        discount = 0.25
    elif user_type == 3:
        discount = 0.35
    else:
        discount = 0.05
    
    tax_rate = 0.0825
    shipping = 5.99 if base_price * quantity < 50 else 0
    
    subtotal = base_price * quantity * (1 - discount)
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping
    
    if total > 1000:
        total *= 0.95
    
    return round(total, 2)

def check_timeout(elapsed_time):
    if elapsed_time > 30000:
        return True
    if elapsed_time > 15000:
        send_warning()
    return False
```

**Why It's Bad**:
- No context for what numbers mean
- Changing values requires finding all occurrences
- Easy to introduce bugs when modifying
- Requires memorization or hunting for meaning

**Solution**: Use named constants:
```python
from enum import IntEnum

class UserType(IntEnum):
    STANDARD = 1
    PREMIUM = 2
    VIP = 3
    TRIAL = 4

DISCOUNT_RATES = {
    UserType.STANDARD: 0.05,
    UserType.PREMIUM: 0.15,
    UserType.VIP: 0.25,
    UserType.TRIAL: 0.35,
}

TAX_RATE = 0.0825
FREE_SHIPPING_THRESHOLD = 50.0
BASE_SHIPPING_COST = 5.99
BULK_ORDER_THRESHOLD = 1000.0
BULK_DISCOUNT = 0.95

TIMEOUT_MS = 30000
WARNING_THRESHOLD_MS = 15000

def calculate_price(base_price, quantity, user_type):
    discount = DISCOUNT_RATES.get(user_type, DISCOUNT_RATES[UserType.STANDARD])
    
    subtotal = base_price * quantity * (1 - discount)
    tax = subtotal * TAX_RATE
    
    shipping = 0 if subtotal >= FREE_SHIPPING_THRESHOLD else BASE_SHIPPING_COST
    total = subtotal + tax + shipping
    
    if total > BULK_ORDER_THRESHOLD:
        total *= BULK_DISCOUNT
    
    return round(total, 2)
```

### Silent Failures

**Problem**: Errors are caught but not properly handled or logged, causing issues to go unnoticed.

**Bad Example**:
```python
def save_user_data(user_id, data):
    try:
        db.save(user_id, data)
    except Exception:
        pass  # Silently ignore errors

def load_configuration():
    try:
        config = json.load(open('config.json'))
        return config
    except:
        return {}  # Return empty config on any error

def send_notification(user, message):
    try:
        email_service.send(user.email, message)
        sms_service.send(user.phone, message)
        push_service.send(user.device_id, message)
    except Exception as e:
        logger.error(e)  # Log but don't alert or retry
        # User never receives critical notification
```

**Why It's Bad**:
- Errors go unnoticed until they cause major issues
- No way to diagnose problems after the fact
- Data loss can occur silently
- Users experience broken functionality without explanation

**Solution**: Proper error handling with visibility:
```python
def save_user_data(user_id, data):
    try:
        db.save(user_id, data)
        logger.info(f"Successfully saved data for user {user_id}")
    except DatabaseError as e:
        logger.error(f"Database error saving user {user_id}: {e}")
        alert_team("CRITICAL", f"Database save failed for user {user_id}")
        raise
    except ValidationError as e:
        logger.warning(f"Invalid data for user {user_id}: {e}")
        raise InvalidUserDataError(f"Cannot save invalid data: {e}")

def load_configuration():
    config_path = Path('config.json')
    
    if not config_path.exists():
        logger.error("Configuration file missing")
        raise ConfigurationError("config.json not found")
    
    try:
        with open(config_path) as f:
            config = json.load(f)
        validate_config(config)
        return config
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config file: {e}")
        raise ConfigurationError(f"Malformed config: {e}")
    except Exception as e:
        logger.error(f"Unexpected error loading config: {e}")
        raise
```

### Resource Leaks

**Problem**: Resources like files, connections, or memory are not properly released.

**Bad Example**:
```python
def read_large_file(filename):
    f = open(filename, 'r')
    content = f.read()
    # Forgot to close file
    return content

def process_images(image_paths):
    results = []
    for path in image_paths:
        conn = DatabaseConnection()
        img = load_image(path)
        processed = apply_filter(img)
        conn.save(processed)
        # Connection never closed
        results.append(processed)
    return results

def cache_results(data):
    global cache
    cache = {}  # Old cache lost, never cleaned up
    for item in data:
        key = generate_key(item)
        cache[key] = item  # Cache grows unbounded
```

**Why It's Bad**:
- File handles exhaust system limits
- Database connections pool depleted
- Memory usage grows indefinitely
- Application crashes under load

**Solution**: Use context managers and proper cleanup:
```python
from contextlib import contextmanager

def read_large_file(filename):
    with open(filename, 'r') as f:
        return f.read()

@contextmanager
def database_connection():
    conn = DatabaseConnection()
    try:
        yield conn
    finally:
        conn.close()

def process_images(image_paths):
    results = []
    for path in image_paths:
        with database_connection() as conn:
            img = load_image(path)
            processed = apply_filter(img)
            conn.save(processed)
            results.append(processed)
    return results

class LRUCache:
    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
```

### Race Conditions

**Problem**: Concurrent access to shared resources without proper synchronization.

**Bad Example**:
```python
# Global counter accessed by multiple threads
counter = 0

def increment_counter():
    global counter
    temp = counter
    time.sleep(0.001)  # Simulate some work
    counter = temp + 1

# Multiple threads calling increment_counter()
# Expected: counter = 1000
# Actual: counter = ~300-700 (varies randomly)

# Bank account example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if self.balance >= amount:
            # Another thread could withdraw between check and update
            self.balance -= amount
            return True
        return False
```

**Why It's Bad**:
- Non-deterministic behavior
- Data corruption
- Lost updates
- Extremely difficult to reproduce and debug

**Solution**: Use proper synchronization:
```python
import threading
from decimal import Decimal

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

class BankAccount:
    def __init__(self, balance):
        self.balance = Decimal(str(balance))
        self._lock = threading.RLock()
    
    def withdraw(self, amount):
        with self._lock:
            amount = Decimal(str(amount))
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False
    
    def deposit(self, amount):
        with self._lock:
            self.balance += Decimal(str(amount))
    
    def transfer(self, to_account, amount):
        # Acquire locks in consistent order to prevent deadlock
        first, second = sorted([self, to_account], key=id)
        with first._lock:
            with second._lock:
                if self.withdraw(amount):
                    to_account.deposit(amount)
                    return True
                return False
```

### SQL Injection Vulnerabilities

**Problem**: User input is directly concatenated into SQL queries.

**Bad Example**:
```python
def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query)
    return result is not None

def get_user_by_id(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return db.execute(query)

def search_products(search_term):
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
    return db.execute(query)
```

**Why It's Bad**:
- Allows attackers to execute arbitrary SQL
- Can lead to data breaches
- Enables data manipulation or deletion
- One of the most common web vulnerabilities

**Solution**: Use parameterized queries:
```python
def login(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    result = db.execute(query, (username, password))
    return result is not None

def get_user_by_id(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    return db.execute(query, (user_id,))

def search_products(search_term):
    query = "SELECT * FROM products WHERE name LIKE ?"
    return db.execute(query, (f"%{search_term}%",))

# With SQLAlchemy ORM
def get_user(username):
    return session.query(User).filter(User.username == username).first()
```

### Premature Optimization

**Problem**: Optimizing code before identifying actual bottlenecks, sacrificing readability.

**Bad Example**:
```python
# Overly complex "optimized" code
def process_data(data):
    # Unnecessary micro-optimizations
    result = []
    append = result.append
    for i in range(len(data)):
        item = data[i]
        if item & 1:
            append(item << 1)
        else:
            append(item >> 1)
    return result

# Using obscure one-liners
def find_duplicates(arr):
    return list(set([x for x in arr if arr.count(x) > 1]))

# Manual loop unrolling
def sum_array(arr):
    total = 0
    for i in range(0, len(arr), 4):
        if i + 3 < len(arr):
            total += arr[i] + arr[i+1] + arr[i+2] + arr[i+3]
        else:
            for j in range(i, len(arr)):
                total += arr[j]
    return total
```

**Why It's Bad**:
- Code is harder to read and maintain
- Optimizations may not provide measurable benefit
- Makes future changes more difficult
- Wastes development time on non-issues

**Solution**: Write clear code first, optimize based on profiling:
```python
def process_data(data):
    """Double odd numbers, halve even numbers."""
    result = []
    for item in data:
        if item % 2 == 1:
            result.append(item * 2)
        else:
            result.append(item // 2)
    return result

def find_duplicates(arr):
    """Find elements that appear more than once."""
    from collections import Counter
    counts = Counter(arr)
    return [item for item, count in counts.items() if count > 1]

def sum_array(arr):
    """Sum all elements in array."""
    return sum(arr)

# Profile first, then optimize if needed:
# import cProfile
# cProfile.run('process_data(large_dataset)')
```

## Common Failure Scenarios

### Null Pointer / NoneType Errors

**Failure Example**:
```python
def get_user_email(user_id):
    user = database.get_user(user_id)
    # user might be None
    return user.email  # AttributeError: 'NoneType' object has no attribute 'email'

def process_response(response):
    data = response.json()
    return data['results'][0]['name']  # KeyError or IndexError
```

**Prevention**:
```python
def get_user_email(user_id):
    user = database.get_user(user_id)
    if user is None:
        raise UserNotFoundError(f"User {user_id} not found")
    return user.email

def process_response(response):
    data = response.json()
    results = data.get('results', [])
    if not results:
        return None
    return results[0].get('name')
```

### Off-by-One Errors

**Failure Example**:
```python
# Iterate through array
for i in range(len(items) + 1):  # Goes one too far
    process(items[i])  # IndexError on last iteration

# Array indexing
middle = len(items) / 2  # Float instead of int in Python 3

# Boundary conditions
if index <= len(items):  # Should be < not <=
    return items[index]  # IndexError when index == len(items)
```

**Prevention**:
```python
for i in range(len(items)):
    process(items[i])

# Or better:
for item in items:
    process(item)

middle = len(items) // 2

if index < len(items):
    return items[index]
```

### Integer Overflow

**Failure Example**:
```python
def calculate_total(prices, quantities):
    total = 0
    for price, qty in zip(prices, quantities):
        total += price * qty  # Can overflow with large numbers
    return total

def binary_search_mid(left, right):
    mid = (left + right) // 2  # Can overflow if left + right > MAX_INT
    return mid
```

**Prevention**:
```python
from decimal import Decimal

def calculate_total(prices, quantities):
    total = Decimal('0')
    for price, qty in zip(prices, quantities):
        total += Decimal(str(price)) * Decimal(str(qty))
    return total

def binary_search_mid(left, right):
    mid = left + (right - left) // 2  # Avoids overflow
    return mid
```

### Timezone and Date Handling Failures

**Failure Example**:
```python
from datetime import datetime

def schedule_reminder(date_string):
    # Different formats cause failures
    reminder_date = datetime.strptime(date_string, "%Y-%m-%d")
    
    # Comparing naive and aware datetimes
    now = datetime.now()
    if reminder_date < now:  # TypeError if one is timezone-aware
        send_reminder()
    
    # Assuming all dates are UTC
    expiry = datetime(2024, 12, 31, 23, 59, 59)
    # Is this UTC? Local time? Which timezone?
```

**Prevention**:
```python
from datetime import datetime, timezone
from dateutil import parser

def schedule_reminder(date_string):
    # Use robust parsing
    reminder_date = parser.parse(date_string)
    
    # Always use timezone-aware datetimes
    now = datetime.now(timezone.utc)
    reminder_date = reminder_date.astimezone(timezone.utc)
    
    if reminder_date < now:
        send_reminder()
    
    # Explicitly specify timezone
    expiry = datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
```

## Lessons Learned

### From Real-World Failures

1. **Ariane 5 Rocket Explosion (1996)**
   - Cause: Integer overflow converting 64-bit float to 16-bit integer
   - Lesson: Validate type conversions, especially in safety-critical systems

2. **Mars Climate Orbiter Loss (1999)**
   - Cause: Imperial vs metric unit mismatch
   - Lesson: Use type systems and units libraries to prevent unit errors

3. **Knight Capital Trading Loss ($440M in 45 minutes)**
   - Cause: Deployed old code with flag that triggered unintended trades
   - Lesson: Automated testing, feature flags, gradual rollouts

4. **Cloudflare Memory Leak (2017)**
   - Cause: Buffer overread in HTML parser leaked sensitive data
   - Lesson: Bounds checking, memory safety, thorough security review

### Key Takeaways

1. **Always validate inputs** - Never trust external data
2. **Handle errors explicitly** - Silent failures are dangerous
3. **Test edge cases** - Boundaries are where bugs hide
4. **Use appropriate abstractions** - Don't reinvent standard solutions
5. **Document assumptions** - Make implicit knowledge explicit
6. **Monitor in production** - Catch issues before users do
7. **Review code regularly** - Fresh eyes catch problems
8. **Learn from incidents** - Post-mortems prevent recurrence

## Checklist for Avoiding Common Failures

- [ ] All inputs validated and sanitized
- [ ] Error handling covers all failure modes
- [ ] Resources properly cleaned up (files, connections, memory)
- [ ] Concurrent access properly synchronized
- [ ] No hardcoded magic numbers or strings
- [ ] SQL queries use parameterization
- [ ] Timezone handling is explicit and consistent
- [ ] Array indices bounds-checked
- [ ] Null/None cases handled
- [ ] Logging provides adequate debugging information
- [ ] Tests cover edge cases and error paths
- [ ] Code reviewed by at least one other developer
