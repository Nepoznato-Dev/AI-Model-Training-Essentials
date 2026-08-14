<!--
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

-->
# دارت — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| 1.0 | 2013 | الإصدار الأولي (جوجل، لارس باك وكاسبر لوند) |
| 1.2 | 2014 | تحسينات مترجم Dart2JS |
| 1.3 | 2014 |  دعم`async`/`await`|
| 1.4 | 2014 |  `enum`، تحسينات على المزج |
| 1.5 | 2014 | مولدات (`sync*`,`async*`) |
| 1.6 | 2014 |  تحسينات`Future`|
| 1.8 | 2014 |  تحسينات`dart:io`|
| 1.9 | 2015 | الوضع القوي (الاشتراك) |
| 1.11 | 2015 |  تحسينات`Future.then`|
| 1.12 | 2015 | **الوضع القوي** مفروض |
| 2.0 | 2018 | ** التخصص **: نظام نوع الصوت، إعداد السلامة `null`، إعادة كتابة المجموعات |
| 2.1 | 2018 |  توحيد`int`/ `double`،`await for`|
| 2.2 | 2019 | `Set`الحرفي، تحسينات مجموعة`const`|
| 2.3 | 2019 | المجموعة`if`, المجموعة`for`, مشغل الانتشار`...`|
| 2.6 | 2019 | طرق التمديد |
| 2.7 | 2020 | المعلمات المسماة الافتراضية |
| 2.10 | 2020 | **سلامة الصوت الخالية** (الاشتراك) |
| 2.12 | 2021 | ** تم تمكين الأمان الفارغ بشكل افتراضي ** |
| 2.13 | 2021 | منشئ المسيل للدموع |
| 2.14 | 2021 |  تحسينات `late`، الأعداد الصحيحة غير الموقعة |
| 2.15 | 2021 | تمزيق المُنشئ أنواع الوظائف الثابتة والعامة |
| 2.17 | 2022 | ** المعلمات الفائقة **، التعدادات المحسنة |
| 2.18 | 2022 | الاستدلال النوعي المحسّن |
| 2.19 | 2023 | السجلات والأنماط (معاينة) |
| 3.0 | 2023 | **التخصص**: السجلات والأنماط ومعدلات الفئة وتعبيرات`switch`|
| 3.1 | 2023 | تحسينات النمط، فصول مختومة |
| 3.2 | 2023 | تحسينات التحليل الثابت |
| 3.3 | 2024 | أنواع الامتدادات، تحسينات تعبير`switch`|
| 3.4 | 2024 |  عناصر `if`، تحسينات`case`|
| 3.5 | 2024 | وحدات الماكرو (معاينة)، مزيد من التحسينات اللغوية |
| 3.6 | 2025 | التطوير المستمر |
## المعالم الرئيسية
### Dart 1.x — السنوات الأولى (2013-2017)
- **2013**: أطلقت Google لعبة Dart — المصممة لبرمجة الويب المنظمة
- **الهدف**: استبدال JavaScript لتطوير الويب (تمحور الطموح لاحقًا)
- **1.0**: الفئات، الواجهات، العزلات، الكتابة الاختيارية
- **1.3**: دعم`async`/ `await`
- **1.9**: الوضع القوي (تمكين الكتابة الصارمة)
- تم استخدام Dart VM في Chromium لفترة وجيزة، ثم تمت إزالته
### محور الرفرفة (2017-2018)
- **2017**: الإعلان عن إطار Flutter — أصبحت Dart هي لغة واجهة المستخدم
- يجد Dart غرضه: تطوير الأجهزة المحمولة/سطح المكتب/الويب عبر الأنظمة الأساسية
- **2.0 (2018)**: إعادة كتابة كاملة — نظام نوع الصوت، مجموعات حديثة
### Dart 2.x — دارت الحديثة (2018–2023)
- **2.0**: نظام نوع الصوت، لا مزيد من`dynamic`بشكل افتراضي
- **2.3**: مجموعة`if`/ `for`، عامل الانتشار - رائع لأشجار عناصر واجهة المستخدم Flutter
- **2.6**: طرق الامتداد
- **2.10**: سلامة الصوت الخالية (الاشتراك)
- **2.12**: **السلامة الخالية ممكّنة افتراضيًا** — أنواع`?`الخالية
- **2.17**: المعلمات الفائقة (`super.x`)، التعدادات المحسنة
### Dart 3.x — السجلات والأنماط (2023 إلى الوقت الحاضر)
- **3.0 (2023)**: **السجلات** (حاملات البيانات المجهولة)، **الأنماط** (التدمير)، **معدلات الفئة** ( تعبيرات`sealed`,`final`,`interface`,`base`), `switch`
- **3.3 (2024)**: أنواع الامتدادات (أغلفة بدون تكلفة)
- **3.5 (2024)**: معاينة وحدات الماكرو - البرمجة الوصفية لوقت الترجمة
## تطور بناء الجملة
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

## نوع تطور النظام
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

## مبادئ التصميم الرئيسية
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## نمو النظام البيئي
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
