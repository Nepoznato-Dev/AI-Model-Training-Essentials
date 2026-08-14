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
# Süratli
Swift, Apple (Chris Lattner liderliğinde) tarafından geliştirilen ve ilk olarak 2014'te piyasaya sürülen modern, derlenmiş bir programlama dilidir. Apple platformu geliştirme (iOS, macOS, watchOS, tvOS, VisionOS) için birincil dil olarak Objective-C'nin yerini almak üzere tasarlanmıştır. Swift, derlenmiş dillerin performansını betik dillerinin ifade gücüyle birleştirir ve özellikle boş değerler, bellek yönetimi ve tür hataları konusunda güvenliği vurgular.
Apple platformlarının ötesinde Swift, sunucu tarafı geliştirme (Vapor, Hummingbird), platformlar arası uygulamalar ve hatta makine öğrenimi (Apple'ın Create ML'si) için giderek daha fazla kullanılıyor. Swift'in Sunucuda kullanıma sunulması ve platformlar arası desteğiyle Swift, bir "Apple dili" olmaktan çok daha fazlası haline geliyor.
---

## Swift Neden Önemlidir
- **Apple platformu standardı**: iOS, macOS, watchOS, tvOS ve vizyonOS geliştirme için birincil dil.
- **Tasarım gereği güvenlik**: İsteğe bağlı seçenekler boş işaretçi çökmelerini ortadan kaldırır. Değer türleri istenmeyen mutasyonları önler.
- **Performans**: LLVM aracılığıyla yerel makine koduna derlenir; birçok görev için C++ ile rekabet eder.
- **Modern sözdizimi**: Temiz, etkileyici, kapanışlar, genel bilgiler, protokol odaklı programlama ve kalıp eşleştirme.
- **SwiftUI**: Apple platformu arayüzlerini oluşturmayı hızlı ve sezgisel hale getiren bildirime dayalı kullanıcı arayüzü çerçevesi.
- **Açık kaynak**: Swift derleyicisi ve standart kitaplık açık kaynaktır; Linux ve Windows'ta çalışır.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Elma merkezli** | En iyi araçlar ve ekosistem Apple platformları içindir | Sunucu tarafı için Vapor'u kullanın; platformlar arası destek gelişiyor |
| **Sınırlı platformlar arası GUI** | Windows/Linux için olgun GUI çerçevesi yok | Çapraz platform için web teknolojilerini veya Flutter'ı kullanın |
| **Daha küçük iş piyasası (Apple dışında)** | Java, Python veya JavaScript'ten daha az rol | iOS/macOS geliştirme rolleri çoktur |
| **Hızlı evrim** | Sürümler arasındaki sık sözdizimi değişiklikleri kodu bozabilir | Pin Swift versiyonları; Swift Paket Yöneticisini kullanın |
| **Derleme zamanları** | Karmaşık genel kodun derlenmesi yavaş olabilir | Tür ifadelerini basitleştirin; @inlinable'ı akıllıca kullanın |
---

## Söz Diziminin Temelleri
### Değişkenler ve Sabitler
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

### İsteğe Bağlı Seçenekler -- Swift'in Null Çözümü
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

### İşlevler ve Kapanışlar
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

### Protokoller ve Yapılar
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

### Hata İşleme
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

## Gelişmiş Sözdizimi ve Desenler
### Jenerikler
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

### Gelişmiş Desen Eşleştirme
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

### Özellik Paketleyiciler ve Sonuç Oluşturucular
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

## Eşzamanlılık ve Paralellik (Hızlı Eşzamanlılık)
### eşzamansız/beklemede
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

### Yapılandırılmış Eşzamanlılık
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı (Swift Paketi)
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

### Paket.swift
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

### Temel Komutlar
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### XCTest Çerçevesi
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

## Birlikte Çalışabilirlik
### Objective-C Birlikte Çalışma
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

### C Birlikte Çalışma
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## Tasarım Desenleri
### Delege Modeli
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

### Protokol Odaklı Tasarım
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

## Performans ve Optimizasyon
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

## SwiftUI -- Bildirime Dayalı Kullanıcı Arayüzü
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

## Dağıtım
### Sunucu Tarafı Swift
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Üretim için derlenmiş ikili dosyayı Ubuntu çalıştıran bir Linux sunucusuna dağıtın. Uygulama yaşam döngüsünü yönetmek için systemd gibi bir süreç yöneticisi kullanın.
---

## Swift Ne Zaman Kullanılmalı
| Senaryo | Neden Swift | Daha İyi Alternatif |
|----------|----------|----------|
| iOS/macOS uygulamaları | Standart Apple dili | -- |
| watchOS/visionOS uygulamaları | Tek seçenek | -- |
| Sunucu tarafı (Buhar) | Büyüyen ekosistem | Daha olgun sunucu ekosistemleri için Node.js'ye gidin |
| Platformlar arası mobil | Mümkün ama birincil değil | Flutter, Yerel Tepki |
| Sistem programlama | Mümkün (Linux) | Pas, C, C++ |
| Genel uygulama geliştirme (Apple dışı) | Sınırlı ekosistem | Python, Git, Java |
---

## Sentetik Soru-Cevap
### S1: Seçenekler nelerdir ve Swift neden beni bunları açmaya zorluyor?
**A:** İsteğe bağlı (`Type?`), bulunmayabilecek bir değeri temsil eder;`.some(value)`veya `.none`'dir (nil). Swift, çalışma zamanında boş işaretçi çökmelerini önlemek için açık paket açma işlemini zorlar. `if let`, `guard let`, zorla açma (`!`), isteğe bağlı zincirleme (`?.`) veya sıfır birleştirme (`??`) ile paketi açabilirsiniz. Derleyici sıfır durumu halletmenizi sağlar; bu, tüm bir hata sınıfını ortadan kaldırır.
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

### S2: Swift'deki yapılar ve sınıflar arasındaki fark nedir?
**C:** Yapılar değer türleridir (atama sırasında kopyalanır), sınıflar ise referans türleridir (paylaşılır). Yapılar, üye bazında ücretsiz bir başlatıcıya sahiptir ve miras, başlatıcıları kaldırıcılar ve referans sayımı dışında sınıfların tüm özelliklerini destekler. Swift'in standart kütüphane türlerinin (`String`,`Array`,`Dictionary`) tümü yapılardır. Yapıları varsayılan olarak tercih edin; Paylaşılan değişken duruma veya mirasa ihtiyaç duyduğunuzda sınıfları kullanın.
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

### S3: Protokoller ve protokol odaklı programlama nasıl çalışır?
**C:** Protokoller yöntemlerin, özelliklerin ve gereksinimlerin bir planını tanımlar. Herhangi bir tür, gereksinimlerini uygulayarak bir protokole uyabilir. Protokol uzantıları varsayılan uygulamaları sağlar. Protokollerle kısıtlanan jenerikler size sınıf mirasının ek yükü olmadan polimorfizm sağlar - bu "protokol odaklı programlamadır."
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

### S4: Swift'de`async/await`nedir ve bunun oyuncularla ilişkisi nedir?
**C:** Swift'in eşzamanlılık modeli (5.5+), eşzamansız kod için `async/await`'yi ve güvenli paylaşılan değişken durum için `actors`'yi kullanır. `async`işlevleri askıya alınabilir ve devam ettirilebilir. `await`askı noktalarını işaretler. Aktörler, değişken durumlarına erişimi serileştirerek veri yarışlarını önler; derleyici bunu derleme zamanında uygular.
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

### S5: Özellik sarmalayıcılar ve sonuç oluşturucular nasıl çalışır?
**C:** Özellik sarmalayıcılar (`@propertyWrapper`), özellik depolamaya mantık ekler (SwiftUI'deki`@State`gibi). Sonuç oluşturucular (`@resultBuilder`), doğal söz dizimini (SwiftUI'nin görünüm hiyerarşisi gibi) kullanarak veri yapıları oluşturmanıza olanak tanır. Her ikisi de ortak metni azaltan metaprogramlama biçimleridir.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Tip Güvenli Yönlendirici Oluşturun
**Sorun Açıklaması:** Her rotanın ilişkili parametrelere sahip olduğu ve derleyicinin belirli bir rota için mevcut olmayan parametrelere erişimi engellediği bir iOS uygulaması için tür açısından güvenli bir URL yönlendirici oluşturun.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) yazılan parametrelerle rota tanımları, (2) rota + parametreleri çıkarmak için URL ayrıştırma, (3) tür açısından güvenli parametre erişimi — derleyici yalnızca her rota için mevcut olan parametreleri okumanızı sağlar. Bu, ilişkili değerlere sahip numaralandırmalar gerektirir.
**2. Adım — Yaklaşımı Belirleyin:**
- Rotaları tanımlamak için ilişkili değerlere sahip bir numaralandırma kullanın.
- Her durum, girilen değerler olarak kendine özgü parametreleri taşır.
- Bir ayrıştırıcı, URL dizelerini numaralandırma durumlarını yönlendirmek için dönüştürür.
- Desen eşleştirme, derleme zamanı güvenliğiyle parametreleri çıkarır.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Tip güvenliği: Her rota durumu tam olarak ihtiyaç duyduğu parametreleri taşır. Derleyici,`.userProfile`üzerinde `variant`'ye erişimi engeller.
- Kapsamlılık:`switch`tüm durumları ele almalıdır; yeni bir rota eklenmesi tüm işleyicilerin güncellenmesini zorunlu kılar.
- Genişletilebilirlik: numaralandırma durumları ekleyerek yeni rotalar ekleyin; derleyici size güncellenmesi gereken her şeyi söyler.
- Üretim: Daha büyük uygulamalar için`swift-url-routing`veya`TCA`yönlendirmesini düşünün.
### Sorun 2: Reaktif Durum Konteynerinin Uygulanması
**Sorun Açıklaması:** Swift'de durum değişikliklerinin gözlemlenebildiği ve abonelerin belirli durum değişiklikleri konusunda bilgilendirildiği basit bir reaktif durum kapsayıcısı (Redux/Vuex'e benzer) oluşturun.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) uygulama durumunu tutan bir durum kapsayıcısı, (2) durum değişikliklerini tanımlayan eylemler, (3) mevcut durum + eylemden yeni durum üreten bir düşürücü, (4) durum değişikliklerini gözlemleyen aboneler. Bu tek yönlü veri akış modelidir.
**2. Adım — Yaklaşımı Belirleyin:**
-`@Published`benzeri davranışa sahip genel bir`Store<State>`sınıfı kullanın.
- Eylemleri bir numaralandırma olarak tanımlayın.
-`(State, Action) -> State`redüktör fonksiyonunu kullanın.
- Aboneler yeni durumu kapanış yoluyla alırlar.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Tek yönlü akış: eylemler → düşürücü → yeni durum → aboneler. Düşünmek ve test etmek kolaydır.
- İş parçacığı güvenliği: sevk kuyruğu durum mutasyonlarını serileştirir.
- Aboneler tam durumu alır; gereksiz yeniden oluşturmaları önlemek için seçicileri veya`Equatable`kontrollerini kullanın.
- Prodüksiyon: Efektler, testler ve SwiftUI entegrasyonuyla üretim düzeyinde bir uygulama için Point-Free'nin`The Composable Architecture`(TCA) ürününü kullanın.
---

## Özet
Swift, Apple platformunun geliştirilmesi için gerekli olan modern, güvenli ve etkileyici bir dildir. Güvenliğe verdiği önem (isteğe bağlı seçenekler, değer türleri, model eşleştirme) tüm hata kategorilerini önler. Swift, Apple platformlarının ötesinde sunucu tarafı geliştirme ve platformlar arası uygulamalarda da büyüyor. iOS/macOS geliştirme için Swift net bir seçimdir. Diğer alanlar için ise daha küçük ama büyüyen bir ekosisteme sahip yetenekli bir dildir.