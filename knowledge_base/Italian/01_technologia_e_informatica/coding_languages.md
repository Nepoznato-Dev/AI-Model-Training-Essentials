# Linguaggi di programmazione

## Python

Python è un linguaggio di programmazione di alto livello, interpretato, tipizzato dinamicamente e di uso generale. Enfatizza la leggibilità e utilizza rientri significativi come delimitatori di blocco.

### Nozioni di base sulla sintassi

```python
# Variabili e tipi
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Condizionali
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Cicli
for i in range(5):
    print(i)

while active:
    active = False
```

### Funzioni e suggerimenti sul tipo

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### List comprehension

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classi e OOP

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

### Modelli comuni

- Utilizzare `with open(path) as f:` per la lettura e scrittura di file.
- Preferisci le stringhe f (`f"hello {name}"`) rispetto a `%` o `.format()`.
- Utilizzare `dataclasses.dataclass` per le classi di soli dati.
- Utilizzare `pathlib.Path` invece di `os.path` per i percorsi dei file.

### Strumenti

- `pip install <package>` installa i pacchetti.
- `python -m venv .venv && source .venv/bin/activate` crea un ambiente virtuale.
- `pip freeze > requirements.txt` salva le dipendenze.
- `pip install -r requirements.txt` li ripristina.
- `pyproject.toml` è il moderno standard di configurazione del progetto.

---

## JavaScript

JavaScript è il linguaggio principale del web. Funziona nei browser e sui server tramite Node.js. È tipizzato dinamicamente e basato su prototipi.

### Sintassi moderna (ES6+)

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

### Programmazione asincrona

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

### Metodi degli array

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Manipolazione del DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Strumenti

- `npm init -y` inizializza un progetto.
- `npm install <package>` aggiunge una dipendenza.
- `npm run <script>` esegue uno script definito in `package.json`.
- `node index.js` esegue uno script con Node.js.

---

## TypeScript

TypeScript è un superset di JavaScript tipizzato staticamente che viene compilato in JavaScript semplice. Aggiunge annotazioni di tipo, interfacce, generici ed enumerazioni.

### Annotazioni di tipo

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfacce e tipi

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Generici

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Classi con modificatori di accesso

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

### Elementi essenziali di tsconfig.json

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

### Strumenti

- `npm install -g typescript` installa il compilatore.
- `tsc` compila il progetto.
- `ts-node src/index.ts` esegue direttamente TypeScript.

---

## Rust

Rust è un linguaggio di programmazione di sistemi incentrato su sicurezza, velocità e concorrenza. Previene i bug di sicurezza della memoria in fase di compilazione attraverso il suo sistema di proprietà.

### Proprietà e prestiti

Ogni valore in Rust ha esattamente un proprietario. Quando il proprietario esce dall'ambito, il valore viene eliminato. Il prestito consente referenze senza trasferire la proprietà.

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

I prestiti mutabili (`&mut T`) richiedono che non esistano altri prestiti contemporaneamente.

### Lifetime

La durata garantisce che i riferimenti non sopravvivano ai dati a cui puntano.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enumerazioni e corrispondenza di modelli

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

### Gestione degli errori

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

L'operatore `?` propaga automaticamente gli errori all'interno delle funzioni che restituiscono `Result`.

### Strumenti (carico)

- `cargo new project_name` crea un nuovo progetto.
- `cargo build` compila.
- `cargo run` compila ed esegue.
- `cargo test` esegue i test.
- `cargo add <crate>` aggiunge una dipendenza a `Cargo.toml`.
- `cargo fmt` formatta il codice. `cargo clippy` lint.

---

## Go

Go (Golang) è un linguaggio compilato tipizzato staticamente progettato per semplicità e programmi simultanei ad alte prestazioni.

### Nozioni di base

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Funzioni e valori restituiti multipli

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Interfacce

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

Qualsiasi tipo che implementa tutti i metodi di un'interfaccia la soddisfa: non è necessaria alcuna dichiarazione esplicita.

### Goroutine e canali

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

### `defer`

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

### Strumenti

- `go mod init module/name` inizializza un modulo.
- `go get ./...` scarica le dipendenze.
- `go build ./...` compila.
- `go test ./...` esegue i test.
- `go fmt ./...` formatta il codice.
- `go vet ./...` controlla gli errori comuni.

---

## C e C++

C è un linguaggio procedurale compilato di basso livello. C++ estende C con classi, modelli e la libreria di modelli standard (STL).

### Nozioni di base sul C

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

### Puntatori

Un puntatore memorizza l'indirizzo di memoria di un'altra variabile. `*ptr` lo dereferenzia; `&var` prende un indirizzo.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Classi C++ e RAII

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

RAII (Resource Acquisition Is Initialization) lega il ciclo di vita delle risorse a quello degli oggetti, così il rilascio avviene automaticamente nei distruttori.

### Contenitori STL

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

### Punti chiave del C++ moderno (C++17 / C++20)

- deduzione del tipo con `auto`.
- Cicli `for` basati su intervalli: `for (auto& item : container)`.
- Puntatori intelligenti: `std::unique_ptr`, `std::shared_ptr` — evitare l’uso diretto di `new`/`delete` quando possibile.
- Associazioni strutturate: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilazione
- `gcc main.c -o main` compila C.
- `g++ -std=c++20 -Wall main.cpp -o main` compila C++.
- `make` automatizza le build multi-file tramite un `Makefile`.
- `cmake` è il generatore di sistemi di compilazione standard per progetti più grandi.

---

## Swift

Swift è un linguaggio di programmazione moderno e tipizzato staticamente sviluppato da Apple per iOS, macOS, watchOS e tvOS. È disponibile anche su Linux.

### Nozioni di base

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Opzionali

Un facoltativo (`T?`) rappresenta un valore che può essere presente o meno.

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

### Funzioni e chiusure

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classi e strutture

Swift ha sia classi (tipi di riferimento) che strutture (tipi di valore). Preferire strutture per modelli di dati semplici.

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

### Protocolli

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### `Codable` (codifica/decodifica JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Nozioni di base su SwiftUI

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

### Strumenti

- `swift build` compila un progetto Swift Package Manager.
- `swift run` esegue il progetto.
- `swift test` esegue i test.
- `swift package init --type executable` crea un nuovo progetto eseguibile.
- Xcode è l'IDE principale per lo sviluppo della piattaforma Apple.

---

## Fondamenti di programmazione (indipendenti dal linguaggio)

### Flusso di lavoro per la risoluzione dei problemi

1. Definire l'input, l'output e i vincoli prima di scrivere il codice.
2. Suddividere l'attività in sottoproblemi più piccoli.
3. Parti da una soluzione semplice e corretta, poi ottimizzala solo se necessario.
4. Convalida con test, casi limite e input realistici.

### Strutture dati fondamentali

- **Array/List**: raccolta ordinata con letture indicizzate veloci.
- **Mappa hash/Dizionario**: archivio di valori-chiave con ricerca media O(1).
- **Set**: valori univoci, utili per la verifica dell'appartenenza.
- **Stack**: LIFO (last in, first out), comune nell'analisi e nella ricorsione.
- **Coda**: FIFO (first in, first out), utile per la pianificazione e BFS.
- **Albero/Grafico**: relazioni gerarchiche e di tipo network.

### Complessità algoritmica (Big O)

- Big O descrive come il runtime o la memoria crescono con la dimensione dell'input.
- Costi tipici:
  - O(1): ricerca in tempo costante (ad esempio, accesso alla mappa hash).
  - O(log n): ricerca binaria.
  - O(n): passaggio singolo dei dati.
  - O(n log n): ordinamento efficiente.
  - O(n²): cicli annidati su input di dimensioni simili.
- Preferire un codice chiaro e gestibile a meno che la profilazione non mostri un collo di bottiglia.

### Principi di debug

- Riprodurre prima il bug in modo affidabile.
- Minimizzare il caso di guasto per isolare la causa.
- Esaminare registri, input e ipotesi.
- Modificare una variabile alla volta durante il test.
- Aggiungi test di regressione per evitare che lo stesso bug si ripresenti.

### Piramide dei test

- **Test unitari**: controlli rapidi e mirati di piccole unità logiche.
- **Test di integrazione**: verifica le interazioni tra moduli/servizi.
- **Test end-to-end**: convalida dei flussi utente in ambienti realistici.
- Una suite bilanciata ha molti test unitari e meno test end-to-end lenti.

### Pratiche di qualità del codice

- Utilizzare nomi significativi e piccole funzioni mirate.
- Preferire le funzioni pure (meno effetti collaterali) quando pratico.
- Mantenere i moduli coesi e le interfacce esplicite.
- Utilizzare linter/formattatori per coerenza.
- Rivedere il codice per correttezza, chiarezza e sicurezza.

### Nozioni di base sulla sicurezza per gli sviluppatori

- Convalidare e disinfettare l'input esterno.
- Utilizzare query con parametri per impedire l'iniezione SQL.
- Memorizza le password usando algoritmi di hashing robusti, come Argon2 o bcrypt.
- Evitare di incorporare segreti nel codice sorgente.
- Applicare il privilegio minimo per credenziali e servizi.