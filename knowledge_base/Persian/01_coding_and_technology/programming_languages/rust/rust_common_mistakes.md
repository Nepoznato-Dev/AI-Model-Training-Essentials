---
# Metadata
title: "Rust — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Rust that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
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

# زنگ زدگی - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها را در Rust فهرست می کند. هر ورودی رویکرد نادرست را نشان می دهد، توضیح می دهد که چرا شکست می خورد، و راه حل صحیح را ارائه می دهد. کامپایلر Rust خطاهای زیادی پیدا می کند، اما درک این الگوها منحنی یادگیری شما را تسریع می کند.
---

## 1. مبارزه با جستجوگر قرض - شبیه سازی غیر ضروری
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

## 2. رشته در مقابل سردرگمی &str
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

## 3. نادیده گرفتن نتایج با`unwrap()`در تولید
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

## 4. اشتباهات حاشیه نویسی مادام العمر
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

## 5. ضد الگو: استفاده از`Rc`/`RefCell`در همه جا
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

## 6. عدم درک معناشناسی حرکت
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

## 7. ضد الگو:`to_string()`بیش از حد / `to_owned()`
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

## 8. مسمومیت با موتکس
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

## 9. Iterator Invalidation - جمع آوری غیر ضروری
```rust
// ❌ WRONG — collecting into Vec when not needed
let result: Vec<i32> = (0..1000).map(|x| x * 2).collect();
let sum = result.iter().sum::<i32>();

// ✅ CORRECT — chain iterators lazily
let sum: i32 = (0..1000).map(|x| x * 2).sum();
```

---

## 10. Anti-Pattern: Enum Without Methods
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

## 11. عدم استفاده از`#[derive]`برای صفات مشترک
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

## 12. کد ناامن بدون مستندات
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

## خلاصه
کامپایلر Rust سختگیرانه اما منصفانه است - بیشتر خطاها چیزی در مورد ایمنی حافظه به شما می آموزند. بزرگ‌ترین اشتباهات خطاهای کامپایلر نیستند، بلکه ضد الگوها هستند: شبیه‌سازی غیرضروری برای دلجویی از وام‌گیر، استفاده از`unwrap()`در تولید، دستیابی به`Rc<RefCell<T>>`قبل از تلاش برای مالکیت، و تخصیص رشته‌ها در صورت کافی بودن مراجع. طرز فکر Rustacean این است: اجازه دهید کامپایلر شما را به سمت انتزاعات بدون هزینه راهنمایی کند. فقط در صورت لزوم کلون کنید، خطاها را با`?`منتشر کنید،`&str`را به`String`ترجیح دهید، و هر بلوک`unsafe`را مستند کنید.