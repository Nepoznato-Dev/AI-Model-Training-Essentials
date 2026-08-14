<!--
---
# Metadata
title: "Python — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Python that catch even experienced developers, with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
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

-->
# পাইথন — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি পাইথনের সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নের ক্যাটালগ করে। প্রতিটি এন্ট্রি ভুল পদ্ধতি দেখায়, ব্যাখ্যা করে কেন এটি ব্যর্থ হয় এবং সঠিক সমাধান প্রদান করে। এই ত্রুটিগুলি বোঝা আপনাকে আরও শক্তিশালী, পাইথনিক কোড লিখতে সাহায্য করবে।
---

## 1. পরিবর্তনযোগ্য ডিফল্ট আর্গুমেন্ট
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

**এটি কেন হয়:** ডিফল্ট আর্গুমেন্টগুলি একবার ফাংশন সংজ্ঞার সময় মূল্যায়ন করা হয়, প্রতিটি কলে নয়। একটি পরিবর্তনযোগ্য ডিফল্ট (তালিকা, নির্দেশ, সেট) সমস্ত আহ্বান জুড়ে ভাগ করা হয়।
---

## 2. পুনরাবৃত্তি করার সময় একটি তালিকা পরিবর্তন করা
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

## 3. ক্লোজারে দেরী বাঁধাই
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

## 4.`isinstance()`এর পরিবর্তে`type()`ব্যবহার করা
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

## 5. সম্পদের জন্য কনটেক্সট ম্যানেজার ব্যবহার না করা
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

## 6. মূল্য তুলনার জন্য`is`অপারেটর
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

## 7. সার্কুলার আমদানি
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

## 8. পাইথনের স্কোপ রুলস (LEGB) না বোঝা
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

## 9. লুপগুলিতে স্ট্রিং সংযোগ
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

## 10. অ্যান্টি-প্যাটার্ন:`except:`বেয়ার ব্যবহার করা ছাড়া
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

## 11. অভ্যন্তরীণ রাজ্যে পরিবর্তনযোগ্য রেফারেন্স ফিরিয়ে দেওয়া
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

## 12.`setdefault`বা`collections.defaultdict`ব্যবহার করছেন না
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

## 13. শর্তে`==`এবং`=`বিভ্রান্তিকর
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

## 14. জেনারেটরের ক্লান্তি না বোঝা
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

## 15. অ্যান্টি-প্যাটার্ন: ঈশ্বর বস্তু / ওভারলোডেড ক্লাস
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

## সারাংশ
পাইথনের সরলতা প্রতারণামূলক — পরিবর্তনযোগ্য ডিফল্ট, দেরীতে বাঁধাই বন্ধ করা, সুযোগের নিয়ম, এবং সংস্থান ব্যবস্থাপনার সবগুলোরই সূক্ষ্ম আচরণ রয়েছে যা ডেভেলপারদের ফাঁদে ফেলে। মনে রাখার মূল নীতিগুলি: ডিফল্টগুলি একবার মূল্যায়ন করা হয়,`is`সমতা নয় পরিচয় পরীক্ষা করে, সর্বদা সম্পদের জন্য প্রসঙ্গ পরিচালক ব্যবহার করুন, নির্দিষ্ট ব্যতিক্রমগুলি ধরুন এবং ঈশ্বরের বস্তুর উপর রচনার পক্ষে। পাইথনিক কোড লেখার অর্থ হল এই সমস্যাগুলি বোঝা এবং ভাষার বৈশিষ্ট্যগুলি (প্রসঙ্গ পরিচালক, বোধগম্যতা, জেনারেটর,`collections`মডিউল) উদ্দেশ্য অনুসারে ব্যবহার করা।