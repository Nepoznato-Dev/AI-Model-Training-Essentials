---
# Metadata
title: "Python"
description: "Comprehensive reference for the Python programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [python, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "58 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# পাইথন
পাইথন হল একটি উচ্চ-স্তরের, ব্যাখ্যা করা, সাধারণ-উদ্দেশ্যের প্রোগ্রামিং ভাষা যা Guido van Rossum দ্বারা তৈরি করা হয়েছিল এবং 1991 সালে প্রথম প্রকাশিত হয়েছিল। এটি উল্লেখযোগ্য ইন্ডেন্টেশন এবং একটি পরিষ্কার সিনট্যাক্সের মাধ্যমে কোড পাঠযোগ্যতাকে অগ্রাধিকার দেয় যা সাধারণ ইংরেজির কাছাকাছি পড়ে। পাইথন গতিশীলভাবে টাইপ করা, আবর্জনা-সংগৃহীত, এবং পদ্ধতিগত, অবজেক্ট-ওরিয়েন্টেড এবং কার্যকরী প্রোগ্রামিং সহ একাধিক প্রোগ্রামিং দৃষ্টান্ত সমর্থন করে।
আজ, পাইথন হল AI/ML, ডেটা সায়েন্স, সায়েন্টিফিক কম্পিউটিং, এবং অটোমেশনে প্রভাবশালী ভাষা - যদিও নতুনদের জন্য সেরা ভাষাগুলির মধ্যে একটি। সেই দ্বৈত পরিচয় (প্রথম স্ক্রিপ্টের জন্য যথেষ্ট সহজ, বৃহৎ ভাষার মডেল প্রশিক্ষণের জন্য যথেষ্ট শক্তিশালী) যা এটিকে আলাদা করে।
---

## কেন পাইথন ব্যাপার
- **ডিজাইন দ্বারা পঠনযোগ্যতা**: কোন সেমিকোলন নেই, কোন বন্ধনী নেই — ইন্ডেন্টেশন সুযোগকে সংজ্ঞায়িত করে। কোড pseudocode মত পড়া.
- **ম্যাসিভ ইকোসিস্টেম**: PyPI কার্যত প্রতিটি ডোমেন কভার করে 500,000-এর বেশি প্যাকেজ হোস্ট করে।
- **AI-এর ভাষা**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — সমগ্র AI/ML স্ট্যাকটি পাইথন-প্রথম।
- **আঠালো ভাষা**: একটি C++ ইঞ্জিনকে একটি ওয়েব API এর সাথে একটি ডাটাবেসের সাথে সংযোগ করুন মাত্র কয়েকটি লাইনে।
- **ক্রস-প্ল্যাটফর্ম**: পরিবর্তন ছাড়াই Windows, macOS, Linux, এবং এমবেডেড সিস্টেমে চলে।
- **সম্প্রদায়**: বিশ্বের বৃহত্তম এবং সবচেয়ে সক্রিয় প্রোগ্রামিং সম্প্রদায়।
## বাণিজ্য বন্ধ
পাইথন নিখুঁত নয়। এর সীমাবদ্ধতাগুলি বোঝা আপনাকে কখন অন্য কিছুর জন্য পৌঁছাতে হবে তা নির্ধারণ করতে সহায়তা করে:
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **সম্পাদনার গতি** | CPU- আবদ্ধ কাজগুলির জন্য C-এর চেয়ে 10-100x ধীর গরম লুপের জন্য NumPy/PyTorch (হুডের নিচে C), অথবা Cython/Numba ব্যবহার করুন |
| **GIL (গ্লোবাল ইন্টারপ্রেটার লক)** | CPU-বাউন্ড কাজের জন্য সত্য মাল্টি-থ্রেডেড সমান্তরালতা প্রতিরোধ করে |`multiprocessing`,`asyncio`, বা সেলারির মত টাস্ক কিউ ব্যবহার করুন |
| **মোবাইল ডেভেলপমেন্ট** | iOS/Android অ্যাপের জন্য উপযুক্ত নয় নেটিভের জন্য সুইফট/কোটলিন ব্যবহার করুন, অথবা ক্রস-প্ল্যাটফর্মের জন্য ফ্লাটার/রিঅ্যাক্ট নেটিভ ব্যবহার করুন
| **এমবেডেড সিস্টেম** | মাইক্রোকন্ট্রোলারের জন্য খুব ভারী | MicroPython ব্যবহার করুন (একটি লাইটওয়েট বৈকল্পিক) অথবা C/Rust | এ স্যুইচ করুন
| **মেমরি ব্যবহার** | সংকলিত ভাষার চেয়ে উচ্চ মেমরি পদচিহ্ন | বেশিরভাগ অ্যাপ্লিকেশনের জন্য গ্রহণযোগ্য; বড় ডেটার জন্য জেনারেটর ব্যবহার করুন |
---

## সিনট্যাক্স মৌলিক
### ভেরিয়েবল এবং প্রকার
পাইথন গতিশীল টাইপিং ব্যবহার করে — আপনি পরিবর্তনশীল প্রকারগুলি ঘোষণা করেন না, তবে আপনি স্পষ্টতা এবং টুলিং সমর্থনের জন্য টাইপ ইঙ্গিত যোগ করতে পারেন।
```python
# Basic types — inferred automatically
name = "Alice"          # str
age = 30                # int
score = 9.5             # float
is_active = True        # bool
items = None            # NoneType

# Type hints (optional but recommended for larger projects)
name: str = "Alice"
age: int = 30
scores: list[float] = [9.5, 8.0, 7.5]
config: dict[str, int] = {"timeout": 30, "retries": 3}
```

### নিয়ন্ত্রণ প্রবাহ
```python
# Conditionals
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Loops
for item in items:
    print(item)

for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

while is_active:
    do_something()
    if done:
        is_active = False

# List comprehension — Python's signature idiom
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
```

### ফাংশন
```python
def greet(name: str, times: int = 1) -> str:
    """Return a greeting repeated `times`."""
    return (f"Hello, {name}! " * times).strip()

# *args and **kwargs for flexible arguments
def log(*messages, level="info", **metadata):
    prefix = f"[{level.upper()}]"
    for msg in messages:
        print(f"{prefix} {msg} | {metadata}")

# Lambda (anonymous functions)
square = lambda x: x ** 2
sorted_users = sorted(users, key=lambda u: u["age"])
```

### অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং
```python
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Abstract base class — defines an interface
class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        ...

# Concrete implementation
class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"

# Dataclass — concise data containers (Python 3.7+)
@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5
```

### ত্রুটি হ্যান্ডলিং
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
except (TypeError, ValueError):
    print("Type or value problem")
else:
    print("No errors occurred")
finally:
    print("This always runs")

# Raising custom exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount:.2f} from ${balance:.2f}")
```

---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
###`typing`মডিউল সহ জেনেরিক
পাইথনের`typing`মডিউল পুনর্ব্যবহারযোগ্য, টাইপ-নিরাপদ উপাদান নির্মাণের জন্য জেনেরিক ধরনের সমর্থন প্রদান করে। স্থির বিশ্লেষণের জন্য টাইপ তথ্য সংরক্ষণ করার সময় জেনেরিক্স আপনাকে ফাংশন এবং ক্লাস লিখতে দেয় যা যেকোনো ধরনের সাথে কাজ করে।
```python
from typing import TypeVar, Generic, Protocol, runtime_checkable

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

# Generic class — a type-safe container
class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value

    def map(self, func: callable) -> "Box":
        return Box(func(self.value))

int_box: Box[int] = Box(42)
str_box: Box[str] = Box("hello")

# Generic function with constraints
def first(items: list[T]) -> T | None:
    return items[0] if items else None

# Protocols — structural subtyping (duck typing for type checkers)
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

# Circle is considered a Drawable even without explicit inheritance
def render(obj: Drawable) -> None:
    obj.draw()

render(Circle())  # Works — Circle satisfies the Drawable protocol
```

### ডেকোরেটর এবং মেটাপ্রোগ্রামিং
ডেকোরেটর হল পাইথনের সবচেয়ে শক্তিশালী বৈশিষ্ট্যগুলির মধ্যে একটি — তারা আপনাকে তাদের সোর্স কোড পরিবর্তন না করেই ফাংশন এবং ক্লাসের আচরণ পরিবর্তন বা প্রসারিত করতে দেয়।
```python
import functools
import time
import logging
from typing import Callable, Any

# --- Decorator with arguments (retry logic) ---
def retry(max_attempts: int = 3, delay: float = 1.0):
    """Retry a function up to max_attempts times on failure."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.5)
def fetch_data(url: str) -> dict:
    import requests
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

# --- Class decorator — automatically adds repr ---
def auto_repr(cls):
    """Add a __repr__ method based on instance attributes."""
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    cls.__repr__ = __repr__
    return cls

@auto_repr
class Config:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

print(Config("localhost", 8080))  # Config(host='localhost', port=8080)

# --- Metaclasses — control class creation itself ---
class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists."""
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True — same instance
```

### স্ট্রাকচারাল প্যাটার্ন ম্যাচিং (পাইথন 3.10+)
পাইথনের`match/case`বিবৃতিটি ধ্বংস, গার্ড এবং নেস্টেড প্যাটার্নের সাথে শক্তিশালী প্যাটার্ন ম্যাচিং প্রদান করে।
```python
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

@dataclass
class Triangle:
    base: float
    height: float

# --- Pattern matching with class patterns ---
def area(shape) -> float:
    match shape:
        case Circle(radius=r):
            return 3.14159 * r ** 2
        case Rectangle(width=w, height=h):
            return w * h
        case Triangle(base=b, height=h):
            return 0.5 * b * h
        case _:
            raise ValueError(f"Unknown shape: {shape}")

# --- Matching with guards and OR patterns ---
def classify(value: int) -> str:
    match value:
        case 0:
            return "zero"
        case n if n > 0 and n <= 10:
            return "small positive"
        case n if n > 10:
            return "large positive"
        case -1 | -2 | -3:
            return "small negative"
        case _:
            return "other negative"

# --- Destructuring nested data ---
def process_command(command: str) -> None:
    match command.split():
        case ["quit"]:
            print("Goodbye!")
        case ["go", direction] if direction in ("north", "south", "east", "west"):
            print(f"Moving {direction}")
        case ["go", _]:
            print("Invalid direction")
        case ["take", item]:
            print(f"Picked up {item}")
        case _:
            print("Unknown command")
```

### বন্ধ, উচ্চ-ক্রম ফাংশন, এবং পুনরাবৃত্তিকারী
```python
from functools import partial, reduce
from itertools import islice, chain, count

# --- Closure — captures state from enclosing scope ---
def make_counter(start: int = 0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter(10)
print(counter())  # 11
print(counter())  # 12

# --- Higher-order functions ---
def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x * 2, 3))  # 12

# partial application — freeze some arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(5))   # 25
print(cube(5))     # 125

# reduce — fold a sequence into a single value
nums = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, nums)  # 120

# --- Custom iterator ---
class FibonacciIterator:
    def __init__(self, max_count: int):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

for num in FibonacciIterator(8):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13
```

### অপারেটর ওভারলোডিং
```python
from dataclasses import dataclass
import math

@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector2D":
        return self.__mul__(scalar)  # supports 3.0 * vector

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.x, -self.y)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __bool__(self) -> bool:
        return abs(self) > 1e-10

v1 = Vector2D(3.0, 4.0)
v2 = Vector2D(1.0, 2.0)

print(v1 + v2)       # Vector2D(4.0, 6.0)
print(v1 * 2)        # Vector2D(6.0, 8.0)
print(3 * v2)        # Vector2D(3.0, 6.0)
print(abs(v1))       # 5.0
```

### কাস্টম ব্যতিক্রম শ্রেণিবিন্যাস
```python
class AppError(Exception):
    """Base exception for the application."""
    def __init__(self, message: str, code: str = "UNKNOWN"):
        self.code = code
        super().__init__(message)

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"Validation failed for '{field}': {message}", code="VALIDATION")

class NotFoundError(AppError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource: str, identifier: str):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} not found: {identifier}", code="NOT_FOUND")

class AuthenticationError(AppError):
    """Raised when authentication fails."""
    pass

class AuthorizationError(AppError):
    """Raised when a user lacks permission."""
    pass

# Usage with structured error handling
def get_user(user_id: str) -> dict:
    if not user_id:
        raise ValidationError("user_id", "cannot be empty")
    raise NotFoundError("User", user_id)

try:
    user = get_user("")
except ValidationError as e:
    print(f"Bad input: {e.field}")
except NotFoundError as e:
    print(f"Missing: {e.resource} #{e.identifier}")
except AppError as e:
    print(f"Application error [{e.code}]: {e}")
```

---

## গভীরতার মূল বৈশিষ্ট্য
### স্ট্যান্ডার্ড লাইব্রেরি ("ব্যাটারি অন্তর্ভুক্ত")
একটি বিস্তৃত স্ট্যান্ডার্ড লাইব্রেরি সহ পাইথন জাহাজ। সর্বাধিক ব্যবহৃত কিছু মডিউল:
| মডিউল | উদ্দেশ্য | উদাহরণ ব্যবহার |
|---------|---------|---------------|
| `os`/`pathlib`| ফাইল সিস্টেম অপারেশন | `Path("data/output.csv").exists()`|
| `json`| JSON এনকোডিং/ডিকোডিং | `json.loads(response_text)`|
| `datetime`| তারিখ এবং সময় পরিচালনা | `datetime.now(timezone.utc)`|
| `collections`| বিশেষ পাত্রে | `Counter(words)`,`defaultdict(list)`|
| `itertools`| ইটারেটর বিল্ডিং ব্লক | `combinations(items, 2)`|
| `functools`| ফাংশন টুল | `lru_cache`,`partial`,`reduce`|
| `re`| নিয়মিত অভিব্যক্তি | `re.findall(r"\d+", text)`|
| `subprocess`| বাহ্যিক কমান্ড চালান | `subprocess.run(["ls", "-la"])`|
| `logging`| আবেদন লগিং | `logging.basicConfig(level=logging.INFO)`|
| `typing`| টাইপ ইঙ্গিত সমর্থন | `Optional[str]`,`Union[int, float]`|
| `http.server`| সহজ HTTP সার্ভার | `python -m http.server 8000`|
| `threading`/`asyncio`| সঙ্গতি | ওয়েব স্ক্র্যাপারের জন্য Async I/O |
### ভার্চুয়াল পরিবেশ এবং প্যাকেজ ব্যবস্থাপনা
প্রতিটি পাইথন প্রকল্পের নির্ভরতা বিচ্ছিন্ন করার জন্য একটি ভার্চুয়াল পরিবেশ ব্যবহার করা উচিত:
```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install packages
pip install requests flask numpy

# Freeze dependencies
pip freeze > requirements.txt

# Reproduce the environment
pip install -r requirements.txt
```

আধুনিক পাইথন প্রকল্পগুলি`uv`,`poetry`, বা`hatch`এর মতো সরঞ্জামগুলির সাথে`pyproject.toml`ক্রমবর্ধমানভাবে ব্যবহার করে নির্ভরতা ব্যবস্থাপনার জন্য, পুরানো`setup.py`/`requirements.txt`পদ্ধতির পরিবর্তে।
### অ্যাসিঙ্ক প্রোগ্রামিং
পাইথনের`asyncio`থ্রেড ছাড়াই সমসাময়িক I/O সক্ষম করে — ওয়েব স্ক্র্যাপার, চ্যাট সার্ভার এবং API ক্লায়েন্টদের জন্য অপরিহার্য:
```python
import asyncio
import aiohttp

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://httpbin.org/get"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, html in zip(urls, results):
        print(f"{url}: {len(html)} bytes")

asyncio.run(main())
```

---

## সামঞ্জস্য এবং সমান্তরালতা
পাইথন বেশ কয়েকটি সমসাময়িক মডেল অফার করে, প্রতিটি ভিন্ন কাজের চাপের জন্য উপযুক্ত। CPython এ GIL (গ্লোবাল ইন্টারপ্রেটার লক) থ্রেডের সাথে সত্যিকারের CPU সমান্তরালতাকে বাধা দেয়, তাই সঠিক মডেলটি নির্ভর করে আপনার কাজের চাপ I/O-বাউন্ড নাকি CPU-বাউন্ড।
### থ্রেডিং (I/O-বাউন্ড টাস্ক)
```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def download_file(url: str, output: str) -> None:
    print(f"Downloading {url}...")
    time.sleep(2)  # Simulate network I/O
    print(f"Saved to {output}")

urls = [
    ("https://example.com/file1.zip", "file1.zip"),
    ("https://example.com/file2.zip", "file2.zip"),
    ("https://example.com/file3.zip", "file3.zip"),
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_file, url, out) for url, out in urls]
    for future in futures:
        future.result()  # Wait for completion and raise exceptions
```

### মাল্টিপ্রসেসিং (সিপিইউ-বাউন্ড টাস্ক)
```python
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import math

def is_prime(n: int) -> bool:
    """CPU-intensive computation."""
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1000000007, 1000000009, 1000000021, 999999999989]

with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
    results = list(executor.map(is_prime, numbers))

for num, prime in zip(numbers, results):
    print(f"{num}: {'prime' if prime else 'not prime'}")
```

### Asyncio অভ্যন্তরীণ
```python
import asyncio

async def producer(queue: asyncio.Queue, name: str):
    for i in range(5):
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:  # Sentinel value to stop
            break
        print(f"Consumed: {item}")
        await asyncio.sleep(0.15)
        queue.task_done()

async def main():
    queue: asyncio.Queue = asyncio.Queue(maxsize=10)
    prod_task = asyncio.create_task(producer(queue, "worker"))
    cons_task = asyncio.create_task(consumer(queue))
    await prod_task
    await queue.put(None)  # Signal consumer to stop
    await cons_task

asyncio.run(main())

# --- Synchronisation primitives ---
async def worker(lock: asyncio.Lock, name: str):
    async with lock:
        print(f"{name} acquired lock")
        await asyncio.sleep(1)
        print(f"{name} releasing lock")

async def main_locks():
    lock = asyncio.Lock()
    await asyncio.gather(worker(lock, "A"), worker(lock, "B"))
```

---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রজেক্ট ডাইরেক্টরি স্ট্রাকচার
```
my-python-project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── services.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   └── test_services.py
├── docs/
│   └── index.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── .python-version
├── .env.example
├── README.md
├── LICENSE
└── .gitignore
```

### বিল্ড কনফিগারেশন — `pyproject.toml`
```toml
[project]
name = "my-package"
version = "1.0.0"
description = "A sample Python project"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Alice Developer", email = "alice@example.com"},
]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0",
    "structlog>=23.1.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4",
    "pytest-cov>=4.1",
    "ruff>=0.1.0",
    "mypy>=1.5",
]

[project.scripts]
my-tool = "my_package.main:cli_entry"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP", "B", "A", "SIM"]

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov=my_package --cov-report=term-missing"
```

### আধুনিক সরঞ্জাম সহ নির্ভরশীলতা ব্যবস্থাপনা
```bash
# Using uv (fastest — Rust-based)
uv init my-project
uv add requests pydantic
uv add --dev pytest ruff mypy
uv lock
uv sync

# Using Poetry
poetry init
poetry add requests pydantic
poetry add --group dev pytest ruff mypy
poetry lock
poetry install
```

### লিন্টিং এবং কোড কোয়ালিটি
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD পাইপলাইন — গিটহাব অ্যাকশন
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Lint
        run: |
          uv run ruff check .
          uv run mypy src/

      - name: Test
        run: uv run pytest --cov=my_package --cov-report=xml

      - name: Upload coverage
        if: matrix.python-version == '3.12'
        uses: codecov/codecov-action@v4
        with:
          file: coverage.xml
```

---

## পরীক্ষা
### টেস্টিং ফ্রেমওয়ার্ক এবং সেটআপ
পাইথনের টেস্টিং ইকোসিস্টেম`pytest`এর চারপাশে কেন্দ্র করে, পাইথন পরীক্ষার জন্য প্রকৃত মান।
```bash
# Install testing tools
pip install pytest pytest-cov pytest-mock pytest-asyncio

# Run tests
pytest                          # Run all tests
pytest tests/test_models.py     # Run specific file
pytest -k "test_create"         # Run tests matching pattern
pytest -v                       # Verbose output
pytest --cov=my_package         # With coverage report
pytest -x                       # Stop on first failure
```

### পাইটেস্ট সহ ইউনিট পরীক্ষা
```python
# tests/test_models.py
import pytest
from my_package.models import User, UserService

class TestUser:
    def test_create_user(self):
        user = User(name="Alice", email="alice@example.com", age=30)
        assert user.name == "Alice"
        assert user.email == "alice@example.com"

    def test_user_validation(self):
        with pytest.raises(ValueError, match="email must contain @"):
            User(name="Bob", email="invalid", age=25)

    @pytest.mark.parametrize("age,expected", [
        (17, "minor"),
        (18, "adult"),
        (65, "adult"),
        (66, "senior"),
    ])
    def test_age_category(self, age, expected):
        user = User(name="Test", email="test@test.com", age=age)
        assert user.age_category == expected

class TestUserService:
    def test_find_user(self, mocker):
        mock_repo = mocker.Mock()
        mock_repo.find_by_id.return_value = User("Alice", "a@b.com", 30)

        service = UserService(mock_repo)
        user = service.find_by_id(1)

        assert user.name == "Alice"
        mock_repo.find_by_id.assert_called_once_with(1)

    def test_user_not_found(self, mocker):
        mock_repo = mocker.Mock()
        mock_repo.find_by_id.return_value = None
        service = UserService(mock_repo)

        with pytest.raises(LookupError):
            service.find_by_id(999)
```

### অ্যাসিঙ্ক টেস্ট এবং ইন্টিগ্রেশন টেস্ট
```python
# tests/test_async_services.py
import pytest
import asyncio
from my_package.services import AsyncDataFetcher

@pytest.mark.asyncio
async def test_fetch_data():
    fetcher = AsyncDataFetcher()
    result = await fetcher.fetch("https://httpbin.org/get")
    assert "url" in result

@pytest.mark.asyncio
async def test_concurrent_fetches():
    fetcher = AsyncDataFetcher()
    urls = ["https://httpbin.org/get"] * 5
    results = await asyncio.gather(*[fetcher.fetch(u) for u in urls])
    assert len(results) == 5

# tests/conftest.py — shared fixtures
import pytest
import json

@pytest.fixture
def sample_data_file(tmp_path):
    """Create a temporary JSON file with test data."""
    data = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
    filepath = tmp_path / "data.json"
    filepath.write_text(json.dumps(data))
    return filepath

@pytest.fixture
def mock_db():
    """Provide an in-memory database for testing."""
    return {"users": {1: {"name": "Alice"}, 2: {"name": "Bob"}}}
```

---

## ইন্টারঅপারেবিলিটি
### ctypes সহ C/C++ কল করা হচ্ছে
```python
import ctypes

# Load a shared library
lib = ctypes.CDLL("./mathlib.so")  # Linux/macOS
# lib = ctypes.CDLL("./mathlib.dll")  # Windows

# Define argument and return types
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

result = lib.add(3, 5)  # Calls C function: int add(int a, int b)
print(result)  # 8
```

### আরও জটিল C ইন্টারপের জন্য cffi ব্যবহার করা
```python
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    typedef struct {
        double x;
        double y;
    } Point;
    double distance(Point* a, Point* b);
""")

C = ffi.dlopen("./geometry.so")

p1 = ffi.new("Point*", {"x": 0.0, "y": 0.0})
p2 = ffi.new("Point*", {"x": 3.0, "y": 4.0})
dist = C.distance(p1, p2)
print(dist)  # 5.0
```

### সাইথন — সি পারফরম্যান্স সহ পাইথন
```python
# fibonacci_cython.pyx
def fibonacci_cython(int n):
    cdef int i
    cdef long long a = 0, b = 1
    for i in range(n):
        a, b = b, a + b
    return a

# Compile with: cythonize -i fibonacci_cython.pyx
```

### Pybind11 — C++ এক্সটেনশন
```python
# Binding C++ code to Python with pybind11
# main.cpp
# #include <pybind11/pybind11.h>
# #include <pybind11/stl.h>
#
# std::vector<int> filter_even(std::vector<int> nums) {
#     std::vector<int> result;
#     for (int n : nums) {
#         if (n % 2 == 0) result.push_back(n);
#     }
#     return result;
# }
#
# PYBIND11_MODULE(mymodule, m) {
#     m.def("filter_even", &filter_even, "Filter even numbers");
# }

# After compiling, use from Python:
# import mymodule
# mymodule.filter_even([1, 2, 3, 4, 5, 6])  # [2, 4, 6]
```

---

## ডিজাইন প্যাটার্ন
### সিঙ্গেলটন
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Pythonic alternative — use a module (modules are singletons by nature)
# config.py
DATABASE_URL = "postgresql://localhost/mydb"
DEBUG = True
```

### কারখানার প্যাটার্ন
```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        ...

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

class SlackNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Slack: {message}")

class NotificationFactory:
    _registry = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "slack": SlackNotification,
    }

    @classmethod
    def create(cls, channel: str) -> Notification:
        notifier_class = cls._registry.get(channel)
        if notifier_class is None:
            raise ValueError(f"Unknown channel: {channel}")
        return notifier_class()

notifier = NotificationFactory.create("email")
notifier.send("Server is down!")
```

### পর্যবেক্ষক প্যাটার্ন
```python
from typing import Protocol

class Observer(Protocol):
    def update(self, event: str, data: dict) -> None:
        ...

class EventBus:
    def __init__(self):
        self._subscribers: dict[str, list] = {}

    def subscribe(self, event: str, observer: Observer) -> None:
        self._subscribers.setdefault(event, []).append(observer)

    def publish(self, event: str, data: dict | None = None) -> None:
        for observer in self._subscribers.get(event, []):
            observer.update(event, data or {})

class Logger:
    def update(self, event: str, data: dict) -> None:
        print(f"[LOG] {event}: {data}")

bus = EventBus()
bus.subscribe("user.login", Logger())
bus.publish("user.login", {"user_id": 42})
```

### কনটেক্সট ম্যানেজার প্যাটার্ন
```python
import sqlite3
from contextlib import contextmanager

class DatabaseConnection:
    """Context manager for database connections."""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        return False

# Usage
with DatabaseConnection("app.db") as conn:
    conn.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

# Generator-based context manager
@contextmanager
def temporary_directory():
    import tempfile, shutil
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)
```

### কৌশল প্যাটার্ন
```python
from typing import Protocol

class CompressionStrategy(Protocol):
    def compress(self, data: bytes) -> bytes:
        ...

class GzipCompression:
    def compress(self, data: bytes) -> bytes:
        import gzip
        return gzip.compress(data)

class Bzip2Compression:
    def compress(self, data: bytes) -> bytes:
        import bz2
        return bz2.compress(data)

class FileExporter:
    def __init__(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def export(self, filepath: str, data: bytes) -> None:
        compressed = self._strategy.compress(data)
        with open(filepath, "wb") as f:
            f.write(compressed)

# Swap strategies at runtime
exporter = FileExporter(GzipCompression())
exporter.export("data.gz", b"some large dataset...")
```

---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
```bash
# cProfile — built-in CPU profiler
python -m cProfile -s cumulative my_script.py

# Line-by-line profiling with line_profiler
pip install line_profiler
# Add @profile decorator to functions, then:
kernprof -l -v my_script.py

# Memory profiling with memory_profiler
pip install memory_profiler
python -m memory_profiler my_script.py

# Heap analysis with objgraph
pip install objgraph
import objgraph
objgraph.show_most_common_types(limit=20)
```

### অপ্টিমাইজেশন কৌশল
```python
# 1. Use generators instead of lists for large sequences
# BAD — loads everything into memory
data = [x ** 2 for x in range(10_000_000)]

# GOOD — lazy evaluation, constant memory
data = (x ** 2 for x in range(10_000_000))

# 2. Use collections.deque for fast queue operations
from collections import deque
queue = deque(maxlen=1000)  # O(1) append/pop from both ends

# 3. Use sets for membership testing
# BAD — O(n) lookup
valid_names = ["alice", "bob", "charlie"]
if name in valid_names:  # Slow for large lists

# GOOD — O(1) lookup
valid_names = {"alice", "bob", "charlie"}
if name in valid_names:  # Fast

# 4. Use functools.lru_cache for memoisation
from functools import lru_cache

@lru_cache(maxsize=1024)
def expensive_computation(n: int) -> int:
    return sum(i * i for i in range(n))

# 5. Use NumPy for numerical operations
import numpy as np
arr = np.arange(1_000_000)
result = arr * 2 + 1  # Vectorised — 100x faster than pure Python loop
```

### বেঞ্চমার্কিং
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## স্থাপনা
### প্যাকেজিং এবং বিতরণ
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### ডকারফাইল
```dockerfile
FROM python:3.12-slim AS base

WORKDIR /app

# Install dependencies first (leverage Docker cache)
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-dev

# Copy application code
COPY src/ src/

# Run the application
CMD ["uv", "run", "python", "-m", "my_package.main"]
```

### প্ল্যাটফর্ম-নির্দিষ্ট স্থাপনা
```bash
# AWS Lambda — use a container image
docker build -t my-lambda-function .
docker tag my-lambda-function 123456789.dkr.ecr.us-east-1.amazonaws.com/my-lambda-function
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/my-lambda-function

# Google Cloud Run
gcloud run deploy my-service --source . --region us-central1

# Heroku
git push heroku main

# Railway / Render / Fly.io
fly deploy
```

---

## ইকোসিস্টেম
পাইথনের শক্তি কেবল ভাষা নয় - এটি এটির চারপাশে নির্মিত ইকোসিস্টেম।
### এআই এবং মেশিন লার্নিং
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| পাইটর্চ | গভীর শিক্ষা (গবেষণা ও উৎপাদন) |
| টেনসরফ্লো / কেরাস | গভীর শিক্ষা (উৎপাদন-কেন্দ্রিক) |
| scikit-learn | ক্লাসিক্যাল ML (রিগ্রেশন, ক্লাস্টারিং, শ্রেণীবিভাগ) |
| আলিঙ্গন মুখ ট্রান্সফরমার | প্রাক-প্রশিক্ষিত NLP/ভিশন মডেল |
| LangChain / LlamaIndex | এলএলএম সহ অ্যাপ্লিকেশন তৈরি করা |
| NumPy | সংখ্যাসূচক কম্পিউটিং (অ্যারে, রৈখিক বীজগণিত) |
| পান্ডা | ডেটা ম্যানিপুলেশন এবং বিশ্লেষণ |
| Matplotlib/Seaborn/Plotly | ডেটা ভিজ্যুয়ালাইজেশন |
### ওয়েব ডেভেলপমেন্ট
| ফ্রেমওয়ার্ক | শৈলী | জন্য সেরা |
|------------|-------|----------|
| জ্যাঙ্গো | ফুল-স্ট্যাক, "ব্যাটারি অন্তর্ভুক্ত" | অ্যাডমিন প্যানেল, ORM, প্রমাণ সহ জটিল ওয়েব অ্যাপস
| ফাস্টএপিআই | আধুনিক, অ্যাসিঙ্ক, টাইপ-চালিত | API এবং মাইক্রোসার্ভিস (বর্তমানে দ্রুত বর্ধনশীল) |
| ফ্লাস্ক | ন্যূনতম, নমনীয় | ছোট অ্যাপস এবং প্রোটোটাইপ |
| স্ট্রিমলিট | ডেটা-অ্যাপ ফোকাসড | বিশুদ্ধ পাইথনে ড্যাশবোর্ড এবং ডেটা ডেমো |
### অটোমেশন এবং স্ক্রিপ্টিং
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| `subprocess`/`os`| সিস্টেম প্রশাসন |
| `requests`/`httpx`| HTTP ক্লায়েন্ট |
| `BeautifulSoup`/`Scrapy`| ওয়েব স্ক্র্যাপিং |
| `Selenium`/`Playwright`| ব্রাউজার অটোমেশন |
| `Celery`| বিতরণ করা টাস্ক সারি |
| `Airflow`| ওয়ার্কফ্লো অর্কেস্ট্রেশন |
### বৈজ্ঞানিক কম্পিউটিং
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| NumPy | অ্যারে অপারেশন এবং রৈখিক বীজগণিত |
| SciPy | বৈজ্ঞানিক অ্যালগরিদম (অপ্টিমাইজেশন, সিগন্যাল প্রসেসিং) |
| SymPy | প্রতীকী গণিত |
| জুপিটার নোটবুক | ইন্টারেক্টিভ কম্পিউটিং পরিবেশ |
| JAX | উচ্চ-কর্মক্ষমতা সংখ্যাসূচক কম্পিউটিং (GPU-ত্বরিত) |
---

## পাইথন কখন ব্যবহার করবেন
| দৃশ্যকল্প | কেন পাইথন | ভাল বিকল্প |
|------------|------------|---------|
| AI/ML/ডেটা সায়েন্স | ইকোসিস্টেম অতুলনীয় | — |
| অটোমেশন এবং স্ক্রিপ্টিং | লিখতে এবং ডিবাগ করার জন্য দ্রুততম | সাধারণ সিসাডমিন কাজের জন্য শেল/পাওয়ারশেল
| ওয়েব ব্যাকএন্ড (APIs) | ফাস্টএপিআই চমৎকার | খুব উচ্চ-থ্রুপুট পরিষেবার জন্য যান বা জাভা |
| প্রোটোটাইপিং | ধারণা থেকে কার্যকারী কোডে দ্রুততম পথ | — |
| শিক্ষা | সবচেয়ে শিক্ষানবিস-বান্ধব ভাষা | — |
| ডেস্কটপ অ্যাপ্লিকেশন | সম্ভাব্য কিন্তু অস্বাভাবিক | C# (উইন্ডোজ), সুইফট (macOS) |
| কর্মক্ষমতা-সমালোচনামূলক সিস্টেম | এড়িয়ে চলুন — খুব ধীর | C, C++, মরিচা |
| মোবাইল অ্যাপস | সঠিক টুল নয় | সুইফট (iOS), Kotlin (Android) |
| এমবেডেড সিস্টেম | খুব সম্পদ-ভারী | সি, রাস্ট বা মাইক্রোপাইথন সাধারণ ক্ষেত্রে |
---

## পাইথন সংস্করণ
ভাষা বিকশিত হতে থাকে। মূল সাম্প্রতিক সংযোজন:
| সংস্করণ | বছর | উল্লেখযোগ্য বৈশিষ্ট্য |
|---------|------|-----------------|
| 3.10 | 2021 | স্ট্রাকচারাল প্যাটার্ন ম্যাচিং (`match/case`), আরও ভাল ত্রুটি বার্তা |
| 3.11 | 2022 | 10-60% দ্রুত সম্পাদন, উন্নত ট্রেসব্যাক |
| 3.12 | 2023 | আরো নমনীয় f-স্ট্রিং,`type`স্টেটমেন্ট, কর্মক্ষমতা লাভ |
| 3.13 | 2024 | পরীক্ষামূলক ফ্রি-থ্রেডেড মোড (কোনও জিআইএল নেই), উন্নত REPL |
| 3.14 | 2025 | আরও নো-জিআইএল উন্নতি, টাইপ সিস্টেম বর্ধন |
Python 2 1 জানুয়ারী, 2020-এ শেষ-জীবনে পৌঁছেছে। সমস্ত নতুন প্রকল্পে Python 3.10 বা তার পরে ব্যবহার করা উচিত।
---

## দ্রুত রেফারেন্স: সাধারণ ইডিয়ম
```python
# Unpacking
first, *rest = [1, 2, 3, 4, 5]     # first=1, rest=[2,3,4,5]
a, b = b, a                         # swap variables

# Ternary expression
status = "adult" if age >= 18 else "minor"

# Walrus operator (Python 3.8+)
if (n := len(data)) > 10:
    print(f"Too many items: {n}")

# Context manager (resource cleanup)
with open("file.txt") as f:
    content = f.read()

# f-string formatting
print(f"Name: {name:>10} | Score: {score:.2f}")

# Generators for memory efficiency
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Decorators
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time; time.sleep(1)
```

---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: তালিকা এবং টিপলের মধ্যে পার্থক্য কী এবং আমার প্রতিটি কখন ব্যবহার করা উচিত?
**A:** তালিকাগুলি পরিবর্তনযোগ্য ( `[]`), টিপলগুলি অপরিবর্তনীয় ( `()`)। আপনি যখন উপাদান যোগ, অপসারণ বা পরিবর্তন করতে চান তখন তালিকা ব্যবহার করুন। ভিন্নধর্মী ডেটা, অভিধান কী, ফাংশন রিটার্ন মান, বা যখন আপনি "এটি পরিবর্তন করা উচিত নয়" সংকেত দিতে চান তার নির্দিষ্ট সংগ্রহের জন্য টিপল ব্যবহার করুন। Tuples সামান্য বেশি মেমরি-দক্ষ এবং সেট/ডিক্ট কী হিসাবে ব্যবহার করা যেতে পারে; তালিকা করতে পারে না।
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### প্রশ্ন 2: গ্লোবাল ইন্টারপ্রেটার লক (GIL) কীভাবে আমার কোডকে প্রভাবিত করে এবং এটি সম্পর্কে আমার কী করা উচিত?
**A:** GIL একাধিক থ্রেডকে একই সাথে Python বাইটকোড কার্যকর করতে বাধা দেয়, যার ফলে থ্রেডিং সিপিইউ-বাউন্ড কাজের জন্য অকার্যকর হয়। I/O- আবদ্ধ কাজগুলির জন্য (নেটওয়ার্ক অনুরোধ, ফাইল I/O),`threading`বা`asyncio`ভাল কাজ করে কারণ GIL I/O এর সময় মুক্তি পায়। সিপিইউ-বাউন্ড কাজগুলির জন্য,`multiprocessing`(আলাদা প্রসেস, প্রতিটির নিজস্ব GIL সহ) ব্যবহার করুন অথবা C এক্সটেনশনগুলিতে অফলোড করুন (NumPy, Cython, Numba) যা GIL কে অভ্যন্তরীণভাবে প্রকাশ করে।
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### প্রশ্ন 3: আমার কি সব জায়গায় টাইপ ইঙ্গিত ব্যবহার করা উচিত? ব্যবহারিক ট্রেড-অফ কি?
**A:** টাইপ ইঙ্গিত (`def greet(name: str) -> str:`) ঐচ্ছিক এবং রানটাইমে প্রয়োগ করা হয় না। তারা IDE স্বয়ংসম্পূর্ণতা উন্নত করে, স্ট্যাটিক বিশ্লেষণ টুল (mypy) এবং নথির অভিপ্রায়ের মাধ্যমে বাগ ধরতে পারে। ট্রেড-অফ হল অতিরিক্ত শব্দচয়ন এবং উন্নত ধরনের (`Union` ,`Generic`, `Protocol`) এর জন্য একটি শেখার বক্রতা। সুপারিশ: ~500 লাইনের বেশি যেকোনো প্রকল্পে ফাংশন স্বাক্ষরের জন্য টাইপ ইঙ্গিত ব্যবহার করুন; সংক্ষিপ্ত স্ক্রিপ্টে তাদের ব্যবহার করুন। ধীরে ধীরে প্রয়োগের জন্য CI তে mypy সক্ষম করুন।
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### প্রশ্ন 4: পাইথনে ব্যতিক্রমগুলি পরিচালনা করার জন্য সেরা অনুশীলনগুলি কী কী?
**A:** খালি`except:`(যা`SystemExit`এবং`KeyboardInterrupt`কেও ধরে) এর পরিবর্তে নির্দিষ্ট ব্যতিক্রমগুলি ধরুন। হ্যাপি-পাথ লজিককে ত্রুটি হ্যান্ডলিং থেকে আলাদা করতে`try/except/else/finally`ব্যবহার করুন। লাইব্রেরির জন্য কাস্টম ব্যতিক্রম শ্রেণিবিন্যাস সংজ্ঞায়িত করুন। পারফরম্যান্স-সংবেদনশীল কোডে নিয়ন্ত্রণ প্রবাহের জন্য কখনই ব্যতিক্রমগুলি ব্যবহার করবেন না — সেগুলি ধীর। সম্পূর্ণ ট্রেসব্যাক ক্যাপচার করতে`logging.exception()`দিয়ে ব্যতিক্রম লগ করুন৷
```python
import logging

class ConfigError(Exception):
    """Raised when configuration is invalid."""

def load_config(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise ConfigError(f"Config file not found: {path}")
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in {path}: {e}") from e
```

### প্রশ্ন 5: জেনারেটর কিভাবে মেমরি সংরক্ষণ করে, এবং কখন আমি সেগুলোকে তালিকায় ব্যবহার করব?
**A:** জেনারেটরগুলি মেমরিতে একটি সম্পূর্ণ তালিকা তৈরি করার পরিবর্তে অলসভাবে মান তৈরি করে — এক সময়ে, চাহিদা অনুযায়ী। বড় ডেটাসেটের জন্য (লক্ষ লক্ষ সারি, অসীম সিকোয়েন্স, স্ট্রিমিং ডেটা), জেনারেটরগুলি আকার নির্বিশেষে ধ্রুবক মেমরি ব্যবহার করে। আপনি একবার পুনরাবৃত্তি করার সময় জেনারেটর ব্যবহার করুন এবং ইন্ডেক্সিং বা`len()`এর প্রয়োজন নেই। আপনার এলোমেলো অ্যাক্সেস, একাধিক পুনরাবৃত্তি বা সংগ্রহ ছোট হলে তালিকা ব্যবহার করুন।
```python
# This reads the entire file into memory
lines = open("huge.csv").readlines()  # BAD for large files

# This reads one line at a time — constant memory
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

# Generator expression — like a list comprehension but lazy
total = sum(x * x for x in range(10_000_000))  # No intermediate list created
```

---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: র‌্যাঙ্কিং সহ একটি ওয়ার্ড ফ্রিকোয়েন্সি কাউন্টার তৈরি করুন
**সমস্যা বিবৃতি:** একটি বড় টেক্সট ফাইল দেওয়া হয়েছে, প্রতিটি শব্দের ফ্রিকোয়েন্সি গণনা করুন, তাদের ফ্রিকোয়েন্সি (অবরোহণ) অনুসারে র‌্যাঙ্ক করুন এবং শীর্ষ N ফলাফলগুলি দিন৷ কেস সংবেদনশীলতা, বিরাম চিহ্ন পরিচালনা করুন এবং মেমরিতে ফিট করার জন্য খুব বড় ফাইলগুলিকে দক্ষতার সাথে প্রক্রিয়া করুন।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) পাঠ্য পড়া, (2) শব্দে বিভক্ত করা, (3) কেস স্বাভাবিক করা, (4) স্ট্রিপ বিরাম চিহ্ন, (5) ঘটনাগুলি গণনা করা, (6) অবরোহ গণনা অনুসারে সাজানো, (7) শীর্ষে ফিরে আসা। "মেমরিতে মাপসই করা খুব বড়" সীমাবদ্ধতার মানে আমাদের জেনারেটর দিয়ে লাইন-বাই-লাইন প্রক্রিয়া করা উচিত।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- মধ্যবর্তী তালিকা তৈরি না করে দক্ষ শব্দ নিষ্কাশনের জন্য`re.finditer`ব্যবহার করুন।
- প্রতি শব্দে O(1) বৃদ্ধির জন্য`collections.Counter`ব্যবহার করুন।
-`Counter.most_common(n)`ব্যবহার করুন যা অভ্যন্তরীণভাবে একটি হিপ ব্যবহার করে — সম্পূর্ণ সাজানোর জন্য O(n log n) এর পরিবর্তে O(k log n) ব্যবহার করে।
- মেমরি স্থির রাখতে জেনারেটরের মাধ্যমে লাইন-বাই-লাইন প্রক্রিয়া করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```python
import re
from collections import Counter
from typing import Iterator

def word_stream(path: str) -> Iterator[str]:
    """Yield lowercase words from a file, one at a time."""
    word_pattern = re.compile(r'[a-z\']+')
    with open(path, encoding='utf-8') as f:
        for line in f:
            for match in word_pattern.finditer(line.lower()):
                yield match.group()

def top_words(path: str, n: int = 20) -> list[tuple[str, int]]:
    """Return the n most frequent words in a text file."""
    counter = Counter(word_stream(path))
    return counter.most_common(n)

# Usage
for word, count in top_words("shakespeare.txt", 10):
    print(f"{word:>15} : {count}")
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- মেমরি: শুধুমাত্র কাউন্টার ডিক্ট মেমরিতে রয়েছে (প্রতি অনন্য শব্দে একটি এন্ট্রি), ফাইলের বিষয়বস্তু নয়। ইংরেজি পাঠ্যের জন্য, ~100K অনন্য শব্দ ≈ কয়েক এমবি।
- সময়: O(W) সমস্ত শব্দ স্ক্যান করার জন্য + O(U log N) টপ-N নিষ্কাশনের জন্য, যেখানে W = মোট শব্দ, U = অনন্য শব্দ।
- এজ কেস: সংকোচনের অ্যাপোস্ট্রফিস ("করবেন না") রেজেক্স দ্বারা সংরক্ষিত হয়। ইউনিকোড পাঠ্যের প্রয়োজন হবে`re.UNICODE`পতাকা বা একটি ভিন্ন প্যাটার্ন।
### সমস্যা 2: একটি থ্রেড-নিরাপদ LRU ক্যাশে প্রয়োগ করুন
**সমস্যা বিবৃতি:** স্ক্র্যাচ থেকে একটি সর্বনিম্ন সাম্প্রতিক ব্যবহৃত (LRU) ক্যাশে তৈরি করুন যা থ্রেড-নিরাপদ, O(1) গেট এবং পুট অপারেশন সমর্থন করে এবং ক্ষমতা অতিক্রম করা হলে স্বয়ংক্রিয়ভাবে সর্বনিম্ন ব্যবহৃত আইটেমটি উচ্ছেদ করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
একটি এলআরইউ ক্যাশের প্রয়োজন: (1) কী → হ্যাশ ম্যাপ দ্বারা দ্রুত সন্ধান, (2) রিসেন্সি → দ্বিগুণ লিঙ্কযুক্ত তালিকা, (3) থ্রেড সুরক্ষা → লকিং দ্বারা দ্রুত ক্রম।`get(key)`এ: আইটেমটিকে সামনে নিয়ে যান।`put(key, val)`এ: সামনে সন্নিবেশ করান; ধারণক্ষমতা বেশি হলে পিছন থেকে সরান।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- পাইথনের`dict`সন্নিবেশের ক্রম (3.7+) বজায় রাখে, তাই আমরা একটি আদেশকৃত ডিক্ট পদ্ধতি ব্যবহার করতে পারি: শেষের দিকে যেতে মুছুন এবং পুনরায় সন্নিবেশ করুন।
- থ্রেড নিরাপত্তার জন্য, পারস্পরিক বর্জনের জন্য`threading.Lock`ব্যবহার করুন।
- বিকল্প:`collections.OrderedDict`ব্যবহার করুন যার`move_to_end()`আছে।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```python
import threading
from collections import OrderedDict

class ThreadSafeLRU:
    def __init__(self, capacity: int):
        self._cache: OrderedDict = OrderedDict()
        self._capacity = capacity
        self._lock = threading.Lock()

    def get(self, key: str) -> object | None:
        with self._lock:
            if key not in self._cache:
                return None
            self._cache.move_to_end(key)  # Mark as most recent
            return self._cache[key]

    def put(self, key: str, value: object) -> None:
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
            self._cache[key] = value
            if len(self._cache) > self._capacity:
                self._cache.popitem(last=False)  # Remove least recent

    def __len__(self) -> int:
        with self._lock:
            return len(self._cache)

# Usage
cache = ThreadSafeLRU(capacity=100)
cache.put("user:1", {"name": "Alice"})
result = cache.get("user:1")  # {"name": "Alice"}
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- সময়ের জটিলতা:`get`এবং`put`উভয়ের জন্য O(1) —`OrderedDict.move_to_end()`এবং`popitem()`হল O(1)।
- থ্রেড নিরাপত্তা:`Lock`পারমাণবিকতা নিশ্চিত করে। উচ্চতর থ্রুপুটের জন্য,`threading.RLock`বা একটি রিড-রাইট লক প্যাটার্ন বিবেচনা করুন, তবে বেশিরভাগ ব্যবহারের ক্ষেত্রে একটি সাধারণ লক যথেষ্ট।
- প্রোডাকশন নোট: একক-থ্রেডেড কোডের জন্য,`functools.lru_cache`আরও সহজ এবং ভাল পারফরম্যান্সের জন্য C-তে প্রয়োগ করা হয়েছে।
### সমস্যা 3: একটি গাণিতিক অভিব্যক্তি পার্স এবং মূল্যায়ন করুন
**সমস্যা বিবৃতি:** একটি পার্সার লিখুন যেটি`"3 + 4 * 2 / (1 - 5)"`এর মতো একটি স্ট্রিং নেয় এবং অপারেটর অগ্রাধিকার এবং বন্ধনীকে সম্মান করে এটি সঠিকভাবে মূল্যায়ন করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
এর জন্য প্রয়োজন: (1) ইনপুট স্ট্রিংকে সংখ্যা, অপারেটর এবং বন্ধনীতে টোকেনাইজ করা, (2) সঠিক অগ্রাধিকার সহ পার্সিং (`*` এবং`/``+` এবং`-`এর আগে), (3) নেস্টেড প্যারেন্টসেস পরিচালনা করা। একটি নির্বোধ বাম থেকে ডান মূল্যায়ন ভুল ফলাফল দেবে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
ক্লাসিক সমাধান হল **শান্টিং-ইয়ার্ড অ্যালগরিদম** (ডিজকস্ট্রা) যা ইনফিক্সকে পোস্টফিক্সে রূপান্তর করে (রিভার্স পোলিশ নোটেশন), তারপর পোস্টফিক্সের মূল্যায়ন করে। বিকল্পভাবে, একটি রিকার্সিভ ডিসেন্ট পার্সার ব্যবহার করুন। পাইথনের জন্য বিশেষভাবে, আমরা নিরাপদ মূল্যায়নের জন্য`ast.literal_eval`ব্যবহার করতে পারি — তবে আসুন এটি সঠিকভাবে বাস্তবায়ন করি।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```python
import re
from typing import List

def tokenize(expr: str) -> List[str]:
    return re.findall(r'\d+\.?\d*|[+\-*/()]', expr.replace(' ', ''))

def to_postfix(tokens: List[str]) -> List[str]:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output, ops = [], []
    for token in tokens:
        if re.match(r'\d', token):
            output.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()  # Remove '('
        else:  # Operator
            while ops and ops[-1] != '(' and precedence.get(ops[-1], 0) >= precedence[token]:
                output.append(ops.pop())
            ops.append(token)
    return output + ops[::-1]

def evaluate_postfix(postfix: List[str]) -> float:
    stack = []
    for token in postfix:
        if re.match(r'\d', token):
            stack.append(float(token))
        else:
            b, a = stack.pop(), stack.pop()
            ops = {'+': lambda x, y: x+y, '-': lambda x, y: x-y,
                   '*': lambda x, y: x*y, '/': lambda x, y: x/y}
            stack.append(ops[token](a, b))
    return stack[0]

def calculate(expr: str) -> float:
    return evaluate_postfix(to_postfix(tokenize(expr)))

# Usage
print(calculate("3 + 4 * 2 / (1 - 5)"))  # 1.0
print(calculate("10 + 20 * 3 - 4 / 2"))   # 68.0
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- সঠিকতা:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→ `1.0`। সঠিক।
- সময়: টোকেনাইজেশনের জন্য O(N), শান্টিং-ইয়ার্ডের জন্য O(N), মূল্যায়নের জন্য O(N) — সামগ্রিক O(N)।
- পরিচালনার জন্য এজ কেস: নেতিবাচক সংখ্যা (অন্যারি`-`এর আগে`0`), শূন্য দিয়ে বিভাজন (ত্রুটি পরিচালনা যোগ করুন), অবৈধ ইনপুট (টোকেন যাচাই করুন)।
- পাইথনিক বিকল্প:`eval()`ছাড়া নিরাপদ মূল্যায়নের জন্য একটি কাস্টম নোড ভিজিটর সহ `ast.parse(expr, mode='eval')`৷
### সমস্যা 4: রিয়েল-টাইম ডেটা আপডেট সহ একটি CLI ড্যাশবোর্ড তৈরি করুন
**সমস্যা বিবৃতি:** একটি টার্মিনাল-ভিত্তিক ড্যাশবোর্ড তৈরি করুন যা রঙ-কোডেড থ্রেশহোল্ড এবং প্রতিক্রিয়াশীল লেআউট সহ রিয়েল-টাইমে সিস্টেম মেট্রিক্স (CPU, মেমরি, ডিস্ক) আপডেট করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) পর্যায়ক্রমিক সিস্টেম মেট্রিক সংগ্রহ, (2) কার্সার নিয়ন্ত্রণের সাথে টার্মিনাল রেন্ডারিং, (3) থ্রেশহোল্ডের উপর ভিত্তি করে রঙের আউটপুট, (4) প্রস্থান করার জন্য নন-ব্লকিং কীবোর্ড ইনপুট। এটি একটি রেন্ডারিং লুপ সহ একটি প্রযোজক-ভোক্তা প্যাটার্ন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- ক্রস-প্ল্যাটফর্ম সিস্টেম মেট্রিক্সের জন্য`psutil`ব্যবহার করুন।
- কার্সার পজিশনিং এবং রঙের জন্য ANSI এস্কেপ কোড ব্যবহার করুন (বা উচ্চ-স্তরের API-এর জন্য`rich`লাইব্রেরি)।
- আপডেট ব্যবধানের জন্য`time.sleep`ব্যবহার করুন।
- এইভাবে কাঠামো: ডেটা সংগ্রহ → বিন্যাস → রেন্ডারিং পাইপলাইন৷
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```python
import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colorize(value, warn_thresh, crit_thresh):
    if value >= crit_thresh:
        return f"\033[91m{value:.1f}%\033[0m"  # Red
    elif value >= warn_thresh:
        return f"\033[93m{value:.1f}%\033[0m"  # Yellow
    return f"\033[92m{value:.1f}%\033[0m"      # Green

def progress_bar(value, width=30):
    filled = int(width * value / 100)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}]"

def render_dashboard():
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters()

    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║         SYSTEM DASHBOARD                 ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  CPU:    {colorize(cpu, 60, 85):>8}  {progress_bar(cpu)}  ║")
    print(f"║  Memory: {colorize(mem, 70, 90):>8}  {progress_bar(mem)}  ║")
    print(f"║  Disk:   {colorize(disk, 75, 90):>8}  {progress_bar(disk)}  ║")
    print(f"║  Net ↑:  {net.bytes_sent / 1e6:.1f} MB  ↓: {net.bytes_recv / 1e6:.1f} MB    ║")
    print("╚══════════════════════════════════════════╝")
    print("Press Ctrl+C to exit")

try:
    while True:
        render_dashboard()
        time.sleep(2)
except KeyboardInterrupt:
    clear_screen()
    print("Dashboard closed.")
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
-`cpu_percent(interval=0.5)`পরিমাপ করার জন্য 0.5 সেকেন্ডের জন্য ব্লক করে — এটি সঠিক পদ্ধতি (নন-ব্লকিং মোড প্রথম কলে 0% দেয়)।
- ANSI কোডগুলি আধুনিক উইন্ডোজ টার্মিনাল এবং সমস্ত ইউনিক্স টার্মিনালে কাজ করে। লিগ্যাসি Windows cmd-এর জন্য,`os.system('color')`যোগ করুন বা`colorama`ব্যবহার করুন।
- প্রোডাকশন আপগ্রেড: ফ্লিকার-ফ্রি রেন্ডারিং, স্বয়ংক্রিয় লেআউট এবং ক্রস-প্ল্যাটফর্ম সামঞ্জস্যের জন্য`rich`লাইব্রেরি (`rich.live`) ব্যবহার করুন৷
- এক্সটেনসিবিলিটি: প্রতিটি মেট্রিক একটি স্বাধীন ফাংশন, যা GPU তাপমাত্রা, প্রক্রিয়া গণনা বা নেটওয়ার্ক সংযোগ যোগ করা সহজ করে তোলে।
---

## সারাংশ
পাইথনের পঠনযোগ্যতা, বহুমুখিতা এবং বাস্তুতন্ত্রের গভীরতার সমন্বয় এটিকে বিশ্বের সবচেয়ে বেশি ব্যবহৃত প্রোগ্রামিং ভাষা করে তোলে। এটি AI/ML-এর জন্য ডিফল্ট পছন্দ, ওয়েব ব্যাকএন্ড এবং অটোমেশনের জন্য একটি শক্তিশালী বিকল্প এবং একটি চমৎকার শিক্ষার ভাষা। এর প্রধান দুর্বলতাগুলি — সম্পাদনের গতি এবং মোবাইল/এমবেডেড সমর্থন — ভালভাবে বোঝা যায় এবং সমাধানগুলি প্রতিষ্ঠা করেছে৷ বেশিরভাগ প্রকল্পের জন্য, পাইথন একটি যুক্তিসঙ্গত সূচনা পয়েন্ট।