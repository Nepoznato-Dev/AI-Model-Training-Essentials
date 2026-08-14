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
# سوئیفت - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم سوئیفت را پوشش می‌دهد.
---

## زنجیره ابزار
| ابزار | هدف |
|------|---------|
| **سریع** | کامپایلر و REPL |
| **swiftc** | کامپایلر سوئیفت |
| **مدیر بسته سوئیفت (SPM)** | مدیریت بسته داخلی |
| **Xcode** | IDE اپل (فقط macOS) |
| **xcodebuild** | ابزار ساخت CLI |
| **xcrun** | برنامه نویس ابزار runner |
| **ابزار** | پروفایل عملکرد |
| **SwiftLint** | کد لینتینگ |
| **SwiftFormat** | قالب بندی کد |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## مدیریت بسته
| ابزار | نوع | یادداشت ها |
|------|------|-------|
| **مدیر بسته سوئیفت** | داخلی | پلتفرم رسمی اپل |
| **CocoaPods** | بر پایه یاقوت | iOS/macOS، اکوسیستم بزرگ |
| **کارتاژ** | غیر متمرکز | چارچوب های باینری |
| **تویست** | تولید پروژه | مدیریت پروژه Xcode |
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

## چارچوب های وب (سوئیفت سمت سرور)
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **بخار** | تمام پشته | محبوب ترین، آماده تولید |
| **مرغ مگس خوار** | سبک | سریع، مدرن، async-first |
| **کیتورا** | آی بی ام | سازمانی (بایگانی شده) |
| **کامل** | مدولار | سوییفت سمت سرور |
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

## پایگاه داده و ORM
| فناوری | نوع |
|------------|------|
| **مسلط** | ORM Vapor (PostgreSQL، MySQL، SQLite) |
| **GRDB** | جعبه ابزار SQLite |
| **قلمرو** | پایگاه داده موبایل |
| **داده های اصلی** | چارچوب گراف شی اپل |
| **SwiftData** | پایداری مدرن اپل (iOS 17+) |
| **PostgresNIO** | درایور PostgreSQL (async) |
---

## تست
| چارچوب | هدف |
|-----------|---------|
| **XCTest** | تست داخلی اپل |
| **سریع** | تست سبک BDD |
| **زیبا** | چارچوب تطبیق (جفت با Quick) |
| **تست سریع** | مبتنی بر ماکرو مدرن (Swift 5.9+) |
| **تست عکس فوری** | تست UI/Snapshot |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **SwiftLint** | لینتینگ، اجرای سبک |
| **SwiftFormat** | قالب بندی کد |
| **SwiftLint + قوانین سفارشی** | قوانین خاص پروژه |
| **حاشیه** | تشخیص کد استفاده نشده |
| **SonarQube** | پلت فرم کیفیت کد |
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

## Apple Frameworks (iOS/macOS)
| چارچوب | هدف |
|-----------|---------|
| **SwiftUI** | رابط کاربری اعلامی (همه پلتفرم های اپل) |
| **UIKit** | رابط کاربری سنتی iOS |
| **AppKit** | رابط کاربری macOS |
| **ترکیب** | برنامه نویسی واکنشی |
| **ناهمگام/انتظار** | Concurrency (Swift Concurrency) |
| **بازیگران** | حالت قابل تغییر در حالت ایمن |
| **CoreML** | یادگیری ماشینی |
| **ARKit** | واقعیت افزوده |
| **HealthKit** | داده های سلامت |
| **CloudKit** | ادغام iCloud |
| **ویجت کیت** | ابزارک ها |
| **StoreKit 2** | خریدهای درون برنامه ای |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **آلاموفایر** | شبکه HTTP |
| **Kingfisher / Nuke** | بارگذاری / ذخیره سازی تصویر |
| **SnapKit** | طرح بندی خودکار DSL |
| **لاتی** | انیمیشن های افتر افکت |
| **SwiftyJSON** | تجزیه JSON |
| **قابل کدگذاری** | سریال سازی داخلی |
| **KeychainAccess** | ذخیره سازی اطلاعات کاربری امن |
| **SwiftLint** | کد لینتینگ |
| **RxSwift** | پسوندهای واکنشی |
| **معماری ترکیب پذیر** | معماری یک طرفه |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **Xcode** | مورد نیاز برای توسعه پلتفرم اپل |
| **VS Code + Swift** | توسعه سوئیفت بین پلتفرمی |
| **Neovim + sourcekit-lsp** | مبتنی بر ترمینال |
| **AppCode** | JetBrains (قطع شده، از Xcode استفاده کنید) |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **اپ استور** | توزیع iOS/macOS |
| **TestFlight** | تست بتا |
| **Fastlane** | ساخت/استقرار خودکار |
| **Xcode Cloud** | CI/CD اپل |
| **اقدامات گیت هاب** | کراس پلتفرم CI |
| **داکر** | استقرار سوئیفت سمت سرور |
| **بخار در راه آهن/Fly.io** | هاست سمت سرور |
---

## خلاصه
اکوسیستم سوئیفت بین توسعه پلتفرم اپل و سویفت سمت سرور تقسیم شده است. برای اپل: **Xcode** به عنوان IDE، **SwiftUI** برای UI، **Swift Concurrency** (ناهمگام/انتظار، بازیگران) برای موازی سازی، **SwiftData** یا **Core Data** برای پایداری، و **XCTest** یا **تست سریع** برای تست ها. برای سمت سرور: **Vapor** یا **Hummingbird** به عنوان چارچوب، **SPM** برای بسته ها و **Docker** برای استقرار. SwiftLint کیفیت کد را اعمال می کند. نقاط قوت سوئیفت ایمنی (اختیاری، انواع ارزش)، عملکرد (کامپایل شده، LLVM) و نحو مدرن است. این اکوسیستم برای هر کسی که برنامه‌های iOS، macOS، watchOS یا tvOS می‌سازد ضروری است.