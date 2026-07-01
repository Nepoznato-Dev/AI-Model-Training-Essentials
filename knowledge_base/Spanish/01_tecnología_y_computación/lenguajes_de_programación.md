<!-- 
Este archivo fue traducido del inglés al español.
Fuente: coding_languages.md
Nota: Los términos técnicos, ejemplos de código y nombres propios pueden permanecer en inglés.
Para mejoras de precisión, por favor contribuya con ediciones mediante pull requests.
-->

# Lenguajes de Programación

## Python

Python es un lenguaje de programación de alto nivel, interpretado, dinámicamente tipado y de propósito general. Enfatiza la legibilidad y usa la indentación significativa como delimitadores de bloque.

### Sintaxis básica

```python
# Variables y tipos
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Condicionales
if age >= 18:
    print("adulto")
elif age >= 13:
    print("adolescente")
else:
    print("niño")

# Bucles
for i in range(5):
    print(i)

while active:
    active = False
```

### Funciones y anotaciones de tipo

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### Comprensión de listas

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Clases y Programación Orientada a Objetos

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} dice guau"
```

### Patrones comunes

- Usa `with open(path) as f:` para E/S de archivos.
- Prefiere f-strings (`f"hola {name}"`) sobre `%` o `.format()`.
- Usa `dataclasses.dataclass` para clases que solo contienen datos.
- Usa `pathlib.Path` en lugar de `os.path` para rutas de archivos.

### Herramientas

- `pip install <package>` instala paquetes.
- `python -m venv .venv && source .venv/bin/activate` crea un entorno virtual.
- `pip freeze > requirements.txt` guarda las dependencias.
- `pip install -r requirements.txt` las restaura.
- `pyproject.toml` es el estándar moderno de configuración de proyectos.

---

## JavaScript

JavaScript es el lenguaje principal de la web. Se ejecuta en navegadores y en servidores mediante Node.js. Es dinámicamente tipado y basado en prototipos.

### Sintaxis moderna (ES6+)

```javascript
// Declaraciones de variables
const PI = 3.14159;
let counter = 0;

// Funciones flecha
const add = (a, b) => a + b;

// Plantillas literales
const greet = name => `Hello, ${name}!`;

// Desestructuración
const { x, y } = point;
const [first, ...rest] = array;

// Spread
const merged = { ...defaults, ...overrides };
```

### Programación asíncrona

```javascript
// Promesas
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

### Métodos de arrays

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### Manipulación del DOM

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### Herramientas

- `npm init -y` inicializa un proyecto.
- `npm install <package>` añade una dependencia.
- `npm run <script>` ejecuta un script definido en `package.json`.
- `node index.js` ejecuta un script con Node.js.

---

## TypeScript

TypeScript es un superconjunto estáticamente tipado de JavaScript que compila a JavaScript puro. Añade anotaciones de tipo, interfaces, genéricos y enumerados.

### Anotaciones de tipo

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### Interfaces y tipos

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // propiedad opcional
}

type Status = "active" | "inactive" | "banned";
```

### Genéricos

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### Clases con modificadores de acceso

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

### Esenciales de tsconfig.json

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

### Herramientas

- `npm install -g typescript` instala el compilador.
- `tsc` compila el proyecto.
- `ts-node src/index.ts` ejecuta TypeScript directamente.

---

## Rust

Rust es un lenguaje de programación de sistemas enfocado en seguridad, velocidad y concurrencia. Previene errores de seguridad de memoria en tiempo de compilación mediante su sistema de propiedad.

### Propiedad y préstamo

Cada valor en Rust tiene exactamente un propietario. Cuando el propietario sale del ámbito, el valor se elimina. El préstamo permite referencias sin transferir la propiedad.

```rust
fn main() {
    let s = String::from("hello");  // s posee el string
    let len = calculate_length(&s); // toma prestado s
    println!("{} tiene longitud {}", s, len); // s sigue siendo válido
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Los préstamos mutables (`&mut T`) requieren que no existan otros préstamos al mismo tiempo.

### Tiempos de vida

Los tiempos de vida aseguran que las referencias no sobrevivan más que los datos a los que apuntan.

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Enumerados y coincidencia de patrones

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

### Manejo de errores

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

El operador `?` propaga errores automáticamente dentro de funciones que devuelven `Result`.

### Herramientas (Cargo)

- `cargo new project_name` crea un nuevo proyecto.
- `cargo build` compila.
- `cargo run` compila y ejecuta.
- `cargo test` ejecuta pruebas.
- `cargo add <crate>` añade una dependencia a `Cargo.toml`.
- `cargo fmt` formatea el código. `cargo clippy` realiza análisis estático.

---

## Go

Go (Golang) es un lenguaje compilado y estáticamente tipado diseñado para simplicidad y programas concurrentes de alto rendimiento.

### Conceptos básicos

```go
package main

import "fmt"

func main() {
    name := "world"          // declaración corta de variable
    fmt.Printf("Hello, %s!\n", name)
}
```

### Funciones y valores de retorno múltiples

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("división por cero")
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

func (d Dog) Speak() string { return d.Name + " dice guau" }
```

Cualquier tipo que implemente todos los métodos de una interfaz la satisface — no se necesita declaración explícita.

### Goroutines y channels

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
    defer f.Close()   // se ejecuta cuando la función retorna
    // … procesar f …
    return nil
}
```

### Herramientas

- `go mod init module/name` inicializa un módulo.
- `go get ./...` descarga dependencias.
- `go build ./...` compila.
- `go test ./...` ejecuta pruebas.
- `go fmt ./...` formatea el código.
- `go vet ./...` verifica errores comunes.

---

## C y C++

C es un lenguaje procedural, compilado y de bajo nivel. C++ extiende C con clases, plantillas y la Biblioteca Estándar de Plantillas (STL).

### Conceptos básicos de C

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* Memoria dinámica */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* siempre libera lo que asignaste con malloc */

    return 0;
}
```

### Punteros

Un puntero almacena la dirección de memoria de otra variable. `*ptr` desreferencia; `&var` obtiene una dirección.

```c
int a = 10;
int *p = &a;
*p = 20;   /* a ahora es 20 */
```

### Clases de C++ y RAII

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

RAII (Resource Acquisition Is Initialization / Adquisición de Recursos es Inicialización) vincula los tiempos de vida de los recursos a los tiempos de vida de los objetos, asegurando que la limpieza ocurra automáticamente en los destructores.

### Contenedores STL

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

### Aspectos destacados de C++ moderno (C++17 / C++20)

- Deducción de tipo `auto`.
- Bucles `for` basados en rango: `for (auto& item : container)`.
- Punteros inteligentes: `std::unique_ptr`, `std::shared_ptr` — evita `new`/`delete` crudos.
- Enlazados estructurados: `auto [key, val] = pair;`.
- `std::optional`, `std::variant`, `std::string_view`.

### Compilación

- `gcc main.c -o main` compila C.
- `g++ -std=c++20 -Wall main.cpp -o main` compila C++.
- `make` automatiza construcciones de múltiples archivos mediante un `Makefile`.
- `cmake` es el generador de sistemas de construcción estándar para proyectos grandes.

---

## Swift

Swift es un lenguaje de programación moderno y estáticamente tipado desarrollado por Apple para iOS, macOS, watchOS y tvOS. También está disponible en Linux.

### Conceptos básicos

```swift
let greeting = "Hello, world!"   // constante (inmutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### Opcionales

Un opcional (`T?`) representa un valor que puede o no estar presente.

```swift
var name: String? = nil
name = "Alice"

// Desempaquetado seguro
if let n = name {
    print("Hello, \(n)")
}

// Nil-coalescing
let display = name ?? "Guest"

// Encadenamiento opcional
let length = name?.count
```

### Funciones y closures

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### Clases y structs

Swift tiene tanto clases (tipos de referencia) como structs (tipos de valor). Prefiere structs para modelos de datos simples.

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

### Protocolos

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable (codificación / decodificación JSON)

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### Conceptos básicos de SwiftUI

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

### Herramientas

- `swift build` compila un proyecto de Swift Package Manager.
- `swift run` ejecuta el proyecto.
- `swift test` ejecuta pruebas.
- `swift package init --type executable` crea un nuevo proyecto ejecutable.
- Xcode es el IDE principal para desarrollo en plataformas Apple.

---

## Fundamentos de Programación (Independiente del Lenguaje)

### Flujo de trabajo para resolución de problemas

1. Define la entrada, salida y restricciones antes de escribir código.
2. Divide la tarea en subproblemas más pequeños.
3. Comienza con una solución simple y correcta, luego optimiza si es necesario.
4. Valida con pruebas, casos límite y entradas realistas.

### Estructuras de datos fundamentales

- **Array / Lista**: colección ordenada con lecturas indexadas rápidas.
- **Hash map / Diccionario**: almacén clave-valor con búsqueda promedio O(1).
- **Set**: valores únicos, útil para verificaciones de pertenencia.
- **Pila (Stack)**: LIFO (último en entrar, primero en salir), común en análisis sintáctico y recursión.
- **Cola (Queue)**: FIFO (primero en entrar, primero en salir), útil para planificación y BFS.
- **Árbol / Grafo**: relaciones jerárquicas y de estilo red.

### Complejidad algorítmica (Big O)

- Big O describe cómo crece el tiempo de ejecución o la memoria con el tamaño de la entrada.
- Costos típicos:
  - O(1): acceso en tiempo constante (ej. acceso a hash map).
  - O(log n): búsqueda binaria.
  - O(n): paso único a través de los datos.
  - O(n log n): ordenamiento eficiente.
  - O(n²): bucles anidados sobre entradas de tamaño similar.
- Prefiere código claro y mantenible a menos que el profiling muestre un cuello de botella.

### Principios de depuración

- Reproduce el error de manera confiable primero.
- Minimiza el caso fallido para aislar la causa.
- Inspecciona registros, entradas y suposiciones.
- Cambia una variable a la vez mientras pruebas.
- Añade pruebas de regresión para que el mismo error no vuelva.

### Pirámide de pruebas

- **Pruebas unitarias**: verificaciones rápidas y enfocadas de pequeñas unidades lógicas.
- **Pruebas de integración**: verifican interacciones entre módulos/servicios.
- **Pruebas end-to-end**: validan flujos de usuario en entornos realistas.
- Un conjunto equilibrado tiene muchas pruebas unitarias y menos pruebas end-to-end lentas.

### Prácticas de calidad de código

- Usa nombres significativos y funciones pequeñas y enfocadas.
- Prefiere funciones puras (menos efectos secundarios) cuando sea práctico.
- Mantén módulos cohesivos e interfaces explícitas.
- Usa linters/formateadores para consistencia.
- Revisa el código para corrección, claridad y seguridad.

### Conceptos básicos de seguridad para desarrolladores

- Valida y sanitiza la entrada externa.
- Usa consultas parametrizadas para prevenir inyección SQL.
- Almacena contraseñas con algoritmos de hashing fuertes (ej. Argon2, bcrypt).
- Evita incrustar secretos en el código fuente.
- Aplica el principio de menor privilegio para credenciales y servicios.
