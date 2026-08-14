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

# মরিচা
মরিচা হল একটি স্থিতিশীলভাবে টাইপ করা, সংকলিত প্রোগ্রামিং ভাষা যা প্রথম 2015 সালে প্রকাশিত হয়েছিল, যা মূলত Mozilla-এ Graydon Hoare দ্বারা বিকশিত হয়েছিল। মরিচা এর সংজ্ঞায়িত প্রতিশ্রুতি হল **আবর্জনা সংগ্রহ ছাড়াই স্মৃতির নিরাপত্তা**। এটি তার মালিকানা ব্যবস্থার মাধ্যমে এটি অর্জন করে — কম্পাইলের সময় প্রয়োগ করা নিয়মের একটি সেট যা C বা C++ এর মতো দ্রুত কোড তৈরি করার সময় বাগগুলির সম্পূর্ণ বিভাগ (নাল পয়েন্টার ডিরেফারেন্স, ডেটা রেস, বাফার ওভারফ্লো, ব্যবহার-পর-মুক্ত) দূর করে।
একাধিক বছর ধরে স্ট্যাক ওভারফ্লো ডেভেলপার সার্ভেতে রাস্টকে "সবচেয়ে প্রিয়" প্রোগ্রামিং ভাষা হিসেবে ভোট দেওয়া হয়েছে। এটি ক্রমবর্ধমানভাবে সিস্টেম প্রোগ্রামিং, ওয়েব অ্যাসেম্বলি, CLI টুলস, ক্লাউড অবকাঠামো এবং নিরাপত্তা-সমালোচনামূলক প্রসঙ্গে C/C++ এর প্রতিস্থাপন হিসাবে ব্যবহৃত হচ্ছে। লিনাক্স কার্নেল এখন মরিচা কোড গ্রহণ করে।
---

## কেন মরিচা ব্যাপার
- **জিসি ছাড়া মেমরি নিরাপত্তা**: মালিকানা সিস্টেম কম্পাইলের সময় নাল পয়েন্টার, ডেটা রেস এবং ঝুলন্ত পয়েন্টারকে বাধা দেয় — শূন্য রানটাইম ওভারহেড সহ।
- **পারফরম্যান্স**: বেশিরভাগ কাজের চাপের জন্য C/C++ মেলে বা অতিক্রম করে। কোন আবর্জনা সংগ্রহকারী মানে কোন অপ্রত্যাশিত বিরতি.
- **ভয়হীন সমঝোতা**: টাইপ সিস্টেম কম্পাইলের সময় ডেটা রেস প্রতিরোধ করে। যদি এটি কম্পাইল হয়, এটি থ্রেড-নিরাপদ।
- **আধুনিক টুলিং**:`cargo`(বিল্ড সিস্টেম + প্যাকেজ ম্যানেজার) যেকোন ভাষায় অন্যতম সেরা।  `cargo build`, `cargo test`,`cargo doc`সবই বাক্সের বাইরে কাজ করে৷
- **WebAssembly**: WASM-এ কম্পাইল করার জন্য প্রথম-শ্রেণীর সমর্থন, ব্রাউজারে কাছাকাছি-নেটিভ পারফরম্যান্স সক্ষম করে।
- **ক্রমবর্ধমান গ্রহণ**: AWS, Google (Android), Microsoft (Windows kernel), Cloudflare, Discord, Dropbox এবং Meta দ্বারা ব্যবহৃত।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **খাড়া শেখার বক্ররেখা** | মালিকানা, ধার নেওয়া, জীবনকাল অন্যান্য ভাষার মত নয় | "দ্য রাস্ট বুক" এ সময় বিনিয়োগ করুন; ধারণাগুলি অনুশীলনের সাথে ক্লিক করুন |
| **ধীরে সংকলন** | কম্পাইল সময় বড় প্রকল্পের জন্য দীর্ঘ হতে পারে | দ্রুত টাইপ-পরীক্ষার জন্য`cargo check`ব্যবহার করুন; ক্রমবর্ধমান সংকলন সাহায্য করে |
| **ভার্বোস ত্রুটি পরিচালনা** | `Result<T, E>`এবং`?`অপারেটরের সুস্পষ্ট হ্যান্ডলিং প্রয়োজন | অ্যাপ্লিকেশনের জন্য `anyhow`, লাইব্রেরির জন্য`thiserror`ব্যবহার করুন |
| **ছোট চাকরীর বাজার** | জাভা, পাইথন বা জাভাস্ক্রিপ্টের চেয়ে কম মরিচা কাজ (কিন্তু দ্রুত ক্রমবর্ধমান) | বেশিরভাগ মরিচা ভূমিকা সিস্টেম প্রোগ্রামিং, ক্রিপ্টো, বা অবকাঠামো |
| ** অপরিণত ইকোসিস্টেম** | কিছু ডোমেনের জন্য Python/Java/JS এর ​​চেয়ে কম লাইব্রেরি | বাস্তুতন্ত্র দ্রুত বৃদ্ধি পাচ্ছে; অনেক ক্রেট চমৎকার মানের |
---

## সিনট্যাক্স মৌলিক
### মৌলিক কাঠামো
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

### মালিকানা এবং ধার করা
এটি মরিচা এর মূল উদ্ভাবন। প্রতিটি মান ঠিক একজন মালিক আছে. মালিক সুযোগের বাইরে গেলে, মান বাদ দেওয়া হয়।
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

### কাঠামো, এনাম এবং প্যাটার্ন ম্যাচিং
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

### ত্রুটি হ্যান্ডলিং
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক এবং বৈশিষ্ট্যের সীমানা
জেনেরিক্স আপনাকে কোড লিখতে দেয় যা সম্পূর্ণ ধরণের নিরাপত্তা বজায় রেখে যেকোন ধরণের সাথে কাজ করে। বৈশিষ্ট্যগুলি ভাগ করা আচরণকে সংজ্ঞায়িত করে।
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

### ম্যাক্রো
মরিচা দুটি ধরণের ম্যাক্রো আছে: ঘোষণামূলক (`macro_rules!`) এবং পদ্ধতিগত (উত্পন্ন, বৈশিষ্ট্য, ফাংশন-মত)।
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

### উন্নত প্যাটার্ন ম্যাচিং এবং ডিস্ট্রাকচারিং
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

### অপারেটর ওভারলোডিং
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

### কাস্টম ত্রুটি শ্রেণিবিন্যাস
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

## সামঞ্জস্য এবং সমান্তরালতা
### থ্রেড মডেল এবং সিঙ্ক্রোনাইজেশন
মরিচা এর মালিকানা সিস্টেম কম্পাইল সময়ে ডেটা রেস প্রতিরোধ করে।`Send`এবং`Sync`বৈশিষ্ট্যগুলি থ্রেড নিরাপত্তা জোরদার করে৷
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

### চ্যানেল — বার্তা পাসিং
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

### Tokio-এর সাথে Async/অপেক্ষা করুন
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

### স্কোপড থ্রেড (মরিচা 1.63+)
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
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

### Cargo.toml কনফিগারেশন
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

### প্রয়োজনীয় কার্গো কমান্ড
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

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### ইউনিট পরীক্ষা
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

### ইন্টিগ্রেশন টেস্ট
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

### বেঞ্চমার্ক টেস্টিং
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

## ইন্টারঅপারেবিলিটি
### এফএফআই এর সাথে সি
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

### পাইথন থেকে কলিং রাস্ট (PyO3)
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

## ডিজাইন প্যাটার্ন
### নির্মাতা প্যাটার্ন
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

### নিউটাইপ প্যাটার্ন (টাইপ সেফটি)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### বৈশিষ্ট্য সহ ভান্ডার প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### ক্রস-সংকলন
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### ডকার স্থাপনা
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

### ওয়েব অ্যাসেম্বলি স্থাপনা
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## ইকোসিস্টেম
| টুল | উদ্দেশ্য |
|------|---------|
| **মালপত্র** | সিস্টেম, প্যাকেজ ম্যানেজার, টেস্ট রানার, ডক জেনারেটর তৈরি করুন |
| **crates.io** | প্যাকেজ রেজিস্ট্রি (150,000+ ক্রেট) |
| **rustfmt** | কোড ফরম্যাটার |
| **ক্লিপি** | শত শত সহায়ক চেক সহ লিন্টার |
| **টোকিও** | Async রানটাইম (অসিঙ্ক মরিচা জন্য মানক) |
| **সেরদে** | সিরিয়ালাইজেশন/ডিসারিয়ালাইজেশন ফ্রেমওয়ার্ক |
| **অ্যাক্টিক্স-ওয়েব/অ্যাক্সাম** | ওয়েব ফ্রেমওয়ার্ক |
| **ডিজেল / sqlx** | ডাটাবেস ORMs / ক্যোয়ারী নির্মাতা |
---

## কখন মরিচা ব্যবহার করবেন
| দৃশ্যকল্প | কেন মরিচা | ভাল বিকল্প |
|------------|---------|---------|
| সিস্টেম প্রোগ্রামিং | মেমরি নিরাপত্তা + কর্মক্ষমতা | C/C++ যদি আপনার নিরাপত্তা গ্যারান্টির প্রয়োজন না হয় |
| ওয়েব অ্যাসেম্বলি | সেরা WASM সমর্থন | -- |
| CLI টুলস | দ্রুত, একক বাইনারি, দুর্দান্ত UX | সহজ CLIs জন্য যান |
| এমবেডেড সিস্টেম | জিসি নেই, হার্ডওয়্যার অ্যাক্সেস, নিরাপত্তা | সি সহজতর এমবেডের জন্য |
| কর্মক্ষমতা-সমালোচনা কোড | মেলে C/C++ গতি | -- |
| ক্লাউড অবকাঠামো | ক্রমবর্ধমান দত্তক গ্রহণ (AWS, Cloudflare) | দ্রুত উন্নয়নের জন্য যান |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | খাড়া শেখার বক্ররেখা দেবকে ধীর করে দেয় | পাইথন, গো, জাভা |
| ওয়েব ব্যাকএন্ড | সম্ভব কিন্তু ইকোসিস্টেম ছোট | Go, Node.js, Python |
| ডেটা সায়েন্স / এমএল | এর জন্য ইকোসিস্টেম নয় | পাইথন, আর |
| দ্রুত স্ক্রিপ্ট / প্রোটোটাইপ | খুব ভার্বস এবং লিখতে ধীর | পাইথন, জাভাস্ক্রিপ্ট |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: মালিকানা ব্যবস্থা কী এবং কেন এটি মরিচা থাকে?
**A:** মরিচা-এর প্রতিটি মানের ঠিক একজন মালিক আছে। মালিক সুযোগের বাইরে চলে গেলে, মানটি বাদ দেওয়া হয় (মেমরি মুক্ত)। এটি মেমরি সুরক্ষার গ্যারান্টি দেওয়ার সময় আবর্জনা সংগ্রহকারীর প্রয়োজনীয়তা দূর করে। অ্যাসাইনমেন্ট, ফাংশন প্যারামিটার এবং রিটার্ন মান সমস্ত হস্তান্তর মালিকানা ("মুভ")। স্থানান্তর না করে শেয়ার করতে, রেফারেন্স ব্যবহার করুন ( ধারের জন্য `&T`, পরিবর্তনযোগ্য ধারের জন্য `&mut T`)। কম্পাইলার প্রয়োগ করে: আপনার একই সাথে একই মানের পরিবর্তনযোগ্য রেফারেন্স এবং অপরিবর্তনীয় রেফারেন্স থাকতে পারে না।
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### প্রশ্ন 2: কখন আমি`String`বনাম`&str`ব্যবহার করব?
**A:**`String`হল একটি মালিকানাধীন, হিপ-বরাদ্দ, বৃদ্ধিযোগ্য UTF-8 স্ট্রিং। `&str`হল একটি UTF-8 স্ট্রিং স্লাইসের একটি ধার করা রেফারেন্স (একটি`String`, একটি স্ট্রিং আক্ষরিক, বা যেকোনো একটি অংশের দিকে নির্দেশ করতে পারে)। যখন আপনার একটি স্ট্রিং মালিকানা, পরিবর্তন বা নির্মাণের প্রয়োজন হয় তখন`String`ব্যবহার করুন৷ ফাংশন প্যারামিটারের জন্য`&str`ব্যবহার করুন (আরো নমনীয় — উভয়ই গ্রহণ করে), শুধুমাত্র পঠনযোগ্য দৃশ্য এবং স্ট্রিং লিটারেল। ফাংশন স্বাক্ষরে`&str`গ্রহণ করুন; যখন কলারের মালিকানা প্রয়োজন তখন`String`ফেরত দিন।
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### প্রশ্ন 3: মরিচা কীভাবে ব্যতিক্রম ছাড়া ত্রুটিগুলি পরিচালনা করে?
**A:** মরিচা পুনরুদ্ধারযোগ্য ত্রুটির জন্য`Result<T, E>`enum এবং অপুনরুদ্ধারযোগ্য ত্রুটিগুলির জন্য`panic!`ব্যবহার করে৷ যে ফাংশনগুলি ব্যর্থ হতে পারে সেগুলি`Result`ফেরত দেয়।`?`অপারেটর সংক্ষিপ্তভাবে ত্রুটিগুলি প্রচার করে৷ এই পদ্ধতিটি ত্রুটি পরিচালনাকে সুস্পষ্ট করে তোলে — আপনি দুর্ঘটনাক্রমে একটি ত্রুটি উপেক্ষা করতে পারবেন না। অ্যাপ্লিকেশন ত্রুটি পরিচালনার জন্য`anyhow`ব্যবহার করুন (সুবিধাজনক প্রসঙ্গ) এবং`thiserror`লাইব্রেরির ত্রুটির ধরনগুলির জন্য (ম্যাক্রো প্রাপ্ত করুন)।
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

### প্রশ্ন 4: জীবনকাল কি, এবং কখন সেগুলি টীকা করতে হবে?
**A:** লাইফটাইম ট্র্যাক করে কতক্ষণ রেফারেন্স বৈধ। কম্পাইলার বেশিরভাগ ক্ষেত্রেই "লাইফটাইম এলিশন নিয়ম" এর মাধ্যমে অনুমান করে। যখন কম্পাইলার ইনপুট এবং আউটপুট জীবনকালের মধ্যে সম্পর্ক নির্ধারণ করতে পারে না তখন আপনার স্পষ্ট টীকা দরকার - সাধারণত যখন একটি ফাংশন একাধিক রেফারেন্স নেয় এবং একটি ফেরত দেয়। লাইফটাইম শূন্য রানটাইম খরচ সহ কম্পাইল টাইমে ড্যাংলিং রেফারেন্স প্রতিরোধ করে।
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

### প্রশ্ন 5:`Vec<T>`, অ্যারে এবং স্লাইসের মধ্যে পার্থক্য কী?
**A:** অ্যারেগুলি`[T; N]`স্থির-আকার, স্ট্যাক-বরাদ্দ, এবং তাদের দৈর্ঘ্য প্রকারের অংশ। `Vec<T>`একটি বৃদ্ধিযোগ্য, গাদা-বরাদ্দ সংগ্রহ। স্লাইসগুলি`&[T]`হল ফ্যাট পয়েন্টার (পয়েন্টার + দৈর্ঘ্য) যা একটি অ্যারে বা Vec এর একটি সংলগ্ন অংশ ধার করে। ছোট, নির্দিষ্ট আকারের ডেটার জন্য অ্যারে ব্যবহার করুন। গতিশীল সংগ্রহের জন্য Vec ব্যবহার করুন। সর্বাধিক নমনীয়তার জন্য ফাংশন প্যারামিটারে`&[T]`গ্রহণ করুন।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি থ্রেড-সেফ কী-ভ্যালু স্টোর তৈরি করুন
**সমস্যা বিবৃতি:** মরিচা-এ একটি সমবর্তী কী-মানের দোকান প্রয়োগ করুন যা ডেটা রেস ছাড়াই একাধিক থ্রেড থেকে`get`,`set`, এবং`delete`অপারেশনগুলিকে সমর্থন করে৷ অভ্যন্তরীণ পরিবর্তনশীলতা ব্যবহার করুন এবং নিশ্চিত করুন যে বাস্তবায়নটি ইডিওম্যাটিক রাস্ট।
**ধাপ 1 — সমস্যাটি বুঝুন:**
একটি শেয়ার্ড হ্যাশম্যাপে একাধিক থ্রেড পড়তে এবং লিখতে হবে। মরিচা-এর মালিকানা ব্যবস্থা কম্পাইলের সময়ে ডেটা রেসকে বাধা দেয়, কিন্তু আমাদের শেয়ার্ড মালিকানার জন্য `Arc`-এ মোড়ানো অভ্যন্তরীণ পরিবর্তনশীলতা (`RwLock` বা `Mutex`) প্রয়োজন। `RwLock`একাধিক সমসাময়িক পাঠক বা একজন একচেটিয়া লেখককে অনুমতি দেয় — পড়া-ভারী কাজের চাপের জন্য আরও ভাল।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- শেয়ার করা, থ্রেড-নিরাপদ অ্যাক্সেসের জন্য`Arc<RwLock<HashMap<K, V>>>`ব্যবহার করুন।
-`get`এর জন্য`RwLock::read()`(একাধিক পাঠক অনুমোদিত)।
-`set`এবং`delete`(এক্সক্লুসিভ অ্যাক্সেস) এর জন্য `RwLock::write()`।
- একটি পরিষ্কার API দিয়ে একটি কাঠামোতে মোড়ানো।
- প্রতিটি থ্রেডের জন্য`Arc`ক্লোন করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- থ্রেড নিরাপত্তা: মরিচা কম্পাইলার কোনও ডেটা রেসের গ্যারান্টি দেয় না —`RwLock`পারস্পরিক বর্জন প্রয়োগ করে, এবং`Arc`নিরাপদ শেয়ার্ড মালিকানা প্রদান করে। যদি এই কম্পাইল, এটা সঠিক.
- কর্মক্ষমতা:`RwLock`পঠন-ভারী কাজের চাপের জন্য`Mutex`এর চেয়ে ভাল৷ লেখা-ভারী কাজের চাপের জন্য,`Mutex`ব্যবহার করুন (সহজ, কোনো পাঠক-লেখক ওভারহেড নেই)।
- উৎপাদন আপগ্রেড:`parking_lot::RwLock`(দ্রুত, কোন বিষক্রিয়া নয়, ছোট মেমরি পদচিহ্ন) বা`dashmap::DashMap`(লক-মুক্ত সমবর্তী হ্যাশম্যাপ) ব্যবহার করুন।
### সমস্যা 2: একটি জিরো-কপি পার্সার প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি পার্সার লিখুন যা নতুন স্ট্রিংগুলি বরাদ্দ না করেই `"name=Alice;age=30;role=admin"`-এর মতো কনফিগারেশন স্ট্রিং থেকে কী-মান জোড়া বের করে — শুধুমাত্র ইনপুট থেকে নেওয়া স্ট্রিং স্লাইসগুলি ব্যবহার করে৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের`key=value`জোড়াকে`;`দ্বারা পৃথক করা পার্স করতে হবে। মূল সীমাবদ্ধতা হল "শূন্য-কপি" — প্রত্যাবর্তিত ডেটা অবশ্যই`&str`ইনপুট থেকে ধার করতে হবে, নতুন`String`s বরাদ্দ না করে৷ এর মানে হল ইনপুটের সাথে আবদ্ধ জীবনকালের সাথে`Vec<(&str, &str)>`ফেরত দেওয়া।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
-`&str`পদ্ধতিগুলি ব্যবহার করুন (`split`,`find`, স্লাইসিং) — সবগুলি ইনপুট থেকে ধার নেওয়া`&str`স্লাইস ফেরত দেয়৷
-`.to_string()`বা`String::from()`কোথাও এড়িয়ে চলুন।
- লাইফটাইম টীকা: আউটপুট ইনপুট থেকে ধার করে — `fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- জিরো-কপি:`split`,`split_once`, এবং`trim`সবগুলি`&str`স্লাইস ফেরত দেয় — কোনও হিপ বরাদ্দ নেই৷
- লাইফটাইম এলিশন নিয়ম সঠিকভাবে আউটপুট লাইফটাইমকে ইনপুটের সাথে সংযুক্ত করে।
- এজ কেস: খালি ইনপুট`[]`প্রদান করে; অনুপস্থিত`=`জোড়াটি এড়িয়ে যায় (`filter_map` এর মাধ্যমে);`=`এর চারপাশে সাদা স্থান`trim`দ্বারা পরিচালিত হয়৷
- আরও জটিল পার্সিংয়ের জন্য,`nom`ক্রেট ব্যবহার করুন (সংযোজক-ভিত্তিক, এছাড়াও শূন্য-কপি)।
### সমস্যা 3: চ্যানেলের সাথে পর্যবেক্ষক প্যাটার্ন প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি প্রকাশ-সাবস্ক্রাইব সিস্টেম তৈরি করুন যেখানে একাধিক গ্রাহক একজন প্রকাশকের কাছ থেকে বার্তা পাবেন। মরিচা চ্যানেলগুলি ব্যবহার করুন এবং নিশ্চিত করুন যে সিস্টেমটি প্রকাশককে ব্লক না করে ধীর গ্রাহকদের পরিচালনা করে৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের একাধিক গ্রাহককে বার্তা পাঠানোর জন্য একজন প্রকাশকের প্রয়োজন৷ রাস্টের`mpsc`চ্যানেলটি বহু-প্রযোজক একক-ভোক্তা — আমাদের প্রয়োজন বিপরীত (একক-প্রযোজক বহু-ভোক্তা)। আমরা`broadcast`চ্যানেল ব্যবহার করতে পারি (`tokio` থেকে) অথবা একাধিক`mpsc`প্রেরক ব্যবহার করে ফ্যান-আউট বাস্তবায়ন করতে পারি।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- স্ট্যান্ডার্ড চ্যানেলের জন্য`std::sync::mpsc`ব্যবহার করুন।
- ফ্যান-আউটের জন্য: প্রতিটিতে একটি`Vec<Sender<T>>`এবং ক্লোন বার্তাগুলি বজায় রাখুন৷
- ধীর গ্রাহকদের জন্য: ব্যাকপ্রেশার সহ`try_send`(নন-ব্লকিং) বা আবদ্ধ চ্যানেল ব্যবহার করুন।
- পরিষ্কার API এর জন্য একটি`Bus`স্ট্রাকটে মোড়ানো।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
-`retain`মৃত গ্রাহকদের স্বয়ংক্রিয়ভাবে পরিষ্কার করে — সংযোগ বিচ্ছিন্ন থ্রেড থেকে কোনও মেমরি লিক হয় না।
-`message.clone()`প্রয়োজনীয় কারণ প্রতিটি গ্রাহকের নিজস্ব অনুলিপি প্রয়োজন৷ ব্যয়বহুল-থেকে-ক্লোন প্রকারের জন্য,`Arc<T>`এ মোড়ানো।
- বাউন্ডেড চ্যানেল: ব্যাকপ্রেশারের জন্য`mpsc::channel()`কে`mpsc::sync_channel(N)`দিয়ে প্রতিস্থাপন করুন —`publish`গ্রাহকের বাফার পূর্ণ হলে ব্লক করে।
- উৎপাদন: async pub/sub-এর জন্য `tokio::sync::broadcast`, বা বাউন্ডেড/আনবাউন্ডেড বিকল্পগুলির সাথে দ্রুত mpsc-এর জন্য`flume`ব্যবহার করুন।
---

## সারাংশ
মরিচা হল এমন একটি ভাষা যা আপনাকে মেমরি, মালিকানা, এবং সংমিশ্রণ সম্পর্কে চিন্তা করতে বাধ্য করে -- এবং আপনাকে কোড দিয়ে পুরস্কৃত করে যা নির্মাণ দ্বারা সঠিক। শেখার বক্ররেখা বাস্তব, কিন্তু অর্থপ্রদান তাৎপর্যপূর্ণ: যে প্রোগ্রামগুলি C এর মতো দ্রুত কিন্তু নাল পয়েন্টার বাগ, ডেটা রেস এবং মেমরি লিক থেকে মুক্ত। মরিচা একটি সাধারণ-উদ্দেশ্য উত্পাদনশীলতার ভাষা নয় -- এটি একটি সিস্টেমের ভাষা যখন সঠিকতা এবং কর্মক্ষমতা উভয়ই গুরুত্বপূর্ণ। শিল্পে এর ক্রমবর্ধমান গ্রহণ (লিনাক্স কার্নেল এবং অ্যান্ড্রয়েড সহ) পরামর্শ দেয় যে এটি ক্রমবর্ধমান গুরুত্বপূর্ণ হবে।