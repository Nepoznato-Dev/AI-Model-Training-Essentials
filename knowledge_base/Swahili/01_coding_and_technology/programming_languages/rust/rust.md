<!--
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

-->
#Kutu
Rust ni lugha ya programu iliyoandikwa kwa kitakwimu, iliyokusanywa kwa mara ya kwanza mnamo 2015, iliyotayarishwa asili na Graydon Hoare huko Mozilla. Ahadi ya kufafanua ya kutu ni **usalama wa kumbukumbu bila mkusanyiko wa takataka**. Inafanikisha hili kupitia mfumo wake wa umiliki - seti ya sheria zinazotekelezwa wakati wa kukusanya ambayo huondoa kategoria zote za hitilafu (kuacha marejeleo ya vielekezi visivyofaa, jamii za data, kufurika kwa bafa, matumizi baada ya bila malipo) huku ikitoa msimbo haraka kama C au C++.
Rust imepigiwa kura kuwa lugha ya programu "inayopendwa zaidi" katika Utafiti wa Wasanidi Programu wa Stack Overflow kwa miaka mingi mfululizo. Inazidi kutumika katika upangaji wa mifumo, WebAssembly, zana za CLI, miundombinu ya wingu, na kama badala ya C/C++ katika miktadha muhimu ya usalama. Kiini cha Linux sasa kinakubali msimbo wa kutu.
---

## Kwa Nini Kutu Ni Mambo
- **Usalama wa kumbukumbu bila GC**: Mfumo wa umiliki huzuia viashirio batili, mbio za data na viashirio vinavyoning'inia kwa wakati wa kukusanya - kwa kutumia muda wa sifuri wa kukimbia.
- **Utendaji**: Inalingana au inazidi C/C++ kwa mizigo mingi ya kazi. Hakuna mtoza takataka inamaanisha hakuna pause zisizotabirika.
- **Upatanishi usio na woga**: Mfumo wa aina huzuia mbio za data kwa wakati wa kukusanya. Ikiwa itajumuisha, ni salama kwa uzi.
- **Vifaa vya kisasa**:`cargo`(mfumo wa kujenga + kidhibiti kifurushi) ni mojawapo ya bora zaidi katika lugha yoyote. `cargo build`,`cargo test`,`cargo doc`zote zinafanya kazi nje ya boksi.
- **WebAssembly**: Usaidizi wa daraja la kwanza wa kuandaa WASM, unaowezesha utendaji wa karibu wa asili katika vivinjari.
- **Kukua kwa uasili**: Inatumiwa na AWS, Google (Android), Microsoft (Windows kernel), Cloudflare, Discord, Dropbox, na Meta.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Njia kali ya kujifunza** | Umiliki, kukopa, maisha ni tofauti na chochote katika lugha zingine | Wekeza wakati katika "Kitabu cha Kutu"; dhana bonyeza kwa mazoezi |
| **Mkusanyiko wa polepole** | Nyakati za kukusanya zinaweza kuwa ndefu kwa miradi mikubwa | Tumia`cargo check`kwa ukaguzi wa haraka wa aina; mkusanyiko unaoongezeka husaidia |
| **Ushughulikiaji wa makosa ya Verbose** |  Opereta`Result<T, E>`na`?`zinahitaji ushughulikiaji wazi | Tumia`anyhow`kwa programu-tumizi,`thiserror`kwa maktaba |
| **Soko dogo la ajira** | Ajira chache za kutu kuliko Java, Python, au JavaScript (lakini zinakua haraka) | Majukumu mengi ya Rust ni katika upangaji programu wa mifumo, crypto, au miundombinu |
| **Mfumo wa ikolojia ambao haujakomaa** | Maktaba chache kuliko Python/Java/JS kwa baadhi ya vikoa | Mfumo wa ikolojia unakua kwa kasi; kreti nyingi ni za ubora bora |
---

## Misingi ya Sintaksia
### Muundo Msingi
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

### Umiliki na Ukopaji
Huu ni uvumbuzi wa msingi wa Rust. Kila thamani ina mmiliki mmoja. Mmiliki anapotoka nje ya upeo, thamani imeshuka.
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

### Miundo, Enum, na Ulinganishaji wa Miundo
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

### Kushughulikia Hitilafu
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

## Sintaksia na Miundo ya Kina
### Jenerali na Mipaka ya Sifa
Jenetiki hukuruhusu kuandika msimbo unaofanya kazi na aina yoyote huku ukidumisha usalama wa aina kamili. Tabia hufafanua tabia ya pamoja.
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

### Macros
Kutu ina aina mbili za macros: declarative (`macro_rules!`) na kiutaratibu (deive, sifa, kazi-kama).
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

### Ulinganishaji wa Muundo wa Kina na Uharibifu
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

### Kupakia kwa Opereta
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

### Daraja Maalum za Hitilafu
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

## Concurrency & Usambamba
### Muundo wa Thread na Usawazishaji
Mfumo wa umiliki wa Rust huzuia mbio za data kwa wakati wa kukusanya. Sifa za`Send`na`Sync`hutekeleza usalama wa nyuzi.
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

### Vituo — Ujumbe Unapita
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

### Async/Subiri ukitumia Tokio
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

### Minyororo ya Nyuzi (Kutu 1.63+)
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi
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

Usanidi wa ### Cargo.toml
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

### Amri Muhimu za Mizigo
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

### CI/CD Bomba (Vitendo vya GitHub)
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

##Upimaji
### Vipimo vya Kitengo
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

### Majaribio ya Ujumuishaji
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

### Jaribio la Benchmark
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

## Kuingiliana
### FFI pamoja na C
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

### Kupiga Rust kutoka kwa Python (PyO3)
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

## Miundo ya Kubuni
### Muundo wa Wajenzi
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

### Mchoro wa Aina Mpya (Aina ya Usalama)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Muundo wa Hifadhi wenye Sifa
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
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

### Mbinu za Kuboresha
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

## Usambazaji
### Mkusanyiko-Mtambuka
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Usambazaji wa Docker
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

### Usambazaji wa WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## Mfumo wa Ikolojia
| Zana | Kusudi |
|------|----------|
| **mzigo** | Jenga mfumo, meneja wa kifurushi, kiendesha jaribio, jenereta ya hati |
| **makreti.io** | Sajili ya kifurushi (makreti 150,000+) |
| **rustfmt** | Mpangilio wa msimbo |
| **clippy** | Linter na mamia ya hundi muhimu |
| **tokio** | Async Rust (kiwango cha Async Rust) |
| **sede** | Mfumo wa usanifu/uondoaji bidhaa |
| **actix-web / axum** | Miundo ya wavuti |
| **dizeli / sqlx** | Hifadhidata ORMs / wajenzi wa hoja |
---

## Wakati wa Kutumia Kutu
| Hali | Kwa nini Kutu | Mbadala Bora |
|----------|---------|-------------------|
| Upangaji wa mifumo | Usalama wa kumbukumbu + utendaji | C/C++ ikiwa hauitaji dhamana za usalama |
| WebAssembly | Usaidizi bora wa WASM wa darasani | -- |
| Zana za CLI | Haraka, jozi moja, UX bora | Nenda kwa CLI rahisi zaidi |
| Mifumo iliyopachikwa | Hakuna GC, ufikiaji wa maunzi, usalama | C kwa iliyopachikwa rahisi |
| Msimbo muhimu wa utendaji | Inalingana na kasi ya C/C++ | -- |
| Miundombinu ya wingu | Kupitishwa kwa kukua (AWS, Cloudflare) | Nenda kwa maendeleo ya haraka |
| Maendeleo ya maombi ya jumla | Mwendo mwinuko wa kujifunza hupunguza dev | Python, Nenda, Java |
| Nyuma za wavuti | Inawezekana lakini mfumo wa ikolojia ni mchanga | Nenda, Node.js, Python |
| Sayansi ya data / ML | Sio mfumo ikolojia wa hii | Chatu, R |
| Hati za haraka / prototypes | Maneno mengi na polepole kuandika | Python, JavaScript |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Mfumo wa umiliki ni upi, na kwa nini Rust inayo?
**J:** Kila thamani katika Rust ina mmiliki mmoja haswa. Mmiliki anapotoka nje ya upeo, thamani hupunguzwa (kumbukumbu huru). Hii inaondoa hitaji la mtoza takataka huku ikihakikisha usalama wa kumbukumbu. Mgawo, vigezo vya utendakazi, na urejeshaji huthamini umiliki wote wa uhamishaji ("hamisha"). Ili kushiriki bila kuhamisha, tumia marejeleo (`&T`kwa kukopa,`&mut T`kwa ukopaji unaoweza kugeuzwa). Mkusanyaji anatekeleza: huwezi kuwa na marejeleo inayoweza kubadilika na rejeleo lisiloweza kubadilika la thamani sawa kwa wakati mmoja.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2: Ni lini nitumie`String`vs`&str`?
**J:**`String`ni mfuatano wa UTF-8 unaomilikiwa, uliogawiwa kwa rundo, unaoweza kukua. `&str`ni marejeleo yaliyokopwa kwa kipande cha uzi cha UTF-8 (kinaweza kuelekeza kwa`String`, mfuatano halisi, au sehemu ya mojawapo). Tumia`String`unapohitaji kumiliki, kurekebisha, au kuunda mfuatano. Tumia`&str`kwa vigezo vya utendakazi (inayonyumbulika zaidi - inakubali zote mbili), mionekano ya kusoma tu, na maandishi ya mfuatano. Kubali`&str`katika saini za kazi; rudisha`String`mpigaji simu anapohitaji umiliki.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: Rust hushughulikiaje makosa bila ubaguzi?
**J:** Rust hutumia enum ya`Result<T, E>`kwa makosa yanayoweza kurejeshwa na`panic!`kwa yale ambayo hayawezi kurekebishwa. Kazi ambazo zinaweza kushindwa kurudisha`Result`. Opereta wa`?`hueneza makosa kwa ufupi. Mbinu hii hufanya kushughulikia makosa kuwa wazi - huwezi kupuuza kosa kimakosa. Tumia`anyhow`kwa kushughulikia makosa ya programu (muktadha unaofaa) na`thiserror`kwa aina za makosa ya maktaba (deive macros).
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

### Q4: Muda wa maisha ni nini, na ni lini ninahitaji kufafanua?
**J:** Muda wa maisha hufuatilia muda ambao marejeleo ni halali. Mkusanyaji huwashawishi katika hali nyingi kupitia "sheria za kutokomeza maisha." Unahitaji ufafanuzi wazi wakati mkusanyaji hawezi kubainisha uhusiano kati ya maisha ya ingizo na matokeo - kwa kawaida wakati chaguo za kukokotoa huchukua marejeleo mengi na kurudisha moja. Muda wa maisha huzuia marejeleo yanayoning'inia wakati wa kukusanya bila gharama ya muda wa utekelezaji.
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

### Q5: Kuna tofauti gani kati ya`Vec<T>`, safu, na vipande?
**J:** Mikusanyiko`[T; N]`ni ya ukubwa usiobadilika, imetengwa kwa rafu, na urefu wake ni sehemu ya aina. `Vec<T>`ni mkusanyiko unaoweza kukua, uliogawiwa kwa rundo. Vipande`&[T]`ni viashirio vya mafuta (kielekezi + urefu) ambavyo hukopa sehemu inayoshikamana ya safu au Vec. Tumia safu kwa data ndogo, ya saizi isiyobadilika. Tumia Vec kwa mikusanyiko inayobadilika. Kubali`&[T]`katika vigezo vya utendakazi kwa unyumbufu wa juu zaidi.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tengeneza Hifadhi ya Thamani ya Ufunguo-salama
**Taarifa ya Tatizo:** Tekeleza hifadhi ya thamani ya ufunguo kwa wakati mmoja katika Rust inayoauni`get`,`set`, na uendeshaji wa`delete`kutoka kwa nyuzi nyingi bila jamii za data. Tumia kubadilika kwa mambo ya ndani na hakikisha utekelezwaji ni kutu ya nahau.
**Hatua ya 1 - Elewa Tatizo:**
Mazungumzo mengi yanahitaji kusoma na kuandika kwa HashMap iliyoshirikiwa. Mfumo wa umiliki wa Rust huzuia mbio za data kwa wakati wa kukusanya, lakini tunahitaji mabadiliko ya ndani (`RwLock`au`Mutex`) iliyofungwa kwa`Arc`kwa umiliki wa pamoja. `RwLock`inaruhusu wasomaji wengi kwa wakati mmoja AU mwandishi mmoja wa kipekee - bora kwa kazi nzito ya kusoma.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`Arc<RwLock<HashMap<K, V>>>`kwa ufikiaji wa pamoja, wa uzi-salama.
-`RwLock::read()`kwa`get`(visomaji vingi vinaruhusiwa).
-`RwLock::write()`kwa`set`na`delete`(ufikiaji wa kipekee).
- Funga kwa muundo na API safi.
- Funga`Arc`kwa kila uzi.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa nyuzi: mkusanyaji wa Rust huhakikisha hakuna mbio za data -`RwLock`hutekeleza kutengwa kwa pande zote, na`Arc`hutoa umiliki salama wa pamoja. Ikiwa hii itajumuisha, ni sawa.
- Utendaji:`RwLock`ni bora kuliko`Mutex`kwa mzigo mzito wa kazi. Kwa mzigo mzito wa maandishi, tumia`Mutex`(rahisi, hakuna kichwa cha juu cha msomaji-mwandishi).
- Uboreshaji wa uzalishaji: tumia`parking_lot::RwLock`(haraka zaidi, hakuna sumu, alama ndogo ya kumbukumbu) au`dashmap::DashMap`(HashMap inayotumika wakati mmoja bila kufuli).
### Tatizo la 2: Tekeleza Kichanganuzi cha Nakala Sifuri
**Taarifa ya Tatizo:** Andika kichanganuzi ambacho huchomoa jozi za thamani-msingi kutoka kwa mfuatano wa usanidi kama vile`"name=Alice;age=30;role=admin"`bila kutenga Mifuatano mipya - kwa kutumia vipande vya nyuzi pekee vinavyoazima kutoka kwenye ingizo.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji kuchanganua jozi za`key=value`zilizotenganishwa na`;`. Kizuizi kikuu ni "nakala sifuri" - data iliyorejeshwa lazima iazima kutoka kwa ingizo`&str`, sio kutenga`String`s mpya. Hii inamaanisha kurudisha`Vec<(&str, &str)>`na muda wa maisha ukiwa umefungwa kwenye ingizo.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia mbinu za`&str`(`split`,`find`, kukata) — zote zinarejesha vipande vya`&str`vilivyoazima kutoka kwa pembejeo.
- Epuka`.to_string()`au`String::from()`popote.
- Dokezo la maisha yote: pato hukopa kutoka kwa ingizo —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Nakala sifuri:`split`,`split_once`, na`trim`zote zinarudisha vipande vya`&str`- hakuna mgao wa lundo.
- Kanuni za kuondoa muda wa maisha hufungamanisha kwa usahihi muda wa maisha ya matokeo kwenye ingizo.
- Kesi za makali: pembejeo tupu inarudi`[]`; kukosa`=`inaruka jozi (kupitia`filter_map`); whitespace karibu na`=`inashughulikiwa na`trim`.
- Kwa uchanganuzi changamano zaidi, tumia kreti ya`nom`(msingi wa kiunganisha, pia nakala sifuri).
### Tatizo la 3: Tekeleza Mchoro wa Waangalizi kwa Idhaa
**Taarifa ya Tatizo:** Unda mfumo wa uchapishaji wa kujisajili ambapo wateja wengi wanaojisajili hupokea ujumbe kutoka kwa mchapishaji. Tumia chaneli za Rust na uhakikishe kuwa mfumo unashughulikia wanaofuatilia polepole bila kumzuia mchapishaji.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji mchapishaji mmoja kutuma ujumbe kwa watumiaji wengi wanaojisajili. Kituo cha Rust cha`mpsc`ni cha utayarishaji wengi cha mtumiaji mmoja - tunahitaji kinyume (mtayarishaji mmoja wa watumiaji wengi). Tunaweza kutumia chaneli za`broadcast`(kutoka`tokio`) au kutekeleza uondoaji wa mashabiki kwa kutumia watumaji wengi wa `mpsc`.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`std::sync::mpsc`kwa chaneli za kawaida.
- Kwa shabiki-out: kudumisha`Vec<Sender<T>>`na clone ujumbe kwa kila mmoja.
- Kwa wanaofuatilia polepole: tumia`try_send`(isiyozuia) au chaneli zilizo na msukumo wa nyuma.
- Funga muundo wa`Bus`kwa API safi.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
-`retain`husafisha watumiaji waliokufa kiotomatiki - hakuna uvujaji wa kumbukumbu kutoka kwa nyuzi ambazo hazijaunganishwa.
-`message.clone()`ni muhimu kwa sababu kila mteja anahitaji nakala yake. Kwa aina za bei ya juu-kwa-clone, funga ndani`Arc<T>`.
- Vituo vilivyo na mipaka: badilisha`mpsc::channel()`na`mpsc::sync_channel(N)`kwa shinikizo la nyuma -`publish`huzuia ikiwa bafa ya mteja imejaa.
- Uzalishaji: tumia`tokio::sync::broadcast`kwa async pub/sub, au`flume`kwa mpsc ya kasi iliyo na chaguo zilizo na mipaka/zisizo na mipaka.
---

## Muhtasari
Rust ni lugha inayokulazimisha kufikiria kuhusu kumbukumbu, umiliki, na upatanisho -- na hukupa msimbo ambao ni sahihi kulingana na ujenzi. Njia ya kujifunza ni halisi, lakini faida yake ni kubwa: programu ambazo ni haraka kama C lakini zisizo na hitilafu za vielekezi, mbio za data na uvujaji wa kumbukumbu. Kutu si lugha ya madhumuni ya jumla yenye tija -- ni lugha ya mifumo ambayo usahihi na utendaji ni muhimu. Kupitishwa kwake katika tasnia (pamoja na Linux kernel na Android) kunapendekeza kuwa itakuwa muhimu zaidi.