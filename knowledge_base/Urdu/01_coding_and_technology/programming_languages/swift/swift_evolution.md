---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# سوئفٹ - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 2014 | ابتدائی ریلیز (کرس لیٹنر، ایپل) |
| 1.1 | 2014 | ناکام شروع کرنے والے،`@autoclosure`|
| 1.2 | 2015 | `as?`/`as!`,`Set`قسم، ٹپل موازنہ |
| 2.0 | 2015 | پروٹوکول ایکسٹینشنز،`defer`,`guard`,`errortype`|
| 2.1 | 2015 |  `try?`، لٹریلز میں سٹرنگ انٹرپولیشن |
| 2.2 | 2016 | `#selector`,`defer`, tuple ریٹرن |
| 3.0 | 2016 | **میجر**: API کو دوبارہ ڈیزائن کرنا — نام دینے کے کنونشنز،`@discardableResult`|
| 4.0 | 2017 | `Codable`,`String`دوبارہ لکھنا، ملٹی لائن لٹریلز |
| 5.0 | 2019 | **میجر**:`async/await`پریپ، ABI استحکام،`Result`قسم |
| 5.1 | 2019 | `some`(مبہم اقسام)، پراپرٹی ریپر،`@resultBuilder`|
| 5.2 | 2020 | فنکشن کے طور پر کال کریں،`KeyPath`بطور فنکشن |
| 5.3 | 2020 | `@MainActor`, ایک سے زیادہ پچھلی بندشیں،`enum`بہتری |
| 5.4 | 2021 | متعدد متغیر پیرامیٹرز،`@resultBuilder`بہتری |
| 5.5 | 2021 | **`async/await`**، اداکار،`Sendable`|
| 5.6 | 2022 | `any`کلیدی لفظ,`Clock`,`Duration`|
| 5.7 | 2022 | `if let`شارٹ ہینڈ،`Regex`لٹریلز،`Clock`پروٹوکول |
| 5.8 | 2023 | فنکشن بیک تعیناتی،`Clock`بہتری |
| 5.9 | 2023 | **میکروز**، پیرامیٹر پیک،`consume`/`discard`|
| 5.10 | 2024 | مکمل ہم آہنگی کی جانچ، سخت ڈیٹا ریس سیفٹی |
| 6.0 | 2024 | **میجر**: پہلے سے طے شدہ طور پر سخت موافقت، ٹائپ شدہ تھرو |
| 6.1 | 2025 | (متوقع) مزید ہم آہنگی کی اصلاح |
## اہم سنگ میل
### Swift 1.x — پیدائش (2014–2015)
- **2014**: WWDC میں اعلان کیا گیا؛ ایپل کی ترقی کے لیے Objective-C کی جگہ لے لیتا ہے۔
- **1.0**: اختیاری، عام، بندش، قسم کا اندازہ، پروٹوکول
- **1.2**:`as?`/`as!`پیٹرن،`Set`قسم
### Swift 2.x — ایرر ہینڈلنگ (2015–2016)
- **2.0**: پروٹوکول ایکسٹینشنز (پروٹوکول پر مبنی پروگرامنگ)، `guard`، `defer`،`do/try/catch`
- **2.1**: اختیاری غلطی سے نمٹنے کے لیے `try?`
### Swift 3.x — عظیم API کا نام تبدیل کرنا (2016)
- **3.0**: بڑے پیمانے پر API کو دوبارہ ڈیزائن کرنا - "گرینڈ یونیفائیڈ نام تبدیل کرنا"
- نام دینے کے معاہدے:`stringByAppendingString`→`appending`
- ہٹائے گئے C طرز کے`for`لوپس،`++`/`--`آپریٹرز
- پہلے پیرامیٹر لیبل بطور ڈیفالٹ
### Swift 4.x — کوڈ ایبل (2017)
- **4.0**:`Codable`پروٹوکول (JSON انکوڈنگ/ڈیکوڈنگ)،`String`دوبارہ لکھنا، ملٹی لائن سٹرنگ لٹریلز
### Swift 5.x — استحکام (2019–2024)
- **5.0**: ABI استحکام (ایپس چھوٹی ہو جاتی ہیں)،`Result`قسم، خام تاریں
- **5.1**: مبہم اقسام (`some View`)، پراپرٹی ریپرز (`@State`، `@Binding`)
- **5.5**: **`async/await`**، اداکار،`Sendable`پروٹوکول
- **5.9**: میکروس (کمپائل ٹائم کوڈ جنریشن)، پیرامیٹر پیک
### Swift 6.x — کنکرنسی سیفٹی (2024–موجودہ)
- **6.0**: ڈیفالٹ کے لحاظ سے سخت ہم آہنگی کی جانچ، ٹائپ شدہ تھرو
## ہم آہنگی ارتقاء
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## ٹائپ سسٹم ارتقاء
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## دوسرے پلیٹ فارمز پر سوئفٹ
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

## تیز ارتقاء کا عمل
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

## ماحولیاتی نظام کی نمو
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
