<!--
---
# Metadata
title: "Swift"
description: "Comprehensive reference for the Swift programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [swift, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "26 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Rápido
Swift es un lenguaje de programación compilado moderno desarrollado por Apple (dirigido por Chris Lattner) y lanzado por primera vez en 2014. Fue diseñado para reemplazar Objective-C como lenguaje principal para el desarrollo de plataformas Apple (iOS, macOS, watchOS, tvOS, visionOS). Swift combina el rendimiento de los lenguajes compilados con la expresividad de los lenguajes de scripting y enfatiza la seguridad, particularmente en torno a los valores nulos, la gestión de la memoria y los errores tipográficos.
Más allá de las plataformas de Apple, Swift se utiliza cada vez más para el desarrollo del lado del servidor (Vapor, Hummingbird), aplicaciones multiplataforma e incluso aprendizaje automático (Create ML de Apple). Con la introducción de Swift en el servidor y el soporte multiplataforma, Swift se está convirtiendo en algo más que un "lenguaje de Apple".
---

## Por qué es importante Swift
- **Estándar de plataforma Apple**: el idioma principal para el desarrollo de iOS, macOS, watchOS, tvOS y visionOS.
- **Seguridad por diseño**: las opciones opcionales eliminan los fallos del puntero nulo. Los tipos de valores evitan mutaciones no deseadas.
- **Rendimiento**: compila en código de máquina nativo a través de LLVM, competitivo con C++ para muchas tareas.
- **Sintaxis moderna**: limpia, expresiva, con cierres, genéricos, programación orientada a protocolos y coincidencia de patrones.
- **SwiftUI**: marco de interfaz de usuario declarativo que hace que la creación de interfaces de plataforma Apple sea rápida e intuitiva.
- **Código abierto**: el compilador Swift y la biblioteca estándar son de código abierto; Se ejecuta en Linux y Windows.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Centrado en Apple** | Las mejores herramientas y ecosistemas son para plataformas Apple | Utilice Vapor para el lado del servidor; el soporte multiplataforma está mejorando |
| **GUI multiplataforma limitada** | No hay un marco GUI maduro para Windows/Linux | Utilice tecnologías web o Flutter para multiplataforma |
| **Mercado laboral más pequeño (fuera de Apple)** | Menos roles que Java, Python o JavaScript | Los roles de desarrollo de iOS/macOS son abundantes |
| **Rápida evolución** | Los cambios frecuentes de sintaxis entre versiones pueden romper el código | Versiones Pin Swift; utilizar el Administrador de paquetes Swift |
| **Tiempos de compilación** | El código genérico complejo puede tardar en compilarse | Simplificar expresiones tipográficas; utilice @inlinable con prudencia |
---

## Fundamentos de sintaxis
### Variables y constantes
```swift
// Constants (let) -- preferred by default
let name = "Alice"
let age = 30
let score = 9.5
let active = true

// Variables (var) -- when you need to change the value
var count = 0
count += 1

// Type annotations (optional -- compiler usually infers)
let greeting: String = "Hello"
let numbers: [Int] = [1, 2, 3]

// String interpolation
print("Hello, \(name)! Age: \(age), Score: \(score)")
```

### Opcionales: la solución de Swift para nulos
```swift
var nickname: String? = "Al"
nickname = nil  // That is fine -- it is optional

if let actualNickname = nickname {
    print("Nickname: \(actualNickname)")
} else {
    print("No nickname")
}

// Guard -- early exit if nil
func greet(user: String?) {
    guard let name = user else {
        print("No name provided")
        return
    }
    print("Hello, \(name)!")
}

// Nil coalescing
let displayName = nickname ?? "Anonymous"

// Optional chaining
let upperNickname = nickname?.uppercased()
```

### Funciones y Cierres
```swift
func divide(_ a: Double, by b: Double) -> (result: Double, remainder: Double)? {
    guard b != 0 else { return nil }
    return (a / b, a.truncatingRemainder(dividingBy: b))
}

if let answer = divide(10, by: 3) {
    print("Result: \(answer.result), Remainder: \(answer.remainder)")
}

// Closures
let sorted = [3, 1, 4, 1, 5].sorted { $0 < $1 }
let doubled = [1, 2, 3].map { $0 * 2 }
let evens = [1, 2, 3, 4, 5, 6].filter { $0 % 2 == 0 }
let total = [1, 2, 3, 4, 5].reduce(0, +)
```

### Protocolos y estructuras
```swift
protocol Describable {
    var description: String { get }
    func summarize() -> String
}

struct Point {
    var x: Double
    var y: Double

    func distance(to other: Point) -> Double {
        let dx = x - other.x
        let dy = y - other.y
        return (dx * dx + dy * dy).squareRoot()
    }
}

extension Point: Describable {
    var description: String { "(\(x), \(y))" }
    func summarize() -> String { "Point at \(description)" }
}

enum Shape {
    case circle(radius: Double)
    case rectangle(width: Double, height: Double)
    case triangle(base: Double, height: Double)

    func area() -> Double {
        switch self {
        case .circle(let radius): return .pi * radius * radius
        case .rectangle(let w, let h): return w * h
        case .triangle(let b, let h): return 0.5 * b * h
        }
    }
}
```

### Manejo de errores
```swift
enum NetworkError: Error {
    case invalidURL
    case noData
    case decodingFailed(String)
}

func fetchData(from url: String) throws -> Data {
    guard !url.isEmpty else { throw NetworkError.invalidURL }
    return Data()
}

do {
    let data = try fetchData(from: "https://api.example.com")
    print("Got \(data.count) bytes")
} catch NetworkError.invalidURL {
    print("Invalid URL")
} catch {
    print("Unknown error: \(error)")
}

let data = try? fetchData(from: "https://api.example.com")
```

---

## Sintaxis y patrones avanzados
### Genéricos
```swift
// Generic function
func findIndex<T: Equatable>(of value: T, in array: [T]) -> Int? {
    for (index, item) in array.enumerated() {
        if item == value { return index }
    }
    return nil
}

// Generic struct with type constraint
struct Stack<Element> {
    private var items: [Element] = []

    mutating func push(_ item: Element) { items.append(item) }
    mutating func pop() -> Element? { items.popLast() }
    var isEmpty: Bool { items.isEmpty }
    var count: Int { items.count }
}

// Protocol with associated type
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}

// Protocol extensions with default implementations
extension Container where Item: Equatable {
    func contains(_ item: Item) -> Bool {
        for i in 0..<count {
            if self[i] == item { return true }
        }
        return false
    }
}

// Opaque return types (some)
func makeAnimal() -> some Describable {
    Point(x: 1, y: 2)
}
```

### Coincidencia de patrones avanzada
```swift
// Exhaustive switch with associated values
enum NetworkResult {
    case success(Data, URLResponse)
    case redirect(Int, URL)
    case failure(Error)
}

func handle(_ result: NetworkResult) {
    switch result {
    case .success(let data, let response) where response.url != nil:
        print("Got \(data.count) bytes from \(response.url!)")
    case .success(let data, _):
        print("Got \(data.count) bytes")
    case .redirect(let code, let url) where (300...399).contains(code):
        print("Redirect to \(url)")
    case .failure(let error):
        print("Error: \(error)")
    }
}

// Pattern matching in if/while
let point = (x: 3, y: 0)
if case (_, 0) = point {
    print("Point is on the x-axis")
}

// Recursive enums with indirect
indirect enum ArithmeticExpression {
    case number(Int)
    case addition(ArithmeticExpression, ArithmeticExpression)
    case multiplication(ArithmeticExpression, ArithmeticExpression)
}

func evaluate(_ expr: ArithmeticExpression) -> Int {
    switch expr {
    case .number(let n): return n
    case .addition(let l, let r): return evaluate(l) + evaluate(r)
    case .multiplication(let l, let r): return evaluate(l) * evaluate(r)
    }
}
```

### Envoltorios de propiedades y creadores de resultados
```swift
// Property wrapper
@propertyWrapper
struct Clamped<T: Comparable> {
    var wrappedValue: T {
        didSet { wrappedValue = min(max(wrappedValue, range.lowerBound), range.upperBound) }
    }
    let range: ClosedRange<T>

    init(wrappedValue: T, _ range: ClosedRange<T>) {
        self.range = range
        self.wrappedValue = min(max(wrappedValue, range.lowerBound), range.upperBound)
    }
}

struct Player {
    @Clamped(0...100) var health: Int = 100
    @Clamped(0...999) var score: Int = 0
}

var player = Player()
player.health = 150  // Clamped to 100
player.health = -10  // Clamped to 0
```

---

## Simultaneidad y paralelismo (simultaneidad rápida)
### asíncrono/espera
```swift
// Async function
func fetchUser(id: Int) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, response) = try await URLSession.shared.data(from: url)
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw NetworkError.noData
    }
    return try JSONDecoder().decode(User.self, from: data)
}

// Calling async code
Task {
    do {
        let user = try await fetchUser(id: 42)
        print("User: \(user.name)")
    } catch {
        print("Error: \(error)")
    }
}
```

### Simultaneidad estructurada
```swift
// async let -- concurrent child tasks
func loadDashboard() async throws -> DashboardData {
    async let profile = fetchProfile()
    async let notifications = fetchNotifications()
    async let settings = fetchSettings()

    return try await DashboardData(
        profile: profile,
        notifications: notifications,
        settings: settings
    )
}

// TaskGroup -- dynamic number of child tasks
func fetchAllUsers(ids: [Int]) async throws -> [User] {
    try await withThrowingTaskGroup(of: User.self) { group in
        for id in ids {
            group.addTask { try await fetchUser(id: id) }
        }
        var users: [User] = []
        for try await user in group {
            users.append(user)
        }
        return users
    }
}

// Actors -- thread-safe reference types
actor BankAccount {
    private var balance: Double
    init(balance: Double) { self.balance = balance }

    func deposit(_ amount: Double) { balance += amount }
    func getBalance() -> Double { balance }
    func transfer(_ amount: Double, to other: BankAccount) async {
        balance -= amount
        await other.deposit(amount)
    }
}
```

---

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto (paquete Swift)
```
MyPackage/
+-- Package.swift
+-- Sources/
|   +-- MyLibrary/
|   |   +-- MyLibrary.swift
|   |   +-- Models/
|   |       +-- User.swift
|   +-- MyExecutable/
|       +-- main.swift
+-- Tests/
|   +-- MyLibraryTests/
|       +-- MyLibraryTests.swift
+-- .swift-format
```

### Paquete.swift
```swift
// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "MyPackage",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "MyLibrary", targets: ["MyLibrary"]),
        .executable(name: "MyExecutable", targets: ["MyExecutable"]),
    ],
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", from: "4.100.0"),
        .package(url: "https://github.com/apple/swift-log.git", from: "1.5.0"),
    ],
    targets: [
        .target(name: "MyLibrary", dependencies: [
            .product(name: "Logging", package: "swift-log"),
        ]),
        .executableTarget(name: "MyExecutable", dependencies: ["MyLibrary"]),
        .testTarget(name: "MyLibraryTests", dependencies: ["MyLibrary"]),
    ]
)
```

### Comandos esenciales
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Canalización de CI/CD (acciones de GitHub)
```yaml
name: Swift CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4
      - run: swift build
      - run: swift test
```

---

## Pruebas
### Marco de prueba XCT
```swift
import XCTest
@testable import MyLibrary

final class StackTests: XCTestCase {
    var stack: Stack<Int>!

    override func setUp() {
        super.setUp()
        stack = Stack<Int>()
    }

    func testPushAndPop() {
        stack.push(1)
        stack.push(2)
        XCTAssertEqual(stack.pop(), 2)
        XCTAssertEqual(stack.pop(), 1)
        XCTAssertNil(stack.pop())
    }

    func testIsEmpty() {
        XCTAssertTrue(stack.isEmpty)
        stack.push(42)
        XCTAssertFalse(stack.isEmpty)
    }
}

func testFetchUser() async throws {
    let user = try await fetchUser(id: 1)
    XCTAssertNotNil(user.name)
}
```

```bash
swift test                              # Run all tests
swift test --filter StackTests          # Specific test class
swift test --enable-code-coverage       # With coverage
```

---

## Interoperabilidad
### Interoperabilidad de Objective-C
```swift
// Swift can directly use Objective-C classes via bridging header
// Bridging-Header.h:
// #import "LegacyObjectiveCClass.h"

let legacy = LegacyObjectiveCClass()
legacy.doSomething()

// Exposing Swift to Objective-C
@objc class SwiftCalculator: NSObject {
    @objc func add(_ a: Int, _ b: Int) -> Int {
        return a + b
    }
}
```

### Interoperabilidad C
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Patrones de diseño
### Patrón de delegado
```swift
protocol DataLoaderDelegate: AnyObject {
    func didLoadData(_ data: [String])
    func didFailWithError(_ error: Error)
}

class DataLoader {
    weak var delegate: DataLoaderDelegate?

    func load() {
        DispatchQueue.global().async { [weak self] in
            let data = ["item1", "item2", "item3"]
            DispatchQueue.main.async {
                self?.delegate?.didLoadData(data)
            }
        }
    }
}
```

### Diseño orientado a protocolos
```swift
protocol Renderable {
    func render(on context: CGContext)
}

protocol Resizable {
    mutating func resize(to size: CGSize)
}

struct Button: Renderable, Resizable {
    var size: CGSize
    var title: String
    func render(on context: CGContext) { /* Draw */ }
    mutating func resize(to size: CGSize) { self.size = size }
}

extension Renderable where Self: Resizable {
    func renderWithBorder(on context: CGContext) {
        render(on: context)
    }
}
```

---

## Rendimiento y optimización
```swift
// Use value types (structs) over reference types when possible
let config = AppConfig(host: "localhost", port: 8080)

// Lazy properties for expensive initialisation
class DataManager {
    lazy var expensiveResource: Resource = {
        return Resource()
    }()
}

// Use Set for O(1) lookup
var seen = Set<String>()
```

---

## SwiftUI: interfaz de usuario declarativa
```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0
    var body: some View {
        VStack(spacing: 20) {
            Text("Count: \(count)")
                .font(.largeTitle)
            Button("Increment") { count += 1 }
                .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}
```

---

## Implementación
### Swift del lado del servidor
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Para producción, implemente el binario compilado en un servidor Linux que ejecute Ubuntu. Utilice un administrador de procesos como systemd para administrar el ciclo de vida de la aplicación.
---

## Cuándo usar Swift
| Escenario | Por qué Swift | Mejor alternativa |
|----------|----------|-------------------|
| Aplicaciones iOS/macOS | El lenguaje estándar de Apple | -- |
| aplicaciones watchOS/visionOS | Única opción | -- |
| Lado del servidor (Vapor) | Ecosistema en crecimiento | Vaya, Node.js para ecosistemas de servidores más maduros |
| Móvil multiplataforma | Posible pero no primario | Flutter, reaccionar nativo |
| Programación de sistemas | Posible (Linux) | Óxido, C, C++ |
| Desarrollo de aplicaciones generales (no Apple) | Ecosistema limitado | Python, Ir, Java |
---

## Preguntas y respuestas sintéticas
### P1: ¿Qué son las opciones y por qué Swift me obliga a desenvolverlas?
**R:** Un opcional (`Type?`) representa un valor que podría estar ausente: es`.some(value)`o`.none`(nulo). Swift fuerza el desenvolvimiento explícito para evitar fallas del puntero nulo en tiempo de ejecución. Puede desenvolver con`if let`,`guard let`, forzar desenvolver (`!`), encadenamiento opcional (`?.`) o fusión nula (`??`). El compilador garantiza que usted maneje el caso nulo; esto elimina toda una clase de errores.
```swift
// Optional declaration
var name: String? = nil
name = "Alice"

// Safe unwrapping with if let
if let unwrapped = name {
    print("Name: \(unwrapped)")
} else {
    print("Name is nil")
}

// Guard let — early exit
func greet(user: String?) {
    guard let name = user else {
        print("No user provided")
        return
    }
    print("Hello, \(name)!")
}

// Nil coalescing
let displayName = name ?? "Anonymous"

// Optional chaining
class Address { var city: String? }
class User { var address: Address? }
let user = User()
let city = user.address?.city  // String? — nil at any point
let cityOrUnknown = user.address?.city ?? "Unknown"
```

### P2: ¿Cuál es la diferencia entre estructuras y clases en Swift?
**R:** Las estructuras son tipos de valor (copiadas en la asignación), las clases son tipos de referencia (compartidas). Las estructuras obtienen un inicializador gratuito para miembros y admiten todas las características de las clases, excepto la herencia, los desinicializadores y el recuento de referencias. Los tipos de biblioteca estándar de Swift (`String`,`Array`,`Dictionary`) son todas estructuras. Prefiere estructuras por defecto; use clases cuando necesite herencia o estado mutable compartido.
```swift
// Struct — value type, copied on assignment
struct Point {
    var x: Double
    var y: Double

    mutating func move(by dx: Double, _ dy: Double) {
        x += dx
        y += dy
    }
}

var p1 = Point(x: 1, y: 2)
var p2 = p1          // Copy
p2.x = 10
print(p1.x)          // 1 — unchanged

// Class — reference type, shared
class ViewController {
    var title: String = ""
}
let vc1 = ViewController()
let vc2 = vc1        // Same reference
vc2.title = "Home"
print(vc1.title)     // "Home" — same object
```

### P3: ¿Cómo funcionan los protocolos y la programación orientada a protocolos?
**R:** Los protocolos definen un modelo de métodos, propiedades y requisitos. Cualquier tipo puede ajustarse a un protocolo implementando sus requisitos. Las extensiones de protocolo proporcionan implementaciones predeterminadas. Los genéricos restringidos por protocolos brindan polimorfismo sin la sobrecarga de la herencia de clases; esto es "programación orientada a protocolos".
```swift
// Protocol definition
protocol Drawable {
    func draw(on context: GraphicsContext)
    var bounds: CGRect { get }
}

// Default implementation via extension
extension Drawable {
    func describe() -> String {
        return "Drawable at \(bounds)"
    }
}

// Conforming types
struct Circle: Drawable {
    let center: CGPoint
    let radius: CGFloat

    func draw(on context: GraphicsContext) { /* ... */ }
    var bounds: CGRect { /* computed from center + radius */ CGRect() }
}

// Protocol as generic constraint
func renderAll<T: Drawable>(_ items: [T], on context: GraphicsContext) {
    for item in items {
        item.draw(on: context)
    }
}

// Protocol composition
func process(_ item: Drawable & Codable & Sendable) { /* ... */ }
```

### P4: ¿Qué es`async/await`en Swift y cómo se relaciona con los actores?
**R:** El modelo de concurrencia de Swift (5.5+) usa`async/await`para código asincrónico y`actors`para estado mutable compartido seguro.  Las funciones`async`se pueden suspender y reanudar. `await`marca los puntos de suspensión. Los actores evitan las carreras de datos serializando el acceso a su estado mutable; el compilador aplica esto en el momento de la compilación.
```swift
// Async function
func fetchUser(id: String) async throws -> User {
    let (data, _) = try await URLSession.shared.data(
        from: URL(string: "https://api.example.com/users/\(id)")!
    )
    return try JSONDecoder().decode(User.self, from: data)
}

// Actor — safe shared mutable state
actor BankAccount {
    private var balance: Double = 0

    func deposit(_ amount: Double) {
        balance += amount  // Only accessible within actor
    }

    func getBalance() -> Double { balance }
}

// Usage
let account = BankAccount()
await account.deposit(100)
let balance = await account.getBalance()

// Concurrent execution with async let
async let user = fetchUser(id: "1")
async let posts = fetchPosts(userId: "1")
let dashboard = try await Dashboard(user: user, posts: posts)
```

### P5: ¿Cómo funcionan los contenedores de propiedades y los creadores de resultados?
**R:** Los contenedores de propiedades (`@propertyWrapper`) agregan lógica al almacenamiento de propiedades (como`@State`en SwiftUI). Los creadores de resultados (`@resultBuilder`) le permiten crear estructuras de datos utilizando sintaxis natural (como la jerarquía de vistas de SwiftUI). Ambas son formas de metaprogramación que reducen el texto repetitivo.
```swift
// Property wrapper
@propertyWrapper
struct Clamped<T: Comparable> {
    var wrappedValue: T {
        didSet { wrappedValue = min(max(wrappedValue, range.lowerBound), range.upperBound) }
    }
    let range: ClosedRange<T>

    init(wrappedValue: T, _ range: ClosedRange<T>) {
        self.range = range
        self.wrappedValue = min(max(wrappedValue, range.lowerBound), range.upperBound)
    }
}

struct Player {
    @Clamped(0...100) var health: Int = 100
    @Clamped(0...999) var score: Int = 0
}

var player = Player()
player.health = 150  // Clamped to 100
player.health = -10  // Clamped to 0
```

---

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: construir un enrutador de tipo seguro
**Declaración del problema:** Cree un enrutador de URL con seguridad de tipos para una aplicación de iOS donde cada ruta tenga parámetros asociados y el compilador impida el acceso a parámetros que no existen para una ruta determinada.
**Paso 1: comprenda el problema:**
Necesitamos: (1) definiciones de ruta con parámetros escritos, (2) análisis de URL para extraer ruta + parámetros, (3) acceso a parámetros de tipo seguro: el compilador garantiza que solo lea los parámetros que existen para cada ruta. Esto requiere enumeraciones con valores asociados.
**Paso 2: Identifique el enfoque:**
- Utilice una enumeración con valores asociados para definir rutas.
- Cada caso lleva sus parámetros específicos como valores escritos.
- Un analizador convierte cadenas de URL para enrutar casos de enumeración.
- La coincidencia de patrones extrae parámetros con seguridad en tiempo de compilación.
**Paso 3: Implementar la solución:**
```swift
enum Route: Equatable {
    case home
    case userProfile(id: String)
    case productDetail(id: String, variant: String?)
    case search(query: String, page: Int)
    case settings(section: SettingsSection)

    enum SettingsSection: String {
        case general, notifications, privacy, about
    }

    // Parse URL to route
    static func from(url: URL) -> Route? {
        let path = url.pathComponents.dropFirst()  // Remove leading /
        let query = URLComponents(url: url, resolvingAgainstBaseURL: false)?
            .queryItems ?? []

        switch path {
        case []:
            return .home
        case ["users", let id]:
            return .userProfile(id: id)
        case ["products", let id]:
            let variant = query.first(where: { $0.name == "variant" })?.value
            return .productDetail(id: id, variant: variant)
        case ["search"]:
            guard let q = query.first(where: { $0.name == "q" })?.value else { return nil }
            let page = query.first(where: { $0.name == "page" })
                .flatMap { Int($0.value ?? "1") } ?? 1
            return .search(query: q, page: page)
        case ["settings", let section]:
            guard let s = SettingsSection(rawValue: section) else { return nil }
            return .settings(section: s)
        default:
            return nil
        }
    }
}

// Usage — type-safe parameter extraction
func handle(route: Route) {
    switch route {
    case .home:
        showHomeScreen()
    case .userProfile(let id):
        showProfile(userId: id)  // id is guaranteed String
    case .productDetail(let id, let variant):
        showProduct(id: id, variant: variant)  // variant is String?
    case .search(let query, let page):
        performSearch(query: query, page: page)  // page is guaranteed Int
    case .settings(let section):
        showSettings(section: section)  // section is SettingsSection enum
    }
}

// Handle deep link
if let url = URL(string: "myapp://products/abc123?variant=blue"),
   let route = Route.from(url: url) {
    handle(route: route)
}
```

**Paso 4: Verificar y optimizar:**
- Seguridad de tipo: cada caso de ruta lleva exactamente los parámetros que necesita. El compilador impide el acceso a`variant`en `.userProfile`.
- Exhaustividad: el`switch`debe manejar todos los casos; agregar una nueva ruta obliga a actualizar todos los controladores.
- Extensibilidad: agregue nuevas rutas agregando casos de enumeración; el compilador le indica todos los lugares que necesitan actualización.
- Producción: considere el enrutamiento`swift-url-routing`o`TCA`para aplicaciones más grandes.
### Problema 2: implementar un contenedor de estado reactivo
**Declaración del problema:** Cree un contenedor de estado reactivo simple (similar a Redux/Vuex) en Swift donde los cambios de estado sean observables y los suscriptores sean notificados de cambios de estado específicos.
**Paso 1: comprenda el problema:**
Necesitamos: (1) un contenedor de estado que contenga el estado de la aplicación, (2) acciones que describan los cambios de estado, (3) un reductor que produzca un nuevo estado a partir del estado actual + acción, (4) suscriptores que observen los cambios de estado. Este es el patrón de flujo de datos unidireccional.
**Paso 2: Identifique el enfoque:**
- Utilice una clase`Store<State>`genérica con un comportamiento similar al de `@Published`.
- Definir acciones como una enumeración.
- Utilizar una función reductora `(State, Action) -> State`.
- Los suscriptores reciben el nuevo estado mediante cierres.
**Paso 3: Implementar la solución:**
```swift
// Action protocol
protocol Action {}

// Store — holds state and dispatches actions
class Store<State> {
    private(set) var state: State
    private let reducer: (State, Action) -> State
    private var subscribers: [(State) -> Void] = []
    private let queue = DispatchQueue(label: "store.queue")

    init(initialState: State, reducer: @escaping (State, Action) -> State) {
        self.state = initialState
        self.reducer = reducer
    }

    func dispatch(_ action: Action) {
        queue.async { [weak self] in
            guard let self else { return }
            let newState = self.reducer(self.state, action)
            self.state = newState
            self.notifySubscribers(newState)
        }
    }

    func subscribe(_ callback: @escaping (State) -> Void) -> () -> Void {
        subscribers.append(callback)
        callback(state)  // Emit current state immediately

        // Return unsubscribe function
        let index = subscribers.count - 1
        return { [weak self] in
            self?.subscribers.remove(at: index)
        }
    }

    private func notifySubscribers(_ state: State) {
        for subscriber in subscribers {
            subscriber(state)
        }
    }
}

// Example usage
struct AppState {
    var todos: [Todo] = []
    var filter: TodoFilter = .all
    var isLoading: Bool = false
}

enum TodoAction: Action {
    case addTodo(String)
    case toggleTodo(Int)
    case setFilter(TodoFilter)
    case setLoading(Bool)
}

enum TodoFilter { case all, active, completed }

struct Todo: Equatable {
    let id: Int
    let title: String
    var isDone: Bool = false
}

// Reducer
func todoReducer(state: AppState, action: Action) -> AppState {
    var newState = state
    guard let action = action as? TodoAction else { return state }

    switch action {
    case .addTodo(let title):
        let id = (state.todos.map(\.id).max() ?? 0) + 1
        newState.todos.append(Todo(id: id, title: title))
    case .toggleTodo(let id):
        if let idx = newState.todos.firstIndex(where: { $0.id == id }) {
            newState.todos[idx].isDone.toggle()
        }
    case .setFilter(let filter):
        newState.filter = filter
    case .setLoading(let loading):
        newState.isLoading = loading
    }
    return newState
}

// Wire it up
let store = Store(initialState: AppState(), reducer: todoReducer)

let unsubscribe = store.subscribe { state in
    print("Todos: \(state.todos.count), Filter: \(state.filter)")
}

store.dispatch(TodoAction.addTodo("Learn Swift"))
store.dispatch(TodoAction.addTodo("Build an app"))
store.dispatch(TodoAction.toggleTodo(1))
store.dispatch(TodoAction.setFilter(.active))
```

**Paso 4: Verificar y optimizar:**
- Flujo unidireccional: acciones → reductor → nuevo estado → suscriptores. Fácil de razonar y probar.
- Seguridad de subprocesos: la cola de despacho serializa las mutaciones de estado.
- Los suscriptores obtienen el estado completo: utilice selectores o comprobaciones`Equatable`para evitar reproducciones innecesarias.
- Producción: utilice`The Composable Architecture`(TCA) de Point-Free para una implementación de nivel de producción con efectos, pruebas e integración con SwiftUI.
---

## Resumen
Swift es un lenguaje moderno, seguro y expresivo esencial para el desarrollo de la plataforma Apple. Su énfasis en la seguridad (opcionales, tipos de valores, coincidencia de patrones) evita categorías enteras de errores. Más allá de las plataformas de Apple, Swift está creciendo en el desarrollo del lado del servidor y en aplicaciones multiplataforma. Para el desarrollo de iOS/macOS, Swift es la opción clara. Para otros dominios, es un lenguaje capaz con un ecosistema más pequeño pero en crecimiento.