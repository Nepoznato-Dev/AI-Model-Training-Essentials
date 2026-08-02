# Python Basics for AI Development

**Time needed:** 15-20 minutes  
**Goal:** Learn the 10 essential Python concepts you need for AI

---

## Why Python for AI?

Python is the #1 language for AI because:
- ✅ Easy to read and write
- ✅ Huge library ecosystem (PyTorch, TensorFlow, etc.)
- ✅ Great community support
- ✅ Perfect for prototyping and experimentation

---

## The 10 Essential Concepts

### 1. Variables and Data Types

Variables store information. Python has several types:

```python
# String (text)
name = "Alice"

# Integer (whole number)
age = 25

# Float (decimal number)
height = 5.7

# Boolean (True/False)
is_student = True

# Print them
print(name)        # Output: Alice
print(age)         # Output: 25
print(type(age))   # Output: <class 'int'>
```

**Try it:** Create variables for your name, age, and favorite number, then print them.

---

### 2. Lists (Storing Multiple Items)

Lists hold collections of items:

```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access items (index starts at 0!)
print(fruits[0])    # Output: apple
print(fruits[1])    # Output: banana

# Add items
fruits.append("orange")

# Get length
print(len(fruits))  # Output: 4

# Loop through a list
for fruit in fruits:
    print(fruit)
```

**AI connection:** You'll use lists to store datasets, model predictions, and more!

---

### 3. Dictionaries (Key-Value Pairs)

Dictionaries store data as key-value pairs:

```python
# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access values by key
print(person["name"])    # Output: Alice
print(person["age"])     # Output: 25

# Add new key-value
person["job"] = "Engineer"

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

**AI connection:** Dictionaries are used for configuration settings, model parameters, and data batches.

---

### 4. If Statements (Making Decisions)

Control flow with conditions:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators:
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
```

**Try it:** Write an if statement that checks if a number is positive, negative, or zero.

---

### 5. For Loops (Repeating Actions)

Repeat code for each item in a sequence:

```python
# Loop through a range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# Loop through a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Loop with index
for i, color in enumerate(colors):
    print(f"{i}: {color}")
    # Output: 
    # 0: red
    # 1: green
    # 2: blue
```

**AI connection:** You'll use loops to iterate through datasets, training epochs, and model layers.

---

### 6. Functions (Reusable Code Blocks)

Functions let you package code for reuse:

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)    # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)     # Output: 8

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # Output: 9 (3^2)
print(power(3, 3))    # Output: 27 (3^3)
```

**Try it:** Write a function that takes a list of numbers and returns their average.

---

### 7. List Comprehensions (Concise List Creation)

A compact way to create lists:

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension (same result, one line!)
squares = [i ** 2 for i in range(10)]

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]

# Transform a list
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)    # Output: [2, 4, 6, 8, 10]
```

**AI connection:** Used extensively for data preprocessing and transforming datasets.

---

### 8. Importing Libraries (Using Other People's Code)

Python has thousands of libraries. Import them to use their functions:

```python
# Import entire library
import math

print(math.sqrt(16))    # Output: 4.0
print(math.pi)          # Output: 3.14159...

# Import specific functions
from math import sqrt, pi

print(sqrt(25))         # Output: 5.0

# Import with alias (common convention)
import numpy as np
import pandas as pd

# Use the alias
arr = np.array([1, 2, 3])
```

**Common AI libraries:**
```python
import torch              # PyTorch for deep learning
import tensorflow as tf   # TensorFlow for deep learning
import numpy as np        # Numerical computing
import pandas as pd       # Data manipulation
import matplotlib.pyplot as plt  # Visualization
```

---

### 9. Working with Files

Read and write files:

```python
# Write to a file
with open("myfile.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is AI training!")

# Read from a file
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("myfile.txt", "r") as f:
    for line in f:
        print(line.strip())    # .strip() removes newline characters
```

**AI connection:** You'll load datasets from files, save model weights, and log training results.

---

### 10. Error Handling (Try/Except)

Handle errors gracefully:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("Operation complete!")
```

**AI connection:** Essential for debugging model training and handling missing data.

---

## Putting It All Together: Mini Project

Create a simple data analyzer:

```python
# Sample dataset (e.g., daily temperatures)
temperatures = [72, 75, 68, 80, 82, 79, 76, 74, 71, 77]

# Calculate statistics using what we learned
def analyze_data(data):
    """Analyze a list of numbers"""
    
    # Basic stats
    average = sum(data) / len(data)
    minimum = min(data)
    maximum = max(data)
    
    # Find hot days (above average)
    hot_days = [temp for temp in data if temp > average]
    
    # Return results as dictionary
    return {
        "average": average,
        "min": minimum,
        "max": maximum,
        "hot_days_count": len(hot_days),
        "total_days": len(data)
    }

# Run the analysis
results = analyze_data(temperatures)

# Print results
print("Temperature Analysis:")
print(f"Average: {results['average']:.2f}°F")
print(f"Range: {results['min']}°F - {results['max']}°F")
print(f"Hot days: {results['hot_days_count']} out of {results['total_days']}")
```

**Expected output:**
```
Temperature Analysis:
Average: 75.40°F
Range: 68°F - 82°F
Hot days: 5 out of 10
```

---

## Practice Exercises

### Exercise 1: List Operations
```python
# Create a list of your 5 favorite books
# Print the first and last book
# Add a new book
# Loop through and print each with its position
```

### Exercise 2: Function Writing
```python
# Write a function called `celsius_to_fahrenheit`
# It should take a temperature in Celsius
# Return the temperature in Fahrenheit
# Formula: F = (C * 9/5) + 32
```

### Exercise 3: Data Filtering
```python
# Given this list of numbers:
numbers = [1, 5, 12, 8, 23, 45, 3, 17, 9, 31]

# Use list comprehension to create:
# 1. A list of only even numbers
# 2. A list of numbers greater than 15
# 3. A list of all numbers squared
```

---

## Common Mistakes & Solutions

### ❌ Mistake: Index Out of Range
```python
my_list = [1, 2, 3]
print(my_list[3])    # ERROR! Index 3 doesn't exist
```
✅ **Solution:** Remember indices start at 0. Use `len(my_list)` to check size.

### ❌ Mistake: Forgetting Colons
```python
if x > 5    # ERROR! Missing colon
    print(x)
```
✅ **Solution:** Always add `:` after `if`, `for`, `def`, `else`, `elif`.

### ❌ Mistake: Indentation Errors
```python
def my_function():
print("Hello")    # ERROR! Needs indentation
```
✅ **Solution:** Use 4 spaces (or Tab) for indentation inside blocks.

### ❌ Mistake: Modifying a List While Looping
```python
for item in my_list:
    my_list.remove(item)    # Can cause unexpected behavior!
```
✅ **Solution:** Create a new list with list comprehension instead.

---

## Next Steps

✅ You now know Python basics! Continue by:

1. **Practice:** Complete the exercises above
2. **Install packages:** Try `pip install numpy`
3. **Explore libraries:** Look at NumPy documentation
4. **Move forward:** Go to [Git Basics](git_basics.md) or start your first AI guide!

---

## Quick Reference Card

```python
# Variables
x = 5
name = "Alice"

# Lists
my_list = [1, 2, 3]
my_list.append(4)

# Dictionaries
my_dict = {"key": "value"}

# If statements
if x > 5:
    print("Big")
elif x == 5:
    print("Equal")
else:
    print("Small")

# Loops
for i in range(10):
    print(i)

# Functions
def my_func(param):
    return param * 2

# List comprehension
squares = [x**2 for x in range(10)]

# Imports
import numpy as np

# File I/O
with open("file.txt", "r") as f:
    content = f.read()
```

---

**Congratulations!** You've learned the Python essentials needed for AI development. 🎉
