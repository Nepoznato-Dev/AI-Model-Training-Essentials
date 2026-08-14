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
# Mwepesi
Swift ni lugha ya kisasa, iliyokusanywa ya programu iliyotengenezwa na Apple (inayoongozwa na Chris Lattner) na ilitolewa kwa mara ya kwanza mnamo 2014. Iliundwa kuchukua nafasi ya Objective-C kama lugha ya msingi ya ukuzaji wa jukwaa la Apple (iOS, macOS, watchOS, tvOS, visionOS). Swift inachanganya utendakazi wa lugha zilizokusanywa na uwazi wa lugha za uandishi, na inasisitiza usalama -- hasa kuhusu thamani batili, udhibiti wa kumbukumbu na makosa ya aina.
Zaidi ya majukwaa ya Apple, Swift inazidi kutumika kwa ukuzaji wa upande wa seva (Mvuke, Hummingbird), utumizi wa majukwaa mtambuka, na hata kujifunza kwa mashine (Apple's Create ML). Kwa kuanzishwa kwa Swift kwenye Seva na usaidizi wa jukwaa-msingi, Swift inakuwa zaidi ya "lugha ya Apple."
---

## Why Swift Matters
- **kiwango cha jukwaa la Apple**: Lugha msingi ya iOS, macOS, watchOS, tvOS, na ukuzaji wa visionOS.
- **Usalama kulingana na muundo**: Hiari huondoa hitilafu za viashiria. Aina za thamani huzuia mabadiliko yasiyotarajiwa.
- **Utendaji**: Hujumuisha msimbo wa mashine asilia kupitia LLVM -- inashindana na C++ kwa kazi nyingi.
- **Sintaksia ya kisasa**: Safi, wazi, na kufungwa, jenetiki, upangaji unaozingatia itifaki, na kulinganisha muundo.
- **SwiftUI**: Mfumo wa UI unaobainisha ambao hufanya ujenzi wa violesura vya jukwaa la Apple kwa haraka na angavu.
- **Chanzo huria**: Kikusanyaji cha Swift na maktaba ya kawaida ni chanzo wazi; inaendesha kwenye Linux na Windows.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Apple-centric** | Vifaa bora na mfumo wa ikolojia ni wa majukwaa ya Apple | Tumia Mvuke kwa upande wa seva; usaidizi wa majukwaa mbalimbali unaboreka |
| **GUI ya majukwaa mtambuka** | Hakuna mfumo wa GUI uliokomaa wa Windows/Linux | Tumia teknolojia za wavuti au Flutter kwa jukwaa mtambuka |
| **Soko dogo la ajira (nje ya Apple)** | Majukumu machache kuliko Java, Python, au JavaScript | Majukumu ya ukuzaji wa iOS/macOS ni mengi |
| **Mageuzi ya haraka** | Mabadiliko ya mara kwa mara ya sintaksia kati ya matoleo yanaweza kuvunja msimbo | Bandika matoleo ya Swift; tumia Kidhibiti cha Kifurushi cha Swift |
| **Kukusanya nyakati** | Nambari tata ya jumla inaweza kuwa polepole kuunda | Rahisisha usemi wa aina; tumia @inlinable kwa busara |
---

## Misingi ya Sintaksia
### Vigezo na Mara kwa mara
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

### Chaguo -- Suluhisho la Swift Kufuta
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

### Kazi na Kufungwa
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

### Itifaki na Miundo
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

### Kushughulikia Hitilafu
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

## Sintaksia na Miundo ya Kina
### Jenerali
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

### Ulinganishaji wa Miundo ya Kina
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

### Vitambaa vya Mali na Wajenzi wa Matokeo
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

## Sarafu na Usambamba (Fedha za Mwepesi)
### hailingani/inasubiri
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

### Concurrency Muundo
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi (Kifurushi Mwepesi)
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

### Kifurushi.mwepesi
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

### Amri Muhimu
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD Bomba (Vitendo vya GitHub)
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

##Upimaji
### Mfumo wa XCTest
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

## Kuingiliana
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

## Miundo ya Kubuni
### Weka Mpangilio
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

### Muundo Unaozingatia Itifaki
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

## Utendaji na Uboreshaji
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

## SwiftUI -- UI ya Kutangaza
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

## Usambazaji
### Seva-Side Swift
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Kwa uzalishaji, peleka binary iliyokusanywa kwa seva ya Linux inayoendesha Ubuntu. Tumia kidhibiti mchakato kama vile systemd kudhibiti mzunguko wa maisha ya programu.
---

## Wakati wa Kutumia Swift
| Hali | Kwa nini Mwepesi | Mbadala Bora |
|----------|----------|-------------------|
| Programu za iOS/macOS | Lugha ya kawaida ya Apple | -- |
| programu za watchOS/visionOS | Chaguo pekee | -- |
| Upande wa seva (Mvuke) | Mfumo wa ikolojia unaokua | Nenda, Node.js kwa mifumo ikolojia ya seva iliyokomaa |
| Simu ya jukwaa tofauti | Inawezekana lakini si ya msingi | Flutter, React Asili |
| Upangaji wa mifumo | Inawezekana (Linux) | Kutu, C, C++ |
| Programu ya jumla ya dev (isiyo ya Apple) | Mfumo ikolojia mdogo | Python, Nenda, Java |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Chaguo ni zipi, na kwa nini Swift ananilazimisha kuzifungua?
**J:** Hiari (`Type?`) inawakilisha thamani ambayo inaweza kuwa haipo - inaweza kuwa`.some(value)`au`.none`(nil). Mwepesi hulazimisha kufunua wazi ili kuzuia ajali za vielelezo tupu wakati wa utekelezaji. Unaweza kufunua kwa`if let`,`guard let`, kufunua kwa nguvu (`!`), mnyororo wa hiari (`?.`), au bila kuunganisha (`??`). Mkusanyaji huhakikisha unashughulikia kesi ya nil - hii huondoa aina nzima ya mende.
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

### Q2: Kuna tofauti gani kati ya muundo na madarasa katika Swift?
**J:** Miundo ni aina za thamani (zimenakiliwa kwenye kazi), madarasa ni aina za marejeleo (zilizoshirikiwa). Mipangilio hupata kianzilishi cha uanachama bila malipo, na inaauni vipengele vyote vya madarasa isipokuwa urithi, vianzilishi, na kuhesabu marejeleo. Aina za maktaba za kawaida za Swift (`String`,`Array`,`Dictionary`) zote ni miundo. Pendelea miundo kwa chaguo-msingi; tumia madarasa unapohitaji hali au urithi unaoweza kubadilishwa.
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

### Q3: Je, itifaki na upangaji programu unaozingatia itifaki hufanya kazi vipi?
**J:** Itifaki hufafanua mchoro wa mbinu, sifa na mahitaji. Aina yoyote inaweza kuendana na itifaki kwa kutekeleza mahitaji yake. Viendelezi vya itifaki hutoa utekelezaji chaguomsingi. Jeniriki zinazozuiliwa na itifaki hukupa upolimishaji bila urithi wa darasa - hii ni "programu inayozingatia itifaki."
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

### Q4:`async/await`ni nini katika Swift, na inahusiana vipi na waigizaji?
**J:** Muundo wa upatanishi wa Swift (5.5+) unatumia`async/await`kwa msimbo usiolingana na`actors`kwa hali salama inayoweza kugeuzwa.  Vitendaji vya`async`vinaweza kusimamishwa na kuanzishwa tena. `await`inaashiria alama za kusimamishwa. Waigizaji huzuia mbio za data kwa kuratibu ufikiaji wa hali yao inayoweza kubadilika - mkusanyaji hutekeleza hili kwa wakati wa kukusanya.
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

### Q5: Vifungashio vya mali na wajenzi wa matokeo hufanya kazi vipi?
**J:** Vifungashio vya mali (`@propertyWrapper`) huongeza mantiki kwenye hifadhi ya mali (kama`@State`katika SwiftUI). Wajenzi wa matokeo (`@resultBuilder`) hukuruhusu utengeneze miundo ya data kwa kutumia sintaksia asilia (kama vile mpangilio wa mtazamo wa SwiftUI). Zote ni aina za metaprogramming ambazo hupunguza boilerplate.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tengeneza Kipanga njia cha Aina-salama
**Taarifa ya Tatizo:** Unda kipanga njia cha URL cha aina salama kwa ajili ya programu ya iOS ambapo kila njia ina vigezo vinavyohusishwa, na mkusanyaji huzuia kufikia vigezo ambavyo havipo kwa njia fulani.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) ufafanuzi wa njia na vigezo vilivyochapwa, (2) uchanganuzi wa URL ili kutoa njia + vigezo, (3) ufikiaji wa kigezo cha aina-salama - mkusanyaji huhakikisha kwamba unasoma tu vigezo vilivyopo kwa kila njia. Hii inahitaji enums na maadili yanayohusiana.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia enum yenye thamani zinazohusiana ili kufafanua njia.
- Kila kesi hubeba vigezo vyake mahususi kama thamani zilizochapwa.
- Kichanganuzi hubadilisha mifuatano ya URL kuwa njia za matukio ya enum.
- Vigezo vya dondoo vinavyolingana na muundo na usalama wa wakati wa kukusanya.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa aina: kila kipochi cha njia hubeba vigezo vinavyohitajika. Mkusanyaji huzuia kufikia`variant`kwenye`.userProfile`.
- Ukamilifu:`switch`lazima ishughulikie matukio yote - kuongeza njia mpya kunalazimisha kusasisha vishikilizi vyote.
- Upanuzi: ongeza njia mpya kwa kuongeza kesi za enum; mkusanyaji anakuambia kila mahali kwamba inahitaji kusasishwa.
- Uzalishaji: zingatia uelekezaji wa`swift-url-routing`au`TCA`kwa programu kubwa zaidi.
### Tatizo la 2: Tekeleza Kontena Tekelezi la Hali
**Taarifa ya Tatizo:** Unda chombo rahisi cha hali tendaji (sawa na Redux/Vuex) katika Swift ambapo mabadiliko ya hali yanaonekana, na wanaojisajili wanaarifiwa kuhusu mabadiliko mahususi ya hali.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) chombo cha serikali ambacho kina hali ya maombi, (2) vitendo vinavyoelezea mabadiliko ya hali, (3) kipunguzaji ambacho hutoa hali mpya kutoka kwa hali ya sasa + kitendo, (4) waliojisajili wanaozingatia mabadiliko ya hali. Huu ni muundo wa mtiririko wa data usio na mwelekeo mmoja.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia darasa la kawaida la`Store<State>`lenye tabia kama ya `@Published`.
- Bainisha vitendo kama enum.
- Tumia kitendakazi cha kupunguza`(State, Action) -> State`.
- Wasajili hupokea hali mpya kupitia kufungwa.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Mtiririko wa mwelekeo mmoja: vitendo → kipunguzaji → hali mpya → waliojisajili. Rahisi kufikiria na kujaribu.
- Usalama wa nyuzi: foleni ya kutuma husasisha mabadiliko ya hali.
- Wanaojisajili wanapata hali kamili - tumia viteuzi au ukaguzi wa`Equatable`ili kuzuia uwasilishaji upya usio wa lazima.
- Uzalishaji: tumia`The Composable Architecture`(TCA) by Point-Free kwa utekelezaji wa kiwango cha uzalishaji wenye athari, majaribio na ushirikiano wa SwiftUI.
---

## Muhtasari
Swift ni lugha ya kisasa, salama na ya kueleza ambayo ni muhimu kwa maendeleo ya jukwaa la Apple. Msisitizo wake juu ya usalama (chaguo, aina za thamani, kulinganisha muundo) huzuia kategoria nzima za hitilafu. Zaidi ya majukwaa ya Apple, Swift inakua katika ukuzaji wa upande wa seva na utumizi wa majukwaa mtambuka. Kwa maendeleo ya iOS/macOS, Swift ndio chaguo wazi. Kwa vikoa vingine, ni lugha yenye uwezo na mfumo ikolojia mdogo lakini unaokua.