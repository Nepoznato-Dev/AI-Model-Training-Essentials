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
# Sawa
Ang Python ay isang high-level, interpreted, general-purpose programming language na nilikha ni Guido van Rossum at unang inilabas noong 1991. Inuuna nito ang pagiging madaling mabasa ng code sa pamamagitan ng makabuluhang indentation at malinis na syntax na malapit sa simpleng Ingles. Ang Python ay dynamic na na-type, kinokolekta ng basura, at sumusuporta sa maramihang mga paradigm sa programming kabilang ang procedural, object-oriented, at functional programming.
Ngayon, ang Python ang nangingibabaw na wika sa AI/ML, data science, scientific computing, at automation — habang nananatiling isa sa mga pinakamahusay na wika para sa mga nagsisimula. Ang dalawahang pagkakakilanlan na iyon (sapat na simple para sa isang unang script, sapat na makapangyarihan upang sanayin ang malalaking modelo ng wika) ang nagpapahiwalay dito.
---

## Bakit Mahalaga ang Python
- **Pagiging madaling mabasa ayon sa disenyo**: Walang semicolon, walang braces — tinutukoy ng indentation ang saklaw. Ang code ay nagbabasa tulad ng pseudocode.
- **Massive ecosystem**: Nagho-host ang PyPI ng mahigit 500,000 packages na sumasaklaw sa halos bawat domain.
- **Ang wika ng AI**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — ang buong AI/ML stack ay Python-first.
- **Glue language**: Ikonekta ang isang C++ engine sa isang web API sa isang database sa ilang linya lamang.
- **Cross-platform**: Gumagana sa Windows, macOS, Linux, at mga naka-embed na system nang walang pagbabago.
- **Community**: Ang pinakamalaki at pinaka-aktibong programming community sa mundo.
## Ang mga Trade-off
Hindi perpekto ang Python. Ang pag-unawa sa mga limitasyon nito ay nakakatulong sa iyong magpasya kung kailan maabot ang ibang bagay:
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Bilis ng pagpapatupad** | 10–100x na mas mabagal kaysa sa C para sa mga gawaing nakatali sa CPU | Gamitin ang NumPy/PyTorch (C sa ilalim ng hood), o Cython/Numba para sa mga maiinit na loop |
| **GIL (Global Interpreter Lock)** | Pinipigilan ang totoong multi-threaded parallelism para sa CPU-bound na trabaho | Gumamit ng`multiprocessing`,`asyncio`, o mga pila ng gawain tulad ng Celery |
| **Pag-unlad ng mobile** | Hindi angkop para sa iOS/Android app | Gamitin ang Swift/Kotlin para sa native, o Flutter/React Native para sa cross-platform |
| **Mga naka-embed na system** | Masyadong mabigat para sa mga microcontroller | Gumamit ng MicroPython (isang magaan na variant) o lumipat sa C/Rust |
| **Paggamit ng memory** | Mas mataas na memory footprint kaysa sa mga pinagsama-samang wika | Katanggap-tanggap para sa karamihan ng mga application; gumamit ng mga generator para sa malaking data |
---

## Syntax Fundamentals
### Mga Variable at Uri
Gumagamit ang Python ng dynamic na pag-type — hindi ka nagdedeklara ng mga variable na uri, ngunit maaari kang magdagdag ng mga pahiwatig ng uri para sa kalinawan at suporta sa tooling.
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

### Kontrol na Daloy
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

### Mga Pag-andar
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

### Object-Oriented Programming
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

### Error sa Paghawak
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

## Advanced na Syntax at Mga Pattern
### Mga Generic na may`typing`Module
Ang`typing`module ng Python ay nagbibigay ng generic na uri ng suporta para sa pagbuo ng magagamit muli, uri-ligtas na mga bahagi. Hinahayaan ka ng mga generic na magsulat ng mga function at klase na gumagana sa anumang uri habang pinapanatili ang impormasyon ng uri para sa static na pagsusuri.
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

### Mga Dekorador at Metaprogramming
Ang mga dekorador ay isa sa pinakamakapangyarihang feature ng Python — hinahayaan ka nilang baguhin o palawigin ang gawi ng mga function at klase nang hindi binabago ang kanilang source code.
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

### Pagtutugma ng Structural Pattern (Python 3.10+)
Ang`match/case`na pahayag ng Python ay nagbibigay ng malakas na pagtutugma ng pattern sa mga destructuring, guard, at nested pattern.
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

### Mga Pagsasara, Mga Pag-andar ng Mas Mataas na Pagkakasunod-sunod, at Mga Iterator
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

### Overloading ng Operator
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

### Custom Exception Hierarchies
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

## Mga Pangunahing Tampok sa Lalim
### Ang Standard Library ("Mga Baterya Kasama")
Nagpapadala ang Python na may malawak na karaniwang library. Ilan sa mga pinakaginagamit na module:
| Module | Layunin | Halimbawa ng Paggamit |
|--------|---------|-------------|
| `os`/`pathlib`| Mga pagpapatakbo ng file system | `Path("data/output.csv").exists()`|
| `json`| JSON encoding/decoding | `json.loads(response_text)`|
| `datetime`| Petsa at oras ng pangangasiwa | `datetime.now(timezone.utc)`|
| `collections`| Mga espesyal na lalagyan | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Mga bloke ng gusali ng iterator | `combinations(items, 2)`|
| `functools`| Mga tool sa paggana | `lru_cache`,`partial`,`reduce`|
| `re`| Mga regular na expression | `re.findall(r"\d+", text)`|
| `subprocess`| Patakbuhin ang mga panlabas na utos | `subprocess.run(["ls", "-la"])`|
| `logging`| Pag-log ng application | `logging.basicConfig(level=logging.INFO)`|
| `typing`| I-type ang suporta ng pahiwatig | `Optional[str]`,`Union[int, float]`|
| `http.server`| Simpleng HTTP server | `python -m http.server 8000`|
| `threading`/`asyncio`| Concurrency | Async I/O para sa mga web scraper |
### Mga Virtual na Kapaligiran at Pamamahala ng Package
Ang bawat proyekto ng Python ay dapat gumamit ng isang virtual na kapaligiran upang ihiwalay ang mga dependency:
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

Ang mga modernong proyekto ng Python ay lalong gumagamit ng`pyproject.toml`na may mga tool tulad ng`uv`,`poetry`, o`hatch`para sa pamamahala ng dependency, na pinapalitan ang mas lumang`setup.py`/`requirements.txt`na diskarte.
### Async Programming
Ang`asyncio`ng Python ay nagbibigay-daan sa kasabay na I/O na walang mga thread — mahalaga para sa mga web scraper, chat server, at API client:
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

## Concurrency at Paralelismo
Nag-aalok ang Python ng ilang concurrency na modelo, bawat isa ay angkop sa iba't ibang workload. Pinipigilan ng GIL (Global Interpreter Lock) sa CPython ang totoong parallelism ng CPU sa mga thread, kaya ang tamang modelo ay nakasalalay sa kung ang iyong workload ay I/O-bound o CPU-bound.
### Threading (I/O-bound na mga gawain)
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

### Multiprocessing (CPU-bound tasks)
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

## Project Configuration at Build System
### Istraktura ng Direktoryo ng Proyekto
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

### Build Configuration — `pyproject.toml`
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

### Pamamahala ng Dependency gamit ang Mga Makabagong Tool
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

### Linting at Kalidad ng Code
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD Pipeline — Mga Pagkilos sa GitHub
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

## Pagsubok
### Testing Frameworks at Setup
Nakasentro ang testing ecosystem ng Python sa`pytest`, ang de facto na pamantayan para sa pagsubok sa Python.
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

### Mga Pagsusuri sa Unit na may pytest
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

### Mga Pagsusuri sa Async at Mga Pagsusuri sa Pagsasama
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

## Interoperability
### Pagtawag sa C/C++ gamit ang mga ctype
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

### Paggamit ng cffi para sa Mas Kumplikadong C Interop
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

### Cython — Python na may C Performance
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

### Pybind11 — C++ Extension
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

## Mga Pattern ng Disenyo
### Singleton
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

### Pattern ng Pabrika
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

### Pattern ng Tagamasid
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

### Pattern ng Context Manager
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

### Pattern ng Diskarte
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
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

### Mga Teknik sa Pag-optimize
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

### Pag-benchmark
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Deployment
### Packaging at Pamamahagi
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

### Deployment na Partikular sa Platform
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

## Ang Ecosystem
Ang lakas ng Python ay hindi lamang ang wika — ito ang ecosystem na binuo sa paligid nito.
### AI at Machine Learning
| Aklatan | Layunin |
|---------|---------|
| PyTorch | Malalim na pagkatuto (pananaliksik at produksyon) |
| TensorFlow / Keras | Malalim na pagkatuto (nakatuon sa produksyon) |
| scikit-matuto | Classical ML (regression, clustering, classification) |
| Hugging Face Transformers | Mga pre-trained na modelo ng NLP/vision |
| LangChain / LlamaIndex | Pagbuo ng mga application gamit ang mga LLM |
| NumPy | Numerical computing (mga array, linear algebra) |
| Mga Panda | Pagmamanipula at pagsusuri ng data |
| Matplotlib / Seaborn / Plotly | Visualization ng data |
### Web Development
| Balangkas | Estilo | Pinakamahusay Para sa |
|-----------|-------|----------|
| Django | Full-stack, "kasama ang mga baterya" | Mga kumplikadong web app na may mga admin panel, ORM, auth |
| FastAPI | Moderno, async, uri-driven | Mga API at microservice (kasalukuyang pinakamabilis na lumalago) |
| Prasko | Minimal, nababaluktot | Mga maliliit na app at prototype |
| Streamlit | Nakatuon sa data-app | Mga dashboard at data demo sa purong Python |
### Automation at Scripting
| Aklatan | Layunin |
|---------|---------|
| `subprocess`/`os`| Pangangasiwa ng system |
| `requests`/`httpx`| Mga kliyente ng HTTP |
| `BeautifulSoup`/`Scrapy`| Web scraping |
| `Selenium`/`Playwright`| Pag-aautomat ng browser |
| `Celery`| Naipamahagi na mga pila ng gawain |
| `Airflow`| Orkestrasyon ng daloy ng trabaho |
### Scientific Computing
| Aklatan | Layunin |
|---------|---------|
| NumPy | Array operations at linear algebra |
| SciPy | Mga siyentipikong algorithm (pag-optimize, pagpoproseso ng signal) |
| SymPy | Simbolikong matematika |
| Jupyter Notebook | Interactive computing environment |
| JAX | High-performance numerical computing (GPU-accelerated) |
---

## Kailan Gamitin ang Python
| Sitwasyon | Bakit Python | Mas mahusay na Alternatibo |
|----------|-----------|-------------------|
| AI/ML/Data Science | Ang ekosistema ay walang kaparis | — |
| Automation at scripting | Pinakamabilis na magsulat at mag-debug | Shell/PowerShell para sa mga simpleng gawain ng sysadmin |
| Mga backend sa web (mga API) | Mahusay ang FastAPI | Go o Java para sa napakataas na throughput na serbisyo |
| Prototyping | Pinakamabilis na landas mula sa ideya hanggang sa gumaganang code | — |
| Edukasyon | Karamihan sa baguhan-friendly na wika | — |
| Mga desktop application | Posible ngunit hindi karaniwan | C# (Windows), Swift (macOS) |
| Mga sistemang kritikal sa pagganap | Iwasan — masyadong mabagal | C, C++, kalawang |
| Mga mobile app | Hindi ang tamang tool | Swift (iOS), Kotlin (Android) |
| Mga naka-embed na system | Masyadong mabigat sa mapagkukunan | C, Rust, o MicroPython para sa mga simpleng kaso |
---

## Mga Bersyon ng Python
Ang wika ay patuloy na umuunlad. Mga pangunahing kamakailang karagdagan:
| Bersyon | Taon | Mga Kapansin-pansing Tampok |
|---------|------|-----------------|
| 3.10 | 2021 | Structural pattern matching (`match/case`), mas mahusay na mga mensahe ng error |
| 3.11 | 2022 | 10–60% mas mabilis na pagpapatupad, pinahusay na mga traceback |
| 3.12 | 2023 | Mas nababaluktot na mga f-string,`type`na pahayag, mga nadagdag sa pagganap |
| 3.13 | 2024 | Pang-eksperimentong free-threaded mode (walang GIL), pinahusay na REPL |
| 3.14 | 2025 | Karagdagang walang-GIL na mga pagpapabuti, uri ng mga pagpapahusay ng system |
Naabot ng Python 2 ang end-of-life noong Enero 1, 2020. Dapat gumamit ng Python 3.10 o mas bago ang lahat ng bagong proyekto.
---

## Mabilis na Sanggunian: Mga Karaniwang Idyoma
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

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba sa pagitan ng mga listahan at tuple, at kailan ko dapat gamitin ang bawat isa?
**A:** Ang mga listahan ay nababago (`[]`), ang mga tuple ay hindi nababago (`()`). Gumamit ng mga listahan kapag kailangan mong magdagdag, mag-alis, o magpalit ng mga elemento. Gumamit ng mga tuple para sa mga nakapirming koleksyon ng magkakaibang data, mga key ng diksyunaryo, mga halaga ng pagbabalik ng function, o kapag gusto mong i-signal na "hindi ito dapat magbago." Ang mga tuple ay bahagyang mas mahusay sa memorya at maaaring gamitin bilang mga set/dict key; ang mga listahan ay hindi maaaring.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: Paano nakakaapekto ang Global Interpreter Lock (GIL) sa aking code, at ano ang dapat kong gawin tungkol dito?
**A:** Pinipigilan ng GIL ang maraming mga thread mula sa pagpapatupad ng Python bytecode nang sabay-sabay, na ginagawang hindi epektibo ang threading para sa gawaing nakatali sa CPU. Para sa mga gawaing nakatali sa I/O (mga kahilingan sa network, file I/O), gumagana nang maayos ang`threading`o`asyncio`dahil inilalabas ang GIL sa panahon ng I/O. Para sa mga gawaing nakatali sa CPU, gamitin ang`multiprocessing`(mga hiwalay na proseso, bawat isa ay may sariling GIL), o i-offload sa mga extension ng C (NumPy, Cython, Numba) na naglalabas ng GIL sa loob.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: Dapat ba akong gumamit ng mga uri ng pahiwatig sa lahat ng dako? Ano ang mga praktikal na trade-off?
**A:** Ang mga pahiwatig ng uri (`def greet(name: str) -> str:`) ay opsyonal at hindi ipinapatupad sa runtime. Pinapabuti nila ang autocompletion ng IDE, nakakakuha ng mga bug sa pamamagitan ng mga static na tool sa pagsusuri (mypy), at layunin ng dokumento. Ang trade-off ay sobrang verbosity at isang learning curve para sa mga advanced na uri (`Union`,`Generic`,`Protocol`). Rekomendasyon: gumamit ng mga uri ng pahiwatig para sa mga function signature sa anumang proyektong higit sa ~500 linya; gamitin ang mga ito nang matipid sa maikling mga script. Paganahin ang mypy sa CI para sa unti-unting pagpapatupad.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: Ano ang mga pinakamahusay na kasanayan para sa paghawak ng mga pagbubukod sa Python?
**A:** Makakuha ng mga partikular na exception sa halip na`except:`(na nakakakuha din ng`SystemExit`at `KeyboardInterrupt`). Gamitin ang`try/except/else/finally`upang paghiwalayin ang happy-path na logic mula sa paghawak ng error. Tukuyin ang mga custom na hierarchy ng exception para sa mga library. Huwag gumamit ng mga exception para sa control flow sa performance-sensitive code — mabagal ang mga ito. I-log ang exception gamit ang`logging.exception()`para makuha ang buong traceback.
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

### Q5: Paano nakakatipid ng memorya ang mga generator, at kailan ko dapat gamitin ang mga ito sa mga listahan?
**S:** Ang mga generator ay gumagawa ng mga halaga nang tamad — paisa-isa, on demand — sa halip na bumuo ng isang buong listahan sa memorya. Para sa malalaking dataset (milyong-milyong row, infinite sequence, streaming data), ang mga generator ay gumagamit ng pare-parehong memory anuman ang laki. Gumamit ng mga generator kapag umulit ka nang isang beses at hindi kailangan ng pag-index o`len()`. Gumamit ng mga listahan kapag kailangan mo ng random na pag-access, maraming pag-ulit, o maliit ang koleksyon.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Word Frequency Counter na may Ranking
**Pahayag ng Problema:** Dahil sa malaking text file, bilangin ang dalas ng bawat salita, i-rank ang mga ito ayon sa dalas (pababa), at ibalik ang nangungunang N resulta. Pangasiwaan ang case insensitivity, bantas, at mahusay na iproseso ang mga file na masyadong malaki upang magkasya sa memorya.
**Hakbang 1 — Unawain ang Problema:**
Kailangan nating: (1) basahin ang teksto, (2) hatiin sa mga salita, (3) gawing normal ang case, (4) tanggalin ang mga bantas, (5) bilangin ang mga pangyayari, (6) pagbukud-bukurin ayon sa bilang na pababang, (7) ibalik sa itaas ang N. Ang ibig sabihin ng "masyadong malaki upang magkasya sa memorya" ay dapat nating iproseso ang linya-by-linya sa mga generator.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`re.finditer`para sa mahusay na pagkuha ng salita nang hindi gumagawa ng mga intermediate na listahan.
- Gamitin ang`collections.Counter`para sa pagtaas ng O(1) bawat salita.
- Gumamit ng`Counter.most_common(n)`na gumagamit ng heap sa loob — O(k log n) sa halip na O(n log n) para sa buong uri.
- Iproseso ang linya-by-line sa pamamagitan ng generator upang panatilihing pare-pareho ang memorya.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Memorya: tanging ang Counter dict ang nasa memorya (isang entry sa bawat natatanging salita), hindi ang nilalaman ng file. Para sa English na text, ~100K natatanging salita ≈ ilang MB.
- Oras: O(W) para i-scan ang lahat ng salita + O(U log N) para sa top-N extraction, kung saan W = kabuuang salita, U = natatanging salita.
- Mga kaso sa gilid: ang mga kudlit sa contraction ("huwag") ay pinapanatili ng regex. Ang Unicode text ay mangangailangan ng`re.UNICODE`flag o ibang pattern.
### Problema 2: Magpatupad ng Thread-Safe LRU Cache
**Problem Statement:** Bumuo ng isang Least Recently Used (LRU) cache mula sa simula na thread-safe, sumusuporta sa O(1) get and put operations, at awtomatikong nagpapaalis ng hindi gaanong nagamit na item kapag lumampas ang kapasidad.
**Hakbang 1 — Unawain ang Problema:**
Ang LRU cache ay nangangailangan ng: (1) mabilis na paghahanap sa pamamagitan ng key → hash map, (2) mabilis na pag-order ayon sa kabago-bago → dobleng naka-link na listahan, (3) kaligtasan ng thread → pag-lock. Sa`get(key)`: ilipat ang item sa harap. Sa`put(key, val)`: ipasok sa harap; kung sobra sa kapasidad, tanggalin sa likod.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Ang`dict`ng Python ay nagpapanatili ng insertion order (3.7+), para magamit namin ang isang ordered dict approach: tanggalin at muling ipasok upang lumipat sa dulo.
- Para sa kaligtasan ng thread, gamitin ang`threading.Lock`para sa kapwa pagbubukod.
- Alternatibong: gumamit ng`collections.OrderedDict`na mayroong`move_to_end()`.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Pagiging kumplikado ng oras: O(1) para sa parehong`get`at`put`—`OrderedDict.move_to_end()`at`popitem()`ay O(1).
- Kaligtasan sa thread: tinitiyak ng`Lock`ang atomicity. Para sa mas mataas na throughput, isaalang-alang ang`threading.RLock`o isang read-write na pattern ng lock, ngunit para sa karamihan ng mga kaso ng paggamit, sapat na ang isang simpleng lock.
- Tandaan sa produksiyon: para sa single-threaded code, ang`functools.lru_cache`ay mas simple at ipinapatupad sa C para sa mas mahusay na pagganap.
### Problema 3: I-parse at Suriin ang isang Mathematical Expression
**Problem Statement:** Sumulat ng parser na kumukuha ng string tulad ng`"3 + 4 * 2 / (1 - 5)"`at tama itong sinusuri ayon sa operator precedence at panaklong.
**Hakbang 1 — Unawain ang Problema:**
Nangangailangan ito ng: (1) pag-token ng input string sa mga numero, operator, at parentheses, (2) pag-parse nang may tamang precedence (`*`at`/`bago ang`+`at`-`), (3) paghawak ng mga nested parentheses. Ang isang walang muwang na kaliwa-papuntang-kanang pagsusuri ay magbibigay ng mga maling resulta.
**Hakbang 2 — Tukuyin ang Diskarte:**
Ang klasikong solusyon ay ang **shunting-yard algorithm** (Dijkstra) na nagko-convert ng infix sa postfix (Reverse Polish Notation), pagkatapos ay sinusuri ang postfix. Bilang kahalili, gumamit ng recursive descent parser. Para sa Python partikular, maaari rin nating gamitin ang`ast.literal_eval`para sa ligtas na pagsusuri — ngunit ipatupad natin ito nang maayos.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Katumpakan:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. Tama.
- Oras: O(N) para sa tokenization, O(N) para sa shunting-yard, O(N) para sa pagsusuri — pangkalahatang O(N).
- Mga Edge case na hahawakan: mga negatibong numero (prepend`0`bago unary`-`), paghahati sa zero (magdagdag ng paghawak ng error), invalid na input (validate token).
- Pythonic alternative:`ast.parse(expr, mode='eval')`na may custom na node na bisita para sa ligtas na pagsusuri nang walang`eval()`.
### Problema 4: Bumuo ng CLI Dashboard na may Real-Time na Mga Update sa Data
**Problem Statement:** Lumikha ng terminal-based na dashboard na nagpapakita ng mga sukatan ng system (CPU, memory, disk) na ina-update sa real-time, na may mga color-coded na threshold at tumutugon na layout.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) periodic system metric collection, (2) terminal rendering na may kontrol ng cursor, (3) color output batay sa mga threshold, (4) non-blocking keyboard input para sa pag-quit. Isa itong pattern ng producer-consumer na may rendering loop.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`psutil`para sa cross-platform system metrics.
- Gumamit ng mga ANSI escape code para sa pagpoposisyon ng cursor at mga kulay (o ang`rich`library para sa mas mataas na antas ng API).
- Gamitin ang`time.sleep`para sa agwat ng pag-update.
- Istraktura bilang: pagkolekta ng data → pag-format → pag-render ng pipeline.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Ang`cpu_percent(interval=0.5)`ay humaharang nang 0.5s upang masukat — ito ang tamang diskarte (ang non-blocking mode ay nagbibigay ng 0% sa unang tawag).
- Gumagana ang mga ANSI code sa modernong Windows Terminal at lahat ng mga terminal ng Unix. Para sa legacy na Windows cmd, idagdag ang`os.system('color')`o gamitin ang`colorama`.
- Pag-upgrade sa produksyon: gamitin ang`rich`library (`rich.live`) para sa pag-render na walang flicker, awtomatikong layout, at cross-platform na compatibility.
- Extensibility: ang bawat sukatan ay isang independiyenteng function, na ginagawang madali upang magdagdag ng temperatura ng GPU, bilang ng proseso, o mga koneksyon sa network.
---

## Buod
Ang kumbinasyon ng Python ng pagiging madaling mabasa, versatility, at ecosystem depth ay ginagawa itong pinakamalawak na ginagamit na programming language sa mundo. Ito ang default na pagpipilian para sa AI/ML, isang malakas na opsyon para sa mga web backend at automation, at isang mahusay na wika sa pagtuturo. Ang mga pangunahing kahinaan nito — bilis ng execution at mobile/embedded na suporta — ay lubos na nauunawaan at may itinatag na mga solusyon. Para sa karamihan ng mga proyekto, ang Python ay isang makatwirang panimulang punto.