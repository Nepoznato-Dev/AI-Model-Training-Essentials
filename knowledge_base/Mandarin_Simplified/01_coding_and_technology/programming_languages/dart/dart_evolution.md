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
# Dart — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| 1.0 | 2013 |初始版本（Google、Lars Bak 和 Kasper Lund）|
| 1.2 | 1.2 2014年| Dart2JS 编译器改进 |
| 1.3 | 1.3 2014年| `async`/`await`支持 |
| 1.4 | 1.4 2014年|  `enum`，mixin 改进 |
| 1.5 | 1.5 2014年|发电机（`sync*`、`async*`）|
| 1.6 | 1.6 2014年| `Future`改进 |
| 1.8 | 1.8 2014年| `dart:io`改进 |
| 1.9 | 1.9 2015 | 2015强模式（选择加入）|
| 1.11 | 1.11 2015 | 2015 `Future.then`改进 |
| 1.12 | 1.12 2015 | 2015 **强模式**强制执行 |
| 2.0 | 2018 | **专业**：声音类型系统、`null`安全准备、集合重写 |
| 2.1 | 2.1 2018 | `int`/`double`统一，`await for` |
| 2.2 | 2.2 2019 | 2019 `Set`文字、`const` 系列改进 |
| 2.3 | 2.3 2019 | 2019集合`if`、集合`for`、扩展运算符`...`|
| 2.6 | 2.6 2019 | 2019扩展方法 |
| 2.7 | 2.7 2020 |默认命名参数 |
| 2.10 | 2.10 2020 | **声音空安全**（选择加入）|
| 2.12 | 2.12 2021 | **默认启用空安全** |
| 2.13 | 2.13 2021 |构造函数撕裂 |
| 2.14 | 2.14 2021 | `late`改进，无符号整数 |
| 2.15 | 2.15 2021 |构造函数剥离稳定的通用函数类型 |
| 2.17 | 2.17 2022 | 2022 **超级参数**，增强枚举|
| 2.18 | 2.18 2022 | 2022增强型类型推断 |
| 2.19 | 2.19 2023 |记录和模式（预览）|
| 3.0 | 2023 | **主要**：记录、模式、类修饰符、`switch` 表达式 |
| 3.1| 2023 |模式改进，密封类|
| 3.2 | 2023 |静态分析改进 |
| 3.3 | 2024 | 2024扩展类型、`switch` 表达式改进 |
| 3.4 | 3.4 2024 | 2024 `if`元素、`case` 改进 |
| 3.5 | 3.5 2024 | 2024宏（预览），进一步的语言改进 |
| 3.6 | 2025 | 2025持续发展|
## 主要里程碑
### Dart 1.x — 早年（2013-2017）
- **2013**：Google 发布 Dart — 专为结构化 Web 编程而设计
- **目标**：取代 JavaScript 进行 Web 开发（后来的目标发生了变化）
- **1.0**：类、接口、隔离、可选类型
- **1.3**：`async` /`await`支持
- **1.9**：强模式（选择严格输入）
- Dart VM 在 Chromium 中短暂使用，然后被删除
### Flutter 枢轴（2017–2018）
- **2017**：Flutter 框架宣布 — Dart 成为 UI 语言
- Dart 找到了它的目的：跨平台移动/桌面/Web 开发
- **2.0 (2018)**：完全重写 - 声音类型系统，现代集合
### Dart 2.x — 现代 Dart (2018–2023)
- **2.0**：声音类型系统，默认不再有`dynamic`
- **2.3**：集合`if`/`for`，扩展运算符 - 非常适合 Flutter 小部件树
- **2.6**：扩展方法
- **2.10**：声音无效安全（选择加入）
- **2.12**：**默认启用空安全** —`?`可空类型
- **2.17**：超级参数（`super.x`），增强枚举
### Dart 3.x — 记录和模式（2023 年至今）
- **3.0 (2023)**：**记录**（匿名数据载体）、**模式**（解构）、**类修饰符**（`sealed`、`final`、`interface`、`base`）、`switch` 表达式
- **3.3 (2024)**：扩展类型（零成本包装器）
- **3.5 (2024)**：宏预览 - 编译时元编程
## 语法演变
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

## 类型系统的演变
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

## 关键设计原则
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## 生态系统增长
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
