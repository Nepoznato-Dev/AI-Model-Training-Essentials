# Debugging Skill

## Overview

Systematically identify, isolate, and fix bugs in code. This skill provides a structured approach to debugging that minimizes guesswork and maximizes learning.

## When to Use

- A test is failing unexpectedly
- Production code is behaving incorrectly
- You encounter an error message you don't understand
- Performance has degraded unexpectedly
- Features work in some environments but not others

## The Debugging Workflow

### Step 1: Reproduce the Bug

**Goal:** Confirm the bug exists consistently.

**Actions:**
1. Document the exact steps to reproduce
2. Note the environment (OS, browser, versions)
3. Identify the frequency (always, intermittent, rare)
4. Capture error messages and stack traces

```
Bug Report Template:
- What I did: [actions taken]
- What I expected: [expected behavior]
- What happened: [actual behavior]
- Environment: [system details]
- Frequency: [how often it occurs]
```

**Tip:** If you can't reproduce it reliably, you can't fix it reliably.

### Step 2: Isolate the Problem

**Goal:** Narrow down where the bug originates.

**Techniques:**

#### Binary Search (Divide and Conquer)
Split the code path in half repeatedly until you find the smallest section containing the bug.

```
Code Path: A → B → C → D → E → F
                    │
              Bug happens somewhere here

Test at C: Works → Bug is in D, E, or F
Test at E: Fails → Bug is in D or E
Test at D: Works → Bug is in E
```

#### Comment Out / Disable
Temporarily remove sections of code to see if the bug persists.

#### Add Logging
Insert strategic log statements to trace execution flow and variable values.

```python
# Before
def process_data(data):
    result = transform(data)
    return validate(result)

# After - with debugging logs
def process_data(data):
    logger.debug(f"Input data: {data}")
    result = transform(data)
    logger.debug(f"After transform: {result}")
    validated = validate(result)
    logger.debug(f"After validate: {validated}")
    return validated
```

### Step 3: Form a Hypothesis

**Goal:** Create a testable explanation for the bug.

**Structure:**
```
I think [bug description] is happening because [hypothesis].
If I'm right, then [prediction] should occur when I [test action].
```

**Example:**
```
I think the null pointer exception is happening because the user 
object isn't initialized before being accessed.
If I'm right, then adding a null check before line 42 should prevent the crash.
```

### Step 4: Test Your Hypothesis

**Goal:** Prove or disprove your hypothesis.

**Methods:**
- Add assertions to verify assumptions
- Write a minimal reproduction case
- Use a debugger to step through code
- Modify inputs to test edge cases

**Important:** Test one variable at a time. Changing multiple things makes it hard to know what fixed the bug.

### Step 5: Fix and Verify

**Goal:** Implement the fix and ensure it works.

**Checklist:**
1. ✅ Implement the minimal fix
2. ✅ Verify the original bug is gone
3. ✅ Run existing tests to check for regressions
4. ✅ Add a test case to prevent this bug from returning
5. ✅ Consider if similar bugs exist elsewhere

## Debugging Tools

### Print Statements / Logging
Quick and dirty, but effective for tracing execution.

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

### Debugger
Use your IDE's debugger or tools like `pdb`, `gdb`, or browser DevTools.

**Key debugger actions:**
- Breakpoints: Pause execution at specific lines
- Step Over: Execute current line, move to next
- Step Into: Enter function calls
- Step Out: Exit current function
- Watch: Monitor variable values
- Call Stack: See the path to current execution

### Rubber Duck Debugging
Explain your code line-by-line to an inanimate object (or patient colleague). The act of articulation often reveals the problem.

### Git Bisect
Find which commit introduced a bug using binary search through history.

```bash
git bisect start
git bisect bad          # Current version has the bug
git bisect good v1.0    # This version was good
# Git checks out commits; test each and mark good/bad
git bisect reset        # When done
```

## Common Bug Patterns

### Off-by-One Errors
```python
# Wrong: loops 0 to n (inclusive), accessing n+1 elements
for i in range(len(array) + 1):
    process(array[i])

# Right: loops 0 to n-1
for i in range(len(array)):
    process(array[i])
```

### Null/Undefined References
```javascript
// Wrong: assumes property exists
const name = user.profile.name;

// Right: defensive coding
const name = user?.profile?.name ?? 'Anonymous';
```

### Race Conditions
```python
# Wrong: not thread-safe
counter = counter + 1

# Right: use locks or atomic operations
with lock:
    counter = counter + 1
```

### Incorrect Assumptions About Data
```python
# Wrong: assumes sorted data
min_value = data[0]

# Right: explicitly find minimum
min_value = min(data) if data else None
```

## Anti-Patterns to Avoid

❌ **Shotgun Debugging:** Randomly changing code until it works
❌ **Fixing Symptoms:** Addressing the error message instead of the root cause
❌ **Ignoring Edge Cases:** Only testing the happy path
❌ **Premature Optimization:** Trying to make it faster before making it correct
❌ **No Regression Tests:** Fixing without adding tests to catch future occurrences
❌ **Tunnel Vision:** Sticking to one hypothesis despite contradictory evidence

## Learning from Bugs

After fixing a bug, ask:
1. **Why** did this bug occur? (Root cause)
2. **How** could we have caught it earlier?
3. **What** can we add to prevent similar bugs?
4. **Where** else might this pattern exist?

Document significant bugs in a team wiki or issue tracker to build institutional knowledge.
