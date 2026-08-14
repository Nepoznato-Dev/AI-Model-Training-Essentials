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
# Swift — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Swift.
---

## Rantai Alat
| Alat | Tujuan |
|------|---------|
| **cepat** | Kompiler dan REPL |
| **cepat** | Kompiler cepat |
| **Manajer Paket Swift (SPM)** | Manajer paket bawaan |
| **Kode X** | IDE Apple (hanya macOS) |
| **xcodebuild** | Alat pembuatan CLI |
| **xcrun** | Pelari alat pengembang |
| **Instrumen** | Profil kinerja |
| **SwiftLint** | Linting kode |
| **Format Cepat** | Pemformatan kode |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## Manajemen Paket
| Alat | Ketik | Catatan |
|------|------|-------|
| **Manajer Paket Swift** | Bawaan | Resmi Apple, lintas platform |
| **CocoaPod** | Berbasis Ruby | iOS/macOS, ekosistem besar |
| **Kartago** | Terdesentralisasi | Kerangka biner |
| **Tuis** | Pembuatan proyek | Manajemen proyek Xcode |
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

## Kerangka Web (Swift Sisi Server)
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Uap** | Tumpukan penuh | Paling populer, siap produksi |
| **Burung Kolibri** | Ringan | Cepat, modern, mengutamakan asinkron |
| **Kitura** | IBM | Perusahaan (diarsipkan) |
| **Sempurna** | Modular | Swift sisi server |
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

## Basis Data & ORM
| Teknologi | Ketik |
|------------|------|
| **Fancar** | ORM Vapor (PostgreSQL, MySQL, SQLite) |
| **GRDB** | Perangkat SQLite |
| **Alam** | Basis data seluler |
| **Data Inti** | Kerangka grafik objek Apple |
| **SwiftData** | Kegigihan Apple modern (iOS 17+) |
| **PostgresNIO** | Driver PostgreSQL (asinkron) |
---

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Tes XCT** | Pengujian bawaan Apple |
| **Cepat** | Pengujian gaya BDD |
| **Cecah** | Kerangka kerja pencocokan (dipasangkan dengan Quick) |
| **Pengujian Cepat** | Berbasis makro modern (Swift 5.9+) |
| **Pengujian Snapshot** | Pengujian UI/snapshot |
| **OHHTTPStub** | Matikan HTTP |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **SwiftLint** | Linting, penegakan gaya |
| **Format Cepat** | Pemformatan kode |
| **SwiftLint + aturan khusus** | Aturan khusus proyek |
| **Pinggiran** | Deteksi kode yang tidak digunakan |
| **SonarQube** | Platform kualitas kode |
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

## Kerangka Apple (iOS/macOS)
| Kerangka | Tujuan |
|-----------|---------|
| **SwiftUI** | UI Deklaratif (semua platform Apple) |
| **UIKit** | UI iOS tradisional |
| **AppKit** | macOS UI |
| **Gabungkan** | Pemrograman reaktif |
| **asinkron/tunggu** | Konkurensi (Konkurensi Cepat) |
| **Aktor** | Status thread-safe bisa berubah |
| **CoreML** | Pembelajaran mesin |
| **ARKit** | realitas tertambah |
| **Peralatan Kesehatan** | Data kesehatan |
| **CloudKit** | Integrasi iCloud |
| **Kit Widget** | Widget |
| **StoreKit 2** | Pembelian dalam aplikasi |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Alamofire** | Jaringan HTTP |
| **Kingfisher / Nuke** | Pemuatan/cache gambar |
| **SnapKit** | DSL Tata Letak Otomatis |
| **Lottie** | Animasi After Effects |
| **SwiftyJSON** | Penguraian JSON |
| **Dapat dikodekan** | Serialisasi bawaan |
| **Akses Gantungan Kunci** | Penyimpanan kredensial yang aman |
| **SwiftLint** | Linting kode |
| **RxSwift** | Ekstensi reaktif |
| **Arsitektur Komposable** | Arsitektur searah |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode X** | Diperlukan untuk pengembangan platform Apple |
| **Kode VS + Swift** | Pengembangan Swift lintas platform |
| **Neovim + sourcekit-lsp** | Berbasis terminal |
| **Kode Aplikasi** | JetBrains (dihentikan, gunakan Xcode) |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Toko Aplikasi** | Distribusi iOS/macOS |
| **Penerbangan Uji** | Pengujian beta |
| **Jalur Cepat** | Pembuatan/penerapan otomatis |
| **Xcode Awan** | CI/CD Apple |
| **Tindakan GitHub** | CI lintas platform |
| **Buruh pelabuhan** | Penerapan Swift sisi server |
| **Uap di Kereta Api/Fly.io** | Hosting sisi server |
---

## Ringkasan
Ekosistem Swift terbagi antara pengembangan platform Apple dan Swift sisi server. Untuk Apple: **Xcode** sebagai IDE, **SwiftUI** untuk UI, **Swift Concurrency** (async/await, actor) untuk paralelisme, **SwiftData** atau **Core Data** untuk persistensi, dan **XCTest** atau **Swift Testing** untuk pengujian. Untuk sisi server: **Vapor** atau **Hummingbird** sebagai kerangka kerja, **SPM** untuk paket, dan **Docker** untuk penerapan. SwiftLint menerapkan kualitas kode. Kekuatan Swift adalah keamanan (opsional, tipe nilai), kinerja (dikompilasi, LLVM), dan sintaksis modern. Ekosistem ini penting bagi siapa pun yang membuat aplikasi iOS, macOS, watchOS, atau tvOS.