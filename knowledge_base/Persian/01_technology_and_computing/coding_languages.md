# زبان های کدنویسی

## پایتون

پایتون یک زبان برنامه نویسی سطح بالا، تفسیر شده، تایپ شده پویا و همه منظوره است. بر خوانایی تاکید می کند و از تورفتگی قابل توجهی به عنوان جداکننده بلوک استفاده می کند.

### اصول نحو

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

### توابع و تایپ نکات

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### مطالب را فهرست کنید

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### کلاس ها و OOP

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

### الگوهای رایج

- از `with open(path) as f:` برای ورودی/خروجی فایل استفاده کنید.
- رشته های f (`f"hello {name}"`) را به `%` یا `.format()` ترجیح دهید.
- از `dataclasses.dataclass` برای کلاس های فقط داده استفاده کنید.
- از `pathlib.Path` به جای `os.path` برای مسیرهای فایل استفاده کنید.

### ابزار

- `pip install <package>` بسته ها را نصب می کند.
- `python -m venv .venv && source .venv/bin/activate` یک محیط مجازی ایجاد می کند.
- `pip freeze > requirements.txt` وابستگی ها را ذخیره می کند.
- `pip install -r requirements.txt` آنها را بازیابی می کند.
- `pyproject.toml` استاندارد پیکربندی پروژه مدرن است.

---

## جاوا اسکریپت

جاوا اسکریپت زبان اصلی وب است. در مرورگرها و سرورها از طریق Node.js اجرا می شود. به صورت پویا تایپ شده و مبتنی بر نمونه اولیه است.

### نحو مدرن (ES6+)

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

### برنامه نویسی Async

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

### روش های آرایه

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### دستکاری DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### ابزار

- `npm init -y` یک پروژه را مقداردهی اولیه می کند.
- `npm install <package>` یک وابستگی اضافه می کند.
- `npm run <script>` یک اسکریپت تعریف شده در `package.json` را اجرا می کند.
- `node index.js` یک اسکریپت را با Node.js اجرا می کند.

---

## TypeScript

TypeScript یک ابر مجموعه جاوا اسکریپت تایپ شده است که به جاوا اسکریپت ساده کامپایل می شود. حاشیه نویسی نوع، رابط ها، ژنریک ها و فهرست ها را اضافه می کند.

### حاشیه نویسی را تایپ کنید

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### رابط ها و انواع

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### ژنریک

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### کلاس هایی با اصلاح کننده های دسترسی

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

### tsconfig.json ملزومات

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

### ابزار

- `npm install -g typescript` کامپایلر را نصب می کند.
- `tsc` پروژه را کامپایل می کند.
- `ts-node src/index.ts` TypeScript را مستقیماً اجرا می کند.

---

## زنگ زدگی

Rust یک زبان برنامه نویسی سیستمی است که بر ایمنی، سرعت و همزمانی تمرکز دارد. از طریق سیستم مالکیت خود از اشکالات ایمنی حافظه در زمان کامپایل جلوگیری می کند.

### مالکیت و قرض گرفتن

هر مقدار در Rust دقیقاً یک مالک دارد. هنگامی که مالک از محدوده خارج می شود، ارزش حذف می شود. وام گرفتن به مراجع بدون انتقال مالکیت اجازه می دهد.

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

قرض‌های قابل تغییر (<<INLINE_CODE_20>>>) مستلزم آن است که وام‌های دیگری همزمان وجود نداشته باشند.

### طول عمر

مادام‌العمر تضمین می‌کند که منابع از داده‌هایی که به آنها اشاره می‌کنند بیشتر زنده نمی‌مانند.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### شماره ها و تطبیق الگو

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

### رسیدگی به خطا

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

عملگر `?` خطاها را به طور خودکار در توابعی منتشر می کند که `Result` را برمی گرداند.

### ابزار کاری (محموله)

- `cargo new project_name` یک پروژه جدید ایجاد می کند.
- `cargo build` کامپایل می کند.
- `cargo run` کامپایل و اجرا می شود.
- `cargo test` آزمایش ها را اجرا می کند.
- `cargo add <crate>` یک وابستگی به `Cargo.toml` اضافه می کند.
- `cargo fmt` کد قالب‌ها. `cargo clippy` پرزها.

---

## برو

Go (Golang) یک زبان تایپ شده و کامپایل شده است که برای سادگی و برنامه های همزمان با کارایی بالا طراحی شده است.

### اصول

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### توابع و مقادیر چندگانه بازگشتی

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### رابط ها

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

هر نوع که تمام روش های یک رابط را پیاده سازی کند، آن را برآورده می کند - هیچ اعلان صریحی لازم نیست.

### برنامه ها و کانال ها

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

### به تعویق انداختن

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

### ابزار

- `go mod init module/name` یک ماژول را مقداردهی اولیه می کند.
- `go get ./...` وابستگی های دانلودها.
- `go build ./...` کامپایل می کند.
- `go test ./...` آزمایش ها را اجرا می کند.
- `go fmt ./...` کد قالب‌ها.
- `go vet ./...` اشتباهات رایج را بررسی می کند.

---

## C و C++

C یک زبان رویه ای، کامپایل شده و سطح پایین است. C++ C را با کلاس‌ها، قالب‌ها و کتابخانه قالب استاندارد (STL) گسترش می‌دهد.

### اصول C

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

### اشاره گر

یک اشاره گر آدرس حافظه متغیر دیگری را ذخیره می کند. `*ptr` ارجاع آن را لغو می کند. `&var` یک آدرس می گیرد.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### کلاس های C++ و RAII

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

RAII (Resource Acquisition Is Initialization) طول عمر منابع را به طول عمر اشیا مرتبط می کند، و تضمین می کند که پاکسازی به طور خودکار در تخریب کننده ها انجام می شود.

### ظروف STL

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

### C++ مدرن (C++17 / C++20).

- `auto` کسر نوع.
- حلقه های `for` مبتنی بر محدوده: `for (auto& item : container)`.
- نشانگرهای هوشمند: `std::unique_ptr`، `std::shared_ptr` — از خام `new`/<<INLINE_CODE_45>>> اجتناب کنید.
- اتصالات ساختاری: `auto [key, val] = pair;`.
- `std::optional`، `std::variant`، `std::string_view`.

### تالیف- `gcc main.c -o main` C را کامپایل می کند.
- `g++ -std=c++20 -Wall main.cpp -o main` C++ را کامپایل می کند.
- `make` ساخت های چند فایلی را از طریق `Makefile` خودکار می کند.
- `cmake` تولید کننده سیستم ساخت استاندارد برای پروژه های بزرگتر است.

---

## سویفت

Swift یک زبان برنامه نویسی مدرن و ایستا است که توسط اپل برای iOS، macOS، watchOS و tvOS توسعه یافته است. در لینوکس نیز موجود است.

### اصول

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### اختیاری

یک اختیاری (<<INLINE_CODE_55>>>) مقداری را نشان می دهد که ممکن است وجود داشته باشد یا نباشد.

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

### عملکرد و بسته شدن

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### کلاس ها و ساختارها

سوئیفت دارای هر دو کلاس (انواع مرجع) و ساختارها (انواع ارزش) است. ساختارها را برای مدل‌های داده ساده ترجیح دهید.

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

### پروتکل ها

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### قابل کدگذاری (کدگذاری / رمزگشایی JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### اصول اولیه SwiftUI

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

### ابزار

- `swift build` یک پروژه مدیریت بسته Swift را کامپایل می کند.
- `swift run` پروژه را اجرا می کند.
- `swift test` آزمایش ها را اجرا می کند.
- `swift package init --type executable` یک پروژه اجرایی جدید ایجاد می کند.
- Xcode IDE اولیه برای توسعه پلتفرم اپل است.

---

## مبانی کدگذاری (زبان-آگنوستیک)

### گردش کار حل مسئله

1. قبل از نوشتن کد ورودی، خروجی و محدودیت ها را تعریف کنید.
2. کار را به مسائل فرعی کوچکتر تقسیم کنید.
3. با یک راه حل صحیح ساده شروع کنید، سپس در صورت نیاز بهینه سازی کنید.
4. با تست‌ها، موارد لبه و ورودی‌های واقعی اعتبارسنجی کنید.

### ساختارهای داده اصلی

- ** آرایه / لیست **: مجموعه سفارش داده شده با خواندن فهرست سریع.
- ** نقشه هش / دیکشنری **: ذخیره کلید-مقدار با میانگین جستجوی O(1).
- ** مجموعه **: مقادیر منحصر به فرد، مفید برای بررسی عضویت.
- **پشته**: LIFO (آخرین ورود، اولین خروج)، رایج در تجزیه و بازگشت.
- **صف **: FIFO (اول وارد، اولین خروج)، مفید برای برنامه ریزی و BFS.
- ** درخت / نمودار **: روابط سلسله مراتبی و به سبک شبکه.

### پیچیدگی الگوریتمی (Big O)

- Big O توضیح می دهد که چگونه زمان اجرا یا حافظه با اندازه ورودی رشد می کند.
- هزینه های معمول:
  - O(1): جستجوی زمان ثابت (به عنوان مثال، دسترسی به نقشه هش).
  - O(log n): جستجوی دودویی.
  - O(n): یک گذر از طریق داده ها.
  - O(n log n): مرتب سازی کارآمد.
  - O(n²): حلقه های تو در تو روی ورودی های با اندازه مشابه.
- کد واضح و قابل نگهداری را ترجیح دهید مگر اینکه نمایه سازی یک گلوگاه را نشان دهد.

### اصول اشکال زدایی

- ابتدا اشکال را به طور قابل اعتماد بازتولید کنید.
- برای جداسازی علت، موارد شکست را به حداقل برسانید.
- گزارش ها، ورودی ها و فرضیات را بررسی کنید.
- در حین تست، یک متغیر را در یک زمان تغییر دهید.
- تست های رگرسیون را اضافه کنید تا همان باگ برنگردد.

### هرم تست

- ** تست های واحد **: بررسی سریع و متمرکز واحدهای منطقی کوچک.
- **تست های یکپارچه سازی**: بررسی تعاملات بین ماژول ها/سرویس ها.
- **تست های پایان به انتها**: جریان های کاربر را در محیط های واقعی تایید می کند.
- یک مجموعه متعادل دارای تعداد زیادی تست واحد و تست‌های آهسته کمتری است.

### شیوه های کیفیت کد

- از نام های معنی دار و توابع متمرکز کوچک استفاده کنید.
- در صورت عملی بودن، عملکردهای خالص (عوارض جانبی کمتر) را ترجیح دهید.
- ماژول ها را منسجم و رابط ها را واضح نگه دارید.
- از لینتر/فرمترها برای قوام استفاده کنید.
- کد را برای صحت، وضوح و امنیت بررسی کنید.

### اصول اولیه امنیتی برای توسعه دهندگان

- ورودی خارجی را تأیید و ضدعفونی کنید.
- از پرس و جوهای پارامتری برای جلوگیری از تزریق SQL استفاده کنید.
- رمزهای عبور را با الگوریتم های هش قوی (به عنوان مثال، Argon2، bcrypt) ذخیره کنید.
- از قرار دادن اسرار در کد منبع خودداری کنید.
- کمترین امتیاز را برای اعتبارنامه ها و خدمات اعمال کنید.