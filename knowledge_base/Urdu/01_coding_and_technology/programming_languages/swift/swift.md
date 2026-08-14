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

# سوئفٹ
Swift ایک جدید، مرتب کردہ پروگرامنگ لینگویج ہے جسے Apple (کرس لیٹنر کی قیادت میں) نے تیار کیا تھا اور پہلی بار 2014 میں ریلیز کیا گیا تھا۔ اسے ایپل پلیٹ فارم کی ترقی (iOS, macOS, watchOS, tvOS, visionOS) کے لیے بنیادی زبان کے طور پر Objective-C کو تبدیل کرنے کے لیے ڈیزائن کیا گیا تھا۔ سوئفٹ مرتب شدہ زبانوں کی کارکردگی کو اسکرپٹنگ زبانوں کے اظہار کے ساتھ جوڑتا ہے، اور یہ حفاظت پر زور دیتا ہے -- خاص طور پر کالعدم اقدار، میموری مینجمنٹ، اور ٹائپ کی غلطیوں کے ارد گرد۔
ایپل پلیٹ فارمز کے علاوہ، سوئفٹ تیزی سے سرور سائیڈ ڈویلپمنٹ (ویپر، ہمنگ برڈ)، کراس پلیٹ فارم ایپلی کیشنز، اور یہاں تک کہ مشین لرننگ (ایپل کی تخلیق ایم ایل) کے لیے استعمال ہوتا ہے۔ سوفٹ آن سرور اور کراس پلیٹ فارم سپورٹ کے متعارف ہونے کے ساتھ، سوئفٹ صرف ایک "ایپل لینگویج" سے زیادہ بنتا جا رہا ہے۔
---

## کیوں سوئفٹ معاملات
- **ایپل پلیٹ فارم کا معیار**: iOS، macOS، watchOS، tvOS، اور visionOS کی ترقی کے لیے بنیادی زبان۔
- **ڈیزائن کے لحاظ سے حفاظت**: اختیارات null پوائنٹر کریشز کو ختم کرتے ہیں۔ قدر کی قسمیں غیر ارادی تغیر کو روکتی ہیں۔
- **کارکردگی**: LLVM کے ذریعے مقامی مشین کوڈ پر مرتب کرتا ہے -- بہت سے کاموں کے لیے C++ کے ساتھ مسابقتی۔
- **جدید نحو**: صاف، تاثراتی، بندش کے ساتھ، جنرک، پروٹوکول پر مبنی پروگرامنگ، اور پیٹرن میچنگ۔
- **SwiftUI**: اعلانیہ UI فریم ورک جو Apple پلیٹ فارم کے انٹرفیس کو تیز اور بدیہی بناتا ہے۔
- **اوپن سورس**: سوئفٹ کمپائلر اور معیاری لائبریری اوپن سورس ہیں۔ لینکس اور ونڈوز پر چلتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **ایپل مرکوز** | بہترین ٹولنگ اور ایکو سسٹم ایپل پلیٹ فارمز کے لیے ہیں۔ سرور سائیڈ کے لیے بخارات کا استعمال کریں۔ کراس پلیٹ فارم سپورٹ میں بہتری آرہی ہے |
| **محدود کراس پلیٹ فارم GUI** | Windows/Linux کے لیے کوئی بالغ GUI فریم ورک نہیں۔ کراس پلیٹ فارم کے لیے ویب ٹیکنالوجیز یا فلٹر استعمال کریں۔
| **چھوٹی جاب مارکیٹ (ایپل سے باہر)** | Java، Python، یا JavaScript سے کم کردار | iOS/macOS ڈویلپمنٹ رولز بہت زیادہ ہیں۔
| **تیز ارتقاء** | ورژن کے درمیان متواتر نحوی تبدیلیاں کوڈ کو توڑ سکتی ہیں | پن سوئفٹ ورژن؛ سوئفٹ پیکیج مینیجر کا استعمال کریں |
| ** مرتب اوقات** | پیچیدہ عام کوڈ مرتب کرنے میں سست ہو سکتا ہے | قسم کے اظہار کو آسان بنائیں؛ @inlinable کو انصاف کے ساتھ استعمال کریں۔
---

## نحوی بنیادی باتیں
### متغیرات اور مستقل
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

### اختیاری -- سوفٹ کا حل
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

### افعال اور بندشیں۔
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

### پروٹوکول اور ڈھانچے
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

### نقص کو ہینڈل کرنا
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

## اعلی درجے کی نحو اور نمونے۔
### عام
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

### ایڈوانس پیٹرن میچنگ
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

### پراپرٹی ریپرز اور رزلٹ بلڈرز
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

## ہم آہنگی اور ہم آہنگی (Swift Concurrency)
### async/await
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

### سٹرکچرڈ کنکرنسی
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (سوئفٹ پیکیج)
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

### ضروری احکام
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### XCTest فریم ورک
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

## انٹرآپریبلٹی
### Objective-C انٹراپ
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

### C انٹراپ
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## ڈیزائن پیٹرن
### ڈیلیگیٹ پیٹرن
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

### پروٹوکول پر مبنی ڈیزائن
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

## کارکردگی اور اصلاح
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

## SwiftUI -- اعلانیہ UI
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

## تعیناتی۔
### سرور سائیڈ سوئفٹ
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

پروڈکشن کے لیے، مرتب شدہ بائنری کو اوبنٹو چلانے والے لینکس سرور پر تعینات کریں۔ ایپلیکیشن لائف سائیکل کو منظم کرنے کے لیے systemd جیسے پروسیس مینیجر کا استعمال کریں۔
---

## سوئفٹ کب استعمال کریں۔
| منظر نامہ | کیوں سوئفٹ | بہتر متبادل |
|------------|------------|-------------------|
| iOS/macOS ایپس | ایپل کی معیاری زبان | -- |
| watchOS/visionOS ایپس | واحد آپشن | -- |
| سرور کی طرف (بخار) | بڑھتا ہوا ماحولیاتی نظام | مزید بالغ سرور ماحولیاتی نظام کے لیے Node.js پر جائیں |
| کراس پلیٹ فارم موبائل | ممکن ہے لیکن بنیادی نہیں | پھڑپھڑانا، مقامی رد عمل کا اظہار |
| سسٹمز پروگرامنگ | ممکن (لینکس) | زنگ، C، C++ |
| عام ایپلی کیشن ڈیو (غیر ایپل) | محدود ماحولیاتی نظام | ازگر، گو، جاوا |
---

## مصنوعی سوال و جواب
### Q1: اختیاری کیا ہیں، اور Swift مجھے ان کو کھولنے پر کیوں مجبور کرتی ہے؟
**A:** ایک اختیاری (`Type?`) ایک ایسی قدر کی نمائندگی کرتا ہے جو شاید غائب ہو — یہ یا تو`.some(value)`یا`.none`(nil) ہے۔ رن ٹائم پر null پوائنٹر کریشز کو روکنے کے لیے سوئفٹ واضح کھولنے پر مجبور کرتا ہے۔ آپ`if let`,`guard let`, force unwrap (`!`) , اختیاری زنجیر (`?.`) , یا nil coalescing (`??`) کے ساتھ کھول سکتے ہیں۔ کمپائلر اس بات کو یقینی بناتا ہے کہ آپ صفر کیس کو ہینڈل کرتے ہیں - اس سے کیڑے کی پوری کلاس ختم ہوجاتی ہے۔
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

### Q2: سوئفٹ میں سٹرکٹس اور کلاسز میں کیا فرق ہے؟
**A:** سٹرکٹس قدر کی قسمیں ہیں (اسائنمنٹ پر کاپی کی گئی ہیں)، کلاسز ریفرنس کی قسمیں ہیں (مشترکہ)۔ سٹرکٹس کو ایک مفت ممبر وائز انیشیلائزر ملتا ہے، اور وہ کلاسز کی تمام خصوصیات کو سپورٹ کرتے ہیں سوائے وراثت، ڈینیشیئلائزرز، اور حوالہ شمار کے۔ سوئفٹ کی معیاری لائبریری کی اقسام (`String`,`Array`,`Dictionary`) تمام سٹرکٹس ہیں۔ پہلے سے طے شدہ ڈھانچے کو ترجیح دیں؛ جب آپ کو مشترکہ متغیر حالت یا وراثت کی ضرورت ہو تو کلاسز کا استعمال کریں۔
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

### Q3: پروٹوکول اور پروٹوکول پر مبنی پروگرامنگ کیسے کام کرتے ہیں؟
**A:** پروٹوکول طریقوں، خصوصیات اور ضروریات کے بلیو پرنٹ کی وضاحت کرتے ہیں۔ کوئی بھی قسم اپنی ضروریات کو نافذ کرکے پروٹوکول کے مطابق ہوسکتی ہے۔ پروٹوکول ایکسٹینشنز ڈیفالٹ نفاذ فراہم کرتی ہیں۔ پروٹوکول کے ذریعہ محدود جنرکس آپ کو طبقاتی وراثت کے اوور ہیڈ کے بغیر پولیمورفزم دیتے ہیں - یہ "پروٹوکول پر مبنی پروگرامنگ" ہے۔
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

### Q4: سوئفٹ میں`async/await`کیا ہے، اور اس کا اداکاروں سے کیا تعلق ہے؟
**A:** سوئفٹ کا کنکرنسی ماڈل (5.5+) غیر مطابقت پذیر کوڈ کے لیے`async/await`اور محفوظ مشترکہ تغیر پذیر حالت کے لیے`actors`استعمال کرتا ہے۔ `async`فنکشنز کو معطل اور دوبارہ شروع کیا جا سکتا ہے۔ `await`معطلی پوائنٹس کو نشان زد کرتا ہے۔ اداکار اپنی متغیر حالت تک رسائی کو سیریلائز کرکے ڈیٹا کی دوڑ کو روکتے ہیں - مرتب کرنے والا اسے مرتب وقت پر نافذ کرتا ہے۔
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

### Q5: پراپرٹی ریپرز اور رزلٹ بلڈرز کیسے کام کرتے ہیں؟
**A:** پراپرٹی ریپرز (`@propertyWrapper`) پراپرٹی اسٹوریج میں منطق کا اضافہ کرتے ہیں (جیسے SwiftUI میں `@State`)۔ رزلٹ بلڈرز (`@resultBuilder`) آپ کو قدرتی نحو (جیسے SwiftUI کے ویو ہائراکی) کا استعمال کرتے ہوئے ڈیٹا سٹرکچر بنانے دیتے ہیں۔ دونوں میٹاپروگرامنگ کی شکلیں ہیں جو بوائلر پلیٹ کو کم کرتی ہیں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ایک ٹائپ سیف راؤٹر بنائیں
**مسئلہ کا بیان:** iOS ایپ کے لیے ایک ٹائپ سیف یو آر ایل راؤٹر بنائیں جہاں ہر روٹ میں پیرامیٹر منسلک ہوتے ہیں، اور کمپائلر ان پیرامیٹرز تک رسائی کو روکتا ہے جو کسی مخصوص راستے کے لیے موجود نہیں ہیں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ٹائپ شدہ پیرامیٹرز کے ساتھ روٹ کی تعریفیں، (2) روٹ + پیرامیٹرز کو نکالنے کے لیے یو آر ایل پارسنگ، (3) ٹائپ سیف پیرامیٹر تک رسائی — مرتب کرنے والا یقینی بناتا ہے کہ آپ صرف ان پیرامیٹرز کو پڑھیں جو ہر روٹ کے لیے موجود ہیں۔ اس کے لیے متعلقہ اقدار کے ساتھ enums کی ضرورت ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- راستوں کی وضاحت کے لیے متعلقہ اقدار کے ساتھ ایک اینوم استعمال کریں۔
- ہر کیس اپنے مخصوص پیرامیٹرز کو ٹائپ شدہ اقدار کے طور پر رکھتا ہے۔
- ایک تجزیہ کار یو آر ایل کے تاروں کو روٹ اینوم کیسز میں تبدیل کرتا ہے۔
- پیٹرن میچنگ کمپائل ٹائم سیفٹی کے ساتھ پیرامیٹرز کو نکالتا ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- قسم کی حفاظت: ہر روٹ کیس میں بالکل وہی پیرامیٹرز ہوتے ہیں جن کی اسے ضرورت ہوتی ہے۔ کمپائلر`.userProfile`پر`variant`تک رسائی کو روکتا ہے۔
- تھکاوٹ:`switch`کو تمام معاملات کو ہینڈل کرنا چاہیے — ایک نیا روٹ شامل کرنا تمام ہینڈلرز کو اپ ڈیٹ کرنے پر مجبور کرتا ہے۔
- توسیع پذیری: اینوم کیسز شامل کرکے نئے راستے شامل کریں۔ کمپائلر آپ کو ہر جگہ بتاتا ہے جسے اپ ڈیٹ کرنے کی ضرورت ہے۔
- پیداوار: بڑی ایپس کے لیے`swift-url-routing`یا`TCA`کی روٹنگ پر غور کریں۔
### مسئلہ 2: ایک ری ایکٹو اسٹیٹ کنٹینر کو لاگو کریں۔
**مسئلہ کا بیان:** Swift میں ایک سادہ ری ایکٹیو اسٹیٹ کنٹینر (Redux/Vuex کی طرح) بنائیں جہاں ریاست کی تبدیلیاں قابل مشاہدہ ہوں، اور سبسکرائبرز کو مخصوص حالت میں ہونے والی تبدیلیوں کے بارے میں مطلع کیا جائے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ایک اسٹیٹ کنٹینر جو ایپلی کیشن اسٹیٹ رکھتا ہے، (2) وہ اعمال جو ریاست کی تبدیلیوں کو بیان کرتے ہیں، (3) ایک ایسا ریڈوسر جو موجودہ حالت + ایکشن سے نئی حالت پیدا کرتا ہے، (4) سبسکرائبرز جو ریاست کی تبدیلیوں کا مشاہدہ کرتے ہیں۔ یہ یون ڈائریکشنل ڈیٹا فلو پیٹرن ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`@Published`جیسے طرز عمل کے ساتھ ایک عام`Store<State>`کلاس استعمال کریں۔
- اعمال کی تعریف بطور اینوم کریں۔
- ریڈوسر فنکشن`(State, Action) -> State`استعمال کریں۔
- سبسکرائبرز کو بندش کے ذریعے نئی ریاست موصول ہوتی ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- یک سمتی بہاؤ: اعمال → کم کرنے والا → نئی حالت → سبسکرائبرز۔ اس کے بارے میں استدلال اور جانچ کرنا آسان ہے۔
- تھریڈ سیفٹی: ڈسپیچ قطار ریاستی تغیرات کو سیریلائز کرتی ہے۔
- سبسکرائبرز کو پوری حالت مل جاتی ہے — غیر ضروری دوبارہ رینڈرز سے بچنے کے لیے سلیکٹرز یا`Equatable`چیک استعمال کریں۔
- پیداوار:`The Composable Architecture`(TCA) بذریعہ Point-Free استعمال کریں اثرات، جانچ، اور SwiftUI انضمام کے ساتھ پروڈکشن گریڈ کے نفاذ کے لیے۔
---

## خلاصہ
Swift ایک جدید، محفوظ، اور اظہار خیال کرنے والی زبان ہے جو Apple پلیٹ فارم کی ترقی کے لیے ضروری ہے۔ حفاظت پر اس کا زور (اختیاری، قدر کی قسمیں، پیٹرن کی مماثلت) کیڑے کے تمام زمروں کو روکتا ہے۔ ایپل پلیٹ فارمز کے علاوہ، سوئفٹ سرور سائیڈ ڈیولپمنٹ اور کراس پلیٹ فارم ایپلی کیشنز میں ترقی کر رہا ہے۔ iOS/macOS کی ترقی کے لیے، Swift واضح انتخاب ہے۔ دوسرے ڈومینز کے لیے، یہ ایک چھوٹی لیکن بڑھتے ہوئے ماحولیاتی نظام کے ساتھ ایک قابل زبان ہے۔