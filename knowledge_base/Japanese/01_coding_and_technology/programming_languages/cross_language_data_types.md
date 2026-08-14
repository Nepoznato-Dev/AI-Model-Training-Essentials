<!--
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

-->
# 言語間の比較 — データ型と構造
## プリミティブ型
|タイプ |パイソン | JavaScript |さび |行く |ジャワ | C | C++ | C# |
|------|--------|---------------|------|----|------|---|-----|-----|
|整数 | `int`(任意) | `number`|  `i32`、`u64` | `int`|  `int`、`long` | `int`| `int`| `int`|
|フロート | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
|文字列 | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
|ブール値 | `bool`| `boolean`| `bool`| `bool`|  XQZマーカー30XQZ |  (C99) |`bool`| `bool`| `bool`|
|キャラクター | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`|  XQZマーカー40XQZ | `char`|
|ヌル | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## 配列/リスト
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

## マップ / 辞書 / ハッシュ テーブル
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

## セット
|言語 |構文 |
|----------|----------|
|パイソン | `s = {1, 2, 3}`|
| JavaScript | `const s = new Set([1, 2, 3])`|
|さび | `let s: HashSet<i32> = [1, 2, 3].into()`|
|行く | `s := map[int]bool{1: true, 2: true, 3: true}`(組み込みセットなし) |
|ジャワ | `Set<Integer> s = Set.of(1, 2, 3)`|
| C++ | `std::set<int> s = {1, 2, 3}`|
| C# | `var s = new HashSet<int> { 1, 2, 3 }`|
|ルビー | `s = Set[1, 2, 3]`|
|スイフト | `var s: Set<Int> = [1, 2, 3]`|
|コトリン | `val s = setOf(1, 2, 3)`|
|スカラ座 | `val s = Set(1, 2, 3)`|
|ダーツ | `var s = {1, 2, 3}`|
|ジュリア | `s = Set([1, 2, 3])`|
| R | `s <- c(1, 2, 3)`(ネイティブ セットなし。`%in%`を使用) |
## 構造体 / レコード / クラス
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

## 列挙型
|言語 |構文 |
|----------|----------|
|さび | `enum Color { Red, Green, Blue }`|
|スイフト | `enum Color { case red, green, blue }`|
|コトリン | `enum class Color { RED, GREEN, BLUE }`|
|ジャワ | `enum Color { RED, GREEN, BLUE }`|
|タイプスクリプト | `enum Color { Red, Green, Blue }`|
| C | `enum Color { RED, GREEN, BLUE };`|
| C++ | `enum class Color { Red, Green, Blue };`|
| C# | `enum Color { Red, Green, Blue }`|
|行く | `const ( Red = iota; Green; Blue )`(ネイティブ列挙型なし) |
|ダーツ | `enum Color { red, green, blue }`|
| PHP | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
|スカラ座 | `enum Color { case Red, Green, Blue }`(Scala 3) |
|パイソン | `from enum import Enum; class Color(Enum): RED = 1`|
|ルビー |ネイティブ列挙型なし (固定定数または`dry-enum`を使用) |
## ヌルセーフティ
|言語 | Null の処理 |
|----------|--------------|
|パイソン | `None`、コンパイル時の null 安全性なし |
| JavaScript | `null`/ `undefined`、オプションのチェーン`?.`|
|さび | `Option<T>`— null はありません!コンパイル時に強制 |
|行く |  ポインタ、スラ​​イス、マップ、チャネル用の`nil`|
|ジャワ | `null`、`Optional<T>`(Java 8 以降)、`@Nullable`|
| C | `NULL`(`((void*)0)` のマクロ) |
| C++ | `nullptr`(C++11)、`std::optional<T>` |
| C# | `null`、null 許容参照型 (C# 8 以降)、`Nullable<T>` |
|スイフト | `Optional<T>`(`T?`)、`if let`、`guard let`|
|コトリン | `T?`(null 可能)、`?.` セーフ コール、`?:` Elvis |
|タイプスクリプト | `null`/ `undefined`、`strictNullChecks`、`T \| null` |
|ハスケル | `Maybe a`—`Just x`または`Nothing`|
|スカラ座 | `Option[T]`—`Some(x)`または`None`|
|ダーツ | `T?`(null 可能)、null 安全性 (Dart 2.12 以降) |
|ルビー | `nil`(`false`と`nil`を除くすべてが真実です) |
|エリクサー | null なし —`nil`またはパターン一致を使用します。
|アーラン | null なし —`undefined`またはパターン一致を使用します。