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

# Szybki
Swift to nowoczesny, skompilowany język programowania opracowany przez firmę Apple (pod przewodnictwem Chrisa Lattnera) i wydany po raz pierwszy w 2014 roku. Został zaprojektowany w celu zastąpienia Objective-C jako podstawowego języka do tworzenia platform Apple (iOS, macOS, watchOS, tvOS, VisionOS). Swift łączy wydajność języków skompilowanych z ekspresją języków skryptowych i kładzie nacisk na bezpieczeństwo - szczególnie w przypadku wartości null, zarządzania pamięcią i błędów typów.
Poza platformami Apple, Swift jest coraz częściej używany do programowania po stronie serwera (Vapor, Hummingbird), aplikacji międzyplatformowych, a nawet uczenia maszynowego (Create ML firmy Apple). Wraz z wprowadzeniem Swift na serwerze i obsługą wielu platform, Swift staje się czymś więcej niż tylko „językiem Apple”.
---

## Dlaczego szybkość ma znaczenie
- **Standard platformy Apple**: Podstawowy język programowania systemów iOS, macOS, watchOS, tvOS i VisionOS.
- **Bezpieczeństwo z założenia**: Opcje eliminują awarie wskaźnika zerowego. Typy wartości zapobiegają niezamierzonym mutacjom.
- **Wydajność**: Kompiluje się do natywnego kodu maszynowego za pomocą LLVM — w wielu zadaniach konkurencyjny wobec C++.
- **Nowoczesna składnia**: Czysta, wyrazista, z domknięciami, rodzajami generycznymi, programowaniem zorientowanym na protokoły i dopasowywaniem wzorców.
- **SwiftUI**: Deklaratywny framework interfejsu użytkownika, dzięki któremu tworzenie interfejsów platformy Apple jest szybkie i intuicyjne.
- **Open source**: Kompilator Swift i biblioteka standardowa są open source; działa na Linuksie i Windowsie.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Skoncentrowany na Apple** | Najlepsze narzędzia i ekosystemy są przeznaczone dla platform Apple | Użyj Vapor po stronie serwera; poprawia się obsługa wielu platform |
| **Ograniczony wieloplatformowy graficzny interfejs użytkownika** | Brak dojrzałego frameworka GUI dla Windows/Linux | Użyj technologii internetowych lub Flutter dla wielu platform |
| **Mniejszy rynek pracy (poza Apple)** | Mniej ról niż Java, Python lub JavaScript | Role programistów iOS/macOS są liczne |
| **Szybka ewolucja** | Częste zmiany składni między wersjami mogą złamać kod | Wersje Pin Swift; użyj Menedżera pakietów Swift |
| **Czasy kompilacji** | Kompilacja złożonego kodu ogólnego może być powolna | Uprość wyrażenia typu; używaj @inlinable rozsądnie |
---

## Podstawy składni
### Zmienne i stałe
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

### Opcje — rozwiązanie Swifta dla wartości Null
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

### Funkcje i zamknięcia
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

### Protokoły i struktury
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

### Obsługa błędów
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

## Zaawansowana składnia i wzorce
### Ogólne
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

### Zaawansowane dopasowywanie wzorców
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

### Opakowania właściwości i narzędzia do tworzenia wyników
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

## Współbieżność i równoległość (szybka współbieżność)
### asynchronicznie/czekaj
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

### Współbieżność strukturalna
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

## Konfiguracja projektu i budowanie systemu
### Struktura projektu (pakiet Swift)
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

### Pakiet.swift
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

### Podstawowe polecenia
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Potok CI/CD (akcje w GitHub)
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

## Testowanie
### Struktura XCTest
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

## Interoperacyjność
### Interoperacja Objective-C
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

### Współdziałanie C
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Wzorce projektowe
### Wzorzec delegata
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

### Projekt zorientowany na protokół
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

## Wydajność i optymalizacja
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

## SwiftUI — deklaratywny interfejs użytkownika
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

## Zastosowanie
### Swift po stronie serwera
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Na potrzeby produkcyjne wdróż skompilowany plik binarny na serwerze Linux z systemem Ubuntu. Użyj menedżera procesów, takiego jak systemd, aby zarządzać cyklem życia aplikacji.
---

## Kiedy używać Swifta
| Scenariusz | Dlaczego Swift | Lepsza alternatywa |
|---------|----------|--------------------------------|
| Aplikacje na iOS/macOS | Standardowy język Apple | -- |
| aplikacje na system watchOS/visionOS | Jedyna opcja | -- |
| Po stronie serwera (Vapor) | Rosnący ekosystem | Przejdź na Node.js, aby uzyskać bardziej dojrzałe ekosystemy serwerowe |
| Wieloplatformowe urządzenia mobilne | Możliwe, ale nie podstawowe | Trzepotanie, Reaguj natywnie |
| Programowanie systemów | Możliwe (Linux) | Rdza, C, C++ |
| Ogólny programista aplikacji (inny niż Apple) | Ograniczony ekosystem | Python, Go, Java |
---

## Streszczenie
Swift to nowoczesny, bezpieczny i wyrazisty język, niezbędny do rozwoju platformy Apple. Nacisk na bezpieczeństwo (opcje, typy wartości, dopasowywanie wzorców) zapobiega powstawaniu całych kategorii błędów. Poza platformami Apple, Swift rozwija się w zakresie programowania po stronie serwera i aplikacji wieloplatformowych. W przypadku programowania na iOS/macOS Swift jest oczywistym wyborem. W przypadku innych domen jest to sprawny język z mniejszym, ale rozwijającym się ekosystemem.