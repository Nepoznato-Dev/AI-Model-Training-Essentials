# Kodlama Dilleri

## Python

Python, yüksek seviyeli, yorumlanan, dinamik tipli ve genel amaçlı bir programlama dilidir. Okunabilirliğe önem verir ve blok sınırlarını belirlemek için anlamlı girintileme kullanır.

### Sözdizimi temelleri

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

### Fonksiyonlar ve tür ipuçları

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Liste üretimleri

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Sınıflar ve nesne yönelimli programlama

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

- Dosya G/Ç işlemleri için `with open(path) as f:` kullanın.
- `%` veya `.format()` yerine f-string'leri (`f"hello {name}"`) tercih edin.
- Yalnızca veri taşıyan sınıflar için `dataclasses.dataclass` kullanın.
- Dosya yollarında `os.path` yerine `pathlib.Path` kullanın.

### Araçlar

- `pip install <package>` paket kurar.
- `python -m venv .venv && source .venv/bin/activate` bir sanal ortam oluşturur.
- `pip freeze > requirements.txt` bağımlılıkları kaydeder.
- `pip install -r requirements.txt` bunları yeniden kurar.
- `pyproject.toml`, modern proje yapılandırmasının standart dosyasıdır.

---

## JavaScript

JavaScript, web'in temel dilidir. Tarayıcılarda ve Node.js aracılığıyla sunucularda çalışır. Dinamik tipli ve prototip tabanlıdır.

### Modern sözdizimi (ES6+)

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

### Asenkron programlama

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

### Dizi metotları

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM manipülasyonu

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Araçlar

- `npm init -y` bir proje başlatır.
- `npm install <package>` bir bağımlılık ekler.
- `npm run <script>`, `package.json` içinde tanımlı bir betiği çalıştırır.
- `node index.js`, bir betiği Node.js ile çalıştırır.

---

## TypeScript

TypeScript, düz JavaScript'e derlenen, statik tipli bir JavaScript üst kümesidir. Tür ek açıklamaları, arayüzler, generic yapılar ve enum'lar ekler.

### Tür ek açıklamaları

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Arayüzler ve türler

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Generic yapılar

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Erişim belirleyicili sınıflar

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

### tsconfig.json temel ayarları

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

### Araçlar

- `npm install -g typescript` derleyiciyi kurar.
- `tsc` projeyi derler.
- `ts-node src/index.ts` TypeScript'i doğrudan çalıştırır.

---

## Rust

Rust, güvenlik, hız ve eşzamanlılık odaklı bir sistem programlama dilidir. Sahiplik sistemi sayesinde bellek güvenliği hatalarını derleme zamanında önler.

### Sahiplik ve ödünç alma

Rust'ta her değerin tam olarak bir sahibi vardır. Sahibi kapsam dışına çıktığında değer düşürülür. Ödünç alma, sahipliği devretmeden başvuru kullanmayı sağlar.

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

Değiştirilebilir ödünçler (`&mut T`), aynı anda başka hiçbir ödüncün bulunmamasını gerektirir.

### Yaşam süreleri

Yaşam süreleri, başvuruların işaret ettikleri veriden daha uzun yaşamamasını garanti eder.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enum'lar ve desen eşleme

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

### Hata yönetimi

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

`?` işleci, `Result` döndüren fonksiyonlarda hataları otomatik olarak yukarı taşır.

### Araçlar (Cargo)

- `cargo new project_name` yeni bir proje oluşturur.
- `cargo build` derler.
- `cargo run` derler ve çalıştırır.
- `cargo test` testleri çalıştırır.
- `cargo add <crate>`, `Cargo.toml` dosyasına bir bağımlılık ekler.
- `cargo fmt` kodu biçimlendirir. `cargo clippy` lint denetimi yapar.

---

## Go

Go (Golang), sadelik ve yüksek performanslı eşzamanlı programlar için tasarlanmış, statik tipli ve derlenen bir dildir.

### Temeller

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Fonksiyonlar ve çoklu dönüş değerleri

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Arayüzler

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Bir arayüzün tüm metotlarını uygulayan herhangi bir tür, bunu karşılar; ayrıca açık bir bildirim gerekmez.

### Goroutine'ler ve kanallar

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

### Araçlar

- `go mod init module/name` bir modül başlatır.
- `go get ./...` bağımlılıkları indirir.
- `go build ./...` derler.
- `go test ./...` testleri çalıştırır.
- `go fmt ./...` kodu biçimlendirir.
- `go vet ./...` yaygın hataları denetler.

---

## C ve C++

C, düşük seviyeli, derlenen ve prosedürel bir dildir. C++, sınıflar, şablonlar ve Standard Template Library (STL) ile C'yi genişletir.

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

### İşaretçiler

Bir işaretçi, başka bir değişkenin bellek adresini saklar. `*ptr` onu çözümler; `&var` ise adresini alır.

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

RAII (Resource Acquisition Is Initialization), kaynak ömürlerini nesne ömürlerine bağlayarak temizliğin yıkıcılarda otomatik yapılmasını sağlar.

### STL kapsayıcıları

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
- Aralık tabanlı `for` döngüleri: `for (auto& item : container)`.
- Akıllı işaretçiler: `std::unique_ptr`, `std::shared_ptr` — ham `new`/`delete` kullanımından kaçının.
- Yapısal bağlama: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Derleme

- `gcc main.c -o main` C kodunu derler.
- `g++ -std=c++20 -Wall main.cpp -o main` C++ kodunu derler.
- `make`, `Makefile` üzerinden çok dosyalı derlemeleri otomatikleştirir.
- `cmake`, daha büyük projeler için standart derleme sistemi üreticisidir.

---

## Swift

Swift, Apple tarafından iOS, macOS, watchOS ve tvOS için geliştirilmiş, modern ve statik tipli bir programlama dilidir. Linux üzerinde de kullanılabilir.

### Temeller

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Optional (`T?`), bir değerin var olabileceğini de olmayabileceğini de ifade eder.

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

### Fonksiyonlar ve closure'lar

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Sınıflar ve struct'lar

Swift'te hem sınıflar (başvuru türleri) hem de struct'lar (değer türleri) vardır. Basit veri modellerinde struct'ları tercih edin.

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

### Protokoller

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable (JSON kodlama / çözme)

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

### Araçlar

- `swift build` bir Swift Package Manager projesini derler.
- `swift run` projeyi çalıştırır.
- `swift test` testleri çalıştırır.
- `swift package init --type executable` yeni bir çalıştırılabilir proje oluşturur.
- Apple platformu geliştirmede temel IDE Xcode'dur.

---

## Kodlama Temelleri (Dilden Bağımsız)

### Problem çözme iş akışı

1. Kod yazmadan önce girdiyi, çıktıyı ve kısıtları tanımlayın.
2. Görevi daha küçük alt problemlere bölün.
3. Önce basit ve doğru bir çözümle başlayın, gerekirse sonra optimize edin.
4. Testler, uç durumlar ve gerçekçi girdilerle doğrulayın.

### Temel veri yapıları

- **Array / List**: hızlı indeksli okuma sunan sıralı koleksiyon.
- **Hash map / Dictionary**: ortalama O(1) erişim sağlayan anahtar-değer deposu.
- **Set**: üyelik kontrolleri için yararlı olan benzersiz değerler.
- **Stack**: LIFO (son giren ilk çıkar), ayrıştırma ve özyinelemede yaygındır.
- **Queue**: FIFO (ilk giren ilk çıkar), zamanlama ve BFS için kullanışlıdır.
- **Tree / Graph**: hiyerarşik ve ağ benzeri ilişkiler.

### Algoritmik karmaşıklık (Big O)

- Big O, çalışma süresinin veya bellek kullanımının girdi boyutuyla nasıl büyüdüğünü açıklar.
- Tipik maliyetler:
  - O(1): sabit zamanlı erişim (ör. hash map erişimi).
  - O(log n): ikili arama.
  - O(n): veri üzerinde tek geçiş.
  - O(n log n): verimli sıralama.
  - O(n²): benzer boyutlu girdiler üzerinde iç içe döngüler.
- Profiling bir darboğaz göstermedikçe açık ve bakımı kolay kodu tercih edin.

### Hata ayıklama ilkeleri

- Önce hatayı güvenilir biçimde yeniden üretin.
- Nedeni izole etmek için başarısız olan durumu küçültün.
- Günlükleri, girdileri ve varsayımları inceleyin.
- Test ederken aynı anda yalnızca tek bir değişkeni değiştirin.
- Aynı hatanın geri dönmemesi için regresyon testleri ekleyin.

### Test piramidi

- **Birim testleri**: küçük mantık birimlerini hızlı ve odaklı biçimde doğrular.
- **Entegrasyon testleri**: modüller veya servisler arasındaki etkileşimleri doğrular.
- **Uçtan uca testler**: kullanıcı akışlarını gerçekçi ortamlarda doğrular.
- Dengeli bir test paketi çok sayıda birim testi ve daha az sayıda yavaş uçtan uca test içerir.

### Kod kalitesi uygulamaları

- Anlamlı adlar ve küçük, odaklı fonksiyonlar kullanın.
- Uygun olduğunda saf fonksiyonları (daha az yan etki) tercih edin.
- Modülleri tutarlı, arayüzleri açık tutun.
- Tutarlılık için linter ve formatter kullanın.
- Kodu doğruluk, açıklık ve güvenlik açısından gözden geçirin.

### Geliştiriciler için güvenlik temelleri

- Dış girdileri doğrulayın ve temizleyin.
- SQL injection'ı önlemek için parametreli sorgular kullanın.
- Parolaları güçlü karma algoritmalarıyla (ör. Argon2, bcrypt) saklayın.
- Gizli bilgileri kaynak koda gömmekten kaçının.
- Kimlik bilgileri ve servislerde en az ayrıcalık ilkesini uygulayın.
