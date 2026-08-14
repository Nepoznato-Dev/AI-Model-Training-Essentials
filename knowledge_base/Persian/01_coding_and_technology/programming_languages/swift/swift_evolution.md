<!--
---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [swift, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Swift - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 2014 | انتشار اولیه (کریس لاتنر، اپل) |
| 1.1 | 2014 | اولیه سازهای ناموفق،`@autoclosure`|
| 1.2 | 2015 | `as?`/`as!`,`Set`نوع، مقایسه تاپل |
| 2.0 | 2015 | پسوند پروتکل، `defer`، `guard`،`errortype`|
| 2.1 | 2015 |  `try?`، درون یابی رشته ای در لفظ |
| 2.2 | 2016 | `#selector`,`defer`, تاپل بازده |
| 3.0 | 2016 | **عمده**: طراحی مجدد API — قراردادهای نامگذاری،`@discardableResult`|
| 4.0 | 2017 | `Codable`,`String`بازنویسی، چند خطی literals |
| 5.0 | 2019 | **رشته**: آماده سازی `async/await`، پایداری ABI، نوع`Result`|
| 5.1 | 2019 | `some`(انواع مات)، لفاف دار اموال،`@resultBuilder`|
| 5.2 | 2020 | فراخوانی به عنوان تابع،`KeyPath`به عنوان تابع |
| 5.3 | 2020 |  `@MainActor`، بسته شدن چندگانه دنباله دار، بهبود`enum`|
| 5.4 | 2021 | چندین پارامتر متغیر، بهبود`@resultBuilder`|
| 5.5 | 2021 | **`async/await`**, بازیگران,`Sendable`|
| 5.6 | 2022 |  کلمه کلیدی `any`,`Clock`,`Duration`|
| 5.7 | 2022 |  مختصر `if let`،`Regex`literals، پروتکل`Clock`|
| 5.8 | 2023 | استقرار عملکرد عقب، بهبود`Clock`|
| 5.9 | 2023 | **ماکروها**، بسته های پارامتر،`consume`/`discard`|
| 5.10 | 2024 | بررسی همزمانی کامل، ایمنی سختگیرانه مسابقه داده |
| 6.0 | 2024 | ** عمده **: همزمانی دقیق به طور پیش فرض، پرتاب های تایپ شده |
| 6.1 | 2025 | (مورد انتظار) اصلاحات همزمانی بیشتر |
## نقاط عطف اصلی
### Swift 1.x - تولد (2014–2015)
- **2014**: در WWDC اعلام شد. جایگزین Objective-C برای توسعه اپل
- **1.0**: اختیاری، ژنریک، بسته شدن، استنتاج نوع، پروتکل ها
- **1.2**: الگوی`as?`/ `as!`، نوع `Set`
### Swift 2.x - مدیریت خطا (2015–2016)
- **2.0**: پسوندهای پروتکل (برنامه نویسی پروتکل گرا)، `guard`، `defer`،`do/try/catch`
- **2.1**:`try?`برای مدیریت خطای اختیاری
### Swift 3.x - تغییر نام API عالی (2016)
- **3.0**: بازطراحی گسترده API - "تغییر نام بزرگ یکپارچه"
- قراردادهای نامگذاری:`stringByAppendingString`→`appending`
- حلقه های`for`به سبک C، عملگرهای`++`/`--`حذف شدند
- برچسب های پارامتر اول به طور پیش فرض
### سوئیفت 4.x — کدپذیر (2017)
- **4.0**: پروتکل`Codable`(رمزگذاری/رمزگشایی JSON)، بازنویسی `String`، رشته های چند خطی
### سوئیفت 5.x — پایداری (2019–2024)
- **5.0**: پایداری ABI (برنامه ها کوچکتر می شوند)، نوع `Result`، رشته های خام
- **5.1**: انواع مات (`some View`)، پوشش های دارایی (`@State`، `@Binding`)
- **5.5**: **`async/await`**، بازیگران، پروتکل `Sendable`
- **5.9**: ماکروها (تولید کد زمان کامپایل)، بسته های پارامتر
### سوئیفت 6.x — ایمنی همزمان (2024–اکنون)
- **6.0**: بررسی دقیق همزمانی به طور پیش فرض، پرتاب های تایپ شده
## تکامل همزمان
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## تایپ سیستم تکامل
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## سویفت در پلتفرم های دیگر
```
2015: Swift open-sourced (Apache 2.0)
2015: Swift on Linux (Ubuntu)
2016: Swift on ARM (Raspberry Pi)
2017: Swift on Windows (experimental)
2019: TensorFlow Swift (later discontinued)
2020: Swift on AWS Lambda
2021: Vapor (server-side Swift framework)
2023: Swift on embedded systems (embedded Swift)
2025: Swift — cross-platform systems language
```

## فرآیند تکامل سریع
```
SE-0001 (2015): First proposal
Over 400 proposals accepted by 2025
Key proposals:
  SE-0044: Import as member
  SE-0110: Distributed actors
  SE-0295: Codable improvements
  SE-0302: Sendable and @Sendable closures
  SE-0335: Introduce existential any
  SE-0346: Lightweight same-type requirements (some)
  SE-0401: Remove Actor Isolation Inference
  SE-0413: Typed throws
```

## رشد اکوسیستم
```
2014: Swift announced — replaces Objective-C
2015: Open source; Swift Package Manager
2016: Swift 3 — API redesign
2017: Swift 4 — Codable
2019: Swift 5 — ABI stability
2021: SwiftUI matures
2023: Swift 5.9 — macros
2025: Swift 6 — data race safety; used in iOS, macOS, server, embedded
```
