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
# اسکالا - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 2004 | ابتدائی ریلیز (مارٹن اوڈرسکی، ای پی ایف ایل) |
| 2.0 | 2006 | ساختی اقسام، پیٹرن کے ملاپ میں بہتری |
| 2.7 | 2009 | اداکاروں کی لائبریری، بہتر قسم کا اندازہ |
| 2.8 | 2010 | **نامزد/پہلے سے طے شدہ دلائل**، پیکج آبجیکٹ، مجموعے دوبارہ ڈیزائن |
| 2.9 | 2011 | متوازی مجموعے، سٹرنگ انٹرپولیشن |
| 2.10 | 2013 | **ویلیو کلاسز**، مضمر بہتری، سٹرنگ انٹرپولیشن |
| 2.11 | 2014 | سٹرنگ انٹرپولیشن، بہتر مجموعہ |
| 2.12 | 2016 | **SAM کی اقسام** (جاوا 8 لیمبڈاس)، اسٹرا مین پر مجموعہ |
| 2.13 | 2019 | **مجموعوں کو دوبارہ ڈیزائن کریں**، نام کے پیرامیٹرز کے ذریعے |
| 3.0 | 2021 | **میجر**: نیا کمپائلر (ڈاٹی)، `enum`،`given`/ `using`، توسیع کے طریقے |
| 3.1 | 2022 | ایکسپورٹ شقیں،`opaque`قسم کے عرفی نام |
| 3.2 | 2022 | `inline`بہتری،`erased`کلیدی لفظ |
| 3.3 | 2023 | **LTS ریلیز** — واضح nulls،`derives`شق |
| 3.4 | 2024 | نامزد قسم کے دلائل،`@experimental`تشریح |
| 3.5 | 2024 | کیپچر چیکر، بہتر خرابی کے پیغامات |
| 3.6 | 2025 | مزید تطہیر، کارکردگی میں بہتری |
## اہم سنگ میل
### ابتدائی اسکیلا (2004–2010)
- **2004**: مارٹن اوڈرسکی نے اسکالا جاری کیا - JVM پر OOP اور FP کو یکجا کرتے ہوئے
- **2.0–2.7**: ساختی اقسام، اداکار، بہتر قسم کا اندازہ
- **2.8 (2010)**: نامزد/پہلے سے طے شدہ دلائل، پیکیج آبجیکٹ، مجموعوں کو دوبارہ ڈیزائن کرنا — "جدید اسکالا شروع ہوتا ہے"
### Scala 2.x میچورٹی (2011–2020)
- **2.9**: متوازی مجموعہ
- **2.10**: ویلیو کلاسز، سٹرنگ انٹرپولیشن، مضمر بہتری
- **2.12**: SAM کی قسمیں - بغیر کسی رکاوٹ جاوا 8 انٹراپ
- **2.13**: بڑے مجموعوں کی لائبریری کو دوبارہ ڈیزائن کرنا (غیر تبدیل شدہ ڈیفالٹ)
### اسکیلا 3 — دی رینیسانس (2021–موجودہ)
- **3.0 (2021)**: مکمل کمپائلر دوبارہ لکھنا (Dotty → Scala 3)
  -`enum`سیل شدہ ٹریٹ + کیس کلاس بوائلر پلیٹ کی جگہ لے لیتا ہے۔
  -`given`/`using`مضمر پیرامیٹرز کی جگہ لے لیتا ہے
  - توسیع کے طریقے مضمر کلاسوں کی جگہ لے لیتے ہیں۔
  -`match`اقسام، یونین کی اقسام، چوراہے کی اقسام
  - آسان نحو (اختیاری منحنی خطوط وحدانی، کم مطلوبہ الفاظ)
- **3.3 (2023)**: پہلا LTS — واضح nulls،`derives`شق
- **3.4–3.6**: نامزد قسم کے دلائل، کیپچر چیکر، کارکردگی
## نحوی ارتقاء
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

## ٹائپ سسٹم ارتقاء
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

## ہم آہنگی ارتقاء
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## ڈیزائن کے کلیدی اصول
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## ماحولیاتی نظام کی نمو
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
