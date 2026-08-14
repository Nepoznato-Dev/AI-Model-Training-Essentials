<!--
---
# Metadata
title: "Rust — Syntax Reference"
description: "Detailed syntax reference for Rust covering operators, control flow, functions, ownership, data structures, OOP, error handling, traits, concurrency, and advanced features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [rust, syntax-reference, operators, control-flow, ownership, traits, concurrency, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Rust — Riferimento alla sintassi
Questo documento fornisce un riferimento completo e strutturato alla sintassi per Rust. Completa il riferimento principale a Rust concentrandosi su modelli di sintassi esaustivi, tabelle degli operatori e meccanismi interni del sistema di proprietà, tratti e concorrenza.
---

## Operatori ed espressioni
### Operatori aritmetici
| Operatore | Nome | Esempio | Note |
|----------|------|---------|-------|
| `+`| Aggiunta | `3 + 2`| Anche la concatenazione`String`tramite`format!`|
| `-`| Sottrazione | `3 - 2`| |
| `*`| Moltiplicazione | `3 * 2`| |
| `/`| Divisione | `7 / 2`| Divisione intera per numeri interi:`3`|
| `%`| Resto | `7 % 2`| `1`|
| `-x`| Negazione | `-5`| |
### Confronto e operatori logici
| Operatore | Nome | Esempio | Note |
|----------|------|---------|-------|
| `==`| Uguale | `x == y`| Richiede`PartialEq`|
| `!=`| Non uguali | `x != y`| |
|  `<`, `>`, `<=`,`>=`| Ordinare | `x >= y`| Richiede`PartialOrd`|
| `&&`| AND logico | `a && b`| Cortocircuito |
| `\|\|`| OR logico | `a \|\| b`| Cortocircuito |
| `!`| NON logico | `!true`| |
### Operatori bit a bit
| Operatore | Nome | Esempio | Note |
|----------|------|---------|-------|
| `&`| E | `5 & 3`| `1`|
| `\|`| OPPURE | `5 \| 3`| `7`|
| `^`| XOR | `5 ^ 3`| `6`|
| `!`| NON | `!0b1010u8`| Complemento bit a bit |
| `<<`| Maiusc sinistro | `5 << 1`| `10`|
| `>>`| Maiusc destro | `5 >> 1`| `2`|
### Precedenza degli operatori (dal più alto al più basso)
| Precedenza | Operatori | Note |
|------------|-----------|-------|
| 1 (più alto) | `()`percorsi`.`:: | |
| 2| Chiamate di metodo, accesso al campo | Deriferimento automatico |
| 3| `-`(negazione),`!`,`*`(derif) | |
| 4| `as`(tipo lancio) | |
| 5| `*``/``%`| |
| 6| `+``-` | |
| 7| `<<``>>` | |
| 8| `&`| |
| 9| `^`| |
| 10| `\|`| |
| 11| `==``!=``<``>``<=``>=` | |
| 12| `&&`| |
| 13| `\|\|`| |
| 14| `..``..=` | Gamma |
| 15| `=``+=` ecc. | Compito |
| 16 (il più basso) | `return``break``continue`| |
---

## Flusso di controllo
### Espressioni condizionali
```rust
// if / else if / else
let status = if score >= 90 {
    "excellent"
} else if score >= 70 {
    "good"
} else {
    "needs work"
};

// if is an expression — returns a value
let absolute = if x >= 0 { x } else { -x };

// let-else (Rust 1.65+) — early return on pattern mismatch
let Some(value) = maybe_value else {
    return Err("missing value");
};

// match — exhaustive pattern matching
match command {
    "quit" => app.quit(),
    "help" => print_help(),
    name if name.starts_with("goto ") => {
        let target = &name[5..];
        app.navigate(target);
    }
    _ => println!("Unknown command"),
}

// match as expression
let description = match status_code {
    200 => "OK",
    404 => "Not Found",
    500..=599 => "Server Error",
    _ => "Unknown",
};
```

### Cicli
```rust
// loop — infinite loop with break value
let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;  // loop returns a value
    }
};

// while loop
let mut n = 0;
while n < 5 {
    println!("{}", n);
    n += 1;
}

// for loop with range
for i in 0..10 {          // 0 to 9 (exclusive)
    print!("{} ", i);
}
for i in 0..=10 {         // 0 to 10 (inclusive)
    print!("{} ", i);
}

// for loop over iterator
for item in &collection {
    process(item);
}
for (i, item) in collection.iter().enumerate() {
    println!("{}: {}", i, item);
}

// Labeled loops
'outer: for i in 0..5 {
    for j in 0..5 {
        if i * j > 6 {
            break 'outer;
        }
    }
}
```

---

## Funzioni e Chiusure
### Sintassi della funzione
```rust
// Basic function with type annotations
fn add(a: i32, b: i32) -> i32 {
    a + b   // No semicolon = implicit return
}

// Multiple return values via tuple
fn divide(a: f64, b: f64) -> (f64, f64) {
    (a / b, a % b)   // (quotient, remainder)
}
let (quot, rem) = divide(10.0, 3.0);

// Diverging function (never returns)
fn die(message: &str) -> ! {
    eprintln!("Fatal: {}", message);
    std::process::exit(1);
}

// Generic function
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut max = &list[0];
    for item in &list[1..] {
        if item > max { max = item; }
    }
    max
}

// Const function — evaluated at compile time
const fn factorial(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * factorial(n - 1) }
}
const FACT_10: u64 = factorial(10);  // Computed at compile time

// Function pointers
fn apply(f: fn(i32) -> i32, x: i32) -> i32 {
    f(x)
}
fn double(x: i32) -> i32 { x * 2 }
let result = apply(double, 5);  // 10
```

### Chiusure
```rust
// Closure syntax
let add = |a: i32, b: i32| -> i32 { a + b };
let square = |x: i32| x * x;       // Single expression: no braces needed
let greet = || println!("Hello!");  // No parameters

// Closures capture their environment
let name = String::from("Alice");
let greet = || println!("Hello, {}!", name);  // Captures by reference
greet();

let mut count = 0;
let mut increment = || { count += 1; };  // Captures by mutable reference
increment();

// Move closures — take ownership of captured variables
let data = vec![1, 2, 3];
let handler = move || {
    println!("Data: {:?}", data);  // 'data' is moved into closure
};
// println!("{:?}", data);  // Error: data has been moved

// Closure as parameter
fn execute_twice<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(f(x))
}

// Fn trait hierarchy:
// FnOnce — can be called once (consumes captured variables)
// FnMut  — can mutate captured variables
// Fn     — only borrows immutably (most restrictive)
fn with_data<F: Fn(&str)>(callback: F) {
    callback("processed data");
}
```

---

## Proprietà e prestiti
### Regole fondamentali
```rust
// Rule 1: Each value has exactly one owner
let s1 = String::from("hello");
let s2 = s1;           // s1 moved to s2
// println!("{}", s1); // Error: s1 is no longer valid

// Rule 2: References allow borrowing without taking ownership
let s3 = String::from("world");
let r1 = &s3;          // Immutable borrow
let r2 = &s3;          // Multiple immutable borrows OK
println!("{} {}", r1, r2);

// Rule 3: You cannot have mutable and immutable borrows simultaneously
let mut s4 = String::from("hello");
let r3 = &s4;          // Immutable borrow
// let r4 = &mut s4;   // Error: cannot borrow as mutable while immutably borrowed
// println!("{}", r3); // (r3 used here, so it's still alive)
drop(r3);              // End immutable borrow
let r4 = &mut s4;      // Now OK
r4.push_str(" world");

// Copy types — implement Copy trait, assignment copies instead of moves
let x = 42;
let y = x;             // Copy — x is still valid
println!("{} {}", x, y);  // OK

// Clone — explicit deep copy
let s5 = String::from("hello");
let s6 = s5.clone();
println!("{} {}", s5, s6);  // Both valid
```

### A vita
```rust
// Lifetime annotations — tell the compiler how long references live
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Lifetime elision rules (compiler infers these):
// 1. Each parameter gets its own lifetime
// 2. If there's exactly one input lifetime, it's assigned to all outputs
// 3. If one parameter is &self, its lifetime is assigned to all outputs
fn first_word(s: &str) -> &str {  // Lifetime elided: fn first_word<'a>(s: &'a str) -> &'a str
    s.split_whitespace().next().unwrap_or("")
}

// Struct with borrowed data
struct TextExcerpt<'a> {
    text: &'a str,
    word_count: usize,
}

impl<'a> TextExcerpt<'a> {
    fn new(text: &'a str) -> Self {
        Self {
            text,
            word_count: text.split_whitespace().count(),
        }
    }
}

// 'static lifetime — lives for the entire program
let static_str: &'static str = "I live forever";
```

---

## Strutture dati
### Panoramica dei tipi integrati
| Digitare | Stack/Heap | Taglia | Mutabilità | Note |
|------|-----------|------|------------|-------|
| Primitive (`i32`,`f64`,`bool`,`char`) | Pila | Risolto | Immutabile per impostazione predefinita | `Copy`|
| `[T; N]`(matrice) | Pila | Risolto | Mutevole con`mut`| Dimensione fissa,`Copy`se T è`Copy`|
| `Vec<T>`| Mucchio | Dinamico | Mutevole con`mut`| Coltivabile |
| `String`| Mucchio | Dinamico | Mutevole con`mut`| UTF-8, espandibile |
| `&[T]`(fetta) | Pila (fat ptr) | Visualizzazione dinamica | Dipende da`&`o`&mut`| Vista in prestito |
| `HashMap<K, V>`| Mucchio | Dinamico | Mutevole con`mut`| O(1) ricerca media |
| `BTreeMap<K, V>`| Mucchio | Dinamico | Mutabile con`mut`| Ricerca O(log n), ordinata |
| `HashSet<T>`| Mucchio | Dinamico | — | O(1) medio, nessun duplicato |
### Vettori
```rust
// Creation
let mut v = vec![1, 2, 3, 4, 5];
let zeros = vec![0; 10];                    // [0, 0, 0, ..., 0] (10 elements)
let from_iter: Vec<i32> = (0..10).collect();

// Access
let first = &v[0];                          // Panic on out-of-bounds
let safe = v.get(0);                        // Option<&T> — None on out-of-bounds
let last = v.last();                        // Option<&T>
let slice = &v[1..3];                       // &[2, 3] — slice

// Mutation
v.push(6);                                  // Add to end
let popped = v.pop();                       // Remove from end — Option<T>
v.insert(0, 0);                             // Insert at index
v.remove(0);                                // Remove at index
v.truncate(3);                              // Keep first 3 elements
v.clear();                                  // Remove all
v.retain(|&x| x > 2);                       // Keep elements matching predicate
v.sort();                                   // In-place sort (requires Ord)
v.sort_by(|a, b| b.cmp(a));                // Custom sort
v.dedup();                                  // Remove consecutive duplicates
v.reverse();                                // In-place reverse

// Iteration
for item in &v { print!("{} ", item); }
for (i, item) in v.iter().enumerate() { println!("{}: {}", i, item); }
for item in &mut v { *item *= 2; }         // Mutate in place

// Functional patterns
let doubled: Vec<i32> = v.iter().map(|&x| x * 2).collect();
let sum: i32 = v.iter().sum();
let max = v.iter().max();                   // Option<&i32>
let filtered: Vec<&i32> = v.iter().filter(|&&x| x > 3).collect();
```

### HashMap
```rust
use std::collections::{HashMap, BTreeMap, HashSet};

// Creation
let mut scores: HashMap<String, i32> = HashMap::new();
scores.insert("Alice".to_string(), 95);
scores.insert("Bob".to_string(), 87);

// From iterator
let map: HashMap<_, _> = vec![("a", 1), ("b", 2)].into_iter().collect();

// Access
let score = scores.get("Alice");            // Option<&i32>
let score = scores["Alice"];                // Panic if missing
let score = scores.get("Alice").copied().unwrap_or(0);

// Entry API — insert if absent, modify if present
scores.entry("Charlie".to_string()).or_insert(0);
*scores.entry("Alice".to_string()).or_insert(0) += 5;

// Word frequency with entry API
let text = "hello world hello rust hello";
let mut word_count: HashMap<&str, usize> = HashMap::new();
for word in text.split_whitespace() {
    *word_count.entry(word).or_insert(0) += 1;
}

// Mutation
scores.insert("Alice".to_string(), 100);    // Update
scores.remove("Bob");                        // Remove

// Iteration
for (key, value) in &scores {
    println!("{}: {}", key, value);
}

// Conversion
let keys: Vec<&String> = scores.keys().collect();
let values: Vec<&i32> = scores.values().collect();

// HashSet
let mut set: HashSet<i32> = HashSet::from([1, 2, 3, 4]);
set.insert(5);
let contains_3 = set.contains(&3);          // true
let union: HashSet<_> = set.union(&HashSet::from([4, 5, 6])).collect();
let intersection: HashSet<_> = set.intersection(&HashSet::from([3, 4, 5])).collect();
```

### Enumerazioni e corrispondenza di modelli
```rust
// Basic enum
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

// Enum with data
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

// Pattern matching with destructuring
fn process(msg: Message) {
    match msg {
        Message::Quit => println!("Quitting"),
        Message::Move { x, y } => println!("Move to ({}, {})", x, y),
        Message::Write(text) => println!("Write: {}", text),
        Message::ChangeColor(r, g, b) => println!("Color: {}, {}, {}", r, g, b),
    }
}

// if let — single pattern match
if let Message::Write(text) = msg {
    println!("Text: {}", text);
}

// while let — loop while pattern matches
let mut stack = vec![1, 2, 3];
while let Some(top) = stack.pop() {
    println!("{}", top);
}

// Option & Result — the most important enums
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}

// The ? operator — concise error propagation
fn read_config() -> Result<String, std::io::Error> {
    let content = std::fs::read_to_string("config.toml")?;
    // Equivalent to:
    // let content = match std::fs::read_to_string("config.toml") {
    //     Ok(c) => c,
    //     Err(e) => return Err(e),
    // };
    Ok(content)
}
```

---

## Tratti e farmaci generici
### Definizione e implementazione dei tratti
```rust
// Define a trait
trait Summary {
    fn summarize(&self) -> String;

    // Default implementation
    fn preview(&self) -> String {
        format!("{}...", &self.summarize()[..20.min(self.summarize().len())])
    }
}

// Implement trait for a type
struct Article {
    title: String,
    content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}: {}", self.title, &self.content[..50])
    }
}

// Trait bounds on functions
fn notify(item: &impl Summary) {
    println!("Breaking: {}", item.summarize());
}

// Equivalent with where clause
fn notify_generic<T>(item: &T)
where
    T: Summary + Clone,
{
    println!("Breaking: {}", item.summarize());
}

// Return impl Trait
fn create_article() -> impl Summary {
    Article {
        title: "News".to_string(),
        content: "Content here".to_string(),
    }
}

// Trait objects (dynamic dispatch)
fn notify_dyn(item: &dyn Summary) {
    println!("Breaking: {}", item.summarize());
}

// Multiple trait bounds
fn display(item: &(impl Summary + std::fmt::Display)) {
    println!("{}", item);
}
```

### Caratteristiche comuni della libreria standard
```rust
// Display — user-facing formatting
use std::fmt;
impl fmt::Display for Article {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} by {}", self.title, self.content)
    }
}

// Debug — developer formatting (#[derive(Debug)])
#[derive(Debug)]
struct Point { x: f64, y: f64 }

// Clone & Copy
#[derive(Clone, Copy)]
struct Color { r: u8, g: u8, b: u8 }

// From / Into — type conversions
impl From<(u8, u8, u8)> for Color {
    fn from((r, g, b): (u8, u8, u8)) -> Self {
        Color { r, g, b }
    }
}
let color: Color = (255, 128, 0).into();

// Iterator
struct Counter { count: usize, max: usize }
impl Iterator for Counter {
    type Item = usize;
    fn next(&mut self) -> Option<Self::Item> {
        if self.count < self.max {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}

// Deref — smart pointer coercion
use std::ops::Deref;
struct MyBox<T>(T);
impl<T> Deref for MyBox<T> {
    type Target = T;
    fn deref(&self) -> &T { &self.0 }
}

// Drop — custom cleanup
impl<T> Drop for MyBox<T> {
    fn drop(&mut self) {
        println!("Dropping MyBox({:?})", self.0);
    }
}
```

---

## Gestione degli errori
### Modelli di risultati e opzioni
```rust
// Comprehensive error handling
use std::fmt;

#[derive(Debug)]
enum AppError {
    NotFound(String),
    ParseError(std::num::ParseIntError),
    IoError(std::io::Error),
    Custom(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Self::NotFound(msg) => write!(f, "Not found: {}", msg),
            Self::ParseError(e) => write!(f, "Parse error: {}", e),
            Self::IoError(e) => write!(f, "IO error: {}", e),
            Self::Custom(msg) => write!(f, "{}", msg),
        }
    }
}

impl std::error::Error for AppError {}

// Automatic conversion with From
impl From<std::io::Error> for AppError {
    fn from(err: std::io::Error) -> Self {
        AppError::IoError(err)
    }
}

impl From<std::num::ParseIntError> for AppError {
    fn from(err: std::num::ParseIntError) -> Self {
        AppError::ParseError(err)
    }
}

// Using the error type
fn load_number(path: &str) -> Result<i32, AppError> {
    let content = std::fs::read_to_string(path)?;  // io::Error → AppError
    let number: i32 = content.trim().parse()?;      // ParseIntError → AppError
    Ok(number)
}

// Combinators for Option/Result
let value: Option<i32> = Some(42);
let doubled = value.map(|x| x * 2);               // Some(84)
let with_default = value.unwrap_or(0);             // 42
let chained = value.and_then(|x| if x > 0 { Some(x) } else { None });

let result: Result<i32, String> = Ok(42);
let doubled = result.map(|x| x * 2);              // Ok(84)
let recovered = result.unwrap_or_else(|_| 0);     // 42
let mapped_err = result.map_err(|e| format!("Error: {}", e));
```

---

## Concorrenza
### Discussioni e passaggio di messaggi
```rust
use std::thread;
use std::sync::{Arc, Mutex, mpsc};
use std::time::Duration;

// Spawn a thread
let handle = thread::spawn(|| {
    for i in 0..5 {
        println!("Thread: {}", i);
        thread::sleep(Duration::from_millis(100));
    }
});
handle.join().unwrap();

// Move closure to transfer ownership
let data = vec![1, 2, 3];
let handle = thread::spawn(move || {
    println!("Thread owns: {:?}", data);
});

// Channels — message passing
let (tx, rx) = mpsc::channel::<String>();

// Multiple producers
let tx1 = tx.clone();
thread::spawn(move || { tx.send("from thread 1".into()).unwrap(); });
thread::spawn(move || { tx1.send("from thread 2".into()).unwrap(); });

for msg in rx {
    println!("Received: {}", msg);
}

// Shared state with Arc<Mutex<T>>
let counter = Arc::new(Mutex::new(0));
let handles: Vec<_> = (0..10).map(|_| {
    let counter = Arc::clone(&counter);
    thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    })
}).collect();

for h in handles { h.join().unwrap(); }
println!("Count: {}", *counter.lock().unwrap());  // 10
```

### Asincrono/Aspetta (Tokio)
```rust
// Async function
async fn fetch_url(url: &str) -> Result<String, reqwest::Error> {
    let response = reqwest::get(url).await?;
    let body = response.text().await?;
    Ok(body)
}

// Concurrent execution with tokio::join!
async fn load_dashboard() -> (User, Vec<Post>) {
    let (user, posts) = tokio::join!(
        fetch_user(1),
        fetch_posts(1),
    );
    (user.unwrap(), posts.unwrap())
}

// Spawn async tasks
async fn process_all(urls: Vec<String>) {
    let handles: Vec<_> = urls.into_iter().map(|url| {
        tokio::spawn(async move {
            fetch_url(&url).await
        })
    }).collect();

    for handle in handles {
        match handle.await.unwrap() {
            Ok(body) => println!("Got {} bytes", body.len()),
            Err(e) => eprintln!("Error: {}", e),
        }
    }
}
```

---

## Funzionalità avanzate
### Macro
```rust
// Declarative macro (macro_rules!)
macro_rules! vec_of_strings {
    ($($x:expr),*) => {
        vec![$($x.to_string()),*]
    };
    ($($x:expr,)*) => {
        vec_of_strings!($($x),*)
    };
}

let names = vec_of_strings!["Alice", "Bob", "Charlie"];

// Custom derive macro (proc-macro, in separate crate)
// #[derive(Serialize, Deserialize)]  // serde
// #[derive(Debug, Clone, PartialEq)] // std

// Attribute-like macro
// #[tokio::main]
// async fn main() { ... }

// Bang macro (function-like proc macro)
// let sql = sql!("SELECT * FROM users WHERE id = {}", user_id);
```

### Ruggine pericolosa
```rust
// Raw pointers
let mut num = 42;
let r1: *const i32 = &num;
let r2: *mut i32 = &mut num;

unsafe {
    *r2 = 100;
    println!("Value: {}", *r1);
}

// Unsafe functions
unsafe fn dangerous() {
    // Can dereference raw pointers, call FFI, etc.
}
unsafe { dangerous(); }

// FFI — calling C functions
extern "C" {
    fn abs(input: i32) -> i32;
}
let x = unsafe { abs(-42) };

// Exporting for FFI
#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Safe abstraction over unsafe code
fn split_at_mut<T>(slice: &mut [T], mid: usize) -> (&mut [T], &mut [T]) {
    let len = slice.len();
    let ptr = slice.as_mut_ptr();
    assert!(mid <= len);
    unsafe {
        (
            std::slice::from_raw_parts_mut(ptr, mid),
            std::slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

### Puntatori intelligenti
```rust
// Box<T> — heap allocation
let boxed = Box::new(42);
println!("{}", *boxed);  // Deref to 42

// Recursive types with Box
enum List {
    Cons(i32, Box<List>),
    Nil,
}

// Rc<T> — reference counting (single-threaded)
use std::rc::Rc;
let a = Rc::new(String::from("shared"));
let b = Rc::clone(&a);    // Reference count = 2
let c = Rc::clone(&a);    // Reference count = 3
println!("Rc count: {}", Rc::strong_count(&a));  // 3

// RefCell<T> — interior mutability (single-threaded)
use std::cell::RefCell;
let data = RefCell::new(vec![1, 2, 3]);
data.borrow_mut().push(4);    // Mutate through RefCell
println!("{:?}", data.borrow());  // [1, 2, 3, 4]

// Combined: Rc<RefCell<T>> — shared mutable state
let shared = Rc::new(RefCell::new(Vec::new()));
let clone1 = Rc::clone(&shared);
let clone2 = Rc::clone(&shared);
clone1.borrow_mut().push(1);
clone2.borrow_mut().push(2);
println!("{:?}", shared.borrow());  // [1, 2]
```

---

## Riepilogo
La sintassi di Rust è costruita su una base di garanzie di sicurezza applicate in fase di compilazione. Il sistema di proprietà, il polimorfismo basato sui tratti, la corrispondenza dei modelli e le astrazioni a costo zero formano un progetto coerente in cui il compilatore è un partner rigoroso ma giusto. Dal flusso di controllo di base alle funzionalità avanzate come macro, codice non sicuro e puntatori intelligenti, ogni costrutto serve all'obiettivo di una programmazione di sistemi sicura ed efficiente. Comprendere l'interazione tra vite, prestiti e sistema di tipi è la chiave per padroneggiare Rust.