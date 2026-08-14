<!--
---
# Metadata
title: "Kotlin — Version History & Evolution"
description: "Comprehensive version history and evolution of Kotlin from 1.0 to modern Kotlin."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Kotlin - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 2016 | اولین نسخه پایدار (JetBrains) |
| 1.1 | 2017 | کوروتین، نام مستعار نوع، تخریب در لامبدا |
| 1.2 | 2017 | گسترش آرایه،`lateinit`سطح بالا، کاماهای انتهایی |
| 1.3 | 2018 | `inline class`,`contracts`(تجربی) |
| 1.4 | 2020 |  `@JvmDefault`، تبدیل SAM برای رابط های Kotlin |
| 1.5 | 2021 |  `value class`، حاشیه نویسی `OptIn`، regex literals |
| 1.6 | 2021 |  جامعیت `when`، بهینه سازی بازگشت`Unit`|
| 1.7 | 2022 |  ورودی های `enum`، کلاس های ارزش`@JvmInline`|
| 1.8 | 2022 |  پیش نمایش کامپایلر `@SubclassOptInRequired`، K2 |
| 1.9 | 2023 | **کامپایلر K2**، اشیاء `@ConsistentCopyVisibility`،`data`|
| 2.0 | 2024 | **پایدار کامپایلر K2**، `@SubclassOptInRequired`، بهبودهای بازیگران هوشمند |
| 2.1 | 2024 |  موضوعات `when`، بهبود واگذاری اموال |
| 2.2 | 2025 | (مورد انتظار) بهبودهای بیشتر K2 |
## نقاط عطف اصلی
### آغاز (2011–2016)
- **2011**: JetBrains Kotlin (نام جزیره Kotlin در نزدیکی سنت پترزبورگ) را اعلام کرد.
- **2012**: Kotlin منبع باز
- **2016**: **Kotlin 1.0** — آماده تولید برای JVM و Android
### Android Adoption (2017–2019)
- **2017**: گوگل پشتیبانی درجه یک Kotlin را در Google I/O اعلام کرد
- **1.1 (2017)**: **Coroutines** — برنامه نویسی ناهمگام سبک وزن
- **1.2 (2017)**: پروژه های چند پلتفرمی (Kotlin/Native، Kotlin/JS)
- **1.3 (2018)**: `inline class`، قراردادها
### سالهای رشد (2020–2023)
- **1.5 (2021)**: `value class`، حاشیه نویسی `OptIn`، انواع عدد صحیح بدون علامت
- **1.7 (2022)**: ورودی های `enum`، پیش نمایش کامپایلر K2
- **1.9 (2023)**: کامپایلر K2 (طراحی جدید، کامپایل 30٪ سریعتر)، اشیاء `data`
### کاتلین مدرن (2024–اکنون)
- **2.0 (2024)**: **کامپایلر K2 پایدار** - بهبود عملکرد عمده، تجزیه و تحلیل بهتر
- **2.1 (2024)**:`when`پیشرفته، تفویض مالکیت
## سیر تکاملی
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## تکامل چند پلتفرمی
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## تکامل ویژگی زبان
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

## کاتلین در پلتفرم های مختلف
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## رشد اکوسیستم
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

## اصول کلیدی طراحی
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
