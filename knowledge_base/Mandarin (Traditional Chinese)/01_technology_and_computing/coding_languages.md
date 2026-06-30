<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Cod 語言s

# # Python

Python is a high-level, terpreted, dynamically typed, general-purpose programm 語言. It emphasises readability 和 uses significant dentation as block delimiters.

# ## 語法 基礎

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

# ## Functions 和 type hts

```python
def greet(name: str, times: int = 1) -> str:
 return (f"Hello, {name}! " * times).strip()
```

# ## List comprehensions

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
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

- Use `與 open(path) as f:` 為 file I/O.
- Prefer f-strs (`f"hello {name}"`) over `%` or `.為mat()`.
- Use `資料classes.資料class` 為 資料-only classes.
- Use `pathlib.Path` stead 的 `os.path` 為 file paths.

# ## Tool

- `pip stall <package>` stalls packages.
- `python -m venv .venv && source .venv/b/activate` creates a virtual 環境.
- `pip freeze > requirements.txt` saves dependencies.
- `pip stall -r requirements.txt` restores 這m.
- `pyproject.toml` is 這 modern project-configuration st和ard.

---

# # JavaScript

JavaScript is 這 primary 語言 的 這 網路. It runs browsers 和 on servers via Node.js. It is dynamically typed 和 prototype-based.

# ## Modern 語法 (ES6+)

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

# ## Async programm

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
const evens = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

# ## DOM manipulation

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
 document.querySelector(".result").textContent = "Done!";
});
```

# ## Tool

- `npm it -y` itialises a project.
- `npm stall <package>` adds a dependency.
- `npm run <script>` runs a script defed `package.json`.
- `node dex.js` runs a script 與 Node.js.

---

# # TypeScript

TypeScript is a statically typed superset 的 JavaScript that compiles to pla JavaScript. It adds type annotations, terfaces, generics, 和 enums.

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
 email?: string; // optional property
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

# ## Classes 與 access modifiers

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

# ## Tool

- `npm stall -g typescript` stalls 這 compiler.
- `tsc` compiles 這 project.
- `ts-node src/dex.ts` runs TypeScript directly.

---

# # Rust

Rust is a 係統 programm 語言 focused on 安全ty, speed, 和 concurrency. It pr事件 memory-安全ty bugs at compile time through its ownership system.

# ## Ownership 和 borrow

Every value Rust has exactly one owner. When 這 owner goes out 的 scope 這 value is dropped. Borrow allows 參考s 與out transferr ownership.

```rust
fn main() {
 let s = String::from("hello"); // s owns the string
 let len = calculate_length(&s); // borrow s
 println!("{} has length {}", s, len); // s still valid
}

fn calculate_length(s: &String) -> usize {
 s.len()
}
```

Mutable borrows (`&mut T`) require that no o這r borrows exist at 這 same time.

# ## Lifetimes

Lifetimes ensure 參考s do not outlive 這 資料 這y pot to.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
 if x.len() > y.len() { x } else { y }
}
```

# ## Enums 和 pattern match

```rust
enum Shape {
 Circle(f64),
 Rectangle(f64, f64),
}

fn area(shape: &Shape) -> f64 {
 match shape {
 Shape::Circle(r) => std::f64::consts::PI * r * r,
 Shape::Rectangle(w, h) => w * h,
 }
}
```

# ## Error h和l

```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
 fs::read_to_string(path)
}

fn main() {
 match read_file("data.txt") {
 Ok(內容) => println!("{}", 內容),
 Err(e) => eprintln!("Error: {}", e),
 }
}
```

The `?` operator propagates errors automatically side functions that return `Result`.

# ## Tool (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles 和 runs.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` 為mats code. `cargo clippy` lts.

---

# # Go

Go (Golang) is a statically typed, compiled 語言 designed 為 simplicity 和 high-per為mance concurrent programs.

# ## 基礎

```go
package main

import "fmt"

func main() {
 name := "world" // short variable declaration
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

Any type that implements all methods 的 an terface satisfies it — no explicit declaration is needed.

# ## Gorout 和 channels

```go
func worker(id int, jobs <-chan int, results chan<- int) {
 for j := range jobs {
 results <- j * j
 }
}

func main() {
 jobs := make(chan int, 5)
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
 defer f.Close() // runs when function returns
 // … process f …
 return nil
}
```

# ## Tool

- `go mod it module/name` itialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` 為mats code.
- `go vet ./...` checks 為 common mistakes.

---

# # C 和 C++

C is a low-level, compiled, procedural 語言. C++ extends C 與 classes, templates, 和 這 St和ard Template Library (STL).

# ## C 基礎

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
 int x = 42;
 printf("x = %d\n", x);

 /* Dynamic memory */
 int *arr = malloc(5 * sizeof(int));
 for (int i = 0; i < 5; i++) arr[i] = i;
 free(arr); /* always free what you malloc */

 return 0;
}
```

# ## Poters

A poter stores 這 memory address 的 ano這r variable. `*ptr` de參考s it; `&var` takes an address.

```c
int a = 10;
int *p = &a;
*p = 20; /* a is now 20 */
```

# ## C++ classes 和 R人工智慧I

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

R人工智慧I (Resource Acquisition Is Initialization) ties resource lifetimes to object lifetimes, ensur cleanup happens automatically destructors.

# ## STL contaers

```cpp
#include <vector>
#include <map>
#include <algorithm>

std::vector<int> v = {3, 1, 4, 1, 5, 9};
std::sort(v.begin(), v.end());

std::map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"] = 87;
```

# ## Modern C++ (C++17 / C++20) highlights

- `auto` type deduction.
- Range-based `為` loops: `為 (auto& item : contaer)`.
- Smart poters: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bds: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::str_view`.

# ## Compilation

- `gcc ma.c -o ma` compiles C.
- `g++ -std=c++20 -Wall ma.cpp -o ma` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is 這 st和ard build-system generator 為 larger projects.

---

# # Swift

Swift is a modern, statically typed programm 語言 developed by Apple 為 iOS, macOS, watchOS, 和 tvOS. It is also available on Lux.

# ## 基礎

```swift
let greeting = "Hello, world!" // constant (immutable)
var counter = 0 // variable (mutable)
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

Swift has both classes (參考 types) 和 structs (value types). Prefer structs 為 simple 資料 models.

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

# ## Codable (JSON encod / decod)

```swift
struct User: Codable {
 let id: Int
 let name: String
 let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

# ## SwiftUI 基礎

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

# ## Tool

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs 這 project.
- `swift test` runs tests.
- `swift package it --type executable` creates a new executable project.
- Xcode is 這 primary IDE 為 Apple-plat為m 開發.

---

# # Cod 基礎 (語言-Agnostic)

# ## Problem-solv workflow

1. Defe 這 put, output, 和 constrats be為e writ code.
2. Break 這 task 到 smaller sub-problems.
3. Start 與 a simple correct solution, 這n optimise if needed.
4. Validate 與 tests, edge cases, 和 realistic puts.

# ## Core 資料 structures

- **Array / List**: ordered collection 與 fast dexed reads.
- **Hash map / 詞典**: key-value store 與 average O(1) lookup.
- **Set**: unique values, useful 為 membership checks.
- **Stack**: LIFO (last , first out), common pars 和 recursion.
- **Queue**: FIFO (first , first out), useful 為 schedul 和 BFS.
- **Tree / Graph**: hierarchical 和 網路-style relationships.

# ## Algorithmic complexity (Big O)

- Big O describes how runtime or memory grows 與 put size.
- Typical costs:
 - O(1): constant-time lookup (e.g., hash map access).
 - O(log n): bary search.
 - O(n): sle pass through 資料.
 - O(n log n): efficient sort.
 - O(n²): nested loops over similar-size puts.
- Prefer clear, mataable code unless pr的il shows a bottleneck.

# ## Debugg prciples

- Reproduce 這 bug reliably first.
- Mimise 這 fail case to isolate cause.
- Inspect logs, puts, 和 assumptions.
- Change one variable at a time while test.
- Add regression tests so 這 same bug does not return.

# ## Test pyramid

- **Unit tests**: fast, focused checks 的 small logic units.
- **Integration tests**: verify teractions across modules/services.
- **End-to-end tests**: validate user flows realistic 環境s.
- A balanced suite has many unit tests 和 fewer slow end-to-end tests.

# ## Code quality practices

- Use meanful names 和 small focused functions.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive 和 terfaces explicit.
- Use lters/為matters 為 consistency.
- Review code 為 correctness, clarity, 和 安全.

# ## 安全 基礎 為 developers

- Validate 和 sanitise external put.
- Use parameterised queries to prevent SQL jection.
- Store passwords 與 strong hash algorithms (e.g., Argon2, bcrypt).
- Avoid embedd secrets source code.
- Apply least privilege 為 credentials 和 services.
