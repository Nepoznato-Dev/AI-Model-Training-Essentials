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
#cepat
Swift adalah bahasa pemrograman terkompilasi modern yang dikembangkan oleh Apple (dipimpin oleh Chris Lattner) dan pertama kali dirilis pada tahun 2014. Swift dirancang untuk menggantikan Objective-C sebagai bahasa utama untuk pengembangan platform Apple (iOS, macOS, watchOS, tvOS, visionOS). Swift menggabungkan kinerja bahasa yang dikompilasi dengan ekspresi bahasa skrip, dan menekankan keamanan -- khususnya seputar nilai null, manajemen memori, dan kesalahan ketik.
Di luar platform Apple, Swift semakin banyak digunakan untuk pengembangan sisi server (Vapor, Hummingbird), aplikasi lintas platform, dan bahkan pembelajaran mesin (Apple's Create ML). Dengan diperkenalkannya Swift di Server dan dukungan lintas platform, Swift menjadi lebih dari sekedar "bahasa Apple".
---

## Mengapa Swift Penting
- **Standar platform Apple**: Bahasa utama untuk pengembangan iOS, macOS, watchOS, tvOS, dan visionOS.
- **Keamanan berdasarkan desain**: Opsional menghilangkan kerusakan penunjuk nol. Tipe nilai mencegah mutasi yang tidak diinginkan.
- **Kinerja**: Mengkompilasi ke kode mesin asli melalui LLVM -- bersaing dengan C++ untuk banyak tugas.
- **Sintaks modern**: Bersih, ekspresif, dengan penutupan, generik, pemrograman berorientasi protokol, dan pencocokan pola.
- **SwiftUI**: Kerangka UI deklaratif yang membuat pembuatan antarmuka platform Apple menjadi cepat dan intuitif.
- **Sumber terbuka**: Kompiler Swift dan pustaka standar adalah sumber terbuka; berjalan di Linux dan Windows.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Berpusat pada Apple** | Perkakas dan ekosistem terbaik untuk platform Apple | Gunakan Vapor untuk sisi server; dukungan lintas platform semakin membaik |
| **GUI lintas platform terbatas** | Tidak ada kerangka GUI yang matang untuk Windows/Linux | Gunakan teknologi web atau Flutter untuk lintas platform |
| **Pasar kerja yang lebih kecil (di luar Apple)** | Peran lebih sedikit dibandingkan Java, Python, atau JavaScript | Peran pengembangan iOS/macOS sangat banyak |
| **Evolusi cepat** | Perubahan sintaksis yang sering terjadi antar versi dapat merusak kode | Sematkan versi Swift; gunakan Manajer Paket Swift |
| **Waktu kompilasi** | Kode generik yang kompleks bisa jadi lambat untuk dikompilasi | Sederhanakan ekspresi tipe; gunakan @inlinable dengan bijaksana |
---

## Dasar Sintaks
### Variabel dan Konstanta
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

### Opsional -- Solusi Swift untuk Null
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

### Fungsi dan Penutupan
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

### Protokol dan Struktur
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

### Penanganan Kesalahan
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

## Sintaks & Pola Tingkat Lanjut
### Generik
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

### Pencocokan Pola Tingkat Lanjut
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

### Pembungkus Properti dan Pembuat Hasil
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

## Konkurensi & Paralelisme (Konkurensi Cepat)
### async/menunggu
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

### Konkurensi Terstruktur
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek (Paket Swift)
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

### Perintah Penting
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### Saluran CI/CD (Tindakan GitHub)
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

## Pengujian
### Kerangka XCTest
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

## Interoperabilitas
### Interop Objektif-C
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

## Pola Desain
### Pola Delegasi
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

### Desain Berorientasi Protokol
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

## Kinerja & Optimasi
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

## SwiftUI -- UI Deklaratif
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

## Penerapan
### Swift Sisi Server
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

Untuk produksi, sebarkan biner yang dikompilasi ke server Linux yang menjalankan Ubuntu. Gunakan manajer proses seperti systemd untuk mengelola siklus hidup aplikasi.
---

## Kapan Menggunakan Swift
| Skenario | Mengapa Swift | Alternatif Lebih Baik |
|----------|----------|-------------------|
| Aplikasi iOS/macOS | Bahasa standar Apple | -- |
| aplikasi watchOS/visionOS | Satu-satunya pilihan | -- |
| Sisi server (Uap) | Ekosistem Tumbuh | Gunakan Node.js untuk ekosistem server yang lebih matang |
| Seluler lintas platform | Mungkin tapi bukan yang utama | Flutter, Bereaksi Asli |
| Pemrograman sistem | Kemungkinan (Linux) | Karat, C, C++ |
| Pengembang aplikasi umum (non-Apple) | Ekosistem terbatas | Python, Buka, Java |
---

## Tanya Jawab Sintetis
### Q1: Apa saja yang bersifat opsional, dan mengapa Swift memaksa saya untuk membukanya?
**A:** Opsional (`Type?`) mewakili nilai yang mungkin tidak ada — bisa berupa`.some(value)`atau`.none`(nil). Swift memaksa pembukaan bungkus secara eksplisit untuk mencegah crash penunjuk nol saat runtime. Anda dapat membuka bungkusnya dengan`if let`,`guard let`, force unwrap (`!`), rantai opsional (`?.`), atau nihil penggabungan (`??`). Kompiler memastikan Anda menangani kasus nihil — ini menghilangkan seluruh kelas bug.
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

### Q2: Apa perbedaan antara struct dan kelas di Swift?
**A:** Struktur adalah tipe nilai (disalin saat penugasan), kelas adalah tipe referensi (dibagikan). Struct mendapatkan inisialisasi anggota gratis, dan mendukung semua fitur kelas kecuali pewarisan, deinisialisasi, dan penghitungan referensi. Tipe pustaka standar Swift (`String`,`Array`,`Dictionary`) semuanya merupakan struct. Lebih suka struct secara default; gunakan kelas ketika Anda membutuhkan status atau warisan bersama yang dapat diubah.
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

### Q3: Bagaimana cara kerja protokol dan pemrograman berorientasi protokol?
**A:** Protokol menentukan cetak biru metode, properti, dan persyaratan. Tipe apa pun dapat menyesuaikan diri dengan suatu protokol dengan menerapkan persyaratannya. Ekstensi protokol menyediakan implementasi default. Generik yang dibatasi oleh protokol memberi Anda polimorfisme tanpa beban warisan kelas — ini adalah "pemrograman berorientasi protokol".
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

### Q4: Apa itu`async/await`di Swift, dan apa hubungannya dengan aktor?
**A:** Model konkurensi Swift (5.5+) menggunakan`async/await`untuk kode asinkron dan`actors`untuk status bersama yang dapat diubah dan aman.  Fungsi`async`dapat ditangguhkan dan dilanjutkan. `await`menandai titik suspensi. Aktor mencegah data race dengan membuat serial akses ke statusnya yang dapat diubah — kompiler menerapkan hal ini pada waktu kompilasi.
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

### Q5: Bagaimana cara kerja pembungkus properti dan pembuat hasil?
**A:** Pembungkus properti (`@propertyWrapper`) menambahkan logika ke penyimpanan properti (seperti`@State`di SwiftUI). Pembuat hasil (`@resultBuilder`) memungkinkan Anda membangun struktur data menggunakan sintaksis alami (seperti hierarki tampilan SwiftUI). Keduanya merupakan bentuk metaprogramming yang mengurangi boilerplate.
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

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membangun Router yang Aman untuk Tipe
**Pernyataan Masalah:** Buat router URL yang aman untuk tipe untuk aplikasi iOS yang setiap rutenya memiliki parameter terkait, dan compiler mencegah pengaksesan parameter yang tidak ada untuk rute tertentu.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) definisi rute dengan parameter yang diketik, (2) penguraian URL untuk mengekstrak parameter rute +, (3) akses parameter yang aman untuk tipe — kompiler memastikan Anda hanya membaca parameter yang ada untuk setiap rute. Ini memerlukan enum dengan nilai terkait.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan enum dengan nilai terkait untuk menentukan rute.
- Setiap kasus membawa parameter spesifiknya sebagai nilai yang diketik.
- Parser mengonversi string URL untuk merutekan kasus enum.
- Pencocokan pola mengekstrak parameter dengan keamanan waktu kompilasi.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Keamanan jenis: setiap kasus rute membawa parameter yang dibutuhkan secara tepat. Kompiler mencegah akses`variant`pada`.userProfile`.
- Kelengkapan:`switch`harus menangani semua kasus — menambahkan rute baru memaksa memperbarui semua penangan.
- Ekstensibilitas: tambahkan rute baru dengan menambahkan kasus enum; kompiler memberi tahu Anda di mana saja yang perlu diperbarui.
- Produksi: pertimbangkan perutean`swift-url-routing`atau`TCA`untuk aplikasi yang lebih besar.
### Masalah 2: Menerapkan Kontainer Status Reaktif
**Pernyataan Masalah:** Buat wadah status reaktif sederhana (mirip dengan Redux/Vuex) di Swift di mana perubahan status dapat diamati, dan pelanggan diberi tahu tentang perubahan status tertentu.
**Langkah 1 — Pahami Masalahnya:**
Kita membutuhkan: (1) wadah status yang menampung status aplikasi, (2) tindakan yang mendeskripsikan perubahan status, (3) peredam yang menghasilkan status baru dari status saat ini + tindakan, (4) pelanggan yang mengamati perubahan status. Ini adalah pola aliran data searah.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan kelas`Store<State>`generik dengan perilaku seperti `@Published`.
- Tentukan tindakan sebagai enum.
- Gunakan fungsi peredam`(State, Action) -> State`.
- Pelanggan menerima keadaan baru melalui penutupan.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Aliran searah: tindakan → peredam → status baru → pelanggan. Mudah untuk dipikirkan dan diuji.
- Keamanan thread: antrian pengiriman membuat serial mutasi negara.
- Pelanggan mendapatkan status penuh — gunakan penyeleksi atau pemeriksaan`Equatable`untuk menghindari perenderan ulang yang tidak diperlukan.
- Produksi: gunakan`The Composable Architecture`(TCA) oleh Point-Free untuk implementasi tingkat produksi dengan efek, pengujian, dan integrasi SwiftUI.
---

## Ringkasan
Swift adalah bahasa modern, aman, dan ekspresif yang penting untuk pengembangan platform Apple. Penekanannya pada keamanan (opsional, tipe nilai, pencocokan pola) mencegah seluruh kategori bug. Di luar platform Apple, Swift berkembang dalam pengembangan sisi server dan aplikasi lintas platform. Untuk pengembangan iOS/macOS, Swift adalah pilihan yang jelas. Untuk domain lain, ini adalah bahasa yang mumpuni dengan ekosistem yang lebih kecil namun terus berkembang.