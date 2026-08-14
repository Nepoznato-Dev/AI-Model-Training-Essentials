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
# سوئفٹ - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ سوئفٹ ایکو سسٹم میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## ٹول چین
| ٹول | مقصد |
|------|---------|
| **تیز** | کمپائلر اور REPL |
| **swiftc** | سوئفٹ کمپائلر |
| **سوئفٹ پیکیج مینیجر (SPM)** | بلٹ ان پیکیج مینیجر |
| **Xcode** | Apple کا IDE (صرف macOS) |
| **xcodebuild** | CLI تعمیر کا آلہ |
| **xcrun** | ڈویلپر ٹول رنر |
| **آلات** | کارکردگی کی پروفائلنگ |
| **SwiftLint** | کوڈ linting |
| **سوئفٹ فارمیٹ** | کوڈ فارمیٹنگ |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## پیکیج مینجمنٹ
| ٹول | قسم | نوٹس |
|------|------|------|
| **سوئفٹ پیکیج مینیجر** | بلٹ ان | ایپل کا آفیشل، کراس پلیٹ فارم |
| **کوکو پوڈس** | روبی پر مبنی | iOS/macOS، بڑا ماحولیاتی نظام |
| **کارتھیج** | وکندریقرت | بائنری فریم ورک |
| **ٹیوسٹ** | پروجیکٹ جنریشن | ایکس کوڈ پروجیکٹ مینجمنٹ |
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

## ویب فریم ورکس (سرور سائیڈ سوئفٹ)
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **بخار** | مکمل اسٹیک | سب سے زیادہ مقبول، پیداوار کے لیے تیار |
| **ہمنگ برڈ** | ہلکا پھلکا | تیز، جدید، async-first |
| **کتورا** | IBM | انٹرپرائز (محفوظ شدہ) |
| ** کامل** | ماڈیولر | سرور سائیڈ سوئفٹ |
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

## ڈیٹا بیس اور ORM
| ٹیکنالوجی | قسم |
|------------|------|
| **روانی** | Vapor's ORM (PostgreSQL, MySQL, SQLite) |
| **GRDB** | SQLite ٹول کٹ |
| **علاقہ** | موبائل ڈیٹا بیس |
| **بنیادی ڈیٹا** | ایپل کا آبجیکٹ گراف فریم ورک |
| **SwiftData** | جدید ایپل استقامت (iOS 17+) |
| **پوسٹگریس این آئی او** | PostgreSQL ڈرائیور (async) |
---

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **XCTest** | ایپل کی بلٹ میں ٹیسٹنگ |
| **فوری** | BDD طرز کی جانچ |
| ** فرتیلا** | میچر فریم ورک (کوئیک کے ساتھ جوڑے) |
| **سوئفٹ ٹیسٹنگ** | جدید میکرو بیسڈ (Swift 5.9+) |
| **اسنیپ شاٹ ٹیسٹنگ** | UI/اسنیپ شاٹ ٹیسٹنگ |
| **OHHTTPStubs** | HTTP stubbing |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **SwiftLint** | linting، طرز نفاذ |
| **سوئفٹ فارمیٹ** | کوڈ فارمیٹنگ |
| **SwiftLint + حسب ضرورت قواعد** | پروجیکٹ کے مخصوص اصول |
| **پریفیری** | غیر استعمال شدہ کوڈ کا پتہ لگانا |
| **سونار کیوب** | کوڈ کوالٹی پلیٹ فارم |
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

## ایپل فریم ورکس (iOS/macOS)
| فریم ورک | مقصد |
|------------|---------|
| **SwiftUI** | اعلانیہ UI (تمام ایپل پلیٹ فارمز) |
| **UIKit** | روایتی iOS UI |
| **AppKit** | macOS UI |
| **کبائن** | رد عمل پروگرامنگ |
| **async/await** | Concurrency (Swift Concurrency) |
| **اداکار** | تھریڈ سیف تغیر پذیر حالت |
| **کور ایم ایل** | مشین لرننگ |
| **آرکیٹ** | بڑھا ہوا حقیقت |
| **ہیلتھ کٹ** | صحت کے اعداد و شمار |
| **کلاؤڈ کٹ** | iCloud انضمام |
| **ویجیٹ کٹ** | وجیٹس |
| **StoreKit 2** | درون ایپ خریداریاں |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **الااموفائر** | HTTP نیٹ ورکنگ |
| **کنگ فشر / نیوکی** | تصویر کی لوڈنگ/کیشنگ |
| **اسنیپ کٹ** | آٹو لے آؤٹ DSL |
| **لوٹی** | اثرات کے بعد متحرک تصاویر |
| **SwiftyJSON** | JSON پارسنگ |
| **کوڈ ایبل** | بلٹ ان سیریلائزیشن |
| **کیچین تک رسائی** | محفوظ اسناد کا ذخیرہ |
| **SwiftLint** | کوڈ linting |
| **RxSwift** | ری ایکٹیو ایکسٹینشنز |
| **دی کمپوز ایبل آرکیٹیکچر** | یک سمتی فن تعمیر |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **Xcode** | ایپل پلیٹ فارم کی ترقی کے لیے درکار ہے |
| **VS کوڈ + سوئفٹ** | کراس پلیٹ فارم سوئفٹ ڈویلپمنٹ |
| **نیوم + سورس کٹ-ایل ایس پی** | ٹرمینل پر مبنی |
| **ایپ کوڈ** | JetBrains (منقطع، Xcode استعمال کریں) |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **ایپ اسٹور** | iOS/macOS کی تقسیم |
| **ٹیسٹ فلائٹ** | بیٹا ٹیسٹنگ |
| **فاسٹلین** | خودکار تعمیر/تعینات |
| **Xcode کلاؤڈ** | ایپل کا CI/CD |
| **گٹ ہب ایکشنز** | کراس پلیٹ فارم CI |
| **ڈوکر** | سرور سائیڈ سوئفٹ تعیناتی |
| **ریلوے/Fly.io پر بخارات** | سرور سائیڈ ہوسٹنگ |
---

## خلاصہ
سوئفٹ کا ماحولیاتی نظام ایپل پلیٹ فارم ڈویلپمنٹ اور سرور سائیڈ سوئفٹ کے درمیان تقسیم ہے۔ Apple کے لیے: **Xcode** IDE کے بطور، UI کے لیے **SwiftUI**، متوازی کے لیے **Swift Concurrency** (async/await، ایکٹرز)، **SwiftData** یا **Core Data** ثابت قدمی کے لیے، اور **XCTest** یا **Swift Testing** ٹیسٹوں کے لیے۔ سرور سائیڈ کے لیے: **Vapor** یا **Hummingbird** بطور فریم ورک، **SPM** پیکجز کے لیے، اور **Docker** تعیناتی کے لیے۔ SwiftLint کوڈ کے معیار کو نافذ کرتا ہے۔ سوئفٹ کی طاقتیں حفاظت (اختیاری، قدر کی اقسام)، کارکردگی (مرتب کردہ، LLVM)، اور جدید نحو ہیں۔ ماحولیاتی نظام iOS، macOS، watchOS، یا tvOS ایپلیکیشنز بنانے والے ہر فرد کے لیے ضروری ہے۔