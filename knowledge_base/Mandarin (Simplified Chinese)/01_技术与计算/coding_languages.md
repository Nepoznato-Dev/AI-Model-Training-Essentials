# 编程语言

## Python

Python 是一种高级、解释型、动态类型、通用编程语言。它强调可读性，并使用具有语义意义的缩进来界定代码块。

### 语法基础

```python
# 变量和类型
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# 条件语句
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# 循环
for i in range(5):
    print(i)

while active:
    active = False
```

### 函数与类型提示

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### 列表推导式

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### 类与面向对象编程

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

### 常见模式

- 使用 `with open(path) as f:` 进行文件 I/O。
- 相比 `%` 或 `.format()`，优先使用 f-string（`f"hello {name}"`）。
- 对仅承载数据的类，使用 `dataclasses.dataclass`。
- 处理文件路径时，优先使用 `pathlib.Path` 而不是 `os.path`。

### 工具链

- `pip install <package>` 用于安装包。
- `python -m venv .venv && source .venv/bin/activate` 用于创建虚拟环境。
- `pip freeze > requirements.txt` 用于保存依赖。
- `pip install -r requirements.txt` 用于恢复依赖。
- `pyproject.toml` 是现代项目配置的标准文件。

---

## JavaScript

JavaScript 是 Web 的核心语言。它既可在浏览器中运行，也可通过 Node.js 在服务器端运行。它是动态类型语言，并采用基于原型的对象模型。

### 现代语法（ES6+）

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

### 异步编程

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

### 数组方法

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

### 工具链

- `npm init -y` 用于初始化项目。
- `npm install <package>` 用于添加依赖。
- `npm run <script>` 用于运行 `package.json` 中定义的脚本。
- `node index.js` 用于通过 Node.js 运行脚本。

---

## TypeScript

TypeScript 是 JavaScript 的静态类型超集，可编译为普通 JavaScript。它增加了类型注解、接口、泛型和枚举。

### 类型注解

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### 接口与类型

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

### 带访问修饰符的类

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

### tsconfig.json 基础配置

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

### 工具链

- `npm install -g typescript` 用于安装编译器。
- `tsc` 用于编译项目。
- `ts-node src/index.ts` 用于直接运行 TypeScript。

---

## Rust

Rust 是一种面向安全、速度和并发的系统编程语言。它通过所有权系统在编译期防止内存安全漏洞。

### 所有权与借用

Rust 中的每个值都恰好有一个所有者。当所有者离开作用域时，该值会被释放。借用允许在不转移所有权的前提下使用引用。

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

可变借用（`&mut T`）要求同一时间不能存在其他借用。

### 生命周期

生命周期确保引用不会比其指向的数据存活得更久。

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### 枚举与模式匹配

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

### 错误处理

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

返回 `Result` 的函数内部可以使用 `?` 运算符自动传播错误。

### 工具链（Cargo）

- `cargo new project_name` 用于创建新项目。
- `cargo build` 用于编译。
- `cargo run` 用于编译并运行。
- `cargo test` 用于运行测试。
- `cargo add <crate>` 用于向 `Cargo.toml` 添加依赖。
- `cargo fmt` 用于格式化代码。`cargo clippy` 用于静态检查。

---

## Go

Go（Golang）是一种静态类型、编译型语言，旨在以简洁的方式构建高性能并发程序。

### 基础

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### 函数与多返回值

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### 接口

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

任何实现了接口全部方法的类型都会满足该接口，无需显式声明。

### Goroutine 与 Channel

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

### 工具链

- `go mod init module/name` 用于初始化模块。
- `go get ./...` 用于下载依赖。
- `go build ./...` 用于编译。
- `go test ./...` 用于运行测试。
- `go fmt ./...` 用于格式化代码。
- `go vet ./...` 用于检查常见错误。

---

## C 和 C++

C 是一种低级、编译型、过程式语言。C++ 在 C 的基础上扩展了类、模板以及标准模板库（STL）。

### C 基础

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

### 指针

指针保存另一个变量的内存地址。`*ptr` 用于解引用，`&var` 用于取地址。

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ 类与 RAII

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

RAII（Resource Acquisition Is Initialization，资源获取即初始化）将资源生命周期绑定到对象生命周期上，从而确保资源会在析构函数中自动清理。

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

### 现代 C++（C++17 / C++20）亮点

- `auto` 类型推导。
- 基于范围的 `for` 循环：`for (auto& item : container)`。
- 智能指针：`std::unique_ptr`、`std::shared_ptr` —— 避免直接使用原始 `new`/`delete`。
- 结构化绑定：`auto [key, val] = pair;`。
- `std::optional`、`std::variant`、`std::string_view`。

### 编译

- `gcc main.c -o main` 用于编译 C。
- `g++ -std=c++20 -Wall main.cpp -o main` 用于编译 C++。
- `make` 可通过 `Makefile` 自动化多文件构建。
- `cmake` 是大型项目常用的标准构建系统生成器。

---

## Swift

Swift 是 Apple 为 iOS、macOS、watchOS 和 tvOS 开发的现代静态类型编程语言，也可运行于 Linux。

### 基础

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optional

Optional（`T?`）表示一个值可能存在，也可能不存在。

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

### 函数与闭包

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### 类与结构体

Swift 同时拥有类（引用类型）和结构体（值类型）。对于简单的数据模型，优先使用结构体。

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

### 协议

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable（JSON 编码 / 解码）

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### SwiftUI 基础

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

### 工具链

- `swift build` 用于编译 Swift Package Manager 项目。
- `swift run` 用于运行项目。
- `swift test` 用于运行测试。
- `swift package init --type executable` 用于创建新的可执行项目。
- Xcode 是 Apple 平台开发的主要 IDE。

---

## 编程基础（与语言无关）

### 问题求解流程

1. 编写代码前，先定义输入、输出和约束条件。
2. 将任务拆分为更小的子问题。
3. 先写出一个简单且正确的方案，再在需要时进行优化。
4. 用测试、边界情况和真实输入来验证结果。

### 核心数据结构

- **Array / List**：有序集合，支持快速按索引读取。
- **Hash map / Dictionary**：键值存储，平均查找复杂度为 O(1)。
- **Set**：元素唯一，适合做成员检查。
- **Stack**：LIFO（后进先出），常用于解析和递归。
- **Queue**：FIFO（先进先出），适用于调度和 BFS。
- **Tree / Graph**：表示层次关系与网络关系。

### 算法复杂度（Big O）

- Big O 用于描述运行时间或内存占用如何随输入规模增长。
- 典型复杂度：
  - O(1)：常数时间查找（例如哈希表访问）。
  - O(log n)：二分查找。
  - O(n)：对数据进行一次线性遍历。
  - O(n log n)：高效排序。
  - O(n²)：对规模相近的输入做嵌套循环。
- 除非性能分析显示存在瓶颈，否则应优先选择清晰、易维护的代码。

### 调试原则

- 首先稳定复现问题。
- 尽量缩小失败用例以定位原因。
- 检查日志、输入和既有假设。
- 测试时一次只改变一个变量。
- 添加回归测试，避免同类问题再次出现。

### 测试金字塔

- **单元测试**：快速、聚焦于小型逻辑单元。
- **集成测试**：验证模块或服务之间的交互。
- **端到端测试**：在真实环境中验证用户流程。
- 一个平衡的测试体系通常包含大量单元测试和较少的慢速端到端测试。

### 代码质量实践

- 使用有意义的命名和小而专注的函数。
- 在可行时优先使用纯函数（更少副作用）。
- 保持模块内聚、接口明确。
- 使用 linter / formatter 保持一致性。
- 从正确性、清晰度和安全性角度审查代码。

### 开发者安全基础

- 对外部输入进行验证和清洗。
- 使用参数化查询防止 SQL 注入。
- 使用强哈希算法存储密码（如 Argon2、bcrypt）。
- 避免将密钥或凭据直接写入源代码。
- 为凭据和服务应用最小权限原则。
