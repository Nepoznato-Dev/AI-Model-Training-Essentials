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
# パイソン
Python は、Guido van Rossum によって作成され、1991 年に初めてリリースされた、高レベルのインタプリタ型汎用プログラミング言語です。Python は、大幅なインデントと、平易な英語に近いきれいな構文によって、コードの可読性を優先しています。 Python は動的に型指定され、ガベージ コレクションが行われ、手続き型プログラミング、オブジェクト指向プログラミング、関数型プログラミングなどの複数のプログラミング パラダイムをサポートします。
現在、Python は AI/ML、データ サイエンス、科学技術コンピューティング、オートメーションの分野で主流の言語でありながら、初心者にとって最適な言語の 1 つであり続けています。この二重のアイデンティティ (最初のスクリプトとして十分シンプルであること、大規模な言語モデルをトレーニングするのに十分強力であること) が、それを区別するものです。
---

## Python が重要な理由
- **設計による読みやすさ**: セミコロンや中括弧は使用しません。インデントによって範囲が定義されます。コードは擬似コードのように読み取れます。
- **大規模なエコシステム**: PyPI は、事実上すべてのドメインをカバーする 500,000 を超えるパッケージをホストします。
- **AI の言語**: PyTorch、TensorFlow、scikit-learn、Hugging Face、LangChain — AI/ML スタック全体が Python ファーストです。
- **Glue 言語**: わずか数行で、C++ エンジンを Web API、データベースに接続します。
- **クロスプラットフォーム**: Windows、macOS、Linux、および組み込みシステム上で変更を加えずに実行できます。
- **コミュニティ**: 世界で最大かつ最も活発なプログラミング コミュニティ。
## トレードオフ
Python は完璧ではありません。その制限を理解すると、いつ他のものに手を伸ばすかを決定するのに役立ちます。
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **実行速度** | CPU に依存するタスクでは C よりも 10 ～ 100 倍遅い |ホット ループには NumPy/PyTorch (内部 C)、または Cython/Numba を使用します。
| **GIL (グローバル インタープリター ロック)** | CPU に依存した作業のための真のマルチスレッド並列処理を防止します。`multiprocessing`、`asyncio`、または Celery のようなタスク キューを使用します。
| **モバイル開発** | iOS/Android アプリには適していません |ネイティブには Swift/Kotlin を使用し、クロスプラットフォームには Flutter/React Native を使用します。
| **組み込みシステム** |マイクロコントローラーには重すぎる | MicroPython (軽量バージョン) を使用するか、C/Rust に切り替えます。
| **メモリ使用量** |コンパイル言語よりもメモリ フットプリントが大きい |ほとんどのアプリケーションに使用可能です。大きなデータにはジェネレータを使用する |
---

## 構文の基礎
### 変数と型
Python は動的型付けを使用します。変数の型を宣言しませんが、明確さとツールのサポートのために型ヒントを追加できます。
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

### 制御フロー
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

### 関数
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

### オブジェクト指向プログラミング
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

### エラー処理
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

## 高度な構文とパターン
###`typing`モジュールを使用したジェネリックス
Python の`typing`モジュールは、再利用可能でタ​​イプセーフなコンポーネントを構築するためのジェネリック型サポートを提供します。ジェネリックを使用すると、静的分析用の型情報を保持しながら、任意の型で動作する関数やクラスを作成できます。
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

### デコレータとメタプログラミング
デコレータは Python の最も強力な機能の 1 つです。デコレータを使用すると、ソース コードを変更せずに関数やクラスの動作を変更または拡張できます。
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

### 構造パターン マッチング (Python 3.10 以降)
Python の`match/case`ステートメントは、構造化、ガード、およびネストされたパターンを使用した強力なパターン マッチングを提供します。
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

### クロージャ、高階関数、イテレータ
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

### 演算子のオーバーロード
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

### カスタム例外階層
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

## 主な機能の詳細
### 標準ライブラリ (「電池付属」)
Python には広範な標準ライブラリが付属しています。最もよく使用されるモジュールの一部:
|モジュール |目的 |使用例 |
|----------|----------|---------------|
| `os`/`pathlib`|ファイル システムの操作 | `Path("data/output.csv").exists()`|
| `json`| JSON エンコード/デコード | `json.loads(response_text)`|
| `datetime`|日付と時刻の処理 | `datetime.now(timezone.utc)`|
| `collections`|特殊コンテナ |  `Counter(words)`、`defaultdict(list)` |
| `itertools`|イテレータの構成要素 | `combinations(items, 2)`|
| `functools`|機能ツール |  `lru_cache`、`partial`、`reduce` |
| `re`|正規表現 | `re.findall(r"\d+", text)`|
| `subprocess`|外部コマンドを実行する | `subprocess.run(["ls", "-la"])`|
| `logging`|アプリケーションのログ | `logging.basicConfig(level=logging.INFO)`|
| `typing`|タイプヒントのサポート |  `Optional[str]`、`Union[int, float]` |
| `http.server`|シンプルなHTTPサーバー | `python -m http.server 8000`|
| `threading`/`asyncio`|同時実行性 | Web スクレイパーの非同期 I/O |
### 仮想環境とパッケージ管理
すべての Python プロジェクトは、依存関係を分離するために仮想環境を使用する必要があります。
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

最新の Python プロジェクトでは、依存関係管理に`uv`、`poetry`、`hatch`などのツールとともに`pyproject.toml`を使用することが増えており、古い`setup.py`/`requirements.txt`アプローチに代わっています。
### 非同期プログラミング
Python の`asyncio`は、スレッドなしで同時 I/O を可能にします。これは、Web スクレイパー、チャット サーバー、および API クライアントに不可欠です。
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

## 同時実行性と並列処理
Python は、さまざまなワークロードに適した複数の同時実行モデルを提供します。 CPython の GIL (グローバル インタープリター ロック) は、スレッドによる真の CPU 並列処理を妨げるため、適切なモデルは、ワークロードが I/O バウンドであるか CPU バウンドであるかによって異なります。
### スレッディング (I/O バウンドのタスク)
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

### マルチプロセッシング (CPU 依存タスク)
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

### Asyncio の内部構造
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

## プロジェクトの構成とシステムの構築
### プロジェクトのディレクトリ構造
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

### ビルド構成 — `pyproject.toml`
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

### 最新ツールによる依存関係管理
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

### リンティングとコードの品質
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### CI/CD パイプライン — GitHub アクション
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

## テスト
### テストフレームワークとセットアップ
Python のテスト エコシステムは、Python テストの事実上の標準である`pytest`を中心にしています。
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

### pytest を使用した単体テスト
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

### 非同期テストと統合テスト
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

## 相互運用性
### ctypes を使用した C/C++ の呼び出し
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

### より複雑な C 相互運用のための cffi の使用
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

### Cython — C パフォーマンスを備えた Python
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

### Pybind11 — C++ 拡張機能
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

## デザインパターン
### シングルトン
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

### ファクトリーパターン
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

### オブザーバーパターン
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

### コンテキストマネージャーパターン
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

### 戦略パターン
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

## パフォーマンスと最適化
### プロファイリングツール
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

### 最適化手法
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

### ベンチマーク
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## デプロイメント
### パッケージングと流通
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

### プラットフォーム固有の展開
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

## エコシステム
Python の強みは言語だけではなく、それを中心に構築されたエコシステムです。
### AI と機械学習
|図書館 |目的 |
|----------|----------|
|パイトーチ |ディープラーニング（研究・制作） |
| TensorFlow / ケラス |ディープラーニング (本番環境中心) |
| scikit-learn |古典的な ML (回帰、クラスタリング、分類) |
|ハグフェイストランスフォーマー |事前トレーニングされた NLP/ビジョン モデル |
|ラングチェーン / ラマインデックス | LLM を使用したアプリケーションの構築 |
|ナムピ |数値計算 (配列、線形代数) |
|パンダ |データ操作と分析 |
| Matplotlib / Seaborn / Plotly |データの視覚化 |
### ウェブ開発
|フレームワーク |スタイル |最適な用途 |
|----------|----------|----------|
|ジャンゴ |フルスタック、「バッテリー付属」 |管理パネル、ORM、認証を備えた複雑な Web アプリ |
|ファストAPI |モダン、非同期、タイプ駆動 | API とマイクロサービス (現在最も急速に成長している) |
|フラスコ |ミニマル、フレキシブル |小さなアプリとプロトタイプ |
|ストリームリット |データアプリ中心 |純粋な Python によるダッシュボードとデータのデモ |
### 自動化とスクリプト作成
|図書館 |目的 |
|----------|----------|
| `subprocess`/`os`|システム管理 |
| `requests`/`httpx`| HTTP クライアント |
| `BeautifulSoup`/`Scrapy`| Webスクレイピング |
| `Selenium`/`Playwright`|ブラウザの自動化 |
| `Celery`|分散タスクキュー |
| `Airflow`|ワークフロー オーケストレーション |
### 科学コンピューティング
|図書館 |目的 |
|----------|----------|
|ナムピ |配列演算と線形代数 |
|サイピー |科学的アルゴリズム (最適化、信号処理) |
|シンピー |記号数学 |
|ジュピターノート |インタラクティブ コンピューティング環境 |
|ジャックス |高性能数値計算 (GPU アクセラレーション) |
---

## Python を使用する場合
|シナリオ |なぜPythonなのか |より良い代替案 |
|----------|-----------|--------|
| AI/ML/データサイエンス |エコシステムは比類のないものです | — |
|自動化とスクリプト作成 |書き込みとデバッグが最速 |単純なシステム管理タスク用のシェル/PowerShell |
| Web バックエンド (API) | FastAPI は優れています |非常に高スループットのサービスには Go または Java |
|プロトタイピング |アイデアから実用的なコードへの最速パス | — |
|教育 |最も初心者に優しい言語 | — |
|デスクトップ アプリケーション |可能だが珍しい | C# (Windows)、Swift (macOS) |
|パフォーマンスが重要なシステム |避けてください — 遅すぎます | C、C++、Rust |
|モバイルアプリ |適切なツールではありません | Swift (iOS)、Kotlin (Android) |
|組み込みシステム |リソースが多すぎる |単純な場合は C、Rust、または MicroPython |
---

## Python のバージョン
言語は進化し続けています。最近の主な追加内容:
|バージョン |年 |注目すべき機能 |
|-------|------|------|
| 3.10 | 2021年 |構造パターン マッチング (`match/case`)、エラー メッセージの改善 |
| 3.11 | 2022年 | 10 ～ 60% 高速な実行、改善されたトレースバック |
| 3.12 | 2023年 |より柔軟な f-strings、`type` ステートメント、パフォーマンスの向上 |
| 3.13 | 2024年 |実験的なフリースレッド モード (GIL なし)、改善された REPL |
| 3.14 | 2025年 | GIL を使用しないさらなる改善、型システムの機能強化 |
Python 2 は、2020 年 1 月 1 日にサポートが終了しました。すべての新しいプロジェクトでは、Python 3.10 以降を使用する必要があります。
---

## クイックリファレンス: 一般的なイディオム
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

## 総合的な Q&A
### Q1: リストとタプルの違いは何ですか? それぞれをいつ使用する必要がありますか?
**A:** リストは変更可能 (`[]`)、タプルは変更不可 (`()`) です。要素を追加、削除、または変更する必要がある場合は、リストを使用します。タプルは、異種データ、辞書キー、関数の戻り値の固定コレクションに使用するか、「これは変更すべきではない」という信号を送りたい場合に使用します。タプルはメモリ効率がわずかに高く、set/dict キーとして使用できます。リストではできません。
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: グローバル インタプリタ ロック (GIL) はコードにどのような影響を与えますか?また、それに対して何をすべきですか?
**A:** GIL は、複数のスレッドが Python バイトコードを同時に実行することを防ぎ、CPU バウンドの作業ではスレッド処理を無効にします。 I/O バウンドのタスク (ネットワーク リクエスト、ファイル I/O) の場合、GIL は I/O 中に解放されるため、`threading` または`asyncio`は正常に動作します。 CPU バウンドのタスクの場合は、`multiprocessing` (それぞれ独自の GIL を持つ個別のプロセス) を使用するか、内部で GIL を解放する C 拡張機能 (NumPy、Cython、Numba) にオフロードします。
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: あらゆる場所でタイプヒントを使用する必要がありますか?実際的なトレードオフは何でしょうか?
**A:** 型ヒント (`def greet(name: str) -> str:`) はオプションであり、実行時に強制されません。これらは、IDE のオートコンプリートを改善し、静的分析ツール (mypy) を介してバグを捕捉し、意図を文書化します。トレードオフは、冗長性と高度な型 (`Union`、`Generic`、`Protocol`) の学習曲線です。推奨事項: 500 行を超えるプロジェクトでは、関数シグネチャの型ヒントを使用してください。短いスクリプトでは控えめに使用してください。段階的な適用のために CI で mypy を有効にします。
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: Python で例外を処理するためのベスト プラクティスは何ですか?
**A:** 裸の`except:`ではなく、特定の例外をキャッチします (`SystemExit` と`KeyboardInterrupt`もキャッチします)。`try/except/else/finally`を使用して、ハッピー パス ロジックをエラー処理から分離します。ライブラリのカスタム例外階層を定義します。パフォーマンス重視のコードでは制御フローに例外を使用しないでください。例外は遅いからです。`logging.exception()`を使用して例外をログに記録し、完全なトレースバックをキャプチャします。
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

### Q5: ジェネレーターはどのようにしてメモリを節約しますか?また、いつリストに対してジェネレーターを使用する必要がありますか?
**A:** ジェネレーターは、メモリ内にリスト全体を構築するのではなく、オンデマンドで一度に 1 つずつ値を遅延的に生成します。大規模なデータセット (数百万行、無限シーケンス、ストリーミング データ) の場合、ジェネレーターはサイズに関係なく定数メモリを使用します。 1 回反復し、インデックス作成や`len()`が必要ない場合は、ジェネレーターを使用します。ランダム アクセス、複数の反復が必要な場合、またはコレクションが小さい場合は、リストを使用します。
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

## 思考連鎖による問題解決
### 問題 1: ランキング付きの単語頻度カウンターを構築する
**問題ステートメント:** 大きなテキスト ファイルが与えられた場合、各単語の頻度をカウントし、頻度によってランク付けし (降順)、上位 N 個の結果を返します。大文字と小文字を区別せず、句読点を処理し、メモリに収まらないほど大きすぎるファイルを効率的に処理します。
**ステップ 1 — 問題を理解する:**
(1) テキストを読み取る、(2) 単語に分割する、(3) 大文字と小文字を正規化する、(4) 句読点を削除する、(5) 出現数をカウントする、(6) カウントの降順で並べ替える、(7) 上位 N を返す必要があります。「大きすぎてメモリに収まらない」という制約は、ジェネレーターで 1 行ずつ処理する必要があることを意味します。
**ステップ 2 — アプローチを特定する:**
- 中間リストを作成せずに効率的に単語を抽出するには、`re.finditer` を使用します。
- ワードごとに O(1) 増分するには、`collections.Counter` を使用します。
- 内部でヒープを使用する`Counter.most_common(n)`を使用します。フル ソートの場合は O(n log n) ではなく O(k log n) です。
- ジェネレーターを介して行ごとに処理し、メモリを一定に保ちます。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- メモリ: ファイルの内容ではなく、Counter dict のみがメモリ内にあります (一意の単語ごとに 1 つのエントリ)。英語のテキストの場合、約 100K の一意の単語 ≈ 数 MB。
- 時間: すべての単語をスキャンするための O(W) + 上位 N 抽出のための O(U log N)。ここで、W = 合計単語、U = 固有の単語。
- 特殊なケース: 短縮形のアポストロフィ (「don't」) は正規表現によって保持されます。 Unicode テキストには、`re.UNICODE` フラグまたは別のパターンが必要です。
### 問題 2: スレッドセーフな LRU キャッシュの実装
**問題ステートメント:** スレッドセーフで、O(1) の get および put 操作をサポートし、容量を超えた場合に最も最近使用されていない項目を自動的に削除する、最も最近使用されていない (LRU) キャッシュを最初から構築します。
**ステップ 1 — 問題を理解する:**
LRU キャッシュには、(1) キーによる高速ルックアップ → ハッシュ マップ、(2) 最新性による高速順序付け → 二重リンク リスト、(3) スレッド セーフ → ロックが必要です。`get(key)`の場合: 項目を前に移動します。`put(key, val)`の場合: 前に挿入します。容量を超えた場合は背面から取り外してください。
**ステップ 2 — アプローチを特定する:**
- Python の`dict`は挿入順序を維持する (3.7 以降)。そのため、順序付けされた dict アプローチ (削除して再挿入して最後に移動する) を使用できます。
- スレッドの安全性を確保するため、相互排他には`threading.Lock`を使用します。
- 代替案:`move_to_end()`を持つ`collections.OrderedDict`を使用します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- 時間計算量:`get`と`put`の両方で O(1) —`OrderedDict.move_to_end()`と`popitem()`は O(1) です。
- スレッド セーフ:`Lock`はアトミック性を保証します。スループットを高めるには、`threading.RLock` または読み取り/書き込みロック パターンを検討してください。ただし、ほとんどの使用例では単純なロックで十分です。
- 制作メモ: シングルスレッド コードの場合、`functools.lru_cache` はより単純であり、パフォーマンスを向上させるために C で実装されています。
### 問題 3: 数式を解析して評価する
**問題ステートメント:**`"3 + 4 * 2 / (1 - 5)"`のような文字列を受け取り、演算子の優先順位と括弧を考慮してそれを正しく評価するパーサーを作成します。
**ステップ 1 — 問題を理解する:**
これには、(1) 入力文字列を数値、演算子、括弧にトークン化すること、(2) 正しい優先順位 (`+`および`-`の前に`*`および`/`) で解析すること、(3) ネストされた括弧を処理することが必要です。単純な左から右への評価では、誤った結果が得られます。
**ステップ 2 — アプローチを特定する:**
古典的な解決策は、中置記号を後置記号 (逆ポーランド記法) に変換し、その後後置記号を評価する **待避所アルゴリズム** (ダイクストラ) です。あるいは、再帰降下パーサーを使用します。特に Python の場合、安全な評価のために`ast.literal_eval`を使用することもできますが、それを適切に実装しましょう。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- 正確さ:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`。正しい。
- 時間: トークン化に O(N)、操車場に O(N)、評価に O(N) — 全体で O(N)。
- 処理するエッジ ケース: 負の数 (単項`-`の前に`0`を追加)、ゼロによる除算 (エラー処理の追加)、無効な入力 (トークンの検証)。
- Python の代替:`eval()`を使用せずに安全に評価するためのカスタム ノード ビジターを使用した`ast.parse(expr, mode='eval')`。
### 問題 4: リアルタイム データ更新を備えた CLI ダッシュボードを構築する
**問題ステートメント:** 色分けされたしきい値と応答性の高いレイアウトを使用して、リアルタイムで更新されるシステム メトリクス (CPU、メモリ、ディスク) を表示する端末ベースのダッシュボードを作成します。
**ステップ 1 — 問題を理解する:**
(1) 定期的なシステム メトリック収集、(2) カーソル コントロールによるターミナル レンダリング、(3) しきい値に基づくカラー出力、(4) 終了のためのノンブロッキング キーボード入力が必要です。これは、レンダリング ループを備えたプロデューサー/コンシューマー パターンです。
**ステップ 2 — アプローチを特定する:**
- クロスプラットフォーム システム メトリックには`psutil`を使用します。
- カーソルの位置と色には ANSI エスケープ コードを使用します (または、高レベル API の場合は`rich`ライブラリ)。
・更新間隔は`time.sleep`を使用してください。
- データ収集 → フォーマット → レンダリング パイプラインの構造。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
-`cpu_percent(interval=0.5)`は 0.5 秒間ブロックして測定します。これは正しいアプローチです (非ブロッキング モードでは最初の呼び出しで 0% が与えられます)。
- ANSI コードは、最新の Windows ターミナルおよびすべての Unix ターミナルで動作します。従来の Windows cmd の場合は、`os.system('color')`を追加するか、`colorama`を使用します。
- 製品アップグレード: ちらつきのないレンダリング、自動レイアウト、およびクロスプラットフォーム互換性を実現するには、`rich` ライブラリ (`rich.live`) を使用します。
- 拡張性: 各メトリックは独立した関数であるため、GPU 温度、プロセス数、またはネットワーク接続を簡単に追加できます。
---

＃＃ まとめ
Python は、読みやすさ、多用途性、エコシステムの深さの組み合わせにより、世界で最も広く使用されているプログラミング言語となっています。これは AI/ML のデフォルトの選択肢であり、Web バックエンドと自動化の強力なオプションであり、優れた教育言語です。その主な弱点 (実行速度とモバイル/組み込みサポート) はよく理解されており、回避策が確立されています。ほとんどのプロジェクトでは、Python が適切な出発点となります。