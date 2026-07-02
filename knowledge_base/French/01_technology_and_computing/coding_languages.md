# Langages de programmation

## Python

Python est un langage de programmation de haut niveau, interprété, à typage dynamique et polyvalent. Il met l'accent sur la lisibilité et utilise une indentation significative comme délimiteur de blocs.

### Bases de la syntaxe

```python
# Variables et types
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Conditions
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

### Compréhensions de listes

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes et POO

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

- Utilisez `with open(path) as f:` pour les E/S de fichiers.
- Préférez les f-strings (`f"hello {name}"`) à `%` ou `.format()`.
- Utilisez `dataclasses.dataclass` pour les classes contenant uniquement des données.
- Utilisez `pathlib.Path` au lieu de `os.path` pour les chemins de fichiers.

### Outils

- `pip install <package>` installe des packages.
- `python -m venv .venv && source .venv/bin/activate` crée un environnement virtuel.
- `pip freeze > requirements.txt` enregistre les dépendances.
- `pip install -r requirements.txt` les restaure.
- `pyproject.toml` est le standard moderne de configuration de projet.

---

## JavaScript

JavaScript est le langage principal du web. Il s'exécute dans les navigateurs et sur les serveurs via Node.js. Il est à typage dynamique et basé sur les prototypes.

### Syntaxe moderne (ES6+)

```javascript
// Déclarations de variables
const PI = 3.14159;
let counter = 0;

// Fonctions fléchées
const add = (a, b) => a + b;

// Gabarits de chaînes
const greet = name => `Hello, ${name}!`;

// Déstructuration
const { x, y } = point;
const [first, ...rest] = array;

// Spread
const merged = { ...defaults, ...overrides };
```

### Programmation asynchrone

```javascript
// Promesses
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

TypeScript est un surensemble de JavaScript à typage statique qui se compile en JavaScript standard. Il ajoute des annotations de type, des interfaces, des génériques et des énumérations.

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
  email?: string;   // propriété optionnelle
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

Rust est un langage de programmation système axé sur la sécurité, la vitesse et la concurrence. Il empêche les bugs de sécurité mémoire à la compilation grâce à son système d'ownership.

### Ownership et borrowing

Chaque valeur en Rust possède exactement un propriétaire. Lorsque le propriétaire sort de la portée, la valeur est libérée. Le borrowing permet d'utiliser des références sans transférer l'ownership.

```rust
fn main() {
    let s = String::from("hello");  // s possède la chaîne
    let len = calculate_length(&s); // emprunte s
    println!("{} has length {}", s, len); // s reste valide
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Les emprunts mutables (`&mut T`) exigent qu'aucun autre emprunt n'existe au même moment.

### Lifetimes

Les lifetimes garantissent que les références ne survivent pas aux données qu'elles pointent.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums et pattern matching

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

L'opérateur `?` propage automatiquement les erreurs dans les fonctions qui renvoient `Result`.

### Outils (Cargo)

- `cargo new project_name` crée un nouveau projet.
- `cargo build` compile.
- `cargo run` compile et exécute.
- `cargo test` exécute les tests.
- `cargo add <crate>` ajoute une dépendance à `Cargo.toml`.
- `cargo fmt` formate le code. `cargo clippy` réalise l'analyse statique.

---

## Go

Go (Golang) est un langage compilé à typage statique conçu pour la simplicité et les programmes concurrents haute performance.

### Bases

```go
package main

import "fmt"

func main() {
    name := "world"          // déclaration courte de variable
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

Tout type qui implémente toutes les méthodes d'une interface la satisfait — aucune déclaration explicite n'est nécessaire.

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

### Defer

```go
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()   // s'exécute au retour de la fonction
    // … traite f …
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

C est un langage bas niveau, compilé et procédural. C++ étend C avec des classes, des templates et la Standard Template Library (STL).

### Bases du C

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* Mémoire dynamique */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* libérez toujours ce que vous allouez avec malloc */

    return 0;
}
```

### Pointeurs

Un pointeur stocke l'adresse mémoire d'une autre variable. `*p` la déréférence ; `&a` prend une adresse.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a vaut maintenant 20 */
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

RAII (Resource Acquisition Is Initialization) lie la durée de vie des ressources à celle des objets, ce qui garantit un nettoyage automatique dans les destructeurs.

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
- Smart pointers : `std::unique_ptr`, `std::shared_ptr` — évitez `new`/`delete` bruts.
- Structured bindings : `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilation

- `gcc main.c -o main` compile du C.
- `g++ -std=c++20 -Wall main.cpp -o main` compile du C++.
- `make` automatise les builds multi-fichiers via un `Makefile`.
- `cmake` est le générateur de systèmes de build standard pour les projets plus importants.

---

## Swift

Swift est un langage de programmation moderne à typage statique développé par Apple pour iOS, macOS, watchOS et tvOS. Il est également disponible sous Linux.

### Bases

```swift
let greeting = "Hello, world!"   // constante (immuable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Un optional (`T?`) représente une valeur qui peut être présente ou non.

```swift
var name: String? = nil
name = "Alice"

// Déballage sécurisé
if let n = name {
    print("Hello, \(n)")
}

// Nil-coalescing
let display = name ?? "Guest"

// Chaînage optionnel
let length = name?.count
```

### Fonctions et closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classes et structs

Swift propose à la fois des classes (types référence) et des structs (types valeur). Préférez les structs pour les modèles de données simples.

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

1. Définissez l'entrée, la sortie et les contraintes avant d'écrire du code.
2. Découpez la tâche en sous-problèmes plus petits.
3. Commencez par une solution simple et correcte, puis optimisez si nécessaire.
4. Validez avec des tests, des cas limites et des entrées réalistes.

### Structures de données fondamentales

- **Array / List** : collection ordonnée avec lecture indexée rapide.
- **Hash map / Dictionary** : stockage clé-valeur avec recherche moyenne en O(1).
- **Set** : valeurs uniques, utile pour les tests d'appartenance.
- **Stack** : LIFO (dernier entré, premier sorti), courant en parsing et récursivité.
- **Queue** : FIFO (premier entré, premier sorti), utile pour l'ordonnancement et le BFS.
- **Tree / Graph** : relations hiérarchiques et de type réseau.

### Complexité algorithmique (Big O)

- Big O décrit la croissance du temps d'exécution ou de la mémoire avec la taille de l'entrée.
- Coûts typiques :
  - O(1) : accès en temps constant (ex. accès à une hash map).
  - O(log n) : recherche binaire.
  - O(n) : parcours unique de données.
  - O(n log n) : tri efficace.
  - O(n²) : boucles imbriquées sur des entrées de taille comparable.
- Préférez un code clair et maintenable sauf si le profiling montre un goulot d'étranglement.

### Principes de débogage

- Reproduisez d'abord le bug de manière fiable.
- Réduisez le cas d'échec au minimum pour isoler la cause.
- Inspectez les logs, les entrées et les hypothèses.
- Modifiez une seule variable à la fois pendant les tests.
- Ajoutez des tests de régression pour éviter que le bug ne revienne.

### Pyramide de tests

- **Unit tests** : vérifications rapides et ciblées de petites unités de logique.
- **Integration tests** : vérifient les interactions entre modules/services.
- **End-to-end tests** : valident les parcours utilisateur dans des environnements réalistes.
- Une suite équilibrée comporte beaucoup de tests unitaires et moins de tests end-to-end lents.

### Pratiques de qualité de code

- Utilisez des noms explicites et de petites fonctions ciblées.
- Préférez les fonctions pures (moins d'effets de bord) lorsque c'est pertinent.
- Gardez des modules cohérents et des interfaces explicites.
- Utilisez des linters/formatters pour la cohérence.
- Relisez le code pour la justesse, la clarté et la sécurité.

### Bases de sécurité pour les développeurs

- Validez et assainissez les entrées externes.
- Utilisez des requêtes paramétrées pour éviter l'injection SQL.
- Stockez les mots de passe avec des algorithmes de hachage robustes (ex. Argon2, bcrypt).
- Évitez d'intégrer des secrets dans le code source.
- Appliquez le principe du moindre privilège pour les identifiants et les services.
