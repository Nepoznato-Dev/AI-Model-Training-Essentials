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
# ازگر
Python ایک اعلی سطحی، تشریح شدہ، عام مقصد کی پروگرامنگ زبان ہے جسے Guido van Rossum نے تخلیق کیا تھا اور اسے پہلی بار 1991 میں جاری کیا گیا تھا۔ یہ اہم انڈینٹیشن اور صاف نحو کے ذریعے کوڈ پڑھنے کی اہلیت کو ترجیح دیتا ہے جو سادہ انگریزی کے قریب پڑھتا ہے۔ Python متحرک طور پر ٹائپ کیا جاتا ہے، کوڑا کرکٹ جمع کیا جاتا ہے، اور متعدد پروگرامنگ پیراڈائمز بشمول طریقہ کار، آبجیکٹ اورینٹڈ، اور فنکشنل پروگرامنگ کی حمایت کرتا ہے۔
آج، Python AI/ML، ڈیٹا سائنس، سائنسی کمپیوٹنگ، اور آٹومیشن میں غالب زبان ہے - جبکہ ابتدائی افراد کے لیے بہترین زبانوں میں سے ایک ہے۔ وہ دوہری شناخت (پہلے اسکرپٹ کے لیے کافی آسان، بڑی زبان کے ماڈلز کو تربیت دینے کے لیے کافی طاقتور) اسے الگ کرتا ہے۔
---

## ازگر کیوں اہمیت رکھتا ہے۔
- **ڈیزائن کے لحاظ سے پڑھنے کی اہلیت**: کوئی سیمی کالون نہیں، کوئی منحنی خطوط وحدانی نہیں - انڈینٹیشن دائرہ کار کی وضاحت کرتا ہے۔ کوڈ pseudocode کی طرح پڑھتا ہے۔
- **بڑے پیمانے پر ماحولیاتی نظام**: PyPI تقریباً ہر ڈومین پر مشتمل 500,000 پیکجز کی میزبانی کرتا ہے۔
- **AI کی زبان**: PyTorch, TensorFlow, scit-learn, Hugging Face, LangChain — پورا AI/ML اسٹیک Python-first ہے۔
- **گلو لینگویج**: ایک C++ انجن کو ویب API سے صرف چند لائنوں میں ڈیٹا بیس سے جوڑیں۔
- **کراس پلیٹ فارم**: بغیر کسی ترمیم کے Windows، macOS، Linux، اور ایمبیڈڈ سسٹمز پر چلتا ہے۔
- **کمیونٹی**: دنیا کی سب سے بڑی اور فعال پروگرامنگ کمیونٹی۔
## ٹریڈ آف
ازگر کامل نہیں ہے۔ اس کی حدود کو سمجھنے سے آپ کو یہ فیصلہ کرنے میں مدد ملتی ہے کہ کسی اور چیز تک کب پہنچنا ہے:
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **عمل کی رفتار** | CPU سے منسلک کاموں کے لیے C سے 10–100x سست | NumPy/PyTorch (ہڈ کے نیچے C)، یا گرم لوپس کے لیے Cython/Numba کا استعمال کریں |
| **GIL (گلوبل انٹرپریٹر لاک)** | CPU کے پابند کام کے لیے حقیقی ملٹی تھریڈڈ ہم آہنگی کو روکتا ہے | استعمال کریں`multiprocessing`,`asyncio`, یا سیلری کی طرح کام کی قطاریں
| **موبائل ڈویلپمنٹ** | iOS/Android ایپس کے لیے موزوں نہیں ہے۔ مقامی کے لیے Swift/Kotlin، یا کراس پلیٹ فارم کے لیے Flutter/React Native کا استعمال کریں۔
| **ایمبیڈڈ سسٹم** | مائکروکنٹرولرز کے لیے بہت بھاری | MicroPython (ایک ہلکا پھلکا ویرینٹ) استعمال کریں یا C/Rust | پر سوئچ کریں۔
| **میموری کا استعمال** | مرتب شدہ زبانوں سے زیادہ میموری فوٹ پرنٹ | زیادہ تر ایپلی کیشنز کے لیے قابل قبول؛ بڑے ڈیٹا کے لیے جنریٹر استعمال کریں |
---

## نحوی بنیادی باتیں
### متغیرات اور اقسام
Python متحرک ٹائپنگ کا استعمال کرتا ہے - آپ متغیر قسموں کا اعلان نہیں کرتے ہیں، لیکن آپ وضاحت اور ٹولنگ سپورٹ کے لیے قسم کے اشارے شامل کر سکتے ہیں۔
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

### کنٹرول فلو
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

### افعال
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

### آبجیکٹ اورینٹڈ پروگرامنگ
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

### نقص کو ہینڈل کرنا
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

## اعلی درجے کی نحو اور نمونے۔
###`typing`ماڈیول کے ساتھ جنرک
Python کا`typing`ماڈیول دوبارہ قابل استعمال، ٹائپ سیف اجزاء کی تعمیر کے لیے عام قسم کی مدد فراہم کرتا ہے۔ جنرکس آپ کو فنکشنز اور کلاسز لکھنے دیتے ہیں جو کسی بھی قسم کے ساتھ کام کرتے ہیں جبکہ جامد تجزیہ کے لیے قسم کی معلومات کو محفوظ رکھتے ہیں۔
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

### ڈیکوریٹر اور میٹا پروگرامنگ
ڈیکوریٹرز Python کی سب سے طاقتور خصوصیات میں سے ایک ہیں — وہ آپ کو اپنے ماخذ کوڈ کو تبدیل کیے بغیر فنکشنز اور کلاسز کے رویے میں ترمیم یا توسیع کرنے دیتے ہیں۔
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

### ساختی پیٹرن میچنگ (Python 3.10+)
Python کا`match/case`بیان تباہی، گارڈز، اور نیسٹڈ پیٹرن کے ساتھ طاقتور پیٹرن میچنگ فراہم کرتا ہے۔
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

### بندش، اعلیٰ ترتیب کے افعال، اور تکرار کرنے والے
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

### آپریٹر اوورلوڈنگ
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

### اپنی مرضی کے استثنائی درجہ بندی
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

## گہرائی میں اہم خصوصیات
### معیاری لائبریری ("بیٹریاں شامل")
ایک وسیع معیاری لائبریری کے ساتھ ازگر جہاز۔ کچھ سب سے زیادہ استعمال ہونے والے ماڈیولز:
| ماڈیول | مقصد | استعمال کی مثال |
|---------|---------|------------|
| `os`/`pathlib`| فائل سسٹم آپریشنز | `Path("data/output.csv").exists()`|
| `json`| JSON انکوڈنگ/ڈی کوڈنگ | `json.loads(response_text)`|
| `datetime`| تاریخ اور وقت ہینڈلنگ | `datetime.now(timezone.utc)`|
| `collections`| خصوصی کنٹینرز | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Iterator بلڈنگ بلاکس | `combinations(items, 2)`|
| `functools`| فنکشن ٹولز | `lru_cache`,`partial`,`reduce`|
| `re`| باقاعدہ اظہار | `re.findall(r"\d+", text)`|
| `subprocess`| بیرونی کمانڈز چلائیں | `subprocess.run(["ls", "-la"])`|
| `logging`| درخواست لاگنگ | `logging.basicConfig(level=logging.INFO)`|
| `typing`| قسم کے اشارے کی حمایت | `Optional[str]`,`Union[int, float]`|
| `http.server`| سادہ HTTP سرور | `python -m http.server 8000`|
| `threading`/`asyncio`| ہم آہنگی | ویب سکریپرز کے لیے Async I/O |
### ورچوئل ماحولیات اور پیکیج مینجمنٹ
ہر Python پروجیکٹ کو انحصار کو الگ تھلگ کرنے کے لیے ورچوئل ماحول استعمال کرنا چاہیے:
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

جدید Python پروجیکٹس پرانے`setup.py`/`requirements.txt`اپروچ کی جگہ لے کر، انحصار کے انتظام کے لیے`pyproject.toml`کو `uv`، `poetry`، یا`hatch`جیسے ٹولز کے ساتھ تیزی سے استعمال کرتے ہیں۔
### Async پروگرامنگ
Python کا`asyncio`بغیر دھاگوں کے سمورتی I/O کو قابل بناتا ہے — ویب سکریپرز، چیٹ سرورز، اور API کلائنٹس کے لیے ضروری:
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

## ہم آہنگی اور ہم آہنگی
Python متعدد کنکرنسی ماڈل پیش کرتا ہے، ہر ایک مختلف کام کے بوجھ کے لیے موزوں ہے۔ CPython میں GIL (گلوبل انٹرپریٹر لاک) دھاگوں کے ساتھ حقیقی CPU متوازی کو روکتا ہے، لہذا صحیح ماڈل اس بات پر منحصر ہے کہ آیا آپ کا کام کا بوجھ I/O- پابند ہے یا CPU- پابند ہے۔
### تھریڈنگ (I/O- پابند کام)
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

### ملٹی پروسیسنگ (سی پی یو سے منسلک کام)
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

### Asyncio اندرونی
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ ڈائرکٹری کا ڈھانچہ
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

### تشکیل کنفیگریشن — `pyproject.toml`
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

### جدید آلات کے ساتھ انحصار کا انتظام
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

### لنٹنگ اور کوڈ کوالٹی
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD پائپ لائن — GitHub ایکشنز
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

## ٹیسٹنگ
### ٹیسٹنگ فریم ورک اور سیٹ اپ
Python کا ٹیسٹنگ ایکو سسٹم`pytest`کے ارد گرد ہے، جو Python ٹیسٹنگ کا اصل معیار ہے۔
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

### pytest کے ساتھ یونٹ ٹیسٹ
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

### Async ٹیسٹ اور انٹیگریشن ٹیسٹ
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

## انٹرآپریبلٹی
### cytypes کے ساتھ C/C++ کال کرنا
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

### مزید پیچیدہ C انٹراپ کے لیے cffi کا استعمال
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

### Cython — C کارکردگی کے ساتھ ازگر
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

### Pybind11 — C++ ایکسٹینشنز
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

## ڈیزائن پیٹرن
### سنگلٹن
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

### فیکٹری پیٹرن
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

### مبصر پیٹرن
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

### سیاق و سباق کے مینیجر کا پیٹرن
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

### حکمت عملی کا نمونہ
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

### اصلاح کی تکنیک
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

### بینچ مارکنگ
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## تعیناتی۔
### پیکیجنگ اور تقسیم
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### ڈاکر فائل
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

### پلیٹ فارم کے لیے مخصوص تعیناتی۔
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

## ماحولیاتی نظام
ازگر کی طاقت صرف زبان نہیں ہے - یہ اس کے ارد گرد بنایا گیا ماحولیاتی نظام ہے۔
### AI اور مشین لرننگ
| لائبریری | مقصد |
|---------|---------|
| PyTorch | گہری تعلیم (تحقیق اور پیداوار) |
| TensorFlow / Keras | گہری تعلیم (پروڈکشن پر مرکوز) |
| scikit-learn | کلاسیکل ML (رجعت، کلسٹرنگ، درجہ بندی) |
| گلے لگانا چہرہ ٹرانسفارمرز | پہلے سے تربیت یافتہ NLP/وژن ماڈلز |
| LangChain / LlamaIndex | LLMs کے ساتھ ایپلی کیشنز بنانا |
| NumPy | عددی کمپیوٹنگ (ارے، لکیری الجبرا) |
| پانڈا | ڈیٹا ہیرا پھیری اور تجزیہ |
| Matplotlib / Seaborn / Plotly | ڈیٹا ویژولائزیشن |
### ویب ڈویلپمنٹ
| فریم ورک | انداز | کے لیے بہترین |
|------------|-------|------------|
| جینگو | مکمل اسٹیک، "بیٹریاں شامل" | ایڈمن پینلز کے ساتھ پیچیدہ ویب ایپس، ORM، auth |
| فاسٹ اے پی آئی | جدید، async، قسم سے چلنے والا | APIs اور مائیکرو سروسز (فی الحال سب سے تیزی سے بڑھتی ہوئی) |
| فلاسک | کم سے کم، لچکدار | چھوٹی ایپس اور پروٹو ٹائپس |
| Streamlit | ڈیٹا ایپ فوکسڈ | ڈیش بورڈز اور ڈیٹا ڈیمو خالص ازگر میں |
### آٹومیشن اور اسکرپٹنگ
| لائبریری | مقصد |
|---------|---------|
| `subprocess`/`os`| سسٹم ایڈمنسٹریشن |
| `requests`/`httpx`| HTTP کلائنٹس |
| `BeautifulSoup`/`Scrapy`| ویب سکریپنگ |
| `Selenium`/`Playwright`| براؤزر آٹومیشن |
| `Celery`| تقسیم شدہ کام کی قطاریں |
| `Airflow`| ورک فلو آرکیسٹریشن |
### سائنسی کمپیوٹنگ
| لائبریری | مقصد |
|---------|---------|
| NumPy | سرنی آپریشنز اور لکیری الجبرا |
| SciPy | سائنسی الگورتھم (اصلاح، سگنل پروسیسنگ) |
| SymPy | علامتی ریاضی |
| Jupyter نوٹ بک | انٹرایکٹو کمپیوٹنگ ماحول |
| JAX | اعلی کارکردگی والی عددی کمپیوٹنگ (GPU-accelerated) |
---

## ازگر کا استعمال کب کریں۔
| منظر نامہ | کیوں ازگر | بہتر متبادل |
|------------|------------|-------------------|
| AI/ML/ڈیٹا سائنس | ماحولیاتی نظام بے مثال ہے | - |
| آٹومیشن اور اسکرپٹنگ | لکھنے اور ڈیبگ کرنے میں سب سے تیز | شیل/پاور شیل سادہ سیسڈمین کاموں کے لیے |
| ویب بیک اینڈز (APIs) | FastAPI بہترین ہے | بہت اعلی تھرو پٹ خدمات کے لیے جاوا یا جاوا |
| پروٹو ٹائپنگ | آئیڈیا سے ورکنگ کوڈ تک تیز ترین راستہ | - |
| تعلیم | سب سے زیادہ ابتدائی دوستانہ زبان | - |
| ڈیسک ٹاپ ایپلی کیشنز | ممکنہ لیکن غیر معمولی | C# (ونڈوز)، سوئفٹ (macOS) |
| کارکردگی کے اہم نظام | بچیں — بہت سست | C, C++, Rust |
| موبائل ایپس | صحیح ٹول نہیں | سوئفٹ (iOS)، کوٹلن (Android) |
| ایمبیڈڈ سسٹمز | بہت زیادہ وسائل سے بھرا ہوا | سادہ کیسز کے لیے C، Rust، یا MicroPython |
---

## ازگر کے ورژن
زبان کا ارتقاء جاری ہے۔ اہم حالیہ اضافے:
| ورژن | سال | قابل ذکر خصوصیات |
|---------|---------|------|
| 3.10 | 2021 | ساختی پیٹرن کی مماثلت (`match/case`)، بہتر خرابی کے پیغامات |
| 3.11 | 2022 | 10-60% تیزی سے عملدرآمد، بہتر ٹریس بیکس |
| 3.12 | 2023 | مزید لچکدار f-strings،`type`بیان، کارکردگی کے فوائد |
| 3.13 | 2024 | تجرباتی فری تھریڈڈ موڈ (کوئی GIL نہیں)، بہتر REPL |
| 3.14 | 2025 | مزید No-GIL بہتری، ٹائپ سسٹم میں اضافہ |
Python 2 1 جنوری 2020 کو آخری زندگی کو پہنچ گیا۔ تمام نئے پروجیکٹوں کو Python 3.10 یا اس کے بعد کا ورژن استعمال کرنا چاہیے۔
---

## فوری حوالہ: عام محاورے۔
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

## مصنوعی سوال و جواب
### Q1: فہرستوں اور tuples میں کیا فرق ہے، اور مجھے ہر ایک کب استعمال کرنا چاہیے؟
**A:** فہرستیں متغیر ہیں (`[]`)، ٹیپلز ناقابل تغیر (`()`) ہیں۔ جب آپ کو عناصر کو شامل کرنے، ہٹانے یا تبدیل کرنے کی ضرورت ہو تو فہرستوں کا استعمال کریں۔ متضاد ڈیٹا، ڈکشنری کیز، فنکشن ریٹرن ویلیوز، یا جب آپ "یہ تبدیل نہیں ہونا چاہیے" کا اشارہ دینا چاہتے ہیں، کے فکسڈ کلیکشن کے لیے ٹیپلز کا استعمال کریں۔ Tuples قدرے زیادہ میموری کے قابل ہیں اور انہیں سیٹ/ڈکٹ کیز کے طور پر استعمال کیا جا سکتا ہے۔ فہرستیں نہیں کر سکتے ہیں.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: گلوبل انٹرپریٹر لاک (GIL) میرے کوڈ کو کیسے متاثر کرتا ہے، اور مجھے اس کے بارے میں کیا کرنا چاہیے؟
**A:** GIL متعدد تھریڈز کو بیک وقت Python بائیک کوڈ پر عمل کرنے سے روکتا ہے، جس سے تھریڈنگ CPU کے پابند کام کے لیے غیر موثر ہو جاتی ہے۔ I/O- پابند کاموں کے لیے (نیٹ ورک کی درخواستیں، فائل I/O)،`threading`یا`asyncio`ٹھیک کام کرتے ہیں کیونکہ GIL I/O کے دوران جاری ہوتا ہے۔ CPU کے پابند کاموں کے لیے،`multiprocessing`(علیحدہ عمل، ہر ایک کی اپنی GIL کے ساتھ) استعمال کریں، یا C ایکسٹینشنز (NumPy، Cython، Numba) پر آف لوڈ کریں جو GIL کو اندرونی طور پر جاری کرتے ہیں۔
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: کیا مجھے ہر جگہ قسم کے اشارے استعمال کرنے چاہئیں؟ عملی تجارت کیا ہیں؟
**A:** قسم کے اشارے (`def greet(name: str) -> str:`) اختیاری ہیں اور رن ٹائم پر نافذ نہیں ہوتے ہیں۔ وہ IDE خودکار تکمیل کو بہتر بناتے ہیں، جامد تجزیہ ٹولز (mypy) اور دستاویز کے ارادے کے ذریعے کیڑے پکڑتے ہیں۔ ٹریڈ آف اضافی وربوسٹی اور اعلی درجے کی اقسام (`Union`، `Generic`، `Protocol`) کے لیے سیکھنے کا منحنی خطوط ہے۔ تجویز: ~500 لائنوں سے زیادہ کے کسی بھی پروجیکٹ میں فنکشن کے دستخطوں کے لیے قسم کے اشارے استعمال کریں۔ مختصر اسکرپٹ میں ان کا تھوڑا سا استعمال کریں۔ بتدریج نفاذ کے لیے CI میں mypy کو فعال کریں۔
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: Python میں مستثنیات سے نمٹنے کے لیے بہترین طریقے کیا ہیں؟
**A:** ننگے`except:`(جو`SystemExit`اور`KeyboardInterrupt`کو بھی پکڑتا ہے) کے بجائے مخصوص استثناء کو پکڑیں۔ خوش راہ منطق کو غلطی سے نمٹنے سے الگ کرنے کے لیے`try/except/else/finally`استعمال کریں۔ لائبریریوں کے لیے حسب ضرورت استثنائی درجہ بندی کی وضاحت کریں۔ کارکردگی کے لحاظ سے حساس کوڈ میں کنٹرول کے بہاؤ کے لیے کبھی استثنیٰ کا استعمال نہ کریں — وہ سست ہیں۔ مکمل ٹریس بیک کیپچر کرنے کے لیے`logging.exception()`کے ساتھ استثناء کو لاگ کریں۔
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

### Q5: جنریٹر میموری کو کیسے محفوظ کرتے ہیں، اور مجھے انہیں فہرستوں پر کب استعمال کرنا چاہیے؟
**A:** جنریٹرز میموری میں پوری فہرست بنانے کے بجائے سستی سے قدریں تیار کرتے ہیں — ایک وقت میں، ایک مانگ پر —۔ بڑے ڈیٹا سیٹس کے لیے (لاکھوں قطاریں، لامحدود ترتیب، سٹریمنگ ڈیٹا)، جنریٹر سائز سے قطع نظر مستقل میموری استعمال کرتے ہیں۔ جب آپ ایک بار اعادہ کریں اور انڈیکسنگ یا`len()`کی ضرورت نہ ہو تو جنریٹر استعمال کریں۔ فہرستیں استعمال کریں جب آپ کو بے ترتیب رسائی کی ضرورت ہو، متعدد تکرار، یا مجموعہ چھوٹا ہو۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: درجہ بندی کے ساتھ ورڈ فریکوئنسی کاؤنٹر بنائیں
**مسئلہ کا بیان:** ایک بڑی ٹیکسٹ فائل کو دیکھتے ہوئے، ہر لفظ کی فریکوئنسی شمار کریں، انہیں فریکوئنسی (نزولی) کے لحاظ سے درجہ دیں، اور سرفہرست N نتائج لوٹائیں۔ کیس کی غیر حساسیت، اوقاف کو ہینڈل کریں، اور میموری میں فٹ ہونے کے لیے بہت بڑی فائلوں کو مؤثر طریقے سے پروسیس کریں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں یہ کرنے کی ضرورت ہے: (1) متن کو پڑھنا، (2) الفاظ میں تقسیم کرنا، (3) کیس کو معمول پر لانا، (4) رموز اوقاف، (5) واقعات کو شمار کرنا، (6) نزول شمار کے حساب سے ترتیب دینا، (7) اوپر واپس آنا۔ "میموری میں فٹ ہونے کے لیے بہت بڑا" رکاوٹ کا مطلب ہے کہ ہمیں جنریٹر کے ساتھ لائن بہ لائن عمل کرنا چاہیے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- انٹرمیڈیٹ لسٹیں بنائے بغیر موثر الفاظ نکالنے کے لیے`re.finditer`استعمال کریں۔
- فی لفظ O(1) انکریمنٹ کے لیے`collections.Counter`استعمال کریں۔
-`Counter.most_common(n)`استعمال کریں جو اندرونی طور پر ایک ہیپ کا استعمال کرتا ہے — O(k log n) کی بجائے مکمل ترتیب کے لیے۔
- میموری کو مستقل رکھنے کے لیے جنریٹر کے ذریعے لائن بہ لائن عمل کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- میموری: صرف کاؤنٹر ڈکٹ میموری میں ہے (فی منفرد لفظ ایک اندراج)، فائل کا مواد نہیں۔ انگریزی متن کے لیے، ~100K منفرد الفاظ ≈ چند MB۔
- وقت: O(W) تمام الفاظ کو اسکین کرنے کے لیے + O(U log N) ٹاپ-N نکالنے کے لیے، جہاں W = کل الفاظ، U = منفرد الفاظ۔
- ایج کیسز: سنکچن میں apostrophes ("نہیں") ریجیکس کے ذریعہ محفوظ ہیں۔ یونیکوڈ متن کو`re.UNICODE`پرچم یا ایک مختلف پیٹرن کی ضرورت ہوگی۔
### مسئلہ 2: تھریڈ سیف LRU کیشے کو لاگو کریں۔
**مسئلہ کا بیان:** شروع سے ہی کم سے کم استعمال شدہ (LRU) کیشے بنائیں جو تھریڈ سے محفوظ ہو، O(1) گیٹ اینڈ پوٹ آپریشنز کو سپورٹ کرتا ہو، اور صلاحیت سے زیادہ ہونے پر حال ہی میں استعمال ہونے والی کم از کم استعمال شدہ شے کو خود بخود نکال دیتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ایک LRU کیش کی ضرورت ہے: (1) کلید → ہیش میپ کے ذریعہ تیزی سے تلاش کرنا، (2) رجعت کے ذریعہ تیزی سے ترتیب دینا → دوگنا لنک شدہ فہرست، (3) تھریڈ سیفٹی → لاکنگ۔`get(key)`پر: آئٹم کو سامنے لے جائیں۔`put(key, val)`پر: سامنے داخل کریں؛ اگر گنجائش سے زیادہ ہو تو پیچھے سے ہٹا دیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- Python کا`dict`اندراج آرڈر (3.7+) کو برقرار رکھتا ہے، لہذا ہم ایک ترتیب شدہ ڈکٹ اپروچ استعمال کر سکتے ہیں: ختم کرنے کے لیے حذف کریں اور دوبارہ داخل کریں۔
- دھاگے کی حفاظت کے لیے، باہمی اخراج کے لیے`threading.Lock`استعمال کریں۔
- متبادل:`collections.OrderedDict`استعمال کریں جس میں`move_to_end()`ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- وقت کی پیچیدگی: O(1)`get`اور`put`دونوں کے لیے —`OrderedDict.move_to_end()`اور`popitem()`O(1) ہیں۔
- تھریڈ سیفٹی:`Lock`ایٹمی ہونے کو یقینی بناتا ہے۔ زیادہ تھرو پٹ کے لیے،`threading.RLock`یا ریڈ رائٹ لاک پیٹرن پر غور کریں، لیکن زیادہ تر استعمال کے معاملات کے لیے ایک سادہ لاک کافی ہے۔
- پروڈکشن نوٹ: سنگل تھریڈڈ کوڈ کے لیے، بہتر کارکردگی کے لیے`functools.lru_cache`آسان اور C میں لاگو کیا گیا ہے۔
### مسئلہ 3: ریاضی کے اظہار کو پارس کریں اور اس کا اندازہ کریں۔
**مسئلہ کا بیان:** ایک پارسر لکھیں جو`"3 + 4 * 2 / (1 - 5)"`جیسی سٹرنگ لے اور آپریٹر کی ترجیح اور قوسین کا احترام کرتے ہوئے اس کا صحیح اندازہ کرے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
اس کی ضرورت ہے: (1) ان پٹ سٹرنگ کو نمبرز، آپریٹرز، اور قوسین میں ٹوکنائز کرنا، (2) درست ترجیح کے ساتھ تجزیہ کرنا (`*` اور`/`سے پہلے`+`اور `-`)، (3) نیسٹڈ پیرنٹیسز کو ہینڈل کرنا۔ ایک بولی بائیں سے دائیں تشخیص غلط نتائج دے گی۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
کلاسک حل **شنٹنگ یارڈ الگورتھم** (ڈجکسٹرا) ہے جو انفکس کو پوسٹ فکس (ریورس پولش نوٹیشن) میں تبدیل کرتا ہے، پھر پوسٹ فکس کا جائزہ لیتا ہے۔ متبادل طور پر، ایک بار بار آنے والا ڈیسنٹ پارسر استعمال کریں۔ خاص طور پر Python کے لیے، ہم محفوظ تشخیص کے لیے`ast.literal_eval`بھی استعمال کر سکتے ہیں — لیکن آئیے اسے صحیح طریقے سے نافذ کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- درستگی:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`۔ درست۔
- وقت: ٹوکنائزیشن کے لیے O(N)، شنٹنگ یارڈ کے لیے O(N)، تشخیص کے لیے O(N) — مجموعی طور پر O(N)۔
- ہینڈل کرنے کے لیے ایج کیسز: منفی نمبرز (Unary`-`سے پہلے `0`)، صفر سے تقسیم (خرابی کو سنبھالنا شامل کریں)، غلط ان پٹ (ٹوکنز کی توثیق کریں)۔
- پائتھونک متبادل:`eval()`کے بغیر محفوظ تشخیص کے لیے اپنی مرضی کے مطابق نوڈ وزیٹر کے ساتھ `ast.parse(expr, mode='eval')`۔
### مسئلہ 4: ریئل ٹائم ڈیٹا اپڈیٹس کے ساتھ CLI ڈیش بورڈ بنائیں
**مسئلہ کا بیان:** ایک ٹرمینل پر مبنی ڈیش بورڈ بنائیں جو سسٹم میٹرکس (سی پی یو، میموری، ڈسک) کو ریئل ٹائم میں اپ ڈیٹ کرتے ہوئے، کلر کوڈڈ تھریشولڈز اور ریسپانسیو لے آؤٹ کے ساتھ دکھائے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) متواتر سسٹم میٹرک کلیکشن، (2) کرسر کنٹرول کے ساتھ ٹرمینل رینڈرنگ، (3) حد کی بنیاد پر کلر آؤٹ پٹ، (4) چھوڑنے کے لیے نان بلاکنگ کی بورڈ ان پٹ۔ یہ رینڈرنگ لوپ کے ساتھ ایک پروڈیوسر صارف پیٹرن ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- کراس پلیٹ فارم سسٹم میٹرکس کے لیے`psutil`استعمال کریں۔
- کرسر کی پوزیشننگ اور رنگوں کے لیے ANSI فرار کوڈز کا استعمال کریں (یا اعلی سطح کے API کے لیے`rich`لائبریری)۔
- اپ ڈیٹ وقفہ کے لیے`time.sleep`استعمال کریں۔
- اس طرح کی ساخت: ڈیٹا اکٹھا کرنا → فارمیٹنگ → رینڈرنگ پائپ لائن۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
-`cpu_percent(interval=0.5)`کی پیمائش کے لیے 0.5s کے لیے بلاکس — یہ صحیح طریقہ ہے (نان بلاکنگ موڈ پہلی کال پر 0% دیتا ہے)۔
- ANSI کوڈ جدید ونڈوز ٹرمینل اور تمام یونکس ٹرمینلز پر کام کرتے ہیں۔ Windows cmd کے لیے،`os.system('color')`شامل کریں یا`colorama`استعمال کریں۔
- پروڈکشن اپ گریڈ: فلکر فری رینڈرنگ، خودکار لے آؤٹ، اور کراس پلیٹ فارم مطابقت کے لیے`rich`لائبریری (`rich.live`) کا استعمال کریں۔
- توسیع پذیری: ہر میٹرک ایک آزاد فنکشن ہے، جس سے GPU درجہ حرارت، عمل کی گنتی، یا نیٹ ورک کنکشن شامل کرنا آسان ہو جاتا ہے۔
---

## خلاصہ
Python کی پڑھنے کی اہلیت، استعداد، اور ماحولیاتی نظام کی گہرائی کا مجموعہ اسے دنیا میں سب سے زیادہ استعمال ہونے والی پروگرامنگ زبان بناتا ہے۔ یہ AI/ML کے لیے پہلے سے طے شدہ انتخاب ہے، ویب بیک اینڈ اور آٹومیشن کے لیے ایک مضبوط آپشن، اور ایک بہترین تدریسی زبان ہے۔ اس کی بنیادی کمزوریاں - عمل درآمد کی رفتار اور موبائل/ایمبیڈڈ سپورٹ - اچھی طرح سمجھی جاتی ہیں اور اس نے کام کے حل کو قائم کیا ہے۔ زیادہ تر پروجیکٹس کے لیے، ازگر ایک معقول نقطہ آغاز ہے۔