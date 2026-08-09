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

#หลาม
Python เป็นภาษาโปรแกรมระดับสูงที่มีการตีความและมีวัตถุประสงค์ทั่วไป สร้างขึ้นโดย Guido van Rossum และเปิดตัวครั้งแรกในปี 1991 โดยจัดลำดับความสำคัญของความสามารถในการอ่านโค้ดผ่านการเยื้องที่สำคัญและไวยากรณ์ที่สะอาดตาที่อ่านได้ใกล้เคียงกับภาษาอังกฤษธรรมดา Python มีการพิมพ์แบบไดนามิก รวบรวมขยะ และรองรับกระบวนทัศน์การเขียนโปรแกรมหลายรูปแบบ รวมถึงการเขียนโปรแกรมเชิงขั้นตอน เชิงวัตถุ และเชิงฟังก์ชัน
ปัจจุบัน Python เป็นภาษาที่โดดเด่นในด้าน AI/ML วิทยาศาสตร์ข้อมูล การประมวลผลเชิงวิทยาศาสตร์ และระบบอัตโนมัติ ในขณะที่ยังคงเป็นหนึ่งในภาษาที่ดีที่สุดสำหรับผู้เริ่มต้น เอกลักษณ์คู่นั้น (ง่ายพอสำหรับสคริปต์แรก ทรงพลังพอที่จะฝึกฝนโมเดลภาษาขนาดใหญ่) คือสิ่งที่ทำให้มันแตกต่าง
---

## ทำไม Python จึงมีความสำคัญ
- **ความสามารถในการอ่านตามการออกแบบ**: ไม่มีอัฒภาค ไม่มีเครื่องหมายปีกกา — การเยื้องจะกำหนดขอบเขต รหัสอ่านเหมือนรหัสเทียม
- **ระบบนิเวศขนาดใหญ่**: PyPI โฮสต์แพ็คเกจมากกว่า 500,000 รายการ ครอบคลุมแทบทุกโดเมน
- **ภาษาของ AI**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain — สแต็ก AI/ML ทั้งหมดเน้น Python เป็นหลัก
- **ภาษากาว**: เชื่อมต่อกลไก C++ กับเว็บ API ไปยังฐานข้อมูลภายในเพียงไม่กี่บรรทัด
- **ข้ามแพลตฟอร์ม**: ทำงานบน Windows, macOS, Linux และระบบฝังตัวโดยไม่มีการดัดแปลง
- **ชุมชน**: ชุมชนการเขียนโปรแกรมที่ใหญ่ที่สุดและกระตือรือร้นที่สุดในโลก
## การแลกเปลี่ยน
Python ไม่สมบูรณ์แบบ การทำความเข้าใจข้อจำกัดของมันช่วยให้คุณตัดสินใจว่าเมื่อใดควรเข้าถึงสิ่งอื่น:
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ความเร็วในการดำเนินการ** | ช้ากว่า C 10–100 เท่าสำหรับงานที่ผูกกับ CPU ใช้ NumPy/PyTorch (C ใต้ฝากระโปรง) หรือ Cython/Numba สำหรับ hot loop |
| **GIL (ล็อคล่ามสากล)** | ป้องกันการขนานแบบมัลติเธรดที่แท้จริงสำหรับงานที่ผูกกับ CPU ใช้`multiprocessing`,`asyncio`หรือคิวงานเช่น Celery |
| **การพัฒนามือถือ** | ไม่เหมาะกับแอป iOS/Android | ใช้ Swift/Kotlin สำหรับเนทีฟ หรือใช้ Flutter/React Native สำหรับข้ามแพลตฟอร์ม |
| **ระบบสมองกลฝังตัว** | หนักเกินไปสำหรับไมโครคอนโทรลเลอร์ | ใช้ MicroPython (เวอร์ชันน้ำหนักเบา) หรือเปลี่ยนเป็น C/Rust |
| **การใช้หน่วยความจำ** | หน่วยความจำที่สูงกว่าภาษาที่คอมไพล์ | ยอมรับได้สำหรับแอปพลิเคชันส่วนใหญ่ ใช้เครื่องกำเนิดไฟฟ้าสำหรับข้อมูลขนาดใหญ่ |
---

## พื้นฐานไวยากรณ์
### ตัวแปรและประเภท
Python ใช้การพิมพ์แบบไดนามิก คุณไม่ต้องประกาศประเภทตัวแปร แต่คุณสามารถเพิ่มคำแนะนำประเภทเพื่อความชัดเจนและการสนับสนุนเครื่องมือได้
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

### การควบคุมการไหล
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

### ฟังก์ชั่น
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

### การเขียนโปรแกรมเชิงวัตถุ
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

### การจัดการข้อผิดพลาด
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ข้อมูลทั่วไปที่มีโมดูล `typing`
โมดูล`typing`ของ Python ให้การสนับสนุนประเภททั่วไปสำหรับการสร้างส่วนประกอบที่ใช้ซ้ำได้และปลอดภัยต่อประเภท ข้อมูลทั่วไปช่วยให้คุณสามารถเขียนฟังก์ชันและคลาสที่ทำงานกับประเภทใดก็ได้ โดยที่ยังคงรักษาข้อมูลประเภทไว้สำหรับการวิเคราะห์แบบคงที่
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

### ตกแต่งและการเขียนโปรแกรมเมตา
Decorators เป็นหนึ่งในคุณสมบัติที่ทรงพลังที่สุดของ Python โดยให้คุณแก้ไขหรือขยายพฤติกรรมของฟังก์ชันและคลาสโดยไม่ต้องเปลี่ยนซอร์สโค้ด
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

### การจับคู่รูปแบบโครงสร้าง (Python 3.10+)
คำสั่ง`match/case`ของ Python ให้การจับคู่รูปแบบที่มีประสิทธิภาพกับการทำลายล้าง การป้องกัน และรูปแบบที่ซ้อนกัน
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

### การปิด ฟังก์ชันลำดับที่สูงกว่า และตัววนซ้ำ
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

### โอเปอเรเตอร์โอเวอร์โหลด
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

### ลำดับชั้นข้อยกเว้นที่กำหนดเอง
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

## คุณสมบัติหลักในเชิงลึก
### ไลบรารีมาตรฐาน ("รวมแบตเตอรี่")
Python มาพร้อมกับไลบรารีมาตรฐานที่กว้างขวาง โมดูลที่ใช้มากที่สุดบางส่วน:
| โมดูล | วัตถุประสงค์ | ตัวอย่างการใช้ |
|--------|---------|-------------|
| `os`/`pathlib`| การทำงานของระบบไฟล์ | `Path("data/output.csv").exists()`|
| `json`| การเข้ารหัส / ถอดรหัส JSON | `json.loads(response_text)`|
| `datetime`| การจัดการวันที่และเวลา | `datetime.now(timezone.utc)`|
| `collections`| ตู้คอนเทนเนอร์แบบพิเศษ | `Counter(words)`,`defaultdict(list)`|
| `itertools`| หน่วยการสร้างตัววนซ้ำ | `combinations(items, 2)`|
| `functools`| เครื่องมือฟังก์ชั่น | `lru_cache`,`partial`,`reduce`|
| `re`| นิพจน์ทั่วไป | `re.findall(r"\d+", text)`|
| `subprocess`| เรียกใช้คำสั่งภายนอก | `subprocess.run(["ls", "-la"])`|
| `logging`| การบันทึกแอปพลิเคชัน | `logging.basicConfig(level=logging.INFO)`|
| `typing`| พิมพ์คำใบ้สนับสนุน | `Optional[str]`,`Union[int, float]`|
| `http.server`| เซิร์ฟเวอร์ HTTP แบบธรรมดา | `python -m http.server 8000`|
| `threading`/`asyncio`| เห็นพ้องต้องกัน | Async I/O สำหรับเว็บแครปเปอร์ |
### สภาพแวดล้อมเสมือนจริงและการจัดการแพ็คเกจ
ทุกโครงการ Python ควรใช้สภาพแวดล้อมเสมือนเพื่อแยกการพึ่งพา:
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

โปรเจ็กต์ Python สมัยใหม่ใช้`pyproject.toml`กับเครื่องมือต่างๆ เช่น`uv`,`poetry`หรือ`hatch`มากขึ้นเรื่อยๆ สำหรับการจัดการการพึ่งพา โดยแทนที่แนวทาง`setup.py`/`requirements.txt`แบบเก่า
### การเขียนโปรแกรมแบบอะซิงโครนัส
`asyncio` ของ Python เปิดใช้งาน I/O พร้อมกันโดยไม่มีเธรด ซึ่งจำเป็นสำหรับเว็บสแครปเปอร์ เซิร์ฟเวอร์แชท และไคลเอนต์ API:
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

## การเห็นพ้องต้องกันและความเท่าเทียม
Python มีโมเดลการทำงานพร้อมกันหลายรูปแบบ ซึ่งแต่ละโมเดลเหมาะกับปริมาณงานที่แตกต่างกัน GIL (Global Interpreter Lock) ใน CPython ป้องกันการขนานกันของ CPU กับเธรดอย่างแท้จริง ดังนั้นโมเดลที่ถูกต้องจึงขึ้นอยู่กับว่าปริมาณงานของคุณเป็น I/O-bound หรือ CPU-bound
### เธรด (งาน I/O-bound)
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

### การประมวลผลหลายตัว (งานที่เกี่ยวข้องกับ CPU)
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างไดเรกทอรีโครงการ
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

### การกำหนดค่าบิวด์ — `pyproject.toml`
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

### การจัดการการพึ่งพาด้วยเครื่องมือที่ทันสมัย
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

### Linting และคุณภาพของรหัส
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### ไปป์ไลน์ CI/CD — การดำเนินการ GitHub
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

## การทดสอบ
### กรอบการทดสอบและการตั้งค่า
ระบบนิเวศการทดสอบของ Python มีศูนย์กลางอยู่ที่`pytest`ซึ่งเป็นมาตรฐานโดยพฤตินัยสำหรับการทดสอบ Python
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

### การทดสอบหน่วยด้วย pytest
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

### การทดสอบ Async และการทดสอบการรวมระบบ
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

## การทำงานร่วมกัน
### กำลังเรียก C/C++ ด้วย ctypes
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

### การใช้ cffi สำหรับ More Complex C Interop
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

### Cython - Python พร้อมประสิทธิภาพของ C
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

### Pybind11 — ส่วนขยาย C++
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

## รูปแบบการออกแบบ
### ซิงเกิลตัน
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

### ลายโรงงาน
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

### รูปแบบผู้สังเกตการณ์
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

### รูปแบบตัวจัดการบริบท
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

### รูปแบบกลยุทธ์
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

### การเปรียบเทียบ
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## การปรับใช้
### บรรจุภัณฑ์และการจัดจำหน่าย
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### ด็อคเกอร์ไฟล์
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

### การใช้งานเฉพาะแพลตฟอร์ม
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

## ระบบนิเวศ
จุดแข็งของ Python ไม่ใช่แค่ภาษาเท่านั้น แต่ยังรวมถึงระบบนิเวศที่สร้างขึ้นด้วย
### AI และการเรียนรู้ของเครื่อง
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| ไพทอร์ช | การเรียนรู้เชิงลึก (การวิจัยและการผลิต) |
| TensorFlow / Keras | การเรียนรู้เชิงลึก (เน้นการผลิต) |
| scikit-เรียนรู้ | Classical ML (การถดถอย การจัดกลุ่ม การจำแนกประเภท) |
| กอดใบหน้า Transformers | NLP/โมเดลการมองเห็นที่ผ่านการฝึกอบรมล่วงหน้า |
| LangChain / LlamaIndex | การสร้างแอปพลิเคชันด้วย LLM |
| นัมปี | การคำนวณเชิงตัวเลข (อาร์เรย์ พีชคณิตเชิงเส้น) |
| หมีแพนด้า | การจัดการและการวิเคราะห์ข้อมูล |
| Matplotlib / ทะเลเกิด / พล็อต | การแสดงข้อมูลเป็นภาพ |
### การพัฒนาเว็บ
| กรอบ | สไตล์ | ดีที่สุดสำหรับ |
|----------|-------|----------|
| จังโก้ | กองเต็ม "รวมแบตเตอรี่" | เว็บแอปที่ซับซ้อนพร้อมแผงผู้ดูแลระบบ, ORM, auth |
| FastAPI | ทันสมัย ​​ไม่ตรงกัน ขับเคลื่อนด้วยประเภท | API และไมโครเซอร์วิส (ปัจจุบันเติบโตเร็วที่สุด) |
| กระติกน้ำ | น้อยที่สุด ยืดหยุ่น | แอพขนาดเล็กและต้นแบบ |
| สตรีมไลท์ | แอปข้อมูลเน้น | แดชบอร์ดและการสาธิตข้อมูลใน Python | ล้วนๆ
### ระบบอัตโนมัติและการเขียนสคริปต์
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| `subprocess`/`os`| การดูแลระบบ |
| `requests`/`httpx`| ไคลเอนต์ HTTP |
| `BeautifulSoup`/`Scrapy`| การขูดเว็บ |
| `Selenium`/`Playwright`| เบราว์เซอร์อัตโนมัติ |
| `Celery`| คิวงานแบบกระจาย |
| `Airflow`| การจัดลำดับเวิร์กโฟลว์ |
### คอมพิวเตอร์วิทยาศาสตร์
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| นัมปี | การดำเนินการอาร์เรย์และพีชคณิตเชิงเส้น |
| วิทย์ | อัลกอริธึมทางวิทยาศาสตร์ (การเพิ่มประสิทธิภาพ การประมวลผลสัญญาณ) |
| ซิมปี | คณิตศาสตร์เชิงสัญลักษณ์ |
| โน๊ตบุ๊ค Jupyter | สภาพแวดล้อมการคำนวณแบบโต้ตอบ |
| แจ๊กซ์ | การคำนวณเชิงตัวเลขประสิทธิภาพสูง (เร่งด้วย GPU) |
---

## เมื่อใดควรใช้ Python
| สถานการณ์ | ทำไมต้องหลาม | ทางเลือกที่ดีกว่า |
|----------|-----------|-------------------|
| AI/ML/วิทยาศาสตร์ข้อมูล | ระบบนิเวศน์ไม่มีใครเทียบได้ | — |
| ระบบอัตโนมัติและการเขียนสคริปต์ | เร็วที่สุดในการเขียนและแก้ไขข้อบกพร่อง | Shell/PowerShell สำหรับงานดูแลระบบอย่างง่าย |
| เว็บแบ็กเอนด์ (API) | FastAPI นั้นยอดเยี่ยม | ไปหรือ Java สำหรับบริการที่มีปริมาณงานสูงมาก |
| การสร้างต้นแบบ | เส้นทางที่เร็วที่สุดจากแนวคิดไปสู่โค้ดที่ใช้งานได้ | — |
| การศึกษา | ภาษาที่เป็นมิตรกับผู้เริ่มต้นมากที่สุด | — |
| แอปพลิเคชันเดสก์ท็อป | เป็นไปได้แต่ไม่ธรรมดา | C# (Windows), Swift (macOS) |
| ระบบที่เน้นประสิทธิภาพ | หลีกเลี่ยง — ช้าเกินไป | C, C++, สนิม |
| แอพมือถือ | ไม่ใช่เครื่องมือที่เหมาะสม | Swift (iOS), Kotlin (Android) |
| ระบบสมองกลฝังตัว | ทรัพยากรมากเกินไป | C, Rust หรือ MicroPython สำหรับกรณีธรรมดา |
---

## เวอร์ชันหลาม
ภาษายังคงพัฒนาต่อไป การเพิ่มล่าสุดที่สำคัญ:
| เวอร์ชั่น | ปี | คุณสมบัติเด่น |
|---------|-|-----------------|
| 3.10 | 2021 | การจับคู่รูปแบบโครงสร้าง (`match/case`) ข้อความแสดงข้อผิดพลาดที่ดีกว่า |
| 3.11 | 2022 | ดำเนินการเร็วขึ้น 10–60% ปรับปรุงการติดตามย้อนกลับ |
| 3.12 | 2023 | f-strings ที่ยืดหยุ่นมากขึ้น, คำสั่ง `type`, ประสิทธิภาพที่เพิ่มขึ้น |
| 3.13 | 2024 | โหมดฟรีเธรดแบบทดลอง (ไม่มี GIL) ปรับปรุง REPL |
| 3.14 | 2025 | การปรับปรุงที่ไม่มี GIL เพิ่มเติม การปรับปรุงระบบประเภท |
Python 2 สิ้นสุดอายุการใช้งานในวันที่ 1 มกราคม 2020 โปรเจ็กต์ใหม่ทั้งหมดควรใช้ Python 3.10 หรือใหม่กว่า
---

## การอ้างอิงด่วน: สำนวนทั่วไป
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

## สรุป
การผสมผสานระหว่างความสามารถในการอ่าน ความอเนกประสงค์ และความลึกของระบบนิเวศของ Python ทำให้ Python เป็นภาษาโปรแกรมที่ใช้กันอย่างแพร่หลายมากที่สุดในโลก มันเป็นตัวเลือกเริ่มต้นสำหรับ AI/ML ซึ่งเป็นตัวเลือกที่ดีสำหรับแบ็กเอนด์ของเว็บและระบบอัตโนมัติ และเป็นภาษาการสอนที่ยอดเยี่ยม จุดอ่อนหลัก — ความเร็วในการดำเนินการและการสนับสนุนบนมือถือ/แบบฝัง — เป็นที่เข้าใจกันดีและได้กำหนดแนวทางแก้ไขแล้ว สำหรับโปรเจ็กต์ส่วนใหญ่ Python เป็นจุดเริ่มต้นที่สมเหตุสมผล