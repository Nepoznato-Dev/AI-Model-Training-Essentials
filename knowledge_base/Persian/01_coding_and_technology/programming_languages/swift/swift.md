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

#سوئیفت
سوئیفت یک زبان برنامه نویسی مدرن و کامپایل شده است که توسط اپل (به رهبری کریس لاتنر) توسعه یافته و اولین بار در سال 2014 منتشر شد. این زبان برای جایگزینی Objective-C به عنوان زبان اصلی برای توسعه پلتفرم اپل (iOS، macOS، watchOS، tvOS، visionOS) طراحی شده است. سوئیفت عملکرد زبان‌های کامپایل شده را با بیان زبان‌های برنامه‌نویسی ترکیب می‌کند و بر ایمنی تأکید می‌کند - به ویژه در مورد مقادیر تهی، مدیریت حافظه و خطاهای نوع.
فراتر از پلتفرم های اپل، سوئیفت به طور فزاینده ای برای توسعه سمت سرور (Vapor، Hummingbird)، برنامه های کاربردی بین پلتفرمی و حتی یادگیری ماشینی (Apple's Create ML) استفاده می شود. با معرفی سوئیفت روی سرور و پشتیبانی از پلتفرم های مختلف، سوئیفت به چیزی بیش از یک «زبان اپل» تبدیل شده است.
---

## چرا سوئیفت مهم است
- **استاندارد پلتفرم اپل**: زبان اصلی برای توسعه iOS، macOS، watchOS، tvOS و visionOS.
- **ایمنی بر اساس طراحی**: موارد اختیاری خرابی نشانگر تهی را از بین می برد. انواع ارزش از جهش ناخواسته جلوگیری می کند.
- ** عملکرد **: از طریق LLVM به کد ماشین بومی کامپایل می شود - برای بسیاری از کارها با C++ رقابت می کند.
- ** نحو مدرن **: تمیز، رسا، با بسته شدن، ژنریک، برنامه نویسی پروتکل گرا، و تطبیق الگو.
- **SwiftUI**: چارچوب UI اعلامی که ساخت رابط های پلت فرم اپل را سریع و بصری می کند.
- **متن باز**: کامپایلر سوئیفت و کتابخانه استاندارد منبع باز هستند. روی لینوکس و ویندوز اجرا می شود.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **سیب محور** | بهترین ابزار و اکوسیستم برای پلتفرم های اپل است | از Vapor برای سمت سرور استفاده کنید. پشتیبانی بین پلتفرمی در حال بهبود است |
| ** رابط کاربری گرافیکی کراس پلتفرم محدود ** | بدون چارچوب رابط کاربری گرافیکی بالغ برای ویندوز/لینوکس | از فناوری‌های وب یا Flutter برای کراس پلتفرم |
| **بازار کار کوچکتر (خارج از اپل)** | نقش های کمتر از جاوا، پایتون یا جاوا اسکریپت | نقش های توسعه iOS/macOS فراوان هستند |
| **تکامل سریع** | تغییرات سینتکس مکرر بین نسخه ها می تواند کد را خراب کند | پین کردن نسخه های سوئیفت؛ استفاده از Swift Package Manager |
| **زمان کامپایل** | کامپایل کد عمومی پیچیده می تواند کند باشد | ساده کردن عبارات نوع؛ از @inlinable به طور عاقلانه استفاده کنید |
---

## اصول نحو
### متغیرها و ثابت ها
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

### گزینه‌های اختیاری - راه‌حل Swift برای Null
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

### توابع و بسته شدن
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

### پروتکل ها و ساختارها
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

### رسیدگی به خطا
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

## نحو و الگوهای پیشرفته
### ژنریک
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

### تطبیق الگوی پیشرفته
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

### بسته‌بندی‌های دارایی و سازندگان نتایج
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

## همزمانی و موازی (همگامی سریع)
### ناهمگام/انتظار
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

### همزمانی ساختاریافته
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (بسته سوئیفت)
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

### دستورات ضروری
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### چارچوب XCTest
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

## قابلیت همکاری
### Interop Objective-C
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

## الگوهای طراحی
### الگوی نماینده
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

### طراحی پروتکل گرا
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

## عملکرد و بهینه سازی
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

## SwiftUI -- رابط کاربری اعلامی
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

## استقرار
### سوییفت سمت سرور
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

برای تولید، باینری کامپایل شده را روی یک سرور لینوکس که اوبونتو را اجرا می کند، مستقر کنید. از یک مدیر فرآیند مانند systemd برای مدیریت چرخه عمر برنامه استفاده کنید.
---

## چه زمانی از Swift استفاده کنیم
| سناریو | چرا سویفت | جایگزین بهتر |
|----------|---------|-------------------|
| برنامه های iOS/macOS | زبان استاندارد اپل | -- |
| برنامه های watchOS/visionOS | تنها گزینه | -- |
| سمت سرور (بخار) | اکوسیستم در حال رشد | برو، Node.js برای اکوسیستم های سرور بالغ تر |
| موبایل کراس پلتفرم | ممکن است اما نه اولیه | Flutter، React Native |
| برنامه نویسی سیستم ها | ممکن (لینوکس) | Rust, C, C++ |
| توسعه دهنده برنامه عمومی (غیر اپل) | اکوسیستم محدود | پایتون، برو، جاوا |
---

## پرسش و پاسخ مصنوعی
### Q1: گزینه های اختیاری چیست و چرا سوئیفت من را مجبور می کند آنها را باز کنم؟
**A:** یک اختیاری (`Type?`) مقداری را نشان می دهد که ممکن است وجود نداشته باشد - یا`.some(value)`یا`.none`(نفر). سوئیفت برای جلوگیری از خرابی نشانگر تهی در زمان اجرا، باز کردن صریح را مجبور می‌کند. می‌توانید با `if let`، `guard let`، باز کردن اجباری (`!`)، زنجیر کردن اختیاری (`?.`)، یا ادغام صفر (`??`) باز کنید. کامپایلر تضمین می‌کند که شما با nil case مدیریت می‌کنید – این کار کل کلاس باگ‌ها را حذف می‌کند.
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

### Q2: تفاوت بین ساختارها و کلاس ها در سوئیفت چیست؟
**A:** ساختارها انواع ارزش هستند (در زمان تکلیف کپی می شوند)، کلاس ها انواع مرجع (اشتراک گذاری شده) هستند. ساختارها یک اولیه‌ساز رایگان عضو دریافت می‌کنند و از همه ویژگی‌های کلاس‌ها به جز وراثت، deinitializers و شمارش مرجع پشتیبانی می‌کنند. انواع استاندارد کتابخانه سوئیفت (`String`، `Array`، `Dictionary`) همگی ساختار هستند. ترجیح ساختارها به طور پیش فرض. در مواقعی که به وضعیت یا وراثت قابل تغییر مشترک نیاز دارید از کلاس ها استفاده کنید.
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

### Q3: پروتکل ها و برنامه نویسی پروتکل گرا چگونه کار می کنند؟
**A:** پروتکل ها طرحی از روش ها، ویژگی ها و الزامات را تعریف می کنند. هر نوع می تواند با اجرای الزامات یک پروتکل مطابقت داشته باشد. پسوندهای پروتکل پیاده سازی های پیش فرض را ارائه می دهند. ژنریک های محدود شده توسط پروتکل ها به شما چندشکلی می دهند بدون سربار وراثت کلاس - این "برنامه نویسی پروتکل گرا" است.
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

### Q4:`async/await`در سوئیفت چیست و چه ارتباطی با بازیگران دارد؟
**A:** مدل همزمانی سوئیفت (5.5+) از`async/await`برای کد ناهمزمان و`actors`برای حالت ایمن قابل تغییر مشترک استفاده می کند.  عملکردهای`async`را می توان به حالت تعلیق درآورد و از سر گرفت. `await`نقاط تعلیق را مشخص می کند. بازیگران با سریال‌سازی دسترسی به حالت تغییرپذیرشان از مسابقه داده‌ها جلوگیری می‌کنند - کامپایلر این را در زمان کامپایل اعمال می‌کند.
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

### Q5: پوشش های دارایی و سازندگان نتیجه چگونه کار می کنند؟
** پاسخ: ** بسته‌بندی‌های دارایی (`@propertyWrapper`) منطق را به ذخیره‌سازی دارایی اضافه می‌کنند (مانند`@State`در SwiftUI). سازندگان نتایج (`@resultBuilder`) به شما امکان می‌دهند ساختارهای داده را با استفاده از نحو طبیعی بسازید (مانند سلسله مراتب مشاهده SwiftUI). هر دو شکلی از فرابرنامه هستند که صفحه دیگ بخار را کاهش می دهند.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک روتر Type-Safe بسازید
**بیانیه مشکل:** یک مسیریاب URL ایمن برای یک برنامه iOS ایجاد کنید که در آن هر مسیر دارای پارامترهای مرتبط است و کامپایلر از دسترسی به پارامترهایی که برای یک مسیر مشخص وجود ندارند جلوگیری می کند.
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) تعاریف مسیر با پارامترهای تایپ شده، (2) تجزیه URL برای استخراج مسیر + پارامترها، (3) دسترسی به پارامترهای ایمن - کامپایلر تضمین می‌کند که شما فقط پارامترهای موجود برای هر مسیر را می‌خوانید. برای این کار باید تعدادهای همراه با مقادیر مرتبط باشد.
** مرحله 2 - شناسایی رویکرد: **
- از یک enum با مقادیر مرتبط برای تعریف مسیرها استفاده کنید.
- هر مورد پارامترهای خاص خود را به عنوان مقادیر تایپ شده حمل می کند.
- یک تجزیه کننده رشته های URL را به موارد enum مسیریابی می کند.
- تطبیق الگو پارامترها را با ایمنی زمان کامپایل استخراج می کند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی نوع: هر مورد مسیر دقیقاً پارامترهای مورد نیاز خود را دارد. کامپایلر از دسترسی به`variant`در`.userProfile`جلوگیری می کند.
- جامع بودن:`switch`باید همه موارد را کنترل کند - با افزودن یک مسیر جدید که همه کنترل کننده ها را به روز می کند.
- توسعه پذیری: اضافه کردن مسیرهای جدید با اضافه کردن موارد enum. کامپایلر همه جا به شما می گوید که نیاز به به روز رسانی دارد.
- تولید: مسیریابی`swift-url-routing`یا`TCA`را برای برنامه های بزرگتر در نظر بگیرید.
### مسئله 2: یک کانتینر حالت واکنشی را پیاده سازی کنید
**بیانیه مشکل:** یک کانتینر حالت واکنشی ساده (مشابه Redux/Vuex) در سوئیفت بسازید که در آن تغییرات حالت قابل مشاهده است و مشترکین از تغییرات وضعیت خاص مطلع می شوند.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) یک محفظه حالت که دارای حالت برنامه باشد، (2) اقداماتی که تغییرات حالت را توصیف می کند، (3) یک کاهنده که حالت جدیدی را از حالت فعلی + عمل ایجاد کند، (4) مشترکینی که تغییرات حالت را مشاهده می کنند. این الگوی جریان داده یک طرفه است.
** مرحله 2 - شناسایی رویکرد: **
- از یک کلاس`Store<State>`عمومی با رفتار مشابه`@Published`استفاده کنید.
- اقدامات را به صورت enum تعریف کنید.
- از یک تابع کاهنده`(State, Action) -> State`استفاده کنید.
- مشترکین وضعیت جدید را از طریق بسته شدن دریافت می کنند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- جریان یک طرفه: اقدامات → کاهش دهنده → وضعیت جدید → مشترکین. استدلال و آزمایش آسان است.
- ایمنی رشته: صف اعزام جهش های حالت را سریال می کند.
- مشترکین وضعیت کامل را دریافت می کنند - از انتخابگرها یا چک های`Equatable`برای جلوگیری از ارائه مجدد غیرضروری استفاده کنید.
- تولید: از`The Composable Architecture`(TCA) توسط Point-Free برای اجرای درجه تولید با افکت‌ها، آزمایش و ادغام SwiftUI استفاده کنید.
---

## خلاصه
Swift یک زبان مدرن، ایمن و رسا است که برای توسعه پلتفرم اپل ضروری است. تاکید آن بر ایمنی (اختیاری، انواع ارزش، تطبیق الگو) از کل دسته‌بندی اشکالات جلوگیری می‌کند. سوئیفت فراتر از پلتفرم های اپل، در توسعه سمت سرور و برنامه های کاربردی چند پلتفرمی در حال رشد است. برای توسعه iOS/macOS، سوئیفت انتخاب واضحی است. برای سایر حوزه‌ها، زبانی توانا با اکوسیستم کوچک‌تر اما در حال رشد است.