# برگه مرجع سینتکس پایتون

Quick reference for Python 3.x syntax and common patterns.

---

## Basic Syntax

### Variables and Data Types
```python
# Variable assignment (no declaration needed)
x = 5
name = "Alice"
is_active = True
price = 19.99

# Type checking
type(x)           # <class 'int'>
isinstance(x, int)  # True

# Type conversion
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### Strings
```python
s = "Hello, World!"

# Slicing
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # Reverse string

# Methods
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # Remove whitespace
f"Value: {x}"     # f-string formatting
```

---

## Control Flow

### شرطی‌ها
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# Ternary operator
result = "yes" if condition else "no"
```

### حلقه‌ها
```python
# For loop
for i in range(5):      # 0 to 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# While loop
while x < 10:
    x += 1

# Loop control
break       # Exit loop
continue    # Skip to next iteration
else:       # Execute if loop completes without break
```

---

## Data Structures

### Lists
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # Add to end
lst.insert(0, 0)        # Insert at index
lst.remove(3)           # Remove by value
lst.pop()               # Remove and return last
lst.pop(0)              # Remove and return first
lst.index(2)            # Find index of value
lst.count(2)            # Count occurrences
lst.sort()              # Sort in place
sorted(lst)             # Return sorted copy
lst.reverse()           # Reverse in place
lst[1:4]                # Slice
[i*2 for i in lst]      # List comprehension
```

### Dictionaries
```python
d = {"name": "Alice", "age": 30}

d["age"]                # Access value
d.get("age", 0)         # Safe access with default
d.keys()                # Get all keys
d.values()              # Get all values
d.items()               # Get key-value pairs
d.update({"city": "NYC"})
del d["age"]            # Delete key

{k: v*2 for k, v in d.items()}  # Dict comprehension
```

### Sets
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - duplicates removed

s.add(5)
s.remove(3)
s.discard(10)           # Remove if exists (no error)
s.union({4, 5, 6})      # Combine sets
s.intersection({2, 3})  # Common elements
s.difference({3, 4})    # Elements in s but not other
```

### Tuples
```python
t = (1, 2, 3)
t[0]                    # Access (immutable)
x, y, z = t             # Unpacking
```

---

## توابع

### Definition
```python
def greet(name, greeting="Hello"):
    """Docstring: Describe the function"""
    return f"{greeting}, {name}!"

# Call with positional and keyword args
greet("Alice")
greet("Bob", greeting="Hi")

# Variable arguments
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### Lambda Functions
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## کلاس‌ها

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age
    
    def greet(self):          # Instance method
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# Inheritance
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## File I/O

```python
# Reading files
with open("file.txt", "r") as f:
    content = f.read()        # Read entire file
    lines = f.readlines()     # Read as list of lines

# Writing files
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Append mode
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
except Exception as e:
    print(f"General error: {e}")
else:
    print("No errors occurred")
finally:
    print("Always executes")

# Raise exceptions
raise ValueError("Invalid value")
```

---

## Modules and Imports

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# Common standard library modules
os, sys, json, re, random, itertools, functools, pathlib
```

---

## Common Patterns

### List Operations
```python
# Filter
evens = [x for x in lst if x % 2 == 0]

# Map
squares = [x**2 for x in lst]

# Zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# Enumerate
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### String Operations
```python
# Join list of strings
", ".join(["a", "b", "c"])  # "a, b, c"

# Split string
"a,b,c".split(",")          # ['a', 'b', 'c']

# Check substring
"test" in "this is a test"  # True

# Format strings
"{} {}".format("Hello", "World")
f"{value:.2f}"              # 2 decimal places
```

### Dictionary Operations
```python
# Merge dictionaries
{**d1, **d2}
d1 | d2                     # Python 3.9+

# Default value
d.get("key", default_value)

# Iterate
for k, v in d.items():
    pass
```

---

## Built-in Functions

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce from functools
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## Quick Tips

- Use `#` for single-line comments
- Use `"""triple quotes"""` for docstrings and multi-line strings
- Indentation matters (typically 4 spaces)
- Naming conventions: `snake_case` for variables/functions, `PascalCase` for classes
- `__name__ == "__main__"` to check if script is run directly
- Use `virtualenv` or `venv` for project isolation
- Install packages with `pip install package_name`

---

*Last updated: June 2025 | Python 3.x*
