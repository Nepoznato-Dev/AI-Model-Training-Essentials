---
# Metadata
title: "Rust"
description: "Comprehensive reference for the Rust programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# kalawang
Ang Rust ay isang statically typed, compiled programming language na unang inilabas noong 2015, na orihinal na binuo ni Graydon Hoare sa Mozilla. Ang tiyak na pangako ni Rust ay **kaligtasan sa memorya nang walang koleksyon ng basura**. Nakakamit ito sa pamamagitan ng sistema ng pagmamay-ari nito — isang hanay ng mga panuntunang ipinapatupad sa oras ng pag-compile na nag-aalis ng mga buong kategorya ng mga bug (null pointer dereference, data race, buffer overflow, use-after-free) habang gumagawa ng code na kasing bilis ng C o C++.
Ang Rust ay binoto bilang "pinakamahal" na programming language sa Stack Overflow Developer Survey sa loob ng maraming magkakasunod na taon. Ito ay lalong ginagamit sa mga system programming, WebAssembly, CLI tool, cloud infrastructure, at bilang kapalit ng C/C++ sa mga kontekstong kritikal sa seguridad. Ang Linux kernel ay tumatanggap na ngayon ng Rust code.
---

## Bakit Mahalaga ang kalawang
- **Kaligtasan sa memorya nang walang GC**: Pinipigilan ng system ng pagmamay-ari ang mga null pointer, data race, at dangling pointer sa oras ng compile — na may zero runtime overhead.
- **Pagganap**: Tumutugma o lumampas sa C/C++ para sa karamihan ng mga workload. Ang ibig sabihin ng walang basurero ay walang mga hindi inaasahang paghinto.
- **Walang takot na pagkakasabay**: Pinipigilan ng uri ng system ang mga karera ng data sa oras ng pag-compile. Kung ito ay nag-compile, ito ay thread-safe.
- **Modernong tooling**: Ang`cargo`(build system + package manager) ay isa sa pinakamahusay sa anumang wika. `cargo build`,`cargo test`,`cargo doc`lahat ay gumagana sa labas ng kahon.
- **WebAssembly**: First-class na suporta para sa pag-compile sa WASM, na nagpapagana ng halos katutubong pagganap sa mga browser.
- **Growing adoption**: Ginamit ng AWS, Google (Android), Microsoft (Windows kernel), Cloudflare, Discord, Dropbox, at Meta.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Steep learning curve** | Ang pagmamay-ari, paghiram, habang-buhay ay hindi katulad ng anumang bagay sa ibang mga wika | Mag-invest ng oras sa "The Rust Book"; ang mga konsepto ay nag-click sa pagsasanay |
| **Mabagal na compilation** | Maaaring mahaba ang oras ng pag-compile para sa malalaking proyekto | Gamitin ang`cargo check`para sa mabilis na pag-type-check; nakakatulong ang incremental compilation |
| **Verbose error handling** |  Ang`Result<T, E>`at`?`operator ay nangangailangan ng tahasang paghawak | Gamitin ang`anyhow`para sa mga application,`thiserror`para sa mga aklatan |
| **Mas maliit na market ng trabaho** | Mas kaunting mga Rust na trabaho kaysa sa Java, Python, o JavaScript (ngunit mabilis na lumalaki) | Karamihan sa mga tungkulin ng Rust ay nasa programming system, crypto, o imprastraktura |
| **Immature ecosystem** | Mas kaunting mga aklatan kaysa sa Python/Java/JS para sa ilang domain | Ang ecosystem ay mabilis na lumalaki; maraming crates ay mahusay na kalidad |
---

## Syntax Fundamentals
### Pangunahing Istruktura
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

### Pagmamay-ari at Panghihiram
Ito ang pangunahing inobasyon ni Rust. Ang bawat halaga ay may eksaktong isang may-ari. Kapag wala sa saklaw ang may-ari, ibinababa ang halaga.
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

### Mga Struct, Enum, at Pagtutugma ng Pattern
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

### Error sa Paghawak
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

## Advanced na Syntax at Mga Pattern
### Mga Generic at Mga Hangganan ng Ugali
Hinahayaan ka ng mga generic na magsulat ng code na gumagana sa anumang uri habang pinapanatili ang ganap na kaligtasan ng uri. Tinutukoy ng mga katangian ang ibinahaging pag-uugali.
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

### Mga Macro
May dalawang uri ng macro ang kalawang: declarative (`macro_rules!`) at procedural (derive, attribute, function-like).
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

### Advanced na Pagtutugma ng Pattern at Pagsira
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

### Overloading ng Operator
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

### Mga Custom na Hierarchy ng Error
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

## Concurrency at Paralelismo
### Thread Model at Synchronization
Pinipigilan ng sistema ng pagmamay-ari ng Rust ang mga karera ng data sa oras ng pag-compile. Ang mga katangiang`Send`at`Sync`ay nagpapatupad ng kaligtasan ng thread.
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

### Mga Channel — Pagpasa ng Mensahe
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

### Async/Maghintay sa Tokio
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

### Mga Saklaw na Thread (Rust 1.63+)
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

## Project Configuration at Build System
### Istraktura ng Proyekto
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

### Configuration ng Cargo.toml
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

### Mahahalagang Cargo Command
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

### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### Mga Pagsusuri sa Yunit
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

### Mga Pagsusulit sa Pagsasama
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

### Benchmark Testing
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

## Interoperability
### FFI kasama si C
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

### Pagtawag kay Rust mula sa Python (PyO3)
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

## Mga Pattern ng Disenyo
### Pattern ng Tagabuo
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

### Newtype Pattern (Kaligtasan ng Uri)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Pattern ng Repository na may Mga Katangian
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
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

### Mga Teknik sa Pag-optimize
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

## Deployment
### Cross-Compilation
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Docker Deployment
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

### WebAssembly Deployment
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## Ang Ecosystem
| Tool | Layunin |
|------|---------|
| **karga** | Bumuo ng system, package manager, test runner, doc generator |
| **crates.io** | Package registry (150,000+ crates) |
| **rustfmt** | Taga-format ng code |
| **clippy** | Linter na may daan-daang mga kapaki-pakinabang na tseke |
| **tokio** | Async runtime (ang pamantayan para sa async Rust) |
| **serde** | Serialization/deserialization framework |
| **actix-web / axum** | Mga framework sa web |
| **diesel / sqlx** | Mga ORM ng database / tagabuo ng query |
---

## Kailan Gamitin ang kalawang
| Sitwasyon | Bakit kalawang | Mas mahusay na Alternatibo |
|----------|---------|-------------------|
| System programming | Kaligtasan ng memorya + pagganap | C/C++ kung hindi mo kailangan ng mga garantiya sa kaligtasan |
| WebAssembly | Pinakamahusay na suporta sa WASM | -- |
| Mga tool sa CLI | Mabilis, solong binary, mahusay na UX | Pumunta para sa mas simpleng mga CLI |
| Mga naka-embed na system | Walang GC, hardware access, kaligtasan | C para sa mas simpleng naka-embed na |
| Code na kritikal sa pagganap | Tumutugma sa bilis ng C/C++ | -- |
| Imprastraktura ng ulap | Lumalagong pag-aampon (AWS, Cloudflare) | Pumunta para sa mas mabilis na pag-unlad |
| Pangkalahatang pag-unlad ng application | Ang matarik na curve ng pag-aaral ay nagpapabagal sa dev | Python, Go, Java |
| Mga backend sa web | Posible ngunit mas bata ang ecosystem | Pumunta, Node.js, Python |
| Data science / ML | Hindi ang ecosystem para dito | Python, R |
| Mga mabilisang script / prototype | Masyadong verbose at mabagal magsulat | Python, JavaScript |
---

## Synthetic na Q&A
### Q1: Ano ang sistema ng pagmamay-ari, at bakit mayroon nito si Rust?
**A:** Ang bawat value sa Rust ay may eksaktong isang may-ari. Kapag ang may-ari ay wala sa saklaw, ang halaga ay ibinabagsak (memory freed). Inaalis nito ang pangangailangan para sa isang kolektor ng basura habang ginagarantiyahan ang kaligtasan ng memorya. Ang pagtatalaga, mga parameter ng function, at mga halaga ng pagbabalik ay lahat ng paglilipat ng pagmamay-ari ("move"). Upang magbahagi nang hindi naglilipat, gumamit ng mga sanggunian (`&T`para sa paghiram,`&mut T`para sa nababagong paghiram). Ipinapatupad ng compiler: hindi ka maaaring magkaroon ng nababagong reference at isang hindi nababagong reference sa parehong halaga nang sabay-sabay.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2: Kailan ko dapat gamitin ang`String`vs`&str`?
**A:** Ang`String`ay isang pag-aari, heap-allocated, growable UTF-8 string.  Ang`&str`ay isang hiniram na reference sa isang UTF-8 string slice (maaaring tumuro sa isang`String`, isang string literal, o bahagi ng alinman). Gamitin ang`String`kapag kailangan mong pagmamay-ari, baguhin, o bumuo ng string. Gamitin ang`&str`para sa mga parameter ng function (mas flexible — tumatanggap ng pareho), read-only na view, at string literal. Tanggapin ang`&str`sa mga function signature; ibalik ang`String`kapag ang tumatawag ay nangangailangan ng pagmamay-ari.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: Paano pinangangasiwaan ni Rust ang mga error nang walang mga exception?
**A:** Ginagamit ng Rust ang`Result<T, E>`enum para sa mga nare-recover na error at`panic!`para sa mga hindi na mababawi. Mga function na maaaring mabigo sa pagbabalik`Result`. Ang`?`operator ay nagpapalaganap ng mga error nang maigsi. Ginagawang tahasan ng diskarteng ito ang paghawak ng error — hindi mo sinasadyang balewalain ang isang error. Gumamit ng`anyhow`para sa paghawak ng error sa application (maginhawang konteksto) at`thiserror`para sa mga uri ng error sa library (kumuha ng mga macro).
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

### Q4: Ano ang mga lifetime, at kailan ko kailangang i-annotate ang mga ito?
**A:** Sinusubaybayan ng mga habambuhay kung gaano katagal ang mga sanggunian ay wasto. Infers ng compiler ang mga ito sa karamihan ng mga kaso sa pamamagitan ng "lifetime elision rules." Kailangan mo ng mga tahasang anotasyon kapag hindi matukoy ng compiler ang kaugnayan sa pagitan ng mga buhay ng input at output — kadalasan kapag ang isang function ay tumatagal ng maraming reference at nagbabalik ng isa. Ang habambuhay ay pumipigil sa mga nakabitin na sanggunian sa oras ng pag-compile na may zero na gastos sa runtime.
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

### Q5: Ano ang pagkakaiba sa pagitan ng`Vec<T>`, arrays, at slices?
**A:** Ang mga array`[T; N]`ay fixed-size, stack-allocated, at ang haba ng mga ito ay bahagi ng uri.  Ang`Vec<T>`ay isang growable, heap-allocated na koleksyon. Ang mga hiwa`&[T]`ay mga matabang pointer (pointer + haba) na humihiram ng magkadikit na bahagi ng isang array o Vec. Gumamit ng mga array para sa maliit, fixed-size na data. Gamitin ang Vec para sa mga dynamic na koleksyon. Tanggapin ang`&[T]`sa mga parameter ng function para sa maximum na flexibility.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Tindahan ng Key-Value na Ligtas sa Thread
**Problem Statement:** Magpatupad ng kasabay na key-value store sa Rust na sumusuporta sa`get`,`set`, at`delete`na mga operasyon mula sa maraming thread na walang data race. Gumamit ng interior mutability at tiyaking ang pagpapatupad ay idiomatic Rust.
**Hakbang 1 — Unawain ang Problema:**
Maraming mga thread ang kailangang magbasa at magsulat sa isang nakabahaging HashMap. Pinipigilan ng system ng pagmamay-ari ng Rust ang mga data race sa oras ng pag-compile, ngunit kailangan namin ng interior mutability (`RwLock`o`Mutex`) na nakabalot sa`Arc`para sa shared ownership.  Binibigyang-daan ng`RwLock`ang maramihang magkakasabay na mambabasa O isang eksklusibong manunulat — mas mabuti para sa mga read-heavy workloads.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`Arc<RwLock<HashMap<K, V>>>`para sa shared, thread-safe na access.
-`RwLock::read()`para sa`get`(pinapayagan ang maraming mambabasa).
-`RwLock::write()`para sa`set`at`delete`(eksklusibong access).
- I-wrap sa isang struct na may malinis na API.
- I-clone ang`Arc`para sa bawat thread.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Kaligtasan sa thread: ginagarantiyahan ng Rust compiler na walang mga data race — ipinapatupad ng`RwLock`ang mutual exclusion, at ang`Arc`ay nagbibigay ng ligtas na ibinahaging pagmamay-ari. Kung ito ay nag-compile, ito ay tama.
- Pagganap: Ang`RwLock`ay mas mahusay kaysa sa`Mutex`para sa mga read-heavy workloads. Para sa mga write-heavy workloads, gamitin ang`Mutex`(mas simple, walang reader-writer overhead).
- Pag-upgrade sa produksyon: gumamit ng`parking_lot::RwLock`(mas mabilis, walang pagkalason, mas maliit na memory footprint) o`dashmap::DashMap`(kasabay na HashMap na walang lock).
### Problema 2: Magpatupad ng Zero-Copy Parser
**Problem Statement:** Sumulat ng parser na kumukuha ng mga key-value pairs mula sa configuration string tulad ng`"name=Alice;age=30;role=admin"`nang hindi naglalaan ng bagong Strings — gamit lang ang mga string slice na humihiram mula sa input.
**Hakbang 1 — Unawain ang Problema:**
Kailangan nating i-parse ang mga pares ng`key=value`na pinaghihiwalay ng`;`. Ang pangunahing hadlang ay "zero-copy" — ang ibinalik na data ay dapat humiram mula sa input`&str`, hindi maglaan ng bagong`String`s. Nangangahulugan ito na ibabalik ang`Vec<(&str, &str)>`na may mga habambuhay na nakatali sa input.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng mga pamamaraan ng`&str`(`split`,`find`, slicing) — lahat ay nagbabalik ng`&str`na mga hiwa na humiram mula sa input.
- Iwasan ang`.to_string()`o`String::from()`kahit saan.
- Panghabambuhay na anotasyon: humiram ang output mula sa input —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Zero-copy:`split`,`split_once`, at`trim`lahat ay nagbabalik ng`&str`slice — walang heap allocation.
- Ang mga panuntunan sa panghabambuhay na elision ay wastong itali ang mga haba ng output sa input.
- Mga kaso sa gilid: ang walang laman na input ay nagbabalik`[]`; ang nawawalang`=`ay lumalaktaw sa pares (sa pamamagitan ng`filter_map`); Ang whitespace sa paligid ng`=`ay pinangangasiwaan ng`trim`.
- Para sa mas kumplikadong pag-parse, gamitin ang`nom`crate (combinator-based, zero-copy din).
### Problema 3: Ipatupad ang Pattern ng Observer na may Mga Channel
**Problem Statement:** Bumuo ng isang publish-subscribe system kung saan maraming subscriber ang tumatanggap ng mga mensahe mula sa isang publisher. Gumamit ng mga Rust channel at tiyaking pinangangasiwaan ng system ang mga mabagal na subscriber nang hindi hinaharangan ang publisher.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng isang publisher na nagpapadala ng mga mensahe sa maraming subscriber. Ang`mpsc`channel ng Rust ay multi-producer na single-consumer — kailangan natin ang reverse (single-producer multi-consumer). Maaari kaming gumamit ng mga`broadcast`channel (mula sa`tokio`) o magpatupad ng fan-out gamit ang maramihang mga nagpapadala ng `mpsc`.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`std::sync::mpsc`para sa mga karaniwang channel.
- Para sa fan-out: panatilihin ang isang`Vec<Sender<T>>`at i-clone ang mga mensahe sa bawat isa.
- Para sa mga mabagal na subscriber: gumamit ng`try_send`(non-blocking) o mga bounded channel na may backpressure.
- I-wrap sa isang`Bus`struct para sa malinis na API.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Awtomatikong nililinis ng`retain`ang mga patay na subscriber — walang tumagas na memory mula sa mga nakadiskonektang thread.
- Kailangan ang`message.clone()`dahil kailangan ng bawat subscriber ng sarili nitong kopya. Para sa mga uri ng mahal-to-clone, balutin sa`Arc<T>`.
- Bounded channels: palitan ang`mpsc::channel()`ng`mpsc::sync_channel(N)`para sa backpressure —`publish`block kung puno na ang buffer ng subscriber.
- Produksyon: gumamit ng`tokio::sync::broadcast`para sa async na pub/sub, o`flume`para sa mas mabilis na mpsc na may mga bounded/unbounded na opsyon.
---

## Buod
Ang Rust ay isang wika na pumipilit sa iyong isipin ang tungkol sa memorya, pagmamay-ari, at pagkakatugma -- at binibigyan ka ng gantimpala ng code na tama sa pamamagitan ng pagbuo. Totoo ang curve ng pag-aaral, ngunit mahalaga ang kabayaran: mga program na kasing bilis ng C ngunit libre sa mga null pointer bug, data race, at memory leaks. Ang kalawang ay hindi isang pangkalahatang layunin na wika ng pagiging produktibo -- ito ay isang wika ng system kung kailan mahalaga ang kawastuhan at pagganap. Ang lumalagong pag-aampon nito sa industriya (kabilang ang Linux kernel at Android) ay nagpapahiwatig na ito ay lalong magiging mahalaga.