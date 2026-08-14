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
# Swift — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz Swift ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Alet Zinciri
| Araç | Amaç |
|------|------------|
| **hızlı** | Derleyici ve REPL |
| **hızlı** | Hızlı derleyici |
| **Swift Paket Yöneticisi (SPM)** | Yerleşik paket yöneticisi |
| **Xcode** | Apple'ın IDE'si (yalnızca macOS) |
| **xcodebuild** | CLI oluşturma aracı |
| **xcrun** | Geliştirici aracı çalıştırıcısı |
| **Enstrümanlar** | Performans profili oluşturma |
| **SwiftLint** | Kod astarlama |
| **Hızlı Format** | Kod biçimlendirme |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## Paket Yönetimi
| Araç | Tür | Notlar |
|------|------|----------|
| **Swift Paket Yöneticisi** | Dahili | Apple'ın resmi, platformlar arası |
| **CocoaPod'lar** | Ruby tabanlı | iOS/macOS, büyük ekosistem |
| **Kartaca** | Merkezi Olmayan | İkili çerçeveler |
| **Tuist** | Proje oluşturma | Xcode proje yönetimi |
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

## Web Çerçeveleri (Sunucu Tarafı Swift)
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Buhar** | Tam yığın | En popüler, üretime hazır |
| **sinek kuşu** | Hafif | Hızlı, modern, asenkron öncelikli |
| **Kitura** | IBM | Kurumsal (arşivlenmiş) |
| **Mükemmel** | Modüler | Sunucu Tarafı Swift |
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

## Veritabanı ve ORM
| Teknoloji | Tür |
|---------------|------|
| **Akıcı** | Vapor'un ORM'si (PostgreSQL, MySQL, SQLite) |
| **GRDB** | SQLite araç seti |
| **Bölge** | Mobil veritabanı |
| **Temel Veriler** | Apple'ın nesne grafiği çerçevesi |
| **SwiftData** | Modern Apple kalıcılığı (iOS 17+) |
| **PostgresNIO** | PostgreSQL sürücüsü (zaman uyumsuz) |
---

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **XCTest** | Apple'ın yerleşik testi |
| **Hızlı** | BDD tarzı testler |
| **çevik** | Eşleştirici çerçevesi (Hızlı ile eşleşir) |
| **Hızlı Test** | Modern makro tabanlı (Swift 5.9+) |
| **Anlık Görüntü Testi** | Kullanıcı arayüzü/anlık görüntü testi |
| **OHHTTPStub'lar** | HTTP saplama |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **SwiftLint** | Linting, stil uygulaması |
| **Hızlı Format** | Kod biçimlendirme |
| **SwiftLint + özel kurallar** | Projeye özel kurallar |
| **Çevre** | Kullanılmayan kod tespiti |
| **SonarQube** | Kod kalitesi platformu |
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

## Apple Çerçeveleri (iOS/macOS)
| Çerçeve | Amaç |
|-----------|------------|
| **SwiftUI** | Bildirime dayalı kullanıcı arayüzü (tüm Apple platformları) |
| **UIKit** | Geleneksel iOS Kullanıcı Arayüzü |
| **AppKit** | macOS kullanıcı arayüzü |
| **Combine** | Reactive programming |
| **async/await** | Eşzamanlılık (Hızlı Eşzamanlılık) |
| **Aktörler** | İş parçacığı açısından güvenli değişken durum |
| **CoreML** | Makine öğrenimi |
| **ARKit** | Augmented reality |
| **HealthKit** | Sağlık verileri |
| **CloudKit** | iCloud entegrasyonu |
| **WidgetKit** | Widgets |
| **StoreKit 2** | Uygulama içi satın alımlar |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Alamofire** | HTTP ağı |
| **Yalıçapkını / Nükleer Silah** | Resim yükleme/önbelleğe alma |
| **SnapKit** | Otomatik Düzen DSL |
| **Lottie** | After Effects animasyonları |
| **SwiftyJSON** | JSON ayrıştırma |
| **Kodlanabilir** | Dahili serileştirme |
| **Anahtarlık Erişimi** | Güvenli kimlik bilgileri depolama |
| **SwiftLint** | Kod astarlama |
| **RxSwift** | Reaktif uzantılar |
| **Şekillendirilebilir Mimari** | Tek yönlü mimari |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **Xcode** | Apple platformu geliştirme için gereklidir |
| **VS Code + Swift** | Platformlar arası Swift geliştirme |
| **Neovim + kaynak kiti-lsp** | Terminal tabanlı |
| **AppCode** | JetBrains (üretilmiyor, Xcode kullanın) |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Uygulama Mağazası** | iOS/macOS dağıtımı |
| **Test Uçuşu** | Beta testi |
| **Hızlı Yol** | Otomatik derleme/dağıtım |
| **Xcode Bulutu** | Apple'ın CI/CD'si |
| **GitHub Eylemleri** | Platformlar arası CI |
| **Docker** | Sunucu tarafı Swift dağıtımı |
| **Demiryolu/Fly.io'daki buhar** | Sunucu tarafı barındırma |
---

## Özet
Swift'in ekosistemi, Apple platformu geliştirme ve sunucu tarafı Swift arasında bölünmüştür. Apple için: IDE olarak **Xcode**, kullanıcı arayüzü için **SwiftUI**, paralellik için **Swift Concurrency** (eşzamansız/beklemede, aktörler), kalıcılık için **SwiftData** veya **Core Data** ve testler için **XCTest** veya **Swift Test**. Sunucu tarafı için: Çerçeve olarak **Vapor** veya **Hummingbird**, paketler için **SPM** ve dağıtım için **Docker**. SwiftLint kod kalitesini zorlar. Swift'in güçlü yönleri güvenlik (isteğe bağlı özellikler, değer türleri), performans (derlenmiş, LLVM) ve modern sözdizimidir. Ekosistem iOS, macOS, watchOS veya tvOS uygulamaları geliştiren herkes için gereklidir.