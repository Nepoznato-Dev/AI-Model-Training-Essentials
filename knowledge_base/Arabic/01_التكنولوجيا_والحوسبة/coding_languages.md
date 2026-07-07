<!-- 
This file was automatically translated from English to Arabic.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Coding Languages

## Python

Python is a high-level, interpreted, dynamically typed, general-purpose programming اللغة. It emphasises readability و uses significant indentation as block delimiters.

### بناء الجملة الأساسيات

```python
# المتغيرات والأنواع
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# الشروط
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# الحلقات
for i in range(5):
    print(i)

while active:
    active = False
```

### الدوال و type hints

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### الفئات و OOP

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

### Common patterns

- Use `مع open(path) as f:` لأجل file I/O.
- Prefer f-strings (`f"hello {name}"`) over `%` or `.format()`.
- Use `dataclasses.dataclass` لأجل البيانات-only classes.
- Use `pathlib.Path` instead من `os.path` لأجل file paths.

### Tooling

- `pip install <package>` installs packages.
- `python -m venv .venv && source .venv/bin/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip install -r requirements.txt` restores them.
- `pyproject.toml` is ال modern project-configuration standard.

---

## JavaScript

JavaScript is ال primary اللغة من ال الويب. It runs في browsers و on servers via Node.js. It is dynamically typed و prototype-based.

### Modern بناء الجملة (ES6+)

```javascript
// Variable declarations
const PI = 3.14159;
let counter = 0;

// Arrow functions
const add = (a, b) => a + b;

// Template literals
const greet = name => `Hello, ${name}!`;

// Destructuring
const { x, y } = point;
const [first, ...rest] = array;

// Spread
const merged = { ...defaults, ...overrides };
```

### Async programming

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

### DOM manipulation

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Tooling

- `npm init -y` initialises a project.
- `npm install <package>` adds a dependency.
- `npm run <script>` runs a script defined في `package.json`.
- `node index.js` runs a script مع Node.js.

---

## TypeScript

TypeScript is a statically typed superset من JavaScript that compiles to plain JavaScript. It adds type annotations, interfaces, generics, و enums.

### Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces و types

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
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

### الفئات مع access modifiers

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

### tsconfig.json essentials

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

### Tooling

- `npm install -g typescript` installs ال compiler.
- `tsc` compiles ال project.
- `ts-node src/index.ts` runs TypeScript directly.

---

## Rust

Rust is a الأنظمة programming اللغة focused on safety, speed, و concurrency. It prevents memory-safety bugs at compile time through its ownership system.

### Ownership و borrowing

Every value في Rust has exactly one owner. When ال owner goes out من scope ال value is dropped. Borrowing allows references without transferring ownership.

```rust
fn main() {
    let s = String::from("hello");  // s owns the string
    let len = calculate_length(&s); // borrow s
    println!("{} has length {}", s, len); // s still valid
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Mutable borrows (`&mut T`) require that no other borrows exist at ال same time.

### Lifetimes

Lifetimes ensure references do not outlive ال البيانات they point to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums و pattern matching

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

### معالجة الأخطاء

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

ال `?` operator propagates errors automatically inside functions that return `Result`.

### Tooling (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles و runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` formats code. `cargo clippy` lints.

---

## Go

Go (Golang) is a statically typed, compiled اللغة designed لأجل simplicity و high-الأداء concurrent programs.

### الأساسيات

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### الدوال و multiple return values

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

Any type that implements all methods من an interface satisfies it — no explicit declaration is needed.

### Goroutines و channels

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
    defer f.Close()   // runs when function returns
    // … process f …
    return nil
}
```

### Tooling

- `go mod init module/name` initialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` formats code.
- `go vet ./...` checks لأجل common mistakes.

---

## C و C++

C is a low-level, compiled, procedural اللغة. C++ extends C مع classes, templates, و ال Standard Template Library (STL).

### C الأساسيات

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* Dynamic memory */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* always free what you malloc */

    return 0;
}
```

### Pointers

A pointer stores ال memory address من another variable. `*ptr` dereferences it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ classes و RAII

```cpp
#include <string>
#include <iostream>

class Person {
public:
    Person(std::string name, int age) : name_(name), age_(age) {}

    void greet() const {
        std::cout << "Hi, I'm " << name_ << "\n";
    }

private:
    std::string name_;
    int age_;
};
```

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensuring cleanup happens automatically في destructors.

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

### Modern C++ (C++17 / C++20) highlights

- `auto` type deduction.
- Range-based `لأجل` loops: `لأجل (auto& item : container)`.
- Smart pointers: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilation

- `gcc main.c -o main` compiles C.
- `g++ -std=c++20 -Wall main.cpp -o main` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is ال standard build-system generator لأجل larger projects.

---

## Swift

Swift is a modern, statically typed programming اللغة developed by Apple لأجل iOS, macOS, watchOS, و tvOS. It is also متاح on Linux.

### الأساسيات

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

An optional (`T?`) represents a value that may or may not be present.

```swift
var name: String? = nil
name = "Alice"

// Safe unwrapping
if let n = name {
    print("Hello, \(n)")
}

// Nil-coalescing
let display = name ?? "Guest"

// Optional chaining
let length = name?.count
```

### الدوال و closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### الفئات و structs

Swift has both classes (مرجع types) و structs (value types). Prefer structs لأجل simple البيانات models.

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

### SwiftUI الأساسيات

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

### Tooling

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs ال project.
- `swift test` runs tests.
- `swift package init --type executable` creates a new executable project.
- Xcode is ال primary IDE لأجل Apple-platform التطوير.

---

## Coding الأساسيات (اللغة-Agnostic)

### Problem-solving workflow

1. Define ال input, output, و constraints before writing code.
2. Break ال task into smaller sub-problems.
3. Start مع a simple correct solution, then optimise if needed.
4. Validate مع tests, edge cases, و realistic inputs.

### Core البيانات structures

- **Array / List**: ordered collection مع fast indexed reads.
- **Hash map / القاموس**: key-value store مع average O(1) lookup.
- **Set**: unique values, useful لأجل membership checks.
- **Stack**: LIFO (last في, first out), common في parsing و recursion.
- **Queue**: FIFO (first في, first out), useful لأجل scheduling و BFS.
- **Tree / Graph**: hierarchical و الشبكة-style relationships.

### Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows مع input size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): binary search.
  - O(n): single pass through البيانات.
  - O(n log n): efficient sorting.
  - O(n²): nested loops over similar-size inputs.
- Prefer clear, maintainable code unless profiling shows a bottleneck.

### Debugging principles

- Reproduce ال bug reliably first.
- Minimise ال failing case to isolate cause.
- Inspect logs, inputs, و assumptions.
- Change one variable at a time while الاختبار.
- Add regression tests so ال same bug does not return.

### الاختبار pyramid

- **Unit tests**: fast, focused checks من small logic units.
- **Integration tests**: verify interactions across modules/services.
- **End-to-end tests**: validate user flows في realistic environments.
- A balanced suite has many unit tests و fewer slow end-to-end tests.

### Code quality practices

- Use meaningful names و small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive و interfaces explicit.
- Use linters/formatters لأجل consistency.
- Review code لأجل correctness, clarity, و الأمان.

### الأمان الأساسيات لأجل developers

- Validate و sanitise external input.
- Use parameterised queries to prevent SQL injection.
- Store passwords مع strong hashing algorithms (e.g., Argon2, bcrypt).
- Avoid embedding secrets في source code.
- Apply least privilege لأجل credentials و services.
