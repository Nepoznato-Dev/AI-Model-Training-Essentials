<!-- 
This file was automatically translated from English to Korean.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 프로그래밍 언어

## Python

Python은 고수준의 인터프리터형 동적 타입 범용 프로그래밍 언어입니다. 가독성을 중시하며, 들여쓰기로 코드 블록을 구분합니다.

### 구문 기본

```python
# 변수와 타입
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# 조건문
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# 루프
for i in range(5):
    print(i)

while active:
    active = False
```

### 함수와 타입 힌트

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### 리스트 컴프리헨션

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### 클래스와 OOP

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

### 자주 쓰는 패턴

- 파일 I/O에는 `with open(path) as f:` 구문을 사용합니다.
- `%`나 `.format()`보다 f-string(`f"hello {name}"`)을 선호합니다.
- 데이터만 담는 클래스에는 `dataclasses.dataclass`가 유용합니다.
- 파일 경로 처리에는 `os.path`보다 `pathlib.Path`를 선호합니다.

### 도구

- `pip install <package>`로 package를 설치합니다.
- `python -m venv .venv && source .venv/bin/activate`로 virtual environment를 만듭니다.
- `pip freeze > requirements.txt`로 dependency 목록을 저장합니다.
- `pip install -r requirements.txt`로 dependency를 복원합니다.
- `pyproject.toml`은 현대적인 프로젝트 설정 표준입니다.

---

## JavaScript

JavaScript는 웹의 핵심 프로그래밍 언어입니다. browser에서 실행되며, Node.js를 통해 server에서도 사용할 수 있습니다. 동적 타입이며 prototype-based 특성을 가집니다.

### 최신 구문 (ES6+)

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

### 비동기 프로그래밍

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

### 배열 메서드

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM 조작

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### 도구

- `npm init -y`로 프로젝트를 초기화합니다.
- `npm install <package>`로 dependency를 추가합니다.
- `npm run <script>`는 `package.json`에 정의된 script를 실행합니다.
- `node index.js`로 Node.js에서 script를 실행합니다.

---

## TypeScript

TypeScript는 JavaScript의 정적 타입 superset으로, 최종적으로 plain JavaScript로 compile됩니다. type annotation, interface, generic, enum을 추가해 더 안전한 개발을 돕습니다.

### 타입 어노테이션

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### 인터페이스와 타입

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### 제네릭

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### 클래스와 접근 제어자

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

### tsconfig.json 핵심 설정

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

### 도구

- `npm install -g typescript`로 compiler를 설치합니다.
- `tsc`로 프로젝트를 compile합니다.
- `ts-node src/index.ts`로 TypeScript를 직접 실행합니다.

---

## Rust

Rust는 안전성, 속도, concurrency에 초점을 맞춘 시스템 프로그래밍 언어입니다. ownership system을 통해 memory-safety bug를 compile time에 방지합니다.

### 소유권과 빌림

Rust의 모든 값은 정확히 한 명의 owner를 가집니다. owner가 scope를 벗어나면 값은 drop됩니다. borrowing을 사용하면 ownership을 넘기지 않고도 참조할 수 있습니다.

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

Mutable borrow(`&mut T`)는 같은 시점에 다른 borrow가 존재하지 않아야 합니다.

### Lifetime

Lifetime은 참조가 가리키는 데이터보다 더 오래 살아남지 않도록 보장합니다.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### enum과 패턴 매칭

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

### 오류 처리

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

`?` operator는 `Result`를 반환하는 함수 안에서 오류를 자동으로 전파합니다.

### 도구 (Cargo)

- `cargo new project_name`으로 새 프로젝트를 만듭니다.
- `cargo build`로 compile합니다.
- `cargo run`으로 build와 실행을 함께 합니다.
- `cargo test`로 test를 실행합니다.
- `cargo add <crate>`로 `Cargo.toml`에 dependency를 추가합니다.
- `cargo fmt`는 formatting, `cargo clippy`는 lint를 담당합니다.

---

## Go

Go(Golang)는 단순함과 고성능 concurrent program 작성을 목표로 설계된 정적 타입 compile 언어입니다.

### 기본

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### 함수와 다중 반환값

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### 인터페이스

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

어떤 타입이 인터페이스에 정의된 모든 메서드를 구현하면, 별도의 선언 없이도 그 인터페이스를 만족합니다.

### goroutine과 channel

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

### 도구

- `go mod init module/name`으로 module을 초기화합니다.
- `go get ./...`로 dependency를 내려받습니다.
- `go build ./...`로 compile합니다.
- `go test ./...`로 test를 실행합니다.
- `go fmt ./...`로 코드를 포맷합니다.
- `go vet ./...`는 흔한 실수를 점검합니다.

---

## C와 C++

C는 저수준의 compile 절차형 언어입니다. C++는 여기에 class, template, Standard Template Library(STL) 등을 더해 확장한 언어입니다.

### C 기본

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

### 포인터

Pointer는 다른 변수의 memory address를 저장합니다. `*ptr`는 역참조를, `&var`는 주소 취득을 의미합니다.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ 클래스와 RAII

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

RAII(Resource Acquisition Is Initialization)는 resource의 수명을 object 수명과 연결해 destructor에서 자동으로 정리가 이뤄지게 하는 방식입니다.

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

### Modern C++ (C++17 / C++20) 핵심 포인트

- `auto`로 type deduction을 할 수 있습니다.
- 범위 기반 `for` loop를 사용할 수 있습니다: `for (auto& item : container)`.
- Smart pointer인 `std::unique_ptr`, `std::shared_ptr`를 사용해 raw `new`/`delete`를 피합니다.
- Structured bindings를 지원합니다: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view` 같은 현대적 도구를 제공합니다.

### 컴파일

- `gcc main.c -o main`으로 C를 compile합니다.
- `g++ -std=c++20 -Wall main.cpp -o main`으로 C++를 compile합니다.
- `make`는 `Makefile`을 통해 여러 파일의 build를 자동화합니다.
- `cmake`는 대형 프로젝트에서 널리 쓰이는 build-system generator입니다.

---

## Swift

Swift는 Apple이 iOS, macOS, watchOS, tvOS 개발을 위해 만든 현대적인 정적 타입 프로그래밍 언어입니다. Linux에서도 사용할 수 있습니다.

### 기본

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optional

Optional(`T?`)은 값이 있을 수도 있고 없을 수도 있음을 나타냅니다.

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

### 함수와 클로저

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### 클래스와 struct

Swift에는 classes(참조 타입)와 structs(값 타입)가 모두 있습니다. 단순한 데이터 모델에는 보통 struct를 우선합니다.

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

### 프로토콜

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

### SwiftUI 기본

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

### 도구

- `swift build`는 Swift Package Manager 프로젝트를 compile합니다.
- `swift run`으로 프로젝트를 실행합니다.
- `swift test`로 test를 실행합니다.
- `swift package init --type executable`로 새 executable 프로젝트를 만듭니다.
- Xcode는 Apple platform 개발의 대표적인 IDE입니다.

---

## 코딩 기초 (언어 불문)

### 문제 해결 흐름

1. 코드를 쓰기 전에 input, output, constraint를 먼저 정의합니다.
2. 문제를 더 작은 하위 문제로 나눕니다.
3. 먼저 단순하지만 정확한 해법을 만든 뒤, 필요할 때 최적화합니다.
4. test, edge case, 실제 입력으로 검증합니다.

### 핵심 데이터 구조

- **Array / List**: 순서가 있는 collection으로, index 기반 읽기가 빠릅니다.
- **Hash map / 사전**: key-value 저장소로, 평균적으로 O(1) lookup이 가능합니다.
- **Set**: 중복 없는 값 집합으로, membership check에 유용합니다.
- **Stack**: LIFO(last in, first out) 구조로, parsing과 recursion에서 자주 씁니다.
- **Queue**: FIFO(first in, first out) 구조로, scheduling과 BFS에 유용합니다.
- **Tree / Graph**: 계층 구조나 네트워크형 관계를 표현합니다.

### 알고리즘 복잡도 (Big O)

- Big O는 입력 크기에 따라 실행 시간이나 메모리 사용량이 어떻게 늘어나는지 설명합니다.
- 대표적인 비용 예시는 다음과 같습니다.
  - O(1): 상수 시간 lookup(예: hash map access)
  - O(log n): binary search
  - O(n): 데이터를 한 번 훑는 경우
  - O(n log n): 효율적인 sorting
  - O(n²): 비슷한 크기의 입력에 대해 중첩 loop를 도는 경우
- profiling에서 병목이 확인되지 않는다면, 지나친 최적화보다 명확하고 유지보수하기 쉬운 코드를 우선합니다.

### 디버깅 원칙

- 먼저 버그를 안정적으로 재현합니다.
- 실패하는 case를 최소화해 원인을 분리합니다.
- log, input, 가정을 차근차근 점검합니다.
- test 중에는 한 번에 한 가지 변수만 바꿉니다.
- 같은 문제가 다시 생기지 않도록 regression test를 추가합니다.

### 테스트 피라미드

- **Unit tests**: 작은 logic 단위를 빠르고 집중적으로 검증합니다.
- **Integration tests**: module이나 service 간 상호작용을 확인합니다.
- **End-to-end tests**: 실제에 가까운 환경에서 사용자 흐름을 검증합니다.
- 균형 잡힌 test suite는 unit test가 많고, 느린 end-to-end test는 상대적으로 적습니다.

### 코드 품질 실천법

- 의미 있는 이름과 작고 집중된 함수를 사용합니다.
- 가능하다면 side effect가 적은 pure function을 선호합니다.
- module은 응집도 높게 유지하고, interface는 명시적으로 설계합니다.
- 일관성을 위해 linter와 formatter를 사용합니다.
- correctness, clarity, security를 중심으로 code review를 진행합니다.

### 개발자를 위한 보안 기본

- 외부 입력은 반드시 검증하고 sanitise합니다.
- SQL injection을 막기 위해 parameterised query를 사용합니다.
- password는 Argon2, bcrypt 같은 강력한 hashing algorithm으로 저장합니다.
- source code 안에 secret을 직접 넣지 않습니다.
- credential과 service에는 least privilege 원칙을 적용합니다.
