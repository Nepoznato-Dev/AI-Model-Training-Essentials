---
# Metadata
title: "Python — Cheat Sheet"
description: "Quick-reference cheat sheet for Python syntax, built-ins, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [python, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# पायथन - चीट शीट
## मूल बातें
```python
# Variables (no type declaration needed)
name = "Alice"
age = 30
pi = 3.14159
is_active = True
items = [1, 2, 3]

# Type checking
type(name)        # <class 'str'>
isinstance(age, int)  # True

# String operations
f"Hello, {name}!"     # f-string (3.6+)
name.upper()           # "ALICE"
name.lower()           # "alice"
name.strip()           # remove whitespace
"hello world".split()  # ['hello', 'world']
", ".join(items_str)   # "1, 2, 3"
```

## डेटा संरचनाएँ
```python
# List
nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)
nums.pop()           # remove & return last
nums[1:3]            # slicing [2, 3]
[x**2 for x in range(5)]  # list comprehension

# Dict
user = {"name": "Alice", "age": 30}
user["email"] = "a@b.com"
user.get("phone", "N/A")  # default value
{k: v for k, v in pairs}  # dict comprehension

# Set
s = {1, 2, 3}
s.add(4)
s | {5}       # union
s & {2, 3}    # intersection

# Tuple (immutable)
point = (3, 4)
x, y = point  # unpacking
```

## प्रवाह को नियंत्रित करें
```python
if condition:
    ...
elif other:
    ...
else:
    ...

# Ternary
result = "yes" if condition else "no"

# Loops
for item in iterable:
    ...

for i, val in enumerate(items):
    ...

for k, v in my_dict.items():
    ...

while condition:
    ...

# Match (3.10+)
match command:
    case "quit": exit()
    case "go" | "run": start()
    case _: print("unknown")
```

## कार्य
```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# *args and **kwargs
def flexible(*args, **kwargs):
    print(args)    # tuple of positional
    print(kwargs)  # dict of keyword

# Lambda
square = lambda x: x ** 2

# Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.2f}s")
        return result
    return wrapper
```

## कक्षाएं
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"

# Dataclass (3.7+)
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"
```

## त्रुटि प्रबंधन
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
else:
    print("No error")
finally:
    print("Always runs")

# Raise
raise ValueError(f"Invalid value: {value}")
```

## मॉड्यूल और आयात
```python
import os
from pathlib import Path
from typing import Optional, List, Dict
from collections import defaultdict, Counter

# Common stdlib
os.path.exists("file.txt")
Path("data").mkdir(parents=True, exist_ok=True)
sorted(items, key=len, reverse=True)
```

## सामान्य पैटर्न
```python
# Unpacking
first, *rest = [1, 2, 3, 4]
a, b = b, a  # swap

# Context manager
with open("file.txt") as f:
    content = f.read()

# Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Walrus operator (3.8+)
if (n := len(items)) > 10:
    print(f"Too many: {n}")
```
