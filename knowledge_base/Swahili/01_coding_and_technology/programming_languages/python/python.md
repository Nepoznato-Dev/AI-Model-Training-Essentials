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
#Chatu
Python ni lugha ya kiwango cha juu, iliyotafsiriwa, na ya kusudi la jumla iliyoundwa na Guido van Rossum na iliyotolewa kwa mara ya kwanza mnamo 1991. Inatanguliza usomaji wa msimbo kupitia ujongezaji muhimu na sintaksia safi inayosomeka karibu na Kiingereza cha kawaida. Python inachapwa kwa nguvu, inakusanywa takataka, na inasaidia dhana nyingi za programu ikiwa ni pamoja na utaratibu, uelekezaji wa kitu, na utendakazi wa programu.
Leo, Python ndiyo lugha kuu katika AI/ML, sayansi ya data, kompyuta ya kisayansi na uwekaji otomatiki - huku ikisalia kuwa mojawapo ya lugha bora zaidi kwa wanaoanza. Kitambulisho hicho cha pande mbili (rahisi vya kutosha kwa hati ya kwanza, yenye nguvu ya kutosha kufunza miundo mikubwa ya lugha) ndicho kinachoitofautisha.
---

## Kwa Nini Chatu Ni Muhimu
- **Usomaji kulingana na muundo**: Hakuna nusukoloni, hakuna viunga - ujongezaji hufafanua upeo. Msimbo unasomeka kama pseudocode.
- **Mfumo mkubwa wa ikolojia**: PyPI hupangisha zaidi ya vifurushi 500,000 vinavyoshughulikia takriban kila kikoa.
- **Lugha ya AI**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — mrundikano wote wa AI/ML ni Python-kwanza.
- **Lugha ya gundi**: Unganisha injini ya C++ kwenye API ya wavuti kwenye hifadhidata kwa njia chache tu.
- **Jukwaa Msalaba**: Hufanya kazi kwenye Windows, macOS, Linux, na mifumo iliyopachikwa bila marekebisho.
- **Jumuiya**: Jumuiya kubwa na inayofanya kazi zaidi ya upangaji programu ulimwenguni.
## Mapatano
Python sio kamili. Kuelewa mapungufu yake hukusaidia kuamua wakati wa kufikia kitu kingine:
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Kasi ya utekelezaji** | 10–100x polepole kuliko C kwa kazi zinazofungamana na CPU | Tumia NumPy/PyTorch (C chini ya kofia), au Cython/Numba kwa vitanzi moto |
| **GIL (Kufuli la Mkalimani Ulimwenguni)** | Huzuia ulinganifu wa kweli wa nyuzi nyingi kwa kazi inayofungamana na CPU | Tumia`multiprocessing`,`asyncio`, au foleni za kazi kama vile Celery |
| **Uendelezaji wa rununu** | Haifai kwa programu za iOS/Android | Tumia Swift/Kotlin kwa asili, au Flutter/React Native kwa jukwaa-msingi |
| **Mifumo iliyopachikwa** | Ni nzito sana kwa vidhibiti vidogo | Tumia MicroPython (lahaja nyepesi) au ubadilishe hadi C/Rust |
| **Matumizi ya kumbukumbu** | Alama ya kumbukumbu ya juu kuliko lugha zilizokusanywa | Inakubalika kwa programu nyingi; tumia jenereta kwa data kubwa |
---

## Misingi ya Sintaksia
### Vigezo na Aina
Python hutumia uchapaji wa nguvu - hautangazi aina tofauti, lakini unaweza kuongeza vidokezo vya aina kwa uwazi na usaidizi wa zana.
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

### Mtiririko wa Kudhibiti
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

### Kazi
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

### Upangaji Unaoelekezwa na Kitu
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

### Kushughulikia Hitilafu
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

## Sintaksia na Miundo ya Kina
### Jenetiki zenye Moduli ya `typing`
Moduli ya`typing`ya Python hutoa usaidizi wa aina ya jumla kwa vipengele vinavyoweza kutumika tena, vya aina-salama. Jenetiki hukuruhusu kuandika chaguo za kukokotoa na darasa zinazofanya kazi na aina yoyote huku ukihifadhi maelezo ya aina kwa uchanganuzi tuli.
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

### Wapambaji na Upangaji programu
Wapambaji ni mojawapo ya vipengele vyenye nguvu zaidi vya Python - hukuruhusu kurekebisha au kupanua tabia ya utendaji na madarasa bila kubadilisha msimbo wao wa chanzo.
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

### Ulinganishaji wa Muundo wa Muundo (Python 3.10+)
Taarifa ya Python's`match/case`hutoa ulinganifu wa muundo wenye nguvu na uharibufu, walinzi, na ruwaza zilizowekwa.
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

### Kufungwa, Kazi za Agizo la Juu, na Viigaji
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

### Kupakia kwa Opereta
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

### Daraja za Vighairi Maalum
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

## Vipengele Muhimu kwa Kina
### Maktaba ya Kawaida ("Betri Zilizojumuishwa")
Meli za Python zilizo na maktaba ya kiwango kikubwa. Baadhi ya moduli zinazotumiwa zaidi:
| Moduli | Kusudi | Mfano Tumia |
|--------|---------|-------------|
| `os`/`pathlib`| Shughuli za mfumo wa faili | `Path("data/output.csv").exists()`|
| `json`| JSON usimbaji/usimbuaji | `json.loads(response_text)`|
| `datetime`| Tarehe na wakati utunzaji | `datetime.now(timezone.utc)`|
| `collections`| Vyombo maalum | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Vitalu vya ujenzi vya Iterator | `combinations(items, 2)`|
| `functools`| Zana za kazi | `lru_cache`,`partial`,`reduce`|
| `re`| Maneno ya kawaida | `re.findall(r"\d+", text)`|
| `subprocess`| Endesha amri za nje | `subprocess.run(["ls", "-la"])`|
| `logging`| Kuweka kumbukumbu za programu | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Chapa msaada wa kidokezo | `Optional[str]`,`Union[int, float]`|
| `http.server`| Seva rahisi ya HTTP | `python -m http.server 8000`|
| `threading`/`asyncio`| Concurrency | Async I/O kwa vichakachuaji vya wavuti |
### Mazingira Pepe na Usimamizi wa Kifurushi
Kila mradi wa Python unapaswa kutumia mazingira ya kawaida kutenganisha utegemezi:
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

Miradi ya kisasa ya Python inazidi kutumia`pyproject.toml`na zana kama`uv`,`poetry`, au`hatch`kwa usimamizi wa utegemezi, ikichukua nafasi ya mbinu ya zamani ya`setup.py`/ `requirements.txt`.
Upangaji wa ### Async
`asyncio` ya Python huwezesha I/O kwa wakati mmoja bila nyuzi - muhimu kwa vichakachuaji vya wavuti, seva za gumzo, na wateja wa API:
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

## Concurrency & Usambamba
Python inatoa mifano kadhaa ya sarafu, kila moja inafaa kwa mzigo tofauti wa kazi. GIL (Global Interpreter Lock) katika CPython huzuia ulinganifu wa kweli wa CPU na nyuzi, kwa hivyo muundo unaofaa unategemea ikiwa mzigo wako wa kazi ni wa I/O au unafungwa na CPU.
### Kuweka nyuzi (Kazi za I/O)
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

### Usindikaji mwingi (majukumu yanayofungamana na CPU)
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Saraka ya Mradi
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

### Usanidi wa Kuunda — `pyproject.toml`
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

### Usimamizi wa Utegemezi kwa Zana za Kisasa
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

### Uwekaji na Ubora wa Kanuni
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD Bomba - Vitendo vya GitHub
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

##Upimaji
### Mifumo ya Kujaribu na Usanidi
Mfumo wa majaribio wa Python unazingatia`pytest`, kiwango halisi cha majaribio ya Chatu.
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

### Vipimo vya Kitengo na pytest
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

### Majaribio ya Async na Majaribio ya Muunganisho
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

## Kuingiliana
### Inapiga C/C++ na ctypes
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

### Kutumia cffi kwa Complex C Interop
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

### Cython — Chatu yenye Utendaji wa C
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

### Pybind11 — Viendelezi vya C++
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

## Miundo ya Kubuni
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

### Muundo wa Kiwanda
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

### Muundo wa Mwangalizi
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

### Muundo wa Kidhibiti Muktadha
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

### Muundo wa Mkakati
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
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

### Mbinu za Kuboresha
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

### Kuweka alama
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Usambazaji
### Ufungaji na Usambazaji
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

### Usambazaji Mahususi wa Mfumo
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

## Mfumo wa Ikolojia
Nguvu ya Python sio lugha tu - ni mfumo wa ikolojia uliojengwa kuizunguka.
### AI na Mafunzo ya Mashine
| Maktaba | Kusudi |
|---------|---------|
| PyTorch | Kujifunza kwa kina (utafiti na uzalishaji) |
| TensorFlow / Keras | Kujifunza kwa kina (kuzingatia uzalishaji) |
| scikit-jifunze | Classical ML (regression, clustering, classification) |
| Transfoma za Uso wa Kukumbatiana | Mifano ya NLP/maono iliyofunzwa mapema |
| LangChain / LlamaIndex | Kujenga programu na LLMs |
| Nambari | Kompyuta ya nambari (safu, aljebra ya mstari) |
| Panda | Udanganyifu na uchambuzi wa data |
| Matplotlib / Seaborn / Plotly | Taswira ya data |
### Maendeleo ya Wavuti
| Mfumo | Mtindo | Bora Kwa |
|-----------|-------------------|
| Django | Rafu kamili, "betri zimejumuishwa" | Programu changamano za wavuti zilizo na paneli za msimamizi, ORM, auth |
| FastAPI | Ya kisasa, isiyolingana, inayoendeshwa kwa aina | API na huduma ndogo (zinazokua kwa kasi zaidi kwa sasa) |
| Chupa | Ndogo, rahisi | Programu ndogo na mifano |
| Sawazisha | Data-programu inayolenga | Dashibodi na demos za data katika Python safi |
### Otomatiki na Maandishi
| Maktaba | Kusudi |
|---------|---------|
| `subprocess`/`os`| Utawala wa mfumo |
| `requests`/`httpx`| Wateja wa HTTP |
| `BeautifulSoup`/`Scrapy`| Kuchakachua mtandao |
| `Selenium`/`Playwright`| Otomatiki ya kivinjari |
| `Celery`| Foleni za kazi zilizosambazwa |
| `Airflow`| Onyesho la mtiririko wa kazi |
### Kompyuta ya Kisayansi
| Maktaba | Kusudi |
|---------|---------|
| Nambari | Uendeshaji wa safu na aljebra ya mstari |
| SciPy | Algorithms za kisayansi (uboreshaji, usindikaji wa ishara) |
| SymPy | Hisabati ya ishara |
| Daftari la Jupyter | Mazingira maingiliano ya kompyuta |
| JAX | Kompyuta ya utendaji wa juu ya nambari (GPU-iliyoharakishwa) |
---

## Wakati wa Kutumia Python
| Hali | Kwa nini Python | Mbadala Bora |
|----------|-----------|-------------------|
| AI/ML/Sayansi ya Data | Mfumo ikolojia haulinganishwi | - |
| Otomatiki na uandishi | Haraka zaidi kuandika na kutatua | Shell/PowerShell kwa kazi rahisi za sysadmin |
| Nyuma za wavuti (API) | FastAPI ni bora | Nenda au Java kwa huduma za upitishaji wa hali ya juu |
| Uchapaji | Njia ya haraka zaidi kutoka kwa wazo hadi nambari ya kufanya kazi | - |
| Elimu | Lugha ya kirafiki zaidi | - |
| Programu za kompyuta ya mezani | Inawezekana lakini isiyo ya kawaida | C# (Windows), Swift (macOS) |
| Mifumo muhimu ya utendaji | Epuka - polepole sana | C, C++, Kutu |
| Programu za simu | Si zana sahihi | Swift (iOS), Kotlin (Android) |
| Mifumo iliyopachikwa | Rasilimali nzito mno | C, Rust, au MicroPython kwa kesi rahisi |
---

## Matoleo ya Python
Lugha inaendelea kubadilika. Nyongeza muhimu za hivi karibuni:
| Toleo | Mwaka | Vipengele Maarufu |
|---------|------|-----------------|
| 3.10 | 2021 | Ulinganishaji wa muundo wa muundo (`match/case`), ujumbe bora wa hitilafu |
| 3.11 | 2022 | Utekelezaji wa haraka wa 10-60%, ufuatiliaji ulioboreshwa |
| 3.12 | 2023 | Mifuatano rahisi zaidi ya f, taarifa ya `type`, faida za utendakazi |
| 3.13 | 2024 | Hali ya majaribio isiyo na nyuzi (hakuna GIL), REPL | iliyoboreshwa
| 3.14 | 2025 | Maboresho zaidi yasiyo ya GIL, aina ya uboreshaji wa mfumo |
Python 2 ilifikia mwisho wa maisha mnamo Januari 1, 2020. Miradi yote mipya inapaswa kutumia Python 3.10 au matoleo mapya zaidi.
---

## Marejeleo ya Haraka: Nahau za Kawaida
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

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya orodha na nakala, na ninapaswa kutumia kila moja lini?
**J:** Orodha zinaweza kubadilika (`[]`), nakala hazibadiliki (`()`). Tumia orodha unapohitaji kuongeza, kuondoa au kubadilisha vipengele. Tumia nakala kwa mikusanyiko isiyobadilika ya data tofauti, funguo za kamusi, thamani za kurejesha utendakazi, au unapotaka kuashiria "hii haipaswi kubadilika." Nakala zinafaa zaidi kwa kumbukumbu na zinaweza kutumika kama vitufe vya kuweka/kuamuru; orodha haziwezi.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: Je, Kufuli ya Wakalimani Ulimwenguni (GIL) inaathiri vipi msimbo wangu, na nifanye nini kuihusu?
**J:** GIL huzuia nyuzi nyingi kutekeleza Python bytecode kwa wakati mmoja, hivyo kufanya uzio kutofaa kwa kazi inayofungamana na CPU. Kwa kazi zinazofungamana na I/O (maombi ya mtandao, faili I/O),`threading`au`asyncio`hufanya kazi vizuri kwa sababu GIL inatolewa wakati wa I/O. Kwa kazi zinazofungamana na CPU, tumia`multiprocessing`(michakato tofauti, kila moja ikiwa na GIL yake), au pakia hadi viendelezi vya C (NumPy, Cython, Numba) vinavyotoa GIL ndani.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: Je, nitumie vidokezo vya aina kila mahali? Je, ni biashara gani ya kivitendo?
**A:** Vidokezo vya aina (`def greet(name: str) -> str:`) ni vya hiari na havitekelezwi wakati wa utekelezaji. Wanaboresha ukamilishaji kiotomatiki wa IDE, kupata hitilafu kupitia zana za uchambuzi tuli (mypy), na dhamira ya hati. Ubadilishanaji ni wa kitenzi cha ziada na mkondo wa kujifunza kwa aina za hali ya juu (`Union`,`Generic`,`Protocol`). Pendekezo: tumia vidokezo vya aina kwa saini za kazi katika mradi wowote zaidi ya mistari ~ 500; zitumie kwa uangalifu katika maandishi mafupi. Washa mypy katika CI kwa utekelezaji wa taratibu.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: Je, ni mbinu gani bora za kushughulikia vighairi katika Python?
**J:** Pata vighairi maalum badala ya`except:`(ambayo hukamata`SystemExit`na`KeyboardInterrupt`pia). Tumia`try/except/else/finally`kutenganisha mantiki ya njia ya furaha na kushughulikia makosa. Bainisha viwango maalum vya ubaguzi kwa maktaba. Kamwe usitumie vighairi kudhibiti mtiririko katika msimbo unaonyeti utendakazi - ni polepole. Weka ubaguzi kwa kutumia`logging.exception()`ili kunasa ufuatiliaji kamili.
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

### Q5: Jenereta huhifadhije kumbukumbu, na ninapaswa kuzitumia lini kwenye orodha?
**J:** Jenereta huzalisha thamani kwa uvivu - moja baada ya nyingine, inapohitajika - badala ya kuunda orodha nzima katika kumbukumbu. Kwa seti kubwa za data (mamilioni ya safu mlalo, mfuatano usio na kikomo, data ya utiririshaji), jenereta hutumia kumbukumbu isiyobadilika bila kujali saizi. Tumia jenereta unaporudia mara moja na huhitaji kuorodhesha au`len()`. Tumia orodha unapohitaji ufikiaji bila mpangilio, marudio mengi, au mkusanyiko ni mdogo.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tengeneza Kaunta ya Marudio ya Neno yenye Nafasi
**Taarifa ya Tatizo:** Kwa kuzingatia faili kubwa ya maandishi, hesabu marudio ya kila neno, yapange kulingana na marudio (kushuka), na urudishe matokeo ya juu ya N. Hushughulikia hali ya kutojali, alama za uakifishaji na kuchakata faili kubwa mno na kutoshea kwenye kumbukumbu.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) kusoma maandishi, (2) kugawanyika katika maneno, (3) kurekebisha hali ya kawaida, (4) kukatwa kwa alama za uakifishaji, (5) matukio ya hesabu, (6) kupanga kwa kuhesabu kushuka, (7) kurudisha sehemu ya juu N. Kizuizi cha "kubwa sana kutoshea kumbukumbu" kinamaanisha kwamba tunapaswa kuchakata mstari kwa mstari na jenereta.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`re.finditer`kwa uchimbaji wa maneno mzuri bila kuunda orodha za kati.
- Tumia`collections.Counter`kwa ongezeko la O(1) kwa kila neno.
- Tumia`Counter.most_common(n)`ambayo hutumia lundo ndani - O(k log n) badala ya O(n log n) kwa kupanga kamili.
- Mchakato wa mstari kwa mstari kupitia jenereta ili kuweka kumbukumbu mara kwa mara.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Kumbukumbu: ni amri ya Counter pekee iliyo kwenye kumbukumbu (ingizo moja kwa kila neno la kipekee), sio yaliyomo kwenye faili. Kwa maandishi ya Kiingereza, ~100K maneno ya kipekee ≈ MB chache.
- Muda: O(W) kuchanganua maneno yote + O(U logi N) kwa ajili ya uchimbaji wa top-N, ambapo W = jumla ya maneno, U = maneno ya kipekee.
- Kesi za makali: apostrophes katika mikazo ("usifanye") huhifadhiwa na regex. Maandishi ya Unicode yangehitaji bendera ya`re.UNICODE`au muundo tofauti.
### Tatizo la 2: Tekeleza Akiba ya LRU ya Thread-Salama
**Taarifa ya Tatizo:** Tengeneza akiba Isiyotumika Hivi Majuzi zaidi (LRU) kuanzia mwanzo ambayo ni salama kwa uzi, inayoauni utendakazi wa O(1) pata na kuweka, na huondoa kiotomatiki kipengee kilichotumika hivi majuzi zaidi wakati uwezo umepitwa.
**Hatua ya 1 - Elewa Tatizo:**
Akiba ya LRU inahitaji: (1) kuangalia haraka kwa ufunguo → ramani ya hashi, (2) kuagiza haraka kwa urejeshaji → orodha iliyounganishwa mara mbili, (3) usalama wa nyuzi → kufunga. Kwenye`get(key)`: sogeza kipengee mbele. Kwenye`put(key, val)`: ingiza mbele; ikiwa ni juu ya uwezo, ondoa kutoka nyuma.
**Hatua ya 2 — Tambua Mbinu:**
- Python's`dict`hudumisha agizo la uwekaji (3.7+), ili tuweze kutumia mbinu ya amri iliyoamriwa: futa na uingize tena ili kusonga hadi mwisho.
- Kwa usalama wa nyuzi, tumia`threading.Lock`kwa kutojumuisha pande zote mbili.
- Mbadala: tumia`collections.OrderedDict`ambayo ina`move_to_end()`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Utata wa saa: O(1) kwa`get`na`put`—`OrderedDict.move_to_end()`na`popitem()`ni O(1).
- Usalama wa nyuzi:`Lock`inahakikisha atomiki. Kwa utumaji wa juu zaidi, zingatia`threading.RLock`au mchoro wa kufuli soma-andika, lakini kwa hali nyingi, kufuli rahisi inatosha.
- Dokezo la uzalishaji: kwa msimbo wa nyuzi moja,`functools.lru_cache`ni rahisi na inatekelezwa katika C kwa utendakazi bora.
### Tatizo la 3: Changanua na Tathmini Usemi wa Hisabati
**Taarifa ya Tatizo:** Andika kichanganuzi ambacho huchukua mfuatano kama`"3 + 4 * 2 / (1 - 5)"`na kukitathmini kwa usahihi kuheshimu utangulizi na mabano ya opereta.
**Hatua ya 1 - Elewa Tatizo:**
Hii inahitaji: (1) kuweka alama kwa mfuatano wa ingizo kuwa nambari, waendeshaji, na mabano, (2) kuchanganua kwa utangulizi sahihi (`*`na`/`kabla ya`+`na`-`), (3) kushughulikia mabano yaliyowekwa. Tathmini isiyoeleweka kutoka kushoto kwenda kulia inaweza kutoa matokeo yasiyo sahihi.
**Hatua ya 2 — Tambua Mbinu:**
Suluhisho la kawaida ni **shunting-yard algoriti** (Dijkstra) ambayo hubadilisha infix kuwa postfix (Reverse Polish Notation), kisha kutathmini postfix. Vinginevyo, tumia kichanganuzi cha mteremko cha kujirudia. Kwa Python haswa, tunaweza pia kutumia`ast.literal_eval`kwa tathmini salama - lakini wacha tuitekeleze ipasavyo.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usahihi:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. Sahihi.
- Saa: O(N) ya kuweka tokeni, O(N) ya shunting-yard, O(N) ya kutathminiwa — kwa ujumla O(N).
- Kesi za kingo za kushughulikia: nambari hasi (tayarisha`0`kabla ya unary`-`), mgawanyiko kwa sufuri (ongeza ushughulikiaji wa hitilafu), ingizo batili (halalisha tokeni).
- Mbadala wa Pythonic:`ast.parse(expr, mode='eval')`na mgeni wa nodi maalum kwa tathmini salama bila`eval()`.
### Tatizo la 4: Tengeneza Dashibodi ya CLI yenye Masasisho ya Data ya Wakati Halisi
**Taarifa ya Tatizo:** Unda dashibodi ya msingi inayoonyesha vipimo vya mfumo (CPU, kumbukumbu, diski) inayosasishwa katika muda halisi, yenye vizingiti vilivyo na alama za rangi na mpangilio unaoitikia.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) ukusanyaji wa vipimo vya mfumo wa mara kwa mara, (2) uwasilishaji wa mwisho kwa kidhibiti cha kishale, (3) utoaji wa rangi kulingana na vizingiti, (4) uingizaji wa kibodi usiozuia ili kuacha. Huu ni muundo wa mzalishaji-watumiaji na kitanzi cha uwasilishaji.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`psutil`kwa vipimo vya mfumo wa majukwaa mtambuka.
- Tumia misimbo ya kutoroka ya ANSI kwa nafasi ya kishale na rangi (au maktaba ya`rich`kwa API ya kiwango cha juu).
- Tumia`time.sleep`kwa muda wa sasisho.
- Muundo kama: ukusanyaji wa data → uumbizaji → uwasilishaji bomba.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
-`cpu_percent(interval=0.5)`huzuia kwa sekunde 0.5 kupima — hii ndiyo njia sahihi (hali ya kutozuia inatoa 0% kwenye simu ya kwanza).
- Misimbo ya ANSI hufanya kazi kwenye Kituo cha kisasa cha Windows na vituo vyote vya Unix. Kwa urithi wa Windows cmd, ongeza`os.system('color')`au tumia`colorama`.
- Uboreshaji wa uzalishaji: tumia maktaba ya`rich`(`rich.live`) kwa uwasilishaji bila kufifia, mpangilio wa kiotomatiki, na uoanifu wa majukwaa mbalimbali.
- Upanuzi: kila kipimo ni chaguo la kukokotoa linalojitegemea, hivyo basi kurahisisha kuongeza halijoto ya GPU, hesabu ya michakato au miunganisho ya mtandao.
---

## Muhtasari
Mchanganyiko wa Python wa usomaji, unyumbulifu, na kina cha mfumo ikolojia huifanya kuwa lugha ya programu inayotumiwa zaidi ulimwenguni. Ni chaguo-msingi la AI/ML, chaguo dhabiti kwa usaidizi wa nyuma wa wavuti na uwekaji otomatiki, na lugha bora ya kufundishia. Udhaifu wake mkuu - kasi ya utekelezaji na usaidizi wa rununu / uliopachikwa - unaeleweka vizuri na umeanzisha suluhisho. Kwa miradi mingi, Python ni mahali pa kuanzia.