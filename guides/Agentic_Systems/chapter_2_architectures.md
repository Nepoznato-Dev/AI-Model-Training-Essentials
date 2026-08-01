# Chapter 2: Agent Architectures

## 🎯 Chapter Overview

**What You'll Learn:**
- ReAct pattern: Reasoning + Acting in loops
- Plan-and-Execute architecture
- Multi-Agent collaboration systems
- Hierarchical agent structures
- How to choose the right architecture

**By the End:** You'll be able to design and implement different agent architectures for various use cases!

**Time Estimate:** 4-6 hours

**Prerequisites:** Chapter 1 (Agent Fundamentals)

---

## 2.1 Why Do We Need Different Architectures?

### One Size Doesn't Fit All

Just like you wouldn't use a hammer to screw in a bolt, different tasks require different agent architectures:

| Task Type | Best Architecture | Why? |
|-----------|------------------|------|
| Simple Q&A | Single-step agent | Direct response needed |
| Math problems | ReAct | Need to reason through steps |
| Trip planning | Plan-and-Execute | Requires upfront strategy |
| Software development | Multi-Agent | Different specialties needed |
| Enterprise automation | Hierarchical | Coordination across teams |

### Key Insight

**Architecture = Strategy for organizing agent thinking and actions**

The right architecture makes your agent:
- ✅ More efficient (fewer steps)
- ✅ More accurate (better decisions)
- ✅ More reliable (fewer errors)
- ✅ Easier to debug (clearer structure)

---

## 2.2 ReAct Pattern: Reason + Act

### What is ReAct?

**ReAct** = **Re**asoning + **Act**ing

Instead of doing all reasoning upfront OR all acting upfront, ReAct interleaves them:

```
Think → Act → Observe → Think → Act → Observe → ... → Answer
```

### Why ReAct Works

Research shows that combining reasoning and acting leads to better performance than either alone:

| Approach | Accuracy on Complex Tasks |
|----------|--------------------------|
| Act-only | 52% |
| Reason-only | 38% |
| **ReAct (combined)** | **73%** |

### The ReAct Loop

```python
def react_loop(question, max_steps=10):
    """
    ReAct: Reason + Act in alternating steps
    """
    thoughts = []
    
    for step in range(max_steps):
        # STEP 1: REASON (Think)
        thought = llm_generate_thought(question, thoughts)
        thoughts.append(f"Thought: {thought}")
        
        # Check if we have enough info to answer
        if "answer" in thought.lower() or "final" in thought.lower():
            return extract_answer(thought)
        
        # STEP 2: ACT
        action = llm_choose_action(thought)
        thoughts.append(f"Action: {action}")
        
        # STEP 3: OBSERVE
        observation = execute_action(action)
        thoughts.append(f"Observation: {observation}")
    
    raise Exception("Max steps reached without answer")
```

### Real Example: Solving a Math Problem

**Question:** "If John has 5 apples, buys 3 more, then gives half to Mary, how many does he have left?"

**ReAct Trace:**

```
Step 1:
Thought: I need to track John's apples through each event. Start with 5.
Action: None (just reasoning)
Observation: Starting count = 5

Step 2:
Thought: John buys 3 more apples. I should add these.
Action: calculate(5 + 3)
Observation: 8

Step 3:
Thought: John gives half to Mary. I need to divide by 2.
Action: calculate(8 / 2)
Observation: 4

Step 4:
Thought: I have the final answer. John has 4 apples left.
Action: finish(4)
Observation: Answer: 4
```

### Building a ReAct Agent from Scratch

Let's create a **Research Assistant** using ReAct:

```python
import re
from typing import Dict, List, Any

class ReActAgent:
    """
    Research Assistant using ReAct pattern
    
    Can search, read, and synthesize information
    """
    
    def __init__(self):
        self.tools = {
            'search': self.search_tool,
            'read': self.read_tool,
            'calculate': self.calculate_tool,
            'compare': self.compare_tool
        }
        
        self.max_steps = 10
        self.thought_history = []
    
    # === TOOLS ===
    
    def search_tool(self, query: str) -> str:
        """Search for information (mock implementation)"""
        # In production, this would call Google/Bing API
        mock_results = {
            'climate change effects': 'Rising temperatures, sea level rise, extreme weather',
            'python benefits': 'Easy syntax, large ecosystem, versatile applications',
            'best programming language 2024': 'Depends on use case: Python for ML, JS for web',
        }
        return mock_results.get(query.lower(), f"No results for '{query}'")
    
    def read_tool(self, source: str) -> str:
        """Read content from a source (mock)"""
        mock_content = {
            'wikipedia_climate': 'Climate change causes include greenhouse gases...',
            'docs_python': 'Python is an interpreted, high-level language...',
        }
        return mock_content.get(source.lower(), f"Content not found: {source}")
    
    def calculate_tool(self, expression: str) -> str:
        """Perform calculation"""
        try:
            # Safe eval for demo (use proper parser in production!)
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)
        except Exception as e:
            return f"Calculation error: {e}"
    
    def compare_tool(self, item1: str, item2: str) -> str:
        """Compare two items"""
        return f"Comparing '{item1}' vs '{item2}': Both are valid choices depending on needs."
    
    # === REACT LOOP ===
    
    def run(self, question: str) -> str:
        """
        Execute ReAct loop: Thought → Action → Observation
        """
        print(f"\n🤔 Question: {question}")
        print("=" * 60)
        
        self.thought_history = []
        
        for step in range(1, self.max_steps + 1):
            print(f"\n--- Step {step} ---")
            
            # Generate thought
            thought = self._generate_thought(question)
            print(f"💭 Thought: {thought}")
            
            # Check if ready to answer
            if self._should_answer(thought):
                answer = self._extract_answer(thought)
                print(f"\n✅ Final Answer: {answer}")
                return answer
            
            # Choose and execute action
            action_name, action_input = self._choose_action(thought)
            print(f"⚡ Action: {action_name}({action_input})")
            
            if action_name:
                observation = self._execute_action(action_name, action_input)
                print(f"👁️  Observation: {observation}")
                
                self.thought_history.append({
                    'step': step,
                    'thought': thought,
                    'action': action_name,
                    'input': action_input,
                    'observation': observation
                })
        
        return "Could not find answer within step limit"
    
    def _generate_thought(self, question: str) -> str:
        """
        Generate next thought based on question and history
        
        In production, this uses an LLM. Here we use simple rules.
        """
        if not self.thought_history:
            # First thought: plan approach
            if 'compare' in question.lower():
                return "I need to compare two things. Let me search for information about each."
            elif any(word in question.lower() for word in ['how many', 'calculate', 'total']):
                return "This requires calculation. I'll break it down step by step."
            else:
                return "I need to search for relevant information to answer this."
        
        # Subsequent thoughts: build on observations
        last = self.thought_history[-1]
        
        if 'no results' in last['observation'].lower():
            return "That search didn't work. Let me try a different approach."
        elif step := last.get('step', 0) > 3:
            return "I have enough information. Time to synthesize an answer."
        else:
            return "Let me gather more information to be thorough."
    
    def _should_answer(self, thought: str) -> bool:
        """Check if thought indicates readiness to answer"""
        answer_keywords = ['answer', 'conclude', 'finally', 'therefore', 'in summary']
        return any(kw in thought.lower() for kw in answer_keywords)
    
    def _extract_answer(self, thought: str) -> str:
        """Extract answer from thought"""
        # Simple extraction - in production, use LLM
        return f"Based on my research: {thought}"
    
    def _choose_action(self, thought: str) -> tuple:
        """Choose which action to take"""
        thought_lower = thought.lower()
        
        if 'search' in thought_lower:
            return 'search', 'general query'
        elif 'calculate' in thought_lower:
            return 'calculate', '1 + 1'  # Demo
        elif 'compare' in thought_lower:
            return 'compare', 'item1, item2'
        else:
            return 'search', 'follow-up query'
    
    def _execute_action(self, action_name: str, action_input: Any) -> str:
        """Execute the chosen action"""
        if action_name not in self.tools:
            return f"Unknown action: {action_name}"
        
        try:
            if isinstance(action_input, dict):
                result = self.tools[action_name](**action_input)
            else:
                result = self.tools[action_name](str(action_input))
            return result
        except Exception as e:
            return f"Error: {e}"


# Test the ReAct agent
if __name__ == "__main__":
    agent = ReActAgent()
    
    questions = [
        "What are the effects of climate change?",
        "Calculate: If you have 10 items and get 5 more, then lose 3",
    ]
    
    for q in questions:
        answer = agent.run(q)
        print(f"\n{'=' * 60}\n")
```

### When to Use ReAct

✅ **Good for:**
- Complex reasoning tasks
- Problems requiring multiple steps
- Situations where you need to verify intermediate results
- Research and investigation

❌ **Not ideal for:**
- Simple lookup questions
- Tasks requiring extensive upfront planning
- Real-time responses (too slow)

---

## 2.3 Plan-and-Execute Architecture

### What is Plan-and-Execute?

Instead of interleaving reasoning and acting (like ReAct), Plan-and-Execute does them in **two distinct phases**:

```
Phase 1: PLAN (create complete strategy)
   ↓
Phase 2: EXECUTE (follow the plan step-by-step)
```

### Why Use Plan-and-Execute?

**Advantages over ReAct:**

| Aspect | ReAct | Plan-and-Execute |
|--------|-------|------------------|
| Coherence | Can lose track | Clear roadmap |
| Efficiency | May repeat work | Optimized upfront |
| Debugging | Hard to trace | Easy to review plan |
| User Trust | Opaque process | Plan is explainable |

### The Two Phases

#### Phase 1: Planning

```python
def create_plan(goal: str) -> List[Dict]:
    """
    Create a complete plan before taking any action
    
    Returns list of steps with dependencies
    """
    plan_prompt = f"""
Goal: {goal}

Create a step-by-step plan to achieve this goal.
For each step, specify:
1. Step number
2. Description
3. Required tools
4. Dependencies (which steps must come before)

Format as JSON list.
"""
    plan = llm_generate(plan_prompt)
    return parse_plan(plan)
```

#### Phase 2: Execution

```python
def execute_plan(plan: List[Dict]) -> Any:
    """
    Execute a pre-defined plan
    
    Handles dependencies and tracks progress
    """
    completed = {}
    results = {}
    
    for step in plan:
        # Wait for dependencies
        for dep in step.get('dependencies', []):
            if dep not in completed:
                wait_for_completion(dep)
        
        # Execute step
        result = execute_step(step)
        results[step['id']] = result
        completed[step['id']] = True
    
    return synthesize_results(results)
```

### Real Example: Planning a Vacation

**Goal:** "Plan a 5-day trip to Japan for under $3000"

**Phase 1: Generated Plan**

```json
{
  "plan": [
    {
      "id": 1,
      "description": "Research flight costs to Tokyo",
      "tool": "flight_search",
      "dependencies": []
    },
    {
      "id": 2,
      "description": "Find accommodation options",
      "tool": "hotel_search",
      "dependencies": []
    },
    {
      "id": 3,
      "description": "Research activities and attractions",
      "tool": "web_search",
      "dependencies": []
    },
    {
      "id": 4,
      "description": "Calculate total costs",
      "tool": "calculate",
      "dependencies": [1, 2, 3]
    },
    {
      "id": 5,
      "description": "Adjust plan if over budget",
      "tool": "optimize",
      "dependencies": [4]
    },
    {
      "id": 6,
      "description": "Generate final itinerary",
      "tool": "summarize",
      "dependencies": [5]
    }
  ]
}
```

**Phase 2: Execution Trace**

```
Executing Step 1: Research flight costs...
  → Found: $1200 round-trip

Executing Step 2: Find accommodation...
  → Found: $150/night × 5 = $750

Executing Step 3: Research activities...
  → Found: ~$500 for attractions

Executing Step 4: Calculate total...
  → Total: $1200 + $750 + $500 = $2450

Executing Step 5: Check budget...
  → Under budget! ($2450 < $3000)

Executing Step 6: Generate itinerary...
  → Complete plan created!
```

### Building a Plan-and-Execute Agent

```python
class PlanAndExecuteAgent:
    """
    Agent that plans first, then executes
    
    Better for complex, multi-step tasks
    """
    
    def __init__(self):
        self.tools = {
            'search': self.search,
            'calculate': self.calculate,
            'book': self.book,
            'summarize': self.summarize
        }
    
    def run(self, goal: str) -> str:
        # PHASE 1: PLAN
        print("📋 PHASE 1: Creating plan...")
        plan = self.create_plan(goal)
        print(f"Generated {len(plan)} steps")
        
        # Display plan for transparency
        self.display_plan(plan)
        
        # PHASE 2: EXECUTE
        print("\n⚡ PHASE 2: Executing plan...")
        results = self.execute_plan(plan)
        
        # Synthesize final answer
        return self.synthesize(goal, results)
    
    def create_plan(self, goal: str) -> List[Dict]:
        """Generate a complete plan"""
        # In production, use LLM
        # For demo, use template matching
        
        if 'trip' in goal.lower() or 'vacation' in goal.lower():
            return [
                {'id': 1, 'desc': 'Search transportation', 'tool': 'search', 'deps': []},
                {'id': 2, 'desc': 'Search accommodation', 'tool': 'search', 'deps': []},
                {'id': 3, 'desc': 'Calculate total cost', 'tool': 'calculate', 'deps': [1, 2]},
                {'id': 4, 'desc': 'Generate summary', 'tool': 'summarize', 'deps': [3]},
            ]
        elif 'compare' in goal.lower():
            return [
                {'id': 1, 'desc': 'Research option A', 'tool': 'search', 'deps': []},
                {'id': 2, 'desc': 'Research option B', 'tool': 'search', 'deps': []},
                {'id': 3, 'desc': 'Compare options', 'tool': 'summarize', 'deps': [1, 2]},
            ]
        else:
            return [
                {'id': 1, 'desc': 'Gather information', 'tool': 'search', 'deps': []},
                {'id': 2, 'desc': 'Synthesize answer', 'tool': 'summarize', 'deps': [1]},
            ]
    
    def display_plan(self, plan: List[Dict]):
        """Show the plan to user"""
        print("\nPlanned Steps:")
        for step in plan:
            deps = f" (after steps {step['deps']})" if step['deps'] else ""
            print(f"  {step['id']}. {step['desc']}{deps}")
    
    def execute_plan(self, plan: List[Dict]) -> Dict:
        """Execute plan respecting dependencies"""
        completed = set()
        results = {}
        
        while len(completed) < len(plan):
            for step in plan:
                # Skip if already done
                if step['id'] in completed:
                    continue
                
                # Check dependencies
                deps_met = all(d in completed for d in step['deps'])
                if not deps_met:
                    continue
                
                # Execute step
                print(f"\n  Executing step {step['id']}: {step['desc']}")
                result = self.tools[step['tool']](step['desc'])
                results[step['id']] = result
                completed.add(step['id'])
                print(f"  → Done: {result[:50]}...")
        
        return results
    
    # Mock tool implementations
    def search(self, query: str) -> str:
        return f"Search results for: {query}"
    
    def calculate(self, query: str) -> str:
        return "Calculation complete: $2450"
    
    def book(self, details: str) -> str:
        return "Booking confirmed"
    
    def summarize(self, query: str) -> str:
        return "Summary generated"
    
    def synthesize(self, goal: str, results: Dict) -> str:
        """Combine results into final answer"""
        return f"Completed goal: {goal}\nResults: {len(results)} steps executed"


# Test
if __name__ == "__main__":
    agent = PlanAndExecuteAgent()
    
    goals = [
        "Plan a weekend trip to Seattle",
        "Compare Python and JavaScript",
    ]
    
    for goal in goals:
        print(f"\n{'=' * 60}")
        print(f"GOAL: {goal}")
        print('=' * 60)
        result = agent.run(goal)
        print(f"\n✅ FINAL: {result}")
```

### When to Use Plan-and-Execute

✅ **Good for:**
- Complex projects with clear steps
- Tasks requiring coordination
- When users want to see/review the plan
- Optimizing for efficiency

❌ **Not ideal for:**
- Exploratory tasks (can't plan upfront)
- Dynamic environments (plan becomes obsolete)
- Simple queries (overhead not worth it)

---

## 2.4 Multi-Agent Systems

### What Are Multi-Agent Systems?

Instead of one agent doing everything, use **multiple specialized agents** working together:

```
┌─────────────┐
│  Manager    │ ← Coordinates the team
└──────┬──────┘
       │
   ┌───┴───┬───────────┬──────────┐
   ▼       ▼           ▼          ▼
┌─────┐ ┌─────┐ ┌─────────┐ ┌────────┐
│Res- │ │Code │ │  Data   │ │  Test  │
│earch│ │Agent│ │ Analyst │ │ Agent  │
└─────┘ └─────┘ └─────────┘ └────────┘
```

### Why Multiple Agents?

**Benefits:**

1. **Specialization**: Each agent excels at its task
2. **Parallelism**: Multiple agents work simultaneously
3. **Modularity**: Easy to update/replace individual agents
4. **Scalability**: Add more agents as needed

### Common Multi-Agent Patterns

#### Pattern 1: Collaborative Team

All agents work together on shared goal:

```python
class CollaborativeTeam:
    """Multiple agents collaborating on one task"""
    
    def __init__(self):
        self.agents = {
            'researcher': ResearchAgent(),
            'writer': WriterAgent(),
            'reviewer': ReviewerAgent(),
        }
    
    def run(self, task: str) -> str:
        # Agent 1: Research
        research = self.agents['researcher'].research(task)
        
        # Agent 2: Write
        draft = self.agents['writer'].write(research)
        
        # Agent 3: Review
        feedback = self.agents['reviewer'].review(draft)
        
        # Iterate if needed
        if feedback['needs_revision']:
            draft = self.agents['writer'].revise(draft, feedback)
        
        return draft
```

#### Pattern 2: Debate/Adversarial

Agents argue different sides to find best answer:

```python
class DebateTeam:
    """Agents debate to reach optimal solution"""
    
    def run(self, question: str) -> str:
        # Agent 1: Propose solution A
        proposal_a = advocate_agent.argue_for(question, option='A')
        
        # Agent 2: Propose solution B
        proposal_b = advocate_agent.argue_for(question, option='B')
        
        # Agent 3: Critique both
        critique_a = critic_agent.critique(proposal_a)
        critique_b = critic_agent.critique(proposal_b)
        
        # Judge: Decide winner
        decision = judge_agent.decide(
            proposal_a, critique_a,
            proposal_b, critique_b
        )
        
        return decision
```

#### Pattern 3: Assembly Line

Each agent handles one stage of processing:

```python
class AssemblyLine:
    """Sequential processing through specialized agents"""
    
    def run(self, input_data: Any) -> Any:
        # Stage 1: Validate
        validated = validator_agent.validate(input_data)
        
        # Stage 2: Transform
        transformed = transformer_agent.transform(validated)
        
        # Stage 3: Enrich
        enriched = enricher_agent.enrich(transformed)
        
        # Stage 4: Format
        output = formatter_agent.format(enriched)
        
        return output
```

### Building a Multi-Agent System

Let's create a **Software Development Team**:

```python
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class Role(Enum):
    PRODUCT_MANAGER = "product_manager"
    DEVELOPER = "developer"
    TESTER = "tester"
    DEVOPS = "devops"

@dataclass
class Message:
    sender: str
    recipient: str
    content: str
    attachments: Dict = None

class Agent:
    """Base agent class"""
    
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.memory = []
    
    def receive(self, message: Message) -> Message:
        """Process incoming message and respond"""
        self.memory.append(message)
        response = self.process(message)
        return response
    
    def process(self, message: Message) -> Message:
        """Override in subclasses"""
        raise NotImplementedError

class ProductManager(Agent):
    """Defines requirements"""
    
    def process(self, message: Message) -> Message:
        if "build" in message.content.lower():
            requirements = self.generate_requirements(message.content)
            return Message(
                sender=self.name,
                recipient="developer",
                content=f"Build this: {requirements}",
                attachments={'requirements': requirements}
            )
        return Message(self.name, message.sender, "Acknowledged")
    
    def generate_requirements(self, request: str) -> str:
        return f"Detailed specs for: {request}"

class Developer(Agent):
    """Writes code"""
    
    def process(self, message: Message) -> Message:
        if "build" in message.content.lower():
            code = self.write_code(message.attachments.get('requirements', ''))
            return Message(
                sender=self.name,
                recipient="tester",
                content="Code ready for testing",
                attachments={'code': code}
            )
        return Message(self.name, message.sender, "Working on it")
    
    def write_code(self, requirements: str) -> str:
        return f"Implementation of: {requirements}"

class Tester(Agent):
    """Tests code"""
    
    def process(self, message: Message) -> Message:
        if "testing" in message.content.lower():
            results = self.run_tests(message.attachments.get('code', ''))
            if results['passed']:
                return Message(
                    sender=self.name,
                    recipient="devops",
                    content="Tests passed, ready to deploy"
                )
            else:
                return Message(
                    sender=self.name,
                    recipient="developer",
                    content=f"Tests failed: {results['failures']}"
                )
        return Message(self.name, message.sender, "Testing...")
    
    def run_tests(self, code: str) -> Dict:
        return {'passed': True, 'failures': []}

class DevOps(Agent):
    """Deploys code"""
    
    def process(self, message: Message) -> Message:
        if "deploy" in message.content.lower():
            status = self.deploy()
            return Message(
                sender=self.name,
                recipient="product_manager",
                content=f"Deployment {status}"
            )
        return Message(self.name, message.sender, "Standing by")
    
    def deploy(self) -> str:
        return "successful"

class MultiAgentSystem:
    """
    Orchestrates multiple agents working together
    """
    
    def __init__(self):
        self.agents = {
            'product_manager': ProductManager("PM Alice", Role.PRODUCT_MANAGER),
            'developer': Developer("Dev Bob", Role.DEVELOPER),
            'tester': Tester("Tester Carol", Role.TESTER),
            'devops': DevOps("DevOps Dave", Role.DEVOPS),
        }
        self.message_queue = []
    
    def run(self, initial_request: str) -> str:
        """Run the multi-agent workflow"""
        print("🚀 Starting multi-agent development workflow")
        print("=" * 60)
        
        # Initial message from user to PM
        current_message = Message(
            sender="user",
            recipient="product_manager",
            content=initial_request
        )
        
        # Process messages until done
        max_iterations = 20
        for i in range(max_iterations):
            print(f"\n--- Iteration {i+1} ---")
            print(f"Message: {current_message.sender} → {current_message.recipient}")
            print(f"Content: {current_message.content[:60]}...")
            
            # Route to appropriate agent
            recipient = current_message.recipient
            if recipient not in self.agents:
                print("✅ Workflow complete!")
                break
            
            agent = self.agents[recipient]
            response = agent.receive(current_message)
            
            # Check if workflow is done
            if response.recipient == "user":
                print(f"\n✅ FINAL RESULT: {response.content}")
                return response.content
            
            current_message = response
        
        return "Workflow timed out"


# Test the multi-agent system
if __name__ == "__main__":
    system = MultiAgentSystem()
    
    request = "Build a login page with authentication"
    result = system.run(request)
    print(f"\n{'=' * 60}")
    print(f"Final Output: {result}")
```

### Communication Patterns

#### 1. Broadcast
One agent sends to all others:
```python
def broadcast(sender, message, recipients):
    for recipient in recipients:
        send_message(sender, recipient, message)
```

#### 2. Request-Response
Synchronous communication:
```python
def request_response(requester, responder, request):
    response = responder.process(request)
    return response
```

#### 3. Blackboard
Shared memory space:
```python
class Blackboard:
    def __init__(self):
        self.data = {}
    
    def post(self, key, value):
        self.data[key] = value
    
    def read(self, key):
        return self.data.get(key)
```

### When to Use Multi-Agent Systems

✅ **Good for:**
- Complex tasks requiring multiple skills
- Parallel processing opportunities
- Modular, maintainable systems
- Simulating real-world teams

❌ **Not ideal for:**
- Simple tasks (overhead not justified)
- Tight latency requirements
- Limited resources

---

## 2.5 Hierarchical Agent Structures

### What is Hierarchical Organization?

Like a company org chart, agents are arranged in **levels**:

```
         CEO Agent (Strategic)
              │
    ┌─────────┼─────────┐
    │         │         │
Manager     Manager   Manager
(Tactical)  (Tactical) (Tactical)
    │         │         │
  Worker    Worker    Worker
(Operational)
```

### Levels of Hierarchy

#### Level 1: Strategic (Top)
- Sets overall goals
- Makes high-level decisions
- Allocates resources

#### Level 2: Tactical (Middle)
- Translates strategy into plans
- Coordinates workers
- Reports progress

#### Level 3: Operational (Bottom)
- Executes specific tasks
- Reports status
- Handles details

### Example: Customer Support Hierarchy

```python
class SupportHierarchy:
    """
    Hierarchical customer support system
    """
    
    def __init__(self):
        # Strategic level
        self.director = SupportDirector()
        
        # Tactical level
        self.managers = {
            'billing': BillingManager(),
            'technical': TechnicalManager(),
            'general': GeneralManager(),
        }
        
        # Operational level
        self.workers = {
            'billing': [BillingAgent() for _ in range(3)],
            'technical': [TechnicalAgent() for _ in range(5)],
            'general': [GeneralAgent() for _ in range(4)],
        }
    
    def handle_request(self, ticket: dict) -> str:
        # Level 1: Director categorizes
        category = self.director.categorize(ticket)
        
        # Level 2: Manager assigns
        manager = self.managers[category]
        priority = manager.assess_priority(ticket)
        
        # Level 3: Worker handles
        worker = self.select_worker(category, priority)
        resolution = worker.resolve(ticket)
        
        return resolution
```

### Benefits of Hierarchy

1. **Clear Responsibilities**: Each level knows its role
2. **Escalation Path**: Problems move up when needed
3. **Efficiency**: Simple tasks handled at low levels
4. **Oversight**: Higher levels ensure quality

### When to Use Hierarchy

✅ **Good for:**
- Large-scale operations
- Clear escalation needs
- Quality control requirements
- Enterprise systems

❌ **Not ideal for:**
- Small/simple tasks
- Fast-paced environments
- Flat organizational cultures

---

## 2.6 Choosing the Right Architecture

### Decision Framework

Use this flowchart:

```
Start: What's the task complexity?
│
├─ Simple (single step)
│  └─→ Single Agent
│
├─ Medium (2-5 steps)
│  ├─ Needs verification?
│  │  ├─ Yes → ReAct
│  │  └─ No → Plan-and-Execute
│  │
│  └─ Multiple skills needed?
│     └─ Yes → Multi-Agent
│
└─ Complex (many steps, many skills)
   ├─ Clear hierarchy needed?
   │  ├─ Yes → Hierarchical
   │  └─ No → Multi-Agent Collaborative
   │
   └─ Scale > 1000 requests/day?
      └─ Yes → Hierarchical + Multi-Agent
```

### Comparison Table

| Architecture | Best For | Complexity | Setup Time | Maintenance |
|-------------|----------|------------|------------|-------------|
| Single Agent | Simple Q&A | Low | Minutes | Easy |
| ReAct | Reasoning tasks | Medium | Hours | Medium |
| Plan-and-Execute | Structured workflows | Medium | Hours | Medium |
| Multi-Agent | Complex, multi-skill | High | Days | Complex |
| Hierarchical | Enterprise scale | Very High | Weeks | Very Complex |

### Real-World Examples

#### Example 1: FAQ Bot
- **Architecture**: Single Agent
- **Why**: Simple lookup, no reasoning needed

#### Example 2: Math Tutor
- **Architecture**: ReAct
- **Why**: Needs to reason through problems step-by-step

#### Example 3: Travel Planner
- **Architecture**: Plan-and-Execute
- **Why**: Clear steps, benefit from upfront planning

#### Example 4: Software Factory
- **Architecture**: Multi-Agent
- **Why**: Requires PM, dev, tester, DevOps skills

#### Example 5: Enterprise Support
- **Architecture**: Hierarchical + Multi-Agent
- **Why**: Scale, escalation, multiple specialties

---

## 2.7 Glossary

| Term | Definition |
|------|------------|
| **ReAct** | Reasoning + Acting interleaved pattern |
| **Plan-and-Execute** | Two-phase: plan completely, then execute |
| **Multi-Agent** | Multiple specialized agents collaborating |
| **Hierarchical** | Agents organized in levels (strategic/tactical/operational) |
| **Agent Loop** | Cycle of perception, reasoning, action |
| **Tool** | Capability an agent can use |
| **Orchestration** | Coordinating multiple agents |
| **Specialization** | Agent focused on specific domain |
| **Collaboration** | Agents working together |
| **Escalation** | Moving tasks up hierarchy |

---

## 2.8 Exercises

### Exercise 1: Implement ReAct for a New Domain (Medium)

**Task:** Adapt the ReAct agent for recipe suggestions

**Requirements:**
- Tools: search_ingredients, find_recipes, calculate_nutrition
- Handle: "What can I make with eggs, flour, and milk?"
- Show full thought-action-observation trace

### Exercise 2: Build a Two-Agent Debate (Hard)

**Task:** Create opposing agents that debate a topic

**Requirements:**
- Proponent agent argues for a position
- Opponent agent argues against
- Judge agent decides winner
- Example topic: "Should remote work be the default?"

### Exercise 3: Design a Hierarchical System (Challenge)

**Task:** Design a hospital triage system

**Requirements:**
- Director level: Categorize urgency
- Manager level: Assign department
- Worker level: Handle specific cases
- Include escalation path for critical cases

---

## 2.9 Troubleshooting

### Problem: ReAct loops forever

**Solution:** Add step limits and termination conditions
```python
if step > max_steps or "answer" in thought:
    break
```

### Problem: Plan is too vague

**Solution:** Improve planning prompt with specifics
```python
prompt = """Create SPECIFIC steps. Each step must have:
- Clear action verb
- Expected output
- Success criteria"""
```

### Problem: Agents don't coordinate

**Solution:** Add explicit communication protocol
```python
class Message:
    sender: str
    recipient: str
    intent: str  # 'request', 'response', 'broadcast'
    payload: dict
```

---

## 2.10 What's Next?

In this chapter you learned:
- ✅ ReAct pattern for reasoning tasks
- ✅ Plan-and-Execute for structured workflows
- ✅ Multi-Agent systems for collaboration
- ✅ Hierarchical structures for scale
- ✅ How to choose the right architecture

**In Chapter 3**, we'll explore:
- 🔧 Advanced tool integration
- 💾 Memory systems (short-term, long-term, episodic)
- 🔄 Self-reflection and learning
- 🛡️ Safety and guardrails

**Continue to** [Chapter 3: Advanced Capabilities](chapter_3_advanced.md)!
