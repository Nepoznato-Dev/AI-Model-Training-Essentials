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
# Óxido
Rust es un lenguaje de programación compilado y tipado estáticamente lanzado por primera vez en 2015, desarrollado originalmente por Graydon Hoare en Mozilla. La promesa definitoria de Rust es **seguridad de la memoria sin recolección de basura**. Lo logra a través de su sistema de propiedad: un conjunto de reglas aplicadas en tiempo de compilación que elimina categorías enteras de errores (desreferencias de puntero nulo, carreras de datos, desbordamientos de búfer, uso después de la liberación) mientras produce código tan rápido como C o C++.
Rust ha sido votado como el lenguaje de programación "más querido" en la encuesta para desarrolladores de Stack Overflow durante varios años consecutivos. Se utiliza cada vez más en programación de sistemas, WebAssembly, herramientas CLI, infraestructura de nube y como reemplazo de C/C++ en contextos críticos para la seguridad. El kernel de Linux ahora acepta código Rust.
---

## Por qué es importante el óxido
- **Seguridad de la memoria sin GC**: el sistema de propiedad evita punteros nulos, carreras de datos y punteros colgantes en tiempo de compilación, sin sobrecarga de tiempo de ejecución.
- **Rendimiento**: iguala o supera a C/C++ para la mayoría de las cargas de trabajo. Sin recolector de basura, no hay pausas impredecibles.
- **Simultaneidad intrépida**: el sistema de tipos evita carreras de datos en el momento de la compilación. Si se compila, es seguro para subprocesos.
- **Herramientas modernas**:`cargo`(sistema de compilación + administrador de paquetes) es uno de los mejores en cualquier idioma.  `cargo build`, `cargo test`,`cargo doc`funcionan desde el primer momento.
- **WebAssembly**: soporte de primera clase para compilar en WASM, lo que permite un rendimiento casi nativo en los navegadores.
- **Adopción creciente**: utilizado por AWS, Google (Android), Microsoft (kernel de Windows), Cloudflare, Discord, Dropbox y Meta.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Curva de aprendizaje pronunciada** | Propiedad, préstamo, vida útil no se parecen a nada en otros idiomas | Invierta tiempo en "The Rust Book"; los conceptos encajan con la práctica |
| **Compilación lenta** | Los tiempos de compilación pueden ser largos para proyectos grandes | Utilice`cargo check`para una verificación rápida de tipos; la compilación incremental ayuda |
| **Manejo detallado de errores** |  Los operadores`Result<T, E>`y`?`requieren un manejo explícito | Utilice`anyhow`para aplicaciones,`thiserror`para bibliotecas |
| **Mercado laboral más pequeño** | Menos trabajos en Rust que en Java, Python o JavaScript (pero creciendo rápidamente) | La mayoría de los roles de Rust se encuentran en programación de sistemas, criptografía o infraestructura |
| **Ecosistema inmaduro** | Menos bibliotecas que Python/Java/JS para algunos dominios | El ecosistema está creciendo rápidamente; muchas cajas son de excelente calidad |
---

## Fundamentos de sintaxis
### Estructura básica
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

### Propiedad y endeudamiento
Esta es la principal innovación de Rust. Cada valor tiene exactamente un dueño. Cuando el propietario sale del alcance, el valor se elimina.
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

### Estructuras, enumeraciones y coincidencia de patrones
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

### Manejo de errores
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

## Sintaxis y patrones avanzados
### Genéricos y límites de rasgos
Los genéricos le permiten escribir código que funcione con cualquier tipo manteniendo la seguridad total de los tipos. Los rasgos definen el comportamiento compartido.
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
Rust tiene dos tipos de macros: declarativas (`macro_rules!`) y de procedimiento (derivadas, de atributos, similares a funciones).
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

### Coincidencia y desestructuración avanzada de patrones
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

### Sobrecarga del operador
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

### Jerarquías de errores personalizadas
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

## Concurrencia y paralelismo
### Modelo de hilo y sincronización
El sistema de propiedad de Rust evita las carreras de datos en el momento de la compilación. Los rasgos`Send`y`Sync`imponen la seguridad de los subprocesos.
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

### Canales: transmisión de mensajes
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

### Asíncrono/Espera con Tokio
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

### Hilos con alcance (Rust 1.63+)
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

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto
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

### Configuración de Cargo.toml
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

### Comandos de carga esenciales
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

### Canalización de CI/CD (acciones de GitHub)
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

## Pruebas
### Pruebas unitarias
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

### Pruebas de integración
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

### Pruebas comparativas
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

## Interoperabilidad
### FFI con C
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

### Llamar a Rust desde Python (PyO3)
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

## Patrones de diseño
### Patrón de constructor
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

### Nuevo patrón de tipo (seguridad de tipos)
```rust
struct Meters(f64);
struct Seconds(f64);

fn calculate_speed(distance: Meters, time: Seconds) -> f64 {
    distance.0 / time.0
}

// Cannot accidentally mix up Meters and Seconds — compiler error!
// calculate_speed(Seconds(10.0), Meters(5.0));  // Type mismatch
```

### Patrón de repositorio con rasgos
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
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

### Técnicas de optimización
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

## Implementación
### Compilación cruzada
```bash
rustup target add x86_64-unknown-linux-musl
rustup target add aarch64-unknown-linux-gnu

# Cross-compile using cross (Docker-based)
cargo install cross
cross build --release --target x86_64-unknown-linux-musl
cross build --release --target aarch64-unknown-linux-gnu
```

### Implementación de Docker
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

### Implementación de ensamblaje web
```bash
rustup target add wasm32-unknown-unknown
cargo build --release --target wasm32-unknown-unknown

# Use wasm-pack for JavaScript interop
cargo install wasm-pack
wasm-pack build --target web
```

---

## El ecosistema
| Herramienta | Propósito |
|------|---------|
| **carga** | Sistema de compilación, administrador de paquetes, ejecutor de pruebas, generador de documentos |
| **cajas.io** | Registro de paquetes (más de 150.000 cajas) |
| **óxido** | Formateador de código |
| **cortante** | Linter con cientos de comprobaciones útiles |
| **tokio** | Tiempo de ejecución asíncrono (el estándar para Rust asíncrono) |
| **serde** | Marco de serialización/deserialización |
| **actix-web/axum** | Marcos web |
| **diésel/sqlx** | ORM de bases de datos/generadores de consultas |
---

## Cuándo utilizar óxido
| Escenario | ¿Por qué oxidarse? Mejor alternativa |
|----------|---------|-------------------|
| Programación de sistemas | Seguridad de la memoria + rendimiento | C/C++ si no necesitas garantías de seguridad |
| Asamblea web | El mejor soporte WASM de su clase | -- |
| Herramientas CLI | Rápido, binario único, excelente UX | Opte por CLI más simples |
| Sistemas integrados | Sin GC, acceso al hardware, seguridad | C para incrustado más simple |
| Código crítico para el rendimiento | Coincide con la velocidad de C/C++ | -- |
| Infraestructura en la nube | Adopción creciente (AWS, Cloudflare) | Opte por un desarrollo más rápido |
| Desarrollo de aplicaciones generales | La pronunciada curva de aprendizaje ralentiza el desarrollo | Python, Ir, Java |
| Servidores web | Posible pero el ecosistema es más joven | Ir, Node.js, Python |
| Ciencia de datos / ML | No es el ecosistema para esto | Pitón, R |
| Scripts rápidos/prototipos | Demasiado detallado y lento para escribir | Python, JavaScript |
---

## Preguntas y respuestas sintéticas
### P1: ¿Qué es el sistema de propiedad y por qué lo tiene Rust?
**R:** Cada valor en Rust tiene exactamente un propietario. Cuando el propietario sale del alcance, el valor se elimina (se libera memoria). Esto elimina la necesidad de un recolector de basura y al mismo tiempo garantiza la seguridad de la memoria. La asignación, los parámetros de función y los valores de retorno transfieren la propiedad ("mover"). Para compartir sin transferir, utilice referencias (`&T` para préstamos,`&mut T`para préstamos mutables). El compilador exige: no se puede tener una referencia mutable y una referencia inmutable al mismo valor simultáneamente.
```rust
let s1 = String::from("hello");
let s2 = s1;           // s1 is MOVED to s2 — s1 is no longer valid
// println!("{}", s1); // Error: value borrowed after move

let s3 = String::from("world");
let len = calculate_length(&s3);  // Borrow — s3 stays valid
fn calculate_length(s: &String) -> usize { s.len() }
```

### P2: ¿Cuándo debo utilizar`String`frente a `&str`?
**R:**`String`es una cadena UTF-8 de propiedad, asignada en montón y cultivable. `&str`es una referencia prestada a un segmento de cadena UTF-8 (puede apuntar a un `String`, un literal de cadena o parte de cualquiera de ellos). Utilice`String`cuando necesite poseer, modificar o crear una cadena. Utilice`&str`para parámetros de función (más flexible: acepta ambos), vistas de solo lectura y literales de cadena. Acepte`&str`en firmas de funciones; devuelve`String`cuando la persona que llama necesita propiedad.
```rust
// Accept &str — works with both String and &str
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)  // Returns owned String
}

let owned = String::from("Alice");
greet(&owned);         // &String coerces to &str
greet("Bob");          // &str literal works directly
```

### P3: ¿Cómo maneja Rust los errores sin excepciones?
**R:** Rust utiliza la enumeración`Result<T, E>`para errores recuperables y`panic!`para los irrecuperables. Las funciones que pueden fallar devuelven`Result`. El operador`?`propaga los errores de forma concisa. Este enfoque hace que el manejo de errores sea explícito: no se puede ignorar un error accidentalmente. Utilice`anyhow`para el manejo de errores de aplicaciones (contexto conveniente) y`thiserror`para tipos de errores de biblioteca (derivar macros).
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

### P4: ¿Qué son las duraciones y cuándo debo anotarlas?
**R:** La vida útil registra cuánto tiempo son válidas las referencias. El compilador los infiere en la mayoría de los casos mediante "reglas de elisión de por vida". Necesita anotaciones explícitas cuando el compilador no puede determinar la relación entre la vida útil de la entrada y la salida, generalmente cuando una función toma varias referencias y devuelve una. La vida útil evita referencias pendientes en tiempo de compilación sin costo de tiempo de ejecución.
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

### P5: ¿Cuál es la diferencia entre `Vec<T>`, matrices y sectores?
**R:** Las matrices`[T; N]`son de tamaño fijo, están asignadas en pila y su longitud es parte del tipo. `Vec<T>`es una colección cultivable y asignada en montón. Los sectores`&[T]`son punteros gruesos (puntero + longitud) que toman prestada una porción contigua de una matriz o Vec. Utilice matrices para datos pequeños y de tamaño fijo. Utilice Vec para colecciones dinámicas. Acepte`&[T]`en los parámetros de función para obtener la máxima flexibilidad.
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

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: crear un almacén de valores clave seguro para subprocesos
**Declaración del problema:** Implemente un almacén de valores-clave simultáneo en Rust que admita operaciones `get`,`set`y`delete`desde múltiples subprocesos sin carreras de datos. Utilice la mutabilidad interior y asegúrese de que la implementación sea idiomática de Rust.
**Paso 1: comprenda el problema:**
Varios subprocesos necesitan leer y escribir en un HashMap compartido. El sistema de propiedad de Rust evita las carreras de datos en el momento de la compilación, pero necesitamos mutabilidad interior (`RwLock`o`Mutex`) incluida en`Arc`para la propiedad compartida. `RwLock`permite múltiples lectores simultáneos O un escritor exclusivo, mejor para cargas de trabajo con mucha lectura.
**Paso 2: Identifique el enfoque:**
- Utilice`Arc<RwLock<HashMap<K, V>>>`para acceso compartido y seguro para subprocesos.
-`RwLock::read()`para`get`(se permiten varios lectores).
-`RwLock::write()`para`set`y`delete`(acceso exclusivo).
- Envolver en una estructura con una API limpia.
- Clonar el`Arc`para cada hilo.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Seguridad de subprocesos: el compilador Rust garantiza que no haya carreras de datos:`RwLock`aplica la exclusión mutua y`Arc`proporciona propiedad compartida segura. Si esto se compila, es correcto.
- Rendimiento:`RwLock`es mejor que`Mutex`para cargas de trabajo con mucha lectura. Para cargas de trabajo con mucha escritura, utilice`Mutex`(más simple, sin sobrecarga de lectura y escritura).
- Actualización de producción: use`parking_lot::RwLock`(más rápido, sin envenenamiento, menor uso de memoria) o`dashmap::DashMap`(HashMap concurrente sin bloqueo).
### Problema 2: implementar un analizador de copia cero
**Declaración del problema:** Escriba un analizador que extraiga pares clave-valor de una cadena de configuración como`"name=Alice;age=30;role=admin"`sin asignar nuevas cadenas, utilizando solo segmentos de cadena tomados prestados de la entrada.
**Paso 1: comprenda el problema:**
Necesitamos analizar pares`key=value`separados por `;`. La restricción clave es "copia cero": los datos devueltos deben tomar prestados de la entrada `&str`, no asignar nuevos `String`. Esto significa devolver`Vec<(&str, &str)>`con tiempos de vida vinculados a la entrada.
**Paso 2: Identifique el enfoque:**
- Utilice métodos`&str`(`split`, `find`, corte): todos devuelven cortes`&str`tomados de la entrada.
- Evite`.to_string()`o`String::from()`en cualquier lugar.
- Anotación de por vida: la salida toma prestado de la entrada: `fn parse<'a>(input: &'a str) -> Vec<(&'a str, &'a str)>`.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Copia cero: `split`,`split_once`y`trim`devuelven porciones `&str`, sin asignaciones de montón.
- Las reglas de elisión de duración vinculan correctamente la duración de la salida con la entrada.
- Casos extremos: la entrada vacía devuelve `[]`; falta`=`omite el par (a través de `filter_map`); Los espacios en blanco alrededor de`=`son manejados por `trim`.
- Para un análisis más complejo, utilice la caja`nom`(basada en un combinador, también de copia cero).
### Problema 3: Implementar el patrón de observador con canales
**Declaración del problema:** Cree un sistema de publicación y suscripción en el que varios suscriptores reciban mensajes de un editor. Utilice canales de Rust y asegúrese de que el sistema maneje suscriptores lentos sin bloquear al editor.
**Paso 1: comprenda el problema:**
Necesitamos que un editor envíe mensajes a varios suscriptores. El canal`mpsc`de Rust es multiproductor y de un solo consumidor; necesitamos lo contrario (un solo productor y multiconsumidor). Podemos usar canales`broadcast`(de `tokio`) o implementar distribución usando múltiples remitentes `mpsc`.
**Paso 2: Identifique el enfoque:**
- Utilice`std::sync::mpsc`para canales estándar.
- Para distribución en abanico: mantenga un`Vec<Sender<T>>`y clone mensajes para cada uno.
- Para suscriptores lentos: use`try_send`(sin bloqueo) o canales acotados con contrapresión.
- Envolver en una estructura`Bus`para una API limpia.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
-`retain`limpia automáticamente los suscriptores muertos: no hay pérdidas de memoria por subprocesos desconectados.
-`message.clone()`es necesario porque cada suscriptor necesita su propia copia. Para tipos costosos de clonar, envuélvalos en`Arc<T>`.
- Canales delimitados: reemplace`mpsc::channel()`con`mpsc::sync_channel(N)`para contrapresión:`publish`se bloquea si el búfer de un suscriptor está lleno.
- Producción: utilice`tokio::sync::broadcast`para pub/sub asíncrono, o`flume`para un mpsc más rápido con opciones limitadas/ilimitadas.
---

## Resumen
Rust es un lenguaje que te obliga a pensar en la memoria, la propiedad y la concurrencia, y te recompensa con un código cuya construcción es correcta. La curva de aprendizaje es real, pero la recompensa es significativa: programas que son tan rápidos como C pero libres de errores de puntero nulo, carreras de datos y pérdidas de memoria. Rust no es un lenguaje de productividad de propósito general, es un lenguaje de sistemas para cuando tanto la corrección como el rendimiento son importantes. Su creciente adopción en la industria (incluido el kernel de Linux y Android) sugiere que será cada vez más importante.