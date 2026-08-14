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
# ডার্ট — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 1.0 | 2013 | প্রাথমিক প্রকাশ (Google, Lars Bak & Kasper Lund) |
| 1.2 | 2014 | Dart2JS কম্পাইলার উন্নতি |
| 1.3 | 2014 | `async`/`await`সমর্থন |
| 1.4 | 2014 | `enum`, মিশ্রিত উন্নতি |
| 1.5 | 2014 | জেনারেটর (`sync*`,`async*`) |
| 1.6 | 2014 | `Future`উন্নতি |
| 1.8 | 2014 | `dart:io`উন্নতি |
| 1.9 | 2015 | শক্তিশালী মোড (অপ্ট-ইন) |
| 1.11 | 2015 | `Future.then`উন্নতি |
| 1.12 | 2015 | **শক্তিশালী মোড** বলবৎ |
| 2.0 | 2018 | **মেজর**: সাউন্ড টাইপ সিস্টেম,`null`নিরাপত্তা প্রস্তুতি, সংগ্রহ পুনর্লিখন |
| 2.1 | 2018 | `int`/`double`একীকরণ,`await for`|
| 2.2 | 2019 | `Set`আক্ষরিক,`const`সংগ্রহের উন্নতি |
| 2.3 | 2019 | সংগ্রহ`if`, সংগ্রহ`for`, স্প্রেড অপারেটর`...`|
| 2.6 | 2019 | এক্সটেনশন পদ্ধতি |
| 2.7 | 2020 | ডিফল্ট নামের পরামিতি |
| 2.10 | 2020 | **সাউন্ড নাল নিরাপত্তা** (অপ্ট-ইন) |
| 2.12 | 2021 | **নাল নিরাপত্তা ডিফল্টরূপে সক্ষম** |
| 2.13 | 2021 | কনস্ট্রাক্টর টিয়ার-অফ |
| 2.14 | 2021 | `late`উন্নতি, স্বাক্ষরবিহীন পূর্ণসংখ্যা |
| 2.15 | 2021 | কনস্ট্রাক্টর টিয়ার-অফ স্থিতিশীল, জেনেরিক ফাংশন প্রকার |
| 2.17 | 2022 | **সুপার প্যারামিটার**, উন্নত enums |
| 2.18 | 2022 | বর্ধিত প্রকার অনুমান |
| 2.19 | 2023 | রেকর্ড এবং নিদর্শন (প্রিভিউ) |
| 3.0 | 2023 | **মেজর**: রেকর্ড, প্যাটার্ন, ক্লাস মডিফায়ার,`switch`এক্সপ্রেশন |
| 3.1 | 2023 | প্যাটার্ন উন্নতি, সিল ক্লাস |
| 3.2 | 2023 | স্ট্যাটিক বিশ্লেষণ উন্নতি |
| 3.3 | 2024 | এক্সটেনশন প্রকার,`switch`এক্সপ্রেশন উন্নতি |
| 3.4 | 2024 | `if`উপাদান,`case`উন্নতি |
| 3.5 | 2024 | ম্যাক্রো (প্রিভিউ), আরও ভাষা পরিমার্জন |
| 3.6 | 2025 | চলমান উন্নয়ন |
## প্রধান মাইলফলক
### ডার্ট 1.x — দ্য আর্লি ইয়ারস (2013-2017)
- **2013**: Google Dart প্রকাশ করেছে — যা স্ট্রাকচার্ড ওয়েব প্রোগ্রামিংয়ের জন্য ডিজাইন করা হয়েছে
- **লক্ষ্য**: ওয়েব ডেভেলপমেন্টের জন্য জাভাস্ক্রিপ্ট প্রতিস্থাপন করুন (আকাঙ্খা পরে পিভট করা হয়েছে)
- **1.0**: ক্লাস, ইন্টারফেস, আইসোলেট, ঐচ্ছিক টাইপিং
- **1.3**:`async`/`await`সমর্থন
- **1.9**: শক্তিশালী মোড (অপ্ট-ইন কঠোর টাইপিং)
- ক্রোমিয়ামে সংক্ষিপ্তভাবে ব্যবহৃত ডার্ট ভিএম, তারপর সরানো হয়েছে
### দ্য ফ্লাটার পিভট (2017-2018)
- **2017**: ফ্লটার ফ্রেমওয়ার্ক ঘোষণা করা হয়েছে — ডার্ট UI ভাষাতে পরিণত হয়েছে
- ডার্ট তার উদ্দেশ্য খুঁজে পায়: ক্রস-প্ল্যাটফর্ম মোবাইল/ডেস্কটপ/ওয়েব উন্নয়ন
- **2.0 (2018): সম্পূর্ণ পুনর্লিখন — সাউন্ড টাইপ সিস্টেম, আধুনিক সংগ্রহ
### ডার্ট 2.x — আধুনিক ডার্ট (2018-2023)
- **2.0**: সাউন্ড টাইপ সিস্টেম, ডিফল্টরূপে`dynamic`আর নেই
- **2.3**: সংগ্রহ`if`/ `for`, স্প্রেড অপারেটর — ফ্লটার উইজেট গাছের জন্য দুর্দান্ত
- **2.6**: এক্সটেনশন পদ্ধতি
- **2.10**: সাউন্ড নাল নিরাপত্তা (অপ্ট-ইন)
- **2.12**: **ডিফল্টরূপে শূন্য নিরাপত্তা সক্রিয়** —`?`বাতিলযোগ্য প্রকার
- **2.17**: সুপার প্যারামিটার (`super.x`), উন্নত enums
### ডার্ট 3.x — রেকর্ড এবং প্যাটার্নস (2023-বর্তমান)
- **3.0 (2023): **রেকর্ড** (বেনামী ডেটা ক্যারিয়ার), **প্যাটার্ন** (ডিস্ট্রাকচারিং), **ক্লাস মডিফায়ার** (`sealed`,`final`,`interface`,`interface`, `base`QZQZQZQZQZ4 এক্সপ্রেস
- **3.3 (2024)**: এক্সটেনশনের ধরন (জিরো-কস্ট র্যাপার)
- **3.5 (2024): ম্যাক্রো প্রিভিউ — কম্পাইল-টাইম মেটাপ্রোগ্রামিং
## সিনট্যাক্স বিবর্তন
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

## টাইপ সিস্টেম বিবর্তন
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

## মূল ডিজাইনের নীতি
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## ইকোসিস্টেম বৃদ্ধি
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
