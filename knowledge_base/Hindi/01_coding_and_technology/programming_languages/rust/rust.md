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
#जंग
रस्ट एक सांख्यिकीय रूप से टाइप की गई, संकलित प्रोग्रामिंग भाषा है जिसे पहली बार 2015 में रिलीज़ किया गया था, जिसे मूल रूप से मोज़िला में ग्रेडन होरे द्वारा विकसित किया गया था। रस्ट का निर्णायक वादा **कचरा संग्रहण के बिना स्मृति सुरक्षा** है। यह अपने स्वामित्व प्रणाली के माध्यम से इसे प्राप्त करता है - संकलन समय पर लागू नियमों का एक सेट जो C या C++ जितनी तेजी से कोड का उत्पादन करते समय बग की पूरी श्रेणियों (नल पॉइंटर डेरेफरेंस, डेटा रेस, बफर ओवरफ्लो, उपयोग-बाद-मुक्त) को समाप्त करता है।
रस्ट को लगातार कई वर्षों से स्टैक ओवरफ़्लो डेवलपर सर्वेक्षण में "सबसे पसंदीदा" प्रोग्रामिंग भाषा चुना गया है। इसका उपयोग सिस्टम प्रोग्रामिंग, वेबअसेंबली, सीएलआई टूल्स, क्लाउड इंफ्रास्ट्रक्चर और सुरक्षा-महत्वपूर्ण संदर्भों में सी/सी++ के प्रतिस्थापन के रूप में तेजी से किया जा रहा है। लिनक्स कर्नेल अब रस्ट कोड स्वीकार करता है।
---

## जंग क्यों मायने रखती है
- **जीसी के बिना मेमोरी सुरक्षा**: स्वामित्व प्रणाली संकलन समय पर शून्य पॉइंटर्स, डेटा रेस और लटकने वाले पॉइंटर्स को रोकती है - शून्य रनटाइम ओवरहेड के साथ।
- **प्रदर्शन**: अधिकांश कार्यभार के लिए C/C++ से मेल खाता है या उससे अधिक है। कोई कचरा संग्रहकर्ता नहीं होने का मतलब कोई अप्रत्याशित रुकावट नहीं है।
- **निडर समवर्ती**: प्रकार प्रणाली संकलन समय पर डेटा दौड़ को रोकती है। यदि यह संकलित होता है, तो यह थ्रेड-सुरक्षित है।
- **आधुनिक टूलींग**:`cargo`(बिल्ड सिस्टम + पैकेज मैनेजर) किसी भी भाषा में सर्वश्रेष्ठ में से एक है। `cargo build`,`cargo test`,`cargo doc`सभी बॉक्स से बाहर काम करते हैं।
- **WebAssembly**: WASM को संकलित करने के लिए प्रथम श्रेणी का समर्थन, ब्राउज़रों में लगभग-मूल प्रदर्शन को सक्षम करना।
- **बढ़ती स्वीकार्यता**: एडब्ल्यूएस, गूगल (एंड्रॉइड), माइक्रोसॉफ्ट (विंडोज कर्नेल), क्लाउडफ्लेयर, डिस्कॉर्ड, ड्रॉपबॉक्स और मेटा द्वारा उपयोग किया जाता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सीखने की तीव्र अवस्था** | स्वामित्व, उधार लेना, जीवनकाल अन्य भाषाओं की किसी भी चीज़ से भिन्न है | "द रस्ट बुक" में समय निवेश करें; अवधारणाएँ अभ्यास के साथ क्लिक करें |
| **धीमा संकलन** | बड़ी परियोजनाओं के लिए संकलन समय लंबा हो सकता है | त्वरित प्रकार-जाँच के लिए`cargo check`का उपयोग करें; वृद्धिशील संकलन मदद करता है |
| **वर्बोज़ त्रुटि प्रबंधन** | `Result<T, E>`और`?`ऑपरेटर को स्पष्ट हैंडलिंग की आवश्यकता होती है | अनुप्रयोगों के लिए `anyhow`, पुस्तकालयों के लिए`thiserror`का उपयोग करें |
| **छोटा नौकरी बाज़ार** | जावा, पायथन, या जावास्क्रिप्ट की तुलना में कम रस्ट जॉब्स (लेकिन तेजी से बढ़ रही हैं) | अधिकांश रस्ट भूमिकाएँ सिस्टम प्रोग्रामिंग, क्रिप्टो, या इन्फ्रास्ट्रक्चर में हैं |
| **अपरिपक्व पारिस्थितिकी तंत्र** | कुछ डोमेन के लिए पायथन/जावा/जेएस की तुलना में कम लाइब्रेरी | पारिस्थितिकी तंत्र तेजी से बढ़ रहा है; कई टोकरे उत्कृष्ट गुणवत्ता वाले हैं |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
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

### स्वामित्व और उधार
यह रस्ट का मुख्य नवाचार है। प्रत्येक मान का बिल्कुल एक स्वामी होता है। जब मालिक दायरे से बाहर चला जाता है, तो मूल्य कम हो जाता है।
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

### संरचनाएं, एनम और पैटर्न मिलान
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

### त्रुटि प्रबंधन
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

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक और विशेषता सीमाएँ
जेनरिक आपको ऐसा कोड लिखने देता है जो पूर्ण प्रकार की सुरक्षा बनाए रखते हुए किसी भी प्रकार के साथ काम करता है। लक्षण साझा व्यवहार को परिभाषित करते हैं।
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

### मैक्रोज़
रस्ट में दो प्रकार के मैक्रोज़ होते हैं: घोषणात्मक (`macro_rules!`) और प्रक्रियात्मक (व्युत्पन्न, विशेषता, फ़ंक्शन-जैसे)।
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

### उन्नत पैटर्न मिलान और विध्वंस
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

### ऑपरेटर ओवरलोडिंग
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

### कस्टम त्रुटि पदानुक्रम
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

## समवर्ती एवं समांतरता
### थ्रेड मॉडल और सिंक्रोनाइज़ेशन
रस्ट की स्वामित्व प्रणाली संकलन समय पर डेटा दौड़ को रोकती है।`Send`और`Sync`लक्षण थ्रेड सुरक्षा लागू करते हैं।
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

### चैनल - संदेश पासिंग
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

### टोकियो के साथ एसिंक/प्रतीक्षा करें
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

### स्कोप्ड थ्रेड्स (जंग 1.63+)
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### कार्गो.टोएमएल कॉन्फ़िगरेशन
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

### आवश्यक कार्गो कमांड
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### यूनिट परीक्षण
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

### एकीकरण परीक्षण
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

### बेंचमार्क परीक्षण
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

## अंतरसंचालनीयता
### सी के साथ एफएफआई
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

### पायथन से रस्ट को कॉल करना (PyO3)
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

## डिज़ाइन पैटर्न
### बिल्डर पैटर्न
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

### न्यूटाइप पैटर्न (टाइप सेफ्टी)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### लक्षणों के साथ रिपोजिटरी पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### अनुकूलन तकनीकें
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

## तैनाती
### क्रॉस-संकलन
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### डॉकर परिनियोजन
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

### वेबअसेंबली परिनियोजन
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## पारिस्थितिकी तंत्र
| उपकरण | उद्देश्य |
|------|---------|
| **कार्गो** | बिल्ड सिस्टम, पैकेज मैनेजर, टेस्ट रनर, डॉक जनरेटर |
| **क्रेट्स.आईओ** | पैकेज रजिस्ट्री (150,000+ क्रेट) |
| **जंगम** | कोड फ़ॉर्मेटर |
| **क्लिपी** | सैकड़ों उपयोगी जांचों के साथ लिंटर |
| **टोकियो** | Async रनटाइम (async रस्ट के लिए मानक) |
| **सर्डे** | क्रमबद्धता/अक्रमांकन रूपरेखा |
| **एक्टिक्स-वेब / एक्सम** | वेब फ्रेमवर्क |
| **डीजल/एसक्यूएलएक्स** | डेटाबेस ओआरएम/क्वेरी बिल्डर्स |
---

## जंग का उपयोग कब करें
| परिदृश्य | जंग क्यों | बेहतर विकल्प |
|---|---|-----|
| सिस्टम प्रोग्रामिंग | मेमोरी सुरक्षा + प्रदर्शन | यदि आपको सुरक्षा गारंटी की आवश्यकता नहीं है तो C/C++ |
| वेबअसेंबली | अपनी श्रेणी में सर्वोत्तम WASM समर्थन | -- |
| सीएलआई उपकरण | तेज़, एकल बाइनरी, बढ़िया UX | सरल सीएलआई के लिए जाएं |
| एंबेडेड सिस्टम | कोई जीसी नहीं, हार्डवेयर पहुंच, सुरक्षा | सरल एम्बेडेड के लिए सी |
| प्रदर्शन-महत्वपूर्ण कोड | C/C++ गति से मेल खाता है | -- |
| क्लाउड इंफ्रास्ट्रक्चर | बढ़ती स्वीकार्यता (एडब्ल्यूएस, क्लाउडफ्लेयर) | तेजी से विकास के लिए आगे बढ़ें |
| सामान्य अनुप्रयोग विकास | तीव्र सीखने की अवस्था विकास को धीमा कर देती है | पायथन, गो, जावा |
| वेब बैकएंड | संभव है लेकिन पारिस्थितिकी तंत्र युवा है | जाओ, नोड.जेएस, पायथन |
| डेटा साइंस/एमएल | इसके लिए पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| त्वरित स्क्रिप्ट/प्रोटोटाइप | बहुत अधिक क्रियात्मक और लिखने में धीमा | पायथन, जावास्क्रिप्ट |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: स्वामित्व प्रणाली क्या है, और रस्ट के पास यह क्यों है?
**ए:** रस्ट में प्रत्येक मूल्य का बिल्कुल एक स्वामी होता है। जब स्वामी दायरे से बाहर चला जाता है, तो मान गिरा दिया जाता है (स्मृति मुक्त हो जाती है)। यह मेमोरी सुरक्षा की गारंटी देते हुए कचरा संग्रहकर्ता की आवश्यकता को समाप्त करता है। असाइनमेंट, फ़ंक्शन पैरामीटर और रिटर्न मान सभी स्वामित्व स्थानांतरित करते हैं ("स्थानांतरित करें")। स्थानांतरित किए बिना साझा करने के लिए, संदर्भों का उपयोग करें (उधार लेने के लिए `&T`, परिवर्तनशील उधार के लिए `&mut T`)। संकलक लागू करता है: आपके पास एक ही मूल्य पर एक परिवर्तनीय संदर्भ और एक अपरिवर्तनीय संदर्भ नहीं हो सकता है।
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2: मुझे`String`बनाम`&str`का उपयोग कब करना चाहिए?
**ए:**`String`एक स्वामित्व वाली, ढेर-आवंटित, बढ़ने योग्य UTF-8 स्ट्रिंग है। `&str`एक UTF-8 स्ट्रिंग स्लाइस का उधार लिया गया संदर्भ है (`String`, एक स्ट्रिंग अक्षरशः, या दोनों में से किसी एक भाग को इंगित कर सकता है)। जब आपको किसी स्ट्रिंग का स्वामित्व, संशोधन या निर्माण करने की आवश्यकता हो तो`String`का उपयोग करें। फ़ंक्शन पैरामीटर (अधिक लचीला - दोनों को स्वीकार करता है), केवल पढ़ने योग्य दृश्य और स्ट्रिंग अक्षर के लिए`&str`का उपयोग करें। फ़ंक्शन हस्ताक्षरों में`&str`स्वीकार करें; जब कॉल करने वाले को स्वामित्व की आवश्यकता हो तो`String`लौटाएँ।
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: रस्ट बिना किसी अपवाद के त्रुटियों को कैसे संभालता है?
**ए:** रस्ट पुनर्प्राप्त करने योग्य त्रुटियों के लिए`Result<T, E>`एनम का उपयोग करता है और अप्राप्य त्रुटियों के लिए`panic!`का उपयोग करता है। जो फ़ंक्शन विफल हो सकते हैं वे`Result`लौटाते हैं।`?`ऑपरेटर त्रुटियों को संक्षिप्त रूप से प्रसारित करता है। यह दृष्टिकोण त्रुटि प्रबंधन को स्पष्ट बनाता है - आप गलती से किसी त्रुटि को अनदेखा नहीं कर सकते। एप्लिकेशन त्रुटि प्रबंधन (सुविधाजनक संदर्भ) के लिए`anyhow`और लाइब्रेरी त्रुटि प्रकारों (मैक्रोज़ प्राप्त करें) के लिए`thiserror`का उपयोग करें।
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

### प्रश्न 4: जीवन काल क्या हैं, और मुझे कब उन पर टिप्पणी करने की आवश्यकता है?
**ए:** लाइफटाइम ट्रैक करता है कि संदर्भ कितने समय तक वैध हैं। कंपाइलर ज्यादातर मामलों में उनका अनुमान "लाइफटाइम एलीजन रूल्स" के माध्यम से लगाता है। जब कंपाइलर इनपुट और आउटपुट जीवनकाल के बीच संबंध निर्धारित नहीं कर पाता है तो आपको स्पष्ट एनोटेशन की आवश्यकता होती है - आमतौर पर जब कोई फ़ंक्शन कई संदर्भ लेता है और एक लौटाता है। जीवनकाल शून्य रनटाइम लागत के साथ संकलन समय पर लटकते संदर्भों को रोकता है।
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

### Q5: `Vec<T>`, सरणियों और स्लाइस के बीच क्या अंतर है?
**ए:** सारणियाँ`[T; N]`निश्चित-आकार, स्टैक-आवंटित हैं, और उनकी लंबाई प्रकार का हिस्सा है। `Vec<T>`एक बढ़ने योग्य, ढेर-आवंटित संग्रह है। स्लाइस`&[T]`मोटे पॉइंटर्स (पॉइंटर + लंबाई) हैं जो किसी सरणी या Vec के सन्निहित हिस्से को उधार लेते हैं। छोटे, निश्चित आकार के डेटा के लिए सरणियों का उपयोग करें। गतिशील संग्रह के लिए Vec का उपयोग करें। अधिकतम लचीलेपन के लिए फ़ंक्शन पैरामीटर में`&[T]`स्वीकार करें।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक थ्रेड-सेफ की-वैल्यू स्टोर बनाएं
**समस्या कथन:** रस्ट में एक समवर्ती कुंजी-मूल्य स्टोर लागू करें जो डेटा रेस के बिना एकाधिक थ्रेड से `get`, `set`, और`delete`संचालन का समर्थन करता है। आंतरिक परिवर्तनशीलता का उपयोग करें और सुनिश्चित करें कि कार्यान्वयन मुहावरेदार जंग है।
**चरण 1 - समस्या को समझें:**
एक साझा हैशमैप पर एकाधिक थ्रेड्स को पढ़ने और लिखने की आवश्यकता होती है। रस्ट की स्वामित्व प्रणाली संकलन समय पर डेटा दौड़ को रोकती है, लेकिन हमें साझा स्वामित्व के लिए`Arc`में लिपटे आंतरिक परिवर्तनशीलता (`RwLock` या `Mutex`) की आवश्यकता है। `RwLock`एकाधिक समवर्ती पाठकों या एक विशेष लेखक की अनुमति देता है - पढ़ने-भारी कार्यभार के लिए बेहतर।
**चरण 2 - दृष्टिकोण को पहचानें:**
- साझा, थ्रेड-सुरक्षित पहुंच के लिए`Arc<RwLock<HashMap<K, V>>>`का उपयोग करें।
-`get`के लिए`RwLock::read()`(एकाधिक पाठकों की अनुमति)।
-`set`और`delete`(विशेष पहुंच) के लिए `RwLock::write()`।
- एक स्वच्छ एपीआई के साथ एक संरचना में लपेटें।
- प्रत्येक थ्रेड के लिए`Arc`को क्लोन करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- थ्रेड सुरक्षा: रस्ट कंपाइलर कोई डेटा रेस नहीं होने की गारंटी देता है -`RwLock`पारस्परिक बहिष्करण लागू करता है, और`Arc`सुरक्षित साझा स्वामित्व प्रदान करता है। यदि यह संकलित है, तो यह सही है.
- प्रदर्शन: भारी कार्यभार के लिए `RwLock`,`Mutex`से बेहतर है। लिखने-भारी कार्यभार के लिए,`Mutex`(सरल, कोई पाठक-लेखक ओवरहेड नहीं) का उपयोग करें।
- उत्पादन उन्नयन:`parking_lot::RwLock`(तेज़, कोई विषाक्तता नहीं, छोटी मेमोरी फ़ुटप्रिंट) या`dashmap::DashMap`(लॉक-मुक्त समवर्ती हैशमैप) का उपयोग करें।
### समस्या 2: एक शून्य-प्रतिलिपि पार्सर लागू करें
**समस्या कथन:** एक पार्सर लिखें जो नई स्ट्रिंग्स आवंटित किए बिना`"name=Alice;age=30;role=admin"`जैसी कॉन्फ़िगरेशन स्ट्रिंग से कुंजी-मूल्य जोड़े निकालता है - केवल इनपुट से उधार ली गई स्ट्रिंग स्लाइस का उपयोग करके।
**चरण 1 - समस्या को समझें:**
हमें`;`द्वारा अलग किए गए`key=value`जोड़े को पार्स करने की आवश्यकता है। मुख्य बाधा "शून्य-प्रतिलिपि" है - लौटाए गए डेटा को इनपुट`&str`से उधार लिया जाना चाहिए, नए`String`एस आवंटित नहीं करना चाहिए। इसका मतलब है इनपुट से जुड़े जीवनकाल के साथ`Vec<(&str, &str)>`लौटाना।
**चरण 2 - दृष्टिकोण को पहचानें:**
-`&str`विधियों (`split`, `find`, स्लाइसिंग) का उपयोग करें - सभी इनपुट से उधार लिए गए`&str`स्लाइस लौटाते हैं।
- कहीं भी`.to_string()`या`String::from()`से बचें।
- लाइफटाइम एनोटेशन: आउटपुट इनपुट से उधार लेता है - `fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- शून्य-प्रतिलिपि:`split`,`split_once`, और`trim`सभी`&str`स्लाइस लौटाते हैं - कोई ढेर आवंटन नहीं।
- लाइफ़टाइम एलिज़न नियम आउटपुट लाइफ़टाइम को इनपुट से सही ढंग से जोड़ते हैं।
- एज केस: खाली इनपुट रिटर्न `[]`; गुम`=`जोड़ी को छोड़ देता है (`filter_map` के माध्यम से);`=`के आसपास रिक्त स्थान को`trim`द्वारा नियंत्रित किया जाता है।
- अधिक जटिल पार्सिंग के लिए,`nom`क्रेट (कॉम्बिनेटर-आधारित, शून्य-कॉपी भी) का उपयोग करें।
### समस्या 3: चैनलों के साथ पर्यवेक्षक पैटर्न लागू करें
**समस्या कथन:** एक प्रकाशन-सदस्यता प्रणाली बनाएं जहां कई ग्राहकों को एक प्रकाशक से संदेश प्राप्त होते हैं। रस्ट चैनलों का उपयोग करें और सुनिश्चित करें कि सिस्टम प्रकाशक को अवरुद्ध किए बिना धीमे ग्राहकों को संभालता है।
**चरण 1 - समस्या को समझें:**
हमें अनेक ग्राहकों को संदेश भेजने वाले एक प्रकाशक की आवश्यकता है। रस्ट का`mpsc`चैनल बहु-निर्माता एकल-उपभोक्ता है - हमें रिवर्स (एकल-निर्माता बहु-उपभोक्ता) की आवश्यकता है। हम`broadcast`चैनल (`tokio` से) का उपयोग कर सकते हैं या कई`mpsc`प्रेषकों का उपयोग करके फैन-आउट लागू कर सकते हैं।
**चरण 2 - दृष्टिकोण को पहचानें:**
- मानक चैनलों के लिए`std::sync::mpsc`का उपयोग करें।
- फैन-आउट के लिए: एक`Vec<Sender<T>>`बनाए रखें और प्रत्येक के लिए संदेशों को क्लोन करें।
- धीमे ग्राहकों के लिए:`try_send`(नॉन-ब्लॉकिंग) या बैकप्रेशर वाले बाउंडेड चैनल का उपयोग करें।
- स्वच्छ एपीआई के लिए`Bus`संरचना में लपेटें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
-`retain`स्वचालित रूप से मृत ग्राहकों को साफ़ करता है - डिस्कनेक्ट किए गए थ्रेड से कोई मेमोरी लीक नहीं होती है।
-`message.clone()`आवश्यक है क्योंकि प्रत्येक ग्राहक को इसकी अपनी प्रति की आवश्यकता होती है। महंगे-से-क्लोन प्रकारों के लिए,`Arc<T>`में लपेटें।
- बाउंडेड चैनल: बैकप्रेशर के लिए`mpsc::channel()`को`mpsc::sync_channel(N)`से बदलें - यदि ग्राहक का बफर भर गया है तो`publish`ब्लॉक हो जाता है।
- उत्पादन: एसिंक पब/सब के लिए`tokio::sync::broadcast`का उपयोग करें, या बाउंडेड/अनबाउंड विकल्पों के साथ तेज़ एमपीएससी के लिए`flume`का उपयोग करें।
---

## सारांश
रस्ट एक ऐसी भाषा है जो आपको स्मृति, स्वामित्व और समवर्तीता के बारे में सोचने के लिए मजबूर करती है - और आपको ऐसे कोड से पुरस्कृत करती है जो निर्माण द्वारा सही है। सीखने की अवस्था वास्तविक है, लेकिन लाभ महत्वपूर्ण है: ऐसे प्रोग्राम जो C जितने तेज़ हैं लेकिन शून्य पॉइंटर बग, डेटा रेस और मेमोरी लीक से मुक्त हैं। रस्ट एक सामान्य प्रयोजन उत्पादकता भाषा नहीं है - यह एक सिस्टम भाषा है जब शुद्धता और प्रदर्शन दोनों मायने रखते हैं। उद्योग (लिनक्स कर्नेल और एंड्रॉइड सहित) में इसकी बढ़ती स्वीकार्यता से पता चलता है कि यह तेजी से महत्वपूर्ण होगा।