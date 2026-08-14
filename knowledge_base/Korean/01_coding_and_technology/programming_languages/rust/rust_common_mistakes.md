---
# Metadata
title: "Rust — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Rust that catch even experienced developers, with explanations and corrections."
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
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [rust, common-mistakes, anti-patterns, pitfalls, best-practices, ownership, borrowing, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Rust — 일반적인 실수와 안티 패턴
이 문서는 Rust에서 가장 흔히 발생하는 실수, 함정, 안티패턴을 나열합니다. 각 항목은 잘못된 접근 방식을 보여주고, 실패 이유를 설명하며, 올바른 솔루션을 제공합니다. Rust의 컴파일러는 많은 오류를 포착하지만 이러한 패턴을 이해하면 학습 곡선이 가속화됩니다.
---

## 1. Borrow Checker와의 싸움 - 불필요한 복제
```rust
// ❌ WRONG — cloning to appease the compiler
fn process(data: Vec<i32>) {
    let cloned = data.clone();  // expensive copy
    println!("{:?}", cloned);
    println!("{:?}", data);
}

// ✅ CORRECT — borrow instead
fn process(data: &[i32]) {
    println!("{:?}", data);
    // use data by reference throughout
}

// ✅ CORRECT — use references
fn process(data: &Vec<i32>) {
    let view = data;  // just a reference, no copy
    println!("{:?}", view);
    println!("{:?}", data);
}
```

---

## 2. 문자열 대 &str 혼란
```rust
// ❌ WRONG — always allocating when a reference suffices
fn greet(name: String) -> String {
    format!("Hello, {}!", name)
}

// ✅ CORRECT — accept &str, more flexible
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}
// Works with String, &str, string literals, etc.
```

---

## 3. 프로덕션에서 `unwrap()`로 결과 무시하기
```rust
// ❌ WRONG — unwrap panics on error
fn read_config(path: &str) -> String {
    std::fs::read_to_string(path).unwrap()  // panic if file missing!
}

// ✅ CORRECT — propagate errors
fn read_config(path: &str) -> Result<String, std::io::Error> {
    std::fs::read_to_string(path)
}

// ✅ CORRECT — provide defaults
fn read_config(path: &str) -> String {
    std::fs::read_to_string(path)
        .unwrap_or_else(|_| String::from("default_config"))
}
```

---

## 4. 평생 주석 실수
```rust
// ❌ WRONG — compiler can't infer which reference to use
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() { x } else { y }
}
// Error: missing lifetime specifier

// ✅ CORRECT — explicit lifetime annotations
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

---

## 5. 안티 패턴:`Rc`/ `RefCell`를 어디서나 사용하기
```rust
// ❌ WRONG — reaching for interior mutability too quickly
use std::rc::Rc;
use std::cell::RefCell;

struct App {
    data: Rc<RefCell<Vec<String>>>,
}

// ✅ CORRECT — use ownership and borrowing first
struct App {
    data: Vec<String>,
}

// ✅ CORRECT — use &mut for mutation
fn update(app: &mut App) {
    app.data.push("new item".to_string());
}
```

---

## 6. 이동 의미를 이해하지 못함
```rust
// ❌ WRONG — expecting value to still be usable after move
let v1 = vec![1, 2, 3];
let v2 = v1;  // v1 is moved
println!("{:?}", v1);  // Error: value used after move

// ✅ CORRECT — clone if you need both
let v1 = vec![1, 2, 3];
let v2 = v1.clone();
println!("{:?} {:?}", v1, v2);

// ✅ CORRECT — borrow if you just need to read
let v1 = vec![1, 2, 3];
let v2 = &v1;  // borrow, don't move
println!("{:?} {:?}", v1, v2);
```

---

## 7. 안티 패턴: 과도한`to_string()`/ `to_owned()`
```rust
// ❌ WRONG — allocating strings unnecessarily
let key = "user_id".to_string();
let map: HashMap<String, i32> = HashMap::new();
map.insert(key, 42);

// ✅ CORRECT — use &str keys with HashMap
let mut map: HashMap<&str, i32> = HashMap::new();
map.insert("user_id", 42);

// ✅ CORRECT — use Cow for flexible ownership
use std::borrow::Cow;
fn process(input: Cow<str>) {
    // works with both owned and borrowed strings
}
```

---

## 8. 뮤텍스 중독
```rust
// ❌ WRONG — not handling Mutex poison
let mutex = Mutex::new(0);
let guard = mutex.lock().unwrap();  // panics if thread panicked

// ✅ CORRECT — handle poison gracefully
match mutex.lock() {
    Ok(guard) => { /* use guard */ },
    Err(poisoned) => {
        let guard = poisoned.into_inner();
        // recover state from poisoned mutex
    }
}
```

---

## 9. 반복자 무효화 — 불필요하게 수집
```rust
// ❌ WRONG — collecting into Vec when not needed
let result: Vec<i32> = (0..1000).map(|x| x * 2).collect();
let sum = result.iter().sum::<i32>();

// ✅ CORRECT — chain iterators lazily
let sum: i32 = (0..1000).map(|x| x * 2).sum();
```

---

## 10. 안티 패턴: 메소드가 없는 열거형
```rust
// ❌ WRONG — treating enums like C constants
enum Status {
    Active,
    Inactive,
    Pending,
}
// Status logic scattered across the codebase

// ✅ CORRECT — attach behavior to enums
impl Status {
    fn can_transition_to(&self, target: &Status) -> bool {
        matches!((self, target),
            (Status::Active, Status::Inactive) |
            (Status::Inactive, Status::Active) |
            (Status::Pending, Status::Active)
        )
    }

    fn label(&self) -> &'static str {
        match self {
            Status::Active => "Active",
            Status::Inactive => "Inactive",
            Status::Pending => "Pending Review",
        }
    }
}
```

---

## 11. 일반적인 특성에 `#[derive]`를 사용하지 않음
```rust
// ❌ WRONG — manual trait implementations
struct Point { x: f64, y: f64 }
impl PartialEq for Point {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}
impl Clone for Point {
    fn clone(&self) -> Self {
        Point { x: self.x, y: self.y }
    }
}

// ✅ CORRECT — use derive macros
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct Point { x: f64, y: f64 }
```

---

## 12. 문서가 없으면 안전하지 않은 코드
```rust
// ❌ WRONG — unsafe block with no safety comment
unsafe {
    let ptr = &x as *const i32;
    do_something(ptr);
}

// ✅ CORRECT — document safety invariants
// SAFETY: ptr is valid because x is alive for the entire scope
// and we don't create any mutable references to x.
unsafe {
    let ptr = &x as *const i32;
    do_something(ptr);
}
```

---

## 요약
Rust의 컴파일러는 엄격하지만 공정합니다. 대부분의 오류는 메모리 안전에 대해 알려줍니다. 가장 큰 실수는 컴파일러 오류가 아니라 안티 패턴입니다. 빌림 검사기를 달래기 위한 불필요한 복제, 프로덕션에서`unwrap()`사용, 소유권을 시도하기 전에 `Rc<RefCell<T>>`에 도달, 참조가 충분할 때 문자열 할당 등입니다. Rustacean의 사고방식은: 컴파일러가 비용이 들지 않는 추상화를 향해 여러분을 안내하도록 하는 것입니다. 필요한 경우에만 복제하고, `?`를 사용하여 오류를 전파하고, `String`보다 `&str`를 선호하고, 모든`unsafe`블록을 문서화하세요.