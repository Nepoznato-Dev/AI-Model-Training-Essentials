<!--
---
# Metadata
title: "Swift — Syntax Reference"
description: "Detailed syntax reference for Swift covering optionals, control flow, protocols, generics, concurrency, property wrappers, and modern Swift features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [swift, syntax-reference, optionals, protocols, generics, concurrency, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Swift — 구문 참조
이 문서는 Swift(5.9+)에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, 옵션, 프로토콜 지향 프로그래밍 및 최신 동시성에 중점을 두어 기본 Swift 참조를 보완합니다.
---

## 연산자 및 표현식
### 핵심 운영자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `+``-``*``/``%`| 산술 | `a + b`| |
| `..``...` | 범위 | `1...10`|  `...`가 닫혔습니다. `..<`반열림 |
| `==``!=``<``>``<=``>=` | 비교 | `a == b`|`Equatable`/`Comparable`필요 |
| `===``!==` | 정체성 | `a === b`| 동일한 참조(수업에만 해당) |
| `&&``\|\|``!`| 논리적 | `a && b`| 단락 |
| `??`| Nil 합체 | `a ?? b`| `a`가 nil인 경우 `b`를 반환합니다. |
| `?.`| 선택적 체인 | `a?.b`| `a`가 nil인 경우 nil을 반환합니다. |
| `!`| 강제 풀기 | `a!`| nil인 경우 충돌 — 방지 |
| `&`| 입력 매개변수 | `swap(&a, &b)`| 참조로 전달 |
### Nil 처리 연산자
```swift
// Optional chaining — returns optional
let count: Int? = "hello".firstIndex(of: "e").map { "hello".distance(from: "hello".startIndex, to: $0) }

// Nil coalescing — provide default
let name: String? = nil
let display = name ?? "Anonymous"

// Force unwrap — crashes if nil (avoid in production)
let value: Int? = 42
let forced = value!  // 42 — but crashes if nil

// Optional binding
if let unwrapped = value {
    print(unwrapped)
}

// Shorthand (Swift 5.7+)
if let value {
    print(value)
}

// Guard let
guard let value else { return }
```

---

## 제어 흐름
### 패턴 매칭
```swift
// Switch with pattern matching
switch value {
case 0:
    print("zero")
case 1...9:
    print("single digit")
case let x where x % 2 == 0:
    print("\(x) is even")
default:
    print("other")
}

// Tuple matching
let point = (x: 3, y: -2)
switch point {
case (0, 0):
    print("origin")
case (_, 0):
    print("on x-axis")
case (0, _):
    print("on y-axis")
case (-2...2, -2...2):
    print("near origin")
default:
    print("far from origin")
}

// Enum with associated values
enum NetworkResult {
    case success(Data, URLResponse)
    case failure(Error)
}

switch result {
case .success(let data, let response) where response.statusCode == 200:
    process(data)
case .success(_, let response):
    print("Status: \(response.statusCode)")
case .failure(let error):
    print("Error: \(error)")
}

// if/switch expressions (Swift 5.9+)
let label = switch state {
case .active: "Active"
case .inactive: "Inactive"
case .pending: "Pending"
}
```

---

## 심층 옵션
```swift
// Optional is an enum
enum Optional<Wrapped> {
    case none
    case some(Wrapped)
}

// Optional mapping
let number: Int? = Int("42")
let doubled = number.map { $0 * 2 }           // Optional(84)
let string = number.map { String($0) }         // Optional("42")

// Optional flatMap
let nested: Int?? = Optional(Optional(42))
let flat = nested.flatMap { $0 }               // Optional(42)

// Filter
let even: Int? = 42
let result = even.filter { $0 > 50 }          // nil (42 is not > 50)

// try? — convert throwing to optional
let data = try? fetchFromNetwork()

// Implicitly unwrapped optional (rare — for IBOutlets)
var label: UILabel!
```

---

## 프로토콜 및 제네릭
```swift
// Protocol with associated type
protocol Container {
    associatedtype Item
    var count: Int { get }
    mutating func add(_ item: Item)
    subscript(i: Int) -> Item { get }
}

// Generic function with protocol constraint
func findIndex<T: Equatable>(of value: T, in array: [T]) -> Int? {
    for (index, item) in array.enumerated() {
        if item == value { return index }
    }
    return nil
}

// Protocol with default implementation
extension Collection where Element: Equatable {
    func containsAll(_ elements: [Element]) -> Bool {
        elements.allSatisfy { contains($0) }
    }
}

// Opaque types (some)
func makeAnimal() -> some Animal {
    Dog()  // Caller knows it's Animal, but not which specific type
}

// Existential types (any)
func feedAll(animals: [any Animal]) {
    for animal in animals {
        animal.eat()
    }
}
```

---

## 동시성
```swift
// async/await
func fetchUser(id: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, response) = try await URLSession.shared.data(from: url)
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw APIError.badResponse
    }
    return try JSONDecoder().decode(User.self, from: data)
}

// Task — fire and forget
Task {
    let user = try await fetchUser(id: "1")
    await MainActor.run { self.user = user }
}

// TaskGroup — structured concurrency
func loadDashboard() async throws -> Dashboard {
    try await withThrowingTaskGroup(of: DashboardComponent.self) { group in
        group.addTask { .user(try await fetchUser(id: "1")) }
        group.addTask { .posts(try await fetchPosts(userId: "1")) }
        group.addTask { .notifications(try await fetchNotifications()) }

        var components = DashboardComponents()
        for try await component in group {
            components.add(component)
        }
        return Dashboard(components: components)
    }
}

// Actor — safe mutable state
actor Counter {
    private var value = 0
    func increment() { value += 1 }
    func get() -> Int { value }
}

// Sendable — concurrency-safe types
struct UserDTO: Sendable, Codable {
    let id: String
    let name: String
}
```

---

## 속성 래퍼 및 결과 빌더
```swift
// Property wrapper
@propertyWrapper
struct Trimmed {
    private var value: String = ""
    var wrappedValue: String {
        get { value }
        set { value = newValue.trimmingCharacters(in: .whitespacesAndNewlines) }
    }
    init(wrappedValue: String) { self.wrappedValue = wrappedValue }
}

struct Article {
    @Trimmed var title: String
    @Trimmed var body: String
}

// Result builder (like SwiftUI's ViewBuilder)
@resultBuilder
struct HTMLBuilder {
    static func buildBlock(_ components: String...) -> String {
        components.joined(separator: "\n")
    }
    static func buildOptional(_ component: String?) -> String {
        component ?? ""
    }
    static func buildEither(first: String) -> String { first }
    static func buildEither(second: String) -> String { second }
}

func html(@HTMLBuilder content: () -> String) -> String {
    "<html><body>\(content())</body></html>"
}
```

---

## 요약
Swift의 구문은 안전성과 표현력의 균형을 유지합니다. 옵션은 널 충돌을 제거하고, 프로토콜은 상속 없이 유연한 구성을 가능하게 하며, 최신 동시성(비동기/대기, 행위자)을 통해 안전한 동시 프로그래밍에 액세스할 수 있게 해줍니다. 언어는 매개변수 팩, 매크로, 소유권과 같은 기능을 통해 계속해서 발전하고 있습니다. 각각의 기능이 추가되면 Swift의 핵심 약속인 코드 구성이 안전하다는 것을 유지하면서 Swift를 더욱 안전하고 강력하게 만들 수 있습니다.