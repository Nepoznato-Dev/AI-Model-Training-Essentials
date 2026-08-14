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
# المقارنة بين اللغات – أنواع البيانات وبنيتها
## الأنواع البدائية
| اكتب | بايثون | جافا سكريبت | الصدأ | اذهب | جافا | ج | سي++ | ج # |
|------|--------|-----------|----|------|---|-----|-----|
| عدد صحيح | `int`(تعسفي) | `number`| `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| تعويم | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| سلسلة | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| منطقية | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| حرف | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| فارغة | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## المصفوفات/القوائم
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

## الخرائط / القواميس / جداول التجزئة
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

## مجموعات
| اللغة | بناء الجملة |
|----------|--------|
| بايثون | `s = {1, 2, 3}`|
| جافا سكريبت | `const s = new Set([1, 2, 3])`|
| الصدأ | `let s: HashSet<i32> = [1, 2, 3].into()`|
| اذهب | `s := map[int]bool{1: true, 2: true, 3: true}`(بدون مجموعة مدمجة) |
| جافا | `Set<Integer> s = Set.of(1, 2, 3)`|
| سي++ | `std::set<int> s = {1, 2, 3}`|
| ج # | `var s = new HashSet<int> { 1, 2, 3 }`|
| روبي | `s = Set[1, 2, 3]`|
| سويفت | `var s: Set<Int> = [1, 2, 3]`|
| كوتلين | `val s = setOf(1, 2, 3)`|
| سكالا | `val s = Set(1, 2, 3)`|
| دارت | `var s = {1, 2, 3}`|
| جوليا | `s = Set([1, 2, 3])`|
| ص | `s <- c(1, 2, 3)`(لا توجد مجموعة أصلية؛ استخدم `%in%`) |
## الهياكل / السجلات / الفئات
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

## التعدادات
| اللغة | بناء الجملة |
|----------|--------|
| الصدأ | `enum Color { Red, Green, Blue }`|
| سويفت | `enum Color { case red, green, blue }`|
| كوتلين | `enum class Color { RED, GREEN, BLUE }`|
| جافا | `enum Color { RED, GREEN, BLUE }`|
| تايب سكريبت | `enum Color { Red, Green, Blue }`|
| ج | `enum Color { RED, GREEN, BLUE };`|
| سي++ | `enum class Color { Red, Green, Blue };`|
| ج # | `enum Color { Red, Green, Blue }`|
| اذهب | `const ( Red = iota; Green; Blue )`(لا يوجد تعداد أصلي) |
| دارت | `enum Color { red, green, blue }`|
| PHP | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| سكالا | `enum Color { case Red, Green, Blue }`(سكالا 3) |
| بايثون | `from enum import Enum; class Color(Enum): RED = 1`|
| روبي | لا يوجد تعداد أصلي (استخدم الثوابت المجمدة أو`dry-enum`) |
## أمان فارغ
| اللغة | معالجة فارغة |
|----------|-------------|
| بايثون |  `None`، لا يوجد أمان فارغ في وقت الترجمة |
| جافا سكريبت | `null`/ `undefined`، تسلسل اختياري`?.`|
| الصدأ | `Option<T>`— لا يوجد شيء فارغ! وقت الترجمة فرض |
| اذهب | `nil`للمؤشرات والشرائح والخرائط والقنوات |
| جافا |  `null`،`Optional<T>`(جافا 8+)،`@Nullable`|
| ج | `NULL`(ماكرو لـ `((void*)0)`) |
| سي++ | `nullptr`(C++11)،`std::optional<T>`|
| ج # |  `null`، أنواع المراجع الخالية (C# 8+)،`Nullable<T>`|
| سويفت | `Optional<T>`(`T?`),`if let`,`guard let`|
| كوتلين | `T?`(لاغية)،`?.`مكالمة آمنة،`?:`Elvis |
| تايب سكريبت | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| هاسكل | `Maybe a`—`Just x`أو`Nothing`|
| سكالا | `Option[T]`—`Some(x)`أو`None`|
| دارت | `T?`(لاغية)، سلامة لاغية (Dart 2.12+) |
| روبي | `nil`(كل شيء صحيح باستثناء`false`و`nil`) |
| الإكسير | لا توجد قيمة فارغة - استخدم`nil`أو مطابقة النمط |
| إرلانج | لا توجد قيمة فارغة - استخدم`undefined`أو مطابقة النمط |