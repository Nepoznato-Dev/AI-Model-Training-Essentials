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

# Ржавчина
Rust — это статически типизированный компилируемый язык программирования, впервые выпущенный в 2015 году и первоначально разработанный Грейдоном Хоаром из Mozilla. Определяющее обещание Rust — **безопасность памяти без сборки мусора**. Это достигается за счет системы владения — набора правил, применяемых во время компиляции, который устраняет целые категории ошибок (разыменование нулевого указателя, гонки данных, переполнение буфера, использование после освобождения), создавая при этом код так же быстро, как C или C++.
Rust уже несколько лет подряд признается «самым любимым» языком программирования в опросе разработчиков Stack Overflow. Он все чаще используется в системном программировании, WebAssembly, инструментах CLI, облачной инфраструктуре и в качестве замены C/C++ в контекстах, критически важных для безопасности. Ядро Linux теперь принимает код Rust.
---

## Почему ржавчина важна
- **Безопасность памяти без GC**: система владения предотвращает появление нулевых указателей, гонок за данными и висячих указателей во время компиляции — с нулевыми издержками во время выполнения.
- **Производительность**: соответствует или превосходит C/C++ для большинства рабочих нагрузок. Отсутствие сборщика мусора означает отсутствие непредсказуемых пауз.
- **Бесстрашный параллелизм**: система типов предотвращает гонки данных во время компиляции. Если он компилируется, он потокобезопасен.
- **Современный инструментарий**:`cargo`(система сборки + менеджер пакетов) — один из лучших на любом языке.  `cargo build`, `cargo test`,`cargo doc`— все работают «из коробки».
- **WebAssembly**: первоклассная поддержка компиляции в WASM, обеспечивающая почти нативную производительность в браузерах.
- **Растущее распространение**: используется AWS, Google (Android), Microsoft (ядро Windows), Cloudflare, Discord, Dropbox и Meta.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Сложная кривая обучения** | Владение, заимствование, продолжительность жизни не похожи ни на что на других языках | Потратьте время на «Ржавую книгу»; концепции совпадают с практикой |
| **Медленная компиляция** | Время компиляции больших проектов может быть долгим | Используйте`cargo check`для быстрой проверки типов; помогает инкрементная компиляция |
| **Подробная обработка ошибок** |  Операторы`Result<T, E>`и`?`требуют явной обработки | Используйте`anyhow`для приложений,`thiserror`для библиотек |
| **Меньший рынок труда** | Меньше рабочих мест на Rust, чем на Java, Python или JavaScript (но быстро растет) | Большинство должностей в Rust связаны с системным программированием, криптографией или инфраструктурой |
| **Неразвитая экосистема** | Меньше библиотек, чем Python/Java/JS для некоторых доменов | Экосистема быстро растет; многие ящики отличного качества |
---

## Основы синтаксиса
### Базовая структура
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

### Право собственности и заимствование
Это основная инновация Rust. У каждого значения есть ровно один владелец. Когда владелец выходит за пределы области действия, значение удаляется.
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

### Структуры, перечисления и сопоставление с образцом
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

### Обработка ошибок
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

## Расширенный синтаксис и шаблоны
### Обобщения и границы свойств
Обобщенные шаблоны позволяют писать код, который работает с любым типом, сохраняя при этом полную безопасность типов. Черты определяют общее поведение.
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

### Макросы
В Rust есть два типа макросов: декларативные (`macro_rules!`) и процедурные (производные, атрибутивные, функциональные).
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

### Расширенное сопоставление и деструктуризация шаблонов
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

### Перегрузка оператора
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

### Пользовательские иерархии ошибок
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

## Параллелизм и параллелизм
### Модель потока и синхронизация
Система владения Rust предотвращает гонки данных во время компиляции. Признаки`Send`и`Sync`обеспечивают безопасность потоков.
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

### Каналы — передача сообщений
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

### Async/Await с Tokio
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

### Потоки с ограниченной областью действия (Rust 1.63+)
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

## Конфигурация проекта и система сборки
### Структура проекта
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

### Конфигурация Cargo.toml
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

### Основные команды по работе с грузами
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

### Конвейер CI/CD (действия GitHub)
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

## Тестирование
### Модульные тесты
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

### Интеграционные тесты
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

### Тестирование производительности
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

## Совместимость
### FFI с C
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

### Вызов Rust из Python (PyO3)
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

## Шаблоны проектирования
### Шаблон «Строитель»
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

### Шаблон Newtype (безопасность типов)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Шаблон репозитория с признаками
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

## Производительность и оптимизация
### Инструменты профилирования
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

### Методы оптимизации
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

## Развертывание
### Кросс-компиляция
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Развертывание Docker
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

### Развертывание WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## Экосистема
| Инструмент | Цель |
|------|---------|
| **груз** | Система сборки, менеджер пакетов, средство запуска тестов, генератор документов |
| **crates.io** | Реестр пакетов (более 150 000 ящиков) |
| **растфмт** | Форматер кода |
| **кратко** | Линтер с сотнями полезных проверок |
| **токио** | Асинхронная среда выполнения (стандарт асинхронной среды Rust) |
| **серде** | Платформа сериализации/десериализации |
| **actix-web / axum** | Веб-фреймворки |
| **дизель / sqlx** | ORM базы данных/построители запросов |
---

## Когда использовать Rust
| Сценарий | Почему ржавчина | Лучшая альтернатива |
|----------|---------|-------------------|
| Системное программирование | Безопасность памяти + производительность | C/C++, если вам не нужны гарантии безопасности |
| Веб-сборка | Лучшая в своем классе поддержка WASM | -- |
| Инструменты CLI | Быстрый, единый двоичный файл, отличный UX | Выбирайте более простые интерфейсы командной строки |
| Встраиваемые системы | Нет GC, доступ к оборудованию, безопасность | C для более простого встроенного |
| Код, критичный к производительности | Соответствует скорости C/C++ | -- |
| Облачная инфраструктура | Растущее внедрение (AWS, Cloudflare) | Стремитесь к более быстрому развитию |
| Общая разработка приложений | Крутая кривая обучения замедляет разработку | Питон, Го, Java |
| Веб-серверы | Возможно, но экосистема моложе | Go, Node.js, Python |
| Наука о данных / ML | Не экосистема для этого | Питон, Р |
| Быстрые скрипты/прототипы | Слишком многословно и медленно писать | Питон, JavaScript |
---

## Синтетические вопросы и ответы
### Вопрос 1: Что такое система владения и почему она есть в Rust?
**О:** Каждое значение в Rust имеет ровно одного владельца. Когда владелец выходит за пределы области действия, значение удаляется (память освобождается). Это устраняет необходимость в сборщике мусора и гарантирует безопасность памяти. Присваивание, параметры функции и возвращаемые значения переносят право собственности («перемещают»). Чтобы поделиться без передачи, используйте ссылки (`&T`для заимствования,`&mut T`для изменяемого заимствования). Компилятор обеспечивает следующее: вы не можете одновременно иметь изменяемую ссылку и неизменяемую ссылку на одно и то же значение.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Вопрос 2: Когда следует использовать `String`, а не `&str`?
**A:**`String`— это собственная, распределенная в куче, расширяемая строка UTF-8. `&str`— это заимствованная ссылка на фрагмент строки UTF-8 (может указывать на `String`, строковый литерал или их часть). Используйте `String`, когда вам нужно владеть, изменять или создавать строку. Используйте`&str`для параметров функции (более гибкий — принимает и то и другое), представлений только для чтения и строковых литералов. Примите`&str`в сигнатурах функций; верните `String`, когда вызывающему объекту необходимо владение.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Вопрос 3: Как Rust обрабатывает ошибки без исключений?
**A:** Rust использует перечисление`Result<T, E>`для устранимых ошибок и`panic!`для неисправимых. Функции, которые могут завершиться неудачей, возвращают `Result`. Оператор`?`кратко распространяет ошибки. Такой подход делает обработку ошибок явной — вы не можете случайно проигнорировать ошибку. Используйте`anyhow`для обработки ошибок приложения (удобный контекст) и`thiserror`для типов ошибок библиотеки (производные макросы).
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

### Вопрос 4. Что такое время жизни и когда мне нужно его комментировать?
**О:** Время жизни отслеживает срок действия ссылок. Компилятор выводит их в большинстве случаев с помощью «правил исключения на весь срок службы». Явные аннотации нужны, когда компилятор не может определить взаимосвязь между временем жизни входных и выходных данных — обычно, когда функция принимает несколько ссылок и возвращает одну. Время жизни предотвращает висячие ссылки во время компиляции с нулевыми затратами во время выполнения.
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

### Вопрос 5: В чем разница между`Vec<T>`, массивами и срезами?
**A:** Массивы`[T; N]`имеют фиксированный размер, распределяются в стеке, и их длина является частью типа. `Vec<T>`— это расширяемая коллекция, распределенная в куче. Срезы`&[T]`— это толстые указатели (указатель + длина), которые занимают непрерывную часть массива или Vec. Используйте массивы для небольших данных фиксированного размера. Используйте Vec для динамических коллекций. Примите`&[T]`в параметрах функции для максимальной гибкости.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создание потокобезопасного хранилища ключей и значений
**Постановка задачи:** Реализуйте параллельное хранилище значений ключа в Rust, которое поддерживает операции`get`,`set`и`delete`из нескольких потоков без гонок за данными. Используйте внутреннюю изменчивость и убедитесь, что реализация соответствует идиоматике Rust.
**Шаг 1. Поймите проблему:**
Несколько потоков должны читать и записывать в общий HashMap. Система владения Rust предотвращает гонки данных во время компиляции, но нам нужна внутренняя изменчивость (`RwLock` или `Mutex`), завернутая в`Arc`для совместного владения. `RwLock`позволяет выполнять несколько одновременных операций чтения ИЛИ одну эксклюзивную запись — лучше для рабочих нагрузок с большим количеством операций чтения.
**Шаг 2. Определите подход:**
- Используйте`Arc<RwLock<HashMap<K, V>>>`для общего поточно-безопасного доступа.
-`RwLock::read()`для`get`(разрешено несколько считывателей).
-`RwLock::write()`для`set`и`delete`(эксклюзивный доступ).
- Оберните структуру с чистым API.
- Клонируйте`Arc`для каждого потока.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Потокобезопасность: компилятор Rust гарантирует отсутствие гонок за данными —`RwLock`обеспечивает взаимное исключение, а`Arc`обеспечивает безопасное совместное владение. Если это скомпилируется, это правильно.
- Производительность:`RwLock`лучше, чем `Mutex`, для рабочих нагрузок с большим объемом чтения. Для рабочих нагрузок с большим объемом записи используйте`Mutex`(проще, без накладных расходов на чтение и запись).
- Обновление производства: используйте`parking_lot::RwLock`(быстрее, без отравления, меньший объем памяти) или`dashmap::DashMap`(параллельный HashMap без блокировки).
### Проблема 2: реализация парсера с нулевым копированием
**Постановка задачи:** Напишите синтаксический анализатор, который извлекает пары ключ-значение из строки конфигурации, например `"name=Alice;age=30;role=admin"`, без выделения новых строк — используя только фрагменты строк, заимствованные из входных данных.
**Шаг 1. Поймите проблему:**
Нам нужно проанализировать пары `key=value`, разделенные `;`. Ключевым ограничением является «нулевая копия» — возвращаемые данные должны заимствоваться из входных `&str`, а не выделять новые `String`. Это означает возврат`Vec<(&str, &str)>`со временем жизни, привязанным к входным данным.
**Шаг 2. Определите подход:**
— Используйте методы`&str`(`split`,`find`, slicing) — все возвращают фрагменты `&str`, заимствованные из входных данных.
- Избегайте использования`.to_string()`или`String::from()`где угодно.
— Пожизненная аннотация: выходные данные заимствуются из входных — `fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Нулевое копирование:`split`,`split_once`и`trim`возвращают фрагменты`&str`— без выделения кучи.
- Правила исключения времени жизни правильно привязывают время жизни выходных данных к входным.
- Краевые случаи: пустой ввод возвращает`[]`; отсутствие`=`пропускает пару (через`filter_map`); Пробелы вокруг`=`обрабатываются `trim`.
- Для более сложного анализа используйте крейт`nom`(на основе комбинатора, также с нулевым копированием).
### Проблема 3: реализация шаблона наблюдателя с каналами
**Постановка задачи:** Создайте систему публикации-подписки, в которой несколько подписчиков получают сообщения от издателя. Используйте каналы Rust и убедитесь, что система обрабатывает медленных подписчиков, не блокируя издателя.
**Шаг 1. Поймите проблему:**
Нам нужен один издатель, отправляющий сообщения нескольким подписчикам. Канал`mpsc`в Rust — это канал с несколькими производителями и одним потребителем — нам нужен обратный процесс (один производитель с несколькими потребителями). Мы можем использовать каналы`broadcast`(из `tokio`) или реализовать разветвление с использованием нескольких отправителей `mpsc`.
**Шаг 2. Определите подход:**
- Используйте`std::sync::mpsc`для стандартных каналов.
- Для разветвления: сохраните`Vec<Sender<T>>`и клонируйте сообщения для каждого.
- Для медленных абонентов: используйте`try_send`(неблокирующие) или ограниченные каналы с противодавлением.
— Оберните структуру`Bus`для чистого API.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
—`retain`автоматически очищает мертвых подписчиков — утечки памяти из-за отключенных потоков не происходит.
-`message.clone()`необходим, поскольку каждому подписчику нужна своя копия. Для типов, которые требуют больших затрат на клонирование, оберните их`Arc<T>`.
— Ограниченные каналы: замените`mpsc::channel()`на`mpsc::sync_channel(N)`для противодавления —`publish`блокируется, если буфер подписчика заполнен.
- Производство: используйте`tokio::sync::broadcast`для асинхронной публикации/подписки или`flume`для более быстрого mpsc с ограниченными/неограниченными параметрами.
---

## Краткое содержание
Rust — это язык, который заставляет вас думать о памяти, владении и параллельности — и вознаграждает вас правильным по конструкции кодом. Кривая обучения реальна, но и отдача значительна: программы, которые работают так же быстро, как C, но не содержат ошибок с нулевым указателем, гонок за данными и утечек памяти. Rust — это не универсальный язык повышения производительности — это системный язык, когда важны и правильность, и производительность. Его растущее распространение в промышленности (включая ядро ​​Linux и Android) предполагает, что его важность будет возрастать.