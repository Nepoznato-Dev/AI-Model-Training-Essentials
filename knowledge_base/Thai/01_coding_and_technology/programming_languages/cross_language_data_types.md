---
# Metadata
title: "Cross-Language Comparison — Data Types & Structures"
description: "Side-by-side comparison of data types and structures across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# การเปรียบเทียบข้ามภาษา - ประเภทข้อมูลและโครงสร้าง
## ประเภทดั้งเดิม
| พิมพ์ | หลาม | จาวาสคริปต์ | สนิม | ไป | ชวา | ซี | ซี++ | ซี# |
|------|--------|------------|-|----|------|---|-----|-----|
| จำนวนเต็ม | `int`(โดยพลการ) | `number`| `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| ลอย | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| สตริง | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| บูลีน | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| ตัวละคร | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| โมฆะ | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## อาร์เรย์ / รายการ
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

## แผนที่ / พจนานุกรม / ตารางแฮช
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

## ชุด
| ภาษา | ไวยากรณ์ |
|---------||--------|
| หลาม | `s = {1, 2, 3}`|
| จาวาสคริปต์ | `const s = new Set([1, 2, 3])`|
| สนิม | `let s: HashSet<i32> = [1, 2, 3].into()`|
| ไป | `s := map[int]bool{1: true, 2: true, 3: true}`(ไม่มี Set ในตัว) |
| ชวา | `Set<Integer> s = Set.of(1, 2, 3)`|
| ซี++ | `std::set<int> s = {1, 2, 3}`|
| ซี# | `var s = new HashSet<int> { 1, 2, 3 }`|
| ทับทิม | `s = Set[1, 2, 3]`|
| สวิฟท์ | `var s: Set<Int> = [1, 2, 3]`|
| คอตลิน | `val s = setOf(1, 2, 3)`|
| สกาล่า | `val s = Set(1, 2, 3)`|
| โผ | `var s = {1, 2, 3}`|
| จูเลีย | `s = Set([1, 2, 3])`|
| อาร์ | `s <- c(1, 2, 3)`(ไม่มีชุดเนทิฟ ใช้`%in%`) |
## โครงสร้าง / บันทึก / คลาส
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

## อีนัมส์
| ภาษา | ไวยากรณ์ |
|---------||--------|
| สนิม | `enum Color { Red, Green, Blue }`|
| สวิฟท์ | `enum Color { case red, green, blue }`|
| คอตลิน | `enum class Color { RED, GREEN, BLUE }`|
| ชวา | `enum Color { RED, GREEN, BLUE }`|
| ประเภทสคริปต์ | `enum Color { Red, Green, Blue }`|
| ซี | `enum Color { RED, GREEN, BLUE };`|
| ซี++ | `enum class Color { Red, Green, Blue };`|
| ซี# | `enum Color { Red, Green, Blue }`|
| ไป | `const ( Red = iota; Green; Blue )`(ไม่มี enum ดั้งเดิม) |
| โผ | `enum Color { red, green, blue }`|
| PHP | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| สกาล่า | `enum Color { case Red, Green, Blue }`(สกาล่า 3) |
| หลาม | `from enum import Enum; class Color(Enum): RED = 1`|
| ทับทิม | ไม่มี enum ดั้งเดิม (ใช้ค่าคงที่แช่แข็งหรือ`dry-enum`) |
## ความปลอดภัยเป็นศูนย์
| ภาษา | การจัดการค่าว่าง |
|----------|--------------|
| หลาม | `None`ไม่มีความปลอดภัยแบบ null เวลาคอมไพล์ |
| จาวาสคริปต์ | `null`/`undefined`, การต่อสายโซ่เสริม`?.`|
| สนิม | `Option<T>`— ไม่มีค่าว่าง! บังคับใช้เวลาคอมไพล์ |
| ไป | `nil`สำหรับพอยน์เตอร์ สไลซ์ แผนที่ ช่อง |
| ชวา | `null`,`Optional<T>`(จาวา 8+),`@Nullable`|
| ซี | `NULL`(มาโครสำหรับ`((void*)0)`) |
| ซี++ | `nullptr`(C++11),`std::optional<T>`|
| ซี# | `null`, ประเภทการอ้างอิงที่เป็นโมฆะ (C# 8+),`Nullable<T>`|
| สวิฟท์ | `Optional<T>`(`T?`),`if let`,`guard let`|
| คอตลิน | `T?`(เป็นโมฆะ),`?.`โทรปลอดภัย,`?:`Elvis |
| ประเภทสคริปต์ | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| ฮาสเคล | `Maybe a`—`Just x`หรือ`Nothing`|
| สกาล่า | `Option[T]`—`Some(x)`หรือ`None`|
| โผ | `T?`(เป็นโมฆะ), ความปลอดภัยเป็นโมฆะ (Dart 2.12+) |
| ทับทิม | `nil`(ทุกอย่างเป็นความจริง ยกเว้น`false`และ`nil`) |
| ยาอายุวัฒนะ | ไม่มีค่าว่าง — ใช้`nil`หรือการจับคู่รูปแบบ |
| เออร์ลัง | ไม่มีค่าว่าง — ใช้`undefined`หรือการจับคู่รูปแบบ |