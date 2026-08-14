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

# 斯威夫特
Swift 是一种现代编译型编程语言，由 Apple（由 Chris Lattner 领导）开发，于 2014 年首次发布。它旨在取代 Objective-C，成为 Apple 平台开发（iOS、macOS、watchOS、tvOS、visionOS）的主要语言。 Swift 将编译语言的性能与脚本语言的表达能力结合在一起，并且强调安全性——特别是在空值、内存管理和类型错误方面。
除了 Apple 平台之外，Swift 越来越多地用于服务器端开发（Vapor、Hummingbird）、跨平台应用程序，甚至机器学习（Apple 的 Create ML）。随着 Swift on Server 和跨平台支持的推出，Swift 不再只是一种“Apple 语言”。
---

## 为什么 Swift 很重要
- **Apple 平台标准**：iOS、macOS、watchOS、tvOS 和 VisionOS 开发的主要语言。
- **设计安全**：选项消除了空指针崩溃。值类型可以防止意外的突变。
- **性能**：通过 LLVM 编译为本机机器代码——在许多任务上可与 C++ 竞争。
- **现代语法**：干净、富有表现力、带有闭包、泛型、面向协议的编程和模式匹配。
- **SwiftUI**：声明式 UI 框架，使构建 Apple 平台界面变得快速而直观。
- **开源**：Swift编译器和标准库都是开源的；在 Linux 和 Windows 上运行。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **以苹果为中心** |最好的工具和生态系统是针对Apple平台的|服务器端使用Vapor；跨平台支持正在改进|
| **有限的跨平台 GUI** | Windows/Linux 尚无成熟的 GUI 框架 |使用 Web 技术或 Flutter 实现跨平台 |
| **就业市场较小（苹果以外）** |角色数量少于 Java、Python 或 JavaScript | iOS/macOS 开发角色丰富 |
| **快速进化** |版本之间频繁的语法更改可能会破坏代码 |固定 Swift 版本；使用 Swift 包管理器 |
| **编译时间** |复杂的通用代码编译速度可能会很慢 |简化类型表达式；明智地使用@inlinable |
---

## 语法基础知识
### 变量和常量
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

### 可选值——Swift 的 Null 解决方案
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

### 函数和闭包
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

### 协议和结构
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

### 错误处理
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

## 高级语法和模式
### 泛型
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

### 高级模式匹配
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

### 属性包装器和结果生成器
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

## 并发与并行（Swift Concurrency）
### 异步/等待
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

### 结构化并发
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

## 项目配置和构建系统
### 项目结构（Swift 包）
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

### 包.swift
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

### 基本命令
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD 管道 (GitHub Actions)
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

## 测试
### XCTest框架
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

## 互操作性
### Objective-C 互操作
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

### C 互操作
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## 设计模式
### 委托模式
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

### 面向协议的设计
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

## 性能与优化
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

## SwiftUI -- 声明式 UI
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

## 部署
### 服务器端 Swift
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

对于生产，将编译的二进制文件部署到运行 Ubuntu 的 Linux 服务器。使用 systemd 等流程管理器来管理应用程序生命周期。
---

## 何时使用 Swift
|场景|为什么选择斯威夫特 |更好的选择|
|----------|----------|--------------------|
| iOS/macOS 应用 |标准Apple语言| --|
| watchOS/visionOS 应用 |唯一的选择| --|
|服务器端（Vapor）|不断发展的生态系统 | Go、Node.js 打造更成熟的服务器生态系统 |
|跨平台移动|可能但不是主要的 | Flutter、React Native |
|系统编程|可能（Linux）| Rust、C、C++ |
|通用应用程序开发（非Apple）|有限的生态系统| Python、Go、Java |
---

## 综合问答
### Q1：什么是可选值，为什么 Swift 强迫我解开它们？
**A:** 可选 (`Type?`) 表示可能不存在的值 — 它是`.some(value)`或`.none`(nil)。 Swift 强制显式展开以防止运行时空指针崩溃。您可以使用`if let`、`guard let`、强制解包 (`!`)、可选链接 (`?.`) 或零合并 (`??`) 进行解包。编译器确保您处理 nil 情况 - 这消除了一整类错误。
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

### Q2：Swift 中的结构体和类有什么区别？
**A:** 结构是值类型（在赋值时复制），类是引用类型（共享）。结构体有一个免费的成员初始化器，并且它们支持类的所有功能，除了继承、反初始化器和引用计数之外。 Swift 的标准库类型（`String`、`Array`、`Dictionary`）都是结构体。默认情况下更喜欢结构体；当您需要共享可变状态或继承时，请使用类。
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

### Q3：协议和面向协议的编程如何工作？
**答：** 协议定义了方法、属性和要求的蓝图。任何类型都可以通过实现其要求来符合协议。协议扩展提供默认实现。受协议约束的泛型为您提供多态性，而无需类继承的开销——这就是“面向协议的编程”。
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

### Q4：Swift 中的`async/await`是什么？它与 actor 有何关系？
**答：** Swift 的并发模型 (5.5+) 使用`async/await`进行异步代码，使用`actors`进行安全共享可变状态。 `async`功能可以暂停和恢复。 `await`标记悬挂点。参与者通过序列化对其可变状态的访问来防止数据竞争——编译器在编译时强制执行此操作。
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

### Q5：属性包装器和结果生成器如何工作？
**A:** 属性包装器 (`@propertyWrapper`) 向属性存储添加逻辑（如 SwiftUI 中的`@State`）。结果构建器 (`@resultBuilder`) 允许您使用自然语法（如 SwiftUI 的视图层次结构）构建数据结构。两者都是减少样板代码的元编程形式。
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

## 解决问题的思路
### 问题 1：构建类型安全的路由器
**问题陈述：** 为 iOS 应用程序创建类型安全的 URL 路由器，其中每个路由都有关联的参数，并且编译器会阻止访问给定路由不存在的参数。
**第 1 步 — 了解问题：**
我们需要：（1）带有类型化参数的路由定义，（2）URL解析以提取路由+参数，（3）类型安全的参数访问——编译器确保您只读取每个路由存在的参数。这需要具有关联值的枚举。
**第 2 步 — 确定方法：**
- 使用具有关联值的枚举来定义路由。
- 每个案例都将其特定参数作为键入值。
- 解析器将 URL 字符串转换为路由枚举情况。
- 模式匹配提取具有编译时安全性的参数。
**第 3 步 — 实施解决方案：**
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

**第 4 步 — 验证和优化：**
- 类型安全：每个路由案例都准确地携带其所需的参数。编译器阻止访问`.userProfile`上的`variant`。
- 详尽性：`switch` 必须处理所有情况 - 添加新路由会强制更新所有处理程序。
- 可扩展性：通过添加枚举案例来添加新路由；编译器会告诉您所有需要更新的地方。
- 生产：考虑`swift-url-routing`或`TCA`的大型应用程序的路由。
### 问题 2：实现反应式状态容器
**问题陈述：** 在 Swift 中构建一个简单的反应式状态容器（类似于 Redux/Vuex），其中状态更改是可观察的，并且订阅者会收到特定状态更改的通知。
**第 1 步 — 了解问题：**
我们需要：（1）一个保存应用程序状态的状态容器，（2）描述状态更改的操作，（3）一个从当前状态+操作生成新状态的reducer，（4）观察状态更改的订阅者。这就是单向数据流模式。
**第 2 步 — 确定方法：**
- 使用具有类似`@Published`行为的通用`Store<State>`类。
- 将操作定义为枚举。
- 使用减速函数`(State, Action) -> State`。
- 订阅者通过闭包接收新状态。
**第 3 步 — 实施解决方案：**
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

**第 4 步 — 验证和优化：**
- 单向流：动作→减速器→新状态→订阅者。易于推理和测试。
- 线程安全：调度队列序列化状态突变。
- 订阅者获得完整状态 - 使用选择器或`Equatable`检查以避免不必要的重新渲染。
- 生产：使用 Point-Free 的`The Composable Architecture`(TCA) 进行生产级实现，包括效果、测试和 SwiftUI 集成。
---

＃＃ 概括
Swift 是一种现代、安全且富有表现力的语言，对于 Apple 平台开发至关重要。它对安全性（可选、值类型、模式匹配）的强调可以防止整个类别的错误。除了 Apple 平台之外，Swift 在服务器端开发和跨平台应用程序方面也在不断发展。对于 iOS/macOS 开发，Swift 是明智的选择。对于其他领域来说，它是一种功能强大的语言，具有较小但不断增长的生态系统。