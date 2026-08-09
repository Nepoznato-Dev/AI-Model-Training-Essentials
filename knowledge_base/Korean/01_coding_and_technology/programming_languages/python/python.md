---
# Metadata
title: "Python"
description: "Comprehensive reference for the Python programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# 파이썬
Python은 Guido van Rossum이 만들고 1991년에 처음 출시된 고급 해석형 범용 프로그래밍 언어입니다. Python은 상당한 들여쓰기와 일반 영어에 가까운 깔끔한 구문을 통해 코드 가독성을 우선시합니다. Python은 동적으로 유형이 지정되고 가비지 수집되며 절차적 프로그래밍, 객체 지향 프로그래밍, 함수형 프로그래밍을 포함한 여러 프로그래밍 패러다임을 지원합니다.
오늘날 Python은 AI/ML, 데이터 과학, 과학 컴퓨팅 및 자동화 분야에서 지배적인 언어이면서 동시에 초보자에게도 최고의 언어 중 하나입니다. 이러한 이중 정체성(첫 번째 스크립트를 만들기에는 충분히 단순하고 대규모 언어 모델을 훈련할 만큼 강력함)이 이를 차별화하는 요소입니다.
---

## 파이썬이 중요한 이유
- **가독성을 고려한 디자인**: 세미콜론이나 중괄호가 없습니다. 들여쓰기가 범위를 정의합니다. 코드는 의사코드처럼 읽혀집니다.
- **대규모 생태계**: PyPI는 거의 모든 도메인을 포괄하는 500,000개 이상의 패키지를 호스팅합니다.
- **AI 언어**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — 전체 AI/ML 스택은 Python 우선입니다.
- **글루 언어**: 단 몇 줄만으로 C++ 엔진을 웹 API와 데이터베이스에 연결합니다.
- **크로스 플랫폼**: 수정 없이 Windows, macOS, Linux 및 임베디드 시스템에서 실행됩니다.
- **커뮤니티**: 세계에서 가장 크고 활동적인 프로그래밍 커뮤니티입니다.
## 절충안
파이썬은 완벽하지 않습니다. 한계를 이해하면 언제 다른 것을 찾아야 할지 결정하는 데 도움이 됩니다.
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **실행 속도** | CPU 바인딩 작업의 경우 C보다 10~100배 느림 | NumPy/PyTorch(내부적으로는 C) 또는 핫 루프용 Cython/Numba 사용 |
| **GIL(전역 통역사 잠금)** | CPU 바인딩 작업에 대한 진정한 다중 스레드 병렬 처리 방지 |`multiprocessing`,`asyncio`또는 Celery |
| **모바일 개발** | iOS/Android 앱에는 적합하지 않음 | 네이티브에는 Swift/Kotlin을 사용하고 크로스 플랫폼에는 Flutter/React Native를 사용하세요.
| **임베디드 시스템** | 마이크로컨트롤러에 비해 너무 무거움 | MicroPython(경량 변형)을 사용하거나 C/Rust |
| **메모리 사용량** | 컴파일된 언어보다 더 높은 메모리 공간 | 대부분의 응용 분야에 적합합니다. 대용량 데이터 생성기 사용 |
---

## 구문 기본 사항
### 변수 및 유형
Python은 동적 유형 지정을 사용합니다. 변수 유형을 선언하지 않지만 명확성과 도구 지원을 위해 유형 힌트를 추가할 수 있습니다.
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

### 제어 흐름
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

### 기능
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

### 객체 지향 프로그래밍
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

### 오류 처리
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

## 고급 구문 및 패턴
###`typing`모듈을 사용한 제네릭
Python의`typing`모듈은 재사용 가능하고 유형이 안전한 구성 요소를 구축하기 위한 일반 유형 지원을 제공합니다. 제네릭을 사용하면 정적 분석을 위한 유형 정보를 유지하면서 모든 유형에서 작동하는 함수와 클래스를 작성할 수 있습니다.
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

### 데코레이터와 메타프로그래밍
데코레이터는 Python의 가장 강력한 기능 중 하나입니다. 데코레이터를 사용하면 소스 코드를 변경하지 않고도 함수와 클래스의 동작을 수정하거나 확장할 수 있습니다.
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

### 구조적 패턴 일치(Python 3.10+)
Python의`match/case`문은 구조 분해, 가드 및 중첩 패턴과의 강력한 패턴 일치를 제공합니다.
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

### 클로저, 고차 함수 및 반복자
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

### 연산자 오버로딩
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

### 사용자 정의 예외 계층
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

## 심층 주요 기능
### 표준 라이브러리("배터리 포함")
Python은 광범위한 표준 라이브러리와 함께 제공됩니다. 가장 많이 사용되는 모듈 중 일부는 다음과 같습니다.
| 모듈 | 목적 | 사용예 |
|---------|---------|------------|
|  __보호_0__ / __보호_1__ | 파일 시스템 작업 |  __보호됨_2__ |
|  __보호됨_3__ | JSON 인코딩/디코딩 |  __보호됨_4__ |
|  __보호됨_5__ | 날짜 및 시간 처리 |  __보호_6__ |
|  __보호_7__ | 전문용기 |  __보호_8__ , __보호_9__ |
|  __보호됨_10__ | 반복자 빌딩 블록 |  __보호됨_11__ |
|  __보호됨_12__ | 기능 도구 | `lru_cache`,`partial`,`reduce`|
|  __보호됨_16__ | 정규식 |  __보호됨_17__ |
|  __보호됨_18__ | 외부 명령 실행 |  __보호됨_19__ |
|  __보호됨_20__ | 애플리케이션 로깅 |  __보호됨_21__ |
|  __보호됨_22__ | 유형 힌트 지원 |  __보호_23__ , __보호_24__ |
|  __보호됨_25__ | 간단한 HTTP 서버 |  __보호됨_26__ |
|  __보호_27__ / __보호_28__ | 동시성 | 웹 스크레이퍼용 비동기 I/O |
### 가상 환경 및 패키지 관리
모든 Python 프로젝트는 가상 환경을 사용하여 종속성을 격리해야 합니다.
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

최신 Python 프로젝트에서는 종속성 관리를 위해`uv`,`poetry`또는 `hatch`와 같은 도구와 함께 `pyproject.toml`를 점점 더 많이 사용하여 이전`setup.py`/`requirements.txt`접근 방식을 대체합니다.
### 비동기 프로그래밍
Python의 `asyncio`는 스레드 없이 동시 I/O를 가능하게 합니다. 이는 웹 스크레이퍼, 채팅 서버 및 API 클라이언트에 필수적입니다.
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

## 동시성 및 병렬성
Python은 각각 서로 다른 워크로드에 적합한 여러 동시성 모델을 제공합니다. CPython의 GIL(Global Interpreter Lock)은 스레드와의 실제 CPU 병렬 처리를 방지하므로 올바른 모델은 워크로드가 I/O 바인딩인지 CPU 바인딩인지에 따라 달라집니다.
### 스레딩(I/O 바인딩 작업)
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

### 다중 처리(CPU 바인딩 작업)
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

### Asyncio 내부
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 디렉터리 구조
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

### 빌드 구성 — `pyproject.toml`
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

### 최신 도구를 사용한 종속성 관리
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

### 린팅 및 코드 품질
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD 파이프라인 — GitHub Actions
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

## 테스트
### 테스트 프레임워크 및 설정
Python의 테스트 생태계는 Python 테스트의 사실상 표준인`pytest`를 중심으로 합니다.
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

### pytest를 사용한 단위 테스트
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

### 비동기 테스트 및 통합 테스트
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

## 상호 운용성
### ctypes로 C/C++ 호출하기
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

### 보다 복잡한 C Interop을 위해 cffi 사용
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

### Cython — C 성능을 갖춘 Python
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

### Pybind11 — C++ 확장
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

## 디자인 패턴
### 싱글톤
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

### 팩토리 패턴
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

### 관찰자 패턴
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

### 컨텍스트 관리자 패턴
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

### 전략 패턴
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

## 성능 및 최적화
### 프로파일링 도구
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

### 최적화 기술
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

### 벤치마킹
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## 배포
### 포장 및 유통
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### 도커파일
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

### 플랫폼별 배포
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

## 생태계
Python의 강점은 단지 언어에만 있는 것이 아닙니다. Python을 중심으로 구축된 생태계에도 있습니다.
### AI 및 머신러닝
| 도서관 | 목적 |
|---------|---------|
| 파이토치 | 딥러닝(연구 및 생산) |
| 텐서플로우/케라스 | 딥러닝(프로덕션 중심) |
| scikit 학습 | 기존 ML(회귀, 클러스터링, 분류) |
| 포옹 얼굴 트랜스포머 | 사전 훈련된 NLP/비전 모델 |
| 랭체인 / LlamaIndex | LLM을 사용하여 애플리케이션 구축 |
| 넘파이 | 수치 컴퓨팅(배열, 선형 대수) |
| 팬더 | 데이터 조작 및 분석 |
| Matplotlib / Seaborn / Plotly | 데이터 시각화 |
### 웹 개발
| 프레임워크 | 스타일 | 최고의 대상 |
|------------|-------|----------|
| 장고 | 풀스택, "배터리 포함" | 관리 패널, ORM, 인증을 갖춘 복잡한 웹 앱 |
| FastAPI | 현대적, 비동기식, 유형 중심 | API 및 마이크로서비스(현재 가장 빠르게 성장하고 있음) |
| 플라스크 | 최소한의 유연성 | 소형 앱 및 프로토타입 |
| 스트림라이트 | 데이터 앱 중심 | 순수 Python의 대시보드 및 데이터 데모 |
### 자동화 및 스크립팅
| 도서관 | 목적 |
|---------|---------|
|  __보호_0__ / __보호_1__ | 시스템 관리 |
|  __보호_2__ / __보호_3__ | HTTP 클라이언트 |
|  __보호_4__ / __보호_5__ | 웹 스크래핑 |
|  __보호_6__ / __보호_7__ | 브라우저 자동화 |
|  __보호됨_8__ | 분산 작업 대기열 |
|  __보호_9__ | 워크플로 조정 |
### 과학 컴퓨팅
| 도서관 | 목적 |
|---------|---------|
| 넘파이 | 배열 연산 및 선형 대수학 |
| 사이파이 | 과학적인 알고리즘(최적화, 신호 처리) |
| 심파이 | 기호 수학 |
| 주피터 노트북 | 대화형 컴퓨팅 환경 |
| 잭스 | 고성능 수치 컴퓨팅(GPU 가속) |
---

## Python을 사용해야 하는 경우
| 시나리오 | 왜 파이썬인가 | 더 나은 대안 |
|----------|------------|------|
| AI/ML/데이터 과학 | 생태계는 타의 추종을 불허합니다 | — |
| 자동화 및 스크립팅 | 가장 빠른 작성 및 디버깅 | 간단한 시스템 관리 작업을 위한 Shell/PowerShell |
| 웹 백엔드(API) | FastAPI는 훌륭합니다 | 처리량이 매우 높은 서비스를 위한 Go 또는 Java |
| 프로토타이핑 | 아이디어에서 작업 코드까지 가장 빠른 경로 | — |
| 교육 | 가장 초보자 친화적인 언어 | — |
| 데스크탑 애플리케이션 | 가능하지만 흔하지 않음 | C#(Windows), Swift(macOS) |
| 성능이 중요한 시스템 | 피하십시오 - 너무 느림 | C, C++, 러스트 |
| 모바일 앱 | 올바른 도구가 아닙니다 | 스위프트(iOS), 코틀린(안드로이드) |
| 임베디드 시스템 | 리소스가 너무 많이 사용됨 | 간단한 경우에는 C, Rust 또는 MicroPython |
---

## 파이썬 버전
언어는 계속 진화하고 있습니다. 최근 추가된 주요 내용:
| 버전 | 연도 | 주목할만한 기능 |
|---------|------|----|
| 3.10 | 2021 | 구조적 패턴 일치(`match/case`), 더 나은 오류 메시지 |
| 3.11 | 2022 | 10~60% 더 빠른 실행, 개선된 역추적 |
| 3.12 | 2023 | 더욱 유연한 f-문자열,`type`문, 성능 향상 |
| 3.13 | 2024년 | 실험적인 자유 스레드 모드(GIL 없음), 개선된 REPL |
| 3.14 | 2025년 | 추가 GIL 개선, 유형 시스템 개선 |
Python 2는 2020년 1월 1일에 수명이 종료되었습니다. 모든 새 프로젝트는 Python 3.10 이상을 사용해야 합니다.
---

## 빠른 참조: 일반적인 숙어
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

## 요약
Python은 가독성, 다양성, 생태계 깊이가 결합되어 세계에서 가장 널리 사용되는 프로그래밍 언어입니다. 이는 AI/ML을 위한 기본 선택이고 웹 백엔드 및 자동화를 위한 강력한 옵션이며 탁월한 교육 언어입니다. 주요 약점인 실행 속도와 모바일/내장 지원은 잘 알려져 있으며 해결 방법이 확립되어 있습니다. 대부분의 프로젝트에서 Python은 합리적인 출발점입니다.