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
# Veloce
Swift è un linguaggio di programmazione moderno e compilato sviluppato da Apple (guidato da Chris Lattner) e rilasciato per la prima volta nel 2014. È stato progettato per sostituire Objective-C come linguaggio principale per lo sviluppo della piattaforma Apple (iOS, macOS, watchOS, tvOS, visionOS). Swift combina le prestazioni dei linguaggi compilati con l'espressività dei linguaggi di scripting e enfatizza la sicurezza, in particolare riguardo ai valori nulli, alla gestione della memoria e agli errori di tipo.
Oltre alle piattaforme Apple, Swift è sempre più utilizzato per lo sviluppo lato server (Vapor, Hummingbird), applicazioni multipiattaforma e persino per l'apprendimento automatico (Crea ML di Apple). Con l'introduzione di Swift su Server e il supporto multipiattaforma, Swift sta diventando più di un semplice "linguaggio Apple".
---

## Perché Swift è importante
- **Piattaforma standard Apple**: il linguaggio principale per lo sviluppo di iOS, macOS, watchOS, tvOS e visionOS.
- **Sicurezza fin dalla progettazione**: gli optional eliminano i crash del puntatore nullo. I tipi di valore impediscono la mutazione involontaria.
- **Prestazioni**: compila in codice macchina nativo tramite LLVM: competitivo con C++ per molte attività.
- **Sintassi moderna**: pulita, espressiva, con chiusure, generici, programmazione orientata al protocollo e corrispondenza di modelli.
- **SwiftUI**: framework dell'interfaccia utente dichiarativa che rende la creazione di interfacce della piattaforma Apple veloce e intuitiva.
- **Open source**: il compilatore Swift e la libreria standard sono open source; funziona su Linux e Windows.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Incentrato sulla mela** | I migliori strumenti ed ecosistemi sono per le piattaforme Apple | Usa Vapor per lato server; il supporto multipiattaforma sta migliorando |
| **GUI multipiattaforma limitata** | Nessun framework GUI maturo per Windows/Linux | Utilizza le tecnologie web o Flutter per multipiattaforma |
| **Mercato del lavoro più piccolo (al di fuori di Apple)** | Meno ruoli di Java, Python o JavaScript | I ruoli di sviluppo iOS/macOS sono numerosi |
| **Evoluzione rapida** | Frequenti modifiche alla sintassi tra le versioni possono interrompere il codice | Versioni Pin Swift; utilizzare Swift Package Manager |
| **Tempi di compilazione** | Il codice generico complesso può essere lento da compilare | Semplificare le espressioni di tipo; usa @inlinable con giudizio |
---

## Fondamenti di sintassi
### Variabili e costanti
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

### Opzionali -- Soluzione di Swift per Null
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

### Funzioni e Chiusure
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

### Protocolli e strutture
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

### Gestione degli errori
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

## Sintassi e modelli avanzati
### Generici
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

### Corrispondenza di modelli avanzata
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

### Wrapper di proprietà e generatori di risultati
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

## Concorrenza e parallelismo (concorrenza rapida)
### asincrono/attendo
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

### Concorrenza strutturata
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

## Configurazione del progetto e sistema di creazione
### Struttura del progetto (pacchetto Swift)
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

### Pacchetto.swift
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

### Comandi essenziali
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Pipeline CI/CD (azioni GitHub)
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

## Test
### Quadro XCTest
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

## Interoperabilità
### Interoperabilità Objective-C
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

### Interoperabilità C
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Modelli di progettazione
### Modello delegato
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

### Progettazione orientata al protocollo
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

## Prestazioni e ottimizzazione
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

## SwiftUI: interfaccia utente dichiarativa
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

## Distribuzione
### Swift lato server
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Per la produzione, distribuisci il file binario compilato su un server Linux che esegue Ubuntu. Utilizza un gestore di processi come systemd per gestire il ciclo di vita dell'applicazione.
---

## Quando utilizzare Swift
| Scenario | Perché Swift | Alternativa migliore |
|----------|----------|-------------|
| App iOS/macOS | La lingua standard di Apple | -- |
| app watchOS/visionOS | Unica opzione | -- |
| Lato server (Vapor) | Ecosistema in crescita | Vai, Node.js per ecosistemi di server più maturi |
| Mobile multipiattaforma | Possibile ma non primario | Svolazza, reagisci Nativo |
| Programmazione dei sistemi | Possibile (Linux) | Ruggine, C, C++ |
| Sviluppo di applicazioni generali (non Apple) | Ecosistema limitato | Python, Go, Java |
---

## Domande e risposte sintetiche
### D1: Cosa sono gli optional e perché Swift mi obbliga a scartarli?
**R:** Un facoltativo (`Type?`) rappresenta un valore che potrebbe essere assente: è`.some(value)`o`.none`(zero). Swift forza l'unwrapping esplicito per evitare arresti anomali del puntatore null in fase di esecuzione. È possibile eseguire lo scarto con`if let`,`guard let`, forzare lo scarto (`!`), il concatenamento opzionale (`?.`) o la coalescenza nulla (`??`). Il compilatore ti assicura di gestire il caso nil: questo elimina un'intera classe di bug.
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

### Q2: Qual è la differenza tra strutture e classi in Swift?
**R:** Le strutture sono tipi di valore (copiati durante l'assegnazione), le classi sono tipi di riferimento (condivisi). Le strutture ottengono un inizializzatore membro gratuito e supportano tutte le funzionalità delle classi tranne l'ereditarietà, i deinizializzatori e il conteggio dei riferimenti. I tipi di libreria standard di Swift (`String`,`Array`,`Dictionary`) sono tutte strutture. Preferisci le strutture per impostazione predefinita; utilizzare le classi quando è necessario uno stato mutabile condiviso o un'ereditarietà.
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

### D3: Come funzionano i protocolli e la programmazione orientata ai protocolli?
**R:** I protocolli definiscono un modello di metodi, proprietà e requisiti. Qualsiasi tipo può conformarsi a un protocollo implementandone i requisiti. Le estensioni del protocollo forniscono implementazioni predefinite. I generici vincolati dai protocolli forniscono il polimorfismo senza il sovraccarico dell'ereditarietà delle classi: questa è "programmazione orientata al protocollo".
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

### D4: Cos'è`async/await`in Swift e come si collega agli attori?
**R:** Il modello di concorrenza di Swift (5.5+) utilizza`async/await`per il codice asincrono e`actors`per lo stato mutabile condiviso sicuro.  Le funzioni`async`possono essere sospese e riprese. `await`segna i punti di sospensione. Gli attori impediscono le corse dei dati serializzando l'accesso al loro stato mutabile: il compilatore lo impone in fase di compilazione.
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

### D5: Come funzionano i wrapper di proprietà e i generatori di risultati?
**R:** I wrapper di proprietà (`@propertyWrapper`) aggiungono logica all'archiviazione delle proprietà (come`@State`in SwiftUI). I generatori di risultati (`@resultBuilder`) ti consentono di creare strutture di dati utilizzando la sintassi naturale (come la gerarchia di visualizzazione di SwiftUI). Entrambe sono forme di metaprogrammazione che riducono il livello standard.
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

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: costruire un router type-safe
**Dichiarazione del problema:** crea un router URL indipendente dai tipi per un'app iOS in cui a ogni percorso sono associati parametri e il compilatore impedisce l'accesso a parametri che non esistono per un determinato percorso.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) definizioni di percorso con parametri tipizzati, (2) analisi dell'URL per estrarre percorso + parametri, (3) accesso ai parametri indipendente dal tipo: il compilatore garantisce che tu legga solo i parametri che esistono per ogni percorso. Ciò richiede enumerazioni con valori associati.
**Passaggio 2: identificare l'approccio:**
- Utilizzare un'enumerazione con valori associati per definire i percorsi.
- Ogni caso porta i suoi parametri specifici come valori digitati.
- Un parser converte le stringhe URL per instradare i casi di enumerazione.
- La corrispondenza dei modelli estrae i parametri con sicurezza in fase di compilazione.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Sicurezza del tipo: ogni caso di percorso porta esattamente i parametri di cui ha bisogno. Il compilatore impedisce l'accesso a`variant`su`.userProfile`.
- Completezza:`switch`deve gestire tutti i casi: l'aggiunta di un nuovo percorso impone l'aggiornamento di tutti i gestori.
- Estendibilità: aggiungi nuovi percorsi aggiungendo casi enum; il compilatore ti dice ovunque che necessita di aggiornamento.
- Produzione: considera il routing di`swift-url-routing`o`TCA`per app più grandi.
### Problema 2: implementare un contenitore di stato reattivo
**Dichiarazione del problema:** Crea un semplice contenitore di stati reattivi (simile a Redux/Vuex) in Swift in cui i cambiamenti di stato sono osservabili e gli abbonati ricevono una notifica di cambiamenti di stato specifici.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) un contenitore di stati che contenga lo stato dell'applicazione, (2) azioni che descrivano i cambiamenti di stato, (3) un riduttore che produca un nuovo stato dallo stato corrente + azione, (4) abbonati che osservino i cambiamenti di stato. Questo è il modello di flusso di dati unidirezionale.
**Passaggio 2: identificare l'approccio:**
- Utilizzare una classe`Store<State>`generica con comportamento simile a `@Published`.
- Definire le azioni come un'enumerazione.
- Utilizzare una funzione di riduzione`(State, Action) -> State`.
- Gli abbonati ricevono il nuovo stato tramite chiusure.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Flusso unidirezionale: azioni → riduttore → nuovo stato → abbonati. Facile ragionare e testare.
- Sicurezza del thread: la coda di invio serializza le mutazioni di stato.
- Gli abbonati ottengono lo stato completo: utilizza i selettori o i controlli`Equatable`per evitare rendering inutili.
- Produzione: utilizza`The Composable Architecture`(TCA) di Point-Free per un'implementazione di livello produttivo con effetti, test e integrazione SwiftUI.
---

## Riepilogo
Swift è un linguaggio moderno, sicuro ed espressivo essenziale per lo sviluppo della piattaforma Apple. La sua enfasi sulla sicurezza (opzionali, tipi di valore, corrispondenza di modelli) previene intere categorie di bug. Oltre alle piattaforme Apple, Swift sta crescendo nello sviluppo lato server e nelle applicazioni multipiattaforma. Per lo sviluppo iOS/macOS, Swift è la scelta chiara. Per altri domini, è un linguaggio capace con un ecosistema più piccolo ma in crescita.