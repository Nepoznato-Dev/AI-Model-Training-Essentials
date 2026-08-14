---
# Metadata
title: "System Reliability Issues"
description: "System failures and reliability patterns"
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

# Mga Isyu sa Pagiging Maaasahan ng System
Pinagsasama-sama ng dokumentong ito ang mga isyu sa pagiging maaasahan kabilang ang mga pagtagas ng memorya, kundisyon ng lahi, kasabay na mga error sa programming, at mga pagkabigo sa disenyo ng system.
---

## Memory Leaks
Nangyayari ang mga pagtagas ng memorya kapag ang mga programa ay naglalaan ng memorya ngunit nabigo itong ilabas kapag hindi na kailangan, na nagiging sanhi ng unti-unting paglago ng pagkonsumo ng memorya.
### Mga Nakalimutang Tagapakinig ng Kaganapan
**Masamang Halimbawa (JavaScript):**```javascript
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

**Mas mahusay na Diskarte:**```javascript
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

### Mga Hindi Saradong Mapagkukunan
**Masamang Halimbawa (Python):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**Mas mahusay na Diskarte:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### Mga Pabilog na Sanggunian
**Masamang Halimbawa (Python):**```python
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

**Solusyon:** Gumamit ng mahihinang reference para sa back-reference```python
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

## Mga Kundisyon ng Lahi
Nagaganap ang mga kundisyon ng lahi kapag ang pag-uugali ng software ay nakasalalay sa kaugnay na timing ng mga kaganapan, gaya ng pagkakasunud-sunod ng pagpapatupad ng thread.
### Suriin-Pagkatapos-Act Race Kundisyon
**Masamang Halimbawa (Python):**```python
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

**Senaryo ng Problema:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**Mas mahusay na Diskarte:**```python
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

### Read-Modify-Write Race Condition
**Masama Halimbawa:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**Mas mahusay na Diskarte:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### Kundisyon ng Lazy Initialization Race
**Masama Halimbawa:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**Mas mahusay na Diskarte:**```python
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

## Concurrency Anti-Pattern
### Deadlock
**Masama Halimbawa:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**Pag-iwas:** Palaging kumuha ng mga kandado sa pare-parehong pagkakasunud-sunod```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### Livelock
**Masama Halimbawa:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### Pagkagutom
**Masama Halimbawa:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**Solusyon:** Gumamit ng patas na pag-iiskedyul o priyoridad na pagtanda
---

## Mga Isyu sa Pagganap
### N+1 na Problema sa Query
**Masama Halimbawa:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**Mas mahusay na Diskarte:**```python
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

### Hindi Mahusay na Mga Loop
**Masama Halimbawa:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**Mas mahusay na Diskarte:**```python
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

## Buod ng Pinakamahuhusay na Kasanayan
### Pamamahala ng Memory
1. **Gamitin ang RAII**: Ang Pagkuha ng Resource ay Pattern ng Initialization
2. **Mga Tagapamahala ng Konteksto**: Gumamit ng mga pahayag ng`with`para sa mga mapagkukunan
3. **Mahinang Mga Sanggunian**: Para sa mga cache at back-reference
4. **Profiling**: Regular na memory profiling sa produksyon
### Kasabay
1. **I-minimize ang Nakabahaging Estado**: Mas gusto ang pagpasa ng mensahe
2. **Gumamit ng High-Level Abstractions**: Mga thread pool, async/naghihintay
3. **Lock Ordering**: Pigilan ang mga deadlock na may pare-parehong pag-order
4. **Test Concurrently**: Gumamit ng mga stress test at race detector
### Pagganap
1. **Profile Una**: Sukatin bago mag-optimize
2. **Algorithm Choice**: Pumili ng mga naaangkop na istruktura ng data
3. **Batch Operations**: Bawasan ang mga round trip sa mga database/API
4. **Caching**: I-cache ang mga mamahaling computations nang naaangkop
---

## Mga Kaugnay na Paksa
- **Mga Kahinaan sa Seguridad**: Tingnan ang`security_vulnerabilities.md`para sa mga isyung nauugnay sa seguridad
- **Code Quality**: Tingnan ang`code_quality_issues.md`para sa mga alalahanin sa maintainability
- **Disenyo ng API**: Tingnan ang`../07_api_system_design/api_system_design.md`para sa mga pattern ng arkitektura ng system
- **AI/LLM Failures**: Tingnan ang`ai_llm_failures.md`para sa mga isyu sa pagiging maaasahan na partikular sa AI
---

## Karagdagang Mga Pattern ng Pagkakaaasahan ng System
### Pagkaubos ng Mapagkukunan
**Ano Ito:** Nauubos ang mga mapagkukunan ng system (mga hawakan ng file, mga koneksyon, memorya) sa pamamagitan ng walang hangganang paglalaan.
**Masama Halimbawa:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**Mas mahusay na Diskarte:**```python
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

### Mga Pagkabigo sa Cascade
**Ano Ito:** Ang pagkabigo sa isang bahagi ay nagpapalitaw ng mga pagkabigo sa mga umaasang bahagi.
**Masama Halimbawa:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**Mas mahusay na Diskarte:**```python
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

### Mga Isang Punto ng Pagkabigo
**Masama Halimbawa:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**Mas mahusay na Diskarte:**```markdown
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

## Mga Isyu sa Pagsubaybay at Pagmamasid
### Nawawalang Mga Pagsusuri sa Kalusugan
**Masama Halimbawa:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**Mas mahusay na Diskarte:**```python
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

### Hindi Sapat na Pag-log
**Masama Halimbawa:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**Mas mahusay na Diskarte:**```python
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

### Walang Koleksyon ng Sukatan
**Masama Halimbawa:**```python
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

**Mas mahusay na Diskarte:**```python
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

## Mga Hamon sa Distributed System
### Mga Isyu sa Clock Skew
**Masama Halimbawa:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**Mas mahusay na Diskarte:**```python
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

### Paghawak ng Network Partition
**Masama Halimbawa:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**Mas mahusay na Diskarte:**```python
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

## Chaos Engineering Principles
### Mga Sitwasyon ng Pagkabigo sa Pagsubok
**Ano ang Susubukan:**
1. **Mga pagkabigo ng instance**: Patayin ang mga random na pod/VM
2. **Mga isyu sa network**: Magdagdag ng latency, mag-drop ng mga packet
3. **Resource exhaustion**: Fill disk, exhaust memory
4. **Mga pagkabigo sa dependency**: Mga kunwaring pagkawala ng serbisyo
5. **Clock skew**: I-desynchronize ang mga orasan ng server
**Halimbawa ng Chaos Experiment:**```yaml
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

### Mga Araw ng Laro
Mga regular na ehersisyo upang subukan ang katatagan ng system:
1. **Iskedyul**: Mga quarterly na araw ng laro
2. **Saklaw**: Kapaligiran na parang produksyon
3. **Mga Sitwasyon**: Maramihang sabay-sabay na pagkabigo
4. **Mga Sukatan**: Sukatin ang oras ng pagtuklas, oras ng pagbawi
5. **Mga Natutunan**: Idokumento at pagbutihin ang mga runbook
---

## Pagpaplano ng Kapasidad
### Under-Provisioning
**Masama Halimbawa:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**Mas mahusay na Diskarte:**```markdown
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

### Over-Provisioning Basura
**Masama Halimbawa:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**Mas mahusay na Diskarte:**```markdown
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

## Pinakamahuhusay na Kasanayan sa Pagtugon sa Insidente
### On-Call Burnout Prevention
**Masasamang Gawi:**
- Parehong taong on-call bawat linggo
- Walang escalation path
- Mga alerto para sa mga item na hindi naaaksyunan
- Mga post-mortem na nagbibigay ng kasalanan
**Magandang Kasanayan:**```markdown
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

### Kalidad ng Runbook
**Masama Runbook:**```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**Magandang Runbook:**```markdown
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
PUMILI * MULA sa pg_stat_activity 
   WHERE estado = 'aktibo' 
   ORDER NG query_start;   ```

2. Check for locks:
   ```sql
SELECT * FROM pg_locks WHERE granted = false;   ```

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
