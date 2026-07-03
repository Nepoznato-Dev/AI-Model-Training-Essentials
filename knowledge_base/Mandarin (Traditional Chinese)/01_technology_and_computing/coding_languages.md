# 程式語言

## Python

Python 是一種高階、解釋型、動態型別、通用程式語言。它強調可讀性，並使用具有語義意義的縮排來界定程式碼塊。

### 語法基礎

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

### 函式與型別提示

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### 列表推導式

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### 類與物件導向程式設計

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

### 常見模式

- 使用 `with open(path) as f:` 進行檔案 I/O。
- 相比 `%` 或 `.format()`，優先使用 f-string（`f"hello {name}"`）。
- 對僅承載資料的類，使用 `dataclasses.dataclass`。
- 處理檔案路徑時，優先使用 `pathlib.Path` 而不是 `os.path`。

### 工具鏈

- `pip install <package>` 用於安裝包。
- `python -m venv .venv && source .venv/bin/activate` 用於建立虛擬環境。
- `pip freeze > requirements.txt` 用於儲存依賴。
- `pip install -r requirements.txt` 用於恢復依賴。
- `pyproject.toml` 是現代專案設定的標準檔案。

---

## JavaScript

JavaScript 是 Web 的核心語言。它既可在瀏覽器中執行，也可透過 Node.js 在伺服器端執行。它是動態型別語言，並採用基於原型的物件模型。

### 現代語法（ES6+）

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

### 非同步程式設計

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

### 陣列方法

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM 操作

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### 工具鏈

- `npm init -y` 用於初始化專案。
- `npm install <package>` 用於新增依賴。
- `npm run <script>` 用於執行 `package.json` 中定義的指令碼。
- `node index.js` 用於透過 Node.js 執行指令碼。

---

## TypeScript

TypeScript 是 JavaScript 的靜態型別超集，可編譯為普通 JavaScript。它增加了型別註解、介面、泛型和列舉。

### 型別註解

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### 介面與型別

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### 泛型

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### 帶存取修飾詞的類

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

### tsconfig.json 基礎設定

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

### 工具鏈

- `npm install -g typescript` 用於安裝編譯器。
- `tsc` 用於編譯專案。
- `ts-node src/index.ts` 用於直接執行 TypeScript。

---

## Rust

Rust 是一種面向安全、速度和併發的系統程式語言。它透過所有權系統在編譯期防止記憶體安全漏洞。

### 所有權與借用

Rust 中的每個值都恰好有一個所有者。當所有者離開作用域時，該值會被釋放。借用允許在不轉移所有權的前提下使用引用。

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

可變借用（`&mut T`）要求同一時間不能存在其他借用。

### 生命週期

生命週期確保引用不會比其指向的資料存活得更久。

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### 列舉與模式匹配

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

### 錯誤處理

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

返回 `Result` 的函式內部可以使用 `?` 運算子自動傳播錯誤。

### 工具鏈（Cargo）

- `cargo new project_name` 用於建立新專案。
- `cargo build` 用於編譯。
- `cargo run` 用於編譯並執行。
- `cargo test` 用於執行測試。
- `cargo add <crate>` 用於向 `Cargo.toml` 新增依賴。
- `cargo fmt` 用於格式化程式碼。`cargo clippy` 用於靜態檢查。

---

## Go

Go（Golang）是一種靜態型別、編譯型語言，旨在以簡潔的方式構建高效能併發程式。

### 基礎

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### 函式與多返回值

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### 介面

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

任何實現了介面全部方法的型別都會滿足該介面，無需顯式宣告。

### Goroutine 與 Channel

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

### 工具鏈

- `go mod init module/name` 用於初始化模組。
- `go get ./...` 用於下載依賴。
- `go build ./...` 用於編譯。
- `go test ./...` 用於執行測試。
- `go fmt ./...` 用於格式化程式碼。
- `go vet ./...` 用於檢查常見錯誤。

---

## C 和 C++

C 是一種低階、編譯型、過程式語言。C++ 在 C 的基礎上擴充套件了類、模板以及標準模板庫（STL）。

### C 基礎

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

### 指標

指標儲存另一個變數的記憶體地址。`*ptr` 用於解引用，`&var` 用於取地址。

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ 類與 RAII

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

RAII（Resource Acquisition Is Initialization，資源獲取即初始化）將資源生命週期繫結到物件生命週期上，從而確保資源會在解構函式中自動清理。

### STL 容器

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

### 現代 C++（C++17 / C++20）亮點

- `auto` 型別推導。
- 基於範圍的 `for` 迴圈：`for (auto& item : container)`。
- 智慧指標：`std::unique_ptr`、`std::shared_ptr` —— 避免直接使用原始 `new`/`delete`。
- 結構化繫結：`auto [key, val] = pair;`。
- `std::optional`、`std::variant`、`std::string_view`。

### 編譯

- `gcc main.c -o main` 用於編譯 C。
- `g++ -std=c++20 -Wall main.cpp -o main` 用於編譯 C++。
- `make` 可透過 `Makefile` 自動化多檔案構建。
- `cmake` 是大型專案常用的標準構建系統生成器。

---

## Swift

Swift 是 Apple 為 iOS、macOS、watchOS 和 tvOS 開發的現代靜態型別程式語言，也可執行於 Linux。

### 基礎

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optional

Optional（`T?`）表示一個值可能存在，也可能不存在。

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

### 函式與閉包

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### 類與結構體

Swift 同時擁有類（引用型別）和結構體（值型別）。對於簡單的資料模型，優先使用結構體。

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

### 協議

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable（JSON 編碼 / 解碼）

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### SwiftUI 基礎

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

### 工具鏈

- `swift build` 用於編譯 Swift Package Manager 專案。
- `swift run` 用於執行專案。
- `swift test` 用於執行測試。
- `swift package init --type executable` 用於建立新的可執行專案。
- Xcode 是 Apple 平台開發的主要 IDE。

---

## 程式設計基礎（與語言無關）

### 問題求解流程

1. 編寫程式碼前，先定義輸入、輸出和約束條件。
2. 將任務拆分為更小的子問題。
3. 先寫出一個簡單且正確的方案，再在需要時進行最佳化。
4. 用測試、邊界情況和真實輸入來驗證結果。

### 核心資料結構

- **Array / List**：有序集合，支援快速按索引讀取。
- **Hash map / Dictionary**：鍵值儲存，平均查詢複雜度為 O(1)。
- **Set**：元素唯一，適合做成員檢查。
- **Stack**：LIFO（後進先出），常用於解析和遞迴。
- **Queue**：FIFO（先進先出），適用於排程和 BFS。
- **Tree / Graph**：表示層次關係與網路關係。

### 演算法複雜度（Big O）

- Big O 用於描述執行時間或記憶體佔用如何隨輸入規模成長。
- 典型複雜度：
  - O(1)：常數時間查詢（例如雜湊表存取）。
  - O(log n)：二分查詢。
  - O(n)：對資料進行一次線性遍歷。
  - O(n log n)：高效排序。
  - O(n²)：對規模相近的輸入做巢狀迴圈。
- 除非效能分析顯示存在瓶頸，否則應優先選擇清晰、易維護的程式碼。

### 除錯原則

- 首先穩定復現問題。
- 儘量縮小失敗用例以定位原因。
- 檢查日誌、輸入和既有假設。
- 測試時一次只改變一個變數。
- 新增回歸測試，避免同類問題再次出現。

### 測試金字塔

- **單元測試**：快速、聚焦於小型邏輯單元。
- **整合測試**：驗證模組或服務之間的互動。
- **端到端測試**：在真實環境中驗證使用者流程。
- 一個平衡的測試體系通常包含大量單元測試和較少的慢速端到端測試。

### 程式碼品質實踐

- 使用有意義的命名和小而專注的函式。
- 在可行時優先使用純函式（更少副作用）。
- 保持模組內聚、介面明確。
- 使用 linter / formatter 保持一致性。
- 從正確性、清晰度和安全性角度審查程式碼。

### 開發者安全基礎

- 對外部輸入進行驗證和清洗。
- 使用參數化查詢防止 SQL 注入。
- 使用強雜湊演算法儲存密碼（如 Argon2、bcrypt）。
- 避免將金鑰或憑據直接寫入原始碼。
- 為憑據和服務應用最小許可權原則。
