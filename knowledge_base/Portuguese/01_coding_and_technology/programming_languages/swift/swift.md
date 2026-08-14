---
# Metadata
title: "Swift"
description: "Comprehensive reference for the Swift programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Rápido
Swift é uma linguagem de programação compilada moderna desenvolvida pela Apple (liderada por Chris Lattner) e lançada pela primeira vez em 2014. Ela foi projetada para substituir Objective-C como linguagem principal para o desenvolvimento da plataforma Apple (iOS, macOS, watchOS, tvOS, visionOS). Swift combina o desempenho das linguagens compiladas com a expressividade das linguagens de script e enfatiza a segurança – especialmente em torno de valores nulos, gerenciamento de memória e erros de tipo.
Além das plataformas Apple, o Swift é cada vez mais usado para desenvolvimento no lado do servidor (Vapor, Hummingbird), aplicativos multiplataforma e até mesmo aprendizado de máquina (Create ML da Apple). Com a introdução do Swift no servidor e o suporte multiplataforma, o Swift está se tornando mais do que apenas uma “linguagem da Apple”.
---

## Por que o Swift é importante
- **Padrão da plataforma Apple**: a linguagem principal para desenvolvimento em iOS, macOS, watchOS, tvOS e visionOS.
- **Segurança por design**: opcionais eliminam falhas de ponteiro nulo. Os tipos de valor evitam mutações não intencionais.
- **Desempenho**: Compila para código de máquina nativo via LLVM – competitivo com C++ para muitas tarefas.
- **Sintaxe moderna**: Limpa, expressiva, com fechamentos, genéricos, programação orientada a protocolo e correspondência de padrões.
- **SwiftUI**: estrutura de UI declarativa que torna a construção de interfaces da plataforma Apple rápida e intuitiva.
- **Código aberto**: O compilador Swift e a biblioteca padrão são de código aberto; roda em Linux e Windows.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Centrado na Apple** | As melhores ferramentas e ecossistema são para plataformas Apple | Use o Vapor para o lado do servidor; o suporte multiplataforma está melhorando |
| **GUI multiplataforma limitada** | Nenhuma estrutura GUI madura para Windows/Linux | Use tecnologias web ou Flutter para plataforma cruzada |
| **Mercado de trabalho menor (fora da Apple)** | Menos funções que Java, Python ou JavaScript | As funções de desenvolvimento iOS/macOS são abundantes |
| **Evolução rápida** | Mudanças freqüentes de sintaxe entre versões podem quebrar o código | Versões Pin Swift; use o Gerenciador de Pacotes Swift |
| **Tempos de compilação** | Código genérico complexo pode ser lento para compilar | Simplifique expressões de tipo; use @inlinable criteriosamente |
---

## Fundamentos de sintaxe
### Variáveis ​​e Constantes
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

### Opcionais – Solução do Swift para Null
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

### Funções e fechamentos
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

### Protocolos e Estruturas
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

### Tratamento de erros
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

## Sintaxe e padrões avançados
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

### Correspondência avançada de padrões
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

### Wrappers de propriedades e construtores de resultados
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

## Simultaneidade e paralelismo (simultaneidade rápida)
### assíncrono/aguarda
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

### Simultaneidade Estruturada
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

## Configuração do projeto e sistema de construção
### Estrutura do Projeto (Pacote Swift)
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

### Pacote.swift
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

### Comandos essenciais
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Pipeline de CI/CD (ações do GitHub)
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

## Teste
### Estrutura XCTest
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

## Interoperabilidade
### Interoperabilidade Objective-C
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

### Interoperabilidade C
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Padrões de Projeto
### Padrão de Delegado
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

### Design Orientado a Protocolo
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

## Desempenho e otimização
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

## SwiftUI – UI declarativa
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

## Implantação
### Swift do lado do servidor
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Para produção, implante o binário compilado em um servidor Linux executando Ubuntu. Use um gerenciador de processos como o systemd para gerenciar o ciclo de vida do aplicativo.
---

## Quando usar Swift
| Cenário | Por que rápido | Melhor Alternativa |
|----------|----------|-------------------|
| Aplicativos iOS/macOS | A linguagem padrão da Apple | -- |
| Aplicativos watchOS/visionOS | Única opção | -- |
| Lado do servidor (Vapor) | Ecossistema crescente | Vá, Node.js para ecossistemas de servidores mais maduros |
| Móvel multiplataforma | Possível, mas não primário | Flutter, reagir nativo |
| Programação de sistemas | Possível (Linux) | Ferrugem, C, C++ |
| Desenvolvimento de aplicativos gerais (não Apple) | Ecossistema limitado | Python, Go, Java |
---

## Perguntas e respostas sintéticas
### Q1: O que são opcionais e por que o Swift me força a desembrulhá-los?
**R:** Um opcional (`Type?`) representa um valor que pode estar ausente — é`.some(value)`ou`.none`(nil). Swift força o desempacotamento explícito para evitar travamentos do ponteiro nulo em tempo de execução. Você pode desembrulhar com`if let`,`guard let`, forçar o desempacotamento (`!`), encadeamento opcional (`?.`) ou coalescência nula (`??`). O compilador garante que você lide com o caso nulo – isso elimina uma classe inteira de bugs.
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

### Q2: Qual é a diferença entre estruturas e classes em Swift?
**R:** Estruturas são tipos de valor (copiados na atribuição), classes são tipos de referência (compartilhados). As estruturas recebem um inicializador gratuito para membros e oferecem suporte a todos os recursos de classes, exceto herança, desinicializadores e contagem de referências. Os tipos de biblioteca padrão do Swift (`String`,`Array`,`Dictionary`) são todos estruturas. Prefira estruturas por padrão; use classes quando precisar de estado mutável compartilhado ou herança.
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

### Q3: Como funcionam os protocolos e a programação orientada a protocolos?
**R:** Os protocolos definem um modelo de métodos, propriedades e requisitos. Qualquer tipo pode estar em conformidade com um protocolo implementando seus requisitos. As extensões de protocolo fornecem implementações padrão. Genéricos restritos por protocolos fornecem polimorfismo sem a sobrecarga da herança de classe - isso é "programação orientada a protocolo".
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

### Q4: O que é`async/await`em Swift e como ele se relaciona com os atores?
**R:** O modelo de simultaneidade do Swift (5.5+) usa`async/await`para código assíncrono e`actors`para estado mutável compartilhado seguro.  As funções`async`podem ser suspensas e retomadas. `await`marca pontos de suspensão. Os atores evitam corridas de dados serializando o acesso ao seu estado mutável — o compilador impõe isso em tempo de compilação.
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

### Q5: Como funcionam os wrappers de propriedades e os construtores de resultados?
**R:** Wrappers de propriedades (`@propertyWrapper`) adicionam lógica ao armazenamento de propriedades (como`@State`no SwiftUI). Os construtores de resultados (`@resultBuilder`) permitem construir estruturas de dados usando sintaxe natural (como a hierarquia de visualização do SwiftUI). Ambas são formas de metaprogramação que reduzem o clichê.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construa um roteador com segurança de tipo
**Declaração do problema:** Crie um roteador de URL de tipo seguro para um aplicativo iOS em que cada rota tenha parâmetros associados e o compilador impeça o acesso a parâmetros que não existem para uma determinada rota.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) definições de rota com parâmetros digitados, (2) análise de URL para extrair rota + parâmetros, (3) acesso a parâmetros com segurança de tipo - o compilador garante que você leia apenas os parâmetros que existem para cada rota. Isso requer enums com valores associados.
**Etapa 2 — Identifique a abordagem:**
- Use um enum com valores associados para definir rotas.
- Cada caso carrega seus parâmetros específicos como valores digitados.
- Um analisador converte strings de URL para rotear casos de enum.
- A correspondência de padrões extrai parâmetros com segurança em tempo de compilação.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Segurança de tipo: cada caso de rota carrega exatamente os parâmetros que necessita. O compilador impede o acesso`variant`em`.userProfile`.
- Exaustividade: o`switch`deve tratar todos os casos — adicionar uma nova rota força a atualização de todos os manipuladores.
- Extensibilidade: adicione novas rotas adicionando casos enum; o compilador informa todos os lugares que precisam de atualização.
- Produção: considere o roteamento de`swift-url-routing`ou`TCA`para aplicativos maiores.
### Problema 2: Implementar um contêiner de estado reativo
**Declaração do problema:** Crie um contêiner de estado reativo simples (semelhante ao Redux/Vuex) em Swift onde as mudanças de estado são observáveis ​​e os assinantes são notificados sobre mudanças de estado específicas.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) um contêiner de estado que contenha o estado do aplicativo, (2) ações que descrevam as mudanças de estado, (3) um redutor que produza um novo estado a partir do estado atual + ação, (4) assinantes que observem as mudanças de estado. Este é o padrão de fluxo de dados unidirecional.
**Etapa 2 — Identifique a abordagem:**
- Use uma classe genérica`Store<State>`com comportamento semelhante ao `@Published`.
- Defina ações como um enum.
- Use uma função redutora`(State, Action) -> State`.
- Os assinantes recebem o novo estado por meio de encerramentos.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Fluxo unidirecional: ações → redutor → novo estado → assinantes. Fácil de raciocinar e testar.
- Segurança de thread: a fila de despacho serializa mutações de estado.
- Os assinantes obtêm o estado completo – use seletores ou verificações`Equatable`para evitar novas renderizações desnecessárias.
- Produção: use`The Composable Architecture`(TCA) da Point-Free para uma implementação de nível de produção com efeitos, testes e integração SwiftUI.
---

## Resumo
Swift é uma linguagem moderna, segura e expressiva essencial para o desenvolvimento da plataforma Apple. Sua ênfase na segurança (opcionais, tipos de valores, correspondência de padrões) evita categorias inteiras de bugs. Além das plataformas Apple, o Swift está crescendo no desenvolvimento do lado do servidor e em aplicativos multiplataforma. Para desenvolvimento iOS/macOS, Swift é a escolha certa. Para outros domínios, é uma linguagem capaz com um ecossistema menor, mas crescente.