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

#زنگ
Rust ایک مستحکم طور پر ٹائپ کی گئی، مرتب کردہ پروگرامنگ زبان ہے جو پہلی بار 2015 میں جاری کی گئی تھی، جسے اصل میں Mozilla میں Graydon Hoare نے تیار کیا تھا۔ زنگ کا واضح وعدہ **کوڑا جمع کیے بغیر میموری کی حفاظت** ہے۔ یہ اسے اپنے ملکیتی نظام کے ذریعے حاصل کرتا ہے — مرتب وقت پر نافذ قوانین کا ایک مجموعہ جو C یا C++ جتنی تیزی سے کوڈ تیار کرتے ہوئے بگز (نال پوائنٹر ڈیریفرینس، ڈیٹا ریس، بفر اوور فلوز، استعمال کے بعد مفت) کو ختم کرتا ہے۔
زنگ کو اسٹیک اوور فلو ڈویلپر سروے میں مسلسل کئی سالوں سے "سب سے زیادہ پسند کی جانے والی" پروگرامنگ زبان کے طور پر ووٹ دیا گیا ہے۔ یہ تیزی سے سسٹم پروگرامنگ، ویب اسمبلی، CLI ٹولز، کلاؤڈ انفراسٹرکچر، اور C/C++ کے متبادل کے طور پر سیکورٹی کے اہم سیاق و سباق میں استعمال ہوتا ہے۔ لینکس کرنل اب رسٹ کوڈ کو قبول کرتا ہے۔
---

## زنگ کیوں اہمیت رکھتا ہے۔
- **جی سی کے بغیر میموری کی حفاظت**: اونر شپ سسٹم null پوائنٹرز، ڈیٹا ریس، اور ڈینگلنگ پوائنٹرز کو کمپائل ٹائم پر روکتا ہے — صفر رن ٹائم اوور ہیڈ کے ساتھ۔
- **کارکردگی**: زیادہ تر کام کے بوجھ کے لیے C/C++ سے مماثل یا اس سے زیادہ۔ کوئی کوڑا اٹھانے والے کا مطلب ہے کہ کوئی غیر متوقع وقفہ نہیں۔
- **فیئرلیس کنکرنسی**: ٹائپ سسٹم کمپائل کے وقت ڈیٹا کی دوڑ کو روکتا ہے۔ اگر یہ مرتب کرتا ہے تو یہ تھریڈ سیف ہے۔
- **جدید ٹولنگ**:`cargo`(بلڈ سسٹم + پیکیج مینیجر) کسی بھی زبان میں بہترین میں سے ایک ہے۔ `cargo build`,`cargo test`,`cargo doc`تمام کام باکس سے باہر ہیں۔
- **WebAssembly**: WASM کو مرتب کرنے کے لیے فرسٹ کلاس سپورٹ، براؤزرز میں قریبی مقامی کارکردگی کو فعال کرنا۔
- **بڑھتی ہوئی اپنائیت**: AWS، Google (Android)، Microsoft (Windows kernel)، Cloudflare، Discord، Dropbox، اور Meta کے ذریعے استعمال کیا جاتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کھڑا سیکھنے کا وکر** | ملکیت، ادھار، زندگیاں دوسری زبانوں میں کسی بھی چیز کے برعکس ہیں | "زنگ کی کتاب" میں وقت لگائیں؛ تصورات مشق کے ساتھ کلک کرتے ہیں |
| **سست تالیف** | بڑے منصوبوں کے لیے مرتب کرنے کا وقت طویل ہو سکتا ہے | فوری ٹائپ چیکنگ کے لیے`cargo check`استعمال کریں۔ اضافی تالیف میں مدد ملتی ہے |
| **وربوز ایرر ہینڈلنگ** | `Result<T, E>`اور`?`آپریٹر کو واضح ہینڈلنگ کی ضرورت ہے | ایپلی کیشنز کے لیے `anyhow`، لائبریریوں کے لیے`thiserror`استعمال کریں
| **چھوٹی جاب مارکیٹ** | جاوا، ازگر، یا جاوا اسکرپٹ (لیکن تیزی سے بڑھ رہی ہے) سے کم مورچا نوکریاں | زنگ کے زیادہ تر کردار سسٹمز پروگرامنگ، کرپٹو، یا انفراسٹرکچر میں ہوتے ہیں۔
| **نادان ماحولیاتی نظام** | کچھ ڈومینز کے لیے Python/Java/JS سے کم لائبریریاں | ماحولیاتی نظام تیزی سے بڑھ رہا ہے؛ بہت سے خانے بہترین معیار کے ہیں |
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
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

### ملکیت اور قرض لینا
یہ زنگ کی بنیادی اختراع ہے۔ ہر قدر کا بالکل ایک مالک ہوتا ہے۔ جب مالک دائرہ کار سے باہر ہو جاتا ہے تو قیمت گرا دی جاتی ہے۔
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

### سٹرکٹس، اینمز، اور پیٹرن میچنگ
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

### نقص کو ہینڈل کرنا
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

## اعلی درجے کی نحو اور نمونے۔
### عام اور خاصیت کی حدیں۔
جنرک آپ کو کوڈ لکھنے دیتے ہیں جو مکمل حفاظت کو برقرار رکھتے ہوئے کسی بھی قسم کے ساتھ کام کرتا ہے۔ خصلتیں مشترکہ رویے کی وضاحت کرتی ہیں۔
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

### میکرو
زنگ کے دو قسم کے میکرو ہوتے ہیں: اعلانیہ (`macro_rules!`) اور طریقہ کار ( اخذ، وصف، فعل کی طرح)۔
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

### ایڈوانسڈ پیٹرن میچنگ اور ڈیسٹرکچرنگ
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

### آپریٹر اوورلوڈنگ
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

### حسب ضرورت خرابی کے درجہ بندی
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

## ہم آہنگی اور ہم آہنگی
### تھریڈ ماڈل اور سنکرونائزیشن
مورچا کی ملکیت کا نظام مرتب وقت پر ڈیٹا کی دوڑ کو روکتا ہے۔`Send`اور`Sync`خصوصیات دھاگے کی حفاظت کو نافذ کرتی ہیں۔
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

### چینلز — پیغام گزر رہا ہے۔
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

### Async/Tokio کے ساتھ انتظار کریں۔
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

### اسکوپڈ تھریڈز (زنگ 1.63+)
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ
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

### Cargo.toml کنفیگریشن
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

### ضروری کارگو کمانڈز
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

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### یونٹ ٹیسٹ
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

### انٹیگریشن ٹیسٹ
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

### بینچ مارک ٹیسٹنگ
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

## انٹرآپریبلٹی
### ایف ایف آئی کے ساتھ سی
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

### ازگر سے زنگ کو کال کرنا (PyO3)
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

## ڈیزائن پیٹرن
### بلڈر پیٹرن
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

### نیو ٹائپ پیٹرن (قسم کی حفاظت)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### خصائل کے ساتھ ذخیرہ پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### کراس تالیف
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### ڈاکر کی تعیناتی۔
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

### WebAssembly تعیناتی۔
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## ماحولیاتی نظام
| ٹول | مقصد |
|------|---------|
| **کارگو** | سسٹم بنائیں، پیکیج مینیجر، ٹیسٹ رنر، ڈاکٹر جنریٹر |
| **crates.io** | پیکیج رجسٹری (150,000+ کریٹس) |
| **رسٹ ایف ایم ٹی** | کوڈ فارمیٹر |
| **کلیپی** | سینکڑوں مددگار چیک کے ساتھ لنٹر |
| **ٹوکیو** | Async رن ٹائم (async Rust کے لیے معیاری) |
| **سردے** | سیریلائزیشن/ڈی سیریلائزیشن فریم ورک |
| **ایکٹکس ویب / ایکسوم** | ویب فریم ورک |
| **ڈیزل / sqlx** | ڈیٹا بیس ORMs / استفسار کرنے والے |
---

## زنگ کب استعمال کریں۔
| منظر نامہ | زنگ کیوں | بہتر متبادل |
|------------|---------|-------------------|
| سسٹمز پروگرامنگ | میموری کی حفاظت + کارکردگی | C/C++ اگر آپ کو حفاظتی ضمانتوں کی ضرورت نہیں ہے۔
| ویب اسمبلی | بہترین درجے میں WASM سپورٹ | -- |
| CLI ٹولز | تیز، واحد بائنری، زبردست UX | آسان CLIs کے لیے جائیں |
| ایمبیڈڈ سسٹمز | کوئی جی سی، ہارڈ ویئر تک رسائی، حفاظت نہیں | سی آسان ایمبیڈڈ کے لیے |
| کارکردگی کا اہم کوڈ | C/C++ رفتار | -- |
| کلاؤڈ انفراسٹرکچر | بڑھتے ہوئے گود لینے (AWS، Cloudflare) | تیز تر ترقی کے لیے جائیں |
| عام درخواست کی ترقی | کھڑی سیکھنے کا وکر دیو کو سست کر دیتا ہے | ازگر، گو، جاوا |
| ویب بیک اینڈز | ممکن ہے لیکن ماحولیاتی نظام چھوٹا ہے | Go, Node.js, Python |
| ڈیٹا سائنس / ایم ایل | اس کے لیے ماحولیاتی نظام نہیں | ازگر، آر |
| فوری اسکرپٹس / پروٹو ٹائپس | بہت لفظی اور لکھنے میں سست | Python, JavaScript |
---

## مصنوعی سوال و جواب
### Q1: ملکیت کا نظام کیا ہے، اور یہ زنگ کیوں ہوتا ہے؟
**A:** زنگ میں ہر قدر کا بالکل ایک مالک ہوتا ہے۔ جب مالک دائرہ کار سے باہر ہو جاتا ہے، تو قدر گرا دی جاتی ہے (میموری آزاد)۔ یہ میموری کی حفاظت کی ضمانت دیتے ہوئے کوڑا اٹھانے والے کی ضرورت کو ختم کرتا ہے۔ تفویض، فنکشن پیرامیٹرز، اور واپسی کی قدریں تمام منتقلی ملکیت ("منتقل")۔ منتقلی کے بغیر اشتراک کرنے کے لیے، حوالہ جات استعمال کریں۔ مرتب کرنے والا نافذ کرتا ہے: آپ کے پاس ایک ہی قیمت کا ایک متغیر حوالہ اور ایک ناقابل تغیر حوالہ بیک وقت نہیں ہوسکتا ہے۔
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2: مجھے`String`بمقابلہ`&str`کب استعمال کرنا چاہیے؟
**A:**`String`ایک ملکیتی، ہیپ سے مختص، بڑھنے کے قابل UTF-8 سٹرنگ ہے۔ `&str`UTF-8 سٹرنگ سلائس کا ایک مستعار حوالہ ہے (`String`، ایک سٹرنگ لٹریل، یا کسی ایک حصے کی طرف اشارہ کر سکتا ہے)۔`String`استعمال کریں جب آپ کو سٹرنگ کا مالک ہونا، اس میں ترمیم کرنا یا اسے بنانے کی ضرورت ہے۔ فنکشن پیرامیٹرز کے لیے`&str`استعمال کریں (زیادہ لچکدار — دونوں کو قبول کرتا ہے)، صرف پڑھنے کے نظارے، اور سٹرنگ لٹریلز۔ فنکشن دستخطوں میں`&str`قبول کریں؛ جب کال کرنے والے کو ملکیت کی ضرورت ہو تو`String`واپس کریں۔
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: Rust بغیر کسی استثناء کے غلطیوں کو کیسے ہینڈل کرتا ہے؟
**A:** زنگ قابل بازیافت غلطیوں کے لیے`Result<T, E>`enum اور ناقابل بازیافت غلطیوں کے لیے`panic!`استعمال کرتا ہے۔ وہ فنکشنز جو ناکام ہو سکتے ہیں واپس`Result`۔`?`آپریٹر غلطیوں کو اختصار کے ساتھ پھیلاتا ہے۔ یہ نقطہ نظر غلطی سے نمٹنے کو واضح بناتا ہے - آپ غلطی سے غلطی کو نظر انداز نہیں کر سکتے۔ ایپلیکیشن ایرر ہینڈلنگ (آسان سیاق و سباق) کے لیے`anyhow`اور لائبریری کی خرابی کی اقسام کے لیے`thiserror`استعمال کریں (میکروز حاصل کریں)۔
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

### Q4: زندگی کے اوقات کیا ہیں، اور مجھے ان کی تشریح کب کرنی ہوگی؟
**A:** لائف ٹائم ٹریک کرتا ہے کہ حوالہ جات کتنے عرصے تک درست ہیں۔ مرتب کرنے والا زیادہ تر معاملات میں "زندگی بھر کے ایلیشن رولز" کے ذریعے ان کا اندازہ لگاتا ہے۔ آپ کو واضح تشریحات کی ضرورت ہوتی ہے جب کمپائلر ان پٹ اور آؤٹ پٹ لائف ٹائم کے درمیان تعلق کا تعین نہیں کر سکتا — عام طور پر جب کوئی فنکشن متعدد حوالہ جات لیتا ہے اور ایک واپس کرتا ہے۔ لائف ٹائمز زیرو رن ٹائم لاگت کے ساتھ کمپائل ٹائم پر لٹکتے حوالوں کو روکتے ہیں۔
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

### Q5: `Vec<T>`، arrays اور slices میں کیا فرق ہے؟
**A:** Arrays`[T; N]`فکسڈ سائز، اسٹیک سے مختص ہیں، اور ان کی لمبائی قسم کا حصہ ہے۔ `Vec<T>`ایک قابل اضافہ، ڈھیر سے مختص مجموعہ ہے۔ سلائسز`&[T]`فیٹ پوائنٹر (پوائنٹر + لمبائی) ہیں جو کسی سرنی یا Vec کے متصل حصے کو ادھار لیتے ہیں۔ چھوٹے، مقررہ سائز کے ڈیٹا کے لیے صفوں کا استعمال کریں۔ متحرک جمع کرنے کے لیے Vec استعمال کریں۔ زیادہ سے زیادہ لچک کے لیے فنکشن پیرامیٹرز میں`&[T]`قبول کریں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: تھریڈ سیف کی-ویلیو اسٹور بنائیں
**مسئلہ کا بیان:** رسٹ میں ایک کنکرنٹ کلیدی قدر والے اسٹور کو لاگو کریں جو ڈیٹا ریس کے بغیر متعدد تھریڈز سے `get`، `set`، اور`delete`آپریشنز کو سپورٹ کرتا ہے۔ اندرونی تغیرات کا استعمال کریں اور یقینی بنائیں کہ نفاذ محاوراتی زنگ ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ایک سے زیادہ تھریڈز کو مشترکہ HashMap پر پڑھنے اور لکھنے کی ضرورت ہے۔ زنگ کا ملکیتی نظام مرتب کرنے کے وقت ڈیٹا کی دوڑ کو روکتا ہے، لیکن ہمیں مشترکہ ملکیت کے لیے اندرونی تبدیلی (`RwLock`یا`Mutex`)`Arc`میں لپیٹنے کی ضرورت ہے۔ `RwLock`متعدد ہم آہنگ قارئین یا ایک خصوصی مصنف کی اجازت دیتا ہے — پڑھنے والے بھاری کام کے بوجھ کے لیے بہتر۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- مشترکہ، دھاگے سے محفوظ رسائی کے لیے`Arc<RwLock<HashMap<K, V>>>`استعمال کریں۔
-`RwLock::read()`برائے`get`(متعدد قارئین کی اجازت ہے)۔
-`RwLock::write()`برائے`set`اور`delete`(خصوصی رسائی)۔
- صاف API کے ساتھ ڈھانچے میں لپیٹیں۔
- ہر تھریڈ کے لیے`Arc`کو کلون کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- تھریڈ سیفٹی: رسٹ کمپائلر ڈیٹا ریس کی کوئی ضمانت نہیں دیتا ہے —`RwLock`باہمی اخراج کو نافذ کرتا ہے، اور`Arc`محفوظ مشترکہ ملکیت فراہم کرتا ہے۔ اگر یہ مرتب کرتا ہے تو یہ درست ہے۔
- کارکردگی:`RwLock`پڑھنے والے بھاری کام کے بوجھ کے لیے`Mutex`سے بہتر ہے۔ لکھنے کے لیے بھاری کام کے بوجھ کے لیے،`Mutex`(سادہ، کوئی ریڈر رائٹر اوور ہیڈ) استعمال کریں۔
- پروڈکشن اپ گریڈ:`parking_lot::RwLock`(تیز، کوئی زہر نہیں، چھوٹا میموری فوٹ پرنٹ) یا`dashmap::DashMap`(لاک فری کنکرنٹ ہیش میپ) استعمال کریں۔
### مسئلہ 2: زیرو کاپی پارسر کو لاگو کریں۔
**مسئلہ کا بیان:** ایک پارسر لکھیں جو کنفیگریشن سٹرنگ جیسے`"name=Alice;age=30;role=admin"`سے کلیدی قدر کے جوڑے نکالے بغیر نئی سٹرنگز مختص کیے — صرف سٹرنگ سلائسز کا استعمال کرتے ہوئے جو ان پٹ سے لی گئی ہیں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں`key=value`جوڑوں کو`;`سے الگ کرنے کی ضرورت ہے۔ کلیدی رکاوٹ "زیرو کاپی" ہے — واپس کیے گئے ڈیٹا کو ان پٹ`&str`سے قرض لینا چاہیے، نئے`String`کو مختص نہیں کرنا چاہیے۔ اس کا مطلب ہے`Vec<(&str, &str)>`کو ان پٹ سے منسلک زندگی بھر کے ساتھ واپس کرنا۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`&str`طریقوں کا استعمال کریں (`split`,`find`, سلائسنگ) - تمام ان پٹ سے قرض لینے والے`&str`سلائسز واپس کرتے ہیں۔
- کہیں بھی`.to_string()`یا`String::from()`سے بچیں۔
- لائف ٹائم تشریح: آؤٹ پٹ ان پٹ سے لیتا ہے —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- زیرو کاپی: `split`، `split_once`، اور`trim`سبھی`&str`سلائسز واپس کرتے ہیں — کوئی ہیپ مختص نہیں۔
- لائف ٹائم ایلیژن کے اصول آؤٹ پٹ لائف ٹائم کو صحیح طریقے سے ان پٹ سے جوڑتے ہیں۔
- ایج کیسز: خالی ان پٹ`[]`واپس کرتا ہے۔ غائب`=`جوڑے کو چھوڑ دیتا ہے (`filter_map` کے ذریعے)`=`کے ارد گرد خالی جگہ کو`trim`کے ذریعے ہینڈل کیا جاتا ہے۔
- زیادہ پیچیدہ تجزیہ کے لیے،`nom`کریٹ استعمال کریں (کمبینیٹر پر مبنی، صفر کاپی بھی)۔
### مسئلہ 3: چینلز کے ساتھ مبصر پیٹرن کو نافذ کریں۔
**مسئلہ کا بیان:** ایک پبلش سبسکرائب سسٹم بنائیں جہاں ایک سے زیادہ سبسکرائبرز کو پبلشر سے پیغامات موصول ہوں۔ رسٹ چینلز کا استعمال کریں اور یقینی بنائیں کہ سسٹم ناشر کو بلاک کیے بغیر سست سبسکرائبرز کو ہینڈل کرتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ایک پبلشر کی ضرورت ہے جو متعدد سبسکرائبرز کو پیغامات بھیجے۔ زنگ کا`mpsc`چینل ملٹی پروڈیوسر سنگل کنزیومر ہے — ہمیں ریورس (سنگل پروڈیوسر ملٹی کنزیومر) کی ضرورت ہے۔ ہم`broadcast`چینلز استعمال کر سکتے ہیں (`tokio` سے ) یا متعدد`mpsc`بھیجنے والوں کا استعمال کر کے فین آؤٹ کر سکتے ہیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- معیاری چینلز کے لیے`std::sync::mpsc`استعمال کریں۔
- فین آؤٹ کے لیے: ایک`Vec<Sender<T>>`کو برقرار رکھیں اور ہر ایک کو پیغامات کلون کریں۔
- سست سبسکرائبرز کے لیے: بیک پریشر کے ساتھ`try_send`(نان بلاکنگ) یا باؤنڈڈ چینلز استعمال کریں۔
- صاف API کے لیے`Bus`ڈھانچے میں لپیٹیں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
-`retain`مردہ سبسکرائبرز کو خود بخود صاف کرتا ہے - منقطع دھاگوں سے کوئی میموری لیک نہیں ہوتی ہے۔
-`message.clone()`ضروری ہے کیونکہ ہر سبسکرائبر کو اپنی کاپی کی ضرورت ہوتی ہے۔ مہنگی سے کلون کی اقسام کے لیے،`Arc<T>`میں لپیٹیں۔
- باؤنڈڈ چینلز: بیک پریشر کے لیے`mpsc::channel()`کو`mpsc::sync_channel(N)`سے تبدیل کریں — اگر کسی سبسکرائبر کا بفر بھرا ہوا ہو تو`publish`بلاک کرتا ہے۔
- پیداوار: async pub/sub کے لیے `tokio::sync::broadcast`، یا`flume`باؤنڈڈ/ان باؤنڈ اختیارات کے ساتھ تیز mpsc کے لیے استعمال کریں۔
---

## خلاصہ
زنگ ایک ایسی زبان ہے جو آپ کو میموری، ملکیت، اور ہم آہنگی کے بارے میں سوچنے پر مجبور کرتی ہے -- اور آپ کو کوڈ سے نوازتی ہے جو تعمیر کے لحاظ سے درست ہے۔ سیکھنے کا منحنی خطوط حقیقی ہے، لیکن ادائیگی اہم ہے: ایسے پروگرام جو C جتنی تیز ہیں لیکن null پوائنٹر بگ، ڈیٹا ریس، اور میموری لیک سے پاک ہیں۔ زنگ عام مقصد کی پیداواری زبان نہیں ہے -- یہ ایک نظام کی زبان ہے جب درستگی اور کارکردگی دونوں اہم ہیں۔ صنعت میں اس کی بڑھتی ہوئی اپنائیت (بشمول لینکس کرنل اور اینڈرائیڈ) بتاتی ہے کہ یہ تیزی سے اہم ہوگا۔