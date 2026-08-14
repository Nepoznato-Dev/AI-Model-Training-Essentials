<!--
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

-->
#پایتون
پایتون یک زبان برنامه نویسی سطح بالا، تفسیر شده و همه منظوره است که توسط Guido van Rossum ایجاد شد و اولین بار در سال 1991 منتشر شد. این زبان خوانایی کد را از طریق تورفتگی قابل توجه و یک نحو تمیز که نزدیک به انگلیسی ساده می خواند، اولویت بندی می کند. پایتون به صورت پویا تایپ می شود، زباله جمع آوری می شود و از الگوهای برنامه نویسی متعدد از جمله برنامه نویسی رویه ای، شی گرا و تابعی پشتیبانی می کند.
امروزه، پایتون زبان غالب در AI/ML، علم داده، محاسبات علمی و اتوماسیون است – در حالی که همچنان یکی از بهترین زبان ها برای مبتدیان است. این هویت دوگانه (به اندازه کافی ساده برای اولین اسکریپت، به اندازه کافی قدرتمند برای آموزش مدل های زبان بزرگ) چیزی است که آن را متمایز می کند.
---

## چرا پایتون مهم است
- ** خوانایی بر اساس طراحی **: بدون نقطه ویرگول، بدون بریس - تورفتگی محدوده را مشخص می کند. کد مانند شبه کد خوانده می شود.
- **اکوسیستم عظیم**: PyPI میزبان بیش از 500000 بسته است که تقریباً هر دامنه را پوشش می دهد.
- **زبان هوش مصنوعی**: PyTorch، TensorFlow، scikit-learn، Hugging Face، LangChain - کل پشته AI/ML اولین پایتون است.
- **زبان چسب**: موتور ++C را به یک وب API به پایگاه داده تنها در چند خط وصل کنید.
- **کراس پلتفرم**: روی ویندوز، macOS، لینوکس و سیستم های جاسازی شده بدون تغییر اجرا می شود.
- **Community**: بزرگترین و فعال ترین انجمن برنامه نویسی در جهان.
## مبادلات
پایتون کامل نیست. درک محدودیت های آن به شما کمک می کند تصمیم بگیرید که چه زمانی به چیز دیگری برسید:
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **سرعت اجرا** | 10-100 برابر کندتر از C برای کارهای محدود به CPU | از NumPy/PyTorch (C زیر کاپوت)، یا Cython/Numba برای حلقه های داغ استفاده کنید |
| **GIL (قفل مترجم جهانی)** | از موازی سازی چند رشته ای واقعی برای کار با CPU جلوگیری می کند | از `multiprocessing`،`asyncio`یا صف های وظیفه مانند Celery |
| **توسعه موبایل** | برای برنامه های iOS/Android مناسب نیست | از Swift/Kotlin برای بومی یا Flutter/React Native برای کراس پلتفرم |
| **سیستم های تعبیه شده** | خیلی سنگین برای میکروکنترلرها | از MicroPython (یک نوع سبک وزن) استفاده کنید یا به C/Rust | بروید
| **استفاده از حافظه** | ردپای حافظه بالاتر از زبان های کامپایل شده | قابل قبول برای اکثر برنامه ها؛ استفاده از ژنراتور برای داده های بزرگ |
---

## اصول نحو
### متغیرها و انواع
پایتون از تایپ پویا استفاده می‌کند – شما انواع متغیر را اعلام نمی‌کنید، اما می‌توانید نکات نوع را برای وضوح و پشتیبانی ابزار اضافه کنید.
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

### کنترل جریان
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

### توابع
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

### برنامه نویسی شی گرا
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

### رسیدگی به خطا
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

## نحو و الگوهای پیشرفته
### ژنریک با ماژول `typing`
ماژول`typing`پایتون پشتیبانی از نوع عمومی را برای ساخت اجزای قابل استفاده مجدد و ایمن برای نوع فراهم می کند. Generics به شما امکان می دهد توابع و کلاس هایی را بنویسید که با هر نوع کار می کنند و در عین حال اطلاعات نوع را برای تجزیه و تحلیل استاتیک حفظ می کنند.
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

### دکوراتورها و فرابرنامه نویسی
دکوراتورها یکی از قدرتمندترین ویژگی‌های پایتون هستند – آنها به شما اجازه می‌دهند رفتار توابع و کلاس‌ها را بدون تغییر کد منبع آن‌ها اصلاح یا گسترش دهید.
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

### تطبیق الگوی ساختاری (Python 3.10+)
دستور`match/case`پایتون تطبیق الگوی قدرتمندی با ساختار، محافظ و الگوهای تودرتو ارائه می‌کند.
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

### بسته‌ها، توابع مرتبه بالاتر و تکرارکننده‌ها
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

### بارگذاری بیش از حد اپراتور
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

### سلسله مراتب استثنای سفارشی
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

## ویژگی های کلیدی در عمق
### کتابخانه استاندارد ("باتری ها شامل")
پایتون با یک کتابخانه استاندارد گسترده عرضه می شود. برخی از ماژول های پرکاربرد:
| ماژول | هدف | مثال استفاده |
|--------|--------|-------------|
| `os`/`pathlib`| عملیات سیستم فایل | `Path("data/output.csv").exists()`|
| `json`| رمزگذاری/رمزگشایی JSON | `json.loads(response_text)`|
| `datetime`| رسیدگی به تاریخ و زمان | `datetime.now(timezone.utc)`|
| `collections`| ظروف تخصصی | `Counter(words)`,`defaultdict(list)`|
| `itertools`| بلوک های ساختمان Iterator | `combinations(items, 2)`|
| `functools`| ابزار کارکرد | `lru_cache`,`partial`,`reduce`|
| `re`| عبارات منظم | `re.findall(r"\d+", text)`|
| `subprocess`| اجرای دستورات خارجی | `subprocess.run(["ls", "-la"])`|
| `logging`| ثبت برنامه | `logging.basicConfig(level=logging.INFO)`|
| `typing`| پشتیبانی راهنمایی را تایپ کنید | `Optional[str]`,`Union[int, float]`|
| `http.server`| سرور HTTP ساده | `python -m http.server 8000`|
| `threading`/`asyncio`| همزمانی | Async I/O برای وب اسکراپر |
### محیط های مجازی و مدیریت بسته
هر پروژه پایتون باید از یک محیط مجازی برای جداسازی وابستگی ها استفاده کند:
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

پروژه های مدرن پایتون به طور فزاینده ای از`pyproject.toml`با ابزارهایی مانند `uv`، `poetry`، یا`hatch`برای مدیریت وابستگی استفاده می کنند و جایگزین رویکرد قدیمی`setup.py`/`requirements.txt`می شوند.
### برنامه نویسی همگام
`asyncio` پایتون ورودی/خروجی همزمان را بدون رشته‌ها فعال می‌کند - برای اسکراپرهای وب، سرورهای چت و کلاینت‌های API ضروری است:
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

## همزمانی و موازی
پایتون چندین مدل همزمان ارائه می دهد که هر کدام برای بارهای کاری مختلف مناسب هستند. GIL (قفل مترجم جهانی) در CPython از موازی سازی واقعی CPU با رشته ها جلوگیری می کند، بنابراین مدل مناسب به این بستگی دارد که حجم کاری شما محدود به I/O یا محدود به CPU باشد.
### Threading (کارهای I/O-Bound)
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

### چند پردازش (کارهای محدود به CPU)
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

### Asyncio Internals
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

## پیکربندی پروژه و سیستم ساخت
### ساختار فهرست پروژه
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

### پیکربندی ساخت — `pyproject.toml`
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

### مدیریت وابستگی با ابزارهای مدرن
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

### لینتینگ و کیفیت کد
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### خط لوله CI/CD — اقدامات GitHub
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

## تست
### تست چارچوب ها و راه اندازی
اکوسیستم آزمایش پایتون حول محور `pytest`، استاندارد واقعی برای آزمایش پایتون است.
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

### تست واحد با pytest
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

### تست های Async و تست های یکپارچه سازی
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

## قابلیت همکاری
### تماس C/C++ با ctypes
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

### استفاده از cffi برای Complex C Interop
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

### Cython - پایتون با عملکرد C
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

### Pybind11 - برنامه های افزودنی C++
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

## الگوهای طراحی
### سینگلتون
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

### الگوی کارخانه
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

### الگوی مشاهده گر
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

### الگوی مدیریت زمینه
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

### الگوی استراتژی
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### تکنیک های بهینه سازی
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

### محک زدن
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## استقرار
### بسته بندی و توزیع
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### Dockerfile
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

### استقرار ویژه پلتفرم
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

## اکوسیستم
قدرت پایتون فقط زبان نیست، بلکه اکوسیستمی است که پیرامون آن ساخته شده است.
### هوش مصنوعی و یادگیری ماشینی
| کتابخانه | هدف |
|---------|---------|
| PyTorch | یادگیری عمیق (تحقیق و تولید) |
| TensorFlow / Keras | یادگیری عمیق (محور تولید) |
| scikit-learn | ML کلاسیک (رگرسیون، خوشه بندی، طبقه بندی) |
| ترانسفورماتورهای صورت در آغوش گرفته | مدل های NLP/Vision از پیش آموزش دیده |
| LangChain / LlamaIndex | ساخت برنامه های کاربردی با LLM |
| NumPy | محاسبات عددی (آرایه ها، جبر خطی) |
| پانداها | دستکاری و تجزیه و تحلیل داده ها |
| Matplotlib / Seaborn / Plotly | تجسم داده ها |
### توسعه وب
| چارچوب | سبک | بهترین برای |
|-----------|-------|----------|
| جانگو | تمام پشته، "باتری شامل" | برنامه های وب پیچیده با پنل های مدیریت، ORM، auth |
| FastAPI | مدرن، ناهمگام، نوع محور | API ها و میکروسرویس ها (در حال حاضر سریع ترین رشد را دارند) |
| فلاسک | حداقل، انعطاف پذیر | برنامه های کوچک و نمونه های اولیه |
| Streamlit | مبتنی بر برنامه داده | داشبوردها و دموهای داده در پایتون خالص |
### اتوماسیون و اسکریپت نویسی
| کتابخانه | هدف |
|---------|---------|
| `subprocess`/`os`| مدیریت سیستم |
| `requests`/`httpx`| مشتریان HTTP |
| `BeautifulSoup`/`Scrapy`| خراش دادن وب |
| `Selenium`/`Playwright`| اتوماسیون مرورگر |
| `Celery`| صف های وظیفه توزیع شده |
| `Airflow`| ارکستراسیون گردش کار |
### محاسبات علمی
| کتابخانه | هدف |
|---------|---------|
| NumPy | عملیات آرایه و جبر خطی |
| SciPy | الگوریتم های علمی (بهینه سازی، پردازش سیگنال) |
| Sympy | ریاضیات نمادین |
| نوت بوک ژوپیتر | محیط محاسباتی تعاملی |
| JAX | محاسبات عددی با کارایی بالا (با شتاب GPU) |
---

## چه زمانی از پایتون استفاده کنیم
| سناریو | چرا پایتون | جایگزین بهتر |
|----------|----------|------------------|
| AI/ML/Data Science | اکوسیستم بی بدیل است | — |
| اتوماسیون و اسکریپت | سریعترین نوشتن و اشکال زدایی | Shell/PowerShell برای کارهای ساده sysadmin |
| پشتیبان های وب (API) | FastAPI عالی است | برو یا جاوا برای خدمات بسیار پرتوان |
| نمونه سازی | سریعترین مسیر از ایده تا کد کار | — |
| آموزش و پرورش | مبتدی ترین زبان | — |
| برنامه های دسکتاپ | ممکن است اما غیر معمول | سی شارپ (ویندوز)، سوئیفت (macOS) |
| سیستم های حیاتی عملکرد | اجتناب - خیلی کند | C, C++, Rust |
| برنامه های موبایل | ابزار مناسبی نیست | سوئیفت (iOS)، کاتلین (اندروید) |
| سیستم های تعبیه شده | منابع بسیار سنگین | C، Rust یا MicroPython برای موارد ساده |
---

## نسخه های پایتون
زبان به تکامل خود ادامه می دهد. افزوده های کلیدی اخیر:
| نسخه | سال | ویژگی های قابل توجه |
|---------|------|-----------------|
| 3.10 | 2021 | تطبیق الگوی ساختاری (`match/case`)، پیام های خطای بهتر |
| 3.11 | 2022 | اجرای 10 تا 60 درصد سریعتر، ردیابی بهبود یافته |
| 3.12 | 2023 | رشته‌های f انعطاف‌پذیرتر، بیانیه `type`، افزایش عملکرد |
| 3.13 | 2024 | حالت آزاد تجربی (بدون GIL)، بهبود REPL |
| 3.14 | 2025 | بهبودهای بیشتر بدون GIL، بهبود سیستم نوع |
پایتون 2 در 1 ژانویه 2020 به پایان عمر خود رسید. همه پروژه های جدید باید از Python 3.10 یا بالاتر استفاده کنند.
---

## مرجع سریع: اصطلاحات رایج
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

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین لیست ها و تاپل ها چیست و چه زمانی باید از هر کدام استفاده کنم؟
**A:** لیست ها قابل تغییر هستند (`[]`)، تاپل ها تغییر ناپذیر هستند (`()`). هنگامی که نیاز به افزودن، حذف یا تغییر عناصر دارید از لیست ها استفاده کنید. از تاپل ها برای مجموعه های ثابت داده های ناهمگن، کلیدهای فرهنگ لغت، مقادیر برگردانده تابع یا زمانی که می خواهید علامت دهید "این نباید تغییر کند" استفاده کنید. تاپل ها کمی از نظر حافظه کارآمدتر هستند و می توانند به عنوان کلیدهای تنظیم/دیکت استفاده شوند. لیست ها نمی توانند
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: قفل مترجم جهانی (GIL) چگونه روی کد من تأثیر می‌گذارد، و در مورد آن چه باید بکنم؟
**الف:** GIL از اجرای همزمان بایت کد پایتون توسط چندین رشته جلوگیری می کند و این موضوع باعث می شود تا threading برای کارهای محدود به CPU بی اثر شود. برای کارهای مرتبط با ورودی/خروجی (درخواست‌های شبکه، ورودی/خروجی فایل)،`threading`یا`asyncio`به خوبی کار می‌کنند، زیرا GIL در طول I/O آزاد می‌شود. برای کارهای محدود به CPU، از`multiprocessing`(فرآیندهای مجزا، هر کدام GIL خاص خود را دارند)، یا به پسوندهای C (NumPy، Cython، Numba) که GIL را به صورت داخلی آزاد می کنند، بارگذاری کنید.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: آیا باید از نکات نوع در همه جا استفاده کنم؟ معاوضه های عملی چیست؟
**A:** نکات نوع (`def greet(name: str) -> str:`) اختیاری هستند و در زمان اجرا اجرا نمی شوند. آنها تکمیل خودکار IDE را بهبود می بخشند، اشکالات را از طریق ابزارهای تجزیه و تحلیل استاتیک (mypy) و قصد سند پیدا می کنند. مبادله، پرحرفی بیشتر و یک منحنی یادگیری برای انواع پیشرفته است (`Union`، `Generic`، `Protocol`). توصیه: از نکات نوع برای امضای تابع در هر پروژه بیش از 500 خط استفاده کنید. از آنها در اسکریپت های کوتاه کم استفاده کنید. برای اجرای تدریجی mypy را در CI فعال کنید.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: بهترین روش ها برای مدیریت استثناها در پایتون چیست؟
**A:** استثناهای خاص را به جای`except:`خالی (که`SystemExit`و`KeyboardInterrupt`را نیز می گیرد) بگیرید. از`try/except/else/finally`برای جدا کردن منطق مسیر شاد از مدیریت خطا استفاده کنید. سلسله مراتب استثنایی سفارشی را برای کتابخانه ها تعریف کنید. هرگز از استثناها برای کنترل جریان در کدهای حساس به عملکرد استفاده نکنید - آنها کند هستند. برای ثبت ردیابی کامل، استثنا را با`logging.exception()`ثبت کنید.
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

### Q5: چگونه ژنراتورها حافظه را ذخیره می کنند، و چه زمانی باید از آنها در لیست استفاده کنم؟
**الف:** ژنراتورها به جای ساختن یک لیست کامل در حافظه، مقادیر را به تنبلی تولید می کنند - یک در یک زمان، بنا به تقاضا. برای مجموعه داده‌های بزرگ (میلیون‌ها ردیف، دنباله‌های بی‌نهایت، داده‌های جریانی)، مولدها بدون توجه به اندازه از حافظه ثابت استفاده می‌کنند. هنگامی که یک بار تکرار می کنید و نیازی به نمایه سازی یا`len()`ندارید از ژنراتورها استفاده کنید. زمانی که به دسترسی تصادفی، تکرارهای متعدد یا کوچک بودن مجموعه نیاز دارید، از لیست ها استفاده کنید.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک شمارشگر فرکانس کلمه با رتبه بندی بسازید
**بیان مشکل:** با توجه به یک فایل متنی بزرگ، تعداد دفعات هر کلمه را بشمارید، آنها را بر اساس فرکانس (نزولی) رتبه بندی کنید و N نتایج برتر را برگردانید. عدم حساسیت به حروف کوچک، علائم نگارشی و پردازش کارآمد فایل‌های بیش از حد بزرگ که در حافظه جای نمی‌گیرد.
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) متن را بخوانیم، (2) به کلمات تقسیم کنیم، (3) حروف کوچک را عادی کنیم، (4) علائم نگارشی نواری، (5) تعداد رخدادها، (6) مرتب سازی بر اساس تعداد نزولی، (7) بالای N را برگردانیم. محدودیت "بسیار بزرگ برای جا افتادن در حافظه" به این معنی است که باید خط به خط را با ژنراتورها پردازش کنیم.
** مرحله 2 - شناسایی رویکرد: **
- از`re.finditer`برای استخراج کارآمد کلمات بدون ایجاد لیست های میانی استفاده کنید.
- از`collections.Counter`برای افزایش O(1) در هر کلمه استفاده کنید.
- از`Counter.most_common(n)`استفاده کنید که از یک پشته در داخل استفاده می کند - O(k log n) به جای O(n log n) برای مرتب سازی کامل.
- پردازش خط به خط از طریق ژنراتور برای ثابت نگه داشتن حافظه.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- Memory: فقط Counter dict در حافظه است (یک ورودی برای هر کلمه منحصر به فرد)، نه محتوای فایل. برای متن انگلیسی، ~ 100K کلمه منحصر به فرد ≈ چند مگابایت.
- زمان: O(W) برای اسکن همه کلمات + O(U log N) برای استخراج top-N، که در آن W = کل کلمات، U = کلمات منحصر به فرد.
- موارد لبه: آپوستروف در انقباضات ("نباید") توسط regex حفظ می شود. متن یونیکد به پرچم`re.UNICODE`یا الگوی دیگری نیاز دارد.
### مشکل 2: یک Thread-Safe LRU Cache را پیاده سازی کنید
**بیانیه مشکل:** یک حافظه نهان اخیراً استفاده شده (LRU) از ابتدا بسازید که از نظر نخ ایمن باشد، از عملیات get و put O(1) پشتیبانی کند، و به طور خودکار مواردی که اخیراً استفاده شده است را در صورت افزایش ظرفیت خارج می کند.
** مرحله 1 - مشکل را درک کنید:**
یک حافظه پنهان LRU به موارد زیر نیاز دارد: (1) جستجوی سریع توسط کلید → نقشه هش، (2) مرتب سازی سریع بر اساس تازگی → لیست پیوندی دوگانه، (3) ایمنی رشته → قفل کردن. در `get(key)`: مورد را به جلو منتقل کنید. در `put(key, val)`: درج در جلو. اگر ظرفیت بیش از حد است، از پشت خارج کنید.
** مرحله 2 - شناسایی رویکرد: **
-`dict`پایتون نظم درج (3.7+) را حفظ می‌کند، بنابراین می‌توانیم از یک رویکرد دستوری مرتب استفاده کنیم: حذف و دوباره درج برای حرکت به پایان.
- برای ایمنی نخ، از`threading.Lock`برای حذف متقابل استفاده کنید.
- جایگزین: از`collections.OrderedDict`که دارای`move_to_end()`است استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- پیچیدگی زمانی: O(1) برای`get`و`put`—`OrderedDict.move_to_end()`و`popitem()`O(1) هستند.
- ایمنی رزوه:`Lock`اتمی بودن را تضمین می کند. برای توان عملیاتی بالاتر،`threading.RLock`یا الگوی قفل خواندن-نوشتن را در نظر بگیرید، اما برای بیشتر موارد استفاده، یک قفل ساده کافی است.
- نکته تولید: برای کدهای تک رشته ای،`functools.lru_cache`ساده تر است و برای عملکرد بهتر در C پیاده سازی شده است.
### مسئله 3: یک عبارت ریاضی را تجزیه و ارزیابی کنید
**بیانیه مشکل:** تجزیه کننده ای بنویسید که رشته ای مانند`"3 + 4 * 2 / (1 - 5)"`را بگیرد و با رعایت اولویت عملگر و پرانتز آن را به درستی ارزیابی کند.
** مرحله 1 - مشکل را درک کنید:**
این امر مستلزم: (1) توکن کردن رشته ورودی به اعداد، عملگرها و پرانتزها، (2) تجزیه با اولویت صحیح (`*` و`/`قبل از`+`و `-`)، (3) مدیریت پرانتزهای تو در تو. یک ارزیابی ساده لوحانه از چپ به راست نتایج اشتباهی به همراه خواهد داشت.
** مرحله 2 - شناسایی رویکرد: **
راه حل کلاسیک **الگوریتم حیاط شنتینگ** (Dijkstra) است که infix را به postfix تبدیل می کند (Reverse Polish Notation)، سپس پسوند را ارزیابی می کند. روش دیگر، از یک تجزیه کننده نزولی بازگشتی استفاده کنید. به طور خاص برای پایتون، ما همچنین می توانیم از`ast.literal_eval`برای ارزیابی ایمن استفاده کنیم - اما بیایید آن را به درستی پیاده سازی کنیم.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- صحت:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. درست است.
- زمان: O(N) برای نشانه گذاری، O(N) برای شانتینگ یارد، O(N) برای ارزیابی - O(N) کلی.
- موارد لبه برای رسیدگی: اعداد منفی (قبل از`0`قبل از`-`یکنواخت)، تقسیم بر صفر (اضافه کردن رسیدگی به خطا)، ورودی نامعتبر (توکن‌های اعتبارسنجی).
- جایگزین پایتونیک:`ast.parse(expr, mode='eval')`با بازدیدکننده گره سفارشی برای ارزیابی ایمن بدون `eval()`.
### مشکل 4: یک داشبورد CLI با به‌روزرسانی‌های بی‌درنگ داده بسازید
**بیانیه مشکل:** داشبورد مبتنی بر ترمینال ایجاد کنید که معیارهای سیستم (CPU، حافظه، دیسک) را در زمان واقعی به‌روزرسانی می‌کند، با آستانه‌های رنگی و طرح‌بندی پاسخگو.
** مرحله 1 - مشکل را درک کنید:**
ما به موارد زیر نیاز داریم: (1) مجموعه متریک سیستم دوره ای، (2) رندر پایانه با کنترل مکان نما، (3) خروجی رنگ بر اساس آستانه، (4) ورودی صفحه کلید غیر مسدود کننده برای خروج. این یک الگوی تولیدکننده-مصرف کننده با یک حلقه رندر است.
** مرحله 2 - شناسایی رویکرد: **
- از`psutil`برای معیارهای سیستم متقابل پلتفرم استفاده کنید.
- از کدهای فرار ANSI برای موقعیت یابی مکان نما و رنگ ها استفاده کنید (یا از کتابخانه`rich`برای یک API سطح بالاتر).
- از`time.sleep`برای فاصله به روز رسانی استفاده کنید.
- ساختار به عنوان: جمع آوری داده ها → قالب بندی → خط لوله رندر.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
-`cpu_percent(interval=0.5)`برای اندازه گیری 0.5 ثانیه بلوک می کند - این رویکرد صحیح است (حالت غیر مسدود کننده در اولین تماس 0٪ می دهد).
- کدهای ANSI روی ترمینال مدرن ویندوز و تمام پایانه های یونیکس کار می کنند. برای cmd ویندوز قدیمی،`os.system('color')`را اضافه کنید یا از`colorama`استفاده کنید.
- ارتقای تولید: از کتابخانه`rich`(`rich.live`) برای رندر بدون سوسو، چیدمان خودکار و سازگاری با پلتفرم استفاده کنید.
- توسعه پذیری: هر متریک یک تابع مستقل است که اضافه کردن دمای GPU، تعداد فرآیند یا اتصالات شبکه را آسان می کند.
---

## خلاصه
ترکیبی از خوانایی، تطبیق پذیری و عمق اکوسیستم پایتون، آن را به پرکاربردترین زبان برنامه نویسی در جهان تبدیل کرده است. این انتخاب پیش‌فرض برای AI/ML، یک گزینه قوی برای پشتیبان‌های وب و اتوماسیون، و یک زبان آموزشی عالی است. نقاط ضعف اصلی آن - سرعت اجرا و پشتیبانی تلفن همراه / جاسازی شده - به خوبی درک شده است و راه‌حل‌هایی را ایجاد کرده است. برای اکثر پروژه ها، پایتون یک نقطه شروع معقول است.