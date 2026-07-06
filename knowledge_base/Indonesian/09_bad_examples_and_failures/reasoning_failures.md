# Reasoning Failures

## Overview

Reasoning failures occur when AI systems make logical errors, fail to follow multi-step reasoning, or draw incorrect conclusions from valid premises. This document catalogs common reasoning failures and provides strategies for improvement.

## Types of Reasoning Failures

### Multi-Step Logic Errors

**Bad Example:**
```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Why It's Bad:**
- Commits the fallacy of affirming the consequent
- Alice could write code without being a programmer
- Logical structure: (P→Q, Q) ⊬ P

**Correct Reasoning:**
```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone 
who writes code is a programmer. Alice could be a student, hobbyist, or 
work in another field that involves coding.
```

### Mathematical Reasoning Failures

**Bad Example:**
```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball. 
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Why It's Bad:**
- Incorrect intuitive answer
- If ball = $0.10, then bat = $1.10, total = $1.20 (wrong)
- Fails to set up and solve equations properly

**Correct Reasoning:**
```
Let x = ball cost
Bat cost = x + 1.00
x + (x + 1.00) = 1.10
2x + 1.00 = 1.10
2x = 0.10
x = 0.05

The ball costs $0.05 (bat costs $1.05, total = $1.10).
```

### Temporal Reasoning Errors

**Bad Example:**
```
User: John was born in 1990. He graduated college at age 22. 
It's now 2024. How many years ago did he graduate?
Assistant: He graduated 2 years ago.
```

**Why It's Bad:**
- Graduation year: 1990 + 22 = 2012
- Years since graduation: 2024 - 2012 = 12 years
- Model failed to chain temporal calculations correctly

**Correct Reasoning:**
```
Birth year: 1990
Graduation age: 22
Graduation year: 1990 + 22 = 2012
Current year: 2024
Years since graduation: 2024 - 2012 = 12 years ago
```

### Causal Reasoning Failures

**Bad Example:**
```
User: Ice cream sales and drowning deaths both increase in summer. 
Does eating ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Why It's Bad:**
- Confuses correlation with causation
- Ignores confounding variable (hot weather)
- Both increase due to third factor, not direct causation

**Correct Reasoning:**
```
No, ice cream doesn't cause drowning. Both increase in summer due to 
a common cause: hot weather. More people swim in hot weather (increasing 
drowning risk) and more people buy ice cream. This is correlation, not 
causation.
```

### Counterfactual Reasoning Failures

**Bad Example:**
```
User: If I had left home 5 minutes earlier, I would have caught the train. 
The train leaves every 30 minutes. Would leaving 10 minutes earlier help?
Assistant: No, because you already missed it.
```

**Why It's Bad:**
- Fails to reason about counterfactual scenarios
- Doesn't consider the hypothetical properly
- Misses that 10 minutes earlier might catch an earlier train

**Correct Reasoning:**
```
In the counterfactual scenario where you left 10 minutes earlier instead 
of 5, you would have arrived even earlier, potentially catching the train. 
However, if trains run every 30 minutes and you only missed it by a few 
minutes, leaving 10 minutes earlier likely would have caught that same train.
```

## Real-World Scenarios

### Scenario 1: Planning and Scheduling

**Failure:**
```
User: I need to schedule meetings with teams in New York, London, and Tokyo. 
Find a time that works for everyone during their business hours (9 AM - 5 PM).
Assistant: 9 AM EST works for everyone.
```

**Problem:**
- 9 AM EST = 2 PM London (OK) but 11 PM Tokyo (not business hours)
- Failed to consider all timezone constraints simultaneously

**Better Approach:**
```
Finding overlap for 9 AM - 5 PM in each timezone:
- New York (EST): 9 AM - 5 PM
- London (GMT): 2 PM - 10 PM EST equivalent
- Tokyo (JST): 7 PM - 3 AM EST equivalent

No time works for all three during standard business hours. 
Consider rotating meeting times or accepting some inconvenience.
```

### Scenario 2: Resource Allocation

**Failure:**
```
User: I have 10 tasks taking 3 hours each. I have 2 workers and 8 hours per day. 
How many days to complete all tasks?
Assistant: 15 days.
```

**Problem:**
- Total work: 10 × 3 = 30 hours
- Daily capacity: 2 workers × 8 hours = 16 hours/day
- Days needed: 30 ÷ 16 = 1.875 → 2 days
- Model made arithmetic error

**Better Approach:**
```
Total task hours: 10 tasks × 3 hours = 30 hours
Daily capacity: 2 workers × 8 hours = 16 hours/day
Days required: 30 ÷ 16 = 1.875 days
Rounded up: 2 days to complete all tasks
```

### Scenario 3: Conditional Logic

**Failure:**
```
User: If it rains, bring an umbrella. If you bring an umbrella, you won't get wet. 
It's raining. Will you get wet?
Assistant: Maybe, umbrellas can fail.
```

**Problem:**
- Overcomplicates simple logical deduction
- Within the given premises: Rain → Umbrella → Not Wet
- Should follow the logical chain provided

**Better Approach:**
```
Following the given logic:
1. It's raining (given)
2. If raining → bring umbrella (premise 1)
3. If umbrella → won't get wet (premise 2)
Therefore: You won't get wet (within this logical framework)
```

## Detection Patterns

### Signs of Reasoning Failures

1. **Skipping Steps:**
   - Jumps directly to conclusions
   - Missing intermediate calculations
   - No visible reasoning chain

2. **Inconsistent Application:**
   - Applies rules differently in similar situations
   - Contradicts earlier reasoning
   - Changes logic mid-explanation

3. **Arithmetic Errors:**
   - Simple calculation mistakes
   - Unit conversion errors
   - Order of operations failures

4. **Logical Fallacies:**
   - Affirming the consequent
   - Denying the antecedent
   - False dichotomy
   - Circular reasoning

## Improvement Strategies

### Chain-of-Thought Prompting

```python
# BAD: Direct question
prompt = "If x + y = 10 and x - y = 2, what is x?"

# GOOD: Encourage step-by-step reasoning
prompt = """If x + y = 10 and x - y = 2, what is x?

Solve this step by step:
1. Write down the equations
2. Choose a method (substitution or elimination)
3. Show each algebraic step
4. Verify your answer
5. State the final answer"""
```

### Verification Steps

```python
def verify_reasoning(question, initial_answer):
    # Generate reasoning trace
    reasoning = generate_reasoning_trace(question)
    
    # Check each step
    steps_valid = validate_each_step(reasoning)
    
    # Verify final answer independently
    independent_answer = solve_independently(question)
    
    if steps_valid and initial_answer == independent_answer:
        return initial_answer
    else:
        return regenerate_with_corrections(question, reasoning)
```

### Self-Correction

```python
def self_correcting_response(prompt):
    # Initial response
    response = llm.generate(prompt)
    
    # Critique own response
    critique = llm.generate(f"Critique this answer for errors: {response}")
    
    # Revise based on critique
    revised = llm.generate(f"Original: {response}\nCritique: {critique}\nRevise:")
    
    return revised
```

## Testing Checklist

- [ ] Test multi-step mathematical problems
- [ ] Verify temporal reasoning across timezones
- [ ] Check conditional logic chains
- [ ] Test with classic logic puzzles
- [ ] Verify causal vs correlational reasoning
- [ ] Test counterfactual scenarios
- [ ] Check constraint satisfaction problems
- [ ] Validate resource allocation calculations
- [ ] Test syllogistic reasoning
- [ ] Verify probabilistic reasoning

## Related Documents

- [[logical_fallacies]] - Common reasoning errors and fallacies
- [[cognitive_biases]] - Human and AI cognitive biases
- [[hallucination_examples]] - Fabricated information
- [[bad_agent_design]] - Poor autonomous agent reasoning
