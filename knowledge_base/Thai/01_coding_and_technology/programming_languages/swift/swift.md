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

#สวิฟท์
Swift เป็นภาษาโปรแกรมคอมไพล์สมัยใหม่ที่พัฒนาโดย Apple (นำโดย Chris Lattner) และเปิดตัวครั้งแรกในปี 2014 ได้รับการออกแบบมาเพื่อแทนที่ Objective-C ในฐานะภาษาหลักสำหรับการพัฒนาแพลตฟอร์ม Apple (iOS, macOS, watchOS, tvOS, VisionOS) Swift ผสมผสานประสิทธิภาพของภาษาที่คอมไพล์เข้ากับความหมายของภาษาสคริปต์ และเน้นเรื่องความปลอดภัย โดยเฉพาะเกี่ยวกับค่า Null การจัดการหน่วยความจำ และข้อผิดพลาดด้านประเภท
นอกเหนือจากแพลตฟอร์มของ Apple แล้ว Swift ยังถูกใช้มากขึ้นเพื่อการพัฒนาฝั่งเซิร์ฟเวอร์ (Vapor, Hummingbird), แอปพลิเคชันข้ามแพลตฟอร์ม และแม้แต่การเรียนรู้ของเครื่อง (Create ML ของ Apple) ด้วยการเปิดตัว Swift บนเซิร์ฟเวอร์และการรองรับข้ามแพลตฟอร์ม Swift จึงเป็นมากกว่า "ภาษาของ Apple"
---

## ทำไม Swift ถึงสำคัญ
- **มาตรฐานแพลตฟอร์ม Apple**: ภาษาหลักสำหรับการพัฒนา iOS, macOS, watchOS, tvOS และ VisionOS
- **ความปลอดภัยตามการออกแบบ**: ตัวเลือกเสริมช่วยขจัดปัญหาตัวชี้ว่าง ประเภทค่าป้องกันการกลายพันธุ์โดยไม่ได้ตั้งใจ
- **ประสิทธิภาพ**: คอมไพล์เป็นโค้ดเครื่องเนทิฟผ่าน LLVM -- แข่งขันกับ C++ สำหรับงานหลายอย่างได้
- **ไวยากรณ์สมัยใหม่**: สะอาดตา แสดงออกชัดเจน พร้อมการปิด ทั่วไป การเขียนโปรแกรมเชิงโปรโตคอล และการจับคู่รูปแบบ
- **SwiftUI**: เฟรมเวิร์ก UI ที่ประกาศซึ่งทำให้การสร้างอินเทอร์เฟซแพลตฟอร์ม Apple รวดเร็วและใช้งานง่าย
- **โอเพ่นซอร์ส**: คอมไพเลอร์ Swift และไลบรารีมาตรฐานเป็นโอเพ่นซอร์ส ทำงานบน Linux และ Windows
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **แอปเปิ้ลเป็นศูนย์กลาง** | เครื่องมือและระบบนิเวศที่ดีที่สุดสำหรับแพลตฟอร์ม Apple | ใช้ Vapor สำหรับฝั่งเซิร์ฟเวอร์ การสนับสนุนข้ามแพลตฟอร์มกำลังปรับปรุง |
| **GUI ข้ามแพลตฟอร์มจำกัด** | ไม่มีเฟรมเวิร์ก GUI ที่เป็นผู้ใหญ่สำหรับ Windows/Linux | ใช้เทคโนโลยีเว็บหรือ Flutter สำหรับข้ามแพลตฟอร์ม |
| **ตลาดงานเล็กลง (นอก Apple)** | บทบาทน้อยกว่า Java, Python หรือ JavaScript | บทบาทการพัฒนา iOS/macOS มีมากมาย |
| **วิวัฒนาการอย่างรวดเร็ว** | การเปลี่ยนแปลงไวยากรณ์บ่อยครั้งระหว่างเวอร์ชันต่างๆ อาจทำให้โค้ดเสียหาย | ปักหมุดเวอร์ชัน Swift; ใช้ Swift Package Manager |
| **เวลาในการคอมไพล์** | รหัสทั่วไปที่ซับซ้อนสามารถคอมไพล์ได้ช้า | ลดความซับซ้อนของนิพจน์ประเภท ใช้ @inlinable อย่างรอบคอบ |
---

## พื้นฐานไวยากรณ์
### ตัวแปรและค่าคงที่
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

### ตัวเลือก - วิธีแก้ปัญหาของ Swift เป็น Null
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

### ฟังก์ชั่นและการปิด
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

### โปรโตคอลและโครงสร้าง
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

### การจัดการข้อผิดพลาด
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ทั่วไป
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

### การจับคู่รูปแบบขั้นสูง
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

### ตัวห่อคุณสมบัติและตัวสร้างผลลัพธ์
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

## เห็นพ้องและความเท่าเทียม (Swift Concurrency)
### ไม่พร้อมกัน/รอ
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

### การทำงานพร้อมกันอย่างมีโครงสร้าง
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ (Swift Package)
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

### แพ็คเกจสวิฟท์
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

### คำสั่งที่จำเป็น
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### กรอบงาน XCTest
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

## การทำงานร่วมกัน
### วัตถุประสงค์-C Interop
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

### ซี อินเตอร์ออป
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## รูปแบบการออกแบบ
### รูปแบบการมอบหมาย
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

### การออกแบบเชิงโปรโตคอล
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
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

## SwiftUI - UI ที่ประกาศ
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

## การปรับใช้
### Swift ฝั่งเซิร์ฟเวอร์
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

สำหรับการใช้งานจริง ให้ปรับใช้ไบนารีที่คอมไพล์แล้วกับเซิร์ฟเวอร์ Linux ที่ใช้ Ubuntu ใช้ตัวจัดการกระบวนการเช่น systemd เพื่อจัดการวงจรการใช้งานของแอปพลิเคชัน
---

## เมื่อใดควรใช้ Swift
| สถานการณ์ | ทำไมต้องสวิฟท์ | ทางเลือกที่ดีกว่า |
|----------|----------|-------------------|
| แอพ iOS/macOS | ภาษามาตรฐานของ Apple | -- |
| แอพ watchOS/visionOS | ตัวเลือกเท่านั้น | -- |
| ฝั่งเซิร์ฟเวอร์ (ไอ) | ระบบนิเวศที่กำลังเติบโต | ไป Node.js สำหรับระบบนิเวศเซิร์ฟเวอร์ที่สมบูรณ์ยิ่งขึ้น |
| มือถือข้ามแพลตฟอร์ม | เป็นไปได้แต่ไม่ใช่หลัก | กระพือ, ตอบสนองพื้นเมือง |
| การเขียนโปรแกรมระบบ | เป็นไปได้ (Linux) | สนิม, C, C++ |
| dev แอปพลิเคชันทั่วไป (ไม่ใช่ Apple) | ระบบนิเวศที่จำกัด | Python, Go, Java |
---

## สรุป
Swift เป็นภาษาที่ทันสมัย ​​ปลอดภัย และแสดงออกซึ่งจำเป็นสำหรับการพัฒนาแพลตฟอร์มของ Apple การเน้นเรื่องความปลอดภัย (ตัวเลือก, ประเภทค่า, การจับคู่รูปแบบ) ป้องกันข้อผิดพลาดทั้งหมวดหมู่ นอกเหนือจากแพลตฟอร์มของ Apple แล้ว Swift ยังเติบโตในด้านการพัฒนาฝั่งเซิร์ฟเวอร์และแอปพลิเคชันข้ามแพลตฟอร์ม สำหรับการพัฒนา iOS/macOS นั้น Swift คือตัวเลือกที่ชัดเจน สำหรับโดเมนอื่นๆ นี่เป็นภาษาที่มีความสามารถและมีระบบนิเวศที่เล็กกว่าแต่กำลังเติบโต