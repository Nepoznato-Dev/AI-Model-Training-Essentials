# Programlama Dilleri

## Python

Python, üst düzey, yorumlanan, dinamik olarak türlenen, genel amaçlı bir programlama dilidir. Okunabilirliği vurgular ve blok ayırıcı olarak anlamlı girintileme kullanır.

### Söz dizimi temelleri

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

### Functions ve type hints

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes ve OOP

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

### Yaygın kalıplar

- Dosya G/Ç için `with open(path) as f:` kullanın.
- `%` veya `.format()` yerine f-string'leri (`f"hello {name}"`) tercih edin.
- Yalnızca veri taşıyan sınıflar için `dataclasses.dataclass` kullanın.
- Dosya yollarında `os.path` yerine `pathlib.Path` kullanın.

### Tooling

- `pip install <package>` paket kurar.
- `python -m venv .venv && source .venv/bin/activate` sanal ortam oluşturur.
- `pip freeze > requirements.txt` bağımlılıkları kaydeder.
- `pip install -r requirements.txt` bunları geri yükler.
- `pyproject.toml` modern proje yapılandırma standardıdır.

---

## JavaScript

JavaScript, web'in birincil dilidir. Tarayıcılarda ve Node.js aracılığıyla sunucularda çalışır. Dinamik olarak türlenir ve prototype tabanlıdır.

### Modern söz dizimi (ES6+)

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

### Async programlama

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

### Array methods

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM manipulation

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Tooling

- `npm init -y` bir proje başlatır.
- `npm install <package>` bağımlılık ekler.
- `npm run <script>`, `package.json` içinde tanımlı bir script'i çalıştırır.
- `node index.js` bir script'i Node.js ile çalıştırır.

---

## TypeScript

TypeScript, düz JavaScript'e derlenen, statik olarak türlenmiş bir JavaScript üst kümesidir. Tür anotasyonları, interface'ler, generics ve enums ekler.

### Type annotations

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces ve types

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

### Access modifiers kullanan sınıflar

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

### tsconfig.json essentials

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

### Tooling

- `npm install -g typescript` derleyiciyi kurar.
- `tsc` projeyi derler.
- `ts-node src/index.ts` TypeScript'i doğrudan çalıştırır.

---

## Rust

Rust, güvenlik, hız ve eşzamanlılığa odaklanan bir sistem programlama dilidir. Ownership sistemi sayesinde bellek güvenliği hatalarını derleme zamanında önler.

### Ownership ve borrowing

Rust'ta her değerin tam olarak bir sahibi vardır. Sahip kapsam dışına çıktığında değer düşürülür. Borrowing, sahipliği devretmeden referans kullanımına izin verir.

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

Mutable borrow'lar (`&mut T`), aynı anda başka borrow bulunmamasını gerektirir.

### Lifetimes

Lifetime'lar, referansların işaret ettikleri veriden daha uzun yaşamamasını garanti eder.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums ve pattern matching

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

### Error handling

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

`?` operatörü, `Result` döndüren fonksiyonların içinde hataları otomatik olarak yukarı iletir.

### Tooling (Cargo)

- `cargo new project_name` yeni proje oluşturur.
- `cargo build` derler.
- `cargo run` derler ve çalıştırır.
- `cargo test` testleri çalıştırır.
- `cargo add <crate>` `Cargo.toml` dosyasına bağımlılık ekler.
- `cargo fmt` kodu biçimlendirir. `cargo clippy` lint çalıştırır.

---

## Go

Go (Golang), sadelik ve yüksek performanslı eşzamanlı programlar için tasarlanmış, statik olarak türlenmiş derlenmiş bir dildir.

### Temeller

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Functions ve çoklu dönüş değerleri

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

Bir interface'in tüm method'larını uygulayan her tür onu karşılar — açık bir bildirim gerekmez.

### Goroutines ve channels

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

### Tooling

- `go mod init module/name` bir modül başlatır.
- `go get ./...` bağımlılıkları indirir.
- `go build ./...` derler.
- `go test ./...` testleri çalıştırır.
- `go fmt ./...` kodu biçimlendirir.
- `go vet ./...` yaygın hataları kontrol eder.

---

## C ve C++

C, düşük seviyeli, derlenmiş, prosedürel bir dildir. C++, sınıflar, şablonlar ve Standard Template Library (STL) ile C'yi genişletir.

### C temelleri

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

Bir pointer, başka bir değişkenin bellek adresini saklar. `*ptr` onu dereference eder; `&var` adres alır.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ sınıfları ve RAII

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

RAII (Resource Acquisition Is Initialization), kaynak ömürlerini nesne ömürlerine bağlar; böylece temizlik işlemi destructor'larda otomatik gerçekleşir.

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

### Modern C++ (C++17 / C++20) öne çıkanlar

- `auto` tür çıkarımı.
- Range-based `for` döngüleri: `for (auto& item : container)`.
- Smart pointer'lar: `std::unique_ptr`, `std::shared_ptr` — ham `new`/`delete` kullanımından kaçının.
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilation

- `gcc main.c -o main` C kodunu derler.
- `g++ -std=c++20 -Wall main.cpp -o main` C++ kodunu derler.
- `make`, `Makefile` aracılığıyla çok dosyalı derlemeyi otomatikleştirir.
- `cmake`, daha büyük projeler için standart build-system generator aracıdır.

---

## Swift

Swift, Apple tarafından iOS, macOS, watchOS ve tvOS için geliştirilmiş modern, statik olarak türlenmiş bir programlama dilidir. Linux'ta da kullanılabilir.

### Temeller

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Optional (`T?`), var olabilen ya da olmayabilen bir değeri temsil eder.

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

### Functions ve closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classes ve structs

Swift'te hem sınıflar (reference types) hem de struct'lar (value types) vardır. Basit veri modelleri için struct tercih edilir.

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

### SwiftUI temelleri

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

### Tooling

- `swift build` bir Swift Package Manager projesini derler.
- `swift run` projeyi çalıştırır.
- `swift test` testleri çalıştırır.
- `swift package init --type executable` yeni bir çalıştırılabilir proje oluşturur.
- Xcode, Apple platformu geliştirme için birincil IDE'dir.

---

## Programlama Temelleri (Dilden Bağımsız)

### Problem çözme iş akışı

1. Kod yazmadan önce girdiyi, çıktıyı ve kısıtları tanımlayın.
2. Görevi daha küçük alt problemlere bölün.
3. Önce basit ve doğru bir çözümle başlayın, gerekirse sonra optimize edin.
4. Testler, uç durumlar ve gerçekçi girdilerle doğrulayın.

### Temel veri yapıları

- **Array / List**: Hızlı indeksli okuma sunan sıralı koleksiyon.
- **Hash map / Dictionary**: Ortalama O(1) erişime sahip anahtar-değer deposu.
- **Set**: Benzersiz değerler içerir, üyelik kontrolünde kullanışlıdır.
- **Stack**: LIFO (last in, first out), parsing ve recursion'da yaygındır.
- **Queue**: FIFO (first in, first out), zamanlama ve BFS için kullanışlıdır.
- **Tree / Graph**: Hiyerarşik ve ağ benzeri ilişkileri temsil eder.

### Algoritmik karmaşıklık (Big O)

- Big O, çalışma süresi veya belleğin girdi boyutuyla nasıl büyüdüğünü açıklar.
- Tipik maliyetler:
  - O(1): sabit zamanlı erişim (ör. hash map erişimi).
  - O(log n): binary search.
  - O(n): veri üzerinde tek geçiş.
  - O(n log n): verimli sıralama.
  - O(n²): benzer boyutlu girdiler üzerinde iç içe döngüler.
- Profiling bir darboğaz göstermedikçe açık ve sürdürülebilir kodu tercih edin.

### Debugging ilkeleri

- Önce hatayı güvenilir biçimde yeniden üretin.
- Nedeni izole etmek için başarısız örneği küçültün.
- Günlükleri, girdileri ve varsayımları inceleyin.
- Test ederken aynı anda yalnızca bir değişkeni değiştirin.
- Aynı hatanın geri dönmemesi için regression test ekleyin.

### Testing pyramid

- **Unit tests**: Küçük mantık birimlerini hızlı ve odaklı biçimde kontrol eder.
- **Integration tests**: Modüller/hizmetler arası etkileşimi doğrular.
- **End-to-end tests**: Gerçekçi ortamlarda kullanıcı akışlarını doğrular.
- Dengeli bir test paketi çok sayıda unit test ve daha az sayıda yavaş end-to-end test içerir.

### Kod kalitesi uygulamaları

- Anlamlı adlar ve küçük, odaklı fonksiyonlar kullanın.
- Mümkün olduğunda pure function'ları (daha az yan etki) tercih edin.
- Modülleri uyumlu, interface'leri açık tutun.
- Tutarlılık için linter/formatter kullanın.
- Kodu doğruluk, açıklık ve güvenlik açısından gözden geçirin.

### Geliştiriciler için temel güvenlik

- Dış girdileri doğrulayın ve sanitize edin.
- SQL injection'ı önlemek için parameterized query kullanın.
- Parolaları güçlü hashing algoritmalarıyla saklayın (ör. Argon2, bcrypt).
- Kaynak koda secret gömmekten kaçının.
- Kimlik bilgileri ve hizmetlerde least privilege uygulayın.
