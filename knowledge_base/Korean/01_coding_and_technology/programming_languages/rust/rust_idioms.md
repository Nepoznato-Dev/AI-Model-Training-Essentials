---
# Metadata
title: "Rust — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, safe Rust code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [rust, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Rust — 관용적 패턴 및 모범 사례
이 가이드는 깨끗하고 안전한 Rust 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 소유권 및 차용
```rust
// ✅ Prefer borrowing over ownership
fn print_length(s: &str) -> usize {  // &str, not String
    s.len()
}

// ✅ Return owned types, accept borrowed
fn create_greeting(name: &str) -> String {
    format!("Hello, {}!", name)
}

// ✅ Use &mut only when mutation is needed
fn sort_in_place(items: &mut [i32]) {
    items.sort();
}

// ✅ Clone only when necessary
let owned = borrowed.to_owned();
let string = borrowed.to_string();
```

---

## 오류 처리
```rust
// ✅ Use Result, never panic in library code
fn read_config(path: &str) -> Result<Config, ConfigError> {
    let content = std::fs::read_to_string(path)?;
    let config: Config = toml::from_str(&content)?;
    Ok(config)
}

// ✅ Custom error types with thiserror
use thiserror::Error;

#[derive(Error, Debug)]
enum AppError {
    #[error("database error: {0}")]
    Database(#[from] sqlx::Error),
    #[error("not found: {0}")]
    NotFound(String),
    #[error("validation: {field} - {message}")]
    Validation { field: String, message: String },
}

// ✅ Use ? operator for propagation
fn process() -> Result<(), AppError> {
    let user = find_user(1)?;
    let orders = get_orders(user.id)?;
    Ok(())
}

// ✅ expect() with meaningful messages (not unwrap)
let value = result.expect("database connection must succeed at startup");

// ✅ Use Option for absence
fn find_user(id: i64) -> Option<User> { ... }
```

---

## 열거형 패턴
```rust
// ✅ Enums with methods
enum Payment {
    Cash(f64),
    Card { number: String, expiry: String },
    Digital(String),
}

impl Payment {
    fn display(&self) -> String {
        match self {
            Payment::Cash(amount) => format!("Cash: ${:.2}", amount),
            Payment::Card { number, .. } => format!("Card: ****{}", &number[^4..]),
            Payment::Digital(provider) => format!("Digital: {}", provider),
        }
    }
}

// ✅ State machine with enums
enum Connection {
    Disconnected,
    Connecting { host: String },
    Connected { session: Session },
}

impl Connection {
    fn handle(self) -> Connection {
        match self {
            Connection::Disconnected => Connection::Connecting { host: "default".into() },
            Connection::Connecting { host } => { /* ... */ Connection::Connected { session: s } },
            Connection::Connected { session } => self,
        }
    }
}
```

---

## 특성 및 일반
```rust
// ✅ Use traits for abstraction
trait Repository<T> {
    fn find(&self, id: i64) -> Result<Option<T>, Error>;
    fn save(&self, entity: &T) -> Result<(), Error>;
}

// ✅ Trait bounds
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut max = &list[0];
    for item in &list[1..] {
        if item > max { max = item; }
    }
    max
}

// ✅ Derive common traits
#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
struct User {
    id: i64,
    name: String,
}

// ✅ impl Trait for return types
fn create_iterator() -> impl Iterator<Item = i32> {
    (0..10).filter(|x| x % 2 == 0)
}

// ✅ Generic with where clause
fn process<T>(item: T) -> String
where
    T: Display + Clone + Send + 'static,
{
    format!("{}", item)
}
```

---

## 반복자 패턴
```rust
// ✅ Chain iterator methods
let result: Vec<String> = users
    .iter()
    .filter(|u| u.active)
    .map(|u| u.name.to_uppercase())
    .collect();

// ✅ fold for accumulation
let total: i64 = items.iter().map(|i| i.price).sum();
let count = items.iter().filter(|i| i.active).count();

// ✅ find, any, all
let user = users.iter().find(|u| u.id == target_id);
let has_admins = users.iter().any(|u| u.role == Role::Admin);
let all_active = users.iter().all(|u| u.active);

// ✅ zip for parallel iteration
let pairs: Vec<_> = names.iter().zip(scores.iter()).collect();

// ✅ enumerate
for (i, item) in items.iter().enumerate() {
    println!("{}: {}", i, item);
}

// ✅ flat_map for nested
let all_tags: Vec<_> = users.iter().flat_map(|u| u.tags.iter()).collect();
```

---

## 스마트 포인터
```rust
// ✅ Box for heap allocation / recursive types
enum List {
    Cons(i32, Box<List>),
    Nil,
}

// ✅ Rc/Arc for shared ownership
use std::sync::Arc;
let shared = Arc::new(Data::new());
let clone1 = Arc::clone(&shared);

// ✅ RefCell for interior mutability (single-threaded)
use std::cell::RefCell;
let data = RefCell::new(Vec::new());
data.borrow_mut().push(42);

// ✅ Mutex for thread-safe interior mutability
use std::sync::Mutex;
let counter = Arc::new(Mutex::new(0));
```

---

## 수명
```rust
// ✅ Let the compiler infer when possible
fn first_word(s: &str) -> &str {
    s.split_whitespace().next().unwrap_or("")
}

// ✅ Explicit lifetimes only when needed
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// ✅ Lifetime on structs
struct Parser<'input> {
    input: &'input str,
    position: usize,
}
```

---

## 모듈 구성
```rust
// ✅ lib.rs structure
pub mod models;
pub mod services;
pub mod errors;
pub mod utils;

// ✅ Use pub(crate) for internal visibility
pub(crate) fn internal_helper() { }

// ✅ Re-exports for clean API
pub use crate::errors::AppError;
pub use crate::services::UserService;

// ✅ Pre-commitment: use rustfmt and clippy
// cargo fmt
// cargo clippy -- -D warnings
```

---

## 동시성
```rust
// ✅ Scoped threads (no Arc needed for stack data)
std::thread::scope(|s| {
    s.spawn(|| println!("from thread 1"));
    s.spawn(|| println!("from thread 2"));
});

// ✅ Tokio async
#[tokio::main]
async fn main() {
    let (tx, mut rx) = mpsc::channel(32);
    
    tokio::spawn(async move {
        tx.send("hello").await.unwrap();
    });
    
    let msg = rx.recv().await.unwrap();
}

// ✅ Join multiple futures
let (users, posts) = tokio::join!(fetch_users(), fetch_posts());
```

---

## 요약
Rust 관용구는 소유권과 차용, 오류 처리를 위한`Result`/ `Option`, 메서드가 포함된 열거형, 추상화를 위한 특성, 반복자 체이닝, 공유 상태를 위한 스마트 포인터 및 비용이 들지 않는 추상화를 강조합니다. 서식 지정은 `rustfmt`, 린팅은 `clippy`, Rust API 지침을 따르세요. Rust 커뮤니티는 안전성, 성능, 정확성을 중요하게 생각합니다. "컴파일하면 작동합니다." 함수 인수에서는 `String`보다 `&str`를 선호하고, 오류 전파에는 `?`를 사용하고, `#[derive(Debug, Clone, ...)]`를 사용하여 공통 특성을 도출합니다.