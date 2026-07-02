# لغات البرمجة

## Python

Python هي لغة برمجة عالية المستوى، مفسَّرة، ذات أنواع ديناميكية، وعامة الأغراض. تركّز على قابلية القراءة وتستخدم المسافات البادئة ذات الدلالة كمحددات للكتل.

### أساسيات الصياغة

```python
# المتغيرات والأنواع
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# العبارات الشرطية
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

### الأصناف والبرمجة كائنية التوجه

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

- استخدم `with open(path) as f:` لإدخال/إخراج الملفات.
- فضّل f-strings (`f"hello {name}"`) على `%` أو `.format()`.
- استخدم `dataclasses.dataclass` للأصناف المخصّصة للبيانات فقط.
- استخدم `pathlib.Path` بدلاً من `os.path` لمسارات الملفات.

### الأدوات

- `pip install <package>` يثبّت الحزم.
- `python -m venv .venv && source .venv/bin/activate` ينشئ بيئة افتراضية.
- `pip freeze > requirements.txt` يحفظ التبعيات.
- `pip install -r requirements.txt` يستعيدها.
- `pyproject.toml` هو المعيار الحديث لإعدادات المشروع.

---

## JavaScript

JavaScript هي اللغة الأساسية للويب. تعمل في المتصفحات وعلى الخوادم عبر Node.js. وهي ذات أنواع ديناميكية وقائمة على النماذج الأولية.

### الصياغة الحديثة (ES6+)

```javascript
// تعريفات المتغيرات
const PI = 3.14159;
let counter = 0;

// الدوال السهمية
const add = (a, b) => a + b;

// القوالب النصية
const greet = name => `Hello, ${name}!`;

// التفكيك
const { x, y } = point;
const [first, ...rest] = array;

// النشر
const merged = { ...defaults, ...overrides };
```

### البرمجة غير المتزامنة

```javascript
// الوعود
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

### أساليب المصفوفات

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

- `npm init -y` يهيّئ مشروعًا.
- `npm install <package>` يضيف تبعية.
- `npm run <script>` يشغّل نصًا برمجيًا معرّفًا في `package.json`.
- `node index.js` يشغّل نصًا برمجيًا باستخدام Node.js.

---

## TypeScript

TypeScript هي مجموعة شاملة ذات أنواع ثابتة من JavaScript تُصرَّف إلى JavaScript عادية. تضيف تعليقات الأنواع والواجهات والأنواع العامة والتعدادات.

### تعليقات الأنواع

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
  email?: string;   // خاصية اختيارية
}

type Status = "active" | "inactive" | "banned";
```

### الأنواع العامة

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### الأصناف مع محددات الوصول

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

### أساسيات `tsconfig.json`

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

- `npm install -g typescript` يثبّت المصرّف.
- `tsc` يصرّف المشروع.
- `ts-node src/index.ts` يشغّل TypeScript مباشرة.

---

## Rust

Rust هي لغة برمجة نظم تركّز على السلامة والسرعة والتزامن. تمنع أخطاء سلامة الذاكرة وقت التصريف عبر نظام الملكية الخاص بها.

### الملكية والاستعارة

كل قيمة في Rust لها مالك واحد بالضبط. عندما يخرج المالك من النطاق تُحذف القيمة. تسمح الاستعارة بالمراجع دون نقل الملكية.

```rust
fn main() {
    let s = String::from("hello");  // s يملك السلسلة النصية
    let len = calculate_length(&s); // استعارة s
    println!("{} has length {}", s, len); // لا يزال s صالحًا
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

تتطلب الاستعارات القابلة للتغيير (`&mut T`) ألّا توجد أي استعارات أخرى في الوقت نفسه.

### الأعمار

تضمن الأعمار ألّا تعيش المراجع مدة أطول من البيانات التي تشير إليها.

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

يقوم العامل `?` بتمرير الأخطاء تلقائيًا داخل الدوال التي تعيد `Result`.

### الأدوات (Cargo)

- `cargo new project_name` ينشئ مشروعًا جديدًا.
- `cargo build` يصرّف.
- `cargo run` يصرّف ويشغّل.
- `cargo test` يشغّل الاختبارات.
- `cargo add <crate>` يضيف تبعية إلى `Cargo.toml`.
- `cargo fmt` ينسّق الشيفرة. و`cargo clippy` يفحصها.

---

## Go

Go (Golang) هي لغة ذات أنواع ثابتة ومصرَّفة صُممت للبساطة ولبرامج التزامن عالية الأداء.

### الأساسيات

```go
package main

import "fmt"

func main() {
    name := "world"          // تعريف مختصر لمتغير
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

### الواجهات

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

أي نوع يطبّق جميع أساليب الواجهة يحققها — ولا حاجة إلى تصريح صريح.

### الروتينات الخفيفة والقنوات

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

### `defer`

```go
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()   // يُنفَّذ عند عودة الدالة
    // … عالج f …
    return nil
}
```

### الأدوات

- `go mod init module/name` يهيّئ وحدة.
- `go get ./...` ينزّل التبعيات.
- `go build ./...` يصرّف.
- `go test ./...` يشغّل الاختبارات.
- `go fmt ./...` ينسّق الشيفرة.
- `go vet ./...` يتحقق من الأخطاء الشائعة.

---

## C و C++

C هي لغة منخفضة المستوى، مصرَّفة، وإجرائية. وتوسّع C++ لغة C بإضافة الأصناف والقوالب ومكتبة القوالب القياسية (STL).

### أساسيات C

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* ذاكرة ديناميكية */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* حرّر دائمًا ما خصصته بـ malloc */

    return 0;
}
```

### المؤشرات

يخزن المؤشر عنوان الذاكرة لمتغير آخر. يقوم `*ptr` بفك الإشارة إليه؛ ويأخذ `&var` عنوانًا.

```c
int a = 10;
int *p = &a;
*p = 20;   /* أصبحت a الآن 20 */
```

### أصناف C++ و RAII

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

يربط RAII ‏(Resource Acquisition Is Initialization) أعمار الموارد بأعمار الكائنات، مما يضمن حدوث التنظيف تلقائيًا في المهدّمات.

### حاويات STL

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

### أبرز ميزات C++ الحديثة (C++17 / C++20)

- استنتاج النوع باستخدام `auto`.
- حلقات `for` المعتمدة على النطاق: `for (auto& item : container)`.
- المؤشرات الذكية: `std::unique_ptr` و`std::shared_ptr` — تجنب `new`/`delete` الخامّين.
- الربط البنيوي: `auto [key, val] = pair;`.
- `std::optional` و`std::variant` و`std::string_view`.

### التصريف

- `gcc main.c -o main` يصرّف C.
- `g++ -std=c++20 -Wall main.cpp -o main` يصرّف C++.
- `make` يؤتمت البنى متعددة الملفات عبر `Makefile`.
- `cmake` هو مولّد أنظمة البناء القياسي للمشاريع الأكبر.

---

## Swift

Swift هي لغة برمجة حديثة ذات أنواع ثابتة طورتها Apple لأنظمة iOS وmacOS وwatchOS وtvOS. وهي متاحة أيضًا على Linux.

### الأساسيات

```swift
let greeting = "Hello, world!"   // ثابت (غير قابل للتغيير)
var counter  = 0                  // متغير (قابل للتغيير)
counter += 1

let pi: Double = 3.14159
```

### القيم الاختيارية

تمثل القيمة الاختيارية (`T?`) قيمة قد تكون موجودة أو غير موجودة.

```swift
var name: String? = nil
name = "Alice"

// فكّ آمن
if let n = name {
    print("Hello, \(n)")
}

// الدمج مع nil
let display = name ?? "Guest"

// التسلسل الاختياري
let length = name?.count
```

### الدوال والإغلاقات

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### الأصناف والبُنى

تحتوي Swift على كلٍّ من الأصناف (أنواع مرجعية) والبُنى (أنواع قيمية). فضّل البُنى لنماذج البيانات البسيطة.

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

### البروتوكولات

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### `Codable` ‏(ترميز / فك ترميز JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### أساسيات SwiftUI

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

- `swift build` يصرّف مشروع Swift Package Manager.
- `swift run` يشغّل المشروع.
- `swift test` يشغّل الاختبارات.
- `swift package init --type executable` ينشئ مشروعًا تنفيذيًا جديدًا.
- Xcode هو بيئة التطوير المتكاملة الأساسية لتطوير منصات Apple.

---

## أساسيات البرمجة (غير مرتبطة بلغة معينة)

### سير عمل حل المشكلات

1. حدّد المدخلات والمخرجات والقيود قبل كتابة الشيفرة.
2. قسّم المهمة إلى مشكلات فرعية أصغر.
3. ابدأ بحل بسيط وصحيح، ثم حسّنه إذا لزم الأمر.
4. تحقّق باستخدام الاختبارات والحالات الطرفية والمدخلات الواقعية.

### هياكل البيانات الأساسية

- **Array / List**: مجموعة مرتبة مع قراءات مفهرسة سريعة.
- **Hash map / Dictionary**: مخزن مفاتيح-قيم بمتوسط بحث O(1).
- **Set**: قيم فريدة، مفيدة للتحقق من العضوية.
- **Stack**: ‏LIFO ‏(الأخير دخولًا، الأول خروجًا)، شائع في التحليل والتكرار الذاتي.
- **Queue**: ‏FIFO ‏(الأول دخولًا، الأول خروجًا)، مفيدة للجدولة وBFS.
- **Tree / Graph**: علاقات هرمية وعلاقات على نمط الشبكات.

### التعقيد الخوارزمي (Big O)

- يصف Big O كيف يزداد زمن التنفيذ أو الذاكرة مع حجم المدخلات.
- التكاليف المعتادة:
  - O(1): بحث بزمن ثابت (مثل الوصول إلى hash map).
  - O(log n): البحث الثنائي.
  - O(n): مرور واحد عبر البيانات.
  - O(n log n): فرز فعّال.
  - O(n²): حلقات متداخلة على مدخلات متقاربة الحجم.
- فضّل الشيفرة الواضحة والقابلة للصيانة ما لم يُظهر التحليل وجود عنق زجاجة.

### مبادئ التنقيح

- أعد إنتاج الخطأ بشكل موثوق أولًا.
- قلّل الحالة الفاشلة لعزل السبب.
- افحص السجلات والمدخلات والافتراضات.
- غيّر متغيرًا واحدًا في كل مرة أثناء الاختبار.
- أضف اختبارات انحدار حتى لا يعود الخطأ نفسه.

### هرم الاختبار

- **اختبارات الوحدة**: فحوصات سريعة ومركزة لوحدات منطقية صغيرة.
- **اختبارات التكامل**: تتحقق من التفاعلات عبر الوحدات/الخدمات.
- **اختبارات الطرف إلى الطرف**: تتحقق من تدفقات المستخدم في بيئات واقعية.
- تتضمن المجموعة المتوازنة الكثير من اختبارات الوحدة وعددًا أقل من اختبارات الطرف إلى الطرف البطيئة.

### ممارسات جودة الشيفرة

- استخدم أسماء ذات معنى ودوال صغيرة ومركزة.
- فضّل الدوال النقية (ذات الآثار الجانبية الأقل) عندما يكون ذلك عمليًا.
- حافظ على تماسك الوحدات ووضوح الواجهات.
- استخدم أدوات linting/formatting لتحقيق الاتساق.
- راجع الشيفرة من أجل الصحة والوضوح والأمان.

### أساسيات الأمان للمطورين

- تحقّق من المدخلات الخارجية ونظّفها.
- استخدم الاستعلامات المعلمّة لمنع حقن SQL.
- خزّن كلمات المرور باستخدام خوارزميات تجزئة قوية (مثل Argon2 وbcrypt).
- تجنب تضمين الأسرار في الشيفرة المصدرية.
- طبّق مبدأ أقل الصلاحيات على بيانات الاعتماد والخدمات.
