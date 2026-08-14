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

# Rouiller
Rust est un langage de programmation compilé et typé statiquement publié pour la première fois en 2015, développé à l'origine par Graydon Hoare chez Mozilla. La promesse déterminante de Rust est **la sécurité de la mémoire sans garbage collection**. Il y parvient grâce à son système de propriété – un ensemble de règles appliquées au moment de la compilation qui élimine des catégories entières de bogues (déréférences de pointeurs nuls, courses de données, débordements de tampon, utilisation après libération) tout en produisant du code aussi rapide que C ou C++.
Rust a été élu langage de programmation « le plus apprécié » dans l'enquête auprès des développeurs Stack Overflow pendant plusieurs années consécutives. Il est de plus en plus utilisé dans la programmation système, WebAssembly, les outils CLI, l'infrastructure cloud et en remplacement du C/C++ dans des contextes critiques en matière de sécurité. Le noyau Linux accepte désormais le code Rust.
---

## Pourquoi la rouille est importante
- **Sécurité de la mémoire sans GC** : le système de propriété empêche les pointeurs nuls, les courses de données et les pointeurs suspendus au moment de la compilation, sans aucune surcharge d'exécution.
- **Performance** : égale ou dépasse le C/C++ pour la plupart des charges de travail. Pas de garbage collector signifie pas de pauses imprévisibles.
- **Concurrence sans peur** : le système de types empêche les courses de données au moment de la compilation. S'il compile, il est thread-safe.
- **Outils modernes** :`cargo`(système de build + gestionnaire de packages) est l'un des meilleurs dans n'importe quel langage. `cargo build`,`cargo test`,`cargo doc`fonctionnent tous immédiatement.
- **WebAssembly** : prise en charge de première classe pour la compilation vers WASM, permettant des performances quasi natives dans les navigateurs.
- **Adoption croissante** : utilisé par AWS, Google (Android), Microsoft (noyau Windows), Cloudflare, Discord, Dropbox et Meta.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Courbe d'apprentissage abrupte** | La propriété, l'emprunt, la durée de vie ne ressemblent à rien dans d'autres langues | Investissez du temps dans « The Rust Book » ; les concepts cliquent avec la pratique |
| **Compilation lente** | Les temps de compilation peuvent être longs pour les grands projets | Utilisez`cargo check`pour une vérification de type rapide ; la compilation incrémentielle aide |
| **Gestion détaillée des erreurs** |  Les opérateurs`Result<T, E>`et`?`nécessitent une gestion explicite | Utilisez`anyhow`pour les applications,`thiserror`pour les bibliothèques |
| **Marché du travail plus petit** | Moins de tâches Rust que Java, Python ou JavaScript (mais en croissance rapide) | La plupart des rôles Rust concernent la programmation système, la cryptographie ou l'infrastructure |
| **Écosystème immature** | Moins de bibliothèques que Python/Java/JS pour certains domaines | L'écosystème se développe rapidement ; de nombreuses caisses sont d'excellente qualité |
---

## Fondamentaux de la syntaxe
### Structure de base
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

### Propriété et emprunt
C'est l'innovation fondamentale de Rust. Chaque valeur a exactement un propriétaire. Lorsque le propriétaire sort du champ d'application, la valeur est supprimée.
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

### Structures, énumérations et correspondance de modèles
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

### Gestion des erreurs
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

## Syntaxe et modèles avancés
### Génériques et limites des traits
Les génériques vous permettent d'écrire du code qui fonctionne avec n'importe quel type tout en conservant une sécurité totale des types. Les traits définissent un comportement partagé.
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

###Macro
Rust a deux types de macros : déclaratives (`macro_rules!`) et procédurales (dérivées, attributaires, de type fonction).
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

### Correspondance de modèles et déstructuration avancées
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

### Surcharge des opérateurs
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

### Hiérarchies d'erreurs personnalisées
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

## Concurrence et parallélisme
### Modèle de thread et synchronisation
Le système de propriété de Rust empêche les courses de données au moment de la compilation. Les traits`Send`et`Sync`renforcent la sécurité des threads.
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

### Canaux – Passage de messages
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

### Async/Await avec Tokio
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

### Fils de portée (Rust 1.63+)
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

## Configuration du projet et système de construction
### Structure du projet
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

### Configuration de Cargo.toml
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

### Commandes de fret essentielles
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

### Pipeline CI/CD (actions GitHub)
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

## Tests
### Tests unitaires
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

### Tests d'intégration
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

### Tests de référence
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

## Interopérabilité
### FFI avec C
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

### Appeler Rust depuis Python (PyO3)
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

## Modèles de conception
### Modèle de constructeur
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

### Modèle Newtype (sécurité des types)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Modèle de référentiel avec traits
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

## Performances et optimisation
### Outils de profilage
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

### Techniques d'optimisation
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

## Déploiement
### Compilation croisée
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Déploiement de Docker
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

### Déploiement de WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## L'écosystème
| Outil | Objectif |
|------|--------------|
| **cargo** | Système de build, gestionnaire de packages, exécuteur de tests, générateur de documents |
| **crates.io** | Registre des packages (plus de 150 000 caisses) |
| **rustfmt** | Formateur de code |
| **clignotant** | Linter avec des centaines de contrôles utiles |
| **tokio** | Runtime asynchrone (le standard pour Rust asynchrone) |
| **serde** | Cadre de sérialisation/désérialisation |
| **actix-web / axum** | Cadres Web |
| **diesel / sqlx** | ORM de bases de données/générateurs de requêtes |
---

## Quand utiliser Rust
| Scénario | Pourquoi la rouille | Meilleure alternative |
|--------------|---------|-------------------|
| Programmation systèmes | Sécurité de la mémoire + performances | C/C++ si vous n'avez pas besoin de garanties de sécurité |
| WebAssembly | Support WASM de premier ordre | -- |
| Outils CLI | Rapide, binaire unique, excellent UX | Optez pour des CLI plus simples |
| Systèmes embarqués | Pas de GC, accès matériel, sécurité | C pour un intégration plus simple |
| Code critique pour les performances | Correspond à la vitesse C/C++ | -- |
| Infrastructure cloud | Adoption croissante (AWS, Cloudflare) | Optez pour un développement plus rapide |
| Développement d'applications générales | Une courbe d'apprentissage abrupte ralentit le développement | Python, Go, Java |
| Moteurs Web | Possible mais l'écosystème est plus jeune | Allez, Node.js, Python |
| Science des données / ML | Pas l'écosystème pour ça | Python, R |
| Scripts rapides/prototypes | Trop verbeux et lent à écrire | Python, JavaScript |
---

## Questions et réponses synthétiques
### Q1 : Qu'est-ce que le système de propriété et pourquoi Rust l'a-t-il mis en place ?
**R :** Chaque valeur dans Rust a exactement un propriétaire. Lorsque le propriétaire sort de la portée, la valeur est supprimée (mémoire libérée). Cela élimine le besoin d’un ramasse-miettes tout en garantissant la sécurité de la mémoire. L'affectation, les paramètres de fonction et les valeurs de retour transfèrent tous la propriété (« déplacement »). Pour partager sans transférer, utilisez des références (`&T`pour l'emprunt,`&mut T`pour l'emprunt mutable). Le compilateur applique : vous ne pouvez pas avoir simultanément une référence mutable et une référence immuable à la même valeur.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2 : Quand dois-je utiliser`String`ou `&str` ?
**R :**`String`est une chaîne UTF-8 détenue, allouée par tas et extensible. `&str`est une référence empruntée à une tranche de chaîne UTF-8 (peut pointer vers un`String`, un littéral de chaîne ou une partie de l'un ou l'autre). Utilisez`String`lorsque vous devez posséder, modifier ou créer une chaîne. Utilisez`&str`pour les paramètres de fonction (plus flexible – accepte les deux), les vues en lecture seule et les littéraux de chaîne. Acceptez`&str`dans les signatures de fonction ; renvoie`String`lorsque l'appelant a besoin de propriété.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3 : Comment Rust gère-t-il les erreurs sans exceptions ?
**R :** Rust utilise l'énumération`Result<T, E>`pour les erreurs récupérables et`panic!`pour les erreurs irrécupérables. Les fonctions qui peuvent échouer renvoient`Result`. L'opérateur`?`propage les erreurs de manière concise. Cette approche rend la gestion des erreurs explicite : vous ne pouvez pas ignorer accidentellement une erreur. Utilisez`anyhow`pour la gestion des erreurs d’application (contexte pratique) et`thiserror`pour les types d’erreurs de bibliothèque (macros dérivées).
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

### Q4 : Que sont les durées de vie et quand dois-je les annoter ?
**R :** Les durées de vie suivent la durée de validité des références. Le compilateur les déduit dans la plupart des cas via des « règles d'élision à vie ». Vous avez besoin d'annotations explicites lorsque le compilateur ne peut pas déterminer la relation entre les durées de vie d'entrée et de sortie - généralement lorsqu'une fonction prend plusieurs références et en renvoie une. Les durées de vie évitent les références pendantes au moment de la compilation avec un coût d'exécution nul.
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

### Q5 : Quelle est la différence entre`Vec<T>`, les tableaux et les tranches ?
**R :** Les tableaux`[T; N]`sont de taille fixe, alloués par pile, et leur longueur fait partie du type. `Vec<T>`est une collection extensible et allouée par tas. Les tranches`&[T]`sont de gros pointeurs (pointeur + longueur) qui empruntent une partie contiguë d'un tableau ou d'un Vec. Utilisez des tableaux pour les petites données de taille fixe. Utilisez Vec pour les collections dynamiques. Acceptez`&[T]`dans les paramètres de fonction pour une flexibilité maximale.
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : Créer un magasin de valeurs-clés Thread-Safe
**Énoncé du problème :** Implémentez un magasin clé-valeur simultané dans Rust qui prend en charge les opérations`get`,`set`et`delete`à partir de plusieurs threads sans courses de données. Utilisez la mutabilité intérieure et assurez-vous que la mise en œuvre est Rust idiomatique.
**Étape 1 — Comprendre le problème :**
Plusieurs threads doivent lire et écrire sur un HashMap partagé. Le système de propriété de Rust empêche les courses de données au moment de la compilation, mais nous avons besoin d'une mutabilité interne (`RwLock`ou`Mutex`) enveloppée dans`Arc`pour la propriété partagée. `RwLock`permet plusieurs lecteurs simultanés OU un rédacteur exclusif – ce qui est idéal pour les charges de travail lourdes en lecture.
**Étape 2 — Identifiez l'approche :**
- Utilisez`Arc<RwLock<HashMap<K, V>>>`pour un accès partagé et thread-safe.
-`RwLock::read()`pour`get`(plusieurs lecteurs autorisés).
-`RwLock::write()`pour`set`et`delete`(accès exclusif).
- Enveloppez dans une structure avec une API propre.
- Clonez le`Arc`pour chaque thread.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Sécurité des threads : le compilateur Rust garantit l'absence de courses de données – `RwLock` applique l'exclusion mutuelle et`Arc`offre une propriété partagée sécurisée. Si cela compile, c'est correct.
- Performances :`RwLock`est meilleur que`Mutex`pour les charges de travail lourdes en lecture. Pour les charges de travail lourdes en écriture, utilisez`Mutex`(plus simple, sans surcharge lecteur-écrivain).
- Mise à niveau de production : utilisez`parking_lot::RwLock`(plus rapide, sans empoisonnement, empreinte mémoire réduite) ou`dashmap::DashMap`(HashMap simultané sans verrouillage).
### Problème 2 : implémenter un analyseur sans copie
**Énoncé du problème :** Écrivez un analyseur qui extrait les paires clé-valeur d'une chaîne de configuration telle que`"name=Alice;age=30;role=admin"`sans allouer de nouvelles chaînes, en utilisant uniquement des tranches de chaîne qui empruntent à l'entrée.
**Étape 1 — Comprendre le problème :**
Nous devons analyser les paires`key=value`séparées par`;`. La contrainte clé est "zéro copie" — les données renvoyées doivent emprunter à l'entrée`&str`, et non allouer de nouveaux`String`. Cela signifie renvoyer`Vec<(&str, &str)>`avec des durées de vie liées à l'entrée.
**Étape 2 — Identifiez l'approche :**
- Utilisez les méthodes`&str`(`split`,`find`, slicing) — toutes renvoient des tranches`&str`empruntant à l'entrée.
- Évitez`.to_string()`ou`String::from()`n'importe où.
- Annotation à vie : la sortie emprunte à l'entrée —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Zéro copie :`split`,`split_once`et`trim`renvoient tous des tranches`&str`— aucune allocation de tas.
- Les règles d'élision de durée de vie lient correctement les durées de vie de sortie à l'entrée.
- Cas extrêmes : une entrée vide renvoie `[]` ;`=`manquant ignore la paire (via`filter_map`) ; les espaces autour de`=`sont gérés par`trim`.
- Pour une analyse plus complexe, utilisez la caisse`nom`(basée sur un combinateur, également sans copie).
### Problème 3 : implémenter le modèle d'observateur avec des canaux
**Énoncé du problème :** Créez un système de publication-abonnement dans lequel plusieurs abonnés reçoivent des messages d'un éditeur. Utilisez les canaux Rust et assurez-vous que le système gère les abonnés lents sans bloquer l'éditeur.
**Étape 1 — Comprendre le problème :**
Nous avons besoin d'un éditeur qui envoie des messages à plusieurs abonnés. Le canal`mpsc`de Rust est multi-producteur et mono-consommateur — nous avons besoin de l'inverse (multi-producteur et multi-consommateur). Nous pouvons utiliser les canaux`broadcast`(à partir de`tokio`) ou implémenter la diffusion en utilisant plusieurs expéditeurs `mpsc`.
**Étape 2 — Identifiez l'approche :**
- Utilisez`std::sync::mpsc`pour les canaux standard.
- Pour la diffusion : conservez un`Vec<Sender<T>>`et clonez les messages sur chacun.
- Pour les abonnés lents : utilisez`try_send`(non bloquant) ou des canaux bornés avec contre-pression.
- Enveloppez dans une structure`Bus`pour une API propre.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
-`retain`nettoie automatiquement les abonnés morts — aucune fuite de mémoire provenant des threads déconnectés.
-`message.clone()`est nécessaire car chaque abonné a besoin de sa propre copie. Pour les types coûteux à cloner, enveloppez`Arc<T>`.
- Canaux limités : remplacez`mpsc::channel()`par`mpsc::sync_channel(N)`pour la contre-pression – `publish` bloque si le tampon d'un abonné est plein.
- Production : utilisez`tokio::sync::broadcast`pour une publication/sub asynchrone, ou`flume`pour un mpsc plus rapide avec des options limitées/illimitées.
---

## Résumé
Rust est un langage qui vous oblige à réfléchir à la mémoire, à la propriété et à la concurrence – et vous récompense avec un code dont la construction est correcte. La courbe d'apprentissage est réelle, mais les résultats sont significatifs : des programmes aussi rapides que le C mais exempts de bogues de pointeur nul, de courses de données et de fuites de mémoire. Rust n'est pas un langage de productivité à usage général - c'est un langage système lorsque l'exactitude et les performances comptent toutes deux. Son adoption croissante dans l’industrie (y compris le noyau Linux et Android) suggère qu’elle deviendra de plus en plus importante.