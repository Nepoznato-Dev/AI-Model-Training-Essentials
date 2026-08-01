<!-- 
This file was automatically translated from English to Arabic.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# لغات البرمجة

## Python

Python لغة برمجة عالية المستوى، مفسَّرة، ديناميكية الأنواع، وعامة الاستخدام. تركّز على قابلية القراءة وتستخدم المسافات البادئة ذات الدلالة لتحديد كتل التعليمات.

### أساسيات بناء الجملة

```python
# المتغيرات والأنواع
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# الشروط
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# الحلقات
for i in range(5):
    print(i)

while active:
    active = False
```

### الدوال وتلميحات الأنواع

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### استيعابات القوائم

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### الفئات والبرمجة كائنية التوجه (OOP)

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

### أنماط شائعة

- استخدم `with open(path) as f:` للتعامل مع إدخال/إخراج الملفات.
- فضّل f-strings مثل (`f"hello {name}"`) على `%` أو `.format()`.
- استخدم `dataclasses.dataclass` للفئات التي تقتصر على البيانات.
- استخدم `pathlib.Path` بدلًا من `os.path` لمسارات الملفات.

### الأدوات

- يثبّت `pip install <package>` الحزم.
- ينشئ `python -m venv .venv && source .venv/bin/activate` بيئة افتراضية.
- يحفظ `pip freeze > requirements.txt` الاعتماديات.
- يستعيدها `pip install -r requirements.txt`.
- يُعد `pyproject.toml` المعيار الحديث لضبط إعدادات المشروع.

---

## JavaScript

JavaScript هي اللغة الأساسية للويب. تعمل في المتصفحات وعلى الخوادم عبر Node.js، وهي ديناميكية الأنواع وقائمة على النماذج الأولية.

### بناء الجملة الحديث (ES6+)

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

### البرمجة غير المتزامنة

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

### دوال المصفوفات

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### التعامل مع DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### الأدوات

- `npm init -y` initialises a project.
- `npm install <package>` adds a dependency.
- `npm run <script>` runs a script defined في `package.json`.
- `node index.js` runs a script مع Node.js.

---

## TypeScript

TypeScript هي امتداد لـ JavaScript يضيف الأنواع الثابتة ويُصرَّف إلى JavaScript عادية. تضيف تلميحات الأنواع والواجهات والأنواع العامة والتعدادات.

### تلميحات الأنواع

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### الواجهات والأنواع

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Generics

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### الفئات مع معدِّلات الوصول

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

### أساسيات tsconfig.json

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

### الأدوات

- `npm install -g typescript` installs المصرّف.
- `tsc` compiles المشروع.
- `ts-node src/index.ts` runs TypeScript directly.

---

## Rust

Rust لغة برمجة أنظمة تركز على الأمان والسرعة والتزامن. تمنع أخطاء سلامة الذاكرة وقت التصريف عبر نظام الملكية الخاص بها.

### الملكية والاستعارة

لكل قيمة في Rust مالك واحد فقط. عندما يخرج المالك من النطاق تُحرَّر القيمة. تتيح الاستعارة استخدام المراجع من دون نقل الملكية.

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

تتطلب الاستعارات القابلة للتغيير (`&mut T`) ألا توجد استعارات أخرى في الوقت نفسه.

### Lifetimes

تضمن فترات الحياة ألا تعيش المراجع مدة أطول من البيانات التي تشير إليها.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### التعدادات ومطابقة الأنماط

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

### معالجة الأخطاء

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

ينشر المعامل `?` الأخطاء تلقائيًا داخل الدوال التي تُرجع `Result`.

### الأدوات (Cargo)

- `cargo new project_name` creates a new project.
- `cargo build` compiles.
- `cargo run` compiles وruns.
- `cargo test` runs tests.
- `cargo add <crate>` adds a dependency to `Cargo.toml`.
- `cargo fmt` formats code. `cargo clippy` lints.

---

## Go

Go (Golang) لغة مصرَّفة ثابتة الأنواع صُممت للبساطة وبناء برامج متزامنة عالية الأداء.

### الأساسيات

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### الدوال وقيم الإرجاع المتعددة

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Interfaces

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

أي نوع يطبّق جميع دوال واجهة ما يُعد مستوفيًا لها؛ ولا حاجة إلى تصريح صريح.

### Goroutines والقنوات

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

### الأدوات

- `go mod init module/name` initialises a module.
- `go get ./...` downloads dependencies.
- `go build ./...` compiles.
- `go test ./...` runs tests.
- `go fmt ./...` formats code.
- `go vet ./...` checks لـcommon mistakes.

---

## C وC++

C لغة إجرائية منخفضة المستوى ومصرَّفة. توسّع C++ لغة C بإضافة الفئات والقوالب وStandard Template Library (STL).

### أساسيات C

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

### Pointers

يخزّن المؤشر عنوان الذاكرة لمتغير آخر. يفك `*ptr` الإشارة إلى القيمة، بينما يأخذ `&var` العنوان.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### فئات C++ وRAII

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

يربط مبدأ RAII (Resource Acquisition Is Initialization) عمر الموارد بعمر الكائنات، ما يضمن تنفيذ التنظيف تلقائيًا في المدمّرات.

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

### Modern C++ (C++17 / C++20) highlights

- `auto` type deduction.
- Range-based `لأجل` loops: `لأجل (auto& item : container)`.
- Smart pointers: `std::unique_ptr`, `std::shared_ptr` — avoid raw `new`/`delete`.
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### التصريف

- `gcc main.c -o main` compiles C.
- `g++ -std=c++20 -Wall main.cpp -o main` compiles C++.
- `make` automates multi-file builds via a `Makefile`.
- `cmake` is المعيار build-system generator لـlarger projects.

---

## Swift

Swift لغة برمجة حديثة ثابتة الأنواع طورتها Apple لـiOS وmacOS وwatchOS وtvOS. وهي متاحة أيضًا على Linux.

### الأساسيات

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

يمثل النوع الاختياري (`T?`) قيمة قد تكون موجودة أو غير موجودة.

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

### الدوال والإغلاقات

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### الفئات والتراكيب

تدعم Swift كلًا من الفئات (أنواع مرجعية) والتراكيب (أنواع قيمية). يُفضَّل استخدام التراكيب لنماذج البيانات البسيطة.

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

### Protocols

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

### SwiftUI الأساسيات

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

### الأدوات

- `swift build` compiles a Swift Package Manager project.
- `swift run` runs المشروع.
- `swift test` runs tests.
- `swift package init --type executable` creates a new executable project.
- Xcode هو بيئة التطوير المتكاملة الأساسية لتطوير منصات Apple.

---

## أساسيات البرمجة (مستقلة عن اللغة)

### سير عمل حل المشكلات

1. حدّد المدخلات والمخرجات والقيود قبل كتابة الكود.
2. قسّم المهمة إلى مشكلات فرعية أصغر.
3. ابدأ بحل بسيط وصحيح، ثم حسّنه عند الحاجة.
4. تحقّق باستخدام الاختبارات والحالات الطرفية والمدخلات الواقعية.

### هياكل البيانات الأساسية

- **Array / List**: مجموعة مرتبة تتيح قراءة سريعة عبر الفهارس.
- **Hash map / Dictionary**: مخزن أزواج مفتاح-قيمة بمتوسط بحث O(1).
- **Set**: قيم فريدة، مفيدة لاختبارات العضوية.
- **Stack**: بنية LIFO (الأخير دخولًا هو الأول خروجًا)، شائعة في التحليل والاستدعاء الذاتي.
- **Queue**: بنية FIFO (الأول دخولًا هو الأول خروجًا)، مفيدة للجدولة وBFS.
- **Tree / Graph**: علاقات هرمية أو شبكية.

### التعقيد الخوارزمي (Big O)

- تصف Big O كيفية نمو زمن التنفيذ أو استهلاك الذاكرة مع حجم المدخلات.
- التكاليف الشائعة:
  - O(1): بحث بزمن ثابت، مثل الوصول إلى Hash map.
  - O(log n): البحث الثنائي.
  - O(n): مرور واحد على البيانات.
  - O(n log n): فرز فعّال.
  - O(n²): حلقات متداخلة على مدخلات متقاربة الحجم.
- فضّل الكود الواضح والقابل للصيانة ما لم يُظهر قياس الأداء وجود عنق زجاجة.

### مبادئ تصحيح الأخطاء

- أعد إنتاج الخطأ بشكل موثوق أولًا.
- صغّر حالة الفشل لعزل السبب.
- افحص السجلات والمدخلات والافتراضات.
- غيّر متغيرًا واحدًا في كل مرة أثناء الاختبار.
- أضف اختبارات ارتدادية حتى لا يتكرر الخطأ نفسه.

### هرم الاختبار

- **Unit tests**: فحوص سريعة ومركزة لوحدات منطقية صغيرة.
- **Integration tests**: تتحقق من التفاعلات بين الوحدات أو الخدمات.
- **End-to-end tests**: تتحقق من مسارات المستخدم في بيئات واقعية.
- تحتوي الحزمة المتوازنة على كثير من اختبارات الوحدة وعدد أقل من اختبارات end-to-end البطيئة.

### ممارسات جودة الكود

- استخدم أسماء ذات معنى ودوال صغيرة مركزة.
- Prefer pure functions (fewer side effects) when practical.
- Keep modules cohesive وinterfaces explicit.
- Use linters/formatters لـconsistency.
- Review code لـcorrectness, clarity, والأمان.

### أساسيات الأمان للمطورين

- Validate وsanitise external input.
- Use parameterised queries to prevent SQL injection.
- Store passwords مع strong hashing algorithms (e.g., Argon2, bcrypt).
- Avoid embedding secrets في source code.
- Apply least privilege لـcredentials وservices.
