# Linguagens de Programação

## Python

Python é uma linguagem de programação de alto nível, interpretada, de tipagem dinâmica e de propósito geral. Ela enfatiza a legibilidade e usa indentação significativa como delimitador de blocos.

### Sintaxe básica

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

### Funções e type hints

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### List comprehensions

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes e OOP

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

### Padrões comuns

- Use `with open(path) as f:` para I/O de arquivos.
- Prefira f-strings (`f"hello {name}"`) em vez de `%` ou `.format()`.
- Use `dataclasses.dataclass` para classes apenas de dados.
- Use `pathlib.Path` em vez de `os.path` para caminhos de arquivos.

### Ferramentas

- `pip install <package>` instala pacotes.
- `python -m venv .venv && source .venv/bin/activate` cria um ambiente virtual.
- `pip freeze > requirements.txt` salva dependências.
- `pip install -r requirements.txt` as restaura.
- `pyproject.toml` é o padrão moderno de configuração de projetos.

---

## JavaScript

JavaScript é a principal linguagem da web. Ele roda em navegadores e em servidores via Node.js. Tem tipagem dinâmica e é baseado em protótipos.

### Sintaxe moderna (ES6+)

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

### Programação assíncrona

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

### Métodos de array

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Manipulação do DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Ferramentas

- `npm init -y` inicializa um projeto.
- `npm install <package>` adiciona uma dependência.
- `npm run <script>` executa um script definido em `package.json`.
- `node index.js` executa um script com Node.js.

---

## TypeScript

TypeScript é um superconjunto do JavaScript com tipagem estática que compila para JavaScript puro. Ele adiciona anotações de tipo, interfaces, generics e enums.

### Anotações de tipo

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces e types

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

### Classes com modificadores de acesso

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

### Itens essenciais do tsconfig.json

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

### Ferramentas

- `npm install -g typescript` instala o compilador.
- `tsc` compila o projeto.
- `ts-node src/index.ts` executa TypeScript diretamente.

---

## Rust

Rust é uma linguagem de programação de sistemas focada em segurança, velocidade e concorrência. Ela evita bugs de segurança de memória em tempo de compilação por meio de seu sistema de ownership.

### Ownership e borrowing

Todo valor em Rust tem exatamente um owner. Quando o owner sai de escopo, o valor é descartado. Borrowing permite referências sem transferir ownership.

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

Mutable borrows (`&mut T`) exigem que não existam outros borrows ao mesmo tempo.

### Lifetimes

Lifetimes garantem que as referências não sobrevivam além dos dados para os quais apontam.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enums e pattern matching

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

### Tratamento de erros

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

O operador `?` propaga erros automaticamente dentro de funções que retornam `Result`.

### Ferramentas (Cargo)

- `cargo new project_name` cria um novo projeto.
- `cargo build` compila.
- `cargo run` compila e executa.
- `cargo test` executa testes.
- `cargo add <crate>` adiciona uma dependência ao `Cargo.toml`.
- `cargo fmt` formata código. `cargo clippy` faz lint.

---

## Go

Go (Golang) é uma linguagem compilada e estaticamente tipada, projetada para simplicidade e programas concorrentes de alto desempenho.

### Fundamentos

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### Funções e múltiplos valores de retorno

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

Qualquer tipo que implemente todos os métodos de uma interface a satisfaz — não é necessária declaração explícita.

### Goroutines e channels

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

### Ferramentas

- `go mod init module/name` inicializa um módulo.
- `go get ./...` baixa dependências.
- `go build ./...` compila.
- `go test ./...` executa testes.
- `go fmt ./...` formata.
- `go vet ./...` verifica erros comuns.

---

## C e C++

C é uma linguagem de baixo nível, compilada e procedural. C++ amplia C com classes, templates e a Standard Template Library (STL).

### Fundamentos de C

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

### Ponteiros

Um ponteiro armazena o endereço de memória de outra variável. `*ptr` faz a desreferenciação; `&var` obtém o endereço.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### Classes em C++ e RAII

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

RAII (Resource Acquisition Is Initialization) vincula o ciclo de vida de recursos ao ciclo de vida de objetos, garantindo que a limpeza aconteça automaticamente nos destrutores.

### Containers da STL

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

### Destaques do C++ moderno (C++17 / C++20)

- Dedução de tipo com `auto`.
- Loops `for` baseados em intervalo: `for (auto& item : container)`.
- Smart pointers: `std::unique_ptr`, `std::shared_ptr` — evite `new`/`delete` brutos.
- Structured bindings: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilação

- `gcc main.c -o main` compila C.
- `g++ -std=c++20 -Wall main.cpp -o main` compila C++.
- `make` automatiza builds com vários arquivos por meio de um `Makefile`.
- `cmake` é o gerador de sistema de build padrão para projetos maiores.

---

## Swift

Swift é uma linguagem de programação moderna, estaticamente tipada, desenvolvida pela Apple para iOS, macOS, watchOS e tvOS. Também está disponível no Linux.

### Fundamentos

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Optionals

Um optional (`T?`) representa um valor que pode ou não estar presente.

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

### Funções e closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Classes e structs

Swift tem classes (tipos por referência) e structs (tipos por valor). Prefira structs para modelos de dados simples.

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

### Codable (codificação / decodificação JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Fundamentos de SwiftUI

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

### Ferramentas

- `swift build` compila um projeto Swift Package Manager.
- `swift run` executa o projeto.
- `swift test` executa testes.
- `swift package init --type executable` cria um novo projeto executável.
- Xcode é a IDE principal para desenvolvimento nas plataformas Apple.

---

## Fundamentos de Programação (Independentes de Linguagem)

### Fluxo de resolução de problemas

1. Defina a entrada, a saída e as restrições antes de escrever código.
2. Divida a tarefa em subproblemas menores.
3. Comece com uma solução simples e correta; depois otimize, se necessário.
4. Valide com testes, edge cases e entradas realistas.

### Estruturas de dados fundamentais

- **Array / List**: coleção ordenada com leitura indexada rápida.
- **Hash map / Dictionary**: armazenamento chave-valor com busca média O(1).
- **Set**: valores únicos, útil para verificações de pertencimento.
- **Stack**: LIFO (last in, first out), comum em parsing e recursão.
- **Queue**: FIFO (first in, first out), útil para agendamento e BFS.
- **Tree / Graph**: relacionamentos hierárquicos e em forma de rede.

### Complexidade algorítmica (Big O)

- Big O descreve como o tempo de execução ou o uso de memória cresce com o tamanho da entrada.
- Custos típicos:
  - O(1): busca em tempo constante (por exemplo, acesso a hash map).
  - O(log n): busca binária.
  - O(n): passagem única pelos dados.
  - O(n log n): ordenação eficiente.
  - O(n²): loops aninhados sobre entradas de tamanho semelhante.
- Prefira código claro e fácil de manter, a menos que o profiling mostre um gargalo.

### Princípios de debugging

- Reproduza o bug de forma confiável primeiro.
- Minimize o caso com falha para isolar a causa.
- Inspecione logs, entradas e premissas.
- Altere uma variável por vez durante os testes.
- Adicione testes de regressão para que o mesmo bug não volte.

### Pirâmide de testes

- **Unit tests**: verificações rápidas e focadas de pequenas unidades de lógica.
- **Integration tests**: verificam interações entre módulos/serviços.
- **End-to-end tests**: validam fluxos de usuário em ambientes realistas.
- Uma suíte equilibrada tem muitos testes unitários e menos testes end-to-end lentos.

### Práticas de qualidade de código

- Use nomes significativos e funções pequenas e focadas.
- Prefira funções puras (menos efeitos colaterais) quando for prático.
- Mantenha módulos coesos e interfaces explícitas.
- Use linters/formatters para consistência.
- Revise o código quanto à correção, clareza e segurança.

### Noções básicas de segurança para desenvolvedores

- Valide e sanitize entradas externas.
- Use consultas parametrizadas para evitar SQL injection.
- Armazene senhas com algoritmos fortes de hashing (por exemplo, Argon2, bcrypt).
- Evite incorporar segredos no código-fonte.
- Aplique o princípio do menor privilégio a credenciais e serviços.
