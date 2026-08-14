---
# Metadata
title: "Kotlin — Version History & Evolution"
description: "Comprehensive version history and evolution of Kotlin from 1.0 to modern Kotlin."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [kotlin, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# کوٹلن - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 2016 | پہلی مستحکم ریلیز (JetBrains) |
| 1.1 | 2017 | Coroutines، قسم عرفی نام، lambdas میں destructuring |
| 1.2 | 2017 | ارے اسپریڈ،`lateinit`ٹاپ لیول، ٹریلنگ کوما |
| 1.3 | 2018 | `inline class`,`contracts`(تجرباتی) |
| 1.4 | 2020 |  `@JvmDefault`، کوٹلن انٹرفیس کے لیے SAM کی تبدیلیاں |
| 1.5 | 2021 | `value class`,`OptIn`تشریح، regex لٹریلز |
| 1.6 | 2021 | `when`تھکن،`Unit`واپسی کی اصلاح |
| 1.7 | 2022 | `enum`اندراجات،`@JvmInline`ویلیو کلاسز |
| 1.8 | 2022 | `@SubclassOptInRequired`, K2 کمپائلر پیش نظارہ |
| 1.9 | 2023 | **K2 کمپائلر**, `@ConsistentCopyVisibility`,`data`اشیاء |
| 2.0 | 2024 | **K2 کمپائلر مستحکم**، `@SubclassOptInRequired`، سمارٹ کاسٹ میں بہتری |
| 2.1 | 2024 | `when`مضامین، پراپرٹی ڈیلیگیشن میں بہتری |
| 2.2 | 2025 | (متوقع) K2 میں مزید بہتری |
## اہم سنگ میل
### The Beginning (2011–2016)
- **2011**: جیٹ برینز نے کوٹلن کا اعلان کیا (سینٹ پیٹرزبرگ کے قریب جزیرہ کوٹلن کے نام سے منسوب)
- **2012**: کوٹلن اوپن سورس
- **2016**: **Kotlin 1.0** — JVM اور Android کے لیے پروڈکشن کے لیے تیار
### Android اپنانا (2017–2019)
- **2017**: گوگل نے گوگل I/O پر فرسٹ کلاس کوٹلن سپورٹ کا اعلان کیا۔
- **1.1 (2017)**: **کورٹائنز** — ہلکا پھلکا async پروگرامنگ
- **1.2 (2017)**: ملٹی پلیٹ فارم پروجیکٹس (Kotlin/Native, Kotlin/JS)
- **1.3 (2018)**: `inline class`، معاہدے
### ترقی کے سال (2020-2023)
- **1.5 (2021)**: `value class`،`OptIn`تشریح، غیر دستخط شدہ عددی اقسام
- **1.7 (2022)**:`enum`اندراجات، K2 مرتب کرنے والا پیش نظارہ
- **1.9 (2023)**: K2 کمپائلر (نیا فرنٹ اینڈ، 30% تیز تالیف)،`data`اشیاء
### ماڈرن کوٹلن (2024–موجودہ)
- **2.0 (2024)**: **K2 مرتب کرنے والا مستحکم** — کارکردگی میں اہم بہتری، بہتر تجزیہ
- **2.1 (2024)**: بڑھا ہوا `when`، پراپرٹی ڈیلی گیشن
## کورٹین ارتقاء
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## ملٹی پلیٹ فارم ارتقاء
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## زبان کی خصوصیت کا ارتقا
```
Null Safety:
  1.0:  Nullable types (String?), safe calls (?.), Elvis (?:)
  1.5:  OptIn annotation for experimental APIs
  2.0:  Smart cast improvements

Pattern Matching:
  1.0:  when expression, is/as operators
  1.7:  when exhaustiveness checking
  2.1:  Enhanced when subjects

Data Classes:
  1.0:  data class (equals, hashCode, toString, copy, componentN)
  1.9:  data object
  2.0:  @ConsistentCopyVisibility

Value Classes:
  1.3:  inline class (experimental)
  1.5:  value class (renamed)
  1.7:  @JvmInline value class
```

## مختلف پلیٹ فارمز پر کوٹلن
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## ماحولیاتی نظام کی نمو
```
2016: Kotlin 1.0 — JetBrains IDE plugin
2017: Google I/O — first-class Android support
2018: Android KTX, Spring Framework 5 Kotlin support
2019: Kotlin 1.3 — coroutines stable
2021: Kotlin 1.5 — multiplatform matures
2023: Kotlin 1.9 — K2 compiler
2024: Kotlin 2.0 — K2 stable, Compose Multiplatform
2025: Kotlin — top 15 most used language; dominant in Android
```

## ڈیزائن کے کلیدی اصول
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
