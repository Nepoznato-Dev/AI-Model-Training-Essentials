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
# Pitón
Python es un lenguaje de programación interpretado de alto nivel y de propósito general creado por Guido van Rossum y lanzado por primera vez en 1991. Prioriza la legibilidad del código a través de una sangría significativa y una sintaxis limpia que se lee cerca del inglés simple. Python se escribe dinámicamente, se recolecta basura y admite múltiples paradigmas de programación, incluida la programación funcional, orientada a objetos y de procedimientos.
Hoy en día, Python es el lenguaje dominante en IA/ML, ciencia de datos, informática científica y automatización, sin dejar de ser uno de los mejores lenguajes para principiantes. Esa identidad dual (lo suficientemente simple para un primer guión, lo suficientemente potente como para entrenar modelos de lenguaje grandes) es lo que lo distingue.
---

## Por qué es importante Python
- **Legibilidad por diseño**: sin punto y coma, sin llaves: la sangría define el alcance. El código se lee como un pseudocódigo.
- **Ecosistema masivo**: PyPI aloja más de 500.000 paquetes que cubren prácticamente todos los dominios.
- **El lenguaje de la IA**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain: toda la pila de IA/ML es Python primero.
- **Lenguaje Glue**: conecta un motor C++ a una API web a una base de datos en solo unas pocas líneas.
- **Multiplataforma**: se ejecuta en Windows, macOS, Linux y sistemas integrados sin modificaciones.
- **Comunidad**: La comunidad de programación más grande y activa del mundo.
## Las compensaciones
Python no es perfecto. Comprender sus limitaciones le ayuda a decidir cuándo buscar algo más:
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Velocidad de ejecución** | 10 a 100 veces más lento que C para tareas vinculadas a la CPU | Utilice NumPy/PyTorch (C bajo el capó) o Cython/Numba para bucles activos |
| **GIL (Bloqueo global de intérprete)** | Previene un verdadero paralelismo multiproceso para el trabajo vinculado a la CPU | Utilice`multiprocessing`,`asyncio`o colas de tareas como Celery |
| **Desarrollo móvil** | No apto para aplicaciones iOS/Android | Utilice Swift/Kotlin para nativo o Flutter/React Native para multiplataforma |
| **Sistemas integrados** | Demasiado pesado para microcontroladores | Utilice MicroPython (una variante ligera) o cambie a C/Rust |
| **Uso de memoria** | Mayor consumo de memoria que los lenguajes compilados | Aceptable para la mayoría de las aplicaciones; utilizar generadores para grandes datos |
---

## Fundamentos de sintaxis
### Variables y tipos
Python utiliza escritura dinámica: no declara tipos de variables, pero puede agregar sugerencias de tipo para mayor claridad y soporte de herramientas.
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

### Flujo de control
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

### Funciones
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

### Programación orientada a objetos
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

### Manejo de errores
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

## Sintaxis y patrones avanzados
### Genéricos con módulo `typing`
El módulo`typing`de Python proporciona soporte de tipos genéricos para crear componentes reutilizables y con seguridad de tipos. Los genéricos le permiten escribir funciones y clases que funcionan con cualquier tipo y al mismo tiempo conservan la información del tipo para el análisis estático.
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

### Decoradores y Metaprogramación
Los decoradores son una de las características más poderosas de Python: le permiten modificar o ampliar el comportamiento de funciones y clases sin cambiar su código fuente.
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

### Coincidencia de patrones estructurales (Python 3.10+)
La declaración`match/case`de Python proporciona una potente coincidencia de patrones con desestructuración, protecciones y patrones anidados.
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

### Cierres, funciones de orden superior e iteradores
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

### Sobrecarga del operador
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

### Jerarquías de excepciones personalizadas
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

## Funciones clave en profundidad
### La biblioteca estándar ("Pilas incluidas")
Python viene con una extensa biblioteca estándar. Algunos de los módulos más utilizados:
| Módulo | Propósito | Uso de ejemplo |
|--------|---------|-------------|
| `os`/`pathlib`| Operaciones del sistema de archivos | `Path("data/output.csv").exists()`|
| `json`| Codificación/decodificación JSON | `json.loads(response_text)`|
| `datetime`| Manejo de fecha y hora | `datetime.now(timezone.utc)`|
| `collections`| Contenedores especializados | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Bloques de construcción del iterador | `combinations(items, 2)`|
| `functools`| Herramientas funcionales |  `lru_cache`, `partial`,`reduce`|
| `re`| Expresiones regulares | `re.findall(r"\d+", text)`|
| `subprocess`| Ejecutar comandos externos | `subprocess.run(["ls", "-la"])`|
| `logging`| Registro de aplicaciones | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Soporte de sugerencia de tipo |  `Optional[str]`,`Union[int, float]`|
| `http.server`| Servidor HTTP sencillo | `python -m http.server 8000`|
| `threading`/`asyncio`| Concurrencia | E/S asíncrona para raspadores web |
### Entornos virtuales y gestión de paquetes
Cada proyecto de Python debe utilizar un entorno virtual para aislar las dependencias:
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

Los proyectos modernos de Python utilizan cada vez más`pyproject.toml`con herramientas como `uv`,`poetry`o`hatch`para la gestión de dependencias, reemplazando el antiguo enfoque `setup.py`/`requirements.txt`.
### Programación asíncrona
`asyncio` de Python permite E/S simultáneas sin subprocesos, algo esencial para raspadores web, servidores de chat y clientes API:
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

## Concurrencia y paralelismo
Python ofrece varios modelos de concurrencia, cada uno de ellos adecuado para diferentes cargas de trabajo. El GIL (Global Interpreter Lock) en CPython evita el verdadero paralelismo de la CPU con los subprocesos, por lo que el modelo correcto depende de si su carga de trabajo está vinculada a E/S o a la CPU.
### Subprocesamiento (tareas vinculadas a E/S)
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

### Multiprocesamiento (tareas vinculadas a la CPU)
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

### Internos de Asyncio
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

## Configuración del proyecto y sistema de construcción
### Estructura del directorio del proyecto
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

### Configuración de compilación: `pyproject.toml`
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

### Gestión de dependencias con herramientas modernas
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

### Linting y calidad del código
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### Canalización de CI/CD: Acciones de GitHub
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

## Pruebas
### Marcos de prueba y configuración
El ecosistema de pruebas de Python se centra en `pytest`, el estándar de facto para las pruebas de Python.
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

### Pruebas unitarias con pytest
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

### Pruebas asíncronas y pruebas de integración
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

## Interoperabilidad
### Llamar a C/C++ con ctypes
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

### Uso de cffi para una interoperabilidad C más compleja
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

### Cython: Python con rendimiento C
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

### Pybind11: Extensiones C++
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

## Patrones de diseño
### único
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

### Patrón de fábrica
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

### Patrón de observador
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

### Patrón del administrador de contexto
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

### Patrón de estrategia
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
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

### Técnicas de optimización
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

### Evaluación comparativa
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Implementación
### Embalaje y Distribución
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### Archivo Docker
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

### Implementación específica de la plataforma
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

## El ecosistema
La fortaleza de Python no es sólo el lenguaje, sino el ecosistema construido a su alrededor.
### IA y aprendizaje automático
| Biblioteca | Propósito |
|---------|---------|
| PyTorch | Aprendizaje profundo (investigación y producción) |
| TensorFlow/Keras | Aprendizaje profundo (centrado en producción) |
| aprendizaje de ciencias | ML clásico (regresión, agrupamiento, clasificación) |
| Transformadores de cara abrazada | Modelos de visión/PNL previamente entrenados |
| LangChain / LlamaIndex | Creación de aplicaciones con LLM |
| NumPy | Computación numérica (matrices, álgebra lineal) |
| Pandas | Manipulación y análisis de datos |
| Matplotlib / Seaborn / Trama | Visualización de datos |
### Desarrollo web
| Marco | Estilo | Mejor para |
|-----------|-------|----------|
| Django | Full-stack, "baterías incluidas" | Aplicaciones web complejas con paneles de administración, ORM, autenticación |
| API rápida | Moderno, asíncrono, basado en tipos | API y microservicios (actualmente los de mayor crecimiento) |
| matraz | Mínimo, flexible | Pequeñas aplicaciones y prototipos |
| Iluminado | Centrado en aplicaciones de datos | Paneles y demostraciones de datos en Python puro |
### Automatización y secuencias de comandos
| Biblioteca | Propósito |
|---------|---------|
| `subprocess`/`os`| Administración del sistema |
| `requests`/`httpx`| Clientes HTTP |
| `BeautifulSoup`/`Scrapy`| Raspado web |
| `Selenium`/`Playwright`| Automatización del navegador |
| `Celery`| Colas de tareas distribuidas |
| `Airflow`| Orquestación del flujo de trabajo |
### Computación científica
| Biblioteca | Propósito |
|---------|---------|
| NumPy | Operaciones con matrices y álgebra lineal |
| Ciencia ficción | Algoritmos científicos (optimización, procesamiento de señales) |
| SymPy | Matemáticas simbólicas |
| Cuaderno Jupyter | Entorno informático interactivo |
| JAX | Computación numérica de alto rendimiento (acelerada por GPU) |
---

## Cuándo usar Python
| Escenario | ¿Por qué Python? Mejor alternativa |
|----------|-----------|-------------------|
| IA/ML/Ciencia de datos | El ecosistema es incomparable | — |
| Automatización y scripting | Más rápido para escribir y depurar | Shell/PowerShell para tareas simples de administrador de sistemas |
| Backends web (API) | FastAPI es excelente | Go o Java para servicios de muy alto rendimiento |
| Creación de prototipos | El camino más rápido desde la idea hasta el código de trabajo | — |
| Educación | El lenguaje más amigable para principiantes | — |
| Aplicaciones de escritorio | Posible pero poco común | C# (Windows), Swift (macOS) |
| Sistemas críticos para el rendimiento | Evitar: demasiado lento | C, C++, óxido |
| Aplicaciones móviles | No es la herramienta adecuada | Swift (iOS), Kotlin (Android) |
| Sistemas integrados | Demasiados recursos | C, Rust o MicroPython para casos simples |
---

## Versiones de Python
El idioma sigue evolucionando. Adiciones recientes clave:
| Versión | Año | Características notables |
|---------|------|-----------------|
| 3.10 | 2021 | Coincidencia de patrones estructurales (`match/case`), mejores mensajes de error |
| 3.11 | 2022 | Ejecución entre un 10 % y un 60 % más rápida, rastreos mejorados |
| 3.12 | 2023 | Cuerdas f más flexibles, declaración `type`, mejoras en el rendimiento |
| 3.13 | 2024 | Modo experimental de subprocesos libres (sin GIL), REPL mejorado |
| 3.14 | 2025 | Otras mejoras sin GIL, mejoras en el sistema de tipos |
Python 2 llegó al final de su vida útil el 1 de enero de 2020. Todos los proyectos nuevos deben usar Python 3.10 o posterior.
---

## Referencia rápida: modismos comunes
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

## Preguntas y respuestas sintéticas
### P1: ¿Cuál es la diferencia entre listas y tuplas, y cuándo debo usar cada una?
**R:** Las listas son mutables (`[]`), las tuplas son inmutables (`()`). Utilice listas cuando necesite agregar, eliminar o cambiar elementos. Utilice tuplas para colecciones fijas de datos heterogéneos, claves de diccionario, valores de retorno de funciones o cuando desee indicar "esto no debería cambiar". Las tuplas consumen un poco más la memoria y se pueden utilizar como claves set/dict; las listas no pueden.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### P2: ¿Cómo afecta el bloqueo global de intérprete (GIL) a mi código y qué debo hacer al respecto?
**R:** El GIL evita que varios subprocesos ejecuten código de bytes de Python simultáneamente, lo que hace que los subprocesos sean ineficaces para el trabajo vinculado a la CPU. Para tareas vinculadas a E/S (solicitudes de red, E/S de archivos),`threading`o`asyncio`funcionan bien porque el GIL se libera durante la E/S. Para tareas vinculadas a la CPU, use`multiprocessing`(procesos separados, cada uno con su propio GIL) o descargue a extensiones C (NumPy, Cython, Numba) que liberan el GIL internamente.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### P3: ¿Debería utilizar sugerencias de escritura en todas partes? ¿Cuáles son las compensaciones prácticas?
**R:** Las sugerencias de tipo (`def greet(name: str) -> str:`) son opcionales y no se aplican en tiempo de ejecución. Mejoran el autocompletado de IDE, detectan errores mediante herramientas de análisis estático (mypy) y la intención del documento. La compensación es una mayor verbosidad y una curva de aprendizaje para tipos avanzados (`Union`,`Generic`,`Protocol`). Recomendación: utilice sugerencias de tipo para firmas de funciones en cualquier proyecto de más de ~500 líneas; Úselos con moderación en guiones cortos. Habilite mypy en CI para una aplicación gradual.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### P4: ¿Cuáles son las mejores prácticas para manejar excepciones en Python?
**R:** Capture excepciones específicas en lugar de`except:`(que también detecta`SystemExit`y `KeyboardInterrupt`). Utilice`try/except/else/finally`para separar la lógica de ruta feliz del manejo de errores. Defina jerarquías de excepciones personalizadas para bibliotecas. Nunca utilice excepciones para controlar el flujo en código sensible al rendimiento: son lentas. Registre la excepción con`logging.exception()`para capturar el rastreo completo.
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

### P5: ¿Cómo ahorran memoria los generadores y cuándo debo usarlos en lugar de listas?
**R:** Los generadores producen valores de forma perezosa (uno a la vez, según demanda) en lugar de crear una lista completa en la memoria. Para conjuntos de datos grandes (millones de filas, secuencias infinitas, transmisión de datos), los generadores utilizan memoria constante independientemente del tamaño. Utilice generadores cuando itere una vez y no necesite indexación o `len()`. Utilice listas cuando necesite acceso aleatorio, múltiples iteraciones o la colección sea pequeña.
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

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: crear un contador de frecuencia de palabras con clasificación
**Declaración del problema:** Dado un archivo de texto grande, cuente la frecuencia de cada palabra, clasifíquelas por frecuencia (descendente) y devuelva los N primeros resultados. Maneje la insensibilidad entre mayúsculas y minúsculas, la puntuación y procese eficientemente archivos demasiado grandes para caber en la memoria.
**Paso 1: comprenda el problema:**
Necesitamos: (1) leer texto, (2) dividir en palabras, (3) normalizar mayúsculas y minúsculas, (4) eliminar puntuación, (5) contar ocurrencias, (6) ordenar por conteo descendente, (7) devolver N superior. La restricción "demasiado grande para caber en la memoria" significa que debemos procesar línea por línea con generadores.
**Paso 2: Identifique el enfoque:**
- Utilice`re.finditer`para una extracción eficiente de palabras sin crear listas intermedias.
- Utilice`collections.Counter`para incrementos de O(1) por palabra.
- Utilice `Counter.most_common(n)`, que utiliza un montón internamente: O(k log n) en lugar de O(n log n) para una clasificación completa.
- Procese línea por línea a través del generador para mantener la memoria constante.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Memoria: sólo el dictado del contador está en la memoria (una entrada por palabra única), no el contenido del archivo. Para texto en inglés, ~100.000 palabras únicas ≈ unos pocos MB.
- Tiempo: O(W) para escanear todas las palabras + O(U log N) para la extracción de las N principales, donde W = palabras totales, U = palabras únicas.
- Casos extremos: la expresión regular conserva los apóstrofes en las contracciones ("no"). El texto Unicode necesitaría la bandera`re.UNICODE`o un patrón diferente.
### Problema 2: implementar una caché LRU segura para subprocesos
**Declaración del problema:** Cree una caché de uso menos reciente (LRU) desde cero que sea segura para subprocesos, admita operaciones de obtención y colocación O(1) y desaloje automáticamente el elemento utilizado menos recientemente cuando se exceda la capacidad.
**Paso 1: comprenda el problema:**
Un caché LRU necesita: (1) búsqueda rápida por clave → mapa hash, (2) ordenamiento rápido por actualidad → lista doblemente enlazada, (3) seguridad de subprocesos → bloqueo. En `get(key)`: mueve el elemento al frente. En `put(key, val)`: inserción en la parte delantera; si excede su capacidad, retírela por la parte posterior.
**Paso 2: Identifique el enfoque:**
-`dict`de Python mantiene el orden de inserción (3.7+), por lo que podemos usar un enfoque de dictado ordenado: eliminar y volver a insertar para ir al final.
- Para seguridad del hilo, utilice`threading.Lock`para exclusión mutua.
- Alternativa: use`collections.OrderedDict`que tiene `move_to_end()`.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Complejidad temporal: O(1) tanto para`get`como para`put`—`OrderedDict.move_to_end()`y`popitem()`son O(1).
- Seguridad del hilo: el`Lock`garantiza la atomicidad. Para un mayor rendimiento, considere`threading.RLock`o un patrón de bloqueo de lectura y escritura, pero para la mayoría de los casos de uso es suficiente un bloqueo simple.
- Nota de producción: para código de un solo subproceso,`functools.lru_cache`es más simple y está implementado en C para un mejor rendimiento.
### Problema 3: analizar y evaluar una expresión matemática
**Declaración del problema:** Escriba un analizador que tome una cadena como`"3 + 4 * 2 / (1 - 5)"`y la evalúe correctamente respetando la precedencia de operadores y los paréntesis.
**Paso 1: comprenda el problema:**
Esto requiere: (1) convertir la cadena de entrada en números, operadores y paréntesis, (2) analizar con precedencia correcta (`*`y`/`antes de`+`y`-`), (3) manejar paréntesis anidados. Una evaluación ingenua de izquierda a derecha daría resultados erróneos.
**Paso 2: Identifique el enfoque:**
La solución clásica es el **algoritmo de patio de maniobras** (Dijkstra) que convierte infijo en sufijo (notación polaca inversa) y luego evalúa el sufijo. Alternativamente, utilice un analizador de descenso recursivo. Específicamente para Python, también podemos usar`ast.literal_eval`para una evaluación segura, pero implementémoslo correctamente.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Corrección:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→ `1.0`. Correcto.
- Tiempo: O(N) para tokenización, O(N) para patio de maniobras, O(N) para evaluación, O(N) general.
- Casos extremos a manejar: números negativos (anteponer`0`antes de`-`unario), división por cero (agregar manejo de errores), entrada no válida (validar tokens).
- Alternativa Pythonic:`ast.parse(expr, mode='eval')`con un visitante de nodo personalizado para una evaluación segura sin `eval()`.
### Problema 4: crear un panel CLI con actualizaciones de datos en tiempo real
**Declaración del problema:** Cree un panel basado en terminal que muestre las métricas del sistema (CPU, memoria, disco) actualizándose en tiempo real, con umbrales codificados por colores y diseño responsivo.
**Paso 1: comprenda el problema:**
Necesitamos: (1) recopilación periódica de métricas del sistema, (2) representación de terminal con control del cursor, (3) salida de color basada en umbrales, (4) entrada de teclado sin bloqueo para salir. Este es un patrón productor-consumidor con un bucle de renderizado.
**Paso 2: Identifique el enfoque:**
- Utilice`psutil`para métricas del sistema multiplataforma.
- Utilice códigos de escape ANSI para la posición del cursor y los colores (o la biblioteca`rich`para una API de nivel superior).
- Utilice`time.sleep`para el intervalo de actualización.
- Estructura como: recopilación de datos → formato → canalización de renderizado.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- El`cpu_percent(interval=0.5)`bloquea durante 0,5 segundos para medir; este es el enfoque correcto (el modo sin bloqueo da 0% en la primera llamada).
- Los códigos ANSI funcionan en terminales Windows modernos y en todos los terminales Unix. Para cmd de Windows heredado, agregue`os.system('color')`o use `colorama`.
- Actualización de producción: utilice la biblioteca`rich`(`rich.live`) para renderizado sin parpadeos, diseño automático y compatibilidad multiplataforma.
- Extensibilidad: cada métrica es una función independiente, lo que facilita agregar la temperatura de la GPU, el recuento de procesos o las conexiones de red.
---

## Resumen
La combinación de legibilidad, versatilidad y profundidad del ecosistema de Python lo convierte en el lenguaje de programación más utilizado del mundo. Es la opción predeterminada para AI/ML, una opción sólida para backends web y automatización, y un excelente lenguaje de enseñanza. Sus principales debilidades (velocidad de ejecución y soporte móvil/integrado) se comprenden bien y se han establecido soluciones alternativas. Para la mayoría de los proyectos, Python es un punto de partida razonable.