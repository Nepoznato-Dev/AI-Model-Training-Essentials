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

# Rdza
Rust to skompilowany język programowania ze statycznym typem, wydany po raz pierwszy w 2015 roku, opracowany pierwotnie przez Graydona Hoare'a z Mozilli. Najważniejszą obietnicą Rusta jest **bezpieczeństwo pamięci bez usuwania śmieci**. Osiąga to poprzez swój system własności — zestaw reguł egzekwowanych w czasie kompilacji, który eliminuje całe kategorie błędów (dereferencje zerowych wskaźników, wyścigi danych, przepełnienia bufora, użycie po zwolnieniu), jednocześnie tworząc kod tak szybko, jak C lub C++.
Rust został uznany za „najbardziej lubiany” język programowania w ankiecie deweloperów Stack Overflow przez wiele lat z rzędu. Jest coraz częściej stosowany w programowaniu systemów, WebAssembly, narzędziach CLI, infrastrukturze chmurowej oraz jako zamiennik C/C++ w kontekstach krytycznych dla bezpieczeństwa. Jądro Linuksa akceptuje teraz kod Rust.
---

## Dlaczego rdza ma znaczenie
- **Bezpieczeństwo pamięci bez GC**: System własności zapobiega wskaźnikom zerowym, wyścigom danych i wskaźnikom wiszącym w czasie kompilacji — przy zerowym nakładzie czasowym.
- **Wydajność**: Dorównuje lub przekracza C/C++ w przypadku większości obciążeń. Brak modułu zbierającego śmieci oznacza brak nieprzewidywalnych przerw.
- **Nieustraszona współbieżność**: System typów zapobiega wyścigom danych w czasie kompilacji. Jeśli się skompiluje, jest bezpieczny dla wątków.
- **Nowoczesne oprzyrządowanie**:`cargo`(system kompilacji + menedżer pakietów) jest jednym z najlepszych w dowolnym języku. `cargo build`,`cargo test`,`cargo doc`działają od razu po wyjęciu z pudełka.
- **WebAssembly**: Pierwszorzędna obsługa kompilacji do WASM, umożliwiająca działanie w przeglądarkach zbliżone do natywnego.
- **Rosnące przyjęcie**: Używane przez AWS, Google (Android), Microsoft (jądro Windows), Cloudflare, Discord, Dropbox i Meta.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Stroma krzywa uczenia się** | Własność, pożyczki, okresy życia są inne niż wszystko w innych językach | Zainwestuj czas w „Księgę rdzy”; koncepcje łączą się z praktyką |
| **Powolna kompilacja** | Czasy kompilacji mogą być długie w przypadku dużych projektów | Użyj`cargo check`do szybkiego sprawdzania typu; kompilacja przyrostowa pomaga |
| **Rozszerzona obsługa błędów** |  Operatory`Result<T, E>`i`?`wymagają jawnej obsługi | Użyj`anyhow`dla aplikacji,`thiserror`dla bibliotek |
| **Mniejszy rynek pracy** | Mniej stanowisk pracy w Rust niż Java, Python i JavaScript (ale szybko rośnie) | Większość ról Rusta dotyczy programowania systemów, kryptografii lub infrastruktury |
| **Niedojrzały ekosystem** | Mniej bibliotek niż Python/Java/JS dla niektórych domen | Ekosystem szybko się rozwija; wiele skrzynek jest doskonałej jakości |
---

## Podstawy składni
### Podstawowa struktura
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

### Własność i pożyczki
To podstawowa innowacja firmy Rust. Każda wartość ma dokładnie jednego właściciela. Gdy właściciel wykracza poza zakres, wartość jest usuwana.
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

### Struktury, wyliczenia i dopasowywanie wzorców
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

### Obsługa błędów
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

## Zaawansowana składnia i wzorce
### Typy ogólne i granice cech
Generics umożliwiają pisanie kodu, który działa z dowolnym typem, przy jednoczesnym zachowaniu pełnego bezpieczeństwa typów. Cechy definiują wspólne zachowanie.
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

### Makra
Rust ma dwa rodzaje makr: deklaratywne (`macro_rules!`) i proceduralne (wyprowadzenie, atrybut, funkcja podobna).
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

### Zaawansowane dopasowywanie i destrukturyzacja wzorców
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

### Przeciążenie operatora
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

### Niestandardowe hierarchie błędów
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

## Współbieżność i równoległość
### Model wątku i synchronizacja
System własności Rusta zapobiega wyścigom danych w czasie kompilacji. Cechy`Send`i`Sync`wymuszają bezpieczeństwo wątków.
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

### Kanały — przekazywanie wiadomości
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

### Async/Await z Tokio
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

### Gwinty o ograniczonym zakresie (Rdza 1.63+)
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

## Konfiguracja projektu i budowanie systemu
### Struktura projektu
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

### Konfiguracja Cargo.toml
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

### Podstawowe polecenia dotyczące ładunku
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

### Potok CI/CD (akcje w GitHub)
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

## Testowanie
### Testy jednostkowe
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

### Testy integracyjne
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

### Testowanie porównawcze
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

## Interoperacyjność
### FFI z C
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

### Wywoływanie Rusta z Pythona (PyO3)
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

## Wzorce projektowe
### Wzór konstruktora
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

### Wzorzec nowego typu (bezpieczeństwo typu)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Wzorzec repozytorium z cechami
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

## Wydajność i optymalizacja
### Narzędzia do profilowania
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

### Techniki optymalizacji
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

## Zastosowanie
### Kompilacja krzyżowa
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Wdrożenie Dockera
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

### Wdrożenie zestawu WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## Ekosystem
| Narzędzie | Cel |
|------|-------------|
| **ładunek** | Kompiluj system, menedżer pakietów, uruchamiacz testów, generator dokumentów |
| **crates.io** | Rejestr paczek (ponad 150 000 skrzynek) |
| **rdza** | Formater kodu |
| **spinacz** | Linter z setkami pomocnych kontroli |
| **Tokio** | Asynchroniczne środowisko wykonawcze (standard dla asynchronicznego Rusta) |
| **serde** | Struktura serializacji/deserializacji |
| **actix-web / axum** | Frameworki internetowe |
| **diesel / sqlx** | Bazy danych ORM / narzędzia do tworzenia zapytań |
---

## Kiedy używać rdzy
| Scenariusz | Dlaczego rdza | Lepsza alternatywa |
|---------|---------|--------------------------------|
| Programowanie systemów | Bezpieczeństwo pamięci + wydajność | C/C++, jeśli nie potrzebujesz gwarancji bezpieczeństwa |
| Zespół WWW | Najlepsza w swojej klasie obsługa WASM | -- |
| Narzędzia CLI | Szybki, pojedynczy plik binarny, świetny UX | Wybierz prostsze interfejsy CLI |
| Systemy wbudowane | Brak GC, dostępu do sprzętu, bezpieczeństwa | C dla prostszego osadzenia |
| Kod krytyczny dla wydajności | Pasuje do szybkości C/C++ | -- |
| Infrastruktura chmurowa | Rosnące przyjęcie (AWS, Cloudflare) | Postaw na szybszy rozwój |
| Ogólne tworzenie aplikacji | Stroma krzywa uczenia się spowalnia programistów | Python, Go, Java |
| Backendy internetowe | Możliwe, ale ekosystem jest młodszy | Idź, Node.js, Python |
| Nauka o danych / ML | To nie jest ekosystem do tego | Python, R |
| Szybkie skrypty / prototypy | Zbyt gadatliwy i powolny do napisania | Python, JavaScript |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaki jest system własności i dlaczego Rust go posiada?
**A:** Każda wartość w Rust ma dokładnie jednego właściciela. Kiedy właściciel wyjdzie poza zakres, wartość zostanie usunięta (pamięć zostanie zwolniona). Eliminuje to potrzebę stosowania modułu zbierającego elementy bezużyteczne, gwarantując jednocześnie bezpieczeństwo pamięci. Przypisanie, parametry funkcji i zwracane wartości przenoszą własność („przenieś”). Aby udostępnić bez przenoszenia, użyj referencji (`&T` dla pożyczania,`&mut T`dla modyfikowalnego pożyczania). Kompilator wymusza: nie można jednocześnie mieć odniesienia zmiennego i odniesienia niezmiennego do tej samej wartości.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### P2: Kiedy powinienem używać`String`zamiast `&str`?
**A:**`String`jest posiadanym, przydzielonym stercie i rozwijalnym ciągiem UTF-8. `&str`jest zapożyczonym odniesieniem do wycinka ciągu UTF-8 (może wskazywać na`String`, literał ciągu lub część któregokolwiek z nich). Użyj `String`, jeśli chcesz posiadać, modyfikować lub budować ciąg. Użyj`&str`dla parametrów funkcji (bardziej elastyczne — akceptuje oba), widoków tylko do odczytu i literałów łańcuchowych. Zaakceptuj`&str`w sygnaturach funkcji; zwróć `String`, gdy osoba wywołująca potrzebuje własności.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### P3: Jak Rust radzi sobie z błędami bez wyjątków?
**A:** Rust używa wyliczenia`Result<T, E>`dla błędów możliwych do naprawienia, a`panic!`dla błędów nienaprawialnych. Funkcje, które mogą zakończyć się niepowodzeniem, zwracają`Result`. Operator`?`zwięźle propaguje błędy. Dzięki takiemu podejściu obsługa błędów jest jawna — nie można przypadkowo zignorować błędu. Użyj`anyhow`do obsługi błędów aplikacji (wygodny kontekst) i`thiserror`do typów błędów bibliotek (makra pochodne).
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

### P4: Co to są okresy istnienia i kiedy muszę je opisywać?
**O:** Czasy życia monitorują, jak długo referencje są ważne. Kompilator wnioskuje je w większości przypadków na podstawie „reguł eliminacji na całe życie”. Potrzebujesz wyraźnych adnotacji, gdy kompilator nie może określić relacji między okresami istnienia danych wejściowych i wyjściowych — zazwyczaj, gdy funkcja pobiera wiele odniesień i zwraca jedno. Czasy życia zapobiegają zawieszaniu się referencji w czasie kompilacji przy zerowym koszcie czasu wykonania.
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

### P5: Jaka jest różnica między`Vec<T>`, tablicami i wycinkami?
**A:** Tablice`[T; N]`mają stały rozmiar, alokację stosu, a ich długość jest częścią typu. `Vec<T>`to kolekcja, którą można rozwijać i przydzielać na stercie. Plasterki`&[T]`to grube wskaźniki (wskaźnik + długość), które pożyczają ciągłą część tablicy lub Vec. Używaj tablic dla małych danych o stałym rozmiarze. Użyj Vec do kolekcji dynamicznych. Zaakceptuj`&[T]`w parametrach funkcji, aby uzyskać maksymalną elastyczność.
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

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zbuduj bezpieczny wątkowo magazyn klucz-wartość
**Opis problemu:** Zaimplementuj współbieżną składnicę klucz-wartość w Rust, która obsługuje operacje`get`,`set`i`delete`z wielu wątków bez wyścigów danych. Użyj zmienności wewnętrznej i upewnij się, że implementacja jest idiomatyczna w stylu Rust.
**Krok 1 — Zrozum problem:**
Wiele wątków musi czytać i zapisywać w udostępnionej HashMap. System własności Rusta zapobiega wyścigom danych w czasie kompilacji, ale potrzebujemy wewnętrznej zmienności (`RwLock`lub`Mutex`) zawiniętej w`Arc`w celu zapewnienia współwłasności. `RwLock`umożliwia wielu jednoczesnych czytników LUB jednego wyłącznego zapisu – lepiej w przypadku obciążeń wymagających dużego odczytu.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`Arc<RwLock<HashMap<K, V>>>`do współdzielonego, bezpiecznego dla wątków dostępu.
-`RwLock::read()`dla`get`(dozwolonych jest wiele czytników).
-`RwLock::write()`dla`set`i`delete`(wyłączny dostęp).
- Zawiń strukturę za pomocą czystego interfejsu API.
- Sklonuj`Arc`dla każdego wątku.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Bezpieczeństwo wątków: kompilator Rust gwarantuje brak wyścigów danych —`RwLock`wymusza wzajemne wykluczanie, a`Arc`zapewnia bezpieczną współwłasność. Jeśli to się skompiluje, jest poprawne.
- Wydajność:`RwLock`jest lepszy niż`Mutex`w przypadku obciążeń wymagających dużego odczytu. W przypadku obciążeń wymagających dużej liczby zapisów użyj`Mutex`(prościej, bez narzutu czytnika i zapisu).
- Aktualizacja produkcyjna: użyj`parking_lot::RwLock`(szybciej, bez zatruwania, mniejsze zużycie pamięci) lub`dashmap::DashMap`(współbieżna HashMap bez blokad).
### Problem 2: Zaimplementuj parser z zerową kopią
**Opis problemu:** Napisz parser, który wyodrębnia pary klucz-wartość z ciągu konfiguracyjnego, takiego jak `"name=Alice;age=30;role=admin"`, bez przydzielania nowych ciągów — używając tylko wycinków ciągów zapożyczonych z danych wejściowych.
**Krok 1 — Zrozum problem:**
Musimy przeanalizować pary`key=value`oddzielone`;`. Kluczowym ograniczeniem jest „kopia zerowa” — zwrócone dane muszą pożyczyć z wejścia `&str`, a nie przydzielać nowe `String`. Oznacza to zwrócenie`Vec<(&str, &str)>`z okresami życia powiązanymi z danymi wejściowymi.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj metod`&str`(`split`,`find`, krojenie) — wszystkie zwracają wycinki`&str`zapożyczone z wejścia.
- Unikaj`.to_string()`lub`String::from()`w dowolnym miejscu.
- Adnotacja dotycząca okresu istnienia: dane wyjściowe zapożyczają się z danych wejściowych —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Kopia zerowa:`split`,`split_once`i`trim`zwracają wycinki`&str`— bez alokacji sterty.
- Reguły eliminacji czasu życia poprawnie wiążą czasy życia wyjścia z wejściem.
- Przypadki Edge: puste wejście zwraca`[]`; brakujący`=`pomija parę (przez`filter_map`); białe znaki wokół`=`są obsługiwane przez`trim`.
- W przypadku bardziej złożonego analizowania użyj skrzynki`nom`(opartej na kombinatorze, również z kopią zerową).
### Problem 3: Zaimplementuj wzorzec obserwatora za pomocą kanałów
**Opis problemu:** Zbuduj system publikowania i subskrybowania, w którym wielu subskrybentów otrzymuje wiadomości od wydawcy. Użyj kanałów Rust i upewnij się, że system obsługuje powolnych subskrybentów bez blokowania wydawcy.
**Krok 1 — Zrozum problem:**
Potrzebujemy jednego wydawcy wysyłającego wiadomości do wielu subskrybentów. Kanał`mpsc`Rusta to kanał obejmujący wielu producentów i jednego konsumenta — potrzebujemy odwrotności (jeden producent, wielu konsumentów). Możemy użyć kanałów`broadcast`(z`tokio`) lub wdrożyć fan-out przy użyciu wielu nadawców `mpsc`.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`std::sync::mpsc`dla kanałów standardowych.
- W przypadku rozgałęzienia: zachowaj`Vec<Sender<T>>`i sklonuj wiadomości do każdego z nich.
- W przypadku wolnych abonentów: użyj`try_send`(nieblokującego) lub kanałów ograniczonych z przeciwciśnieniem.
- Zawiń strukturę `Bus`, aby uzyskać czyste API.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
-`retain`automatycznie czyści martwych subskrybentów — nie ma wycieków pamięci z powodu rozłączonych wątków.
-`message.clone()`jest konieczny, ponieważ każdy abonent potrzebuje własnej kopii. W przypadku typów, które są drogie w klonowaniu, zawiń w`Arc<T>`.
- Kanały ograniczone: zamień`mpsc::channel()`na`mpsc::sync_channel(N)`dla przeciwciśnienia —`publish`blokuje, jeśli bufor abonenta jest pełny.
- Produkcja: użyj`tokio::sync::broadcast`dla asynchronicznego pub/sub lub`flume`dla szybszego mpsc z opcjami ograniczonymi/nieograniczonymi.
---

## Streszczenie
Rust to język, który zmusza do myślenia o pamięci, własności i współbieżności - i nagradza kodem, który jest poprawny pod względem konstrukcji. Krzywa uczenia się jest realna, ale korzyści są znaczące: programy tak szybkie jak C, ale wolne od błędów wskaźnika zerowego, wyścigów danych i wycieków pamięci. Rust nie jest językiem produktywności ogólnego przeznaczenia — jest językiem systemowym, gdy liczy się zarówno poprawność, jak i wydajność. Jego rosnące zastosowanie w przemyśle (w tym w jądrze Linuksa i systemie Android) sugeruje, że będzie ono zyskiwać coraz większe znaczenie.