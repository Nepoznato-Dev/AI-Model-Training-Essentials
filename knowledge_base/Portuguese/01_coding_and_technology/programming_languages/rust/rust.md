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

# Ferrugem
Rust é uma linguagem de programação compilada e digitada estaticamente, lançada pela primeira vez em 2015, desenvolvida originalmente por Graydon Hoare na Mozilla. A promessa definidora do Rust é **segurança da memória sem coleta de lixo**. Ele consegue isso por meio de seu sistema de propriedade - um conjunto de regras aplicadas em tempo de compilação que elimina categorias inteiras de bugs (desreferências de ponteiro nulo, corridas de dados, buffer overflows, uso após liberação) enquanto produz código tão rápido quanto C ou C++.
Rust foi eleita a linguagem de programação “mais amada” na Stack Overflow Developer Survey por vários anos consecutivos. Ele é cada vez mais usado em programação de sistemas, WebAssembly, ferramentas CLI, infraestrutura em nuvem e como substituto de C/C++ em contextos críticos de segurança. O kernel Linux agora aceita código Rust.
---

## Por que a ferrugem é importante
- **Segurança de memória sem GC**: o sistema de propriedade evita ponteiros nulos, disputas de dados e ponteiros pendentes em tempo de compilação — sem sobrecarga de tempo de execução.
- **Desempenho**: corresponde ou excede C/C++ para a maioria das cargas de trabalho. Nenhum coletor de lixo significa que não há pausas imprevisíveis.
- **Simultaneidade destemida**: O sistema de tipos evita corridas de dados em tempo de compilação. Se compilar, é thread-safe.
- **Ferramentas modernas**:`cargo`(sistema de construção + gerenciador de pacotes) é um dos melhores em qualquer linguagem. `cargo build`,`cargo test`,`cargo doc`todos funcionam imediatamente.
- **WebAssembly**: suporte de primeira classe para compilação para WASM, permitindo desempenho quase nativo em navegadores.
- **Adoção crescente**: Usado por AWS, Google (Android), Microsoft (kernel do Windows), Cloudflare, Discord, Dropbox e Meta.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Curva de aprendizado acentuada** | Propriedade, empréstimos e vidas são diferentes de tudo em outras línguas | Invista tempo em "The Rust Book"; os conceitos combinam com a prática |
| **Compilação lenta** | Os tempos de compilação podem ser longos para grandes projetos | Use`cargo check`para verificação rápida de tipo; compilação incremental ajuda |
| **Tratamento detalhado de erros** |  Os operadores`Result<T, E>`e`?`requerem tratamento explícito | Use`anyhow`para aplicativos,`thiserror`para bibliotecas |
| **Mercado de trabalho menor** | Menos trabalhos Rust do que Java, Python ou JavaScript (mas crescendo rapidamente) | A maioria das funções do Rust são em programação de sistemas, criptografia ou infraestrutura |
| **Ecossistema imaturo** | Menos bibliotecas que Python/Java/JS para alguns domínios | O ecossistema está a crescer rapidamente; muitas caixas são de excelente qualidade |
---

## Fundamentos de sintaxe
### Estrutura Básica
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

### Propriedade e empréstimo
Esta é a principal inovação da Rust. Cada valor tem exatamente um proprietário. Quando o proprietário sai do escopo, o valor é eliminado.
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

### Estruturas, enumerações e correspondência de padrões
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

### Tratamento de erros
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

## Sintaxe e padrões avançados
### Genéricos e limites de características
Os genéricos permitem escrever código que funciona com qualquer tipo, mantendo a segurança total do tipo. As características definem o comportamento compartilhado.
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

### Macros
Rust possui dois tipos de macros: declarativas (`macro_rules!`) e procedurais (derivadas, atributos, semelhantes a funções).
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

### Correspondência e desestruturação avançada de padrões
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

### Sobrecarga do Operador
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

### Hierarquias de erros personalizadas
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

## Simultaneidade e paralelismo
### Modelo de Thread e Sincronização
O sistema de propriedade do Rust evita corridas de dados em tempo de compilação. As características`Send`e`Sync`reforçam a segurança do encadeamento.
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

### Canais — Passagem de Mensagens
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

### Assíncrono/Aguarde com Tokio
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

### Threads com escopo (Rust 1.63+)
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

## Configuração do projeto e sistema de construção
### Estrutura do Projeto
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

### Configuração do Cargo.toml
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

### Comandos de Carga Essenciais
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

### Pipeline de CI/CD (ações do GitHub)
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

## Teste
### Testes unitários
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

### Testes de Integração
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

### Teste de referência
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

## Interoperabilidade
###FFI com C
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

### Chamando Rust de Python (PyO3)
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

## Padrões de Projeto
### Padrão do Construtor
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

### Padrão Newtype (Segurança de Tipo)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Padrão de repositório com características
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

## Desempenho e otimização
### Ferramentas de criação de perfil
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

### Técnicas de otimização
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

## Implantação
### Compilação Cruzada
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Implantação do Docker
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

### Implantação do WebAssembly
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## O Ecossistema
| Ferramenta | Finalidade |
|------|---------|
| **carga** | Sistema de compilação, gerenciador de pacotes, executor de testes, gerador de documentos |
| **crates.io** | Registro de pacotes (mais de 150.000 caixas) |
| **ferrugem** | Formatador de código |
| **cortante** | Linter com centenas de verificações úteis |
| **Tóquio** | Tempo de execução assíncrono (o padrão para Rust assíncrono) |
| **serde** | Estrutura de serialização/desserialização |
| **actix-web/axum** | Estruturas web |
| **diesel/sqlx** | ORMs de banco de dados / construtores de consultas |
---

## Quando usar ferrugem
| Cenário | Por que ferrugem | Melhor Alternativa |
|----------|---------|-------------------|
| Programação de sistemas | Segurança de memória + desempenho | C/C++ se você não precisar de garantias de segurança |
| WebAssembly | O melhor suporte WASM da categoria | -- |
| Ferramentas CLI | Binário único rápido e excelente UX | Opte por CLIs mais simples |
| Sistemas embarcados | Sem GC, acesso a hardware, segurança | C para incorporação mais simples |
| Código crítico para desempenho | Corresponde à velocidade C/C++ | -- |
| Infraestrutura em nuvem | Adoção crescente (AWS, Cloudflare) | Busque um desenvolvimento mais rápido |
| Desenvolvimento geral de aplicações | Curva de aprendizado acentuada retarda desenvolvimento | Python, Go, Java |
| Back-ends da Web | Possível, mas o ecossistema é mais jovem | Vá, Node.js, Python |
| Ciência de dados / ML | Não é o ecossistema para isso | Pitão, R |
| Scripts/protótipos rápidos | Muito detalhado e lento para escrever | Python, JavaScript |
---

## Perguntas e respostas sintéticas
### Q1: Qual é o sistema de propriedade e por que Rust o possui?
**R:** Cada valor em Rust tem exatamente um proprietário. Quando o proprietário sai do escopo, o valor é eliminado (memória liberada). Isso elimina a necessidade de um coletor de lixo e garante a segurança da memória. Atribuição, parâmetros de função e valores de retorno transferem propriedade ("mover"). Para compartilhar sem transferir, use referências (`&T`para empréstimo,`&mut T`para empréstimo mutável). O compilador impõe: você não pode ter uma referência mutável e uma referência imutável para o mesmo valor simultaneamente.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### Q2: Quando devo usar`String`vs `&str`?
**R:**`String`é uma string UTF-8 própria, alocada em heap e expansível. `&str`é uma referência emprestada para uma fatia de string UTF-8 (pode apontar para um`String`, uma string literal ou parte de qualquer uma). Use`String`quando precisar possuir, modificar ou construir uma sequência. Use`&str`para parâmetros de função (mais flexível — aceita ambos), visualizações somente leitura e literais de string. Aceite`&str`nas assinaturas de função; retorne`String`quando o chamador precisar de propriedade.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### Q3: Como o Rust lida com erros sem exceções?
**R:** Rust usa o enum`Result<T, E>`para erros recuperáveis ​​e`panic!`para erros irrecuperáveis. Funções que podem falhar retornam`Result`. O operador`?`propaga erros de forma concisa. Essa abordagem torna o tratamento de erros explícito — você não pode ignorar acidentalmente um erro. Use`anyhow`para tratamento de erros de aplicativo (contexto conveniente) e`thiserror`para tipos de erros de biblioteca (derivar macros).
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

### Q4: O que são tempos de vida e quando preciso anotá-los?
**R:** As vidas úteis monitoram por quanto tempo as referências são válidas. O compilador os infere na maioria dos casos por meio de "regras de elisão vitalícias". Você precisa de anotações explícitas quando o compilador não consegue determinar a relação entre os tempos de vida de entrada e saída — normalmente quando uma função recebe múltiplas referências e retorna uma. As vidas úteis evitam referências pendentes em tempo de compilação com custo zero de tempo de execução.
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

### Q5: Qual é a diferença entre`Vec<T>`, matrizes e fatias?
**R:** Os arrays`[T; N]`têm tamanho fixo, são alocados em pilha e seu comprimento faz parte do tipo. `Vec<T>`é uma coleção expansível e alocada em heap. As fatias`&[T]`são ponteiros grossos (ponteiro + comprimento) que emprestam uma parte contígua de um array ou Vec. Use arrays para dados pequenos e de tamanho fixo. Use Vec para coleções dinâmicas. Aceite`&[T]`nos parâmetros de função para máxima flexibilidade.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construa um armazenamento de valores-chave seguro para threads
**Declaração do problema:** Implemente um armazenamento de valor-chave simultâneo em Rust que suporta operações`get`,`set`e`delete`de vários threads sem corridas de dados. Use a mutabilidade interior e garanta que a implementação seja Rust idiomática.
**Etapa 1 — Entenda o problema:**
Vários threads precisam ler e gravar em um HashMap compartilhado. O sistema de propriedade do Rust evita corridas de dados em tempo de compilação, mas precisamos de mutabilidade interna (`RwLock`ou`Mutex`) envolvida em`Arc`para propriedade compartilhada. `RwLock`permite vários leitores simultâneos OU um gravador exclusivo – melhor para cargas de trabalho com muita leitura.
**Etapa 2 — Identifique a abordagem:**
- Use`Arc<RwLock<HashMap<K, V>>>`para acesso compartilhado e seguro para threads.
-`RwLock::read()`para`get`(são permitidos vários leitores).
-`RwLock::write()`para`set`e`delete`(acesso exclusivo).
- Envolver uma estrutura com uma API limpa.
- Clone o`Arc`para cada thread.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Segurança de thread: o compilador Rust não garante disputas de dados —`RwLock`impõe exclusão mútua e`Arc`fornece propriedade compartilhada segura. Se isso compilar, está correto.
- Desempenho:`RwLock`é melhor que`Mutex`para cargas de trabalho com muita leitura. Para cargas de trabalho com muita gravação, use`Mutex`(mais simples, sem sobrecarga de leitor-gravador).
- Atualização de produção: use`parking_lot::RwLock`(mais rápido, sem envenenamento, menor consumo de memória) ou`dashmap::DashMap`(HashMap simultâneo sem bloqueio).
### Problema 2: Implementar um analisador de cópia zero
**Declaração do problema:** Escreva um analisador que extraia pares de valores-chave de uma string de configuração como`"name=Alice;age=30;role=admin"`sem alocar novas Strings — usando apenas fatias de string emprestadas da entrada.
**Etapa 1 — Entenda o problema:**
Precisamos analisar pares`key=value`separados por`;`. A restrição principal é "cópia zero" - os dados retornados devem ser emprestados da entrada`&str`, e não alocar novos`String`s. Isso significa retornar`Vec<(&str, &str)>`com tempos de vida vinculados à entrada.
**Etapa 2 — Identifique a abordagem:**
- Use métodos`&str`(`split`,`find`, fatiamento) - todos retornam fatias`&str`emprestadas da entrada.
- Evite`.to_string()`ou`String::from()`em qualquer lugar.
- Anotação vitalícia: a saída é emprestada da entrada —`fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Cópia zero:`split`,`split_once`e`trim`retornam fatias`&str`— sem alocações de heap.
- As regras de elisão de tempo de vida vinculam corretamente os tempos de vida da saída à entrada.
- Casos extremos: entrada vazia retorna`[]`; faltando`=`ignora o par (via`filter_map`); o espaço em branco em torno de`=`é tratado por`trim`.
- Para uma análise mais complexa, use a caixa`nom`(baseada em combinador, também com cópia zero).
### Problema 3: Implementar o Padrão Observador com Canais
**Declaração do problema:** Crie um sistema de publicação-assinatura onde vários assinantes recebem mensagens de um editor. Use canais Rust e garanta que o sistema lide com assinantes lentos sem bloquear o editor.
**Etapa 1 — Entenda o problema:**
Precisamos de um editor enviando mensagens para vários assinantes. O canal`mpsc`de Rust é multiprodutor e consumidor único - precisamos do inverso (produtor único e multiconsumidor). Podemos usar canais`broadcast`(de`tokio`) ou implementar fan-out usando vários remetentes `mpsc`.
**Etapa 2 — Identifique a abordagem:**
- Use`std::sync::mpsc`para canais padrão.
- Para distribuição: mantenha um`Vec<Sender<T>>`e clone mensagens para cada um.
- Para assinantes lentos: use`try_send`(sem bloqueio) ou canais limitados com contrapressão.
- Envolver uma estrutura`Bus`para API limpa.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
-`retain`limpa assinantes mortos automaticamente — sem vazamentos de memória devido a threads desconectados.
-`message.clone()`é necessário porque cada assinante precisa de sua própria cópia. Para tipos caros para clonar, inclua`Arc<T>`.
- Canais limitados: substitua`mpsc::channel()`por`mpsc::sync_channel(N)`para contrapressão — blocos`publish`se o buffer de um assinante estiver cheio.
- Produção: use`tokio::sync::broadcast`para pub/sub assíncrono ou`flume`para um mpsc mais rápido com opções limitadas/ilimitadas.
---

## Resumo
Rust é uma linguagem que força você a pensar sobre memória, propriedade e simultaneidade – e recompensa você com código que está correto por construção. A curva de aprendizado é real, mas a recompensa é significativa: programas que são tão rápidos quanto C, mas livres de bugs de ponteiro nulo, corridas de dados e vazamentos de memória. Rust não é uma linguagem de produtividade de uso geral – é uma linguagem de sistema para quando a correção e o desempenho são importantes. A sua crescente adoção na indústria (incluindo o kernel Linux e Android) sugere que será cada vez mais importante.