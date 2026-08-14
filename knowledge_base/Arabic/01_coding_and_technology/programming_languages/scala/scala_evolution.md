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
# سكالا — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| 1.0 | 2004 | الإصدار الأولي (مارتن أودرسكي، EPFL) |
| 2.0 | 2006 | الأنواع الهيكلية، تحسينات مطابقة الأنماط |
| 2.7 | 2009 | مكتبة الممثلين، تحسين نوع الاستدلال |
| 2.8 | 2010 | **الوسائط المسماة/الافتراضية**، كائنات الحزمة، إعادة تصميم المجموعات |
| 2.9 | 2011 | المجموعات المتوازية، استيفاء السلسلة |
| 2.10 | 2013 | **فئات القيمة**، التحسينات الضمنية، استيفاء السلسلة |
| 2.11 | 2014 | استيفاء السلسلة، تحسين المجموعات |
| 2.12 | 2016 | **أنواع SAM** (Java 8 lambdas)، مجموعات على Strawman |
| 2.13 | 2019 | **إعادة تصميم المجموعات**، معلمات الاسم الضمني |
| 3.0 | 2021 | **التخصص**: مترجم جديد (Dotty)، `enum`،`given`/ `using`، طرق الامتداد |
| 3.1 | 2022 | عبارات التصدير، الأسماء المستعارة للنوع`opaque`|
| 3.2 | 2022 |  تحسينات `inline`، الكلمة الرئيسية`erased`|
| 3.3 | 2023 | **إصدار LTS** — القيم الخالية الصريحة، جملة`derives`|
| 3.4 | 2024 | وسيطات النوع المُسمى، التعليق التوضيحي`@experimental`|
| 3.5 | 2024 | مدقق الالتقاط، رسائل خطأ محسنة |
| 3.6 | 2025 | مزيد من التحسينات وتحسينات الأداء |
## المعالم الرئيسية
### أوائل سكالا (2004-2010)
- **2004**: أصدر Martin Odersky Scala — الذي يجمع بين OOP وFP على JVM
- **2.0–2.7**: الأنواع الهيكلية، الجهات الفاعلة، الاستدلال المحسّن للنوع
- **2.8 (2010)**: الوسائط المُسماة/الافتراضية، وكائنات الحزمة، وإعادة تصميم المجموعات - "بدء Scala الحديث"
### نضج سكالا 2.x (2011-2020)
- **2.9**: المجموعات المتوازية
- **2.10**: فئات القيمة، واستيفاء السلسلة، والتحسينات الضمنية
- **2.12**: أنواع SAM — التشغيل التفاعلي السلس لـ Java 8
- **2.13**: إعادة تصميم مكتبة المجموعات الرئيسية (افتراضي غير قابل للتغيير)
### سكالا 3 — عصر النهضة (2021 إلى الوقت الحاضر)
- **3.0 (2021)**: إعادة كتابة المترجم بالكامل (Dotty → Scala 3)
  - يستبدل`enum`الصفة المعيارية المختومة + فئة الحالة
  -`given`/`using`يستبدل المعلمات الضمنية
  - تحل طرق الامتداد محل الفئات الضمنية
  - أنواع `match`، أنواع الاتحاد، أنواع التقاطع
  - بناء الجملة المبسط (الأقواس الاختيارية، عدد أقل من الكلمات الرئيسية)
- **3.3 (2023)**: أول LTS — القيم الخالية الصريحة، جملة `derives`
- **3.4–3.6**: وسيطات النوع المُسمى، ومدقق الالتقاط، والأداء
## تطور بناء الجملة
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

## نوع تطور النظام
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

## تطور التزامن
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## مبادئ التصميم الرئيسية
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## نمو النظام البيئي
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
