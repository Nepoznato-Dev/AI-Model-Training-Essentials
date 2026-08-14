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
# Dart — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| 1.0     | 2013 | Initial release (Google, Lars Bak & Kasper Lund) |
| 1.2     | 2014 | Dart2JS compiler improvements |
| 1.3     | 2014 | `async`/`await` support |
| 1.4     | 2014 | `enum`, mixins improvements |
| 1.5     | 2014 | Generators (`sync*`, `async*`) |
| 1.6     | 2014 | `Future` improvements |
| 1.8     | 2014 | `dart:io` improvements |
| 1.9     | 2015 | Strong mode (opt-in) |
| 1.11    | 2015 | `Future.then` improvements |
| 1.12    | 2015 | **Strong mode** enforced |
| 2.0     | 2018 | **Major**: Sound type system, `null` safety prep, collections rewrite |
| 2.1     | 2018 | `int`/`double` unification, `await for` |
| 2.2     | 2019 | `Set` literal, `const` collection improvements |
| 2.3     | 2019 | Collection `if`, collection `for`, spread operator `...` |
| 2.6     | 2019 | Extension methods |
| 2.7     | 2020 | Default named parameters |
| 2.10    | 2020 | **Sound null safety** (opt-in) |
| 2.12    | 2021 | **Null safety enabled by default** |
| 2.13    | 2021 | Constructor tear-offs |
| 2.14    | 2021 | `late` improvements, unsigned integers |
| 2.15    | 2021 | Constructor tear-offs stable, generic function types |
| 2.17    | 2022 | **Super parameters**, enhanced enums |
| 2.18    | 2022 | Enhanced type inference |
| 2.19    | 2023 | Records and patterns (preview) |
| 3.0     | 2023 | **Major**: Records, patterns, class modifiers, `switch` expressions |
| 3.1     | 2023 | Pattern improvements, sealed classes |
| 3.2     | 2023 | Static analysis improvements |
| 3.3     | 2024 | Extension types, `switch` expression improvements |
| 3.4     | 2024 | `if` elements, `case` improvements |
| 3.5     | 2024 | Macros (preview), further language refinements |
| 3.6     | 2025 | Ongoing development |

## Major Milestones

### Dart 1.x — The Early Years (2013–2017)
- **2013**: Google releases Dart — designed for structured web programming
- **Goal**: Replace JavaScript for web development (ambition later pivoted)
- **1.0**: Classes, interfaces, isolates, optional typing
- **1.3**: `async`/`await` support
- **1.9**: Strong mode (opt-in strict typing)
- Dart VM used in Chromium briefly, then removed

### The Flutter Pivot (2017–2018)
- **2017**: Flutter framework announced — Dart becomes the UI language
- Dart finds its purpose: cross-platform mobile/desktop/web development
- **2.0 (2018)**: Complete rewrite — sound type system, modern collections

### Dart 2.x — Modern Dart (2018–2023)
- **2.0**: Sound type system, no more `dynamic` by default
- **2.3**: Collection `if`/`for`, spread operator — great for Flutter widget trees
- **2.6**: Extension methods
- **2.10**: Sound null safety (opt-in)
- **2.12**: **Null safety enabled by default** — `?` nullable types
- **2.17**: Super parameters (`super.x`), enhanced enums

### Dart 3.x — Records & Patterns (2023–present)
- **3.0 (2023)**: **Records** (anonymous data carriers), **patterns** (destructuring), **class modifiers** (`sealed`, `final`, `interface`, `base`), `switch` expressions
- **3.3 (2024)**: Extension types (zero-cost wrappers)
- **3.5 (2024)**: Macros preview — compile-time metaprogramming

## Syntax Evolution

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

## Type System Evolution

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

## Key Design Principles

```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Ecosystem Growth

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
