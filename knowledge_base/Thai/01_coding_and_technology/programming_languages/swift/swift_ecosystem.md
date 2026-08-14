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
# Swift - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศของ Swift
---

## ห่วงโซ่เครื่องมือ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **รวดเร็ว** | คอมไพเลอร์และ REPL |
| **swiftc** | คอมไพเลอร์ Swift |
| **ตัวจัดการแพ็คเกจ Swift (SPM)** | ตัวจัดการแพ็คเกจในตัว |
| **Xcode** | IDE ของ Apple (macOS เท่านั้น) |
| **xcodebuild** | เครื่องมือสร้าง CLI |
| **xcrun** | นักวิ่งเครื่องมือสำหรับนักพัฒนา |
| **เครื่องดนตรี** | โปรไฟล์ประสิทธิภาพ |
| **SwiftLint** | รหัสขุย |
| **รูปแบบ Swift** | การจัดรูปแบบโค้ด |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | พิมพ์ | หมายเหตุ |
|-|-------|-------|
| **ตัวจัดการแพ็คเกจ Swift** | ในตัว | ข้ามแพลตฟอร์มอย่างเป็นทางการของ Apple |
| **โกโก้พอดส์** | ที่ใช้ทับทิม | iOS/macOS ระบบนิเวศขนาดใหญ่ |
| **คาร์เธจ** | กระจายอำนาจ | กรอบไบนารี |
| **ตุยส์** | การสร้างโครงการ | การจัดการโครงการ Xcode |
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

## กรอบงานเว็บ (Swift ฝั่งเซิร์ฟเวอร์)
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **ไอระเหย** | เต็มกอง | ยอดนิยม พร้อมผลิต |
| **ฮัมมิ่งเบิร์ด** | น้ำหนักเบา | รวดเร็ว ทันสมัย ​​ไม่พร้อมกัน |
| **กิทูรา** | ไอบีเอ็ม | องค์กร (เก็บถาวร) |
| **สมบูรณ์แบบ** | โมดูลาร์ | Swift ฝั่งเซิร์ฟเวอร์ |
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

## ฐานข้อมูลและ ORM
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **คล่อง** | ORM ของ Vapor (PostgreSQL, MySQL, SQLite) |
| **GRDB** | ชุดเครื่องมือ SQLite |
| **อาณาจักร** | ฐานข้อมูลมือถือ |
| **ข้อมูลหลัก** | กรอบกราฟวัตถุของ Apple |
| **สวิฟท์ดาต้า** | ความคงอยู่ของ Apple ยุคใหม่ (iOS 17+) |
| **PostgresNIO** | ไดรเวอร์ PostgreSQL (แบบอะซิงโครนัส) |
---

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **XCTest** | การทดสอบในตัวของ Apple |
| **ด่วน** | การทดสอบแบบ BDD |
| **ว่องไว** | Matcher framework (จับคู่กับ Quick) |
| **การทดสอบที่รวดเร็ว** | อิงมาโครสมัยใหม่ (Swift 5.9+) |
| **การทดสอบภาพรวม** | การทดสอบ UI/สแนปชอต |
| **OHHTTPStubs** | การขัดถู HTTP |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **SwiftLint** | Linting การบังคับใช้สไตล์ |
| **รูปแบบ Swift** | การจัดรูปแบบโค้ด |
| **SwiftLint + กฎที่กำหนดเอง** | กฎเฉพาะโครงการ |
| **รอบนอก** | การตรวจจับรหัสที่ไม่ได้ใช้ |
| **โซนาร์คิวบ์** | แพลตฟอร์มคุณภาพรหัส |
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

## กรอบงาน Apple (iOS/macOS)
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **SwiftUI** | UI ที่เปิดเผย (แพลตฟอร์ม Apple ทั้งหมด) |
| **UIKit** | iOS UI แบบดั้งเดิม |
| **AppKit** | macOS UI |
| **รวมกัน** | การเขียนโปรแกรมเชิงโต้ตอบ |
| **async/รอ** | เห็นพ้องต้องกัน (Swift Concurrency) |
| **นักแสดง** | สถานะไม่แน่นอนของเธรดที่ปลอดภัย |
| **CoreML** | การเรียนรู้ของเครื่อง |
| **อาร์คิท** | เติมความเป็นจริง |
| **เฮลท์คิท** | ข้อมูลสุขภาพ |
| **คลาวด์คิท** | การรวม iCloud |
| **WidgetKit** | วิดเจ็ต |
| **StoreKit 2** | การซื้อในแอป |
---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **อลาโมไฟร์** | เครือข่าย HTTP |
| **นกกระเต็น / นุก** | กำลังโหลดรูปภาพ/แคช |
| **SnapKit** | เค้าโครงอัตโนมัติ DSL |
| **ลอตตี้** | ภาพเคลื่อนไหว After Effects |
| **SwiftyJSON** | การแยกวิเคราะห์ JSON |
| **เขียนโค้ดได้** | การทำให้เป็นอนุกรมในตัว |
| **การเข้าถึงพวงกุญแจ** | การจัดเก็บข้อมูลรับรองที่ปลอดภัย |
| **SwiftLint** | รหัสขุย |
| **RxSwift** | ส่วนขยายที่เกิดปฏิกิริยา |
| **สถาปัตยกรรมแบบประกอบได้** | สถาปัตยกรรมทิศทางเดียว |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **Xcode** | จำเป็นสำหรับการพัฒนาแพลตฟอร์ม Apple |
| **รหัส VS + Swift** | การพัฒนา Swift ข้ามแพลตฟอร์ม |
| **Neovim + sourcekit-lsp** | บนเทอร์มินัล |
| **รหัสแอป** | JetBrains (ยกเลิกใช้ Xcode) |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **แอปสโตร์** | การกระจาย iOS/macOS |
| **ทดสอบเที่ยวบิน** | การทดสอบเบต้า |
| **ฟาสต์เลน** | สร้าง/ปรับใช้อัตโนมัติ |
| **Xcode คลาวด์** | CI/CD ของ Apple |
| **การดำเนินการ GitHub** | CI ข้ามแพลตฟอร์ม |
| **นักเทียบท่า** | การปรับใช้ Swift ฝั่งเซิร์ฟเวอร์ |
| **ไอระเหยบนรถไฟ/Fly.io** | โฮสติ้งฝั่งเซิร์ฟเวอร์ |
---

## สรุป
ระบบนิเวศของ Swift ถูกแบ่งระหว่างการพัฒนาแพลตฟอร์ม Apple และ Swift ฝั่งเซิร์ฟเวอร์ สำหรับ Apple: **Xcode** เป็น IDE, **SwiftUI** สำหรับ UI, **Swift Concurrency** (async/await,actors) สำหรับการทำงานแบบขนาน, **SwiftData** หรือ **Core Data** สำหรับความคงอยู่ และ **XCTest** หรือ **Swift Testing** สำหรับการทดสอบ สำหรับฝั่งเซิร์ฟเวอร์: **Vapor** หรือ **Hummingbird** เป็นเฟรมเวิร์ก **SPM** สำหรับแพ็คเกจ และ **Docker** สำหรับการปรับใช้ SwiftLint บังคับใช้คุณภาพของโค้ด จุดแข็งของ Swift คือความปลอดภัย (ตัวเลือก, ประเภทค่า), ประสิทธิภาพ (คอมไพล์, LLVM) และไวยากรณ์สมัยใหม่ ระบบนิเวศเป็นสิ่งจำเป็นสำหรับทุกคนที่สร้างแอปพลิเคชัน iOS, macOS, watchOS หรือ tvOS