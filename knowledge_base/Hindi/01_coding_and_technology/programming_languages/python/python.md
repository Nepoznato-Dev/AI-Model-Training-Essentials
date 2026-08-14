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

#पायथन
पायथन एक उच्च-स्तरीय, व्याख्या की गई, सामान्य-उद्देश्य वाली प्रोग्रामिंग भाषा है जो गुइडो वैन रोसुम द्वारा बनाई गई थी और पहली बार 1991 में जारी की गई थी। यह महत्वपूर्ण इंडेंटेशन और एक साफ वाक्यविन्यास के माध्यम से कोड पठनीयता को प्राथमिकता देता है जो सादे अंग्रेजी के करीब पढ़ता है। पायथन गतिशील रूप से टाइप किया गया है, कचरा-संग्रहित है, और प्रक्रियात्मक, ऑब्जेक्ट-ओरिएंटेड और कार्यात्मक प्रोग्रामिंग सहित कई प्रोग्रामिंग प्रतिमानों का समर्थन करता है।
आज, पायथन एआई/एमएल, डेटा साइंस, वैज्ञानिक कंप्यूटिंग और ऑटोमेशन में प्रमुख भाषा है - जबकि शुरुआती लोगों के लिए सबसे अच्छी भाषाओं में से एक बनी हुई है। वह दोहरी पहचान (पहली स्क्रिप्ट के लिए पर्याप्त सरल, बड़े भाषा मॉडल को प्रशिक्षित करने के लिए पर्याप्त शक्तिशाली) ही इसे अलग करती है।
---

## पायथन क्यों मायने रखता है
- **डिज़ाइन द्वारा पठनीयता**: कोई अर्धविराम, कोई ब्रेसिज़ नहीं - इंडेंटेशन दायरे को परिभाषित करता है। कोड छद्मकोड की तरह पढ़ता है।
- **विशाल पारिस्थितिकी तंत्र**: PyPI लगभग हर डोमेन को कवर करते हुए 500,000 से अधिक पैकेज होस्ट करता है।
- **AI की भाषा**: PyTorch, TensorFlow, scikit-learn, Hugging Face, LangChain - संपूर्ण AI/ML स्टैक Python-first है।
- **ग्लू भाषा**: एक C++ इंजन को वेब एपीआई से कुछ ही पंक्तियों में डेटाबेस से कनेक्ट करें।
- **क्रॉस-प्लेटफ़ॉर्म**: विंडोज़, मैकओएस, लिनक्स और एम्बेडेड सिस्टम पर बिना किसी संशोधन के चलता है।
- **समुदाय**: दुनिया का सबसे बड़ा और सबसे सक्रिय प्रोग्रामिंग समुदाय।
## समझौता
पाइथॉन पूर्ण नहीं है. इसकी सीमाओं को समझने से आपको यह निर्णय लेने में मदद मिलती है कि किसी और चीज़ तक कब पहुंचना है:
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **निष्पादन गति** | सीपीयू-बाध्य कार्यों के लिए सी की तुलना में 10-100 गुना धीमा | हॉट लूप के लिए NumPy/PyTorch (हुड के नीचे C), या Cython/Numba का उपयोग करें |
| **जीआईएल (ग्लोबल इंटरप्रेटर लॉक)** | सीपीयू-बाउंड कार्य के लिए वास्तविक बहु-थ्रेडेड समानता को रोकता है |`multiprocessing`,`asyncio`, या सेलेरी जैसी कार्य कतारों का उपयोग करें |
| **मोबाइल विकास** | आईओएस/एंड्रॉइड ऐप्स के लिए उपयुक्त नहीं है | नेटिव के लिए स्विफ्ट/कोटलिन, या क्रॉस-प्लेटफ़ॉर्म के लिए फ़्लटर/रिएक्ट नेटिव का उपयोग करें
| **एम्बेडेड सिस्टम** | माइक्रोकंट्रोलर्स के लिए बहुत भारी | माइक्रोपायथन (एक हल्का संस्करण) का उपयोग करें या सी/रस्ट | पर स्विच करें
| **मेमोरी उपयोग** | संकलित भाषाओं की तुलना में अधिक मेमोरी फ़ुटप्रिंट | अधिकांश अनुप्रयोगों के लिए स्वीकार्य; बड़े डेटा के लिए जनरेटर का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
### चर और प्रकार
पायथन डायनामिक टाइपिंग का उपयोग करता है - आप परिवर्तनीय प्रकार घोषित नहीं करते हैं, लेकिन आप स्पष्टता और टूलींग समर्थन के लिए प्रकार संकेत जोड़ सकते हैं।
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

### प्रवाह को नियंत्रित करें
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

### कार्य
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

### ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग
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

### त्रुटि प्रबंधन
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

## उन्नत सिंटैक्स और पैटर्न
###`typing`मॉड्यूल के साथ जेनरिक
पायथन का`typing`मॉड्यूल पुन: प्रयोज्य, प्रकार-सुरक्षित घटकों के निर्माण के लिए सामान्य प्रकार का समर्थन प्रदान करता है। जेनरिक आपको ऐसे फ़ंक्शन और कक्षाएं लिखने देता है जो स्थैतिक विश्लेषण के लिए प्रकार की जानकारी को संरक्षित करते हुए किसी भी प्रकार के साथ काम करते हैं।
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

### डेकोरेटर और मेटाप्रोग्रामिंग
डेकोरेटर्स पायथन की सबसे शक्तिशाली विशेषताओं में से एक हैं - वे आपको उनके स्रोत कोड को बदले बिना फ़ंक्शन और कक्षाओं के व्यवहार को संशोधित या विस्तारित करने देते हैं।
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

### संरचनात्मक पैटर्न मिलान (पायथन 3.10+)
पायथन का`match/case`स्टेटमेंट डिस्ट्रक्चरिंग, गार्ड और नेस्टेड पैटर्न के साथ शक्तिशाली पैटर्न मिलान प्रदान करता है।
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

### क्लोज़र, उच्च-क्रम फ़ंक्शंस, और इटरेटर
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

### ऑपरेटर ओवरलोडिंग
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

### कस्टम अपवाद पदानुक्रम
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

## गहराई में मुख्य विशेषताएं
### मानक पुस्तकालय ("बैटरी शामिल")
एक व्यापक मानक पुस्तकालय के साथ पायथन जहाज। सबसे अधिक उपयोग किए जाने वाले कुछ मॉड्यूल:
| मॉड्यूल | उद्देश्य | उदाहरण प्रयोग |
|--------|---|---|
| `os`/`pathlib`| फ़ाइल सिस्टम संचालन | `Path("data/output.csv").exists()`|
| `json`| JSON एन्कोडिंग/डिकोडिंग | `json.loads(response_text)`|
| `datetime`| दिनांक और समय प्रबंधन | `datetime.now(timezone.utc)`|
| `collections`| विशिष्ट कंटेनर | `Counter(words)`,`defaultdict(list)`|
| `itertools`| इटरेटर बिल्डिंग ब्लॉक्स | `combinations(items, 2)`|
| `functools`| कार्य उपकरण | `lru_cache`,`partial`,`reduce`|
| `re`| नियमित अभिव्यक्ति | `re.findall(r"\d+", text)`|
| `subprocess`| बाहरी आदेश चलाएँ | `subprocess.run(["ls", "-la"])`|
| `logging`| एप्लिकेशन लॉगिंग | `logging.basicConfig(level=logging.INFO)`|
| `typing`| संकेत समर्थन टाइप करें | `Optional[str]`,`Union[int, float]`|
| `http.server`| सरल HTTP सर्वर | `python -m http.server 8000`|
| `threading`/`asyncio`| समवर्ती | वेब स्क्रेपर्स के लिए Async I/O |
### आभासी वातावरण और पैकेज प्रबंधन
प्रत्येक पायथन परियोजना को निर्भरता को अलग करने के लिए एक आभासी वातावरण का उपयोग करना चाहिए:
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

आधुनिक पायथन प्रोजेक्ट निर्भरता प्रबंधन के लिए`uv`,`poetry`, या`hatch`जैसे टूल के साथ`pyproject.toml`का उपयोग कर रहे हैं, जो पुराने`setup.py`/`requirements.txt`दृष्टिकोण की जगह ले रहे हैं।
### एसिंक प्रोग्रामिंग
पायथन का`asyncio`बिना थ्रेड के समवर्ती I/O को सक्षम बनाता है - वेब स्क्रेपर्स, चैट सर्वर और एपीआई क्लाइंट के लिए आवश्यक:
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

## समवर्ती एवं समांतरता
पायथन कई समवर्ती मॉडल पेश करता है, जिनमें से प्रत्येक अलग-अलग कार्यभार के लिए उपयुक्त है। CPython में GIL (ग्लोबल इंटरप्रेटर लॉक) थ्रेड के साथ वास्तविक CPU समानता को रोकता है, इसलिए सही मॉडल इस बात पर निर्भर करता है कि आपका कार्यभार I/O-बाउंड है या CPU-बाउंड है।
### थ्रेडिंग (आई/ओ-बाध्य कार्य)
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

### मल्टीप्रोसेसिंग (सीपीयू-बाध्य कार्य)
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

### एसिंसिओ इंटरनल्स
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना निर्देशिका संरचना
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

### कॉन्फ़िगरेशन बनाएँ - `pyproject.toml`
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

### आधुनिक उपकरणों के साथ निर्भरता प्रबंधन
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

### लिंटिंग और कोड गुणवत्ता
```bash
# Ruff — extremely fast linter and formatter (replaces flake8, isort, black)
ruff check .                  # Lint
ruff check --fix .            # Auto-fix lint issues
ruff format .                 # Format code

# Mypy — static type checking
mypy src/                     # Check types
mypy --strict src/            # Strict mode
```

### सीआई/सीडी पाइपलाइन - गिटहब क्रियाएँ
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

## परीक्षण
### परीक्षण ढाँचे और सेटअप
पायथन का परीक्षण पारिस्थितिकी तंत्र`pytest`के आसपास केंद्रित है, जो पायथन परीक्षण के लिए वास्तविक मानक है।
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

### पाइटेस्ट के साथ यूनिट टेस्ट
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

### Async परीक्षण और एकीकरण परीक्षण
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

## अंतरसंचालनीयता
### ctypes के साथ C/C++ को कॉल करना
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

### अधिक कॉम्प्लेक्स सी इंटरऑप के लिए सीएफआई का उपयोग करना
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

### साइथॉन - सी परफॉर्मेंस के साथ पायथन
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

### Pybind11 - C++ एक्सटेंशन
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

## डिज़ाइन पैटर्न
### सिंगलटन
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

### फ़ैक्टरी पैटर्न
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

### प्रेक्षक पैटर्न
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

### संदर्भ प्रबंधक पैटर्न
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

### रणनीति पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### अनुकूलन तकनीकें
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

### बेंचमार्किंग
```python
import timeit

# Benchmark a small code snippet
setup = "from math import sqrt"
stmt = "sqrt(12345.6789)"

time = timeit.timeit(stmt, setup=setup, number=1_000_000)
print(f"1M iterations: {time:.3f}s")
```

---

## तैनाती
### पैकेजिंग और वितरण
```bash
# Build a wheel and source distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install my-package
```

### डॉकरफ़ाइल
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

### प्लेटफ़ॉर्म-विशिष्ट परिनियोजन
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

## पारिस्थितिकी तंत्र
पायथन की ताकत सिर्फ भाषा नहीं है - यह इसके चारों ओर बना पारिस्थितिकी तंत्र है।
### एआई और मशीन लर्निंग
| पुस्तकालय | उद्देश्य |
|---------|---------|
| पायटोरच | गहन शिक्षा (अनुसंधान और उत्पादन) |
| टेन्सरफ्लो / केरस | गहन शिक्षा (उत्पादन-केंद्रित) |
| स्किकिट-लर्न | शास्त्रीय एमएल (प्रतिगमन, क्लस्टरिंग, वर्गीकरण) |
| हगिंग फेस ट्रांसफॉर्मर | पूर्व-प्रशिक्षित एनएलपी/विज़न मॉडल |
| लैंगचेन / लामाइंडेक्स | एलएलएम के साथ अनुप्रयोगों का निर्माण |
| न्यूमपी | संख्यात्मक कंप्यूटिंग (सरणी, रैखिक बीजगणित) |
| पांडा | डेटा हेरफेर और विश्लेषण |
| मैटप्लोटलिब/सीबॉर्न/प्लॉटली | डेटा विज़ुअलाइज़ेशन |
### वेब विकास
| ढाँचा | शैली | के लिए सर्वश्रेष्ठ |
|----|-------|-------|
| जैंगो | फुल-स्टैक, "बैटरी शामिल" | एडमिन पैनल, ओआरएम, ऑथ के साथ जटिल वेब ऐप्स |
| फास्टएपीआई | आधुनिक, एसिंक्स, टाइप-संचालित | एपीआई और माइक्रोसर्विसेज (वर्तमान में सबसे तेजी से बढ़ने वाली) |
| फ्लास्क | न्यूनतम, लचीला | छोटे ऐप्स और प्रोटोटाइप |
| स्ट्रीमलाइट | डेटा-ऐप केंद्रित | शुद्ध पायथन में डैशबोर्ड और डेटा डेमो |
### स्वचालन और स्क्रिप्टिंग
| पुस्तकालय | उद्देश्य |
|---------|---------|
| `subprocess`/`os`| सिस्टम प्रशासन |
| `requests`/`httpx`| HTTP क्लाइंट |
| `BeautifulSoup`/`Scrapy`| वेब स्क्रैपिंग |
| `Selenium`/`Playwright`| ब्राउज़र स्वचालन |
| `Celery`| वितरित कार्य कतारें |
| `Airflow`| वर्कफ़्लो ऑर्केस्ट्रेशन |
### वैज्ञानिक कंप्यूटिंग
| पुस्तकालय | उद्देश्य |
|---------|---------|
| न्यूमपी | सारणी संचालन और रैखिक बीजगणित |
| साइपी | वैज्ञानिक एल्गोरिदम (अनुकूलन, सिग्नल प्रोसेसिंग) |
| सिम्पी | प्रतीकात्मक गणित |
| ज्यूपिटर नोटबुक | इंटरैक्टिव कंप्यूटिंग वातावरण |
| जैक्स | उच्च-प्रदर्शन संख्यात्मक कंप्यूटिंग (जीपीयू-त्वरित) |
---

## पायथन का उपयोग कब करें
| परिदृश्य | पायथन क्यों | बेहतर विकल्प |
|---|----|-----|
| एआई/एमएल/डेटा विज्ञान | पारिस्थितिकी तंत्र बेजोड़ है | — |
| स्वचालन और स्क्रिप्टिंग | लिखने और डीबग करने में सबसे तेज़ | सरल सिस्टम एडमिन कार्यों के लिए शेल/पॉवरशेल |
| वेब बैकएंड (एपीआई) | फास्टएपीआई उत्कृष्ट है | अत्यधिक उच्च-थ्रूपुट सेवाओं के लिए जाएं या जावा |
| प्रोटोटाइपिंग | आइडिया से वर्किंग कोड तक का सबसे तेज़ रास्ता | — |
| शिक्षा | सबसे शुरुआती-अनुकूल भाषा | — |
| डेस्कटॉप एप्लिकेशन | संभव लेकिन असामान्य | सी# (विंडोज़), स्विफ्ट (मैकओएस) |
| प्रदर्शन-महत्वपूर्ण सिस्टम | बचें - बहुत धीमी गति से | सी, सी++, जंग |
| मोबाइल ऐप्स | सही उपकरण नहीं | स्विफ्ट (आईओएस), कोटलिन (एंड्रॉइड) |
| एंबेडेड सिस्टम | बहुत अधिक संसाधन-भारी | साधारण मामलों के लिए सी, रस्ट, या माइक्रोपायथन |
---

## पायथन संस्करण
भाषा का विकास जारी है। प्रमुख हालिया परिवर्धन:
| संस्करण | वर्ष | उल्लेखनीय विशेषताएं |
|------|------|-----------------|
| 3.10 | 2021 | संरचनात्मक पैटर्न मिलान (`match/case`), बेहतर त्रुटि संदेश |
| 3.11 | 2022 | 10-60% तेज़ निष्पादन, बेहतर ट्रेसबैक |
| 3.12 | 2023 | अधिक लचीली एफ-स्ट्रिंग्स,`type`स्टेटमेंट, प्रदर्शन लाभ |
| 3.13 | 2024 | प्रायोगिक फ्री-थ्रेडेड मोड (कोई जीआईएल नहीं), बेहतर आरईपीएल |
| 3.14 | 2025 | इसके अलावा नो-जीआईएल सुधार, प्रकार सिस्टम संवर्द्धन |
1 जनवरी, 2020 को Python 2 का जीवनकाल समाप्त हो गया। सभी नई परियोजनाओं में Python 3.10 या उसके बाद के संस्करण का उपयोग किया जाना चाहिए।
---

## त्वरित संदर्भ: सामान्य मुहावरे
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

## सिंथेटिक प्रश्नोत्तर
### Q1: सूचियों और टुपल्स के बीच क्या अंतर है, और मुझे प्रत्येक का उपयोग कब करना चाहिए?
**ए:** सूचियाँ परिवर्तनशील हैं (`[]`), टुपल्स अपरिवर्तनीय हैं (`()`)। जब आपको तत्वों को जोड़ने, हटाने या बदलने की आवश्यकता हो तो सूचियों का उपयोग करें। विषम डेटा, शब्दकोश कुंजियों, फ़ंक्शन रिटर्न मानों के निश्चित संग्रह के लिए टुपल्स का उपयोग करें, या जब आप संकेत देना चाहते हैं कि "यह नहीं बदलना चाहिए।" टुपल्स थोड़े अधिक मेमोरी-कुशल होते हैं और इन्हें सेट/डिक्ट कुंजी के रूप में उपयोग किया जा सकता है; सूचियाँ नहीं हो सकतीं.
```python
# Tuple as dictionary key (lists would raise TypeError)
locations = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}

# Tuple unpacking for multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5])
```

### Q2: ग्लोबल इंटरप्रेटर लॉक (जीआईएल) मेरे कोड को कैसे प्रभावित करता है, और मुझे इसके बारे में क्या करना चाहिए?
**ए:** जीआईएल कई थ्रेड्स को एक साथ पायथन बाइटकोड निष्पादित करने से रोकता है, जिससे थ्रेडिंग सीपीयू-बाउंड कार्य के लिए अप्रभावी हो जाती है। I/O-बाउंड कार्यों (नेटवर्क अनुरोध, फ़ाइल I/O) के लिए,`threading`या`asyncio`ठीक काम करते हैं क्योंकि I/O के दौरान GIL जारी किया जाता है। सीपीयू-बाउंड कार्यों के लिए,`multiprocessing`(अलग-अलग प्रक्रियाएं, प्रत्येक की अपनी GIL के साथ) का उपयोग करें, या C एक्सटेंशन (NumPy, Cython, Numba) पर ऑफलोड करें जो आंतरिक रूप से GIL जारी करते हैं।
```python
import multiprocessing
import time

def cpu_heavy(n):
    return sum(i * i for i in range(n))

# Multiprocessing bypasses the GIL
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_heavy, [10_000_000] * 4)
```

### Q3: क्या मुझे हर जगह टाइप संकेत का उपयोग करना चाहिए? व्यावहारिक व्यापार-बंद क्या हैं?
**ए:** प्रकार के संकेत (`def greet(name: str) -> str:`) वैकल्पिक हैं और रनटाइम पर लागू नहीं होते हैं। वे आईडीई स्वत: पूर्णता में सुधार करते हैं, स्थैतिक विश्लेषण उपकरण (मायपी) और दस्तावेज़ इरादे के माध्यम से बग पकड़ते हैं। ट्रेड-ऑफ अतिरिक्त वाचालता है और उन्नत प्रकारों (`Union`, `Generic`, `Protocol`) के लिए सीखने की अवस्था है। सिफ़ारिश: ~500 से अधिक लाइनों वाले किसी भी प्रोजेक्ट में फ़ंक्शन हस्ताक्षर के लिए प्रकार संकेत का उपयोग करें; छोटी स्क्रिप्ट में इनका संयमित प्रयोग करें। क्रमिक प्रवर्तन के लिए सीआई में mypy सक्षम करें।
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

# Structural subtyping — no inheritance needed
def display(obj: Renderable) -> None:
    print(obj.render())
```

### Q4: पायथन में अपवादों को संभालने के लिए सर्वोत्तम अभ्यास क्या हैं?
**ए:** नंगे`except:`(जो`SystemExit`और`KeyboardInterrupt`को भी पकड़ता है) के बजाय विशिष्ट अपवाद पकड़ें। हैप्पी-पाथ लॉजिक को त्रुटि प्रबंधन से अलग करने के लिए`try/except/else/finally`का उपयोग करें। पुस्तकालयों के लिए कस्टम अपवाद पदानुक्रम को परिभाषित करें। प्रदर्शन-संवेदनशील कोड में नियंत्रण प्रवाह के लिए कभी भी अपवादों का उपयोग न करें - वे धीमे होते हैं। पूर्ण ट्रेसबैक कैप्चर करने के लिए`logging.exception()`के साथ अपवाद लॉग करें।
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

### Q5: जनरेटर मेमोरी को कैसे सहेजते हैं, और मुझे सूचियों पर उनका उपयोग कब करना चाहिए?
**ए:** जेनरेटर मेमोरी में पूरी सूची बनाने के बजाय आलस्यपूर्वक मान उत्पन्न करते हैं - एक समय में एक, मांग पर। बड़े डेटासेट (लाखों पंक्तियाँ, अनंत अनुक्रम, स्ट्रीमिंग डेटा) के लिए, जनरेटर आकार की परवाह किए बिना निरंतर मेमोरी का उपयोग करते हैं। जब आप एक बार पुनरावृति करते हैं तो जनरेटर का उपयोग करें और आपको अनुक्रमणिका या`len()`की आवश्यकता नहीं है। जब आपको रैंडम एक्सेस, एकाधिक पुनरावृत्तियों की आवश्यकता हो, या संग्रह छोटा हो तो सूचियों का उपयोग करें।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: रैंकिंग के साथ एक वर्ड फ़्रीक्वेंसी काउंटर बनाएं
**समस्या कथन:** एक बड़ी टेक्स्ट फ़ाइल को देखते हुए, प्रत्येक शब्द की आवृत्ति की गणना करें, उन्हें आवृत्ति (अवरोही) के आधार पर रैंक करें, और शीर्ष एन परिणाम लौटाएं। केस की असंवेदनशीलता, विराम चिह्न को संभालें और स्मृति में फिट होने के लिए बहुत बड़ी फ़ाइलों को कुशलतापूर्वक संसाधित करें।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) पाठ पढ़ें, (2) शब्दों में विभाजित करें, (3) केस को सामान्य करें, (4) स्ट्रिप विराम चिह्न, (5) घटनाओं की गिनती करें, (6) गिनती के आधार पर क्रमबद्ध करें, (7) शीर्ष एन लौटाएं। "मेमोरी में फिट होने के लिए बहुत बड़ा" बाधा का मतलब है कि हमें जनरेटर के साथ लाइन-दर-लाइन प्रक्रिया करनी चाहिए।
**चरण 2 - दृष्टिकोण को पहचानें:**
- मध्यवर्ती सूचियाँ बनाए बिना कुशल शब्द निष्कर्षण के लिए`re.finditer`का उपयोग करें।
- प्रति शब्द O(1) वृद्धि के लिए`collections.Counter`का उपयोग करें।
-`Counter.most_common(n)`का उपयोग करें जो आंतरिक रूप से एक ढेर का उपयोग करता है - पूर्ण सॉर्ट के लिए O(n log n) के बजाय O(k log n)।
- मेमोरी को स्थिर रखने के लिए जनरेटर के माध्यम से लाइन-दर-लाइन प्रोसेस करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- मेमोरी: केवल काउंटर डिक्ट मेमोरी में है (प्रति अद्वितीय शब्द एक प्रविष्टि), फ़ाइल सामग्री नहीं। अंग्रेजी पाठ के लिए, ~100K अद्वितीय शब्द ≈ कुछ एमबी।
- समय: सभी शब्दों को स्कैन करने के लिए O(W) + शीर्ष-एन निष्कर्षण के लिए O(U लॉग N), जहां W = कुल शब्द, U = अद्वितीय शब्द।
- किनारे के मामले: संकुचन में एपोस्ट्रोफ ("नहीं") रेगेक्स द्वारा संरक्षित हैं। यूनिकोड टेक्स्ट के लिए`re.UNICODE`ध्वज या एक अलग पैटर्न की आवश्यकता होगी।
### समस्या 2: थ्रेड-सुरक्षित एलआरयू कैश लागू करें
**समस्या कथन:** स्क्रैच से कम से कम हाल ही में उपयोग किए गए (एलआरयू) कैश का निर्माण करें जो थ्रेड-सुरक्षित है, ओ (1) प्राप्त करने और डालने के संचालन का समर्थन करता है, और क्षमता से अधिक होने पर स्वचालित रूप से कम से कम हाल ही में उपयोग किए गए आइटम को बाहर निकाल देता है।
**चरण 1 - समस्या को समझें:**
एक एलआरयू कैश की आवश्यकता है: (1) कुंजी द्वारा तेज़ लुकअप → हैश मैप, (2) रीसेंसी द्वारा तेज़ ऑर्डरिंग → दोगुनी लिंक की गई सूची, (3) थ्रेड सुरक्षा → लॉकिंग।`get(key)`पर: आइटम को सामने ले जाएं।`put(key, val)`पर: सामने डालें; यदि क्षमता से अधिक हो तो पीछे से हटा दें।
**चरण 2 - दृष्टिकोण को पहचानें:**
- पायथन का`dict`सम्मिलन क्रम (3.7+) बनाए रखता है, इसलिए हम एक आदेशित तानाशाही दृष्टिकोण का उपयोग कर सकते हैं: अंत तक जाने के लिए हटाएं और पुनः डालें।
- थ्रेड सुरक्षा के लिए, पारस्परिक बहिष्करण के लिए`threading.Lock`का उपयोग करें।
- वैकल्पिक:`collections.OrderedDict`का उपयोग करें जिसमें`move_to_end()`है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- समय जटिलता:`get`और`put`दोनों के लिए O(1) -`OrderedDict.move_to_end()`और`popitem()`O(1) हैं।
- थ्रेड सुरक्षा:`Lock`परमाणुता सुनिश्चित करता है। उच्च थ्रूपुट के लिए,`threading.RLock`या रीड-राइट लॉक पैटर्न पर विचार करें, लेकिन अधिकांश उपयोग के मामलों के लिए एक साधारण लॉक पर्याप्त है।
- प्रोडक्शन नोट: सिंगल-थ्रेडेड कोड के लिए,`functools.lru_cache`सरल है और बेहतर प्रदर्शन के लिए C में लागू किया गया है।
### समस्या 3: गणितीय अभिव्यक्ति का विश्लेषण और मूल्यांकन करें
**समस्या कथन:** एक पार्सर लिखें जो`"3 + 4 * 2 / (1 - 5)"`जैसी स्ट्रिंग लेता है और ऑपरेटर प्राथमिकता और कोष्ठक का सम्मान करते हुए इसका सही मूल्यांकन करता है।
**चरण 1 - समस्या को समझें:**
इसके लिए आवश्यक है: (1) इनपुट स्ट्रिंग को संख्याओं, ऑपरेटरों और कोष्ठकों में टोकनाइज़ करना, (2) सही प्राथमिकता के साथ पार्स करना (`+`और`+`और`-`से पहले`*`और`/`), (3) नेस्टेड कोष्ठकों को संभालना। बाएं से दाएं का अनुभवहीन मूल्यांकन गलत परिणाम देगा।
**चरण 2 - दृष्टिकोण को पहचानें:**
क्लासिक समाधान **शंटिंग-यार्ड एल्गोरिदम** (डिज्क्स्ट्रा) है जो इनफ़िक्स को पोस्टफ़िक्स (रिवर्स पोलिश नोटेशन) में परिवर्तित करता है, फिर पोस्टफ़िक्स का मूल्यांकन करता है। वैकल्पिक रूप से, एक पुनरावर्ती वंश पार्सर का उपयोग करें। विशेष रूप से पायथन के लिए, हम सुरक्षित मूल्यांकन के लिए`ast.literal_eval`का भी उपयोग कर सकते हैं - लेकिन आइए इसे ठीक से लागू करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- शुद्धता:`3 + 4 * 2 / (1 - 5)`→`3 + 8 / (-4)`→`3 + (-2)`→ `1.0`। सही।
- समय: टोकनाइजेशन के लिए ओ(एन), शंटिंग-यार्ड के लिए ओ(एन), मूल्यांकन के लिए ओ(एन) - कुल मिलाकर ओ(एन)।
- संभालने के लिए किनारे के मामले: नकारात्मक संख्याएं (यूनरी`-`से पहले`0`जोड़ें), शून्य से विभाजन (त्रुटि प्रबंधन जोड़ें), अमान्य इनपुट (टोकन मान्य करें)।
- पायथोनिक विकल्प:`eval()`के बिना सुरक्षित मूल्यांकन के लिए एक कस्टम नोड विज़िटर के साथ `ast.parse(expr, mode='eval')`।
### समस्या 4: रीयल-टाइम डेटा अपडेट के साथ एक सीएलआई डैशबोर्ड बनाएं
**समस्या कथन:** एक टर्मिनल-आधारित डैशबोर्ड बनाएं जो रंग-कोडित थ्रेशोल्ड और प्रतिक्रियाशील लेआउट के साथ वास्तविक समय में अपडेट होने वाले सिस्टम मेट्रिक्स (सीपीयू, मेमोरी, डिस्क) को प्रदर्शित करता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) आवधिक प्रणाली मीट्रिक संग्रह, (2) कर्सर नियंत्रण के साथ टर्मिनल रेंडरिंग, (3) थ्रेशोल्ड के आधार पर रंग आउटपुट, (4) छोड़ने के लिए गैर-अवरुद्ध कीबोर्ड इनपुट। यह एक रेंडरिंग लूप वाला निर्माता-उपभोक्ता पैटर्न है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- क्रॉस-प्लेटफ़ॉर्म सिस्टम मेट्रिक्स के लिए`psutil`का उपयोग करें।
- कर्सर स्थिति और रंगों के लिए एएनएसआई एस्केप कोड का उपयोग करें (या उच्च-स्तरीय एपीआई के लिए`rich`लाइब्रेरी)।
- अद्यतन अंतराल के लिए`time.sleep`का उपयोग करें।
- संरचना इस प्रकार है: डेटा संग्रह → फ़ॉर्मेटिंग → रेंडरिंग पाइपलाइन।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- मापने के लिए`cpu_percent(interval=0.5)`0.5 सेकंड के लिए ब्लॉक करता है - यह सही तरीका है (नॉन-ब्लॉकिंग मोड पहली कॉल पर 0% देता है)।
- एएनएसआई कोड आधुनिक विंडोज टर्मिनल और सभी यूनिक्स टर्मिनलों पर काम करते हैं। लीगेसी Windows cmd के लिए,`os.system('color')`जोड़ें या`colorama`का उपयोग करें।
- उत्पादन उन्नयन: झिलमिलाहट मुक्त रेंडरिंग, स्वचालित लेआउट और क्रॉस-प्लेटफॉर्म संगतता के लिए`rich`लाइब्रेरी (`rich.live`) का उपयोग करें।
- विस्तारशीलता: प्रत्येक मीट्रिक एक स्वतंत्र फ़ंक्शन है, जिससे GPU तापमान, प्रक्रिया गणना या नेटवर्क कनेक्शन जोड़ना आसान हो जाता है।
---

## सारांश
पायथन की पठनीयता, बहुमुखी प्रतिभा और पारिस्थितिकी तंत्र की गहराई का संयोजन इसे दुनिया में सबसे व्यापक रूप से उपयोग की जाने वाली प्रोग्रामिंग भाषा बनाता है। यह एआई/एमएल के लिए डिफ़ॉल्ट विकल्प है, वेब बैकएंड और ऑटोमेशन के लिए एक मजबूत विकल्प और एक उत्कृष्ट शिक्षण भाषा है। इसकी मुख्य कमजोरियाँ - निष्पादन गति और मोबाइल/एम्बेडेड समर्थन - अच्छी तरह से समझी जाती हैं और उन्होंने समाधान स्थापित किए हैं। अधिकांश परियोजनाओं के लिए, पायथन एक उचित प्रारंभिक बिंदु है।