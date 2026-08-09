---
# Metadata
title: "Debugging"
description: "Systematically identify, isolate, and fix bugs in code"
category: "Behavior Skills"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Behavior Skills Team"
next_review: "2027-01-15"

# Classification
tags:
  - debugging
  - troubleshooting
  - problem-solving
  - root-cause-analysis
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Debugging Skill

## Overview

Systematically identify, isolate, and fix bugs in code. This skill provides a structured approach to debugging that minimizes guesswork and maximizes learning.

## Core Competencies

- **Systematic Reproduction**: Consistently reproduce bugs to confirm and document them
- **Binary Search Isolation**: Narrow down bug location by halving the search space repeatedly
- **Hypothesis Testing**: Form testable explanations and verify one variable at a time
- **Tool Proficiency**: Use debuggers, loggers, and git bisect effectively
- **Root Cause Analysis**: Identify underlying causes, not just symptoms, and prevent recurrence

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

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Shotgun debugging | Random changes introduce new bugs | Change one variable at a time |
| Fixing symptoms only | Bug returns in different form | Trace to root cause before fixing |
| No regression test | Same bug recurs after future changes | Always add a test for the fix |
| Ignoring edge cases | Bug reappears with different inputs | Test boundary conditions thoroughly |
| Tunnel vision on one hypothesis | Misses the actual root cause | Consider multiple hypotheses in parallel |

## Best Practices

1. **Reproduce first**: Never attempt a fix until you can reliably reproduce the issue
2. **Read the error message carefully**: Most bugs tell you exactly what's wrong if you listen
3. **Use a debugger**: Step through code instead of adding print statements blindly
4. **Check recent changes**: `git log` and `git diff` often reveal the culprit quickly
5. **Rubber duck**: Explain the problem out loud — articulation reveals solutions
6. **Add the regression test**: Every bug fix should include a test that would have caught it

## Tools & Resources

- **IDE Debuggers** - VS Code, JetBrains, browser DevTools for breakpoints and stepping
- **Git Bisect** - Binary search through commit history to find when a bug was introduced
- **Logging frameworks** - Python `logging`, JavaScript `console`, structured logging with levels
- **`pdb`/`gdb`** - Command-line debuggers for Python and C/C++
- **Rubber Duck Debugging** - Explain the code line-by-line to find the issue

## Example Application

**Scenario:** Production API returns 500 errors intermittently under high load

**Application:**
1. **Reproduce**: Confirmed error occurs when >50 concurrent requests hit `/api/users` endpoint
2. **Isolate**: Binary search through middleware stack — error in auth token validation module
3. **Hypothesis**: Race condition in token cache — shared dictionary accessed without locking
4. **Test**: Added thread lock around cache access → errors stopped in staging
5. **Fix & Verify**: Deployed fix, added load test to CI pipeline, error rate dropped to 0%

**Outcome:** Bug resolved in 4 hours. Load test added to prevent regression. Team documented the race condition pattern for future reference.

## Success Indicators

You've mastered debugging when you can:

- ✅ Reproduce any reported bug consistently within 15 minutes
- ✅ Isolate the root cause without guessing or making random changes
- ✅ Write a regression test for every bug fix
- ✅ Use a debugger proficiently (breakpoints, stepping, watch expressions)
- ✅ Document bugs and fixes to build team knowledge
- ✅ Reduce mean time to resolution by >50% over baseline

## Related Skills

- [Learning](learning.md) - Learning from bugs to build institutional knowledge
- [Planning](planning.md) - Structured approach to investigation
- [Unit Testing](../testing-skills/unit_testing.md) - Writing regression tests
- [Algorithm Design](../technical-skills/algorithm_design.md) - Understanding code logic paths

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
