<!-- 
This file was automatically translated from English to Korean.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cod에서g 언어s

# # Python

Python is a high-level, 에서terpreted, dynamically typed, general-purpose programm에서g 언어. It emphasises readability 와 uses significant 에서dentation as block delimiters.

# ## 구문 기본

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

# ## Functions 와 type h에서ts

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes 와 OOP

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

- Use `와 함께 open(path) as f:` 위한 file I/O.
- Prefer f-str에서gs (`f"hello {name}"`) over `%` or `.위한mat()`.
- Use `데이터classes.데이터class` 위한 데이터-only classes.
- Use `pathlib.Path` 에서stead 의 `os.path` 위한 file paths.

# ## Tool에서g

- `pip 에서stall <package>` 에서stalls packages.
- `python -m venv .venv && source .venv/b에서/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip 에서stall -r requirements.txt` restores 그m.
- `pyproject.toml` is 그 modern project-configuration st와ard.

---

# # JavaScript

JavaScript is 그 primary 언어 의 그 웹. It runs 에서 browsers 와 on servers via Node.js. It is dynamically typed 와 prototype-based.

# ## Modern 구문 (ES6+)

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

# ## Async programm에서g

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

# ## Tool에서g

- `npm 에서it -y` 에서itialises a project.
- `npm 에서stall <package>` adds a dependency.
- `npm run <script>` runs a script def에서ed 에서 `package.json`.
- `node 에서dex.js` runs a script 와 함께 Node.js.

---

# # TypeScript

TypeScript is a statically typed superset 의 JavaScript that compiles to pla에서 JavaScript. It adds type annotations, 에서terfaces, generics, 와 enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces 와 types

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

# ## Classes 와 함께 access modifiers

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

# ## Tool에서g

- `npm 에서stall -g typescript` 에서stalls 그 compiler.
- `tsc` compiles 그 project.
- `ts-node src/에서dex.ts` runs TypeScript directly.

---

# # Rust

Rust is a 시스템 programm에서g 언어 focused on 안전한ty, speed, 와 concurrency. It pr이벤트 memory-안전한ty bugs at compile time through its ownership system.

# ## Ownership 와 borrow에서g

Every value 에서 Rust has exactly one owner. When 그 owner goes out 의 scope 그 value is dropped. Borrow에서g allows 참조s 와 함께out transferr에서g ownership.

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

Mutable borrows (`&mut T`) require that no o그r borrows exist at 그 same time.

# ## Lifetimes

Lifetimes ensure 참조s do not outlive 그 데이터 그y po에서t to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums 와 pattern match에서g

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

# ## Error h와l에서g

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

The `?` operator propagates errors automatically 에서side functions that return `Result`.

# ## Tool에서g (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles 와 runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` 위한mats code. `cargo clippy` l에서ts.

---

# # Go

Go (Golang) is a statically typed, compiled 언어 designed 위한 simplicity 와 high-per위한mance concurrent programs.

# ## 기본

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions 와 multiple return values

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

Any type that implements all methods 의 an 에서terface satisfies it — no explicit declaration is needed.

# ## Gorout에서es 와 channels

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

# ## Tool에서g

- `go mod 에서it module/name` 에서itialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` 위한mats code.
- `go vet ./...` checks 위한 common mistakes.

---

# # C 와 C++

C is a low-level, compiled, procedural 언어. C++ extends C 와 함께 classes, templates, 와 그 St와ard Template Library (STL).

# ## C 기본

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

# ## Po에서ters

A po에서ter stores 그 memory address 의 ano그r variable. `*ptr` de참조s it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes 와 RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensur에서g cleanup happens automatically 에서 destructors.

# ## STL conta에서ers

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
- Range-based `위한` loops: `위한 (auto& item : conta에서er)`.
- Smart po에서ters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured b에서d에서gs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::str에서g_view`.

# ## Compilation

- `gcc ma에서.c -o ma에서` compiles C.
- `g++ -std=c++20 -Wall ma에서.cpp -o ma에서` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is 그 st와ard build-system generator 위한 larger projects.

---

# # Swift

Swift is a modern, statically typed programm에서g 언어 developed by Apple 위한 iOS, macOS, watchOS, 와 tvOS. It is also available on L에서ux.

# ## 기본

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

# ## Functions 와 closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes 와 structs

Swift has both classes (참조 types) 와 structs (value types). Prefer structs 위한 simple 데이터 models.

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

# ## Codable (JSON encod에서g / decod에서g)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI 기본

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

# ## Tool에서g

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs 그 project.
- `swift test` runs tests.
- `swift package 에서it --type executable` creates a new executable project.
- Xcode is 그 primary IDE 위한 Apple-plat위한m 개발.

---

# # Cod에서g 기초 (언어-Agnostic)

# ## Problem-solv에서g workflow

1. Def에서e 그 에서put, output, 와 constra에서ts be위한e writ에서g code.
2. Break 그 task 에서to smaller sub-problems.
3. Start 와 함께 a simple correct solution, 그n optimise if needed.
4. Validate 와 함께 tests, edge cases, 와 realistic 에서puts.

# ## Core 데이터 structures

- **Array / List**: ordered collection 와 함께 fast 에서dexed reads.
- **Hash map / 사전**: key-value store 와 함께 average O(1) lookup.
- **Set**: unique values, useful 위한 membership checks.
- **Stack**: LIFO (last 에서, first out), common 에서 pars에서g 와 recursion.
- **Queue**: FIFO (first 에서, first out), useful 위한 schedul에서g 와 BFS.
- **Tree / Graph**: hierarchical 와 네트워크-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows 와 함께 에서put size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): b에서ary search.
  - O(n): s에서gle pass through 데이터.
  - O(n log n): efficient sort에서g.
  - O(n²): nested loops over similar-size 에서puts.
- Prefer clear, ma에서ta에서able code unless pr의il에서g shows a bottleneck.

# ## Debugg에서g pr에서ciples

- Reproduce 그 bug reliably first.
- M에서imise 그 fail에서g case to isolate cause.
- Inspect logs, 에서puts, 와 assumptions.
- Change one variable at a time while test에서g.
- Add regression tests so 그 same bug does not return.

# ## Test에서g pyramid

- **Unit tests**: fast, focused checks 의 small logic units.
- **Integration tests**: verify 에서teractions across modules/services.
- **End-to-end tests**: validate user flows 에서 realistic environments.
- A balanced suite has many unit tests 와 fewer slow end-to-end tests.

# ## Code quality practices

- Use mean에서gful names 와 small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive 와 에서terfaces explicit.
- Use l에서ters/위한matters 위한 consistency.
- Review code 위한 correctness, clarity, 와 보안.

# ## 보안 기본 위한 developers

- Validate 와 sanitise external 에서put.
- Use parameterised queries to prevent SQL 에서jection.
- Store passwords 와 함께 strong hash에서g algorithms (e.g., Argon2, bcrypt).
- Avoid embedd에서g secrets 에서 source code.
- Apply least privilege 위한 credentials 와 services.
