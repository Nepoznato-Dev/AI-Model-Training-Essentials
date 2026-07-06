# Bad Agent Design

## Overview

AI agents are autonomous systems that can perceive, reason, act, and learn to accomplish tasks. Bad agent design results in inefficient task completion, unreliable behavior, poor error handling, or unsafe actions. Common issues include inadequate planning, missing feedback loops, improper tool usage, and lack of safety constraints.

## When to Reference This Document

- Designing AI agent architectures
- Debugging agent behavior issues
- Implementing tool-using agents
- Building multi-agent systems
- Ensuring agent safety and reliability

## Common Agent Design Failures

### No Clear Goal Definition

**Bad Example**:
```python
class VagueAgent:
    def __init__(self):
        self.llm = load_llm()
    
    def run(self, user_input):
        # No clear objective, just reacts to input
        response = self.llm.generate(user_input)
        return response
    
    # Agent has no defined success criteria
    # Cannot measure if task is complete
```

**Why It's Bad**:
- Unclear when task is complete
- Cannot measure success
- May loop indefinitely
- Hard to debug failures

**Solution**: Define explicit goals and success criteria
```python
class GoalDrivenAgent:
    def __init__(self, goal_spec):
        self.llm = load_llm()
        self.goal = goal_spec
        self.success_criteria = goal_spec.success_criteria
    
    def run(self, initial_state):
        state = initial_state
        max_iterations = 10
        
        for i in range(max_iterations):
            if self.check_success(state):
                return {"status": "success", "result": state}
            
            action = self.plan_action(state)
            state = self.execute(action, state)
        
        return {"status": "failed", "reason": "max_iterations"}
    
    def check_success(self, state):
        # Explicit success criteria
        return all(criterion(state) for criterion in self.success_criteria)
```

### Missing Observation-Action Loop

**Bad Example**:
```python
class OneShotAgent:
    def run(self, task):
        # Generates entire plan without feedback
        plan = llm.generate(f"Plan to: {task}")
        
        # Executes all steps blindly
        for step in plan:
            execute(step)
        
        # No verification of intermediate results
        return "Done"
```

**Why It's Bad**:
- Cannot adapt to changing conditions
- Errors cascade through execution
- No opportunity to correct course
- Brittle to unexpected outcomes

**Solution**: Implement observe-plan-act loop
```python
class ReflectiveAgent:
    def run(self, task):
        state = self.observe()
        history = []
        
        while not self.is_complete(task, state):
            # Plan based on current state
            plan = self.planner.generate(task, state, history)
            
            # Execute one step
            action = plan[0]
            result = self.execute(action)
            
            # Observe new state
            new_state = self.observe()
            
            # Update history
            history.append({
                "action": action,
                "result": result,
                "state_before": state,
                "state_after": new_state
            })
            
            state = new_state
            
            # Check if we need to replan
            if self.is_stuck(history):
                self.replan(task, history)
        
        return self.summarize(history)
```

### Unbounded Tool Usage

**Bad Example**:
```python
class UnrestrictedAgent:
    tools = [SearchTool(), CalculatorTool(), CodeExecutor(), ...]
    
    def run(self, task):
        while True:
            # Can call any tool infinitely
            tool_name, args = self.decide_tool(task)
            result = self.tools[tool_name].execute(args)
            
            # No limits on API calls, compute, or time
```

**Why It's Bad**:
- Runaway API costs
- Infinite loops possible
- Resource exhaustion
- Potential for abuse

**Solution**: Implement safeguards and limits
```python
class SafeAgent:
    def __init__(self, config):
        self.max_iterations = config.max_iterations
        self.max_api_calls = config.max_api_calls
        self.timeout = config.timeout
        self.allowed_tools = config.allowed_tools
        self.cost_budget = config.cost_budget
    
    def run(self, task):
        start_time = time.time()
        iteration_count = 0
        api_call_count = 0
        total_cost = 0
        
        while iteration_count < self.max_iterations:
            # Check timeout
            if time.time() - start_time > self.timeout:
                raise TimeoutError("Agent exceeded time limit")
            
            # Check API budget
            if api_call_count >= self.max_api_calls:
                raise BudgetExceeded("Max API calls reached")
            
            # Check cost budget
            if total_cost >= self.cost_budget:
                raise BudgetExceeded("Cost budget exceeded")
            
            # Execute with monitoring
            tool_name, args = self.decide_tool(task)
            if tool_name not in self.allowed_tools:
                raise SecurityError(f"Tool {tool_name} not allowed")
            
            result, cost = self.tools[tool_name].execute(args)
            total_cost += cost
            api_call_count += 1
            iteration_count += 1
```

### Poor Error Handling

**Bad Example**:
```python
class FragileAgent:
    def run(self, task):
        plan = self.planner.generate(task)
        
        for step in plan:
            # No error handling
            result = self.execute(step)
            # If this fails, entire agent crashes
        
        return result
```

**Why It's Bad**:
- Single failure stops everything
- No recovery mechanism
- Poor user experience
- Hard to diagnose issues

**Solution**: Robust error handling with retry and fallback
```python
class ResilientAgent:
    def run(self, task):
        max_retries = 3
        history = []
        
        for attempt in range(max_retries):
            try:
                plan = self.planner.generate(task, history)
                
                for step in plan:
                    try:
                        result = self.execute_with_timeout(step, timeout=30)
                        history.append({"step": step, "result": result, "status": "success"})
                    except TimeoutError:
                        history.append({"step": step, "error": "timeout", "status": "failed"})
                        self replan_after_failure(history)
                    except ToolError as e:
                        history.append({"step": step, "error": str(e), "status": "failed"})
                        alternative = self.find_alternative(step)
                        if alternative:
                            result = self.execute(alternative)
                            history.append({"step": alternative, "result": result})
                
                return self.summarize(history)
                
            except PlanningError:
                if attempt == max_retries - 1:
                    raise
                self.wait_and_retry(attempt)
```

### Missing Memory Management

**Bad Example**:
```python
class StatelessAgent:
    def run(self, task):
        # Forgets everything between interactions
        response = llm.generate(task)
        return response
    
    # Cannot learn from past interactions
    # Repeats same mistakes
```

**Why It's Bad**:
- No learning from experience
- Repeats errors
- Cannot build on previous work
- Poor long-term task handling

**Solution**: Implement memory systems
```python
class MemoryAgent:
    def __init__(self):
        self.short_term = []  # Current conversation
        self.long_term = VectorStore()  # Persistent memories
        self.working_memory = {}  # Task-specific state
    
    def run(self, task):
        # Retrieve relevant memories
        relevant = self.long_term.search(task, k=5)
        
        # Build context with memory
        context = self.build_context(task, relevant)
        
        # Generate response
        response = self.llm.generate(context)
        
        # Update short-term memory
        self.short_term.append({"task": task, "response": response})
        
        # Consolidate important info to long-term
        if self.should_memorize(task, response):
            self.long_term.add({
                "content": f"{task}: {response}",
                "metadata": {"timestamp": time.time()}
            })
        
        return response
```

## Real-World Scenarios

### Scenario 1: Customer Service Agent
Unbounded tool usage leads to excessive API calls, running up costs and hitting rate limits during peak hours.

### Scenario 2: Research Assistant Agent
Missing observation loop causes agent to cite outdated sources without verifying current information.

### Scenario 3: Code Generation Agent
Poor error handling means a single compilation error stops the entire development workflow.

## Detection Patterns

Watch for these warning signs:
- Agents running indefinitely
- Excessive API costs
- Repeated failed actions
- No adaptation to feedback
- Crashes on minor errors
- Forgetting context mid-task

## Prevention Strategies

1. **Define Clear Goals**: Specify success criteria explicitly
2. **Implement Feedback Loops**: Observe-plan-act cycles
3. **Set Boundaries**: Limits on iterations, costs, time
4. **Handle Errors Gracefully**: Retry, fallback, recover
5. **Manage Memory**: Short-term and long-term storage
6. **Monitor Behavior**: Log actions, track metrics
7. **Test Extensively**: Edge cases, failure scenarios

## Testing Checklist

- [ ] Are goals and success criteria clearly defined?
- [ ] Does agent observe before acting?
- [ ] Are there bounds on iterations and resources?
- [ ] Does agent handle errors gracefully?
- [ ] Is memory managed appropriately?
- [ ] Can agent recover from failures?
- [ ] Are actions logged and auditable?

## Related Documents

- [[bad_system_prompts]] - Prompt issues affecting agent behavior
- [[hallucination_examples]] - When agents generate false information
- [[prompt_injection_examples]] - Security vulnerabilities in agents
- [[unsafe_code]] - Safety concerns with code-executing agents
