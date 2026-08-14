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
# مسائل مربوط به قابلیت اطمینان سیستم
این سند مسائل مربوط به قابلیت اطمینان از جمله نشت حافظه، شرایط مسابقه، خطاهای برنامه‌نویسی همزمان و خرابی‌های طراحی سیستم را ادغام می‌کند.
---

## نشت حافظه
نشت حافظه زمانی اتفاق می‌افتد که برنامه‌ها حافظه را تخصیص می‌دهند، اما در زمانی که دیگر مورد نیاز نیست، آن را آزاد نمی‌کنند و باعث رشد تدریجی مصرف حافظه می‌شود.
### شنوندگان رویداد فراموش شده
**مثال بد (جاوا اسکریپت):**```javascript
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

**رویکرد بهتر:**```javascript
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

### منابع بسته نشده
**نمونه بد (پایتون):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**رویکرد بهتر:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### مراجع دایره ای
**نمونه بد (پایتون):**```python
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

**راه حل:** از مراجع ضعیف برای ارجاعات برگشتی استفاده کنید```python
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

## شرایط مسابقه
شرایط مسابقه زمانی رخ می‌دهد که رفتار نرم‌افزار به زمان‌بندی نسبی رویدادها، مانند ترتیب اجرای رشته، بستگی داشته باشد.
### شرایط مسابقه را بررسی کنید سپس عمل کنید
**نمونه بد (پایتون):**```python
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

**سناریوی مشکل:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**رویکرد بهتر:**```python
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

### شرایط مسابقه خواندن-تغییر-نوشتن
**مثال بد:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**رویکرد بهتر:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### شرایط مسابقه اولیه سازی تنبل
**مثال بد:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**رویکرد بهتر:**```python
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

## ضد الگوهای همزمان
### بن بست
**مثال بد:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**پیشگیری:** همیشه قفل ها را به ترتیب ثابت تهیه کنید```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### Livelock
**مثال بد:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### گرسنگی
**مثال بد:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**راه حل:** از برنامه ریزی منصفانه یا اولویت پیری استفاده کنید
---

## مسائل مربوط به عملکرد
### مشکل پرس و جو N+1
**مثال بد:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**رویکرد بهتر:**```python
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

### حلقه های ناکارآمد
**مثال بد:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**رویکرد بهتر:**```python
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

## خلاصه بهترین شیوه ها
### مدیریت حافظه
1. **از RAII** استفاده کنید: اکتساب منابع الگوی اولیه سازی است
2. **مدیران زمینه**: از عبارات`with`برای منابع استفاده کنید
3. **ارجاع ضعیف**: برای حافظه پنهان و مراجع پشتیبان
4. **پروفایلینگ**: پروفایل حافظه منظم در تولید
### همزمانی
1. **به حداقل رساندن وضعیت مشترک **: ارسال پیام را ترجیح دهید
2. **استفاده از انتزاعات سطح بالا**: Thread pools، async/wait
3. ** ترتیب قفل **: با نظم دهی مداوم از بن بست جلوگیری کنید
4. **تست همزمان**: از تست استرس و آشکارسازهای مسابقه استفاده کنید
### عملکرد
1. **پروفایل اول **: قبل از بهینه سازی اندازه گیری کنید
2. **انتخاب الگوریتم**: ساختارهای داده مناسب را انتخاب کنید
3. **عملیات دسته ای**: سفرهای رفت و برگشت به پایگاه های داده/API ها را کاهش دهید
4. **Caching**: محاسبات گران قیمت را به طور مناسب ذخیره کنید
---

## موضوعات مرتبط
- **آسیب پذیری های امنیتی**: برای مسائل مربوط به امنیت به`security_vulnerabilities.md`مراجعه کنید
- **کیفیت کد**: برای نگرانی های مربوط به نگهداری به`code_quality_issues.md`مراجعه کنید
- **طراحی API**: برای الگوهای معماری سیستم به`../07_api_system_design/api_system_design.md`مراجعه کنید
- **مشکلات AI/LLM**: برای مسائل مربوط به قابلیت اطمینان ویژه هوش مصنوعی به`ai_llm_failures.md`مراجعه کنید
---

## الگوهای قابلیت اطمینان اضافی سیستم
### فرسودگی منابع
**چیست:** تخلیه منابع سیستم (دسته فایل، اتصالات، حافظه) از طریق تخصیص نامحدود.
**مثال بد:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**رویکرد بهتر:**```python
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

### شکست های آبشاری
**چیست:** خرابی در یک جزء باعث ایجاد خرابی در اجزای وابسته می شود.
**مثال بد:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**رویکرد بهتر:**```python
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

### تنها نقاط شکست
**مثال بد:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**رویکرد بهتر:**```markdown
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

## مسائل نظارت و مشاهده
### چک های بهداشتی از دست رفته
**مثال بد:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**رویکرد بهتر:**```python
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

### ثبت نام کافی
**مثال بد:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**رویکرد بهتر:**```python
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

### بدون مجموعه معیارها
**مثال بد:**```python
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

**رویکرد بهتر:**```python
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

## چالش های سیستم توزیع شده
### مشکلات انحراف ساعت
**مثال بد:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**رویکرد بهتر:**```python
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

### مدیریت پارتیشن شبکه
**مثال بد:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**رویکرد بهتر:**```python
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

## اصول مهندسی آشوب
### سناریوهای شکست تست
**چه چیزی را تست کنیم:**
1. ** خرابی های نمونه **: غلاف ها/ ماشین های مجازی تصادفی را بکشید
2. **مشکلات شبکه**: تأخیر اضافه کنید، بسته ها را رها کنید
3. **استخراج منابع**: دیسک را پر کنید، حافظه اگزوز را پر کنید
4. ** خرابی وابستگی **: قطع سرویس ساختگی
5. ** انحراف ساعت **: همگام سازی ساعت های سرور
**نمونه آزمایش آشوب:**```yaml
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

### روزهای بازی
تمرینات منظم برای آزمایش انعطاف پذیری سیستم:
1. **برنامه**: روزهای بازی سه ماهه
2. **حوزه**: محیطی شبیه تولید
3. **سناریوها**: چندین شکست همزمان
4. ** معیارها **: اندازه گیری زمان تشخیص، زمان بازیابی
5. **یادگیری**: مستندسازی و بهبود runbookها
---

## برنامه ریزی ظرفیت
### کمبود تامین
**مثال بد:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**رویکرد بهتر:**```markdown
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

### تامین بیش از حد زباله
**مثال بد:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**رویکرد بهتر:**```markdown
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

## بهترین شیوه های واکنش به حادثه
### پیشگیری از فرسودگی حین تماس
**روش های بد:**
- هر هفته همان فرد در حال تماس است
- بدون مسیر تشدید
- هشدار برای موارد غیر قابل عمل
- کالبد شکافی هایی که سرزنش می کنند
**روش های خوب:**```markdown
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

### کیفیت Runbook
**رابنامه بد:**```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**رانبوک خوب:**```markdown
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
SELECT * FROM pg_stat_activity 
   وضعیت WHERE = "فعال" 
   سفارش با query_start.   ```

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
