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
# Dart — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| 1.0 | 2013 | Paunang release (Google, Lars Bak & Kasper Lund) |
| 1.2 | 2014 | Mga pagpapabuti ng Dart2JS compiler |
| 1.3 | 2014 | `async`/`await`suporta |
| 1.4 | 2014 | `enum`, pinagsasama ang mga pagpapabuti |
| 1.5 | 2014 | Mga Generator (`sync*`,`async*`) |
| 1.6 | 2014 | `Future`mga pagpapabuti |
| 1.8 | 2014 | `dart:io`mga pagpapabuti |
| 1.9 | 2015 | Malakas na mode (opt-in) |
| 1.11 | 2015 | `Future.then`mga pagpapabuti |
| 1.12 | 2015 | **Strong mode** ipinatupad |
| 2.0 | 2018 | **Major**: Sound type system,`null`safety prep, collections rewrite |
| 2.1 | 2018 | `int`/`double`pag-iisa,`await for`|
| 2.2 | 2019 | `Set`literal,`const`mga pagpapabuti sa koleksyon |
| 2.3 | 2019 | Collection`if`, koleksyon`for`, spread operator`...`|
| 2.6 | 2019 | Mga paraan ng extension |
| 2.7 | 2020 | Default na pinangalanang mga parameter |
| 2.10 | 2020 | **Sound null safety** (opt-in) |
| 2.12 | 2021 | **Null na kaligtasan ay pinagana bilang default** |
| 2.13 | 2021 | Mga tear-off ng konstruktor |
| 2.14 | 2021 | `late`mga pagpapabuti, unsigned integer |
| 2.15 | 2021 | Matatag ang mga tear-off ng konstruktor, mga generic na uri ng function |
| 2.17 | 2022 | **Mga super parameter**, mga pinahusay na enum |
| 2.18 | 2022 | Pinahusay na uri ng hinuha |
| 2.19 | 2023 | Mga tala at pattern (preview) |
| 3.0 | 2023 | **Major**: Mga tala, pattern, modifier ng klase,`switch`expression |
| 3.1 | 2023 | Mga pagpapabuti ng pattern, mga selyadong klase |
| 3.2 | 2023 | Mga pagpapabuti ng static na pagsusuri |
| 3.3 | 2024 | Mga uri ng extension,`switch`mga pagpapabuti ng expression |
| 3.4 | 2024 | `if`elemento,`case`mga pagpapabuti |
| 3.5 | 2024 | Macros (preview), karagdagang mga pagpipino ng wika |
| 3.6 | 2025 | Patuloy na pag-unlad |
## Mga Pangunahing Milestone
### Dart 1.x — The Early Years (2013–2017)
- **2013**: Inilabas ng Google ang Dart — dinisenyo para sa structured web programming
- **Layunin**: Palitan ang JavaScript para sa web development (na-pivote ang ambisyon sa ibang pagkakataon)
- **1.0**: Mga klase, interface, isolates, opsyonal na pag-type
- **1.3**: Suporta sa`async`/ `await`
- **1.9**: Strong mode (mahigpit na pag-type)
- Saglit na ginamit ang Dart VM sa Chromium, pagkatapos ay inalis
### The Flutter Pivot (2017–2018)
- **2017**: Inanunsyo ang Flutter framework — Nagiging UI language ang Dart
- Hinahanap ng Dart ang layunin nito: cross-platform na mobile/desktop/web development
- **2.0 (2018)**: Kumpletuhin ang muling pagsulat — sound type system, mga modernong koleksyon
### Dart 2.x — Modern Dart (2018–2023)
- **2.0**: Sound type system, wala nang`dynamic`bilang default
- **2.3**: Collection`if`/`for`, spread operator — mahusay para sa Flutter widget tree
- **2.6**: Mga paraan ng extension
- **2.10**: Sound null safety (opt-in)
- **2.12**: **Null na kaligtasan ay pinagana bilang default** —`?`na mga nullable na uri
- **2.17**: Mga sobrang parameter (`super.x`), mga pinahusay na enum
### Dart 3.x — Mga Tala at Pattern (2023–kasalukuyan)
- **3.0 (2023)**: **Records** (anonymous data carriers), **patterns** (destructuring), **class modifiers** (`sealed`,`final`,`interface`,`base`),`switch`expression
- **3.3 (2024)**: Mga uri ng extension (zero-cost wrapper)
- **3.5 (2024)**: Macros preview — compile-time na metaprogramming
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

## Uri ng System Evolution
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Paglago ng Ecosystem
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
