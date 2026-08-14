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
# Быстрый
Swift — это современный компилируемый язык программирования, разработанный Apple (под руководством Криса Латтнера) и впервые выпущенный в 2014 году. Он был разработан для замены Objective-C в качестве основного языка разработки платформ Apple (iOS, macOS, watchOS, tvOS, VisionOS). Swift сочетает в себе производительность скомпилированных языков с выразительностью языков сценариев и уделяет особое внимание безопасности — особенно в отношении нулевых значений, управления памятью и ошибок типов.
Помимо платформ Apple, Swift все чаще используется для разработки на стороне сервера (Vapor, Hummingbird), кроссплатформенных приложений и даже машинного обучения (Apple Create ML). С появлением Swift on Server и кроссплатформенной поддержки Swift становится больше, чем просто «языком Apple».
---

## Почему Swift важен
- **Стандарт платформы Apple**: основной язык разработки для iOS, macOS, watchOS, tvOS и VisionOS.
- **Продуманная безопасность**: дополнительные возможности исключают сбои при нулевом указателе. Типы значений предотвращают непреднамеренную мутацию.
- **Производительность**: компилируется в машинный код через LLVM, что позволяет конкурировать с C++ во многих задачах.
- **Современный синтаксис**: чистый, выразительный, с замыканиями, обобщениями, протокольно-ориентированным программированием и сопоставлением шаблонов.
- **SwiftUI**: декларативная среда пользовательского интерфейса, которая делает создание интерфейсов платформы Apple быстрым и интуитивно понятным.
- **Открытый исходный код**: компилятор Swift и стандартная библиотека имеют открытый исходный код; работает на Linux и Windows.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Ориентация на яблоки** | Лучшие инструменты и экосистема предназначены для платформ Apple | Используйте Vapor для серверной части; кроссплатформенная поддержка улучшается |
| **Ограниченный кроссплатформенный графический интерфейс** | Нет развитой инфраструктуры графического интерфейса для Windows/Linux | Используйте веб-технологии или Flutter для кроссплатформенности |
| **Меньший рынок труда (за пределами Apple)** | Меньше ролей, чем в Java, Python или JavaScript | Ролей разработчиков iOS/macOS множество |
| **Быстрая эволюция** | Частые изменения синтаксиса между версиями могут привести к поломке кода | Pin-версии Swift; использовать диспетчер пакетов Swift |
| **Время компиляции** | Сложный универсальный код может компилироваться медленно | Упрощение выражений типов; используйте @inlinable разумно |
---

## Основы синтаксиса
### Переменные и константы
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

### Опциональные возможности — решение Swift для нуля
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

### Функции и замыкания
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

### Протоколы и структуры
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

### Обработка ошибок
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

## Расширенный синтаксис и шаблоны
### Дженерики
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

### Расширенное сопоставление с образцом
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

### Обертки свойств и построители результатов
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

## Параллелизм и параллелизм (быстрый параллелизм)
### асинхронный/ожидание
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

### Структурированный параллелизм
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

## Конфигурация проекта и система сборки
### Структура проекта (Swift Package)
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

### Пакет.swift
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

### Основные команды
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Конвейер CI/CD (действия GitHub)
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

## Тестирование
### Платформа XCTest
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

## Совместимость
### Взаимодействие с Objective-C
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

### Взаимодействие с C
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Шаблоны проектирования
### Шаблон делегата
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

### Протокольно-ориентированный дизайн
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

## Производительность и оптимизация
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

## SwiftUI — Декларативный пользовательский интерфейс
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

## Развертывание
### Swift на стороне сервера
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Для производства разверните скомпилированный двоичный файл на Linux-сервере под управлением Ubuntu. Используйте диспетчер процессов, например systemd, для управления жизненным циклом приложения.
---

## Когда использовать Swift
| Сценарий | Почему Свифт | Лучшая альтернатива |
|----------|----------|-------------------|
| Приложения для iOS/macOS | Стандартный язык Apple | -- |
| Приложения watchOS/visionOS | Единственный вариант | -- |
| Серверная часть (Vapor) | Растущая экосистема | Вперёд, Node.js для более зрелых серверных экосистем |
| Кроссплатформенный мобильный | Возможно, но не первично | Флаттер, React Native |
| Системное программирование | Возможно (Linux) | Руст, Си, С++ |
| Общая разработка приложений (не Apple) | Ограниченная экосистема | Питон, Го, Java |
---

## Синтетические вопросы и ответы
### Вопрос 1. Что такое опциональные параметры и почему Swift заставляет меня их разворачивать?
**A:** Необязательный параметр (`Type?`) представляет значение, которое может отсутствовать — это либо `.some(value)`, либо`.none`(ноль). Swift принудительно выполняет явную развертку, чтобы предотвратить сбои нулевого указателя во время выполнения. Вы можете выполнить развертывание с помощью `if let`, `guard let`, принудительного развертывания (`!`), дополнительного объединения (`?.`) или нулевого объединения (`??`). Компилятор гарантирует, что вы обработаете нулевой случай — это устраняет целый класс ошибок.
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

### Вопрос 2: В чем разница между структурами и классами в Swift?
**A:** Структуры — это типы значений (копируются при присвоении), классы — это ссылочные типы (общие). Структуры получают бесплатный почленный инициализатор и поддерживают все функции классов, кроме наследования, деинициализаторов и подсчета ссылок. Все типы стандартной библиотеки Swift (`String`,`Array`,`Dictionary`) являются структурами. Предпочитать структуры по умолчанию; используйте классы, когда вам нужно общее изменяемое состояние или наследование.
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

### Вопрос 3: Как работают протоколы и протоколо-ориентированное программирование?
**О:** Протоколы определяют схему методов, свойств и требований. Любой тип может соответствовать протоколу, реализуя его требования. Расширения протокола предоставляют реализации по умолчанию. Обобщенные шаблоны, ограниченные протоколами, дают вам полиморфизм без накладных расходов на наследование классов — это «протокольно-ориентированное программирование».
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

### Q4: Что такое`async/await`в Swift и как он связан с актерами?
**A:** Модель параллелизма Swift (5.5+) использует`async/await`для асинхронного кода и`actors`для безопасного общего изменяемого состояния.  Функции`async`можно приостанавливать и возобновлять. `await`отмечает точки подвески. Актеры предотвращают гонки данных путем сериализации доступа к их изменяемому состоянию — компилятор обеспечивает это во время компиляции.
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

### Вопрос 5. Как работают оболочки свойств и построители результатов?
**A:** Обертки свойств (`@propertyWrapper`) добавляют логику к хранилищу свойств (например,`@State`в SwiftUI). Построители результатов (`@resultBuilder`) позволяют создавать структуры данных, используя естественный синтаксис (например, иерархию представлений SwiftUI). Оба являются формами метапрограммирования, которые сокращают шаблонность.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создайте типобезопасный маршрутизатор
**Постановка задачи.** Создайте типобезопасный URL-маршрутизатор для приложения iOS, в котором каждый маршрут имеет связанные параметры, а компилятор предотвращает доступ к параметрам, которые не существуют для данного маршрута.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) определения маршрутов с типизированными параметрами, (2) анализ URL-адресов для извлечения маршрута и параметров, (3) типобезопасный доступ к параметрам — компилятор гарантирует, что вы читаете только те параметры, которые существуют для каждого маршрута. Для этого требуются перечисления со связанными значениями.
**Шаг 2. Определите подход:**
- Используйте перечисление со связанными значениями для определения маршрутов.
- Каждый случай содержит свои конкретные параметры в виде типизированных значений.
— Анализатор преобразует строки URL-адресов в случаи перечисления маршрутов.
- Сопоставление с образцом извлекает параметры с безопасностью во время компиляции.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Типовая безопасность: каждый случай маршрута несет именно те параметры, которые ему необходимы. Компилятор предотвращает доступ к`variant`на `.userProfile`.
— Полнота:`switch`должен обрабатывать все случаи — добавление нового маршрута приводит к обновлению всех обработчиков.
- Расширяемость: добавляйте новые маршруты путем добавления случаев перечисления; компилятор везде сообщает вам, что необходимо обновить.
- Производство: рассмотрите маршрутизацию`swift-url-routing`или`TCA`для более крупных приложений.
### Проблема 2: реализация контейнера реактивного состояния
**Постановка задачи:** Создайте простой контейнер реактивного состояния (похожий на Redux/Vuex) в Swift, где изменения состояния будут наблюдаемы, а подписчики будут уведомлены о конкретных изменениях состояния.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) контейнер состояний, который хранит состояние приложения, (2) действия, описывающие изменения состояния, (3) редуктор, который создает новое состояние из текущего состояния + действие, (4) подписчики, которые наблюдают за изменениями состояния. Это однонаправленный шаблон потока данных.
**Шаг 2. Определите подход:**
- Используйте общий класс`Store<State>`с поведением, подобным `@Published`.
- Определить действия как перечисление.
- Используйте функцию редуктора `(State, Action) -> State`.
- Подписчики получают новое состояние через замыкания.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Однонаправленный поток: действия → редуктор → новое состояние → подписчики. Легко рассуждать и тестировать.
- Потокобезопасность: очередь отправки сериализует изменения состояния.
— Подписчики получают полное состояние — используйте селекторы или проверки `Equatable`, чтобы избежать ненужных повторных рендерингов.
- Производство: используйте`The Composable Architecture`(TCA) от Point-Free для реализации промышленного уровня с эффектами, тестированием и интеграцией SwiftUI.
---

## Краткое содержание
Swift — это современный, безопасный и выразительный язык, необходимый для разработки платформ Apple. Его упор на безопасность (опции, типы значений, сопоставление с образцом) предотвращает целые категории ошибок. Помимо платформ Apple, Swift развивается в области разработки серверных и кроссплатформенных приложений. Для разработки iOS/macOS Swift — очевидный выбор. Для других областей это подходящий язык с меньшей, но растущей экосистемой.