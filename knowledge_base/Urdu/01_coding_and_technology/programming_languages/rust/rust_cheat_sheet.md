<!--
---
# Metadata
title: "Rust — Cheat Sheet"
description: "Quick-reference cheat sheet for Rust syntax, ownership, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [rust, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# زنگ - دھوکہ شیٹ
## بنیادی باتیں
```rust
// Variables
let x = 42;              // immutable
let mut y = 10;          // mutable
const PI: f64 = 3.14159; // compile-time constant
static MAX: u32 = 1000;  // global

// Types
let i: i32 = -42;
let u: u64 = 100;
let f: f64 = 3.14;
let b: bool = true;
let c: char = 'A';
let s: &str = "hello";
let owned: String = String::from("hello");

// Type conversion
let n: i32 = 42;
let big: i64 = n as i64;
let parsed: i32 = "42".parse().unwrap();

// String formatting
format!("Hello, {}!", name);
format!("{:.2}", 3.14159);  // "3.14"
format!("{:?}", value);      // debug format
println!("{name} is {age}"); // named args
```

## ملکیت اور قرض لینا
```rust
// Move semantics
let s1 = String::from("hello");
let s2 = s1;  // s1 is moved, no longer valid

// Clone
let s2 = s1.clone();  // deep copy

// Borrowing
fn print_len(s: &String) { println!("{}", s.len()); }
let s = String::from("hello");
print_len(&s);  // borrow — s still valid

// Mutable borrow
fn append_excl(s: &mut String) { s.push('!'); }
let mut s = String::from("hello");
append_excl(&mut s);

// Rules: one mutable XOR many immutable borrows
```

## ڈیٹا سٹرکچرز
```rust
// Vec
let mut v = vec![1, 2, 3];
v.push(4);
v.iter().map(|x| x * 2).collect::<Vec<_>>();
&v[1..3]  // slice

// HashMap
use std::collections::HashMap;
let mut map = HashMap::new();
map.insert("key", 42);
map.entry("key").or_insert(0);
map.get("key");  // Option<&V>

// Tuple
let t: (i32, f64, &str) = (1, 3.14, "hello");
let (a, b, c) = t;

// Struct
struct Point { x: f64, y: f64 }
let p = Point { x: 1.0, y: 2.0 };
let Point { x, y } = p;  // destructure
```

## اینمز اور پیٹرن میچنگ
```rust
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
    Point,
}

match shape {
    Shape::Circle(r) => println!("Circle r={r}"),
    Shape::Rectangle(w, h) => println!("{w}x{h}"),
    Shape::Point => println!("Point"),
}

// Option & Result
let val: Option<i32> = Some(42);
let doubled = val.map(|x| x * 2);
let unwrapped = val.unwrap_or(0);

let res: Result<i32, String> = Ok(42);
res.unwrap_or_else(|e| { println!("{e}"); 0 });
```

## کنٹرول فلو
```rust
if condition { ... } else if other { ... } else { ... }

let result = if x > 0 { "positive" } else { "non-positive" };

// Loops
for item in &collection { ... }
for i in 0..10 { ... }          // 0..9
for i in 0..=10 { ... }         // 0..10
for (i, val) in iter.enumerate() { ... }

while condition { ... }
loop { ... }  // infinite
loop { ... break 42; }  // loop with value

// Iterator adapters
(0..10).filter(|x| x % 2 == 0).map(|x| x * x).collect::<Vec<_>>();
```

## افعال اور بندش
```rust
fn add(a: i32, b: i32) -> i32 { a + b }  // last expr = return

// Closure
let double = |x: i32| -> i32 { x * 2 };
let square = |x| x * x;  // inferred types

// Higher-order
fn apply(f: impl Fn(i32) -> i32, x: i32) -> i32 { f(x) }

// Returning closures
fn make_adder(n: i32) -> impl Fn(i32) -> i32 {
    move |x| x + n  // move captures by value
}
```

## خصلتیں اور عمومیات
```rust
trait Greet {
    fn greet(&self) -> String;
}

impl Greet for User {
    fn greet(&self) -> String {
        format!("Hi, I'm {}", self.name)
    }
}

// Generic function
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    list.iter().max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap()
}

// Trait bounds
fn process<T: Display + Clone>(item: T) { ... }
fn process<T>(item: T) where T: Display + Clone { ... }
```

## ہینڈلنگ کی خرابی۔
```rust
// Result
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 { return Err("Division by zero".into()); }
    Ok(a / b)
}

// ? operator
fn read_file() -> Result<String, std::io::Error> {
    let mut s = String::new();
    std::fs::File::open("data.txt")?.read_to_string(&mut s)?;
    Ok(s)
}

// Panic (unrecoverable)
panic!("critical error: {}", msg);
```

## زندگی بھر
```rust
// Named lifetime
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Struct with reference
struct Config<'a> {
    name: &'a str,
}
```
