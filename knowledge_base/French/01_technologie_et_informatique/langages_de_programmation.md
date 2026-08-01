<!-- 
This file was automatically translated from English to French.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Langages de programmation

## Python

Python est un langage de programmation généraliste de haut niveau, interprété et à typage dynamique. Il met l'accent sur la lisibilité et utilise une indentation significative pour délimiter les blocs.

### Bases de la syntaxe

```python
# Variables et types
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Conditionnels
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Boucles
for i in range(5):
    print(i)

while active:
    active = False
```

### Fonctions et annotations de type

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Compréhensions de liste

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes et programmation orientée objet

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

### Modèles courants

- Utilisez `with open(path) as f:` pour les entrées/sorties de fichiers.
- Préférez les f-strings (`f"hello {name}"`) à `%` ou `.format()`.
- Utilisez `dataclasses.dataclass` pour les classes ne contenant que des données.
- Utilisez `pathlib.Path` au lieu de `os.path` pour les chemins de fichiers.

### Outils

- `pip install <package>` installe des paquets.
- `python -m venv .venv && source .venv/bin/activate` crée un environnement virtuel.
- `pip freeze > requirements.txt` enregistre les dépendances.
- `pip install -r requirements.txt` les restaure.
- `pyproject.toml` est le standard moderne de configuration des projets.

---

## JavaScript

JavaScript est le langage principal du Web. Il s'exécute dans les navigateurs et sur les serveurs via Node.js. Il est à typage dynamique et fondé sur les prototypes.

### Syntaxe moderne (ES6+)

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

### Programmation asynchrone

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

### Méthodes de tableau

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Manipulation du DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Outils

- `npm init -y` initialise un projet.
- `npm install <package>` ajoute une dépendance.
- `npm run <script>` exécute un script défini dans `package.json`.
- `node index.js` exécute un script avec Node.js.

---

## TypeScript

TypeScript est un sur-ensemble de JavaScript à typage statique qui se compile en JavaScript standard. Il ajoute des annotations de type, des interfaces, des génériques et des enums.

### Annotations de type

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces et types

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### Génériques

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Classes avec modificateurs d'accès

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

### Éléments essentiels de tsconfig.json

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

### Outils

- `npm install -g typescript` installe le compilateur.
- `tsc` compile le projet.
- `ts-node src/index.ts` exécute TypeScript directement.

---

## Rust

Rust est un langage de programmation système axé sur la sûreté, la vitesse et la concurrence. Il prévient les bogues de sûreté mémoire à la compilation grâce à son système de propriété.

### Propriété et emprunt

Chaque valeur en Rust possède exactement un propriétaire. Lorsque le propriétaire sort de sa portée, la valeur est détruite. L'emprunt permet d'utiliser des références sans transférer la propriété.

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

Les emprunts mutables (`&mut T`) exigent qu'aucun autre emprunt n'existe au même moment.

### Durées de vie

Les durées de vie garantissent que les références ne survivent pas aux données qu'elles pointent.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Énumérations et filtrage par motifs

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

### Gestion des erreurs

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

L'opérateur `?` propage automatiquement les erreurs à l'intérieur des fonctions qui renvoient `Result`.

### Outils (Cargo)

- `cargo new project_name` crée un nouveau projet.
- `cargo build` compile.
- `cargo run` compile et exécute.
- `cargo test` exécute les tests.
- `cargo add <crate>` ajoute une dépendance à `Cargo.toml`.
- `cargo fmt` formate le code. `cargo clippy` effectue l'analyse statique.

---

## Go

Go (Golang) est un langage compilé et à typage statique, conçu pour écrire des programmes concurrents simples et performants.

### Bases

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Fonctions et valeurs de retour multiples

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

Tout type qui implémente toutes les méthodes d'une interface la satisfait ; aucune déclaration explicite n'est nécessaire.

### Goroutines et channels

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

### Instruction `defer`

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

### Outils

- `go mod init module/name` initialise un module.
- `go get ./...` télécharge les dépendances.
- `go build ./...` compile.
- `go test ./...` exécute les tests.
- `go fmt ./...` formate le code.
- `go vet ./...` vérifie les erreurs courantes.

---

## C et C++

C est un langage compilé, procédural et de bas niveau. C++ étend C avec des classes, des templates et la Standard Template Library (STL).

### Bases du C

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

### Pointeurs

Un pointeur stocke l'adresse mémoire d'une autre variable. `*ptr` la déréférence ; `&var` en récupère l'adresse.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Classes C++ et RAII

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

Le RAII (Resource Acquisition Is Initialization) lie la durée de vie des ressources à celle des objets, ce qui garantit un nettoyage automatique dans les destructeurs.

### Conteneurs STL

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

### Points forts du C++ moderne (C++17 / C++20)

- Déduction de type avec `auto`.
- Boucles `for` basées sur des intervalles : `for (auto& item : container)`.
- Pointeurs intelligents : `std::unique_ptr`, `std::shared_ptr` — évitez les `new`/`delete` bruts.
- Structured bindings : `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilation

- `gcc main.c -o main` compile du C.
- `g++ -std=c++20 -Wall main.cpp -o main` compile du C++.
- `make` automatise les builds multi-fichiers via un `Makefile`.
- `cmake` est le générateur de systèmes de build standard pour les projets plus importants.

---

## Swift

Swift est un langage de programmation moderne et à typage statique, développé par Apple pour iOS, macOS, watchOS et tvOS. Il est également disponible sur Linux.

### Bases

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Valeurs optionnelles

Un optional (`T?`) représente une valeur qui peut être présente ou non.

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

### Fonctions et closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classes et structures

Swift possède à la fois des classes (types par référence) et des structs (types par valeur). Préférez les structs pour les modèles de données simples.

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

### Protocoles

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable (encodage / décodage JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Bases de SwiftUI

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

### Outils

- `swift build` compile un projet Swift Package Manager.
- `swift run` exécute le projet.
- `swift test` exécute les tests.
- `swift package init --type executable` crée un nouveau projet exécutable.
- Xcode est l'IDE principal pour le développement sur les plateformes Apple.

---

## Fondamentaux du code (indépendants du langage)

### Démarche de résolution de problème

1. Définissez les entrées, les sorties et les contraintes avant d'écrire du code.
2. Découpez la tâche en sous-problèmes plus petits.
3. Commencez par une solution simple et correcte, puis optimisez si nécessaire.
4. Validez avec des tests, des cas limites et des entrées réalistes.

### Structures de données de base

- **Array / List** : collection ordonnée avec lecture indexée rapide.
- **Hash map / Dictionnaire** : stockage clé-valeur avec recherche moyenne en O(1).
- **Set** : ensemble de valeurs uniques, utile pour les tests d'appartenance.
- **Stack** : LIFO (dernier entré, premier sorti), courant en parsing et en récursion.
- **Queue** : FIFO (premier entré, premier sorti), utile pour l'ordonnancement et le BFS.
- **Tree / Graph** : relations hiérarchiques et en réseau.

### Complexité algorithmique (Big O)

- Le Big O décrit la façon dont le temps d'exécution ou l'usage mémoire évolue avec la taille de l'entrée.
- Coûts typiques :
  - O(1) : accès en temps constant (par ex. accès à une table de hachage).
  - O(log n) : recherche binaire.
  - O(n) : parcours simple des données.
  - O(n log n) : tri efficace.
  - O(n²) : boucles imbriquées sur des entrées de taille comparable.
- Préférez un code clair et maintenable, sauf si le profiling montre un goulot d'étranglement.

### Principes de débogage

- Reproduisez d'abord le bug de manière fiable.
- Réduisez le cas d'échec au minimum pour isoler la cause.
- Inspectez les logs, les entrées et les hypothèses.
- Modifiez une seule variable à la fois pendant les tests.
- Ajoutez des tests de régression pour éviter que le même bug ne réapparaisse.

### Pyramide des tests

- **Tests unitaires** : vérifications rapides et ciblées de petites unités logiques.
- **Tests d'intégration** : vérification des interactions entre modules et services.
- **Tests de bout en bout** : validation des parcours utilisateur dans des environnements réalistes.
- Une suite équilibrée comporte de nombreux tests unitaires et moins de tests lents de bout en bout.

### Pratiques de qualité du code

- Utilisez des noms explicites et des fonctions courtes et ciblées.
- Préférez les fonctions pures (avec moins d'effets de bord) lorsque c'est pertinent.
- Gardez des modules cohérents et des interfaces explicites.
- Utilisez des linters et des formatters pour assurer la cohérence.
- Relisez le code pour vérifier la correction, la clarté et la sécurité.

### Bases de sécurité pour les développeurs

- Validez et assainissez les entrées externes.
- Utilisez des requêtes paramétrées pour éviter les injections SQL.
- Stockez les mots de passe avec des algorithmes de hachage robustes (par ex. Argon2, bcrypt).
- Évitez d'intégrer des secrets dans le code source.
- Appliquez le principe du moindre privilège aux identifiants et aux services.
