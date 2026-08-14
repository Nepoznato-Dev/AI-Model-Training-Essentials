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
#スウィフト
Swift は、Apple (Chris Lattner 率いる) によって開発され、2014 年に初めてリリースされた最新のコンパイル済みプログラミング言語です。Swift は、Apple プラットフォーム開発 (iOS、macOS、watchOS、tvOS、visionOS) の主要言語として Objective-C に代わるように設計されました。 Swift は、コンパイル言語のパフォーマンスとスクリプト言語の表現力を組み合わせており、特に null 値、メモリ管理、および型エラーに関する安全性を重視しています。
Apple プラットフォームを超えて、Swift はサーバーサイド開発 (Vapor、Hummingbird)、クロスプラットフォーム アプリケーション、さらには機械学習 (Apple の Create ML) にもますます使用されています。 Swift on Server の導入とクロスプラットフォームのサポートにより、Swift は単なる「Apple 言語」以上のものになりつつあります。
---

## なぜ Swift が重要なのか
- **Apple プラットフォーム標準**: iOS、macOS、watchOS、tvOS、visionOS 開発の主要言語。
- **安全設計**: オプションにより、Null ポインターのクラッシュが排除されます。値型は、意図しない突然変異を防ぎます。
- **パフォーマンス**: LLVM 経由でネイティブ マシン コードにコンパイルします。多くのタスクにおいて C++ と競合します。
- **最新の構文**: クロージャー、ジェネリックス、プロトコル指向のプログラミング、パターン マッチングを備えたクリーンで表現力豊かな構文。
- **SwiftUI**: Apple プラットフォーム インターフェイスの構築を高速かつ直感的に行う宣言型 UI フレームワーク。
- **オープンソース**: Swift コンパイラーと標準ライブラリはオープンソースです。 Linux および Windows 上で動作します。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **Apple 中心** |最適なツールとエコシステムは Apple プラットフォーム用です |サーバー側には Vapor を使用します。クロスプラットフォームのサポートが向上しています |
| **限定されたクロスプラットフォーム GUI** | Windows/Linux 用の成熟した GUI フレームワークがない |クロスプラットフォームには Web テクノロジーまたは Flutter を使用する |
| **小規模な雇用市場 (Apple 以外)** | Java、Python、または JavaScript よりもロールが少ない | iOS/macOS 開発の役割は豊富です |
| **急速な進化** |バージョン間で構文が頻繁に変更されると、コードが破損する可能性があります。 Swift のバージョンをピン留めします。 Swift パッケージ マネージャーを使用する |
| **コンパイル時間** |複雑な汎用コードはコンパイルに時間がかかる場合があります。型式を簡素化します。 @inlinable は慎重に使用してください。
---

## 構文の基礎
### 変数と定数
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

### オプション -- Null に対する Swift の解決策
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

### 関数とクロージャ
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

### プロトコルと構造体
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

### エラー処理
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

## 高度な構文とパターン
### ジェネリック医薬品
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

### 高度なパターン マッチング
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

### プロパティ ラッパーと結果ビルダー
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

## 同時実行性と並列処理 (Swift 同時実行性)
### 非同期/待機
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

### 構造化された同時実行性
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

## プロジェクトの構成とシステムの構築
### プロジェクト構造 (Swift パッケージ)
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

### パッケージ.swift
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

### 必須コマンド
```bash
swift build                  # Build the package
swift test                   # Run tests
swift run MyExecutable       # Run executable target
swift package resolve        # Resolve dependencies
swift package update         # Update dependencies
swift package init --type executable  # New package
```

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### XCTest フレームワーク
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

## 相互運用性
### Objective-C 相互運用性
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

### C 相互運用性
```swift
import Glibc  // Linux
let result = abs(-42)  // C function
let size = MemoryLayout<Int>.size
```

---

## デザインパターン
### デリゲートパターン
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

### プロトコル指向の設計
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

## パフォーマンスと最適化
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

## SwiftUI -- 宣言型 UI
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

## デプロイメント
### サーバーサイド Swift
```bash
# Build for release
swift build -c release

# Run the server
.build/release/MyApp
```

運用環境の場合は、コンパイルされたバイナリを Ubuntu を実行している Linux サーバーにデプロイします。 systemd などのプロセス マネージャーを使用して、アプリケーションのライフサイクルを管理します。
---

## Swift を使用する場合
|シナリオ |なぜスウィフトなのか |より良い代替案 |
|----------|----------|----------|
| iOS/macOS アプリ |標準の Apple 言語 | -- |
| watchOS/visionOS アプリ |唯一のオプション | -- |
|サーバー側 (Vapor) |成長するエコシステム |より成熟したサーバー エコシステムを実現するには、Node.js を使用してください |
|クロスプラットフォームモバイル |可能ですが、プライマリではありません |フラッター、リアクトネイティブ |
|システムプログラミング |可能 (Linux) | Rust、C、C++ |
|一般的なアプリケーション開発 (Apple 以外) |限られたエコシステム | Python、Go、Java |
---

## 総合的な Q&A
### Q1: オプションとは何ですか?また、Swift がオプションのラップを解除するよう強制するのはなぜですか?
**A:** オプション (`Type?`) は、存在しない可能性のある値を表します。`.some(value)` または`.none`(nil) のいずれかです。 Swift は、実行時の null ポインターのクラッシュを防ぐために、明示的なアンラップを強制します。`if let`、`guard let`、強制アンラップ (`!`)、オプションのチェーン (`?.`)、または nil 合体 (`??`) を使用してラップを解除できます。コンパイラーは nil ケースを確実に処理できるようにします。これにより、バグのクラス全体が排除されます。
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

### Q2: Swift の構造体とクラスの違いは何ですか?
**A:** 構造体は値型 (代入時にコピー)、クラスは参照型 (共有) です。構造体は無料のメンバーごとの初期化子を取得し、継承、初期化解除子、および参照カウントを除くクラスのすべての機能をサポートします。 Swift の標準ライブラリの型 (`String`、`Array`、`Dictionary`) はすべて構造体です。デフォルトでは構造体を優先します。共有の可変状態または継承が必要な場合は、クラスを使用します。
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

### Q3: プロトコルとプロトコル指向プログラミングはどのように機能しますか?
**A:** プロトコルは、メソッド、プロパティ、要件の設計図を定義します。どのタイプでも、その要件を実装することでプロトコルに準拠できます。プロトコル拡張機能はデフォルトの実装を提供します。プロトコルによって制約されたジェネリックスは、クラス継承のオーバーヘッドなしでポリモーフィズムを実現します。これが「プロトコル指向プログラミング」です。
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

### Q4: Swift の`async/await`とは何ですか? それはアクターとどのように関係しますか?
**A:** Swift の同時実行モデル (5.5 以降) は、非同期コードに`async/await`を使用し、安全な共有可変状態に`actors`を使用します。 `async`機能は一時停止および再開できます。 `await`は一時停止ポイントをマークします。アクターは、可変状態へのアクセスをシリアル化することでデータ競合を防ぎます。コンパイラーはコンパイル時にこれを強制します。
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

### Q5: プロパティ ラッパーと結果ビルダーはどのように機能しますか?
**A:** プロパティ ラッパー (`@propertyWrapper`) は、プロパティ ストレージにロジックを追加します (SwiftUI の`@State`など)。結果ビルダー (`@resultBuilder`) を使用すると、自然な構文 (SwiftUI のビュー階層など) を使用してデータ構造を構築できます。どちらも定型文を削減するメタプログラミングの形式です。
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

## 思考連鎖による問題解決
### 問題 1: タイプセーフなルーターを構築する
**問題ステートメント:** 各ルートにパラメータが関連付けられている iOS アプリ用のタイプ セーフ URL ルーターを作成します。コンパイラは、特定のルートに存在しないパラメータへのアクセスを防ぎます。
**ステップ 1 — 問題を理解する:**
(1) 型付きパラメータを含むルート定義、(2) ルート + パラメータを抽出するための URL 解析、(3) タイプセーフなパラメータ アクセス — コンパイラは、各ルートに存在するパラメータのみを読み取ることを保証します。これには、関連付けられた値を持つ列挙型が必要です。
**ステップ 2 — アプローチを特定する:**
- 関連付けられた値を持つ列挙型を使用してルートを定義します。
- 各ケースは、その特定のパラメーターを型付きの値として保持します。
- パーサーは URL 文字列をルート列挙型のケースに変換します。
- パターン マッチングにより、コンパイル時に安全なパラメータが抽出されます。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- タイプ セーフティ: 各ルート ケースは、必要なパラメータを正確に保持します。コンパイラは、`.userProfile`上の`variant`へのアクセスを禁止します。
- 網羅性:`switch`はすべてのケースを処理する必要があります。新しいルートを追加すると、すべてのハンドラーが強制的に更新されます。
- 拡張性: enum ケースを追加することで新しいルートを追加します。コンパイラは、更新が必要な箇所をすべて通知します。
- 本番環境: 大規模なアプリの場合は、`swift-url-routing`または`TCA`のルーティングを検討してください。
### 問題 2: リアクティブ ステート コンテナーの実装
**問題ステートメント:** Swift で単純なリアクティブ ステート コンテナー (Redux/Vuex と同様) を構築します。このコンテナーでは、状態の変化が観察可能であり、サブスクライバーに特定の状態の変化が通知されます。
**ステップ 1 — 問題を理解する:**
(1) アプリケーションの状態を保持する状態コンテナー、(2) 状態の変化を記述するアクション、(3) 現在の状態 + アクションから新しい状態を生成するリデューサー、(4) 状態の変化を監視するサブスクライバーが必要です。これは単方向のデータ フロー パターンです。
**ステップ 2 — アプローチを特定する:**
-`@Published`のような動作を持つ汎用`Store<State>`クラスを使用します。
- アクションを列挙型として定義します。
- リデューサー関数`(State, Action) -> State`を使用します。
- サブスクライバーはクロージャを介して新しい状態を受け取ります。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- 一方向フロー: アクション → リデューサー → 新しい状態 → サブスクライバー。推論とテストが簡単です。
- スレッド セーフ: ディスパッチ キューは状態の変更をシリアル化します。
- サブスクライバーは完全な状態を取得します。セレクターまたは`Equatable`チェックを使用して、不必要な再レンダリングを回避します。
- 実稼働: エフェクト、テスト、および SwiftUI 統合を備えた実稼働グレードの実装には、Point-Free の`The Composable Architecture`(TCA) を使用します。
---

＃＃ まとめ
Swift は、Apple プラットフォームの開発に不可欠な、最新の安全かつ表現力豊かな言語です。安全性 (オプション、値のタイプ、パターン マッチング) に重点を置いているため、カテゴリ全体のバグが防止されます。 Apple プラットフォームを超えて、Swift はサーバーサイド開発とクロスプラットフォーム アプリケーションで成長しています。 iOS/macOS 開発には、Swift が明確な選択肢です。他のドメインにとっては、小規模ながら成長を続けるエコシステムを備えた有能な言語です。