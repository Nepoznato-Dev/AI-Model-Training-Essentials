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
# 스위프트
Swift는 Apple(Chris Lattner 주도)에서 개발하고 2014년에 처음 출시된 현대적이고 컴파일된 프로그래밍 언어입니다. Swift는 Apple 플랫폼 개발(iOS, macOS, watchOS, tvOS, VisionOS)의 기본 언어로 Objective-C를 대체하도록 설계되었습니다. Swift는 컴파일된 언어의 성능과 스크립팅 언어의 표현력을 결합하고 특히 null 값, 메모리 관리 및 유형 오류와 관련된 안전성을 강조합니다.
Apple 플랫폼 외에도 Swift는 서버측 개발(Vapor, Hummingbird), 크로스 플랫폼 애플리케이션, 심지어 기계 학습(Apple의 Create ML)에도 점점 더 많이 사용되고 있습니다. Swift on Server 및 크로스 플랫폼 지원이 도입되면서 Swift는 단순한 "Apple 언어" 그 이상으로 변모하고 있습니다.
---

## 스위프트가 중요한 이유
- **Apple 플랫폼 표준**: iOS, macOS, watchOS, tvOS 및 VisionOS 개발을 위한 기본 언어입니다.
- **안전성을 고려한 설계**: 옵션으로 널 포인터 충돌을 제거합니다. 값 유형은 의도하지 않은 변형을 방지합니다.
- **성능**: LLVM을 통해 네이티브 기계어 코드로 컴파일 - 많은 작업에서 C++와 경쟁할 수 있습니다.
- **현대적인 구문**: 클로저, 제네릭, 프로토콜 지향 프로그래밍 및 패턴 일치를 포함하여 깔끔하고 표현력이 뛰어납니다.
- **SwiftUI**: Apple 플랫폼 인터페이스를 빠르고 직관적으로 구축할 수 있게 해주는 선언적 UI 프레임워크입니다.
- **오픈 소스**: Swift 컴파일러와 표준 라이브러리는 오픈 소스입니다. Linux와 Windows에서 실행됩니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **애플 중심** | Apple 플랫폼을 위한 최고의 도구와 생태계 | 서버 측에는 Vapor을 사용하십시오. 크로스 플랫폼 지원이 개선되고 있습니다 |
| **제한된 크로스 플랫폼 GUI** | Windows/Linux를 위한 성숙한 GUI 프레임워크가 없습니다 | 크로스 플랫폼에 웹 기술 또는 Flutter 사용 |
| **작은 채용 시장(Apple 외부)** | Java, Python 또는 JavaScript보다 역할이 적음 | iOS/macOS 개발 역할이 풍부합니다 |
| **빠른 진화** | 버전 간에 구문을 자주 변경하면 코드가 손상될 수 있음 | Swift 버전 고정; Swift 패키지 관리자 사용 |
| **컴파일 시간** | 복잡한 일반 코드는 컴파일 속도가 느릴 수 있음 | 유형 표현식을 단순화합니다. @inlinable을 신중하게 사용하세요 |
---

## 구문 기본 사항
### 변수 및 상수
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

### 옵션 -- Swift의 Null 솔루션
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

### 함수 및 클로저
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

### 프로토콜 및 구조체
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

### 오류 처리
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

## 고급 구문 및 패턴
### 제네릭
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

### 고급 패턴 매칭
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

### 속성 래퍼 및 결과 빌더
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

## 동시성 및 병렬성(신속한 동시성)
### 비동기/대기
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

### 구조화된 동시성
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조(Swift 패키지)
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

### 패키지.스위프트
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

### 필수 명령
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### XCTest 프레임워크
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

## 상호 운용성
### 오브젝티브-C 상호 운용성
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

### C 상호 운용성
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## 디자인 패턴
### 델리게이트 패턴
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

### 프로토콜 중심 설계
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

## 성능 및 최적화
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

## SwiftUI -- 선언적 UI
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

## 배포
### 서버측 Swift
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

프로덕션의 경우 컴파일된 바이너리를 Ubuntu를 실행하는 Linux 서버에 배포합니다. 애플리케이션 수명주기를 관리하려면 systemd와 같은 프로세스 관리자를 사용하세요.
---

## Swift를 사용해야 하는 경우
| 시나리오 | 왜 스위프트인가 | 더 나은 대안 |
|----------|----------|------|
| iOS/macOS 앱 | 표준 Apple 언어 | -- |
| watchOS/visionOS 앱 | 유일한 옵션 | -- |
| 서버측(Vapor) | 생태계 성장 | 더 성숙한 서버 생태계를 위한 Go, Node.js |
| 크로스 플랫폼 모바일 | 가능하지만 기본은 아님 | 플러터, 리액트 네이티브 |
| 시스템 프로그래밍 | 가능(리눅스) | 러스트, C, C++ |
| 일반 애플리케이션 개발(Apple 외) | 제한된 생태계 | 파이썬, 바둑, 자바 |
---

## 종합 Q&A
### Q1: 옵션이란 무엇이며, Swift에서 옵션을 풀도록 강요하는 이유는 무엇인가요?
**A:** 선택 사항(`Type?`)은 없을 수 있는 값을 나타냅니다. 이는`.some(value)`또는 `.none`(nil)입니다. Swift는 런타임 시 널 포인터 충돌을 방지하기 위해 명시적 언래핑을 강제합니다.`if let`,`guard let`, 강제 언랩(`!`), 선택적 체인(`?.`) 또는 nil 병합(`??`)을 사용하여 언래핑할 수 있습니다. 컴파일러는 nil 사례를 처리하도록 보장합니다. 이는 전체 버그 클래스를 제거합니다.
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

### Q2: Swift에서 구조체와 클래스의 차이점은 무엇인가요?
**답:** 구조체는 값 유형(할당 시 복사)이고 클래스는 참조 유형(공유)입니다. 구조체는 무료 멤버별 초기화 기능을 제공하며 상속, 초기화 해제 및 참조 계산을 제외한 클래스의 모든 기능을 지원합니다. Swift의 표준 라이브러리 유형(`String`,`Array`,`Dictionary`)은 모두 구조체입니다. 기본적으로 구조체를 선호합니다. 공유된 변경 가능한 상태나 상속이 필요할 때 클래스를 사용하세요.
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

### Q3: 프로토콜과 프로토콜 지향 프로그래밍은 어떻게 작동하나요?
**답변:** 프로토콜은 방법, 속성 및 요구 사항의 청사진을 정의합니다. 모든 유형은 요구사항을 구현하여 프로토콜을 준수할 수 있습니다. 프로토콜 확장은 기본 구현을 제공합니다. 프로토콜에 의해 제한된 제네릭은 클래스 상속의 오버헤드 없이 다형성을 제공합니다. 이것이 "프로토콜 지향 프로그래밍"입니다.
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

### Q4: Swift의 `async/await`는 무엇이며 액터와 어떤 관련이 있나요?
**A:** Swift의 동시성 모델(5.5+)은 비동기 코드에 `async/await`를 사용하고 안전한 공유 변경 가능 상태에 `actors`를 사용합니다. `async`기능을 일시 중지하고 재개할 수 있습니다.  `await`는 정지 지점을 표시합니다. 행위자는 변경 가능한 상태에 대한 액세스를 직렬화하여 데이터 경합을 방지합니다. 컴파일러는 컴파일 타임에 이를 시행합니다.
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

### Q5: 속성 래퍼와 결과 빌더는 어떻게 작동하나요?
**A:** 속성 래퍼( ​​`@propertyWrapper` )는 속성 저장소(예: SwiftUI의 `@State`)에 논리를 추가합니다. 결과 빌더(`@resultBuilder`)를 사용하면 SwiftUI의 뷰 계층 구조와 같은 자연 구문을 사용하여 데이터 구조를 구축할 수 있습니다. 둘 다 상용구를 줄이는 메타 프로그래밍 형태입니다.
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

## 사고 사슬 문제 해결
### 문제 1: 유형 안전 라우터 구축
**문제 설명:** 각 경로에 연결된 매개변수가 있는 iOS 앱에 대해 유형이 안전한 URL 라우터를 생성하고 컴파일러는 지정된 경로에 존재하지 않는 매개변수에 액세스하는 것을 방지합니다.
**1단계 - 문제 이해:**
(1) 형식화된 매개변수가 있는 경로 정의, (2) 경로 + 매개변수를 추출하기 위한 URL 구문 분석, (3) 유형이 안전한 매개변수 액세스 — 컴파일러는 각 경로에 존재하는 매개변수만 읽도록 보장합니다. 여기에는 연관된 값이 있는 열거형이 필요합니다.
**2단계 - 접근 방식 파악:**
- 관련 값과 함께 열거형을 사용하여 경로를 정의합니다.
- 각 사례는 특정 매개변수를 입력된 값으로 전달합니다.
- 파서는 URL 문자열을 경로 열거 케이스로 변환합니다.
- 패턴 일치는 컴파일 시간 안전성을 고려하여 매개변수를 추출합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 유형 안전성: 각 경로 케이스는 필요한 매개변수를 정확하게 전달합니다. 컴파일러는`.userProfile`에서 `variant`에 액세스하는 것을 방지합니다.
- 완전성: `switch`는 모든 경우를 처리해야 합니다. 새 경로를 추가하면 모든 핸들러가 강제로 업데이트됩니다.
- 확장성: 열거형 케이스를 추가하여 새로운 경로를 추가합니다. 컴파일러는 업데이트가 필요한 모든 곳을 알려줍니다.
- 프로덕션: 대규모 앱의 경우`swift-url-routing`또는 `TCA`의 라우팅을 고려하세요.
### 문제 2: 반응형 상태 컨테이너 구현
**문제 설명:** 상태 변경을 관찰할 수 있고 구독자에게 특정 상태 변경에 대한 알림을 보내는 간단한 반응형 상태 컨테이너(Redux/Vuex와 유사)를 Swift에서 구축합니다.
**1단계 - 문제 이해:**
(1) 애플리케이션 상태를 보유하는 상태 컨테이너, (2) 상태 변경을 설명하는 작업, (3) 현재 상태 + 작업에서 새 상태를 생성하는 리듀서, (4) 상태 변경을 관찰하는 구독자가 필요합니다. 이는 단방향 데이터 흐름 패턴입니다.
**2단계 - 접근 방식 파악:**
- `@Published`와 유사한 동작으로 일반`Store<State>`클래스를 사용합니다.
- 작업을 열거형으로 정의합니다.
- 감속기 기능 `(State, Action) -> State`를 사용합니다.
- 구독자는 클로저를 통해 새로운 상태를 받습니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 단방향 흐름: 작업 → 리듀서 → 새 상태 → 구독자. 추론하고 테스트하기 쉽습니다.
- 스레드 안전성: 디스패치 큐는 상태 변이를 직렬화합니다.
- 구독자는 전체 상태를 얻습니다. 불필요한 재렌더링을 방지하려면 선택기 또는`Equatable`검사를 사용하세요.
- 프로덕션: 효과, 테스트 및 SwiftUI 통합이 포함된 프로덕션급 구현을 위해 Point-Free의 `The Composable Architecture`(TCA)를 사용합니다.
---

## 요약
Swift는 Apple 플랫폼 개발에 필수적인 현대적이고 안전하며 표현력이 풍부한 언어입니다. 안전성(옵션, 값 유형, 패턴 일치)에 중점을 두어 전체 버그 범주를 방지합니다. Apple 플랫폼 외에도 Swift는 서버측 개발 및 크로스 플랫폼 애플리케이션 분야에서 성장하고 있습니다. iOS/macOS 개발의 경우 Swift가 확실한 선택입니다. 다른 도메인의 경우 작지만 성장하는 생태계를 갖춘 유능한 언어입니다.