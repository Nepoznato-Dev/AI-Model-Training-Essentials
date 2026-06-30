<!-- 
This file was automatically translated from English to Portuguese.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Codemg Idiomas

# # Python

Python is a high-level, emterpreted, dynamically typed, general-purpose programmemg idioma. It emphasises readability e uses significant emdentation as block delimiters.

# ## Sintaxe básico

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

# ## Functions e type hemts

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes e OOP

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

- Use `com open(path) as f:` para file I/O.
- Prefer f-stremgs (`f"hello {name}"`) over `%` or `.paramat()`.
- Use `dadosclasses.dadosclass` para dados-only classes.
- Use `pathlib.Path` emstead de `os.path` para file paths.

# ## Toolemg

- `pip emstall <package>` emstalls packages.
- `python -m venv .venv && source .venv/bem/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip emstall -r requirements.txt` restores o/am.
- `pyproject.toml` is o/a modern project-configuration steard.

---

# # JavaScript

JavaScript is o/a primary idioma de o/a web. It runs em browsers e on servers via Node.js. It is dynamically typed e prototype-based.

# ## Modern sintaxe (ES6+)

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

# ## Async programmemg

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

# ## Toolemg

- `npm emit -y` emitialises a project.
- `npm emstall <package>` adds a dependency.
- `npm run <script>` runs a script defemed em `package.json`.
- `node emdex.js` runs a script com Node.js.

---

# # TypeScript

TypeScript is a statically typed superset de JavaScript that compiles to plaem JavaScript. It adds type annotations, emterfaces, generics, e enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces e types

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

# ## Classes com access modifiers

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

# ## Toolemg

- `npm emstall -g typescript` emstalls o/a compiler.
- `tsc` compiles o/a project.
- `ts-node src/emdex.ts` runs TypeScript directly.

---

# # Rust

Rust is a sistemas programmemg idioma focused on seguroty, speed, e concurrency. It preventos memory-seguroty bugs at compile time through its ownership system.

# ## Ownership e borrowemg

Every value em Rust has exactly one owner. When o/a owner goes out de scope o/a value is dropped. Borrowemg allows referências comout transferremg ownership.

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

Mutable borrows (`&mut T`) require that no oo/ar borrows exist at o/a same time.

# ## Lifetimes

Lifetimes ensure referências do not outlive o/a dados o/ay poemt to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums e pattern matchemg

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

# ## Error helemg

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

The `?` operator propagates errors automatically emside functions that return `Result`.

# ## Toolemg (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles e runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` paramats code. `cargo clippy` lemts.

---

# # Go

Go (Golang) is a statically typed, compiled idioma designed para simplicity e high-perparamance concurrent programs.

# ## Básico

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions e multiple return values

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

Any type that implements all methods de an emterface satisfies it — no explicit declaration is needed.

# ## Goroutemes e channels

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

# ## Toolemg

- `go mod emit module/name` emitialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` paramats code.
- `go vet ./...` checks para common mistakes.

---

# # C e C++

C is a low-level, compiled, procedural idioma. C++ extends C com classes, templates, e o/a Steard Template Library (STL).

# ## C básico

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

# ## Poemters

A poemter stores o/a memory address de anoo/ar variable. `*ptr` dereferências it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes e RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensuremg cleanup happens automatically em destructors.

# ## STL contaemers

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
- Range-based `para` loops: `para (auto& item : contaemer)`.
- Smart poemters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bemdemgs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::stremg_view`.

# ## Compilation

- `gcc maem.c -o maem` compiles C.
- `g++ -std=c++20 -Wall maem.cpp -o maem` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is o/a steard build-system generator para larger projects.

---

# # Swift

Swift is a modern, statically typed programmemg idioma developed by Apple para iOS, macOS, watchOS, e tvOS. It is also available on Lemux.

# ## Básico

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

# ## Functions e closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes e structs

Swift has both classes (referência types) e structs (value types). Prefer structs para simple dados models.

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

# ## Codable (JSON encodemg / decodemg)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI básico

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

# ## Toolemg

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs o/a project.
- `swift test` runs tests.
- `swift package emit --type executable` creates a new executable project.
- Xcode is o/a primary IDE para Apple-platparam desenvolvimento.

---

# # Codemg Fundamentos (Idioma-Agnostic)

# ## Problem-solvemg workflow

1. Defeme o/a emput, output, e constraemts beparae writemg code.
2. Break o/a task emto smaller sub-problems.
3. Start com a simple correct solution, o/an optimise if needed.
4. Validate com tests, edge cases, e realistic emputs.

# ## Core dados structures

- **Array / List**: ordered collection com fast emdexed reads.
- **Hash map / Dicionário**: key-value store com average O(1) lookup.
- **Set**: unique values, useful para membership checks.
- **Stack**: LIFO (last em, first out), common em parsemg e recursion.
- **Queue**: FIFO (first em, first out), useful para schedulemg e BFS.
- **Tree / Graph**: hierarchical e rede-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows com emput size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): bemary search.
  - O(n): semgle pass through dados.
  - O(n log n): efficient sortemg.
  - O(n²): nested loops over similar-size emputs.
- Prefer clear, maemtaemable code unless prdeilemg shows a bottleneck.

# ## Debuggemg premciples

- Reproduce o/a bug reliably first.
- Memimise o/a failemg case to isolate cause.
- Inspect logs, emputs, e assumptions.
- Change one variable at a time while testemg.
- Add regression tests so o/a same bug does not return.

# ## Testemg pyramid

- **Unit tests**: fast, focused checks de small logic units.
- **Integration tests**: verify emteractions across modules/services.
- **End-to-end tests**: validate user flows em realistic environments.
- A balanced suite has many unit tests e fewer slow end-to-end tests.

# ## Code quality practices

- Use meanemgful names e small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive e emterfaces explicit.
- Use lemters/paramatters para consistency.
- Review code para correctness, clarity, e segurança.

# ## Segurança básico para developers

- Validate e sanitise external emput.
- Use parameterised queries to prevent SQL emjection.
- Store passwords com strong hashemg algorithms (e.g., Argon2, bcrypt).
- Avoid embeddemg secrets em source code.
- Apply least privilege para credentials e services.
