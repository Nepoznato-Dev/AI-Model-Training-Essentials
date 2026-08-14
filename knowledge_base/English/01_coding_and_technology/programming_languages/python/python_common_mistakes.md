---
# Metadata
title: "Python — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Python that catch even experienced developers, with explanations and corrections."
category: "Coding and Technology"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [python, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Python — Common Mistakes & Anti-Patterns

This document catalogs the most common mistakes, traps, and anti-patterns in Python. Each entry shows the incorrect approach, explains why it fails, and provides the correct solution. Understanding these pitfalls will help you write more robust, Pythonic code.

---

## 1. Mutable Default Arguments

```python
# ❌ WRONG — shared across all calls
def append_to(element, lst=[]):
    lst.append(element)
    return lst

append_to(1)  # [1]
append_to(2)  # [1, 2] — not [2]!

# ✅ CORRECT — use None as sentinel
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

**Why it happens:** Default arguments are evaluated once at function definition time, not at each call. A mutable default (list, dict, set) is shared across all invocations.

---

## 2. Modifying a List While Iterating

```python
# ❌ WRONG — skips elements
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
# numbers = [1, 3, 5] — but 4 was skipped!

# ✅ CORRECT — iterate over a copy or use list comprehension
numbers = [n for n in numbers if n % 2 != 0]

# ✅ CORRECT — iterate in reverse if modifying in-place
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        del numbers[i]
```

---

## 3. Late Binding in Closures

```python
# ❌ WRONG — all lambdas capture the same variable
funcs = [lambda: i for i in range(5)]
[f() for f in funcs]  # [4, 4, 4, 4, 4] — not [0, 1, 2, 3, 4]

# ✅ CORRECT — capture with default argument
funcs = [lambda i=i: i for i in range(5)]
[f() for f in funcs]  # [0, 1, 2, 3, 4]

# ✅ CORRECT — use functools.partial
from functools import partial
funcs = [partial(lambda x: x, i) for i in range(5)]
```

---

## 4. Using `type()` Instead of `isinstance()`

```python
# ❌ WRONG — ignores inheritance
class Dog(Animal):
    pass

dog = Dog()
type(dog) == Animal  # False!

# ✅ CORRECT — respects inheritance
isinstance(dog, Animal)  # True
```

---

## 5. Not Using Context Managers for Resources

```python
# ❌ WRONG — file may stay open on exception
f = open("data.txt", "r")
data = f.read()
f.close()  # never reached if read() raises

# ✅ CORRECT — automatic cleanup
with open("data.txt", "r") as f:
    data = f.read()
```

---

## 6. The `is` Operator for Value Comparison

```python
# ❌ WRONG — `is` checks identity, not equality
x = 500
y = 500
x == y  # True
x is y  # False! (different objects; CPython caches only -5 to 256)

# ✅ CORRECT — use `==` for value comparison
x == y  # True

# `is` is only for singletons
value is None   # correct
value is True   # correct
```

---

## 7. Circular Imports

```python
# ❌ WRONG — a.py imports b.py, b.py imports a.py
# a.py
from b import func_b
def func_a():
    return func_b()

# b.py
from a import func_a  # ImportError!

# ✅ CORRECT — restructure to avoid circular dependency
# Move shared code to a third module, or use lazy imports
# c.py (shared)
def shared_logic():
    pass

# a.py
from c import shared_logic

# b.py
from c import shared_logic
```

---

## 8. Not Understanding Python's Scope Rules (LEGB)

```python
# ❌ WRONG — cannot modify outer scope variable
x = 10
def outer():
    x = 20
    def inner():
        x = 30  # creates a new local, doesn't modify outer's x
    inner()
    print(x)  # 20, not 30

# ✅ CORRECT — use nonlocal or global
def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
    inner()
    print(x)  # 30
```

---

## 9. String Concatenation in Loops

```python
# ❌ WRONG — creates a new string each iteration (O(n²))
result = ""
for word in words:
    result += word

# ✅ CORRECT — use join()
result = "".join(words)

# ✅ CORRECT — for complex formatting
from io import StringIO
buf = StringIO()
for word in words:
    buf.write(word)
result = buf.getvalue()
```

---

## 10. Anti-Pattern: Using `except:` Bare Except

```python
# ❌ WRONG — catches EVERYTHING including KeyboardInterrupt, SystemExit
try:
    do_something()
except:
    pass  # silently swallows all errors

# ❌ STILL BAD — catches BaseException
try:
    do_something()
except Exception as e:
    pass  # catches too much

# ✅ CORRECT — catch specific exceptions
try:
    do_something()
except ValueError as e:
    logger.error(f"Bad value: {e}")
except FileNotFoundError:
    logger.error("File not found")
```

---

## 11. Returning Mutable References to Internal State

```python
# ❌ WRONG — caller can corrupt internal state
class Config:
    def __init__(self):
        self._settings = {"debug": False, "verbose": True}

    def get_settings(self):
        return self._settings  # caller can mutate this!

# ✅ CORRECT — return a copy
import copy

def get_settings(self):
    return copy.deepcopy(self._settings)

# ✅ CORRECT — use a mapping proxy or property
from types import MappingProxyType

def get_settings(self):
    return MappingProxyType(self._settings)
```

---

## 12. Not Using `setdefault` or `collections.defaultdict`

```python
# ❌ WRONG — verbose and error-prone
groups = {}
for key, value in items:
    if key not in groups:
        groups[key] = []
    groups[key].append(value)

# ✅ CORRECT — use setdefault
groups.setdefault(key, []).append(value)

# ✅ CORRECT — use defaultdict
from collections import defaultdict
groups = defaultdict(list)
for key, value in items:
    groups[key].append(value)
```

---

## 13. Confusing `==` and `=` in Conditions

```python
# ❌ WRONG — this is assignment, always truthy
if result = compute():
    process(result)

# ✅ CORRECT — use comparison
if result == compute():
    process(result)

# ✅ CORRECT — assign and test (Python 3.8+)
if (result := compute()):
    process(result)
```

---

## 14. Not Understanding Generator Exhaustion

```python
# ❌ WRONG — generators can only be consumed once
gen = (x * 2 for x in range(5))
list(gen)  # [0, 2, 4, 6, 8]
list(gen)  # [] — exhausted!

# ✅ CORRECT — recreate or use a list if reuse is needed
gen = (x * 2 for x in range(5))
first_use = list(gen)

# ✅ CORRECT — use itertools.tee for multiple consumers
from itertools import tee
gen1, gen2 = tee((x * 2 for x in range(5)))
```

---

## 15. Anti-Pattern: God Objects / Overloaded Classes

```python
# ❌ WRONG — one class doing everything
class App:
    def connect_db(self): ...
    def query_users(self): ...
    def send_email(self): ...
    def render_template(self): ...
    def process_payment(self): ...

# ✅ CORRECT — single responsibility
class DatabaseConnection:
    def connect(self): ...
    def query(self, sql): ...

class EmailService:
    def send(self, to, subject, body): ...

class PaymentProcessor:
    def charge(self, amount, method): ...
```

---

## Summary

Python's simplicity is deceptive — mutable defaults, late binding closures, scope rules, and resource management all have subtle behaviors that trap developers. The key principles to remember: defaults are evaluated once, `is` checks identity not equality, always use context managers for resources, catch specific exceptions, and favor composition over god objects. Writing Pythonic code means understanding these pitfalls and using the language's features (context managers, comprehensions, generators, `collections` module) as intended.
