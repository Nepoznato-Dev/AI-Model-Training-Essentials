---
# Metadata
title: "Dart — Version History & Evolution"
description: "Comprehensive version history and evolution of Dart from 1.0 to modern Dart."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Dart - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 2013 | انتشار اولیه (گوگل، لارس باک و کسپر لوند) |
| 1.2 | 2014 | بهبود کامپایلر Dart2JS |
| 1.3 | 2014 |  پشتیبانی از`async`/`await`|
| 1.4 | 2014 |  `enum`، بهبودها را ترکیب می کند |
| 1.5 | 2014 | ژنراتور (`sync*`,`async*`) |
| 1.6 | 2014 |  بهبودهای`Future`|
| 1.8 | 2014 |  بهبودهای`dart:io`|
| 1.9 | 2015 | حالت قوی (انتخاب کردن) |
| 1.11 | 2015 |  بهبودهای`Future.then`|
| 1.12 | 2015 | **حالت قوی** اجرا شد |
| 2.0 | 2018 | **مهم**: سیستم نوع صدا، آماده سازی ایمنی `null`، بازنویسی مجموعه ها |
| 2.1 | 2018 | `int`/`double`یکسان سازی،`await for`|
| 2.2 | 2019 | `Set`تحت اللفظی، بهبود مجموعه`const`|
| 2.3 | 2019 | مجموعه`if`, مجموعه`for`, اسپرد اپراتور`...`|
| 2.6 | 2019 | روش های گسترش |
| 2.7 | 2020 | پارامترهای با نام پیش فرض |
| 2.10 | 2020 | **ایمنی تهی صدا** (انتخاب کردن) |
| 2.12 | 2021 | **ایمنی تهی به طور پیش فرض فعال است** |
| 2.13 | 2021 | پارگی های سازنده |
| 2.14 | 2021 |  بهبودهای `late`، اعداد صحیح بدون علامت |
| 2.15 | 2021 | پارگی سازنده پایدار، انواع عملکرد عمومی |
| 2.17 | 2022 | ** پارامترهای فوق العاده **، enums پیشرفته |
| 2.18 | 2022 | استنتاج نوع پیشرفته |
| 2.19 | 2023 | سوابق و الگوها (پیش نمایش) |
| 3.0 | 2023 | **مهم**: رکوردها، الگوها، اصلاح کننده های کلاس، عبارات`switch`|
| 3.1 | 2023 | بهبود الگو، کلاس های مهر و موم شده |
| 3.2 | 2023 | بهبود تجزیه و تحلیل استاتیک |
| 3.3 | 2024 | انواع پسوند، بهبود بیان`switch`|
| 3.4 | 2024 |  عناصر `if`، بهبودهای`case`|
| 3.5 | 2024 | ماکروها (پیش نمایش)، اصلاحات بیشتر زبان |
| 3.6 | 2025 | توسعه در حال انجام |
## نقاط عطف اصلی
### Dart 1.x - The Early Years (2013–2017)
- **2013**: Google Dart را منتشر می کند — طراحی شده برای برنامه نویسی ساختار یافته وب
- **هدف**: جاوا اسکریپت را برای توسعه وب جایگزین کنید (جاه طلبی بعداً محور شد)
- **1.0**: کلاس ها، رابط ها، ایزوله ها، تایپ اختیاری
- **1.3**: پشتیبانی از`async`/ `await`
- **1.9**: حالت قوی (تایپ دقیق را انتخاب کنید)
- Dart VM به طور خلاصه در Chromium استفاده شد، سپس حذف شد
### The Flutter Pivot (2017–2018)
- **2017**: چارچوب Flutter اعلام شد - دارت به زبان رابط کاربری تبدیل می شود
- دارت هدف خود را پیدا می کند: توسعه تلفن همراه / دسکتاپ / وب بین پلتفرمی
- **2.0 (2018)**: بازنویسی کامل - سیستم نوع صدا، مجموعه های مدرن
### Dart 2.x - دارت مدرن (2018–2023)
- **2.0**: سیستم نوع صدا، به طور پیش فرض دیگر`dynamic`وجود ندارد
- **2.3**: مجموعه`if`/ `for`، عملگر پخش - عالی برای درختان ویجت Flutter
- **2.6**: روش های گسترش
- **2.10**: ایمنی تهی صدا (انتخاب کردن)
- **2.12**: **ایمنی تهی به طور پیش فرض فعال است** — انواع`?`nullable
- **2.17**: پارامترهای فوق العاده (`super.x`)، فهرست های پیشرفته
### Dart 3.x - رکوردها و الگوها (2023–اکنون)
- **3.0 (2023)**: **سوابق** (حامل های داده ناشناس)، **الگوها** (تخریب کننده)، **تغییرکننده های کلاس** (`sealed`، `final`، `interface`، `interface`، XQZMARKER3XZQZ)، بیان XQZMARKER3X
- **3.3 (2024)**: انواع پسوند (پوشش های بدون هزینه)
- **3.5 (2024)**: پیش نمایش ماکروها - فرابرنامه نویسی در زمان کامپایل
## تکامل نحو
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

## تایپ سیستم تکامل
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

## اصول کلیدی طراحی
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## رشد اکوسیستم
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
