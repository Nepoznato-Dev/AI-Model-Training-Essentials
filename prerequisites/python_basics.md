# Python Basics: 10 Essential Concepts 🐍

**Time to complete:** 20 minutes  
**Prerequisites:** [Terminal Basics](./terminal_basics.md)

---

## Why Python for AI?

Python is the #1 language for AI because:
- ✅ Simple, readable syntax
- ✅ Huge library ecosystem (PyTorch, TensorFlow, etc.)
- ✅ Great community support
- ✅ Perfect for beginners

---

## 1. Variables: Storing Data

Variables are like labeled boxes where you store information.

```python
# No need to declare types!
name = "Alice"           # String (text)
age = 25                 # Integer (whole number)
height = 5.7             # Float (decimal)
is_student = True        # Boolean (True/False)

print(name)              # Output: Alice
print(f"{name} is {age}") # Output: Alice is 25
```

---

## 2. Lists: Collections of Items

Lists store multiple items in order.

```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access items (starts at 0!)
print(fruits[0])         # Output: apple
print(fruits[-1])        # Output: cherry (last item)

# Modify lists
fruits.append("orange")  # Add to end
fruits[1] = "blueberry"  # Change item

# Slice a list (get a portion)
print(fruits[1:3])       # Output: ['blueberry', 'cherry']

# List length
print(len(fruits))       # Output: 4
```

---

## 3. Dictionaries: Key-Value Pairs

Dictionaries store data with labels (keys).

```python
# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access values
print(person["name"])    # Output: Alice
print(person.get("age")) # Output: 25

# Add/modify
person["job"] = "Engineer"  # Add new key
person["age"] = 26          # Modify existing

# Get all keys or values
print(person.keys())   # Output: dict_keys(['name', 'age', 'city', 'job'])
print(person.values()) # Output: dict_values(['Alice', 26, 'New York', 'Engineer'])
```

---

## 4. If Statements: Making Decisions

Control flow based on conditions.

```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")   # This runs!
else:
    print("Adult")

# Comparison operators
# == equal, != not equal
# < less than, > greater than
# <= less than or equal, >= greater than or equal

# Logical operators
if age >= 18 and age < 65:
    print("Working age")

if age < 13 or age > 65:
    print("Not working age")
```

---

## 5. For Loops: Repeating Actions

Loop through items or ranges.

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Loop through a range
for i in range(5):      # 0 to 4
    print(i)

for i in range(2, 6):   # 2 to 5
    print(i)
```

---

## 6. While Loops: Repeat Until Condition

Keep looping while condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1          # Same as: count = count + 1

# Be careful of infinite loops!
# while True:           # This runs forever!
#     print("Help!")
```

---

## 7. Functions: Reusable Code Blocks

Functions let you package code for reuse.

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)          # Output: Hello, Alice!

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))         # Output: 9 (3 squared)
print(power(3, 3))      # Output: 27 (3 cubed)

# Multiple return values
def get_person():
    return "Alice", 25, "NYC"

name, age, city = get_person()
```

---

## 8. List Comprehensions: Compact List Creation

Create lists in one line.

```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)          # Output: [0, 1, 4, 9, 16]

# List comprehension (same result)
squares = [i ** 2 for i in range(5)]
print(squares)          # Output: [0, 1, 4, 9, 16]

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(evens)            # Output: [0, 2, 4, 6, 8]

# Transform a list
names = ["alice", "bob", "charlie"]
capitalized = [name.upper() for name in names]
print(capitalized)      # Output: ['ALICE', 'BOB', 'CHARLIE']
```

---

## 9. Importing Libraries: Using Others' Code

Libraries extend Python's capabilities.

```python
# Import entire library
import math
print(math.sqrt(16))    # Output: 4.0

# Import specific functions
from math import sqrt, pi
print(sqrt(25))         # Output: 5.0
print(pi)               # Output: 3.14159...

# Import with alias
import numpy as np
import pandas as pd

# Common AI libraries
# import torch          # PyTorch
# import tensorflow     # TensorFlow
# import transformers   # Hugging Face
```

---

## 10. Error Handling: Dealing with Problems

Handle errors gracefully.

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Multiple exceptions
try:
    age = int(input("Enter age: "))
    result = 100 / age
except ValueError:
    print("Please enter a number!")
except ZeroDivisionError:
    print("Age can't be zero!")

# Catch any error
try:
    risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    print("This always runs!")
```

---

## Putting It All Together

Here's a complete example using all concepts:

```python
# AI Training Simulator (simplified!)

def train_model(data, epochs=3):
    """Simulate training an AI model"""
    results = []
    
    for epoch in range(epochs):
        print(f"Epoch {epoch + 1}/{epochs}")
        
        # Process each data item
        for item in data:
            if item["quality"] < 0.5:
                continue  # Skip low quality data
            
            # Simulate learning
            accuracy = item["quality"] * (epoch + 1) / epochs
            
            if accuracy > 0.8:
                print(f"  ✓ Good progress: {accuracy:.2f}")
            else:
                print(f"  - Learning: {accuracy:.2f}")
        
        results.append({"epoch": epoch + 1, "accuracy": accuracy})
    
    return results

# Prepare training data
training_data = [
    {"text": "Hello", "quality": 0.9},
    {"text": "Hi", "quality": 0.7},
    {"text": "xyz", "quality": 0.3},  # Low quality
    {"text": "Good morning", "quality": 0.95},
]

# Train the model
final_results = train_model(training_data, epochs=3)

print(f"\nTraining complete! Final accuracy: {final_results[-1]['accuracy']:.2f}")
```

---

## Practice Exercises

### Exercise 1: Temperature Converter
Write a function that converts Celsius to Fahrenheit.
Formula: `F = C * 9/5 + 32`

<details>
<summary>Click for solution</summary>

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_to_fahrenheit(25))  # Output: 77.0
```
</details>

### Exercise 2: Find Even Numbers
Create a list comprehension that filters even numbers from a list.

<details>
<summary>Click for solution</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```
</details>

### Exercise 3: Word Counter
Write a function that counts words in a sentence.

<details>
<summary>Click for solution</summary>

```python
def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Hello world this is Python"))  # Output: 5
```
</details>

---

## Common Errors & Fixes

### Error: `IndentationError`
**Cause:** Inconsistent spacing (Python is picky about indentation!)  
**Fix:** Use 4 spaces per indent level, never mix tabs and spaces

```python
# Wrong ❌
def my_function():
print("Hello")  # Not indented!

# Right ✅
def my_function():
    print("Hello")  # 4 spaces
```

### Error: `NameError: name 'x' is not defined`
**Cause:** Using a variable before creating it  
**Fix:** Define variables before using them

### Error: `TypeError: 'int' object is not iterable`
**Cause:** Trying to loop over a non-iterable  
**Fix:** Use `range()` for numbers

```python
# Wrong ❌
for i in 5:
    print(i)

# Right ✅
for i in range(5):
    print(i)
```

### Error: `IndexError: list index out of range`
**Cause:** Accessing an index that doesn't exist  
**Fix:** Check list length first

```python
my_list = [1, 2, 3]
# my_list[5]  # Error! Only indices 0, 1, 2 exist
```

---

## Next Steps

✅ You now know Python basics!  
➡️ Next: [Git Basics](./git_basics.md)  
➡️ Then: Start the [RAG Guide](../guides/RAG/)

---

## Quick Reference Cheat Sheet

```python
# Variables
x = 5

# Lists
my_list = [1, 2, 3]
my_list.append(4)

# Dictionaries
my_dict = {"key": "value"}

# If statements
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# For loops
for i in range(5):
    print(i)

# Functions
def my_func(param):
    return param * 2

# List comprehension
squares = [x**2 for x in range(5)]

# Import libraries
import math
from math import sqrt

# Error handling
try:
    risky_code()
except Exception as e:
    print(f"Error: {e}")
```

---

**Congratulations!** You've learned the 10 essential Python concepts needed for AI! 🎉
