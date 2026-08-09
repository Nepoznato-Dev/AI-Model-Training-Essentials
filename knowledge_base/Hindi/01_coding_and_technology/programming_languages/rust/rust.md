---
# मेटाडेटा
शीर्षक: "जंग"
विवरण: "रस्ट प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स बुनियादी बातें, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [जंग, प्रोग्रामिंग-भाषा, वाक्यविन्यास, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "40 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
#जंग
रस्ट एक सांख्यिकीय रूप से टाइप की गई, संकलित प्रोग्रामिंग भाषा है जिसे पहली बार 2015 में रिलीज़ किया गया था, जिसे मूल रूप से मोज़िला में ग्रेडन होरे द्वारा विकसित किया गया था। रस्ट का निर्णायक वादा **कचरा संग्रहण के बिना स्मृति सुरक्षा** है। यह अपने स्वामित्व प्रणाली के माध्यम से इसे प्राप्त करता है - संकलन समय पर लागू नियमों का एक सेट जो C या C++ जितनी तेजी से कोड का उत्पादन करते समय बग की पूरी श्रेणियों (नल पॉइंटर डेरेफरेंस, डेटा रेस, बफर ओवरफ्लो, उपयोग-बाद-मुक्त) को समाप्त करता है।
रस्ट को लगातार कई वर्षों से स्टैक ओवरफ़्लो डेवलपर सर्वेक्षण में "सबसे पसंदीदा" प्रोग्रामिंग भाषा चुना गया है। इसका उपयोग सिस्टम प्रोग्रामिंग, वेबअसेंबली, सीएलआई टूल्स, क्लाउड इंफ्रास्ट्रक्चर और सुरक्षा-महत्वपूर्ण संदर्भों में सी/सी++ के प्रतिस्थापन के रूप में तेजी से किया जा रहा है। लिनक्स कर्नेल अब रस्ट कोड स्वीकार करता है।
---

## जंग क्यों मायने रखती है
- **जीसी के बिना मेमोरी सुरक्षा**: स्वामित्व प्रणाली संकलन समय पर शून्य पॉइंटर्स, डेटा रेस और लटकने वाले पॉइंटर्स को रोकती है - शून्य रनटाइम ओवरहेड के साथ।
- **प्रदर्शन**: अधिकांश कार्यभार के लिए C/C++ से मेल खाता है या उससे अधिक है। कोई कचरा संग्रहकर्ता नहीं होने का मतलब कोई अप्रत्याशित रुकावट नहीं है।
- **निडर समवर्ती**: प्रकार प्रणाली संकलन समय पर डेटा दौड़ को रोकती है। यदि यह संकलित होता है, तो यह थ्रेड-सुरक्षित है।
- **आधुनिक टूलींग**:`cargo`(बिल्ड सिस्टम + पैकेज मैनेजर) किसी भी भाषा में सर्वश्रेष्ठ में से एक है।  __प्रोटेक्टेड_1__ , __प्रोटेक्टेड_2__ , __प्रोटेक्टेड_3__ सभी बॉक्स से बाहर काम करते हैं।
- **WebAssembly**: WASM को संकलित करने के लिए प्रथम श्रेणी का समर्थन, ब्राउज़रों में लगभग-मूल प्रदर्शन को सक्षम करना।
- **बढ़ती स्वीकार्यता**: एडब्ल्यूएस, गूगल (एंड्रॉइड), माइक्रोसॉफ्ट (विंडोज कर्नेल), क्लाउडफ्लेयर, डिस्कॉर्ड, ड्रॉपबॉक्स और मेटा द्वारा उपयोग किया जाता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सीखने की तीव्र अवस्था** | स्वामित्व, उधार लेना, जीवनकाल अन्य भाषाओं की किसी भी चीज़ से भिन्न है | "द रस्ट बुक" में समय निवेश करें; अवधारणाएँ अभ्यास के साथ क्लिक करें |
| **धीमा संकलन** | बड़ी परियोजनाओं के लिए संकलन समय लंबा हो सकता है | त्वरित प्रकार-जांच के लिए`cargo check`का उपयोग करें; वृद्धिशील संकलन मदद करता है |
| **वर्बोज़ त्रुटि प्रबंधन** | `Result<T, E>`और`?`ऑपरेटर को स्पष्ट हैंडलिंग की आवश्यकता होती है | अनुप्रयोगों के लिए`anyhow`का उपयोग करें, पुस्तकालयों के लिए`thiserror`का उपयोग करें |
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

## सारांश
रस्ट एक ऐसी भाषा है जो आपको स्मृति, स्वामित्व और समवर्तीता के बारे में सोचने के लिए मजबूर करती है - और आपको ऐसे कोड से पुरस्कृत करती है जो निर्माण द्वारा सही है। सीखने की अवस्था वास्तविक है, लेकिन लाभ महत्वपूर्ण है: ऐसे प्रोग्राम जो C जितने तेज़ हैं लेकिन शून्य पॉइंटर बग, डेटा रेस और मेमोरी लीक से मुक्त हैं। रस्ट एक सामान्य प्रयोजन उत्पादकता भाषा नहीं है - यह एक सिस्टम भाषा है जब शुद्धता और प्रदर्शन दोनों मायने रखते हैं। उद्योग (लिनक्स कर्नेल और एंड्रॉइड सहित) में इसकी बढ़ती स्वीकार्यता से पता चलता है कि यह तेजी से महत्वपूर्ण होगा।