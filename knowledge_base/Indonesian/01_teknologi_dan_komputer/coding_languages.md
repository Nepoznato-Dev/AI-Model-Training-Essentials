# Bahasa Pengkodean

## Piton

Python adalah bahasa pemrograman tujuan umum tingkat tinggi, ditafsirkan, diketik secara dinamis. Ini menekankan keterbacaan dan menggunakan lekukan yang signifikan sebagai pembatas blok.

### Dasar-dasar sintaksis

```python
# Variabel dan tipe
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Kondisional
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Perulangan
for i in range(5):
    print(i)

while active:
    active = False
```

### Fungsi dan petunjuk ketik

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Daftar pemahaman

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Kelas dan OOP

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

### Pola umum

- Gunakan `with open(path) as f:` untuk file I/O.
- Lebih memilih f-string (`f"hello {name}"`) daripada `%` atau `.format()`.
- Gunakan `dataclasses.dataclass` untuk kelas data saja.
- Gunakan `pathlib.Path` daripada `os.path` untuk jalur file.

### Perkakas

- `pip install <package>` menginstal paket.
- `python -m venv .venv && source .venv/bin/activate` membuat lingkungan virtual.
- `pip freeze > requirements.txt` menyimpan dependensi.
- `pip install -r requirements.txt` memulihkannya.
- `pyproject.toml` adalah standar konfigurasi proyek modern.

---

##JavaScript

JavaScript adalah bahasa utama web. Ini berjalan di browser dan di server melalui Node.js. Ini diketik secara dinamis dan berbasis prototipe.

### Sintaks modern (ES6+)

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

### Pemrograman asinkron

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

### Metode susunan

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Manipulasi DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Perkakas

- `npm init -y` menginisialisasi proyek.
- `npm install <package>` menambahkan ketergantungan.
- `npm run <script>` menjalankan skrip yang ditentukan di `package.json`.
- `node index.js` menjalankan skrip dengan Node.js.

---

## Skrip Ketik

TypeScript adalah superset JavaScript yang diketik secara statis yang dikompilasi menjadi JavaScript biasa. Itu menambahkan anotasi tipe, antarmuka, generik, dan enum.

### Ketik anotasi

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Antarmuka dan tipe

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Generik

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Kelas dengan pengubah akses

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

### tsconfig.json penting

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

### Perkakas

- `npm install -g typescript` menginstal kompiler.
- `tsc` mengkompilasi proyek.
- `ts-node src/index.ts` menjalankan TypeScript secara langsung.

---

## Karat

Rust adalah bahasa pemrograman sistem yang berfokus pada keamanan, kecepatan, dan konkurensi. Ini mencegah bug keamanan memori pada waktu kompilasi melalui sistem kepemilikannya.

### Kepemilikan dan peminjaman

Setiap nilai di Rust memiliki satu pemilik. Ketika pemilik keluar dari ruang lingkup, nilainya turun. Peminjaman memungkinkan referensi tanpa mengalihkan kepemilikan.

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

Pinjaman yang dapat diubah (`&mut T`) mengharuskan tidak ada pinjaman lain pada saat yang sama.

### Seumur hidup

Seumur hidup memastikan referensi tidak berumur lebih lama dari data yang ditunjuknya.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enum dan pencocokan pola

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

### Penanganan kesalahan

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

Operator `?` menyebarkan kesalahan secara otomatis di dalam fungsi yang mengembalikan `Result`.

### Perkakas (Kargo)

- `cargo new project_name` membuat proyek baru.
- `cargo build` dikompilasi.
- `cargo run` dikompilasi dan dijalankan.
- `cargo test` menjalankan pengujian.
- `cargo add <crate>` menambahkan ketergantungan ke `Cargo.toml`.
- `cargo fmt` memformat kode. `cargo clippy` serat.

---

## Pergi

Go (Golang) adalah bahasa yang dikompilasi dan diketik secara statis yang dirancang untuk kesederhanaan dan program bersamaan berkinerja tinggi.

### Dasar-dasar

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Fungsi dan beberapa nilai kembalian

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Antarmuka

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Tipe apa pun yang mengimplementasikan semua metode antarmuka akan memenuhinya — tidak diperlukan deklarasi eksplisit.

### Goroutine dan saluran

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

### Tunda

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

### Perkakas

- `go mod init module/name` menginisialisasi modul.
- `go get ./...` mengunduh dependensi.
- `go build ./...` dikompilasi.
- `go test ./...` menjalankan pengujian.
- `go fmt ./...` memformat kode.
- `go vet ./...` memeriksa kesalahan umum.

---

## C dan C++

C adalah bahasa prosedural tingkat rendah, terkompilasi. C++ memperluas C dengan kelas, templat, dan Perpustakaan Templat Standar (STL).

### Dasar-dasar C

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

### Petunjuk

Sebuah pointer menyimpan alamat memori variabel lain. `*ptr` melakukan dereferensi; `&var` mengambil alamat.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Kelas C++ dan RAII

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

RAII (Resource Acquisition Is Initialization) mengikat masa hidup sumber daya dengan masa hidup objek, memastikan pembersihan terjadi secara otomatis di destruktor.

### Kontainer STL

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

### Sorotan C++ modern (C++17 / C++20).

- `auto` ketik pengurangan.
- Loop `for` berbasis rentang: `for (auto& item : container)`.
- Petunjuk cerdas: `std::unique_ptr`, `std::shared_ptr` — hindari `new`/`delete` mentah.
- Ikatan terstruktur: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Kompilasi- `gcc main.c -o main` mengkompilasi C.
- `g++ -std=c++20 -Wall main.cpp -o main` mengkompilasi C++.
- `make` mengotomatiskan pembuatan multi-file melalui `Makefile`.
- `cmake` adalah generator sistem build standar untuk proyek yang lebih besar.

---

## Cepat

Swift adalah bahasa pemrograman modern dengan tipe statis yang dikembangkan oleh Apple untuk iOS, macOS, watchOS, dan tvOS. Ini juga tersedia di Linux.

### Dasar-dasar

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Opsional

Opsional (`T?`) mewakili nilai yang mungkin ada atau tidak ada.

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

### Fungsi dan penutupan

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Kelas dan struct

Swift memiliki kelas (tipe referensi) dan struct (tipe nilai). Lebih suka struct untuk model data sederhana.

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

### Protokol

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Dapat dikodekan (pengkodean/dekode JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Dasar-dasar SwiftUI

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

### Perkakas

- `swift build` mengkompilasi proyek Swift Package Manager.
- `swift run` menjalankan proyek.
- `swift test` menjalankan pengujian.
- `swift package init --type executable` membuat proyek baru yang dapat dieksekusi.
- Xcode adalah IDE utama untuk pengembangan platform Apple.

---

## Dasar-dasar Pengkodean (Agnostik Bahasa)

### Alur kerja pemecahan masalah

1. Tentukan input, output, dan batasan sebelum menulis kode.
2. Bagi tugas menjadi submasalah yang lebih kecil.
3. Mulailah dengan solusi sederhana yang benar, lalu optimalkan jika diperlukan.
4. Validasi dengan pengujian, kasus tepi, dan masukan realistis.

### Struktur data inti

- **Array / Daftar**: koleksi terurut dengan pembacaan terindeks cepat.
- **Peta hash / Kamus**: penyimpanan nilai kunci dengan pencarian rata-rata O(1).
- **Set**: nilai unik, berguna untuk pemeriksaan keanggotaan.
- **Stack**: LIFO (masuk terakhir, keluar pertama), umum dalam penguraian dan rekursi.
- **Antrian**: FIFO (masuk pertama, keluar pertama), berguna untuk penjadwalan dan BFS.
- **Pohon / Grafik**: hubungan hierarki dan gaya jaringan.

### Kompleksitas algoritma (O Besar)

- Big O menjelaskan bagaimana runtime atau memori bertambah seiring dengan ukuran input.
- Biaya umum:
  - O(1): pencarian waktu konstan (misalnya, akses peta hash).
  - O(log n): pencarian biner.
  - O(n): data tembus tunggal.
  - O(n log n): penyortiran yang efisien.
  - O(n²): loop bersarang pada input berukuran serupa.
- Lebih memilih kode yang jelas dan mudah dipelihara kecuali pembuatan profil menunjukkan hambatan.

### Prinsip debug

- Reproduksi bug terlebih dahulu.
- Minimalkan kasus kegagalan untuk mengisolasi penyebabnya.
- Periksa log, masukan, dan asumsi.
- Ubah satu variabel pada satu waktu saat pengujian.
- Tambahkan tes regresi sehingga bug yang sama tidak kembali.

### Menguji piramida

- **Pengujian unit**: pemeriksaan unit logika kecil yang cepat dan terfokus.
- **Tes integrasi**: memverifikasi interaksi antar modul/layanan.
- **Pengujian ujung ke ujung**: memvalidasi alur pengguna dalam lingkungan yang realistis.
- Rangkaian yang seimbang memiliki banyak pengujian unit dan lebih sedikit pengujian ujung ke ujung yang lambat.

### Praktik kualitas kode

- Gunakan nama yang bermakna dan fungsi kecil yang terfokus.
- Lebih memilih fungsi murni (lebih sedikit efek samping) bila praktis.
- Jaga agar modul tetap kohesif dan antarmuka tetap eksplisit.
- Gunakan linter/formatter untuk konsistensi.
- Tinjau kode untuk kebenaran, kejelasan, dan keamanan.

### Dasar-dasar keamanan untuk pengembang

- Validasi dan sanitasi input eksternal.
- Gunakan kueri berparameter untuk mencegah injeksi SQL.
- Simpan kata sandi dengan algoritma hashing yang kuat (mis., Argon2, bcrypt).
- Hindari menyematkan rahasia dalam kode sumber.
- Terapkan hak istimewa paling sedikit untuk kredensial dan layanan.