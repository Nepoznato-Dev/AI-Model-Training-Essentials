<!--
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

-->
# Rust — 常见错误和反模式
本文档列出了 Rust 中最常见的错误、陷阱和反模式。每个条目都会显示错误的方法，解释其失败的原因，并提供正确的解决方案。 Rust 的编译器会捕获许多错误，但理解这些模式将加快您的学习曲线。
---

## 1. 对抗借用检查器——不必要的克隆
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

## 2. String 与 &str 的混淆
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

## 3. 在生产中忽略`unwrap()`的结果
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

## 4. 终生注释错误
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

## 5. 反模式：到处使用`Rc`/ `RefCell`
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

## 6. 不理解移动语义
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

## 7. 反模式：过多的`to_string()`/ `to_owned()`
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

## 8.互斥体中毒
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

## 9. 迭代器失效——不必要的收集
```rust
// ❌ WRONG — collecting into Vec when not needed
let result: Vec<i32> = (0..1000).map(|x| x * 2).collect();
let sum = result.iter().sum::<i32>();

// ✅ CORRECT — chain iterators lazily
let sum: i32 = (0..1000).map(|x| x * 2).sum();
```

---

## 10. 反模式：没有方法的枚举
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

## 11. 不使用`#[derive]`来表示常见特征
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

## 12. 没有文档的不安全代码
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

＃＃ 概括
Rust 的编译器严格但公平——大多数错误都会教你一些关于内存安全的知识。最大的错误不是编译器错误，而是反模式：不必要的克隆来安抚借用检查器，在生产中使用 `unwrap()`，在尝试所有权之前到达 `Rc<RefCell<T>>`，以及在引用足够时分配字符串。 Rustacean 的心态是：让编译器引导您实现零成本抽象。仅在必要时进行克隆，使用`?`传播错误，更喜欢`&str`而不是`String`，并记录每个`unsafe`块。