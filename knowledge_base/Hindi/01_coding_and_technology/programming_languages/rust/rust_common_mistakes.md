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
# जंग - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ रस्ट में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है। प्रत्येक प्रविष्टि गलत दृष्टिकोण दिखाती है, बताती है कि यह विफल क्यों होता है, और सही समाधान प्रदान करती है। रस्ट का कंपाइलर कई त्रुटियां पकड़ता है, लेकिन इन पैटर्न को समझने से आपके सीखने की गति तेज हो जाएगी।
---

## 1. उधार चेक करने वाले से लड़ना - अनावश्यक क्लोनिंग
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

## 2. स्ट्रिंग बनाम &str कन्फ्यूजन
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

## 3. उत्पादन में`unwrap()`के साथ परिणामों की अनदेखी करना
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

## 4. लाइफटाइम एनोटेशन गलतियाँ
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

## 5. एंटी-पैटर्न: हर जगह`Rc`/`RefCell`का उपयोग करना
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

## 6. चाल शब्दार्थ को न समझना
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

## 7. एंटी-पैटर्न: अत्यधिक`to_string()`/ `to_owned()`
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

## 8. म्यूटेक्स विषाक्तता
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

## 9. इटरेटर अमान्यकरण - अनावश्यक रूप से संग्रह करना
```rust
// ❌ WRONG — collecting into Vec when not needed
let result: Vec<i32> = (0..1000).map(|x| x * 2).collect();
let sum = result.iter().sum::<i32>();

// ✅ CORRECT — chain iterators lazily
let sum: i32 = (0..1000).map(|x| x * 2).sum();
```

---

## 10. एंटी-पैटर्न: एनम विदाउट मेथड्स
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

## 11. सामान्य लक्षणों के लिए`#[derive]`का उपयोग नहीं करना
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

## 12. दस्तावेज़ीकरण के बिना असुरक्षित कोड
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

## सारांश
रस्ट का कंपाइलर सख्त लेकिन निष्पक्ष है - अधिकांश त्रुटियाँ आपको मेमोरी सुरक्षा के बारे में कुछ न कुछ सिखाती हैं। सबसे बड़ी गलतियाँ कंपाइलर त्रुटियाँ नहीं बल्कि एंटी-पैटर्न हैं: उधार लेने वाले चेकर को खुश करने के लिए अनावश्यक क्लोनिंग, उत्पादन में`unwrap()`का उपयोग करना, स्वामित्व की कोशिश करने से पहले`Rc<RefCell<T>>`तक पहुंचना, और संदर्भ पर्याप्त होने पर स्ट्रिंग आवंटित करना। रुस्टेशियन मानसिकता यह है: संकलक को आपको शून्य-लागत अमूर्तता की ओर मार्गदर्शन करने दें। केवल आवश्यक होने पर ही क्लोन करें,`?`के साथ त्रुटियों का प्रसार करें,`String`की तुलना में`&str`को प्राथमिकता दें, और प्रत्येक`unsafe`ब्लॉक का दस्तावेजीकरण करें।