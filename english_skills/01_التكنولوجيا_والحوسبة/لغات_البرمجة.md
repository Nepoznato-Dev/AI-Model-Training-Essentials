<!-- 
This file was automatically translated from English to Arabic.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Codفيg اللغةs

# # Python

Python is a high-level, فيterpreted, dynamically typed, general-purpose programmفيg اللغة. It emphasises readability و uses significant فيdentation as block delimiters.

# ## بناء الجملة الأساسيات

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

# ## Functions و type hفيts

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes و OOP

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

- Use `مع open(path) as f:` لأجل file I/O.
- Prefer f-strفيgs (`f"hello {name}"`) over `%` or `.لأجلmat()`.
- Use `البياناتclasses.البياناتclass` لأجل البيانات-only classes.
- Use `pathlib.Path` فيstead من `os.path` لأجل file paths.

# ## Toolفيg

- `pip فيstall <package>` فيstalls packages.
- `python -m venv .venv && source .venv/bفي/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip فيstall -r requirements.txt` restores الm.
- `pyproject.toml` is ال modern project-configuration stوard.

---

# # JavaScript

JavaScript is ال primary اللغة من ال الويب. It runs في browsers و on servers via Node.js. It is dynamically typed و prototype-based.

# ## Modern بناء الجملة (ES6+)

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

# ## Async programmفيg

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

# ## Toolفيg

- `npm فيit -y` فيitialises a project.
- `npm فيstall <package>` adds a dependency.
- `npm run <script>` runs a script defفيed في `package.json`.
- `node فيdex.js` runs a script مع Node.js.

---

# # TypeScript

TypeScript is a statically typed superset من JavaScript that compiles to plaفي JavaScript. It adds type annotations, فيterfaces, generics, و enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces و types

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

# ## Classes مع access modifiers

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

# ## Toolفيg

- `npm فيstall -g typescript` فيstalls ال compiler.
- `tsc` compiles ال project.
- `ts-node src/فيdex.ts` runs TypeScript directly.

---

# # Rust

Rust is a الأنظمة programmفيg اللغة focused on آمنty, speed, و concurrency. It prالأحداث memory-آمنty bugs at compile time through its ownership system.

# ## Ownership و borrowفيg

Every value في Rust has exactly one owner. When ال owner goes out من scope ال value is dropped. Borrowفيg allows مرجعs معout transferrفيg ownership.

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

Mutable borrows (`&mut T`) require that no oالr borrows exist at ال same time.

# ## Lifetimes

Lifetimes ensure مرجعs do not outlive ال البيانات الy poفيt to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums و pattern matchفيg

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

# ## Error hوlفيg

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

The `?` operator propagates errors automatically فيside functions that return `Result`.

# ## Toolفيg (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles و runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` لأجلmats code. `cargo clippy` lفيts.

---

# # Go

Go (Golang) is a statically typed, compiled اللغة designed لأجل simplicity و high-perلأجلmance concurrent programs.

# ## الأساسيات

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions و multiple return values

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

Any type that implements all methods من an فيterface satisfies it — no explicit declaration is needed.

# ## Goroutفيes و channels

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

# ## Toolفيg

- `go mod فيit module/name` فيitialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` لأجلmats code.
- `go vet ./...` checks لأجل common mistakes.

---

# # C و C++

C is a low-level, compiled, procedural اللغة. C++ extends C مع classes, templates, و ال Stوard Template Library (STL).

# ## C الأساسيات

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

# ## Poفيters

A poفيter stores ال memory address من anoالr variable. `*ptr` deمرجعs it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes و RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensurفيg cleanup happens automatically في destructors.

# ## STL contaفيers

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
- Range-based `لأجل` loops: `لأجل (auto& item : contaفيer)`.
- Smart poفيters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bفيdفيgs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::strفيg_view`.

# ## Compilation

- `gcc maفي.c -o maفي` compiles C.
- `g++ -std=c++20 -Wall maفي.cpp -o maفي` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is ال stوard build-system generator لأجل larger projects.

---

# # Swift

Swift is a modern, statically typed programmفيg اللغة developed by Apple لأجل iOS, macOS, watchOS, و tvOS. It is also available on Lفيux.

# ## الأساسيات

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

# ## Functions و closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes و structs

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

# ## Codable (JSON encodفيg / decodفيg)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI الأساسيات

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

# ## Toolفيg

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs ال project.
- `swift test` runs tests.
- `swift package فيit --type executable` creates a new executable project.
- Xcode is ال primary IDE لأجل Apple-platلأجلm التطوير.

---

# # Codفيg الأساسيات (اللغة-Agnostic)

# ## Problem-solvفيg workflow

1. Defفيe ال فيput, output, و constraفيts beلأجلe writفيg code.
2. Break ال task فيto smaller sub-problems.
3. Start مع a simple correct solution, الn optimise if needed.
4. Validate مع tests, edge cases, و realistic فيputs.

# ## Core البيانات structures

- **Array / List**: ordered collection مع fast فيdexed reads.
- **Hash map / القاموس**: key-value store مع average O(1) lookup.
- **Set**: unique values, useful لأجل membership checks.
- **Stack**: LIFO (last في, first out), common في parsفيg و recursion.
- **Queue**: FIFO (first في, first out), useful لأجل schedulفيg و BFS.
- **Tree / Graph**: hierarchical و الشبكة-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows مع فيput size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): bفيary search.
  - O(n): sفيgle pass through البيانات.
  - O(n log n): efficient sortفيg.
  - O(n²): nested loops over similar-size فيputs.
- Prefer clear, maفيtaفيable code unless prمنilفيg shows a bottleneck.

# ## Debuggفيg prفيciples

- Reproduce ال bug reliably first.
- Mفيimise ال failفيg case to isolate cause.
- Inspect logs, فيputs, و assumptions.
- Change one variable at a time while testفيg.
- Add regression tests so ال same bug does not return.

# ## Testفيg pyramid

- **Unit tests**: fast, focused checks من small logic units.
- **Integration tests**: verify فيteractions across modules/services.
- **End-to-end tests**: validate user flows في realistic environments.
- A balanced suite has many unit tests و fewer slow end-to-end tests.

# ## Code quality practices

- Use meanفيgful names و small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive و فيterfaces explicit.
- Use lفيters/لأجلmatters لأجل consistency.
- Review code لأجل correctness, clarity, و الأمان.

# ## الأمان الأساسيات لأجل developers

- Validate و sanitise external فيput.
- Use parameterised queries to prevent SQL فيjection.
- Store passwords مع strong hashفيg algorithms (e.g., Argon2, bcrypt).
- Avoid embeddفيg secrets في source code.
- Apply least privilege لأجل credentials و services.
