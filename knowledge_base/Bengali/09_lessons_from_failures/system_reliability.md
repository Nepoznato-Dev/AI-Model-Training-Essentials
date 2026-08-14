---
# Metadata
title: "System Reliability Issues"
description: "System failures and reliability patterns"
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
tags: [system, reliability, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# সিস্টেম নির্ভরযোগ্যতা সমস্যা
এই নথিটি মেমরি ফাঁস, রেসের অবস্থা, সমসাময়িক প্রোগ্রামিং ত্রুটি এবং সিস্টেম ডিজাইন ব্যর্থতা সহ নির্ভরযোগ্যতার সমস্যাগুলিকে একীভূত করে৷
---

## মেমরি লিক
মেমরি ফাঁস ঘটে যখন প্রোগ্রামগুলি মেমরি বরাদ্দ করে কিন্তু যখন আর প্রয়োজন হয় না তখন এটি প্রকাশ করতে ব্যর্থ হয়, যার ফলে ধীরে ধীরে মেমরি খরচ বৃদ্ধি পায়।
### ভুলে যাওয়া ঘটনা শ্রোতারা
**খারাপ উদাহরণ (জাভাস্ক্রিপ্ট):**```javascript
// VULNERABLE: Event listener never removed
class Component {
    constructor(element) {
        this.element = element;
        this.data = new Array(1000000).fill('large data');
        
        // Listener added but never removed
        window.addEventListener('resize', this.handleResize.bind(this));
    }
    
    handleResize() {
        console.log('Resized', this.data.length);
    }
    
    destroy() {
        // Forgot to remove event listener!
        this.element.remove();
        // Component "destroyed" but listener still references it
        // Memory cannot be garbage collected
    }
}
```

**উত্তম পদ্ধতি:**```javascript
class Component {
    constructor(element) {
        this.element = element;
        this.data = new Array(1000000).fill('large data');
        this.boundHandleResize = this.handleResize.bind(this);
        
        window.addEventListener('resize', this.boundHandleResize);
    }
    
    handleResize() {
        console.log('Resized', this.data.length);
    }
    
    destroy() {
        // Properly clean up
        window.removeEventListener('resize', this.boundHandleResize);
        this.element.remove();
        this.data = null;  // Allow garbage collection
    }
}
```

### অপ্রকাশিত সম্পদ
**খারাপ উদাহরণ (পাইথন):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**উত্তম পদ্ধতি:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### সার্কুলার রেফারেন্স
**খারাপ উদাহরণ (পাইথন):**```python
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        child.parent = self  # Creates circular reference
        self.children.append(child)

# Creating tree structure
root = Node('root')
child = Node('child')
root.add_child(child)

# When deleting root, child keeps reference to root
# When deleting child, root keeps reference to child
# Neither can be garbage collected (in some languages)
```

**সমাধান:** ব্যাক-রেফারেন্সের জন্য দুর্বল রেফারেন্স ব্যবহার করুন```python
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent_ref = None
        self.children = []
    
    @property
    def parent(self):
        if self._parent_ref:
            return self._parent_ref()
        return None
    
    @parent.setter
    def parent(self, node):
        self._parent_ref = weakref.ref(node) if node else None
```

---

## রেসের শর্ত
সফ্টওয়্যার আচরণ ইভেন্টের আপেক্ষিক সময়ের উপর নির্ভর করে, যেমন থ্রেড এক্সিকিউশন অর্ডারের উপর নির্ভর করে রেস অবস্থা।
### চেক-এরপর-অ্যাক্ট রেস কন্ডিশন
**খারাপ উদাহরণ (পাইথন):**```python
# VULNERABLE: Check and act are not atomic
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
    
    def withdraw(self, amount):
        # RACE CONDITION: Another thread can modify balance between check and act
        if self.balance >= amount:  # Check
            time.sleep(0.001)  # Context switch opportunity
            self.balance -= amount  # Act
            return True
        return False
```

**সমস্যা পরিস্থিতি:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**উত্তম পদ্ধতি:**```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
    
    def withdraw(self, amount):
        with self.lock:  # Atomic operation
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False
```

### রিড-মডিফাই-রাইট রেস কন্ডিশন
**খারাপ উদাহরণ:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**উত্তম পদ্ধতি:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### অলস সূচনা রেস অবস্থা
**খারাপ উদাহরণ:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**উত্তম পদ্ধতি:**```python
class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance
```

---

## কনকারেন্সি অ্যান্টি-প্যাটার্নস
### অচলাবস্থা
**খারাপ উদাহরণ:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**প্রতিরোধ:** সর্বদা একটি সামঞ্জস্যপূর্ণ ক্রমে লকগুলি অর্জন করুন```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### লাইভলক
**খারাপ উদাহরণ:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### অনাহার
**খারাপ উদাহরণ:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**সমাধান:** ন্যায্য সময়সূচী বা অগ্রাধিকার বার্ধক্য ব্যবহার করুন
---

## পারফরম্যান্সের সমস্যা
### N+1 কোয়েরি সমস্যা
**খারাপ উদাহরণ:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**উত্তম পদ্ধতি:**```python
# Fetch all users
users = db.query("SELECT * FROM users")
user_ids = [u.id for u in users]

# Single query for all orders
orders = db.query(
    "SELECT * FROM orders WHERE user_id IN (?)",
    user_ids
)

# Group orders by user
orders_by_user = group_by(orders, 'user_id')
for user in users:
    user.orders = orders_by_user.get(user.id, [])
```

### অদক্ষ লুপ
**খারাপ উদাহরণ:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**উত্তম পদ্ধতি:**```python
# O(n) complexity
def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
```

---

## সর্বোত্তম অনুশীলনের সারাংশ
### মেমরি ম্যানেজমেন্ট
1. **RAII ব্যবহার করুন**: রিসোর্স অধিগ্রহণ হল সূচনা প্যাটার্ন
2. **প্রসঙ্গ পরিচালক**: সম্পদের জন্য`with`স্টেটমেন্ট ব্যবহার করুন
3. **দুর্বল রেফারেন্স**: ক্যাশে এবং ব্যাক-রেফারেন্সের জন্য
4. **প্রোফাইলিং**: উত্পাদনে নিয়মিত মেমরি প্রোফাইলিং
### সামঞ্জস্য
1. **শেয়ারড স্টেট মিনিমাইজ করুন**: মেসেজ পাসিং পছন্দ করুন
2. **উচ্চ-স্তরের বিমূর্ততা ব্যবহার করুন**: থ্রেড পুল, অ্যাসিঙ্ক/অপেক্ষা করুন
3. **লক অর্ডার**: ধারাবাহিক অর্ডার দিয়ে অচলাবস্থা প্রতিরোধ করুন
4. **একসঙ্গে পরীক্ষা করুন**: স্ট্রেস টেস্ট এবং রেস ডিটেক্টর ব্যবহার করুন
### পারফরম্যান্স
1. **প্রোফাইল প্রথম**: অপ্টিমাইজ করার আগে পরিমাপ করুন
2. **অ্যালগরিদম চয়েস**: উপযুক্ত ডেটা স্ট্রাকচার নির্বাচন করুন
3. **ব্যাচ অপারেশন**: ডাটাবেস/এপিআই-এ রাউন্ড ট্রিপ কমিয়ে দিন
4. **ক্যাশিং**: ব্যয়বহুল গণনা যথাযথভাবে ক্যাশে করুন
---

## সম্পর্কিত বিষয়
- **নিরাপত্তার দুর্বলতা**: নিরাপত্তা-সম্পর্কিত সমস্যার জন্য`security_vulnerabilities.md`দেখুন
- **কোডের গুণমান**: রক্ষণাবেক্ষণের উদ্বেগের জন্য`code_quality_issues.md`দেখুন
- **API ডিজাইন**: সিস্টেম আর্কিটেকচার প্যাটার্নের জন্য`../07_api_system_design/api_system_design.md`দেখুন
- **AI/LLM ব্যর্থতা**: AI-নির্দিষ্ট নির্ভরযোগ্যতার সমস্যাগুলির জন্য`ai_llm_failures.md`দেখুন
---

## অতিরিক্ত সিস্টেম নির্ভরযোগ্যতা নিদর্শন
### সম্পদ নিঃশেষ
**এটি কী:** সীমাহীন বরাদ্দের মাধ্যমে সিস্টেম সংস্থানগুলি (ফাইল হ্যান্ডেল, সংযোগ, মেমরি) হ্রাস করা।
**খারাপ উদাহরণ:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**উত্তম পদ্ধতি:**```python
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = create_database_connection()
    try:
        yield conn
    finally:
        conn.close()

@app.route('/api/data')
def get_data():
    with get_db_connection() as conn:
        return conn.query("SELECT * FROM data")
```

### ক্যাসকেড ব্যর্থতা
**এটি কী:** একটি উপাদানে ব্যর্থতা নির্ভরশীল উপাদানগুলিতে ব্যর্থতাকে ট্রিগার করে।
**খারাপ উদাহরণ:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**উত্তম পদ্ধতি:**```python
from circuitbreaker import circuit

@circuit(failure_threshold=5, recovery_timeout=30)
def process_order(order):
    try:
        inventory_response = check_inventory(
            order.items, 
            timeout=2.0  # Timeout prevents blocking
        )
        payment_response = process_payment(
            order.payment,
            timeout=3.0
        )
        shipping_response = calculate_shipping(
            order.address,
            timeout=1.0
        )
        return combine_responses(...)
    except CircuitBreakerError:
        # Fail fast when service is unhealthy
        return queue_for_later_processing(order)
    except TimeoutError:
        # Graceful degradation
        return partial_response_with_retry(order)
```

### ব্যর্থতার একক পয়েন্ট
**খারাপ উদাহরণ:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**উত্তম পদ্ধতি:**```markdown
Resilient Architecture:
[Users] → [Load Balancer] → [Multiple Web Servers]
                              ↓
                    [Database Primary]
                              ↓
                    [Database Replica] ← [Read Queries]
                    
Features:
- Automatic failover
- Read scaling
- Zero-downtime maintenance
```

---

## মনিটরিং এবং পর্যবেক্ষণের সমস্যা
### স্বাস্থ্য পরীক্ষা অনুপস্থিত
**খারাপ উদাহরণ:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**উত্তম পদ্ধতি:**```python
@app.route('/health')
def health_check():
    checks = {
        'database': check_database(),
        'cache': check_redis(),
        'external_api': check_external_service()
    }
    
    if all(checks.values()):
        return {'status': 'healthy', 'checks': checks}, 200
    else:
        return {'status': 'unhealthy', 'checks': checks}, 503

@app.route('/ready')
def readiness_check():
    # Is this instance ready to receive traffic?
    if is_warmed_up() and dependencies_healthy():
        return {'status': 'ready'}, 200
    return {'status': 'not ready'}, 503
```

### অপর্যাপ্ত লগিং
**খারাপ উদাহরণ:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**উত্তম পদ্ধতি:**```python
import logging
import uuid

def process_payment(payment):
    correlation_id = str(uuid.uuid4())
    
    logging.info(
        f"Processing payment",
        extra={
            'correlation_id': correlation_id,
            'payment_id': payment.id,
            'amount': payment.amount,
            'currency': payment.currency
        }
    )
    
    try:
        result = charge_card(payment)
        logging.info(
            f"Payment successful",
            extra={'correlation_id': correlation_id, 'result': result}
        )
        return result
    except PaymentError as e:
        logging.error(
            f"Payment failed: {str(e)}",
            extra={
                'correlation_id': correlation_id,
                'error_code': e.code,
                'error_details': e.details
            },
            exc_info=True  # Include stack trace
        )
        raise
```

### কোনো মেট্রিক্স সংগ্রহ নেই
**খারাপ উদাহরণ:**```python
# No metrics exposed
def handle_request(request):
    process(request)
    return response

# Operators are blind to:
# - Request rate
# - Error rate  
# - Latency distribution
# - Resource usage
```

**উত্তম পদ্ধতি:**```python
from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter('http_requests_total', 'Total requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency')
ACTIVE_CONNECTIONS = Gauge('active_connections', 'Number of active connections')

def handle_request(request):
    with REQUEST_LATENCY.time():
        ACTIVE_CONNECTIONS.inc()
        try:
            response = process(request)
            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=request.endpoint,
                status=response.status_code
            ).inc()
            return response
        finally:
            ACTIVE_CONNECTIONS.dec()
```

---

## ডিস্ট্রিবিউটেড সিস্টেম চ্যালেঞ্জ
### ঘড়ি তির্যক সমস্যা
**খারাপ উদাহরণ:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**উত্তম পদ্ধতি:**```python
def is_token_valid(token):
    # Use logical timestamps or vector clocks
    # Or include server time in token
    current_time = get_logical_time()
    return token.logical_timestamp > current_time

# Or use distributed tracing with consistent timestamps
from opentelemetry import trace

def validate_token(token):
    span = trace.get_current_span()
    span.set_attribute("token_expiry", token.expires_at.isoformat())
    # Timestamps from trace context, not local clock
```

### নেটওয়ার্ক পার্টিশন হ্যান্ডলিং
**খারাপ উদাহরণ:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**উত্তম পদ্ধতি:**```python
def update_user_preference(user_id, preference):
    # Choose availability or consistency based on use case
    
    # For preferences (AP system - prefer availability):
    try:
        cache.set(user_id, preference)  # Fast, available
        queue_for_async_db_update(user_id, preference)  # Eventually consistent
        return "Preference saved"
    except CacheUnavailable:
        # Degrade gracefully
        return "Unable to save preference, please try again"
    
    # For financial data (CP system - prefer consistency):
    # try:
    #     db.update_with_consensus(user_id, preference)
    #     return "Updated"
    # except ConsensusFailed:
    #     return "Service temporarily unavailable"
```

---

## বিশৃঙ্খলা প্রকৌশল নীতি
### পরীক্ষার ব্যর্থতার পরিস্থিতি
**কী পরীক্ষা করবেন:**
1. **উদাহরণ ব্যর্থতা**: এলোমেলো পড/ভিএম হত্যা করুন
2. **নেটওয়ার্ক সমস্যা**: লেটেন্সি যোগ করুন, প্যাকেট বাদ দিন
3. **সম্পদ ক্লান্তি**: ডিস্ক পূরণ করুন, মেমরি নিষ্কাশন করুন
4. **নির্ভরতা ব্যর্থতা**: মক পরিষেবা বিভ্রাট
5. **ক্লক স্ক্যু**: সার্ভার ঘড়ি ডিসিঙ্ক্রোনাইজ করুন
**উদাহরণ বিশৃঙ্খলা পরীক্ষা:**```yaml
# Chaos Mesh experiment
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: kill-random-pods
spec:
  action: pod-kill
  mode: random
  selector:
    namespaces: ["production"]
    labelSelectors:
      app: my-service
  scheduler:
    cron: "@every 10m"  # Kill pod every 10 minutes
```

### খেলার দিন
সিস্টেমের স্থিতিস্থাপকতা পরীক্ষা করার জন্য নিয়মিত ব্যায়াম:
1. **সূচি**: ত্রৈমাসিক খেলার দিন
2. **স্কোপ**: উৎপাদনের মতো পরিবেশ
3. **পরিস্থিতি**: একাধিক একযোগে ব্যর্থতা
4. **মেট্রিক্স**: সনাক্তকরণের সময়, পুনরুদ্ধারের সময় পরিমাপ করুন
5. **শিক্ষা**: নথিভুক্ত করুন এবং রানবুক উন্নত করুন
---

## সক্ষমতা পরিকল্পনা
### আন্ডার-প্রভিশনিং
**খারাপ উদাহরণ:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**উত্তম পদ্ধতি:**```markdown
Traffic Analysis:
- Average: 1000 rps
- Peak (95th percentile): 2500 rps
- Maximum observed: 4000 rps

Capacity Planning:
- Target capacity: 6000 rps (50% headroom above max)
- Auto-scaling trigger: 70% utilization
- Scale-up speed: 2x per minute
- Buffer instances: Always keep 20% spare capacity
```

### ওভার-প্রভিশনিং বর্জ্য
**খারাপ উদাহরণ:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**উত্তম পদ্ধতি:**```markdown
Right-sizing Strategy:
1. Analyze historical usage patterns
2. Implement auto-scaling based on metrics
3. Use spot/preemptible instances for flexibility
4. Set up cost alerts and budgets
5. Regular capacity reviews

Result:
- Same reliability
- Cost reduced to $15,000/month
- 70% savings
```

---

## ঘটনার প্রতিক্রিয়া সর্বোত্তম অনুশীলন
### অন-কল বার্নআউট প্রতিরোধ
**খারাপ অভ্যাস:**
- প্রতি সপ্তাহে একই ব্যক্তি অন-কল
- কোন বাড়ানোর পথ নেই
- অ-কার্যযোগ্য আইটেমগুলির জন্য সতর্কতা
- ময়নাতদন্ত যা দায়ী করে
**ভাল অভ্যাস:**```markdown
On-Call Rotation:
- Weekly rotation, never back-to-back weeks
- Secondary on-call for support
- Clear escalation procedures
- Alert fatigue reduction (page only for actionable issues)

Post-Incident:
- Blameless post-mortems
- Focus on systemic fixes
- Track action items to completion
- Share learnings organization-wide
```

### রানবুকের গুণমান
**খারাপ রানবুক:**```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**ভাল রানবুক:**```markdown
## Database Slow Query

### Symptoms
- Query latency > 5 seconds
- Connection pool exhaustion
- Application timeouts

### Detection
- Alert: `db_query_latency_p99 > 5s for 5m`
- Dashboard: Database Performance

### Immediate Actions
1. Identify slow queries:
   ```sql
pg_stat_activity থেকে * নির্বাচন করুন 
   যেখানে রাষ্ট্র = 'সক্রিয়' 
   query_start দ্বারা অর্ডার করুন;   ```

2. Check for locks:
   ```sql
সিলেক্ট * ফ্রম pg_locks WHERE granted = false;   ```

3. If specific query identified:
   - Kill query: `SELECT pg_terminate_backend(pid);`
   - Add index if missing

4. If general slowness:
   - Check CPU/memory: `top`, `vmstat`
   - Check disk I/O: `iostat`
   - Consider read replica failover

### Escalation
- If not resolved in 15 min: Page DBA team
- Contact: dba-oncall@example.com, +1-xxx-xxx-xxxx

### Post-Incident
- Create ticket for root cause analysis
- Update runbook with new learnings
```
