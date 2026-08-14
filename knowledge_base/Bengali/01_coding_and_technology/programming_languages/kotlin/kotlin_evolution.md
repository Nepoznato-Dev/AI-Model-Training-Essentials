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
# কোটলিন — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 1.0 | 2016 | প্রথম স্থিতিশীল প্রকাশ (JetBrains) |
| 1.1 | 2017 | কোরোটিন, টাইপ উপনাম, ল্যাম্বডাসে ধ্বংস |
| 1.2 | 2017 | অ্যারে স্প্রেড,`lateinit`টপ-লেভেল, ট্রেলিং কমা |
| 1.3 | 2018 | `inline class`,`contracts`(পরীক্ষামূলক) |
| 1.4 | 2020 | `@JvmDefault`, Kotlin ইন্টারফেসের জন্য SAM রূপান্তর |
| 1.5 | 2021 | `value class`,`OptIn`টীকা, রেজেক্স আক্ষরিক |
| 1.6 | 2021 | `when`ক্লান্তি,`Unit`রিটার্ন অপ্টিমাইজেশান |
| 1.7 | 2022 | `enum`এন্ট্রি,`@JvmInline`মান ক্লাস |
| 1.8 | 2022 | `@SubclassOptInRequired`, K2 কম্পাইলার প্রিভিউ |
| 1.9 | 2023 | **K2 কম্পাইলার**,`@ConsistentCopyVisibility`,`data`অবজেক্ট |
| 2.0 | 2024 | **K2 কম্পাইলার স্থিতিশীল**,`@SubclassOptInRequired`, স্মার্ট কাস্ট উন্নতি |
| 2.1 | 2024 | `when`বিষয়, সম্পত্তি অর্পণ উন্নতি |
| 2.2 | 2025 | (প্রত্যাশিত) আরও K2 উন্নতি |
## প্রধান মাইলফলক
### দ্য বিগিনিং (2011-2016)
- **2011**: জেটব্রেইন্স কোটলিন ঘোষণা করেছে (সেন্ট পিটার্সবার্গের কাছে কোটলিন দ্বীপের নামে নামকরণ করা হয়েছে)
- **2012**: কোটলিন ওপেন সোর্সড
- **2016**: **কোটলিন 1.0** — JVM এবং Android এর জন্য উৎপাদন-প্রস্তুত
### Android গ্রহণ (2017-2019)
- **2017**: Google Google I/O-এ প্রথম-শ্রেণীর কোটলিন সমর্থন ঘোষণা করেছে৷
- **1.1 (2017): **করোটিনস** — লাইটওয়েট অ্যাসিঙ্ক প্রোগ্রামিং
- **1.2 (2017): মাল্টিপ্ল্যাটফর্ম প্রকল্প (কোটলিন/নেটিভ, কোটলিন/জেএস)
- **1.3 (2018):`inline class`, চুক্তি
### বৃদ্ধির বছর (2020-2023)
- **1.5 (2021):`value class`,`OptIn`টীকা, স্বাক্ষরবিহীন পূর্ণসংখ্যার ধরন
- **1.7 (2022):`enum`এন্ট্রি, K2 কম্পাইলার প্রিভিউ
- **1.9 (2023): K2 কম্পাইলার (নতুন ফ্রন্টএন্ড, 30% দ্রুত কম্পাইলেশন),`data`অবজেক্ট
### আধুনিক কোটলিন (2024-বর্তমান)
- **2.0 (2024): **K2 কম্পাইলার স্থিতিশীল** — প্রধান কর্মক্ষমতা উন্নতি, আরও ভাল বিশ্লেষণ
- **2.1 (2024): বর্ধিত`when`, সম্পত্তি প্রতিনিধি
## করোটিন বিবর্তন
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## মাল্টিপ্ল্যাটফর্ম বিবর্তন
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## ভাষার বৈশিষ্ট্য বিবর্তন
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

## বিভিন্ন প্ল্যাটফর্মে কোটলিন
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## ইকোসিস্টেম বৃদ্ধি
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

## মূল ডিজাইনের নীতি
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
