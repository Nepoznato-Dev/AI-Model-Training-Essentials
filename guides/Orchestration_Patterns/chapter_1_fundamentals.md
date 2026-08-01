# Chapter 1: Orchestration Fundamentals

## 🎯 Learning Objectives

By the end of this chapter, you will:
- Understand what orchestration is and why it's critical for AI systems
- Build a complete workflow engine from scratch
- Implement step execution with dependency management
- Handle errors and failures gracefully
- Visualize workflow execution
- Be ready to learn design patterns in Chapter 2

---

## 1.1 What is Orchestration? (Really Simple Explanation)

### The Problem Without Orchestration

Imagine you're making a sandwich:

**Without a plan:**
1. Get bread
2. Wait, I need peanut butter first
3. Go get peanut butter
4. Oh no, I need a knife to spread it!
5. Put knife down, go get jelly
6. Forget to put bread on plate...

This is chaotic! You're constantly stopping, backtracking, and forgetting steps.

**With orchestration (a recipe):**
1. Gather all ingredients (bread, peanut butter, jelly, knife, plate)
2. Place bread slices on plate
3. Spread peanut butter on one slice
4. Spread jelly on other slice
5. Put slices together
6. Cut in half
7. Serve

Everything flows smoothly because someone thought through the **order**, **dependencies**, and **what to do if something goes wrong**.

### AI Systems Are Like Making Sandwiches (But More Complex)

In AI applications, you often have multiple components that need to work together:

```
User asks: "What's the weather in Tokyo and should I pack an umbrella?"

Your system needs to:
1. Understand the question (NLU model)
2. Extract location: "Tokyo" (Entity extraction)
3. Call weather API (External service)
4. Get forecast data (API response)
5. Analyze if rain is expected (Logic/Model)
6. Generate helpful response (LLM)
7. Send back to user (API response)
```

If any step fails or runs in the wrong order, your system breaks. **Orchestration** ensures everything runs smoothly.

---

## 1.2 Core Concepts

### Workflow

A **workflow** is a defined sequence of steps to accomplish a task.

**Key properties:**
- Has a start and end
- Steps run in a specific order (or parallel when possible)
- Data flows from one step to the next
- Handles success and failure cases

### Step (or Task)

A **step** is a single unit of work within a workflow.

**Examples:**
- Call an API
- Run a machine learning model
- Transform data
- Save to database
- Send notification

**Each step has:**
- A name (for identification)
- An action (the code to execute)
- Dependencies (which steps must complete first)
- Input (data from previous steps)
- Output (result to pass to next steps)

### Dependency

A **dependency** defines the order of execution.

**Example:**
```python
Step(name="generate_response", dependencies=["fetch_data", "analyze"])
```

This means `generate_response` cannot run until BOTH `fetch_data` AND `analyze` have completed successfully.

### DAG (Directed Acyclic Graph)

Don't be scared by the fancy name! A **DAG** is just a diagram showing:
- **Nodes** = Steps
- **Arrows** = Dependencies (which way data flows)
- **Acyclic** = No circles (can't have A→B→C→A)

**Example DAG:**
```
    fetch_data
       ↓
    analyze
       ↓
generate_response
```

This is a simple linear DAG. Real workflows can be more complex:

```
    fetch_weather    fetch_news
          ↓              ↓
       analyze_weather  analyze_news
                ↓        ↓
              combine_results
                    ↓
              generate_response
```

### Orchestrator (Workflow Engine)

The **orchestrator** is the system that:
- Reads the workflow definition
- Figures out which steps can run
- Executes steps in the right order
- Passes data between steps
- Handles errors
- Tracks progress

You'll build one in this chapter!

---

## 1.3 Building Your First Workflow Engine

Let's build a complete workflow engine from scratch. This will be the foundation for everything else.

### Step 1: Define the Data Structures

First, we need to represent steps and their results:

```python
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Callable
import time

class StepStatus(Enum):
    """Possible states for a step"""
    PENDING = "pending"      # Not started yet
    RUNNING = "running"      # Currently executing
    SUCCESS = "success"      # Completed successfully
    FAILED = "failed"        # Encountered an error
    SKIPPED = "skipped"      # Skipped due to condition

@dataclass
class Step:
    """Represents a single step in a workflow"""
    name: str                           # Unique identifier
    action: Callable                    # Function to execute
    dependencies: List[str] = field(default_factory=list)  # Must wait for these
    retry_count: int = 0                # How many times to retry on failure
    timeout: float = None               # Max seconds to run
    
    def __post_init__(self):
        """Validate the step after creation"""
        if not callable(self.action):
            raise ValueError(f"Action for step '{self.name}' must be callable")

@dataclass
class StepResult:
    """Result of executing a step"""
    step_name: str
    status: StepStatus
    output: Any = None                  # Result from successful execution
    error: Optional[str] = None         # Error message if failed
    duration: float = 0.0               # How long it took (seconds)
    retries_used: int = 0               # Number of retry attempts
```

### Step 2: Build the Workflow Engine

Now let's create the orchestrator itself:

```python
class WorkflowEngine:
    """
    A workflow orchestration engine.
    
    This engine:
    - Manages step execution order based on dependencies
    - Handles errors and retries
    - Tracks execution state
    - Provides logging and debugging info
    """
    
    def __init__(self, verbose: bool = True):
        self.steps: Dict[str, Step] = {}
        self.results: Dict[str, StepResult] = {}
        self.verbose = verbose  # Print detailed logs
        
    def add_step(self, step: Step) -> 'WorkflowEngine':
        """
        Add a step to the workflow.
        
        Returns self for method chaining.
        """
        if step.name in self.steps:
            raise ValueError(f"Step '{step.name}' already exists")
        
        self.steps[step.name] = step
        return self
    
    def _log(self, message: str):
        """Print log message if verbose mode is enabled"""
        if self.verbose:
            print(message)
    
    def _can_execute(self, step: Step) -> bool:
        """
        Check if a step is ready to execute.
        
        A step can execute if:
        1. All its dependencies have completed successfully
        2. It hasn't been executed yet
        """
        # Check if already executed
        if step.name in self.results:
            return False
        
        # Check all dependencies
        for dep_name in step.dependencies:
            # Dependency must exist
            if dep_name not in self.steps:
                raise ValueError(
                    f"Step '{step.name}' depends on unknown step '{dep_name}'"
                )
            
            # Dependency must have succeeded
            if dep_name not in self.results:
                return False  # Not run yet
            
            if self.results[dep_name].status != StepStatus.SUCCESS:
                return False  # Failed or skipped
        
        return True
    
    def _execute_step_with_retry(self, step: Step, context: Dict) -> StepResult:
        """
        Execute a step with retry logic.
        """
        attempt = 0
        max_attempts = step.retry_count + 1  # +1 for initial attempt
        
        while attempt < max_attempts:
            attempt += 1
            
            if self.verbose and attempt > 1:
                self._log(f"  🔄 Retry {attempt}/{max_attempts} for {step.name}")
            
            start_time = time.time()
            
            try:
                # Apply timeout if specified
                if step.timeout:
                    # Simple timeout implementation
                    import signal
                    
                    def timeout_handler(signum, frame):
                        raise TimeoutError(f"Step {step.name} exceeded {step.timeout}s timeout")
                    
                    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                    signal.alarm(int(step.timeout))
                
                try:
                    # Execute the action
                    output = step.action(context)
                    
                    if step.timeout:
                        signal.alarm(0)  # Cancel alarm
                        signal.signal(signal.SIGALRM, old_handler)
                    
                    duration = time.time() - start_time
                    
                    return StepResult(
                        step_name=step.name,
                        status=StepStatus.SUCCESS,
                        output=output,
                        duration=duration,
                        retries_used=attempt - 1
                    )
                    
                except Exception as e:
                    if step.timeout:
                        signal.alarm(0)
                        signal.signal(signal.SIGALRM, old_handler)
                    raise  # Re-raise to handle in retry logic
                    
            except Exception as e:
                duration = time.time() - start_time
                
                if attempt >= max_attempts:
                    # All retries exhausted
                    return StepResult(
                        step_name=step.name,
                        status=StepStatus.FAILED,
                        error=str(e),
                        duration=duration,
                        retries_used=attempt - 1
                    )
                # Otherwise, continue to next retry attempt
        
        # Should never reach here, but just in case
        return StepResult(
            step_name=step.name,
            status=StepStatus.FAILED,
            error="Unexpected retry loop exit",
            retries_used=attempt
        )
    
    def run(self, initial_context: Dict = None, 
            stop_on_failure: bool = False) -> Dict[str, StepResult]:
        """
        Execute the entire workflow.
        
        Args:
            initial_context: Initial data to pass to first steps
            stop_on_failure: If True, stop entire workflow on first failure
        
        Returns:
            Dictionary mapping step names to their results
        """
        if initial_context is None:
            initial_context = {}
        
        context = initial_context.copy()
        remaining_steps = set(self.steps.keys())
        
        self._log(f"🚀 Starting workflow: {len(self.steps)} steps")
        self._log("=" * 50)
        
        iteration = 0
        max_iterations = len(self.steps) * 3  # Safety limit
        
        while remaining_steps and iteration < max_iterations:
            iteration += 1
            made_progress = False
            
            # Find all steps that can run now
            ready_steps = []
            for step_name in remaining_steps:
                step = self.steps[step_name]
                if self._can_execute(step):
                    ready_steps.append(step)
            
            if not ready_steps:
                if remaining_steps:
                    # Deadlock or waiting for failed dependencies
                    self._log("\n⚠️  No steps can proceed!")
                    self._log("Remaining steps and their unmet dependencies:")
                    for name in remaining_steps:
                        step = self.steps[name]
                        unmet = [d for d in step.dependencies 
                                if d not in self.results or 
                                self.results[d].status != StepStatus.SUCCESS]
                        if unmet:
                            self._log(f"  - {name}: waiting on {unmet}")
                    
                    if stop_on_failure:
                        break
                    else:
                        # Mark remaining steps as skipped
                        for name in remaining_steps:
                            self.results[name] = StepResult(
                                step_name=name,
                                status=StepStatus.SKIPPED,
                                error="Dependencies not met"
                            )
                        remaining_steps.clear()
                break
            
            # Execute ready steps (one at a time for simplicity)
            for step in ready_steps:
                self._log(f"\n▶️  Executing: {step.name}")
                self._log(f"    Dependencies: {step.dependencies or 'none'}")
                
                # Execute with retry logic
                result = self._execute_step_with_retry(step, context)
                self.results[step.name] = result
                
                # Update context with output
                if result.status == StepStatus.SUCCESS:
                    context[f"{step.name}_output"] = result.output
                    self._log(f"✅ Success ({result.duration:.3f}s)")
                    if result.output is not None:
                        output_str = str(result.output)
                        if len(output_str) > 80:
                            output_str = output_str[:77] + "..."
                        self._log(f"    Output: {output_str}")
                else:
                    self._log(f"❌ Failed: {result.error}")
                    if stop_on_failure:
                        self._log("\n🛑 Stopping workflow due to failure")
                        remaining_steps.clear()
                        break
                
                remaining_steps.remove(step.name)
                made_progress = True
            
            if not made_progress and remaining_steps:
                self._log("\n⚠️  Progress stalled! Possible circular dependency.")
                break
        
        self._log("\n" + "=" * 50)
        self._log(f"📊 Workflow Complete")
        self._log(f"   Total steps: {len(self.steps)}")
        self._log(f"   Successful: {sum(1 for r in self.results.values() if r.status == StepStatus.SUCCESS)}")
        self._log(f"   Failed: {sum(1 for r in self.results.values() if r.status == StepStatus.FAILED)}")
        self._log(f"   Skipped: {sum(1 for r in self.results.values() if r.status == StepStatus.SKIPPED)}")
        
        total_duration = sum(r.duration for r in self.results.values())
        self._log(f"   Total duration: {total_duration:.3f}s")
        
        return self.results
    
    def get_execution_order(self) -> List[str]:
        """
        Return the order steps would be executed (without running them).
        
        Uses topological sort to determine valid execution order.
        """
        # Kahn's algorithm for topological sort
        in_degree = {name: len(step.dependencies) for name, step in self.steps.items()}
        queue = [name for name, degree in in_degree.items() if degree == 0]
        order = []
        
        while queue:
            current = queue.pop(0)
            order.append(current)
            
            # Reduce in-degree for dependent steps
            for name, step in self.steps.items():
                if current in step.dependencies:
                    in_degree[name] -= 1
                    if in_degree[name] == 0:
                        queue.append(name)
        
        if len(order) != len(self.steps):
            raise ValueError("Circular dependency detected!")
        
        return order
```

---

## 1.4 Hands-On Example: Customer Support Workflow

Let's use our workflow engine to build a real customer support system!

### Scenario

A customer sends a message: "My order #12345 hasn't arrived and it's been 2 weeks!"

Our workflow needs to:
1. Parse the message to understand intent
2. Look up the order details
3. Check shipping status
4. Determine appropriate action
5. Generate a response
6. Log the interaction

### Implementation

```python
import random
import time

# Simulated actions (in real life, these would call APIs/models)

def parse_message(context):
    """Extract intent and entities from customer message"""
    time.sleep(0.3)  # Simulate processing
    
    message = context.get("customer_message", "")
    
    # Simple keyword-based parsing (use NLP model in production)
    intent = "unknown"
    entities = {}
    
    if "order" in message.lower() or "#" in message:
        intent = "order_inquiry"
        # Extract order number
        for word in message.split():
            if word.startswith("#"):
                entities["order_id"] = word[1:]
    
    if "late" in message.lower() or "haven't arrived" in message.lower():
        entities["issue"] = "delayed_delivery"
    
    return {
        "intent": intent,
        "entities": entities,
        "confidence": 0.95
    }

def lookup_order(context):
    """Fetch order details from database"""
    time.sleep(0.5)  # Simulate DB query
    
    parsed = context.get("parse_message_output", {})
    entities = parsed.get("entities", {})
    order_id = entities.get("order_id", "UNKNOWN")
    
    # Simulate order lookup
    return {
        "order_id": order_id,
        "customer": "Alice Johnson",
        "items": ["Wireless Headphones"],
        "order_date": "2024-01-01",
        "status": "shipped",
        "tracking_number": "TRK123456789"
    }

def check_shipping(context):
    """Check shipping carrier for delivery status"""
    time.sleep(0.4)  # Simulate API call
    
    order = context.get("lookup_order_output", {})
    tracking = order.get("tracking_number")
    
    # Simulate carrier API response
    return {
        "tracking_number": tracking,
        "carrier": "FedEx",
        "status": "in_transit",
        "estimated_delivery": "2024-01-20",
        "current_location": "Memphis, TN",
        "delay_reason": "weather"
    }

def determine_action(context):
    """Decide what action to take based on analysis"""
    time.sleep(0.2)
    
    shipping = context.get("check_shipping_output", {})
    order = context.get("lookup_order_output", {})
    
    delay_reason = shipping.get("delay_reason")
    
    if delay_reason:
        return {
            "action": "apologize_and_explain",
            "compensation": "10_percent_discount",
            "priority": "high"
        }
    elif shipping.get("status") == "delivered":
        return {
            "action": "confirm_delivery",
            "compensation": None,
            "priority": "normal"
        }
    else:
        return {
            "action": "provide_status_update",
            "compensation": None,
            "priority": "normal"
        }

def generate_response(context):
    """Generate customer-facing response"""
    time.sleep(0.3)
    
    order = context.get("lookup_order_output", {})
    shipping = context.get("check_shipping_output", {})
    action = context.get("determine_action_output", {})
    
    customer = order.get("customer")
    items = order.get("items", [])
    est_delivery = shipping.get("estimated_delivery")
    delay_reason = shipping.get("delay_reason")
    
    response_parts = [f"Dear {customer},"]
    
    if action.get("action") == "apologize_and_explain":
        response_parts.append(f"We sincerely apologize for the delay with your order containing {', '.join(items)}.")
        response_parts.append(f"The delay is due to {delay_reason}.")
        response_parts.append(f"Your new estimated delivery date is {est_delivery}.")
        response_parts.append(f"As compensation, we're offering {action.get('compensation')} on your next order.")
    else:
        response_parts.append(f"Your order with {', '.join(items)} is on track.")
        response_parts.append(f"Expected delivery: {est_delivery}")
    
    response_parts.append("\nThank you for your patience!")
    response_parts.append("- Customer Support Team")
    
    return "\n".join(response_parts)

def log_interaction(context):
    """Log the interaction for analytics"""
    time.sleep(0.1)
    
    results_summary = {
        step: result.status.value 
        for step, result in context.get("_all_results", {}).items()
    }
    
    log_entry = {
        "timestamp": time.time(),
        "results": results_summary,
        "response_generated": context.get("generate_response_output") is not None
    }
    
    # In production, save to database/logging service
    print(f"\n📝 LOGGED: Interaction completed")
    
    return log_entry

# Build and run the workflow
if __name__ == "__main__":
    # Create the workflow engine
    engine = WorkflowEngine(verbose=True)
    
    # Define the workflow
    engine.add_step(Step(name="parse_message", action=parse_message))
    engine.add_step(Step(
        name="lookup_order",
        action=lookup_order,
        dependencies=["parse_message"]
    ))
    engine.add_step(Step(
        name="check_shipping",
        action=check_shipping,
        dependencies=["lookup_order"]
    ))
    engine.add_step(Step(
        name="determine_action",
        action=determine_action,
        dependencies=["check_shipping"]
    ))
    engine.add_step(Step(
        name="generate_response",
        action=generate_response,
        dependencies=["determine_action"]
    ))
    engine.add_step(Step(
        name="log_interaction",
        action=log_interaction,
        dependencies=["generate_response"]
    ))
    
    # Initial context (customer message)
    initial_context = {
        "customer_message": "My order #12345 hasn't arrived and it's been 2 weeks!",
        "channel": "email",
        "customer_id": "CUST_789"
    }
    
    # Run the workflow
    results = engine.run(initial_context)
    
    # Print final response
    print("\n" + "=" * 50)
    print("📧 FINAL RESPONSE TO CUSTOMER:")
    print("=" * 50)
    print(results["generate_response"].output)
```

### Expected Output

```
🚀 Starting workflow: 6 steps
==================================================

▶️  Executing: parse_message
    Dependencies: none
✅ Success (0.301s)
    Output: {'intent': 'order_inquiry', 'entities': {'order_id': '12345', 'issue': ...

▶️  Executing: lookup_order
    Dependencies: ['parse_message']
✅ Success (0.502s)
    Output: {'order_id': '12345', 'customer': 'Alice Johnson', 'items': ...

▶️  Executing: check_shipping
    Dependencies: ['lookup_order']
✅ Success (0.401s)
    Output: {'tracking_number': 'TRK123456789', 'carrier': 'FedEx', ...

▶️  Executing: determine_action
    Dependencies: ['check_shipping']
✅ Success (0.201s)
    Output: {'action': 'apologize_and_explain', 'compensation': '10_percent_...

▶️  Executing: generate_response
    Dependencies: ['determine_action']
✅ Success (0.301s)
    Output: Dear Alice Johnson,
We sincerely apologize for the delay with your order...

▶️  Executing: log_interaction
    Dependencies: ['generate_response']

📝 LOGGED: Interaction completed
✅ Success (0.101s)
    Output: {'timestamp': 1704067200.123, 'results': {...

==================================================
📊 Workflow Complete
   Total steps: 6
   Successful: 6
   Failed: 0
   Skipped: 0
   Total duration: 1.807s

==================================================
📧 FINAL RESPONSE TO CUSTOMER:
==================================================
Dear Alice Johnson,
We sincerely apologize for the delay with your order containing Wireless Headphones.
The delay is due to weather.
Your new estimated delivery date is 2024-01-20.
As compensation, we're offering 10_percent_discount on your next order.

Thank you for your patience!
- Customer Support Team
```

🎉 Congratulations! You've built a complete customer support workflow!

---

## 1.5 Debugging and Troubleshooting

### Common Issues

#### Issue 1: Circular Dependencies

**Symptom:** Workflow hangs or reports "No steps can proceed"

**Example:**
```python
engine.add_step(Step(name="A", action=func_a, dependencies=["C"]))
engine.add_step(Step(name="B", action=func_b, dependencies=["A"]))
engine.add_step(Step(name="C", action=func_c, dependencies=["B"]))
# A → C → B → A (circular!)
```

**Solution:** Use the execution order checker before running:
```python
try:
    order = engine.get_execution_order()
    print(f"Valid order: {order}")
except ValueError as e:
    print(f"Error: {e}")
```

**Fix:** Break the cycle by removing one dependency.

#### Issue 2: Missing Dependencies

**Symptom:** Step fails with "depends on unknown step"

**Example:**
```python
engine.add_step(Step(name="step2", action=func, dependencies=["step1"]))
# But step1 was never added!
```

**Solution:** Always verify step names match exactly:
```python
print(f"Available steps: {list(engine.steps.keys())}")
```

#### Issue 3: Action Raises Unexpected Exception

**Symptom:** Step fails immediately

**Solution:** 
1. Add better error handling in your action function
2. Use retry logic:
```python
Step(name="flaky_api_call", action=call_api, retry_count=3)
```

#### Issue 4: Context Data Not Passed Correctly

**Symptom:** Step receives None or wrong data

**Debug technique:** Add logging to your actions:
```python
def my_action(context):
    print(f"DEBUG: Received context keys: {context.keys()}")
    print(f"DEBUG: Looking for: {expected_key}")
    # ... rest of function
```

---

## 1.6 Visualizing Workflows

Understanding your workflow structure is crucial. Let's create a visualizer:

```python
def visualize_workflow(engine: WorkflowEngine) -> str:
    """
    Generate a text-based visualization of the workflow.
    """
    lines = []
    lines.append("Workflow Diagram:")
    lines.append("=" * 40)
    
    # Group steps by their "level" (distance from root)
    levels = {}
    
    def get_level(step_name, visited=None):
        if visited is None:
            visited = set()
        
        if step_name in visited:
            return -1  # Circular
        
        visited.add(step_name)
        step = engine.steps[step_name]
        
        if not step.dependencies:
            return 0
        
        max_dep_level = -1
        for dep in step.dependencies:
            dep_level = get_level(dep, visited.copy())
            if dep_level == -1:
                return -1
            max_dep_level = max(max_dep_level, dep_level)
        
        return max_dep_level + 1
    
    # Calculate levels
    for step_name in engine.steps:
        level = get_level(step_name)
        if level not in levels:
            levels[level] = []
        levels[level].append(step_name)
    
    # Print by level
    for level in sorted(levels.keys()):
        if level == -1:
            lines.append("⚠️  Circular dependency detected!")
            break
        
        indent = "    " * level
        for step_name in levels[level]:
            step = engine.steps[step_name]
            deps = ", ".join(step.dependencies) if step.dependencies else "start"
            lines.append(f"{indent}├─ {step_name}")
            lines.append(f"{indent}│   (depends on: {deps})")
    
    return "\n".join(lines)

# Usage
print(visualize_workflow(engine))
```

**Output:**
```
Workflow Diagram:
========================================
    ├─ parse_message
    │   (depends on: start)
    ├─ lookup_order
    │   (depends on: parse_message)
    ├─ check_shipping
    │   (depends on: lookup_order)
    ├─ determine_action
    │   (depends on: check_shipping)
    ├─ generate_response
    │   (depends on: determine_action)
    ├─ log_interaction
    │   (depends on: generate_response)
```

For more complex workflows, consider using graph visualization libraries like `graphviz`:

```bash
pip install graphviz
```

---

## 1.7 Best Practices

### ✅ DO:

1. **Name steps clearly**: Use descriptive names like `validate_user_input` not `step1`
2. **Keep steps small**: Each step should do one thing well
3. **Make actions idempotent**: Safe to retry without side effects
4. **Log extensively**: You'll need logs when debugging
5. **Test failure scenarios**: What happens when step 3 of 10 fails?
6. **Set timeouts**: Prevent hung steps from blocking forever
7. **Use retry wisely**: Only retry transient failures (network issues, not validation errors)

### ❌ DON'T:

1. **Create circular dependencies**: Draw your workflow first!
2. **Put business logic in the orchestrator**: Keep orchestration separate from business logic
3. **Ignore failures**: Always handle errors explicitly
4. **Hardcode step order**: Use dependencies, not execution order assumptions
5. **Skip validation**: Validate inputs before processing

---

## 📚 Glossary

| Term | Definition |
|------|------------|
| **Workflow** | A defined sequence of steps to accomplish a task |
| **Step** | A single unit of work within a workflow |
| **Dependency** | Requirement that certain steps complete before others can start |
| **DAG** | Directed Acyclic Graph - the structure of most workflows |
| **Orchestrator** | System that manages workflow execution |
| **Context** | Data passed between steps during execution |
| **Idempotent** | Operation that produces the same result whether run once or multiple times |
| **Topological Sort** | Algorithm to order nodes in a DAG respecting dependencies |
| **Deadlock** | Situation where steps are waiting on each other indefinitely |
| **Retry** | Attempting to re-execute a failed step |
| **Timeout** | Maximum allowed duration for a step before it's considered failed |
| **Circuit Breaker** | Pattern to stop trying when a service is consistently failing |

---

## 🎓 Exercises

### Exercise 1: Add Parallel Execution

Modify the workflow engine to execute independent steps concurrently using Python's `ThreadPoolExecutor`.

**Requirements:**
- Identify all steps that can run simultaneously
- Execute them in parallel
- Wait for all to complete before proceeding
- Handle failures correctly

**Hint:**
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(execute_step, step): step for step in ready_steps}
    for future in as_completed(futures):
        result = future.result()
        # Process result
```

### Exercise 2: Implement Conditional Branching

Add support for conditional steps that only run if a condition is met.

**Requirements:**
- Add a `condition` parameter to Step
- Condition is a function that takes context and returns bool
- If condition returns False, mark step as SKIPPED
- Downstream steps should still run if they have other satisfied dependencies

**Example:**
```python
def is_premium_user(context):
    user = context.get("get_user_output", {})
    return user.get("tier") == "premium"

Step(
    name="show_premium_features",
    action=show_features,
    dependencies=["get_user"],
    condition=is_premium_user
)
```

### Exercise 3: Build a Workflow Builder DSL

Create a domain-specific language (DSL) for defining workflows more naturally.

**Goal:** Allow users to define workflows like:
```python
workflow = (WorkflowBuilder()
    .step("fetch_data").runs(fetch_data)
    .step("process").runs(process_data).after("fetch_data")
    .step("save").runs(save_result).after("process")
    .build())
```

**Bonus:** Add support for parallel groups:
```python
workflow = (WorkflowBuilder()
    .step("fetch_a").runs(fetch_a)
    .step("fetch_b").runs(fetch_b)
    .parallel(["fetch_a", "fetch_b"]).then("combine")
    .build())
```

---

## 🔍 Self-Assessment Checklist

Before moving to Chapter 2, make sure you can:

- [ ] Explain what orchestration is in simple terms
- [ ] Describe what a workflow, step, and dependency are
- [ ] Build a basic workflow engine from scratch
- [ ] Add steps with dependencies
- [ ] Run a workflow and interpret the results
- [ ] Debug common issues (circular deps, missing deps, failures)
- [ ] Visualize a workflow structure
- [ ] Explain why idempotency matters
- [ ] Set up retry logic for flaky operations

If you checked all boxes, you're ready for Chapter 2!

---

## 🚀 What's Next?

In Chapter 2, you'll learn **design patterns** - proven solutions for common orchestration challenges:

- **Chain Pattern**: Simple sequential processing
- **Parallel Pattern**: Run multiple steps concurrently
- **Conditional Pattern**: Dynamic branching based on data
- **Fan-out/Fan-in**: Distribute work and combine results
- **Loop Pattern**: Repeat until condition is met
- **Circuit Breaker**: Protect against cascading failures

These patterns will help you solve real-world problems faster!
