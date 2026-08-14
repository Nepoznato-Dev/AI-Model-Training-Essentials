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

#Píton
Python é uma linguagem de programação interpretada de alto nível e de uso geral criada por Guido van Rossum e lançada pela primeira vez em 1991. Ela prioriza a legibilidade do código por meio de recuo significativo e uma sintaxe limpa que se aproxima do inglês simples. Python é digitado dinamicamente, coletado como lixo e oferece suporte a vários paradigmas de programação, incluindo programação processual, orientada a objetos e funcional.
Hoje, Python é a linguagem dominante em IA/ML, ciência de dados, computação científica e automação – embora continue sendo uma das melhores linguagens para iniciantes. Essa dupla identidade (suficientemente simples para um primeiro script, poderosa o suficiente para treinar grandes modelos de linguagem) é o que o diferencia.
---

## Por que Python é importante
- **Legibilidade por design**: Sem ponto e vírgula, sem colchetes — o recuo define o escopo. O código parece pseudocódigo.
- **Ecossistema massivo**: PyPI hospeda mais de 500.000 pacotes cobrindo praticamente todos os domínios.
- **A linguagem da IA**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — toda a pilha de IA/ML prioriza o Python.
- **Linguagem adesiva**: conecte um mecanismo C++ a uma API web a um banco de dados em apenas algumas linhas.
- **Plataforma cruzada**: funciona em Windows, macOS, Linux e sistemas embarcados sem modificação.
- **Comunidade**: A maior e mais ativa comunidade de programação do mundo.
## As compensações
Python não é perfeito. Compreender suas limitações ajuda você a decidir quando buscar outra coisa:
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Velocidade de execução** | 10–100x mais lento que C para tarefas vinculadas à CPU | Use NumPy/PyTorch (C sob o capô) ou Cython/Numba para hot loops |
| **GIL (bloqueio global de intérprete)** | Impede o verdadeiro paralelismo multithread para trabalho vinculado à CPU | Use`multiprocessing`,`asyncio`ou filas de tarefas como Celery |
| **Desenvolvimento móvel** | Não adequado para aplicativos iOS/Android | Use Swift/Kotlin para nativo ou Flutter/React Native para plataforma cruzada |
| **Sistemas embarcados** | Muito pesado para microcontroladores | Use MicroPython (uma variante leve) ou mude para C/Rust |
| **Uso de memória** | Maior consumo de memória do que linguagens compiladas | Aceitável para a maioria das aplicações; usar geradores para grandes volumes de dados |
---

## Fundamentos de sintaxe
### Variáveis ​​e tipos
Python usa digitação dinâmica — você não declara tipos de variáveis, mas pode adicionar dicas de tipo para maior clareza e suporte de ferramentas.
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

### Fluxo de controle
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

### Funções
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

### Programação Orientada a Objetos
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

### Tratamento de erros
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

## Sintaxe e padrões avançados
### Genéricos com Módulo `typing`
O módulo`typing`do Python fornece suporte de tipo genérico para a construção de componentes reutilizáveis ​​e com segurança de tipo. Os genéricos permitem escrever funções e classes que funcionam com qualquer tipo, preservando as informações do tipo para análise estática.
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

### Decoradores e Metaprogramação
Decoradores são um dos recursos mais poderosos do Python — eles permitem modificar ou estender o comportamento de funções e classes sem alterar seu código-fonte.
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

### Correspondência de padrões estruturais (Python 3.10+)
A instrução`match/case`do Python fornece correspondência de padrões poderosa com desestruturação, guardas e padrões aninhados.
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

### Closures, funções de ordem superior e iteradores
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

### Sobrecarga do Operador
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

### Hierarquias de exceções personalizadas
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

## Principais recursos detalhados
### A Biblioteca Padrão ("Baterias Incluídas")
Python vem com uma extensa biblioteca padrão. Alguns dos módulos mais utilizados:
| Módulo | Finalidade | Exemplo de uso |
|--------|---------|---------|
| `os`/`pathlib`| Operações do sistema de arquivos | `Path("data/output.csv").exists()`|
| `json`| Codificação/decodificação JSON | `json.loads(response_text)`|
| `datetime`| Tratamento de data e hora | `datetime.now(timezone.utc)`|
| `collections`| Contentores especializados | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Blocos de construção do iterador | `combinations(items, 2)`|
| `functools`| Ferramentas funcionais | `lru_cache`,`partial`,`reduce`|
| `re`| Expressões regulares | `re.findall(r"\d+", text)`|
| `subprocess`| Execute comandos externos | `subprocess.run(["ls", "-la"])`|
| `logging`| Registro de aplicativos | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Suporte para dicas de tipo | `Optional[str]`,`Union[int, float]`|
| `http.server`| Servidor HTTP simples | `python -m http.server 8000`|
| `threading`/`asyncio`| Simultaneidade | E/S assíncrona para web scrapers |
### Ambientes Virtuais e Gerenciamento de Pacotes
Todo projeto Python deve usar um ambiente virtual para isolar dependências:
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

Os projetos Python modernos usam cada vez mais`pyproject.toml`com ferramentas como`uv`,`poetry`ou`hatch`para gerenciamento de dependências, substituindo a abordagem mais antiga`setup.py`/ `requirements.txt`.
### Programação Assíncrona
O`asyncio`do Python permite E/S simultânea sem threads – essencial para web scrapers, servidores de chat e clientes API:
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

## Simultaneidade e paralelismo
Python oferece vários modelos de simultaneidade, cada um adequado para diferentes cargas de trabalho. O GIL (Global Interpreter Lock) no CPython evita o verdadeiro paralelismo da CPU com threads, portanto, o modelo certo depende se sua carga de trabalho é vinculada à E/S ou à CPU.
### Threading (tarefas vinculadas a E/S)
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

### Multiprocessamento (tarefas vinculadas à CPU)
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

### Assíncio Internos
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

## Configuração do projeto e sistema de construção
### Estrutura do diretório do projeto
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

### Configuração de compilação — `pyproject.toml`
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

### Gerenciamento de Dependências com Ferramentas Modernas
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

### Linting e qualidade do código
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### Pipeline de CI/CD — Ações do GitHub
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

## Teste
### Estruturas de teste e configuração
O ecossistema de testes do Python gira em torno de`pytest`, o padrão de fato para testes do Python.
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

### Testes unitários com pytest
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

### Testes assíncronos e testes de integração
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

## Interoperabilidade
### Chamando C/C++ com ctypes
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

### Usando cffi para interoperabilidade C mais complexa
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

### Cython — Python com desempenho C
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

### Pybind11 — Extensões C++
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

## Padrões de Projeto
### Solteiro
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

### Padrão de fábrica
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

### Padrão Observador
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

### Padrão do Gerenciador de Contexto
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

### Padrão de Estratégia
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

## Desempenho e otimização
### Ferramentas de criação de perfil
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

### Técnicas de otimização
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

### Comparativo de mercado
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Implantação
### Embalagem e Distribuição
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

### Implantação específica da plataforma
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

## O Ecossistema
A força do Python não é apenas a linguagem – é o ecossistema construído em torno dela.
### IA e aprendizado de máquina
| Biblioteca | Finalidade |
|--------|---------|
| PyTorch | Aprendizado profundo (pesquisa e produção) |
| TensorFlow/Keras | Aprendizado profundo (focado na produção) |
| scikit-aprender | ML clássico (regressão, agrupamento, classificação) |
| Abraçando Transformadores de Rosto | Modelos de PNL/visão pré-treinados |
| LangChain/LlamaIndex | Construindo aplicativos com LLMs |
| NumPy | Computação numérica (matrizes, álgebra linear) |
| Pandas | Manipulação e análise de dados |
| Matplotlib/Seaborn/Plotly | Visualização de dados |
### Desenvolvimento Web
| Estrutura | Estilo | Melhor para |
|----------|-------|----------|
| Django | Full-stack, "baterias incluídas" | Aplicativos web complexos com painéis de administração, ORM, autenticação |
| API rápida | Moderno, assíncrono e baseado em tipo | APIs e microsserviços (atualmente os que mais crescem) |
| Frasco | Mínimo, flexível | Pequenos aplicativos e protótipos |
| Streamlit | Foco em aplicativos de dados | Painéis e demonstrações de dados em Python puro |
### Automação e scripts
| Biblioteca | Finalidade |
|--------|---------|
| `subprocess`/`os`| Administração do sistema |
| `requests`/`httpx`| Clientes HTTP |
| `BeautifulSoup`/`Scrapy`| Raspagem na Web |
| `Selenium`/`Playwright`| Automação do navegador |
| `Celery`| Filas de tarefas distribuídas |
| `Airflow`| Orquestração de fluxo de trabalho |
### Computação Científica
| Biblioteca | Finalidade |
|--------|---------|
| NumPy | Operações de array e álgebra linear |
| SciPy | Algoritmos científicos (otimização, processamento de sinais) |
| SymPy | Matemática simbólica |
| Caderno Jupyter | Ambiente de computação interativo |
| JAX | Computação numérica de alto desempenho (acelerada por GPU) |
---

## Quando usar Python
| Cenário | Por que Python | Melhor Alternativa |
|----------|-----------|-------------------|
| IA/ML/Ciência de Dados | O ecossistema é incomparável | — |
| Automação e scripts | Mais rápido para escrever e depurar | Shell/PowerShell para tarefas simples de administração de sistemas |
| Back-ends da Web (APIs) | FastAPI é excelente | Go ou Java para serviços de alto rendimento |
| Prototipagem | Caminho mais rápido da ideia ao código funcional | — |
| Educação | Linguagem mais amigável para iniciantes | — |
| Aplicativos de desktop | Possível, mas incomum | C# (Windows), Swift (macOS) |
| Sistemas de desempenho crítico | Evite — muito lento | C, C++, Ferrugem |
| Aplicativos móveis | Não é a ferramenta certa | Swift (iOS), Kotlin (Android) |
| Sistemas embarcados | Muitos recursos | C, Rust ou MicroPython para casos simples |
---

## Versões do Python
A linguagem continua a evoluir. Principais adições recentes:
| Versão | Ano | Recursos notáveis ​​|
|--------|------|-----------------|
| 3.10 | 2021 | Correspondência de padrões estruturais (`match/case`), melhores mensagens de erro |
| 3.11 | 2022 | Execução 10–60% mais rápida, rastreamentos aprimorados |
| 3.12 | 2023 | Strings F mais flexíveis, instrução `type`, ganhos de desempenho |
| 3.13 | 2024 | Modo experimental de thread livre (sem GIL), REPL aprimorado |
| 3.14 | 2025 | Outras melhorias no-GIL, digite melhorias no sistema |
O Python 2 atingiu o fim de sua vida útil em 1º de janeiro de 2020. Todos os novos projetos devem usar Python 3.10 ou posterior.
---

## Referência rápida: expressões idiomáticas comuns
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

## Perguntas e respostas sintéticas
### Q1: Qual é a diferença entre listas e tuplas e quando devo usar cada uma?
**R:** As listas são mutáveis ​​(`[]`), as tuplas são imutáveis ​​(`()`). Use listas quando precisar adicionar, remover ou alterar elementos. Use tuplas para coleções fixas de dados heterogêneos, chaves de dicionário, valores de retorno de função ou quando desejar sinalizar "isso não deve mudar". Tuplas são um pouco mais eficientes em termos de memória e podem ser usadas como chaves set/dict; listas não podem.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: Como o Global Interpreter Lock (GIL) afeta meu código e o que devo fazer a respeito?
**R:** O GIL impede que vários threads executem bytecode Python simultaneamente, tornando o threading ineficaz para trabalho vinculado à CPU. Para tarefas vinculadas a E/S (solicitações de rede, E/S de arquivo),`threading`ou`asyncio`funcionam bem porque o GIL é liberado durante a E/S. Para tarefas vinculadas à CPU, use`multiprocessing`(processos separados, cada um com seu próprio GIL) ou transfira para extensões C (NumPy, Cython, Numba) que liberam o GIL internamente.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: Devo usar dicas de tipo em todos os lugares? Quais são as compensações práticas?
**R:** As dicas de tipo (`def greet(name: str) -> str:`) são opcionais e não aplicadas em tempo de execução. Eles melhoram o preenchimento automático do IDE, detectam bugs por meio de ferramentas de análise estática (mypy) e documentam a intenção. A desvantagem é a verbosidade extra e uma curva de aprendizado para tipos avançados (`Union`,`Generic`,`Protocol`). Recomendação: use dicas de tipo para assinaturas de função em qualquer projeto com mais de 500 linhas; use-os com moderação em scripts curtos. Habilite mypy no CI para aplicação gradual.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: Quais são as melhores práticas para lidar com exceções em Python?
**R:** Capture exceções específicas em vez de`except:`simples (que captura`SystemExit`e`KeyboardInterrupt`também). Use`try/except/else/finally`para separar a lógica do caminho feliz do tratamento de erros. Defina hierarquias de exceções personalizadas para bibliotecas. Nunca use exceções para fluxo de controle em código sensível ao desempenho — elas são lentas. Registre a exceção com`logging.exception()`para capturar o rastreamento completo.
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

### Q5: Como os geradores economizam memória e quando devo usá-los em vez de listas?
**R:** Os geradores produzem valores preguiçosamente — um de cada vez, sob demanda — em vez de construir uma lista inteira na memória. Para grandes conjuntos de dados (milhões de linhas, sequências infinitas, streaming de dados), os geradores usam memória constante, independentemente do tamanho. Use geradores quando você iterar uma vez e não precisar de indexação ou`len()`. Use listas quando precisar de acesso aleatório, múltiplas iterações ou a coleção for pequena.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construa um contador de frequência de palavras com classificação
**Declaração do problema:** Dado um arquivo de texto grande, conte a frequência de cada palavra, classifique-as por frequência (decrescente) e retorne os N resultados principais. Lide com insensibilidade a maiúsculas e minúsculas, pontuação e processe com eficiência arquivos grandes demais para caber na memória.
**Etapa 1 — Entenda o problema:**
Precisamos: (1) ler o texto, (2) dividir em palavras, (3) normalizar maiúsculas e minúsculas, (4) retirar a pontuação, (5) contar ocorrências, (6) classificar por contagem decrescente, (7) retornar o N superior. A restrição "muito grande para caber na memória" significa que devemos processar linha por linha com geradores.
**Etapa 2 — Identifique a abordagem:**
- Use`re.finditer`para extração eficiente de palavras sem construir listas intermediárias.
- Use`collections.Counter`para incremento de O(1) por palavra.
- Use`Counter.most_common(n)`que usa um heap internamente - O(k log n) em vez de O(n log n) para classificação completa.
- Processe linha por linha via gerador para manter a memória constante.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Memória: apenas o contador do contador está na memória (uma entrada por palavra única), não o conteúdo do arquivo. Para texto em inglês, aproximadamente 100 mil palavras exclusivas ≈ alguns MB.
- Tempo: O(W) para digitalizar todas as palavras + O(U log N) para extração dos N principais, onde W = total de palavras, U = palavras únicas.
- Casos extremos: apóstrofos em contrações ("don't") são preservados pela regex. O texto Unicode precisaria do sinalizador`re.UNICODE`ou de um padrão diferente.
### Problema 2: Implementar um cache LRU Thread-Safe
**Declaração do problema:** Crie um cache LRU (menos usado recentemente) do zero que seja thread-safe, suporte operações get e put O(1) e remova automaticamente o item usado menos recentemente quando a capacidade for excedida.
**Etapa 1 — Entenda o problema:**
Um cache LRU precisa de: (1) pesquisa rápida por chave → mapa hash, (2) ordenação rápida por tempo recente → lista duplamente vinculada, (3) segurança de thread → bloqueio. Em `get(key)`: mova o item para a frente. Em `put(key, val)`: inserir na frente; se estiver acima da capacidade, remova pela parte de trás.
**Etapa 2 — Identifique a abordagem:**
- O`dict`do Python mantém a ordem de inserção (3.7+), para que possamos usar uma abordagem de dict ordenada: exclua e reinsira para mover para o final.
- Para segurança de thread, use`threading.Lock`para exclusão mútua.
- Alternativa: use`collections.OrderedDict`que possui`move_to_end()`.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Complexidade de tempo: O(1) para`get`e`put`—`OrderedDict.move_to_end()`e`popitem()`são O(1).
- Segurança do thread: o`Lock`garante atomicidade. Para maior rendimento, considere`threading.RLock`ou um padrão de bloqueio de leitura e gravação, mas para a maioria dos casos de uso, um bloqueio simples é suficiente.
- Nota de produção: para código single-threaded,`functools.lru_cache`é mais simples e implementado em C para melhor desempenho.
### Problema 3: Analisar e avaliar uma expressão matemática
**Declaração do problema:** Escreva um analisador que pegue uma string como`"3 + 4 * 2 / (1 - 5)"`e a avalie corretamente respeitando a precedência do operador e os parênteses.
**Etapa 1 — Entenda o problema:**
Isso requer: (1) tokenizar a string de entrada em números, operadores e parênteses, (2) analisar com precedência correta (`*`e`/`antes de`+`e`-`), (3) manipular parênteses aninhados. Uma avaliação ingênua da esquerda para a direita daria resultados errados.
**Etapa 2 — Identifique a abordagem:**
A solução clássica é o **algoritmo de pátio de manobras** (Dijkstra), que converte o infixo em pós-fixo (notação polonesa reversa) e, em seguida, avalia o pós-fixo. Alternativamente, use um analisador descendente recursivo. Especificamente para Python, também podemos usar`ast.literal_eval`para avaliação segura - mas vamos implementá-lo corretamente.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Correção:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. Correto.
- Tempo: O(N) para tokenização, O(N) para pátio de manobra, O(N) para avaliação — geral O(N).
- Casos extremos a serem tratados: números negativos (prefixar`0`antes do unário`-`), divisão por zero (adicionar tratamento de erros), entrada inválida (validar tokens).
- Alternativa Pythonic:`ast.parse(expr, mode='eval')`com um visitante de nó personalizado para avaliação segura sem`eval()`.
### Problema 4: Construa um painel CLI com atualizações de dados em tempo real
**Declaração do problema:** Crie um painel baseado em terminal que exibe as métricas do sistema (CPU, memória, disco) atualizadas em tempo real, com limites codificados por cores e layout responsivo.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) coleta periódica de métricas do sistema, (2) renderização de terminal com controle de cursor, (3) saída de cores baseada em limites, (4) entrada de teclado sem bloqueio para sair. Este é um padrão produtor-consumidor com um loop de renderização.
**Etapa 2 — Identifique a abordagem:**
- Use`psutil`para métricas de sistema multiplataforma.
- Use códigos de escape ANSI para posicionamento e cores do cursor (ou a biblioteca`rich`para uma API de nível superior).
- Use`time.sleep`para o intervalo de atualização.
- Estrutura como: coleta de dados → formatação → pipeline de renderização.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- O`cpu_percent(interval=0.5)`bloqueia por 0,5s para medir - esta é a abordagem correta (o modo sem bloqueio dá 0% na primeira chamada).
- Os códigos ANSI funcionam em terminais Windows modernos e em todos os terminais Unix. Para cmd legado do Windows, adicione`os.system('color')`ou use`colorama`.
- Atualização de produção: use a biblioteca`rich`(`rich.live`) para renderização sem cintilação, layout automático e compatibilidade entre plataformas.
- Extensibilidade: cada métrica é uma função independente, facilitando a adição de temperatura da GPU, contagem de processos ou conexões de rede.
---

## Resumo
A combinação de legibilidade, versatilidade e profundidade do ecossistema do Python torna-o a linguagem de programação mais usada no mundo. É a escolha padrão para IA/ML, uma opção forte para back-ends e automação da web e uma excelente linguagem de ensino. Seus principais pontos fracos — velocidade de execução e suporte móvel/incorporado — são bem compreendidos e possuem soluções alternativas estabelecidas. Para a maioria dos projetos, Python é um ponto de partida razoável.