---
# فراداده
عنوان: "سوئیفت"
توضیحات: "مرجع جامع برای زبان برنامه نویسی سوئیفت که شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن می شود."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [سریع، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "26 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
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

## خلاصه
Swift یک زبان مدرن، ایمن و رسا است که برای توسعه پلتفرم اپل ضروری است. تاکید آن بر ایمنی (اختیاری، انواع ارزش، تطبیق الگو) از کل دسته‌بندی اشکالات جلوگیری می‌کند. سوئیفت فراتر از پلتفرم های اپل، در توسعه سمت سرور و برنامه های کاربردی چند پلتفرمی در حال رشد است. برای توسعه iOS/macOS، سوئیفت انتخاب واضحی است. برای سایر حوزه‌ها، زبانی توانا با اکوسیستم کوچک‌تر اما در حال رشد است.