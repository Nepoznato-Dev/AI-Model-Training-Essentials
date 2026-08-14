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
# 시스템 안정성 문제
이 문서에는 메모리 누수, 경쟁 조건, 동시 프로그래밍 오류 및 시스템 설계 오류를 포함한 안정성 문제가 통합되어 있습니다.
---

## 메모리 누수
메모리 누수는 프로그램이 메모리를 할당했지만 더 이상 필요하지 않을 때 해제하지 못해 점진적인 메모리 소비 증가를 초래할 때 발생합니다.
### 잊어버린 이벤트 리스너
**나쁜 예(자바스크립트):**```javascript
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

**더 나은 접근 방식:**```javascript
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

### 닫히지 않은 리소스
**나쁜 예(Python):**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        f = open(path, 'r')  # Never closed!
        content = f.read()
        results.append(process(content))
        # File handle leaked
    return results
```

**더 나은 접근 방식:**```python
def process_files(file_paths):
    results = []
    for path in file_paths:
        with open(path, 'r') as f:  # Automatically closed
            content = f.read()
            results.append(process(content))
    return results
```

### 순환 참조
**나쁜 예(Python):**```python
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

**해결책:** 역참조에 약한 참조를 사용하세요.```python
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

## 경쟁 조건
경쟁 조건은 소프트웨어 동작이 스레드 실행 순서와 같은 이벤트의 상대적 타이밍에 따라 달라질 때 발생합니다.
### 확인 후 실행 경쟁 조건
**나쁜 예(Python):**```python
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

**문제 시나리오:**```
Initial balance: $100
Thread A: withdraw($80) - checks balance (100 >= 80 ✓)
Thread B: withdraw($50) - checks balance (100 >= 50 ✓)
Thread A: withdraws $80 (balance = $20)
Thread B: withdraws $50 (balance = -$30)  # OVERDRAFT!
```

**더 나은 접근 방식:**```python
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

### 읽기-수정-쓰기 경쟁 조건
**나쁜 예:**```python
# VULNERABLE: Counter increment is not atomic
counter = 0

def increment():
    global counter
    temp = counter      # Read
    temp = temp + 1     # Modify
    counter = temp      # Write

# Multiple threads calling increment() will lose updates
```

**더 나은 접근 방식:**```python
from threading import Lock

counter = 0
counter_lock = Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1  # Atomic operation
```

### 지연 초기화 경쟁 조건
**나쁜 예:**```python
# VULNERABLE: Double-checked locking without proper synchronization
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:  # First check (unlocked)
            cls._instance = cls()   # RACE: Multiple threads can create instances
        return cls._instance
```

**더 나은 접근 방식:**```python
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

## 동시성 안티 패턴
### 교착상태
**나쁜 예:**```python
# Thread 1:                    # Thread 2:
lock_a.acquire()               lock_b.acquire()
lock_b.acquire()  # WAIT       lock_a.acquire()  # WAIT
# DEADLOCK - both threads waiting forever
```

**예방:** 항상 일관된 순서로 잠금을 획득하세요.```python
# Both threads:
lock_a.acquire()
lock_b.acquire()
# ... critical section ...
lock_b.release()
lock_a.release()
```

### 라이브록
**나쁜 예:**```python
# Two threads trying to be polite
while task_not_complete:
    if other_thread_working:
        yield()  # Let other thread go first
    else:
        start_working()
    
    # Both threads keep yielding to each other
    # No progress is made
```

### 기아
**나쁜 예:**```python
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

**해결책:** 공정한 일정 관리 또는 우선순위 에이징을 사용하세요.
---

## 성능 문제
### N+1 쿼리 문제
**나쁜 예:**```python
# Fetch all users
users = db.query("SELECT * FROM users")

# N+1 queries: one query per user to get their orders
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    user.orders = orders
```

**더 나은 접근 방식:**```python
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

### 비효율적인 루프
**나쁜 예:**```python
# O(n²) complexity
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates
```

**더 나은 접근 방식:**```python
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

## 모범 사례 요약
### 메모리 관리
1. **RAII 사용**: 리소스 획득이 초기화 패턴입니다.
2. **컨텍스트 관리자**: 리소스에 대해`with`문을 사용합니다.
3. **약한 참조**: 캐시 및 역참조용
4. **프로파일링**: 프로덕션에서 일반 메모리 프로파일링
### 동시성
1. **공유 상태 최소화**: 메시지 전달을 선호합니다.
2. **고수준 추상화 사용**: 스레드 풀, 비동기/대기
3. **잠금 순서**: 일관된 순서로 교착 상태를 방지합니다.
4. **동시 테스트**: 스트레스 테스트 및 경쟁 감지기 사용
### 성능
1. **프로필 우선**: 최적화 전 측정
2. **알고리즘 선택**: 적절한 데이터 구조 선택
3. **일괄 작업**: 데이터베이스/API에 대한 왕복 횟수 감소
4. **캐싱**: 비용이 많이 드는 계산을 적절하게 캐시합니다.
---

## 관련 주제
- **보안 취약점**: 보안 관련 문제는 `security_vulnerabilities.md`를 참조하세요.
- **코드 품질**: 유지 관리 문제는 `code_quality_issues.md`를 참조하세요.
- **API 디자인**: 시스템 아키텍처 패턴은 `../07_api_system_design/api_system_design.md`를 참조하세요.
- **AI/LLM 오류**: AI 관련 안정성 문제는 `ai_llm_failures.md`를 참조하세요.
---

## 추가 시스템 안정성 패턴
### 자원 고갈
**정의:** 무제한 할당을 통해 시스템 리소스(파일 핸들, 연결, 메모리)를 고갈시킵니다.
**나쁜 예:**```python
# Unbounded connection creation
@app.route('/api/data')
def get_data():
    conn = create_database_connection()  # Never closed!
    return conn.query("SELECT * FROM data")
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

**더 나은 접근 방식:**```python
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

### 계단식 실패
**정의:** 한 구성 요소의 오류로 인해 종속 구성 요소의 오류가 발생합니다.
**나쁜 예:**```python
def process_order(order):
    # No timeout, no circuit breaker
    inventory_response = check_inventory(order.items)
    payment_response = process_payment(order.payment)
    shipping_response = calculate_shipping(order.address)
    
    # If any service is slow, this blocks indefinitely
    # All threads eventually blocked = system down
```

**더 나은 접근 방식:**```python
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

### 단일 실패 지점
**나쁜 예:**```markdown
Architecture:
[Users] → [Web Server] → [Single Database]

Problems:
- Database failure = complete outage
- No redundancy
- Maintenance requires downtime
```

**더 나은 접근 방식:**```markdown
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

## 모니터링 및 관찰 가능성 문제
### 상태 확인 누락
**나쁜 예:**```python
# No health check endpoint
app.run()

# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

**더 나은 접근 방식:**```python
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

### 불충분한 로깅
**나쁜 예:**```python
def process_payment(payment):
    try:
        result = charge_card(payment)
        return result
    except Exception as e:
        print("Error occurred")  # No context!
        return None
```

**더 나은 접근 방식:**```python
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

### 측정항목 수집 없음
**나쁜 예:**```python
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

**더 나은 접근 방식:**```python
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

## 분산 시스템의 과제
### 시계 오차 문제
**나쁜 예:**```python
# Assuming synchronized clocks across servers
def is_token_valid(token):
    return token.expires_at > datetime.now()  # Which server's now?

# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
```

**더 나은 접근 방식:**```python
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

### 네트워크 파티션 처리
**나쁜 예:**```python
# Assumes network is always reliable
def update_user_preference(user_id, preference):
    db.update(user_id, preference)  # Blocks if DB unreachable
    cache.set(user_id, preference)  # What if cache is partitioned?
    return "Success"  # May be wrong!
```

**더 나은 접근 방식:**```python
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

## 카오스 공학 원리
### 테스트 실패 시나리오
**테스트 대상:**
1. **인스턴스 오류**: 무작위 Pod/VM 종료
2. **네트워크 문제**: 지연 시간 추가, 패킷 삭제
3. **리소스 소진**: 디스크 채우기, 메모리 소진
4. **종속성 실패**: 모의 서비스 중단
5. **시계 왜곡**: 서버 시계 비동기화
**카오스 실험 예시:**```yaml
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

### 게임 데이
시스템 복원력을 테스트하기 위한 정기적인 연습:
1. **일정**: 분기별 경기일
2. **범위**: 프로덕션과 유사한 환경
3. **시나리오**: 여러 동시 오류
4. **지표**: 감지 시간, 복구 시간 측정
5. **학습**: 런북 문서화 및 개선
---

## 용량 계획
### 언더프로비저닝
**나쁜 예:**```markdown
Traffic: 1000 requests/second average
Capacity: Sized for exactly 1000 rps

Result: Any spike causes overload and cascading failures
```

**더 나은 접근 방식:**```markdown
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

### 과잉 프로비저닝 낭비
**나쁜 예:**```markdown
Running 100 servers "just in case"
Average utilization: 5%
Monthly cost: $50,000
Wasted: $47,500/month
```

**더 나은 접근 방식:**```markdown
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

## 사고 대응 모범 사례
### 통화 중 소진 방지
**나쁜 관행:**
- 매주 같은 사람이 통화함
- 에스컬레이션 경로 없음
- 실행 불가능한 항목에 대한 경고
- 책임을 묻는 사후부검
**우수 사례:**```markdown
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

### 런북 품질
**잘못된 런북:**```markdown
## Database Slow Query

1. Check database
2. Restart if needed
3. Call DBA
```

**좋은 실행서:**```markdown
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
SELECT * pg_stat_activity에서 
   WHERE 상태 = '활성' 
   ORDER BY 쿼리_시작;   ```

2. Check for locks:
   ```sql
SELECT * FROM pg_locks WHERE 부여됨 = false;   ```

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
