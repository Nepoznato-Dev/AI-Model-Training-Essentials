# Programmiersprachen

## Python

Python ist eine allgemein einsetzbare, interpretierte, dynamisch typisierte Programmiersprache auf hohem Niveau. Sie legt Wert auf Lesbarkeit und verwendet signifikante Einrückung als Blockbegrenzer.

### Syntax-Grundlagen

```python
# Variablen und Typen
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Bedingungen
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Schleifen
for i in range(5):
    print(i)

while active:
    active = False
```

### Funktionen und Type Hints

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### List Comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Klassen und OOP

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

### Häufige Muster

- Verwende `with open(path) as f:` für Datei-I/O.
- Bevorzuge f-strings (`f"hello {name}"`) gegenüber `%` oder `.format()`.
- Verwende `dataclasses.dataclass` für reine Datenklassen.
- Verwende `pathlib.Path` anstelle von `os.path` für Dateipfade.

### Tooling

- `pip install <package>` installiert Pakete.
- `python -m venv .venv && source .venv/bin/activate` erstellt eine virtuelle Umgebung.
- `pip freeze > requirements.txt` speichert Abhängigkeiten.
- `pip install -r requirements.txt` stellt sie wieder her.
- `pyproject.toml` ist der moderne Standard für Projektkonfiguration.

---

## JavaScript

JavaScript ist die primäre Sprache des Webs. Es läuft in Browsern und auf Servern über Node.js. Es ist dynamisch typisiert und prototypbasiert.

### Moderne Syntax (ES6+)

```javascript
// Variablendeklarationen
const PI = 3.14159;
let counter = 0;

// Arrow-Funktionen
const add = (a, b) => a + b;

// Template-Literale
const greet = name => `Hello, ${name}!`;

// Destrukturierung
const { x, y } = point;
const [first, ...rest] = array;

// Spread
const merged = { ...defaults, ...overrides };
```

### Asynchrone Programmierung

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

### Array-Methoden

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM-Manipulation

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Tooling

- `npm init -y` initialisiert ein Projekt.
- `npm install <package>` fügt eine Abhängigkeit hinzu.
- `npm run <script>` führt ein in `package.json` definiertes Skript aus.
- `node index.js` führt ein Skript mit Node.js aus.

---

## TypeScript

TypeScript ist eine statisch typisierte Obermenge von JavaScript, die zu einfachem JavaScript kompiliert wird. Es fügt Typannotationen, Interfaces, Generics und Enums hinzu.

### Typannotationen

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces und Typen

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optionale Eigenschaft
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

### Klassen mit Zugriffsmodifizierern

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

### tsconfig.json-Grundlagen

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

### Tooling

- `npm install -g typescript` installiert den Compiler.
- `tsc` kompiliert das Projekt.
- `ts-node src/index.ts` führt TypeScript direkt aus.

---

## Rust

Rust ist eine Systemprogrammiersprache mit Fokus auf Sicherheit, Geschwindigkeit und Nebenläufigkeit. Sie verhindert Speicher-Sicherheitsfehler bereits zur Compile-Zeit durch ihr Ownership-System.

### Ownership und Borrowing

Jeder Wert in Rust hat genau einen Owner. Wenn der Owner den Gültigkeitsbereich verlässt, wird der Wert freigegeben. Borrowing erlaubt Referenzen, ohne Ownership zu übertragen.

```rust
fn main() {
    let s = String::from("hello");  // s besitzt den String
    let len = calculate_length(&s); // leihe s aus
    println!("{} has length {}", s, len); // s weiterhin gültig
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Veränderliche Borrows (`&mut T`) erfordern, dass gleichzeitig keine anderen Borrows existieren.

### Lifetimes

Lifetimes stellen sicher, dass Referenzen nicht länger leben als die Daten, auf die sie zeigen.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums und Pattern Matching

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

### Fehlerbehandlung

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

Der Operator `?` gibt Fehler in Funktionen, die `Result` zurückgeben, automatisch weiter.

### Tooling (Cargo)

- `cargo new project_name` erstellt ein neues Projekt.
- `cargo build` kompiliert.
- `cargo run` kompiliert und führt aus.
- `cargo test` führt Tests aus.
- `cargo add <crate>` fügt eine Abhängigkeit zu `Cargo.toml` hinzu.
- `cargo fmt` formatiert Code. `cargo clippy` lintet.

---

## Go

Go (Golang) ist eine statisch typisierte, kompilierte Sprache, die für Einfachheit und hochperformante nebenläufige Programme entworfen wurde.

### Grundlagen

```go
package main

import "fmt"

func main() {
    name := "world"          // kurze Variablendeklaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Funktionen und mehrere Rückgabewerte

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Interfaces

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Jeder Typ, der alle Methoden eines Interfaces implementiert, erfüllt es — eine explizite Deklaration ist nicht nötig.

### Goroutines und Channels

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
    defer f.Close()   // wird ausgeführt, wenn die Funktion zurückkehrt
    // … verarbeite f …
    return nil
}
```

### Tooling

- `go mod init module/name` initialisiert ein Modul.
- `go get ./...` lädt Abhängigkeiten herunter.
- `go build ./...` kompiliert.
- `go test ./...` führt Tests aus.
- `go fmt ./...` formatiert Code.
- `go vet ./...` prüft auf häufige Fehler.

---

## C und C++

C ist eine prozedurale, kompilierte Sprache auf niedriger Ebene. C++ erweitert C um Klassen, Templates und die Standard Template Library (STL).

### C-Grundlagen

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* Dynamischer Speicher */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* immer freigeben, was du mit malloc reservierst */

    return 0;
}
```

### Zeiger

Ein Zeiger speichert die Speicheradresse einer anderen Variable. `*ptr` dereferenziert ihn; `&var` liefert eine Adresse.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a ist jetzt 20 */
```

### C++-Klassen und RAII

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

RAII (Resource Acquisition Is Initialization) bindet die Lebensdauer von Ressourcen an die Lebensdauer von Objekten und stellt sicher, dass die Bereinigung in Destruktoren automatisch erfolgt.

### STL-Container

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

### Highlights von modernem C++ (C++17 / C++20)

- `auto`-Typinferenz.
- Bereichsbasierte `for`-Schleifen: `for (auto& item : container)`.
- Smart Pointer: `std::unique_ptr`, `std::shared_ptr` — vermeide rohes `new`/`delete`.
- Strukturierte Bindungen: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Kompilierung

- `gcc main.c -o main` kompiliert C.
- `g++ -std=c++20 -Wall main.cpp -o main` kompiliert C++.
- `make` automatisiert Builds mit mehreren Dateien über ein `Makefile`.
- `cmake` ist der Standard-Build-System-Generator für größere Projekte.

---

## Swift

Swift ist eine moderne, statisch typisierte Programmiersprache, die von Apple für iOS, macOS, watchOS und tvOS entwickelt wurde. Sie ist auch auf Linux verfügbar.

### Grundlagen

```swift
let greeting = "Hello, world!"   // Konstante (unveränderlich)
var counter  = 0                  // Variable (veränderlich)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Ein Optional (`T?`) repräsentiert einen Wert, der vorhanden sein kann oder auch nicht.

```swift
var name: String? = nil
name = "Alice"

// Sicheres Unwrapping
if let n = name {
    print("Hello, \(n)")
}

// Nil-Coalescing
let display = name ?? "Guest"

// Optional Chaining
let length = name?.count
```

### Funktionen und Closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Klassen und Structs

Swift hat sowohl Klassen (Referenztypen) als auch Structs (Wertetypen). Für einfache Datenmodelle sind Structs zu bevorzugen.

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

### Protokolle

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable (JSON encoding / decoding)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### SwiftUI-Grundlagen

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

### Tooling

- `swift build` kompiliert ein Swift-Package-Manager-Projekt.
- `swift run` führt das Projekt aus.
- `swift test` führt Tests aus.
- `swift package init --type executable` erstellt ein neues ausführbares Projekt.
- Xcode ist die primäre IDE für die Entwicklung auf Apple-Plattformen.

---

## Programmiergrundlagen (sprachunabhängig)

### Problemlösungs-Workflow

1. Definiere Eingabe, Ausgabe und Randbedingungen, bevor du Code schreibst.
2. Teile die Aufgabe in kleinere Teilprobleme auf.
3. Beginne mit einer einfachen, korrekten Lösung und optimiere erst bei Bedarf.
4. Validiere mit Tests, Randfällen und realistischen Eingaben.

### Zentrale Datenstrukturen

- **Array / Liste**: geordnete Sammlung mit schnellem indexbasiertem Lesen.
- **Hash Map / Dictionary**: Key-Value-Speicher mit durchschnittlich O(1)-Lookup.
- **Set**: eindeutige Werte, nützlich für Membership-Checks.
- **Stack**: LIFO (last in, first out), häufig beim Parsen und in Rekursion.
- **Queue**: FIFO (first in, first out), nützlich für Scheduling und BFS.
- **Baum / Graph**: hierarchische und netzwerkartige Beziehungen.

### Algorithmische Komplexität (Big O)

- Big O beschreibt, wie Laufzeit oder Speicher mit der Eingabegröße wachsen.
- Typische Kosten:
  - O(1): Lookup in konstanter Zeit (z. B. Zugriff auf eine Hash Map).
  - O(log n): binäre Suche.
  - O(n): einmaliger Durchlauf durch Daten.
  - O(n log n): effizientes Sortieren.
  - O(n²): verschachtelte Schleifen über Eingaben ähnlicher Größe.
- Bevorzuge klaren, wartbaren Code, sofern Profiling keinen Engpass zeigt.

### Debugging-Prinzipien

- Reproduziere den Bug zuerst zuverlässig.
- Minimiere den fehlschlagenden Fall, um die Ursache einzugrenzen.
- Untersuche Logs, Eingaben und Annahmen.
- Ändere beim Testen immer nur eine Variable auf einmal.
- Füge Regressionstests hinzu, damit derselbe Bug nicht zurückkehrt.

### Testpyramide

- **Unit Tests**: schnelle, fokussierte Prüfungen kleiner Logikeinheiten.
- **Integrationstests**: verifizieren Interaktionen zwischen Modulen/Services.
- **End-to-End-Tests**: validieren Nutzerabläufe in realistischen Umgebungen.
- Eine ausgewogene Testsuite hat viele Unit Tests und weniger langsame End-to-End-Tests.

### Praktiken für Codequalität

- Verwende aussagekräftige Namen und kleine, fokussierte Funktionen.
- Bevorzuge, wenn praktikabel, reine Funktionen (weniger Seiteneffekte).
- Halte Module kohäsiv und Schnittstellen explizit.
- Nutze Linter/Formatter für Konsistenz.
- Überprüfe Code auf Korrektheit, Klarheit und Sicherheit.

### Sicherheitsgrundlagen für Entwickler

- Validiere und bereinige externe Eingaben.
- Verwende parametrisierte Abfragen, um SQL Injection zu verhindern.
- Speichere Passwörter mit starken Hashing-Algorithmen (z. B. Argon2, bcrypt).
- Vermeide das Einbetten von Secrets im Quellcode.
- Wende Least Privilege für Anmeldedaten und Services an.
