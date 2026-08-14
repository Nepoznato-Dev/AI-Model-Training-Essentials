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

# matulin
Ang Swift ay isang moderno, pinagsama-samang programming language na binuo ng Apple (pinamumunuan ni Chris Lattner) at unang inilabas noong 2014. Idinisenyo ito upang palitan ang Objective-C bilang pangunahing wika para sa pagbuo ng platform ng Apple (iOS, macOS, watchOS, tvOS, visionOS). Pinagsasama ng Swift ang pagganap ng mga pinagsama-samang wika sa pagpapahayag ng mga wika ng script, at binibigyang-diin nito ang kaligtasan -- partikular na sa paligid ng mga null value, pamamahala ng memorya, at mga error sa uri.
Higit pa sa mga platform ng Apple, ang Swift ay lalong ginagamit para sa server-side development (Vapor, Hummingbird), mga cross-platform na application, at kahit machine learning (Apple's Create ML). Sa pagpapakilala ng Swift sa Server at suporta sa cross-platform, ang Swift ay nagiging higit pa sa isang "wika ng Apple."
---

## Bakit Mahalaga ang Swift
- **Apple platform standard**: Ang pangunahing wika para sa iOS, macOS, watchOS, tvOS, at visionOS development.
- **Kaligtasan ayon sa disenyo**: Ang mga opsyonal ay nag-aalis ng mga null pointer na pag-crash. Pinipigilan ng mga uri ng halaga ang hindi sinasadyang mutation.
- **Pagganap**: Nag-compile sa native machine code sa pamamagitan ng LLVM -- mapagkumpitensya sa C++ para sa maraming gawain.
- **Modern syntax**: Malinis, nagpapahayag, na may mga pagsasara, generics, programming-oriented sa protocol, at pagtutugma ng pattern.
- **SwiftUI**: Declarative UI framework na ginagawang mabilis at intuitive ang pagbuo ng mga interface ng Apple platform.
- **Open source**: Ang Swift compiler at karaniwang library ay open source; tumatakbo sa Linux at Windows.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Apple-centric** | Ang pinakamahusay na tooling at ecosystem ay para sa mga platform ng Apple | Gumamit ng Vapor para sa server-side; ang suporta sa cross-platform ay bumubuti |
| **Limitadong cross-platform GUI** | Walang mature na GUI framework para sa Windows/Linux | Gumamit ng mga teknolohiya sa web o Flutter para sa cross-platform |
| **Mas maliit na market ng trabaho (sa labas ng Apple)** | Mas kaunting mga tungkulin kaysa sa Java, Python, o JavaScript | Ang mga tungkulin sa pagpapaunlad ng iOS/macOS ay marami |
| **Mabilis na ebolusyon** | Ang mga madalas na pagbabago sa syntax sa pagitan ng mga bersyon ay maaaring masira ang code | I-pin ang mga bersyon ng Swift; gamitin ang Swift Package Manager |
| **Mga oras ng pag-compile** | Ang kumplikadong generic na code ay maaaring mabagal sa pag-compile | Pasimplehin ang mga uri ng expression; gamitin ang @inlinable nang matalino |
---

## Syntax Fundamentals
### Mga Variable at Constant
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

### Opsyonal -- Solusyon ni Swift sa Null
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

### Mga Pag-andar at Pagsasara
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

### Mga Protocol at Struct
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

### Error sa Paghawak
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

## Advanced na Syntax at Mga Pattern
### Generics
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

### Advanced na Pagtutugma ng Pattern
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

### Mga Balot ng Ari-arian at Mga Tagabuo ng Resulta
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

## Concurrency at Parallelism (Swift Concurrency)
### async/naghihintay
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

### Structured Concurrency
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

## Project Configuration at Build System
### Istraktura ng Proyekto (Swift Package)
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

### Package.swift
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

### Mahahalagang Utos
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### XCTest Framework
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

## Interoperability
### Objective-C Interop
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

### C Interop
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Mga Pattern ng Disenyo
### Pattern ng Delegado
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

### Protocol-Oriented na Disenyo
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

## Pagganap at Pag-optimize
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

## SwiftUI -- Declarative UI
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

## Deployment
### Server-Side Swift
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Para sa produksyon, i-deploy ang pinagsama-samang binary sa isang Linux server na nagpapatakbo ng Ubuntu. Gumamit ng process manager tulad ng systemd para pamahalaan ang lifecycle ng application.
---

## Kailan Gamitin ang Swift
| Sitwasyon | Bakit Swift | Mas mahusay na Alternatibo |
|----------|----------|-------------------|
| iOS/macOS apps | Ang karaniwang wika ng Apple | -- |
| watchOS/visionOS apps | Tanging pagpipilian | -- |
| Gilid ng server (Vapor) | Lumalagong ecosystem | Pumunta, Node.js para sa mas mature na server ecosystem |
| Cross-platform na mobile | Posible ngunit hindi pangunahin | Flutter, React Native |
| System programming | Posible (Linux) | kalawang, C, C++ |
| Pangkalahatang application dev (hindi Apple) | Limitadong ecosystem | Python, Go, Java |
---

## Synthetic na Q&A
### Q1: Ano ang mga opsyonal, at bakit pinipilit ako ni Swift na i-unwrap ang mga ito?
**A:** Ang isang opsyonal (`Type?`) ay kumakatawan sa isang value na maaaring wala — ito ay alinman sa`.some(value)`o`.none`(nil). Pinipilit ni Swift ang tahasang pag-unwrapping upang maiwasan ang pag-crash ng null pointer sa runtime. Maaari kang mag-unwrap gamit ang`if let`,`guard let`, puwersahang i-unwrap (`!`), opsyonal na chaining (`?.`), o nil coalescing (`??`). Tinitiyak ng compiler na hahawakan mo ang nil case — inaalis nito ang isang buong klase ng mga bug.
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

### Q2: Ano ang pagkakaiba sa pagitan ng mga istruktura at mga klase sa Swift?
**A:** Ang mga istruktura ay mga uri ng halaga (kinopya sa takdang-aralin), ang mga klase ay mga uri ng sanggunian (ibinahagi). Nakakakuha ang Structs ng libreng memberwise initializer, at sinusuportahan nila ang lahat ng feature ng mga klase maliban sa inheritance, deinitializer, at reference counting. Ang mga karaniwang uri ng library ng Swift (`String`,`Array`,`Dictionary`) ay lahat ng mga struct. Mas gusto ang mga struct bilang default; gumamit ng mga klase kapag kailangan mo ng nakabahaging nababagong estado o mana.
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

### Q3: Paano gumagana ang mga protocol at protocol-oriented programming?
**S:** Tinutukoy ng mga protocol ang isang blueprint ng mga pamamaraan, katangian, at kinakailangan. Anumang uri ay maaaring umayon sa isang protocol sa pamamagitan ng pagpapatupad ng mga kinakailangan nito. Nagbibigay ang mga extension ng protocol ng mga default na pagpapatupad. Ang mga generic na pinipigilan ng mga protocol ay nagbibigay sa iyo ng polymorphism nang walang overhead ng class inheritance — ito ay "protocol-oriented programming."
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

### Q4: Ano ang`async/await`sa Swift, at paano ito nauugnay sa mga aktor?
**A:** Gumagamit ang concurrency model (5.5+) ng Swift ng`async/await`para sa asynchronous na code at`actors`para sa ligtas na shared mutable na estado.  Ang mga function ng`async`ay maaaring masuspinde at ipagpatuloy.  Ang`await`ay nagmamarka ng mga punto ng pagsususpinde. Pinipigilan ng mga aktor ang mga karera ng data sa pamamagitan ng pagse-serialize ng access sa kanilang nababagong estado — ipinapatupad ito ng compiler sa oras ng pag-compile.
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

### Q5: Paano gumagana ang mga wrapper ng property at tagabuo ng resulta?
**A:** Ang mga wrapper ng property (`@propertyWrapper`) ay nagdaragdag ng logic sa storage ng property (tulad ng`@State`sa SwiftUI). Hinahayaan ka ng mga tagabuo ng resulta (`@resultBuilder`) na bumuo ng mga istruktura ng data gamit ang natural na syntax (tulad ng hierarchy ng view ng SwiftUI). Parehong mga anyo ng metaprogramming na nagpapababa ng boilerplate.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Uri-Ligtas na Router
**Pahayag ng Problema:** Lumikha ng isang uri-safe na URL router para sa isang iOS app kung saan ang bawat ruta ay may nauugnay na mga parameter, at pinipigilan ng compiler ang pag-access ng mga parameter na wala para sa isang partikular na ruta.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) mga kahulugan ng ruta na may mga na-type na parameter, (2) Pag-parse ng URL upang kunin ang ruta + mga parameter, (3) pag-access ng parameter na ligtas sa uri — tinitiyak ng compiler na nababasa mo lang ang mga parameter na umiiral para sa bawat ruta. Nangangailangan ito ng mga enum na may nauugnay na mga halaga.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng isang enum na may nauugnay na mga halaga upang tukuyin ang mga ruta.
- Ang bawat kaso ay nagdadala ng mga partikular na parameter nito bilang mga nai-type na halaga.
- Ang isang parser ay nagko-convert ng mga string ng URL upang iruta ang mga kaso ng enum.
- Ang pagtutugma ng pattern ay nag-extract ng mga parameter na may kaligtasan sa oras ng pag-compile.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Uri ng kaligtasan: ang bawat kaso ng ruta ay may eksaktong mga parameter na kailangan nito. Pinipigilan ng compiler ang pag-access sa`variant`sa`.userProfile`.
- Pagkaubos: dapat pangasiwaan ng`switch`ang lahat ng kaso — pagdaragdag ng bagong ruta na pumipilit sa pag-update ng lahat ng mga humahawak.
- Extensibility: magdagdag ng mga bagong ruta sa pamamagitan ng pagdaragdag ng mga kaso ng enum; ang compiler ay nagsasabi sa iyo saanman na nangangailangan ng pag-update.
- Produksyon: isaalang-alang ang pagruruta ng`swift-url-routing`o`TCA`para sa mas malalaking app.
### Problema 2: Magpatupad ng Reactive State Container
**Problem Statement:** Bumuo ng isang simpleng reactive state container (katulad ng Redux/Vuex) sa Swift kung saan ang mga pagbabago sa estado ay makikita, at ang mga subscriber ay inaabisuhan ng mga partikular na pagbabago sa estado.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) isang lalagyan ng estado na nagtataglay ng estado ng aplikasyon, (2) mga aksyon na naglalarawan ng mga pagbabago sa estado, (3) isang reducer na gumagawa ng bagong estado mula sa kasalukuyang estado + pagkilos, (4) mga subscriber na nagmamasid sa mga pagbabago sa estado. Ito ang unidirectional na pattern ng daloy ng data.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng generic na`Store<State>`na klase na may`@Published`na pag-uugali.
- Tukuyin ang mga aksyon bilang isang enum.
- Gumamit ng function ng reducer`(State, Action) -> State`.
- Natatanggap ng mga subscriber ang bagong estado sa pamamagitan ng mga pagsasara.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Unidirectional flow: mga aksyon → reducer → bagong estado → subscriber. Madaling mangatwiran at subukan.
- Kaligtasan ng thread: ang dispatch queue ay nagseserye ng mga mutasyon ng estado.
- Nakukuha ng mga subscriber ang buong estado — gumamit ng mga selector o`Equatable`na pagsusuri upang maiwasan ang mga hindi kinakailangang muling pag-render.
- Produksyon: gumamit ng`The Composable Architecture`(TCA) ng Point-Free para sa pagpapatupad ng antas ng produksyon na may mga epekto, pagsubok, at pagsasama ng SwiftUI.
---

## Buod
Ang Swift ay isang moderno, ligtas, at nagpapahayag na wika na mahalaga para sa pagbuo ng platform ng Apple. Ang pagbibigay-diin nito sa kaligtasan (mga opsyon, mga uri ng halaga, pagtutugma ng pattern) ay pumipigil sa buong kategorya ng mga bug. Higit pa sa mga platform ng Apple, ang Swift ay lumalaki sa server-side development at mga cross-platform na application. Para sa pagpapaunlad ng iOS/macOS, ang Swift ang malinaw na pagpipilian. Para sa iba pang mga domain, ito ay isang may kakayahang wika na may mas maliit ngunit lumalaking ecosystem.