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
# ปัญหาความน่าเชื่อถือของระบบ
เอกสารนี้รวบรวมปัญหาด้านความน่าเชื่อถือ รวมถึงหน่วยความจำรั่ว สภาพการแข่งขัน ข้อผิดพลาดในการเขียนโปรแกรมที่เกิดขึ้นพร้อมกัน และความล้มเหลวในการออกแบบระบบ
---

## หน่วยความจำรั่ว
หน่วยความจำรั่วเกิดขึ้นเมื่อโปรแกรมจัดสรรหน่วยความจำแต่ไม่สามารถปล่อยออกเมื่อไม่ต้องการอีกต่อไป ส่งผลให้ปริมาณการใช้หน่วยความจำเพิ่มขึ้นทีละน้อย
### ผู้ฟังเหตุการณ์ที่ถูกลืม
**ตัวอย่างที่ไม่ดี (JavaScript):**```javascript
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

**แนวทางที่ดีกว่า:**```javascript
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

### ทรัพยากรที่ไม่ถูกเปิดเผย
**ตัวอย่างที่ไม่ดี (Python):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**แนวทางที่ดีกว่า:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### การอ้างอิงแบบวงกลม
**ตัวอย่างที่ไม่ดี (Python):**```python
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

**วิธีแก้ไข:** ใช้การอ้างอิงที่ไม่ชัดเจนสำหรับการอ้างอิงด้านหลัง```python
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

## สภาพการแข่งขัน
สภาวะการแข่งขันเกิดขึ้นเมื่อพฤติกรรมของซอฟต์แวร์ขึ้นอยู่กับระยะเวลาที่สัมพันธ์กันของเหตุการณ์ เช่น ลำดับการดำเนินการของเธรด
### ตรวจสอบสภาพการแข่งขันแล้วดำเนินการ
**ตัวอย่างที่ไม่ดี (Python):**```python
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

**สถานการณ์ปัญหา:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**แนวทางที่ดีกว่า:**```python
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

### อ่าน-แก้ไข-เขียนสภาพการแข่งขัน
**ตัวอย่างที่ไม่ดี:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**แนวทางที่ดีกว่า:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### สภาพการแข่งขันการเริ่มต้น Lazy
**ตัวอย่างที่ไม่ดี:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**แนวทางที่ดีกว่า:**```python
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

## การต่อต้านรูปแบบการทำงานพร้อมกัน
### การหยุดชะงัก
**ตัวอย่างที่ไม่ดี:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**การป้องกัน:** ควรซื้อล็อคตามลำดับที่สอดคล้องกันเสมอ```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### ไลฟ์ล็อค
**ตัวอย่างที่ไม่ดี:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### ความอดอยาก
**ตัวอย่างที่ไม่ดี:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**วิธีแก้ไข:** ใช้การกำหนดเวลาที่ยุติธรรมหรือให้ความสำคัญกับการแก่ก่อนวัย
---

## ปัญหาด้านประสิทธิภาพ
### ปัญหาแบบสอบถาม N+1
**ตัวอย่างที่ไม่ดี:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**แนวทางที่ดีกว่า:**```python
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

### ลูปที่ไม่มีประสิทธิภาพ
**ตัวอย่างที่ไม่ดี:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**แนวทางที่ดีกว่า:**```python
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

## สรุปแนวทางปฏิบัติที่ดีที่สุด
### การจัดการหน่วยความจำ
1. **ใช้ RAII**: การได้มาซึ่งทรัพยากรเป็นรูปแบบการเริ่มต้น
2. **Context Managers**: ใช้คำสั่ง`with`สำหรับทรัพยากร
3. **การอ้างอิงที่อ่อนแอ**: สำหรับแคชและการอ้างอิงด้านหลัง
4. **การทำโปรไฟล์**: การทำโปรไฟล์หน่วยความจำตามปกติในการผลิต
### เห็นพ้องต้องกัน
1. **ย่อสถานะที่ใช้ร่วมกันให้เล็กสุด**: ต้องการส่งข้อความ
2. **ใช้นามธรรมระดับสูง**: เธรดพูล, async/await
3. **ล็อคลำดับ**: ป้องกันการหยุดชะงักด้วยการสั่งซื้อที่สอดคล้องกัน
4. **ทดสอบพร้อมกัน**: ใช้การทดสอบความเครียดและเครื่องตรวจจับการแข่งขัน
### ประสิทธิภาพ
1. **โปรไฟล์ต้องมาก่อน**: วัดผลก่อนเพิ่มประสิทธิภาพ
2. **ตัวเลือกอัลกอริทึม**: เลือกโครงสร้างข้อมูลที่เหมาะสม
3. **การดำเนินการเป็นกลุ่ม**: ลดการเดินทางไปกลับไปยังฐานข้อมูล/API
4. **การแคช**: แคชการคำนวณราคาแพงอย่างเหมาะสม
---

## หัวข้อที่เกี่ยวข้อง
- **ช่องโหว่ด้านความปลอดภัย**: ดู`security_vulnerabilities.md`สำหรับปัญหาด้านความปลอดภัย
- **คุณภาพโค้ด**: ดู`code_quality_issues.md`สำหรับข้อกังวลด้านการบำรุงรักษา
- **การออกแบบ API**: ดู`../07_api_system_design/api_system_design.md`สำหรับรูปแบบสถาปัตยกรรมระบบ
- **ความล้มเหลวของ AI/LLM**: ดู`ai_llm_failures.md`สำหรับปัญหาความน่าเชื่อถือเฉพาะของ AI
---

## รูปแบบความน่าเชื่อถือของระบบเพิ่มเติม
### ทรัพยากรหมดไป
**มันคืออะไร:** การทำลายทรัพยากรระบบ (ตัวจัดการไฟล์ การเชื่อมต่อ หน่วยความจำ) ผ่านการจัดสรรที่ไม่มีขอบเขต
**ตัวอย่างที่ไม่ดี:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**แนวทางที่ดีกว่า:**```python
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

### ความล้มเหลวของน้ำตก
**สิ่งนี้คืออะไร:** ความล้มเหลวในส่วนประกอบหนึ่งทำให้เกิดความล้มเหลวในส่วนประกอบที่ต้องพึ่งพา
**ตัวอย่างที่ไม่ดี:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**แนวทางที่ดีกว่า:**```python
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

### จุดเดียวของความล้มเหลว
**ตัวอย่างที่ไม่ดี:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**แนวทางที่ดีกว่า:**```markdown
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

## ปัญหาการตรวจสอบและการสังเกต
### การตรวจสุขภาพที่หายไป
**ตัวอย่างที่ไม่ดี:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**แนวทางที่ดีกว่า:**```python
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

### การบันทึกไม่เพียงพอ
**ตัวอย่างที่ไม่ดี:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**แนวทางที่ดีกว่า:**```python
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

### ไม่มีการรวบรวมเมตริก
**ตัวอย่างที่ไม่ดี:**```python
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

**แนวทางที่ดีกว่า:**```python
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

## ความท้าทายของระบบแบบกระจาย
### ปัญหาการเอียงนาฬิกา
**ตัวอย่างที่ไม่ดี:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**แนวทางที่ดีกว่า:**```python
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

### การจัดการพาร์ติชันเครือข่าย
**ตัวอย่างที่ไม่ดี:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**แนวทางที่ดีกว่า:**```python
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

## หลักวิศวกรรมแห่งความโกลาหล
### สถานการณ์การทดสอบความล้มเหลว
**สิ่งที่ต้องทดสอบ:**
1. **อินสแตนซ์ล้มเหลว**: ฆ่าพ็อด/VM แบบสุ่ม
2. **ปัญหาเครือข่าย**: เพิ่มเวลาแฝง ปล่อยแพ็กเก็ต
3. **ทรัพยากรหมด**: เติมดิสก์ หน่วยความจำหมด
4. **ความล้มเหลวในการพึ่งพา**: บริการจำลองการหยุดทำงาน
5. **การบิดเบือนนาฬิกา**: ยกเลิกการซิงโครไนซ์นาฬิกาเซิร์ฟเวอร์
**ตัวอย่างการทดลองความโกลาหล:**```yaml
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

### วันเกม
การออกกำลังกายเป็นประจำเพื่อทดสอบความยืดหยุ่นของระบบ:
1. **กำหนดการ**: วันแข่งขันรายไตรมาส
2. **ขอบเขต**: สภาพแวดล้อมคล้ายการผลิต
3. **สถานการณ์**: ความล้มเหลวหลายครั้งพร้อมกัน
4. **หน่วยเมตริก**: วัดเวลาในการตรวจจับ เวลาฟื้นตัว
5. **การเรียนรู้**: จัดทำเอกสารและปรับปรุง Runbooks
---

## การวางแผนกำลังการผลิต
### อยู่ระหว่างการจัดเตรียม
**ตัวอย่างที่ไม่ดี:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**แนวทางที่ดีกว่า:**```markdown
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

### ของเสียที่จัดสรรมากเกินไป
**ตัวอย่างที่ไม่ดี:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**แนวทางที่ดีกว่า:**```markdown
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

## แนวทางปฏิบัติที่ดีที่สุดในการตอบสนองต่อเหตุการณ์
### การป้องกันความเหนื่อยล้าขณะโทร
**แนวทางปฏิบัติที่ไม่ดี:**
- คนเดียวกันที่โทรทุกสัปดาห์
- ไม่มีเส้นทางยกระดับ
- การแจ้งเตือนสำหรับรายการที่ไม่สามารถดำเนินการได้
- การชันสูตรพลิกศพที่กำหนดความผิด
**แนวทางปฏิบัติที่ดี:**```markdown
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

### คุณภาพ Runbook
** Runbook ไม่ดี: **```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**รันบุ๊คที่ดี:**```markdown
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
เลือก * จาก pg_stat_activity 
   สถานะ WHERE = 'ใช้งานอยู่' 
   เรียงลำดับตาม query_start;   ```

2. Check for locks:
   ```sql
SELECT * FROM pg_locks โดยที่รับ = false;   ```

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
