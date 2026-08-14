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

# Nhanh
Swift là ngôn ngữ lập trình được biên dịch, hiện đại do Apple (do Chris Lattner dẫn đầu) phát triển và phát hành lần đầu tiên vào năm 2014. Nó được thiết kế để thay thế Objective-C làm ngôn ngữ chính để phát triển nền tảng Apple (iOS, macOS, watchOS, tvOS, VisionOS). Swift kết hợp hiệu suất của các ngôn ngữ được biên dịch với tính biểu cảm của các ngôn ngữ kịch bản và nó nhấn mạnh đến sự an toàn -- đặc biệt là về giá trị null, quản lý bộ nhớ và lỗi loại.
Ngoài các nền tảng của Apple, Swift ngày càng được sử dụng nhiều để phát triển phía máy chủ (Vapor, Hummingbird), các ứng dụng đa nền tảng và thậm chí cả máy học (Creat ML của Apple). Với việc giới thiệu Swift trên Máy chủ và hỗ trợ đa nền tảng, Swift không chỉ trở thành một "ngôn ngữ của Apple".
---

## Tại sao Swift lại quan trọng
- **Tiêu chuẩn nền tảng Apple**: Ngôn ngữ chính để phát triển iOS, macOS, watchOS, tvOS và VisionOS.
- **An toàn theo thiết kế**: Các tùy chọn loại bỏ sự cố con trỏ null. Các loại giá trị ngăn ngừa đột biến ngoài ý muốn.
- **Hiệu suất**: Biên dịch thành mã máy gốc thông qua LLVM -- cạnh tranh với C++ cho nhiều tác vụ.
- **Cú pháp hiện đại**: Rõ ràng, biểu cảm, có các phần đóng, tổng quát, lập trình hướng giao thức và khớp mẫu.
- **SwiftUI**: Khung giao diện người dùng khai báo giúp xây dựng giao diện nền tảng Apple nhanh chóng và trực quan.
- **Mã nguồn mở**: Trình biên dịch Swift và thư viện chuẩn là nguồn mở; chạy trên Linux và Windows.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Lấy Apple làm trung tâm** | Hệ sinh thái và công cụ tốt nhất dành cho nền tảng Apple | Sử dụng Vapor cho phía máy chủ; hỗ trợ đa nền tảng đang được cải thiện |
| **GUI đa nền tảng có giới hạn** | Không có khung GUI hoàn thiện cho Windows/Linux | Sử dụng công nghệ web hoặc Flutter cho đa nền tảng |
| **Thị trường việc làm nhỏ hơn (bên ngoài Apple)** | Ít vai trò hơn Java, Python hoặc JavaScript | Vai trò phát triển iOS/macOS rất phong phú |
| **Tiến hóa nhanh** | Thay đổi cú pháp thường xuyên giữa các phiên bản có thể phá mã | Ghim các phiên bản Swift; sử dụng Trình quản lý gói Swift |
| **Số lần biên dịch** | Mã chung phức tạp có thể biên dịch chậm | Đơn giản hóa các biểu thức kiểu; sử dụng @inlinable một cách thận trọng |
---

##Cơ bản về cú pháp
### Biến và hằng
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

### Tùy chọn -- Giải pháp của Swift cho Null
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

### Chức năng và đóng cửa
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

### Giao thức và cấu trúc
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

### Xử lý lỗi
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

## Cú pháp & Mẫu nâng cao
### Thuốc gốc
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

### So khớp mẫu nâng cao
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

### Trình bao bọc thuộc tính và Trình tạo kết quả
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

## Đồng thời & Song song (Đồng thời nhanh chóng)
### không đồng bộ/đang chờ
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

### Đồng thời có cấu trúc
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án (Gói Swift)
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

### Gói.swift
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

### Các lệnh cần thiết
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### Khung XCTest
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

## Khả năng tương tác
### Tương tác Objective-C
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

### Tương tác C
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Mẫu thiết kế
### Mẫu đại biểu
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

### Thiết kế hướng giao thức
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

## Hiệu suất & Tối ưu hóa
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

## SwiftUI -- Giao diện người dùng khai báo
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

## Triển khai
### Swift phía máy chủ
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Để sản xuất, hãy triển khai tệp nhị phân đã biên dịch lên máy chủ Linux chạy Ubuntu. Sử dụng trình quản lý quy trình như systemd để quản lý vòng đời ứng dụng.
---

## Khi nào nên sử dụng Swift
| Kịch bản | Tại sao Swift | Thay thế tốt hơn |
|----------|----------|-------------------|
| Ứng dụng iOS/macOS | Ngôn ngữ tiêu chuẩn của Apple | -- |
| ứng dụng watchOS/visionOS | Tùy chọn duy nhất | -- |
| Phía máy chủ (Vapor) | Hệ sinh thái đang phát triển | Đi, Node.js để có hệ sinh thái máy chủ trưởng thành hơn |
| Di động đa nền tảng | Có thể nhưng không phải chính | Flutter, React Native |
| Lập trình hệ thống | Có thể (Linux) | Rust, C, C++ |
| Nhà phát triển ứng dụng chung (không phải của Apple) | Hệ sinh thái hạn chế | Python, Go, Java |
---

## Hỏi đáp tổng hợp
### Q1: Tùy chọn là gì và tại sao Swift buộc tôi phải mở khóa chúng?
**A:** Một tùy chọn (`Type?`) đại diện cho một giá trị có thể không có — đó là`.some(value)`hoặc`.none`(nil). Swift buộc phải hủy ghép nối rõ ràng để ngăn chặn sự cố con trỏ null khi chạy. Bạn có thể mở gói bằng`if let`,`guard let`, buộc mở gói (`!`), chuỗi tùy chọn (`?.`) hoặc kết hợp không (`??`). Trình biên dịch đảm bảo bạn xử lý được trường hợp không - điều này giúp loại bỏ toàn bộ lớp lỗi.
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

### Câu 2: Sự khác biệt giữa struct và class trong Swift là gì?
**A:** Cấu trúc là loại giá trị (được sao chép khi gán), lớp là loại tham chiếu (được chia sẻ). Các cấu trúc có được trình khởi tạo thành viên miễn phí và chúng hỗ trợ tất cả các tính năng của các lớp ngoại trừ tính kế thừa, bộ khử khởi tạo và tính tham chiếu. Các loại thư viện tiêu chuẩn của Swift (`String`,`Array`,`Dictionary`) đều là cấu trúc. Ưu tiên cấu trúc theo mặc định; sử dụng các lớp khi bạn cần chia sẻ trạng thái có thể thay đổi hoặc kế thừa.
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

### Câu 3: Các giao thức và lập trình hướng giao thức hoạt động như thế nào?
**A:** Các giao thức xác định bản thiết kế chi tiết về các phương thức, thuộc tính và yêu cầu. Bất kỳ loại nào cũng có thể tuân theo một giao thức bằng cách thực hiện các yêu cầu của nó. Tiện ích mở rộng giao thức cung cấp các triển khai mặc định. Các gen chung bị ràng buộc bởi các giao thức mang lại cho bạn tính đa hình mà không cần phải thừa kế lớp - đây là "lập trình hướng giao thức".
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

### Q4:`async/await`trong Swift là gì và nó liên quan thế nào đến diễn viên?
**A:** Mô hình đồng thời của Swift (5.5+) sử dụng`async/await`cho mã không đồng bộ và`actors`cho trạng thái có thể thay đổi được chia sẻ an toàn.  Các chức năng`async`có thể bị tạm dừng và tiếp tục lại. `await`đánh dấu các điểm treo. Các tác nhân ngăn chặn việc chạy đua dữ liệu bằng cách tuần tự hóa quyền truy cập vào trạng thái có thể thay đổi của chúng — trình biên dịch thực thi điều này tại thời điểm biên dịch.
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

### Câu hỏi 5: Trình bao bọc thuộc tính và trình tạo kết quả hoạt động như thế nào?
**A:** Trình bao bọc thuộc tính (`@propertyWrapper`) thêm logic vào bộ nhớ thuộc tính (như`@State`trong SwiftUI). Trình tạo kết quả (`@resultBuilder`) cho phép bạn xây dựng cấu trúc dữ liệu bằng cú pháp tự nhiên (như phân cấp chế độ xem của SwiftUI). Cả hai đều là hình thức lập trình siêu dữ liệu giúp giảm bớt bản soạn sẵn.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xây dựng một Type-Safe Router
**Báo cáo sự cố:** Tạo bộ định tuyến URL loại an toàn cho ứng dụng iOS trong đó mỗi tuyến có các tham số liên quan và trình biên dịch ngăn truy cập các tham số không tồn tại cho một tuyến nhất định.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) định nghĩa tuyến đường với các tham số đã nhập, (2) phân tích cú pháp URL để trích xuất tuyến + tham số, (3) truy cập tham số an toàn loại - trình biên dịch đảm bảo bạn chỉ đọc các tham số tồn tại cho mỗi tuyến. Điều này đòi hỏi enum với các giá trị liên quan.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng enum với các giá trị liên quan để xác định tuyến đường.
- Mỗi trường hợp mang các tham số cụ thể của nó dưới dạng giá trị được gõ.
- Trình phân tích cú pháp chuyển đổi chuỗi URL thành các trường hợp định tuyến enum.
- Khớp mẫu trích xuất các tham số với sự an toàn trong thời gian biên dịch.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Loại an toàn: mỗi trường hợp tuyến đường mang chính xác các thông số cần thiết. Trình biên dịch ngăn truy cập`variant`trên`.userProfile`.
- Tính đầy đủ:`switch`phải xử lý tất cả các trường hợp — việc thêm một tuyến đường mới buộc phải cập nhật tất cả các trình xử lý.
- Khả năng mở rộng: thêm các tuyến đường mới bằng cách thêm các trường hợp enum; trình biên dịch sẽ cho bạn biết mọi nơi cần cập nhật.
- Sản xuất: xem xét định tuyến của`swift-url-routing`hoặc`TCA`cho các ứng dụng lớn hơn.
### Vấn đề 2: Triển khai Reactive State Container
**Báo cáo vấn đề:** Xây dựng một vùng chứa trạng thái phản ứng đơn giản (tương tự như Redux/Vuex) trong Swift nơi có thể quan sát được các thay đổi trạng thái và người đăng ký được thông báo về các thay đổi trạng thái cụ thể.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng ta cần: (1) một thùng chứa trạng thái chứa trạng thái ứng dụng, (2) các hành động mô tả các thay đổi trạng thái, (3) một bộ giảm tốc tạo ra trạng thái mới từ trạng thái hiện tại + hành động, (4) người đăng ký quan sát các thay đổi trạng thái. Đây là mô hình luồng dữ liệu một chiều.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng lớp`Store<State>`chung có hành vi giống `@Published`.
- Xác định hành động như một enum.
- Sử dụng chức năng giảm tốc `(State, Action) -> State`.
- Người đăng ký nhận được trạng thái mới thông qua việc đóng cửa.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Luồng một chiều: hành động → bộ giảm tốc → trạng thái mới → người đăng ký. Dễ dàng lý luận và kiểm tra.
- An toàn luồng: hàng đợi gửi tuần tự hóa các đột biến trạng thái.
- Người đăng ký nhận được trạng thái đầy đủ — sử dụng bộ chọn hoặc kiểm tra`Equatable`để tránh hiển thị lại không cần thiết.
- Sản xuất: sử dụng`The Composable Architecture`(TCA) của Point-Free để triển khai ở cấp độ sản xuất với các hiệu ứng, thử nghiệm và tích hợp SwiftUI.
---

## Bản tóm tắt
Swift là ngôn ngữ hiện đại, an toàn và biểu cảm, cần thiết cho sự phát triển nền tảng của Apple. Nó nhấn mạnh vào sự an toàn (tùy chọn, loại giá trị, khớp mẫu) ngăn chặn toàn bộ danh mục lỗi. Ngoài các nền tảng của Apple, Swift đang phát triển trong lĩnh vực phát triển phía máy chủ và các ứng dụng đa nền tảng. Để phát triển iOS/macOS, Swift là sự lựa chọn rõ ràng. Đối với các miền khác, đây là ngôn ngữ có khả năng với hệ sinh thái nhỏ hơn nhưng đang phát triển.