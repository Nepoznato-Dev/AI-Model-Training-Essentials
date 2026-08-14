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
#Python
Python adalah bahasa pemrograman tujuan umum tingkat tinggi, ditafsirkan, dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991. Python memprioritaskan keterbacaan kode melalui lekukan yang signifikan dan sintaksis bersih yang mirip dengan bahasa Inggris biasa. Python diketik secara dinamis, pengumpulan sampah, dan mendukung berbagai paradigma pemrograman termasuk pemrograman prosedural, berorientasi objek, dan fungsional.
Saat ini, Python adalah bahasa dominan dalam AI/ML, ilmu data, komputasi ilmiah, dan otomatisasi — namun tetap menjadi salah satu bahasa terbaik untuk pemula. Identitas ganda tersebut (cukup sederhana untuk skrip pertama, cukup kuat untuk melatih model bahasa besar) itulah yang membedakannya.
---

## Mengapa Python Penting
- **Keterbacaan berdasarkan desain**: Tanpa titik koma, tanpa kurung kurawal — lekukan menentukan cakupan. Kode dibaca seperti pseudocode.
- **Ekosistem besar**: PyPI menampung lebih dari 500.000 paket yang mencakup hampir semua domain.
- **Bahasa AI**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — seluruh tumpukan AI/ML mengutamakan Python.
- **Bahasa lem**: Hubungkan mesin C++ ke API web ke database hanya dalam beberapa baris.
- **Lintas platform**: Berjalan di Windows, macOS, Linux, dan sistem tertanam tanpa modifikasi.
- **Komunitas**: Komunitas pemrograman terbesar dan paling aktif di dunia.
## Pengorbanan
Python tidak sempurna. Memahami keterbatasannya membantu Anda memutuskan kapan harus melakukan sesuatu yang lain:
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Kecepatan eksekusi** | 10–100x lebih lambat dibandingkan C untuk tugas yang terikat CPU | Gunakan NumPy/PyTorch (C di bawah tenda), atau Cython/Numba untuk hot loop |
| **GIL (Kunci Penerjemah Global)** | Mencegah paralelisme multi-thread yang sebenarnya untuk pekerjaan yang terikat CPU | Gunakan`multiprocessing`,`asyncio`, atau antrian tugas seperti Celery |
| **Pengembangan seluler** | Tidak cocok untuk aplikasi iOS/Android | Gunakan Swift/Kotlin untuk native, atau Flutter/React Native untuk lintas platform |
| **Sistem tertanam** | Terlalu berat untuk mikrokontroler | Gunakan MicroPython (varian ringan) atau beralih ke C/Rust |
| **Penggunaan memori** | Jejak memori lebih tinggi dibandingkan bahasa yang dikompilasi | Dapat diterima untuk sebagian besar aplikasi; gunakan generator untuk data besar |
---

## Dasar Sintaks
### Variabel dan Tipe
Python menggunakan pengetikan dinamis — Anda tidak mendeklarasikan tipe variabel, namun Anda dapat menambahkan petunjuk tipe untuk kejelasan dan dukungan perkakas.
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

### Aliran Kontrol
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

### Fungsi
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

### Pemrograman Berorientasi Objek
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

### Penanganan Kesalahan
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

## Sintaks & Pola Tingkat Lanjut
### Generik dengan Modul `typing`
Modul`typing`Python menyediakan dukungan tipe generik untuk membangun komponen yang aman untuk digunakan kembali. Generik memungkinkan Anda menulis fungsi dan kelas yang bekerja dengan tipe apa pun sambil mempertahankan informasi tipe untuk analisis statis.
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

### Dekorator dan Metaprogramming
Dekorator adalah salah satu fitur Python yang paling canggih — fitur ini memungkinkan Anda memodifikasi atau memperluas perilaku fungsi dan kelas tanpa mengubah kode sumbernya.
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

### Pencocokan Pola Struktural (Python 3.10+)
Pernyataan`match/case`Python memberikan pencocokan pola yang kuat dengan destrukturisasi, penjaga, dan pola bersarang.
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

### Penutupan, Fungsi Tingkat Tinggi, dan Iterator
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

### Operator Kelebihan Beban
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

### Hirarki Pengecualian Khusus
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

## Fitur Utama Secara Mendalam
### Perpustakaan Standar ("Termasuk Baterai")
Python dikirimkan dengan perpustakaan standar yang luas. Beberapa modul yang paling sering digunakan:
| Modul | Tujuan | Contoh Penggunaan |
|--------|---------|-------------|
| `os`/`pathlib`| Operasi sistem file | `Path("data/output.csv").exists()`|
| `json`| Pengkodean/penguraian JSON | `json.loads(response_text)`|
| `datetime`| Penanganan tanggal dan waktu | `datetime.now(timezone.utc)`|
| `collections`| Wadah khusus | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Blok penyusun Iterator | `combinations(items, 2)`|
| `functools`| Alat fungsi | `lru_cache`,`partial`,`reduce`|
| `re`| Ekspresi reguler | `re.findall(r"\d+", text)`|
| `subprocess`| Jalankan perintah eksternal | `subprocess.run(["ls", "-la"])`|
| `logging`| Pencatatan aplikasi | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Ketik dukungan petunjuk | `Optional[str]`,`Union[int, float]`|
| `http.server`| Server HTTP sederhana | `python -m http.server 8000`|
| `threading`/`asyncio`| Konkurensi | I/O asinkron untuk pencakar web |
### Lingkungan Virtual dan Manajemen Paket
Setiap proyek Python harus menggunakan lingkungan virtual untuk mengisolasi dependensi:
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

Proyek Python modern semakin banyak menggunakan`pyproject.toml`dengan alat seperti`uv`,`poetry`, atau`hatch`untuk manajemen ketergantungan, menggantikan pendekatan`setup.py`/`requirements.txt`yang lebih lama.
### Pemrograman Asinkron
`asyncio` dari Python memungkinkan I/O bersamaan tanpa thread — penting untuk web scraper, server chat, dan klien API:
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

## Konkurensi & Paralelisme
Python menawarkan beberapa model konkurensi, masing-masing disesuaikan dengan beban kerja yang berbeda. GIL (Global Interpreter Lock) di CPython mencegah paralelisme CPU yang sebenarnya dengan thread, sehingga model yang tepat bergantung pada apakah beban kerja Anda terikat I/O atau terikat CPU.
### Threading (tugas terikat I/O)
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

### Multiprosesing (tugas yang terikat CPU)
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

### Asyncio Internal
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Direktori Proyek
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

### Konfigurasi Pembuatan — `pyproject.toml`
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

### Manajemen Ketergantungan dengan Alat Modern
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

### Linting dan Kualitas Kode
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### Saluran CI/CD — Tindakan GitHub
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

## Pengujian
### Kerangka Pengujian dan Penyiapan
Ekosistem pengujian Python berpusat pada`pytest`, standar de facto untuk pengujian Python.
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

### Pengujian Unit dengan pytest
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

### Tes Asinkron dan Tes Integrasi
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

## Interoperabilitas
### Memanggil C/C++ dengan ctypes
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

### Menggunakan cffi untuk Interop C yang Lebih Kompleks
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

### Cython — Python dengan Performa C
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

### Pybind11 — Ekstensi C++
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

## Pola Desain
### Lajang
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

### Pola Pabrik
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

### Pola Pengamat
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

### Pola Manajer Konteks
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

### Pola Strategi
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

## Kinerja & Optimasi
### Alat Pembuatan Profil
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

### Teknik Optimasi
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

### Pembandingan
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Penerapan
### Pengemasan dan Distribusi
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### File Docker
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

### Penerapan Khusus Platform
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

## Ekosistem
Kekuatan Python bukan hanya bahasanya — tapi juga ekosistem yang dibangun di sekitarnya.
### AI dan Pembelajaran Mesin
| Perpustakaan | Tujuan |
|---------|---------|
| PyTorch | Pembelajaran mendalam (penelitian dan produksi) |
| TensorFlow / Keras | Pembelajaran mendalam (berfokus pada produksi) |
| scikit-belajar | ML Klasik (regresi, pengelompokan, klasifikasi) |
| Memeluk Wajah Transformers | Model NLP/visi terlatih |
| LangChain / LlamaIndex | Membangun aplikasi dengan LLM |
| NomorPy | Komputasi numerik (array, aljabar linier) |
| Panda | Manipulasi dan analisis data |
| Matplotlib / Seaborn / Plotly | Visualisasi data |
### Pengembangan Web
| Kerangka | Gaya | Terbaik Untuk |
|-----------|-------|----------|
| Django | Tumpukan penuh, "termasuk baterai" | Aplikasi web kompleks dengan panel admin, ORM, auth |
| API Cepat | Modern, asinkron, berbasis tipe | API dan layanan mikro (saat ini yang paling cepat berkembang) |
| Labu | Minimal, fleksibel | Aplikasi kecil dan prototipe |
| Memperlancar | Berfokus pada aplikasi data | Dasbor dan demo data dengan Python murni |
### Otomatisasi dan Pembuatan Skrip
| Perpustakaan | Tujuan |
|---------|---------|
| `subprocess`/`os`| Administrasi sistem |
| `requests`/`httpx`| Klien HTTP |
| `BeautifulSoup`/`Scrapy`| Pengikisan web |
| `Selenium`/`Playwright`| Otomatisasi peramban |
| `Celery`| Antrian tugas terdistribusi |
| `Airflow`| Orkestrasi alur kerja |
### Komputasi Ilmiah
| Perpustakaan | Tujuan |
|---------|---------|
| NomorPy | Operasi array dan aljabar linier |
| Sains | Algoritma ilmiah (optimasi, pemrosesan sinyal) |
| SymPy | Matematika simbolik |
| Buku Catatan Jupyter | Lingkungan komputasi interaktif |
| JAX | Komputasi numerik berkinerja tinggi (dipercepat GPU) |
---

## Kapan Menggunakan Python
| Skenario | Mengapa Python | Alternatif Lebih Baik |
|----------|-----------|-------------------|
| AI/ML/Ilmu Data | Ekosistem tak tertandingi | — |
| Otomatisasi dan skrip | Tercepat untuk menulis dan men-debug | Shell/PowerShell untuk tugas sysadmin sederhana |
| Backend web (API) | FastAPI luar biasa | Gunakan atau Java untuk layanan dengan throughput yang sangat tinggi |
| Pembuatan Prototipe | Jalur tercepat dari ide ke kode kerja | — |
| Pendidikan | Bahasa paling ramah bagi pemula | — |
| Aplikasi desktop | Mungkin tapi jarang | C# (Windows), Swift (macOS) |
| Sistem yang kritis terhadap kinerja | Hindari — terlalu lambat | C, C++, Karat |
| Aplikasi seluler | Bukan alat yang tepat | Swift (iOS), Kotlin (Android) |
| Sistem tertanam | Terlalu banyak sumber daya | C, Rust, atau MicroPython untuk kasus sederhana |
---

## Versi Python
Bahasanya terus berkembang. Tambahan penting terkini:
| Versi | Tahun | Fitur Penting |
|---------|------|-----------------|
| 3.10 | 2021 | Pencocokan pola struktural (`match/case`), pesan kesalahan yang lebih baik |
| 3.11 | 2022 | Eksekusi 10–60% lebih cepat, penelusuran balik yang lebih baik |
| 3.12 | 2023 | F-string yang lebih fleksibel, pernyataan `type`, peningkatan kinerja |
| 3.13 | 2024 | Mode ulir bebas eksperimental (tanpa GIL), REPL | yang ditingkatkan
| 3.14 | 2025 | Perbaikan tanpa GIL lebih lanjut, ketik peningkatan sistem |
Python 2 mencapai akhir masa pakainya pada 1 Januari 2020. Semua proyek baru harus menggunakan Python 3.10 atau lebih baru.
---

## Referensi Cepat: Idiom Umum
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

## Tanya Jawab Sintetis
### Q1: Apa perbedaan antara daftar dan tupel, dan kapan saya harus menggunakannya?
**A:** Daftar dapat diubah (`[]`), tupel tidak dapat diubah (`()`). Gunakan daftar saat Anda perlu menambah, menghapus, atau mengubah elemen. Gunakan tupel untuk kumpulan data heterogen yang tetap, kunci kamus, nilai pengembalian fungsi, atau saat Anda ingin memberi sinyal "ini tidak boleh berubah". Tupel sedikit lebih hemat memori dan dapat digunakan sebagai kunci set/dict; daftar tidak bisa.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: Bagaimana Global Interpreter Lock (GIL) mempengaruhi kode saya, dan apa yang harus saya lakukan?
**A:** GIL mencegah beberapa thread mengeksekusi bytecode Python secara bersamaan, sehingga membuat threading tidak efektif untuk pekerjaan yang terikat dengan CPU. Untuk tugas terikat I/O (permintaan jaringan, file I/O),`threading`atau`asyncio`berfungsi dengan baik karena GIL dilepaskan selama I/O. Untuk tugas yang terikat dengan CPU, gunakan`multiprocessing`(proses terpisah, masing-masing dengan GIL-nya sendiri), atau pindahkan ke ekstensi C (NumPy, Cython, Numba) yang melepaskan GIL secara internal.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: Haruskah saya menggunakan petunjuk mengetik di mana saja? Apa saja trade-off praktisnya?
**A:** Petunjuk jenis (`def greet(name: str) -> str:`) bersifat opsional dan tidak diterapkan saat runtime. Mereka meningkatkan pelengkapan otomatis IDE, menangkap bug melalui alat analisis statis (mypy), dan maksud dokumen. Imbalannya adalah verbositas ekstra dan kurva pembelajaran untuk tipe tingkat lanjut (`Union`,`Generic`,`Protocol`). Rekomendasi: gunakan petunjuk tipe untuk tanda tangan fungsi di proyek apa pun yang melebihi ~500 baris; gunakan dengan hemat dalam skrip pendek. Aktifkan mypy di CI untuk penerapan bertahap.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: Apa praktik terbaik untuk menangani pengecualian dengan Python?
**A:** Tangkap pengecualian tertentu, bukan`except:`(yang juga menangkap`SystemExit`dan `KeyboardInterrupt`). Gunakan`try/except/else/finally`untuk memisahkan logika jalur bahagia dari penanganan kesalahan. Tentukan hierarki pengecualian khusus untuk perpustakaan. Jangan pernah menggunakan pengecualian untuk aliran kontrol dalam kode yang sensitif terhadap kinerja — pengecualian tersebut lambat. Catat pengecualian dengan`logging.exception()`untuk menangkap penelusuran balik penuh.
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

### Q5: Bagaimana cara generator menghemat memori, dan kapan saya harus menggunakannya pada daftar?
**A:** Generator menghasilkan nilai dengan lambat — satu per satu, sesuai permintaan — alih-alih membuat seluruh daftar di memori. Untuk kumpulan data besar (jutaan baris, urutan tak terbatas, streaming data), generator menggunakan memori konstan berapa pun ukurannya. Gunakan generator saat Anda mengulanginya sekali dan tidak memerlukan pengindeksan atau`len()`. Gunakan daftar saat Anda memerlukan akses acak, beberapa iterasi, atau koleksinya sedikit.
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

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membangun Penghitung Frekuensi Kata dengan Peringkat
**Pernyataan Masalah:** Dengan file teks berukuran besar, hitung frekuensi setiap kata, beri peringkat berdasarkan frekuensi (menurun), dan kembalikan hasil N teratas. Tangani ketidakpekaan huruf besar-kecil, tanda baca, dan proses file yang terlalu besar secara efisien untuk dimasukkan ke dalam memori.
**Langkah 1 — Pahami Masalahnya:**
Kita perlu: (1) membaca teks, (2) membagi menjadi beberapa kata, (3) menormalkan huruf besar/kecil, (4) menghapus tanda baca, (5) menghitung kemunculan, (6) mengurutkan berdasarkan hitungan secara menurun, (7) mengembalikan N teratas. Batasan "terlalu besar untuk dimasukkan ke dalam memori" berarti kita harus memproses baris demi baris dengan generator.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`re.finditer`untuk ekstraksi kata yang efisien tanpa membuat daftar perantara.
- Gunakan`collections.Counter`untuk kenaikan O(1) per kata.
- Gunakan`Counter.most_common(n)`yang menggunakan heap secara internal — O(k log n) dan bukan O(n log n) untuk pengurutan penuh.
- Proses baris demi baris melalui generator untuk menjaga memori tetap konstan.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Memori: hanya dict Counter yang ada di memori (satu entri per kata unik), bukan konten file. Untuk teks bahasa Inggris, ~100 ribu kata unik ≈ beberapa MB.
- Waktu: O(W) untuk memindai semua kata + O(U log N) untuk ekstraksi N teratas, di mana W = total kata, U = kata unik.
- Kasus tepi: apostrof dalam kontraksi ("jangan") dipertahankan oleh regex. Teks unicode memerlukan tanda`re.UNICODE`atau pola yang berbeda.
### Masalah 2: Menerapkan Cache LRU yang Aman untuk Thread
**Pernyataan Masalah:** Buat cache yang Paling Sedikit Terakhir Digunakan (LRU) dari awal yang aman untuk thread, mendukung operasi pengambilan dan penempatan O(1), dan secara otomatis mengeluarkan item yang paling jarang digunakan saat kapasitas terlampaui.
**Langkah 1 — Pahami Masalahnya:**
Cache LRU memerlukan: (1) pencarian cepat berdasarkan kunci → peta hash, (2) pengurutan cepat berdasarkan keterkinian → daftar tertaut ganda, (3) keamanan thread → penguncian. Pada`get(key)`: pindahkan item ke depan. Pada`put(key, val)`: masukkan di depan; jika melebihi kapasitas, keluarkan dari belakang.
**Langkah 2 — Identifikasi Pendekatannya:**
-`dict`Python mempertahankan urutan penyisipan (3.7+), sehingga kita dapat menggunakan pendekatan dict yang dipesan: hapus dan masukkan kembali untuk berpindah ke akhir.
- Untuk keamanan thread, gunakan`threading.Lock`untuk saling mengecualikan.
- Alternatif: gunakan`collections.OrderedDict`yang memiliki`move_to_end()`.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Kompleksitas waktu: O(1) untuk`get`dan`put`—`OrderedDict.move_to_end()`dan`popitem()`adalah O(1).
- Keamanan benang:`Lock`memastikan atomisitas. Untuk throughput yang lebih tinggi, pertimbangkan`threading.RLock`atau pola kunci baca-tulis, namun untuk sebagian besar kasus penggunaan, kunci sederhana sudah cukup.
- Catatan produksi: untuk kode thread tunggal,`functools.lru_cache`lebih sederhana dan diimplementasikan dalam C untuk kinerja yang lebih baik.
### Soal 3: Mengurai dan Mengevaluasi Ekspresi Matematika
**Pernyataan Masalah:** Tulis parser yang menggunakan string seperti`"3 + 4 * 2 / (1 - 5)"`dan mengevaluasinya dengan benar berdasarkan prioritas operator dan tanda kurung.
**Langkah 1 — Pahami Masalahnya:**
Hal ini memerlukan: (1) membuat tokenisasi string masukan menjadi angka, operator, dan tanda kurung, (2) penguraian dengan prioritas yang benar (`*`dan`/`sebelum`+`dan`-`), (3) menangani tanda kurung bertumpuk. Evaluasi kiri-ke-kanan yang naif akan memberikan hasil yang salah.
**Langkah 2 — Identifikasi Pendekatannya:**
Solusi klasiknya adalah **algoritma shunting-yard** (Dijkstra) yang mengubah infiks menjadi postfix (Reverse Polish Notation), lalu mengevaluasi postfix. Alternatifnya, gunakan parser keturunan rekursif. Khusus untuk Python, kita juga dapat menggunakan`ast.literal_eval`untuk evaluasi yang aman — tetapi mari kita terapkan dengan benar.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Kebenaran:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. Benar.
- Waktu: O(N) untuk tokenisasi, O(N) untuk shunting-yard, O(N) untuk evaluasi — keseluruhan O(N).
- Kasus tepi yang harus ditangani: angka negatif (tambahkan`0`sebelum unary`-`), pembagian dengan nol (tambahkan penanganan kesalahan), masukan tidak valid (validasi token).
- Alternatif Pythonic:`ast.parse(expr, mode='eval')`dengan pengunjung node khusus untuk evaluasi aman tanpa`eval()`.
### Masalah 4: Membangun Dasbor CLI dengan Pembaruan Data Waktu Nyata
**Pernyataan Masalah:** Buat dasbor berbasis terminal yang menampilkan pembaruan metrik sistem (CPU, memori, disk) secara real-time, dengan ambang batas berkode warna dan tata letak responsif.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) pengumpulan metrik sistem periodik, (2) rendering terminal dengan kontrol kursor, (3) keluaran warna berdasarkan ambang batas, (4) masukan keyboard non-pemblokiran untuk keluar. Ini adalah pola produsen-konsumen dengan loop rendering.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`psutil`untuk metrik sistem lintas platform.
- Gunakan kode escape ANSI untuk posisi kursor dan warna (atau pustaka`rich`untuk API tingkat yang lebih tinggi).
- Gunakan`time.sleep`untuk interval pembaruan.
- Struktur sebagai: pengumpulan data → pemformatan → pipa rendering.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
-`cpu_percent(interval=0.5)`memblokir selama 0,5 detik untuk diukur — ini adalah pendekatan yang benar (mode non-pemblokiran memberikan 0% pada panggilan pertama).
- Kode ANSI berfungsi pada Terminal Windows modern dan semua terminal Unix. Untuk cmd Windows lawas, tambahkan`os.system('color')`atau gunakan`colorama`.
- Peningkatan produksi: gunakan pustaka`rich`(`rich.live`) untuk rendering bebas kedipan, tata letak otomatis, dan kompatibilitas lintas platform.
- Ekstensibilitas: setiap metrik merupakan fungsi independen, sehingga memudahkan penambahan suhu GPU, jumlah proses, atau koneksi jaringan.
---

## Ringkasan
Kombinasi Python antara keterbacaan, keserbagunaan, dan kedalaman ekosistem menjadikannya bahasa pemrograman yang paling banyak digunakan di dunia. Ini adalah pilihan default untuk AI/ML, opsi kuat untuk backend dan otomatisasi web, serta bahasa pengajaran yang sangat baik. Kelemahan utamanya — kecepatan eksekusi dan dukungan seluler/tersemat — telah dipahami dengan baik dan telah memiliki solusi yang pasti. Untuk sebagian besar proyek, Python adalah titik awal yang masuk akal.