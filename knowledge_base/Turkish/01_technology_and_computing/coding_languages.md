<!-- 
This file was automatically translated from English to Turkish.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Codiçiçindedeg Dils

# # Python

Python is a high-level, içiçindedeterpreted, dynamically typed, general-purpose programmiçiçindedeg dil. It emphasises readability ve uses significant içiçindededentation as block delimiters.

# ## Sözdizimi temeller

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

# ## Functions ve type hiçiçindedets

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

# ## Classes ve OOP

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

- Use `ile open(path) as f:` için file I/O.
- Prefer f-striçiçindedegs (`f"hello {name}"`) over `%` or `.içinmat()`.
- Use `vericlasses.vericlass` için veri-only classes.
- Use `pathlib.Path` içiçindedestead içiçindede `os.path` için file paths.

# ## Tooliçiçindedeg

- `pip içiçindedestall <package>` içiçindedestalls packages.
- `python -m venv .venv && source .venv/biçiçindede/activate` creates a virtual environment.
- `pip freeze > requirements.txt` saves dependencies.
- `pip içiçindedestall -r requirements.txt` restores bum.
- `pyproject.toml` is bu modern project-configuration stveard.

---

# # JavaScript

JavaScript is bu primary dil içiçindede bu web. It runs içiçindede browsers ve on servers via Node.js. It is dynamically typed ve prototype-based.

# ## Modern sözdizimi (ES6+)

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

# ## Async programmiçiçindedeg

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

# ## Tooliçiçindedeg

- `npm içiçindedeit -y` içiçindedeitialises a project.
- `npm içiçindedestall <package>` adds a dependency.
- `npm run <script>` runs a script defiçiçindedeed içiçindede `package.json`.
- `node içiçindededex.js` runs a script ile Node.js.

---

# # TypeScript

TypeScript is a statically typed superset içiçindede JavaScript that compiles to plaiçiçindede JavaScript. It adds type annotations, içiçindedeterfaces, generics, ve enums.

# ## Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

# ## Interfaces ve types

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

# ## Classes ile access modifiers

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

# ## Tooliçiçindedeg

- `npm içiçindedestall -g typescript` içiçindedestalls bu compiler.
- `tsc` compiles bu project.
- `ts-node src/içiçindededex.ts` runs TypeScript directly.

---

# # Rust

Rust is a sistemler programmiçiçindedeg dil focused on güvenlity, speed, ve concurrency. It prolaylar memory-güvenlity bugs at compile time through its ownership system.

# ## Ownership ve borrowiçiçindedeg

Every value içiçindede Rust has exactly one owner. When bu owner goes out içiçindede scope bu value is dropped. Borrowiçiçindedeg allows referanss ileout transferriçiçindedeg ownership.

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

Mutable borrows (`&mut T`) require that no obur borrows exist at bu same time.

# ## Lifetimes

Lifetimes ensure referanss do not outlive bu veri buy poiçiçindedet to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

# ## Enums ve pattern matchiçiçindedeg

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

# ## Error hveliçiçindedeg

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

The `?` operator propagates errors automatically içiçindedeside functions that return `Result`.

# ## Tooliçiçindedeg (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles ve runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` içinmats code. `cargo clippy` liçiçindedets.

---

# # Go

Go (Golang) is a statically typed, compiled dil designed için simplicity ve high-periçinmance concurrent programs.

# ## Temeller

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

# ## Functions ve multiple return values

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

Any type that implements all methods içiçindede an içiçindedeterface satisfies it — no explicit declaration is needed.

# ## Goroutiçiçindedees ve channels

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

# ## Tooliçiçindedeg

- `go mod içiçindedeit module/name` içiçindedeitialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` içinmats code.
- `go vet ./...` checks için common mistakes.

---

# # C ve C++

C is a low-level, compiled, procedural dil. C++ extends C ile classes, templates, ve bu Stveard Template Library (STL).

# ## C temeller

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

# ## Poiçiçindedeters

A poiçiçindedeter stores bu memory address içiçindede anobur variable. `*ptr` dereferanss it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

# ## C++ classes ve RAII

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

RAII (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensuriçiçindedeg cleanup happens automatically içiçindede destructors.

# ## STL contaiçiçindedeers

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
- Range-based `için` loops: `için (auto& item : contaiçiçindedeer)`.
- Smart poiçiçindedeters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured biçiçindedediçiçindedegs: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::striçiçindedeg_view`.

# ## Compilation

- `gcc maiçiçindede.c -o maiçiçindede` compiles C.
- `g++ -std=c++20 -Wall maiçiçindede.cpp -o maiçiçindede` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is bu stveard build-system generator için larger projects.

---

# # Swift

Swift is a modern, statically typed programmiçiçindedeg dil developed by Apple için iOS, macOS, watchOS, ve tvOS. It is also available on Liçiçindedeux.

# ## Temeller

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

# ## Functions ve closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

# ## Classes ve structs

Swift has both classes (referans types) ve structs (value types). Prefer structs için simple veri models.

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

# ## Codable (JSON encodiçiçindedeg / decodiçiçindedeg)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI temeller

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

# ## Tooliçiçindedeg

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs bu project.
- `swift test` runs tests.
- `swift package içiçindedeit --type executable` creates a new executable project.
- Xcode is bu primary IDE için Apple-platiçinm geliştirme.

---

# # Codiçiçindedeg Temeller (Dil-Agnostic)

# ## Problem-solviçiçindedeg workflow

1. Defiçiçindedee bu içiçindedeput, output, ve constraiçiçindedets beiçine writiçiçindedeg code.
2. Break bu task içiçindedeto smaller sub-problems.
3. Start ile a simple correct solution, bun optimise if needed.
4. Validate ile tests, edge cases, ve realistic içiçindedeputs.

# ## Core veri structures

- **Array / List**: ordered collection ile fast içiçindededexed reads.
- **Hash map / Sözlük**: key-value store ile average O(1) lookup.
- **Set**: unique values, useful için membership checks.
- **Stack**: LIFO (last içiçindede, first out), common içiçindede parsiçiçindedeg ve recursion.
- **Queue**: FIFO (first içiçindede, first out), useful için scheduliçiçindedeg ve BFS.
- **Tree / Graph**: hierarchical ve ağ-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows ile içiçindedeput size.
- Typical costs:
  - O(1): constant-time lookup (e.g., hash map access).
  - O(log n): biçiçindedeary search.
  - O(n): siçiçindedegle pass through veri.
  - O(n log n): efficient sortiçiçindedeg.
  - O(n²): nested loops over similar-size içiçindedeputs.
- Prefer clear, maiçiçindedetaiçiçindedeable code unless priçiçindedeiliçiçindedeg shows a bottleneck.

# ## Debuggiçiçindedeg priçiçindedeciples

- Reproduce bu bug reliably first.
- Miçiçindedeimise bu failiçiçindedeg case to isolate cause.
- Inspect logs, içiçindedeputs, ve assumptions.
- Change one variable at a time while testiçiçindedeg.
- Add regression tests so bu same bug does not return.

# ## Testiçiçindedeg pyramid

- **Unit tests**: fast, focused checks içiçindede small logic units.
- **Integration tests**: verify içiçindedeteractions across modules/services.
- **End-to-end tests**: validate user flows içiçindede realistic environments.
- A balanced suite has many unit tests ve fewer slow end-to-end tests.

# ## Code quality practices

- Use meaniçiçindedegful names ve small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive ve içiçindedeterfaces explicit.
- Use liçiçindedeters/içinmatters için consistency.
- Review code için correctness, clarity, ve güvenlik.

# ## Güvenlik temeller için developers

- Validate ve sanitise external içiçindedeput.
- Use parameterised queries to prevent SQL içiçindedejection.
- Store passwords ile strong hashiçiçindedeg algorithms (e.g., Argon2, bcrypt).
- Avoid embeddiçiçindedeg secrets içiçindede source code.
- Apply least privilege için credentials ve services.
