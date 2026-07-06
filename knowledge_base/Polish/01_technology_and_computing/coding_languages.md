# Języki kodowania

## Pythona

Python to interpretowany, dynamicznie typowany język programowania wysokiego poziomu ogólnego przeznaczenia. Podkreśla czytelność i używa znacznych wcięć jako ograniczników bloków.

### Podstawy składni

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

### Funkcje i wskazówki dotyczące typów

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Lista wyrażeń

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Klasy i OOP

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

### Typowe wzorce

- Użyj `with open(path) as f:` dla wejścia/wyjścia pliku.
- Preferuj ciągi f (`f"hello {name}"`) zamiast `%` lub `.format()`.
- Użyj `dataclasses.dataclass` dla klas zawierających tylko dane.
- Użyj `pathlib.Path` zamiast `os.path` dla ścieżek plików.

### Oprzyrządowanie

- `pip install <package>` instaluje pakiety.
- `python -m venv .venv && source .venv/bin/activate` tworzy środowisko wirtualne.
- `pip freeze > requirements.txt` zapisuje zależności.
- `pip install -r requirements.txt` przywraca je.
- `pyproject.toml` to nowoczesny standard konfiguracji projektów.

---

## JavaScript

JavaScript jest głównym językiem sieci. Działa w przeglądarkach i na serwerach poprzez Node.js. Jest dynamicznie wpisywany i oparty na prototypach.

### Nowoczesna składnia (ES6+)

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

### Programowanie asynchroniczne

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

### Metody tablicowe

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Manipulacja DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Oprzyrządowanie

- `npm init -y` inicjuje projekt.
- `npm install <package>` dodaje zależność.
- `npm run <script>` uruchamia skrypt zdefiniowany w `package.json`.
- `node index.js` uruchamia skrypt z Node.js.

---

## Maszynopis

TypeScript to statycznie typowany nadzbiór kodu JavaScript, który kompiluje się do zwykłego kodu JavaScript. Dodaje adnotacje typów, interfejsy, typy generyczne i wyliczenia.

### Wpisz adnotacje

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfejsy i typy

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Ogólne

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Klasy z modyfikatorami dostępu

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

### Podstawowe informacje o pliku tsconfig.json

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

### Oprzyrządowanie

- `npm install -g typescript` instaluje kompilator.
- `tsc` kompiluje projekt.
- `ts-node src/index.ts` bezpośrednio uruchamia TypeScript.

---

## Rdza

Rust to język programowania systemów skupiający się na bezpieczeństwie, szybkości i współbieżności. Zapobiega błędom związanym z bezpieczeństwem pamięci w czasie kompilacji poprzez swój system własności.

### Własność i pożyczanie

Każda wartość w Rust ma dokładnie jednego właściciela. Gdy właściciel wyjdzie poza zakres, wartość zostanie usunięta. Wypożyczanie umożliwia referencje bez przeniesienia własności.

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

Zmienne zapożyczenia (`&mut T`) wymagają, aby w tym samym czasie nie istniały żadne inne zapożyczenia.

### Całe życie

Okresy istnienia zapewniają, że referencje nie przetrwają dłużej niż dane, na które wskazują.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Wyliczenia i dopasowywanie wzorców

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

### Obsługa błędów

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

Operator `?` automatycznie propaguje błędy wewnątrz funkcji zwracających `Result`.

### Oprzyrządowanie (ładunek)

- `cargo new project_name` tworzy nowy projekt.
- `cargo build` kompiluje.
- `cargo run` kompiluje i uruchamia.
- `cargo test` uruchamia testy.
- `cargo add <crate>` dodaje zależność do `Cargo.toml`.
- `cargo fmt` formatuje kod. `cargo clippy` linty.

---

## Idź

Go (Golang) to skompilowany język ze statycznym typem, zaprojektowany z myślą o prostocie i wysokiej wydajności programów współbieżnych.

### Podstawy

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Funkcje i wiele zwracanych wartości

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Interfejsy

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Spełnia go każdy typ, który implementuje wszystkie metody interfejsu — nie jest wymagana żadna jawna deklaracja.

### Goroutines i kanały

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

### Odłóż

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

### Oprzyrządowanie

- `go mod init module/name` inicjuje moduł.
- `go get ./...` pobiera zależności.
- `go build ./...` kompiluje.
- `go test ./...` uruchamia testy.
- `go fmt ./...` formatuje kod.
- `go vet ./...` sprawdza typowe błędy.

---

## C i C++

C jest skompilowanym językiem proceduralnym niskiego poziomu. C++ rozszerza C o klasy, szablony i standardową bibliotekę szablonów (STL).

### Podstawy języka C

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

### Wskazówki

Wskaźnik przechowuje adres pamięci innej zmiennej. `*ptr` usuwa referencje; `&var` pobiera adres.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Klasy C++ i RAII

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

RAII (Resource Acquisition Is Inicjalizacja) wiąże czasy życia zasobów z okresami istnienia obiektów, zapewniając, że czyszczenie w destruktorach odbywa się automatycznie.

### Kontenery STL

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

### Najważniejsze cechy współczesnego C++ (C++17 / C++20).

- `auto` wpisz odliczenie.
- Pętle `for` oparte na zakresach: `for (auto& item : container)`.
- Inteligentne wskaźniki: `std::unique_ptr`, `std::shared_ptr` — unikaj surowych `new`>/`delete`.
- Wiązania strukturalne: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Kompilacja- `gcc main.c -o main` kompiluje C.
- `g++ -std=c++20 -Wall main.cpp -o main` kompiluje C++.
- `make` automatyzuje kompilacje wielu plików za pomocą `Makefile`.
- `cmake` to standardowy generator systemu kompilacji dla większych projektów.

---

## Szybki

Swift to nowoczesny język programowania ze statycznym typem opracowany przez firmę Apple dla systemów iOS, macOS, watchOS i tvOS. Jest również dostępny na Linuksie.

### Podstawy

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Opcjonalne

Opcjonalny (`T?`) reprezentuje wartość, która może występować lub nie.

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

### Funkcje i zamknięcia

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Klasy i struktury

Swift ma zarówno klasy (typy referencyjne), jak i struktury (typy wartości). Preferuj struktury dla prostych modeli danych.

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

### Protokoły

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Kodowalne (kodowanie/dekodowanie JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Podstawy SwiftUI

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

### Oprzyrządowanie

- `swift build` kompiluje projekt Swift Package Manager.
- `swift run` uruchamia projekt.
- `swift test` uruchamia testy.
- `swift package init --type executable` tworzy nowy projekt wykonywalny.
- Xcode jest podstawowym IDE do programowania platformy Apple.

---

## Podstawy kodowania (niezależnie od języka)

### Przepływ pracy związany z rozwiązywaniem problemów

1. Zdefiniuj dane wejściowe, wyjściowe i ograniczenia przed napisaniem kodu.
2. Podziel zadanie na mniejsze podproblemy.
3. Zacznij od prostego, prawidłowego rozwiązania, a następnie zoptymalizuj je, jeśli zajdzie taka potrzeba.
4. Sprawdź poprawność za pomocą testów, przypadków brzegowych i realistycznych danych wejściowych.

### Podstawowe struktury danych

- **Array / List**: uporządkowana kolekcja z szybkimi indeksowanymi odczytami.
- **Mapa skrótów / Słownik**: magazyn klucz-wartość ze średnim wyszukiwaniem O(1).
- **Set**: unikalne wartości, przydatne przy sprawdzaniu członkostwa.
- **Stos**: LIFO (ostatni na wejściu, pierwszy na wyjściu), powszechny w analizowaniu i rekurencji.
- **Kolejka**: FIFO (pierwsze weszło, pierwsze wyszło), przydatne do planowania i BFS.
- **Drzewo / Wykres**: relacje hierarchiczne i sieciowe.

### Złożoność algorytmiczna (duże O)

- Duże O opisuje, jak rośnie czas wykonania lub pamięć wraz z rozmiarem danych wejściowych.
- Typowe koszty:
  - O(1): wyszukiwanie w czasie stałym (np. dostęp do mapy mieszającej).
  - O(log n): wyszukiwanie binarne.
  - O(n): dane z pojedynczym przejściem.
  - O(n log n): efektywne sortowanie.
  - O(n²): zagnieżdżone pętle na wejściach o podobnym rozmiarze.
- Preferuj przejrzysty, łatwy w utrzymaniu kod, chyba że profilowanie wykryje wąskie gardło.

### Zasady debugowania

- Najpierw niezawodnie odtwórz błąd.
- Zminimalizuj przypadek niepowodzenia, aby wyizolować przyczynę.
- Sprawdź dzienniki, dane wejściowe i założenia.
- Zmieniaj jedną zmienną na raz podczas testowania.
- Dodaj testy regresyjne, aby ten sam błąd nie powrócił.

### Piramida testowania

- **Testy jednostkowe**: szybkie, ukierunkowane sprawdzenie małych jednostek logicznych.
- **Testy integracyjne**: weryfikują interakcje pomiędzy modułami/usługami.
- **Kompleksowe testy**: weryfikuj przepływy użytkowników w realistycznych środowiskach.
- Zrównoważony pakiet ma wiele testów jednostkowych i mniej powolnych testów kompleksowych.

### Praktyki dotyczące jakości kodu

- Używaj znaczących nazw i małych funkcji.
- Preferuj czyste funkcje (mniej skutków ubocznych), jeśli jest to praktyczne.
- Zachowaj spójność modułów i przejrzystość interfejsów.
- Aby zachować spójność, użyj lintersów/formatów.
- Przejrzyj kod pod kątem poprawności, przejrzystości i bezpieczeństwa.

### Podstawy bezpieczeństwa dla programistów

- Sprawdź i oczyść dane wejściowe z zewnątrz.
- Używaj sparametryzowanych zapytań, aby zapobiec wstrzykiwaniu SQL.
- Przechowuj hasła za pomocą silnych algorytmów mieszania (np. Argon2, bcrypt).
- Unikaj osadzania sekretów w kodzie źródłowym.
- Zastosuj najmniejsze uprawnienia do poświadczeń i usług.