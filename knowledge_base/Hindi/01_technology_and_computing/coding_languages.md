# कोडिंग भाषाएँ

## Python

Python एक उच्च-स्तरीय, इंटरप्रेटेड, गतिशील प्रकारित, सामान्य-उद्देश्य प्रोग्रामिंग भाषा है। यह पठनीयता पर ज़ोर देती है और blocks की सीमाएँ निर्धारित करने के लिए महत्वपूर्ण indentation का उपयोग करती है।

### सिंटैक्स की मूल बातें

```python
# चर और प्रकार
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# शर्तें
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# लूप्स
for i in range(5):
    print(i)

while active:
    active = False
```

### फ़ंक्शन्स और प्रकार संकेत

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### सूची comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes और OOP

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"
```

### सामान्य पैटर्न

- फ़ाइल I/O के लिए `with open(path) as f:` का उपयोग करें।
- `%` या `.format()` की जगह f-strings (`f"hello {name}"`) को प्राथमिकता दें।
- केवल डेटा रखने वाली classes के लिए `dataclasses.dataclass` का उपयोग करें।
- फ़ाइल paths के लिए `os.path` की जगह `pathlib.Path` का उपयोग करें।

### उपकरण

- `pip install <package>` packages इंस्टॉल करता है।
- `python -m venv .venv && source .venv/bin/activate` एक virtual environment बनाता है।
- `pip freeze > requirements.txt` dependencies सहेजता है।
- `pip install -r requirements.txt` उन्हें पुनर्स्थापित करता है।
- `pyproject.toml` आधुनिक project-configuration मानक है।

---

## JavaScript

JavaScript वेब की प्रमुख भाषा है। यह ब्राउज़र्स में और servers पर Node.js के माध्यम से चलती है। यह गतिशील प्रकारित और prototype-based है।

### आधुनिक सिंटैक्स (ES6+)

```javascript
// चर घोषणाएँ
const PI = 3.14159;
let counter = 0;

// Arrow functions
const add = (a, b) => a + b;

// टेम्पलेट literals
const greet = name => `Hello, ${name}!`;

// संरचना-विभाजन
const { x, y } = point;
const [first, ...rest] = array;

// फैलाव
const merged = { ...defaults, ...overrides };
```

### Async प्रोग्रामिंग

```javascript
// Promises
fetch("/api/data")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// Async / await
async function loadUser(id) {
  try {
    const res = await fetch(`/users/${id}`);
    return await res.json();
  } catch (err) {
    console.error(err);
  }
}
```

### Array methods

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM में बदलाव

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### उपकरण

- `npm init -y` एक project आरंभ करता है।
- `npm install <package>` एक dependency जोड़ता है।
- `npm run <script>` `package.json` में परिभाषित script चलाता है।
- `node index.js` Node.js के साथ एक script चलाता है।

---

## TypeScript

TypeScript, JavaScript का एक statically typed superset है जो plain JavaScript में compile होता है। यह type annotations, interfaces, generics, और enums जोड़ता है।

### प्रकार annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces और types

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // वैकल्पिक प्रॉपर्टी
}

type Status = "active" | "inactive" | "banned";
```

### Generics

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Access modifiers वाली classes

```typescript
class Counter {
  private count: number = 0;

  increment(): void {
    this.count++;
  }

  get value(): number {
    return this.count;
  }
}
```

### `tsconfig.json` की आवश्यक बातें

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "strict": true,
    "outDir": "dist",
    "rootDir": "src"
  }
}
```

### उपकरण

- `npm install -g typescript` compiler इंस्टॉल करता है।
- `tsc` परियोजना को compile करता है।
- `ts-node src/index.ts` TypeScript को सीधे चलाता है।

---

## Rust

Rust एक systems programming language है जो safety, speed, और concurrency पर केंद्रित है। यह अपने ownership system के माध्यम से compile time पर memory-safety bugs को रोकती है।

### Ownership और borrowing

Rust में हर value का ठीक एक owner होता है। जब owner scope से बाहर जाता है, तो value drop हो जाती है। Borrowing, ownership transfer किए बिना references की अनुमति देता है।

```rust
fn main() {
    let s = String::from("hello");  // s string का owner है
    let len = calculate_length(&s); // s को borrow करें
    println!("{} has length {}", s, len); // s अभी भी valid है
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Mutable borrows (`&mut T`) के लिए यह आवश्यक है कि उसी समय कोई अन्य borrow मौजूद न हो।

### Lifetimes

Lifetimes यह सुनिश्चित करते हैं कि references उस data से अधिक समय तक जीवित न रहें, जिसकी ओर वे संकेत करते हैं।

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums और pattern matching

```rust
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

fn area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle(r)       => std::f64::consts::PI * r * r,
        Shape::Rectangle(w, h) => w * h,
    }
}
```

### Error handling

```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
    fs::read_to_string(path)
}

fn main() {
    match read_file("data.txt") {
        Ok(content) => println!("{}", content),
        Err(e)      => eprintln!("Error: {}", e),
    }
}
```

`?` operator उन functions के भीतर errors को अपने आप propagate करता है जो `Result` लौटाते हैं।

### उपकरण (Cargo)

- `cargo new project_name` एक नया project बनाता है।
- `cargo build` compile करता है।
- `cargo run` compile करके चलाता है।
- `cargo test` tests चलाता है।
- `cargo add <crate>` `Cargo.toml` में एक dependency जोड़ता है।
- `cargo fmt` code format करता है। `cargo clippy` linting करता है।

---

## Go

Go (Golang) एक statically typed, compiled language है, जिसे सरलता और high-performance concurrent programs के लिए डिज़ाइन किया गया है।

### मूल बातें

```go
package main

import "fmt"

func main() {
    name := "world"          // संक्षिप्त variable declaration
    fmt.Printf("Hello, %s!
", name)
}
```

### Functions और multiple return values

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Interfaces

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

कोई भी type जो interface की सभी methods लागू करता है, उसे संतुष्ट करता है — किसी explicit declaration की आवश्यकता नहीं होती।

### Goroutines और channels

```go
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * j
    }
}

func main() {
    jobs    := make(chan int, 5)
    results := make(chan int, 5)

    go worker(1, jobs, results)

    for i := 1; i <= 5; i++ {
        jobs <- i
    }
    close(jobs)

    for i := 0; i < 5; i++ {
        fmt.Println(<-results)
    }
}
```

### Defer

```go
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()   // function लौटने पर चलता है
    // … f को process करें …
    return nil
}
```

### उपकरण

- `go mod init module/name` एक module आरंभ करता है।
- `go get ./...` dependencies डाउनलोड करता है।
- `go build ./...` compile करता है।
- `go test ./...` tests चलाता है।
- `go fmt ./...` code format करता है।
- `go vet ./...` सामान्य गलतियों की जाँच करता है।

---

## C और C++

C एक low-level, compiled, procedural language है। C++, classes, templates, और Standard Template Library (STL) के साथ C का विस्तार करती है।

### C की मूल बातें

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d
", x);

    /* गतिशील memory */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* जो malloc किया है उसे हमेशा free करें */

    return 0;
}
```

### Pointers

Pointer किसी दूसरी variable का memory address संग्रहीत करता है। `*ptr` उसे dereference करता है; `&var` address लेता है।

```c
int a = 10;
int *p = &a;
*p = 20;   /* a अब 20 है */
```

### C++ classes और RAII

```cpp
#include <string>
#include <iostream>

class Person {
public:
    Person(std::string name, int age) : name_(name), age_(age) {}

    void greet() const {
        std::cout << "Hi, I'm " << name_ << "
";
    }

private:
    std::string name_;
    int age_;
};
```

RAII (Resource Acquisition Is Initialization) resource lifetimes को object lifetimes से जोड़ता है, जिससे destructors में cleanup अपने आप हो जाता है।

### STL containers

```cpp
#include <vector>
#include <map>
#include <algorithm>

std::vector<int> v = {3, 1, 4, 1, 5, 9};
std::sort(v.begin(), v.end());

std::map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"]   = 87;
```

### Modern C++ (C++17 / C++20) की मुख्य बातें

- `auto` type deduction.
- Range-based `for` loops: `for (auto& item : container)`.
- Smart pointers: `std::unique_ptr`, `std::shared_ptr` — raw `new`/`delete` से बचें।
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilation

- `gcc main.c -o main` C को compile करता है।
- `g++ -std=c++20 -Wall main.cpp -o main` C++ को compile करता है।
- `make` `Makefile` के माध्यम से multi-file builds को स्वचालित करता है।
- `cmake` बड़े projects के लिए मानक build-system generator है।

---

## Swift

Swift एक आधुनिक, statically typed प्रोग्रामिंग भाषा है जिसे Apple ने iOS, macOS, watchOS, और tvOS के लिए विकसित किया है। यह Linux पर भी उपलब्ध है।

### मूल बातें

```swift
let greeting = "Hello, world!"   // स्थिरांक (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Optional (`T?`) ऐसी value को दर्शाता है जो मौजूद हो भी सकती है और नहीं भी।

```swift
var name: String? = nil
name = "Alice"

// सुरक्षित unwrapping
if let n = name {
    print("Hello, \(n)")
}

// Nil-coalescing
let display = name ?? "Guest"

// Optional chaining
let length = name?.count
```

### Functions और closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classes और structs

Swift में classes (reference types) और structs (value types) दोनों होते हैं। सरल data models के लिए structs को प्राथमिकता दें।

```swift
struct Point {
    var x: Double
    var y: Double
}

class Vehicle {
    var speed: Double = 0.0
    func accelerate(by amount: Double) { speed += amount }
}
```

### Protocols

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable (JSON encoding / decoding)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### SwiftUI की मूल बातें

```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
        }
    }
}
```

### उपकरण

- `swift build` एक Swift Package Manager project को compile करता है।
- `swift run` project चलाता है।
- `swift test` tests चलाता है।
- `swift package init --type executable` एक नया executable project बनाता है।
- Apple-platform development के लिए Xcode प्रमुख IDE है।

---

## कोडिंग की बुनियाद (भाषा-स्वतंत्र)

### समस्या-समाधान workflow

1. Code लिखने से पहले input, output, और constraints को परिभाषित करें।
2. कार्य को छोटे उप-समस्याओं में विभाजित करें।
3. एक सरल और सही समाधान से शुरू करें, फिर आवश्यकता होने पर optimise करें।
4. Tests, edge cases, और realistic inputs के साथ validate करें।

### मुख्य data structures

- **Array / List**: क्रमबद्ध संग्रह, जिसमें indexed reads तेज़ होते हैं।
- **Hash map / Dictionary**: key-value store, जिसमें औसतन O(1) lookup मिलता है।
- **Set**: अद्वितीय values, membership checks के लिए उपयोगी।
- **Stack**: LIFO (last in, first out), parsing और recursion में सामान्य।
- **Queue**: FIFO (first in, first out), scheduling और BFS के लिए उपयोगी।
- **Tree / Graph**: पदानुक्रमित और network-style संबंध।

### Algorithmic complexity (Big O)

- Big O बताता है कि input size बढ़ने पर runtime या memory कैसे बढ़ती है।
- सामान्य लागतें:
  - O(1): constant-time lookup (जैसे, hash map access)।
  - O(log n): binary search.
  - O(n): data पर एक single pass.
  - O(n log n): efficient sorting.
  - O(n²): समान आकार के inputs पर nested loops.
- स्पष्ट और maintainable code को प्राथमिकता दें, जब तक profiling किसी bottleneck को न दिखाए।

### Debugging के सिद्धांत

- पहले bug को विश्वसनीय रूप से reproduce करें।
- कारण अलग करने के लिए failing case को न्यूनतम करें।
- Logs, inputs, और assumptions की जाँच करें।
- Test करते समय एक बार में एक ही variable बदलें।
- Regression tests जोड़ें ताकि वही bug दोबारा न आए।

### Testing pyramid

- **Unit tests**: छोटे logic units की तेज़, केंद्रित जाँच।
- **Integration tests**: modules/services के बीच interactions को verify करते हैं।
- **End-to-end tests**: यथार्थवादी environments में user flows को validate करते हैं।
- एक संतुलित suite में बहुत से unit tests और कम धीमे end-to-end tests होते हैं।

### Code quality practices

- अर्थपूर्ण नामों और छोटे, केंद्रित functions का उपयोग करें।
- जहाँ व्यावहारिक हो, pure functions (कम side effects) को प्राथमिकता दें।
- Modules को cohesive और interfaces को explicit रखें।
- Consistency के लिए linters/formatters का उपयोग करें।
- Code की correctness, clarity, और security के लिए review करें।

### Developers के लिए security basics

- बाहरी input को validate और sanitise करें।
- SQL injection रोकने के लिए parameterised queries का उपयोग करें।
- Passwords को मज़बूत hashing algorithms (जैसे, Argon2, bcrypt) के साथ store करें।
- Source code में secrets embed करने से बचें।
- Credentials और services के लिए least privilege लागू करें।
