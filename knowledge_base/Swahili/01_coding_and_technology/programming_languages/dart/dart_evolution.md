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
# Dart - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| 1.0 | 2013 | Toleo la kwanza (Google, Lars Bak & Kasper Lund) |
| 1.2 | 2014 | Maboresho ya mkusanyaji wa Dart2JS |
| 1.3 | 2014 | `async`/`await`msaada |
| 1.4 | 2014 | `enum`, uboreshaji wa mchanganyiko |
| 1.5 | 2014 | Jenereta (`sync*`,`async*`) |
| 1.6 | 2014 |  Maboresho ya`Future`|
| 1.8 | 2014 |  Maboresho ya`dart:io`|
| 1.9 | 2015 | Hali thabiti (chagua kuingia) |
| 1.11 | 2015 |  Maboresho ya`Future.then`|
| 1.12 | 2015 | **Hali thabiti** imetekelezwa |
| 2.0 | 2018 | **Kubwa**: Mfumo wa aina ya sauti, maandalizi ya usalama ya `null`, andika upya mikusanyiko |
| 2.1 | 2018 | `int`/`double`muungano,`await for`|
| 2.2 | 2019 |  Maboresho ya mkusanyiko wa`Set`halisi,`const`|
| 2.3 | 2019 | Mkusanyiko`if`, mkusanyiko`for`, mtoa huduma wa kueneza`...`|
| 2.6 | 2019 | Mbinu za upanuzi |
| 2.7 | 2020 | Vigezo chaguomsingi vilivyopewa majina |
| 2.10 | 2020 | **Usalama usio na sauti** (chagua kuingia) |
| 2.12 | 2021 | **Usalama batili umewezeshwa kwa chaguomsingi** |
| 2.13 | 2021 | Kurarua kwa wajenzi |
| 2.14 | 2021 |  Maboresho ya `late`, nambari kamili ambazo hazijasainiwa |
| 2.15 | 2021 | Maboresho ya wajenzi thabiti, aina za utendakazi generic |
| 2.17 | 2022 | **Vigezo bora**, enum zilizoimarishwa |
| 2.18 | 2022 | Maelekezo ya aina iliyoimarishwa |
| 2.19 | 2023 | Rekodi na mifumo (hakiki) |
| 3.0 | 2023 | **Kubwa**: Rekodi, ruwaza, virekebishaji vya darasa, misemo ya`switch`|
| 3.1 | 2023 | Maboresho ya muundo, madarasa yaliyofungwa |
| 3.2 | 2023 | Maboresho ya uchanganuzi tuli |
| 3.3 | 2024 | Aina za viendelezi, uboreshaji wa usemi wa`switch`|
| 3.4 | 2024 |  Vipengele vya `if`, maboresho ya`case`|
| 3.5 | 2024 | Macros (hakiki), uboreshaji zaidi wa lugha |
| 3.6 | 2025 | Maendeleo yanayoendelea |
## Mafanikio Makuu
### Dart 1.x — Miaka ya Mapema (2013–2017)
- **2013**: Google inatoa Dart - iliyoundwa kwa ajili ya upangaji programu wa wavuti
- **Lengo**: Badilisha JavaScript kwa ukuzaji wa wavuti (matamanio baadaye yalipimwa)
- **1.0**: Madarasa, miingiliano, kutenganisha, kuandika kwa hiari
- **1.3**: Msaada wa`async`/ `await`
- **1.9**: Hali dhabiti (chagua kuandika kwa ukali)
- Dart VM kutumika katika Chromium kwa muda mfupi, kisha kuondolewa
### The Flutter Pivot (2017–2018)
- **2017**: Mfumo wa Flutter umetangazwa - Dart inakuwa lugha ya UI
- Dart hupata madhumuni yake: maendeleo ya jukwaa la rununu/desktop/wavuti
- **2.0 (2018)**: Kamilisha kuandika upya - mfumo wa aina ya sauti, makusanyo ya kisasa
### Dart 2.x — Dart ya Kisasa (2018–2023)
- **2.0**: Mfumo wa aina ya sauti, hakuna`dynamic`zaidi kwa chaguo-msingi
- **2.3**: Mkusanyiko`if`/`for`, mwendeshaji wa kueneza — mzuri kwa miti ya wijeti ya Flutter
- **2.6**: Mbinu za upanuzi
- **2.10**: Usalama batili wa sauti (chagua kuingia)
- **2.12**: **Usalama batili umewezeshwa kwa chaguomsingi** —`?`aina zisizoweza kubatilishwa
- **2.17**: Vigezo bora (`super.x`), enum zilizoimarishwa
### Dart 3.x — Rekodi na Miundo (2023–sasa)
- **3.0 (2023)**: **Rekodi** (wabebaji wa data wasiojulikana), **mifumo** (uharibifu), **marekebisho ya darasa** (`sealed`,`final`,`interface`, XQZMARKER3QZQZMARKs kujieleza),
- **3.3 (2024)**: Aina za viendelezi (karatasi zisizogharimu sifuri)
- **3.5 (2024)**: Onyesho la kuchungulia la Macros - upangaji wa wakati wa kukusanya
## Mageuzi ya Sintaksia
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

## Aina ya Mageuzi ya Mfumo
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

## Kanuni Muhimu za Usanifu
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Ukuaji wa Mfumo ikolojia
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
