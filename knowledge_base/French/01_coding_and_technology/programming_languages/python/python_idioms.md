<!--
---
# Metadata
title: "Python — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, Pythonic code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [python, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Python — Modèles idiomatiques et meilleures pratiques
Ce guide couvre les modèles idiomatiques et les meilleures pratiques pour écrire du code Pythonique propre.
---

## Le Zen de Python
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
```

---

## Compréhensions et générateurs de listes
```python
# ❌ Not idiomatic
squares = []
for x in range(10):
    squares.append(x ** 2)

# ✅ Idiomatic: list comprehension
squares = [x ** 2 for x in range(10)]

# ✅ With condition
evens = [x ** 2 for x in range(10) if x % 2 == 0]

# ✅ Nested comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]

# ✅ Generator expression (lazy, memory-efficient)
total = sum(x ** 2 for x in range(1_000_000))

# ✅ Dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}

# ✅ Set comprehension
unique_lengths = {len(word) for word in words}
```

---

## Déballage et échange
```python
# ✅ Tuple unpacking
name, email, age = user_data

# ✅ Swap variables
a, b = b, a

# ✅ Unpacking with *
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

*initial, last = [1, 2, 3, 4, 5]
# initial = [1, 2, 3, 4], last = 5

# ✅ Unpacking in function calls
coords = (3, 4)
distance = math.hypot(*coords)

# ✅ Dict unpacking (merge)
defaults = {"color": "red", "size": "M"}
custom = {"color": "blue", "brand": "Nike"}
merged = {**defaults, **custom}  # Python 3.5+
merged = defaults | custom        # Python 3.9+
```

---

## Gestionnaires de contexte
```python
# ✅ Use context managers for resource management
with open("file.txt") as f:
    content = f.read()

# ✅ Multiple context managers
with open("input.txt") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read().upper())

# ✅ Custom context manager
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter() - start:.3f}s")

with timer("operation"):
    do_expensive_work()
```

---

## Conditions Pythoniques
```python
# ❌ Not idiomatic
if len(items) > 0:
    process(items)

# ✅ Truthy/falsy (empty collections are falsy)
if items:
    process(items)

# ❌ Not idiomatic
if value is not None and value != "":
    process(value)

# ✅ Use truthy
if value:
    process(value)

# ✅ Walrus operator (Python 3.8+)
if (match := re.search(pattern, text)):
    print(match.group())

# ✅ Ternary expression
status = "adult" if age >= 18 else "minor"

# ✅ Chained comparison
if 0 < x < 100:
    process(x)

# ✅ Multiple assignment with ternary
result = a if condition else b
```

---

## Modèles d'itération
```python
# ❌ Not idiomatic
for i in range(len(items)):
    print(i, items[i])

# ✅ enumerate
for i, item in enumerate(items):
    print(i, item)

# ✅ enumerate with start
for i, item in enumerate(items, start=1):
    print(i, item)

# ✅ zip for parallel iteration
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ✅ dict iteration
for key, value in config.items():
    print(f"{key} = {value}")

# ✅ reversed
for item in reversed(items):
    process(item)

# ✅ sorted with key
users_sorted = sorted(users, key=lambda u: u.name)
```

---

## Fonctions et arguments
```python
# ✅ Keyword arguments for clarity
create_user(name="Alice", email="alice@example.com", age=30)

# ✅ *args and **kwargs
def log(*messages, level="INFO", **context):
    for msg in messages:
        print(f"[{level}] {msg} {context}")

# ✅ Type hints (Python 3.10+)
def greet(name: str, times: int = 1) -> str:
    return f"Hello, {name}! " * times

# ✅ Default mutable argument (avoid!)
# ❌
def append_to(element, lst=[]):
    lst.append(element)
    return lst

# ✅
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

---

## Cours et POO
```python
# ✅ dataclass for data containers
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    email: str
    age: int
    roles: list[str] = field(default_factory=list)

# ✅ Named tuple for simple records
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

# ✅ Property for computed attributes
class Circle:
    def __init__(self, radius: float):
        self._radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value
    
    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

# ✅ __slots__ for memory efficiency
class Lightweight:
    __slots__ = ("name", "value")
    def __init__(self, name, value):
        self.name = name
        self.value = value
```

---

## Gestion des erreurs
```python
# ✅ Catch specific exceptions
try:
    result = divide(a, b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError as e:
    print(f"Invalid types: {e}")

# ✅ EAFP (Easier to Ask Forgiveness than Permission)
try:
    value = my_dict[key]
except KeyError:
    value = default_value

# ✅ vs LBYL (Look Before You Leap) — sometimes better
if key in my_dict:
    value = my_dict[key]

# ✅ Custom exceptions
class ValidationError(Exception):
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"{field}: {message}")

# ✅ Context manager for cleanup
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("temp.txt")
```

---

## Modèles fonctionnels
```python
# ✅ map / filter (but comprehensions are often preferred)
doubled = list(map(lambda x: x * 2, numbers))
adults = list(filter(lambda u: u.age >= 18, users))

# ✅ Prefer comprehensions for simple cases
doubled = [x * 2 for x in numbers]
adults = [u for u in users if u.age >= 18]

# ✅ itertools for complex iteration
from itertools import chain, groupby, islice, product

flat = chain(list1, list2, list3)
first_five = islice(infinite_iter, 5)

# ✅ functools
from functools import reduce, partial, lru_cache

total = reduce(lambda a, b: a + b, numbers)

@lru_cache(maxsize=128)
def expensive(n):
    return sum(i * i for i in range(n))
```

---

## Modèles de modules et de packages
```python
# ✅ __init__.py for clean public API
# mypackage/__init__.py
from .core import process, validate
from .utils import helper

__all__ = ["process", "validate", "helper"]

# ✅ Relative imports within package
from . import utils
from ..core import base

# ✅ if __name__ == "__main__"
def main():
    # entry point
    pass

if __name__ == "__main__":
    main()
```

---

## Modèles asynchrones
```python
# ✅ async/await
import asyncio

async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# ✅ Concurrent execution
async def main():
    results = await asyncio.gather(
        fetch_data("https://api.example.com/users"),
        fetch_data("https://api.example.com/posts"),
        fetch_data("https://api.example.com/comments"),
    )

# ✅ Async generator
async def stream_lines(filepath):
    async with aiofiles.open(filepath) as f:
        async for line in f:
            yield line.strip()
```

---

## Résumé
Le code pythonique suit le Zen de Python : lisible, explicite, simple et plat. Les idiomes clés incluent : les compréhensions de liste/dict/ensemble, les gestionnaires de contexte (`with`), la gestion des erreurs EAFP,`enumerate`/`zip`pour l'itération,`dataclass`pour les conteneurs de données, les astuces de type, le déballage et les vérifications de vérité/fausse. La communauté Python valorise la lisibilité et "il devrait y avoir une manière évidente de le faire". Suivez PEP 8 pour le style, utilisez`ruff`pour le peluchage et préférez la bibliothèque standard aux solutions tierces lorsque cela est possible.