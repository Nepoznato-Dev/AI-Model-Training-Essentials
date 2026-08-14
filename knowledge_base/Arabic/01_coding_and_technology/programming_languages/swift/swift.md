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
#سويفت
Swift هي لغة برمجة حديثة ومجمعة طورتها شركة Apple (بقيادة كريس لاتنر) وتم إصدارها لأول مرة في عام 2014. وقد تم تصميمها لتحل محل لغة Objective-C باعتبارها اللغة الأساسية لتطوير منصة Apple (iOS، وmacOS، وwatchOS، وtvOS، وvisionOS). يجمع Swift بين أداء اللغات المجمعة وتعبير لغات البرمجة النصية، ويؤكد على السلامة - خاصة فيما يتعلق بالقيم الخالية وإدارة الذاكرة وأخطاء الكتابة.
بعيدًا عن منصات Apple، يتم استخدام Swift بشكل متزايد للتطوير من جانب الخادم (Vapor، Hummingbird)، والتطبيقات عبر الأنظمة الأساسية، وحتى التعلم الآلي (Apple’s Create ML). مع تقديم Swift على الخادم والدعم عبر الأنظمة الأساسية، أصبحت Swift أكثر من مجرد "لغة Apple".
---

## لماذا يهم سويفت
- **معيار نظام Apple الأساسي**: اللغة الأساسية لتطوير iOS وmacOS وwatchOS وtvOS وvisionOS.
- **السلامة حسب التصميم**: الاختيارية تقضي على أعطال المؤشر الفارغ. أنواع القيمة تمنع حدوث طفرة غير مقصودة.
- **الأداء**: يتم التجميع إلى كود الجهاز الأصلي عبر LLVM - وهو منافس لـ C++ في العديد من المهام.
- **بناء الجملة الحديث**: واضح ومعبر، مع عمليات الإغلاق والأسماء العامة والبرمجة الموجهة نحو البروتوكول ومطابقة الأنماط.
- **SwiftUI**: إطار عمل تعريفي لواجهة المستخدم يجعل بناء واجهات نظام Apple الأساسي سريعًا وبديهيًا.
- **مصدر مفتوح**: مترجم Swift والمكتبة القياسية مفتوحان المصدر؛ يعمل على لينكس وويندوز.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **تتمحور حول التفاح** | أفضل الأدوات والنظام البيئي مخصص لمنصات Apple | استخدم Vapor من جانب الخادم؛ الدعم عبر الأنظمة الأساسية يتحسن |
| ** واجهة مستخدم رسومية محدودة عبر الأنظمة الأساسية ** | لا يوجد إطار عمل ناضج لواجهة المستخدم الرسومية لنظام التشغيل Windows/Linux | استخدم تقنيات الويب أو Flutter عبر الأنظمة الأساسية |
| **سوق عمل أصغر (خارج شركة Apple)** | أدوار أقل من Java أو Python أو JavaScript | أدوار تطوير iOS/macOS وفيرة |
| **التطور السريع** | يمكن أن تؤدي التغييرات المتكررة في بناء الجملة بين الإصدارات إلى كسر التعليمات البرمجية | إصدارات Pin Swift؛ استخدم مدير الحزم سويفت |
| ** تجميع الأوقات ** | قد يكون تجميع التعليمات البرمجية العامة المعقدة بطيئًا | تبسيط تعبيرات الكتابة؛ استخدم @inlinable بحكمة |
---

## أساسيات بناء الجملة
### المتغيرات والثوابت
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

### الاختيارات - حل Swift للقيمة Null
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

### الوظائف والإغلاقات
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

### البروتوكولات والهياكل
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

### معالجة الأخطاء
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة
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

### مطابقة الأنماط المتقدمة
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

### أغلفة الخصائص وبناة النتائج
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

## التزامن والتوازي (التزامن السريع)
### غير متزامن/انتظار
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

### التزامن المنظم
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

## تكوين المشروع ونظام البناء
### هيكل المشروع (الحزمة السريعة)
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

### الحزمة.سويفت
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

### الأوامر الأساسية
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### إطار عمل XCTest
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

## إمكانية التشغيل البيني
### التشغيل المتداخل للهدف-C
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

### C التشغيل المتداخل
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## أنماط التصميم
### نمط المندوب
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

### تصميم موجه نحو البروتوكول
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

## الأداء والتحسين
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

## SwiftUI - واجهة المستخدم التعريفية
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

## النشر
### سويفت من جانب الخادم
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

للإنتاج، قم بنشر الملف الثنائي المترجم إلى خادم Linux الذي يقوم بتشغيل Ubuntu. استخدم مدير العمليات مثل systemd لإدارة دورة حياة التطبيق.
---

## متى تستخدم سويفت
| السيناريو | لماذا سويفت | البديل الأفضل |
|----------|-------------------------|---|
| تطبيقات iOS/macOS | لغة أبل القياسية | -- |
| تطبيقات watchOS/visionOS | الخيار الوحيد | -- |
| جانب الخادم (بخار) | النظام البيئي المتنامي | اذهب، Node.js لأنظمة خوادم أكثر نضجًا |
| عبر منصة المحمول | ممكن ولكن ليس أساسي | رفرفة، رد فعل أصلي |
| برمجة الأنظمة | ممكن (لينكس) | الصدأ، C، C++ |
| مطور التطبيقات العامة (غير Apple) | النظام البيئي المحدود | بايثون، جو، جافا |
---

## أسئلة وأجوبة اصطناعية
### س1: ما هي الاختيارات، ولماذا يجبرني Swift على فكها؟
**A:** تمثل القيمة الاختيارية (`Type?`) قيمة قد تكون غائبة — وهي إما`.some(value)`أو`.none`(لا شيء). يفرض Swift إلغاء التغليف بشكل صريح لمنع تعطل المؤشر الفارغ في وقت التشغيل. يمكنك إلغاء التغليف باستخدام`if let`أو`guard let`أو فرض الإلغاء (`!`) أو التسلسل الاختياري (`?.`) أو الدمج الصفري (`??`). يضمن لك المترجم التعامل مع حالة الصفر، مما يزيل فئة كاملة من الأخطاء.
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

### س2: ما الفرق بين البنيات والفئات في Swift؟
**أ:** الهياكل هي أنواع قيم (منسوخة عند المهمة)، والفئات هي أنواع مرجعية (مشتركة). تحصل Structs على أداة تهيئة مجانية للأعضاء، وهي تدعم جميع ميزات الفئات باستثناء الميراث وإلغاء التهيئة والعد المرجعي. أنواع مكتبات Swift القياسية (`String`,`Array`,`Dictionary`) كلها بنيات. تفضل البنيات بشكل افتراضي؛ استخدم الفئات عندما تحتاج إلى حالة أو وراثة مشتركة قابلة للتغيير.
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

### س3: كيف تعمل البروتوكولات والبرمجة الموجهة نحو البروتوكول؟
**أ:** تحدد البروتوكولات مخططًا للطرق والخصائص والمتطلبات. يمكن لأي نوع أن يتوافق مع البروتوكول من خلال تنفيذ متطلباته. توفر امتدادات البروتوكول تطبيقات افتراضية. تمنحك الأدوية العامة المقيدة بالبروتوكولات تعدد الأشكال دون تحمل عبء وراثة الفئة - وهذا هو "البرمجة الموجهة نحو البروتوكول".
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

### Q4: ما هو`async/await`في Swift، وما علاقته بالممثلين؟
**أ:** يستخدم نموذج التزامن الخاص بـ Swift (5.5+)`async/await`للتعليمات البرمجية غير المتزامنة و`actors` للحالة المشتركة الآمنة القابلة للتغيير.  يمكن تعليق واستئناف وظائف `async`.  يشير`await`إلى نقاط التعليق. تمنع الجهات الفاعلة سباقات البيانات عن طريق تسلسل الوصول إلى حالتها القابلة للتغيير، ويفرض المترجم ذلك في وقت الترجمة.
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

### س5: كيف تعمل مغلفات الخصائص ومنشئي النتائج؟
**أ:** تضيف أغلفة الخصائص (`@propertyWrapper`) منطقًا إلى تخزين الخصائص (مثل`@State`في SwiftUI). يتيح لك منشئو النتائج (`@resultBuilder`) إنشاء هياكل البيانات باستخدام بناء الجملة الطبيعي (مثل التسلسل الهرمي لعرض SwiftUI). كلاهما شكل من أشكال البرمجة الفوقية التي تقلل من النمطية.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: إنشاء جهاز توجيه آمن النوع
**بيان المشكلة:** قم بإنشاء موجه URL آمن النوع لتطبيق iOS حيث يحتوي كل مسار على معلمات مرتبطة، ويمنع المترجم الوصول إلى المعلمات غير الموجودة لمسار معين.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) تعريفات المسار مع المعلمات المكتوبة، (2) تحليل عنوان URL لاستخراج معلمات المسار +، (3) الوصول الآمن إلى المعلمات - يضمن المترجم أنك تقرأ فقط المعلمات الموجودة لكل مسار. وهذا يتطلب التعدادات مع القيم المرتبطة.
**الخطوة الثانية — تحديد النهج:**
- استخدم التعداد مع القيم المرتبطة لتحديد المسارات.
- تحمل كل حالة معلماتها المحددة كقيم مكتوبة.
- يقوم المحلل اللغوي بتحويل سلاسل URL لتوجيه حالات التعداد.
- مطابقة الأنماط لاستخراج المعلمات مع أمان وقت الترجمة.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- سلامة النوع: تحمل كل حالة مسار المعلمات التي تحتاجها بالضبط. يمنع المترجم الوصول إلى`variant`على `.userProfile`.
- الاستنفاد: يجب أن يتعامل`switch`مع جميع الحالات - فإضافة مسار جديد يفرض تحديث جميع المعالجات.
- القابلية للتوسعة: إضافة مسارات جديدة عن طريق إضافة حالات التعداد؛ يخبرك المترجم في كل مكان يحتاج إلى التحديث.
- الإنتاج: فكر في توجيه`swift-url-routing`أو`TCA`للتطبيقات الأكبر حجمًا.
### المشكلة الثانية: تنفيذ حاوية الحالة التفاعلية
**بيان المشكلة:** أنشئ حاوية حالة تفاعلية بسيطة (على غرار Redux/Vuex) في Swift حيث يمكن ملاحظة تغييرات الحالة، ويتم إخطار المشتركين بتغييرات محددة في الحالة.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) حاوية حالة تحمل حالة التطبيق، (2) إجراءات تصف تغييرات الحالة، (3) مُخفض ينتج حالة جديدة من الحالة الحالية + الإجراء، (4) مشتركون يراقبون تغييرات الحالة. هذا هو نمط تدفق البيانات أحادي الاتجاه.
**الخطوة الثانية — تحديد النهج:**
- استخدم فئة`Store<State>`عامة مع سلوك يشبه `@Published`.
- تعريف الإجراءات باعتبارها التعداد.
- استخدم وظيفة المخفض`(State, Action) -> State`.
- يحصل المشتركون على الحالة الجديدة عن طريق عمليات الإغلاق.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- التدفق أحادي الاتجاه: الإجراءات ← المخفض ← الحالة الجديدة ← المشتركون. من السهل التفكير والاختبار.
- سلامة الخيط: تقوم قائمة انتظار الإرسال بتسلسل طفرات الحالة.
- يحصل المشتركون على الحالة الكاملة — استخدم المحددات أو عمليات فحص`Equatable`لتجنب عمليات إعادة العرض غير الضرورية.
- الإنتاج: استخدم`The Composable Architecture`(TCA) بواسطة Point-Free للتنفيذ على مستوى الإنتاج مع التأثيرات والاختبار وتكامل SwiftUI.
---

## ملخص
Swift هي لغة حديثة وآمنة ومعبرة وهي ضرورية لتطوير منصة Apple. إن تركيزه على السلامة (الاختيارات، وأنواع القيم، ومطابقة الأنماط) يمنع فئات كاملة من الأخطاء. بعيدًا عن منصات Apple، تنمو Swift في مجال التطوير من جانب الخادم والتطبيقات عبر الأنظمة الأساسية. بالنسبة لتطوير iOS/macOS، يعد Swift هو الخيار الواضح. بالنسبة للمجالات الأخرى، فهي لغة قادرة مع نظام بيئي أصغر ولكنه متنامي.