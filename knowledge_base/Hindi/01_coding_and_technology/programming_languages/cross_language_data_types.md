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
# क्रॉस-लैंग्वेज तुलना - डेटा प्रकार और संरचनाएं
## आदिम प्रकार
| प्रकार | पायथन | जावास्क्रिप्ट | जंग | जाओ | जावा | सी | सी++ | सी# |
|------|--------|----------------|------|----|------|---|----|-----|
| पूर्णांक | `int`(मनमाना) | `number`| `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| तैरना | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| स्ट्रिंग | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| बूलियन | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| चरित्र | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| शून्य | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## सारणियाँ/सूचियाँ
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

## मानचित्र/शब्दकोश/हैश तालिकाएँ
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

## सेट
| भाषा | सिंटैक्स |
|---|--------|
| पायथन | `s = {1, 2, 3}`|
| जावास्क्रिप्ट | `const s = new Set([1, 2, 3])`|
| जंग | `let s: HashSet<i32> = [1, 2, 3].into()`|
| जाओ | `s := map[int]bool{1: true, 2: true, 3: true}`(कोई अंतर्निर्मित सेट नहीं) |
| जावा | `Set<Integer> s = Set.of(1, 2, 3)`|
| सी++ | `std::set<int> s = {1, 2, 3}`|
| सी# | `var s = new HashSet<int> { 1, 2, 3 }`|
| रूबी | `s = Set[1, 2, 3]`|
| स्विफ्ट | `var s: Set<Int> = [1, 2, 3]`|
| कोटलिन | `val s = setOf(1, 2, 3)`|
| स्काला | `val s = Set(1, 2, 3)`|
| डार्ट | `var s = {1, 2, 3}`|
| जूलिया | `s = Set([1, 2, 3])`|
| आर | `s <- c(1, 2, 3)`(कोई मूल सेट नहीं;`%in%`का उपयोग करें) |
## संरचनाएं/अभिलेख/वर्ग
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

## एनम
| भाषा | सिंटैक्स |
|---|--------|
| जंग | `enum Color { Red, Green, Blue }`|
| स्विफ्ट | `enum Color { case red, green, blue }`|
| कोटलिन | `enum class Color { RED, GREEN, BLUE }`|
| जावा | `enum Color { RED, GREEN, BLUE }`|
| टाइपस्क्रिप्ट | `enum Color { Red, Green, Blue }`|
| सी | `enum Color { RED, GREEN, BLUE };`|
| सी++ | `enum class Color { Red, Green, Blue };`|
| सी# | `enum Color { Red, Green, Blue }`|
| जाओ | `const ( Red = iota; Green; Blue )`(कोई मूल एनम नहीं) |
| डार्ट | `enum Color { red, green, blue }`|
| पीएचपी | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| स्काला | `enum Color { case Red, Green, Blue }`(स्कैला 3) |
| पायथन | `from enum import Enum; class Color(Enum): RED = 1`|
| रूबी | कोई मूल एनम नहीं (जमे हुए स्थिरांक या`dry-enum`का उपयोग करें) |
## अशक्त सुरक्षा
| भाषा | अशक्त हैंडलिंग |
|---|-----|
| पायथन |  `None`, कोई संकलन-समय शून्य सुरक्षा नहीं |
| जावास्क्रिप्ट | `null`/ `undefined`, वैकल्पिक चेनिंग`?.`|
| जंग | `Option<T>`- कोई शून्य नहीं! संकलन-समय लागू |
| जाओ |  पॉइंटर्स, स्लाइस, मानचित्र, चैनल के लिए`nil`|
| जावा | `null`,`Optional<T>`(जावा 8+),`@Nullable`|
| सी | `NULL`(`((void*)0)` के लिए मैक्रो) |
| सी++ | `nullptr`(C++11),`std::optional<T>`|
| सी# | `null`, निरर्थक संदर्भ प्रकार (C# 8+),`Nullable<T>`|
| स्विफ्ट | `Optional<T>`(`T?`),`if let`,`guard let`|
| कोटलिन | `T?`(शून्य),`?.`सुरक्षित कॉल,`?:`एल्विस |
| टाइपस्क्रिप्ट | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| हास्केल | `Maybe a`—`Just x`या`Nothing`|
| स्काला | `Option[T]`—`Some(x)`या`None`|
| डार्ट | `T?`(शून्य), शून्य सुरक्षा (डार्ट 2.12+) |
| रूबी | `nil`(`false` और`nil`को छोड़कर सब कुछ सत्य है) |
| अमृत ​​| कोई शून्य नहीं -`nil`या पैटर्न मिलान का उपयोग करें |
| एरलांग | कोई शून्य नहीं -`undefined`या पैटर्न मिलान का उपयोग करें |