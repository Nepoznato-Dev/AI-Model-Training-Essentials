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
# 鐵鏽
Rust 是一種靜態類型、編譯型程式語言，於 2015 年首次發布，最初由 Mozilla 的 Graydon Hoare 開發。 Rust 的定義承諾是**記憶體安全，無需垃圾回收**。它透過其所有權系統實現了這一目標——一組在編譯時強制執行的規則，消除了所有類型的錯誤（空指標取消引用、資料競爭、緩衝區溢位、釋放後使用），同時產生程式碼的速度與 C 或 C++ 一樣快。
Rust 連續多年被 Stack Overflow 開發者調查評為「最受歡迎」的程式語言。它越來越多地用於系統程式設計、WebAssembly、CLI 工具、雲端基礎設施，並在安全關鍵環境中作為 C/C++ 的替代品。 Linux 核心現在接受 Rust 程式碼。
---

## 為什麼鐵鏽很重要
- **無需 GC 的記憶體安全性**：所有權系統可在編譯時防止空指標、資料競爭和懸空指標 - 運行時開銷為零。
- **效能**：對於大多數工作負載，匹配或超過 C/C++。沒有垃圾收集器意味著沒有不可預測的暫停。
- **無畏並發**：類型系統可以防止編譯時的資料競爭。如果可以編譯，則它是線程安全的。
- **現代工具**：`cargo`（建置系統+套件管理器）是任何語言中最好的工具之一。 `cargo build`、`cargo test`、`cargo doc`皆開箱即用。
- **WebAssembly**：對編譯為 WASM 的一流支持，在瀏覽器中實現近乎本機的性能。
- **越來越多的採用**：由 AWS、Google (Android)、Microsoft（Windows 核心）、Cloudflare、Discord、Dropbox 和 Meta 使用。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **陡峭的學習曲線** |所有權、借用、生命週期與其他語言中的任何內容都不同 |投入時間閱讀《生鏽之書》；概念與實踐相得益彰|
| **編譯速度慢** |對於大型專案來說，編譯時間可能會很長 |使用`cargo check`進行快速類型檢查；增量編譯有幫助|
| **詳細的錯誤處理** |`Result<T, E>`和`?`運算子需要明確處理 |將`anyhow`用於應用程序，將`thiserror`用於庫 |
| **就業市場較小** | Rust 工作比 Java、Python 或 JavaScript 少（但迅速成長）|大多數 Rust 角色都在系統程式設計、加密或基礎設施中 |
| **生態係不成熟** |對於某些領域，函式庫數量少於 Python/Java/JS |生態系統正在快速發展；許多板條箱品質優良|
---

## 文法基礎知識
### 基本結構
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

### 所有權和借款
這是 Rust 的核心創新。每個值都有一個唯一的所有者。當所有者超出範圍時，該值就會被刪除。
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

### 結構體、枚舉和模式匹配
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

### 錯誤處理
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

## 進階語法和模式
### 泛型與特徵邊界
泛型可讓您編寫適用於任何類型的程式碼，同時保持完整的類型安全。特徵定義了共同的行為。
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

### 宏
Rust 有兩種巨集：聲明性（`macro_rules!`）和過程性（衍生、屬性、類別函數）。
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

### 進階模式比對和解構
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

### 運算子重載
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

### 自訂錯誤層次結構
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

## 並發與平行
### 線程模型和同步
Rust 的所有權系統可防止編譯時的資料競爭。`Send`和`Sync`特徵強制執行線程安全。
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

### 通道－訊息傳遞
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

### 使用 Tokio 進行非同步/等待
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

### 作用域執行緒 (Rust 1.63+)
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

## 專案配置與建置系統
### 專案結構
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

### Cargo.toml 配置
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

### 基本貨物指令
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

### CI/CD 管道 (GitHub Actions)
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

## 測試
### 單元測試
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

### 整合測試
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

### 基準測試
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

## 互通性
### FFI 與 C
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

### 從 Python (PyO3) 呼叫 Rust
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

## 設計模式
### 建構器模式
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

### 新型別模式（型別安全）
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### 具有特徵的儲存庫模式
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

## 效能與最佳化
### 分析工具
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

### 優化技術
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

## 部署
### 交叉編譯
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Docker 部署
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

### WebAssembly 部署
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## 生態系統
|工具|目的|
|------|---------|
| **貨物** |建置系統、套件管理器、測試運行器、文件產生器 |
| **crates.io** |包裹登記（150,000+ 條板條箱）|
| **rustfmt** |程式碼格式化程式|
| **剪輯** | Linter 有數百個有用的檢查 |
| **東京** |非同步運行時（非同步 Rust 的標準）|
| **塞爾德** |序列化/反序列化框架 |
| **actix-web / axum** | Web 框架 |
| **柴油/sqlx** |資料庫 ORM / 查詢產生器 |
---

## 何時使用 Rust
|場景|為什麼生鏽 |更好的選擇|
|----------|---------|--------------------|
|系統程式設計|記憶體安全+效能| C/C++ 如果不需要安全保證 |
|網路組裝 |一流的 WASM 支援 | --|
| CLI 工具 |快速、單一二進位、出色的使用者體驗 |尋求更簡單的 CLI |
|嵌入式系統|無GC、硬體存取、安全| C 實現更簡單的嵌入式 |
|效能關鍵程式碼 |與 C/C++ 速度相符 | --|
|雲端基礎架構|越來越多的採用（AWS、Cloudflare）|追求更快的發展 |
|通用應用程式開發 |陡峭的學習曲線會減慢開發速度| Python、Go、Java |
|網路後端 |可能，但生態系更年輕 | Go、Node.js、Python |
|資料科學/機器學習 |不是這個的生態系統| Python、R |
|快速腳本/原型|寫得太冗長又慢| Python、JavaScript |
---

## 綜合問答
### Q1：什麼是所有權系統，為什麼 Rust 有它？
**答：** Rust 中的每個值都只有一個擁有者。當所有者超出範圍時，該值將被刪除（釋放記憶體）。這消除了對垃圾收集器的需要，同時確保了記憶體安全。賦值、函數參數和回傳值都會轉移所有權（「移動」）。要共享而不轉移，請使用引用（`&T`用於借用，`&mut T`用於可變借用）。編譯器強制規定：不能同時擁有同一值的可變引用和不可變引用。
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2：我什麼時候應該使用`String`和`&str`？
**A:**`String`是一個擁有的、堆疊分配的、可增長的 UTF-8 字串。 `&str`是 UTF-8 字串切片的借用參考（可指向`String`、字串文字或兩者的一部分）。當您需要擁有、修改或建構字串時，請使用 `String`。將`&str`用於函數參數（更靈活 - 接受兩者）、唯讀視圖和字串文字。在函數簽章中接受 `&str`；當呼叫者需要所有權時傳回 `String`。
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3：Rust 如何無異常地處理錯誤？
**A:** Rust 使用`Result<T, E>`枚舉來表示可恢復的錯誤，使用`panic!`來表示不可恢復的錯誤。可能失敗的函數傳回`Result`。`?`運算子簡潔地傳播錯誤。這種方法使錯誤處理變得明確——您不能意外地忽略錯誤。使用`anyhow`進行應用程式錯誤處理（方便的上下文），使用`thiserror`進行程式庫錯誤類型（衍生巨集）。
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

### Q4：什麼是生命週期，什麼時候需要註解它們？
**答：** 生命週期追蹤引用的有效時間。在大多數情況下，編譯器會透過「生命週期省略規則」來推斷它們。當編譯器無法確定輸入和輸出生命週期之間的關係時（通常是當函數接受多個引用並傳回一個引用時），您需要明確註解。生命週期可防止編譯時出現懸空引用，運行時成本為零。
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

### Q5：`Vec<T>`、陣列和切片之間有什麼區別？
**A:** 陣列`[T; N]`是固定大小的、堆疊分配的，它們的長度是類型的一部分。 `Vec<T>`是一個可成長的、堆分配的集合。切片`&[T]`是藉用陣列或 Vec 的連續部分的胖指標（指標 + 長度）。對於小型、固定大小的資料使用陣列。使用 Vec 進行動態集合。在函數參數中接受`&[T]`以獲得最大的靈活性。
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

## 解決問題的思路
### 問題 1：建立線程安全的鍵值存儲
**問題陳述：** 在 Rust 中實現並發鍵值存儲，支援來自多個線程的`get`、`set`和`delete`操作，而無需資料競爭。使用內部可變性並確保實現是慣用的 Rust。
**第 1 步 — 了解問題：**
多個執行緒需要讀寫共享的HashMap。 Rust 的所有權系統可以防止編譯時的資料競爭，但我們需要將內部可變性（`RwLock`或`Mutex`）包裝在`Arc`中以實現共享所有權。 `RwLock`允許多個並發讀取器或一個獨佔寫入器 - 更適合讀取繁重的工作負載。
**第 2 步 — 確定方法：**
- 使用`Arc<RwLock<HashMap<K, V>>>`進行共用、執行緒安全存取。
-`RwLock::read()`用於 `get`（允許多個讀卡器）。
-`RwLock::write()`用於`set`和 `delete`（獨佔存取）。
- 使用乾淨的 API 封裝在結構中。
- 為每個執行緒克隆 `Arc`。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 執行緒安全：Rust 編譯器保證無資料爭用 —`RwLock`強制互斥，`Arc` 提供安全的共用所有權。如果編譯通過，那麼它是正確的。
- 效能：對於讀取密集型工作負載，`RwLock` 優於 `Mutex`。對於寫入量大的工作負載，請使用 `Mutex`（更簡單，無讀寫器開銷）。
- 生產升級：使用`parking_lot::RwLock`（更快，無中毒，記憶體佔用更小）或`dashmap::DashMap`（無鎖並發HashMap）。
### 問題 2：實作零拷貝解析器
**問題陳述：** 編寫一個解析器，從像`"name=Alice;age=30;role=admin"`這樣的配置字串中提取鍵值對，而不分配新字串 - 僅使用從輸入借用的字串切片。
**第 1 步 — 了解問題：**
我們需要解析由`;`分隔的`key=value`對。關鍵約束是「零複製」－傳回的資料必須從輸入`&str`借用，而不是分配新的`String`。這意味著返回`Vec<(&str, &str)>`，其生命週期與輸入相關。
**第 2 步 — 確定方法：**
- 使用`&str`方法（`split`、`find`、切片） — 所有傳回輸入借用的`&str`切片。
- 在任何地方避免`.to_string()`或 `String::from()`。
- 生命週期註解：輸出借用輸入 —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 零拷貝：`split`、`split_once`和`trim`皆回傳`&str`切片 — 無堆疊分配。
- 生命週期省略規則正確地將輸出生命週期與輸入連結。
- 邊緣情況：空輸入返回`[]`；缺少`=`會跳過該對（透過`filter_map`）；`=`周圍的空白由`trim`處理。
- 對於更複雜的解析，請使用`nom`箱（基於組合器，也是零拷貝）。
### 問題 3：使用通道實現觀察者模式
**問題陳述：** 建立一個發布-訂閱系統，其中多個訂閱者從發布者接收訊息。使用 Rust 通道並確保系統處理速度慢的訂閱者而不阻塞發布者。
**第 1 步 — 了解問題：**
我們需要一個發布者向多個訂閱者發送訊息。 Rust 的`mpsc`通道是多生產者單一消費者－我們需要相反（單一生產者多消費者）。我們可以使用`broadcast`通道（來自`tokio`）或使用多個`mpsc`發送器來實現扇出。
**第 2 步 — 確定方法：**
- 對於標準通道使用 `std::sync::mpsc`。
- 對於扇出：維護一個`Vec<Sender<T>>`並將訊息克隆到每個。
- 對於慢速訂閱者：使用 `try_send`（非阻塞）或具有背壓的有界通道。
- 包裝在`Bus`結構中以獲得乾淨的 API。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
-`retain`自動清理失效訂閱者 — 斷開連線的執行緒不會造成記憶體洩漏。
-`message.clone()`是必要的，因為每個訂閱者都需要自己的副本。對於克隆成本高昂的類型，請包裝在`Arc<T>`中。
- 有界通道：將`mpsc::channel()`替換為`mpsc::sync_channel(N)`以實現背壓 — 如果訂閱者的緩衝區已滿，`publish` 將阻塞。
- 生產：使用`tokio::sync::broadcast`進行非同步發布/訂閱，或使用`flume`取得更快的 mpsc，並具有有界/無界選項。
---

＃＃ 概括
Rust 是一種語言，它迫使您思考記憶體、所有權和並發性，並獎勵您建立正確的程式碼。學習曲線是真實的，但回報是顯著的：程式與 C 一樣快，但沒有空指標錯誤、資料競爭和記憶體洩漏。 Rust 不是一種通用的生產力語言－它是一種系統語言，適用於正確性和效能都重要的情況。它在工業界（包括 Linux 核心和 Android）的日益普及表明它將變得越來越重要。