# Bad API Design

Poor API design leads to confusing integrations, increased support burden, and frustrated developers. Good API design follows established conventions and prioritizes developer experience.

---

## Principles of Good API Design

1. **Consistency**: Similar operations should work similarly
2. **Simplicity**: Easy to learn and use
3. **Predictability**: Behavior matches expectations
4. **Discoverability**: Easy to explore without extensive documentation
5. **Error Handling**: Clear, actionable error messages

---

## Common API Design Mistakes

### Inconsistent Naming Conventions

**Bad Example:**
```python
# Mixing naming styles
api.getUserById()
api.delete_user()
api.updateUserDetails()
api.remove_item()
```

**Problems:**
- Inconsistent casing (camelCase vs snake_case)
- Inconsistent verbs (get/delete/update/remove)
- Hard to remember which style applies where

**Better:**
```python
# Consistent RESTful style
api.users.get(user_id)
api.users.delete(user_id)
api.users.update(user_id, data)
api.items.delete(item_id)
```

---

### Leaky Abstractions

**Bad Example:**
```python
def save_user(user_data):
    """Save user to database."""
    # Implementation details exposed
    conn = psycopg2.connect(database="users_db", 
                           user="admin", 
                           password="secret123")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (user_data['name'], user_data['email'])
    )
    conn.commit()
    cursor.close()
    conn.close()
```

**Problems:**
- Database credentials in code
- SQL implementation exposed
- No abstraction layer
- Caller must understand database details

**Better:**
```python
class UserRepository:
    def save(self, user: User) -> None:
        """Persist user to storage."""
        self._db.users.insert_one({
            "name": user.name,
            "email": user.email,
        })
```

---

### Poor Error Handling

**Bad Example:**
```python
def process_payment(amount, card_number):
    try:
        result = payment_gateway.charge(amount, card_number)
        return result
    except Exception as e:
        return {"error": str(e)}
```

**Response examples:**
```json
{"error": "Error: Connection refused"}
{"error": "TypeError: 'NoneType' object is not subscriptable"}
{"error": "DatabaseError: ORA-00942: table or view does not exist"}
```

**Problems:**
- Exposes internal implementation details
- No actionable information for callers
- Inconsistent error formats
- Security risk (leaks system information)

**Better:**
```python
class PaymentError(Exception):
    def __init__(self, code: str, message: str, retryable: bool = False):
        self.code = code
        self.message = message
        self.retryable = retryable

def process_payment(amount, card_number):
    try:
        result = payment_gateway.charge(amount, card_number)
        return result
    except InsufficientFundsError:
        raise PaymentError(
            code="INSUFFICIENT_FUNDS",
            message="The card has insufficient funds",
            retryable=False
        )
    except GatewayConnectionError:
        raise PaymentError(
            code="GATEWAY_UNAVAILABLE",
            message="Payment service temporarily unavailable",
            retryable=True
        )
```

**Error Response:**
```json
{
  "error": {
    "code": "INSUFFICIENT_FUNDS",
    "message": "The card has insufficient funds",
    "retryable": false,
    "documentation_url": "https://api.example.com/errors/INSUFFICIENT_FUNDS"
  }
}
```

---

### Breaking Changes Without Versioning

**Bad Example:**
```python
# Version 1.0
def get_user(user_id):
    return {"id": user_id, "name": "John"}

# Version 1.1 (breaking change!)
def get_user(user_id, include_email=False):
    if include_email:
        return {"id": user_id, "name": "John", "email": "john@example.com"}
    return {"id": user_id, "name": "John", "email": None}  # Breaks existing code
```

**Problems:**
- Existing clients break unexpectedly
- No migration path
- Erodes trust in the API

**Better:**
```python
# Version explicitly
def get_user_v1(user_id):
    return {"id": user_id, "name": "John"}

def get_user_v2(user_id, options=None):
    result = {"id": user_id, "name": "John"}
    if options and options.get("include_email"):
        result["email"] = "john@example.com"
    return result
```

Or use URL versioning:
```
GET /api/v1/users/123
GET /api/v2/users/123?fields=id,name,email
```

---

### Over-fetching and Under-fetching

**Bad Example:**
```python
# Always returns everything
def get_user(user_id):
    return {
        "id": user_id,
        "name": "John",
        "email": "john@example.com",
        "address": {...},
        "orders": [...],
        "payment_methods": [...],
        "preferences": {...},
        "audit_log": [...]
    }
```

**Problems:**
- Wastes bandwidth on mobile
- Exposes unnecessary data
- Slow responses for simple needs

**Better:**
```python
# Field selection
def get_user(user_id, fields=None):
    default_fields = ["id", "name"]
    fields = fields or default_fields
    
    user = fetch_user(user_id)
    return {field: user[field] for field in fields if field in user}

# Usage:
# GET /users/123?fields=id,name,email
```

Or use GraphQL-style queries:
```graphql
query {
  user(id: 123) {
    id
    name
    email
  }
}
```

---

### Hidden Side Effects

**Bad Example:**
```python
def get_user(user_id):
    # Increments login counter (side effect!)
    db.increment_login_count(user_id)
    
    # Sends notification (side effect!)
    if is_new_device(user_id):
        send_security_alert(user_id)
    
    # Returns user data
    return fetch_user(user_id)
```

**Problems:**
- GET request modifies state
- Unexpected behavior for callers
- Hard to test and debug
- Violates HTTP semantics

**Better:**
```python
def get_user(user_id):
    """Retrieve user information (read-only)."""
    return fetch_user(user_id)

def record_login(user_id, device_info):
    """Explicitly record a login event."""
    db.increment_login_count(user_id)
    if is_new_device(device_info):
        send_security_alert(user_id)
```

---

### Missing Pagination

**Bad Example:**
```python
def get_all_users():
    """Returns ALL users."""
    return db.query("SELECT * FROM users")
```

**Problems:**
- Memory exhaustion with large datasets
- Slow response times
- Unreliable network transfers

**Better:**
```python
def list_users(page=1, page_size=50, sort_by="created_at", order="desc"):
    """
    List users with pagination.
    
    Args:
        page: Page number (1-indexed)
        page_size: Items per page (max 100)
        sort_by: Field to sort by
        order: Sort direction (asc/desc)
    
    Returns:
        {
            "items": [...],
            "page": 1,
            "page_size": 50,
            "total_items": 1234,
            "total_pages": 25,
            "next_page": 2,
            "prev_page": null
        }
    """
    offset = (page - 1) * page_size
    items = db.query(
        "SELECT * FROM users ORDER BY {} {} LIMIT {} OFFSET {}".format(
            sort_by, order, page_size, offset
        )
    )
    
    return {
        "items": items,
        "page": page,
        "page_size": page_size,
        "total_items": get_total_count(),
        "total_pages": math.ceil(get_total_count() / page_size),
        "next_page": page + 1 if page < get_total_pages() else None,
        "prev_page": page - 1 if page > 1 else None
    }
```

---

### Ambiguous Parameter Names

**Bad Example:**
```python
def create_order(user, items, flag1, flag2, data):
    pass

# What do these mean?
create_order(1, [item1, item2], True, False, {"x": 1})
```

**Better:**
```python
def create_order(
    user_id: int,
    items: List[Item],
    express_shipping: bool = False,
    gift_wrap: bool = False,
    custom_options: dict = None
):
    """
    Create a new order.
    
    Args:
        user_id: ID of the customer placing the order
        items: List of items to purchase
        express_shipping: Enable expedited shipping
        gift_wrap: Add gift wrapping service
        custom_options: Additional order customizations
    """
```

---

## API Design Checklist

```markdown
## API Quality Checklist

### Design
- [ ] Consistent naming conventions throughout
- [ ] RESTful principles followed (or clear alternative)
- [ ] No hidden side effects in read operations
- [ ] Proper HTTP status codes used
- [ ] Pagination implemented for list endpoints

### Documentation
- [ ] All endpoints documented
- [ ] Request/response examples provided
- [ ] Error codes explained
- [ ] Authentication requirements clear
- [ ] Rate limits documented

### Error Handling
- [ ] Consistent error format
- [ ] Actionable error messages
- [ ] No internal details leaked
- [ ] Retry guidance included when applicable

### Versioning
- [ ] Version strategy defined
- [ ] Backward compatibility maintained
- [ ] Deprecation policy documented
- [ ] Migration guides provided

### Security
- [ ] Authentication required
- [ ] Authorization checked for each resource
- [ ] Input validated and sanitized
- [ ] Rate limiting implemented
- [ ] Sensitive data protected
```

---

## Related Documents

- [[poor_documentation]] - Documentation mistakes
- [[bad_variable_names]] - Naming anti-patterns
- [[security_mistakes]] - Security vulnerabilities
- [[unsafe_code]] - Writing insecure code
