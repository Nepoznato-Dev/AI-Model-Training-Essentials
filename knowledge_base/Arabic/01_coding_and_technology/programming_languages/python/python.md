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
#بايثون
Python هي لغة برمجة عالية المستوى ومفسرة للأغراض العامة أنشأها جويدو فان روسوم وتم إصدارها لأول مرة في عام 1991. وهي تعطي الأولوية لقراءة التعليمات البرمجية من خلال مسافة بادئة كبيرة وبناء جملة واضح يُقرأ بالقرب من اللغة الإنجليزية البسيطة. تتم كتابة لغة بايثون ديناميكيًا، ويتم تجميع البيانات المهملة فيها، وتدعم نماذج برمجة متعددة بما في ذلك البرمجة الإجرائية والموجهة للكائنات والبرمجة الوظيفية.
اليوم، بايثون هي اللغة المهيمنة في الذكاء الاصطناعي/التعلم الآلي، وعلوم البيانات، والحوسبة العلمية، والأتمتة - في حين تظل واحدة من أفضل اللغات للمبتدئين. هذه الهوية المزدوجة (بسيطة بما يكفي للنص الأول، وقوية بما يكفي لتدريب نماذج لغوية كبيرة) هي ما يميزها.
---

## لماذا تعتبر لغة بايثون مهمة؟
- **سهولة القراءة حسب التصميم**: لا توجد فواصل منقوطة، ولا توجد أقواس - المسافة البادئة تحدد النطاق. يقرأ الكود مثل الكود الكاذب.
- **نظام بيئي ضخم**: تستضيف PyPI أكثر من 500000 حزمة تغطي كل مجال تقريبًا.
- **لغة الذكاء الاصطناعي**: PyTorch، وTensorFlow، وscikit-learn، وHugging Face، وLangChain — مجموعة الذكاء الاصطناعي/تعلم الآلة بأكملها تعتمد على لغة Python أولاً.
- **لغة الغراء**: قم بتوصيل محرك C++ بواجهة برمجة تطبيقات الويب إلى قاعدة البيانات في بضعة أسطر فقط.
- **متعدد المنصات**: يعمل على أنظمة Windows وmacOS وLinux والأنظمة المدمجة دون تعديل.
- **المجتمع**: أكبر مجتمع برمجة وأكثره نشاطًا في العالم.
##المقايضات
بايثون ليست مثالية. يساعدك فهم حدوده على تحديد الوقت المناسب للوصول إلى شيء آخر:
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **سرعة التنفيذ** | أبطأ بمقدار 10–100 مرة من لغة C للمهام المرتبطة بوحدة المعالجة المركزية | استخدم NumPy/PyTorch (C أسفل الغطاء)، أو Cython/Numba للحلقات الساخنة |
| **GIL (قفل المترجم العالمي)** | يمنع التوازي الحقيقي متعدد الخيوط للعمل المرتبط بوحدة المعالجة المركزية | استخدم`multiprocessing`أو`asyncio`أو قوائم انتظار المهام مثل Celery |
| **تطوير الهاتف المحمول** | غير مناسب لتطبيقات iOS/Android | استخدم Swift/Kotlin للإصدار الأصلي، أو Flutter/React Native للأنظمة الأساسية المشتركة |
| **الأنظمة المدمجة** | ثقيل جدًا بالنسبة لوحدات التحكم الدقيقة | استخدم MicroPython (متغير خفيف الوزن) أو قم بالتبديل إلى C/Rust |
| **استخدام الذاكرة** | مساحة ذاكرة أعلى من اللغات المترجمة | مقبول لمعظم التطبيقات؛ استخدام المولدات للبيانات الكبيرة |
---

## أساسيات بناء الجملة
### المتغيرات والأنواع
تستخدم لغة Python الكتابة الديناميكية — لا تُعلن عن الأنواع المتغيرة، ولكن يمكنك إضافة تلميحات للنوع من أجل الوضوح ودعم الأدوات.
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

### التحكم في التدفق
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

### الوظائف
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

### البرمجة الشيئية
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

### معالجة الأخطاء
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة مع وحدة `typing`
توفر وحدة`typing`الخاصة بـ Python دعمًا عامًا للنوع لإنشاء مكونات قابلة لإعادة الاستخدام وآمنة للنوع. تتيح لك الأدوية العامة كتابة وظائف وفئات تعمل مع أي نوع مع الحفاظ على معلومات النوع للتحليل الثابت.
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

### الديكور والبرمجة الوصفية
تعد أدوات الديكور إحدى أقوى ميزات Python، فهي تتيح لك تعديل أو توسيع سلوك الوظائف والفئات دون تغيير كود المصدر الخاص بها.
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

### مطابقة الأنماط الهيكلية (Python 3.10+)
يوفر بيان`match/case`الخاص بـ Python مطابقة أنماط قوية مع أنماط التدمير والحراس والأنماط المتداخلة.
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

### عمليات الإغلاق والوظائف ذات الترتيب الأعلى والتكرارات
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

### التحميل الزائد على المشغل
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

### التسلسلات الهرمية للاستثناءات المخصصة
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

## الميزات الرئيسية في العمق
### المكتبة القياسية ("البطاريات متضمنة")
تأتي بايثون مع مكتبة قياسية واسعة النطاق. بعض الوحدات الأكثر استخدامًا:
| الوحدة | الغرض | استخدم المثال |
|--------|---------|-------------|
| `os`/`pathlib`| عمليات نظام الملفات | `Path("data/output.csv").exists()`|
| `json`| ترميز/فك تشفير JSON | `json.loads(response_text)`|
| `datetime`| التعامل مع التاريخ والوقت | `datetime.now(timezone.utc)`|
| `collections`| حاويات متخصصة | `Counter(words)`,`defaultdict(list)`|
| `itertools`| كتل بناء التكرار | `combinations(items, 2)`|
| `functools`| الأدوات الوظيفية | `lru_cache`,`partial`,`reduce`|
| `re`| التعابير العادية | `re.findall(r"\d+", text)`|
| `subprocess`| تشغيل الأوامر الخارجية | `subprocess.run(["ls", "-la"])`|
| `logging`| تسجيل التطبيق | `logging.basicConfig(level=logging.INFO)`|
| `typing`| دعم تلميح النوع | `Optional[str]`,`Union[int, float]`|
| `http.server`| خادم HTTP بسيط | `python -m http.server 8000`|
| `threading`/`asyncio`| التزامن | الإدخال/الإخراج غير المتزامن لكاشطات الويب |
### البيئات الافتراضية وإدارة الحزم
يجب أن يستخدم كل مشروع بايثون بيئة افتراضية لعزل التبعيات:
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

تستخدم مشاريع Python الحديثة`pyproject.toml`بشكل متزايد مع أدوات مثل`uv`أو`poetry`أو`hatch`لإدارة التبعية، لتحل محل نهج`setup.py`/`requirements.txt`الأقدم.
### البرمجة غير المتزامنة
يتيح`asyncio`الخاص بـ Python الإدخال/الإخراج المتزامن بدون سلاسل رسائل - وهو ضروري لبرامج استخراج الويب وخوادم الدردشة وعملاء واجهة برمجة التطبيقات:
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

## التزامن والتوازي
تقدم Python العديد من نماذج التزامن، كل منها يناسب أحمال العمل المختلفة. يمنع GIL (Global Interpreter Lock) في CPython التوازي الحقيقي لوحدة المعالجة المركزية مع الخيوط، لذلك يعتمد النموذج الصحيح على ما إذا كان عبء العمل الخاص بك مرتبطًا بالإدخال/الإخراج أو مرتبطًا بوحدة المعالجة المركزية.
### الخيوط (المهام المرتبطة بالإدخال/الإخراج)
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

### المعالجة المتعددة (المهام المرتبطة بوحدة المعالجة المركزية)
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

### العناصر الداخلية غير المتزامنة
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

## تكوين المشروع ونظام البناء
### هيكل دليل المشروع
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

### تكوين التكوين — `pyproject.toml`
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

### إدارة التبعية باستخدام الأدوات الحديثة
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

### جودة الفحص والرمز
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### خط أنابيب CI/CD — إجراءات GitHub
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

## الاختبار
### أطر الاختبار والإعداد
يتمحور النظام البيئي لاختبار بايثون حول `pytest`، وهو المعيار الفعلي لاختبار بايثون.
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

### اختبارات الوحدة باستخدام pytest
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

### اختبارات المزامنة واختبارات التكامل
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

## إمكانية التشغيل البيني
### استدعاء C/C++ باستخدام ctypes
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

### استخدام cffi لمزيد من التشغيل المتداخل C المعقد
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

### Cython — لغة Python مع أداء لغة C
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

### Pybind11 — ملحقات C++
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

## أنماط التصميم
### سينجلتون
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

### نمط المصنع
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

### نمط المراقب
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

### نمط إدارة السياق
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

### نمط الاستراتيجية
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

## الأداء والتحسين
### أدوات التنميط
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

### تقنيات التحسين
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

### المقارنة المرجعية
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## النشر
### التعبئة والتغليف والتوزيع
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### ملف دوكر
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

### النشر الخاص بالمنصة
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

## النظام البيئي
لا تكمن قوة بايثون في اللغة فحسب، بل في النظام البيئي المبني حولها.
### الذكاء الاصطناعي والتعلم الآلي
| مكتبة | الغرض |
|---------|--------|
| باي تورش | التعلم العميق (البحث والإنتاج) |
| TensorFlow / كيراس | التعلم العميق (يركز على الإنتاج) |
| scikit-تعلم | تعلم الآلة الكلاسيكي (الانحدار، التجميع، التصنيف) |
| معانقة محولات الوجه | نماذج البرمجة اللغوية العصبية/الرؤية المدربة مسبقًا |
| لانج تشين / لاما إندكس | بناء التطبيقات باستخدام LLMs |
| نومبي | الحوسبة العددية (المصفوفات، الجبر الخطي) |
| الباندا | معالجة البيانات وتحليلها |
| ماتبلوتليب / سيبورن / بلوتلي | تصور البيانات |
### تطوير الويب
| الإطار | النمط | الأفضل لـ |
|-----------|------|----------|
| جانجو | مجموعة كاملة، "البطاريات متضمنة" | تطبيقات الويب المعقدة مع لوحات الإدارة، ORM، المصادقة |
| فاستابي | حديث، غير متزامن، يعتمد على النوع | واجهات برمجة التطبيقات والخدمات الصغيرة (الأسرع نموًا حاليًا) |
| قارورة | الحد الأدنى والمرن | تطبيقات صغيرة ونماذج أولية |
| ستريمليت | يركز تطبيق البيانات | لوحات المعلومات والعروض التوضيحية للبيانات بلغة Python النقية |
### الأتمتة والبرمجة
| مكتبة | الغرض |
|---------|--------|
| `subprocess`/`os`| إدارة النظام |
| `requests`/`httpx`| عملاء HTTP |
| `BeautifulSoup`/`Scrapy`| تجريف الويب |
| `Selenium`/`Playwright`| أتمتة المتصفح |
| `Celery`| قوائم انتظار المهام الموزعة |
| `Airflow`| تنسيق سير العمل |
### الحوسبة العلمية
| مكتبة | الغرض |
|---------|--------|
| نومبي | عمليات المصفوفات والجبر الخطي |
| سيبي | الخوارزميات العلمية (التحسين، معالجة الإشارات) |
| سيمبي | الرياضيات الرمزية |
| دفتر جوبيتر | بيئة حاسوبية تفاعلية |
| جاكس | حوسبة رقمية عالية الأداء (تسريع GPU) |
---

## متى تستخدم بايثون
| السيناريو | لماذا بايثون | البديل الأفضل |
|----------|---------|------------------|
| الذكاء الاصطناعي/التعلم الآلي/علوم البيانات | النظام البيئي لا مثيل له | — |
| الأتمتة والبرمجة النصية | الأسرع في الكتابة والتصحيح | Shell/PowerShell لمهام مسؤول النظام البسيطة |
| واجهات الويب الخلفية (واجهات برمجة التطبيقات) | FastAPI ممتاز | Go أو Java لخدمات عالية الإنتاجية للغاية |
| النماذج الأولية | أسرع مسار من الفكرة إلى كود العمل | — |
| تعليم | اللغة الأكثر ملائمة للمبتدئين | — |
| تطبيقات سطح المكتب | ممكن ولكن غير شائع | C# (ويندوز)، سويفت (ماك) |
| أنظمة الأداء الحرجة | تجنب — بطيء جدًا | C، C++، الصدأ |
| تطبيقات الجوال | ليست الأداة الصحيحة | سويفت (iOS)، كوتلين (أندرويد) |
| الأنظمة المدمجة | كثيفة الموارد للغاية | C أو Rust أو MicroPython للحالات البسيطة |
---

## إصدارات بايثون
تستمر اللغة في التطور. الإضافات الأخيرة الرئيسية:
| النسخة | سنة | الميزات البارزة |
|---------|------|-----------------|
| 3.10 | 2021 | مطابقة النمط الهيكلي (`match/case`)، رسائل خطأ أفضل |
| 3.11 | 2022 | تنفيذ أسرع بنسبة 10–60%، وتتبعات محسنة |
| 3.12 | 2023 | سلاسل f أكثر مرونة، بيان `type`، مكاسب الأداء |
| 3.13 | 2024 | وضع تجريبي حر (بدون GIL)، تحسين REPL |
| 3.14 | 2025 | مزيد من التحسينات بدون GIL، اكتب تحسينات النظام |
وصل Python 2 إلى نهاية العمر الافتراضي في 1 يناير 2020. ويجب أن تستخدم جميع المشاريع الجديدة Python 3.10 أو الأحدث.
---

## مرجع سريع: التعابير الشائعة
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

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين القوائم والصفوف، ومتى يجب أن أستخدم كل منهما؟
**أ:** القوائم قابلة للتغيير (`[]`)، والصفوف غير قابلة للتغيير (`()`). استخدم القوائم عندما تحتاج إلى إضافة عناصر أو إزالتها أو تغييرها. استخدم الصفوف للمجموعات الثابتة من البيانات غير المتجانسة، أو مفاتيح القاموس، أو قيم إرجاع الوظائف، أو عندما تريد الإشارة إلى "هذا لا ينبغي أن يتغير". تعد Tuples أكثر كفاءة في الذاكرة قليلاً ويمكن استخدامها كمفاتيح ضبط/إملاء؛ لا يمكن للقوائم.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### السؤال الثاني: كيف يؤثر قفل المترجم العالمي (GIL) على الكود الخاص بي، وماذا يجب أن أفعل حيال ذلك؟
**أ:** يمنع GIL سلاسل رسائل متعددة من تنفيذ كود Python الثانوي في وقت واحد، مما يجعل الترابط غير فعال للعمل المرتبط بوحدة المعالجة المركزية. بالنسبة للمهام المرتبطة بالإدخال/الإخراج (طلبات الشبكة، إدخال/إخراج الملفات)، تعمل`threading`أو`asyncio`بشكل جيد لأنه يتم تحرير GIL أثناء الإدخال/الإخراج. بالنسبة للمهام المرتبطة بوحدة المعالجة المركزية، استخدم`multiprocessing`(عمليات منفصلة، ​​كل منها لها GIL الخاص بها)، أو قم بإلغاء التحميل إلى امتدادات C (NumPy، Cython، Numba) التي تحرر GIL داخليًا.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### س3: هل يجب أن أستخدم تلميحات الكتابة في كل مكان؟ ما هي المقايضات العملية؟
**أ:** تعتبر تلميحات الكتابة (`def greet(name: str) -> str:`) اختيارية ولا يتم فرضها في وقت التشغيل. تعمل على تحسين الإكمال التلقائي لـ IDE، واكتشاف الأخطاء عبر أدوات التحليل الثابت (mypy)، ونية المستند. المقايضة هي الإسهاب الإضافي ومنحنى التعلم للأنواع المتقدمة (`Union`,`Generic`,`Protocol`). توصية: استخدم تلميحات الكتابة لتوقيعات الوظائف في أي مشروع يزيد عن 500 سطر تقريبًا؛ استخدمها باعتدال في النصوص القصيرة. تمكين mypy في CI للتنفيذ التدريجي.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### السؤال الرابع: ما هي أفضل الممارسات للتعامل مع الاستثناءات في بايثون؟
**أ:** احصل على استثناءات محددة بدلاً من`except:`العارية (التي تلتقط`SystemExit`و`KeyboardInterrupt` أيضًا). استخدم`try/except/else/finally`لفصل منطق المسار السعيد عن معالجة الأخطاء. تحديد التسلسلات الهرمية للاستثناءات المخصصة للمكتبات. لا تستخدم أبدًا استثناءات للتحكم في التدفق في التعليمات البرمجية الحساسة للأداء - فهي بطيئة. قم بتسجيل الاستثناء باستخدام`logging.exception()`لالتقاط التتبع الكامل.
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

### س5: كيف تقوم المولدات بحفظ الذاكرة، ومتى يجب استخدامها في القوائم؟
**ج:** تنتج المولدات القيم بتكاسل — واحدة تلو الأخرى، حسب الطلب — بدلاً من إنشاء قائمة كاملة في الذاكرة. بالنسبة لمجموعات البيانات الكبيرة (ملايين الصفوف، والتسلسلات اللانهائية، والبيانات المتدفقة)، تستخدم المولدات ذاكرة ثابتة بغض النظر عن الحجم. استخدم المولدات عندما تتكرر مرة واحدة ولا تحتاج إلى فهرسة أو`len()`. استخدم القوائم عندما تحتاج إلى وصول عشوائي، أو تكرارات متعددة، أو عندما تكون المجموعة صغيرة.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: إنشاء عداد تكرار الكلمات مع التصنيف
**بيان المشكلة:** في حالة وجود ملف نصي كبير، قم بحساب تكرار كل كلمة، ثم قم بترتيبها حسب التكرار (تنازلي)، وقم بإرجاع أعلى النتائج N. تعامل مع عدم حساسية حالة الأحرف وعلامات الترقيم ومعالجة الملفات الكبيرة جدًا بحيث لا يمكن احتواؤها في الذاكرة بكفاءة.
**الخطوة الأولى — فهم المشكلة:**
نحن بحاجة إلى: (1) قراءة النص، (2) تقسيمه إلى كلمات، (3) تطبيع حالة الأحرف، (4) علامات الترقيم، (5) عد التكرارات، (6) الفرز حسب العدد تنازليًا، (7) العودة إلى أعلى N. القيد "كبير جدًا بحيث لا يتناسب مع الذاكرة" يعني أنه يجب علينا معالجة سطرًا تلو الآخر باستخدام المولدات.
**الخطوة الثانية — تحديد النهج:**
- استخدم`re.finditer`لاستخراج الكلمات بكفاءة دون إنشاء قوائم وسيطة.
- استخدم`collections.Counter`لزيادة O(1) لكل كلمة.
- استخدم`Counter.most_common(n)`الذي يستخدم الكومة داخليًا - O(k log n) بدلاً من O(n log n) للفرز الكامل.
- معالجة سطرًا تلو الآخر عبر المولد للحفاظ على ثبات الذاكرة.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- الذاكرة: يوجد فقط إملاء العداد في الذاكرة (إدخال واحد لكل كلمة فريدة)، وليس محتوى الملف. بالنسبة للنص الإنجليزي، ~100 ألف كلمة فريدة ≈ بضع ميغابايت.
- الوقت: O(W) لمسح جميع الكلمات + O(U log N) لاستخراج أعلى N، حيث W = إجمالي الكلمات، U = كلمات فريدة.
- حالات الحافة: يتم الحفاظ على الفواصل العليا في الاختصارات ("لا تفعل") بواسطة التعبير العادي. سيحتاج نص Unicode إلى علامة`re.UNICODE`أو نمط مختلف.
### المشكلة الثانية: تنفيذ ذاكرة تخزين مؤقت LRU آمنة لمؤشر الترابط
**بيان المشكلة:** قم بإنشاء ذاكرة تخزين مؤقت أقل استخدامًا (LRU) من البداية تكون آمنة لمؤشر الترابط، وتدعم عمليات الحصول على O(1) ووضعها، وتقوم تلقائيًا بطرد العنصر الأقل استخدامًا مؤخرًا عند تجاوز السعة.
**الخطوة الأولى — فهم المشكلة:**
تحتاج ذاكرة التخزين المؤقت LRU إلى: (1) بحث سريع عن طريق المفتاح ← خريطة التجزئة، (2) ترتيب سريع حسب الحداثة ← قائمة مرتبطة بشكل مزدوج، (3) أمان الخيط ← القفل. على `get(key)`: انقل العنصر إلى الأمام. في `put(key, val)`: أدخل في المقدمة؛ إذا كان أكثر من السعة، قم بإزالته من الخلف.
**الخطوة الثانية — تحديد النهج:**
- يحتفظ`dict`في Python بترتيب الإدراج (3.7+)، لذلك يمكننا استخدام أسلوب الإملاء المرتب: الحذف وإعادة الإدراج للانتقال إلى النهاية.
- لسلامة الخيط، استخدم`threading.Lock`للاستبعاد المتبادل.
- البديل: استخدم`collections.OrderedDict`الذي يحتوي على`move_to_end()`.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- التعقيد الزمني: O(1) لكل من`get`و`put` -`OrderedDict.move_to_end()`و`popitem()` هما O(1).
- سلامة الخيط: يضمن`Lock`الذرية. للحصول على إنتاجية أعلى، فكر في`threading.RLock`أو نمط قفل القراءة والكتابة، ولكن بالنسبة لمعظم حالات الاستخدام، يكفي القفل البسيط.
- ملاحظة الإنتاج: بالنسبة للكود المفرد، يكون`functools.lru_cache`أبسط ويتم تنفيذه في لغة C للحصول على أداء أفضل.
### المشكلة الثالثة: تحليل وتقييم التعبير الرياضي
**بيان المشكلة:** اكتب محللًا يأخذ سلسلة مثل`"3 + 4 * 2 / (1 - 5)"`ويقوم بتقييمها بشكل صحيح مع مراعاة أسبقية عامل التشغيل والأقواس.
**الخطوة الأولى — فهم المشكلة:**
يتطلب ذلك: (1) ترميز سلسلة الإدخال إلى أرقام وعوامل تشغيل وأقواس، (2) التحليل بالأسبقية الصحيحة (`*`و`/` قبل`+`و`-`)، (3) التعامل مع الأقواس المتداخلة. إن التقييم الساذج من اليسار إلى اليمين من شأنه أن يعطي نتائج خاطئة.
**الخطوة الثانية — تحديد النهج:**
الحل الكلاسيكي هو **خوارزمية التحويلة** (Dijkstra) التي تحول infix إلى postfix (Reverse Polish Notation)، ثم تقوم بتقييم postfix. بدلا من ذلك، استخدم محلل النسب العودي. بالنسبة لـ Python على وجه التحديد، يمكننا أيضًا استخدام`ast.literal_eval`للتقييم الآمن - ولكن دعونا ننفذه بشكل صحيح.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- الصحة:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. صحيح.
- الوقت: O(N) للترميز، O(N) لساحة النقل، O(N) للتقييم - O(N) الإجمالي.
- حالات الحافة التي يجب التعامل معها: الأرقام السالبة (إلحاق`0`قبل`-`الأحادي)، القسمة على صفر (إضافة معالجة الأخطاء)، الإدخال غير الصالح (التحقق من صحة الرموز).
- البديل البايثوني:`ast.parse(expr, mode='eval')`مع زائر عقدة مخصص للتقييم الآمن بدون `eval()`.
### المشكلة الرابعة: إنشاء لوحة تحكم واجهة سطر الأوامر (CLI) مع تحديثات البيانات في الوقت الفعلي
**بيان المشكلة:** قم بإنشاء لوحة معلومات قائمة على المحطة الطرفية تعرض تحديث مقاييس النظام (وحدة المعالجة المركزية والذاكرة والقرص) في الوقت الفعلي، مع حدود مرمزة بالألوان وتخطيط سريع الاستجابة.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) جمع قياسات النظام بشكل دوري، (2) العرض الطرفي مع التحكم في المؤشر، (3) إخراج الألوان استنادًا إلى الحدود، (4) إدخال لوحة المفاتيح غير المحظور لإنهاء العمل. هذا هو نمط المنتج والمستهلك مع حلقة العرض.
**الخطوة الثانية — تحديد النهج:**
- استخدم`psutil`لمقاييس النظام عبر الأنظمة الأساسية.
- استخدم أكواد الهروب ANSI لتحديد موضع المؤشر وألوانه (أو مكتبة`rich`لواجهة برمجة التطبيقات ذات المستوى الأعلى).
- استخدم`time.sleep`للفاصل الزمني للتحديث.
- الهيكل على النحو التالي: جمع البيانات ← التنسيق ← تقديم خط الأنابيب.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- كتل`cpu_percent(interval=0.5)`لمدة 0.5 ثانية للقياس - وهذا هو النهج الصحيح (يعطي الوضع غير المحظور 0% عند الاتصال الأول).
- تعمل رموز ANSI على Windows Terminal الحديث وجميع محطات Unix. بالنسبة إلى Windows cmd القديم، أضف`os.system('color')`أو استخدم`colorama`.
- ترقية الإنتاج: استخدم مكتبة`rich`(`rich.live`) للعرض الخالي من الوميض والتخطيط التلقائي والتوافق عبر الأنظمة الأساسية.
- القابلية للتوسعة: كل مقياس عبارة عن وظيفة مستقلة، مما يجعل من السهل إضافة درجة حرارة وحدة معالجة الرسومات، أو عدد العمليات، أو اتصالات الشبكة.
---

## ملخص
إن مزيج بايثون من سهولة القراءة والتنوع وعمق النظام البيئي يجعلها لغة البرمجة الأكثر استخدامًا في العالم. إنه الخيار الافتراضي لـ AI/ML، وهو خيار قوي لواجهات الويب الخلفية والأتمتة، ولغة تدريس ممتازة. إن نقاط ضعفه الرئيسية - سرعة التنفيذ والدعم المحمول/المضمن - مفهومة جيدًا وقد تم إنشاء حلول بديلة لها. بالنسبة لمعظم المشاريع، تعتبر بايثون نقطة بداية معقولة.