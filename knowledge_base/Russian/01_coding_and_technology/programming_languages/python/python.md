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

# Питон
Python — это высокоуровневый интерпретируемый язык программирования общего назначения, созданный Гвидо ван Россумом и впервые выпущенный в 1991 году. В нем приоритет отдается читаемости кода благодаря значительным отступам и чистому синтаксису, который читается близко к простому английскому языку. Python является динамически типизированным, со сборщиком мусора и поддерживает несколько парадигм программирования, включая процедурное, объектно-ориентированное и функциональное программирование.
Сегодня Python является доминирующим языком в области искусственного интеллекта и машинного обучения, науки о данных, научных вычислений и автоматизации, оставаясь при этом одним из лучших языков для начинающих. Эта двойная идентичность (достаточно простая для первого сценария и достаточно мощная для обучения больших языковых моделей) и отличает его от других.
---

## Почему Python важен
- **Удобочитаемость задумана**: никаких точек с запятой и фигурных скобок — отступы определяют область действия. Код читается как псевдокод.
- **Огромная экосистема**: на PyPI размещено более 500 000 пакетов, охватывающих практически все домены.
- **Язык искусственного интеллекта**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — весь стек искусственного интеллекта и машинного обучения ориентирован на Python.
- **Связывающий язык**: подключите движок C++ к веб-API и базе данных всего за несколько строк.
- **Кроссплатформенность**: работает на Windows, macOS, Linux и встроенных системах без изменений.
- **Сообщество**: самое большое и активное сообщество программистов в мире.
## Компромиссы
Питон не идеален. Понимание его ограничений поможет вам решить, когда следует обратиться к чему-то другому:
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Скорость выполнения** | В 10–100 раз медленнее, чем C, для задач, связанных с процессором | Используйте NumPy/PyTorch (C под капотом) или Cython/Numba для горячих циклов |
| **GIL (глобальная блокировка интерпретатора)** | Предотвращает настоящий многопоточный параллелизм при работе с нагрузкой на ЦП | Используйте `multiprocessing`,`asyncio`или очереди задач, такие как Celery |
| **Мобильная разработка** | Не подходит для приложений iOS/Android | Используйте Swift/Kotlin для нативной разработки или Flutter/React Native для кроссплатформенности |
| **Встроенные системы** | Слишком тяжел для микроконтроллеров | Используйте MicroPython (облегчённый вариант) или переключитесь на C/Rust |
| **Использование памяти** | Больший объем памяти, чем у компилируемых языков | Приемлемо для большинства приложений; использовать генераторы для больших данных |
---

## Основы синтаксиса
### Переменные и типы
Python использует динамическую типизацию — вы не объявляете типы переменных, но можете добавлять подсказки по типам для ясности и поддержки инструментов.
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

### Поток управления
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

### Функции
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

### Объектно-ориентированное программирование
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

### Обработка ошибок
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

## Расширенный синтаксис и шаблоны
### дженерики с модулем `typing`
Модуль Python`typing`обеспечивает поддержку общих типов для создания повторно используемых типобезопасных компонентов. Обобщенные шаблоны позволяют писать функции и классы, которые работают с любым типом, сохраняя при этом информацию о типе для статического анализа.
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

### Декораторы и метапрограммирование
Декораторы — одна из самых мощных функций Python — они позволяют изменять или расширять поведение функций и классов без изменения их исходного кода.
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

### Сопоставление структурных шаблонов (Python 3.10+)
Оператор Python`match/case`обеспечивает мощное сопоставление шаблонов с деструктуризацией, защитой и вложенными шаблонами.
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

### Замыкания, функции высшего порядка и итераторы
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

### Перегрузка оператора
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

### Пользовательские иерархии исключений
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

## Ключевые особенности в деталях
### Стандартная библиотека («Батарейки в комплекте»)
Python поставляется с обширной стандартной библиотекой. Некоторые из наиболее часто используемых модулей:
| Модуль | Цель | Пример использования |
|--------|---------|-------------|
| `os`/`pathlib`| Операции с файловой системой | `Path("data/output.csv").exists()`|
| `json`| Кодирование/декодирование JSON | `json.loads(response_text)`|
| `datetime`| Обработка даты и времени | `datetime.now(timezone.utc)`|
| `collections`| Специализированные контейнеры | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Строительные блоки итератора | `combinations(items, 2)`|
| `functools`| Функциональные инструменты | `lru_cache`,`partial`,`reduce`|
| `re`| Регулярные выражения | `re.findall(r"\d+", text)`|
| `subprocess`| Запуск внешних команд | `subprocess.run(["ls", "-la"])`|
| `logging`| Регистрация приложений | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Поддержка подсказок типа | `Optional[str]`,`Union[int, float]`|
| `http.server`| Простой HTTP-сервер | `python -m http.server 8000`|
| `threading`/`asyncio`| Параллельность | Асинхронный ввод-вывод для парсеров |
### Виртуальные среды и управление пакетами
Каждый проект Python должен использовать виртуальную среду для изоляции зависимостей:
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

Современные проекты Python все чаще используют`pyproject.toml`с такими инструментами, как `uv`,`poetry`или`hatch`для управления зависимостями, заменяя старый подход `setup.py`/`requirements.txt`.
### Асинхронное программирование
`asyncio` в Python обеспечивает одновременный ввод-вывод без потоков, что важно для веб-скребков, серверов чата и клиентов API:
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

## Параллелизм и параллелизм
Python предлагает несколько моделей параллелизма, каждая из которых подходит для разных рабочих нагрузок. GIL (глобальная блокировка интерпретатора) в CPython предотвращает настоящий параллелизм ЦП с потоками, поэтому правильная модель зависит от того, связана ли ваша рабочая нагрузка с операциями ввода-вывода или с ЦП.
### Threading (задачи, связанные с вводом-выводом)
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

### Многопроцессорность (задачи, связанные с процессором)
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

### Внутреннее устройство Asyncio
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

## Конфигурация проекта и система сборки
### Структура каталога проекта
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

### Конфигурация сборки — `pyproject.toml`
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

### Управление зависимостями с помощью современных инструментов
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

### Линтинг и качество кода
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### Конвейер CI/CD — Действия GitHub
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

## Тестирование
### Платформы и настройка тестирования
Экосистема тестирования Python сосредоточена вокруг `pytest`, фактического стандарта тестирования Python.
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

### Юнит-тесты с pytest
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

### Асинхронные тесты и интеграционные тесты
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

## Совместимость
### Вызов C/C++ с помощью ctypes
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

### Использование cffi для более сложного взаимодействия с C
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

### Cython — Python с производительностью C
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

### Pybind11 — Расширения C++
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

## Шаблоны проектирования
### Синглтон
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

### Фабричный шаблон
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

### Шаблон наблюдателя
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

### Шаблон диспетчера контекста
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

### Шаблон стратегии
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

## Производительность и оптимизация
### Инструменты профилирования
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

### Методы оптимизации
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

### Бенчмаркинг
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Развертывание
### Упаковка и распространение
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### Докер-файл
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

### Развертывание для конкретной платформы
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

## Экосистема
Сила Python не только в языке, но и в построенной вокруг него экосистеме.
### ИИ и машинное обучение
| Библиотека | Цель |
|---------|---------|
| ПиТорч | Глубокое обучение (исследования и производство) |
| TensorFlow/Керас | Глубокое обучение (ориентированное на производство) |
| обучение-обучение | Классический МО (регрессия, кластеризация, классификация) |
| Трансформеры с обнимающим лицом | Предварительно обученные модели НЛП/видения |
| LangChain / ЛамаИндекс | Создание приложений с помощью LLM |
| NumPy | Численные вычисления (массивы, линейная алгебра) |
| Панды | Обработка и анализ данных |
| Matplotlib/Seaborn/Plotly | Визуализация данных |
### Веб-разработка
| Рамочная | Стиль | Лучшее для |
|-----------|-------|----------|
| Джанго | Полный стек, «батарейки в комплекте» | Сложные веб-приложения с админ-панелями, ORM, авторизацией |
| ФастAPI | Современный, асинхронный, управляемый типами | API и микросервисы (на данный момент наиболее быстрорастущие) |
| Колба | Минимальный, гибкий | Маленькие приложения и прототипы |
| Стримлит | Ориентирован на приложения для передачи данных | Панели мониторинга и демонстрации данных на чистом Python |
### Автоматизация и сценарии
| Библиотека | Цель |
|---------|---------|
| `subprocess`/`os`| Системное администрирование |
| `requests`/`httpx`| HTTP-клиенты |
| `BeautifulSoup`/`Scrapy`| Парсинг веб-страниц |
| `Selenium`/`Playwright`| Автоматизация браузера |
| `Celery`| Распределенные очереди задач |
| `Airflow`| Оркестровка рабочего процесса |
### Научные вычисления
| Библиотека | Цель |
|---------|---------|
| NumPy | Операции с массивами и линейная алгебра |
| Научный | Научные алгоритмы (оптимизация, обработка сигналов) |
| СимПи | Символьная математика |
| Ноутбук Jupyter | Интерактивная вычислительная среда |
| ДЖАКС | Высокопроизводительные численные вычисления (с графическим процессором) |
---

## Когда использовать Python
| Сценарий | Почему Питон | Лучшая альтернатива |
|----------|-----------|-------------------|
| ИИ/МО/Наука о данных | Экосистема не имеет себе равных | — |
| Автоматизация и создание сценариев | Самый быстрый в написании и отладке | Shell/PowerShell для простых задач системного администратора |
| Веб-серверы (API) | FastAPI превосходен | Go или Java для сервисов с очень высокой пропускной способностью |
| Прототипирование | Кратчайший путь от идеи к рабочему коду | — |
| Образование | Самый удобный для начинающих язык | — |
| Настольные приложения | Возможно, но редко | C# (Windows), Swift (macOS) |
| Системы, критичные к производительности | Избегайте — слишком медленно | Си, С++, Руст |
| Мобильные приложения | Не тот инструмент | Swift (iOS), Котлин (Android) |
| Встраиваемые системы | Слишком ресурсоёмкий | C, Rust или MicroPython для простых случаев |
---

## Версии Python
Язык продолжает развиваться. Основные недавние дополнения:
| Версия | Год | Примечательные особенности |
|---------|------|-----------------|
| 3.10 | 2021 | Структурное сопоставление шаблонов (`match/case`), улучшенные сообщения об ошибках |
| 3.11 | 2022 | Выполнение на 10–60 % быстрее, улучшенная обратная трассировка |
| 3.12 | 2023 | Более гибкие f-строки, оператор `type`, повышение производительности |
| 3.13 | 2024 | Экспериментальный режим без GIL, улучшенный REPL |
| 3.14 | 2025 | Дальнейшие улучшения без GIL, улучшения системы типов |
Срок службы Python 2 истек 1 января 2020 года. Все новые проекты должны использовать Python 3.10 или более позднюю версию.
---

## Краткий справочник: распространенные идиомы
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

## Синтетические вопросы и ответы
### Вопрос 1. В чем разница между списками и кортежами и когда следует использовать каждый из них?
**A:** Списки изменяемы (`[]`), кортежи неизменяемы (`()`). Используйте списки, когда вам нужно добавить, удалить или изменить элементы. Используйте кортежи для фиксированных коллекций разнородных данных, ключей словаря, возвращаемых значений функций или когда вы хотите подать сигнал «это не должно меняться». Кортежи немного более эффективны с точки зрения использования памяти и могут использоваться в качестве ключей set/dict; списки не могут.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Вопрос 2: Как глобальная блокировка интерпретатора (GIL) влияет на мой код и что мне с этим делать?
**A:** GIL не позволяет нескольким потокам одновременно выполнять байт-код Python, что делает многопоточность неэффективной для работы с нагрузкой на процессор. Для задач, связанных с вводом-выводом (сетевые запросы, файловый ввод-вывод),`threading`или`asyncio`работают нормально, поскольку GIL освобождается во время ввода-вывода. Для задач, связанных с ЦП, используйте`multiprocessing`(отдельные процессы, каждый со своим собственным GIL) или выгружайте расширения C (NumPy, Cython, Numba), которые освобождают GIL внутри себя.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### В3: Стоит ли везде использовать подсказки типов? Каковы практические компромиссы?
**A:** Подсказки типов (`def greet(name: str) -> str:`) являются необязательными и не применяются во время выполнения. Они улучшают автодополнение IDE, выявляют ошибки с помощью инструментов статического анализа (mypy) и документируют намерения. Компромиссом является дополнительная многословность и необходимость обучения расширенным типам (`Union`,`Generic`,`Protocol`). Рекомендация: используйте подсказки типов для сигнатур функций в любом проекте длиной ~500 строк; используйте их экономно в коротких сценариях. Включите mypy в CI для постепенного внедрения.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Вопрос 4. Каковы наилучшие методы обработки исключений в Python?
**A:** Перехватывайте конкретные исключения, а не простой`except:`(который также перехватывает`SystemExit`и `KeyboardInterrupt`). Используйте `try/except/else/finally`, чтобы отделить логику счастливого пути от обработки ошибок. Определите пользовательские иерархии исключений для библиотек. Никогда не используйте исключения для потока управления в коде, чувствительном к производительности — они работают медленно. Зарегистрируйте исключение с помощью `logging.exception()`, чтобы получить полную обратную трассировку.
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

### В5: Как генераторы экономят память и когда их следует использовать вместо списков?
**О:** Генераторы лениво создают значения — по одному, по требованию — вместо того, чтобы создавать в памяти целый список. Для больших наборов данных (миллионы строк, бесконечные последовательности, потоковые данные) генераторы используют постоянную память независимо от размера. Используйте генераторы, когда вы выполняете одиночную итерацию и вам не нужна индексация или `len()`. Используйте списки, когда вам нужен произвольный доступ, несколько итераций или если коллекция небольшая.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создайте счетчик частоты слов с ранжированием
**Постановка задачи:** Учитывая большой текстовый файл, подсчитайте частоту каждого слова, ранжируйте их по частоте (по убыванию) и верните N первых результатов. Обеспечьте нечувствительность к регистру и пунктуации, а также эффективно обрабатывайте файлы, слишком большие для размещения в памяти.
**Шаг 1. Поймите проблему:**
Нам нужно: (1) прочитать текст, (2) разбить на слова, (3) нормализовать регистр, (4) удалить знаки препинания, (5) подсчитать вхождения, (6) отсортировать по убыванию количества, (7) вернуть верхнее N. Ограничение «слишком велико, чтобы поместиться в памяти» означает, что мы должны обрабатывать построчно с помощью генераторов.
**Шаг 2. Определите подход:**
- Используйте`re.finditer`для эффективного извлечения слов без построения промежуточных списков.
- Используйте`collections.Counter`для приращения O(1) на слово.
- Используйте `Counter.most_common(n)`, который использует внутреннюю кучу — O(k log n) вместо O(n log n) для полной сортировки.
- Обработка построчно с помощью генератора для поддержания постоянной памяти.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Память: в памяти находится только счетчик счетчиков (одна запись на уникальное слово), а не содержимое файла. Для текста на английском языке ~100 тыс. уникальных слов — несколько МБ.
- Время: O(W) для сканирования всех слов + O(U log N) для извлечения первых N слов, где W = общее количество слов, U = уникальные слова.
- Краевые случаи: апострофы в сокращениях («не») сохраняются регулярным выражением. Для текста в Юникоде потребуется флаг`re.UNICODE`или другой шаблон.
### Проблема 2: реализация потокобезопасного LRU-кэша
**Постановка проблемы:** Создайте с нуля наименее недавно используемый кэш (LRU), который является потокобезопасным, поддерживает операции получения и размещения O(1) и автоматически удаляет наименее использованный элемент при превышении емкости.
**Шаг 1. Поймите проблему:**
Кэш LRU требует: (1) быстрого поиска по ключу → хэш-карты, (2) быстрого упорядочения по давности → двусвязный список, (3) потокобезопасности → блокировки. На `get(key)`: переместите элемент на передний план. На `put(key, val)`: вставьте спереди; если емкость превышает емкость, снимите ее со спины.
**Шаг 2. Определите подход:**
—`dict`в Python поддерживает порядок вставки (3.7+), поэтому мы можем использовать упорядоченный подход: удалить и повторно вставить, чтобы перейти к концу.
- Для обеспечения безопасности потоков используйте`threading.Lock`для взаимного исключения.
- Альтернатива: используйте `collections.OrderedDict`, который имеет`move_to_end()`.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Временная сложность: O(1) для`get`и`put`—`OrderedDict.move_to_end()`и`popitem()`равны O(1).
- Безопасность потоков:`Lock`обеспечивает атомарность. Для более высокой пропускной способности рассмотрите`threading.RLock`или шаблон блокировки чтения-записи, но для большинства случаев использования достаточно простой блокировки.
- Производственное примечание: для однопоточного кода`functools.lru_cache`проще и реализован на C для повышения производительности.
### Проблема 3. Анализ и вычисление математического выражения
**Постановка задачи.** Напишите анализатор, который принимает строку типа`"3 + 4 * 2 / (1 - 5)"`и правильно оценивает ее с учетом приоритета операторов и круглых скобок.
**Шаг 1. Поймите проблему:**
Для этого требуется: (1) разбить входную строку на числа, операторы и круглые скобки, (2) выполнить синтаксический анализ с правильным приоритетом (`*` и`/`перед`+`и `-`), (3) обработать вложенные круглые скобки. Наивная оценка слева направо дала бы неправильные результаты.
**Шаг 2. Определите подход:**
Классическим решением является **алгоритм сортировочной станции** (Дийкстра), который преобразует инфикс в постфикс (обратная польская нотация), а затем оценивает постфикс. В качестве альтернативы используйте анализатор рекурсивного спуска. В частности, для Python мы также можем использовать`ast.literal_eval`для безопасной оценки, но давайте реализуем это правильно.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Правильность:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. Правильный.
- Время: O(N) для токенизации, O(N) для маневровой станции, O(N) для оценки — всего O(N).
— Краевые случаи для обработки: отрицательные числа (добавьте`0`перед унарным `-`), деление на ноль (добавьте обработку ошибок), недопустимый ввод (проверьте токены).
— Pythonic альтернатива:`ast.parse(expr, mode='eval')`с пользовательским посетителем узла для безопасной оценки без `eval()`.
### Проблема 4. Создание информационной панели CLI с обновлением данных в реальном времени
**Постановка задачи:** Создайте панель мониторинга на базе терминала, которая отображает обновление системных показателей (ЦП, памяти, диска) в режиме реального времени, с пороговыми значениями с цветовой кодировкой и адаптивным макетом.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) периодический сбор системных показателей, (2) рендеринг терминала с управлением курсором, (3) вывод цвета на основе пороговых значений, (4) неблокирующий ввод с клавиатуры для выхода. Это шаблон производитель-потребитель с циклом рендеринга.
**Шаг 2. Определите подход:**
- Используйте`psutil`для метрик кросс-платформенной системы.
- Используйте escape-коды ANSI для позиционирования курсора и цветов (или библиотеку`rich`для API более высокого уровня).
- Используйте`time.sleep`для интервала обновления.
- Структура как: сбор данных → форматирование → конвейер рендеринга.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
-`cpu_percent(interval=0.5)`блокируется на 0,5 секунды для измерения — это правильный подход (неблокирующий режим дает 0% при первом вызове).
- Коды ANSI работают на современных терминалах Windows и всех терминалах Unix. Для устаревшего cmd Windows добавьте`os.system('color')`или используйте`colorama`.
- Обновление производства: используйте библиотеку`rich`(`rich.live`) для рендеринга без мерцания, автоматического макета и кроссплатформенной совместимости.
- Расширяемость: каждая метрика представляет собой независимую функцию, что позволяет легко добавлять температуру графического процессора, количество процессов или сетевые подключения.
---

## Краткое содержание
Сочетание читабельности, универсальности и глубины экосистемы Python делает его наиболее широко используемым языком программирования в мире. Это выбор по умолчанию для AI/ML, отличный вариант для веб-серверов и автоматизации, а также отличный язык обучения. Его основные недостатки — скорость выполнения и мобильная/встроенная поддержка — хорошо известны и существуют обходные пути. Для большинства проектов Python является разумной отправной точкой.