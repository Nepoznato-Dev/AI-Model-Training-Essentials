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

＃ Python
Python 是一種高階解釋型通用程式語言，由 Guido van Rossum 創建，於 1991 年首次發布。它透過顯著的縮排和讀起來接近簡單英語的乾淨語法來優先考慮程式碼的可讀性。 Python 是動態類型的、垃圾收集的，並且支援多種程式設計範式，包括過程式設計、物件導向程式設計和函數式程式設計。
如今，Python 是人工智慧/機器學習、資料科學、科學計算和自動化領域的主導語言，同時仍然是初學者的最佳語言之一。這種雙重身分（對於第一個腳本來說足夠簡單，對於訓練大型語言模型來說足夠強大）是它的與眾不同之處。
---

## 為什麼 Python 很重要
- **設計的可讀性**：沒有分號，沒有大括號 - 縮排定義範圍。程式碼讀起來就像偽代碼。
- **龐大的生態系統**：PyPI 託管超過 500,000 個包，幾乎涵蓋每個領域。
- **AI 語言**：PyTorch、TensorFlow、scikit-learn、Hugging Face、LangChain — 整個 AI/ML 堆疊都是 Python 優先。
- **膠水語言**：只需幾行即可將 C++ 引擎連接到 Web API 和資料庫。
- **跨平台**：無需修改即可在 Windows、macOS、Linux 和嵌入式系統上運作。
- **社群**：世界上最大、最活躍的程式設計社群。
## 權衡
Python 並不完美。了解其限制可以幫助您決定何時尋求其他東西：
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **執行速度** |對於 CPU 密集型任務，比 C 慢 10-100 倍 |使用 NumPy/PyTorch（底層 C）或 Cython/Numba 進行熱循環 |
| **GIL（全域解釋器鎖定）** |阻止 CPU 密集型工作的真正多執行緒並行性 |使用`multiprocessing`、`asyncio`或任務佇列，如 Celery |
| **行動開發** |不適合 iOS/Android 應用程式 |使用 Swift/Kotlin 進行原生，或使用 Flutter/React Native 進行跨平台 |
| **嵌入式系統** |對於微控制器來說太重了|使用 MicroPython（輕量級變體）或切換到 C/Rust |
| **記憶體使用情況** |比編譯語言更高的記憶體佔用 |大多數應用程式都可以接受；使用生成器處理大數據 |
---

## 文法基礎知識
### 變數和類型
Python 使用動態類型 — 您無需宣告變數類型，但可以新增類型提示以提高清晰度和工具支援。
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

### 控制流程
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

### 函數
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

### 物件導向編程
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

### 錯誤處理
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

## 進階語法和模式
### 帶有`typing`模組的泛型
Python 的`typing`模組為建構可重複使用、類型安全的元件提供通用型別支援。泛型可讓您編寫適用於任何類型的函數和類，同時保留類型資訊以進行靜態分析。
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

### 裝飾器和元編程
裝飾器是 Python 最強大的功能之一 - 它們允許您修改或擴展函數和類別的行為，而無需更改其原始程式碼。
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

### 結構模式匹配 (Python 3.10+)
Python 的`match/case`語句提供了強大的模式匹配與解構、保護和巢狀模式。
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

### 閉包、高階函數與迭代器
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

### 運算子重載
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

### 自訂異常層次結構
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

## 深入了解主要功能
### 標準庫（「包含電池」）
Python 附帶了一個廣泛的標準函式庫。一些最常用的模組：
|模組|目的|使用範例 |
|--------|---------|-------------|
|`os`/`pathlib`|檔案系統操作|`Path("data/output.csv").exists()`|
|`json`| JSON 編碼/解碼 |`json.loads(response_text)`|
|`datetime`|日期與時間處理 |`datetime.now(timezone.utc)`|
|`collections`|特種貨櫃| `Counter(words)`、`defaultdict(list)` |
|`itertools`|迭代器建構塊 |`combinations(items, 2)`|
|`functools`|功能工具| `lru_cache`、`partial`、`reduce` |
|`re`|正規表示式 |`re.findall(r"\d+", text)`|
|`subprocess`|執行外部命令 |`subprocess.run(["ls", "-la"])`|
|`logging`|應用程式日誌記錄 |`logging.basicConfig(level=logging.INFO)`|
|`typing`|類型提示支援 | `Optional[str]`、`Union[int, float]` |
|`http.server`|簡單的HTTP伺服器|`python -m http.server 8000`|
|`threading`/`asyncio`|並發 |網路爬蟲的非同步 I/O |
### 虛擬環境與套件管理
每個Python專案都應該使用虛擬環境來隔離依賴關係：
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

現代 Python 專案越來越多地使用`pyproject.toml`以及`uv`、`poetry`或`hatch`等工具進行依賴項管理，取代舊的`setup.py`/`requirements.txt`方法。
### 非同步編程
Python 的`asyncio`支援無執行緒並發 I/O — 對於網頁抓取工具、聊天伺服器和 API 用戶端至關重要：
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

## 並發與平行
Python 提供了多種並發模型，每個模型都適合不同的工作負載。 CPython 中的 GIL（全域解釋器鎖定）會阻止真正的 CPU 與執行緒並行，因此正確的模型取決於您的工作負載是 I/O 密集型還是 CPU 密集型。
### 執行緒（I/O 密集型任務）
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

### 多處理（CPU 密集型任務）
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

### Asyncio 內部結構
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

## 專案配置與建置系統
### 專案目錄結構
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

### 建置配置 — `pyproject.toml`
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

### 使用現代工具進行依賴管理
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

### Linting 和程式碼品質
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD 管道 — GitHub Actions
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

## 測試
### 測試框架和設置
Python 的測試生態系統以`pytest`為中心，這是 Python 測試的事實標準。
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

### 使用 pytest 進行單元測試
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

### 非同步測試和整合測試
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

## 互通性
### 使用 ctypes 呼叫 C/C++
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

### 使用 cffi 實作更複雜的 C 互通
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

### Cython — 具有 C 效能的 Python
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

### Pybind11 — C++ 擴展
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

## 設計模式
### 單例
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

### 工廠模式
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

### 觀察者模式
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

### 上下文管理器模式
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

### 策略模式
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

## 效能與最佳化
### 分析工具
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

### 優化技術
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

### 基準測試
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## 部署
### 包裝和分發
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

### 特定於平台的部署
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

## 生態系統
Python 的優點不僅在於語言，還在於圍繞它建構的生態系統。
### 人工智慧與機器學習
|圖書館 |目的|
|---------|---------|
| PyTorch |深度學習（研究與生產）|
| TensorFlow / Keras |深度學習（以生產為中心）|
| scikit 學習 |經典機器學習（迴歸、聚類、分類）|
|擁抱變形金剛|預訓練的 NLP/視覺模型 |
| LangChain/LlamaIndex |與法學碩士建構應用程式 |
| NumPy |數值計算（陣列、線性代數）|
|熊貓 |資料處理與分析|
| Matplotlib / Seaborn / Plotly | Matplotlib / Seaborn / Plotly | Matplotlib資料視覺化|
### 網頁開發
|框架|風格|最適合 |
|------------|--------|----------|
|姜戈 |全棧，「含電池」 |具有管理面板、ORM、身份驗證的複雜 Web 應用程式 |
|快速API |現代、非同步、類型驅動 | API 和微服務（目前成長最快）|
|燒瓶 |最小、靈活 |小型應用程式和原型 |
|串流光 |專注於資料應用 |純 Python 中的儀表板與資料示範 |
### 自動化和腳本
|圖書館 |目的|
|---------|---------|
|`subprocess`/`os`|系統管理|
|`requests`/`httpx`| HTTP 用戶端 |
|`BeautifulSoup`/`Scrapy`|網頁擷取 |
|`Selenium`/`Playwright`|瀏覽器自動化 |
|`Celery`|分散式任務佇列|
|`Airflow`|工作流程編排|
### 科學計算
|圖書館 |目的|
|---------|---------|
| NumPy |陣列運算與線性代數 |
| SciPy |科學演算法（最佳化、訊號處理）|
|症狀|符號數學|
| Jupyter 筆記本 |互動式運算環境|
|賈克斯|高效能數值運算（GPU 加速）|
---

## 何時使用 Python
|場景|為什麼選擇Python？更好的選擇|
|----------|----------|--------------------|
|人工智慧/機器學習/資料科學 |生態系統無與倫比| — |
|自動化和腳本編寫|最快的編寫和調試 |用於簡單系統管理任務的 Shell/PowerShell |
| Web 後端 (API) | FastAPI 很優秀 | Go 或 Java 用於非常高吞吐量的服務 |
|原型製作 |從想法到工作程式碼的最快路徑 | — |
|教育 |最適合初學者的語言 | — |
|桌面應用程式|可能但不常見 | C# (Windows)、Swift (macOS) |
|效能關鍵型系統 |避免－太慢| C、C++、Rust |
|行動應用程式 |沒有合適的工具 | Swift (iOS)、Kotlin (Android) |
|嵌入式系統|資源消耗太大 |用於簡單情況的 C、Rust 或 MicroPython |
---

## Python 版本
語言在不斷發展。最近新增的主要內容：
|版本 |年份|顯著特徵|
|---------|------|-----------------|
| 3.10 | 3.10 2021 |結構模式匹配 (`match/case`)，更好的錯誤訊息 |
| 3.11 | 3.11 2022 | 2022執行速度提高 10–60%，改進回溯 |
| 3.12 | 3.12 2023 |更靈活的 f 字串、`type` 語句、效能提升 |
| 3.13 | 2024 | 2024實驗性自由線程模式（無 GIL），改進的 REPL |
| 3.14 | 3.14 2025 | 2025進一步的 no-GIL 改進、類型系統增強 |
Python 2 已於 2020 年 1 月 1 日終止生命。所有新專案都應使用 Python 3.10 或更高版本。
---

## 快速參考：常見慣用語
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

## 綜合問答
### Q1：列表和元組有什麼區別，什麼時候應該使用它們？
**A:** 清單是可變的 (`[]`)，元組是不可變的 (`()`)。當您需要新增、刪除或變更元素時，請使用清單。將元組用於異質資料、字典鍵、函數傳回值的固定集合，或當您想要表示「這不應該改變」時。元組的記憶體效率稍高，可以用作 set/dict 鍵；列表不能。
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2：全域解釋器鎖定（GIL）如何影響我的程式碼，我該怎麼辦？
**答：** GIL 可防止多個執行緒同時執行 Python 字節碼，使執行緒對於 CPU 密集型工作無效。對於 I/O 密集型任務（網路請求、檔案 I/O），`threading` 或`asyncio`可以正常運作，因為 GIL 在 I/O 期間被釋放。對於 CPU 密集型任務，請使用 `multiprocessing`（單獨的進程，每個進程都有自己的 GIL），或卸載到在內部釋放 GIL 的 C 擴充（NumPy、Cython、Numba）。
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3：我應該在任何地方使用類型提示嗎？實際的權衡是什麼？
**A:** 類型提示 (`def greet(name: str) -> str:`) 是可選的，並且在執行時不強制執行。它們改進了 IDE 自動完成、透過靜態分析工具 (mypy) 捕獲錯誤以及記錄意圖。代價是額外的冗長和高級類型的學習曲線（`Union`、`Generic`、`Protocol`）。建議：在任何超過 500 行的項目中對函數簽名使用類型提示；在簡短的腳本中謹慎使用它們。在 CI 中啟用 mypy 以逐步執行。
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4：Python 中處理異常的最佳實踐是什麼？
**答：** 捕獲特定異常，而不是純粹的 `except:`（它也捕獲`SystemExit`和 `KeyboardInterrupt`）。使用`try/except/else/finally`將快樂路徑邏輯與錯誤處理分開。為庫定義自訂異常層次結構。永遠不要在性能敏感的程式碼中使用異常來控制流——它們很慢。使用`logging.exception()`記錄異常以捕獲完整的回溯。
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

### Q5：生成器如何節省內存，什麼時候應該在列表上使用它們？
**答：** 生成器會延遲生成值（一次一個，按需生成），而不是在記憶體中建立整個列表。對於大型資料集（數百萬行、無限序列、流資料），生成器使用恆定內存，無論大小如何。當您迭代一次並且不需要索引或`len()`時，請使用生成器。當您需要隨機存取、多次迭代或集合較小時，請使用清單。
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

## 解決問題的思路
### 問題 1：建立帶有排名的詞頻計數器
**問題陳述：**給定一個大的文本文件，統計每個單字的頻率，按頻率進行排名（降序），並返回前 N 個結果。處理不區分大小寫、標點符號的問題，並有效處理太大而無法放入記憶體的檔案。
**第 1 步 — 了解問題：**
我們需要：(1) 讀取文本，(2) 拆分為單詞，(3) 大小寫標準化，(4) 去掉標點符號，(5) 計算出現次數，(6) 按計數降序排序，(7) 返回前 N 個。 「太大而無法放入記憶體」約束意味著我們應該使用生成器逐行處理。
**第 2 步 — 確定方法：**
- 使用`re.finditer`進行高效的單字擷取，無需建立中間清單。
- 使用`collections.Counter`實作每個字的 O(1) 增量。
- 使用 `Counter.most_common(n)`，它在內部使用堆疊 - O(k log n) 而不是 O(n log n) 進行完全排序。
- 透過生成器逐行處理以保持記憶體恆定。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 記憶體：記憶體中只有計數器字典（每個唯一單字一個條目），而不是檔案內容。對於英文文本，~100K 唯一單字 ≈ 幾 MB。
- 時間：掃描所有單字的 O(W) + 用於前 N 個提取的 O(U log N)，其中 W = 總單詞，U = 唯一單字。
- 邊緣情況：正規表示式保留縮寫中的撇號（「不」）。 Unicode 文字需要`re.UNICODE`標誌或不同的模式。
### 問題 2：實作執行緒安全的 LRU 快取
**問題陳述：** 從頭開始建立一個執行緒安全的最近最少使用（LRU）緩存，支援 O(1) 的 get 和 put 操作，並在超出容量時自動逐出最近最少使用的項目。
**第 1 步 — 了解問題：**
LRU 快取需要：(1) 按鍵快速尋找 → 雜湊映射，(2) 快速以新近度排序 → 雙鍊錶，(3) 執行緒安全 → 鎖定。在`get(key)`上：將專案移到前面。在`put(key, val)`上：插入在前面；如果超出容量，請從背面移除。
**第 2 步 — 確定方法：**
- Python 的`dict`保持插入順序（3.7+），因此我們可以使用有序字典方法：刪除並重新插入以移動到末尾。
- 為了線程安全，使用`threading.Lock`進行互斥。
- 替代方案：使用具有`move_to_end()`的`collections.OrderedDict`。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 时间复杂度：`get` 和`put`均为 O(1) —`OrderedDict.move_to_end()`和`popitem()`均为 O(1)。
- 线程安全：`Lock` 确保原子性。为了获得更高的吞吐量，请考虑`threading.RLock`或读写锁定模式，但对于大多数用例，简单的锁定就足够了。
- 生产说明：对于单线程代码，`functools.lru_cache` 更简单并用 C 实现以获得更好的性能。
### 問題 3：解析與評估數學表達式
**問題陳述：** 編寫一個解析器，它接受像`"3 + 4 * 2 / (1 - 5)"`這樣的字串，並根據運算子優先權和括號正確地評估它。
**第 1 步 — 了解問題：**
這需要：(1) 將輸入字串標記為數字、運算子和括號，(2) 以正確的優先權進行解析（`*`和`/`在`+`和`-`之前），(3) 處理巢號。幼稚的從左到右的評估會給出錯誤的結果。
**第 2 步 — 確定方法：**
經典的解決方案是**調車場演算法**（Dijkstra），它將中綴轉換為後綴（逆波蘭表示法），然後評估後綴。或者，使用遞歸下降解析器。特別是對於 Python，我們還可以使用`ast.literal_eval`進行安全評估 - 但讓我們正確實現它。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 正確性：`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`。正確的。
- 時間：標記化 O(N)、調車場 O(N)、評估 O(N) — 總體 O(N)。
- 要處理的邊緣情況：負數（在一元`-`之前加上`0`）、除以零（新增錯誤處理）、無效輸入（驗證標記）。
- Pythonic 替代方案：`ast.parse(expr, mode='eval')`具有自訂節點訪客，可在沒有`eval()`的情況下進行安全評估。
### 問題 4：建立具有即時資料更新的 CLI 儀表板
**問題陳述：** 建立一個基於終端的儀表板，顯示即時更新的系統指標（CPU、記憶體、磁碟），並具有顏色編碼的閾值和響應式佈局。
**第 1 步 — 了解問題：**
我們需要：（1）定期系統度量收集，（2）帶有遊標控制的終端渲染，（3）基於閾值的顏色輸出，（4）用於退出的非阻塞鍵盤輸入。这是带有渲染循环的生产者-消费者模式。
**第 2 步 — 確定方法：**
- 使用`psutil`進行跨平台系統指標。
- 使用 ANSI 轉義碼進行遊標定位和顏色（或使用`rich`函式庫實作更高階的 API）。
- 使用`time.sleep`作為更新間隔。
- 結構為：資料收集→格式化→渲染管線。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
-`cpu_percent(interval=0.5)`阻塞 0.5 秒進行測量 — 這是正確的方法（非阻塞模式在第一次呼叫時給出 0%）。
- ANSI 程式碼適用於現代 Windows 終端機和所有 Unix 終端機。對於舊版 Windows cmd，請新增`os.system('color')`或使用`colorama`。
- 生產升級：使用`rich`函式庫 (`rich.live`) 實作無閃爍渲染、自動佈局和跨平台相容性。
- 可擴展性：每個指標都是獨立的函數，可以輕鬆添加 GPU 溫度、進程數或網路連接。
---

＃＃ 概括
Python 兼具可讀性、多功能性和生態系統深度，使其成為世界上使用最廣泛的程式語言。它是 AI/ML 的預設選擇，是 Web 後端和自動化的強大選擇，也是一種出色的教學語言。它的主要弱點——執行速度和行動/嵌入式支援——是眾所周知的，並且已經建立了解決方法。對於大多數專案來說，Python 是一個合理的起點。