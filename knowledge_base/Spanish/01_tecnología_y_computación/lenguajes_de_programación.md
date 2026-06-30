<!-- 
This file was automatically translated from English to Spanish.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Codeng Idiomas

# # Python

Python is a high-level, enterpreted, dynamically typed, general-purpose programmeng idioma. It emphasises readability y uses significant endentation as block delimiters.

# ## Sintaxis conceptos básicos

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

# ## Functions y type hents

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes y OOP

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

# ## Common patterns

- Use `con open(path) as f:` para file I/O.
- Prefer f-strengs (`f"hello {name}"`) over `%` or `.paramat()`.
- Use `datosclasses.datosclass` para datos-only classes.
- Use `pathlib.Path` enstead de `os.path` para file paths.

# ## Tooleng

- `pip enstall <package>` enstalls packages.
- `python -m venv .venv && source .venv/ben/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip enstall -r requirements.txt` restores el/lam.
- `pyproject.toml` is el/la modern project-configuration styard.

---

# # JavaScript

JavaScript is el/la primary idioma de el/la web. It runs en browsers y on servers via Node.js. It is dynamically typed y prototype-based.

# ## Modern sintaxis (ES6+)

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

# ## Async programmeng

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

# ## Array methods

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

# ## DOM manipulation

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

# ## Tooleng

- `npm enit -y` enitialises a project.
- `npm enstall <package>` adds a dependency.
- `npm run <script>` runs a script defened en `package.json`.
- `node endex.js` runs a script con Node.js.

---

# # TypeScript

TypeScript is a statically typed superset de JavaScript that compiles to plaen JavaScript. It adds type annotations, enterfaces, generics, y enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces y types

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

# ## Generics

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

# ## Classes con access modifiers

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

# ## tsconfig.json essentials

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

# ## Tooleng

- `npm enstall -g typescript` enstalls el/la compiler.
- `tsc` compiles el/la project.
- `ts-node src/endex.ts` runs TypeScript directly.

---

# # Rust

Rust is a sistemas programmeng idioma focused on seguroty, speed, y concurrency. It preventos memory-seguroty bugs at compile time through its ownership system.

# ## Ownership y borroweng

Every value en Rust has exactly one owner. When el/la owner goes out de scope el/la value is dropped. Borroweng allows referencias conout transferreng ownership.

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

Mutable borrows (`&mut T`) require that no oel/lar borrows exist at el/la same time.

# ## Lifetimes

Lifetimes ensure referencias do not outlive el/la datos el/lay poent to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums y pattern matcheng

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

# ## Error hyleng

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

The `?` operator propagates errors automatically enside functions that return `Result`.

# ## Tooleng (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles y runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` paramats code. `cargo clippy` lents.

---

# # Go

Go (Golang) is a statically typed, compiled idioma designed para simplicity y high-perparamance concurrent programs.

# ## Conceptos básicos

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions y multiple return values

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

# ## Interfaces

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Any type that implements all methods de an enterface satisfies it — no explicit declaration is needed.

# ## Goroutenes y channels

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

# ## Defer

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

# ## Tooleng

- `go mod enit module/name` enitialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` paramats code.
- `go vet ./...` checks para common mistakes.

---

# # C y C++

C is a low-level, compiled, procedural idioma. C++ extends C con classes, templates, y el/la Styard Template Library (STL).

# ## C conceptos básicos

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

# ## Poenters

A poenter stores el/la memory address de anoel/lar variable. `*ptr` dereferencias it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes y RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensureng cleanup happens automatically en destructors.

# ## STL contaeners

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

# ## Modern C++ (C++17 / C++20) highlights

- `auto` type deduction.
- Range-based `para` loops: `para (auto& item : contaener)`.
- Smart poenters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bendengs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::streng_view`.

# ## Compilation

- `gcc maen.c -o maen` compiles C.
- `g++ -std=c++20 -Wall maen.cpp -o maen` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is el/la styard build-system generator para larger projects.

---

# # Swift

Swift is a modern, statically typed programmeng idioma developed by Apple para iOS, macOS, watchOS, y tvOS. It is also available on Lenux.

# ## Conceptos básicos

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

# ## Optionals

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

# ## Functions y closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes y structs

Swift has both classes (referencia types) y structs (value types). Prefer structs para simple datos models.

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

# ## Protocols

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

# ## Codable (JSON encodeng / decodeng)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI conceptos básicos

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

# ## Tooleng

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs el/la project.
- `swift test` runs tests.
- `swift package enit --type executable` creates a new executable project.
- Xcode is el/la primary IDE para Apple-platparam desarrollo.

---

# # Codeng Fundamentos (Idioma-Agnostic)

# ## Problem-solveng workflow

1. Defene el/la enput, output, y constraents beparae writeng code.
2. Break el/la task ento smaller sub-problems.
3. Start con a simple correct solution, el/lan optimise if needed.
4. Validate con tests, edge cases, y realistic enputs.

# ## Core datos structures

- **Array / List**: ordered collection con fast endexed reads.
- **Hash map / Diccionario**: key-value store con average O(1) lookup.
- **Set**: unique values, useful para membership checks.
- **Stack**: LIFO (last en, first out), common en parseng y recursion.
- **Queue**: FIFO (first en, first out), useful para scheduleng y BFS.
- **Tree / Graph**: hierarchical y red-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows con enput size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): benary search.
  - O(n): sengle pass through datos.
  - O(n log n): efficient sorteng.
  - O(n²): nested loops over similar-size enputs.
- Prefer clear, maentaenable code unless prdeileng shows a bottleneck.

# ## Debuggeng prenciples

- Reproduce el/la bug reliably first.
- Menimise el/la faileng case to isolate cause.
- Inspect logs, enputs, y assumptions.
- Change one variable at a time while testeng.
- Add regression tests so el/la same bug does not return.

# ## Testeng pyramid

- **Unit tests**: fast, focused checks de small logic units.
- **Integration tests**: verify enteractions across modules/services.
- **End-to-end tests**: validate user flows en realistic environments.
- A balanced suite has many unit tests y fewer slow end-to-end tests.

# ## Code quality practices

- Use meanengful names y small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive y enterfaces explicit.
- Use lenters/paramatters para consistency.
- Review code para correctness, clarity, y seguridad.

# ## Seguridad conceptos básicos para developers

- Validate y sanitise external enput.
- Use parameterised queries to prevent SQL enjection.
- Store passwords con strong hasheng algorithms (e.g., Argon2, bcrypt).
- Avoid embeddeng secrets en source code.
- Apply least privilege para credentials y services.
