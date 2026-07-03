<!-- 
This file was automatically translated from English to German.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Coding Languages

## Python

Python is a high-level, interpreted, dynamically typed, general-purpose programming Sprache. It emphasises readability und uses significant indentation as block delimiters.

### Syntax Grundlagen

```python
# Variables and types
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Conditionals
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Loops
for i in range(5):
    print(i)

while active:
    active = False
```

### Functions und type hints

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes und OOP

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

- Use `mit open(path) as f:` für file I/O.
- Prefer f-strings (`f"hello {name}"`) over `%` or `.format()`.
- Use `dataclasses.dataclass` für Daten-only classes.
- Use `pathlib.Path` instead von `os.path` für file paths.

### Tooling

- `pip install <package>` installs packages.
- `python -m venv .venv && source .venv/bin/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip install -r requirements.txt` restores them.
- `pyproject.toml` is der/die/das modern project-configuration standard.

---

## JavaScript

JavaScript is der/die/das primary Sprache von der/die/das Web. It runs in browsers und on servers via Node.js. It is dynamically typed und prototype-based.

### Modern Syntax (ES6+)

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
- `npm run <script>` runs a script defined in `package.json`.
- `node index.js` runs a script mit Node.js.

---

## TypeScript

TypeScript is a statically typed superset von JavaScript that compiles to plain JavaScript. It adds type annotations, interfaces, generics, und enums.

### Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces und types

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

### Classes mit access modifiers

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

- `npm install -g typescript` installs der/die/das compiler.
- `tsc` compiles der/die/das project.
- `ts-node src/index.ts` runs TypeScript directly.

---

## Rust

Rust is a Systeme programming Sprache focused on safety, speed, und concurrency. It prevents memory-safety bugs at compile time through its ownership system.

### Ownership und borrowing

Every value in Rust has exactly one owner. When der/die/das owner goes out von scope der/die/das value is dropped. Borrowing allows references without transferring ownership.

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

Mutable borrows (`&mut T`) require that no other borrows exist at der/die/das same time.

### Lifetimes

Lifetimes ensure references do not outlive der/die/das Daten they point to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums und pattern matching

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

der/die/das `?` operator propagates errors automatically inside functions that return `Result`.

### Tooling (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles und runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` formats code. `cargo clippy` lints.

---

## Go

Go (Golang) is a statically typed, compiled Sprache designed für simplicity und high-Leistung concurrent programs.

### Grundlagen

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Functions und multiple return values

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

Any type that implements all methods von an interface satisfies it — no explicit declaration is needed.

### Goroutines und channels

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
- `go vet ./...` checks für common mistakes.

---

## C und C++

C is a low-level, compiled, procedural Sprache. C++ extends C mit classes, templates, und der/die/das Standard Template Library (STL).

### C Grundlagen

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

A pointer stores der/die/das memory address von another variable. `*ptr` dereferences it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ classes und RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensuring cleanup happens automatically in destructors.

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
- Range-based `für` loops: `für (auto& item : container)`.
- Smart pointers: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilation

- `gcc main.c -o main` compiles C.
- `g++ -std=c++20 -Wall main.cpp -o main` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is der/die/das standard build-system generator für larger projects.

---

## Swift

Swift is a modern, statically typed programming Sprache developed by Apple für iOS, macOS, watchOS, und tvOS. It is also Verfügbar on Linux.

### Grundlagen

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

### Functions und closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classes und structs

Swift has both classes (Referenz types) und structs (value types). Prefer structs für simple Daten models.

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

### SwiftUI Grundlagen

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
- `swift run` runs der/die/das project.
- `swift test` runs tests.
- `swift package init --type executable` creates a new executable project.
- Xcode is der/die/das primary IDE für Apple-platform Entwicklung.

---

## Coding Grundlagen (Sprache-Agnostic)

### Problem-solving workflow

1. Define der/die/das input, output, und constraints before writing code.
2. Break der/die/das task into smaller sub-problems.
3. Start mit a simple correct solution, then optimise if needed.
4. Validate mit tests, edge cases, und realistic inputs.

### Core Daten structures

- **Array / List**: ordered collection mit fast indexed reads.
- **Hash map / Wörterbuch**: key-value store mit average O(1) lookup.
- **Set**: unique values, useful für membership checks.
- **Stack**: LIFO (last in, first out), common in parsing und recursion.
- **Queue**: FIFO (first in, first out), useful für scheduling und BFS.
- **Tree / Graph**: hierarchical und Netzwerk-style relationships.

### Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows mit input size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): binary search.
  - O(n): single pass through Daten.
  - O(n log n): efficient sorting.
  - O(n²): nested loops over similar-size inputs.
- Prefer clear, maintainable code unless profiling shows a bottleneck.

### Debugging principles

- Reproduce der/die/das bug reliably first.
- Minimise der/die/das failing case to isolate cause.
- Inspect logs, inputs, und assumptions.
- Change one variable at a time while Testen.
- Add regression tests so der/die/das same bug does not return.

### Testen pyramid

- **Unit tests**: fast, focused checks von small logic units.
- **Integration tests**: verify interactions across modules/services.
- **End-to-end tests**: validate user flows in realistic environments.
- A balanced suite has many unit tests und fewer slow end-to-end tests.

### Code quality practices

- Use meaningful names und small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive und interfaces explicit.
- Use linters/formatters für consistency.
- Review code für correctness, clarity, und Sicherheit.

### Sicherheit Grundlagen für developers

- Validate und sanitise external input.
- Use parameterised queries to prevent SQL injection.
- Store passwords mit strong hashing algorithms (e.g., Argon2, bcrypt).
- Avoid embedding secrets in source code.
- Apply least privilege für credentials und services.
