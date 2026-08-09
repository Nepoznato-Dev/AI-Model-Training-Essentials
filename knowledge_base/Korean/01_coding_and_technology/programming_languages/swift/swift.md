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
# 스위프트
Swift는 Apple(Chris Lattner 주도)에서 개발하고 2014년에 처음 출시된 현대적이고 컴파일된 프로그래밍 언어입니다. Swift는 Apple 플랫폼 개발(iOS, macOS, watchOS, tvOS, VisionOS)의 기본 언어로 Objective-C를 대체하도록 설계되었습니다. Swift는 컴파일된 언어의 성능과 스크립팅 언어의 표현력을 결합하고 특히 null 값, 메모리 관리 및 유형 오류와 관련된 안전성을 강조합니다.
Apple 플랫폼 외에도 Swift는 서버측 개발(Vapor, Hummingbird), 크로스 플랫폼 애플리케이션, 심지어 기계 학습(Apple의 Create ML)에도 점점 더 많이 사용되고 있습니다. Swift on Server 및 크로스 플랫폼 지원이 도입되면서 Swift는 단순한 "Apple 언어" 그 이상으로 변모하고 있습니다.
---

## 스위프트가 중요한 이유
- **Apple 플랫폼 표준**: iOS, macOS, watchOS, tvOS 및 VisionOS 개발을 위한 기본 언어입니다.
- **안전성을 고려한 설계**: 옵션으로 널 포인터 충돌을 제거합니다. 값 유형은 의도하지 않은 변형을 방지합니다.
- **성능**: LLVM을 통해 네이티브 기계어 코드로 컴파일합니다. 많은 작업에서 C++와 경쟁할 수 있습니다.
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
### 오브젝티브-C 상호운용성
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

프로덕션의 경우 컴파일된 바이너리를 Ubuntu를 실행하는 Linux 서버에 배포합니다. systemd와 같은 프로세스 관리자를 사용하여 애플리케이션 수명주기를 관리하세요.
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

## 요약
Swift는 Apple 플랫폼 개발에 필수적인 현대적이고 안전하며 표현력이 풍부한 언어입니다. 안전성(옵션, 값 유형, 패턴 일치)에 중점을 두어 전체 버그 범주를 방지합니다. Apple 플랫폼 외에도 Swift는 서버측 개발 및 크로스 플랫폼 애플리케이션 분야에서 성장하고 있습니다. iOS/macOS 개발의 경우 Swift가 확실한 선택입니다. 다른 도메인의 경우 작지만 성장하는 생태계를 갖춘 유능한 언어입니다.