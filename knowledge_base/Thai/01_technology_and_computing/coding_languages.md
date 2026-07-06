# ภาษาการเข้ารหัส

## หลาม

Python เป็นภาษาการเขียนโปรแกรมสำหรับวัตถุประสงค์ทั่วไประดับสูง ตีความ พิมพ์ไดนามิก โดยเน้นให้อ่านง่ายและใช้การเยื้องที่สำคัญเป็นตัวคั่นบล็อก

### พื้นฐานไวยากรณ์

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

### ฟังก์ชั่นและคำแนะนำประเภท

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### รายการความเข้าใจ

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### คลาสและ OOP

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

### รูปแบบทั่วไป

- ใช้ `with open(path) as f:` สำหรับไฟล์ I/O
- ชอบ f-strings (`f"hello {name}"`) มากกว่า `%` หรือ `.format()`
- ใช้ `dataclasses.dataclass` สำหรับคลาสข้อมูลเท่านั้น
- ใช้ `pathlib.Path` แทน `os.path` สำหรับเส้นทางของไฟล์

### เครื่องมือ

- `pip install <package>` ติดตั้งแพ็คเกจ
- `python -m venv .venv && source .venv/bin/activate` สร้างสภาพแวดล้อมเสมือนจริง
- `pip freeze > requirements.txt` บันทึกการอ้างอิง
- `pip install -r requirements.txt` คืนค่า
- `pyproject.toml` เป็นมาตรฐานการกำหนดค่าโครงการที่ทันสมัย

---

## จาวาสคริปต์

JavaScript เป็นภาษาหลักของเว็บ มันทำงานในเบราว์เซอร์และบนเซิร์ฟเวอร์ผ่าน Node.js มีการพิมพ์แบบไดนามิกและใช้ต้นแบบ

### ไวยากรณ์สมัยใหม่ (ES6+)

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

### การเขียนโปรแกรมแบบอะซิงก์

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

### วิธีการอาร์เรย์

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### การจัดการ DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### เครื่องมือ

- `npm init -y` เริ่มต้นโครงการ
- `npm install <package>` เพิ่มการขึ้นต่อกัน
- `npm run <script>` รันสคริปต์ที่กำหนดใน `package.json`
- `node index.js` รันสคริปต์ด้วย Node.js

---

## พิมพ์สคริปต์

TypeScript เป็นชุด JavaScript ที่พิมพ์แบบคงที่ซึ่งคอมไพล์เป็น JavaScript ธรรมดา โดยเพิ่มคำอธิบายประกอบประเภท อินเทอร์เฟซ ข้อมูลทั่วไป และแจงนับ

### พิมพ์คำอธิบายประกอบ

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### อินเทอร์เฟซและประเภท

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### ทั่วไป

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### คลาสที่มีตัวดัดแปลงการเข้าถึง

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

### ข้อมูลสำคัญเกี่ยวกับ tsconfig.json

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

### เครื่องมือ

- `npm install -g typescript` ติดตั้งคอมไพเลอร์
- `tsc` รวบรวมโครงการ
- `ts-node src/index.ts` เรียกใช้ TypeScript โดยตรง

---

## สนิม

Rust เป็นภาษาการเขียนโปรแกรมระบบที่เน้นเรื่องความปลอดภัย ความเร็ว และการทำงานพร้อมกัน จะป้องกันข้อบกพร่องด้านความปลอดภัยของหน่วยความจำในเวลาคอมไพล์ผ่านระบบความเป็นเจ้าของ

### กรรมสิทธิ์และการกู้ยืม

ทุกค่าใน Rust มีเจ้าของเพียงคนเดียว เมื่อเจ้าของออกนอกขอบเขต ค่าก็จะลดลง การยืมช่วยให้อ้างอิงได้โดยไม่ต้องโอนกรรมสิทธิ์

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

การยืมที่ไม่แน่นอน (`&mut T`) กำหนดให้ไม่มีการยืมอื่น ๆ ในเวลาเดียวกัน

### ตลอดชีวิต

ตลอดอายุการใช้งานทำให้มั่นใจได้ว่าข้อมูลอ้างอิงจะไม่อยู่นานกว่าข้อมูลที่ชี้ไป

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### การแจงนับและการจับคู่รูปแบบ

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

### การจัดการข้อผิดพลาด

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

ตัวดำเนินการ `?` เผยแพร่ข้อผิดพลาดโดยอัตโนมัติภายในฟังก์ชันที่ส่งคืน `Result`

### เครื่องมือช่าง (สินค้า)

- `cargo new project_name` สร้างโครงการใหม่
- `cargo build` คอมไพล์
- `cargo run` คอมไพล์และรัน
- `cargo test` ทำการทดสอบ
- `cargo add <crate>` เพิ่มการอ้างอิงถึง `Cargo.toml`
- `cargo fmt` รูปแบบโค้ด `cargo clippy` ผ้าสำลี

---

## ไป

Go (Golang) เป็นภาษาคอมไพล์ที่พิมพ์แบบคงที่ซึ่งออกแบบมาเพื่อความเรียบง่ายและโปรแกรมที่ทำงานพร้อมกันประสิทธิภาพสูง

### พื้นฐาน

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### ฟังก์ชั่นและค่าส่งคืนหลายค่า

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### อินเทอร์เฟซ

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

ประเภทใดก็ตามที่ใช้วิธีการทั้งหมดของอินเทอร์เฟซก็เป็นไปตามนั้น ไม่จำเป็นต้องประกาศอย่างชัดเจน

### กิจวัตรและช่องทางต่างๆ

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

### เลื่อนออกไป

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

### เครื่องมือ

- `go mod init module/name` เริ่มต้นโมดูล
- `go get ./...` ดาวน์โหลดการอ้างอิง
- `go build ./...` คอมไพล์
- `go test ./...` ทำการทดสอบ
- `go fmt ./...` รูปแบบโค้ด
- `go vet ./...` ตรวจสอบข้อผิดพลาดทั่วไป

---

## C และ C ++

C เป็นภาษาระดับต่ำ เรียบเรียง เป็นขั้นตอน C++ ขยาย C ด้วยคลาส เทมเพลต และ Standard Template Library (STL)

### พื้นฐานซี

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

### ตัวชี้

ตัวชี้จะเก็บที่อยู่หน่วยความจำของตัวแปรอื่น `*ptr` ยกเลิกการอ้างอิง `&var` รับที่อยู่

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### คลาส C++ และ RAII

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

RAII (การได้มาซึ่งทรัพยากรคือการเริ่มต้น) เชื่อมโยงอายุการใช้งานของทรัพยากรกับอายุการใช้งานของวัตถุ เพื่อให้มั่นใจว่าการล้างข้อมูลจะเกิดขึ้นโดยอัตโนมัติในตัวทำลาย

### คอนเทนเนอร์ STL

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

### ไฮไลท์สมัยใหม่ C++ (C++17 / C++20)

- `auto` ประเภทการหักลดหย่อน
- ตามช่วง `for` ลูป: `for (auto& item : container)`
- ตัวชี้อัจฉริยะ: `std::unique_ptr`, `std::shared_ptr` — หลีกเลี่ยงดิบ `new`/`delete`
- การผูกแบบมีโครงสร้าง: `auto [key, val] = pair;`
- `std::optional`, `std::variant`, `std::string_view`.

### เรียบเรียง- `gcc main.c -o main` คอมไพล์ C.
- `g++ -std=c++20 -Wall main.cpp -o main` คอมไพล์ C++
- `make` สร้างไฟล์หลายไฟล์โดยอัตโนมัติผ่าน `Makefile`
- `cmake` เป็นตัวสร้างระบบมาตรฐานสำหรับโครงการขนาดใหญ่

---

##สวิฟท์

Swift เป็นภาษาโปรแกรมสมัยใหม่ที่มีการพิมพ์แบบคงที่ พัฒนาโดย Apple สำหรับ iOS, macOS, watchOS และ tvOS มีให้บริการบน Linux ด้วย

### พื้นฐาน

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### ตัวเลือก

ตัวเลือก (`T?`) แสดงถึงค่าที่อาจมีหรือไม่มีก็ได้

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

### ฟังก์ชั่นและการปิด

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### คลาสและโครงสร้าง

Swift มีทั้งคลาส (ประเภทอ้างอิง) และโครงสร้าง (ประเภทค่า) ต้องการโครงสร้างสำหรับโมเดลข้อมูลแบบธรรมดา

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

### โปรโตคอล

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### เข้ารหัสได้ (การเข้ารหัส / ถอดรหัส JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### พื้นฐาน SwiftUI

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

### เครื่องมือ

- `swift build` คอมไพล์โครงการ Swift Package Manager
- `swift run` ดำเนินโครงการ
- `swift test` ทำการทดสอบ
- `swift package init --type executable` สร้างโครงการปฏิบัติการใหม่
- Xcode เป็น IDE หลักสำหรับการพัฒนาแพลตฟอร์ม Apple

---

## พื้นฐานการเข้ารหัส (ภาษาที่ไม่เชื่อเรื่องพระเจ้า)

### ขั้นตอนการแก้ปัญหา

1. กำหนดอินพุต เอาต์พุต และข้อจำกัดก่อนเขียนโค้ด
2. แบ่งงานออกเป็นปัญหาย่อยย่อยๆ
3. เริ่มต้นด้วยวิธีแก้ปัญหาง่ายๆ ที่ถูกต้อง จากนั้นปรับให้เหมาะสมหากจำเป็น
4. ตรวจสอบกับการทดสอบ กรณีขอบ และอินพุตที่สมจริง

### โครงสร้างข้อมูลหลัก

- **Array / List**: รวบรวมคำสั่งพร้อมการอ่านดัชนีที่รวดเร็ว
- **แผนที่แฮช / พจนานุกรม**: จัดเก็บคีย์-ค่าพร้อมการค้นหา O(1) โดยเฉลี่ย
- **ชุด**: ค่าที่ไม่ซ้ำ มีประโยชน์สำหรับการตรวจสอบสมาชิก
- **Stack**: LIFO (เข้าหลัง ออกก่อน) ทั่วไปในการแยกวิเคราะห์และการเรียกซ้ำ
- **คิว**: FIFO (เข้าก่อน ออกก่อน) มีประโยชน์สำหรับการตั้งเวลาและ BFS
- **แผนภูมิ / กราฟ**: ความสัมพันธ์แบบลำดับชั้นและแบบเครือข่าย

### ความซับซ้อนของอัลกอริทึม (Big O)

- Big O อธิบายว่ารันไทม์หรือหน่วยความจำเพิ่มขึ้นตามขนาดอินพุต
- ค่าใช้จ่ายทั่วไป:
  - O(1): การค้นหาตามเวลาคงที่ (เช่น การเข้าถึงแผนที่แฮช)
  - O(log n): การค้นหาแบบไบนารี
  - O(n): ข้อมูลผ่านครั้งเดียว
  - O(n log n): การเรียงลำดับที่มีประสิทธิภาพ
  - O(n²): ลูปซ้อนกันบนอินพุตที่มีขนาดใกล้เคียงกัน
- ต้องการโค้ดที่ชัดเจนและบำรุงรักษาได้ เว้นแต่ว่าโปรไฟล์จะแสดงจุดคอขวด

### หลักการดีบัก

- สร้างข้อผิดพลาดอย่างน่าเชื่อถือก่อน
- ลดกรณีที่ล้มเหลวให้เหลือน้อยที่สุดเพื่อแยกสาเหตุ
- ตรวจสอบบันทึก อินพุต และสมมติฐาน
- เปลี่ยนตัวแปรทีละตัวขณะทดสอบ
- เพิ่มการทดสอบการถดถอยเพื่อไม่ให้ข้อผิดพลาดเดียวกันกลับมา

### ทดสอบปิรามิด

- **การทดสอบหน่วย**: การตรวจสอบที่รวดเร็วและมุ่งเน้นของหน่วยลอจิกขนาดเล็ก
- **การทดสอบบูรณาการ**: ตรวจสอบการโต้ตอบระหว่างโมดูล/บริการ
- **การทดสอบแบบครบวงจร**: ตรวจสอบกระแสผู้ใช้ในสภาพแวดล้อมที่สมจริง
- ชุดสมดุลมีการทดสอบหน่วยจำนวนมากและมีการทดสอบแบบ end-to-end ที่ช้าน้อยกว่า

### แนวทางปฏิบัติด้านคุณภาพโค้ด

- ใช้ชื่อที่มีความหมายและฟังก์ชันเน้นเล็กๆ
- ชอบฟังก์ชั่นล้วนๆ (ผลข้างเคียงน้อยกว่า) เมื่อใช้งานได้จริง
- ทำให้โมดูลมีความสอดคล้องและอินเทอร์เฟซที่ชัดเจน
- ใช้ลินเตอร์/ฟอร์แมตเตอร์เพื่อความสม่ำเสมอ
- ตรวจสอบรหัสเพื่อความถูกต้อง ชัดเจน และความปลอดภัย

### พื้นฐานด้านความปลอดภัยสำหรับนักพัฒนา

- ตรวจสอบและฆ่าเชื้ออินพุตภายนอก
- ใช้คำสั่งแบบกำหนดพารามิเตอร์เพื่อป้องกันการฉีด SQL
- จัดเก็บรหัสผ่านด้วยอัลกอริธึมการแฮชที่รัดกุม (เช่น Argon2, bcrypt)
- หลีกเลี่ยงการฝังความลับในซอร์สโค้ด
- ใช้สิทธิพิเศษน้อยที่สุดสำหรับข้อมูลรับรองและบริการ