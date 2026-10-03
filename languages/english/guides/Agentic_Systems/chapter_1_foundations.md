# Chapter 1: Agent Fundamentals

## 🎯 Chapter Overview

**What You'll Learn:**
- What makes a system "agentic" vs regular AI
- The 4 core components of every agent
- How to build an agent loop from scratch
- Tool integration basics
- Debugging common agent failures

**By the End:** You'll have built your first working agent that can use tools to complete tasks!

**Time Estimate:** 3-5 hours

---

## 1.1 What Makes a System "Agentic"?

### Regular AI vs Agentic AI

Let's start with a simple comparison:

| **Regular AI (Chatbot)** | **Agentic AI** |
|--------------------------|----------------|
| Answers questions | Takes actions |
| Gives advice | Executes tasks |
| Passive responder | Active participant |
| "You should book a flight" | "I booked your flight" |
| No memory of past actions | Remembers what it did |
| Single turn interaction | Multi-step workflows |

### Key Insight

**Agency = Ability to act independently toward goals**

An agentic system doesn't just *talk* about doing something—it actually *does* it.

### Real-World Analogy: GPS vs Self-Driving Car

```
🗺️ GPS Navigation (Regular AI)
   - Tells you: "Turn left in 500 feet"
   - You do the driving
   - Can't control the car
   
🚗 Self-Driving Car (Agentic AI)
   - Perceives: Sees road, traffic, obstacles
   - Decides: When to turn, brake, accelerate
   - Acts: Controls steering, pedals
   - Achieves goal: Gets you to destination
```

The GPS **advises**, the self-driving car **acts**. That's the difference!

---

## 1.2 The Four Core Components

Every agentic system has these four components:

### 1. Perception (Input)
**What it does:** Gathers information from the environment

**Examples:**
- Reading user messages
- Checking database records
- Monitoring API responses
- Observing sensor data

**Code Example:**
```python
def perceive(environment):
    """Gather information from the environment"""
    observations = {
        'user_message': environment.get_latest_message(),
        'database_status': environment.check_database(),
        'api_health': environment.ping_api()
    }
    return observations
```

### 2. Reasoning (Decision-Making)
**What it does:** Processes information and decides what to do

**Examples:**
- Planning next steps
- Choosing which tool to use
- Evaluating options
- Making judgments

**Code Example:**
```python
def reason(observations, goal):
    """Decide what action to take"""
    if observations['user_message'] contains "weather":
        return {'action': 'get_weather', 'city': extract_city(observations)}
    elif observations['database_status'] == 'down':
        return {'action': 'alert_admin', 'severity': 'high'}
    else:
        return {'action': 'respond', 'message': "I'm not sure how to help"}
```

### 3. Action (Output)
**What it does:** Executes decisions in the real world

**Examples:**
- Sending emails
- Making API calls
- Updating databases
- Executing code

**Code Example:**
```python
def act(decision):
    """Execute the decided action"""
    if decision['action'] == 'get_weather':
        result = call_weather_api(decision['city'])
    elif decision['action'] == 'send_email':
        result = send_email(decision['to'], decision['body'])
    elif decision['action'] == 'execute_code':
        result = safe_exec(decision['code'])
    
    return result
```

### 4. Memory (Learning)
**What it does:** Stores information for future use

**Examples:**
- Remembering user preferences
- Tracking conversation history
- Learning from mistakes
- Building knowledge base

**Code Example:**
```python
class AgentMemory:
    def __init__(self):
        self.short_term = []  # Current conversation
        self.long_term = {}   # Persistent knowledge
        self.episodic = []    # Past experiences
    
    def store(self, experience):
        self.short_term.append(experience)
        if experience['important']:
            self.long_term[experience['key']] = experience['value']
    
    def retrieve(self, query):
        # Find relevant memories
        return [m for m in self.short_term if query in m]
```

---

## 1.3 The Agent Loop

All agents follow this basic loop:

```
┌──────────────────────────────────────────────┐
│                                              │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│  │Perceive │ →  │ Reason  │ →  │  Act    │  │
│  └─────────┘    └─────────┘    └────┬────┘  │
│       ↑                              │       │
│       │                              │       │
│       │         ┌─────────┐          │       │
│       └─────────│ Memory  │ ←────────┘       │
│                 └─────────┘                  │
│                                              │
└──────────────────────────────────────────────┘
              Repeat until goal achieved
```

### Step-by-Step Walkthrough

Let's trace through a real example:

**Goal:** Book a flight for the user

**Iteration 1:**
1. **Perceive:** User says "Book me a flight to NYC tomorrow"
2. **Reason:** Need to search flights → use flight_search tool
3. **Act:** Call flight_search_api(destination="NYC", date="tomorrow")
4. **Memory:** Store that user wants to go to NYC
5. **Observe:** Get list of available flights

**Iteration 2:**
1. **Perceive:** Have flight options, need user preference
2. **Reason:** Ask user which flight they prefer
3. **Act:** Send message: "Found 3 flights. Which do you prefer?"
4. **Memory:** Store flight options
5. **Observe:** User selects flight #2

**Iteration 3:**
1. **Perceive:** User chose flight #2
2. **Reason:** Proceed with booking
3. **Act:** Call book_flight_api(flight_id=2, user_info=...)
4. **Memory:** Store booking confirmation
5. **Observe:** Booking successful!

**Loop terminates** when goal is achieved.

---

## 1.4 Building Your First Agent (From Scratch)

Let's build a **Calculator Agent** that can perform math operations. This is simple enough to understand completely but demonstrates all core concepts.

### Complete Implementation

Create a file called `calculator_agent.py`:

```python
import re
from typing import Dict, Any, List

class CalculatorAgent:
    """A simple agent that can perform mathematical calculations"""
    
    def __init__(self):
        # Initialize memory
        self.memory = {
            'history': [],
            'variables': {}
        }
        
        # Define available tools
        self.tools = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'store': self.store_variable,
            'recall': self.recall_variable
        }
    
    # === TOOLS (Actions the agent can take) ===
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b"""
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    def store_variable(self, name: str, value: float) -> str:
        """Store a value in memory"""
        self.memory['variables'][name] = value
        return f"Stored {name} = {value}"
    
    def recall_variable(self, name: str) -> float:
        """Recall a stored variable"""
        if name not in self.memory['variables']:
            return f"Error: Variable '{name}' not found"
        return self.memory['variables'][name]
    
    # === PERCEPTION ===
    
    def perceive(self, user_input: str) -> Dict[str, Any]:
        """
        Parse user input to understand what they want
        
        This is where we interpret natural language
        """
        observation = {
            'raw_input': user_input,
            'intent': None,
            'parameters': {},
            'needs_tool': False
        }
        
        input_lower = user_input.lower()
        
        # More robust pattern matching for different intents
        if re.search(r'\b(add|plus|\+)\b', input_lower):
            observation['intent'] = 'add'
            observation['needs_tool'] = True
            observation['parameters'] = self.extract_numbers(user_input)
            
        elif re.search(r'\b(subtract|minus|-)\b', input_lower):
            observation['intent'] = 'subtract'
            observation['needs_tool'] = True
            observation['parameters'] = self.extract_numbers(user_input)
            
        elif any(op in input_lower for op in ['multiply', 'times', '*']):
            observation['intent'] = 'multiply'
            observation['needs_tool'] = True
            observation['parameters'] = self.extract_numbers(user_input)
            
        elif re.search(r'\b(divide|/|divided by)\b', input_lower):
            observation['intent'] = 'divide'
            observation['needs_tool'] = True
            observation['parameters'] = self.extract_numbers(user_input)
            
        elif re.search(r'\b(store|save)\b', input_lower):
            observation['intent'] = 'store'
            observation['needs_tool'] = True
            observation['parameters'] = self.extract_store_command(user_input)
            
        elif re.search(r'\b(recall|what is)\b', input_lower):
            observation['intent'] = 'recall'
            observation['needs_tool'] = True
            observation['parameters'] = self.extract_recall_command(user_input)
        
        return observation
    
    def extract_numbers(self, text: str) -> Dict[str, float]:
        """Extract numbers from text"""
        # Find all numbers (including decimals and negatives)
        found_numbers = re.findall(r'-?\d+(?:\.\d+)?', text)
        
        # Convert to float
        numbers = [float(n) for n in found_numbers]
        
        # Return up to the first two numbers found
        return {'a': numbers[0] if len(numbers) > 0 else 0, 'b': numbers[1] if len(numbers) > 1 else 0}
    
    def extract_store_command(self, text: str) -> Dict[str, Any]:
        """Extract variable name and value from store command"""
        # Simple pattern: "store x as 5" or "save y = 10"
        match = re.search(r'(store|save)\s+(\w+)\s+(?:as|=)?\s*(-?\d+\.?\d*)', text, re.I)
        if match:
            return {'name': match.group(2), 'value': float(match.group(3))}
        return {'name': 'unknown', 'value': 0}
    
    def extract_recall_command(self, text: str) -> Dict[str, str]:
        """Extract variable name from recall command"""
        # Pattern: "recall x" or "what is y"
        match = re.search(r'(?:recall|what is)\s+(\w+)', text, re.I)
        if match:
            return {'name': match.group(1)}
        return {'name': 'unknown'}
    
    # === REASONING ===
    
    def reason(self, observation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Decide which tool to use and with what parameters
        
        This is the "brain" of the agent
        """
        decision = {
            'tool': None,
            'arguments': {},
            'confidence': 0.0,
            'reasoning': ''
        }
        
        if not observation['needs_tool']:
            decision['reasoning'] = "No tool needed"
            return decision
        
        intent = observation['intent']
        
        if intent in self.tools:
            decision['tool'] = intent
            decision['arguments'] = observation['parameters']
            decision['confidence'] = 0.9
            decision['reasoning'] = f"User wants to {intent}, using {intent} tool"
        else:
            decision['reasoning'] = f"Unknown intent: {intent}"
        
        return decision
    
    # === ACTION ===
    
    def act(self, decision: Dict[str, Any]) -> Any:
        """
        Execute the chosen tool
        
        This is where the agent actually DOES something
        """
        if decision['tool'] is None:
            return "I'm not sure how to help with that."
        
        tool_name = decision['tool']
        arguments = decision['arguments']
        
        if tool_name not in self.tools:
            return f"Error: Unknown tool '{tool_name}'"
        
        # Execute the tool
        try:
            result = self.tools[tool_name](**arguments)
            return result
        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"
    
    # === MEMORY ===
    
    def update_memory(self, input_str: str, result: Any):
        """Store the interaction in memory"""
        self.memory['history'].append({
            'input': input_str,
            'result': result,
            'timestamp': len(self.memory['history'])
        })
    
    def get_history(self) -> List[Dict]:
        """Retrieve conversation history"""
        return self.memory['history']
    
    # === MAIN AGENT LOOP ===
    
    def run(self, user_input: str) -> str:
        """
        The main agent loop: Perceive → Reason → Act → Remember
        
        This is the core method that makes the agent work!
        """
        # Step 1: Perceive
        print(f"\n👁️  PERCEIVE: Processing input...")
        observation = self.perceive(user_input)
        print(f"   Intent: {observation['intent']}")
        print(f"   Needs tool: {observation['needs_tool']}")
        
        # Step 2: Reason
        print(f"\n🧠 REASON: Deciding what to do...")
        decision = self.reason(observation)
        print(f"   Chosen tool: {decision['tool']}")
        print(f"   Reasoning: {decision['reasoning']}")
        
        # Step 3: Act
        print(f"\n⚡ ACT: Executing action...")
        result = self.act(decision)
        print(f"   Result: {result}")
        
        # Step 4: Remember
        print(f"\n💾 MEMORY: Storing interaction...")
        self.update_memory(user_input, result)
        print(f"   History length: {len(self.memory['history'])}")
        
        return result


# === TESTING THE AGENT ===

if __name__ == "__main__":
    # Create the agent
    agent = CalculatorAgent()
    
    print("=" * 60)
    print("🤖 CALCULATOR AGENT - Demo")
    print("=" * 60)
    print("\nThis agent can:")
    print("  - Add, subtract, multiply, divide")
    print("  - Store variables")
    print("  - Recall stored values")
    print("\nTry commands like:")
    print("  - 'Add 5 and 3'")
    print("  - 'Multiply 4 times 7'")
    print("  - 'Store x as 10'")
    print("  - 'What is x?'")
    print("=" * 60)
    
    # Test cases
    test_commands = [
        "Add 15 and 25",
        "Subtract 10 from 50",
        "Multiply 6 times 7",
        "Divide 100 by 4",
        "Divide 10 by 0", # Test error handling
        "Store my_age as 30",
        "What is my_age?",
        # This command will fail with the current simple perception,
        # which is a great learning opportunity for Exercise 3!
        # "Add my_age and 5"
        "recall non_existent_var", # Test error handling
        "what is the answer to multiplying 3 and 14" # Test more complex phrasing
    ]
    
    for command in test_commands:
        print(f"\n{'=' * 60}")
        print(f"👤 USER: {command}")
        print("-" * 60)
        
        response = agent.run(command)
        
        print(f"\n🤖 AGENT: {response}")
    
    # Show full history
    print(f"\n{'=' * 60}")
    print("📜 CONVERSATION HISTORY:")
    print("=" * 60)
    for i, entry in enumerate(agent.get_history(), 1):
        print(f"{i}. Input: {entry['input']}")
        print(f"   Result: {entry['result']}")
        print()
```

### Running the Agent

Save the code and run:

```bash
python calculator_agent.py
```

### Expected Output

```
============================================================
🤖 CALCULATOR AGENT - Demo
============================================================

This agent can:
  - Add, subtract, multiply, divide
  - Store variables
  - Recall stored values

Try commands like:
  - 'Add 5 and 3'
  - 'Multiply 4 times 7'
  - 'Store x as 10'
  - 'What is x?'
============================================================

============================================================
👤 USER: Add 15 and 25
------------------------------------------------------------

👁️  PERCEIVE: Processing input...
   Intent: add
   Needs tool: True

🧠 REASON: Deciding what to do...
   Chosen tool: add
   Reasoning: User wants to add, using add tool

⚡ ACT: Executing action...
   Result: 40.0

💾 MEMORY: Storing interaction...
   History length: 1

🤖 AGENT: 40.0
```

...and so on for each command.

### Code Breakdown

Let's understand what each part does:

#### 1. Tools Definition
```python
self.tools = {
    'add': self.add,
    'subtract': self.subtract,
    ...
}
```
- Maps tool names to functions
- Easy to extend: just add new methods!

#### 2. Perception
```python
def perceive(self, user_input: str) -> Dict[str, Any]:
```
- Converts raw text into structured observations
- Uses pattern matching (regex) to extract intent
- Could be replaced with LLM for better understanding

#### 3. Reasoning
```python
def reason(self, observation: Dict[str, Any]) -> Dict[str, Any]:
```
- Decides which tool to use
- Could include confidence scores, multiple options
- In advanced agents, uses LLM for reasoning

#### 4. Action
```python
def act(self, decision: Dict[str, Any]) -> Any:
```
- Actually executes the tool
- Handles errors gracefully
- Returns results

#### 5. Memory
```python
def update_memory(self, input_str: str, result: Any):
```
- Stores interactions for later
- Enables context-aware responses
- Foundation for learning

#### 6. Main Loop
```python
def run(self, user_input: str) -> str:
```
- Orchestrates the entire process
- Calls perceive → reason → act → remember
- This IS the agent!

---

## 1.5 Understanding the Agent Loop Deeply

### Why a Loop?

Agents use loops because most tasks require **multiple steps**:

**Simple Task (One Step):**
- User: "What's 2+2?"
- Agent: "4"
- Done!

**Complex Task (Multiple Steps):**
- User: "Plan my vacation to Japan"
- Agent needs to:
  1. Search flights
  2. Search hotels
  3. Check weather
  4. Create itinerary
  5. Book everything
  6. Send confirmation

Each step requires: Perceive → Reason → Act → Remember

### Loop Termination

How does the agent know when to stop?

**Common Strategies:**

1. **Goal Achievement**
```python
if current_state == goal_state:
    break
```

2. **Maximum Iterations**
```python
max_iterations = 10
for i in range(max_iterations):
    if done:
        break
else:
    raise Exception("Max iterations reached")
```

3. **LLM Decision**
```python
response = llm(prompt)
if "TERMINATE" in response:
    break
```

4. **User Confirmation**
```python
if user_says("yes, that's good"):
    break
```

---

## 1.6 Tool Integration Basics

### What Are Tools?

Tools are **actions the agent can take** in the world:

| Tool Type | Examples |
|-----------|----------|
| APIs | Weather, flights, stocks, news |
| Databases | SQL queries, lookups, updates |
| Code Execution | Python, JavaScript, shell |
| File Operations | Read, write, delete files |
| Communication | Email, SMS, Slack, Discord |
| Web Actions | Search, scrape, interact |

### Tool Design Principles

**Good Tool Design:**

✅ Clear purpose  
✅ Well-defined inputs  
✅ Predictable outputs  
✅ Error handling  
✅ Documentation  

**Example: Well-Designed Tool**

```python
def get_weather(city: str, units: str = "fahrenheit") -> dict:
    """
    Get current weather for a city.
    
    Args:
        city: City name (e.g., "New York")
        units: "fahrenheit" or "celsius" (default: fahrenheit)
    
    Returns:
        dict with keys: temperature, condition, humidity
    
    Raises:
        ValueError: If city not found
    """
    # Implementation here
```

**Bad Tool Design:**

```python
def weather(x):  # ❌ Unclear parameter
    # No docstring
    # Returns inconsistent types
    # No error handling
    pass
```

### Adding a New Tool

Let's add a **currency conversion** tool to our calculator agent:

```python
def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert amount from one currency to another.
    
    Note: In production, you'd call a real API.
    Here we use fixed rates for demo.
    """
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'CAD': 1.25
    }
    
    if from_currency not in rates or to_currency not in rates:
        return "Error: Unknown currency"
    
    # Convert to USD first, then to target
    usd_amount = amount / rates[from_currency]
    result = usd_amount * rates[to_currency]
    
    return round(result, 2)

# Add to tools dictionary
self.tools['convert_currency'] = self.convert_currency
```

Now the agent can handle: "Convert 100 USD to EUR"

---

## 1.7 Debugging Agents

### Common Issues and Fixes

### Issue 1: Infinite Loops

**Symptom:** Agent keeps running forever

**Cause:** No termination condition

**Debug:**
```python
max_iterations = 10
iteration_count = 0

while not done:
    iteration_count += 1
    if iteration_count > max_iterations:
        print(f"ERROR: Stopped after {max_iterations} iterations")
        print("Last 3 actions:", recent_actions[-3:])
        break
```

**Fix:** Add proper termination logic

### Issue 2: Wrong Tool Selection

**Symptom:** Agent uses wrong tool for task

**Cause:** Poor perception or reasoning

**Debug:**
```python
observation = agent.perceive(user_input)
print("Observation:", observation)  # Check if intent detected correctly

decision = agent.reason(observation)
print("Decision:", decision)  # Check if right tool chosen
```

**Fix:** Improve pattern matching or use LLM for understanding

### Issue 3: Tool Errors

**Symptom:** Tool crashes or returns unexpected results

**Cause:** Bad inputs, API failures, edge cases

**Debug:**
```python
try:
    result = tool(**arguments)
except Exception as e:
    print(f"Tool error: {e}")
    print(f"Arguments were: {arguments}")
    result = f"Error: {str(e)}"
```

**Fix:** Add validation and error handling

### Issue 4: Memory Leaks

**Symptom:** Agent slows down over time

**Cause:** Unbounded memory growth

**Debug:**
```python
print(f"Memory size: {len(agent.memory['history'])} entries")
```

**Fix:** Implement memory limits
```python
MAX_HISTORY = 100
if len(self.memory['history']) > MAX_HISTORY:
    self.memory['history'] = self.memory['history'][-MAX_HISTORY:]
```

---

## 1.8 Glossary

| Term | Definition |
|------|------------|
| **Agent** | AI system that can perceive, reason, act, and learn |
| **Agency** | Ability to act independently toward goals |
| **Agent Loop** | Cycle of perceive → reason → act → remember |
| **Perception** | Gathering information from environment |
| **Reasoning** | Processing info and making decisions |
| **Action** | Executing decisions in the world |
| **Memory** | Storing information for future use |
| **Tool** | Specific capability the agent can use |
| **Intent** | What the user wants to accomplish |
| **Observation** | Structured representation of perceived info |
| **Decision** | Choice of which action to take |
| **Termination** | Condition for stopping the agent loop |
| **Iteration** | One complete cycle of the agent loop |
| **Multi-step** | Task requiring multiple agent iterations |

---

## 1.9 Exercises

### Exercise 1: Add New Operations (Easy)

**Task:** Extend the calculator agent with new operations

**Requirements:**
- Add exponentiation (power) operation
- Add square root operation
- Add modulo operation

**Starter Code:**
```python
def power(self, base: float, exponent: float) -> float:
    """Raise base to the power of exponent"""
    # Your code here
    pass

def square_root(self, number: float) -> float:
    """Calculate square root"""
    # Your code here
    pass

# Don't forget to add to self.tools!
```

**Test Commands:**
- "2 to the power of 8"
- "Square root of 144"
- "17 mod 5"

### Exercise 2: Improve Perception (Medium)

**Task:** Make the agent understand more natural language

**Current Limitation:** Only understands exact patterns

**Improvement Ideas:**
- Handle "what is 5 plus 3?" 
- Understand "calculate the product of 4 and 6"
- Support "give me the sum of 10 and 20"

**Hint:** Add more regex patterns or use keyword matching

### Exercise 3: Add Conversation Context (Hard)

**Task:** Enable follow-up questions

**Example Conversation:**
```
User: "Add 5 and 3"
Agent: "8"

User: "Now multiply by 2"  # Should understand "by 2" means 8 * 2
Agent: "16"

User: "What was the previous result?"
Agent: "8"
```

**Requirements:**
- Track the last result
- Understand references like "the result", "that", "it"
- Store conversation context in memory

**Hint:** Add `last_result` to memory and check for contextual keywords

### Exercise 4: Build a Different Agent (Challenge)

**Task:** Create a new type of agent from scratch

**Ideas:**
- **Weather Agent:** Check weather for cities
- **Todo Agent:** Manage task lists
- **Quiz Agent:** Ask questions and track scores
- **Translation Agent:** Translate between languages (use a mock API)

**Requirements:**
- At least 3 different tools
- Proper perceive/reason/act/memory structure
- Handle at least 5 different user commands
- Include error handling

---

## 1.10 Troubleshooting Guide

### Problem: "My agent doesn't understand my input"

**Checklist:**
- [ ] Is the input format correct?
- [ ] Are there typos in keywords?
- [ ] Does the perception function handle this case?
- [ ] Print the observation to debug

**Debug Command:**
```python
observation = agent.perceive("your input here")
print(json.dumps(observation, indent=2))
```

### Problem: "Agent chooses wrong tool"

**Checklist:**
- [ ] Review the reasoning logic
- [ ] Check if intent detection is correct
- [ ] Look for overlapping patterns
- [ ] Add more specific conditions

**Solution:** Add confidence scores and fallback logic

### Problem: "Results are incorrect"

**Checklist:**
- [ ] Verify tool implementation
- [ ] Check parameter extraction
- [ ] Test tool in isolation
- [ ] Look for type conversion issues

**Debug:** Test each tool individually before integrating

### Problem: "Agent is too slow"

**Checklist:**
- [ ] Profile each step (perceive/reason/act)
- [ ] Check for unnecessary computations
- [ ] Consider caching results
- [ ] Optimize regex patterns

**Solution:** Use profiling tools to identify bottlenecks

---

## 1.11 Best Practices

### ✅ DO:

1. **Start Simple**
   - Begin with rule-based perception
   - Add complexity gradually
   - Test each component separately

2. **Handle Errors Gracefully**
   - Always catch exceptions in tools
   - Provide helpful error messages
   - Allow recovery from failures

3. **Log Everything**
   - Log each step of the agent loop
   - Store decisions and reasoning
   - Enable debugging later

4. **Set Limits**
   - Maximum iterations
   - Memory bounds
   - Timeout for actions

5. **Test Extensively**
   - Edge cases
   - Invalid inputs
   - Tool failures

### ❌ DON'T:

1. **Don't Skip Error Handling**
   - Tools will fail in production
   - APIs go down
   - Inputs are unpredictable

2. **Don't Allow Infinite Loops**
   - Always set iteration limits
   - Detect circular reasoning
   - Force termination

3. **Don't Ignore Security**
   - Validate all inputs
   - Sanitize tool arguments
   - Prevent injection attacks

4. **Don't Forget Memory Management**
   - Unbounded memory grows forever
   - Implement cleanup strategies
   - Consider memory compression

---

## 1.12 What's Next?

In this chapter you learned:
- ✅ What makes a system "agentic"
- ✅ The 4 core components (perceive, reason, act, remember)
- ✅ How to build an agent loop from scratch
- ✅ Tool integration basics
- ✅ Debugging techniques

**In Chapter 2**, we'll explore:
- 🔄 **ReAct Pattern**: Combining reasoning and action
- 📋 **Plan-and-Execute**: Strategic planning before acting
- 👥 **Multi-Agent Systems**: Teams of specialized agents
- 🏗️ **Architecture Selection**: When to use each pattern

**Ready for more?** Continue to [Chapter 2: Agent Architectures](chapter_2_architectures.md)!

---

## Appendix: Complete Code Reference

Here's the complete calculator agent again for reference:

[Full code listing as shown earlier in the chapter]
