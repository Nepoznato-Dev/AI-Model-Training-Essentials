<!--
---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [scala, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Scala - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 2004 | انتشار اولیه (مارتین اودرسکی، EPFL) |
| 2.0 | 2006 | انواع سازه، بهبود تطبیق الگو |
| 2.7 | 2009 | کتابخانه بازیگران، استنتاج نوع بهبود یافته |
| 2.8 | 2010 | **آگومان های نامگذاری شده/پیش فرض**، اشیاء بسته، طراحی مجدد مجموعه ها |
| 2.9 | 2011 | مجموعه های موازی، درون یابی رشته ای |
| 2.10 | 2013 | **کلاس های ارزش**، بهبودهای ضمنی، درون یابی رشته ای |
| 2.11 | 2014 | درون یابی رشته ای، مجموعه های بهبود یافته |
| 2.12 | 2016 | **انواع SAM** (Java 8 lambdas)، مجموعه هایی در Strawman |
| 2.13 | 2019 | **طراحی مجدد مجموعه**، پارامترهای ضمنی نام |
| 3.0 | 2021 | **عمده**: کامپایلر جدید (Dotty),`enum`,`given`/`using`, روش های توسعه |
| 3.1 | 2022 | بندهای صادراتی، نام مستعار نوع`opaque`|
| 3.2 | 2022 |  بهبودهای `inline`، کلمه کلیدی`erased`|
| 3.3 | 2023 | **نسخه LTS** — تهی صریح، بند`derives`|
| 3.4 | 2024 | آرگومان های نوع نامگذاری شده، حاشیه نویسی`@experimental`|
| 3.5 | 2024 | جستجوگر ضبط، پیام های خطای بهبود یافته |
| 3.6 | 2025 | اصلاحات بیشتر، بهبود عملکرد |
## نقاط عطف اصلی
### اسکالا اولیه (2004–2010)
- **2004**: مارتین اودرسکی Scala را منتشر کرد - ترکیب OOP و FP در JVM
- **2.0–2.7**: انواع ساختاری، بازیگران، استنتاج نوع بهبود یافته
- **2.8 (2010)**: آرگومان‌های نام‌گذاری شده/پیش‌فرض، اشیاء بسته، طراحی مجدد مجموعه‌ها - "اسکالای مدرن آغاز می‌شود"
### بلوغ Scala 2.x (2011–2020)
- **2.9**: مجموعه های موازی
- **2.10**: کلاس های ارزش، درون یابی رشته ای، بهبودهای ضمنی
- **2.12**: انواع SAM - جاوا 8 بدون درز
- **2.13**: طراحی مجدد کتابخانه مجموعه های اصلی (پیش فرض غیرقابل تغییر)
### اسکالا 3 - رنسانس (2021–اکنون)
- **3.0 (2021)**: بازنویسی کامل کامپایلر (Dotty → Scala 3)
  -`enum`جایگزین صفت مهر و موم شده + کلاس کیس دیگ بخار می شود
  -`given`/`using`جایگزین پارامترهای ضمنی می شود
  - متدهای توسعه جایگزین کلاس های ضمنی می شوند
  - انواع `match`، انواع اتحادیه، انواع تقاطع
  - نحو ساده شده (پرانتز اختیاری، کلمات کلیدی کمتر)
- **3.3 (2023)**: LTS اول - تهی صریح، بند `derives`
- **3.4–3.6**: آرگومان های نوع نامگذاری شده، جستجوگر ضبط، عملکرد
## تکامل نحو
```scala
// Scala 2: Implicit class for extension methods
implicit class StringOps(val s: String) extends AnyVal {
  def shout: String = s.toUpperCase + "!"
}

// Scala 3: Extension methods
extension (s: String)
  def shout: String = s.toUpperCase + "!"

// Scala 2: Sealed trait + case class (ADT)
sealed trait Color
case object Red extends Color
case object Blue extends Color

// Scala 3: enum
enum Color:
  case Red, Blue, Green

// Scala 2: Implicit parameters
def greet(implicit ctx: Context): String = ctx.name

// Scala 3: given/using
given ctx: Context = Context("Alice")
def greet(using ctx: Context): String = ctx.name

// Scala 3: Union types
def process(input: String | Int): String = input.toString

// Scala 3: Match types
type Elem[X] = X match
  case String => Char
  case List[t] => t
  case _ => X
```

## تایپ سیستم تکامل
```
Scala 2.0:  Structural types, refinements
Scala 2.7:  Existential types
Scala 2.8:  Implicit resolution rules
Scala 2.10: Value classes, macro annotations
Scala 2.12: SAM conversion, Java 8 interop
Scala 2.13: Implicit by-name, literal types
Scala 3.0:  Union types, intersection types, match types,
            opaque types, enum, given/using, extension methods
Scala 3.3:  Explicit nulls, derives clause
Scala 3.4:  Named type arguments
Scala 3.5:  Capture checker (experimental)
```

## تکامل همزمان
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## اصول کلیدی طراحی
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## رشد اکوسیستم
```
2004: Scala released by Martin Odersky (EPFL)
2009: Twitter adopts Scala — puts Scala on the map
2011: Akka framework — distributed computing
2012: Play Framework 2.0 — web development
2014: Apache Spark — big data processing in Scala
2016: sbt becomes standard build tool
2021: Scala 3 — modernized language
2025: Scala powers LinkedIn, Twitter, Netflix, The Guardian, Stripe
       sbt, Mill build tools; Akka, ZIO, Cats Effect ecosystems
```
