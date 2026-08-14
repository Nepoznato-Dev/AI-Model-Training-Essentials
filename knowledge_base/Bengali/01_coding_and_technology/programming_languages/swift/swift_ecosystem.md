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
# সুইফট — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি সুইফট ইকোসিস্টেমের প্রয়োজনীয় টুলস, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## টুলচেইন
| টুল | উদ্দেশ্য |
|------|---------|
| **দ্রুত** | কম্পাইলার এবং REPL |
| **swiftc** | সুইফট কম্পাইলার |
| **সুইফট প্যাকেজ ম্যানেজার (SPM)** | অন্তর্নির্মিত প্যাকেজ ম্যানেজার |
| **এক্সকোড** | Apple এর IDE (শুধুমাত্র macOS) |
| **xcodebuild** | CLI বিল্ড টুল |
| **xcrun** | ডেভেলপার টুল রানার |
| **যন্ত্র** | কর্মক্ষমতা প্রোফাইলিং |
| **সুইফটলিন্ট** | কোড লিন্টিং |
| **সুইফট ফরম্যাট** | কোড ফরম্যাটিং |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | প্রকার | নোট |
|------|------|-------|
| **সুইফট প্যাকেজ ম্যানেজার** | অন্তর্নির্মিত | অ্যাপলের অফিসিয়াল, ক্রস-প্ল্যাটফর্ম |
| **কোকোপড** | রুবি ভিত্তিক | iOS/macOS, বড় ইকোসিস্টেম |
| **কর্থেজ** | বিকেন্দ্রীকৃত | বাইনারি ফ্রেমওয়ার্ক |
| **টিউইস্ট** | প্রকল্প প্রজন্ম | Xcode প্রকল্প ব্যবস্থাপনা |
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

## ওয়েব ফ্রেমওয়ার্ক (সার্ভার-সাইড সুইফট)
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **বাষ্প** | ফুল-স্ট্যাক | সর্বাধিক জনপ্রিয়, উত্পাদন প্রস্তুত |
| **হামিংবার্ড** | লাইটওয়েট | দ্রুত, আধুনিক, অ্যাসিঙ্ক-প্রথম |
| **কিতুরা** | আইবিএম | এন্টারপ্রাইজ (সংরক্ষিত) |
| **পারফেক্ট** | মডুলার | সার্ভার-সাইড সুইফট |
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

## ডাটাবেস এবং ওআরএম
| প্রযুক্তি | প্রকার |
|------------|------|
| **সাবলীল** | বাষ্পের ORM (PostgreSQL, MySQL, SQLite) |
| **GRDB** | SQLite টুলকিট |
| **রাজত্ব** | মোবাইল ডাটাবেস |
| **কোর ডেটা** | অ্যাপলের অবজেক্ট গ্রাফ ফ্রেমওয়ার্ক |
| **সুইফটডেটা** | আধুনিক অ্যাপল অধ্যবসায় (iOS 17+) |
| **PostgresNIO** | PostgreSQL ড্রাইভার (async) |
---

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **XCTest** | অ্যাপলের বিল্ট-ইন টেস্টিং |
| **দ্রুত** | বিডিডি-স্টাইল পরীক্ষা |
| **নম্বল** | ম্যাচার ফ্রেমওয়ার্ক (দ্রুত সাথে জোড়া) |
| **সুইফট টেস্টিং** | আধুনিক ম্যাক্রো-ভিত্তিক (Swift 5.9+) |
| **স্ন্যাপশট টেস্টিং** | UI/স্ন্যাপশট পরীক্ষা |
| **OHHTTPSTubs** | HTTP স্টাবিং |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **সুইফটলিন্ট** | লিন্টিং, শৈলী প্রয়োগ |
| **সুইফট ফরম্যাট** | কোড ফরম্যাটিং |
| **SwiftLint + কাস্টম নিয়ম** | প্রকল্প-নির্দিষ্ট নিয়ম |
| **পরিধি** | অব্যবহৃত কোড সনাক্তকরণ |
| **সোনারকিউব** | কোড মানের প্ল্যাটফর্ম |
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

## অ্যাপল ফ্রেমওয়ার্কস (iOS/macOS)
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **SwiftUI** | ঘোষণামূলক UI (সমস্ত অ্যাপল প্ল্যাটফর্ম) |
| **UIKit** | ঐতিহ্যগত iOS UI |
| **অ্যাপকিট** | macOS UI |
| **একত্রিত করুন** | প্রতিক্রিয়াশীল প্রোগ্রামিং |
| **অসিঙ্ক/অপেক্ষা** | কনকারেন্সি (সুইফট কনকারেন্সি) |
| **অভিনেতা** | থ্রেড-নিরাপদ পরিবর্তনযোগ্য অবস্থা |
| **কোরএমএল** | মেশিন লার্নিং |
| **আরকিট** | বর্ধিত বাস্তবতা |
| **হেলথকিট** | স্বাস্থ্য তথ্য |
| **ক্লাউডকিট** | iCloud ইন্টিগ্রেশন |
| **উইজেটকিট** | উইজেট |
| **স্টোরকিট 2** | অ্যাপ-মধ্যস্থ কেনাকাটা |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **আলামোফায়ার** | HTTP নেটওয়ার্কিং |
| **কিংফিশার / নিউকে** | ইমেজ লোডিং/ক্যাশিং |
| **স্ন্যাপকিট** | অটো লেআউট DSL |
| **লটি** | প্রভাব অ্যানিমেশন পরে |
| **SwiftyJSON** | JSON পার্সিং |
| **কোডযোগ্য** | অন্তর্নির্মিত সিরিয়ালাইজেশন |
| **কীচেন অ্যাক্সেস** | নিরাপদ শংসাপত্র সঞ্চয়স্থান |
| **সুইফটলিন্ট** | কোড লিন্টিং |
| **RxSwift** | প্রতিক্রিয়াশীল এক্সটেনশন |
| **দ্য কম্পোজেবল আর্কিটেকচার** | একমুখী স্থাপত্য |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **এক্সকোড** | অ্যাপল প্ল্যাটফর্ম বিকাশের জন্য প্রয়োজনীয় |
| **ভিএস কোড + সুইফট** | ক্রস-প্ল্যাটফর্ম সুইফট উন্নয়ন |
| **নিওভিম + সোর্সকিট-এলএসপি** | টার্মিনাল ভিত্তিক |
| **অ্যাপকোড** | JetBrains (বন্ধ, এক্সকোড ব্যবহার করুন) |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **অ্যাপ স্টোর** | iOS/macOS বিতরণ |
| **টেস্টফ্লাইট** | বিটা টেস্টিং |
| **ফাস্টলেন** | স্বয়ংক্রিয় বিল্ড/ডিপ্লোয় |
| **এক্সকোড ক্লাউড** | অ্যাপলের CI/CD |
| **গিটহাব অ্যাকশন** | ক্রস-প্ল্যাটফর্ম CI |
| **ডকার** | সার্ভার-সাইড সুইফট স্থাপনা |
| ** Railway/Fly.io তে বাষ্প** | সার্ভার-সাইড হোস্টিং |
---

## সারাংশ
সুইফটের ইকোসিস্টেম অ্যাপল প্ল্যাটফর্ম ডেভেলপমেন্ট এবং সার্ভার-সাইড সুইফটের মধ্যে বিভক্ত। Apple এর জন্য: IDE হিসাবে **Xcode**, UI এর জন্য **SwiftUI**, সমান্তরালতার জন্য **Swift Concurrency** (async/await, actors), **SwiftData** বা **Core Data** এবং পরীক্ষার জন্য **XCTest** বা **Swift Testing**। সার্ভার-সাইডের জন্য: ফ্রেমওয়ার্ক হিসাবে **বাষ্প** বা **হামিংবার্ড**, প্যাকেজের জন্য **SPM** এবং স্থাপনার জন্য **ডকার**। সুইফটলিন্ট কোডের গুণমান প্রয়োগ করে। সুইফটের শক্তি হল নিরাপত্তা (ঐচ্ছিক, মান প্রকার), কর্মক্ষমতা (সংকলিত, এলএলভিএম), এবং আধুনিক সিনট্যাক্স। যে কেউ iOS, macOS, watchOS, বা tvOS অ্যাপ্লিকেশন তৈরি করে তাদের জন্য ইকোসিস্টেম অপরিহার্য।