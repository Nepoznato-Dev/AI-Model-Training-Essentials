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
# Python — 일반적인 실수 및 안티 패턴
이 문서는 Python에서 가장 일반적인 실수, 함정 및 안티 패턴을 나열합니다. 각 항목은 잘못된 접근 방식을 보여주고, 실패 이유를 설명하며, 올바른 솔루션을 제공합니다. 이러한 함정을 이해하면 더욱 강력한 Python 코드를 작성하는 데 도움이 됩니다.
---

## 1. 변경 가능한 기본 인수
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

**발생 이유:** 기본 인수는 호출할 때마다가 아니라 함수 정의 시에 한 번 평가됩니다. 변경 가능한 기본값(list, dict, set)은 모든 호출에서 공유됩니다.
---

## 2. 반복하는 동안 목록 수정하기
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

## 3. 클로저의 후기 바인딩
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

## 4.`isinstance()`대신`type()`사용하기
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

## 5. 리소스에 대해 컨텍스트 관리자를 사용하지 않음
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

## 6. 값 비교를 위한`is`연산자
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

## 7. 순환 수입
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

## 8. Python의 범위 규칙을 이해하지 못함(LEGB)
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

## 9. 루프의 문자열 연결
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

## 10. 안티 패턴:`except:`Bare Except 사용
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

## 11. 내부 상태에 대한 가변 참조 반환
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

## 12.`setdefault`또는 `collections.defaultdict`를 사용하지 않음
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

## 13. 조건에서 `==`와 `=`를 혼동함
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

## 14. 발전기 고갈을 이해하지 못함
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

## 15. 안티 패턴: God 객체 / 오버로드된 클래스
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

## 요약
Python의 단순성은 기만적입니다. 변경 가능한 기본값, 지연 바인딩 클로저, 범위 규칙 및 리소스 관리에는 모두 개발자를 가두는 미묘한 동작이 있습니다. 기억해야 할 주요 원칙: 기본값은 한 번 평가되고, `is`는 동일성이 아닌 ID를 확인하고, 항상 리소스에 대해 컨텍스트 관리자를 사용하고, 특정 예외를 포착하고, God 개체보다 구성을 선호합니다. Python 코드를 작성한다는 것은 이러한 함정을 이해하고 언어의 기능(컨텍스트 관리자, 이해, 생성기,`collections`모듈)을 의도한 대로 사용하는 것을 의미합니다.