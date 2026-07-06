# Race Conditions

## Overview

Race conditions occur when the behavior of software depends on the relative timing of events, such as the order in which threads execute. This document provides concrete examples of race conditions and strategies for prevention.

## Types of Race Conditions

### Check-Then-Act Race Condition

**Bad Example (Vulnerable Code):**
```python
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

**Problem Scenario:**
```
Initial balance: $100
Thread A: withdraw(80) - checks balance (100 >= 80 ✓)
Thread B: withdraw(50) - checks balance (100 >= 50 ✓)
Thread A: withdraws 80, balance = 20
Thread B: withdraws 50, balance = -30  ❌

Result: Negative balance, money created from nothing
```

**Why It's Bad:**
- Non-atomic operation allows interleaving
- Invariant (balance >= 0) violated
- Financial data corruption

**Secure Approach:**
```python
# SECURE: Atomic check-and-act with lock
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
    
    def withdraw(self, amount):
        with self.lock:  # Entire check-then-act is atomic
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False
```

### Read-Modify-Write Race Condition

**Bad Example (Vulnerable Code):**
```java
// VULNERABLE: Increment is not atomic
public class Counter {
    private int count = 0;
    
    public void increment() {
        count++;  // Actually: read, modify, write (3 operations)
    }
    
    public int getCount() {
        return count;
    }
}
```

**Problem Scenario:**
```
Initial count: 0
Thread A: reads count (0)
Thread B: reads count (0)
Thread A: increments (0+1=1), writes 1
Thread B: increments (0+1=1), writes 1

Expected: 2
Actual: 1  ❌
```

**Why It's Bad:**
- Lost updates due to non-atomic operation
- Count lower than expected
- Data integrity compromised

**Secure Approaches:**
```java
// Option 1: Synchronized method
public synchronized void increment() {
    count++;
}

// Option 2: Explicit lock
private final Lock lock = new ReentrantLock();
public void increment() {
    lock.lock();
    try {
        count++;
    } finally {
        lock.unlock();
    }
}

// Option 3: Atomic variable (best for simple counters)
private AtomicInteger count = new AtomicInteger(0);
public void increment() {
    count.incrementAndGet();  // Atomic operation
}
```

### Time-of-Check to Time-of-Use (TOCTOU)

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: File access race condition
def secure_file_read(filename, allowed_dir):
    # Check: verify file is in allowed directory
    real_path = os.path.realpath(filename)
    if not real_path.startswith(allowed_dir):
        raise SecurityError("Access denied")
    
    # Time gap where file could be swapped
    
    # Use: read the file
    with open(filename, 'r') as f:  # Might be different file now!
        return f.read()
```

**Attack Scenario:**
```
Attacker creates: /tmp/allowed/file.txt (legitimate)
Program checks: /tmp/allowed/file.txt ✓ (in allowed dir)
Attacker swaps: symlink /tmp/allowed/file.txt -> /etc/passwd
Program reads: /etc/passwd ❌ (sensitive data exposed)
```

**Why It's Bad:**
- File system state changes between check and use
- Security bypass possible
- Sensitive data exposure

**Secure Approach:**
```python
# SECURE: Open first, then validate the opened file descriptor
def secure_file_read(filename, allowed_dir):
    # Open file first (get file descriptor)
    fd = os.open(filename, os.O_RDONLY)
    try:
        # Get info about the opened file (not the path)
        file_stat = os.fstat(fd)
        
        # Verify it's a regular file
        if not stat.S_ISREG(file_stat.st_mode):
            raise SecurityError("Not a regular file")
        
        # Read using file descriptor
        with os.fdopen(fd, 'r') as f:
            return f.read()
    finally:
        os.close(fd)
```

## Real-World Scenarios

### Scenario 1: Double-Spending in E-commerce

**Vulnerable Code:**
```javascript
// Node.js vulnerable - non-atomic balance update
async function purchase(userId, amount) {
    const user = await db.getUser(userId);
    
    if (user.balance >= amount) {
        // Race window here
        await db.updateBalance(userId, user.balance - amount);
        await processOrder(userId, amount);
        return true;
    }
    return false;
}

// Attacker sends 100 concurrent requests simultaneously
```

**Problem:**
```
Balance: $100
100 concurrent requests of $10 each
All 100 pass the balance check before any update
All 100 deduct $10
Final balance: $100 - (100 × $10) = -$900 ❌
```

**Secure Implementation:**
```javascript
// SECURE: Database transaction with row-level locking
async function purchase(userId, amount) {
    return await db.transaction(async (tx) => {
        // Lock the row for update
        const user = await tx.query(
            'SELECT balance FROM users WHERE id = ? FOR UPDATE',
            [userId]
        );
        
        if (user.balance >= amount) {
            await tx.query(
                'UPDATE users SET balance = balance - ? WHERE id = ?',
                [amount, userId]
            );
            await processOrder(userId, amount);
            return true;
        }
        return false;
    });
}
```

### Scenario 2: Singleton Initialization Race

**Vulnerable Code:**
```java
// VULNERABLE: Double-checked locking broken
public class Singleton {
    private static Singleton instance;
    
    public static Singleton getInstance() {
        if (instance == null) {  // First check (no lock)
            synchronized (Singleton.class) {
                if (instance == null) {  // Second check (with lock)
                    instance = new Singleton();  // Not atomic!
                }
            }
        }
        return instance;
    }
}
```

**Problem:**
```
Thread A: instance == null ✓, enters synchronized block
Thread A: creates Singleton object (partially constructed)
Thread B: instance != null (reference exists but not fully initialized)
Thread B: uses partially constructed object ❌
```

**Secure Implementation:**
```java
// Option 1: Eager initialization
public class Singleton {
    private static final Singleton instance = new Singleton();
    public static Singleton getInstance() {
        return instance;
    }
}

// Option 2: Proper double-checked locking with volatile
public class Singleton {
    private static volatile Singleton instance;
    
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}

// Option 3: Initialization-on-demand holder
public class Singleton {
    private Singleton() {}
    
    private static class Holder {
        static final Singleton INSTANCE = new Singleton();
    }
    
    public static Singleton getInstance() {
        return Holder.INSTANCE;
    }
}
```

### Scenario 3: Resource Pool Exhaustion

**Vulnerable Code:**
```python
# VULNERABLE: Non-atomic pool management
class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.active_connections = 0
        self.pool = []
    
    def acquire(self):
        if self.active_connections < self.max_connections:
            # Race window
            self.active_connections += 1
            return self._create_connection()
        raise PoolExhaustedError()
    
    def release(self, conn):
        self.active_connections -= 1
        self.pool.append(conn)
```

**Problem:**
```
Max connections: 10
Active: 9
Thread A: checks (9 < 10 ✓)
Thread B: checks (9 < 10 ✓)
Thread A: increments to 10, creates connection
Thread B: increments to 11, creates connection ❌

Now 11 active connections when max is 10
```

**Secure Implementation:**
```python
# SECURE: Thread-safe with lock
from threading import Lock
import queue

class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.lock = Lock()
        self.pool = queue.LifoQueue(max_connections)
        
        # Pre-create all connections
        for _ in range(max_connections):
            self.pool.put(self._create_connection())
    
    def acquire(self, timeout=None):
        try:
            return self.pool.get(timeout=timeout)  # Blocks if empty
        except queue.Empty:
            raise PoolExhaustedError()
    
    def release(self, conn):
        try:
            self.pool.put_nowait(conn)
        except queue.Full:
            conn.close()  # Discard if pool is full
```

## Prevention Strategies

### Use Atomic Operations

```python
# Python threading
from threading import Lock

lock = Lock()
with lock:
    # Critical section - only one thread at a time
    shared_resource.modify()

# Or use atomic types
from queue import Queue  # Thread-safe queue
```

```java
// Java concurrency utilities
AtomicInteger counter = new AtomicInteger();
counter.incrementAndGet();  // Atomic

AtomicReference<State> state = new AtomicReference<>();
state.compareAndSet(expected, newValue);  // Atomic CAS
```

```python
# Python asyncio (for async code)
import asyncio

lock = asyncio.Lock()
async with lock:
    # Only one coroutine at a time
    await modify_shared_resource()
```

### Use Thread-Safe Collections

```python
# Thread-safe alternatives
from queue import Queue, LifoQueue, PriorityQueue
from collections import deque  # Thread-safe for append/popleft
import threading

# Regular dict is NOT thread-safe for modifications
threading.RLock()  # For protecting custom data structures
```

```java
// Java concurrent collections
ConcurrentHashMap<K, V> map = new ConcurrentHashMap<>();
CopyOnWriteArrayList<T> list = new CopyOnWriteArrayList<>();
BlockingQueue<T> queue = new LinkedBlockingQueue<>();
```

### Database-Level Protection

```sql
-- Row-level locking
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;

-- Optimistic locking with version
UPDATE accounts 
SET balance = balance - 100, version = version + 1 
WHERE id = 1 AND version = 5;  -- Fails if version changed

-- Pessimistic locking
BEGIN TRANSACTION;
-- ... operations ...
COMMIT;
```

### Immutable Objects

```java
// Immutable objects are inherently thread-safe
public final class ImmutablePoint {
    private final int x;
    private final int y;
    
    public ImmutablePoint(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public int getX() { return x; }
    public int getY() { return y; }
    
    // Return new object instead of modifying
    public ImmutablePoint translate(int dx, int dy) {
        return new ImmutablePoint(x + dx, y + dy);
    }
}
```

## Detection Patterns

### Code Review Red Flags

1. **Non-Atomic Compound Operations:**
   ```python
   # BAD
   counter += 1
   balance = balance - amount
   list.append(x); if len(list) > max: list.pop(0)
   ```

2. **Check-Then-Act Without Locking:**
   ```python
   # BAD
   if key not in cache:
       cache[key] = compute_value(key)
   
   if file_exists(path):
       read_file(path)
   ```

3. **Lazy Initialization Without Synchronization:**
   ```java
   // BAD
   if (instance == null) {
       instance = new Singleton();
   }
   ```

4. **Shared Mutable State:**
   ```python
   # BAD: Global mutable state
   global_counter = 0
   
   def increment():
       global global_counter
       global_counter += 1
   ```

### Testing Strategies

```python
# Stress test for race conditions
import threading
import time

def test_concurrent_access():
    counter = SafeCounter()
    num_threads = 100
    increments_per_thread = 1000
    
    def worker():
        for _ in range(increments_per_thread):
            counter.increment()
    
    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    expected = num_threads * increments_per_thread
    assert counter.value == expected, f"Expected {expected}, got {counter.value}"
```

## Testing Checklist

- [ ] Test with high concurrency (100+ threads)
- [ ] Test with random delays in critical sections
- [ ] Test boundary conditions (max capacity, zero values)
- [ ] Test repeated acquire/release cycles
- [ ] Test under load with monitoring
- [ ] Use thread sanitizers (TSan) where available
- [ ] Test database transactions with concurrent users
- [ ] Verify locks are always released (even on exceptions)
- [ ] Check for deadlocks with multiple locks
- [ ] Test timeout scenarios for blocking operations

## Related Documents

- [[unsafe_code]] - Unsafe coding patterns
- [[security_mistakes]] - General security vulnerabilities
- [[bad_api_design]] - API design issues including thread safety
- [[code_smells]] - Indicators of potential concurrency issues
