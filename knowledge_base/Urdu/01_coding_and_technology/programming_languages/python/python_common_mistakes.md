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
# ازگر - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز ازگر میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کی فہرست بناتی ہے۔ ہر اندراج غلط نقطہ نظر کو ظاہر کرتا ہے، یہ بتاتا ہے کہ یہ کیوں ناکام ہوتا ہے، اور صحیح حل فراہم کرتا ہے۔ ان خرابیوں کو سمجھنے سے آپ کو زیادہ مضبوط، Pythonic کوڈ لکھنے میں مدد ملے گی۔
---

## 1. تغیر پذیر ڈیفالٹ دلائل
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

**یہ کیوں ہوتا ہے:** ڈیفالٹ آرگیومینٹس کا اندازہ فنکشن ڈیفینیشن ٹائم پر ایک بار کیا جاتا ہے، ہر کال پر نہیں۔ ایک بدلنے والا ڈیفالٹ (فہرست، ڈیکٹ، سیٹ) تمام درخواستوں میں اشتراک کیا جاتا ہے۔
---

## 2. تکرار کرتے وقت فہرست میں ترمیم کرنا
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

## 3. بندش میں دیر سے بائنڈنگ
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

## 4.`isinstance()`کی بجائے`type()`استعمال کرنا
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

## 5. وسائل کے لیے سیاق و سباق کے مینیجرز کا استعمال نہ کرنا
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

## 6. قیمت کے موازنہ کے لیے`is`آپریٹر
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

## 7. سرکلر درآمدات
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

## 8. ازگر کے دائرہ کار کے قواعد (LEGB) کو نہ سمجھنا
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

## 9. لوپس میں سٹرنگ کنکٹنیشن
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

## 10. اینٹی پیٹرن:`except:`کو استعمال کرنا سوائے
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

## 11. داخلی حالت میں تغیر پذیر حوالہ جات واپس کرنا
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

## 12.`setdefault`یا`collections.defaultdict`استعمال نہیں کرنا
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

## 13. کنفیوزنگ`==`اور`=`شرائط میں
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

## 14. جنریٹر کی تھکن کو نہ سمجھنا
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

## 15. اینٹی پیٹرن: خدا آبجیکٹ / اوورلوڈ کلاسز
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

## خلاصہ
Python کی سادگی دھوکہ دینے والی ہے — بدلنے کے قابل ڈیفالٹس، دیر سے پابند بندش، دائرہ کار کے اصول، اور وسائل کا انتظام سبھی کے لطیف رویے ہوتے ہیں جو ڈویلپرز کو پھنساتے ہیں۔ یاد رکھنے کے اہم اصول: ڈیفالٹس کا ایک بار جائزہ لیا جاتا ہے،`is`شناخت کو چیک کرتا ہے نہ کہ مساوات، وسائل کے لیے ہمیشہ سیاق و سباق کے مینیجرز کا استعمال کریں، مخصوص استثنیٰ کو پکڑیں، اور خدائی اشیاء پر ساخت کو ترجیح دیں۔ Pythonic کوڈ لکھنے کا مطلب ہے کہ ان خرابیوں کو سمجھنا اور زبان کی خصوصیات (سیاق و سباق کے مینیجر، فہم، جنریٹرز،`collections`ماڈیول) کو حسب ارادہ استعمال کرنا ہے۔