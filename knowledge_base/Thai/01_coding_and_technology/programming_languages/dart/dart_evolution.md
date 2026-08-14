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

# Dart - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 1.0 | 2013 | การเปิดตัวครั้งแรก (Google, Lars Bak และ Kasper Lund) |
| 1.2 | 2014 | การปรับปรุงคอมไพเลอร์ Dart2JS |
| 1.3 | 2014 |  รองรับ`async`/`await`|
| 1.4 | 2014 | `enum`การปรับปรุงมิกซ์อิน |
| 1.5 | 2014 | เครื่องกำเนิดไฟฟ้า (`sync*`,`async*`) |
| 1.6 | 2014 |  การปรับปรุง`Future`|
| 1.8 | 2014 |  การปรับปรุง`dart:io`|
| 1.9 | 2558 | โหมดที่แข็งแกร่ง (เลือกใช้) |
| 1.11 | 2558 |  การปรับปรุง`Future.then`|
| 1.12 | 2558 | **โหมดเข้มงวด** บังคับใช้ |
| 2.0 | 2018 | **หลัก**: ระบบประเภทเสียง, การเตรียมความปลอดภัย `null`, การเขียนคอลเลกชันใหม่ |
| 2.1 | 2018 | `int`/`double`การรวม`await for`|
| 2.2 | 2019 | `Set`ตัวอักษร, การปรับปรุงคอลเลกชัน`const`|
| 2.3 | 2019 | คอลเลกชัน`if`, คอลเลกชัน`for`, ตัวดำเนินการสเปรด`...`|
| 2.6 | 2019 | วิธีการขยาย |
| 2.7 | 2020 | พารามิเตอร์ที่มีชื่อเริ่มต้น |
| 2.10 | 2020 | **เสียงปลอดภัยไร้ประโยชน์** (เลือกใช้) |
| 2.12 | 2021 | **ความปลอดภัยแบบ Null เปิดใช้งานตามค่าเริ่มต้น** |
| 2.13 | 2021 | ตัวสร้างการฉีกขาด |
| 2.14 | 2021 |  การปรับปรุง`late`จำนวนเต็มที่ไม่ได้ลงนาม |
| 2.15 | 2021 | ตัวสร้างการฉีกขาดมีความเสถียรประเภทฟังก์ชันทั่วไป |
| 2.17 | 2022 | **ซุปเปอร์พารามิเตอร์** แจงนับที่ได้รับการปรับปรุง |
| 2.18 | 2022 | การอนุมานประเภทขั้นสูง |
| 2.19 | 2023 | บันทึกและรูปแบบ (ตัวอย่าง) |
| 3.0 | 2023 | **หลัก**: บันทึก รูปแบบ ตัวดัดแปลงคลาส นิพจน์`switch`|
| 3.1 | 2023 | การปรับปรุงรูปแบบ คลาสที่ปิดผนึก |
| 3.2 | 2023 | การปรับปรุงการวิเคราะห์แบบคงที่ |
| 3.3 | 2024 | ประเภทส่วนขยาย การปรับปรุงนิพจน์ `switch`
| 3.4 | 2024 |  องค์ประกอบ`if`การปรับปรุง`case`|
| 3.5 | 2024 | มาโคร (ตัวอย่าง) การปรับแต่งภาษาเพิ่มเติม |
| 3.6 | 2025 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### Dart 1.x — ช่วงปีแรกๆ (2013–2017)
- **2013**: Google เปิดตัว Dart — ออกแบบมาสำหรับการเขียนโปรแกรมเว็บที่มีโครงสร้าง
- **เป้าหมาย**: แทนที่ JavaScript สำหรับการพัฒนาเว็บ (ความทะเยอทะยานภายหลัง pivoted)
- **1.0**: คลาส, อินเทอร์เฟซ, ไอโซเลท, การพิมพ์เพิ่มเติม
- **1.3**: รองรับ`async`/ `await`
- **1.9**: โหมดเข้มงวด (เลือกใช้การพิมพ์ที่เข้มงวด)
- Dart VM ที่ใช้ใน Chromium สั้นๆ แล้วลบออก
### The Flutter Pivot (2017–2018)
- **2017**: ประกาศเฟรมเวิร์ก Flutter — Dart กลายเป็นภาษา UI
- Dart ค้นหาจุดประสงค์: การพัฒนามือถือ/เดสก์ท็อป/เว็บข้ามแพลตฟอร์ม
- **2.0 (2018)**: เขียนใหม่ทั้งหมด — ระบบประเภทเสียง คอลเลกชันสมัยใหม่
### Dart 2.x — โมเดิร์นโผ (2018–2023)
- **2.0**: ระบบประเภทเสียง ไม่มี`dynamic`อีกต่อไปตามค่าเริ่มต้น
- **2.3**: คอลเลกชั่น`if`/`for`ตัวดำเนินการสเปรด — เหมาะสำหรับแผนผังวิดเจ็ต Flutter
- **2.6**: วิธีการขยาย
- **2.10**: ความปลอดภัยเป็นโมฆะ (เลือกใช้)
- **2.12**: **ความปลอดภัยแบบ Null เปิดใช้งานตามค่าเริ่มต้น** — ประเภท`?`ที่เป็นโมฆะ
- **2.17**: พารามิเตอร์ขั้นสูง (`super.x`) การแจงนับที่ปรับปรุงแล้ว
### Dart 3.x — บันทึกและรูปแบบ (2023–ปัจจุบัน)
- **3.0 (2023)**: **บันทึก** (ผู้ให้บริการข้อมูลที่ไม่ระบุชื่อ), **รูปแบบ** (การทำลายล้าง), **ตัวดัดแปลงคลาส** (`sealed`,`final`,`interface`,`base`), นิพจน์ `switch`
- **3.3 (2024)**: ประเภทส่วนขยาย (Wrapper ที่ไม่มีต้นทุน)
- **3.5 (2024)**: การแสดงตัวอย่างมาโคร — การเขียนโปรแกรมเมตาเวลาคอมไพล์
## วิวัฒนาการไวยากรณ์
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

## ประเภทวิวัฒนาการของระบบ
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

## หลักการออกแบบที่สำคัญ
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## การเติบโตของระบบนิเวศ
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
