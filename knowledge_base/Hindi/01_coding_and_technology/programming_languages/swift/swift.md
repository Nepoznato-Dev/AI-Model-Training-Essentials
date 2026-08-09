---
# मेटाडेटा
शीर्षक: "स्विफ्ट"
विवरण: "स्विफ्ट प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स बुनियादी बातें, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [स्विफ्ट, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "26 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
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

## सारांश
स्विफ्ट एक आधुनिक, सुरक्षित और अभिव्यंजक भाषा है जो Apple प्लेटफ़ॉर्म विकास के लिए आवश्यक है। सुरक्षा पर इसका जोर (वैकल्पिक, मूल्य प्रकार, पैटर्न मिलान) बग की संपूर्ण श्रेणियों को रोकता है। ऐप्पल प्लेटफ़ॉर्म से परे, स्विफ्ट सर्वर-साइड डेवलपमेंट और क्रॉस-प्लेटफ़ॉर्म एप्लिकेशन में बढ़ रही है। iOS/macOS विकास के लिए, स्विफ्ट स्पष्ट विकल्प है। अन्य डोमेन के लिए, यह एक छोटी लेकिन बढ़ती पारिस्थितिकी तंत्र वाली एक सक्षम भाषा है।