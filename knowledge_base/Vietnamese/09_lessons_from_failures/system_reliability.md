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
# Vấn đề về độ tin cậy của hệ thống
Tài liệu này tổng hợp các vấn đề về độ tin cậy bao gồm rò rỉ bộ nhớ, tình trạng tương tranh, lỗi lập trình đồng thời và lỗi thiết kế hệ thống.
---

## Rò rỉ bộ nhớ
Rò rỉ bộ nhớ xảy ra khi các chương trình phân bổ bộ nhớ nhưng không giải phóng bộ nhớ khi không còn cần thiết, khiến mức tiêu thụ bộ nhớ tăng dần.
### Trình xử lý sự kiện bị lãng quên
**Ví dụ xấu (JavaScript):**```javascript
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

**Cách tiếp cận tốt hơn:**```javascript
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

### Tài nguyên không được tiết lộ
**Ví dụ xấu (Python):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**Cách tiếp cận tốt hơn:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### Tài liệu tham khảo vòng tròn
**Ví dụ xấu (Python):**```python
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

**Giải pháp:** Sử dụng tài liệu tham khảo yếu để tham khảo ngược```python
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

## Điều kiện cuộc đua
Điều kiện cạnh tranh xảy ra khi hành vi của phần mềm phụ thuộc vào thời gian tương đối của các sự kiện, chẳng hạn như thứ tự thực hiện luồng.
### Điều kiện cuộc đua kiểm tra rồi hành động
**Ví dụ xấu (Python):**```python
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

**Tình huống sự cố:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**Cách tiếp cận tốt hơn:**```python
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

### Điều kiện chạy đọc-sửa-ghi
**Ví dụ tồi:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**Cách tiếp cận tốt hơn:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### Điều kiện chạy đua khởi tạo lười biếng
**Ví dụ tồi:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**Cách tiếp cận tốt hơn:**```python
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

## Mẫu chống đồng thời
###Bế tắc
**Ví dụ tồi:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**Phòng ngừa:** Luôn lấy khóa theo thứ tự nhất quán```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### Khóa động
**Ví dụ tồi:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### Đói
**Ví dụ tồi:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**Giải pháp:** Sử dụng lịch trình công bằng hoặc thời hạn ưu tiên
---

## Vấn đề về hiệu suất
### Vấn đề truy vấn N+1
**Ví dụ tồi:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**Cách tiếp cận tốt hơn:**```python
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

### Vòng lặp không hiệu quả
**Ví dụ tồi:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**Cách tiếp cận tốt hơn:**```python
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

## Tóm tắt các phương pháp hay nhất
### Quản lý bộ nhớ
1. **Sử dụng RAII**: Mẫu khởi tạo thu thập tài nguyên
2. **Trình quản lý bối cảnh**: Sử dụng câu lệnh`with`cho tài nguyên
3. **Tham chiếu yếu**: Dành cho bộ nhớ đệm và tham chiếu ngược
4. **Lập hồ sơ**: Lập hồ sơ bộ nhớ thông thường trong sản xuất
### Đồng thời
1. **Giảm thiểu trạng thái chia sẻ**: Ưu tiên chuyển tin nhắn
2. **Sử dụng tính trừu tượng cấp cao**: Nhóm luồng, không đồng bộ/đang chờ
3. **Khóa thứ tự**: Ngăn chặn bế tắc với thứ tự nhất quán
4. **Kiểm tra đồng thời**: Sử dụng các bài kiểm tra căng thẳng và công cụ phát hiện chủng tộc
### Hiệu suất
1. **Hồ sơ đầu tiên**: Đo lường trước khi tối ưu hóa
2. **Lựa chọn thuật toán**: Chọn cấu trúc dữ liệu phù hợp
3. **Hoạt động hàng loạt**: Giảm các chuyến đi khứ hồi tới cơ sở dữ liệu/API
4. **Bộ nhớ đệm**: Lưu vào bộ nhớ đệm các phép tính tốn kém một cách thích hợp
---

## Chủ đề liên quan
- **Lỗ hổng bảo mật**: Xem`security_vulnerabilities.md`để biết các vấn đề liên quan đến bảo mật
- **Chất lượng mã**: Xem`code_quality_issues.md`để biết các vấn đề về khả năng bảo trì
- **Thiết kế API**: Xem`../07_api_system_design/api_system_design.md`để biết các mẫu kiến trúc hệ thống
- **Lỗi AI/LLM**: Xem`ai_llm_failures.md`để biết các vấn đề về độ tin cậy dành riêng cho AI
---

## Các mẫu độ tin cậy của hệ thống bổ sung
### Cạn kiệt tài nguyên
**Nó là gì:** Làm cạn kiệt tài nguyên hệ thống (xử lý tệp, kết nối, bộ nhớ) thông qua phân bổ không giới hạn.
**Ví dụ tồi:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**Cách tiếp cận tốt hơn:**```python
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

### Thất bại xếp tầng
**Nó là gì:** Lỗi ở một thành phần sẽ gây ra lỗi ở các thành phần phụ thuộc.
**Ví dụ tồi:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**Cách tiếp cận tốt hơn:**```python
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

### Điểm thất bại duy nhất
**Ví dụ tồi:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**Cách tiếp cận tốt hơn:**```markdown
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

## Vấn đề về giám sát và quan sát
### Thiếu kiểm tra sức khỏe
**Ví dụ tồi:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**Cách tiếp cận tốt hơn:**```python
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

### Ghi nhật ký không đầy đủ
**Ví dụ tồi:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**Cách tiếp cận tốt hơn:**```python
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

### Không có bộ sưu tập số liệu
**Ví dụ tồi:**```python
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

**Cách tiếp cận tốt hơn:**```python
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

## Những thách thức của hệ thống phân tán
### Vấn đề về độ lệch đồng hồ
**Ví dụ tồi:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**Cách tiếp cận tốt hơn:**```python
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

### Xử lý phân vùng mạng
**Ví dụ tồi:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**Cách tiếp cận tốt hơn:**```python
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

## Nguyên tắc kỹ thuật hỗn loạn
### Các tình huống kiểm thử thất bại
**Nội dung cần kiểm tra:**
1. **Lỗi phiên bản**: Tiêu diệt các nhóm/VM ngẫu nhiên
2. **Sự cố mạng**: Thêm độ trễ, bỏ gói
3. **Cạn kiệt tài nguyên**: Đổ đầy đĩa, cạn kiệt bộ nhớ
4. **Lỗi phụ thuộc**: Dịch vụ giả ngừng hoạt động
5. **Đồng hồ lệch**: Giải đồng bộ đồng hồ máy chủ
**Ví dụ về thí nghiệm hỗn loạn:**```yaml
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

### Ngày thi đấu
Các bài tập thường xuyên để kiểm tra khả năng phục hồi của hệ thống:
1. **Lịch thi đấu**: Ngày thi đấu hàng quý
2. **Phạm vi**: Môi trường giống như sản xuất
3. **Kịch bản**: Nhiều lỗi xảy ra đồng thời
4. **Số liệu**: Đo thời gian phát hiện, thời gian phục hồi
5. **Học tập**: Lập tài liệu và cải tiến sổ tay chạy
---

## Lập kế hoạch năng lực
### Thiếu cấp phép
**Ví dụ tồi:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**Cách tiếp cận tốt hơn:**```markdown
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

### Lãng phí cung cấp quá mức
**Ví dụ tồi:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**Cách tiếp cận tốt hơn:**```markdown
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

## Các phương pháp ứng phó sự cố tốt nhất
### Phòng chống kiệt sức khi gọi điện
**Thực tiễn xấu:**
- Cùng một người trực điện thoại hàng tuần
- Không có đường dẫn leo thang
- Cảnh báo cho các mục không thể hành động
- Khám nghiệm tử thi gán trách nhiệm
**Các phương pháp hay:**```markdown
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

### Chất lượng sách chạy
**Cuốn sách tồi:**```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**Cuốn sách hay:**```markdown
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
CHỌN * TỪ pg_stat_activity 
   Trạng thái WHERE = 'hoạt động' 
   ĐẶT HÀNG THEO query_start;   ```

2. Check for locks:
   ```sql
CHỌN * TỪ pg_locks WHERE được cấp = false;   ```

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
