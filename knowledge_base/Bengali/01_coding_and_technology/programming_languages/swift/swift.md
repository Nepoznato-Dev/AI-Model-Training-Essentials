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
# সুইফট
সুইফট হল একটি আধুনিক, সংকলিত প্রোগ্রামিং ভাষা যা অ্যাপল (ক্রিস ল্যাটনারের নেতৃত্বে) দ্বারা বিকশিত হয়েছে এবং 2014 সালে প্রথম প্রকাশিত হয়েছে। এটি অ্যাপল প্ল্যাটফর্ম বিকাশের জন্য প্রাথমিক ভাষা (iOS, macOS, watchOS, tvOS, visionOS) হিসাবে অবজেক্টিভ-সি প্রতিস্থাপন করার জন্য ডিজাইন করা হয়েছিল। সুইফট কম্পাইল করা ভাষার পারফরম্যান্সকে স্ক্রিপ্টিং ভাষার অভিব্যক্তির সাথে একত্রিত করে, এবং এটি নিরাপত্তার উপর জোর দেয় -- বিশেষ করে শূন্য মান, মেমরি ব্যবস্থাপনা এবং টাইপ ত্রুটির আশেপাশে।
অ্যাপল প্ল্যাটফর্মের বাইরে, সুইফট সার্ভার-সাইড ডেভেলপমেন্ট (বাষ্প, হামিংবার্ড), ক্রস-প্ল্যাটফর্ম অ্যাপ্লিকেশন এবং এমনকি মেশিন লার্নিং (অ্যাপলের ক্রিয়েট এমএল) জন্য ক্রমবর্ধমানভাবে ব্যবহৃত হচ্ছে। সার্ভারে সুইফটের প্রবর্তন এবং ক্রস-প্ল্যাটফর্ম সমর্থনের সাথে, সুইফট কেবল একটি "অ্যাপল ভাষা" হয়ে উঠছে।
---

## কেন সুইফট ব্যাপার
- **Apple প্ল্যাটফর্মের মান**: iOS, macOS, watchOS, tvOS এবং visionOS ডেভেলপমেন্টের জন্য প্রাথমিক ভাষা।
- **ডিজাইন দ্বারা নিরাপত্তা**: ঐচ্ছিক নাল পয়েন্টার ক্র্যাশ দূর করে। মানের প্রকারগুলি অনিচ্ছাকৃত মিউটেশন প্রতিরোধ করে।
- **পারফরম্যান্স**: LLVM-এর মাধ্যমে নেটিভ মেশিন কোডে কম্পাইল করে -- অনেক কাজের জন্য C++ এর সাথে প্রতিযোগিতামূলক।
- **আধুনিক সিনট্যাক্স**: পরিষ্কার, অভিব্যক্তিপূর্ণ, ক্লোজার, জেনেরিক, প্রোটোকল-ভিত্তিক প্রোগ্রামিং এবং প্যাটার্ন ম্যাচিং সহ।
- **SwiftUI**: ঘোষণামূলক UI ফ্রেমওয়ার্ক যা অ্যাপল প্ল্যাটফর্ম ইন্টারফেসগুলিকে দ্রুত এবং স্বজ্ঞাত করে তোলে।
- **ওপেন সোর্স**: সুইফট কম্পাইলার এবং স্ট্যান্ডার্ড লাইব্রেরি হল ওপেন সোর্স; লিনাক্স এবং উইন্ডোজে চলে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **আপেল কেন্দ্রিক** | অ্যাপল প্ল্যাটফর্মের জন্য সেরা টুলিং এবং ইকোসিস্টেম সার্ভার-সাইডের জন্য বাষ্প ব্যবহার করুন; ক্রস-প্ল্যাটফর্ম সমর্থন উন্নতি করছে |
| **সীমিত ক্রস-প্ল্যাটফর্ম GUI** | উইন্ডোজ/লিনাক্সের জন্য কোন পরিপক্ক GUI ফ্রেমওয়ার্ক নেই ক্রস-প্ল্যাটফর্মের জন্য ওয়েব প্রযুক্তি বা ফ্লটার ব্যবহার করুন |
| **ছোট চাকরির বাজার (অ্যাপলের বাইরে)** | Java, Python, বা JavaScript এর চেয়ে কম ভূমিকা | iOS/macOS বিকাশের ভূমিকা প্রচুর |
| **দ্রুত বিবর্তন** | সংস্করণগুলির মধ্যে ঘন ঘন সিনট্যাক্স পরিবর্তন কোড ভাঙতে পারে | পিন সুইফট সংস্করণ; সুইফট প্যাকেজ ম্যানেজার ব্যবহার করুন |
| **সময় কম্পাইল** | জটিল জেনেরিক কোড কম্পাইল করতে ধীর হতে পারে | টাইপ এক্সপ্রেশন সরলীকরণ; @inlinable যুক্তিযুক্তভাবে ব্যবহার করুন |
---

## সিনট্যাক্স মৌলিক
### চলক এবং ধ্রুবক
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

### ঐচ্ছিক -- সুইফট এর সমাধান শূন্য
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

### ফাংশন এবং ক্লোজার
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

### প্রোটোকল এবং কাঠামো
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

### ত্রুটি হ্যান্ডলিং
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক
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

### উন্নত প্যাটার্ন ম্যাচিং
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

### সম্পত্তির মোড়ক এবং ফলাফল নির্মাতা
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

## সামঞ্জস্য এবং সমান্তরালতা (সুইফট কনকারেন্সি)
### অ্যাসিঙ্ক/অপেক্ষা করুন
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

### স্ট্রাকচার্ড কনকারেন্সি
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (সুইফট প্যাকেজ)
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

### অত্যাবশ্যকীয় আদেশ
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### XCTest ফ্রেমওয়ার্ক
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

## ইন্টারঅপারেবিলিটি
### অবজেক্টিভ-সি ইন্টারপ
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

### সি ইন্টারপ
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## ডিজাইন প্যাটার্ন
### প্রতিনিধি প্যাটার্ন
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

### প্রোটোকল-ওরিয়েন্টেড ডিজাইন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
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

## SwiftUI -- ঘোষণামূলক UI
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

## স্থাপনা
### সার্ভার-সাইড সুইফট
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

উত্পাদনের জন্য, উবুন্টু চালিত একটি লিনাক্স সার্ভারে সংকলিত বাইনারি স্থাপন করুন। অ্যাপ্লিকেশন লাইফসাইকেল পরিচালনা করতে সিস্টেমডের মতো একটি প্রক্রিয়া পরিচালক ব্যবহার করুন।
---

## কখন সুইফট ব্যবহার করবেন
| দৃশ্যকল্প | কেন সুইফট | ভাল বিকল্প |
|------------|------------|---------|
| iOS/macOS অ্যাপস | আদর্শ অ্যাপল ভাষা | -- |
| watchOS/visionOS অ্যাপস | একমাত্র বিকল্প | -- |
| সার্ভার-সাইড (বাষ্প) | ক্রমবর্ধমান বাস্তুতন্ত্র | আরও পরিপক্ক সার্ভার ইকোসিস্টেমের জন্য Node.js যান
| ক্রস-প্ল্যাটফর্ম মোবাইল | সম্ভাব্য কিন্তু প্রাথমিক নয় | ফ্লটার, প্রতিক্রিয়া নেটিভ |
| সিস্টেম প্রোগ্রামিং | সম্ভাব্য (লিনাক্স) | মরিচা, সি, সি++ |
| সাধারণ অ্যাপ্লিকেশন ডেভ (অ-অ্যাপল) | সীমিত ইকোসিস্টেম | পাইথন, গো, জাভা |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: ঐচ্ছিক কি, এবং কেন সুইফট আমাকে সেগুলি খুলতে বাধ্য করে?
**A:** একটি ঐচ্ছিক (`Type?`) একটি মান উপস্থাপন করে যা অনুপস্থিত হতে পারে — এটি হয়`.some(value)`বা`.none`(শূন্য)। রানটাইমে নাল পয়েন্টার ক্র্যাশ প্রতিরোধ করতে সুইফ্ট স্পষ্টভাবে মোড়ক খুলে দেয়। আপনি`if let`,`guard let`, ফোর্স আনর্যাপ (`!`), ঐচ্ছিক চেইনিং (`?.`), অথবা নিল কোলেসিং (`??`) দিয়ে খুলতে পারেন৷ কম্পাইলার নিশ্চিত করে যে আপনি শূন্য কেসটি পরিচালনা করছেন - এটি একটি সম্পূর্ণ শ্রেণীর বাগগুলিকে দূর করে।
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

### প্রশ্ন 2: সুইফটে স্ট্রাকট এবং ক্লাসের মধ্যে পার্থক্য কী?
**A:** স্ট্রাকট হল মান প্রকার (অ্যাসাইনমেন্টে কপি করা), ক্লাস হল রেফারেন্স টাইপ (শেয়ার করা)। স্ট্রাকস একটি বিনামূল্যে সদস্যওয়াইজ ইনিশিয়ালাইজার পায়, এবং তারা উত্তরাধিকার, ডিনিটিয়ালাইজার এবং রেফারেন্স গণনা ছাড়া ক্লাসের সমস্ত বৈশিষ্ট্য সমর্থন করে। সুইফ্টের স্ট্যান্ডার্ড লাইব্রেরি প্রকারগুলি (`String`,`Array`,`Dictionary`) হল সমস্ত স্ট্রাকট৷ ডিফল্টরূপে structs পছন্দ করুন; আপনার যখন ভাগ করা পরিবর্তনযোগ্য অবস্থা বা উত্তরাধিকার প্রয়োজন তখন ক্লাস ব্যবহার করুন।
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

### প্রশ্ন 3: প্রোটোকল এবং প্রোটোকল-ভিত্তিক প্রোগ্রামিং কিভাবে কাজ করে?
**A:** প্রোটোকল পদ্ধতি, বৈশিষ্ট্য এবং প্রয়োজনীয়তার একটি ব্লুপ্রিন্ট সংজ্ঞায়িত করে। যে কোনো প্রকারের প্রয়োজনীয়তা বাস্তবায়ন করে একটি প্রোটোকল মেনে চলতে পারে। প্রোটোকল এক্সটেনশনগুলি ডিফল্ট বাস্তবায়ন প্রদান করে। প্রোটোকল দ্বারা সীমাবদ্ধ জেনেরিকগুলি আপনাকে শ্রেণি উত্তরাধিকারের ওভারহেড ছাড়াই পলিমরফিজম দেয় — এটি "প্রটোকল-ভিত্তিক প্রোগ্রামিং।"
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

### প্রশ্ন 4: সুইফটে`async/await`কী এবং এটি অভিনেতাদের সাথে কীভাবে সম্পর্কিত?
**A:** সুইফটের কনকারেন্সি মডেল (5.5+) অ্যাসিঙ্ক্রোনাস কোডের জন্য`async/await`এবং নিরাপদ ভাগ করা পরিবর্তনযোগ্য অবস্থার জন্য`actors`ব্যবহার করে। `async`ফাংশন স্থগিত এবং পুনরায় শুরু করা যেতে পারে। `await`সাসপেনশন পয়েন্ট চিহ্নিত করে। অভিনেতারা তাদের পরিবর্তনযোগ্য অবস্থায় অ্যাক্সেসকে সিরিয়ালাইজ করে ডেটা রেস প্রতিরোধ করে — কম্পাইলার কম্পাইলের সময়ে এটি প্রয়োগ করে।
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

### প্রশ্ন 5: সম্পত্তির মোড়ক এবং ফলাফল নির্মাতারা কীভাবে কাজ করে?
**A:** প্রপার্টি র্যাপার (`@propertyWrapper`) প্রোপার্টি স্টোরেজে যুক্তি যোগ করে (যেমন SwiftUI-তে `@State`)। ফলাফল নির্মাতারা (`@resultBuilder`) আপনাকে প্রাকৃতিক সিনট্যাক্স ব্যবহার করে ডেটা স্ট্রাকচার তৈরি করতে দেয় (যেমন SwiftUI এর ভিউ হায়ারার্কি)। উভয়ই মেটাপ্রোগ্রামিংয়ের রূপ যা বয়লারপ্লেট হ্রাস করে।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি টাইপ-সেফ রাউটার তৈরি করুন
**সমস্যা বিবৃতি:** একটি iOS অ্যাপের জন্য একটি টাইপ-সেফ ইউআরএল রাউটার তৈরি করুন যেখানে প্রতিটি রুটে সংশ্লিষ্ট প্যারামিটার রয়েছে এবং কম্পাইলার প্রদত্ত রুটের জন্য বিদ্যমান নেই এমন প্যারামিটার অ্যাক্সেস করতে বাধা দেয়।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) টাইপ করা প্যারামিটার সহ রুটের সংজ্ঞা, (2) রুট + প্যারামিটারগুলি বের করতে URL পার্সিং, (3) টাইপ-সেফ প্যারামিটার অ্যাক্সেস — কম্পাইলার নিশ্চিত করে যে আপনি প্রতিটি রুটের জন্য বিদ্যমান প্যারামিটারগুলিই পড়তে পারেন৷ এর জন্য সংশ্লিষ্ট মান সহ enums প্রয়োজন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- রুট সংজ্ঞায়িত করতে সংশ্লিষ্ট মান সহ একটি enum ব্যবহার করুন।
- প্রতিটি ক্ষেত্রে টাইপ করা মান হিসাবে তার নির্দিষ্ট পরামিতি বহন করে।
- একটি পার্সার ইউআরএল স্ট্রিংকে রুট enum ক্ষেত্রে রূপান্তর করে।
- প্যাটার্ন ম্যাচিং কম্পাইল-টাইম সেফটি সহ প্যারামিটার বের করে।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- টাইপ নিরাপত্তা: প্রতিটি রুট কেস এর প্রয়োজনীয় প্যারামিটারগুলি বহন করে। কম্পাইলার `.userProfile`-এ`variant`অ্যাক্সেস করতে বাধা দেয়।
- পরিশ্রান্ততা: `switch`-কে অবশ্যই সমস্ত ক্ষেত্রে পরিচালনা করতে হবে — একটি নতুন রুট যোগ করা সমস্ত হ্যান্ডলার আপডেট করে৷
- এক্সটেনসিবিলিটি: enum কেস যোগ করে নতুন রুট যোগ করুন; কম্পাইলার আপনাকে সব জায়গায় বলে যে আপডেট করা দরকার।
- উৎপাদন: বড় অ্যাপের জন্য`swift-url-routing`বা`TCA`এর রাউটিং বিবেচনা করুন।
### সমস্যা 2: একটি প্রতিক্রিয়াশীল স্টেট কন্টেইনার প্রয়োগ করুন
**সমস্যা বিবৃতি:** সুইফটে একটি সাধারণ প্রতিক্রিয়াশীল স্টেট কন্টেইনার (Redux/Vuex-এর মতো) তৈরি করুন যেখানে রাজ্যের পরিবর্তনগুলি পর্যবেক্ষণযোগ্য, এবং গ্রাহকদের নির্দিষ্ট অবস্থার পরিবর্তন সম্পর্কে অবহিত করা হয়।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) একটি স্টেট কন্টেইনার যা অ্যাপ্লিকেশান স্টেট ধারণ করে, (2) অ্যাকশন যা স্টেট পরিবর্তনগুলি বর্ণনা করে, (3) একটি রিডুসার যা বর্তমান স্টেট + অ্যাকশন থেকে নতুন স্টেট তৈরি করে, (4) স্টেট পরিবর্তনগুলি পর্যবেক্ষণ করে এমন গ্রাহক৷ এটি একমুখী ডেটা প্রবাহ প্যাটার্ন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- `@Published`-এর মতো আচরণ সহ একটি জেনেরিক`Store<State>`ক্লাস ব্যবহার করুন৷
- একটি enum হিসাবে কর্ম সংজ্ঞায়িত.
- একটি রিডুসার ফাংশন`(State, Action) -> State`ব্যবহার করুন।
- গ্রাহকরা বন্ধের মাধ্যমে নতুন রাষ্ট্র পাবেন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- একমুখী প্রবাহ: অ্যাকশন → রিডিউসার → নতুন অবস্থা → গ্রাহক। সম্পর্কে যুক্তি এবং পরীক্ষা করা সহজ.
- থ্রেড সেফটি: ডিসপ্যাচ কিউ স্টেট মিউটেশনকে সিরিয়ালাইজ করে।
- গ্রাহকরা সম্পূর্ণ অবস্থা পান — অপ্রয়োজনীয় রি-রেন্ডার এড়াতে নির্বাচক বা`Equatable`চেক ব্যবহার করুন।
- উত্পাদন: প্রভাব, পরীক্ষা, এবং SwiftUI একীকরণ সহ একটি উত্পাদন-গ্রেড বাস্তবায়নের জন্য পয়েন্ট-ফ্রি দ্বারা`The Composable Architecture`(TCA) ব্যবহার করুন।
---

## সারাংশ
Swift হল একটি আধুনিক, নিরাপদ এবং অভিব্যক্তিপূর্ণ ভাষা যা Apple প্ল্যাটফর্মের বিকাশের জন্য অপরিহার্য। নিরাপত্তার উপর এর জোর (ঐচ্ছিক, মান প্রকার, প্যাটার্ন ম্যাচিং) সম্পূর্ণ বাগগুলিকে আটকায়। অ্যাপল প্ল্যাটফর্মের বাইরে, সুইফট সার্ভার-সাইড ডেভেলপমেন্ট এবং ক্রস-প্ল্যাটফর্ম অ্যাপ্লিকেশনগুলিতে বৃদ্ধি পাচ্ছে। iOS/macOS ডেভেলপমেন্টের জন্য, সুইফট হল স্পষ্ট পছন্দ। অন্যান্য ডোমেনের জন্য, এটি একটি ছোট কিন্তু ক্রমবর্ধমান ইকোসিস্টেম সহ একটি সক্ষম ভাষা।