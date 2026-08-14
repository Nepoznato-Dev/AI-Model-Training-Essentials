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
# Comparación entre idiomas: tipos de datos y estructuras
## Tipos primitivos
| Tipo | Pitón | JavaScript | Óxido | Ir | Java | C | C++ | C# |
|------|--------|------------|------|----|------|---|-----|-----|
| Entero | `int`(arbitrario) | `number`| `i32`,`u64`| `int`| `int`,`long`| `int`| `int`| `int`|
| Flotador | `float`| `number`| `f64`| `float64`| `double`| `double`| `double`| `double`|
| Cadena | `str`| `string`| `String`| `string`| `String`| `char*`| `string`| `string`|
| Booleano | `bool`| `boolean`| `bool`| `bool`| `boolean`| `bool`(C99) | `bool`| `bool`|
| Personaje | `str[0]`| `string[0]`| `char`| `rune`| `char`| `char`| `char`| `char`|
| Nulo | `None`| `null`| `Option<T>`| `nil`| `null`| `NULL`| `nullptr`| `null`|
## Matrices / Listas
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

## Mapas / Diccionarios / Tablas hash
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

## Conjuntos
| Idioma | Sintaxis |
|----------|--------|
| Pitón | `s = {1, 2, 3}`|
| JavaScript | `const s = new Set([1, 2, 3])`|
| Óxido | `let s: HashSet<i32> = [1, 2, 3].into()`|
| Ir | `s := map[int]bool{1: true, 2: true, 3: true}`(sin conjunto incorporado) |
| Java | `Set<Integer> s = Set.of(1, 2, 3)`|
| C++ | `std::set<int> s = {1, 2, 3}`|
| C# | `var s = new HashSet<int> { 1, 2, 3 }`|
| Rubí | `s = Set[1, 2, 3]`|
| Rápido | `var s: Set<Int> = [1, 2, 3]`|
| Kotlin | `val s = setOf(1, 2, 3)`|
| Escala | `val s = Set(1, 2, 3)`|
| Dardo | `var s = {1, 2, 3}`|
| Julia | `s = Set([1, 2, 3])`|
| R | `s <- c(1, 2, 3)`(sin conjunto nativo; use `%in%`) |
## Estructuras / Registros / Clases
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

## Enumeraciones
| Idioma | Sintaxis |
|----------|--------|
| Óxido | `enum Color { Red, Green, Blue }`|
| Rápido | `enum Color { case red, green, blue }`|
| Kotlin | `enum class Color { RED, GREEN, BLUE }`|
| Java | `enum Color { RED, GREEN, BLUE }`|
| Mecanografiado | `enum Color { Red, Green, Blue }`|
| C | `enum Color { RED, GREEN, BLUE };`|
| C++ | `enum class Color { Red, Green, Blue };`|
| C# | `enum Color { Red, Green, Blue }`|
| Ir | `const ( Red = iota; Green; Blue )`(sin enumeración nativa) |
| Dardo | `enum Color { red, green, blue }`|
| PHP | `enum Color: string { case Red = 'red'; }`(PHP 8.1) |
| Escala | `enum Color { case Red, Green, Blue }`(Escala 3) |
| Pitón | `from enum import Enum; class Color(Enum): RED = 1`|
| Rubí | Sin enumeración nativa (use constantes congeladas o `dry-enum`) |
## Seguridad nula
| Idioma | Manejo nulo |
|----------|--------------|
| Pitón |  `None`, sin seguridad nula en tiempo de compilación |
| JavaScript | `null`/ `undefined`, encadenamiento opcional`?.`|
| Óxido | `Option<T>`- ¡sin nulo! Tiempo de compilación aplicado |
| Ir | `nil`para punteros, sectores, mapas, canales |
| Java |  `null`,`Optional<T>`(Java 8+),`@Nullable`|
| C | `NULL`(macro para `((void*)0)`) |
| C++ | `nullptr`(C++11),`std::optional<T>`|
| C# |  `null`, tipos de referencia que aceptan valores NULL (C# 8+),`Nullable<T>`|
| Rápido | `Optional<T>`(`T?`),`if let`,`guard let`|
| Kotlin | `T?`(anulable),`?.`llamada segura,`?:`Elvis |
| Mecanografiado | `null`/`undefined`,`strictNullChecks`,`T \| null`|
| Haskel | `Maybe a`—`Just x`o`Nothing`|
| Escala | `Option[T]`—`Some(x)`o`None`|
| Dardo | `T?`(anulable), seguridad nula (Dart 2.12+) |
| Rubí | `nil`(todo es veraz excepto`false`y `nil`) |
| Elixir | No nulo: use`nil`o coincidencia de patrón |
| Erlang | No nulo: use`undefined`o coincidencia de patrón |