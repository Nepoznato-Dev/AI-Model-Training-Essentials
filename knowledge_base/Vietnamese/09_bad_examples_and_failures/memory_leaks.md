# Memory Leaks

## Overview

Memory leaks occur when programs allocate memory but fail to release it when no longer needed, causing gradual memory consumption growth. This document provides concrete examples of memory leaks and prevention strategies.

## Types of Memory Leaks

### Forgotten Event Listeners

**Bad Example (Vulnerable Code):**
```javascript
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
    }
}

// Usage
const comp = new Component(document.getElementById('app'));
comp.destroy();
// Memory leak: listener still holds reference to comp.data
```

**Why It's Bad:**
- Destroyed component still in memory
- Event listener prevents garbage collection
- Repeated create/destroy cycles exhaust memory

**Secure Approach:**
```javascript
// SECURE: Properly clean up event listeners
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
        // Remove listener before cleanup
        window.removeEventListener('resize', this.boundHandleResize);
        this.element.remove();
        this.data = null;  // Explicitly clear large data
    }
}
```

### Caching Without Eviction

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: Unbounded cache growth
cache = {}

def get_user_data(user_id):
    if user_id not in cache:
        # Fetch from database
        data = db.query("SELECT * FROM users WHERE id = ?", user_id)
        cache[user_id] = data  # Never removed
    
    return cache[user_id]

# Over time, cache grows indefinitely
# Every unique user_id adds more memory
```

**Problem Scenario:**
```
Day 1: 1,000 users → cache uses 10 MB
Day 30: 500,000 users → cache uses 5 GB ❌
Application crashes with OOM
```

**Why It's Bad:**
- Cache grows without bounds
- Old entries never evicted
- Eventually exhausts available memory

**Secure Approaches:**
```python
# Option 1: LRU Cache with size limit
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_user_data(user_id):
    return db.query("SELECT * FROM users WHERE id = ?", user_id)

# Option 2: Time-based expiration
import time
from collections import OrderedDict

class ExpiringCache:
    def __init__(self, ttl_seconds=3600, max_size=1000):
        self.cache = OrderedDict()
        self.ttl = ttl_seconds
        self.max_size = max_size
    
    def get(self, key):
        self._cleanup()
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                # Move to end (most recently used)
                self.cache.move_to_end(key)
                return value
            else:
                del self.cache[key]
        return None
    
    def put(self, key, value):
        self._cleanup()
        if len(self.cache) >= self.max_size:
            # Remove oldest entry
            self.cache.popitem(last=False)
        self.cache[key] = (value, time.time())
    
    def _cleanup(self):
        now = time.time()
        expired = [k for k, (_, ts) in self.cache.items() 
                   if now - ts > self.ttl]
        for key in expired:
            del self.cache[key]
```

### Circular References

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: Circular reference prevents GC in some languages
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        child.parent = self  # Child references parent
        self.children.append(child)  # Parent references child
        # Circular reference created

# Create tree
root = Node('root')
child1 = Node('child1')
child2 = Node('child2')

root.add_child(child1)
root.add_child(child2)

# Try to delete
del root
# In Python with reference counting: may not be collected immediately
# In JavaScript: depends on GC implementation
```

**Why It's Bad:**
- Reference cycles prevent simple reference counting GC
- Objects remain in memory even when logically deleted
- Can cause memory growth in long-running applications

**Secure Approaches:**
```python
# Option 1: Use weakref for back-references
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent_ref = None  # Weak reference
        self.children = []
    
    @property
    def parent(self):
        if self._parent_ref is not None:
            return self._parent_ref()
        return None
    
    @parent.setter
    def parent(self, node):
        if node is not None:
            self._parent_ref = weakref.ref(node)
        else:
            self._parent_ref = None
    
    def add_child(self, child):
        child.parent = self  # Weak reference
        self.children.append(child)  # Strong reference

# Option 2: Explicit cleanup method
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def destroy(self):
        for child in self.children:
            child.parent = None
            child.destroy()
        self.children.clear()
        self.parent = None
```

### Unclosed Resources

**Bad Example (Vulnerable Code):**
```python
# VULNERABLE: File handles not closed
def process_files(file_list):
    results = []
    for filepath in file_list:
        f = open(filepath, 'r')  # Opened but never closed
        data = f.read()
        results.append(process(data))
        # f.close() missing!
    
    return results

# After processing many files:
# OSError: [Errno 24] Too many open files
```

**Why It's Bad:**
- File descriptors exhausted
- Other resources (sockets, DB connections) similarly affected
- System-level resource limits hit

**Secure Approaches:**
```python
# Option 1: Context manager (best)
def process_files(file_list):
    results = []
    for filepath in file_list:
        with open(filepath, 'r') as f:  # Automatically closed
            data = f.read()
            results.append(process(data))
    return results

# Option 2: Try-finally
def process_files(file_list):
    results = []
    for filepath in file_list:
        f = None
        try:
            f = open(filepath, 'r')
            data = f.read()
            results.append(process(data))
        finally:
            if f:
                f.close()
    return results

# Option 3: For database connections
def query_users(user_ids):
    conn = None
    try:
        conn = create_db_connection()
        results = []
        for user_id in user_ids:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
                results.append(cursor.fetchone())
            finally:
                cursor.close()
        return results
    finally:
        if conn:
            conn.close()
```

### Growing Collections

**Bad Example (Vulnerable Code):**
```javascript
// VULNERABLE: Unbounded array growth
class Logger {
    constructor() {
        this.logs = [];  // Never cleared
    }
    
    log(message) {
        this.logs.push({
            timestamp: Date.now(),
            message: message,
            stack: new Error().stack  // Large stack trace
        });
    }
    
    // No cleanup method
}

// Usage in long-running server
const logger = new Logger();
setInterval(() => {
    logger.log('Heartbeat');  // Adds entry every second
}, 1000);

// After 1 day: 86,400 log entries
// After 1 week: 604,800 log entries → memory exhaustion
```

**Secure Approaches:**
```javascript
// Option 1: Bounded buffer
class Logger {
    constructor(maxSize = 10000) {
        this.logs = [];
        this.maxSize = maxSize;
    }
    
    log(message) {
        if (this.logs.length >= this.maxSize) {
            // Remove oldest entries
            this.logs.splice(0, this.logs.length - this.maxSize + 1);
        }
        this.logs.push({
            timestamp: Date.now(),
            message: message
        });
    }
    
    clear() {
        this.logs = [];
    }
}

// Option 2: Circular buffer
class CircularBuffer {
    constructor(size) {
        this.buffer = new Array(size);
        this.size = size;
        this.index = 0;
        this.count = 0;
    }
    
    push(item) {
        this.buffer[this.index] = item;
        this.index = (this.index + 1) % this.size;
        this.count = Math.min(this.count + 1, this.size);
    }
    
    getAll() {
        if (this.count < this.size) {
            return this.buffer.slice(0, this.count);
        }
        return [
            ...this.buffer.slice(this.index),
            ...this.buffer.slice(0, this.index)
        ];
    }
}
```

## Real-World Scenarios

### Scenario 1: Single Page Application Memory Leak

**Vulnerable Code:**
```javascript
// React component with memory leak
class Dashboard extends React.Component {
    componentDidMount() {
        // Subscribe to WebSocket
        this.ws = new WebSocket('wss://api.example.com/updates');
        this.ws.onmessage = (event) => {
            this.setState({ data: JSON.parse(event.data) });
        };
        
        // Set up polling interval
        this.pollInterval = setInterval(() => {
            this.fetchUpdates();
        }, 5000);
        
        // Add global event listener
        document.addEventListener('visibilitychange', this.handleVisibility);
    }
    
    componentWillUnmount() {
        // Missing cleanup!
        // WebSocket not closed
        // Interval not cleared
        // Event listener not removed
    }
    
    render() {
        return <div>{/* ... */}</div>;
    }
}
```

**Secure Implementation:**
```javascript
class Dashboard extends React.Component {
    componentDidMount() {
        this.ws = new WebSocket('wss://api.example.com/updates');
        this.ws.onmessage = (event) => {
            this.setState({ data: JSON.parse(event.data) });
        };
        
        this.pollInterval = setInterval(() => {
            this.fetchUpdates();
        }, 5000);
        
        document.addEventListener('visibilitychange', this.handleVisibility);
    }
    
    componentWillUnmount() {
        // Clean up WebSocket
        if (this.ws) {
            this.ws.close();
            this.ws = null;
        }
        
        // Clear interval
        if (this.pollInterval) {
            clearInterval(this.pollInterval);
            this.pollInterval = null;
        }
        
        // Remove event listener
        document.removeEventListener('visibilitychange', this.handleVisibility);
    }
    
    render() {
        return <div>{/* ... */}</div>;
    }
}
```

### Scenario 2: Node.js Stream Memory Leak

**Vulnerable Code:**
```javascript
// VULNERABLE: Stream not properly handled
app.get('/download/:fileId', (req, res) => {
    const filePath = getFilePath(req.params.fileId);
    const readStream = fs.createReadStream(filePath);
    
    readStream.on('data', (chunk) => {
        res.write(chunk);
    });
    
    readStream.on('end', () => {
        res.end();
    });
    
    // Missing error handling
    // If client disconnects, stream continues reading
    // Multiple failed requests accumulate streams
});
```

**Secure Implementation:**
```javascript
app.get('/download/:fileId', (req, res) => {
    const filePath = getFilePath(req.params.fileId);
    const readStream = fs.createReadStream(filePath);
    
    // Handle client disconnection
    req.on('close', () => {
        readStream.destroy();  // Stop reading
    });
    
    readStream.pipe(res);
    
    readStream.on('error', (err) => {
        console.error('Stream error:', err);
        if (!res.headersSent) {
            res.status(500).send('Error reading file');
        } else {
            res.end();
        }
    });
});
```

## Detection Patterns

### Code Review Red Flags

1. **Missing Cleanup in Lifecycle Methods:**
   ```javascript
   // BAD
   componentDidMount() {
       setInterval(...);
       addEventListener(...);
       subscribe(...);
   }
   // No componentWillUnmount
   ```

2. **Unbounded Data Structures:**
   ```python
   # BAD
   global_cache = {}  # No size limit
   all_logs = []  # Never cleared
   ```

3. **Resources Without Context Managers:**
   ```python
   # BAD
   f = open(file)
   data = f.read()
   # No close() or with statement
   ```

4. **Closures Holding Large Objects:**
   ```javascript
   // BAD
   function createHandler() {
       const largeData = new Array(1000000);
       return function() {
           console.log('clicked');  // Doesn't use largeData
       };  // But closure keeps it alive
   }
   ```

### Profiling Tools

```bash
# Node.js heap snapshot
node --inspect app.js
# Then use Chrome DevTools Memory tab

# Python memory profiling
pip install memory-profiler
python -m memory_profiler script.py

# Java VisualVM
jvisualvm  # Built into JDK

# Browser DevTools
# Chrome/Firefox: Performance + Memory tabs
```

## Testing Checklist

- [ ] Monitor memory usage over extended periods
- [ ] Test create/destroy cycles repeatedly
- [ ] Verify event listeners are removed
- [ ] Check for growing collection sizes
- [ ] Profile memory before/after operations
- [ ] Test with high load and many concurrent users
- [ ] Verify file handles are closed
- [ ] Check WebSocket/connection cleanup
- [ ] Monitor heap snapshots for retained objects
- [ ] Test subscription/unsubscription patterns
- [ ] Verify timers/intervals are cleared
- [ ] Check circular reference handling

## Related Documents

- [[unsafe_code]] - Unsafe coding patterns
- [[code_smells]] - Indicators of memory issues
- [[bad_api_design]] - Resource management in APIs
- [[security_mistakes]] - Resource exhaustion attacks
