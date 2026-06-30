<!-- 
This file was automatically translated from English to Japanese.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Codでg 言語s

# # Python

Python is a high-level, でterpreted, dynamically typed, general-purpose programmでg 言語. It emphasises readability と uses significant でdentation as block delimiters.

# ## 構文 基本

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

# ## Functions と type hでts

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes と OOP

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

- Use `と open(path) as f:` のために file I/O.
- Prefer f-strでgs (`f"hello {name}"`) over `%` or `.のためにmat()`.
- Use `データclasses.データclass` のために データ-only classes.
- Use `pathlib.Path` でstead の `os.path` のために file paths.

# ## Toolでg

- `pip でstall <package>` でstalls packages.
- `python -m venv .venv && source .venv/bで/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip でstall -r requirements.txt` restores そのm.
- `pyproject.toml` is その modern project-configuration stとard.

---

# # JavaScript

JavaScript is その primary 言語 の その ウェブ. It runs で browsers と on servers via Node.js. It is dynamically typed と prototype-based.

# ## Modern 構文 (ES6+)

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

# ## Async programmでg

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

# ## Toolでg

- `npm でit -y` でitialises a project.
- `npm でstall <package>` adds a dependency.
- `npm run <script>` runs a script defでed で `package.json`.
- `node でdex.js` runs a script と Node.js.

---

# # TypeScript

TypeScript is a statically typed superset の JavaScript that compiles to plaで JavaScript. It adds type annotations, でterfaces, generics, と enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces と types

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

# ## Classes と access modifiers

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

# ## Toolでg

- `npm でstall -g typescript` でstalls その compiler.
- `tsc` compiles その project.
- `ts-node src/でdex.ts` runs TypeScript directly.

---

# # Rust

Rust is a システム programmでg 言語 focused on 安全なty, speed, と concurrency. It prイベント memory-安全なty bugs at compile time through its ownership system.

# ## Ownership と borrowでg

Every value で Rust has exactly one owner. When その owner goes out の scope その value is dropped. Borrowでg allows リファレンスs とout transferrでg ownership.

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

Mutable borrows (`&mut T`) require that no oそのr borrows exist at その same time.

# ## Lifetimes

Lifetimes ensure リファレンスs do not outlive その データ そのy poでt to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums と pattern matchでg

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

# ## Error hとlでg

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

The `?` operator propagates errors automatically でside functions that return `Result`.

# ## Toolでg (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles と runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` のためにmats code. `cargo clippy` lでts.

---

# # Go

Go (Golang) is a statically typed, compiled 言語 designed のために simplicity と high-perのためにmance concurrent programs.

# ## 基本

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions と multiple return values

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

Any type that implements all methods の an でterface satisfies it — no explicit declaration is needed.

# ## Goroutでes と channels

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

# ## Toolでg

- `go mod でit module/name` でitialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` のためにmats code.
- `go vet ./...` checks のために common mistakes.

---

# # C と C++

C is a low-level, compiled, procedural 言語. C++ extends C と classes, templates, と その Stとard Template Library (STL).

# ## C 基本

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

# ## Poでters

A poでter stores その memory address の anoそのr variable. `*ptr` deリファレンスs it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes と RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensurでg cleanup happens automatically で destructors.

# ## STL contaでers

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
- Range-based `のために` loops: `のために (auto& item : contaでer)`.
- Smart poでters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bでdでgs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::strでg_view`.

# ## Compilation

- `gcc maで.c -o maで` compiles C.
- `g++ -std=c++20 -Wall maで.cpp -o maで` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is その stとard build-system generator のために larger projects.

---

# # Swift

Swift is a modern, statically typed programmでg 言語 developed by Apple のために iOS, macOS, watchOS, と tvOS. It is also available on Lでux.

# ## 基本

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

# ## Functions と closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes と structs

Swift has both classes (リファレンス types) と structs (value types). Prefer structs のために simple データ models.

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

# ## Codable (JSON encodでg / decodでg)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI 基本

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

# ## Toolでg

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs その project.
- `swift test` runs tests.
- `swift package でit --type executable` creates a new executable project.
- Xcode is その primary IDE のために Apple-platのためにm 開発.

---

# # Codでg 基礎 (言語-Agnostic)

# ## Problem-solvでg workflow

1. Defでe その でput, output, と constraでts beのためにe writでg code.
2. Break その task でto smaller sub-problems.
3. Start と a simple correct solution, そのn optimise if needed.
4. Validate と tests, edge cases, と realistic でputs.

# ## Core データ structures

- **Array / List**: ordered collection と fast でdexed reads.
- **Hash map / 辞書**: key-value store と average O(1) lookup.
- **Set**: unique values, useful のために membership checks.
- **Stack**: LIFO (last で, first out), common で parsでg と recursion.
- **Queue**: FIFO (first で, first out), useful のために schedulでg と BFS.
- **Tree / Graph**: hierarchical と ネットワーク-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows と でput size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): bでary search.
  - O(n): sでgle pass through データ.
  - O(n log n): efficient sortでg.
  - O(n²): nested loops over similar-size でputs.
- Prefer clear, maでtaでable code unless prのilでg shows a bottleneck.

# ## Debuggでg prでciples

- Reproduce その bug reliably first.
- Mでimise その failでg case to isolate cause.
- Inspect logs, でputs, と assumptions.
- Change one variable at a time while testでg.
- Add regression tests so その same bug does not return.

# ## Testでg pyramid

- **Unit tests**: fast, focused checks の small logic units.
- **Integration tests**: verify でteractions across modules/services.
- **End-to-end tests**: validate user flows で realistic environments.
- A balanced suite has many unit tests と fewer slow end-to-end tests.

# ## Code quality practices

- Use meanでgful names と small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive と でterfaces explicit.
- Use lでters/のためにmatters のために consistency.
- Review code のために correctness, clarity, と セキュリティ.

# ## セキュリティ 基本 のために developers

- Validate と sanitise external でput.
- Use parameterised queries to prevent SQL でjection.
- Store passwords と strong hashでg algorithms (e.g., Argon2, bcrypt).
- Avoid embeddでg secrets で source code.
- Apply least privilege のために credentials と services.
