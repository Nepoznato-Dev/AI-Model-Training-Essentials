<!-- 
This file was automatically translated from English to French.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Coddansg Langues

# # Python

Python is a high-level, dansterpreted, dynamically typed, general-purpose programmdansg langue. It emphasises readability et uses significant dansdentation as block delimiters.

# ## Syntaxe bases

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

# ## Functions et type hdansts

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes et OOP

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

- Use `avec open(path) as f:` pour file I/O.
- Prefer f-strdansgs (`f"hello {name}"`) over `%` or `.pourmat()`.
- Use `donnéesclasses.donnéesclass` pour données-only classes.
- Use `pathlib.Path` dansstead de `os.path` pour file paths.

# ## Tooldansg

- `pip dansstall <package>` dansstalls packages.
- `python -m venv .venv && source .venv/bdans/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip dansstall -r requirements.txt` restores le/lam.
- `pyproject.toml` is le/la modern project-configuration stetard.

---

# # JavaScript

JavaScript is le/la primary langue de le/la web. It runs dans browsers et on servers via Node.js. It is dynamically typed et prototype-based.

# ## Modern syntaxe (ES6+)

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

# ## Async programmdansg

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

# ## Tooldansg

- `npm dansit -y` dansitialises a project.
- `npm dansstall <package>` adds a dependency.
- `npm run <script>` runs a script defdansed dans `package.json`.
- `node dansdex.js` runs a script avec Node.js.

---

# # TypeScript

TypeScript is a statically typed superset de JavaScript that compiles to pladans JavaScript. It adds type annotations, dansterfaces, generics, et enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces et types

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

# ## Classes avec access modifiers

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

# ## Tooldansg

- `npm dansstall -g typescript` dansstalls le/la compiler.
- `tsc` compiles le/la project.
- `ts-node src/dansdex.ts` runs TypeScript directly.

---

# # Rust

Rust is a systèmes programmdansg langue focused on sûrty, speed, et concurrency. It prévénements memory-sûrty bugs at compile time through its ownership system.

# ## Ownership et borrowdansg

Every value dans Rust has exactly one owner. When le/la owner goes out de scope le/la value is dropped. Borrowdansg allows références avecout transferrdansg ownership.

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

Mutable borrows (`&mut T`) require that no ole/lar borrows exist at le/la same time.

# ## Lifetimes

Lifetimes ensure références do not outlive le/la données le/lay podanst to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums et pattern matchdansg

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

# ## Error hetldansg

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

The `?` operator propagates errors automatically dansside functions that return `Result`.

# ## Tooldansg (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles et runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` pourmats code. `cargo clippy` ldansts.

---

# # Go

Go (Golang) is a statically typed, compiled langue designed pour simplicity et high-perpourmance concurrent programs.

# ## Bases

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions et multiple return values

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

Any type that implements all methods de an dansterface satisfies it — no explicit declaration is needed.

# ## Goroutdanses et channels

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

# ## Tooldansg

- `go mod dansit module/name` dansitialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` pourmats code.
- `go vet ./...` checks pour common mistakes.

---

# # C et C++

C is a low-level, compiled, procedural langue. C++ extends C avec classes, templates, et le/la Stetard Template Library (STL).

# ## C bases

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

# ## Podansters

A podanster stores le/la memory address de anole/lar variable. `*ptr` deréférences it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes et RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensurdansg cleanup happens automatically dans destructors.

# ## STL contadansers

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
- Range-based `pour` loops: `pour (auto& item : contadanser)`.
- Smart podansters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bdansddansgs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::strdansg_view`.

# ## Compilation

- `gcc madans.c -o madans` compiles C.
- `g++ -std=c++20 -Wall madans.cpp -o madans` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is le/la stetard build-system generator pour larger projects.

---

# # Swift

Swift is a modern, statically typed programmdansg langue developed by Apple pour iOS, macOS, watchOS, et tvOS. It is also available on Ldansux.

# ## Bases

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

# ## Functions et closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes et structs

Swift has both classes (référence types) et structs (value types). Prefer structs pour simple données models.

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

# ## Codable (JSON encoddansg / decoddansg)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI bases

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

# ## Tooldansg

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs le/la project.
- `swift test` runs tests.
- `swift package dansit --type executable` creates a new executable project.
- Xcode is le/la primary IDE pour Apple-platpourm développement.

---

# # Coddansg Fondamentaux (Langue-Agnostic)

# ## Problem-solvdansg workflow

1. Defdanse le/la dansput, output, et constradansts bepoure writdansg code.
2. Break le/la task dansto smaller sub-problems.
3. Start avec a simple correct solution, le/lan optimise if needed.
4. Validate avec tests, edge cases, et realistic dansputs.

# ## Core données structures

- **Array / List**: ordered collection avec fast dansdexed reads.
- **Hash map / Dictionnaire**: key-value store avec average O(1) lookup.
- **Set**: unique values, useful pour membership checks.
- **Stack**: LIFO (last dans, first out), common dans parsdansg et recursion.
- **Queue**: FIFO (first dans, first out), useful pour scheduldansg et BFS.
- **Tree / Graph**: hierarchical et réseau-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows avec dansput size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): bdansary search.
  - O(n): sdansgle pass through données.
  - O(n log n): efficient sortdansg.
  - O(n²): nested loops over similar-size dansputs.
- Prefer clear, madanstadansable code unless prdeildansg shows a bottleneck.

# ## Debuggdansg prdansciples

- Reproduce le/la bug reliably first.
- Mdansimise le/la faildansg case to isolate cause.
- Inspect logs, dansputs, et assumptions.
- Change one variable at a time while testdansg.
- Add regression tests so le/la same bug does not return.

# ## Testdansg pyramid

- **Unit tests**: fast, focused checks de small logic units.
- **Integration tests**: verify dansteractions across modules/services.
- **End-to-end tests**: validate user flows dans realistic environments.
- A balanced suite has many unit tests et fewer slow end-to-end tests.

# ## Code quality practices

- Use meandansgful names et small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive et dansterfaces explicit.
- Use ldansters/pourmatters pour consistency.
- Review code pour correctness, clarity, et sécurité.

# ## Sécurité bases pour developers

- Validate et sanitise external dansput.
- Use parameterised queries to prevent SQL dansjection.
- Store passwords avec strong hashdansg algorithms (e.g., Argon2, bcrypt).
- Avoid embedddansg secrets dans source code.
- Apply least privilege pour credentials et services.
