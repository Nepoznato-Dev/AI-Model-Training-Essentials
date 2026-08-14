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
# Python
Python là ngôn ngữ lập trình cấp cao, được diễn giải, có mục đích chung do Guido van Rossum tạo ra và phát hành lần đầu tiên vào năm 1991. Python ưu tiên khả năng đọc mã thông qua khả năng thụt lề đáng kể và cú pháp rõ ràng, đọc gần giống tiếng Anh đơn giản. Python được gõ động, thu thập rác và hỗ trợ nhiều mô hình lập trình bao gồm lập trình thủ tục, hướng đối tượng và chức năng.
Ngày nay, Python là ngôn ngữ thống trị trong AI/ML, khoa học dữ liệu, máy tính khoa học và tự động hóa - đồng thời vẫn là một trong những ngôn ngữ tốt nhất cho người mới bắt đầu. Bản sắc kép đó (đủ đơn giản cho tập lệnh đầu tiên, đủ mạnh để huấn luyện các mô hình ngôn ngữ lớn) là điều làm nên sự khác biệt của nó.
---

## Tại sao Python lại quan trọng
- **Khả năng đọc theo thiết kế**: Không có dấu chấm phẩy, không có dấu ngoặc nhọn — thụt lề xác định phạm vi. Mã đọc giống như mã giả.
- **Hệ sinh thái khổng lồ**: PyPI lưu trữ hơn 500.000 gói bao gồm hầu hết mọi miền.
- **Ngôn ngữ của AI**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — toàn bộ nền tảng AI/ML đều ưu tiên Python.
- **Ngôn ngữ keo**: Kết nối công cụ C++ với API web với cơ sở dữ liệu chỉ trong vài dòng.
- **Đa nền tảng**: Chạy trên Windows, macOS, Linux và các hệ thống nhúng mà không cần sửa đổi.
- **Cộng đồng**: Cộng đồng lập trình lớn nhất và tích cực nhất trên thế giới.
## Sự đánh đổi
Python không hoàn hảo. Hiểu được những hạn chế của nó sẽ giúp bạn quyết định khi nào nên tiếp cận thứ khác:
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Tốc độ thực hiện** | Chậm hơn 10–100 lần so với C đối với các tác vụ liên quan đến CPU | Sử dụng NumPy/PyTorch (C dưới mui xe) hoặc Cython/Numba cho các vòng lặp nóng |
| **GIL (Khóa thông dịch toàn cầu)** | Ngăn chặn sự song song đa luồng thực sự cho công việc liên quan đến CPU | Sử dụng`multiprocessing`,`asyncio`hoặc hàng đợi nhiệm vụ như Celery |
| **Phát triển di động** | Không phù hợp với ứng dụng iOS/Android | Sử dụng Swift/Kotlin cho bản gốc hoặc Flutter/React Native cho đa nền tảng |
| **Hệ thống nhúng** | Quá nặng đối với vi điều khiển | Sử dụng MicroPython (một biến thể nhẹ) hoặc chuyển sang C/Rust |
| **Sử dụng bộ nhớ** | Dung lượng bộ nhớ cao hơn các ngôn ngữ được biên dịch | Có thể chấp nhận được đối với hầu hết các ứng dụng; sử dụng máy phát điện cho dữ liệu lớn |
---

##Cơ bản về cú pháp
### Biến và kiểu
Python sử dụng kiểu gõ động - bạn không khai báo các kiểu biến, nhưng bạn có thể thêm gợi ý kiểu để làm rõ và hỗ trợ công cụ.
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

### Luồng điều khiển
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

### Chức năng
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

### Lập trình hướng đối tượng
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

### Xử lý lỗi
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

## Cú pháp & Mẫu nâng cao
### Generics với Mô-đun `typing`
Mô-đun`typing`của Python cung cấp hỗ trợ kiểu chung để xây dựng các thành phần an toàn, có thể tái sử dụng. Generics cho phép bạn viết các hàm và lớp hoạt động với bất kỳ loại nào trong khi vẫn giữ nguyên thông tin loại để phân tích tĩnh.
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

### Công cụ trang trí và lập trình meta
Trình trang trí là một trong những tính năng mạnh mẽ nhất của Python — chúng cho phép bạn sửa đổi hoặc mở rộng hành vi của các hàm và lớp mà không cần thay đổi mã nguồn của chúng.
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

### Khớp mẫu cấu trúc (Python 3.10+)
Câu lệnh`match/case`của Python cung cấp khả năng khớp mẫu mạnh mẽ với các mẫu phá hủy, bảo vệ và mẫu lồng nhau.
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

### Closure, hàm bậc cao hơn và Iterator
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

### Quá tải toán tử
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

### Phân cấp ngoại lệ tùy chỉnh
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

## Các tính năng chính về chiều sâu
### Thư viện tiêu chuẩn ("Đã bao gồm pin")
Python có một thư viện tiêu chuẩn phong phú. Một số module được sử dụng nhiều nhất:
| Mô-đun | Mục đích | Ví dụ sử dụng |
|--------|----------|-------------|
| `os`/`pathlib`| Hoạt động của hệ thống tập tin | `Path("data/output.csv").exists()`|
| `json`| Mã hóa/giải mã JSON | `json.loads(response_text)`|
| `datetime`| Xử lý ngày giờ | `datetime.now(timezone.utc)`|
| `collections`| Thùng chứa chuyên dụng | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Khối xây dựng Iterator | `combinations(items, 2)`|
| `functools`| Công cụ chức năng | `lru_cache`,`partial`,`reduce`|
| `re`| Biểu thức chính quy | `re.findall(r"\d+", text)`|
| `subprocess`| Chạy lệnh bên ngoài | `subprocess.run(["ls", "-la"])`|
| `logging`| Ghi nhật ký ứng dụng | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Gõ gợi ý hỗ trợ | `Optional[str]`,`Union[int, float]`|
| `http.server`| Máy chủ HTTP đơn giản | `python -m http.server 8000`|
| `threading`/`asyncio`| Đồng thời | I/O không đồng bộ cho người dọn dẹp web |
### Môi trường ảo và quản lý gói
Mọi dự án Python nên sử dụng môi trường ảo để tách biệt các phần phụ thuộc:
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

Các dự án Python hiện đại ngày càng sử dụng`pyproject.toml`với các công cụ như`uv`,`poetry`hoặc`hatch`để quản lý phần phụ thuộc, thay thế cho phương pháp `setup.py`/`requirements.txt` cũ hơn.
### Lập trình không đồng bộ
`asyncio` của Python cho phép I/O đồng thời không có luồng — cần thiết cho người quét web, máy chủ trò chuyện và ứng dụng khách API:
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

## Đồng thời & Song song
Python cung cấp một số mô hình tương tranh, mỗi mô hình phù hợp với khối lượng công việc khác nhau. GIL (Khóa phiên dịch toàn cầu) trong CPython ngăn chặn sự song song thực sự của CPU với các luồng, do đó, mô hình phù hợp sẽ phụ thuộc vào việc khối lượng công việc của bạn là giới hạn I/O hay giới hạn CPU.
### Phân luồng (tác vụ giới hạn I/O)
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

### Đa xử lý (tác vụ liên quan đến CPU)
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

### Nội bộ Asyncio
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc thư mục dự án
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

### Cấu hình bản dựng — `pyproject.toml`
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

### Quản lý phụ thuộc bằng các công cụ hiện đại
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

### Linting và chất lượng mã
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### Đường dẫn CI/CD — Hành động GitHub
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

##Thử nghiệm
### Khung kiểm tra và thiết lập
Hệ sinh thái thử nghiệm của Python xoay quanh `pytest`, tiêu chuẩn thực tế cho thử nghiệm Python.
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

### Unit Test với pytest
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

### Kiểm tra không đồng bộ và kiểm tra tích hợp
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

## Khả năng tương tác
### Gọi C/C++ bằng ctypes
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

### Sử dụng cffi cho Tương tác C phức tạp hơn
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

### Cython — Python với hiệu năng C
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

### Pybind11 — Phần mở rộng C++
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

## Mẫu thiết kế
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

### Mẫu nhà máy
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

### Mẫu người quan sát
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

### Mẫu trình quản lý bối cảnh
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

### Mẫu chiến lược
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

### Kỹ thuật tối ưu hóa
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

### Đo điểm chuẩn
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Triển khai
### Đóng gói và phân phối
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

###Tệp Docker
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

### Triển khai theo nền tảng cụ thể
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

## Hệ sinh thái
Sức mạnh của Python không chỉ ở ngôn ngữ — mà còn là hệ sinh thái được xây dựng xung quanh nó.
### AI và Học máy
| Thư viện | Mục đích |
|----------|----------|
| PyTorch | Học sâu (nghiên cứu và sản xuất) |
| TensorFlow / Keras | Học sâu (tập trung vào sản xuất) |
| scikit-tìm hiểu | ML cổ điển (hồi quy, phân cụm, phân loại) |
| Ôm Mặt Transformers | Các mô hình tầm nhìn/NLP được đào tạo trước |
| LangChain / LlamaIndex | Xây dựng ứng dụng với LLM |
| NumPy | Tính toán số (mảng, đại số tuyến tính) |
| Gấu trúc | Thao tác và phân tích dữ liệu |
| Matplotlib / Seaborn / Plotly | Trực quan hóa dữ liệu |
### Phát triển Web
| Khung | Phong cách | Tốt nhất cho |
|----------|-------|----------|
| Django | Toàn bộ, "bao gồm pin" | Ứng dụng web phức tạp với bảng quản trị, ORM, auth |
| FastAPI | Hiện đại, không đồng bộ, định hướng kiểu | API và microservice (hiện đang phát triển nhanh nhất) |
| Bình | Tối thiểu, linh hoạt | Ứng dụng nhỏ và nguyên mẫu |
| Tinh giản | Tập trung vào ứng dụng dữ liệu | Bảng thông tin và trình diễn dữ liệu bằng Python thuần túy |
### Tự động hóa và viết kịch bản
| Thư viện | Mục đích |
|----------|----------|
| `subprocess`/`os`| Quản trị hệ thống |
| `requests`/`httpx`| Máy khách HTTP |
| `BeautifulSoup`/`Scrapy`| Quét web |
| `Selenium`/`Playwright`| Tự động hóa trình duyệt |
| `Celery`| Hàng đợi nhiệm vụ phân tán |
| `Airflow`| Điều phối quy trình làm việc |
### Tính toán khoa học
| Thư viện | Mục đích |
|----------|----------|
| NumPy | Phép toán mảng và đại số tuyến tính |
| SciPy | Thuật toán khoa học (tối ưu, xử lý tín hiệu) |
| SymPy | Toán biểu tượng |
| Máy tính xách tay Jupyter | Môi trường điện toán tương tác |
| JAX | Điện toán số hiệu năng cao (tăng tốc GPU) |
---

## Khi nào nên sử dụng Python
| Kịch bản | Tại sao Python | Thay thế tốt hơn |
|----------|-------------|-------------------|
| AI/ML/Khoa học dữ liệu | Hệ sinh thái có một không hai | — |
| Tự động hóa và viết kịch bản | Viết và gỡ lỗi nhanh nhất | Shell/PowerShell cho các tác vụ quản trị hệ thống đơn giản |
| Phần phụ trợ web (API) | FastAPI thật tuyệt vời | Go hoặc Java cho các dịch vụ có thông lượng rất cao |
| Tạo nguyên mẫu | Con đường nhanh nhất từ ​​ý tưởng đến mã hoạt động | — |
| Giáo dục | Ngôn ngữ thân thiện với người mới bắt đầu nhất | — |
| Ứng dụng máy tính để bàn | Có thể nhưng không phổ biến | C# (Windows), Swift (macOS) |
| Hệ thống quan trọng về hiệu suất | Tránh - quá chậm | C, C++, Rust |
| Ứng dụng di động | Không phải là công cụ phù hợp | Swift (iOS), Kotlin (Android) |
| Hệ thống nhúng | Quá nặng tài nguyên | C, Rust hoặc MicroPython cho các trường hợp đơn giản |
---

## Phiên bản Python
Ngôn ngữ tiếp tục phát triển. Những bổ sung quan trọng gần đây:
| Phiên bản | Năm | Tính năng nổi bật |
|----------|------|-----------------|
| 3.10 | 2021 | Khớp mẫu cấu trúc (`match/case`), thông báo lỗi tốt hơn |
| 3.11 | 2022 | Thực thi nhanh hơn 10–60%, truy nguyên được cải thiện |
| 3.12 | 2023 | Chuỗi f linh hoạt hơn, câu lệnh `type`, tăng hiệu suất |
| 3.13 | 2024 | Chế độ luồng tự do thử nghiệm (không có GIL), REPL được cải tiến |
| 3.14 | 2025 | Cải tiến thêm không có GIL, cải tiến hệ thống loại |
Python 2 đã hết vòng đời vào ngày 1 tháng 1 năm 2020. Tất cả các dự án mới nên sử dụng Python 3.10 trở lên.
---

## Tham khảo nhanh: Thành ngữ thông dụng
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

## Hỏi đáp tổng hợp
### Câu hỏi 1: Sự khác biệt giữa danh sách và bộ dữ liệu là gì và khi nào tôi nên sử dụng từng bộ dữ liệu?
**A:** Danh sách có thể thay đổi (`[]`), bộ dữ liệu không thể thay đổi (`()`). Sử dụng danh sách khi bạn cần thêm, xóa hoặc thay đổi thành phần. Sử dụng bộ dữ liệu cho các bộ sưu tập cố định gồm dữ liệu không đồng nhất, khóa từ điển, giá trị trả về của hàm hoặc khi bạn muốn báo hiệu "điều này sẽ không thay đổi". Các bộ dữ liệu tiết kiệm bộ nhớ hơn một chút và có thể được sử dụng làm khóa set/dict; danh sách không thể.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Câu 2: Khóa phiên dịch toàn cầu (GIL) ảnh hưởng đến mã của tôi như thế nào và tôi nên làm gì với nó?
**A:** GIL ngăn nhiều luồng thực thi đồng thời mã byte Python, khiến luồng không hiệu quả đối với công việc liên quan đến CPU. Đối với các tác vụ liên quan đến I/O (yêu cầu mạng, tệp I/O),`threading`hoặc`asyncio`hoạt động tốt vì GIL được giải phóng trong I/O. Đối với các tác vụ liên quan đến CPU, hãy sử dụng`multiprocessing`(các quy trình riêng biệt, mỗi quy trình có GIL riêng) hoặc giảm tải cho các tiện ích mở rộng C (NumPy, Cython, Numba) để phát hành GIL nội bộ.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Câu 3: Tôi có nên sử dụng gợi ý kiểu ở mọi nơi không? Sự đánh đổi thực tế là gì?
**A:** Gợi ý loại (`def greet(name: str) -> str:`) là tùy chọn và không được thực thi khi chạy. Chúng cải thiện khả năng tự động hoàn thành của IDE, phát hiện lỗi thông qua các công cụ phân tích tĩnh (mypy) và mục đích ghi lại tài liệu. Sự đánh đổi là tính chi tiết hơn và đường cong học tập cho các loại nâng cao (`Union`,`Generic`,`Protocol`). Khuyến nghị: sử dụng gợi ý loại cho chữ ký hàm trong bất kỳ dự án nào trên ~500 dòng; sử dụng chúng một cách tiết kiệm trong các đoạn văn ngắn. Kích hoạt mypy trong CI để thực thi dần dần.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Câu hỏi 4: Các phương pháp hay nhất để xử lý ngoại lệ trong Python là gì?
**A:** Nắm bắt các trường hợp ngoại lệ cụ thể thay vì`except:`thông thường (bắt cả`SystemExit`và `KeyboardInterrupt`). Sử dụng`try/except/else/finally`để tách logic đường dẫn hạnh phúc khỏi việc xử lý lỗi. Xác định hệ thống phân cấp ngoại lệ tùy chỉnh cho thư viện. Không bao giờ sử dụng ngoại lệ cho luồng điều khiển trong mã nhạy cảm với hiệu suất - chúng chậm. Ghi lại ngoại lệ bằng`logging.exception()`để ghi lại toàn bộ dấu vết.
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

### Câu hỏi 5: Trình tạo tiết kiệm bộ nhớ như thế nào và khi nào tôi nên sử dụng chúng trên danh sách?
**A:** Trình tạo tạo ra các giá trị một cách lười biếng — mỗi lần một giá trị, theo yêu cầu — thay vì tạo toàn bộ danh sách trong bộ nhớ. Đối với các tập dữ liệu lớn (hàng triệu hàng, chuỗi vô hạn, truyền dữ liệu), trình tạo sử dụng bộ nhớ không đổi bất kể kích thước. Sử dụng trình tạo khi bạn lặp lại một lần và không cần lập chỉ mục hoặc`len()`. Sử dụng danh sách khi bạn cần truy cập ngẫu nhiên, lặp lại nhiều lần hoặc bộ sưu tập nhỏ.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Bài toán 1: Xây dựng bộ đếm tần số từ có xếp hạng
**Báo cáo vấn đề:** Cho một tệp văn bản lớn, đếm tần suất của mỗi từ, xếp hạng chúng theo tần suất (giảm dần) và trả về N kết quả hàng đầu. Xử lý trường hợp không phân biệt chữ hoa chữ thường, dấu câu và xử lý hiệu quả các tệp quá lớn để vừa với bộ nhớ.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng ta cần: (1) đọc văn bản, (2) chia thành các từ, (3) chuẩn hóa kiểu chữ, (4) tách dấu câu, (5) đếm số lần xuất hiện, (6) sắp xếp theo số đếm giảm dần, (7) trả về đầu N. Ràng buộc "quá lớn để vừa trong bộ nhớ" có nghĩa là chúng ta nên xử lý từng dòng một bằng các trình tạo.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`re.finditer`để trích xuất từ hiệu quả mà không cần xây dựng danh sách trung gian.
- Sử dụng`collections.Counter`để tăng O(1) cho mỗi từ.
- Sử dụng`Counter.most_common(n)`sử dụng vùng nhớ heap nội bộ — O(k log n) thay vì O(n log n) để sắp xếp đầy đủ.
- Xử lý từng dòng thông qua trình tạo để giữ cho bộ nhớ không đổi.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Bộ nhớ: chỉ có Counter dict trong bộ nhớ (một mục nhập cho mỗi từ duy nhất), không phải nội dung tệp. Đối với văn bản tiếng Anh, ~100K từ duy nhất ≈ vài MB.
- Thời gian: O(W) quét tất cả các từ + O(U log N) để trích xuất top-N, trong đó W = tổng số từ, U = các từ duy nhất.
- Các trường hợp cạnh: dấu nháy đơn trong cách viết tắt ("không") được giữ nguyên bởi biểu thức chính quy. Văn bản Unicode sẽ cần cờ`re.UNICODE`hoặc một mẫu khác.
### Vấn đề 2: Triển khai Bộ nhớ đệm LRU an toàn theo luồng
**Báo cáo vấn đề:** Xây dựng bộ đệm ít được sử dụng gần đây nhất (LRU) từ đầu, an toàn theo luồng, hỗ trợ các thao tác lấy và đặt O(1), đồng thời tự động loại bỏ mục ít được sử dụng gần đây nhất khi vượt quá dung lượng.
**Bước 1 — Tìm hiểu vấn đề:**
Bộ đệm LRU cần: (1) tra cứu nhanh theo khóa → bản đồ băm, (2) sắp xếp nhanh theo lần truy cập gần đây → danh sách liên kết đôi, (3) an toàn luồng → khóa. Trên`get(key)`: di chuyển mục lên phía trước. Trên`put(key, val)`: chèn ở phía trước; nếu vượt quá dung lượng, hãy tháo ra từ phía sau.
**Bước 2 — Xác định phương pháp tiếp cận:**
-`dict`của Python duy trì thứ tự chèn (3.7+), vì vậy chúng ta có thể sử dụng cách tiếp cận chính tả theo thứ tự: xóa và chèn lại để chuyển về cuối.
- Để đảm bảo an toàn cho luồng, hãy sử dụng`threading.Lock`để loại trừ lẫn nhau.
- Cách khác: sử dụng`collections.OrderedDict`có`move_to_end()`.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Độ phức tạp về thời gian: O(1) đối với cả`get`và`put`—`OrderedDict.move_to_end()`và`popitem()`đều là O(1).
- An toàn chỉ:`Lock`đảm bảo tính nguyên tử. Để có thông lượng cao hơn, hãy xem xét`threading.RLock`hoặc mẫu khóa đọc-ghi, nhưng đối với hầu hết các trường hợp sử dụng, chỉ cần một khóa đơn giản là đủ.
- Ghi chú sản xuất: đối với mã đơn luồng,`functools.lru_cache`đơn giản hơn và được triển khai trong C để có hiệu suất tốt hơn.
### Bài 3: Phân tích và tính biểu thức toán học
**Báo cáo vấn đề:** Viết một trình phân tích cú pháp lấy một chuỗi như`"3 + 4 * 2 / (1 - 5)"`và đánh giá chính xác chuỗi đó theo thứ tự ưu tiên của toán tử và dấu ngoặc đơn.
**Bước 1 — Tìm hiểu vấn đề:**
Điều này yêu cầu: (1) mã hóa chuỗi đầu vào thành số, toán tử và dấu ngoặc đơn, (2) phân tích cú pháp với mức độ ưu tiên chính xác (`*`và`/`trước`+`và`-`), (3) xử lý các dấu ngoặc đơn lồng nhau. Đánh giá ngây thơ từ trái sang phải sẽ cho kết quả sai.
**Bước 2 — Xác định phương pháp tiếp cận:**
Giải pháp cổ điển là **thuật toán shunting-yard** (Dijkstra) chuyển đổi tiền tố thành hậu tố (Ký hiệu tiếng Ba Lan đảo ngược), sau đó đánh giá hậu tố đó. Ngoài ra, hãy sử dụng trình phân tích cú pháp gốc đệ quy. Đối với Python cụ thể, chúng ta cũng có thể sử dụng`ast.literal_eval`để đánh giá an toàn - nhưng hãy triển khai nó đúng cách.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Độ chính xác:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→ `1.0`. Chính xác.
- Thời gian: O(N) để mã hóa, O(N) cho sân shunt, O(N) để đánh giá — tổng thể là O(N).
- Các trường hợp cạnh cần xử lý: số âm (thêm`0`trước`-`đơn phân), chia cho 0 (thêm xử lý lỗi), đầu vào không hợp lệ (xác thực mã thông báo).
- Giải pháp thay thế Pythonic:`ast.parse(expr, mode='eval')`với trình truy cập nút tùy chỉnh để đánh giá an toàn mà không cần `eval()`.
### Vấn đề 4: Xây dựng Bảng điều khiển CLI với cập nhật dữ liệu theo thời gian thực
**Báo cáo sự cố:** Tạo trang tổng quan dựa trên thiết bị đầu cuối hiển thị các số liệu hệ thống (CPU, bộ nhớ, ổ đĩa) cập nhật theo thời gian thực, với các ngưỡng được mã hóa màu và bố cục phản hồi.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) thu thập số liệu hệ thống định kỳ, (2) kết xuất thiết bị đầu cuối với điều khiển con trỏ, (3) đầu ra màu dựa trên ngưỡng, (4) đầu vào bàn phím không chặn để thoát. Đây là mẫu nhà sản xuất-người tiêu dùng có vòng lặp kết xuất.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`psutil`cho các số liệu hệ thống đa nền tảng.
- Sử dụng mã thoát ANSI để định vị con trỏ và màu sắc (hoặc thư viện`rich`cho API cấp cao hơn).
- Sử dụng`time.sleep`cho khoảng thời gian cập nhật.
- Cấu trúc như: thu thập dữ liệu → định dạng → đường dẫn kết xuất.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Đo khối`cpu_percent(interval=0.5)`trong 0,5 giây - đây là cách tiếp cận đúng (chế độ không chặn mang lại 0% cho cuộc gọi đầu tiên).
- Mã ANSI hoạt động trên Windows Terminal hiện đại và tất cả các thiết bị đầu cuối Unix. Đối với cmd Windows cũ, hãy thêm`os.system('color')`hoặc sử dụng`colorama`.
- Nâng cấp sản xuất: sử dụng thư viện`rich`(`rich.live`) để hiển thị không nhấp nháy, bố cục tự động và khả năng tương thích đa nền tảng.
- Khả năng mở rộng: mỗi số liệu là một chức năng độc lập, giúp dễ dàng thêm nhiệt độ GPU, số lượng quy trình hoặc kết nối mạng.
---

## Bản tóm tắt
Sự kết hợp giữa khả năng đọc, tính linh hoạt và chiều sâu hệ sinh thái của Python khiến nó trở thành ngôn ngữ lập trình được sử dụng rộng rãi nhất trên thế giới. Đây là lựa chọn mặc định cho AI/ML, một lựa chọn mạnh mẽ cho phần phụ trợ và tự động hóa web, đồng thời là ngôn ngữ giảng dạy xuất sắc. Điểm yếu chính của nó — tốc độ thực thi và hỗ trợ di động/nhúng — đã được hiểu rõ và đã có giải pháp giải quyết. Đối với hầu hết các dự án, Python là điểm khởi đầu hợp lý.