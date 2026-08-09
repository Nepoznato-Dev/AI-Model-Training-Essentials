---
# فراداده
عنوان: "زنگ"
توضیحات: "مرجع جامع برای زبان برنامه نویسی Rust شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [زنگ، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "40 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
# زنگ زدگی
Rust یک زبان برنامه نویسی تایپ شده و کامپایل شده است که برای اولین بار در سال 2015 منتشر شد و در ابتدا توسط Graydon Hoare در موزیلا توسعه یافت. وعده تعیین کننده Rust **ایمنی حافظه بدون جمع آوری زباله** است. این سیستم از طریق سیستم مالکیت خود به این امر دست می یابد - مجموعه قوانینی که در زمان کامپایل اجرا می شوند که کل دسته باگ ها را حذف می کند (عدم ارجاع نشانگر تهی، مسابقه داده، سرریز بافر، استفاده پس از رایگان) در حالی که کد را با سرعت C یا C++ تولید می کند.
Rust برای چندین سال متوالی به عنوان "دوست داشتنی ترین" زبان برنامه نویسی در نظرسنجی توسعه دهندگان Stack Overflow انتخاب شده است. این به طور فزاینده ای در برنامه نویسی سیستم ها، WebAssembly، ابزارهای CLI، زیرساخت های ابری و به عنوان جایگزینی برای C/C++ در زمینه های امنیتی حیاتی استفاده می شود. اکنون هسته لینوکس کد Rust را می پذیرد.
---

## چرا زنگ اهمیت دارد
- **ایمنی حافظه بدون GC**: سیستم مالکیت از نشانگرهای پوچ، مسابقه داده ها و نشانگرهای آویزان در زمان کامپایل جلوگیری می کند - با سربار زمان اجرا صفر.
- **عملکرد**: برای اکثر بارهای کاری با C/C++ مطابقت دارد یا بیشتر از آن است. بدون زباله جمع کن به معنای عدم مکث غیرقابل پیش بینی است.
- **همگامی بی باک**: سیستم نوع از مسابقه داده ها در زمان کامپایل جلوگیری می کند. اگر کامپایل شود، از نظر موضوع ایمن است.
- **ابزار مدرن**:`cargo`(ساخت سیستم + مدیریت بسته) یکی از بهترین ها در هر زبانی است.  `cargo build`، `cargo test`،`cargo doc`همگی خارج از جعبه کار می کنند.
- **WebAssembly**: پشتیبانی درجه یک برای کامپایل در WASM، عملکرد تقریباً بومی را در مرورگرها فعال می کند.
- ** پذیرش رو به رشد **: توسط AWS، Google (اندروید)، مایکروسافت (هسته ویندوز)، Cloudflare، Discord، Dropbox و Meta استفاده می شود.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **منحنی یادگیری شیب دار** | مالکیت، وام گرفتن، طول عمر در زبان های دیگر شبیه هیچ چیز نیست | برای «کتاب زنگار» وقت بگذارید. مفاهیم با تمرین کلیک کنید |
| **تدوین کند** | زمان کامپایل می تواند برای پروژه های بزرگ طولانی باشد | برای بررسی سریع نوع از`cargo check`استفاده کنید. کامپایل افزایشی کمک می کند |
| ** رسیدگی به خطاهای پرمخاطب ** |  اپراتور`Result<T, E>`و`?`نیاز به رسیدگی صریح دارند | از`anyhow`برای برنامه ها،`thiserror`برای کتابخانه ها استفاده کنید |
| **بازار کار کوچکتر** | کارهای Rust کمتر از جاوا، پایتون یا جاوا اسکریپت (اما به سرعت در حال رشد هستند) | بیشتر نقش های Rust در برنامه نویسی سیستم، رمزنگاری یا زیرساخت |
| **اکوسیستم نابالغ** | کتابخانه های کمتری نسبت به Python/Java/JS برای برخی دامنه ها | اکوسیستم به سرعت در حال رشد است. بسیاری از جعبه ها با کیفیت عالی هستند |
---

## اصول نحو
### ساختار اساسی
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

### مالکیت و قرض گرفتن
این نوآوری اصلی Rust است. هر ارزش دقیقاً یک مالک دارد. وقتی مالک از محدوده خارج می شود، مقدار حذف می شود.
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

### ساختارها، Enums، و تطبیق الگو
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

### رسیدگی به خطا
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

## نحو و الگوهای پیشرفته
### ژنریک و مرزهای صفت
Generics به شما امکان می دهد کدی را بنویسید که با هر نوع کار کند و در عین حال ایمنی کامل را حفظ کنید. صفات رفتار مشترک را تعریف می کنند.
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

### ماکروها
Rust دو نوع ماکرو دارد: اعلانی (`macro_rules!`) و رویه ای (مشتق، ویژگی، تابع مانند).
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

### تطبیق و تخریب الگوی پیشرفته
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

### بارگذاری بیش از حد اپراتور
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

### سلسله مراتب خطای سفارشی
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

## همزمانی و موازی
### مدل موضوع و همگام سازی
سیستم مالکیت Rust از مسابقه داده ها در زمان کامپایل جلوگیری می کند. ویژگی های`Send`و`Sync`ایمنی نخ را اعمال می کنند.
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

### کانال ها - ارسال پیام
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

### Async/Await with Tokio
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

### رشته های محدوده (Rust 1.63+)
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### پیکربندی Cargo.toml
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

### دستورات ضروری محموله
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### تست های واحد
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

### تست های یکپارچه سازی
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

### تست معیار
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

## قابلیت همکاری
### FFI با C
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

### فراخوانی Rust از پایتون (PyO3)
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

## الگوهای طراحی
### الگوی سازنده
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

### الگوی جدید (ایمنی نوع)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### الگوی مخزن با صفات
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### تکنیک های بهینه سازی
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

## استقرار
### تالیف متقاطع
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### استقرار داکر
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

### استقرار WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## اکوسیستم
| ابزار | هدف |
|------|---------|
| **محموله** | سیستم ساخت، مدیر بسته، اجرای آزمایشی، مولد اسناد |
| **crates.io** | رجیستری بسته (150000+ جعبه) |
| **rustfmt** | فرمت کننده کد |
| **کلیپی** | لینتر با صدها چک مفید |
| **توکیو** | زمان اجرا Async (استاندارد async Rust) |
| **سرد** | چارچوب سریال‌سازی/آسیاب‌زدایی |
| **actix-web / axum** | چارچوب های وب |
| **دیزل / sqlx** | ORMهای پایگاه داده / سازندگان پرس و جو |
---

## چه زمانی از Rust استفاده کنیم
| سناریو | چرا زنگ | جایگزین بهتر |
|----------|---------|-------------------|
| برنامه نویسی سیستم ها | ایمنی حافظه + عملکرد | C/C++ اگر به ضمانت ایمنی نیاز ندارید |
| WebAssembly | بهترین پشتیبانی WASM در کلاس | -- |
| ابزارهای CLI | سریع، تک باینری، UX عالی | به سراغ CLI های ساده تر بروید
| سیستم های تعبیه شده | بدون GC، دسترسی سخت افزاری، ایمنی | C برای تعبیه ساده تر |
| کد حیاتی عملکرد | مطابق با C/C++ سرعت | -- |
| زیرساخت ابری | پذیرش رو به رشد (AWS، Cloudflare) | به سمت توسعه سریعتر بروید |
| توسعه برنامه عمومی | منحنی یادگیری شیب دار توسعه را کند می کند | پایتون، برو، جاوا |
| پشتیبان های وب | ممکن است اما اکوسیستم جوان تر است | برو، Node.js، پایتون |
| علم داده / ML | نه اکوسیستم برای این | پایتون، R |
| اسکریپت های سریع / نمونه های اولیه | خیلی پرمخاطب و آهسته برای نوشتن | پایتون، جاوا اسکریپت |
---

## خلاصه
Rust زبانی است که شما را مجبور می‌کند در مورد حافظه، مالکیت و همزمانی فکر کنید - و کدی را به شما پاداش می‌دهد که با ساخت صحیح است. منحنی یادگیری واقعی است، اما بازده آن قابل توجه است: برنامه هایی که به سرعت C هستند اما از اشکالات نشانگر تهی، مسابقه داده ها و نشت حافظه خالی هستند. Rust یک زبان بهره وری همه منظوره نیست - زبان سیستمی است برای زمانی که صحت و عملکرد هر دو مهم هستند. پذیرش رو به رشد آن در صنعت (از جمله هسته لینوکس و اندروید) نشان می دهد که اهمیت فزاینده ای خواهد داشت.