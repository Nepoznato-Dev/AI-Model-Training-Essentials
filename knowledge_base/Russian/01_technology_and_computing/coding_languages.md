# Языки программирования

## Python

Python — это высокоуровневый, интерпретируемый, динамически типизированный язык программирования общего назначения. Он делает акцент на читаемости и использует значимые отступы как разделители блоков.

### Основы синтаксиса

```python
# Variables and types
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Conditionals
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Loops
for i in range(5):
    print(i)

while active:
    active = False
```

### Функции и подсказки типов

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Генераторы списков

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Классы и ООП

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"
```

### Распространенные приемы

- Используйте `with open(path) as f:` для работы с файлами.
- Предпочитайте f-строки (`f"hello {name}"`) вместо `%` или `.format()`.
- Используйте `dataclasses.dataclass` для классов, хранящих только данные.
- Используйте `pathlib.Path` вместо `os.path` для путей к файлам.

### Инструменты

- `pip install <package>` устанавливает пакеты.
- `python -m venv .venv && source .venv/bin/activate` создает виртуальное окружение.
- `pip freeze > requirements.txt` сохраняет зависимости.
- `pip install -r requirements.txt` восстанавливает их.
- `pyproject.toml` — современный стандарт конфигурации проекта.

---

## JavaScript

JavaScript — основной язык web-разработки. Он работает в браузерах и на серверах через Node.js. Это динамически типизированный язык, основанный на прототипах.

### Современный синтаксис (ES6+)

```javascript
// Variable declarations
const PI = 3.14159;
let counter = 0;

// Arrow functions
const add = (a, b) => a + b;

// Template literals
const greet = name => `Hello, ${name}!`;

// Destructuring
const { x, y } = point;
const [first, ...rest] = array;

// Spread
const merged = { ...defaults, ...overrides };
```

### Асинхронное программирование

```javascript
// Promises
fetch("/api/data")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// Async / await
async function loadUser(id) {
  try {
    const res = await fetch(`/users/${id}`);
    return await res.json();
  } catch (err) {
    console.error(err);
  }
}
```

### Методы массивов

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Манипуляция DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Инструменты

- `npm init -y` инициализирует проект.
- `npm install <package>` добавляет зависимость.
- `npm run <script>` запускает скрипт, определенный в `package.json`.
- `node index.js` запускает скрипт через Node.js.

---

## TypeScript

TypeScript — это статически типизированное надмножество JavaScript, которое компилируется в обычный JavaScript. Оно добавляет аннотации типов, интерфейсы, generics и enum'ы.

### Аннотации типов

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Интерфейсы и типы

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Generics

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Классы с модификаторами доступа

```typescript
class Counter {
  private count: number = 0;

  increment(): void {
    this.count++;
  }

  get value(): number {
    return this.count;
  }
}
```

### Базовые настройки tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "strict": true,
    "outDir": "dist",
    "rootDir": "src"
  }
}
```

### Инструменты

- `npm install -g typescript` устанавливает компилятор.
- `tsc` компилирует проект.
- `ts-node src/index.ts` запускает TypeScript напрямую.

---

## Rust

Rust — это системный язык программирования, ориентированный на безопасность, скорость и конкурентность. Он предотвращает ошибки безопасности памяти на этапе компиляции благодаря системе владения.

### Владение и заимствование

У каждого значения в Rust есть ровно один владелец. Когда владелец выходит из области видимости, значение уничтожается. Заимствование позволяет использовать ссылки без передачи владения.

```rust
fn main() {
    let s = String::from("hello");  // s owns the string
    let len = calculate_length(&s); // borrow s
    println!("{} has length {}", s, len); // s still valid
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Изменяемые заимствования (`&mut T`) требуют, чтобы в тот же момент не существовало других заимствований.

### Времена жизни

Времена жизни гарантируют, что ссылки не переживут данные, на которые указывают.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enum'ы и сопоставление с образцом

```rust
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

fn area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle(r)       => std::f64::consts::PI * r * r,
        Shape::Rectangle(w, h) => w * h,
    }
}
```

### Обработка ошибок

```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
    fs::read_to_string(path)
}

fn main() {
    match read_file("data.txt") {
        Ok(content) => println!("{}", content),
        Err(e)      => eprintln!("Error: {}", e),
    }
}
```

Оператор `?` автоматически пробрасывает ошибки внутри функций, которые возвращают `Result`.

### Инструменты (Cargo)

- `cargo new project_name` создает новый проект.
- `cargo build` компилирует.
- `cargo run` компилирует и запускает.
- `cargo test` запускает тесты.
- `cargo add <crate>` добавляет зависимость в `Cargo.toml`.
- `cargo fmt` форматирует код. `cargo clippy` выполняет lint-проверку.

---

## Go

Go (Golang) — статически типизированный компилируемый язык, созданный для простоты и высокопроизводительных конкурентных программ.

### Основы

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Функции и несколько возвращаемых значений

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Интерфейсы

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Любой тип, реализующий все методы интерфейса, удовлетворяет ему — явное объявление не требуется.

### Goroutines и channels

```go
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * j
    }
}

func main() {
    jobs    := make(chan int, 5)
    results := make(chan int, 5)

    go worker(1, jobs, results)

    for i := 1; i <= 5; i++ {
        jobs <- i
    }
    close(jobs)

    for i := 0; i < 5; i++ {
        fmt.Println(<-results)
    }
}
```

### Defer

```go
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()   // runs when function returns
    // … process f …
    return nil
}
```

### Инструменты

- `go mod init module/name` инициализирует модуль.
- `go get ./...` загружает зависимости.
- `go build ./...` компилирует.
- `go test ./...` запускает тесты.
- `go fmt ./...` форматирует код.
- `go vet ./...` проверяет распространенные ошибки.

---

## C and C++

C — это низкоуровневый компилируемый процедурный язык. C++ расширяет C классами, шаблонами и Standard Template Library (STL).

### Основы C

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* Dynamic memory */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* always free what you malloc */

    return 0;
}
```

### Указатели

Указатель хранит адрес памяти другой переменной. `*ptr` разыменовывает его, а `&var` берет адрес.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Классы C++ и RAII

```cpp
#include <string>
#include <iostream>

class Person {
public:
    Person(std::string name, int age) : name_(name), age_(age) {}

    void greet() const {
        std::cout << "Hi, I'm " << name_ << "\n";
    }

private:
    std::string name_;
    int age_;
};
```

RAII (Resource Acquisition Is Initialization) связывает время жизни ресурсов со временем жизни объектов, благодаря чему очистка автоматически выполняется в деструкторах.

### Контейнеры STL

```cpp
#include <vector>
#include <map>
#include <algorithm>

std::vector<int> v = {3, 1, 4, 1, 5, 9};
std::sort(v.begin(), v.end());

std::map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"]   = 87;
```

### Основные возможности современного C++ (C++17 / C++20)

- Выведение типов через `auto`.
- Циклы `for` по диапазону: `for (auto& item : container)`.
- Умные указатели: `std::unique_ptr`, `std::shared_ptr` — избегайте сырых `new`/`delete`.
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Компиляция

- `gcc main.c -o main` компилирует C.
- `g++ -std=c++20 -Wall main.cpp -o main` компилирует C++.
- `make` автоматизирует сборку из нескольких файлов через `Makefile`.
- `cmake` — стандартный генератор build-систем для более крупных проектов.

---

## Swift

Swift — современный статически типизированный язык программирования, разработанный Apple для iOS, macOS, watchOS и tvOS. Он также доступен на Linux.

### Основы

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Optional (`T?`) представляет значение, которое может присутствовать, а может и отсутствовать.

```swift
var name: String? = nil
name = "Alice"

// Safe unwrapping
if let n = name {
    print("Hello, \(n)")
}

// Nil-coalescing
let display = name ?? "Guest"

// Optional chaining
let length = name?.count
```

### Функции и closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Классы и структуры

В Swift есть и классы (reference types), и структуры (value types). Для простых моделей данных обычно лучше выбирать структуры.

```swift
struct Point {
    var x: Double
    var y: Double
}

class Vehicle {
    var speed: Double = 0.0
    func accelerate(by amount: Double) { speed += amount }
}
```

### Protocols

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable (кодирование / декодирование JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Основы SwiftUI

```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
        }
    }
}
```

### Инструменты

- `swift build` компилирует проект Swift Package Manager.
- `swift run` запускает проект.
- `swift test` запускает тесты.
- `swift package init --type executable` создает новый исполняемый проект.
- Xcode — основная IDE для разработки под платформы Apple.

---

## Основы программирования (независимо от языка)

### Рабочий процесс решения задач

1. Перед написанием кода определите входные данные, выходные данные и ограничения.
2. Разбейте задачу на более мелкие подзадачи.
3. Начните с простого корректного решения, а затем оптимизируйте при необходимости.
4. Проверяйте результат тестами, граничными случаями и реалистичными входными данными.

### Базовые структуры данных

- **Array / List**: упорядоченная коллекция с быстрым доступом по индексу.
- **Hash map / Dictionary**: хранилище ключ-значение со средней сложностью поиска O(1).
- **Set**: уникальные значения, полезны для проверки принадлежности.
- **Stack**: LIFO (last in, first out), часто используется при разборе и рекурсии.
- **Queue**: FIFO (first in, first out), полезна для планирования и BFS.
- **Tree / Graph**: иерархические и сетевые связи.

### Алгоритмическая сложность (Big O)

- Big O описывает, как время выполнения или потребление памяти растет с размером входных данных.
- Типичные оценки:
  - O(1): доступ за постоянное время (например, доступ к hash map).
  - O(log n): бинарный поиск.
  - O(n): один проход по данным.
  - O(n log n): эффективная сортировка.
  - O(n²): вложенные циклы по входным данным схожего размера.
- Предпочитайте ясный и удобный в сопровождении код, если только профилирование не показало узкое место.

### Принципы отладки

- Сначала стабильно воспроизведите ошибку.
- Минимизируйте воспроизводящийся пример, чтобы изолировать причину.
- Проверяйте логи, входные данные и предположения.
- Меняйте по одной переменной за раз во время тестирования.
- Добавляйте регрессионные тесты, чтобы ошибка не возвращалась.

### Пирамида тестирования

- **Unit tests**: быстрые и точечные проверки небольших единиц логики.
- **Integration tests**: проверяют взаимодействие между модулями и сервисами.
- **End-to-end tests**: валидируют пользовательские сценарии в реалистичной среде.
- В сбалансированном наборе много unit-тестов и меньше медленных end-to-end-тестов.

### Практики качества кода

- Используйте понятные имена и небольшие сфокусированные функции.
- По возможности предпочитайте pure functions (меньше побочных эффектов).
- Держите модули целостными, а интерфейсы — явными.
- Используйте linters и formatters для единообразия.
- Проверяйте код на корректность, ясность и безопасность.

### Основы безопасности для разработчиков

- Валидируйте и очищайте внешний ввод.
- Используйте параметризованные запросы для защиты от SQL injection.
- Храните пароли с помощью надежных алгоритмов хеширования (например, Argon2, bcrypt).
- Не встраивайте секреты в исходный код.
- Применяйте принцип наименьших привилегий к учетным данным и сервисам.
