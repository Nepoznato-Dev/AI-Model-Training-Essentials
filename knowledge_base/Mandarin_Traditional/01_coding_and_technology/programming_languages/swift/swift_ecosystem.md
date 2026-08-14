---
# Metadata
title: "Swift — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Swift ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Swift — 生態系統與工具指南
本指南涵蓋了 Swift 生態系統中的基本工具、框架和基礎設施。
---

## 工具鏈
|工具|目的|
|------|---------|
| **迅速** |編譯器和 REPL |
| **斯威夫特** | Swift 編譯器 |
| **Swift 套件管理器 (SPM)** |內建套件管理器 |
| **Xcode** | Apple 的 IDE（僅限 macOS）|
| **xcodebuild** | CLI 建置工具 |
| **xcrun** |開發者工具運行器 |
| **儀器** |性能分析 |
| **SwiftLint** |程式碼檢查 |
| **SwiftFormat** |程式碼格式化 |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## 套件管理
|工具|類型 |筆記|
|------|------|--------|
| **Swift 套件管理器** |內建|蘋果官方，跨平台|
| **CocoaPods** |基於 Ruby 的 | iOS/macOS，龐大的生態系統 |
| **迦太基** |去中心化|二元框架 |
| **圖伊斯特** |專案產生| Xcode 專案管理 |
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

## Web 框架（伺服器端 Swift）
|框架|類型 |最適合 |
|------------|------|----------|
| **蒸氣** |全端|最受歡迎、可投入生產 |
| **蜂鳥** |輕量化|快速、現代、非同步優先 |
| **基圖拉** | IBM|IBM企業（已存檔）|
| **完美** |模組化|伺服器端 Swift |
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

## 資料庫和 ORM
|技術 |類型 |
|------------|------|
| **流利** | Vapor 的 ORM（PostgreSQL、MySQL、SQLite）|
| **GRDB** | SQLite 工具包 |
| **領域** |行動資料庫|
| **核心資料** |蘋果的物件圖框架|
| **SwiftData** |現代蘋果的堅持（iOS 17+）|
| **PostgresNIO** | PostgreSQL 驅動程式（非同步）|
---

## 測試
|框架|目的|
|------------|---------|
| **XC測試** |蘋果內建測試|
| **快** | BDD 式測驗 |
| **靈活** | Matcher 框架（與 Quick 配對）|
| **快速測試** |基於現代巨集（Swift 5.9+）|
| **快照測試** | UI/快照測試 |
| **OHHTTPStubs** | HTTP 存根 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **SwiftLint** | Linting、風格執行 |
| **SwiftFormat** |程式碼格式化 |
| **SwiftLint + 自訂規則** |專案特定規則 |
| **週邊** |未使用的代碼檢測 |
| **SonarQube** |程式碼品質平台|
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

## Apple 框架 (iOS/macOS)
|框架|目的|
|------------|---------|
| **SwiftUI** |聲明式 UI（所有 Apple 平台）|
| **UIKit** |傳統的 iOS UI |
| **應用程式包** | macOS 使用者介面 |
| **合併** |反應式程式設計 |
| **非同步/等待** |並發（Swift 並發）|
| **演員** |線程安全的可變狀態 |
| **CoreML** |機器學習 |
| **ARKit** |擴增實境|
| **健康套件** |健康數據|
| **雲端套件** | iCloud 整合 |
| **小工具套件** |小工具 |
| **商店套件 2** |應用程式內購買 |
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **阿拉莫菲爾** | HTTP 網路 |
| **翠鳥/核武** |圖片載入/快取 |
| **SnapKit** |自動佈局 DSL |
| **洛蒂** | After Effects 動畫 |
| **SwiftyJSON** | JSON解析|
| **可編碼** |內建序列化 |
| **鑰匙圈存取** |安全憑證儲存 |
| **SwiftLint** |程式碼檢查 |
| **RxSwift** |反應式擴充 |
| **可組合架構** |單向架構 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **Xcode** | Apple平台開發所需|
| **VS Code + Swift** |跨平台 Swift 開發 |
| **Neovim + sourcekit-lsp** |基於終端 |
| **應用程式代碼** | JetBrains（已停產，使用 Xcode）|
---

## 部署
|方法|筆記|
|--------|--------|
| **應用程式商店** | iOS/macOS 發行版 |
| **試飛** | Beta 測試 |
| **快車道** |自動化建置/部署 |
| **Xcode 雲** |蘋果的CI/CD |
| **GitHub 操作** |跨平台 CI |
| **碼頭工人** |伺服器端Swift部署|
| **鐵路蒸汽/Fly.io** |伺服器端託管 |
---

＃＃ 概括
Swift 的生態系統分為 Apple 平台開發和伺服器端 Swift。對於 Apple：**Xcode** 作為 IDE，**SwiftUI** 用於 UI，**Swift Concurrency**（非同步/等待、參與者）用於並行性，**SwiftData** 或 **Core Data** 用於持久性，以及 **XCTest** 或 **Swift Testing** 用於測試。對於伺服器端：**Vapor** 或 **Hummingbird** 作為框架，**SPM** 用於包，**Docker** 用於部署。 SwiftLint 強制執行程式碼品質。 Swift 的優點是安全性（可選、值類型）、效能（編譯、LLVM）和現代語法。該生態系統對於任何建立 iOS、macOS、watchOS 或 tvOS 應用程式的人來說都是至關重要的。