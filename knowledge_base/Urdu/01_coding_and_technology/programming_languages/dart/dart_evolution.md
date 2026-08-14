---
# Metadata
title: "Dart — Version History & Evolution"
description: "Comprehensive version history and evolution of Dart from 1.0 to modern Dart."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [dart, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# ڈارٹ - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 2013 | ابتدائی ریلیز (گوگل، لارس باک اور کاسپر لنڈ) |
| 1.2 | 2014 | Dart2JS کمپائلر میں بہتری |
| 1.3 | 2014 | `async`/`await`سپورٹ |
| 1.4 | 2014 | `enum`, mixins بہتری |
| 1.5 | 2014 | جنریٹرز (`sync*`,`async*`) |
| 1.6 | 2014 | `Future`بہتری |
| 1.8 | 2014 | `dart:io`بہتری |
| 1.9 | 2015 | مضبوط موڈ (آپٹ ان) |
| 1.11 | 2015 | `Future.then`بہتری |
| 1.12 | 2015 | **مضبوط موڈ** نافذ |
| 2.0 | 2018 | **میجر**: ساؤنڈ ٹائپ سسٹم،`null`حفاظتی تیاری، مجموعے دوبارہ لکھنا |
| 2.1 | 2018 | `int`/`double`اتحاد،`await for`|
| 2.2 | 2019 | `Set`لفظی،`const`مجموعہ میں بہتری |
| 2.3 | 2019 | مجموعہ`if`, مجموعہ`for`, اسپریڈ آپریٹر`...`|
| 2.6 | 2019 | توسیع کے طریقے |
| 2.7 | 2020 | پہلے سے طے شدہ پیرامیٹرز |
| 2.10 | 2020 | **ساؤنڈ نال سیفٹی** (آپٹ ان) |
| 2.12 | 2021 | **بذریعہ ڈیفالٹ کالعدم حفاظت فعال** |
| 2.13 | 2021 | کنسٹرکٹر کے آنسو |
| 2.14 | 2021 | `late`بہتری، غیر دستخط شدہ عدد |
| 2.15 | 2021 | کنسٹرکٹر ٹیر آف مستحکم، عام فنکشن کی قسمیں |
| 2.17 | 2022 | **سپر پیرامیٹرز**، بڑھا ہوا enums |
| 2.18 | 2022 | بہتر قسم کا اندازہ |
| 2.19 | 2023 | ریکارڈز اور پیٹرن (پیش نظارہ) |
| 3.0 | 2023 | **بڑا**: ریکارڈز، پیٹرن، کلاس موڈیفائر،`switch`اظہار |
| 3.1 | 2023 | پیٹرن میں بہتری، مہربند کلاسز |
| 3.2 | 2023 | جامد تجزیہ میں بہتری |
| 3.3 | 2024 | ایکسٹینشن کی اقسام،`switch`اظہار میں بہتری |
| 3.4 | 2024 | `if`عناصر،`case`بہتری |
| 3.5 | 2024 | میکروس (پیش نظارہ)، مزید زبان کی اصلاح |
| 3.6 | 2025 | جاری ترقی |
## اہم سنگ میل
### ڈارٹ 1.x — ابتدائی سال (2013–2017)
- **2013**: گوگل نے ڈارٹ کو ریلیز کیا — جسے سٹرکچرڈ ویب پروگرامنگ کے لیے ڈیزائن کیا گیا ہے۔
- **مقصد**: ویب ڈویلپمنٹ کے لیے جاوا اسکرپٹ کو تبدیل کریں (عزیز بعد میں محور)
- **1.0**: کلاسز، انٹرفیس، الگ تھلگ، اختیاری ٹائپنگ
- **1.3**:`async`/`await`سپورٹ
- **1.9**: مضبوط موڈ (آپٹ ان سخت ٹائپنگ)
- Chromium میں مختصر طور پر استعمال ہونے والا Dart VM، پھر ہٹا دیا گیا۔
### دی فلٹر پیوٹ (2017–2018)
- **2017**: فلٹر فریم ورک کا اعلان کیا گیا — Dart UI زبان بن گئی۔
- ڈارٹ نے اپنا مقصد تلاش کیا: کراس پلیٹ فارم موبائل/ڈیسک ٹاپ/ویب ڈویلپمنٹ
- **2.0 (2018): مکمل دوبارہ لکھنا — ساؤنڈ ٹائپ سسٹم، جدید مجموعے
### ڈارٹ 2.x — ماڈرن ڈارٹ (2018–2023)
- **2.0**: ساؤنڈ ٹائپ سسٹم، ڈیفالٹ کے طور پر مزید`dynamic`نہیں
- **2.3**: مجموعہ`if`/ `for`، اسپریڈ آپریٹر — فلٹر ویجیٹ درختوں کے لیے بہترین
- **2.6**: توسیع کے طریقے
- **2.10**: ساؤنڈ نال سیفٹی (آپٹ ان)
- **2.12**: **بذریعہ ڈیفالٹ کالعدم حفاظت فعال** —`?`کالعدم قسمیں
- **2.17**: سپر پیرامیٹرز (`super.x`)، بڑھا ہوا enums
### Dart 3.x — ریکارڈز اور پیٹرنز (2023–موجودہ)
- **3.0 (2023)**: **ریکارڈز** (گمنام ڈیٹا کیریئرز)، **پیٹرنز** (ڈسٹرکچرنگ)، **کلاس موڈیفائر** (`sealed`,`final`,`interface`,`interface`, `base`QZQZQ4X
- **3.3 (2024)**: توسیع کی اقسام (صفر لاگت والے ریپرز)
- **3.5 (2024)**: میکرو پیش نظارہ - مرتب وقت میٹا پروگرامنگ
## نحوی ارتقاء
```dart
// Dart 1.x: Verbose, JavaScript-like
class Person {
  String name;
  int age;
  Person(this.name, this.age);
}

// Dart 2.0: Sound types
Person createPerson(String name, int age) {
  return Person(name, age);
}

// Dart 2.3: Collection if/for, spread
var widgets = [
  if (showHeader) HeaderWidget(),
  for (var item in items) ItemWidget(item),
  ...otherWidgets,
];

// Dart 2.6: Extension methods
extension StringX on String {
  String get shout => toUpperCase() + '!';
}

// Dart 2.12: Null safety
String? nullable;     // can be null
String nonNullable;   // cannot be null (enforced)

// Dart 2.17: Super parameters, enhanced enums
class NamedPerson extends Person {
  NamedPerson({super.name, super.age});  // pass to super constructor
}

enum Status {
  active('Active'),
  inactive('Inactive');
  final String label;
  const Status(this.label);
}

// Dart 3.0: Records and patterns
(String, int) getNameAndAge() => ('Alice', 30);

sealed class Shape {}
class Circle extends Shape { final double radius; Circle(this.radius); }
class Rect extends Shape { final double w, h; Rect(this.w, this.h); }

String describe(Shape s) => switch (s) {
  Circle(radius: var r) => 'Circle($r)',
  Rect(w: var w, h: var h) => 'Rect(${w}x${h})',
};
```

## ٹائپ سسٹم ارتقاء
```
Dart 1.0:  Optional types (annotations only)
Dart 1.9:  Strong mode (opt-in)
Dart 2.0:  Sound type system (enforced)
Dart 2.10: Sound null safety (opt-in)
Dart 2.12: Null safety by default (? nullable, ! assert)
Dart 2.15: Generic function types
Dart 3.0:  Records, sealed classes, patterns, class modifiers
Dart 3.3:  Extension types (zero-cost wrappers)
Dart 3.5:  Macros (compile-time metaprogramming)
```

## ڈیزائن کے کلیدی اصول
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## ماحولیاتی نظام کی نمو
```
2013: Dart 1.0 released by Google
2015: AngularDart — Google uses Dart internally
2017: Flutter announced — Dart finds its purpose
2018: Dart 2.0 — sound type system
2021: Dart 2.12 — null safety
2022: Flutter 3 — iOS, Android, Web, Desktop, Embedded
2023: Dart 3.0 — records, patterns, sealed classes
2025: Flutter + Dart power apps from BMW, Alibaba, Google Pay, Toyota
       pub.dev hosts 30,000+ packages
       Dart runs on: mobile (Flutter), web (dart2wasm), server (dart:io), embedded
```
