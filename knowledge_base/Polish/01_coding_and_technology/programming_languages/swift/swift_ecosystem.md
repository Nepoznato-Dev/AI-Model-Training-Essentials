<!--
---
# Metadata
title: "Swift — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Swift ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [swift, ecosystem, tooling, apple, ios, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Swift — przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie Swift.
---

## Łańcuch narzędzi
| Narzędzie | Cel |
|------|-------------|
| **szybki** | Kompilator i REPL |
| **szybki** | Szybki kompilator |
| **Szybki menedżer pakietów (SPM)** | Wbudowany menedżer pakietów |
| **Xkod** | IDE firmy Apple (tylko macOS) |
| **xcodebuild** | Narzędzie do tworzenia CLI |
| **xcrun** | Narzędzie dla programistów uruchamiające |
| **Instrumenty** | Profilowanie wydajności |
| **SwiftLint** | Linting kodu |
| **SwiftFormat** | Formatowanie kodu |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## Zarządzanie pakietami
| Narzędzie | Wpisz | Notatki |
|------|------|------|
| **Swift Menedżer pakietów** | Wbudowany | Oficjalna, wieloplatformowa platforma Apple |
| **CocoaPods** | Na bazie rubinu | iOS/macOS, duży ekosystem |
| **Kartagina** | Zdecentralizowany | Frameworki binarne |
| **Tuista** | Generowanie projektu | Zarządzanie projektami Xcode |
```swift
// Package.swift
// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "MyApp",
    platforms: [.macOS(.v14), .iOS(.v17)],
    dependencies: [
        .package(url: "https://github.com/Alamofire/Alamofire", from: "5.9.0"),
        .package(url: "https://github.com/SwiftyJSON/SwiftyJSON", from: "5.0.0"),
    ],
    targets: [
        .executableTarget(
            name: "MyApp",
            dependencies: ["Alamofire", "SwiftyJSON"]),
        .testTarget(name: "MyAppTests", dependencies: ["MyApp"]),
    ]
)
```

---

## Struktury internetowe (Swift po stronie serwera)
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Para** | Pełny stos | Najpopularniejszy, gotowy do produkcji |
| **Koliber** | Lekki | Szybki, nowoczesny, przede wszystkim asynchroniczny |
| **Kitura** | IBM | Przedsiębiorstwo (archiwum) |
| **Idealny** | Modułowe | Swift po stronie serwera |
```swift
// Vapor example
import Vapor

func routes(_ app: Application) throws {
    app.get("hello") { req in
        "Hello, World!"
    }

    app.get("users", ":id") { req async throws -> User in
        let id = req.parameters.get("id")!
        return try await User.find(id, on: req.db) ?? abort(.notFound)
    }
}
```

---

## Baza danych i ORM
| Technologia | Wpisz |
|------------|------|
| **Płynny** | ORM Vapor (PostgreSQL, MySQL, SQLite) |
| **GRDB** | Zestaw narzędzi SQLite |
| **Kraina** | Mobilna baza danych |
| **Podstawowe dane** | Struktura wykresów obiektowych firmy Apple |
| **SwiftDane** | Nowoczesna trwałość Apple (iOS 17+) |
| **PostgresNIO** | Sterownik PostgreSQL (asynchroniczny) |
---

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **XCTest** | Wbudowane testy Apple |
| **Szybkie** | Testowanie w stylu BDD |
| **Zwinny** | Framework Matchera (paruje się z Quick) |
| **Szybkie testowanie** | Nowoczesne oparte na makrach (Swift 5.9+) |
| **Testowanie migawek** | Testowanie interfejsu użytkownika/migawki |
| **OHHTTPStuby** | Stubbing HTTP |
```swift
// Swift Testing (modern)
import Testing

@Test("user creation")
func createUser() async throws {
    let service = UserService()
    let user = try await service.create(name: "Alice", email: "alice@example.com")
    #expect(user.name == "Alice")
    #expect(user.email == "alice@example.com")
}

// XCTest
class UserServiceTests: XCTestCase {
    func testCreateUser() async throws {
        let service = UserService()
        let user = try await service.create(name: "Alice", email: "alice@example.com")
        XCTAssertEqual(user.name, "Alice")
    }
}
```

---

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **SwiftLint** | Linting, egzekwowanie stylu |
| **SwiftFormat** | Formatowanie kodu |
| **SwiftLint + niestandardowe reguły** | Zasady specyficzne dla projektu |
| **Pyferia** | Wykrywanie niewykorzystanego kodu |
| **SonarQube** | Platforma jakości kodu |
```yaml
# .swiftlint.yml
included:
  - Sources
excluded:
  - Tests/.build

line_length:
  warning: 120
  error: 200

type_body_length:
  warning: 300
  error: 500
```

---

## Struktury Apple (iOS/macOS)
| Ramy | Cel |
|---------------|--------|
| **SwiftUI** | Deklaratywny interfejs użytkownika (wszystkie platformy Apple) |
| **UIKit** | Tradycyjny interfejs iOS |
| **Aplikacja** | Interfejs macOS |
| **Połącz** | Programowanie reaktywne |
| **asynchronizacja/oczekiwanie** | Współbieżność (szybka współbieżność) |
| **Aktorzy** | Zmienny stan bezpieczny dla wątków |
| **CoreML** | Uczenie maszynowe |
| **ARKit** | Rzeczywistość rozszerzona |
| **Zestaw zdrowotny** | Dane zdrowotne |
| **CloudKit** | Integracja z iCloud |
| **WidgetKit** | Widżety |
| **StoreKit 2** | Zakupy w aplikacji |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Alamofire** | Sieć HTTP |
| **Zimorodek / Nuke** | Ładowanie/buforowanie obrazu |
| **SnapKit** | Automatyczny układ DSL |
| **Lotti** | Animacje After Effects |
| **SwiftyJSON** | Analiza JSON |
| **Kodowane** | Wbudowana serializacja |
| **Dostęp do pęku kluczy** | Bezpieczne przechowywanie danych uwierzytelniających |
| **SwiftLint** | Linting kodu |
| **RxSwift** | Rozszerzenia reaktywne |
| **Architektura komponowalna** | Architektura jednokierunkowa |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Xkod** | Wymagane do rozwoju platformy Apple |
| **Kod VS + Swift** | Szybki rozwój międzyplatformowy |
| **Neovim + sourcekit-lsp** | Oparte na terminalu |
| **Kod aplikacji** | JetBrains (wycofane, użyj Xcode) |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Sklep z aplikacjami** | Dystrybucja iOS/macOS |
| **Lot testowy** | Testy beta |
| **Szybka linia** | Zautomatyzowane budowanie/wdrażanie |
| **Chmura Xcode** | CI/CD firmy Apple |
| **Działania na GitHubie** | Wieloplatformowy CI |
| **Doker** | Wdrożenie Swift po stronie serwera |
| **Vapor na Railway/Fly.io** | Hosting po stronie serwera |
---

## Streszczenie
Ekosystem Swift jest podzielony na platformę Apple i Swift po stronie serwera. Dla Apple: **Xcode** jako IDE, **SwiftUI** dla interfejsu użytkownika, **Swift Concurrency** (asynchronizacja/oczekiwanie, aktorzy) dla równoległości, **SwiftData** lub **Core Data** dla trwałości oraz **XCTest** lub **Swift Testing** dla testów. Po stronie serwera: **Vapor** lub **Hummingbird** jako framework, **SPM** dla pakietów i **Docker** do wdrożenia. SwiftLint wymusza jakość kodu. Mocne strony Swifta to bezpieczeństwo (opcje, typy wartości), wydajność (skompilowana, LLVM) i nowoczesna składnia. Ekosystem jest niezbędny dla każdego, kto tworzy aplikacje na iOS, macOS, watchOS lub tvOS.