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
# 跨语言比较——数据类型和结构
## 原始类型
|类型 |蟒蛇 | JavaScript |铁锈|去 |爪哇 | C | C++ | C# |
|------|--------|------------|-----|----|-----|---|-----|-----|
|整数|  `int`（任意）| `number`|  `i32`、`u64` | `int`|  `int`、`long` | `int`| `int`| `int`|
|浮动| `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
|字符串| `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
|布尔 | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
|人物 | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
|空 | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## 数组/列表
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

## 地图/字典/哈希表
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

＃＃ 套
|语言 |语法 |
|----------|--------|
|蟒蛇 | `s = {1, 2, 3}`|
| JavaScript | `const s = new Set([1, 2, 3])`|
|铁锈| `let s: HashSet<i32> = [1, 2, 3].into()`|
|去 |  `s := map[int]bool{1: true, 2: true, 3: true}`（无内置套装）|
|爪哇 | `Set<Integer> s = Set.of(1, 2, 3)`|
| C++ | `std::set<int> s = {1, 2, 3}`|
| C# | `var s = new HashSet<int> { 1, 2, 3 }`|
|红宝石 | `s = Set[1, 2, 3]`|
|斯威夫特 | `var s: Set<Int> = [1, 2, 3]`|
|科特林 | `val s = setOf(1, 2, 3)`|
|斯卡拉 | `val s = Set(1, 2, 3)`|
|飞镖 | `var s = {1, 2, 3}`|
|朱莉娅 | `s = Set([1, 2, 3])`|
|右 | `s <- c(1, 2, 3)`（无本机设置；使用`%in%`）|
## 结构/记录/类
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

## 枚举
|语言 |语法 |
|----------|--------|
|铁锈| `enum Color { Red, Green, Blue }`|
|斯威夫特 | `enum Color { case red, green, blue }`|
|科特林 | `enum class Color { RED, GREEN, BLUE }`|
|爪哇 | `enum Color { RED, GREEN, BLUE }`|
|打字稿 | `enum Color { Red, Green, Blue }`|
| C | `enum Color { RED, GREEN, BLUE };`|
| C++ | `enum class Color { Red, Green, Blue };`|
| C# | `enum Color { Red, Green, Blue }`|
|去 |  `const ( Red = iota; Green; Blue )`（无本机枚举）|
|飞镖 | `enum Color { red, green, blue }`|
| PHP | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
|斯卡拉 | `enum Color { case Red, Green, Blue }`(Scala 3) |
|蟒蛇 | `from enum import Enum; class Color(Enum): RED = 1`|
|红宝石 |无本机枚举（使用冻结常量或`dry-enum`）|
## 空安全
|语言 |空处理 |
|----------|--------------|
|蟒蛇 | `None`，无编译时空安全 |
| JavaScript | `null`/`undefined`，可选链接`?.`|
|铁锈| `Option<T>`— 不为空！编译时强制 |
|去 | `nil`用于指针、切片、映射、通道 |
|爪哇 |  `null`、`Optional<T>`（Java 8+）、`@Nullable` |
| C |  `NULL`（`((void*)0)` 的宏）|
| C++ | `nullptr`(C++11)、`std::optional<T>` |
| C# | `null`、可为 null 的引用类型 (C# 8+)、`Nullable<T>` |
|斯威夫特 | `Optional<T>`(`T?`),`if let`,`guard let`|
|科特林 |  `T?`（可为空）、`?.` 安全调用、`?:` Elvis |
|打字稿 | `null`/`undefined`、`strictNullChecks`、`T \| null`|
|哈斯克尔 | `Maybe a`—`Just x`或`Nothing`|
|斯卡拉 | `Option[T]`—`Some(x)`或`None`|
|飞镖 |  `T?`（可空），空安全（Dart 2.12+）|
|红宝石 |  `nil`（除了`false`和`nil`之外，一切都是真实的）|
|长生不老药 |无 null — 使用`nil`或模式匹配 |
|二郎 |无 null — 使用`undefined`或模式匹配 |