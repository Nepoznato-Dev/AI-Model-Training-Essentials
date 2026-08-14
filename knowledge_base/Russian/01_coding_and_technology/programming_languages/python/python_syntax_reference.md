---
# Metadata
title: "Python — Syntax Reference"
description: "Detailed syntax reference for Python covering operators, control flow, functions, data structures, OOP, error handling, modules, and advanced features."
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
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [python, syntax-reference, operators, control-flow, functions, oop, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Python — Справочник по синтаксису
Этот документ предоставляет исчерпывающий структурированный справочник по синтаксису Python. Он дополняет основной справочник по Python, уделяя особое внимание исчерпывающим синтаксическим шаблонам, таблицам операторов и внутренней механике.
---

## Операторы и выражения
### Арифметические операторы
| Оператор | Имя | Пример | Результат | Заметки |
|----------|------|---------|--------|-------|
| `+`| Дополнение | `3 + 2`| `5`| Также объединение строк/списков |
| `-`| Вычитание | `3 - 2`| `1`| Также унарное отрицание |
| `*`| Умножение | `3 * 2`| `6`| Также повторение строки/списка |
| `/`| Истинное разделение | `7 / 2`| `3.5`| Всегда возвращает число с плавающей запятой |
| `//`| Отдел этажей | `7 // 2`| `3`| Округление к отрицательной бесконечности |
| `%`| Модуль | `7 % 2`| `1`| Знак соответствует делителю |
| `**`| Возведение в степень | `2 ** 10`| `1024`| Правоассоциативный |
### Сравнение и логические операторы
| Оператор | Имя | Пример | Заметки |
|----------|------|---------|-------|
| `==`| Равный | `x == y`| Сравнение значений (не тождество) |
| `!=`| Не равно | `x != y`| |
| `<`,`>`,`<=`,`>=`| Заказ | `x >= y`| Цепочка:`a < b < c`|
| `is`| идентичность | `x is y`| Тот же объект в памяти |
| `is not`| Не личность | `x is not None`| Предпочтительнее`!= None`|
| `in`| Членство | `x in collection`| O(1) для наборов/слов, O(n) для списков |
| `and`| Логическое И | `a and b`| Короткое замыкание; возвращает последнее истинное/ложное значение |
| `or`| Логическое ИЛИ | `a or b`| Короткое замыкание; возвращает первое истинное/ложное значение |
| `not`| Логическое НЕ | `not x`| |
### Побитовые операторы
| Оператор | Имя | Пример | Заметки |
|----------|------|---------|-------|
| `&`| И | `5 & 3`| `1`|
| `\|`| ИЛИ | `5 \| 3`| `7`|
| `^`| ИСКЛЮЧАЮЩЕЕ ИЛИ | `5 ^ 3`| `6`|
| `~`| НЕ | `~5`| `-6`(дополнение до двух) |
| `<<`| Левый сдвиг | `5 << 1`| `10`|
| `>>`| Правый сдвиг | `5 >> 1`| `2`|
### Приоритет оператора (от самого высокого к самому низкому)
| Приоритет | Операторы | Ассоциативность |
|------------|-----------|---------------|
| 1 (самый высокий) | `()`| Группировка |
| 2 | `**`| Правильно |
| 3 | `~`,`+x`,`-x`| Унарный |
| 4 | `*`,`/`,`//`,`%`| Левый |
| 5 | `+`,`-`| Левый |
| 6 | `<<`,`>>`| Левый |
| 7 | `&`| Левый |
| 8 | `^`| Левый |
| 9 | `\|`| Левый |
| 10 | `==`,`!=`,`<`,`>`,`<=`,`>=`,`is`,`in`| Цепной |
| 11 | `not`| Правильно |
| 12 | `and`| Левый |
| 13 (самый низкий) | `or`| Левый |
### Назначение и расширенное назначение
```python
x = 10          # Basic assignment
x += 5          # x = x + 5
x -= 3          # x = x - 3
x *= 2          # x = x * 2
x /= 4          # x = x / 4  (float result)
x //= 3         # x = x // 3 (floor division)
x %= 7          # x = x % 7
x **= 2         # x = x ** 2
x &= 0xFF       # Bitwise AND
x |= 0x0F       # Bitwise OR
x ^= 0xFF       # Bitwise XOR
x <<= 2         # Left shift
x >>= 1         # Right shift

# Walrus operator (Python 3.8+) — assign and use in one expression
if (n := len(data)) > 100:
    print(f"Dataset has {n} items — too large")
```

---

## Поток управления
### Условные операторы
```python
# Basic if/elif/else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary expression
status = "pass" if score >= 60 else "fail"

# Structural pattern matching (Python 3.10+)
match command.split():
    case ["quit"]:
        app.quit()
    case ["goto", target]:
        app.navigate(target)
    case ["move", direction, int(steps)]:
        app.move(direction, steps)
    case ["save", filename] if filename.endswith(".json"):
        app.save_json(filename)
    case _:
        print(f"Unknown command: {command}")
```

### Циклы
```python
# For loop with range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

# For loop over collection
for item in ["a", "b", "c"]:
    print(item)

# Enumerate — index + value
for i, item in enumerate(["a", "b", "c"], start=1):
    print(f"{i}: {item}")

# Zip — parallel iteration
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # Skip to next iteration
    if i == 7:
        break       # Exit loop
    print(i)
else:
    # Executes only if loop completes without break
    print("Loop finished normally")

# Nested loop with labeled break (via exception or flag)
found = False
for row in matrix:
    for val in row:
        if val == target:
            found = True
            break
    if found:
        break
```

### Понимания
```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [val for sublist in nested for val in sublist]

# Dict comprehension
word_lengths = {word: len(word) for word in sentences}
inverted = {v: k for k, v in original.items()}

# Set comprehension
unique_lengths = {len(word) for word in words}

# Generator expression (lazy — no list created)
total = sum(x**2 for x in range(1_000_000))
lines = (line.strip() for line in open("file.txt"))
```

---

## Функции и замыкания
### Определение и вызов функции
```python
# Basic function with type hints
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting string."""
    return f"{greeting}, {name}!"

# Positional-only parameters (Python 3.8+)
def power(base, exp, /, mod=None):
    # base and exp can only be positional
    result = base ** exp
    return result % mod if mod else result

power(2, 10)            # OK
power(2, 10, mod=100)   # OK
# power(base=2, exp=10) # TypeError

# Keyword-only parameters
def connect(*, host: str, port: int, timeout: float = 30.0):
    pass

connect(host="localhost", port=8080)

# Variadic arguments
def log(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, val in kwargs.items():
        print(f"{key}={val}")

log("info", "startup", level=3, verbose=True)

# Unpacking arguments
def add(a, b, c):
    return a + b + c

values = [1, 2, 3]
add(*values)                    # Unpack list to positional args
config = {"a": 1, "b": 2, "c": 3}
add(**config)                   # Unpack dict to keyword args
```

### Замыкания и функции высшего порядка
```python
# Closure — inner function captures outer scope
def make_multiplier(factor: int):
    def multiplier(x: int) -> int:
        return x * factor       # 'factor' is captured from enclosing scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15

# Higher-order functions
numbers = [1, 2, 3, 4, 5]

# map — apply function to each element
squared = list(map(lambda x: x**2, numbers))

# filter — keep elements matching predicate
evens = list(filter(lambda x: x % 2 == 0, numbers))

# sorted with key function
words = ["banana", "apple", "cherry"]
by_length = sorted(words, key=len)           # ['apple', 'banana', 'cherry']
by_last_char = sorted(words, key=lambda w: w[-1])

# functools.partial — fix some arguments
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5))   # 25
print(cube(5))     # 125
```

### Декораторы
```python
import functools
import time

# Decorator with arguments
def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.5)
def fetch_data(url: str) -> dict:
    import urllib.request
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

# Class decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
```

### Генераторы и сопрограммы
```python
# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator with send() — coroutine
def accumulator():
    total = 0
    while True:
        value = yield total    # Receive value from caller
        total += value

acc = accumulator()
next(acc)              # Prime the generator → 0
acc.send(10)           # → 10
acc.send(20)           # → 30
acc.send(5)            # → 35

# Async generator (Python 3.6+)
async def stream_lines(path: str):
    with open(path) as f:
        for line in f:
            yield line.strip()
            await asyncio.sleep(0)  # Yield control to event loop

# Async comprehension
results = [line async for line in stream_lines("data.txt")]
```

---

## Структуры данных
### Обзор встроенных коллекций
| Коллекция | Заказал | Изменяемый | Дубликаты | Синтаксис | Поиск |
|------------|---------|---------|------------|--------|--------|
| `list`| Да | Да | Да | `[1, 2, 3]`| О(п) |
| `tuple`| Да | Нет | Да | `(1, 2, 3)`| О(п) |
| `dict`| Да (3.7+) | Да | Ключи: Нет | `{"k": "v"}`| O(1) среднее |
| `set`| Нет | Да | Нет | `{1, 2, 3}`| O(1) среднее |
| `frozenset`| Нет | Нет | Нет | `frozenset({1,2})`| O(1) среднее |
### Списки
```python
# Creation
nums = [1, 2, 3, 4, 5]
from_range = list(range(10))
from_string = list("hello")          # ['h', 'e', 'l', 'l', 'o']

# Access & slicing
first = nums[0]                       # 1
last = nums[-1]                       # 5
middle = nums[1:4]                    # [2, 3, 4]
reversed_slice = nums[::-1]           # [5, 4, 3, 2, 1]
every_other = nums[::2]              # [1, 3, 5]

# Mutation
nums.append(6)                        # Add to end
nums.insert(0, 0)                     # Insert at index
nums.extend([7, 8, 9])               # Append multiple items
nums += [10, 11]                      # Same as extend
removed = nums.pop()                  # Remove and return last
removed = nums.pop(0)                 # Remove and return at index
nums.remove(5)                        # Remove first occurrence of value
nums.sort()                           # In-place sort
nums.sort(key=len, reverse=True)      # Custom sort
nums.reverse()                        # In-place reverse
nums.clear()                          # Remove all items
```

### Словари
```python
# Creation
user = {"name": "Alice", "age": 30}
from_pairs = dict([("a", 1), ("b", 2)])
from_keys = dict.fromkeys(["x", "y", "z"], 0)
merged = {**dict1, **dict2}           # Merge (Python 3.5+)
merged = dict1 | dict2                # Merge operator (Python 3.9+)

# Access
name = user["name"]                   # KeyError if missing
name = user.get("name", "Unknown")   # Default value if missing
name = user.setdefault("name", "N/A")

# Mutation
user["email"] = "alice@example.com"  # Add/update
del user["age"]                       # Delete key
age = user.pop("age", 0)             # Remove and return with default
user.update({"role": "admin"})       # Bulk update

# Iteration
for key in user:                      # Keys
    print(key)
for key, value in user.items():       # Key-value pairs
    print(f"{key}: {value}")
for value in user.values():           # Values only
    print(value)

# Dict views (live, dynamic)
common_keys = dict1.keys() & dict2.keys()    # Set intersection
all_keys = dict1.keys() | dict2.keys()       # Set union
```

### Наборы и замороженные наборы
```python
# Creation
colors = {"red", "green", "blue"}
from_list = set([1, 2, 2, 3, 3])    # {1, 2, 3} — deduplication
empty_set = set()                     # NOT {} (that's an empty dict)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b                         # {1, 2, 3, 4, 5, 6}
intersection = a & b                  # {3, 4}
difference = a - b                    # {1, 2}
symmetric_diff = a ^ b                # {1, 2, 5, 6}

# Subset/superset
{1, 2}.issubset({1, 2, 3})           # True
{1, 2, 3}.issuperset({1, 2})          # True

# Mutation
colors.add("yellow")
colors.update(["orange", "purple"])
colors.remove("red")                  # KeyError if missing
colors.discard("red")                 # No error if missing
popped = colors.pop()                 # Remove arbitrary element
```

### Модуль коллекций
```python
from collections import Counter, defaultdict, deque, namedtuple, ChainMap

# Counter — frequency counting
word_counts = Counter(["a", "b", "a", "c", "a", "b"])
# Counter({'a': 3, 'b': 2, 'c': 1})
word_counts.most_common(2)            # [('a', 3), ('b', 2)]

# defaultdict — auto-initialize missing keys
graph = defaultdict(list)
graph["A"].append("B")               # No KeyError — creates [] first

# deque — double-ended queue, O(1) append/pop from both ends
queue = deque(maxlen=100)             # Bounded deque
queue.append("right")
queue.appendleft("left")
queue.pop()                           # Remove from right
queue.popleft()                       # Remove from left
queue.rotate(3)                       # Rotate elements

# namedtuple — lightweight immutable data class
Point = namedtuple("Point", ["x", "y", "z"])
p = Point(1, 2, 3)
print(p.x, p.y, p.z)                 # 1 2 3
```

---

## Объектно-ориентированное программирование
### Классы и наследование
```python
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{self.__class__.__name__}: area={self.area():.2f}"

# Concrete class with multiple inheritance
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

# Dataclass — auto-generates __init__, __repr__, __eq__
@dataclass(frozen=True, order=True)
class Vector:
    x: float
    y: float
    z: float = 0.0

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

# Property decorator
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (value - 32) * 5/9

# Method resolution order
print(Rectangle.__mro__)
# (Rectangle, Shape, ABC, object)
```

### Магические (Дандер) методы
```python
class Matrix:
    def __init__(self, data: list[list[float]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __repr__(self) -> str:
        return f"Matrix({self.rows}x{self.cols})"

    def __str__(self) -> str:
        return "\n".join(str(row) for row in self.data)

    def __len__(self) -> int:
        return self.rows * self.cols

    def __getitem__(self, key):
        if isinstance(key, tuple):
            r, c = key
            return self.data[r][c]
        return self.data[key]

    def __setitem__(self, key, value):
        r, c = key
        self.data[r][c] = value

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __eq__(self, other) -> bool:
        return self.data == other.data

    def __iter__(self):
        for row in self.data:
            yield row

    def __contains__(self, value) -> bool:
        return any(value in row for row in self.data)
```

---

## Обработка ошибок
### Иерархия исключений
```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError
    ├── AttributeError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── NameError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── TimeoutError
    ├── TypeError
    ├── ValueError
    └── RuntimeError
```

### Шаблоны обработки исключений
```python
# Full try/except/else/finally structure
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Bad value: {e}")
    raise                          # Re-raise after logging
except (TypeError, KeyError) as e:
    logger.warning(f"Type/key issue: {e}")
    result = default_value()
else:
    # Runs only if no exception occurred
    logger.info(f"Success: {result}")
finally:
    # Always runs — cleanup
    cleanup_resources()

# Custom exception hierarchy
class AppError(Exception):
    """Base exception for the application."""

class ConfigError(AppError):
    """Configuration-related errors."""

class AuthError(AppError):
    """Authentication-related errors."""
    def __init__(self, message, user=None):
        super().__init__(message)
        self.user = user

# Context manager for exception handling
class suppress:
    """Suppress specific exceptions (like a targeted try/except)."""
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            return True              # Suppress the exception
        return False                 # Propagate

with suppress(FileNotFoundError):
    os.remove("temp.txt")           # No error if file doesn't exist
```

---

## Модули и пакеты
### Система импорта
```python
# Standard imports
import os
import sys
import json

# Import specific names
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timedelta

# Relative imports (within packages)
from . import utils                  # Same package
from ..config import settings        # Parent package
from ...shared.types import Model    # Grandparent package

# Aliased imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Conditional / lazy imports
try:
    import orjson as json_lib        # Fast JSON library
except ImportError:
    import json as json_lib           # Fallback to stdlib

# Dynamic imports
import importlib
module = importlib.import_module("my_package.utils")
func = getattr(module, "helper_function")
```

### Структура пакета
```
my_package/
├── __init__.py          # Package initialization; defines public API
├── core/
│   ├── __init__.py
│   ├── engine.py
│   └── config.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── validators.py
└── py.typed             # Marker for PEP 561 type checking support
```

```python
# my_package/__init__.py — define public API
from .core.engine import Engine, run
from .utils.helpers import format_output

__all__ = ["Engine", "run", "format_output"]
__version__ = "1.0.0"
```

---

## Расширенные функции
### Метаклассы
```python
# Metaclass — controls class creation
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, url: str):
        self.url = url

# Both variables point to the same instance
db1 = Database("postgres://localhost/mydb")
db2 = Database("postgres://localhost/mydb")
assert db1 is db2

# __init_subclass__ — simpler alternative to metaclasses
class PluginBase:
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase._registry[cls.__name__.lower()] = cls

class CSVPlugin(PluginBase):
    def process(self): ...

# PluginBase._registry now contains {"csvplugin": <class CSVPlugin>}
```

### Дескрипторы и свойства
```python
class Validated:
    """Descriptor for validated numeric fields."""
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.name}", None)

    def __set__(self, obj, value):
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}")
        setattr(obj, f"_{self.name}", value)

class Product:
    price = Validated(min_val=0)
    quantity = Validated(min_val=0, max_val=10000)

    def __init__(self, price: float, quantity: int):
        self.price = price
        self.quantity = quantity
```

### Менеджеры контекста
```python
import contextlib
from typing import Generator

# Class-based context manager
class DatabaseConnection:
    def __init__(self, dsn: str):
        self.dsn = dsn

    def __enter__(self):
        self.conn = connect(self.dsn)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        return False  # Don't suppress exceptions

# Generator-based context manager
@contextlib.contextmanager
def temporary_directory() -> Generator[Path, None, None]:
    tmp = Path(tempfile.mkdtemp())
    try:
        yield tmp
    finally:
        shutil.rmtree(tmp)

# Stacking context managers
@contextlib.contextmanager
def transaction(db):
    with db.cursor() as cursor:
        try:
            yield cursor
            db.commit()
        except Exception:
            db.rollback()
            raise
```

### Тип системы и протоколы
```python
from typing import (
    TypeVar, Generic, Protocol, runtime_checkable,
    TypeAlias, TypeGuard, Literal, Annotated,
    overload, final, Self
)

# Type aliases
Matrix: TypeAlias = list[list[float]]
JSON: TypeAlias = str | int | float | bool | None | list["JSON"] | dict[str, "JSON"]

# Generics
T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

# Protocols (structural subtyping — duck typing with type checking)
@runtime_checkable
class Drawable(Protocol):
    def draw(self, canvas: "Canvas") -> None: ...

# Any class with a draw() method satisfies Drawable — no inheritance needed

# TypeGuard — custom type narrowing
def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

# Overload — different signatures for type checker
@overload
def process(data: str) -> str: ...
@overload
def process(data: bytes) -> bytes: ...
def process(data):
    return data.upper() if isinstance(data, str) else data.decode().upper().encode()

# Literal types
Mode = Literal["r", "w", "a", "r+", "w+"]

# Annotated — attach metadata to types
from typing import Annotated
Temperature = Annotated[float, "celsius", "range: -273.15 to 1000"]
```

---

## Краткое содержание
Этот справочник по синтаксису охватывает полный набор функций Python — от базовых операторов и потока управления до расширенного метапрограммирования, дескрипторов и системы типов. Синтаксис Python намеренно минимален и удобочитаем, но его глубина значительна: сопоставление с образцом, асинхронные генераторы, протоколы и метаклассы предоставляют мощные инструменты для сложных приложений. Язык продолжает развиваться, и в каждом выпуске добавляются функции, улучшающие выразительность при сохранении обратной совместимости.