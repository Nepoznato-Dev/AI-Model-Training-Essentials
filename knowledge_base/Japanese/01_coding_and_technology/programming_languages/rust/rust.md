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
＃ さび
Rust は、2015 年に初めてリリースされた静的型付けのコンパイルされたプログラミング言語で、元々は Mozilla の Graydon Hoare によって開発されました。 Rust の決定的な約束は、**ガベージ コレクションを使用しないメモリの安全性**です。これは所有権システムを通じて実現されます。これはコンパイル時に適用される一連のルールであり、C または C++ と同じくらい高速にコードを生成しながら、バグのカテゴリ全体 (null ポインターの逆参照、データ競合、バッファ オーバーフロー、解放後の使用) を排除します。
Rust は、Stack Overflow Developer Survey で複数年連続で「最も愛されている」プログラミング言語に選ばれています。システム プログラミング、WebAssembly、CLI ツール、クラウド インフラストラクチャで、またセキュリティ クリティカルなコンテキストで C/C++ の代替として使用されることが増えています。 Linux カーネルは Rust コードを受け入れるようになりました。
---

## なぜ錆が重要なのか
- **GC を使用しないメモリの安全性**: 所有権システムにより、実行時のオーバーヘッドがゼロで、コンパイル時に null ポインター、データ競合、およびダングリング ポインターが防止されます。
- **パフォーマンス**: ほとんどのワークロードで C/C++ と同等かそれを上回ります。ガベージ コレクターがないということは、予測できない一時停止がないことを意味します。
- **恐れのない同時実行**: 型システムにより、コンパイル時のデータ競合が防止されます。コンパイルできれば、スレッドセーフになります。
- **最新のツール**:`cargo`(ビルド システム + パッケージ マネージャー) は、あらゆる言語の中で最高のものの 1 つです。 `cargo build`、`cargo test`、`cargo doc`はすべてすぐに機能します。
- **WebAssembly**: WASM へのコンパイルに対する最上級のサポートにより、ブラウザーでネイティブに近いパフォーマンスが可能になります。
- **採用の増加**: AWS、Google (Android)、Microsoft (Windows カーネル)、Cloudflare、Discord、Dropbox、Meta で使用されています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **急な学習曲線** |所有、借用、生涯は他の言語とは異なります。 「The Rust Book」に時間を投資してください。概念は実践で理解できる |
| **コンパイルが遅い** |大規模なプロジェクトではコンパイル時間が長くなる可能性があります。素早い型チェックには`cargo check`を使用します。インクリメンタルコンパイルが役立ちます。
| **詳細なエラー処理** | `Result<T, E>`および`?`演算子は明示的な処理が必要です。アプリケーションには `anyhow`、ライブラリには`thiserror`を使用します。
| **小規模な雇用市場** | Rust のジョブは Java、Python、JavaScript よりも少ない (ただし急速に増加) | Rust のほとんどの役割は、システム プログラミング、暗号化、またはインフラストラクチャにあります。
| **未成熟な生態系** |一部のドメインでは Python/Java/JS よりライブラリが少ない |エコシステムは急速に成長しています。多くの木枠は優れた品質です。
---

## 構文の基礎
### 基本構造
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

### 所有権と借用
これがRustの核となるイノベーションです。すべての値には 1 人の所有者がいます。所有者がスコープ外になると、値は削除されます。
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

### 構造体、列挙型、およびパターン マッチング
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

### エラー処理
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

## 高度な構文とパターン
### ジェネリックとトレイトの境界
ジェネリックを使用すると、完全な型の安全性を維持しながら、あらゆる型で動作するコードを作成できます。特性は共有される行動を定義します。
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

### マクロ
Rust には、宣言型 (`macro_rules!`) と手続き型 (派生、属性、関数のような) の 2 種類のマクロがあります。
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

### 高度なパターン マッチングと構造化
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

### 演算子のオーバーロード
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

### カスタムエラー階層
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

## 同時実行性と並列処理
### スレッドモデルと同期
Rust の所有権システムは、コンパイル時のデータ競合を防ぎます。`Send`および`Sync`トレイトは、スレッド セーフを強制します。
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

### チャネル — メッセージパッシング
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

### Tokio との非同期/待機
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

### スコープ付きスレッド (Rust 1.63+)
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

## プロジェクトの構成とシステムの構築
### プロジェクトの構造
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

### Cargo.toml の設定
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

### 必須の貨物コマンド
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

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### 単体テスト
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

### 統合テスト
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

### ベンチマークテスト
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

## 相互運用性
### C による FFI
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

### Python から Rust を呼び出す (PyO3)
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

## デザインパターン
### ビルダーパターン
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

### Newtype パターン (タイプ セーフティ)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### 特性を備えたリポジトリ パターン
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

## パフォーマンスと最適化
### プロファイリングツール
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

### 最適化手法
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

## デプロイメント
### クロスコンパイル
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Docker のデプロイメント
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

### WebAssembly のデプロイメント
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## エコシステム
|ツール |目的 |
|-----|----------|
| **貨物** |ビルド システム、パッケージ マネージャー、テスト ランナー、ドキュメント ジェネレーター |
| **crates.io** |パッケージ レジストリ (150,000+ クレート) |
| **錆びた** |コードフォーマッタ |
| **クリッピー** |何百もの役立つチェックを含むリンター |
| **トキオ** |非同期ランタイム (非同期 Rust の標準) |
| **セルデ** |シリアル化/逆シリアル化フレームワーク |
| **actix-web / axum** | Web フレームワーク |
| **ディーゼル / SQL** |データベース ORM / クエリ ビルダー |
---

## Rust を使用する場合
|シナリオ |なぜ錆びるのか |より良い代替案 |
|----------|----------|----------|
|システムプログラミング |メモリの安全性 + パフォーマンス |安全性の保証が必要ない場合は C/C++ |
|ウェブアセンブリ |クラス最高の WASM サポート | -- |
| CLI ツール |高速、単一バイナリ、優れた UX |よりシンプルな CLI を選択してください |
|組み込みシステム | GC なし、ハードウェア アクセス、安全性 |より単純な埋め込み用の C |
|パフォーマンスが重要なコード | C/C++ の速度に一致 | -- |
|クラウドインフラ |導入の拡大 (AWS、Cloudflare) |より迅速な開発を目指します |
|一般的なアプリケーション開発 |急な学習曲線により開発が遅くなる | Python、Go、Java |
| Web バックエンド |可能だがエコシステムは若い | Go、Node.js、Python |
|データ サイエンス / ML |これはエコシステムではありません |パイソン、R |
|クイックスクリプト/プロトタイプ |冗長すぎて書くのが遅い | Python、JavaScript |
---

## 総合的な Q&A
### Q1: 所有権システムとは何ですか? なぜ Rust には所有権システムがあるのですか?
**A:** Rust のすべての値には、正確に 1 人の所有者がいます。所有者がスコープ外に出ると、値は削除されます (メモリが解放されます)。これにより、メモリの安全性が保証されながら、ガベージ コレクターが不要になります。代入、関数パラメータ、および戻り値はすべて所有権を譲渡します (「移動」)。転送せずに共有するには、参照を使用します (借用の場合は `&T`、変更可能な借用の場合は `&mut T`)。コンパイラは、同じ値への可変参照と不変参照を同時に持つことはできないことを強制します。
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2:`String`と`&str`をいつ使用する必要がありますか?
**A:**`String`は、所有され、ヒープに割り当てられ、拡張可能な UTF-8 文字列です。 `&str`は、UTF-8 文字列スライスへの借用参照です (`String`、文字列リテラル、またはその一部を指すことができます)。文字列を所有、変更、または構築する必要がある場合は、`String` を使用します。関数パラメーター (より柔軟 - 両方を受け入れます)、読み取り専用ビュー、および文字列リテラルには`&str`を使用します。関数シグネチャで`&str`を受け入れます。呼び出し元が所有権を必要とする場合は、`String` を返します。
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: Rust は例外なくエラーをどのように処理しますか?
**A:** Rust は回復可能なエラーには`Result<T, E>`列挙型を使用し、回復不可能なエラーには`panic!`列挙型を使用します。失敗する可能性がある関数は`Result`を返します。`?`演算子はエラーを簡潔に伝播します。このアプローチにより、エラー処理が明示的になり、誤ってエラーを無視することができなくなります。アプリケーション エラー処理 (便利なコンテキスト) には`anyhow`を使用し、ライブラリ エラー タイプ (派生マクロ) には`thiserror`を使用します。
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

### Q4: ライフタイムとは何ですか?いつライフタイムに注釈を付ける必要がありますか?
**A:** ライフタイムは、参照の有効期間を追跡します。コンパイラは、ほとんどの場合、「ライフタイム省略ルール」を通じてそれらを推論します。コンパイラーが入力と出力の存続期間の関係を判断できない場合、つまり関数が複数の参照を受け取り、1 つを返す場合など、明示的なアノテーションが必要になります。ライフタイムにより、実行時のコストがゼロで、コンパイル時に未解決の参照が発生するのを防ぎます。
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

### Q5:`Vec<T>`、配列、スライスの違いは何ですか?
**A:** 配列`[T; N]`は固定サイズでスタック割り当てされ、その長さは型の一部です。 `Vec<T>`は、拡張可能なヒープ割り当てコレクションです。スライス`&[T]`は、配列または Vec の連続部分を借用するファット ポインター (ポインター + 長さ) です。小さい固定サイズのデータ​​には配列を使用します。動的コレクションには Vec を使用します。柔軟性を最大限に高めるために、関数パラメーターで`&[T]`を受け入れます。
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

## 思考連鎖による問題解決
### 問題 1: スレッドセーフな Key-Value ストアを構築する
**問題ステートメント:** データ競合のない複数のスレッドからの`get`、`set`、および`delete`操作をサポートする同時キー値ストアを Rust に実装します。内部可変性を使用し、実装が慣用的な Rust であることを確認します。
**ステップ 1 — 問題を理解する:**
複数のスレッドが共有 HashMap の読み取りと書き込みを行う必要があります。 Rust の所有権システムはコンパイル時のデータ競合を防ぎますが、共有所有権のために`Arc`でラップされた内部可変性 (`RwLock`または`Mutex`) が必要です。 `RwLock`では、複数の同時読み取りまたは 1 つの排他的書き込みが可能で、読み取り負荷の高いワークロードに適しています。
**ステップ 2 — アプローチを特定する:**
- 共有のスレッドセーフなアクセスには`Arc<RwLock<HashMap<K, V>>>`を使用します。
-`RwLock::read()`の場合は`get`(複数のリーダーが許可されます)。
-`set`および`delete`の場合は`RwLock::write()`(排他的アクセス)。
- クリーンな API を使用して構造体でラップします。
- スレッドごとに`Arc`のクローンを作成します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- スレッド セーフ: Rust コンパイラはデータ競合がないことを保証します。`RwLock` は相互排他を強制し、`Arc` は安全な共有所有権を提供します。これでコンパイルできれば正解です。
- パフォーマンス: 読み取り負荷の高いワークロードでは、`RwLock` の方が`Mutex`よりも優れています。書き込みの多いワークロードの場合は、`Mutex` (よりシンプルでリーダー/ライターのオーバーヘッドなし) を使用します。
- 運用アップグレード:`parking_lot::RwLock`(高速、ポイズニングなし、メモリ使用量が小さい) または`dashmap::DashMap`(ロックフリーの同時実行 HashMap) を使用します。
### 問題 2: ゼロコピー パーサーの実装
**問題ステートメント:** 新しい文字列を割り当てることなく、入力から借用した文字列スライスのみを使用して、`"name=Alice;age=30;role=admin"` のような構成文字列からキーと値のペアを抽出するパーサーを作成します。
**ステップ 1 — 問題を理解する:**
`;` で区切られた`key=value`ペアを解析する必要があります。キー制約は「ゼロコピー」です。返されるデータは、新しい`String`を割り当てるのではなく、入力`&str`から借用する必要があります。これは、入力に関連付けられた有効期間を持つ`Vec<(&str, &str)>`を返すことを意味します。
**ステップ 2 — アプローチを特定する:**
-`&str`メソッド (`split`、`find`、スライス) を使用します。すべて、入力から借用した`&str`スライスを返します。
-`.to_string()`または`String::from()`はどこでも避けてください。
- ライフタイム注釈: 出力​​は入力 —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`から借用します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- ゼロコピー:`split`、`split_once`、および`trim`はすべて`&str`スライスを返します。ヒープ割り当てはありません。
- ライフタイム省略ルールは、出力ライフタイムを入力に正しく結び付けます。
- エッジケース: 空の入力は`[]`を返します。`=`が見つからない場合はペアをスキップします (`filter_map`経由)。`=`の周囲の空白は`trim`によって処理されます。
- より複雑な解析の場合は、`nom` クレート (コンビネータベース、ゼロコピー) を使用します。
### 問題 3: チャネルを使用したオブザーバー パターンの実装
**問題ステートメント:** 複数のサブスクライバーがパブリッシャーからメッセージを受信するパブリッシュ/サブスクライブ システムを構築します。 Rust チャネルを使用して、システムがパブリッシャーをブロックすることなく低速サブスクライバーを処理できるようにします。
**ステップ 1 — 問題を理解する:**
複数のサブスクライバーにメッセージを送信する 1 つのパブリッシャーが必要です。 Rust の`mpsc`チャネルはマルチプロデューサー、シングルコンシューマーです。その逆 (シングルプロデューサー、マルチコンシューマー) が必要です。`broadcast`チャネル (`tokio`から) を使用することも、複数の`mpsc`送信機を使用してファンアウトを実装することもできます。
**ステップ 2 — アプローチを特定する:**
- 標準チャネルには`std::sync::mpsc`を使用します。
- ファンアウトの場合:`Vec<Sender<T>>`を維持し、それぞれにメッセージを複製します。
- 遅いサブスクライバの場合:`try_send`(非ブロッキング) またはバックプレッシャーのある制限付きチャネルを使用します。
- クリーンな API のために`Bus`構造体でラップします。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
-`retain`は、無効なサブスクライバを自動的にクリーンアップします。切断されたスレッドによるメモリ リークはありません。
- 各サブスクライバには独自のコピーが必要なため、`message.clone()` が必要です。クローン作成にコストがかかる型の場合は、`Arc<T>`でラップします。
- 境界チャネル: バックプレッシャー用に`mpsc::channel()`を`mpsc::sync_channel(N)`に置き換えます — サブスクライバのバッファがいっぱいの場合、`publish` はブロックされます。
- 本番環境: 非同期パブリッシュ/サブスクライブには`tokio::sync::broadcast`を使用し、制限付き/制限なしオプションを備えたより高速な mpsc には`flume`を使用します。
---

＃＃ まとめ
Rust は、メモリ、所有権、同時実行性について考えることを強制する言語であり、構築時に正しいコードが得られます。学習曲線は現実のものですが、その見返りは大きく、C と同じくらい高速でありながら、ヌル ポインターのバグ、データ競合、メモリ リークのないプログラムが得られます。 Rust は汎用の生産性言語ではありません。正確さとパフォーマンスの両方が重要な場合に使用されるシステム言語です。業界 (Linux カーネルや Android を含む) での採用の増加は、その重要性がますます高まっていることを示唆しています。