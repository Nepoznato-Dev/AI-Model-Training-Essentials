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
# স্কালা — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 1.0 | 2004 | প্রাথমিক প্রকাশ (মার্টিন ওডারস্কি, ইপিএফএল) |
| 2.0 | 2006 | কাঠামোগত প্রকার, প্যাটার্ন মিলে উন্নতি |
| 2.7 | 2009 | অভিনেতা লাইব্রেরি, উন্নত ধরনের অনুমান |
| 2.8 | 2010 | **নামযুক্ত/ডিফল্ট আর্গুমেন্ট**, প্যাকেজ অবজেক্ট, সংগ্রহ পুনরায় ডিজাইন |
| 2.9 | 2011 | সমান্তরাল সংগ্রহ, স্ট্রিং ইন্টারপোলেশন |
| 2.10 | 2013 | **মান ক্লাস**, নিহিত উন্নতি, স্ট্রিং ইন্টারপোলেশন |
| 2.11 | 2014 | স্ট্রিং ইন্টারপোলেশন, উন্নত সংগ্রহ |
| 2.12 | 2016 | **SAM প্রকার** (জাভা 8 ল্যাম্বডাস), স্ট্রম্যানের সংগ্রহ |
| 2.13 | 2019 | **সংগ্রহগুলি পুনরায় ডিজাইন করুন**, নাম পরামিতি দ্বারা অন্তর্নিহিত |
| 3.0 | 2021 | **মেজর**: নতুন কম্পাইলার (ডটি),`enum`,`given`/`using`, এক্সটেনশন পদ্ধতি |
| 3.1 | 2022 | রপ্তানি ধারা,`opaque`প্রকার উপনাম |
| 3.2 | 2022 | `inline`উন্নতি,`erased`কীওয়ার্ড |
| 3.3 | 2023 | **LTS প্রকাশ** — স্পষ্ট নাল,`derives`ধারা |
| 3.4 | 2024 | নামযুক্ত টাইপ আর্গুমেন্ট,`@experimental`টীকা |
| 3.5 | 2024 | ক্যাপচার চেকার, উন্নত ত্রুটি বার্তা |
| 3.6 | 2025 | আরও পরিমার্জন, কর্মক্ষমতা উন্নতি |
## প্রধান মাইলফলক
### প্রারম্ভিক স্কালা (2004-2010)
- **2004**: মার্টিন ওডারস্কি স্কালা প্রকাশ করেছেন — JVM-এ OOP এবং FP একত্রিত করে
- **2.0–2.7**: কাঠামোগত প্রকার, অভিনেতা, উন্নত ধরনের অনুমান
- **2.8 (2010)**: নামযুক্ত/ডিফল্ট আর্গুমেন্ট, প্যাকেজ অবজেক্ট, সংগ্রহ পুনরায় ডিজাইন — "আধুনিক স্কালা শুরু হয়"
### স্কেলা 2.x পরিপক্কতা (2011-2020)
- **2.9**: সমান্তরাল সংগ্রহ
- **2.10**: মান শ্রেণী, স্ট্রিং ইন্টারপোলেশন, অন্তর্নিহিত উন্নতি
- **2.12**: SAM প্রকারগুলি — সিমলেস জাভা 8 ইন্টারপ
- **2.13**: প্রধান সংগ্রহ লাইব্রেরি পুনরায় ডিজাইন (অপরিবর্তনীয় ডিফল্ট)
### স্কালা 3 — দ্য রেনেসাঁ (2021-বর্তমান)
- **3.0 (2021)**: সম্পূর্ণ কম্পাইলার পুনর্লিখন (ডটি → স্কালা 3)
  -`enum`সিল করা বৈশিষ্ট্য + কেস ক্লাস বয়লারপ্লেট প্রতিস্থাপন করে
  -`given`/`using`অন্তর্নিহিত প্যারামিটার প্রতিস্থাপন করে
  - এক্সটেনশন পদ্ধতি অন্তর্নিহিত ক্লাস প্রতিস্থাপন করে
  -`match`প্রকার, ইউনিয়ন প্রকার, ছেদ প্রকার
  - সরলীকৃত সিনট্যাক্স (ঐচ্ছিক ধনুর্বন্ধনী, কম কীওয়ার্ড)
- **3.3 (2023): প্রথম LTS — স্পষ্ট নাল,`derives`ধারা
- **3.4–3.6**: নামযুক্ত টাইপ আর্গুমেন্ট, ক্যাপচার চেকার, পারফরম্যান্স
## সিনট্যাক্স বিবর্তন
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

## টাইপ সিস্টেম বিবর্তন
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

## কনকারেন্সি বিবর্তন
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## মূল ডিজাইনের নীতি
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## ইকোসিস্টেম বৃদ্ধি
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
