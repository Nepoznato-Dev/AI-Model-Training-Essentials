# Circular Dependencies

## Overview

Circular dependencies occur when modules, classes, or packages depend on each other directly or indirectly, creating cycles that make code difficult to maintain, test, and understand. This document provides examples and solutions for eliminating circular dependencies.

## Types of Circular Dependencies

### Direct Circular Dependencies

**Bad Example:**
```python
# module_a.py
from module_b import process_data

def handle_request(data):
    return process_data(data)

# module_b.py
from module_a import handle_request  # CIRCULAR!

def process_data(data):
    # Need to call back to module_a
    return handle_request(transform(data))
```

**Why It's Bad:**
- Import errors at runtime
- Impossible to import either module independently
- Code cannot be tested in isolation
- Indicates poor architectural design

**Better Approach:**
```python
# module_common.py (shared functionality)
def transform(data):
    return data.upper()

# module_a.py
from module_common import transform

def handle_request(data):
    processed = transform(data)
    return {"result": processed}

# module_b.py
from module_common import transform

def process_data(data):
    return transform(data)
```

### Indirect Circular Dependencies

**Bad Example:**
```python
# user.py
from order import Order  # User has orders

class User:
    def __init__(self, id):
        self.id = id
        self.orders = []
    
    def get_total_spent(self):
        return sum(order.total for order in self.orders)

# order.py
from user import User  # Order belongs to user (CIRCULAR!)
from product import Product

class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products
        self.total = sum(p.price for p in products)

# product.py
from order import Order  # Product can be in orders (another cycle!)

class Product:
    def __init__(self, id, price):
        self.id = id
        self.price = price
```

**Why It's Bad:**
- Complex web of dependencies
- Changes ripple through entire system
- Difficult to understand object lifecycle
- Testing requires mocking entire dependency chain

**Better Approach:**
```python
# Use IDs instead of object references
# user.py
class User:
    def __init__(self, id):
        self.id = id
        self.order_ids = []

# order.py
class Order:
    def __init__(self, user_id, product_ids, total):
        self.user_id = user_id  # Reference by ID
        self.product_ids = product_ids
        self.total = total

# product.py
class Product:
    def __init__(self, id, price):
        self.id = id
        self.price = price

# repository.py (handles relationships)
class UserRepository:
    def get_user_with_orders(self, user_id):
        user = self.get(user_id)
        orders = order_repo.get_by_user_id(user_id)
        return UserWithOrders(user, orders)
```

### Inheritance Cycles

**Bad Example:**
```typescript
// FileA.ts
import { ClassB } from './FileB';

export class ClassA extends ClassB {
    doSomething() {
        return super.doSomething();
    }
}

// FileB.ts
import { ClassA } from './FileA';  // CIRCULAR!

export class ClassB extends ClassA {
    doSomething() {
        return "B";
    }
}
```

**Why It's Bad:**
- Logical contradiction in inheritance
- Runtime errors in most languages
- Indicates flawed class hierarchy design

**Better Approach:**
```typescript
// Extract common functionality
export abstract class BaseClass {
    abstract doSomething(): string;
    
    commonMethod() {
        return "shared";
    }
}

// FileA.ts
import { BaseClass } from './BaseClass';

export class ClassA extends BaseClass {
    doSomething() {
        return "A";
    }
}

// FileB.ts
import { BaseClass } from './BaseClass';

export class ClassB extends BaseClass {
    doSomething() {
        return "B";
    }
}
```

## Real-World Scenarios

### Scenario 1: Service Layer Circular Dependency

**Vulnerable Code:**
```javascript
// userService.js
const orderService = require('./orderService');

async function getUserDetails(userId) {
    const user = await db.users.findById(userId);
    const orders = await orderService.getUserOrders(userId);
    return { ...user, orders };
}

// orderService.js
const userService = require('./userService');  // CIRCULAR!

async function getUserOrders(userId) {
    const user = await userService.getUser(userId);  // Why??
    return await db.orders.findByUserId(userId);
}

async function createOrder(orderData) {
    const user = await userService.getUser(orderData.userId);
    // ... create order
}
```

**Problem:**
- `userService` imports `orderService`
- `orderService` imports `userService`
- Node.js may return incomplete module exports
- Runtime errors: `TypeError: Cannot read property 'getUser' of undefined`

**Secure Implementation:**
```javascript
// userService.js
const orderService = require('./orderService');

async function getUserDetails(userId) {
    const user = await db.users.findById(userId);
    const orders = await orderService.getUserOrders(userId);
    return { ...user, orders };
}

async function getUser(userId) {
    return await db.users.findById(userId);
}

module.exports = { getUserDetails, getUser };

// orderService.js
// Remove circular dependency - don't need userService
async function getUserOrders(userId) {
    // Just query orders directly, no need to fetch user
    return await db.orders.findByUserId(userId);
}

async function createOrder(orderData) {
    // Validate userId exists via database constraint
    // No need to fetch full user object
    return await db.orders.create(orderData);
}

module.exports = { getUserOrders, createOrder };
```

### Scenario 2: UI Component Circular Imports

**Vulnerable Code:**
```jsx
// Modal.jsx
import Button from './Button';

function Modal({ children, onClose }) {
    return (
        <div className="modal">
            {children}
            <Button onClick={onClose}>Close</Button>
        </div>
    );
}

// Button.jsx
import Modal from './Modal';  // CIRCULAR!

function Button({ children, onClick, showModal }) {
    return (
        <button onClick={onClick}>
            {showModal ? <Modal>Content</Modal> : children}
        </button>
    );
}
```

**Problem:**
- Webpack/Vite may fail to bundle
- Components load incorrectly
- Hot reload breaks

**Secure Implementation:**
```jsx
// Modal.jsx
import Button from './Button';

function Modal({ children, onClose }) {
    return (
        <div className="modal">
            {children}
            <Button onClick={onClose}>Close</Button>
        </div>
    );
}

// Button.jsx
// Remove Modal dependency - Button shouldn't know about Modal
function Button({ children, onClick }) {
    return (
        <button onClick={onClick}>
            {children}
        </button>
    );
}

// Usage in parent component
function ParentComponent() {
    const [showModal, setShowModal] = useState(false);
    
    return (
        <>
            <Button onClick={() => setShowModal(true)}>
                Open Modal
            </Button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    Content
                </Modal>
            )}
        </>
    );
}
```

## Prevention Strategies

### Dependency Injection

```python
# BAD: Direct imports create coupling
class UserService:
    def __init__(self):
        self.email_service = EmailService()  # Hard dependency
        self.db = Database()

# GOOD: Inject dependencies
class UserService:
    def __init__(self, email_service, db):
        self.email_service = email_service
        self.db = db

# Even better: Use interfaces/protocols
from typing import Protocol

class EmailSender(Protocol):
    def send(self, to: str, subject: str, body: str) -> None: ...

class UserService:
    def __init__(self, email_sender: EmailSender, db):
        self.email_sender = email_sender
        self.db = db
```

### Event-Based Architecture

```python
# BAD: Direct calls between modules
class OrderProcessor:
    def complete_order(self, order):
        # Direct coupling to notification, inventory, analytics
        notification_service.send_confirmation(order)
        inventory_service.update_stock(order)
        analytics_service.track_purchase(order)

# GOOD: Event-based decoupling
class EventBus:
    def __init__(self):
        self.listeners = {}
    
    def subscribe(self, event_type, handler):
        self.listeners.setdefault(event_type, []).append(handler)
    
    def publish(self, event_type, data):
        for handler in self.listeners.get(event_type, []):
            handler(data)

# Each service subscribes independently
event_bus.subscribe('order.completed', notification_handler)
event_bus.subscribe('order.completed', inventory_handler)
event_bus.subscribe('order.completed', analytics_handler)

# OrderProcessor just publishes events
class OrderProcessor:
    def complete_order(self, order):
        # ... process order ...
        event_bus.publish('order.completed', order)
```

### Common Module Extraction

```python
# BAD: Two modules depending on each other
# utils/validation.py <-> utils/formatting.py

# GOOD: Extract shared code to third module
# utils/common.py (no dependencies on other utils)
def validate_and_format(data):
    # Shared functionality

# utils/validation.py
from utils.common import validate_and_format

# utils/formatting.py  
from utils.common import validate_and_format
```

### Lazy Loading / Deferred Imports

```python
# When circular dependency is unavoidable
class ClassA:
    def method_needing_b(self):
        # Import inside method, not at module level
        from module_b import ClassB
        return ClassB().do_something()
```

## Detection Patterns

### Tools for Detection

```bash
# Python: detect circular imports
pip install pylint
pylint --enable=import-cycle your_module/

# JavaScript: madge tool
npx madge --circular src/

# TypeScript: ts-madge
npx ts-madge --circular .

# Java: JDepend, SonarQube
```

### Code Review Red Flags

1. **Mutual Imports:**
   ```python
   # module_a.py imports from module_b
   # module_b.py imports from module_a
   ```

2. **Import Inside Functions:**
   ```python
   # Often indicates circular dependency workaround
   def my_function():
       from other_module import Something  # Smell!
   ```

3. **Long Import Chains:**
   ```
   A → B → C → D → A (indirect cycle)
   ```

## Testing Checklist

- [ ] Run circular dependency detection tools
- [ ] Verify modules can be imported independently
- [ ] Test each module in isolation
- [ ] Check for import statements inside functions
- [ ] Review module dependency graph
- [ ] Ensure clear layer boundaries
- [ ] Verify dependency injection is used
- [ ] Check for forward declarations where needed
- [ ] Monitor build warnings about circular refs
- [ ] Document allowed dependencies between layers

## Related Documents

- [[code_smells]] - Indicators of code quality issues
- [[bad_api_design]] - Module and API boundaries
- [[spaghetti_code]] - Poorly structured code
- [[bad_agent_design]] - System architecture patterns
