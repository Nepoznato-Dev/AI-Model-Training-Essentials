---
# Metadata
title: "Swift — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, Swift code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [swift, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Swift — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔한 Swift 코드 작성을 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 옵션 및 안전
```swift
// ✅ guard for early exit
func process(user: User?) {
    guard let user else { return }
    // user is unwrapped here
    print(user.name)
}

// ✅ if let for optional binding
if let name = user?.name {
    print("Hello, \(name)")
}

// ✅ Nil-coalescing
let displayName = user?.name ?? "Anonymous"

// ✅ Optional chaining
let city = user?.address?.city

// ✅ fatalError for impossible states
switch suit {
case .hearts, .diamonds: print("Red")
case .clubs, .spades: print("Black")
}
// No default needed — compiler checks exhaustiveness
```

---

## 값 유형
```swift
// ✅ Prefer structs over classes
struct User: Identifiable, Hashable {
    let id: UUID
    var name: String
    var email: String
}

// ✅ let by default, var only when needed
let name = "Alice"  // immutable
var count = 0       // mutable

// ✅ Copy-on-write for large structs
struct LargeData {
    private var _storage: [Int]
    // COW semantics
}
```

---

## 열거형 및 패턴 일치
```swift
// ✅ Enums with associated values
enum Result<Value> {
    case success(Value)
    case failure(Error)
}

enum Payment {
    case cash(Double)
    case card(number: String, expiry: String)
    case digital(provider: String)
}

// ✅ Pattern matching with switch
switch payment {
case .cash(let amount):
    print("Cash: $\(amount)")
case .card(let number, _) where number.hasSuffix("1234"):
    print("Known card")
case .card:
    print("Other card")
case .digital(let provider):
    print("Digital: \(provider)")
}

// ✅ Enum with methods
enum Status: String, CaseIterable {
    case active, inactive, pending
    
    var displayName: String {
        switch self {
        case .active: "Active"
        case .inactive: "Inactive"
        case .pending: "Pending Review"
        }
    }
}
```

---

## 프로토콜 및 제네릭
```swift
// ✅ Protocol-oriented design
protocol Repository {
    associatedtype Entity
    func find(id: String) async throws -> Entity?
    func save(_ entity: Entity) async throws
}

// ✅ Protocol extensions for default behavior
extension Repository {
    func findAll() async throws -> [Entity] {
        // default implementation
        []
    }
}

// ✅ Generic constraints
func largest<T: Comparable>(_ values: [T]) -> T? {
    values.max()
}

// ✅ where clause
func process<T: Collection>(items: T) where T.Element: Hashable {
    let unique = Set(items)
}
```

---

## 동시성
```swift
// ✅ async/await
func fetchUser(id: Int) async throws -> User {
    let response = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: response.0)
}

// ✅ async let for parallel execution
async let users = fetchUsers()
async let posts = fetchPosts()
let dashboard = try await Dashboard(users: users, posts: posts)

// ✅ TaskGroup for dynamic parallelism
let results = try await withThrowingTaskGroup(of: Data.self) { group in
    for url in urls {
        group.addTask { try await download(url) }
    }
    var collected: [Data] = []
    for try await data in group {
        collected.append(data)
    }
    return collected
}

// ✅ @MainActor for UI updates
@MainActor
func updateUI(with user: User) {
    nameLabel.text = user.name
}
```

---

## 클로저 및 기능
```swift
// ✅ Trailing closure syntax
let names = users
    .filter { $0.isActive }
    .map { $0.name }
    .sorted()

// ✅ Key paths as functions
let names = users.map(\.name)

// ✅ Shorthand argument names
let doubled = numbers.map { $0 * 2 }

// ✅ Closure with explicit capture list
var value = 0
let closure = { [weak self] in
    self?.update()
}
```

---

## 요약
Swift 관용구는 안전(옵션, 가드), 값 유형(구조체), 프로토콜 지향 설계, 패턴 일치, 비동기/대기 및 불변성(기본적으로 `let`)을 강조합니다. Swift API 디자인 지침을 따르고 코드 품질을 위해 SwiftLint를 사용하고 서식 지정을 위해 SwiftFormat을 사용하세요. Swift는 안전성과 표현력을 중요하게 생각합니다. "컴파일한다면 아마도 정확할 것입니다."