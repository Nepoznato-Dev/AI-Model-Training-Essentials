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
# स्विफ्ट
स्विफ्ट एक आधुनिक, संकलित प्रोग्रामिंग भाषा है जिसे Apple द्वारा विकसित किया गया है (क्रिस लैटनर के नेतृत्व में) और पहली बार 2014 में जारी किया गया था। इसे Apple प्लेटफ़ॉर्म डेवलपमेंट (iOS, macOS, watchOS, tvOS, VisionOS) के लिए प्राथमिक भाषा के रूप में ऑब्जेक्टिव-सी को बदलने के लिए डिज़ाइन किया गया था। स्विफ्ट संकलित भाषाओं के प्रदर्शन को स्क्रिप्टिंग भाषाओं की अभिव्यक्ति के साथ जोड़ती है, और यह सुरक्षा पर जोर देती है - विशेष रूप से शून्य मानों, मेमोरी प्रबंधन और प्रकार की त्रुटियों के आसपास।
Apple प्लेटफ़ॉर्म से परे, स्विफ्ट का उपयोग सर्वर-साइड डेवलपमेंट (वेपर, हमिंगबर्ड), क्रॉस-प्लेटफ़ॉर्म एप्लिकेशन और यहां तक ​​कि मशीन लर्निंग (Apple's Create ML) के लिए भी तेजी से किया जा रहा है। सर्वर पर स्विफ्ट की शुरूआत और क्रॉस-प्लेटफॉर्म समर्थन के साथ, स्विफ्ट सिर्फ एक "एप्पल भाषा" से कहीं अधिक बनती जा रही है।
---

## स्विफ्ट क्यों मायने रखती है
- **Apple प्लेटफ़ॉर्म मानक**: iOS, macOS, watchOS, tvOS और VisionOS विकास के लिए प्राथमिक भाषा।
- **डिज़ाइन द्वारा सुरक्षा**: वैकल्पिक शून्य पॉइंटर क्रैश को समाप्त करते हैं। मूल्य प्रकार अनपेक्षित उत्परिवर्तन को रोकते हैं।
- **प्रदर्शन**: एलएलवीएम के माध्यम से मूल मशीन कोड को संकलित करता है - कई कार्यों के लिए सी++ के साथ प्रतिस्पर्धी।
- **आधुनिक सिंटैक्स**: क्लोजर, जेनेरिक, प्रोटोकॉल-उन्मुख प्रोग्रामिंग और पैटर्न मिलान के साथ स्वच्छ, अभिव्यंजक।
- **स्विफ्टयूआई**: डिक्लेरेटिव यूआई फ्रेमवर्क जो एप्पल प्लेटफॉर्म इंटरफेस के निर्माण को तेज और सहज बनाता है।
- **ओपन सोर्स**: स्विफ्ट कंपाइलर और मानक लाइब्रेरी ओपन सोर्स हैं; लिनक्स और विंडोज़ पर चलता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सेब-केंद्रित** | सर्वोत्तम टूलिंग और इकोसिस्टम Apple प्लेटफ़ॉर्म के लिए हैं | सर्वर-साइड के लिए वाष्प का उपयोग करें; क्रॉस-प्लेटफ़ॉर्म समर्थन में सुधार हो रहा है |
| **सीमित क्रॉस-प्लेटफॉर्म जीयूआई** | विंडोज़/लिनक्स के लिए कोई परिपक्व जीयूआई ढांचा नहीं | क्रॉस-प्लेटफ़ॉर्म के लिए वेब तकनीकों या फ़्लटर का उपयोग करें |
| **छोटा नौकरी बाज़ार (एप्पल के बाहर)** | जावा, पायथन, या जावास्क्रिप्ट की तुलना में कम भूमिकाएँ | iOS/macOS विकास भूमिकाएँ भरपूर हैं |
| **तेजी से विकास** | संस्करणों के बीच बार-बार सिंटैक्स परिवर्तन से कोड टूट सकता है | पिन स्विफ्ट संस्करण; स्विफ्ट पैकेज मैनेजर का उपयोग करें |
| **संकलन समय** | जटिल जेनेरिक कोड संकलित करने में धीमा हो सकता है | प्रकार के भावों को सरल बनाएं; @inlinable का विवेकपूर्ण ढंग से उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
### चर और स्थिरांक
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

### वैकल्पिक - स्विफ्ट का शून्य समाधान
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

### कार्य और समापन
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

### प्रोटोकॉल और संरचनाएं
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

### त्रुटि प्रबंधन
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

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक
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

### उन्नत पैटर्न मिलान
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

### प्रॉपर्टी रैपर्स और रिजल्ट बिल्डर्स
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

## समवर्ती एवं समांतरता (स्विफ्ट समवर्ती)
### एसिंक/प्रतीक्षा करें
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

### संरचित समवर्ती
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (स्विफ्ट पैकेज)
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

### पैकेज.स्विफ्ट
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

### आवश्यक आदेश
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### XCTest फ्रेमवर्क
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

## अंतरसंचालनीयता
### ऑब्जेक्टिव-सी इंटरऑप
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

### सी इंटरऑप
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## डिज़ाइन पैटर्न
### प्रतिनिधि पैटर्न
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

### प्रोटोकॉल-उन्मुख डिज़ाइन
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

## प्रदर्शन एवं अनुकूलन
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

## स्विफ्टयूआई - घोषणात्मक यूआई
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

## तैनाती
### सर्वर-साइड स्विफ्ट
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

उत्पादन के लिए, संकलित बाइनरी को उबंटू चलाने वाले लिनक्स सर्वर पर तैनात करें। एप्लिकेशन जीवनचक्र को प्रबंधित करने के लिए सिस्टमड जैसे प्रोसेस मैनेजर का उपयोग करें।
---

## स्विफ्ट का उपयोग कब करें
| परिदृश्य | स्विफ्ट क्यों | बेहतर विकल्प |
|---|---|-----|
| iOS/macOS ऐप्स | मानक Apple भाषा | -- |
| watchOS/visionOS ऐप्स | एकमात्र विकल्प | -- |
| सर्वर-साइड (वाष्प) | बढ़ता पारिस्थितिकी तंत्र | अधिक परिपक्व सर्वर पारिस्थितिकी तंत्र के लिए Node.js पर जाएँ |
| क्रॉस-प्लेटफ़ॉर्म मोबाइल | संभव है लेकिन प्राथमिक नहीं | स्पंदन, प्रतिक्रिया मूल |
| सिस्टम प्रोग्रामिंग | संभव (लिनक्स) | जंग, सी, सी++ |
| सामान्य एप्लिकेशन डेव (गैर-एप्पल) | सीमित पारिस्थितिकी तंत्र | पायथन, गो, जावा |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: वैकल्पिक क्या हैं, और स्विफ्ट मुझे उन्हें खोलने के लिए क्यों मजबूर करती है?
**ए:** एक वैकल्पिक (`Type?`) एक मान का प्रतिनिधित्व करता है जो अनुपस्थित हो सकता है - यह या तो`.some(value)`या`.none`(शून्य) है। रनटाइम पर नल पॉइंटर क्रैश को रोकने के लिए स्विफ्ट स्पष्ट रूप से अनरैपिंग को बाध्य करती है। आप`if let`,`guard let`, बलपूर्वक खोलना (`!`), वैकल्पिक चेनिंग (`?.`), या शून्य कोलेसिंग (`??`) के साथ खोल सकते हैं। कंपाइलर यह सुनिश्चित करता है कि आप शून्य केस को संभालें - यह बग की एक पूरी श्रेणी को समाप्त कर देता है।
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

### Q2: स्विफ्ट में स्ट्रक्चर और क्लास के बीच क्या अंतर है?
**ए:** संरचनाएं मूल्य प्रकार हैं (असाइनमेंट पर कॉपी की गई), कक्षाएं संदर्भ प्रकार हैं (साझा)। स्ट्रक्चर्स को एक मुफ़्त सदस्यवार इनिशियलाइज़र मिलता है, और वे इनहेरिटेंस, डीइनिशियलाइज़र और रेफरेंस काउंटिंग को छोड़कर कक्षाओं की सभी सुविधाओं का समर्थन करते हैं। स्विफ्ट के मानक पुस्तकालय प्रकार (`String`, `Array`, `Dictionary`) सभी संरचनाएं हैं। डिफ़ॉल्ट रूप से संरचनाओं को प्राथमिकता दें; जब आपको साझा परिवर्तनीय स्थिति या विरासत की आवश्यकता हो तो कक्षाओं का उपयोग करें।
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

### Q3: प्रोटोकॉल और प्रोटोकॉल-उन्मुख प्रोग्रामिंग कैसे काम करते हैं?
**ए:** प्रोटोकॉल तरीकों, गुणों और आवश्यकताओं का एक खाका परिभाषित करते हैं। कोई भी प्रकार अपनी आवश्यकताओं को लागू करके प्रोटोकॉल के अनुरूप हो सकता है। प्रोटोकॉल एक्सटेंशन डिफ़ॉल्ट कार्यान्वयन प्रदान करते हैं। प्रोटोकॉल द्वारा बाधित जेनेरिक आपको वर्ग वंशानुक्रम के ओवरहेड के बिना बहुरूपता प्रदान करते हैं - यह "प्रोटोकॉल-उन्मुख प्रोग्रामिंग" है।
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

### Q4: स्विफ्ट में`async/await`क्या है, और यह अभिनेताओं से कैसे संबंधित है?
**ए:** स्विफ्ट का समवर्ती मॉडल (5.5+) एसिंक्रोनस कोड के लिए`async/await`और सुरक्षित साझा उत्परिवर्तनीय स्थिति के लिए`actors`का उपयोग करता है। `async`फ़ंक्शंस को निलंबित और फिर से शुरू किया जा सकता है। `await`निलंबन बिंदुओं को चिह्नित करता है। अभिनेता अपनी परिवर्तनशील स्थिति तक पहुंच को क्रमबद्ध करके डेटा दौड़ को रोकते हैं - कंपाइलर इसे संकलन समय पर लागू करता है।
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

### Q5: प्रॉपर्टी रैपर्स और रिजल्ट बिल्डर्स कैसे काम करते हैं?
**ए:** प्रॉपर्टी रैपर्स (`@propertyWrapper`) प्रॉपर्टी स्टोरेज में तर्क जोड़ते हैं (जैसे स्विफ्टयूआई में `@State`)। परिणाम निर्माता (`@resultBuilder`) आपको प्राकृतिक सिंटैक्स (जैसे स्विफ्टयूआई के दृश्य पदानुक्रम) का उपयोग करके डेटा संरचनाएं बनाने देते हैं। दोनों मेटाप्रोग्रामिंग के रूप हैं जो बॉयलरप्लेट को कम करते हैं।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक प्रकार-सुरक्षित राउटर बनाएं
**समस्या कथन:** एक आईओएस ऐप के लिए एक प्रकार-सुरक्षित यूआरएल राउटर बनाएं जहां प्रत्येक रूट में संबंधित पैरामीटर होते हैं, और कंपाइलर उन पैरामीटर तक पहुंचने से रोकता है जो किसी दिए गए रूट के लिए मौजूद नहीं हैं।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) टाइप किए गए पैरामीटर के साथ रूट परिभाषाएँ, (2) रूट + पैरामीटर निकालने के लिए यूआरएल पार्सिंग, (3) टाइप-सुरक्षित पैरामीटर एक्सेस - कंपाइलर सुनिश्चित करता है कि आप केवल उन पैरामीटर को पढ़ें जो प्रत्येक रूट के लिए मौजूद हैं। इसके लिए संबंधित मानों वाली गणनाओं की आवश्यकता होती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- मार्गों को परिभाषित करने के लिए संबंधित मानों के साथ एक एनम का उपयोग करें।
- प्रत्येक मामले में टाइप किए गए मानों के रूप में इसके विशिष्ट पैरामीटर होते हैं।
- एक पार्सर यूआरएल स्ट्रिंग्स को रूट एनम मामलों में परिवर्तित करता है।
- पैटर्न मिलान संकलन-समय सुरक्षा के साथ पैरामीटर निकालता है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- प्रकार की सुरक्षा: प्रत्येक रूट केस में बिल्कुल वही पैरामीटर होते हैं जिनकी उसे आवश्यकता होती है। कंपाइलर`.userProfile`पर`variant`तक पहुंचने से रोकता है।
- थकावट:`switch`को सभी मामलों को संभालना होगा - एक नया मार्ग जोड़ने से सभी हैंडलर को अपडेट करने पर मजबूर होना पड़ेगा।
- विस्तारशीलता: एनम केस जोड़कर नए मार्ग जोड़ें; कंपाइलर आपको हर जगह बताता है कि अद्यतन करने की आवश्यकता है।
- उत्पादन: बड़े ऐप्स के लिए`swift-url-routing`या`TCA`की रूटिंग पर विचार करें।
### समस्या 2: एक प्रतिक्रियाशील राज्य कंटेनर लागू करें
**समस्या कथन:** स्विफ्ट में एक सरल प्रतिक्रियाशील राज्य कंटेनर (Redux/Vuex के समान) बनाएं जहां राज्य परिवर्तन देखे जा सकते हैं, और ग्राहकों को विशिष्ट राज्य परिवर्तनों के बारे में सूचित किया जाता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) एक राज्य कंटेनर जो एप्लिकेशन स्थिति रखता है, (2) क्रियाएं जो राज्य परिवर्तनों का वर्णन करती हैं, (3) एक रिड्यूसर जो वर्तमान स्थिति + कार्रवाई से नई स्थिति उत्पन्न करती है, (4) ग्राहक जो राज्य परिवर्तनों का निरीक्षण करते हैं। यह यूनिडायरेक्शनल डेटा प्रवाह पैटर्न है।
**चरण 2 - दृष्टिकोण को पहचानें:**
-`@Published`जैसे व्यवहार के साथ एक सामान्य`Store<State>`वर्ग का उपयोग करें।
- क्रियाओं को एक गणना के रूप में परिभाषित करें।
- रिड्यूसर फ़ंक्शन`(State, Action) -> State`का उपयोग करें।
- सब्सक्राइबर्स को क्लोजर के माध्यम से नई स्थिति प्राप्त होती है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- यूनिडायरेक्शनल प्रवाह: क्रियाएँ → रेड्यूसर → नई स्थिति → ग्राहक। इसके बारे में तर्क करना और परीक्षण करना आसान है।
- थ्रेड सुरक्षा: प्रेषण कतार राज्य उत्परिवर्तन को क्रमबद्ध करती है।
- सब्सक्राइबर्स को पूरी स्थिति मिलती है - अनावश्यक री-रेंडर से बचने के लिए चयनकर्ताओं या`Equatable`चेक का उपयोग करें।
- उत्पादन: प्रभाव, परीक्षण और स्विफ्टयूआई एकीकरण के साथ उत्पादन-ग्रेड कार्यान्वयन के लिए प्वाइंट-फ्री द्वारा`The Composable Architecture`(TCA) का उपयोग करें।
---

## सारांश
स्विफ्ट एक आधुनिक, सुरक्षित और अभिव्यंजक भाषा है जो Apple प्लेटफ़ॉर्म विकास के लिए आवश्यक है। सुरक्षा पर इसका जोर (वैकल्पिक, मूल्य प्रकार, पैटर्न मिलान) बग की संपूर्ण श्रेणियों को रोकता है। ऐप्पल प्लेटफ़ॉर्म से परे, स्विफ्ट सर्वर-साइड डेवलपमेंट और क्रॉस-प्लेटफ़ॉर्म एप्लिकेशन में बढ़ रही है। iOS/macOS विकास के लिए, स्विफ्ट स्पष्ट विकल्प है। अन्य डोमेन के लिए, यह एक छोटी लेकिन बढ़ती पारिस्थितिकी तंत्र वाली एक सक्षम भाषा है।