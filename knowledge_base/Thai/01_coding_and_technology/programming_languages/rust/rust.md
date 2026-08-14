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

#สนิม
Rust เป็นภาษาโปรแกรมคอมไพล์แบบคงที่ซึ่งเปิดตัวครั้งแรกในปี 2558 พัฒนาโดย Graydon Hoare ที่ Mozilla คำมั่นสัญญาที่กำหนดของ Rust คือ **ความปลอดภัยของหน่วยความจำโดยไม่ต้องเก็บขยะ** บรรลุสิ่งนี้ได้ผ่านระบบความเป็นเจ้าของ — ชุดของกฎที่บังคับใช้ ณ เวลาคอมไพล์ที่กำจัดข้อบกพร่องทุกประเภท (การยกเลิกตัวชี้แบบ null การแข่งขันของข้อมูล บัฟเฟอร์ล้น ใช้งานหลังเลิกใช้งาน) ในขณะที่สร้างโค้ดให้เร็วเท่ากับ C หรือ C++
Rust ได้รับการโหวตให้เป็นภาษาโปรแกรมที่ "ชื่นชอบมากที่สุด" ในการสำรวจนักพัฒนา Stack Overflow เป็นเวลาหลายปีติดต่อกัน มีการใช้กันมากขึ้นในการเขียนโปรแกรมระบบ, WebAssembly, เครื่องมือ CLI, โครงสร้างพื้นฐานคลาวด์ และแทนที่ C/C++ ในบริบทที่มีความสำคัญต่อความปลอดภัย ตอนนี้เคอร์เนล Linux ยอมรับรหัสสนิมแล้ว
---

## ทำไมเรื่องสนิม
- **ความปลอดภัยของหน่วยความจำโดยไม่มี GC**: ระบบความเป็นเจ้าของจะป้องกันพอยน์เตอร์ว่าง การแย่งของข้อมูล และพอยน์เตอร์ห้อย ณ เวลาคอมไพล์ โดยไม่มีค่าใช้จ่ายรันไทม์เป็นศูนย์
- **ประสิทธิภาพ**: ตรงหรือเกินกว่า C/C++ สำหรับปริมาณงานส่วนใหญ่ ไม่มีตัวเก็บขยะหมายความว่าจะไม่มีการหยุดชั่วคราวที่คาดเดาไม่ได้
- **การทำงานพร้อมกันอย่างไม่เกรงกลัว**: ระบบประเภทจะป้องกันการแข่งขันของข้อมูล ณ เวลารวบรวม ถ้ามันคอมไพล์ มันก็ปลอดภัยสำหรับเธรด
- **เครื่องมือสมัยใหม่**:`cargo`(ระบบบิลด์ + ตัวจัดการแพ็คเกจ) เป็นหนึ่งในเครื่องมือที่ดีที่สุดในทุกภาษา `cargo build`,`cargo test`,`cargo doc`ทั้งหมดทำงานนอกกรอบ
- **WebAssembly**: การสนับสนุนระดับเฟิร์สคลาสสำหรับการคอมไพล์ไปยัง WASM ช่วยให้สามารถใช้งานเบราว์เซอร์ได้อย่างมีประสิทธิภาพใกล้เคียงกัน
- **การนำไปใช้ที่เพิ่มขึ้น**: ใช้โดย AWS, Google (Android), Microsoft (เคอร์เนล Windows), Cloudflare, Discord, Dropbox และ Meta
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **เส้นโค้งการเรียนรู้ที่สูงชัน** | กรรมสิทธิ์ การยืม อายุการใช้งาน ไม่เหมือนในภาษาอื่น | ลงทุนใน "The Rust Book"; คลิกแนวคิดพร้อมแบบฝึกหัด |
| **รวบรวมช้า** | เวลาคอมไพล์อาจใช้เวลานานสำหรับโปรเจ็กต์ขนาดใหญ่ | ใช้`cargo check`เพื่อตรวจสอบประเภทอย่างรวดเร็ว การรวบรวมส่วนเพิ่มช่วยได้ |
| **การจัดการข้อผิดพลาดอย่างละเอียด** |  ตัวดำเนินการ`Result<T, E>`และ`?`ต้องการการจัดการ | อย่างชัดเจน ใช้`anyhow`สำหรับแอปพลิเคชัน`thiserror`สำหรับไลบรารี |
| **ตลาดงานเล็กลง** | งาน Rust น้อยกว่า Java, Python หรือ JavaScript (แต่เติบโตอย่างรวดเร็ว) | บทบาท Rust ส่วนใหญ่อยู่ในการเขียนโปรแกรมระบบ การเข้ารหัสลับ หรือโครงสร้างพื้นฐาน |
| **ระบบนิเวศที่ยังไม่สมบูรณ์** | ไลบรารีน้อยกว่า Python/Java/JS สำหรับบางโดเมน | ระบบนิเวศกำลังเติบโตอย่างรวดเร็ว หลายลังมีคุณภาพดีเยี่ยม |
---

## พื้นฐานไวยากรณ์
### โครงสร้างพื้นฐาน
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

### กรรมสิทธิ์และการยืม
นี่คือนวัตกรรมหลักของรัส ทุกค่ามีเจ้าของเพียงคนเดียว เมื่อเจ้าของอยู่นอกขอบเขต ค่าก็จะลดลง
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

### โครงสร้าง Enums และการจับคู่รูปแบบ
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

### การจัดการข้อผิดพลาด
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ข้อมูลทั่วไปและขอบเขตลักษณะ
Generics ช่วยให้คุณสามารถเขียนโค้ดที่ใช้งานได้กับทุกประเภทโดยยังคงรักษาความปลอดภัยของประเภทเต็มรูปแบบ ลักษณะกำหนดพฤติกรรมร่วมกัน
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

### มาโคร
Rust มีมาโครสองประเภท: แบบประกาศ (`macro_rules!`) และขั้นตอน (สืบทอด แอตทริบิวต์ เหมือนฟังก์ชัน)
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

### การจับคู่รูปแบบขั้นสูงและการทำลายล้าง
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

### โอเปอเรเตอร์โอเวอร์โหลด
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

### ลำดับชั้นข้อผิดพลาดที่กำหนดเอง
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### โมเดลเธรดและการซิงโครไนซ์
ระบบความเป็นเจ้าของของ Rust ป้องกันการแข่งขันของข้อมูลในเวลารวบรวม คุณลักษณะ`Send`และ`Sync`บังคับใช้ความปลอดภัยของเธรด
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

### ช่อง — การส่งข้อความ
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

### Async/รอด้วย Tokio
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

### เธรดที่กำหนดขอบเขต (Rust 1.63+)
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ
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

### การกำหนดค่า Cargo.toml
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

### คำสั่งขนส่งสินค้าที่จำเป็น
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

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### การทดสอบหน่วย
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

### การทดสอบบูรณาการ
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

### การทดสอบเกณฑ์มาตรฐาน
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

## การทำงานร่วมกัน
### FFI กับ C
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

### การเรียกสนิมจาก Python (PyO3)
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

## รูปแบบการออกแบบ
### รูปแบบตัวสร้าง
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

### รูปแบบรูปแบบใหม่ (ประเภทความปลอดภัย)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### รูปแบบพื้นที่เก็บข้อมูลพร้อมคุณสมบัติ
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### การรวบรวมข้าม
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### การปรับใช้นักเทียบท่า
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

### การปรับใช้ WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## ระบบนิเวศ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **สินค้า** | ระบบบิลด์, ตัวจัดการแพ็คเกจ, ตัวทดสอบ, ตัวสร้าง doc |
| **crates.io** | ทะเบียนแพ็คเกจ (150,000+ ลัง) |
| **สนิมfmt** | ตัวจัดรูปแบบโค้ด |
| **คลิป** | Linter พร้อมเช็คที่มีประโยชน์หลายร้อยรายการ |
| **โตเกียว** | Async runtime (มาตรฐานสำหรับ async Rust) |
| **เซิร์ด** | กรอบงานการทำให้เป็นอนุกรม/ดีซีเรียลไลซ์ |
| **actix-web / axum** | กรอบงานเว็บ |
| **ดีเซล / sqlx** | ORM ฐานข้อมูล / ตัวสร้างแบบสอบถาม |
---

## เมื่อใดจึงควรใช้สนิม
| สถานการณ์ | ทำไมต้องเป็นสนิม | ทางเลือกที่ดีกว่า |
|----------|---------|-------------------|
| การเขียนโปรแกรมระบบ | ความปลอดภัยของหน่วยความจำ + ประสิทธิภาพ | C/C++ หากคุณไม่ต้องการการรับประกันความปลอดภัย |
| เว็บแอสเซมบลี | รองรับ WASM ที่ดีที่สุดในระดับเดียวกัน | -- |
| เครื่องมือ CLI | รวดเร็ว ไบนารีเดี่ยว UX ที่ยอดเยี่ยม | เลือกใช้ CLI ที่ง่ายกว่า |
| ระบบสมองกลฝังตัว | ไม่มี GC, การเข้าถึงฮาร์ดแวร์, ความปลอดภัย | C เพื่อการฝังที่ง่ายขึ้น |
| รหัสที่มีความสำคัญต่อประสิทธิภาพ | จับคู่ความเร็ว C/C++ | -- |
| โครงสร้างพื้นฐานคลาวด์ | การนำไปใช้ที่เพิ่มขึ้น (AWS, Cloudflare) | ก้าวไปสู่การพัฒนาที่เร็วขึ้น |
| การพัฒนาแอพพลิเคชั่นทั่วไป | เส้นโค้งการเรียนรู้ที่สูงชันทำให้ dev | ช้าลง Python, Go, Java |
| แบ็กเอนด์ของเว็บ | เป็นไปได้แต่ระบบนิเวศยังอายุน้อยกว่า | ไป, Node.js, Python |
| วิทยาศาสตร์ข้อมูล / ML | ไม่ใช่ระบบนิเวศสำหรับสิ่งนี้ | หลาม, อาร์ |
| สคริปต์ด่วน / ต้นแบบ | ละเอียดเกินไปและเขียนช้าเกินไป | หลาม, จาวาสคริปต์ |
---

## คำถามและคำตอบสังเคราะห์
### Q1: ระบบความเป็นเจ้าของคืออะไร และทำไม Rust ถึงมีระบบนี้?
**A:** ทุกค่าใน Rust มีเจ้าของเพียงคนเดียวเท่านั้น เมื่อเจ้าของอยู่นอกขอบเขต ค่าจะลดลง (หน่วยความจำว่าง) ซึ่งช่วยลดความจำเป็นในการเก็บขยะในขณะที่รับประกันความปลอดภัยของหน่วยความจำ การกำหนด พารามิเตอร์ฟังก์ชัน และค่าที่ส่งคืนทั้งหมดจะโอนความเป็นเจ้าของ ("ย้าย") หากต้องการแชร์โดยไม่โอน ให้ใช้ข้อมูลอ้างอิง (`&T`สำหรับการยืม`&mut T`สำหรับการยืมที่ไม่แน่นอน) คอมไพเลอร์บังคับใช้: คุณไม่สามารถมีการอ้างอิงที่ไม่แน่นอนและการอ้างอิงที่ไม่เปลี่ยนรูปเป็นค่าเดียวกันพร้อมกันได้
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2: เมื่อใดที่ฉันควรใช้`String`กับ `&str`
**A:**`String`เป็นสตริง UTF-8 ที่จัดสรรฮีปและมีเจ้าของเองและขยายได้ `&str`เป็นการยืมการอ้างอิงไปยังส่วนสตริง UTF-8 (สามารถชี้ไปที่`String`ซึ่งเป็นสตริงลิเทอรัล หรือส่วนหนึ่งของอย่างใดอย่างหนึ่ง) ใช้`String`เมื่อคุณต้องการเป็นเจ้าของ แก้ไข หรือสร้างสตริง ใช้`&str`สำหรับพารามิเตอร์ฟังก์ชัน (ยืดหยุ่นมากขึ้น - ยอมรับทั้งสองอย่าง) มุมมองแบบอ่านอย่างเดียว และค่าสตริง ยอมรับ`&str`ในลายเซ็นฟังก์ชัน ส่งคืน`String`เมื่อผู้โทรต้องการความเป็นเจ้าของ
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: Rust จัดการกับข้อผิดพลาดโดยไม่มีข้อยกเว้นอย่างไร
**A:** Rust ใช้`Result<T, E>`enum สำหรับข้อผิดพลาดที่กู้คืนได้ และ`panic!`สำหรับข้อผิดพลาดที่ไม่สามารถกู้คืนได้ ฟังก์ชันที่ไม่สามารถส่งคืน`Result`ได้ ตัวดำเนินการ`?`เผยแพร่ข้อผิดพลาดอย่างกระชับ แนวทางนี้ทำให้การจัดการข้อผิดพลาดมีความชัดเจน คุณไม่สามารถเพิกเฉยต่อข้อผิดพลาดโดยไม่ตั้งใจได้ ใช้`anyhow`สำหรับการจัดการข้อผิดพลาดของแอปพลิเคชัน (บริบทที่สะดวก) และ`thiserror`สำหรับประเภทข้อผิดพลาดของไลบรารี (มาโครที่รับมา)
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

### คำถามที่ 4: อายุการใช้งานคืออะไร และฉันต้องใส่คำอธิบายประกอบเมื่อใด
**ตอบ:** อายุการใช้งานจะติดตามว่าข้อมูลอ้างอิงมีอายุการใช้งานนานเท่าใด คอมไพลเลอร์อนุมานสิ่งเหล่านั้นในกรณีส่วนใหญ่ผ่าน "กฎการกำจัดตลอดชีวิต" คุณต้องมีคำอธิบายประกอบที่ชัดเจนเมื่อคอมไพลเลอร์ไม่สามารถระบุความสัมพันธ์ระหว่างอายุการใช้งานอินพุตและเอาท์พุตได้ โดยทั่วไปเมื่อฟังก์ชันใช้การอ้างอิงหลายครั้งและส่งกลับค่าเดียว อายุการใช้งานป้องกันการอ้างอิงห้อย ณ เวลาคอมไพล์โดยไม่มีค่าใช้จ่ายรันไทม์เป็นศูนย์
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

### Q5: อะไรคือความแตกต่างระหว่าง`Vec<T>`, อาร์เรย์ และสไลซ์?
**A:** อาร์เรย์`[T; N]`มีขนาดคงที่ จัดสรรเป็นสแต็ก และมีความยาวเป็นส่วนหนึ่งของประเภท `Vec<T>`เป็นคอลเลกชันที่จัดสรรฮีปที่เติบโตได้ Slices`&[T]`เป็นตัวชี้ไขมัน (ตัวชี้ + ความยาว) ที่ยืมส่วนที่ต่อเนื่องกันของอาร์เรย์หรือ Vec ใช้อาร์เรย์สำหรับข้อมูลขนาดเล็กและขนาดคงที่ ใช้ Vec สำหรับคอลเลกชันแบบไดนามิก ยอมรับ`&[T]`ในพารามิเตอร์ฟังก์ชันเพื่อความยืดหยุ่นสูงสุด
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

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: สร้างที่เก็บคีย์-ค่าที่ปลอดภัยสำหรับเธรด
**คำชี้แจงปัญหา:** ใช้การจัดเก็บคีย์-ค่าพร้อมกันใน Rust ที่รองรับการดำเนินการ`get`,`set`และ`delete`จากหลายเธรดโดยไม่มีการแข่งขันข้อมูล ใช้ความไม่แน่นอนภายในและให้แน่ใจว่าการใช้งานนั้นเป็นสำนวน Rust
**ขั้นตอนที่ 1 — ทำความเข้าใจปัญหา:**
จำเป็นต้องอ่านและเขียนหลายเธรดไปยัง HashMap ที่แชร์ ระบบความเป็นเจ้าของของ Rust ป้องกันการแข่งขันของข้อมูลในเวลารวบรวม แต่เราต้องการความไม่แน่นอนภายใน (`RwLock`หรือ`Mutex`) ที่ห่อด้วย`Arc`สำหรับการเป็นเจ้าของร่วมกัน `RwLock`อนุญาตให้มีเครื่องอ่านหลายเครื่องพร้อมกันหรือเครื่องเขียนพิเศษเพียงเครื่องเดียว — ดีกว่าสำหรับปริมาณงานที่มีการอ่านจำนวนมาก
**ขั้นตอนที่ 2 — ระบุแนวทาง:**
- ใช้`Arc<RwLock<HashMap<K, V>>>`สำหรับการเข้าถึงแบบแชร์และปลอดภัยสำหรับเธรด
-`RwLock::read()`สำหรับ`get`(อนุญาตให้มีผู้อ่านหลายคนได้)
-`RwLock::write()`สำหรับ`set`และ`delete`(การเข้าถึงพิเศษ)
- รวมโครงสร้างด้วย API ที่สะอาด
- โคลน`Arc`สำหรับแต่ละเธรด
**ขั้นตอนที่ 3 — ปรับใช้โซลูชัน:**
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

**ขั้นตอนที่ 4 — ตรวจสอบและเพิ่มประสิทธิภาพ:**
- ความปลอดภัยของเธรด: คอมไพเลอร์ Rust รับประกันว่าจะไม่มีการแย่งชิงข้อมูล -`RwLock`บังคับใช้การแยกออกร่วมกัน และ`Arc`ให้การเป็นเจ้าของร่วมกันอย่างปลอดภัย หากคอมไพล์สิ่งนี้ถูกต้อง
- ประสิทธิภาพ:`RwLock`ดีกว่า`Mutex`สำหรับเวิร์กโหลดที่มีการอ่านจำนวนมาก สำหรับเวิร์กโหลดที่เขียนจำนวนมาก ให้ใช้`Mutex`(ง่ายกว่า ไม่มีค่าใช้จ่ายในการเขียนของผู้อ่านและผู้เขียน)
- อัปเกรดการผลิต: ใช้`parking_lot::RwLock`(เร็วขึ้น ไม่มีพิษ ใช้หน่วยความจำน้อยลง) หรือ`dashmap::DashMap`(HashMap พร้อมกันที่ไม่มีการล็อค)
### ปัญหาที่ 2: ใช้ Zero-Copy Parser
**คำชี้แจงปัญหา:** เขียน parser ที่แยกคู่คีย์-ค่าออกจากสตริงการกำหนดค่า เช่น`"name=Alice;age=30;role=admin"`โดยไม่ต้องจัดสรรสตริงใหม่ โดยใช้เฉพาะส่วนของสตริงที่ยืมมาจากอินพุต
**ขั้นตอนที่ 1 — ทำความเข้าใจปัญหา:**
เราจำเป็นต้องแยกวิเคราะห์คู่`key=value`คั่นด้วย`;`ข้อจำกัดที่สำคัญคือ "zero-copy" — ข้อมูลที่ส่งคืนจะต้องยืมจากอินพุต`&str`ไม่ใช่จัดสรร`String`ใหม่ นี่หมายถึงการส่งคืน`Vec<(&str, &str)>`โดยมีอายุการใช้งานเชื่อมโยงกับอินพุต
**ขั้นตอนที่ 2 — ระบุแนวทาง:**
- ใช้วิธี`&str`(`split`,`find`, slicing) — ชิ้น`&str`ที่ส่งคืนทั้งหมดที่ยืมมาจากอินพุต
- หลีกเลี่ยง`.to_string()`หรือ`String::from()`ทุกที่
- คำอธิบายประกอบตลอดอายุการใช้งาน: เอาต์พุตยืมมาจากอินพุต — `fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`
**ขั้นตอนที่ 3 — ปรับใช้โซลูชัน:**
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

**ขั้นตอนที่ 4 — ตรวจสอบและเพิ่มประสิทธิภาพ:**
- Zero-copy:`split`,`split_once`และ`trim`ส่งคืนชิ้นส่วน`&str`ทั้งหมด — ไม่มีการจัดสรรฮีป
- กฎการตัดอายุการใช้งานจะเชื่อมโยงอายุการใช้งานเอาต์พุตกับอินพุตอย่างถูกต้อง
- กรณี Edge: อินพุตว่างส่งคืน`[]`; ไม่มี`=`ข้ามคู่ (ผ่าน`filter_map`); ช่องว่างรอบ ๆ`=`ได้รับการจัดการโดย `trim`
- สำหรับการแยกวิเคราะห์ที่ซับซ้อนมากขึ้น ให้ใช้ลัง`nom`(แบบใช้ตัวรวมและไม่มีการคัดลอกเช่นกัน)
### ปัญหาที่ 3: ใช้รูปแบบผู้สังเกตการณ์กับช่องสัญญาณ
**คำชี้แจงปัญหา:** สร้างระบบเผยแพร่และสมัครสมาชิกโดยที่สมาชิกหลายรายได้รับข้อความจากผู้จัดพิมพ์ ใช้ช่อง Rust และตรวจสอบให้แน่ใจว่าระบบจัดการกับสมาชิกที่ช้าโดยไม่ปิดกั้นผู้เผยแพร่
**ขั้นตอนที่ 1 — ทำความเข้าใจปัญหา:**
เราต้องการผู้เผยแพร่หนึ่งรายที่ส่งข้อความถึงสมาชิกหลายคน ช่องทาง`mpsc`ของ Rust เป็นผู้บริโภครายเดียวที่มีผู้ผลิตหลายราย - เราต้องการช่องทางย้อนกลับ (ผู้ผลิตรายเดียวที่มีผู้บริโภคหลายราย) เราสามารถใช้ช่อง`broadcast`(จาก`tokio`) หรือใช้การกระจายออกโดยใช้ผู้ส่ง`mpsc`หลายราย
**ขั้นตอนที่ 2 — ระบุแนวทาง:**
- ใช้`std::sync::mpsc`สำหรับช่องมาตรฐาน
- สำหรับการกระจายออก: รักษา`Vec<Sender<T>>`และโคลนข้อความให้กับแต่ละข้อความ
- สำหรับสมาชิกที่ช้า: ใช้`try_send`(ไม่บล็อก) หรือช่องที่มีขอบเขตพร้อม backpressure
- รวมโครงสร้าง`Bus`เพื่อ Clean API
**ขั้นตอนที่ 3 — ปรับใช้โซลูชัน:**
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

**ขั้นตอนที่ 4 — ตรวจสอบและเพิ่มประสิทธิภาพ:**
-`retain`ทำความสะอาดสมาชิกที่ใช้งานไม่ได้โดยอัตโนมัติ — ไม่มีหน่วยความจำรั่วไหลจากเธรดที่ถูกตัดการเชื่อมต่อ
-`message.clone()`เป็นสิ่งจำเป็นเนื่องจากสมาชิกแต่ละคนต้องการสำเนาของตัวเอง สำหรับประเภทการโคลนที่มีราคาแพง ให้ห่อด้วย `Arc<T>`
- ช่องที่มีขอบเขต: แทนที่`mpsc::channel()`ด้วย`mpsc::sync_channel(N)`สำหรับแรงดันย้อนกลับ —`publish`จะบล็อกหากบัฟเฟอร์ของสมาชิกเต็ม
- การผลิต: ใช้`tokio::sync::broadcast`สำหรับ async pub/sub หรือใช้`flume`เพื่อ mpsc ที่เร็วขึ้นพร้อมตัวเลือกที่มีขอบเขต/ไม่มีขอบเขต
---

## สรุป
Rust เป็นภาษาที่บังคับให้คุณคิดถึงความทรงจำ ความเป็นเจ้าของ และการทำงานพร้อมกัน และให้รางวัลแก่คุณด้วยโค้ดที่ถูกต้องจากการสร้าง เส้นโค้งการเรียนรู้นั้นมีอยู่จริง แต่ผลตอบแทนนั้นสำคัญ: โปรแกรมที่เร็วเท่ากับ C แต่ปราศจากจุดบกพร่องของตัวชี้ว่าง การแข่งขันของข้อมูล และหน่วยความจำรั่ว Rust ไม่ใช่ภาษาเพิ่มประสิทธิภาพการทำงานทั่วไป แต่เป็นภาษาของระบบที่ความถูกต้องและประสิทธิภาพมีความสำคัญทั้งคู่ การยอมรับที่เพิ่มขึ้นในอุตสาหกรรม (รวมถึงเคอร์เนล Linux และ Android) ชี้ให้เห็นว่าจะมีความสำคัญมากขึ้น