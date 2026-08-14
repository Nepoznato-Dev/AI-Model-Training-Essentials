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

# کراس لینگویج کا موازنہ — ڈیٹا کی اقسام اور ڈھانچے
## قدیم اقسام
| قسم | ازگر | جاوا اسکرپٹ | مورچا | جاؤ | جاوا | سی | C++ | C# |
|------|---------|------------|------|----|------|---|------|------|
| عدد | `int`(من مانی) | `number`| `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| فلوٹ | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| سٹرنگ | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| بولین | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| کردار | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| کالعدم | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## صفیں / فہرستیں۔
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

## نقشے / لغتیں / ہیش ٹیبلز
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

## سیٹ
| زبان | نحو |
|------------|---------|
| ازگر | `s = {1, 2, 3}`|
| جاوا اسکرپٹ | `const s = new Set([1, 2, 3])`|
| مورچا | `let s: HashSet<i32> = [1, 2, 3].into()`|
| جاؤ | `s := map[int]bool{1: true, 2: true, 3: true}`(کوئی بلٹ ان سیٹ نہیں) |
| جاوا | `Set<Integer> s = Set.of(1, 2, 3)`|
| C++ | `std::set<int> s = {1, 2, 3}`|
| C# | `var s = new HashSet<int> { 1, 2, 3 }`|
| روبی | `s = Set[1, 2, 3]`|
| سوئفٹ | `var s: Set<Int> = [1, 2, 3]`|
| کوٹلن | `val s = setOf(1, 2, 3)`|
| سکالا | `val s = Set(1, 2, 3)`|
| ڈارٹ | `var s = {1, 2, 3}`|
| جولیا | `s = Set([1, 2, 3])`|
| آر | `s <- c(1, 2, 3)`(کوئی مقامی سیٹ نہیں؛`%in%`استعمال کریں) |
## ڈھانچے / ریکارڈز / کلاسز
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

## انومس
| زبان | نحو |
|------------|---------|
| مورچا | `enum Color { Red, Green, Blue }`|
| سوئفٹ | `enum Color { case red, green, blue }`|
| کوٹلن | `enum class Color { RED, GREEN, BLUE }`|
| جاوا | `enum Color { RED, GREEN, BLUE }`|
| TypeScript | `enum Color { Red, Green, Blue }`|
| سی | `enum Color { RED, GREEN, BLUE };`|
| C++ | `enum class Color { Red, Green, Blue };`|
| C# | `enum Color { Red, Green, Blue }`|
| جاؤ | `const ( Red = iota; Green; Blue )`(کوئی مقامی enum نہیں) |
| ڈارٹ | `enum Color { red, green, blue }`|
| پی ایچ پی | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| سکالا | `enum Color { case Red, Green, Blue }`(Scala 3) |
| ازگر | `from enum import Enum; class Color(Enum): RED = 1`|
| روبی | کوئی مقامی enum نہیں (منجمد مستقل یا`dry-enum`استعمال کریں) |
## کالعدم حفاظت
| زبان | null ہینڈلنگ |
|------------|---------------|
| ازگر |  `None`، کوئی کمپائل ٹائم null سیفٹی نہیں |
| جاوا اسکرپٹ | `null`/`undefined`, اختیاری سلسلہ`?.`|
| مورچا | `Option<T>`— کوئی کالعدم نہیں! مرتب وقت نافذ |
| جاؤ | `nil`پوائنٹرز، سلائسس، نقشے، چینلز کے لیے |
| جاوا | `null`,`Optional<T>`(Java 8+),`@Nullable`|
| سی | `NULL`( میکرو برائے`((void*)0)`) |
| C++ | `nullptr`(C++11),`std::optional<T>`|
| C# | `null`, nullable reference type (C# 8+),`Nullable<T>`|
| سوئفٹ | `Optional<T>`(`T?`) ,`if let`,`guard let`|
| کوٹلن | `T?`(منسوخ)،`?.`محفوظ کال،`?:`ایلوس |
| TypeScript | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| ہاسکل | `Maybe a`—`Just x`یا`Nothing`|
| سکالا | `Option[T]`—`Some(x)`یا`None`|
| ڈارٹ | `T?`(منسوخ)، null حفاظت (Dart 2.12+) |
| روبی | `nil`(ہر چیز سچی ہے سوائے`false`اور`nil`) |
| ایلکسیر | کوئی کالعدم نہیں —`nil`یا پیٹرن میچ استعمال کریں۔
| ایرلنگ | کوئی کالعدم نہیں —`undefined`یا پیٹرن میچ استعمال کریں۔