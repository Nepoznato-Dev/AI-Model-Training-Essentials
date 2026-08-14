---
# Metadata
title: "Rust"
description: "Comprehensive reference for the Rust programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [rust, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "40 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Pas
Rust, ilk olarak 2015 yılında piyasaya sürülen ve orijinal olarak Mozilla'da Graydon Hoare tarafından geliştirilen, statik olarak yazılan, derlenmiş bir programlama dilidir. Rust'ın belirleyici vaadi **çöp toplama olmadan bellek güvenliğidir**. Bunu, C veya C++ kadar hızlı kod üretirken tüm hata kategorilerini (boş işaretçi referansları, veri yarışları, arabellek taşmaları, serbest kullanım sonrası kullanım) ortadan kaldıran, derleme zamanında uygulanan bir dizi kural olan sahiplik sistemi aracılığıyla başarır.
Rust, Stack Overflow Geliştirici Anketi'nde üst üste birkaç yıl boyunca "en sevilen" programlama dili seçildi. Sistem programlamada, WebAssembly'de, CLI araçlarında, bulut altyapısında ve güvenlik açısından kritik bağlamlarda C/C++'ın yerine giderek daha fazla kullanılmaktadır. Linux çekirdeği artık Rust kodunu kabul ediyor.
---

## Pas Neden Önemlidir
- **GC'siz bellek güvenliği**: Sahiplik sistemi, derleme zamanında boş işaretçileri, veri yarışlarını ve sarkan işaretçileri sıfır çalışma süresi ek yüküyle önler.
- **Performans**: Çoğu iş yükü için C/C++ ile eşleşir veya onu aşar. Çöp toplayıcının olmaması öngörülemeyen duraklamaların olmayacağı anlamına gelir.
- **Korkusuz eşzamanlılık**: Tür sistemi, derleme zamanında veri yarışlarını önler. Derlenirse iş parçacığı açısından güvenlidir.
- **Modern araçlar**:`cargo`(derleme sistemi + paket yöneticisi) herhangi bir dildeki en iyilerden biridir. `cargo build`,`cargo test`,`cargo doc`hepsi kutudan çıktığı gibi çalışır.
- **WebAssembly**: WASM'ye derleme için birinci sınıf destek, tarayıcılarda yerele yakın performans sağlar.
- **Giderek benimseniyor**: AWS, Google (Android), Microsoft (Windows çekirdeği), Cloudflare, Discord, Dropbox ve Meta tarafından kullanılmaktadır.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Dik öğrenme eğrisi** | Mülkiyet, ödünç alma ve ömürler diğer dillerdeki hiçbir şeye benzemez | "The Rust Book"a zaman ayırın; kavramlar pratikle tıklanır |
| **Yavaş derleme** | Büyük projelerde derleme süreleri uzun olabilir | Hızlı tip kontrolü için `cargo check`'yi kullanın; artımlı derleme yardımcı olur |
| **Ayrıntılı hata işleme** | `Result<T, E>`ve`?`operatörü açık işlem gerektirir | Uygulamalar için `anyhow`'yi, kütüphaneler için `thiserror`'yi kullanın |
| **Daha küçük iş piyasası** | Java, Python veya JavaScript'ten daha az Rust işi var (ancak hızla büyüyor) | Rust rollerinin çoğu sistem programlama, kripto veya altyapı alanındadır |
| **Olgunlaşmamış ekosistem** | Bazı alan adları için Python/Java/JS'den daha az kitaplık | Ekosistem hızla büyüyor; birçok kasa mükemmel kalitededir |
---

## Söz Diziminin Temelleri
### Temel Yapı
```rust
fn main() {
    // Immutable by default
    let name = "Alice";
    let age = 30;

    // Mutable requires explicit `mut`
    let mut count = 0;
    count += 1;

    // Type annotations (optional — compiler usually infers)
    let score: f64 = 9.5;
    let active: bool = true;

    println!("Hello, {}! Age: {}, Score: {}", name, age, score);
}
```

### Mülkiyet ve Borç Alma
Bu Rust'un temel yeniliğidir. Her değerin tam olarak bir sahibi vardır. Sahibi kapsam dışına çıktığında değer düşer.
```rust
// Ownership — each value has one owner
let s1 = String::from("hello");
let s2 = s1;  // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1);  // ERROR: s1 has been moved

// Cloning — explicit deep copy
let s3 = s2.clone();
println!("{} {}", s2, s3);  // Both valid

// Borrowing — references without taking ownership
fn length(s: &String) -> usize {
    s.len()
}

let s = String::from("hello");
let len = length(&s);
println!("{} has length {}", s, len);

// Mutable borrowing (only one mutable reference at a time)
fn append_exclamation(s: &mut String) {
    s.push('!');
}

let mut greeting = String::from("hello");
append_exclamation(&mut greeting);
println!("{}", greeting);  // "hello!"
```

### Yapılar, Numaralandırmalar ve Desen Eşleştirme
```rust
struct Point {
    x: f64,
    y: f64,
}

impl Point {
    fn distance_to(&self, other: &Point) -> f64 {
        ((self.x - other.x).powi(2) + (self.y - other.y).powi(2)).sqrt()
    }
}

enum Shape {
    Circle { radius: f64 },
    Rectangle { width: f64, height: f64 },
    Triangle { base: f64, height: f64 },
}

impl Shape {
    fn area(&self) -> f64 {
        match self {
            Shape::Circle { radius } => std::f64::consts::PI * radius.powi(2),
            Shape::Rectangle { width, height } => width * height,
            Shape::Triangle { base, height } => 0.5 * base * height,
        }
    }
}

fn describe(number: i32) -> String {
    match number {
        0 => "zero".to_string(),
        1..=9 => "single digit".to_string(),
        n if n < 0 => format!("negative: {}", n),
        _ => "large positive".to_string(),
    }
}
```

### Hata İşleme
```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

match divide(10.0, 3.0) {
    Ok(result) => println!("Result: {}", result),
    Err(e) => println!("Error: {}", e),
}

// The ? operator — propagate errors concisely
fn calculate(a: f64, b: f64, c: f64) -> Result<f64, String> {
    let ab = divide(a, b)?;
    let abc = divide(ab, c)?;
    Ok(abc)
}

fn find_first_even(numbers: &[i32]) -> Option<i32> {
    numbers.iter().find(|&&n| n % 2 == 0).copied()
}
```

---

## Gelişmiş Sözdizimi ve Desenler
### Jenerikler ve Özellik Sınırları
Jenerikler, tam tür güvenliğini korurken herhangi bir türle çalışan kod yazmanıza olanak tanır. Özellikler paylaşılan davranışı tanımlar.
```rust
// Generic function with trait bound
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut max = &list[0];
    for item in &list[1..] {
        if item > max { max = item; }
    }
    max
}

// Generic struct
struct Pair<T: Clone + std::fmt::Debug> {
    first: T,
    second: T,
}

impl<T: Clone + std::fmt::Debug> Pair<T> {
    fn new(first: T, second: T) -> Self {
        Pair { first, second }
    }
    fn swap(&mut self) {
        std::mem::swap(&mut self.first, &mut self.second);
    }
}

// Trait definition with default method
trait Summary {
    fn summarize(&self) -> String;
    fn preview(&self) -> String {
        format!("{}...", &self.summarize()[..20])
    }
}

struct Article { title: String, content: String }

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}: {}", self.title, &self.content[..50])
    }
}

// where clause for complex bounds
fn compare<T, U>(a: &T, b: &U) -> String
where
    T: Summary + std::fmt::Display,
    U: Summary + std::fmt::Debug,
{
    format!("{} vs {:?}", a.summarize(), b)
}
```

### Makrolar
Rust'un iki tür makrosu vardır: bildirimsel (`macro_rules!`) ve prosedürel (türetme, nitelik, işlev benzeri).
```rust
// Declarative macro with repetition
macro_rules! hashmap {
    ( $( $key:expr => $value:expr ),* $(,)? ) => {{
        let mut map = std::collections::HashMap::new();
        $( map.insert($key, $value); )*
        map
    }};
}

let config = hashmap! {
    "host" => "localhost",
    "port" => "8080",
    "debug" => "true",
};

// Expression macro
macro_rules! vec_map {
    ($v:expr, $f:expr) => {{
        let mut result = Vec::new();
        for item in $v {
            result.push(($f)(item));
        }
        result
    }};
}

let numbers = vec![1, 2, 3, 4, 5];
let doubled = vec_map!(numbers, |x| x * 2);

// Procedural derive macro (from serde crate)
// #[derive(Serialize, Deserialize)]
// struct Config {
//     host: String,
//     port: u16,
// }
```

### Gelişmiş Desen Eşleştirme ve Yok Etme
```rust
struct Point { x: f64, y: f64 }

fn describe_point(p: &Point) -> &str {
    match p {
        Point { x: 0.0, y: 0.0 } => "origin",
        Point { x, y: 0.0 } if *x > 0.0 => "positive x-axis",
        Point { x: 0.0, y } if *y > 0.0 => "positive y-axis",
        _ => "somewhere in space",
    }
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    Color(u8, u8, u8),
}

fn process(msg: &Message) {
    match msg {
        Message::Quit => println!("Quit"),
        Message::Move { x, y } => println!("Move to ({}, {})", x, y),
        Message::Write(text) => println!("Write: {}", text),
        Message::Color(r, g, b) => println!("#{},{},{}", r, g, b),
    }
}

// if let — concise single-case matching
let config_value: Option<&str> = Some("production");
if let Some("production") = config_value {
    println!("Production mode");
}

// let-else (Rust 1.65+)
fn parse_id(input: &str) -> Option<u64> {
    let Ok(num) = input.parse::<u64>() else {
        return None;
    };
    Some(num)
}
```

### Operatör Aşırı Yüklemesi
```rust
use std::ops::{Add, Mul};

struct Vector2D { x: f64, y: f64 }

impl Add for Vector2D {
    type Output = Self;
    fn add(self, other: Self) -> Self {
        Vector2D { x: self.x + other.x, y: self.y + other.y }
    }
}

impl Mul<f64> for Vector2D {
    type Output = Self;
    fn mul(self, scalar: f64) -> Self {
        Vector2D { x: self.x * scalar, y: self.y * scalar }
    }
}

impl std::fmt::Display for Vector2D {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

let v1 = Vector2D { x: 1.0, y: 2.0 };
let v2 = Vector2D { x: 3.0, y: 4.0 };
let v3 = v1 + v2;        // Uses Add trait
let scaled = v3 * 2.0;   // Uses Mul<f64> trait
println!("{}", scaled);   // "(8, 12)"
```

### Özel Hata Hiyerarşileri
```rust
use std::fmt;

#[derive(Debug)]
enum AppError {
    Io(std::io::Error),
    Parse(std::num::ParseIntError),
    Network { status: u16, message: String },
    Validation(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::Io(e) => write!(f, "IO error: {}", e),
            AppError::Parse(e) => write!(f, "Parse error: {}", e),
            AppError::Network { status, message } =>
                write!(f, "Network error {}: {}", status, message),
            AppError::Validation(msg) => write!(f, "Validation: {}", msg),
        }
    }
}

impl std::error::Error for AppError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            AppError::Io(e) => Some(e),
            AppError::Parse(e) => Some(e),
            _ => None,
        }
    }
}

impl From<std::io::Error> for AppError {
    fn from(e: std::io::Error) -> Self { AppError::Io(e) }
}

// Usage: the ? operator auto-converts io::Error to AppError
fn read_config(path: &str) -> Result<String, AppError> {
    let content = std::fs::read_to_string(path)?;
    Ok(content)
}
```

---

## Eşzamanlılık ve Paralellik
### Konu Modeli ve Senkronizasyon
Rust'un sahiplik sistemi derleme zamanında veri yarışlarını önler.`Send`ve`Sync`özellikleri iş parçacığı güvenliğini güçlendirir.
```rust
use std::thread;
use std::sync::{Arc, Mutex, RwLock};

// Arc<Mutex<T>> — thread-safe shared mutable state
fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for i in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
            println!("Thread {} incremented to {}", i, *num);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("Final count: {}", *counter.lock().unwrap());
}

// RwLock — multiple readers OR one writer
let data = Arc::new(RwLock::new(vec![1, 2, 3]));
let reader_data = Arc::clone(&data);
let reader = thread::spawn(move || {
    let r = reader_data.read().unwrap();
    println!("Read: {:?}", *r);
});
let writer_data = Arc::clone(&data);
let writer = thread::spawn(move || {
    let mut w = writer_data.write().unwrap();
    w.push(4);
});
reader.join().unwrap();
writer.join().unwrap();
```

### Kanallar — Mesaj Aktarma
```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();
    let tx1 = tx.clone();
    let tx2 = tx.clone();

    thread::spawn(move || { tx1.send("from thread 1").unwrap(); });
    thread::spawn(move || { tx2.send("from thread 2").unwrap(); });
    thread::spawn(move || { tx.send("from main thread").unwrap(); });

    for _ in 0..3 {
        let msg = rx.recv().unwrap();
        println!("Received: {}", msg);
    }
}
```

### Tokio ile Eşzamansız/Bekleme
```rust
// Cargo.toml: tokio = { version = "1", features = ["full"] }
use tokio;

async fn fetch_data(url: &str) -> Result<String, reqwest::Error> {
    let response = reqwest::get(url).await?;
    response.text().await
}

async fn process_urls(urls: Vec<&str>) -> Vec<String> {
    let mut handles = vec![];
    for url in urls {
        let handle = tokio::spawn(async move {
            match fetch_data(url).await {
                Ok(text) => text,
                Err(e) => format!("Error: {}", e),
            }
        });
        handles.push(handle);
    }
    let mut results = vec![];
    for handle in handles {
        results.push(handle.await.unwrap());
    }
    results
}

#[tokio::main]
async fn main() {
    let urls = vec!["https://example.com", "https://httpbin.org/get"];
    let results = process_urls(urls).await;
    for (i, r) in results.iter().enumerate() {
        println!("Result {}: {} bytes", i, r.len());
    }
}
```

### Kapsamlı Konular (Pas 1.63+)
```rust
use std::thread;

fn main() {
    let mut data = vec![1, 2, 3, 4];
    thread::scope(|s| {
        s.spawn(|| {
            println!("Data: {:?}", data);
        });
        s.spawn(|| {
            for item in data.iter_mut() { *item *= 2; }
        });
    });
    println!("Modified: {:?}", data);
}
```

---

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
```
my_project/
+-- Cargo.toml            # Package manifest
+-- Cargo.lock            # Dependency lock file (auto-generated)
+-- src/
|   +-- main.rs           # Binary entry point
|   +-- lib.rs            # Library root
|   +-- config.rs         # Module
|   +-- models/
|   |   +-- mod.rs
|   |   +-- user.rs
|   |   +-- post.rs
|   +-- handlers/
|       +-- mod.rs
|       +-- api.rs
+-- tests/
|   +-- integration_test.rs
+-- benches/
|   +-- benchmark.rs
+-- examples/
|   +-- basic_usage.rs
+-- .cargo/
|   +-- config.toml       # Cargo configuration
+-- rustfmt.toml          # Formatter configuration
```

### Cargo.toml Yapılandırması
```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"
authors = ["Developer <dev@example.com>"]
rust-version = "1.75"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
reqwest = { version = "0.12", features = ["json"] }
anyhow = "1.0"
thiserror = "2.0"

[dev-dependencies]
criterion = { version = "0.5", features = ["html_reports"] }
mockall = "0.13"

[[bench]]
name = "performance"
harness = false

[profile.release]
opt-level = 3
lto = "fat"
codegen-units = 1
strip = "symbols"
```

### Temel Kargo Komutları
```bash
cargo new my_project          # Create binary project
cargo new --lib my_library    # Create library project
cargo build                   # Debug build
cargo build --release         # Optimised release build
cargo check                   # Type-check without compilation (fast)
cargo run                     # Build and run
cargo test                    # Run all tests
cargo test --lib              # Unit tests only
cargo fmt                     # Format code
cargo clippy                  # Run linter
cargo doc --open              # Generate and open docs
cargo add serde --features derive   # Add dependency
cargo tree                    # Show dependency tree
cargo update                  # Update dependencies
```

### CI/CD İşlem Hattı (GitHub Eylemleri)
```yaml
name: Rust CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
env:
  CARGO_TERM_COLOR: always
  RUSTFLAGS: "-Dwarnings"
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with:
          components: rustfmt, clippy
      - uses: Swatinem/rust-cache@v2
      - run: cargo fmt -- --check
      - run: cargo clippy --all-targets --all-features
      - run: cargo test --all-features
  build:
    needs: check
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: Swatinem/rust-cache@v2
      - run: cargo build --release
```

---

## Test etme
### Birim Testleri
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_addition() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    #[should_panic(expected = "division by zero")]
    fn test_divide_by_zero() {
        divide(10.0, 0.0).unwrap();
    }

    #[test]
    fn test_result_ok() {
        let result = divide(10.0, 2.0);
        assert!(result.is_ok());
        assert!((result.unwrap() - 5.0).abs() < f64::EPSILON);
    }
}
```

### Entegrasyon Testleri
```rust
// tests/integration_test.rs
use my_library::{Config, App};

#[test]
fn test_app_initialisation() {
    let config = Config::default();
    let app = App::new(config);
    assert!(app.is_ready());
}

#[test]
fn test_full_workflow() {
    let mut app = App::new(Config::default());
    app.process("input data").expect("processing failed");
    assert_eq!(app.result_count(), 1);
}
```

### Karşılaştırma Testi
```rust
// benches/benchmark.rs
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use my_library::fibonacci;

fn bench_fibonacci(c: &mut Criterion) {
    c.bench_function("fibonacci(30)", |b| {
        b.iter(|| fibonacci(black_box(30)))
    });
}

criterion_group!(benches, bench_fibonacci);
criterion_main!(benches);
```

```bash
cargo bench                    # Run benchmarks
cargo bench --bench performance  # Specific benchmark
```

---

## Birlikte Çalışabilirlik
### C ile FFI
```rust
use std::ffi::{CStr, CString};
use std::os::raw::{c_char, c_int};

// Calling C functions from Rust
extern "C" {
    fn abs(x: c_int) -> c_int;
    fn strlen(s: *const c_char) -> usize;
}

fn main() {
    unsafe {
        println!("abs(-5) = {}", abs(-5));
        let s = CString::new("hello").unwrap();
        println!("strlen = {}", strlen(s.as_ptr()));
    }
}

// Exposing Rust functions to C
#[no_mangle]
pub extern "C" fn rust_add(a: c_int, b: c_int) -> c_int {
    a + b
}

// Safe wrapper around unsafe C API
struct SafeString { ptr: *mut c_char }

impl SafeString {
    fn new(s: &str) -> Self {
        let c_string = CString::new(s).expect("CString::new failed");
        SafeString { ptr: c_string.into_raw() }
    }
    fn as_str(&self) -> &str {
        unsafe {
            CStr::from_ptr(self.ptr).to_str().expect("Invalid UTF-8")
        }
    }
}

impl Drop for SafeString {
    fn drop(&mut self) {
        unsafe { let _ = CString::from_raw(self.ptr); }
    }
}
```

### Python'dan Rust'ı çağırmak (PyO3)
```rust
// Cargo.toml: pyo3 = { version = "0.22", features = ["extension-module"] }
use pyo3::prelude::*;

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pymodule]
fn my_rust_lib(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}
```

---

## Tasarım Desenleri
### Oluşturucu Deseni
```rust
#[derive(Debug)]
struct Request {
    url: String,
    method: String,
    headers: Vec<(String, String)>,
    timeout_ms: u64,
}

struct RequestBuilder {
    url: String,
    method: String,
    headers: Vec<(String, String)>,
    timeout_ms: u64,
}

impl RequestBuilder {
    fn new(url: &str) -> Self {
        RequestBuilder {
            url: url.to_string(),
            method: "GET".to_string(),
            headers: vec![],
            timeout_ms: 30_000,
        }
    }
    fn method(mut self, method: &str) -> Self {
        self.method = method.to_string(); self
    }
    fn header(mut self, key: &str, value: &str) -> Self {
        self.headers.push((key.to_string(), value.to_string())); self
    }
    fn timeout(mut self, ms: u64) -> Self {
        self.timeout_ms = ms; self
    }
    fn build(self) -> Request {
        Request {
            url: self.url, method: self.method,
            headers: self.headers, timeout_ms: self.timeout_ms,
        }
    }
}

// Usage — fluent builder chain
let req = RequestBuilder::new("https://api.example.com")
    .method("POST")
    .header("Content-Type", "application/json")
    .timeout(5000)
    .build();
```

### Yeni Tip Desen (Tip Güvenliği)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Nitelikli Depo Modeli
```rust
trait Repository<T> {
    fn find(&self, id: u64) -> Option<T>;
    fn save(&mut self, item: &T) -> Result<(), String>;
    fn delete(&mut self, id: u64) -> Result<(), String>;
}

struct InMemoryRepo { data: Vec<User> }

impl Repository<User> for InMemoryRepo {
    fn find(&self, id: u64) -> Option<User> {
        self.data.iter().find(|u| u.id == id).cloned()
    }
    fn save(&mut self, item: &User) -> Result<(), String> {
        self.data.push(item.clone()); Ok(())
    }
    fn delete(&mut self, id: u64) -> Result<(), String> {
        self.data.retain(|u| u.id != id); Ok(())
    }
}
```

---

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
```bash
# Flame graph profiling
cargo install flamegraph
cargo flamegraph --bin my_app

# Criterion benchmarks (statistical rigour)
cargo bench

# Compile-time profiling
cargo build --timings

# Memory profiling with valgrind (Linux)
valgrind --tool=massif ./target/release/my_app

# perf integration (Linux)
perf record ./target/release/my_app
perf report
```

### Optimizasyon Teknikleri
```rust
// Iterators compile to the same code as manual loops
let sum: i64 = (0..1_000_000).filter(|x| x % 2 == 0).sum();

// Borrowed types avoid allocations
fn process(data: &[u8]) -> usize {
    data.iter().filter(|&&b| b > 128).count()
}

// Stack allocation for small data
let small_data: [u8; 64] = [0; 64];

// Box for large data to avoid stack overflow
let large_buffer: Box<[u8; 1_000_000]> = Box::new([0; 1_000_000]);

// Inline hints for hot-path functions
#[inline(always)]
fn fast_add(a: i32, b: i32) -> i32 { a + b }

// Parallel iteration with rayon
use rayon::prelude::*;
let sum: i64 = (0..1_000_000i64).par_iter().sum();
```

---

## Dağıtım
### Çapraz Derleme
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Docker Dağıtımı
```dockerfile
FROM rust:1.80 AS builder
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release

FROM debian:bookworm-slim
RUN apt-get update; apt-get install -y ca-certificates; apt-get clean
COPY --from=builder /app/target/release/my_app /usr/local/bin/my_app
EXPOSE 8080
CMD ["my_app"]
```

### WebAssembly Dağıtımı
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## Ekosistem
| Araç | Amaç |
|------|------------|
| **kargo** | Derleme sistemi, paket yöneticisi, test çalıştırıcısı, belge oluşturucu |
| **crates.io** | Paket kaydı (150.000'den fazla kasa) |
| **rustfmt** | Kod biçimlendirici |
| **keskin** | Yüzlerce faydalı kontrolle Linter |
| **tokio** | Zaman uyumsuz çalışma zamanı (zaman uyumsuz Rust için standart) |
| **serde** | Serileştirme/seri durumdan çıkarma çerçevesi |
| **actix-web / axum** | Web çerçeveleri |
| **dizel / sqlx** | Veritabanı ORM'leri / sorgu oluşturucuları |
---

## Rust Ne Zaman Kullanılmalı
| Senaryo | Neden Pas | Daha İyi Alternatif |
|----------|------------|-----------|
| Sistem programlama | Bellek güvenliği + performansı | Güvenlik garantisine ihtiyacınız yoksa C/C++ |
| Web Montajı | Sınıfının en iyisi WASM desteği | -- |
| CLI araçları | Hızlı, tek ikili, harika UX | Daha basit CLI'leri tercih edin |
| Gömülü sistemler | GC yok, donanım erişimi, güvenlik | Daha basit gömülü için C |
| Performans açısından kritik kod | C/C++ hızıyla eşleşir | -- |
| Bulut altyapısı | Kullanım artışı (AWS, Cloudflare) | Daha hızlı gelişmeye gidin |
| Genel uygulama geliştirme | Dik öğrenme eğrisi geliştirmeyi yavaşlatıyor | Python, Git, Java |
| Web arka uçları | Mümkün ama ekosistem daha genç | Git, Node.js, Python |
| Veri bilimi / ML | Bunun için ekosistem değil | Python, R |
| Hızlı komut dosyaları / prototipler | Yazmak için çok ayrıntılı ve yavaş | Python, JavaScript |
---

## Sentetik Soru-Cevap
### S1: Sahiplik sistemi nedir ve Rust'ta neden bu sistem var?
**C:** Rust'taki her değerin tam olarak bir sahibi vardır. Sahibi kapsam dışına çıktığında değer düşürülür (bellek serbest bırakılır). Bu, bellek güvenliğini garanti ederken çöp toplayıcı ihtiyacını ortadan kaldırır. Atama, işlev parametreleri ve dönüş değerlerinin tümü sahipliği aktarır ("taşıma"). Aktarmadan paylaşmak için referansları kullanın (ödünç almak için `&T`, değişken ödünç almak için `&mut T`). Derleyici şunları uygular: aynı anda aynı değere yönelik değişken bir referansa ve değişmez bir referansa sahip olamazsınız.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### S2:`String`ve `&str`'yi ne zaman kullanmalıyım?
**C:**`String`sahip olunan, yığına ayrılmış, büyütülebilir bir UTF-8 dizisidir.  `&str`, UTF-8 dize dilimine yönelik ödünç alınmış bir referanstır (bir `String`'ye, bir dize değişmez değerine veya her ikisinin bir kısmına işaret edebilir). Bir dizeye sahip olmanız, değiştirmeniz veya oluşturmanız gerektiğinde `String`'yi kullanın. İşlev parametreleri (daha esnek — her ikisini de kabul eder), salt okunur görünümler ve dize değişmezleri için`&str`kullanın. İşlev imzalarında `&str`'yi kabul edin; arayanın sahipliğe ihtiyacı olduğunda `String`'yi döndürün.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### S3: Rust, hataları istisnasız nasıl ele alıyor?
**C:** Rust, kurtarılabilir hatalar için`Result<T, E>`numaralandırmasını, kurtarılamayan hatalar için ise`panic!`numaralandırmasını kullanır. Başarısız olabilecek işlevler`Result`değerini döndürür.`?`operatörü hataları tam olarak yayar. Bu yaklaşım, hata işlemeyi açık hale getirir; bir hatayı yanlışlıkla göz ardı edemezsiniz. Uygulama hatası işleme için `anyhow`'yi (uygun bağlam) ve kitaplık hata türleri için (makroları türetme) `thiserror`'yi kullanın.
```rust
use std::fs;
use std::num;

fn read_and_parse(path: &str) -> Result<i64, Box<dyn std::error::Error>> {
    let content = fs::read_to_string(path)?;   // Propagates io::Error
    let number: i64 = content.trim().parse()?;  // Propagates ParseIntError
    Ok(number)
}

// With context (anyhow crate)
fn load_config() -> anyhow::Result<Config> {
    let content = fs::read_to_string("config.toml")
        .context("Failed to read config file")?;
    let config: Config = toml::from_str(&content)
        .context("Failed to parse config TOML")?;
    Ok(config)
}
```

### S4: Yaşam süreleri nedir ve bunlara ne zaman açıklama eklemem gerekir?
**C:** Yaşam süreleri, referansların ne kadar süreyle geçerli olduğunu izler. Derleyici çoğu durumda bunları "ömür boyu seçim kuralları" aracılığıyla çıkarır. Derleyici giriş ve çıkış yaşam süreleri arasındaki ilişkiyi belirleyemediğinde (genellikle bir işlev birden fazla referans alıp bir tane döndürdüğünde) açık açıklamalara ihtiyacınız vardır. Yaşam süreleri, sıfır çalışma zamanı maliyetiyle derleme zamanında referansların sarkmasını önler.
```rust
// The compiler needs to know: does the return value borrow from x or y?
// Explicit lifetime 'a says: both inputs and output share the same lifetime
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Struct holding a reference — must declare lifetime
struct ConfigRef<'a> {
    name: &'a str,
    value: &'a str,
}

// 'static — lives for the entire program duration (string literals)
let s: &'static str = "I live forever";
```

### S5: `Vec<T>`, diziler ve dilimler arasındaki fark nedir?
**A:**`[T; N]`dizileri sabit boyutludur, yığına ayrılmıştır ve uzunlukları türün bir parçasıdır.  `Vec<T>`, büyütülebilir, yığın tahsisli bir koleksiyondur.`&[T]`dilimleri, bir dizinin veya Vec'in bitişik bir bölümünü ödünç alan kalın işaretçilerdir (işaretçi + uzunluk). Küçük, sabit boyutlu veriler için dizileri kullanın. Dinamik koleksiyonlar için Vec'i kullanın. Maksimum esneklik için fonksiyon parametrelerinde `&[T]`'yi kabul edin.
```rust
let arr = [1, 2, 3, 4, 5];            // [i32; 5] — fixed size, on stack
let mut vec = vec![10, 20, 30];        // Vec<i32> — growable, on heap
vec.push(40);

// Slice — borrow of a contiguous sequence
let slice: &[i32] = &vec[1..3];        // [20, 30]
let full: &[i32] = &vec;               // Entire vec as slice

// Functions should accept slices for flexibility
fn sum(numbers: &[i32]) -> i32 {
    numbers.iter().sum()
}

sum(&arr);       // Works — array coerces to slice
sum(&vec);       // Works — Vec coerces to slice
sum(&vec[1..3]); // Works — already a slice
```

---

## Düşünce Zinciri Problem Çözme
### Sorun 1: İş parçacığı açısından güvenli bir anahtar/değer deposu oluşturun
**Sorun Açıklaması:** Rust'ta, veri yarışları olmadan birden fazla iş parçacığından `get`,`set`ve`delete`işlemlerini destekleyen eşzamanlı bir anahtar/değer deposu uygulayın. Dahili değiştirilebilirliği kullanın ve uygulamanın deyimsel Rust olduğundan emin olun.
**1. Adım — Sorunu Anlayın:**
Birden fazla iş parçacığının paylaşılan bir HashMap'i okuması ve yazması gerekir. Rust'un sahiplik sistemi, derleme zamanında veri yarışlarını önler, ancak ortak sahiplik için `Arc`'ye sarılmış dahili değiştirilebilirliğe (`RwLock`veya`Mutex`) ihtiyacımız var. `RwLock`birden fazla eşzamanlı okuyucuya VEYA tek bir özel yazıcıya izin verir; okuma ağırlıklı iş yükleri için daha iyidir.
**2. Adım — Yaklaşımı Belirleyin:**
- Paylaşılan, iş parçacığı açısından güvenli erişim için`Arc<RwLock<HashMap<K, V>>>`kullanın.
-`get`için`RwLock::read()`(birden fazla okuyucuya izin verilir).
-`set`ve`delete`için`RwLock::write()`(özel erişim).
- Temiz bir API ile bir yapıya sarın.
- Her iş parçacığı için `Arc`'yi kopyalayın.
**3. Adım — Çözümü Uygulayın:**
```rust
use std::collections::HashMap;
use std::sync::{Arc, RwLock};
use std::hash::Hash;

struct KeyValueStore<K, V> {
    data: Arc<RwLock<HashMap<K, V>>>,
}

impl<K: Hash + Eq + Send + Sync, V: Clone + Send + Sync> KeyValueStore<K, V> {
    fn new() -> Self {
        Self {
            data: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    fn get(&self, key: &K) -> Option<V> {
        let data = self.data.read().unwrap();
        data.get(key).cloned()
    }

    fn set(&self, key: K, value: V) {
        let mut data = self.data.write().unwrap();
        data.insert(key, value);
    }

    fn delete(&self, key: &K) -> bool {
        let mut data = self.data.write().unwrap();
        data.remove(key).is_some()
    }

    fn clone_handle(&self) -> Self {
        Self {
            data: Arc::clone(&self.data),
        }
    }
}

// Usage — concurrent access from multiple threads
use std::thread;

fn main() {
    let store = KeyValueStore::new();

    let handles: Vec<_> = (0..4).map(|i| {
        let s = store.clone_handle();
        thread::spawn(move || {
            for j in 0..100 {
                s.set(format!("key-{}-{}", i, j), i * 100 + j);
            }
        })
    }).collect();

    for h in handles { h.join().unwrap(); }

    println!("Total entries: {}", store.data.read().unwrap().len());  // 400
}
```

**4. Adım — Doğrulayın ve Optimize Edin:**
- İş parçacığı güvenliği: Rust derleyicisi veri yarışı olmayacağını garanti eder —`RwLock`karşılıklı hariç tutmayı uygular ve`Arc`güvenli paylaşımlı sahiplik sağlar. Bu derlenirse doğrudur.
- Performans: `RwLock`, okuma ağırlıklı iş yükleri için `Mutex`'den daha iyidir. Yazma ağırlıklı iş yükleri için`Mutex`kullanın (daha basit, okuyucu-yazıcı yükü yok).
- Üretim yükseltmesi:`parking_lot::RwLock`(daha hızlı, zehirlenme yok, daha küçük bellek alanı) veya`dashmap::DashMap`(kilitsiz eşzamanlı HashMap) kullanın.
### Sorun 2: Sıfır Kopyalı Ayrıştırıcı Uygulama
**Sorun Açıklaması:** Yalnızca girişten ödünç alınan dize dilimlerini kullanarak, yeni Dizeler ayırmadan`"name=Alice;age=30;role=admin"`gibi bir yapılandırma dizesinden anahtar/değer çiftlerini ayıklayan bir ayrıştırıcı yazın.
**1. Adım — Sorunu Anlayın:**
`;` ile ayrılmış`key=value`çiftlerini ayrıştırmamız gerekiyor. Temel kısıtlama "sıfır kopyadır" - döndürülen veriler yeni`String`tahsis etmek değil,`&str`girişinden ödünç alınmalıdır. Bu, girişe bağlı yaşam süreleri ile `Vec<(&str, &str)>`'nin döndürülmesi anlamına gelir.
**2. Adım — Yaklaşımı Belirleyin:**
-`&str`yöntemlerini kullanın (`split`,`find`, dilimleme) — tümü girişten ödünç alınan`&str`dilimlerini döndürür.
- Her yerde`.to_string()`veya `String::from()`'den kaçının.
- Ömür boyu açıklama: çıktı girdiden ödünç alınır —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**3. Adım — Çözümü Uygulayın:**
```rust
fn parse_config(input: &str) -> Vec<(&str, &str)> {
    input
        .split(';')
        .filter_map(|pair| {
            let pair = pair.trim();
            if pair.is_empty() { return None; }
            pair.split_once('=')
                .map(|(k, v)| (k.trim(), v.trim()))
        })
        .collect()
}

// The compiler infers: fn parse_config<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>

fn main() {
    let config = "name = Alice; age = 30; role = admin";
    let pairs = parse_config(config);

    for (key, value) in &pairs {
        println!("{} = {}", key, value);
    }

    // Zero allocations — all slices point into 'config'
    assert_eq!(pairs[0], ("name", "Alice"));
    assert_eq!(pairs[1], ("age", "30"));
    assert_eq!(pairs[2], ("role", "admin"));
}
```

**4. Adım — Doğrulayın ve Optimize Edin:**
- Sıfır kopya:`split`,`split_once`ve `trim`'nin tümü`&str`dilimlerini döndürür — yığın tahsisi yoktur.
- Yaşam boyu seçim kuralları, çıktı yaşam sürelerini girdiye doğru şekilde bağlar.
- Kenar durumları: boş giriş`[]`değerini döndürür; eksik`=`çifti atlar (`filter_map` aracılığıyla);`=`etrafındaki boşluklar`trim`tarafından işlenir.
- Daha karmaşık ayrıştırma için`nom`sandığını kullanın (birleştirici tabanlı, ayrıca sıfır kopya).
### Sorun 3: Gözlemci Modelini Kanallarla Uygulama
**Sorun Açıklaması:** Birden fazla abonenin bir yayıncıdan mesaj aldığı bir yayınlama-abone olma sistemi oluşturun. Rust kanallarını kullanın ve yayıncıyı engellemeden sistemin yavaş aboneleri işlemesini sağlayın.
**1. Adım — Sorunu Anlayın:**
Birden fazla aboneye mesaj gönderen bir yayıncıya ihtiyacımız var. Rust'un`mpsc`kanalı çok yapımcılı tek tüketicidir; bunun tersine ihtiyacımız var (tek yapımcı çok tüketici).`broadcast`kanallarını (`tokio`'den) kullanabilir veya birden fazla`mpsc`gönderici kullanarak yayma uygulayabiliriz.
**2. Adım — Yaklaşımı Belirleyin:**
- Standart kanallar için`std::sync::mpsc`kullanın.
- Genişletme için: bir`Vec<Sender<T>>`bulundurun ve mesajları her birine kopyalayın.
- Yavaş aboneler için:`try_send`(engellenmeyen) veya karşı basınçlı sınırlı kanalları kullanın.
- Temiz API için bir`Bus`yapısına sarın.
**3. Adım — Çözümü Uygulayın:**
```rust
use std::sync::mpsc::{self, Sender, Receiver};
use std::sync::{Arc, Mutex};
use std::thread;

struct Bus<T: Clone + Send + 'static> {
    subscribers: Arc<Mutex<Vec<Sender<T>>>>,
}

impl<T: Clone + Send + 'static> Bus<T> {
    fn new() -> Self {
        Self {
            subscribers: Arc::new(Mutex::new(Vec::new())),
        }
    }

    fn subscribe(&self) -> Receiver<T> {
        let (tx, rx) = mpsc::channel();
        self.subscribers.lock().unwrap().push(tx);
        rx
    }

    fn publish(&self, message: T) {
        let mut subs = self.subscribers.lock().unwrap();
        // Remove disconnected subscribers (their receiver was dropped)
        subs.retain(|tx| !tx.is_disconnected());
        for tx in subs.iter() {
            let _ = tx.send(message.clone());  // Ignore send errors
        }
    }

    fn subscriber_count(&self) -> usize {
        let subs = self.subscribers.lock().unwrap();
        subs.iter().filter(|tx| !tx.is_disconnected()).count()
    }
}

fn main() {
    let bus = Bus::new();

    // Subscribe from multiple threads
    let handles: Vec<_> = (0..3).map(|id| {
        let rx = bus.subscribe();
        thread::spawn(move || {
            for msg in rx {
                println!("Subscriber {} received: {}", id, msg);
            }
        })
    }).collect();

    // Publish messages
    for i in 0..5 {
        bus.publish(format!("Event #{}", i));
    }

    // Drop the bus — subscribers' channels close, loops end
    drop(bus);
    for h in handles { h.join().unwrap(); }
}
```

**4. Adım — Doğrulayın ve Optimize Edin:**
-`retain`ölü aboneleri otomatik olarak temizler — bağlantısız iş parçacıklarından bellek sızıntısı olmaz.
-`message.clone()`gereklidir çünkü her abonenin kendi kopyasına ihtiyacı vardır. Klonlanması pahalı türler için `Arc<T>`'ye sarın.
- Sınırlı kanallar: karşı basınç için `mpsc::channel()`'yi`mpsc::sync_channel(N)`ile değiştirin — abonenin arabelleği doluysa`publish`bloke eder.
- Üretim: eşzamansız pub/sub için `tokio::sync::broadcast`'yi veya sınırlı/sınırsız seçeneklerle daha hızlı mpsc için `flume`'yi kullanın.
---

## Özet
Rust, sizi bellek, sahiplik ve eşzamanlılık hakkında düşünmeye zorlayan ve yapısı gereği doğru kodla ödüllendiren bir dildir. Öğrenme eğrisi gerçektir, ancak getirisi önemlidir: C kadar hızlı ancak boş işaretçi hatalarından, veri yarışlarından ve bellek sızıntılarından arınmış programlar. Rust genel amaçlı bir üretkenlik dili değildir; doğruluk ve performansın her ikisinin de önemli olduğu durumlarda kullanılan bir sistem dilidir. Endüstride giderek artan şekilde benimsenmesi (Linux çekirdeği ve Android dahil), giderek daha önemli olacağını gösteriyor.