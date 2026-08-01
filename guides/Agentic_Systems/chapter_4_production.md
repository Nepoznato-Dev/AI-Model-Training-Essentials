# Chapter 4: Production Deployment

## 🎯 Chapter Overview

**What You'll Learn:**
- Deploying agents to production environments
- Monitoring and observability
- Scaling to handle thousands of requests
- Cost optimization strategies
- Security best practices
- Real-world project implementations

**By the End:** You'll have deployed production-ready agent systems!

**Time Estimate:** 6-8 hours

**Prerequisites:** Chapters 1-3

---

## 4.1 Production Architecture

### From Prototype to Production

Moving from a Jupyter notebook to production requires:

```
Prototype                          Production
┌─────────────┐                   ┌──────────────────┐
│ Single      │                   │ Load Balancer    │
│ Agent       │         →         ├──────────────────┤
│ Local       │                   │ Agent Pool (N)   │
│ No logging  │                   ├──────────────────┤
│             │                   │ Message Queue    │
│             │                   ├──────────────────┤
│             │                   │ Monitoring       │
└─────────────┘                   └──────────────────┘
```

### Core Components

#### 1. API Gateway
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Agent API")

class AgentRequest(BaseModel):
    user_id: str
    message: str
    context: dict = None

class AgentResponse(BaseModel):
    response: str
    confidence: float
    steps: int
    duration_ms: float

@app.post("/agent/chat", response_model=AgentResponse)
async def chat(request: AgentRequest):
    """Main chat endpoint"""
    start_time = time.time()
    
    try:
        # Get agent from pool
        agent = await get_available_agent()
        
        # Process request
        response = await agent.process(
            message=request.message,
            context=request.context
        )
        
        duration = (time.time() - start_time) * 1000
        
        return AgentResponse(
            response=response['text'],
            confidence=response['confidence'],
            steps=response['steps'],
            duration_ms=duration
        )
    
    except Exception as e:
        logger.error(f"Agent error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 2. Agent Pool Manager
```python
import asyncio
from typing import Optional
from dataclasses import dataclass

@dataclass
class AgentInstance:
    id: str
    agent: object
    busy: bool = False
    requests_handled: int = 0
    last_used: datetime = None

class AgentPool:
    """Manage pool of agent instances"""
    
    def __init__(self, pool_size: int = 10):
        self.pool_size = pool_size
        self.agents: List[AgentInstance] = []
        self.lock = asyncio.Lock()
        
        # Initialize pool
        for i in range(pool_size):
            agent = create_agent()  # Your agent creation logic
            self.agents.append(AgentInstance(
                id=f"agent-{i}",
                agent=agent
            ))
    
    async def acquire(self) -> Optional[AgentInstance]:
        """Get an available agent"""
        async with self.lock:
            for agent_instance in self.agents:
                if not agent_instance.busy:
                    agent_instance.busy = True
                    agent_instance.last_used = datetime.now()
                    agent_instance.requests_handled += 1
                    return agent_instance
        return None
    
    async def release(self, agent_id: str):
        """Return agent to pool"""
        async with self.lock:
            for agent_instance in self.agents:
                if agent_instance.id == agent_id:
                    agent_instance.busy = False
                    break
    
    async def scale(self, new_size: int):
        """Scale pool up or down"""
        async with self.lock:
            if new_size > self.pool_size:
                # Add agents
                for i in range(self.pool_size, new_size):
                    agent = create_agent()
                    self.agents.append(AgentInstance(
                        id=f"agent-{i}",
                        agent=agent
                    ))
            elif new_size < self.pool_size:
                # Remove idle agents
                self.agents = [
                    a for a in self.agents 
                    if not a.busy
                ][:new_size]
            
            self.pool_size = new_size
    
    def get_stats(self) -> dict:
        """Get pool statistics"""
        busy_count = sum(1 for a in self.agents if a.busy)
        return {
            'total': self.pool_size,
            'busy': busy_count,
            'available': self.pool_size - busy_count,
            'utilization': busy_count / self.pool_size
        }
```

#### 3. Message Queue
```python
import aio_pika
import json

class MessageQueue:
    """Async message queue for agent requests"""
    
    def __init__(self, rabbitmq_url: str):
        self.url = rabbitmq_url
        self.connection = None
        self.channel = None
    
    async def connect(self):
        """Connect to RabbitMQ"""
        self.connection = await aio_pika.connect_robust(self.url)
        self.channel = await self.connection.channel()
        
        # Declare queues
        self.request_queue = await self.channel.declare_queue(
            'agent_requests',
            durable=True
        )
        self.response_queue = await self.channel.declare_queue(
            'agent_responses',
            durable=True
        )
    
    async def publish_request(self, request: dict):
        """Send request to queue"""
        await self.channel.default_exchange.publish(
            aio_pika.Message(
                body=json.dumps(request).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT
            ),
            routing_key='agent_requests'
        )
    
    async def consume_requests(self, callback):
        """Process incoming requests"""
        async with self.request_queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    request = json.loads(message.body)
                    response = await callback(request)
                    await self.publish_response(response)
    
    async def publish_response(self, response: dict):
        """Send response back"""
        await self.channel.default_exchange.publish(
            aio_pika.Message(
                body=json.dumps(response).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT
            ),
            routing_key='agent_responses'
        )
```

---

## 4.2 Monitoring and Observability

### Why Monitoring Matters

In production, you need to know:
- Is the agent working?
- How fast is it responding?
- What errors are occurring?
- Are users satisfied?

### Metrics to Track

```python
from prometheus_client import Counter, Histogram, Gauge
import time

# Define metrics
REQUEST_COUNT = Counter(
    'agent_requests_total',
    'Total number of requests',
    ['status', 'endpoint']
)

REQUEST_DURATION = Histogram(
    'agent_request_duration_seconds',
    'Request duration',
    ['endpoint']
)

ACTIVE_CONNECTIONS = Gauge(
    'agent_active_connections',
    'Number of active connections'
)

TOKEN_USAGE = Counter(
    'agent_tokens_total',
    'Total tokens used',
    ['model']
)

ERROR_COUNT = Counter(
    'agent_errors_total',
    'Total errors',
    ['error_type']
)

# Instrument your agent
class MonitoredAgent:
    def __init__(self, agent):
        self.agent = agent
    
    async def process(self, message: str, context: dict = None):
        start_time = time.time()
        
        try:
            ACTIVE_CONNECTIONS.inc()
            
            result = await self.agent.process(message, context)
            
            REQUEST_COUNT.labels(status='success', endpoint='chat').inc()
            TOKEN_USAGE.labels(model=result.get('model', 'unknown')).inc(
                result.get('tokens_used', 0)
            )
            
            return result
        
        except Exception as e:
            REQUEST_COUNT.labels(status='error', endpoint='chat').inc()
            ERROR_COUNT.labels(error_type=type(e).__name__).inc()
            raise
        
        finally:
            duration = time.time() - start_time
            REQUEST_DURATION.labels(endpoint='chat').observe(duration)
            ACTIVE_CONNECTIONS.dec()
```

### Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Setup tracing
provider = TracerProvider()
processor = BatchSpanProcessor(JaegerExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

class TracedAgent:
    @tracer.start_as_current_span("agent_process")
    async def process(self, message: str, context: dict = None):
        span = trace.get_current_span()
        span.set_attribute("message_length", len(message))
        
        with tracer.start_as_current_span("perception"):
            observation = await self.perceive(message)
        
        with tracer.start_as_current_span("reasoning"):
            decision = await self.reason(observation)
        
        with tracer.start_as_current_span("action"):
            result = await self.act(decision)
        
        with tracer.start_as_current_span("response_generation"):
            response = await self.generate_response(result)
        
        return response
```

### Logging Strategy

```python
import structlog
import json

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

class LoggedAgent:
    async def process(self, message: str, context: dict = None):
        logger.info(
            "agent_request_started",
            message_length=len(message),
            context_keys=list(context.keys()) if context else []
        )
        
        try:
            result = await self.agent.process(message, context)
            
            logger.info(
                "agent_request_completed",
                steps=result.get('steps', 0),
                tokens_used=result.get('tokens_used', 0),
                confidence=result.get('confidence', 0)
            )
            
            return result
        
        except Exception as e:
            logger.error(
                "agent_request_failed",
                error=str(e),
                error_type=type(e).__name__
            )
            raise
```

### Dashboard Example (Grafana)

```yaml
# dashboard.json
{
  "dashboard": {
    "title": "Agent Performance",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [{
          "expr": "rate(agent_requests_total[5m])"
        }]
      },
      {
        "title": "P95 Latency",
        "targets": [{
          "expr": "histogram_quantile(0.95, rate(agent_request_duration_seconds_bucket[5m]))"
        }]
      },
      {
        "title": "Error Rate",
        "targets": [{
          "expr": "rate(agent_errors_total[5m]) / rate(agent_requests_total[5m])"
        }]
      },
      {
        "title": "Token Usage",
        "targets": [{
          "expr": "rate(agent_tokens_total[5m])"
        }]
      }
    ]
  }
}
```

---

## 4.3 Scaling Strategies

### Horizontal Scaling

Run multiple agent instances behind a load balancer:

```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
  
  agent-1:
    build: .
    environment:
      - AGENT_ID=1
    deploy:
      replicas: 10
  
  redis:
    image: redis:alpine
  
  rabbitmq:
    image: rabbitmq:3-management
  
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
  
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

### Auto-Scaling

```python
from kubernetes import client, config

class AutoScaler:
    """Auto-scale agent deployment based on load"""
    
    def __init__(self, namespace: str = 'default'):
        config.load_incluster_config()
        self.apps_v1 = client.AppsV1Api()
        self.namespace = namespace
    
    def scale(self, deployment_name: str, target_replicas: int):
        """Scale deployment to target replicas"""
        deployment = self.apps_v1.read_namespaced_deployment(
            name=deployment_name,
            namespace=self.namespace
        )
        
        deployment.spec.replicas = target_replicas
        
        self.apps_v1.patch_namespaced_deployment(
            name=deployment_name,
            namespace=self.namespace,
            body=deployment
        )
    
    def auto_scale(self, deployment_name: str, metrics: dict):
        """Auto-scale based on metrics"""
        current_replicas = metrics['current_replicas']
        utilization = metrics['cpu_utilization']
        queue_depth = metrics['queue_depth']
        
        # Scale up if overloaded
        if utilization > 80 or queue_depth > 100:
            target = min(current_replicas * 2, 100)  # Max 100 replicas
            self.scale(deployment_name, target)
        
        # Scale down if underutilized
        elif utilization < 30 and queue_depth < 10:
            target = max(current_replicas // 2, 1)  # Min 1 replica
            self.scale(deployment_name, target)
```

### Caching Strategies

```python
import redis
import hashlib
import json

class ResponseCache:
    """Cache agent responses to reduce load"""
    
    def __init__(self, redis_url: str, ttl: int = 3600):
        self.redis = redis.from_url(redis_url)
        self.ttl = ttl
    
    def _generate_key(self, message: str, context: dict) -> str:
        """Generate cache key"""
        content = f"{message}:{json.dumps(context, sort_keys=True)}"
        return f"agent_cache:{hashlib.md5(content.encode()).hexdigest()}"
    
    async def get(self, message: str, context: dict = None) -> Optional[str]:
        """Get cached response"""
        key = self._generate_key(message, context or {})
        cached = self.redis.get(key)
        return cached.decode() if cached else None
    
    async def set(self, message: str, response: str, context: dict = None):
        """Cache response"""
        key = self._generate_key(message, context or {})
        self.redis.setex(key, self.ttl, response)
    
    async def invalidate(self, pattern: str):
        """Invalidate cache entries"""
        keys = self.redis.keys(f"agent_cache:{pattern}*")
        if keys:
            self.redis.delete(*keys)

# Use in agent
class CachedAgent:
    def __init__(self, agent, cache: ResponseCache):
        self.agent = agent
        self.cache = cache
    
    async def process(self, message: str, context: dict = None):
        # Check cache first
        cached = await self.cache.get(message, context)
        if cached:
            return json.loads(cached)
        
        # Process normally
        result = await self.agent.process(message, context)
        
        # Cache successful responses
        if result.get('cacheable', True):
            await self.cache.set(message, json.dumps(result), context)
        
        return result
```

---

## 4.4 Cost Optimization

### Token Usage Optimization

```python
class TokenOptimizer:
    """Optimize LLM token usage"""
    
    def __init__(self, max_tokens: int = 4000):
        self.max_tokens = max_tokens
    
    def truncate_context(self, messages: list) -> list:
        """Truncate context to fit token limit"""
        total_tokens = sum(len(m['content'].split()) * 1.3 for m in messages)
        
        while total_tokens > self.max_tokens and len(messages) > 1:
            # Remove oldest message
            removed = messages.pop(0)
            total_tokens -= len(removed['content'].split()) * 1.3
        
        return messages
    
    def compress_message(self, message: str) -> str:
        """Compress message while preserving meaning"""
        # Remove unnecessary whitespace
        message = ' '.join(message.split())
        
        # Truncate if still too long
        if len(message.split()) * 1.3 > self.max_tokens:
            message = ' '.join(message.split()[:int(self.max_tokens/1.3)])
        
        return message
    
    def estimate_cost(self, tokens: int, model: str) -> float:
        """Estimate cost for token count"""
        pricing = {
            'gpt-4': 0.03 / 1000,  # $0.03 per 1K tokens
            'gpt-3.5-turbo': 0.002 / 1000,
            'claude-3': 0.015 / 1000,
        }
        return tokens * pricing.get(model, 0.002 / 1000)
```

### Model Selection Strategy

```python
class ModelRouter:
    """Route requests to appropriate model based on complexity"""
    
    def __init__(self):
        self.models = {
            'simple': {'model': 'gpt-3.5-turbo', 'max_tokens': 500},
            'medium': {'model': 'gpt-4', 'max_tokens': 2000},
            'complex': {'model': 'gpt-4', 'max_tokens': 4000},
        }
    
    def classify_complexity(self, message: str) -> str:
        """Classify message complexity"""
        word_count = len(message.split())
        
        if word_count < 10 and '?' not in message:
            return 'simple'
        elif word_count < 50:
            return 'medium'
        else:
            return 'complex'
    
    def route(self, message: str) -> dict:
        """Route to appropriate model"""
        complexity = self.classify_complexity(message)
        return self.models[complexity]
```

### Batch Processing

```python
class BatchProcessor:
    """Process multiple requests together for efficiency"""
    
    def __init__(self, batch_size: int = 10, max_wait: float = 1.0):
        self.batch_size = batch_size
        self.max_wait = max_wait
        self.queue = asyncio.Queue()
        self.results = {}
    
    async def submit(self, request_id: str, message: str) -> str:
        """Submit request for batch processing"""
        await self.queue.put((request_id, message))
        
        # Wait for result
        while request_id not in self.results:
            await asyncio.sleep(0.1)
        
        return self.results.pop(request_id)
    
    async def process_batches(self, agent):
        """Process requests in batches"""
        while True:
            # Collect batch
            batch = []
            start_time = time.time()
            
            while len(batch) < self.batch_size:
                try:
                    item = await asyncio.wait_for(
                        self.queue.get(),
                        timeout=self.max_wait - (time.time() - start_time)
                    )
                    batch.append(item)
                except asyncio.TimeoutError:
                    break
            
            if not batch:
                continue
            
            # Process batch
            request_ids, messages = zip(*batch)
            results = await agent.process_batch(list(messages))
            
            # Store results
            for request_id, result in zip(request_ids, results):
                self.results[request_id] = result
```

---

## 4.5 Security Best Practices

### Authentication & Authorization

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()

async def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> str:
    """Verify JWT token"""
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=['HS256']
        )
        user_id = payload.get('sub')
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid token'
            )
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token'
        )

@app.post("/agent/chat")
async def chat(
    request: AgentRequest,
    user_id: str = Depends(verify_token)
):
    """Authenticated chat endpoint"""
    # user_id is verified and available
    ...
```

### Input Sanitization

```python
import bleach

class InputSanitizer:
    """Sanitize all user inputs"""
    
    @staticmethod
    def sanitize_text(text: str) -> str:
        """Remove potentially dangerous content"""
        # Remove HTML tags
        text = bleach.clean(text, tags=[], strip=True)
        
        # Limit length
        if len(text) > 10000:
            text = text[:10000]
        
        return text
    
    @staticmethod
    def validate_json(json_str: str) -> dict:
        """Validate and parse JSON safely"""
        try:
            data = json.loads(json_str)
            # Ensure it's a dict, not arbitrary object
            if not isinstance(data, dict):
                raise ValueError("JSON must be an object")
            return data
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON")
```

### Rate Limiting by User

```python
from slowapi import SlowApi, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()
slowapi = SlowApi()
app.state.limiter = slowapi
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/agent/chat")
@slowapi.limit("60/minute")  # 60 requests per minute
async def chat(request: AgentRequest):
    ...
```

---

## 4.6 Real-World Projects

### Project 1: Customer Support Agent

Complete implementation:

```python
class CustomerSupportAgent:
    """Production customer support agent"""
    
    def __init__(self):
        self.tools = {
            'lookup_order': self.lookup_order,
            'process_refund': self.process_refund,
            'schedule_pickup': self.schedule_pickup,
            'escalate_to_human': self.escalate_to_human,
        }
        self.memory = AgentMemory()
        self.safety = SafetySystem()
    
    async def handle_ticket(self, ticket: dict) -> dict:
        """Handle a support ticket"""
        # Safety check
        safety_result = self.safety.check_request(
            ticket['user_id'],
            ticket['message']
        )
        if not safety_result['safe']:
            return {'status': 'rejected', 'reason': safety_result['reason']}
        
        # Look up customer history
        history = self.memory.long_term.retrieve(category=ticket['user_id'])
        
        # Process with ReAct
        response = await self.react_loop(ticket['message'], history)
        
        # Log interaction
        self.memory.episodic.record(
            situation=ticket['message'],
            action=response['action'],
            outcome=response['result'],
            reward=1 if response['resolved'] else -1
        )
        
        return response
```

### Project 2: Research Assistant

```python
class ResearchAssistant:
    """Multi-step research agent"""
    
    def __init__(self):
        self.sources = ['google_scholar', 'arxiv', 'pubmed']
        self.summarizer = TextSummarizer()
    
    async def research(self, topic: str, depth: int = 3) -> dict:
        """Conduct comprehensive research"""
        results = []
        
        # Search multiple sources
        for source in self.sources:
            papers = await self.search_source(source, topic)
            results.extend(papers[:depth])
        
        # Summarize each
        summaries = []
        for paper in results:
            summary = await self.summarizer.summarize(paper['abstract'])
            summaries.append({
                'title': paper['title'],
                'summary': summary,
                'relevance': paper['relevance_score']
            })
        
        # Synthesize findings
        synthesis = await self.synthesize(summaries)
        
        return {
            'topic': topic,
            'papers_found': len(results),
            'summaries': summaries,
            'synthesis': synthesis,
            'references': [p['citation'] for p in results]
        }
```

### Project 3: Multi-Agent Collaboration

```python
class DevelopmentTeam:
    """Multi-agent software development team"""
    
    def __init__(self):
        self.agents = {
            'architect': ArchitectAgent(),
            'developer': DeveloperAgent(),
            'reviewer': ReviewerAgent(),
            'tester': TesterAgent(),
        }
        self.blackboard = Blackboard()
    
    async def build_feature(self, requirement: str) -> dict:
        """Build a feature through collaboration"""
        # Architect designs
        design = await self.agents['architect'].design(requirement)
        self.blackboard.post('design', design)
        
        # Developer implements
        code = await self.agents['developer'].implement(design)
        self.blackboard.post('code', code)
        
        # Reviewer checks
        review = await self.agents['reviewer'].review(code)
        if review['needs_changes']:
            code = await self.agents['developer'].revise(code, review)
        
        # Tester validates
        test_results = await self.agents['tester'].test(code)
        
        return {
            'requirement': requirement,
            'design': design,
            'code': code,
            'review': review,
            'tests': test_results,
            'status': 'complete' if test_results['passed'] else 'failed'
        }
```

---

## 4.7 Glossary

| Term | Definition |
|------|------------|
| **API Gateway** | Entry point for all API requests |
| **Load Balancer** | Distributes traffic across instances |
| **Auto-Scaling** | Automatically adjusts resources based on load |
| **Observability** | Ability to understand internal state from outputs |
| **Distributed Tracing** | Tracking requests across services |
| **Token Optimization** | Reducing LLM token usage |
| **Rate Limiting** | Restricting request frequency |
| **Horizontal Scaling** | Adding more instances |
| **Message Queue** | Async communication between services |
| **Cache Hit** | Request served from cache |

---

## 4.8 Exercises

### Exercise 1: Deploy a Simple Agent (Medium)
Containerize your agent and deploy it with Docker. Add basic monitoring.

### Exercise 2: Implement Auto-Scaling (Hard)
Set up Kubernetes deployment with HPA (Horizontal Pod Autoscaler) based on CPU/memory.

### Exercise 3: Build Complete Support System (Challenge)
Create a full customer support system with authentication, rate limiting, caching, and monitoring.

---

## 4.9 Troubleshooting

### Problem: High latency in production
**Solution:** Check bottlenecks with tracing, add caching, optimize prompts

### Problem: Running out of memory
**Solution:** Reduce context size, implement streaming, scale horizontally

### Problem: Inconsistent responses
**Solution:** Set temperature=0, use system prompts, add validation

### Problem: Costs too high
**Solution:** Use model routing, cache responses, optimize token usage

---

## 4.10 Conclusion

Congratulations! You've completed the Agentic Systems guide. You now know how to:

✅ Build agents from scratch  
✅ Choose appropriate architectures  
✅ Add memory and self-reflection  
✅ Implement safety guardrails  
✅ Deploy to production  
✅ Monitor and scale  
✅ Optimize costs  

**Next Steps:**
- Join the agent community
- Contribute to open-source projects
- Build your own production system
- Share your learnings!

**Resources:**
- LangChain documentation
- AutoGen GitHub
- Agent evaluation benchmarks
- Production deployment guides

Happy building! 🚀
