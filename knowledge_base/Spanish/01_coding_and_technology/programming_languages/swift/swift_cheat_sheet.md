---
# Metadata
title: "Swift — Cheat Sheet"
description: "Quick-reference cheat sheet for Swift syntax, optionals, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [swift, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Swift – Hoja de trucos
## Conceptos básicos
```swift
// Variables
var name = "Alice"       // mutable
let age = 30             // immutable
let pi: Double = 3.14159
let active: Bool = true

// Type annotations
var count: Int = 42
var text: String = "hello"
var items: [Int] = [1, 2, 3]
var lookup: [String: Int] = ["alice": 90]

// String interpolation
"Hello, \(name)! Age: \(age)"
"Pi is \(String(format: "%.2f", pi))"

// String methods
name.count
name.uppercased()
name.lowercased()
name.trimmingCharacters(in: .whitespaces)
name.contains("lic")
name.hasPrefix("Al")
name.replacingOccurrences(of: "Alice", with: "Bob")
name.dropFirst(2)  // "ice"
```

## Opcionales
```swift
// Optional declaration
var email: String? = nil
var phone: String? = "555-1234"

// Unwrapping
if let email = email {
    print(email)  // safely unwrapped
}

// Guard
guard let phone = phone else { return }
print(phone)  // available from here

// Nil coalescing
let value = phone ?? "N/A"

// Optional chaining
let length = email?.count  // Optional<Int>

// Force unwrap (avoid)
let forced = phone!  // crash if nil

// Map & flatMap
let upper = email.map { $0.uppercased() }  // Optional<String>

// if let shorthand (Swift 5.7+)
if let email {
    print(email)
}
```

## Estructuras de datos
```swift
// Array
var arr = [1, 2, 3]
arr.append(4)
arr.insert(0, at: 0)
arr[1...3]  // slice (ArraySlice)
arr.map { $0 * 2 }
arr.filter { $0 > 2 }
arr.reduce(0, +)
arr.enumerated()  // (offset, element)
arr.sorted()
arr.first(where: { $0 > 2 })

// Dictionary
var dict = ["alice": 90, "bob": 85]
dict["charlie"] = 78
dict["alice"]  // Optional<Int>
dict.keys
dict.values
dict.map { "\($0.key): \($0.value)" }
dict.filter { $0.value >= 90 }

// Set
var set: Set<Int> = [1, 2, 3]
set.insert(4)
set.contains(2)
set.union([5, 6])
set.intersection([2, 3])

// Tuple
let point = (x: 3.0, y: 4.0)
point.x
let (x, y) = point
```

## Controlar el flujo
```swift
if condition {
    // ...
} else if other {
    // ...
} else {
    // ...
}

// Ternary
let result = condition ? "yes" : "no"

// Switch
switch value {
case 0:
    print("zero")
case 1...9:
    print("single digit")
case let n where n > 100:
    print("big")
default:
    print("other")
}

// Enum-based switch
enum Direction { case north, south, east, west }
switch direction {
case .north: print("up")
case .south: print("down")
case .east, .west: print("sideways")
}

// Loops
for item in collection { ... }
for (i, item) in collection.enumerated() { ... }
for i in 0..<10 { ... }      // 0 to 9
for i in 0...10 { ... }      // 0 to 10
for i in stride(from: 0, to: 100, by: 5) { ... }
while condition { ... }
```

## Estructuras y clases
```swift
// Struct (value type)
struct Point {
    var x: Double
    var y: Double

    func distance(to other: Point) -> Double {
        sqrt((x - other.x) ** 2 + (y - other.y) ** 2)
    }

    mutating func moveBy(dx: Double, dy: Double) {
        x += dx
        y += dy
    }
}

// Class (reference type)
class User {
    let name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    deinit { /* cleanup */ }
}

// Enum with associated values
enum Result<Success, Failure: Error> {
    case success(Success)
    case failure(Failure)
}

// Enum with methods
enum Suit: String, CaseIterable {
    case hearts, diamonds, clubs, spades
    var symbol: String {
        switch self {
        case .hearts: return "♥"
        case .diamonds: return "♦"
        case .clubs: return "♣"
        case .spades: return "♠"
        }
    }
}
```

## Protocolos y extensiones
```swift
protocol Drawable {
    func draw() -> String
    var color: String { get }
}

extension Drawable {
    var color: String { "black" }  // default implementation
}

struct Circle: Drawable {
    let radius: Double
    func draw() -> String { "Circle r=\(radius)" }
}

// Protocol composition
func render(_ shape: Drawable & Printable) { ... }

// Extension
extension String {
    var isBlank: Bool { trimmingCharacters(in: .whitespaces).isEmpty }
    func repeated(_ times: Int) -> String { (0..<times).map { _ in self }.joined() }
}
```

## Cierres y asincrónicos
```swift
// Closure
let square: (Int) -> Int = { $0 * $0 }
let add: (Int, Int) -> Int = { $0 + $1 }
arr.map { $0 * 2 }
arr.filter { $0 > 5 }
arr.sort { $0 < $1 }

// Trailing closure
UIView.animate(withDuration: 0.3) {
    view.alpha = 0
}

// Async/Await
func fetchUser(id: Int) async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// Task
Task {
    let user = try await fetchUser(id: 1)
    await MainActor.run { updateUI(user) }
}

// AsyncSequence
for await item in stream {
    process(item)
}
```

## Manejo de errores
```swift
enum AppError: Error {
    case notFound
    case unauthorized(String)
}

func load(id: Int) throws -> Data {
    guard id > 0 else { throw AppError.notFound }
    return Data()
}

do {
    let data = try load(id: 1)
} catch AppError.notFound {
    print("Not found")
} catch AppError.unauthorized(let reason) {
    print("Unauthorized: \(reason)")
} catch {
    print("Unexpected: \(error)")
}

// try?
let data = try? load(id: 1)  // Optional<Data>

// try!
let data = try! load(id: 1)  // crash on error
```
