---
# Metadata
title: "Cross-Language Comparison — Data Types & Structures"
description: "Side-by-side comparison of data types and structures across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [data-types, data-structures, cross-language, comparison, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# ক্রস-ল্যাঙ্গুয়েজ তুলনা — ডেটা টাইপ এবং স্ট্রাকচার
## আদিম প্রকার
| প্রকার | পাইথন | জাভাস্ক্রিপ্ট | মরিচা | যান | জাভা | গ | সি++ | C# |
|------|---------|------------|------|----|------|---|------|------|
| পূর্ণসংখ্যা | `int`(স্বেচ্ছাচারী) | `number`| `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| ভাসা | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| স্ট্রিং | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| বুলিয়ান | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| চরিত্র | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| শূন্য | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## অ্যারে / তালিকা
```python
# Python: list (dynamic, heterogeneous)
nums = [1, 2, 3]
nums.append(4)
nums[0]  # 1
```

```javascript
// JavaScript: Array (dynamic)
const nums = [1, 2, 3];
nums.push(4);
nums[0];  // 1
```

```rust
// Rust: Vec (dynamic) and arrays (fixed)
let mut nums = vec![1, 2, 3];
nums.push(4);
let fixed: [i32; 3] = [1, 2, 3];  // fixed size
```

```go
// Go: slice (dynamic) and array (fixed)
nums := []int{1, 2, 3}
nums = append(nums, 4)
var fixed [3]int = [3]int{1, 2, 3}  // fixed size
```

```java
// Java: ArrayList (dynamic) and array (fixed)
List<Integer> nums = new ArrayList<>(List.of(1, 2, 3));
nums.add(4);
int[] fixed = {1, 2, 3};  // fixed size
```

```c
// C: arrays (fixed size)
int nums[3] = {1, 2, 3};
// Dynamic: malloc
int *dyn = malloc(3 * sizeof(int));
```

## মানচিত্র / অভিধান / হ্যাশ টেবিল
```python
# Python: dict
person = {"name": "Alice", "age": 30}
person["email"] = "alice@example.com"
```

```javascript
// JavaScript: Object / Map
const person = { name: "Alice", age: 30 };
// Or Map
const map = new Map([["name", "Alice"], ["age", 30]]);
```

```rust
// Rust: HashMap
use std::collections::HashMap;
let mut person = HashMap::new();
person.insert("name", "Alice");
person.insert("age", "30");
```

```go
// Go: map
person := map[string]string{
    "name": "Alice",
    "age":  "30",
}
person["email"] = "alice@example.com"
```

```java
// Java: HashMap
Map<String, String> person = new HashMap<>();
person.put("name", "Alice");
person.put("age", "30");
```

```csharp
// C#: Dictionary
var person = new Dictionary<string, string> {
    ["name"] = "Alice",
    ["age"] = "30"
};
```

```ruby
# Ruby: Hash
person = { "name" => "Alice", "age" => 30 }
person["email"] = "alice@example.com"
```

```swift
// Swift: Dictionary
var person: [String: Any] = ["name": "Alice", "age": 30]
person["email"] = "alice@example.com"
```

```haskell
-- Haskell: Data.Map
import qualified Data.Map as Map
person = Map.fromList [("name", "Alice"), ("age", "30")]
```

```erlang
% Erlang: maps
Person = #{name => "Alice", age => 30},
Person2 = Person#{email => "alice@example.com"}.
```

```elixir
# Elixir: map
person = %{name: "Alice", age: 30}
Map.put(person, :email, "alice@example.com")
```

## সেট
| ভাষা | সিনট্যাক্স |
|------------|---------|
| পাইথন | `s = {1, 2, 3}`|
| জাভাস্ক্রিপ্ট | `const s = new Set([1, 2, 3])`|
| মরিচা | `let s: HashSet<i32> = [1, 2, 3].into()`|
| যান | `s := map[int]bool{1: true, 2: true, 3: true}`(কোন অন্তর্নির্মিত সেট) |
| জাভা | `Set<Integer> s = Set.of(1, 2, 3)`|
| সি++ | `std::set<int> s = {1, 2, 3}`|
| C# | `var s = new HashSet<int> { 1, 2, 3 }`|
| রুবি | `s = Set[1, 2, 3]`|
| সুইফট | `var s: Set<Int> = [1, 2, 3]`|
| কোটলিন | `val s = setOf(1, 2, 3)`|
| স্কালা | `val s = Set(1, 2, 3)`|
| ডার্ট | `var s = {1, 2, 3}`|
| জুলিয়া | `s = Set([1, 2, 3])`|
| আর | `s <- c(1, 2, 3)`(কোন নেটিভ সেট নয়;`%in%`ব্যবহার করুন) |
## কাঠামো / রেকর্ড / ক্লাস
```python
# Python: class or dataclass
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

```rust
// Rust: struct
struct Person {
    name: String,
    age: u32,
}
```

```go
// Go: struct
type Person struct {
    Name string
    Age  int
}
```

```java
// Java: record (Java 14+) or class
record Person(String name, int age) {}

// Traditional class
class Person {
    String name;
    int age;
    Person(String name, int age) { this.name = name; this.age = age; }
}
```

```c
// C: struct
typedef struct {
    char name[50];
    int age;
} Person;
```

```swift
// Swift: struct
struct Person {
    var name: String
    var age: Int
}
```

```kotlin
// Kotlin: data class
data class Person(val name: String, val age: Int)
```

```typescript
// TypeScript: interface or type
interface Person {
    name: string;
    age: number;
}
// Or
type Person = { name: string; age: number };
```

```csharp
// C#: record (C# 9+)
record Person(string Name, int Age);
```

```haskell
-- Haskell: algebraic data type
data Person = Person { name :: String, age :: Int }
```

```scala
// Scala: case class
case class Person(name: String, age: Int)
```

```dart
// Dart: class
class Person {
    final String name;
    final int age;
    Person(this.name, this.age);
}
```

```ruby
# Ruby: Struct or class
Person = Struct.new(:name, :age)
# Or
class Person
    attr_accessor :name, :age
    def initialize(name, age)
        @name = name
        @age = age
    end
end
```

```elixir
# Elixir: struct
defmodule Person do
    defstruct name: "", age: 0
end
%Person{name: "Alice", age: 30}
```

```erlang
% Erlang: record (or map)
-record(person, {name, age}).
#person{name = "Alice", age = 30}.
```

## এনামস
| ভাষা | সিনট্যাক্স |
|------------|---------|
| মরিচা | `enum Color { Red, Green, Blue }`|
| সুইফট | `enum Color { case red, green, blue }`|
| কোটলিন | `enum class Color { RED, GREEN, BLUE }`|
| জাভা | `enum Color { RED, GREEN, BLUE }`|
| টাইপস্ক্রিপ্ট | `enum Color { Red, Green, Blue }`|
| গ | `enum Color { RED, GREEN, BLUE };`|
| সি++ | `enum class Color { Red, Green, Blue };`|
| C# | `enum Color { Red, Green, Blue }`|
| যান | `const ( Red = iota; Green; Blue )`(কোন নেটিভ enum) |
| ডার্ট | `enum Color { red, green, blue }`|
| পিএইচপি | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| স্কালা | `enum Color { case Red, Green, Blue }`(স্ক্যালা 3) |
| পাইথন | `from enum import Enum; class Color(Enum): RED = 1`|
| রুবি | কোন স্থানীয় enum নেই (হিমায়িত ধ্রুবক বা`dry-enum`ব্যবহার করুন) |
## শূন্য নিরাপত্তা
| ভাষা | নাল হ্যান্ডলিং |
|------------|---------------|
| পাইথন | `None`, কোন কম্পাইল-টাইম নাল নিরাপত্তা নেই |
| জাভাস্ক্রিপ্ট | `null`/`undefined`, ঐচ্ছিক চেইনিং`?.`|
| মরিচা | `Option<T>`— কোন নাল! কম্পাইল-টাইম বলবৎ |
| যান |  পয়েন্টার, স্লাইস, মানচিত্র, চ্যানেলের জন্য`nil`|
| জাভা | `null`,`Optional<T>`(জাভা 8+),`@Nullable`|
| গ | `NULL`(`((void*)0)` এর জন্য ম্যাক্রো) |
| সি++ | `nullptr`(C++11),`std::optional<T>`|
| C# | `null`, বাতিলযোগ্য রেফারেন্স প্রকার (C# 8+),`Nullable<T>`|
| সুইফট | `Optional<T>`(`T?`),`if let`,`guard let`|
| কোটলিন | `T?`(শূন্য),`?.`নিরাপদ কল,`?:`এলভিস |
| টাইপস্ক্রিপ্ট | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| হাসকেল | `Maybe a`—`Just x`বা`Nothing`|
| স্কালা | `Option[T]`—`Some(x)`বা`None`|
| ডার্ট | `T?`( বাতিলযোগ্য), নাল নিরাপত্তা (Dart 2.12+) |
| রুবি | `nil`(`false` এবং`nil`ছাড়া সবকিছুই সত্য) |
| এলিক্সির | কোন নাল নেই —`nil`বা প্যাটার্ন ম্যাচ ব্যবহার করুন |
| এরলাং | কোন নাল নেই —`undefined`বা প্যাটার্ন ম্যাচ ব্যবহার করুন |