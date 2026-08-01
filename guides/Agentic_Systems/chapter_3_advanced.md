# Chapter 3: Advanced Capabilities

## 🎯 Chapter Overview

**What You'll Learn:**
- Advanced tool integration patterns
- Memory systems (short-term, long-term, episodic)
- Self-reflection and learning from mistakes
- Safety mechanisms and guardrails
- Evaluation frameworks for agents

**By the End:** You'll be able to build sophisticated agents with memory, self-improvement, and safety features!

**Time Estimate:** 5-7 hours

**Prerequisites:** Chapters 1-2

---

## 3.1 Advanced Tool Integration

### Beyond Simple Functions

In Chapter 1, we used simple Python functions as tools. Now let's explore production-ready tool patterns.

### Tool Categories

#### 1. API Tools
```python
class APITool:
    """Wrapper for REST API calls"""
    
    def __init__(self, base_url: str, auth_token: str = None):
        self.base_url = base_url
        self.session = requests.Session()
        if auth_token:
            self.session.headers['Authorization'] = f'Bearer {auth_token}'
    
    def call(self, endpoint: str, method: str = 'GET', **kwargs) -> dict:
        """Make API call with error handling and retries"""
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(3):
            try:
                response = self.session.request(method, url, **kwargs, timeout=10)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return {}
```

#### 2. Database Tools
```python
class DatabaseTool:
    """Safe database query tool"""
    
    def __init__(self, connection_string: str):
        self.conn = psycopg2.connect(connection_string)
    
    def query(self, sql: str, params: tuple = None) -> list:
        """Execute read-only query with validation"""
        # Validate SQL is SELECT only
        if not sql.strip().upper().startswith('SELECT'):
            raise ValueError("Only SELECT queries allowed")
        
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    
    def safe_query(self, table: str, filters: dict) -> list:
        """Build safe query from parameters"""
        # Prevent SQL injection
        columns = ', '.join(filters.keys())
        placeholders = ', '.join(['%s'] * len(filters))
        values = tuple(filters.values())
        
        sql = f"SELECT * FROM {table} WHERE {columns} = ({placeholders})"
        return self.query(sql, values)
```

#### 3. Code Execution Tools
```python
class CodeExecutionTool:
    """Sandboxed code execution"""
    
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
    
    def execute_python(self, code: str, context: dict = None) -> dict:
        """Execute Python code safely"""
        import ast
        import sys
        from io import StringIO
        
        # Validate code doesn't contain dangerous operations
        dangerous_patterns = ['__import__', 'eval(', 'exec(', 'open(', 'os.']
        for pattern in dangerous_patterns:
            if pattern in code:
                return {'error': f'Dangerous pattern detected: {pattern}'}
        
        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            # Execute with limited globals
            safe_globals = {'__builtins__': {'min': min, 'max': max, 'sum': sum}}
            local_context = context or {}
            
            exec(code, safe_globals, local_context)
            output = sys.stdout.getvalue()
            
            return {
                'success': True,
                'output': output,
                'variables': {k: v for k, v in local_context.items() if not k.startswith('_')}
            }
        except Exception as e:
            return {'error': str(e)}
        finally:
            sys.stdout = old_stdout
```

### Tool Registration System

```python
class ToolRegistry:
    """Central registry for all available tools"""
    
    def __init__(self):
        self.tools = {}
        self.tool_schemas = {}
    
    def register(self, name: str, func: callable, schema: dict, description: str):
        """Register a tool with metadata"""
        self.tools[name] = func
        self.tool_schemas[name] = {
            'name': name,
            'description': description,
            'parameters': schema
        }
    
    def get_tool(self, name: str) -> callable:
        """Retrieve tool by name"""
        if name not in self.tools:
            raise KeyError(f"Tool '{name}' not found")
        return self.tools[name]
    
    def get_schema(self, name: str) -> dict:
        """Get tool schema for LLM prompting"""
        return self.tool_schemas.get(name, {})
    
    def list_tools(self) -> list:
        """List all available tools"""
        return list(self.tools.keys())


# Usage example
registry = ToolRegistry()

registry.register(
    name='get_weather',
    func=get_weather_api,
    schema={
        'type': 'object',
        'properties': {
            'city': {'type': 'string', 'description': 'City name'}
        },
        'required': ['city']
    },
    description='Get current weather for a city'
)
```

---

## 3.2 Memory Systems

### Why Memory Matters

Without memory, agents are amnesiac—every interaction starts from zero. Memory enables:
- Context awareness
- Learning from experience
- Personalization
- Multi-turn conversations

### Types of Memory

#### 1. Short-Term Memory (Working Memory)
Holds information for current task only.

```python
class ShortTermMemory:
    """Context window for current conversation"""
    
    def __init__(self, max_tokens: int = 4000):
        self.messages = []
        self.max_tokens = max_tokens
        self.current_tokens = 0
    
    def add(self, role: str, content: str):
        """Add message, removing oldest if needed"""
        token_count = len(content.split()) * 1.3  # Approximate
        
        while self.current_tokens + token_count > self.max_tokens:
            if self.messages:
                removed = self.messages.pop(0)
                self.current_tokens -= len(removed['content'].split()) * 1.3
            else:
                break
        
        self.messages.append({'role': role, 'content': content})
        self.current_tokens += token_count
    
    def get_context(self) -> list:
        """Get full conversation history"""
        return self.messages
    
    def clear(self):
        """Reset memory"""
        self.messages = []
        self.current_tokens = 0
```

#### 2. Long-Term Memory (Persistent Storage)
Stores information across sessions.

```python
class LongTermMemory:
    """Persistent knowledge storage"""
    
    def __init__(self, storage_path: str = 'memory.db'):
        self.db = sqlite3.connect(storage_path)
        self._initialize_tables()
    
    def _initialize_tables(self):
        """Create database tables"""
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY,
                key TEXT UNIQUE,
                value TEXT,
                category TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db.commit()
    
    def store(self, key: str, value: str, category: str = 'general'):
        """Store a fact"""
        cursor = self.db.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO facts (key, value, category)
            VALUES (?, ?, ?)
        ''', (key, value, category))
        self.db.commit()
    
    def retrieve(self, key: str = None, category: str = None) -> dict:
        """Retrieve facts by key or category"""
        cursor = self.db.cursor()
        
        if key:
            cursor.execute('SELECT key, value FROM facts WHERE key = ?', (key,))
        elif category:
            cursor.execute('SELECT key, value FROM facts WHERE category = ?', (category,))
        else:
            cursor.execute('SELECT key, value FROM facts')
        
        return dict(cursor.fetchall())
    
    def search(self, query: str) -> list:
        """Semantic search through memories"""
        # In production, use vector embeddings
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT key, value FROM facts 
            WHERE value LIKE ?
        ''', (f'%{query}%',))
        return cursor.fetchall()
```

#### 3. Episodic Memory (Experience Records)
Remembers specific events and interactions.

```python
class EpisodicMemory:
    """Records of specific experiences"""
    
    def __init__(self):
        self.episodes = []
    
    def record(self, situation: str, action: str, outcome: str, reward: float = 0):
        """Record an episode"""
        episode = {
            'situation': situation,
            'action': action,
            'outcome': outcome,
            'reward': reward,
            'timestamp': datetime.now()
        }
        self.episodes.append(episode)
    
    def find_similar(self, situation: str, top_k: int = 5) -> list:
        """Find similar past experiences"""
        # Simple keyword matching (use embeddings in production)
        situation_words = set(situation.lower().split())
        
        scored = []
        for ep in self.episodes:
            ep_words = set(ep['situation'].lower().split())
            overlap = len(situation_words & ep_words)
            scored.append((overlap, ep))
        
        scored.sort(reverse=True)
        return [ep for _, ep in scored[:top_k]]
    
    def learn_from_outcomes(self):
        """Analyze episodes to improve future decisions"""
        successful_actions = {}
        
        for ep in self.episodes:
            if ep['reward'] > 0:
                action = ep['action']
                successful_actions[action] = successful_actions.get(action, 0) + 1
        
        return successful_actions
```

### Unified Memory Architecture

Combine all memory types:

```python
class AgentMemory:
    """Unified memory system"""
    
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.episodic = EpisodicMemory()
    
    def process_interaction(self, user_input: str, agent_response: str, outcome: str = ''):
        """Process and store an interaction"""
        # Add to short-term
        self.short_term.add('user', user_input)
        self.short_term.add('assistant', agent_response)
        
        # Extract and store important facts
        facts = self._extract_facts(user_input, agent_response)
        for key, value in facts.items():
            self.long_term.store(key, value)
        
        # Record episode if there was an outcome
        if outcome:
            reward = self._evaluate_outcome(outcome)
            self.episodic.record(user_input, agent_response, outcome, reward)
    
    def get_relevant_context(self, query: str) -> dict:
        """Retrieve all relevant memories"""
        return {
            'conversation': self.short_term.get_context(),
            'facts': self.long_term.search(query),
            'similar_experiences': self.episodic.find_similar(query)
        }
    
    def _extract_facts(self, input_text: str, response: str) -> dict:
        """Extract storable facts from conversation"""
        # Use NLP or LLM to extract facts
        # For demo, simple pattern matching
        facts = {}
        
        # Pattern: "My name is X"
        if 'my name is' in input_text.lower():
            name = input_text.lower().split('my name is')[1].strip()
            facts['user_name'] = name
        
        return facts
    
    def _evaluate_outcome(self, outcome: str) -> float:
        """Evaluate if outcome was positive"""
        positive_words = ['success', 'completed', 'done', 'great', 'thanks']
        negative_words = ['error', 'failed', 'wrong', 'bad', 'disappointed']
        
        score = 0
        for word in positive_words:
            if word in outcome.lower():
                score += 1
        for word in negative_words:
            if word in outcome.lower():
                score -= 1
        
        return score
```

---

## 3.3 Self-Reflection and Learning

### What is Self-Reflection?

Self-reflection allows agents to:
- Evaluate their own performance
- Learn from mistakes
- Improve over time
- Adapt strategies

### Reflection Loop

```python
class ReflectiveAgent:
    """Agent that learns from its actions"""
    
    def __init__(self):
        self.memory = AgentMemory()
        self.performance_log = []
    
    def act(self, situation: str) -> str:
        """Take action with reflection"""
        # Get relevant context
        context = self.memory.get_relevant_context(situation)
        
        # Check similar past experiences
        similar = context['similar_experiences']
        if similar:
            best_action = self._select_best_from_experience(similar)
            action = best_action
        else:
            action = self._decide_action(situation)
        
        return action
    
    def reflect(self, situation: str, action: str, outcome: str):
        """Reflect on the outcome and learn"""
        # Evaluate outcome
        success = self._evaluate_success(outcome)
        
        # Store episode
        self.memory.episodic.record(situation, action, outcome, reward=1 if success else -1)
        
        # Analyze what went well/poorly
        if not success:
            analysis = self._analyze_failure(situation, action, outcome)
            self._update_strategy(analysis)
        
        # Log for tracking
        self.performance_log.append({
            'situation': situation,
            'action': action,
            'outcome': outcome,
            'success': success,
            'timestamp': datetime.now()
        })
    
    def _analyze_failure(self, situation: str, action: str, outcome: str) -> dict:
        """Analyze why something failed"""
        analysis = {
            'situation_factors': self._identify_situation_factors(situation),
            'action_appropriateness': self._evaluate_action_choice(action, situation),
            'execution_issues': self._check_execution_problems(outcome),
            'alternative_actions': self._generate_alternatives(situation)
        }
        return analysis
    
    def _update_strategy(self, analysis: dict):
        """Update decision-making based on analysis"""
        # In production, update model weights or rules
        # For demo, log insights
        print("Learning from failure:")
        print(f"  Situation factors: {analysis['situation_factors']}")
        print(f"  Better alternatives: {analysis['alternative_actions']}")
```

### Implementation Patterns

#### Pattern 1: Post-Action Review
```python
def post_action_review(agent, task, result):
    """Review after each action"""
    
    review = {
        'task': task,
        'result': result,
        'expected': agent.expected_outcome,
        'actual': result,
        'gap': calculate_gap(agent.expected_outcome, result),
        'lessons': []
    }
    
    if review['gap'] > threshold:
        review['lessons'] = generate_lessons(task, result)
        agent.update_knowledge(review['lessons'])
    
    return review
```

#### Pattern 2: Periodic Self-Assessment
```python
def periodic_assessment(agent, window_size=100):
    """Assess performance over recent interactions"""
    
    recent = agent.performance_log[-window_size:]
    
    metrics = {
        'success_rate': sum(1 for r in recent if r['success']) / len(recent),
        'avg_steps': np.mean([len(r.get('steps', [])) for r in recent]),
        'common_failures': identify_common_failures(recent),
        'improvement_trend': calculate_trend(recent)
    }
    
    if metrics['success_rate'] < 0.7:
        agent.trigger_retraining()
    
    return metrics
```

#### Pattern 3: Counterfactual Reasoning
```python
def counterfactual_analysis(agent, situation, actual_action, outcome):
    """Consider what would have happened with different actions"""
    
    alternatives = generate_alternative_actions(situation)
    
    simulations = []
    for alt_action in alternatives:
        simulated_outcome = simulate_outcome(situation, alt_action)
        simulations.append({
            'action': alt_action,
            'simulated_outcome': simulated_outcome,
            'better_than_actual': evaluate_better(simulated_outcome, outcome)
        })
    
    best_alternative = max(simulations, key=lambda x: x['simulated_outcome']['score'])
    
    if best_alternative['better_than_actual']:
        agent.learn_preferred_action(situation, best_alternative['action'])
```

---

## 3.4 Safety and Guardrails

### Why Safety Matters

Agents can take real actions in the world. Safety prevents:
- Harmful actions
- Security breaches
- Privacy violations
- Unintended consequences

### Layers of Safety

#### Layer 1: Input Validation
```python
class InputValidator:
    """Validate all inputs before processing"""
    
    @staticmethod
    def validate_user_input(text: str) -> bool:
        """Check for malicious input"""
        
        # Check length
        if len(text) > 10000:
            return False
        
        # Check for injection patterns
        dangerous_patterns = [
            r'<script>',
            r'SELECT.*FROM',
            r'DROP\s+TABLE',
            r'rm\s+-rf',
            r'__import__',
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return False
        
        return True
    
    @staticmethod
    def sanitize(text: str) -> str:
        """Sanitize input"""
        # Remove potentially dangerous characters
        sanitized = html.escape(text)
        return sanitized
```

#### Layer 2: Action Approval
```python
class ActionApprover:
    """Require approval for sensitive actions"""
    
    def __init__(self):
        self.sensitive_actions = {
            'delete': {'requires_approval': True, 'risk_level': 'high'},
            'transfer_money': {'requires_approval': True, 'risk_level': 'critical'},
            'send_email': {'requires_approval': False, 'risk_level': 'low'},
            'read_file': {'requires_approval': False, 'risk_level': 'medium'},
        }
    
    def check(self, action: str, parameters: dict) -> dict:
        """Check if action requires approval"""
        
        action_info = self.sensitive_actions.get(action, {'requires_approval': False})
        
        if action_info['requires_approval']:
            return {
                'approved': False,
                'requires_human_approval': True,
                'risk_level': action_info['risk_level'],
                'reason': f"Action '{action}' requires human approval"
            }
        
        # Additional checks
        if action_info['risk_level'] == 'critical':
            return {
                'approved': False,
                'requires_human_approval': True,
                'risk_level': 'critical'
            }
        
        return {'approved': True}
```

#### Layer 3: Output Filtering
```python
class OutputFilter:
    """Filter agent outputs before delivery"""
    
    def __init__(self):
        self.forbidden_topics = [
            'instructions for illegal activities',
            'hate speech',
            'personal information requests',
        ]
    
    def filter(self, text: str) -> str:
        """Filter inappropriate content"""
        
        # Check for forbidden topics
        for topic in self.forbidden_topics:
            if topic.lower() in text.lower():
                return "[Content filtered for safety]"
        
        # Check for PII leakage
        pii_patterns = [
            r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
            r'\b\d{16}\b',  # Credit card
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
        ]
        
        for pattern in pii_patterns:
            text = re.sub(pattern, '[REDACTED]', text)
        
        return text
```

#### Layer 4: Rate Limiting
```python
class RateLimiter:
    """Prevent abuse through rate limiting"""
    
    def __init__(self, max_requests_per_minute=60):
        self.max_rpm = max_requests_per_minute
        self.request_times = []
    
    def check_rate_limit(self, user_id: str) -> bool:
        """Check if user has exceeded rate limit"""
        now = time.time()
        minute_ago = now - 60
        
        # Remove old requests
        self.request_times = [t for t in self.request_times if t > minute_ago]
        
        if len(self.request_times) >= self.max_rpm:
            return False
        
        self.request_times.append(now)
        return True
```

### Comprehensive Safety System

```python
class SafetySystem:
    """Multi-layer safety for agents"""
    
    def __init__(self):
        self.input_validator = InputValidator()
        self.action_approver = ActionApprover()
        self.output_filter = OutputFilter()
        self.rate_limiter = RateLimiter()
    
    def check_request(self, user_id: str, input_text: str) -> dict:
        """Comprehensive safety check"""
        
        # Rate limiting
        if not self.rate_limiter.check_rate_limit(user_id):
            return {'safe': False, 'reason': 'Rate limit exceeded'}
        
        # Input validation
        if not self.input_validator.validate_user_input(input_text):
            return {'safe': False, 'reason': 'Invalid input detected'}
        
        return {'safe': True}
    
    def check_action(self, action: str, parameters: dict) -> dict:
        """Check if action is safe to execute"""
        return self.action_approver.check(action, parameters)
    
    def filter_response(self, response: str) -> str:
        """Filter response before sending to user"""
        return self.output_filter.filter(response)
```

---

## 3.5 Evaluation Frameworks

### Why Evaluate Agents?

Evaluation helps you:
- Measure performance
- Identify weaknesses
- Compare architectures
- Track improvements

### Key Metrics

#### 1. Task Success Rate
```python
def calculate_success_rate(results: list) -> float:
    """Percentage of tasks completed successfully"""
    successful = sum(1 for r in results if r['success'])
    return successful / len(results) if results else 0
```

#### 2. Efficiency Metrics
```python
def calculate_efficiency(results: list) -> dict:
    """Measure resource usage"""
    return {
        'avg_steps': np.mean([r['steps'] for r in results]),
        'avg_time': np.mean([r['duration'] for r in results]),
        'avg_tokens': np.mean([r['tokens_used'] for r in results]),
        'cost_per_task': np.mean([r['cost'] for r in results])
    }
```

#### 3. Quality Metrics
```python
def evaluate_quality(results: list) -> dict:
    """Measure output quality"""
    return {
        'accuracy': calculate_accuracy(results),
        'completeness': calculate_completeness(results),
        'coherence': calculate_coherence(results),
        'user_satisfaction': calculate_satisfaction(results)
    }
```

### Evaluation Pipeline

```python
class AgentEvaluator:
    """Comprehensive agent evaluation"""
    
    def __init__(self, test_suite: list):
        self.test_suite = test_suite
        self.results = []
    
    def run_evaluation(self, agent) -> dict:
        """Run full evaluation suite"""
        
        for test in self.test_suite:
            result = self.run_single_test(agent, test)
            self.results.append(result)
        
        return self.generate_report()
    
    def run_single_test(self, agent, test: dict) -> dict:
        """Run individual test case"""
        start_time = time.time()
        
        try:
            response = agent.run(test['input'])
            success = self.verify_output(response, test['expected'])
            
            return {
                'test_name': test['name'],
                'success': success,
                'steps': agent.steps_taken,
                'duration': time.time() - start_time,
                'response': response
            }
        except Exception as e:
            return {
                'test_name': test['name'],
                'success': False,
                'error': str(e)
            }
    
    def verify_output(self, actual, expected) -> bool:
        """Verify output matches expectations"""
        if isinstance(expected, dict):
            return all(actual.get(k) == v for k, v in expected.items())
        return actual == expected
    
    def generate_report(self) -> dict:
        """Generate evaluation report"""
        return {
            'total_tests': len(self.results),
            'passed': sum(1 for r in self.results if r['success']),
            'failed': sum(1 for r in self.results if not r['success']),
            'success_rate': calculate_success_rate(self.results),
            'efficiency': calculate_efficiency([r for r in self.results if r['success']]),
            'detailed_results': self.results
        }
```

### Benchmark Datasets

Create standardized test sets:

```python
BENCHMARK_SUITE = [
    {
        'name': 'simple_lookup',
        'input': 'What is the capital of France?',
        'expected': 'Paris'
    },
    {
        'name': 'multi_step_reasoning',
        'input': 'If John has 5 apples and buys 3 more, then gives half away, how many left?',
        'expected': '4'
    },
    {
        'name': 'tool_use',
        'input': 'What\'s the weather in Tokyo?',
        'expected': {'action': 'get_weather', 'city': 'Tokyo'}
    },
    {
        'name': 'context_retention',
        'input': 'Remember my name is Alice. What is my name?',
        'expected': 'Alice'
    },
]
```

---

## 3.6 Glossary

| Term | Definition |
|------|------------|
| **Short-Term Memory** | Temporary storage for current conversation |
| **Long-Term Memory** | Persistent storage across sessions |
| **Episodic Memory** | Records of specific experiences |
| **Self-Reflection** | Agent evaluating its own performance |
| **Guardrails** | Safety mechanisms preventing harmful actions |
| **Input Validation** | Checking inputs for safety |
| **Action Approval** | Requiring authorization for sensitive actions |
| **Rate Limiting** | Preventing abuse through request limits |
| **Success Rate** | Percentage of tasks completed successfully |
| **Efficiency** | Resource usage (time, tokens, cost) |

---

## 3.7 Exercises

### Exercise 1: Build a Memory System (Medium)
Implement a unified memory system with short-term, long-term, and episodic components. Test it with multi-turn conversations.

### Exercise 2: Add Self-Reflection (Hard)
Modify an existing agent to reflect on failures and improve. Track improvement over multiple iterations.

### Exercise 3: Implement Safety Layer (Challenge)
Create a comprehensive safety system with input validation, action approval, and output filtering. Test with adversarial inputs.

---

## 3.8 Troubleshooting

### Problem: Memory grows unbounded
**Solution:** Implement TTL (time-to-live) and size limits
```python
if len(memory) > MAX_SIZE:
    memory = memory[-MAX_SIZE:]
```

### Problem: Agent refuses safe actions
**Solution:** Tune safety thresholds and add whitelists
```python
whitelist = ['read_public_data', 'calculate']
if action in whitelist:
    skip_approval = True
```

### Problem: Evaluation is too slow
**Solution:** Parallelize tests and use sampling
```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(run_test, test_suite)
```

---

## 3.9 What's Next?

In this chapter you learned:
- ✅ Advanced tool integration patterns
- ✅ Memory systems (short-term, long-term, episodic)
- ✅ Self-reflection and learning
- ✅ Safety mechanisms and guardrails
- ✅ Evaluation frameworks

**In Chapter 4**, we'll build complete production systems with deployment, monitoring, and scaling!

**Continue to** [Chapter 4: Production Deployment](chapter_4_production.md)!
