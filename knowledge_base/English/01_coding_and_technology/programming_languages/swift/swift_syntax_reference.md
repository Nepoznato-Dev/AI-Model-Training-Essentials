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
# Swift — Syntax Reference

This document provides a comprehensive, structured syntax reference for Swift (5.9+). It complements the main Swift reference by focusing on exhaustive syntax patterns, optionals, protocol-oriented programming, and modern concurrency.

---

## Operators & Expressions

### Core Operators

| Operator | Name | Example | Notes |
|----------|------|---------|-------|
| `+` `-` `*` `/` `%` | Arithmetic | `a + b` | |
| `..` `...` | Range | `1...10` | `...` closed; `..<` half-open |
| `==` `!=` `<` `>` `<=` `>=` | Comparison | `a == b` | Requires `Equatable`/`Comparable` |
| `===` `!==` | Identity | `a === b` | Same reference (classes only) |
| `&&` `\|\|` `!` | Logical | `a && b` | Short-circuit |
| `??` | Nil coalescing | `a ?? b` | Returns `b` if `a` is nil |
| `?.` | Optional chaining | `a?.b` | Returns nil if `a` is nil |
| `!` | Force unwrap | `a!` | Crashes if nil — avoid |
| `&` | Inout parameter | `swap(&a, &b)` | Pass by reference |

### Nil Handling Operators

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

## Control Flow

### Pattern Matching

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

## Optionals in Depth

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

## Protocols & Generics

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

## Concurrency

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

## Property Wrappers & Result Builders

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

## Summary

Swift's syntax balances safety with expressiveness. Optionals eliminate null crashes, protocols enable flexible composition without inheritance, and modern concurrency (async/await, actors) makes safe concurrent programming accessible. The language continues to evolve with features like parameter packs, macros, and ownership — each addition making Swift safer and more powerful while maintaining its core promise: code that is safe by construction.
