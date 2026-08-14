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

# 언어 간 비교 — 데이터 유형 및 구조
## 기본 유형
| 유형 | 파이썬 | 자바스크립트 | 녹 | 이동 | 자바 | 다 | C++ | C# |
|------|----------|------------|------|----|------|---|------|----|
| 정수 |  `int`(임의) | `number`|  `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| 플로트 | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| 문자열 | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| 부울 | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| 캐릭터 | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| 널 | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## 배열/목록
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

## 지도/사전/해시 테이블
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

## 세트
| 언어 | 구문 |
|----------|---------|
| 파이썬 | `s = {1, 2, 3}`|
| 자바스크립트 | `const s = new Set([1, 2, 3])`|
| 녹 | `let s: HashSet<i32> = [1, 2, 3].into()`|
| 이동 |  `s := map[int]bool{1: true, 2: true, 3: true}`(내장 세트 없음) |
| 자바 | `Set<Integer> s = Set.of(1, 2, 3)`|
| C++ | `std::set<int> s = {1, 2, 3}`|
| C# | `var s = new HashSet<int> { 1, 2, 3 }`|
| 루비 | `s = Set[1, 2, 3]`|
| 스위프트 | `var s: Set<Int> = [1, 2, 3]`|
| 코틀린 | `val s = setOf(1, 2, 3)`|
| 스칼라 | `val s = Set(1, 2, 3)`|
| 다트 | `var s = {1, 2, 3}`|
| 줄리아 | `s = Set([1, 2, 3])`|
| R |  `s <- c(1, 2, 3)`(네이티브 세트 없음,`%in%`사용) |
## 구조체/레코드/클래스
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

## 열거형
| 언어 | 구문 |
|----------|---------|
| 녹 | `enum Color { Red, Green, Blue }`|
| 스위프트 | `enum Color { case red, green, blue }`|
| 코틀린 | `enum class Color { RED, GREEN, BLUE }`|
| 자바 | `enum Color { RED, GREEN, BLUE }`|
| 타입스크립트 | `enum Color { Red, Green, Blue }`|
| 다 | `enum Color { RED, GREEN, BLUE };`|
| C++ | `enum class Color { Red, Green, Blue };`|
| C# | `enum Color { Red, Green, Blue }`|
| 이동 |  `const ( Red = iota; Green; Blue )`(네이티브 열거형 없음) |
| 다트 | `enum Color { red, green, blue }`|
| PHP | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| 스칼라 |  `enum Color { case Red, Green, Blue }`(스칼라 3) |
| 파이썬 | `from enum import Enum; class Color(Enum): RED = 1`|
| 루비 | 네이티브 열거형 없음(고정 상수 또는`dry-enum`사용) |
## 안전이 보장되지 않음
| 언어 | Null 처리 |
|------------|--------------|
| 파이썬 | `None`, 컴파일 타임 null 안전성 없음 |
| 자바스크립트 | `null`/`undefined`, 선택적 체인`?.`|
| 녹 | `Option<T>`— null이 아닙니다! 컴파일 시간 시행 |
| 이동 |  포인터, 슬라이스, 맵, 채널용`nil`|
| 자바 | `null`, `Optional<T>`(자바 8+),`@Nullable`|
| 다 |  `NULL`(`((void*)0)`용 매크로) |
| C++ |  `nullptr`(C++11),`std::optional<T>`|
| C# | `null`, null 허용 참조 유형(C# 8+),`Nullable<T>`|
| 스위프트 | `Optional<T>`(`T?`),`if let`,`guard let`|
| 코틀린 |  `T?`(null 가능),`?.`안전 호출,`?:`Elvis |
| 타입스크립트 | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| 하스켈 | `Maybe a`—`Just x`또는`Nothing`|
| 스칼라 | `Option[T]`—`Some(x)`또는`None`|
| 다트 |  `T?`(null 가능), null 안전(Dart 2.12+) |
| 루비 | `nil`(`false` 및 `nil`를 제외한 모든 것이 진실입니다) |
| 엘릭서 | null 없음 —`nil`또는 패턴 일치 사용 |
| 얼랭 | null 없음 —`undefined`또는 패턴 일치 사용 |