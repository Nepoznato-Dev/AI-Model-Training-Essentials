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
# Dart — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 1.0 | 2013 |初始版本（Google、Lars Bak 和 Kasper Lund）|
| 1.2 | 1.2 2014 | Dart2JS 編譯器改進 |
| 1.3 | 1.3 2014年|`async`/`await`支援 |
| 1.4 | 1.4 2014 | `enum`，mixin 改進 |
| 1.5 | 1.5 2014年|發電機（`sync*`、`async*`）|
| 1.6 | 1.6 2014年|`Future`改進 |
| 1.8 | 1.8 2014年|`dart:io`改進 |
| 1.9 | 1.9 2015 | 2015強模式（選擇加入）|
| 1.11 | 1.11 2015 | 2015`Future.then`改進 |
| 1.12 | 1.12 2015 | 2015 **強模式**強制執行 |
| 2.0 | 2018 | **專業**：聲音類型系統、`null`安全準備、集合重寫 |
| 2.1 | 2.1 2018 |`int`/`double`統一，`await for` |
| 2.2 | 2.2 2019 | 2019`Set`文字、`const` 系列改進 |
| 2.3 | 2.3 2019 | 2019集合`if`、集合`for`、擴充運算子`...`|
| 2.6 | 2.6 2019 | 2019擴展方法 |
| 2.7 | 2.7 2020 |預設命名參數 |
| 2.10 | 2.10 2020 | **聲音空安全**（選擇加入）|
| 2.12 | 2.12 2021 | **預設啟用空安全** |
| 2.13 | 2.13 2021 |構造函數撕裂 |
| 2.14 | 2.14 2021 |`late`改進，無符號整數 |
| 2.15 | 2.15 2021 |建構子剝離穩定的通用函數型別 |
| 2.17 | 2.17 2022 | 2022 **超級參數**，增強枚舉|
| 2.18 | 2.18 2022 | 2022增強型類型推論 |
| 2.19 | 2.19 2023 |記錄與模式（預覽）|
| 3.0 | 2023 | **主要**：記錄、模式、類別修飾符、`switch` 表達式 |
| 3.1| 2023 |模式改進，密封類別|
| 3.2 | 2023 |靜態分析改進 |
| 3.3 | 2024 | 2024擴充型別、`switch` 表達式改進 |
| 3.4 | 3.4 2024 | 2024`if`元素、`case` 改進 |
| 3.5 | 3.5 2024 | 2024宏（預覽），進一步的語言改進 |
| 3.6 | 2025 | 2025持續發展|
## 主要里程碑
### Dart 1.x — 早年（2013-2017）
- **2013**：Google 發佈 Dart — 專為結構化 Web 程式設計
- **目標**：取代 JavaScript 進行 Web 開發（後來的目標改變了）
- **1.0**：類別、介面、隔離、選用類型
- **1.3**：`async` /`await`支持
- **1.9**：強模式（選擇嚴格輸入）
- Dart VM 在 Chromium 中短暫使用，然後被刪除
### Flutter 樞軸（2017–2018）
- **2017**：Flutter 框架宣告 — Dart 成為 UI 語言
- Dart 找到了它的目的：跨平台行動/桌面/Web 開發
- **2.0 (2018)**：完全重寫 - 聲音類型系統，現代集合
### Dart 2.x — 現代 Dart (2018–2023)
- **2.0**：聲音類型系統，預設不再有`dynamic`
- **2.3**：集合`if`/`for`，擴展運算子 - 非常適合 Flutter 小部件樹
- **2.6**：擴充方法
- **2.10**：聲音無效安全（選擇加入）
- **2.12**：**預設啟用空安全** —`?`可空類型
- **2.17**：超級參數（`super.x`），增強枚舉
### Dart 3.x — 記錄與模式（2023 年至今）
- **3.0 (2023)**：**記錄**（匿名資料載體）、**模式**（解構）、**類別修飾符**（`sealed`、`final`、`interface`、 `base`）、XQZMARKER4XZ 表達式
- **3.3 (2024)**：擴充類型（零成本包裝器）
- **3.5 (2024)**：巨集預覽 - 編譯時元編程
## 語法演變
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

## 類型系統的演變
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

## 關鍵設計原則
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## 生態系成長
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
