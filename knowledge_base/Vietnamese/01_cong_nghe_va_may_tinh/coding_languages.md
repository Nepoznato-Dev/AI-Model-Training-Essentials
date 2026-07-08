# Ngôn ngữ mã hóa

## Python

Python là ngôn ngữ lập trình có mục đích chung, được giải thích, được gõ động và cấp cao. Nó nhấn mạnh đến khả năng đọc và sử dụng thụt lề đáng kể làm dấu phân cách khối.

###Cú pháp cơ bản

```python
# Biến và kiểu
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Điều kiện
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Vòng lặp
for i in range(5):
    print(i)

while active:
    active = False
```

### Gợi ý hàm và kiểu

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Hiểu danh sách

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Lớp và OOP

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

### Các mẫu phổ biến

- Sử dụng `with open(path) as f:` cho tệp I/O.
- Ưu tiên chuỗi f (`f"hello {name}"`) hơn `%` hoặc `.format()`.
- Sử dụng `dataclasses.dataclass` cho các lớp chỉ có dữ liệu.
- Sử dụng `pathlib.Path` thay vì `os.path` cho đường dẫn tệp.

### Dụng cụ

- `pip install <package>` cài đặt gói.
- `python -m venv .venv && source .venv/bin/activate` tạo môi trường ảo.
- `pip freeze > requirements.txt` lưu các phần phụ thuộc.
- `pip install -r requirements.txt` khôi phục chúng.
- `pyproject.toml` là tiêu chuẩn cấu hình dự án hiện đại.

---

## Javascript

JavaScript là ngôn ngữ chính của web. Nó chạy trong trình duyệt và trên máy chủ thông qua Node.js. Nó được gõ động và dựa trên nguyên mẫu.

### Cú pháp hiện đại (ES6+)

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

### Lập trình không đồng bộ

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

### Các phương thức mảng

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Thao tác trên DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Dụng cụ

- `npm init -y` khởi tạo một dự án.
- `npm install <package>` thêm phần phụ thuộc.
- `npm run <script>` chạy tập lệnh được xác định trong `package.json`.
- `node index.js` chạy tập lệnh với Node.js.

---

## TypeScript

TypeScript là một siêu tập hợp JavaScript được gõ tĩnh để biên dịch thành JavaScript đơn giản. Nó thêm chú thích kiểu, giao diện, generic và enum.

###Gõ chú thích

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Giao diện và loại

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Thuốc gốc

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Các lớp có công cụ sửa đổi truy cập

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

### những điều cần thiết về tsconfig.json

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

### Dụng cụ

- `npm install -g typescript` cài đặt trình biên dịch.
- `tsc` biên dịch dự án.
- `ts-node src/index.ts` chạy trực tiếp TypeScript.

---

## Rỉ sét

Rust là ngôn ngữ lập trình hệ thống tập trung vào sự an toàn, tốc độ và tính đồng thời. Nó ngăn ngừa các lỗi an toàn bộ nhớ tại thời điểm biên dịch thông qua hệ thống sở hữu của nó.

### Quyền sở hữu và vay mượn

Mọi giá trị trong Rust đều có chính xác một chủ sở hữu. Khi chủ sở hữu đi ra khỏi phạm vi, giá trị sẽ bị loại bỏ. Việc mượn cho phép tài liệu tham khảo mà không cần chuyển quyền sở hữu.

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

Các khoản vay có thể thay đổi (`&mut T`) yêu cầu không có khoản vay nào khác tồn tại cùng một lúc.

### Cuộc đời

Vòng đời đảm bảo các tham chiếu không tồn tại lâu hơn dữ liệu mà chúng trỏ tới.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums và khớp mẫu

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

### Xử lý lỗi

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

Toán tử `?` tự động truyền lỗi bên trong các hàm trả về `Result`.

### Dụng cụ (Hàng hóa)

- `cargo new project_name` tạo một dự án mới.
- `cargo build` biên dịch.
- `cargo run` biên dịch và chạy.
- `cargo test` chạy thử nghiệm.
- `cargo add <crate>` thêm phần phụ thuộc vào `Cargo.toml`.
- Mã định dạng `cargo fmt`. `cargo clippy` xơ vải.

---

## Đi

Go (Golang) là một ngôn ngữ được biên dịch, gõ tĩnh được thiết kế cho các chương trình đồng thời đơn giản và hiệu suất cao.

### Cơ bản

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Hàm và nhiều giá trị trả về

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Giao diện

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Bất kỳ loại nào thực hiện tất cả các phương thức của một giao diện đều thỏa mãn nó - không cần khai báo rõ ràng.

### Goroutine và kênh

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

### Trì hoãn

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

### Dụng cụ

- `go mod init module/name` khởi tạo một mô-đun.
- `go get ./...` tải xuống các phần phụ thuộc.
- `go build ./...` biên dịch.
- `go test ./...` chạy thử nghiệm.
- Mã định dạng `go fmt ./...`.
- `go vet ./...` kiểm tra các lỗi thường gặp.

---

## C và C++

C là một ngôn ngữ thủ tục, được biên dịch, cấp thấp. C++ mở rộng C với các lớp, mẫu và Thư viện mẫu chuẩn (STL).

###C cơ bản về C

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

### Con trỏ

Một con trỏ lưu trữ địa chỉ bộ nhớ của một biến khác. `*ptr` hủy đăng ký nó; `&var` lấy một địa chỉ.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Các lớp C++ và RAII

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

RAII (Thu thập tài nguyên là khởi tạo) liên kết thời gian tồn tại của tài nguyên với thời gian tồn tại của đối tượng, đảm bảo quá trình dọn dẹp diễn ra tự động trong các hàm hủy.

### thùng chứa STL

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

### Điểm nổi bật của C++ hiện đại (C++17 / C++20)

- `auto` khấu trừ loại.
- Vòng lặp `for` dựa trên phạm vi: `for (auto& item : container)`.
- Con trỏ thông minh: `std::unique_ptr`, `std::shared_ptr` — tránh `new`/`delete` thô.
- Liên kết có cấu trúc: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Biên soạn- `gcc main.c -o main` biên dịch C.
- `g++ -std=c++20 -Wall main.cpp -o main` biên dịch C++.
- `make` tự động hóa việc xây dựng nhiều tệp thông qua `Makefile`.
- `cmake` là trình tạo hệ thống xây dựng tiêu chuẩn cho các dự án lớn hơn.

---

## Nhanh

Swift là ngôn ngữ lập trình hiện đại, kiểu tĩnh được Apple phát triển cho iOS, macOS, watchOS và tvOS. Nó cũng có sẵn trên Linux.

### Cơ bản

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Tùy chọn

Tùy chọn (`T?`) đại diện cho một giá trị có thể có hoặc không có.

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

### Hàm và các bao đóng

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Lớp và cấu trúc

Swift có cả lớp (kiểu tham chiếu) và cấu trúc (kiểu giá trị). Thích cấu trúc cho các mô hình dữ liệu đơn giản.

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

### Giao thức

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Có thể mã hóa (mã hóa/giải mã JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Thông tin cơ bản về SwiftUI

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

### Dụng cụ

- `swift build` biên dịch dự án Trình quản lý gói Swift.
- `swift run` chạy dự án.
- `swift test` chạy thử nghiệm.
- `swift package init --type executable` tạo một dự án thực thi mới.
- Xcode là IDE chính để phát triển nền tảng Apple.

---

## Nguyên tắc cơ bản về mã hóa (Ngôn ngữ bất khả tri)

### Quy trình giải quyết vấn đề

1. Xác định đầu vào, đầu ra và các ràng buộc trước khi viết mã.
2. Chia nhiệm vụ thành các vấn đề nhỏ hơn.
3. Bắt đầu với một giải pháp đơn giản, chính xác, sau đó tối ưu hóa nếu cần.
4. Xác thực bằng các thử nghiệm, trường hợp đặc biệt và thông tin đầu vào thực tế.

### Cấu trúc dữ liệu cốt lõi

- **Mảng / Danh sách**: bộ sưu tập được sắp xếp với tốc độ đọc được lập chỉ mục nhanh.
- **Bản đồ băm / Từ điển**: lưu trữ khóa-giá trị với mức tra cứu trung bình O(1).
- **Đặt**: các giá trị duy nhất, hữu ích cho việc kiểm tra tư cách thành viên.
- **Stack**: LIFO (last in, first out), phổ biến trong phân tích cú pháp và đệ quy.
- **Hàng đợi**: FIFO (nhập trước, xuất trước), hữu ích cho việc lập lịch và BFS.
- **Cây / Đồ thị**: mối quan hệ phân cấp và kiểu mạng.

### Độ phức tạp của thuật toán (Big O)

- Big O mô tả thời gian chạy hoặc bộ nhớ tăng lên như thế nào với kích thước đầu vào.
- Chi phí điển hình:
  - O(1): tra cứu theo thời gian liên tục (ví dụ: truy cập bản đồ băm).
  - O(log n): tìm kiếm nhị phân.
  - O(n): dữ liệu truyền một lần.
  - O(n log n): sắp xếp hiệu quả.
  - O(n²): các vòng lặp lồng nhau trên các đầu vào có kích thước tương tự.
- Ưu tiên mã rõ ràng, có thể bảo trì trừ khi hồ sơ hiển thị nút thắt cổ chai.

### Nguyên tắc gỡ lỗi

- Tái tạo lỗi một cách đáng tin cậy trước tiên.
- Hạn chế tối đa các trường hợp hư hỏng để tách biệt nguyên nhân.
- Kiểm tra nhật ký, đầu vào và giả định.
- Thay đổi một biến tại một thời điểm trong khi thử nghiệm.
- Thêm các bài kiểm tra hồi quy để lỗi tương tự không quay trở lại.

### Thử nghiệm kim tự tháp

- **Kiểm tra đơn vị**: kiểm tra nhanh, tập trung các đơn vị logic nhỏ.
- **Thử nghiệm tích hợp**: xác minh sự tương tác giữa các mô-đun/dịch vụ.
- **Thử nghiệm toàn diện**: xác thực luồng người dùng trong môi trường thực tế.
- Một bộ cân bằng có nhiều bài kiểm tra đơn vị và ít bài kiểm tra đầu cuối chậm hơn.

### Thực hành chất lượng mã

- Sử dụng tên có ý nghĩa và chức năng tập trung nhỏ.
- Ưu tiên các hàm thuần túy (ít tác dụng phụ hơn) khi thực tế.
- Giữ các mô-đun gắn kết và giao diện rõ ràng.
- Sử dụng linters/formatters để đảm bảo tính nhất quán.
- Xem lại mã về tính chính xác, rõ ràng và bảo mật.

### Thông tin cơ bản về bảo mật dành cho nhà phát triển

- Xác thực và vệ sinh đầu vào bên ngoài.
- Sử dụng các truy vấn được tham số hóa để ngăn chặn việc tiêm SQL.
- Lưu trữ mật khẩu bằng thuật toán băm mạnh (ví dụ: Argon2, bcrypt).
- Tránh nhúng bí mật vào mã nguồn.
- Áp dụng đặc quyền tối thiểu cho thông tin xác thực và dịch vụ.