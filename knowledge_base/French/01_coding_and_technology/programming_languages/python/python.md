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
Python est un langage de programmation généraliste interprété de haut niveau, créé par Guido van Rossum et publié pour la première fois en 1991. Il donne la priorité à la lisibilité du code grâce à une indentation significative et une syntaxe claire qui se lit proche de l'anglais simple. Python est typé dynamiquement, ramassé et prend en charge plusieurs paradigmes de programmation, notamment la programmation procédurale, orientée objet et fonctionnelle.
Aujourd'hui, Python est le langage dominant dans les domaines de l'IA/ML, de la science des données, du calcul scientifique et de l'automatisation, tout en restant l'un des meilleurs langages pour les débutants. Cette double identité (assez simple pour un premier script, suffisamment puissante pour entraîner de grands modèles de langage) est ce qui le distingue.
---

## Pourquoi Python est important
- **Lisibilité dès la conception** : pas de points-virgules, pas d'accolades — l'indentation définit la portée. Le code se lit comme un pseudocode.
- **Écosystème massif** : PyPI héberge plus de 500 000 packages couvrant pratiquement tous les domaines.
- **Le langage de l'IA** : PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — l'ensemble de la pile IA/ML est d'abord Python.
- **Langage Glue** : Connectez un moteur C++ à une API web à une base de données en quelques lignes seulement.
- **Multiplateforme** : fonctionne sur Windows, macOS, Linux et les systèmes embarqués sans modification.
- **Communauté** : la communauté de programmation la plus grande et la plus active au monde.
## Les compromis
Python n'est pas parfait. Comprendre ses limites vous aide à décider quand passer à autre chose :
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Vitesse d'exécution** | 10 à 100 fois plus lent que C pour les tâches liées au processeur | Utilisez NumPy/PyTorch (C sous le capot) ou Cython/Numba pour les boucles chaudes |
| **GIL (Global Interpreter Lock)** | Empêche le véritable parallélisme multithread pour les travaux liés au processeur | Utilisez`multiprocessing`,`asyncio`ou des files d'attente de tâches comme Celery |
| **Développement mobile** | Ne convient pas aux applications iOS/Android | Utilisez Swift/Kotlin pour le natif ou Flutter/React Native pour le multiplateforme |
| **Systèmes embarqués** | Trop lourd pour les microcontrôleurs | Utilisez MicroPython (une variante légère) ou passez à C/Rust |
| **Utilisation de la mémoire** | Empreinte mémoire plus élevée que les langages compilés | Acceptable pour la plupart des applications ; utiliser des générateurs pour les données volumineuses |
---

## Fondamentaux de la syntaxe
### Variables et types
Python utilise le typage dynamique : vous ne déclarez pas de types de variables, mais vous pouvez ajouter des indications de type pour plus de clarté et pour la prise en charge des outils.
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

### Flux de contrôle
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

### Fonctions
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

### Programmation orientée objet
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

### Gestion des erreurs
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

## Syntaxe et modèles avancés
### Génériques avec le module `typing`
Le module`typing`de Python fournit une prise en charge de type générique pour la création de composants réutilisables et sécurisés. Les génériques vous permettent d'écrire des fonctions et des classes qui fonctionnent avec n'importe quel type tout en préservant les informations de type pour l'analyse statique.
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

### Décorateurs et métaprogrammation
Les décorateurs sont l'une des fonctionnalités les plus puissantes de Python : ils vous permettent de modifier ou d'étendre le comportement des fonctions et des classes sans changer leur code source.
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

### Correspondance de modèles structurels (Python 3.10+)
L'instruction`match/case`de Python fournit une puissante correspondance de modèles avec des modèles de déstructuration, de garde et d'imbrication.
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

### Fermetures, fonctions d'ordre supérieur et itérateurs
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

### Surcharge des opérateurs
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

### Hiérarchies d'exceptions personnalisées
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

## Principales fonctionnalités en profondeur
### La bibliothèque standard ("Piles incluses")
Python est livré avec une vaste bibliothèque standard. Quelques-uns des modules les plus utilisés :
| Module | Objectif | Exemple d'utilisation |
|--------|---------|-------------|
| `os`/`pathlib`| Opérations du système de fichiers | `Path("data/output.csv").exists()`|
| `json`| Encodage/décodage JSON | `json.loads(response_text)`|
| `datetime`| Gestion de la date et de l'heure | `datetime.now(timezone.utc)`|
| `collections`| Conteneurs spécialisés | `Counter(words)`,`defaultdict(list)`|
| `itertools`| Blocs de construction d'itérateur | `combinations(items, 2)`|
| `functools`| Outils fonctionnels | `lru_cache`,`partial`,`reduce`|
| `re`| Expressions régulières | `re.findall(r"\d+", text)`|
| `subprocess`| Exécuter des commandes externes | `subprocess.run(["ls", "-la"])`|
| `logging`| Journalisation des applications | `logging.basicConfig(level=logging.INFO)`|
| `typing`| Prise en charge des indices de saisie | `Optional[str]`,`Union[int, float]`|
| `http.server`| Serveur HTTP simple | `python -m http.server 8000`|
| `threading`/`asyncio`| Concurrence | E/S asynchrones pour les scrapers Web |
### Environnements virtuels et gestion des packages
Chaque projet Python doit utiliser un environnement virtuel pour isoler les dépendances :
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

Les projets Python modernes utilisent de plus en plus`pyproject.toml`avec des outils tels que`uv`,`poetry`ou`hatch`pour la gestion des dépendances, remplaçant l'ancienne approche`setup.py`/ `requirements.txt`.
### Programmation asynchrone
Le`asyncio`de Python permet des E/S simultanées sans threads, ce qui est essentiel pour les web scrapers, les serveurs de chat et les clients API :
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

## Concurrence et parallélisme
Python propose plusieurs modèles de concurrence, chacun adapté à différentes charges de travail. Le GIL (Global Interpreter Lock) de CPython empêche un véritable parallélisme du CPU avec les threads, donc le bon modèle dépend si votre charge de travail est liée aux E/S ou au CPU.
### Threading (tâches liées aux E/S)
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

### Multitraitement (tâches liées au CPU)
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

### Composants internes d'Asyncio
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

## Configuration du projet et système de construction
### Structure du répertoire du projet
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

### Configuration de construction — `pyproject.toml`
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

### Gestion des dépendances avec des outils modernes
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

### Peluchage et qualité du code
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### Pipeline CI/CD — Actions GitHub
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

## Tests
### Cadres de test et configuration
L'écosystème de test de Python est centré sur`pytest`, la norme de facto pour les tests Python.
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

### Tests unitaires avec pytest
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

### Tests asynchrones et tests d'intégration
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

## Interopérabilité
### Appeler C/C++ avec des ctypes
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

### Utilisation de cffi pour une interopérabilité C plus complexe
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

### Cython — Python avec performances C
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

### Pybind11 — Extensions C++
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

## Modèles de conception
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

### Modèle d'usine
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

### Modèle d'observateur
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

### Modèle de gestionnaire de contexte
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

### Modèle de stratégie
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

## Performances et optimisation
### Outils de profilage
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

### Techniques d'optimisation
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

### Analyse comparative
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## Déploiement
### Emballage et distribution
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### Fichier Docker
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

### Déploiement spécifique à la plate-forme
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

## L'écosystème
La force de Python ne réside pas seulement dans le langage, c'est aussi dans l'écosystème construit autour de lui.
### IA et apprentissage automatique
| Bibliothèque | Objectif |
|---------|---------|
| PyTorch | Deep learning (recherche et production) |
| TensorFlow/Keras | Apprentissage profond (axé sur la production) |
| scikit-apprendre | ML classique (régression, clustering, classification) |
| Transformateurs de visage câlins | Modèles PNL/vision pré-entraînés |
| LangChain / LlamaIndex | Créer des applications avec des LLM |
| NumPy | Informatique numérique (tableaux, algèbre linéaire) |
| Pandas | Manipulation et analyse de données |
| Matplotlib / Seaborn / Plotly | Visualisation des données |
### Développement Web
| Cadre | Style | Idéal pour |
|---------------|-------|--------------|
| Django | Full-stack, « piles incluses » | Applications Web complexes avec panneaux d'administration, ORM, authentification |
| API rapide | Moderne, asynchrone, axé sur le type | API et microservices (actuellement ceux qui connaissent la croissance la plus rapide) |
| Flacon | Minimal, flexible | Petites applications et prototypes |
| Rationalisé | Axé sur les applications de données | Tableaux de bord et démos de données en Python pur |
### Automatisation et scripts
| Bibliothèque | Objectif |
|---------|---------|
| `subprocess`/`os`| Administration système |
| `requests`/`httpx`| Clients HTTP |
| `BeautifulSoup`/`Scrapy`| Grattage Web |
| `Selenium`/`Playwright`| Automatisation du navigateur |
| `Celery`| Files d'attente de tâches distribuées |
| `Airflow`| Orchestration du flux de travail |
### Calcul scientifique
| Bibliothèque | Objectif |
|---------|---------|
| NumPy | Opérations sur les tableaux et algèbre linéaire |
| SciPy | Algorithmes scientifiques (optimisation, traitement du signal) |
| SymPy | Mathématiques symboliques |
| Carnet Jupyter | Environnement informatique interactif |
| JAX | Calcul numérique haute performance (accélération GPU) |
---

## Quand utiliser Python
| Scénario | Pourquoi Python | Meilleure alternative |
|----------|-----------|-------------------|
| IA/ML/Science des données | L'écosystème est inégalé | — |
| Automatisation et scripts | Le plus rapide à écrire et à déboguer | Shell/PowerShell pour les tâches simples d'administration système |
| Backends Web (API) | FastAPI est excellent | Go ou Java pour des services à très haut débit |
| Prototypage | Le chemin le plus rapide de l'idée au code fonctionnel | — |
| Éducation | Langue la plus adaptée aux débutants | — |
| Applications de bureau | Possible mais rare | C# (Windows), Swift (macOS) |
| Systèmes critiques en termes de performances | Éviter — trop lent | C, C++, Rouille |
| Applications mobiles | Pas le bon outil | Swift (iOS), Kotlin (Android) |
| Systèmes embarqués | Trop gourmand en ressources | C, Rust ou MicroPython pour les cas simples |
---

## Versions Python
La langue continue d'évoluer. Principaux ajouts récents :
| Version | Année | Caractéristiques notables |
|---------|------|-----------------|
| 3.10 | 2021 | Correspondance de modèles structurels (`match/case`), meilleurs messages d'erreur |
| 3.11 | 2022 | Exécution 10 à 60 % plus rapide, traçages améliorés |
| 3.12 | 2023 | Chaînes F plus flexibles, instruction `type`, gains de performances |
| 3.13 | 2024 | Mode expérimental free-thread (pas de GIL), REPL amélioré |
| 3.14 | 2025 | Autres améliorations sans GIL, améliorations du système de saisie |
Python 2 est arrivé en fin de vie le 1er janvier 2020. Tous les nouveaux projets doivent utiliser Python 3.10 ou version ultérieure.
---

## Référence rapide : expressions idiomatiques courantes
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

## Questions et réponses synthétiques
### Q1 : Quelle est la différence entre les listes et les tuples, et quand dois-je les utiliser ?
**A :** Les listes sont mutables (`[]`), les tuples sont immuables (`()`). Utilisez des listes lorsque vous devez ajouter, supprimer ou modifier des éléments. Utilisez des tuples pour des collections fixes de données hétérogènes, des clés de dictionnaire, des valeurs de retour de fonction ou lorsque vous souhaitez signaler « cela ne devrait pas changer ». Les tuples sont légèrement plus économes en mémoire et peuvent être utilisés comme clés set/dict ; les listes ne le peuvent pas.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2 : Comment le Global Interpreter Lock (GIL) affecte-t-il mon code et que dois-je faire à ce sujet ?
**R :** Le GIL empêche plusieurs threads d'exécuter le bytecode Python simultanément, ce qui rend le threading inefficace pour le travail lié au processeur. Pour les tâches liées aux E/S (requêtes réseau, E/S de fichiers),`threading`ou`asyncio`fonctionnent correctement car le GIL est libéré lors des E/S. Pour les tâches liées au processeur, utilisez`multiprocessing`(processus distincts, chacun avec son propre GIL) ou déchargez-le vers des extensions C (NumPy, Cython, Numba) qui libèrent le GIL en interne.
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3 : Dois-je utiliser des astuces de saisie partout ? Quels sont les compromis pratiques ?
**A :** Les indications de type (`def greet(name: str) -> str:`) sont facultatives et ne sont pas appliquées au moment de l'exécution. Ils améliorent la saisie semi-automatique de l'IDE, détectent les bogues via des outils d'analyse statique (mypy) et documentent l'intention. Le compromis est une verbosité supplémentaire et une courbe d'apprentissage pour les types avancés (`Union`,`Generic`,`Protocol`). Recommandation : utilisez des astuces de type pour les signatures de fonctions dans tout projet de plus de 500 lignes ; utilisez-les avec parcimonie dans des scripts courts. Activez mypy dans CI pour une application progressive.
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4 : Quelles sont les meilleures pratiques pour gérer les exceptions en Python ?
**R :** Détectez des exceptions spécifiques plutôt que`except:`(qui intercepte également`SystemExit`et `KeyboardInterrupt`). Utilisez`try/except/else/finally`pour séparer la logique du chemin heureux de la gestion des erreurs. Définissez des hiérarchies d'exceptions personnalisées pour les bibliothèques. N'utilisez jamais d'exceptions pour le flux de contrôle dans du code sensible aux performances : elles sont lentes. Enregistrez l'exception avec`logging.exception()`pour capturer le traçage complet.
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

### Q5 : Comment les générateurs économisent-ils de la mémoire et quand dois-je les utiliser sur des listes ?
**R :** Les générateurs produisent des valeurs paresseusement (une à la fois, à la demande) au lieu de créer une liste complète en mémoire. Pour les grands ensembles de données (millions de lignes, séquences infinies, données en streaming), les générateurs utilisent une mémoire constante quelle que soit leur taille. Utilisez des générateurs lorsque vous effectuez une itération une fois et que vous n'avez pas besoin d'indexation ou de`len()`. Utilisez des listes lorsque vous avez besoin d'un accès aléatoire, de plusieurs itérations ou que la collection est petite.
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : Créer un compteur de fréquence de mots avec classement
**Énoncé du problème :** Étant donné un fichier texte volumineux, comptez la fréquence de chaque mot, classez-les par fréquence (décroissant) et renvoyez les N premiers résultats. Gérez l'insensibilité à la casse, à la ponctuation et traitez efficacement les fichiers trop volumineux pour tenir en mémoire.
**Étape 1 — Comprendre le problème :**
Nous devons : (1) lire le texte, (2) diviser en mots, (3) normaliser la casse, (4) supprimer la ponctuation, (5) compter les occurrences, (6) trier par nombre décroissant, (7) renvoyer le N supérieur. La contrainte "trop grande pour tenir en mémoire" signifie que nous devons traiter ligne par ligne avec des générateurs.
**Étape 2 — Identifiez l'approche :**
- Utilisez`re.finditer`pour une extraction de mots efficace sans créer de listes intermédiaires.
- Utilisez`collections.Counter`pour l'incrément O(1) par mot.
- Utilisez`Counter.most_common(n)`qui utilise un tas en interne — O(k log n) au lieu de O(n log n) pour un tri complet.
- Traitez ligne par ligne via un générateur pour maintenir la mémoire constante.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Mémoire : seul le dict du compteur est en mémoire (une entrée par mot unique), pas le contenu du fichier. Pour le texte anglais, ~100 000 mots uniques ≈ quelques Mo.
- Temps : O(W) pour analyser tous les mots + O(U log N) pour l'extraction des N premiers, où W = nombre total de mots, U = mots uniques.
- Cas extrêmes : les apostrophes dans les contractions ("don't") sont conservées par l'expression régulière. Le texte Unicode nécessiterait l’indicateur`re.UNICODE`ou un modèle différent.
### Problème 2 : implémenter un cache LRU Thread-Safe
**Énoncé du problème :** Créez à partir de zéro un cache LRU (Les moins récemment utilisé) qui est thread-safe, prend en charge les opérations get et put O(1) et expulse automatiquement l'élément le moins récemment utilisé lorsque la capacité est dépassée.
**Étape 1 — Comprendre le problème :**
Un cache LRU a besoin de : (1) une recherche rapide par clé → carte de hachage, (2) un classement rapide par récence → liste doublement chaînée, (3) la sécurité des threads → le verrouillage. Sur`get(key)`: déplacer l'élément vers l'avant. Sur`put(key, val)`: insert à l'avant ; en cas de surcapacité, retirer par l'arrière.
**Étape 2 — Identifiez l'approche :**
-`dict`de Python maintient l'ordre d'insertion (3.7+), nous pouvons donc utiliser une approche dict ordonnée : supprimer et réinsérer pour passer à la fin.
- Pour la sécurité des threads, utilisez`threading.Lock`pour l'exclusion mutuelle.
- Alternative : utilisez`collections.OrderedDict`qui a`move_to_end()`.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Complexité temporelle : O(1) pour`get`et`put`—`OrderedDict.move_to_end()`et`popitem()`sont O(1).
- Sécurité du filetage : le`Lock`assure l'atomicité. Pour un débit plus élevé, envisagez`threading.RLock`ou un modèle de verrouillage en lecture-écriture, mais pour la plupart des cas d'utilisation, un simple verrou suffit.
- Note de production : pour le code monothread,`functools.lru_cache`est plus simple et implémenté en C pour de meilleures performances.
### Problème 3 : analyser et évaluer une expression mathématique
**Énoncé du problème :** Écrivez un analyseur qui prend une chaîne telle que`"3 + 4 * 2 / (1 - 5)"`et l'évalue correctement en respectant la priorité des opérateurs et les parenthèses.
**Étape 1 — Comprendre le problème :**
Cela nécessite : (1) la tokenisation de la chaîne d'entrée en nombres, opérateurs et parenthèses, (2) l'analyse avec la priorité correcte (`*`et`/`avant`+`et`-`), (3) la gestion des parenthèses imbriquées. Une évaluation naïve de gauche à droite donnerait des résultats erronés.
**Étape 2 — Identifiez l'approche :**
La solution classique est l'**algorithme de triage** (Dijkstra) qui convertit l'infixe en suffixe (notation polonaise inverse), puis évalue le suffixe. Vous pouvez également utiliser un analyseur de descente récursif. Pour Python en particulier, nous pouvons également utiliser`ast.literal_eval`pour une évaluation sûre – mais implémentons-le correctement.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Exactitude :`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→`1.0`. Correct.
- Temps : O(N) pour la tokenisation, O(N) pour la gare de triage, O(N) pour l'évaluation — O(N) global.
- Cas extrêmes à gérer : nombres négatifs (ajouter`0`avant unaire`-`), division par zéro (ajouter la gestion des erreurs), entrée invalide (valider les jetons).
- Alternative pythonique :`ast.parse(expr, mode='eval')`avec un visiteur de nœud personnalisé pour une évaluation sécurisée sans`eval()`.
### Problème 4 : Créer un tableau de bord CLI avec des mises à jour de données en temps réel
**Énoncé du problème :** Créez un tableau de bord basé sur un terminal qui affiche les métriques du système (CPU, mémoire, disque) mises à jour en temps réel, avec des seuils codés par couleur et une mise en page réactive.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) une collecte périodique de métriques du système, (2) un rendu de terminal avec contrôle du curseur, (3) une sortie couleur basée sur des seuils, (4) une saisie clavier non bloquante pour quitter. Il s'agit d'un modèle producteur-consommateur avec une boucle de rendu.
**Étape 2 — Identifiez l'approche :**
- Utilisez`psutil`pour les métriques système multiplateformes.
- Utilisez les codes d'échappement ANSI pour le positionnement du curseur et les couleurs (ou la bibliothèque`rich`pour une API de niveau supérieur).
- Utilisez`time.sleep`pour l'intervalle de mise à jour.
- Structure comme : collecte de données → formatage → pipeline de rendu.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Le`cpu_percent(interval=0.5)`bloque pendant 0,5 s pour mesurer — c'est la bonne approche (le mode non bloquant donne 0 % au premier appel).
- Les codes ANSI fonctionnent sur les terminaux Windows modernes et tous les terminaux Unix. Pour les anciennes cmd Windows, ajoutez`os.system('color')`ou utilisez`colorama`.
- Mise à niveau de production : utilisez la bibliothèque`rich`(`rich.live`) pour un rendu sans scintillement, une mise en page automatique et une compatibilité multiplateforme.
- Extensibilité : chaque métrique est une fonction indépendante, ce qui facilite l'ajout de la température du GPU, du nombre de processus ou des connexions réseau.
---

## Résumé
La combinaison de lisibilité, de polyvalence et de profondeur de l'écosystème de Python en fait le langage de programmation le plus utilisé au monde. Il s'agit du choix par défaut pour l'IA/ML, une option solide pour les backends Web et l'automatisation, et un excellent langage d'enseignement. Ses principales faiblesses – vitesse d’exécution et prise en charge mobile/embarquée – sont bien comprises et des solutions de contournement ont été établies. Pour la plupart des projets, Python constitue un point de départ raisonnable.