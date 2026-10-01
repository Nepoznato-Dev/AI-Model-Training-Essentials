# Chapter 3: Advanced Orchestration

## 🎯 Learning Objectives

By the end of this chapter, you will:
- Scale orchestration to thousands of concurrent workflows
- Implement distributed orchestration across multiple machines
- Build comprehensive monitoring and observability
- Achieve fault tolerance and automatic recovery
- Persist workflow state for reliability
- Implement rate limiting and throttling

---

## 3.1 Scaling to Thousands of Workflows

### The Challenge

Your simple workflow engine works great for dozens of workflows. But what happens at scale?

**Problems at scale:**
- Memory exhaustion (storing all state in RAM)
- CPU bottleneck (single-threaded execution)
- No persistence (lose everything on restart)
- Can't distribute across machines
- Monitoring becomes impossible

### Solution: Architecture Redesign

```
┌─────────────────────────────────────────────────┐
│              Load Balancer                       │
└────────────────┬────────────────────────────────┘
                 │
    ┌────────────┼────────────┐
    ↓            ↓            ↓
┌───────┐  ┌─────────┐  ┌─────────┐
│Worker 1│  │Worker 2 │  │Worker N │
└───┬───┘  └────┬────┘  └────┬────┘
    │          │            │
    └──────────┼────────────┘
               ↓
        ┌──────────────┐
        │ Message Queue │
        │  (Redis/RabbitMQ)│
        └───────┬──────┘
                │
    ┌───────────┼───────────┐
    ↓           ↓           ↓
┌───────┐ ┌─────────┐ ┌─────────┐
│ Redis │ │ Postgres│ │  S3     │
│Cache  │ │  DB     │ │Storage  │
└───────┘ └─────────┘ └─────────┘
```

### Implementation: Queue-Based Architecture

```python
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
import pickle
import redis
from dataclasses import dataclass, asdict

@dataclass
class WorkflowInstance:
    """Represents a running workflow instance"""
    id: str
    workflow_name: str
    status: str  # pending, running, completed, failed
    context: Dict
    created_at: float
    updated_at: float
    current_step: Optional[str] = None
    error: Optional[str] = None
    
    def to_json(self) -> str:
        return json.dumps(asdict(self))
    
    @classmethod
    def from_json(cls, json_str: str) -> 'WorkflowInstance':
        data = json.loads(json_str)
        return cls(**data)

class DistributedWorkflowEngine:
    """
    Workflow engine designed for horizontal scaling.
    
    Uses Redis for:
    - Queue management
    - State persistence
    - Distributed locking
    """
    
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(redis_url)
        self.worker_id = f"worker_{uuid.uuid4().hex[:8]}"
        print(f"🆔 Worker started: {self.worker_id}")
    
    def submit_workflow(self, workflow_name: str, 
                       initial_context: Dict) -> str:
        """
        Submit a new workflow for execution.
        
        Returns workflow instance ID.
        """
        instance_id = str(uuid.uuid4())
        
        instance = WorkflowInstance(
            id=instance_id,
            workflow_name=workflow_name,
            status="pending",
            context=initial_context,
            created_at=datetime.now().timestamp(),
            updated_at=datetime.now().timestamp()
        )
        
        # Persist instance
        self.redis.set(
            f"workflow:{instance_id}",
            instance.to_json()
        )
        
        # Add to queue
        self.redis.lpush(
            "workflow_queue",
            json.dumps({
                "instance_id": instance_id,
                "workflow_name": workflow_name
            })
        )
        
        print(f"📤 Submitted workflow {instance_id} ({workflow_name})")
        return instance_id
    
    def claim_workflow(self, timeout: int = 30) -> Optional[WorkflowInstance]:
        """
        Claim a workflow from the queue for processing.
        
        Uses BRPOUP with timeout to block until work is available.
        """
        # Block waiting for work
        result = self.redis.brpop("workflow_queue", timeout=timeout)
        
        if not result:
            return None
        
        _, message = result
        work_item = json.loads(message)
        
        instance_id = work_item["instance_id"]
        
        # Load instance
        instance_data = self.redis.get(f"workflow:{instance_id}")
        if not instance_data:
            print(f"⚠️  Instance {instance_id} not found")
            return None
        
        instance = WorkflowInstance.from_json(instance_data)
        
        # Mark as being processed by this worker
        self.redis.set(
            f"workflow:{instance_id}:lock",
            self.worker_id,
            ex=300  # Lock expires in 5 minutes
        )
        
        instance.status = "running"
        instance.updated_at = datetime.now().timestamp()
        
        return instance
    
    def update_instance(self, instance: WorkflowInstance):
        """Persist instance state"""
        instance.updated_at = datetime.now().timestamp()
        self.redis.set(
            f"workflow:{instance.id}",
            instance.to_json()
        )
    
    def complete_workflow(self, instance: WorkflowInstance, 
                         success: bool, error: str = None):
        """Mark workflow as completed"""
        instance.status = "completed" if success else "failed"
        instance.error = error
        instance.updated_at = datetime.now().timestamp()
        
        self.update_instance(instance)
        
        # Remove lock
        self.redis.delete(f"workflow:{instance.id}:lock")
        
        status_icon = "✅" if success else "❌"
        print(f"{status_icon} Workflow {instance.id} completed")
    
    def get_queue_stats(self) -> Dict:
        """Get current queue statistics"""
        queue_length = self.redis.llen("workflow_queue")
        
        # Count active workflows
        active_count = 0
        for key in self.redis.scan_iter("workflow:*"):
            if ":lock" in key.decode():
                active_count += 1
        
        return {
            "queue_length": queue_length,
            "active_workflows": active_count,
            "worker_id": self.worker_id
        }

# Usage Example
if __name__ == "__main__":
    # Start multiple workers (in separate processes)
    engine = DistributedWorkflowEngine()
    
    # Submit workflows
    for i in range(100):
        engine.submit_workflow("customer_onboarding", {
            "customer_id": f"CUST_{i}",
            "email": f"user{i}@example.com"
        })
    
    # Check stats
    stats = engine.get_queue_stats()
    print(f"\n📊 Queue Stats: {stats}")
```

### Running Multiple Workers

```bash
# Terminal 1
python worker.py --worker-id=worker-1

# Terminal 2
python worker.py --worker-id=worker-2

# Terminal 3
python worker.py --worker-id=worker-3
```

Each worker independently pulls from the same queue, enabling horizontal scaling!

---

## 3.2 Monitoring and Observability

### Why Monitoring Matters

Without monitoring, you're flying blind:
- Workflows fail silently
- Performance degrades unnoticed
- Bottlenecks are invisible
- Debugging is impossible

### Key Metrics to Track

**Volume Metrics:**
- Workflows submitted per minute
- Workflows completed per minute
- Queue depth
- Active workflows

**Performance Metrics:**
- Average execution time
- P95/P99 latency
- Step duration breakdown
- Throughput (workflows/second)

**Error Metrics:**
- Failure rate (%)
- Error types distribution
- Retry count distribution
- Time to recovery

**Resource Metrics:**
- Worker CPU/memory usage
- Queue memory usage
- Database connections
- Network I/O

### Implementation: Metrics Collection

```python
import time
from collections import defaultdict
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define Prometheus metrics
WORKFLOW_SUBMITTED = Counter(
    'workflow_submitted_total',
    'Total workflows submitted',
    ['workflow_name']
)

WORKFLOW_COMPLETED = Counter(
    'workflow_completed_total',
    'Total workflows completed',
    ['workflow_name', 'status']
)

WORKFLOW_DURATION = Histogram(
    'workflow_duration_seconds',
    'Workflow execution duration',
    ['workflow_name'],
    buckets=[0.1, 0.5, 1.0, 5.0, 10.0, 30.0, 60.0, 300.0]
)

STEP_DURATION = Histogram(
    'step_duration_seconds',
    'Step execution duration',
    ['workflow_name', 'step_name']
)

ACTIVE_WORKFLOWS = Gauge(
    'active_workflows',
    'Currently running workflows',
    ['workflow_name']
)

ERROR_COUNT = Counter(
    'workflow_errors_total',
    'Total workflow errors',
    ['workflow_name', 'error_type']
)

class ObservableWorkflowEngine(WorkflowEngine):
    """Workflow engine with built-in observability"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metrics_enabled = True
        
        # Start Prometheus metrics server
        start_http_server(8000)
        print("📊 Metrics server started on :8000/metrics")
    
    def run(self, initial_context: Dict = None, **kwargs) -> Dict[str, StepResult]:
        """Execute workflow with metrics collection"""
        
        workflow_name = initial_context.get("_workflow_name", "unknown")
        start_time = time.time()
        
        # Record submission
        WORKFLOW_SUBMITTED.labels(workflow_name=workflow_name).inc()
        ACTIVE_WORKFLOWS.labels(workflow_name=workflow_name).inc()
        
        try:
            # Execute normally
            results = super().run(initial_context, **kwargs)
            
            # Record completion
            duration = time.time() - start_time
            WORKFLOW_DURATION.labels(workflow_name=workflow_name).observe(duration)
            
            failed_steps = sum(1 for r in results.values() 
                             if r.status == StepStatus.FAILED)
            
            status = "failed" if failed_steps > 0 else "success"
            WORKFLOW_COMPLETED.labels(
                workflow_name=workflow_name,
                status=status
            ).inc()
            
            if failed_steps > 0:
                ERROR_COUNT.labels(
                    workflow_name=workflow_name,
                    error_type="step_failure"
                ).inc(failed_steps)
            
            return results
            
        except Exception as e:
            # Record error
            ERROR_COUNT.labels(
                workflow_name=workflow_name,
                error_type=type(e).__name__
            ).inc()
            
            WORKFLOW_COMPLETED.labels(
                workflow_name=workflow_name,
                status="error"
            ).inc()
            
            raise
            
        finally:
            ACTIVE_WORKFLOWS.labels(workflow_name=workflow_name).dec()
    
    def _execute_step_with_retry(self, step: Step, context: Dict) -> StepResult:
        """Execute step with timing metrics"""
        workflow_name = context.get("_workflow_name", "unknown")
        
        start_time = time.time()
        result = super()._execute_step_with_retry(step, context)
        duration = time.time() - start_time
        
        # Record step duration
        STEP_DURATION.labels(
            workflow_name=workflow_name,
            step_name=step.name
        ).observe(duration)
        
        return result

# Usage with metrics
engine = ObservableWorkflowEngine()

initial_context = {
    "_workflow_name": "customer_onboarding",
    "customer_id": "CUST_123"
}

results = engine.run(initial_context)
```

### Visualization: Grafana Dashboard

Create a `dashboard.json` for Grafana:

```json
{
  "dashboard": {
    "title": "Workflow Orchestration",
    "panels": [
      {
        "title": "Workflows per Minute",
        "type": "graph",
        "targets": [{
          "expr": "rate(workflow_submitted_total[1m])"
        }]
      },
      {
        "title": "Success Rate",
        "type": "gauge",
        "targets": [{
          "expr": "rate(workflow_completed_total{status=\"success\"}[5m]) / rate(workflow_completed_total[5m]) * 100"
        }]
      },
      {
        "title": "P95 Duration",
        "type": "graph",
        "targets": [{
          "expr": "histogram_quantile(0.95, rate(workflow_duration_seconds_bucket[5m]))"
        }]
      },
      {
        "title": "Queue Depth",
        "type": "graph",
        "targets": [{
          "expr": "workflow_queue_length"
        }]
      }
    ]
  }
}
```

---

## 3.3 Fault Tolerance and Recovery

### Types of Failures

1. **Transient failures**: Network blips, temporary service unavailability
2. **Permanent failures**: Invalid data, missing resources
3. **System failures**: Worker crashes, power outages
4. **Timeout failures**: Steps taking too long

### Recovery Strategies

#### Strategy 1: Automatic Retry with Backoff

```python
import random
from datetime import datetime, timedelta

class RetryPolicy:
    """Configurable retry policy"""
    
    def __init__(self, 
                 max_retries: int = 3,
                 base_delay: float = 1.0,
                 max_delay: float = 60.0,
                 exponential_base: float = 2.0,
                 jitter: bool = True):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter
    
    def get_delay(self, attempt: int) -> float:
        """Calculate delay for given attempt number"""
        # Exponential backoff
        delay = self.base_delay * (self.exponential_base ** attempt)
        
        # Cap at max delay
        delay = min(delay, self.max_delay)
        
        # Add jitter to prevent thundering herd
        if self.jitter:
            delay = delay * (0.5 + random.random())
        
        return delay
    
    def should_retry(self, attempt: int, error: Exception) -> bool:
        """Determine if retry should be attempted"""
        if attempt >= self.max_retries:
            return False
        
        # Don't retry certain errors
        non_retryable = [
            "ValidationError",
            "AuthenticationError",
            "PermissionDenied"
        ]
        
        if type(error).__name__ in non_retryable:
            return False
        
        return True

# Integration with workflow engine
class ResilientWorkflowEngine(WorkflowEngine):
    """Engine with advanced retry capabilities"""
    
    def __init__(self, retry_policy: RetryPolicy = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.retry_policy = retry_policy or RetryPolicy()
    
    def _execute_step_with_retry(self, step: Step, context: Dict) -> StepResult:
        """Execute with configurable retry policy"""
        attempt = 0
        
        while True:
            try:
                start_time = time.time()
                output = step.action(context)
                duration = time.time() - start_time
                
                return StepResult(
                    step_name=step.name,
                    status=StepStatus.SUCCESS,
                    output=output,
                    duration=duration,
                    retries_used=attempt
                )
                
            except Exception as e:
                attempt += 1
                
                if not self.retry_policy.should_retry(attempt, e):
                    # Permanent failure
                    return StepResult(
                        step_name=step.name,
                        status=StepStatus.FAILED,
                        error=f"{type(e).__name__}: {str(e)}",
                        retries_used=attempt - 1
                    )
                
                if attempt > self.retry_policy.max_retries:
                    return StepResult(
                        step_name=step.name,
                        status=StepStatus.FAILED,
                        error=f"Max retries exceeded: {str(e)}",
                        retries_used=attempt - 1
                    )
                
                # Wait before retry
                delay = self.retry_policy.get_delay(attempt)
                self._log(f"  ⏳ Retrying in {delay:.2f}s (attempt {attempt}/{self.retry_policy.max_retries})")
                time.sleep(delay)
```

#### Strategy 2: Dead Letter Queue

When retries are exhausted, send to dead letter queue for manual inspection:

```python
class DeadLetterQueue:
    """Store failed workflows for later analysis"""
    
    def __init__(self, redis_url: str):
        self.redis = redis.from_url(redis_url)
    
    def add(self, instance: WorkflowInstance, error: str, 
            step_results: Dict[str, StepResult]):
        """Add failed workflow to DLQ"""
        dlq_entry = {
            "instance_id": instance.id,
            "workflow_name": instance.workflow_name,
            "error": error,
            "failed_at": datetime.now().isoformat(),
            "context": instance.context,
            "step_results": {
                name: {
                    "status": result.status.value,
                    "error": result.error
                }
                for name, result in step_results.items()
            }
        }
        
        self.redis.lpush("dead_letter_queue", json.dumps(dlq_entry))
        print(f"💀 Added {instance.id} to dead letter queue")
    
    def peek(self, limit: int = 10) -> List[Dict]:
        """View recent failures"""
        entries = []
        for item in self.redis.lrange("dead_letter_queue", 0, limit - 1):
            entries.append(json.loads(item))
        return entries
    
    def replay(self, instance_id: str) -> str:
        """Replay a failed workflow"""
        # Find entry in DLQ
        for item in self.redis.lrange("dead_letter_queue", 0, -1):
            entry = json.loads(item)
            if entry["instance_id"] == instance_id:
                # Remove from DLQ
                self.redis.lrem("dead_letter_queue", 1, item)
                
                # Create new instance with same context
                new_id = str(uuid.uuid4())
                print(f"🔄 Replaying {instance_id} as {new_id}")
                return new_id
        
        raise ValueError(f"Instance {instance_id} not found in DLQ")
```

#### Strategy 3: Checkpointing and Resume

Save state periodically to resume from last checkpoint:

```python
class CheckpointManager:
    """Manage workflow checkpoints for recovery"""
    
    def __init__(self, storage_path: str = "./checkpoints"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
    
    def save_checkpoint(self, instance: WorkflowInstance, 
                       completed_steps: Dict[str, StepResult]):
        """Save workflow state"""
        checkpoint = {
            "instance_id": instance.id,
            "workflow_name": instance.workflow_name,
            "context": instance.context,
            "completed_steps": {
                name: {
                    "status": result.status.value,
                    "output": result.output,
                    "duration": result.duration
                }
                for name, result in completed_steps.items()
            },
            "timestamp": datetime.now().isoformat()
        }
        
        filepath = os.path.join(
            self.storage_path, 
            f"{instance.id}.checkpoint"
        )
        
        with open(filepath, 'w') as f:
            json.dump(checkpoint, f)
        
        self._log(f"💾 Checkpoint saved: {filepath}")
    
    def load_checkpoint(self, instance_id: str) -> Optional[Dict]:
        """Load checkpoint if exists"""
        filepath = os.path.join(
            self.storage_path,
            f"{instance_id}.checkpoint"
        )
        
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def resume_from_checkpoint(self, instance_id: str, 
                               workflow_steps: Dict[str, callable]) -> WorkflowInstance:
        """Resume workflow from checkpoint"""
        checkpoint = self.load_checkpoint(instance_id)
        
        if not checkpoint:
            raise ValueError(f"No checkpoint found for {instance_id}")
        
        # Recreate instance
        instance = WorkflowInstance(
            id=instance_id,
            workflow_name=checkpoint["workflow_name"],
            status="running",
            context=checkpoint["context"],
            created_at=datetime.now().timestamp(),
            updated_at=datetime.now().timestamp()
        )
        
        # Restore completed steps
        results = {}
        for step_name, step_data in checkpoint["completed_steps"].items():
            results[step_name] = StepResult(
                step_name=step_name,
                status=StepStatus(step_data["status"]),
                output=step_data["output"],
                duration=step_data["duration"]
            )
        
        # Continue execution from where it left off
        # (Implementation depends on your engine architecture)
        
        return instance
```

---

## 3.4 State Persistence

### Why Persist State?

- Survive system restarts
- Enable debugging and auditing
- Support long-running workflows (hours/days)
- Facilitate compliance requirements

### Storage Options

| Storage | Best For | Pros | Cons |
|---------|----------|------|------|
| **Redis** | Hot state, queues | Fast, atomic ops | Volatile (unless AOF) |
| **PostgreSQL** | Persistent state | Durable, queryable | Slower than Redis |
| **MongoDB** | Flexible schemas | Schemaless, scalable | Less transactional |
| **S3** | Archives, checkpoints | Cheap, durable | High latency |

### Hybrid Approach: Redis + PostgreSQL

```python
import psycopg2
from psycopg2.extras import RealDictCursor

class HybridStateStore:
    """
    Use Redis for hot state, PostgreSQL for durability.
    """
    
    def __init__(self, redis_url: str, postgres_url: str):
        self.redis = redis.from_url(redis_url)
        self.postgres = psycopg2.connect(postgres_url)
    
    def save_workflow_state(self, instance: WorkflowInstance, 
                           step_results: Dict[str, StepResult]):
        """Save to both Redis and PostgreSQL"""
        
        # Hot state in Redis (fast access)
        self.redis.setex(
            f"workflow:{instance.id}",
            3600,  # TTL: 1 hour
            instance.to_json()
        )
        
        # Durable state in PostgreSQL
        with self.postgres.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                INSERT INTO workflow_instances 
                (id, workflow_name, status, context, created_at, updated_at, error)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET
                    status = EXCLUDED.status,
                    updated_at = EXCLUDED.updated_at,
                    error = EXCLUDED.error
            """, (
                instance.id,
                instance.workflow_name,
                instance.status,
                json.dumps(instance.context),
                datetime.fromtimestamp(instance.created_at),
                datetime.fromtimestamp(instance.updated_at),
                instance.error
            ))
            
            # Save step results
            for step_name, result in step_results.items():
                cur.execute("""
                    INSERT INTO workflow_step_results
                    (instance_id, step_name, status, output, error, duration)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (instance_id, step_name) DO UPDATE SET
                        status = EXCLUDED.status,
                        output = EXCLUDED.output,
                        error = EXCLUDED.error,
                        duration = EXCLUDED.duration
                """, (
                    instance.id,
                    step_name,
                    result.status.value,
                    json.dumps(result.output) if result.output else None,
                    result.error,
                    result.duration
                ))
            
            self.postgres.commit()
    
    def get_workflow_history(self, instance_id: str) -> Dict:
        """Retrieve complete workflow history from PostgreSQL"""
        with self.postgres.cursor(cursor_factory=RealDictCursor) as cur:
            # Get instance
            cur.execute("""
                SELECT * FROM workflow_instances WHERE id = %s
            """, (instance_id,))
            instance = cur.fetchone()
            
            # Get step results
            cur.execute("""
                SELECT * FROM workflow_step_results 
                WHERE instance_id = %s
                ORDER BY updated_at
            """, (instance_id,))
            steps = cur.fetchall()
            
            return {
                "instance": dict(instance) if instance else None,
                "steps": [dict(step) for step in steps]
            }
```

### Database Schema

```sql
-- PostgreSQL schema for workflow persistence

CREATE TABLE workflow_instances (
    id UUID PRIMARY KEY,
    workflow_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    context JSONB NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    error TEXT,
    INDEX idx_status (status),
    INDEX idx_created (created_at)
);

CREATE TABLE workflow_step_results (
    instance_id UUID REFERENCES workflow_instances(id),
    step_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    output JSONB,
    error TEXT,
    duration FLOAT,
    started_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (instance_id, step_name)
);

CREATE TABLE workflow_events (
    id SERIAL PRIMARY KEY,
    instance_id UUID REFERENCES workflow_instances(id),
    event_type VARCHAR(100) NOT NULL,
    event_data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 3.5 Rate Limiting and Throttling

### Why Rate Limit?

- Protect external APIs from overload
- Prevent resource exhaustion
- Ensure fair usage across tenants
- Comply with API rate limits

### Token Bucket Algorithm

```python
import time
from threading import Lock

class TokenBucket:
    """
    Rate limiter using token bucket algorithm.
    """
    
    def __init__(self, capacity: int, refill_rate: float):
        """
        Args:
            capacity: Maximum tokens in bucket
            refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = Lock()
    
    def consume(self, tokens: int = 1) -> bool:
        """
        Try to consume tokens.
        
        Returns True if successful, False if rate limited.
        """
        with self.lock:
            now = time.time()
            
            # Refill tokens based on elapsed time
            elapsed = now - self.last_refill
            self.tokens = min(
                self.capacity,
                self.tokens + elapsed * self.refill_rate
            )
            self.last_refill = now
            
            # Try to consume
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            
            return False
    
    def wait_for_token(self, tokens: int = 1, timeout: float = None) -> bool:
        """
        Block until tokens are available.
        
        Returns True if acquired, False if timeout.
        """
        start_time = time.time()
        
        while True:
            if self.consume(tokens):
                return True
            
            if timeout and (time.time() - start_time) >= timeout:
                return False
            
            # Calculate wait time
            with self.lock:
                tokens_needed = tokens - self.tokens
                wait_time = tokens_needed / self.refill_rate
            
            time.sleep(min(wait_time, 0.1))  # Poll every 100ms max

class RateLimitedWorkflowEngine(WorkflowEngine):
    """Engine with rate limiting"""
    
    def __init__(self, rate_limits: Dict[str, Dict] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.rate_limiters = {}
        
        if rate_limits:
            for step_name, config in rate_limits.items():
                self.rate_limiters[step_name] = TokenBucket(
                    capacity=config.get("capacity", 10),
                    refill_rate=config.get("refill_rate", 1.0)
                )
    
    def _execute_step_with_retry(self, step: Step, context: Dict) -> StepResult:
        """Execute step with rate limiting"""
        
        # Check rate limit
        if step.name in self.rate_limiters:
            limiter = self.rate_limiters[step.name]
            
            if not limiter.consume():
                self._log(f"  ⏸️  Rate limited: {step.name}")
                # Could wait or fail fast depending on requirements
                time.sleep(1.0 / limiter.refill_rate)
        
        return super()._execute_step_with_retry(step, context)

# Usage
rate_limits = {
    "call_external_api": {
        "capacity": 5,      # Burst of 5
        "refill_rate": 1.0  # 1 request per second sustained
    },
    "send_email": {
        "capacity": 10,
        "refill_rate": 0.5  # 1 email per 2 seconds
    }
}

engine = RateLimitedWorkflowEngine(rate_limits=rate_limits)
```

---

## 📚 Glossary

| Term | Definition |
|------|------------|
| **Horizontal Scaling** | Adding more machines to handle load |
| **Message Queue** | Buffer for passing work between components |
| **Prometheus** | Open-source monitoring and alerting toolkit |
| **Dead Letter Queue** | Storage for messages that couldn't be processed |
| **Checkpointing** | Saving state periodically for recovery |
| **Token Bucket** | Algorithm for rate limiting |
| **Exponential Backoff** | Increasing wait time between retries |
| **Jitter** | Random variation added to prevent synchronization |
| **Thundering Herd** | Problem where many clients retry simultaneously |
| **Idempotent** | Operation that can be applied multiple times safely |

---

## 🎓 Exercises

### Exercise 1: Build a Multi-Worker System

Set up Redis and create 3 worker processes that pull from the same queue. Measure throughput improvement.

### Exercise 2: Implement Comprehensive Monitoring

Add Prometheus metrics to your workflow engine and create a Grafana dashboard showing:
- Success rate over time
- P95 latency
- Queue depth
- Error breakdown

### Exercise 3: Create a Dead Letter Queue Processor

Build a tool that:
1. Lists all failed workflows in DLQ
2. Shows error details
3. Allows replaying specific workflows
4. Automatically retries after fixing issues

---

## 🔍 Self-Assessment Checklist

- [ ] Explain why single-machine orchestration doesn't scale
- [ ] Implement queue-based distributed orchestration
- [ ] Set up Prometheus metrics for monitoring
- [ ] Configure retry policies with exponential backoff
- [ ] Implement dead letter queue for failed workflows
- [ ] Save and restore workflow checkpoints
- [ ] Apply rate limiting to protect resources
- [ ] Design hybrid storage (Redis + PostgreSQL)

---

## 🚀 What's Next?

Chapter 4 covers **Production Systems**:
- Choosing orchestration frameworks (Airflow, Prefect, Temporal)
- Deploying to cloud infrastructure
- Security best practices
- Testing strategies
- Migration from custom to framework-based
- Real-world case studies

You'll learn how to productionize everything you've built!
