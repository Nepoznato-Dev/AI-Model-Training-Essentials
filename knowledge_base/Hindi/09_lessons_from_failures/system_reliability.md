<!--
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

-->
# सिस्टम विश्वसनीयता मुद्दे
यह दस्तावेज़ मेमोरी लीक, दौड़ की स्थिति, समवर्ती प्रोग्रामिंग त्रुटियों और सिस्टम डिज़ाइन विफलताओं सहित विश्वसनीयता के मुद्दों को समेकित करता है।
---

## स्म्रति से रिसाव
मेमोरी लीक तब होता है जब प्रोग्राम मेमोरी आवंटित करते हैं लेकिन जब जरूरत नहीं रह जाती है तो इसे जारी करने में विफल रहते हैं, जिससे धीरे-धीरे मेमोरी खपत में वृद्धि होती है।
### भूले हुए घटना श्रोता
**खराब उदाहरण (जावास्क्रिप्ट):**```javascript
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

**बेहतर दृष्टिकोण:**```javascript
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

### अज्ञात संसाधन
**बुरा उदाहरण (पायथन):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**बेहतर दृष्टिकोण:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### परिपत्र संदर्भ
**बुरा उदाहरण (पायथन):**```python
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

**समाधान:** बैक-रेफरेंस के लिए कमजोर संदर्भों का उपयोग करें```python
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

## दौड़ की स्थिति
रेस की स्थिति तब उत्पन्न होती है जब सॉफ़्टवेयर व्यवहार घटनाओं के सापेक्ष समय पर निर्भर करता है, जैसे थ्रेड निष्पादन क्रम।
### दौड़ की स्थिति की जांच करें फिर कार्य करें
**बुरा उदाहरण (पायथन):**```python
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

**समस्या परिदृश्य:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**बेहतर दृष्टिकोण:**```python
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

### पढ़ें-संशोधित करें-लिखें दौड़ की स्थिति
**खराब उदाहरण:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**बेहतर दृष्टिकोण:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### आलसी आरंभीकरण दौड़ की स्थिति
**खराब उदाहरण:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**बेहतर दृष्टिकोण:**```python
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

## समवर्ती विरोधी पैटर्न
### गतिरोध
**खराब उदाहरण:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**रोकथाम:** ताले हमेशा एक समान क्रम में खरीदें```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### लाइवलॉक
**खराब उदाहरण:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### भुखमरी
**खराब उदाहरण:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**समाधान:** निष्पक्ष शेड्यूलिंग या प्राथमिकता आयु निर्धारण का उपयोग करें
---

## निष्पादन मुद्दे
### एन+1 क्वेरी समस्या
**खराब उदाहरण:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**बेहतर दृष्टिकोण:**```python
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

### अकुशल लूप्स
**खराब उदाहरण:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**बेहतर दृष्टिकोण:**```python
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

## सर्वोत्तम प्रथाओं का सारांश
### मेमोरी प्रबंधन
1. **RAII का उपयोग करें**: संसाधन अधिग्रहण आरंभीकरण पैटर्न है
2. **संदर्भ प्रबंधक**: संसाधनों के लिए`with`कथनों का उपयोग करें
3. **कमजोर संदर्भ**: कैश और बैक-रेफरेंस के लिए
4. **प्रोफाइलिंग**: उत्पादन में नियमित मेमोरी प्रोफाइलिंग
### समवर्ती
1. **साझा स्थिति को न्यूनतम करें**: संदेश भेजने को प्राथमिकता दें
2. **उच्च-स्तरीय एब्स्ट्रैक्शन का उपयोग करें**: थ्रेड पूल, एसिंक/प्रतीक्षा
3. **ऑर्डरिंग को लॉक करें**: लगातार ऑर्डरिंग के साथ गतिरोध को रोकें
4. **समवर्ती परीक्षण करें**: तनाव परीक्षण और रेस डिटेक्टरों का उपयोग करें
### प्रदर्शन
1. **प्रोफ़ाइल प्रथम**: अनुकूलन से पहले मापें
2. **एल्गोरिदम विकल्प**: उपयुक्त डेटा संरचनाओं का चयन करें
3. **बैच संचालन**: डेटाबेस/एपीआई के लिए राउंड ट्रिप कम करें
4. **कैशिंग**: महंगी गणनाओं को उचित रूप से कैश करें
---

## संबंधित विषय
- **सुरक्षा कमजोरियाँ**: सुरक्षा संबंधी समस्याओं के लिए`security_vulnerabilities.md`देखें
- **कोड गुणवत्ता**: रखरखाव संबंधी चिंताओं के लिए`code_quality_issues.md`देखें
- **एपीआई डिज़ाइन**: सिस्टम आर्किटेक्चर पैटर्न के लिए`../07_api_system_design/api_system_design.md`देखें
- **एआई/एलएलएम विफलताएं**: एआई-विशिष्ट विश्वसनीयता मुद्दों के लिए`ai_llm_failures.md`देखें
---

## अतिरिक्त सिस्टम विश्वसनीयता पैटर्न
### संसाधन की थकावट
**यह क्या है:** असीमित आवंटन के माध्यम से सिस्टम संसाधनों (फ़ाइल हैंडल, कनेक्शन, मेमोरी) को कम करना।
**खराब उदाहरण:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**बेहतर दृष्टिकोण:**```python
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

### कैस्केड विफलताएँ
**यह क्या है:** एक घटक में विफलता आश्रित घटकों में विफलता को ट्रिगर करती है।
**खराब उदाहरण:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**बेहतर दृष्टिकोण:**```python
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

### विफलता के एकल बिंदु
**खराब उदाहरण:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**बेहतर दृष्टिकोण:**```markdown
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

## निगरानी और अवलोकन संबंधी मुद्दे
### स्वास्थ्य जांच का अभाव
**खराब उदाहरण:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**बेहतर दृष्टिकोण:**```python
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

### अपर्याप्त लॉगिंग
**खराब उदाहरण:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**बेहतर दृष्टिकोण:**```python
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

### कोई मेट्रिक्स संग्रह नहीं
**खराब उदाहरण:**```python
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

**बेहतर दृष्टिकोण:**```python
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

## वितरित सिस्टम चुनौतियाँ
### घड़ी की तिरछी समस्याएँ
**खराब उदाहरण:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**बेहतर दृष्टिकोण:**```python
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

### नेटवर्क विभाजन प्रबंधन
**खराब उदाहरण:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**बेहतर दृष्टिकोण:**```python
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

## कैओस इंजीनियरिंग सिद्धांत
### परीक्षण विफलता परिदृश्य
**क्या परीक्षण करें:**
1. **इंस्टेंस विफलता**: यादृच्छिक पॉड्स/वीएम को मारें
2. **नेटवर्क समस्याएँ**: विलंबता जोड़ें, पैकेट छोड़ें
3. **संसाधन समाप्ति**: डिस्क भरें, मेमोरी समाप्त करें
4. **निर्भरता विफलताएं**: मॉक सेवा में रुकावट
5. **घड़ी तिरछा**: सर्वर घड़ियों को डीसिंक्रनाइज़ करें
**उदाहरण अराजकता प्रयोग:**```yaml
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

### खेल के दिन
सिस्टम लचीलेपन का परीक्षण करने के लिए नियमित व्यायाम:
1. **अनुसूची**: त्रैमासिक खेल दिवस
2. **दायरा**: उत्पादन जैसा वातावरण
3. **परिदृश्य**: एक साथ अनेक विफलताएँ
4. **मेट्रिक्स**: पता लगाने का समय, पुनर्प्राप्ति समय मापें
5. **सीखें**: रनबुक का दस्तावेज़ीकरण करें और उसमें सुधार करें
---

## क्षमता की योजना बनाना
### कम प्रावधान
**खराब उदाहरण:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**बेहतर दृष्टिकोण:**```markdown
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

### अति-प्रावधान बर्बादी
**खराब उदाहरण:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**बेहतर दृष्टिकोण:**```markdown
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

## घटना प्रतिक्रिया सर्वोत्तम अभ्यास
### ऑन-कॉल बर्नआउट रोकथाम
**बुरी प्रथाएँ:**
- हर सप्ताह एक ही व्यक्ति ऑन-कॉल
- कोई वृद्धि पथ नहीं
- कार्रवाई न करने योग्य वस्तुओं के लिए अलर्ट
- पोस्टमार्टम जो दोष निर्दिष्ट करते हैं
**अच्छे आचरण:**```markdown
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

### रनबुक गुणवत्ता
**खराब रनबुक:**```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**अच्छी रनबुक:**```markdown
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
pg_stat_activity से * चुनें 
   जहां स्थिति = 'सक्रिय' 
   query_start द्वारा ऑर्डर करें;   ```

2. Check for locks:
   ```sql
चयन करें * pg_locks से जहां अनुमति दी गई = गलत;   ```

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
