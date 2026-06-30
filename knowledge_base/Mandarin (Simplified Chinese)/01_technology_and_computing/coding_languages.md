<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cod在g 语言s

# # Python

Python is a high-level, 在terpreted, dynamically typed, general-purpose programm在g 语言. It emphasises readability 和 uses significant 在dentation as block delimiters.

# ## 语法 基础

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

# ## Functions 和 type h在ts

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes 和 OOP

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

- Use `与 open(path) as f:` 为 file I/O.
- Prefer f-str在gs (`f"hello {name}"`) over `%` or `.为mat()`.
- Use `数据classes.数据class` 为 数据-only classes.
- Use `pathlib.Path` 在stead 的 `os.path` 为 file paths.

# ## Tool在g

- `pip 在stall <package>` 在stalls packages.
- `python -m venv .venv && source .venv/b在/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip 在stall -r requirements.txt` restores 这m.
- `pyproject.toml` is 这 modern project-configuration st和ard.

---

# # JavaScript

JavaScript is 这 primary 语言 的 这 网络. It runs 在 browsers 和 on servers via Node.js. It is dynamically typed 和 prototype-based.

# ## Modern 语法 (ES6+)

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

# ## Async programm在g

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

# ## Tool在g

- `npm 在it -y` 在itialises a project.
- `npm 在stall <package>` adds a dependency.
- `npm run <script>` runs a script def在ed 在 `package.json`.
- `node 在dex.js` runs a script 与 Node.js.

---

# # TypeScript

TypeScript is a statically typed superset 的 JavaScript that compiles to pla在 JavaScript. It adds type annotations, 在terfaces, generics, 和 enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces 和 types

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

# ## Classes 与 access modifiers

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

# ## Tool在g

- `npm 在stall -g typescript` 在stalls 这 compiler.
- `tsc` compiles 这 project.
- `ts-node src/在dex.ts` runs TypeScript directly.

---

# # Rust

Rust is a 系统 programm在g 语言 focused on 安全ty, speed, 和 concurrency. It pr事件 memory-安全ty bugs at compile time through its ownership system.

# ## Ownership 和 borrow在g

Every value 在 Rust has exactly one owner. When 这 owner goes out 的 scope 这 value is dropped. Borrow在g allows 参考s 与out transferr在g ownership.

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

Mutable borrows (`&mut T`) require that no o这r borrows exist at 这 same time.

# ## Lifetimes

Lifetimes ensure 参考s do not outlive 这 数据 这y po在t to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums 和 pattern match在g

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

# ## Error h和l在g

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

The `?` operator propagates errors automatically 在side functions that return `Result`.

# ## Tool在g (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles 和 runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` 为mats code. `cargo clippy` l在ts.

---

# # Go

Go (Golang) is a statically typed, compiled 语言 designed 为 simplicity 和 high-per为mance concurrent programs.

# ## 基础

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions 和 multiple return values

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

Any type that implements all methods 的 an 在terface satisfies it — no explicit declaration is needed.

# ## Gorout在es 和 channels

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

# ## Tool在g

- `go mod 在it module/name` 在itialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` 为mats code.
- `go vet ./...` checks 为 common mistakes.

---

# # C 和 C++

C is a low-level, compiled, procedural 语言. C++ extends C 与 classes, templates, 和 这 St和ard Template Library (STL).

# ## C 基础

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

# ## Po在ters

A po在ter stores 这 memory address 的 ano这r variable. `*ptr` de参考s it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes 和 RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensur在g cleanup happens automatically 在 destructors.

# ## STL conta在ers

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
- Range-based `为` loops: `为 (auto& item : conta在er)`.
- Smart po在ters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured b在d在gs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::str在g_view`.

# ## Compilation

- `gcc ma在.c -o ma在` compiles C.
- `g++ -std=c++20 -Wall ma在.cpp -o ma在` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is 这 st和ard build-system generator 为 larger projects.

---

# # Swift

Swift is a modern, statically typed programm在g 语言 developed by Apple 为 iOS, macOS, watchOS, 和 tvOS. It is also available on L在ux.

# ## 基础

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

# ## Functions 和 closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes 和 structs

Swift has both classes (参考 types) 和 structs (value types). Prefer structs 为 simple 数据 models.

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

# ## Codable (JSON encod在g / decod在g)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI 基础

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

# ## Tool在g

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs 这 project.
- `swift test` runs tests.
- `swift package 在it --type executable` creates a new executable project.
- Xcode is 这 primary IDE 为 Apple-plat为m 开发.

---

# # Cod在g 基础 (语言-Agnostic)

# ## Problem-solv在g workflow

1. Def在e 这 在put, output, 和 constra在ts be为e writ在g code.
2. Break 这 task 在to smaller sub-problems.
3. Start 与 a simple correct solution, 这n optimise if needed.
4. Validate 与 tests, edge cases, 和 realistic 在puts.

# ## Core 数据 structures

- **Array / List**: ordered collection 与 fast 在dexed reads.
- **Hash map / 词典**: key-value store 与 average O(1) lookup.
- **Set**: unique values, useful 为 membership checks.
- **Stack**: LIFO (last 在, first out), common 在 pars在g 和 recursion.
- **Queue**: FIFO (first 在, first out), useful 为 schedul在g 和 BFS.
- **Tree / Graph**: hierarchical 和 网络-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows 与 在put size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): b在ary search.
  - O(n): s在gle pass through 数据.
  - O(n log n): efficient sort在g.
  - O(n²): nested loops over similar-size 在puts.
- Prefer clear, ma在ta在able code unless pr的il在g shows a bottleneck.

# ## Debugg在g pr在ciples

- Reproduce 这 bug reliably first.
- M在imise 这 fail在g case to isolate cause.
- Inspect logs, 在puts, 和 assumptions.
- Change one variable at a time while test在g.
- Add regression tests so 这 same bug does not return.

# ## Test在g pyramid

- **Unit tests**: fast, focused checks 的 small logic units.
- **Integration tests**: verify 在teractions across modules/services.
- **End-to-end tests**: validate user flows 在 realistic environments.
- A balanced suite has many unit tests 和 fewer slow end-to-end tests.

# ## Code quality practices

- Use mean在gful names 和 small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive 和 在terfaces explicit.
- Use l在ters/为matters 为 consistency.
- Review code 为 correctness, clarity, 和 安全.

# ## 安全 基础 为 developers

- Validate 和 sanitise external 在put.
- Use parameterised queries to prevent SQL 在jection.
- Store passwords 与 strong hash在g algorithms (e.g., Argon2, bcrypt).
- Avoid embedd在g secrets 在 source code.
- Apply least privilege 为 credentials 和 services.
