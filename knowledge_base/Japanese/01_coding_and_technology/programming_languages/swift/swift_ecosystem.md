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
# Swift — エコシステムとツールのガイド
このガイドでは、Swift エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## ツールチェーン
|ツール |目的 |
|-----|----------|
| **swift** |コンパイラと REPL |
| **迅速** | Swift コンパイラ |
| **Swift パッケージ マネージャー (SPM)** |組み込みのパッケージマネージャー |
| **Xcode** | Apple の IDE (macOS のみ) |
| **xcodebuild** | CLI ビルド ツール |
| **xcrun** | Developer tool runner |
| **楽器** |パフォーマンスプロファイリング |
| **SwiftLint** |コードリンティング |
| **SwiftFormat** |コードのフォーマット |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## パッケージ管理
|ツール |タイプ |メモ |
|------|------|------|
| **Swift Package Manager** |内蔵 | Apple's official, cross-platform |
| **ココアポッド** | Ruby ベース | iOS/macOS, large ecosystem |
| **カルタゴ** |分散型 |バイナリフレームワーク |
| **チューイスト** |プロジェクトの生成 | Xcode project management |
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

## Web フレームワーク (サーバーサイド Swift)
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **Vapor** |フルスタック |最も人気があり、本番環境に対応 |
| **Hummingbird** |軽量 |高速、最新、非同期優先 |
| **Kitura** | IBM | Enterprise (archived) |
| **Perfect** | Modular | Server-side Swift |
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

## データベースと ORM
|テクノロジー |タイプ |
|-----------|------|
| **流暢** | Vapor's ORM (PostgreSQL, MySQL, SQLite) |
| **GRDB** | SQLite ツールキット |
| **レルム** |モバイルデータベース |
| **コアデータ** | Apple's object graph framework |
| **SwiftData** | Modern Apple persistence (iOS 17+) |
| **PostgresNIO** | PostgreSQL driver (async) |
---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **XCTest** | Apple の組み込みテスト |
| **クイック** | BDD スタイルのテスト |
| **軽快** | Matcher フレームワーク (Quick とペア) |
| **迅速なテスト** |最新のマクロベース (Swift 5.9+) |
| **スナップショットテスト** | UI/スナップショットのテスト |
| **OHHTTPStubs** | HTTP スタブ |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **SwiftLint** |リンティング、スタイル強制 |
| **SwiftFormat** |コードのフォーマット |
| **SwiftLint + カスタム ルール** |プロジェクト固有のルール |
| **周辺** |未使用コードの検出 |
| **ソナークベ** |コード品質プラットフォーム |
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

## Apple フレームワーク (iOS/macOS)
|フレームワーク |目的 |
|----------|----------|
| **SwiftUI** |宣言型 UI (すべての Apple プラットフォーム) |
| **UIKit** |従来の iOS UI |
| **AppKit** | macOS UI |
| **結合** |リアクティブプログラミング |
| **非同期/待機** |同時実行 (Swift 同時実行) |
| **俳優** |スレッドセーフな可変状態 |
| **コアML** |機械学習 |
| **ARKit** |拡張現実 |
| **ヘルスキット** |健康データ |
| **クラウドキット** | iCloud 統合 |
| **ウィジェットキット** |ウィジェット |
| **ストアキット 2** |アプリ内購入 |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **アラモファイア** | HTTP ネットワーキング |
| **カワセミ / 核** |画像のロード/キャッシュ |
| **スナップキット** |自動レイアウト DSL |
| **ロッティ** | After Effects アニメーション |
| **SwiftyJSON** | JSON 解析 |
| **コーディング可能** |組み込みのシリアル化 |
| **キーチェーンアクセス** |安全な認証情報の保管 |
| **SwiftLint** |コードリンティング |
| **RxSwift** |リアクティブ拡張機能 |
| **コンポーザブル アーキテクチャ** |単方向アーキテクチャ |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **Xcode** | Apple プラットフォーム開発に必要 |
| **VS コード + Swift** |クロスプラットフォームの Swift 開発 |
| **Neovim +sourcekit-lsp** |ターミナルベース |
| **アプリコード** | JetBrains (製造中止、Xcode を使用) |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **App ストア** | iOS/macOS ディストリビューション |
| **テストフライト** |ベータテスト |
| **ファストレーン** |自動化されたビルド/デプロイ |
| **Xcode クラウド** | Apple の CI/CD |
| **GitHub アクション** |クロスプラットフォーム CI |
| **ドッカー** |サーバー側の Swift 導入 |
| **鉄道/Fly.io の蒸気** |サーバー側ホスティング |
---

＃＃ まとめ
Swift のエコシステムは、Apple プラットフォーム開発とサーバーサイド Swift に分かれています。 Apple の場合: IDE として **Xcode**、UI として **SwiftUI**、並列処理として **Swift Concurrency** (async/await、アクター)、永続性として **SwiftData** または **Core Data**、テストとして **XCTest** または **Swift Testing**。サーバー側: フレームワークとして **Vapor** または **Hummingbird**、パッケージに **SPM**、デプロイメントに **Docker**。 SwiftLint はコードの品質を強化します。 Swift の強みは、安全性 (オプション、値の型)、パフォーマンス (コンパイル済み、LLVM)、および最新の構文です。エコシステムは、iOS、macOS、watchOS、または tvOS アプリケーションを構築する人にとって不可欠です。