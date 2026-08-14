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
# Dart – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 1,0 | 2013 | Erstveröffentlichung (Google, Lars Bak & Kasper Lund) |
| 1.2 | 2014 | Verbesserungen des Dart2JS-Compilers |
| 1,3 | 2014 | `async`/ `await`-Unterstützung |
| 1,4 | 2014 | `enum`, Mixins-Verbesserungen |
| 1,5 | 2014 | Generatoren (`sync*`,`async*`) |
| 1,6 | 2014 | `Future`Verbesserungen |
| 1,8 | 2014 | `dart:io`Verbesserungen |
| 1,9 | 2015 | Starker Modus (Opt-in) |
| 1.11 | 2015 | `Future.then`Verbesserungen |
| 1.12 | 2015 | **Stranger Modus** erzwungen |
| 2,0 | 2018 | **Major**: Soundtypsystem,`null`Sicherheitsvorbereitung, Neufassung der Sammlungen |
| 2.1 | 2018 | `int`/`double`Vereinheitlichung,`await for`|
| 2.2 | 2019 |  `Set`-Literal, Verbesserungen der `const`-Sammlung |
| 2.3 | 2019 | Sammlung `if`, Sammlung `for`, Spread-Operator`...`|
| 2,6 | 2019 | Erweiterungsmethoden |
| 2,7 | 2020 | Standardmäßig benannte Parameter |
| 2.10 | 2020 | **Keine sichere Sicherheit** (Opt-in) |
| 2.12 | 2021 | **Nullsicherheit standardmäßig aktiviert** |
| 2.13 | 2021 | Konstruktor-Abrisse |
| 2.14 | 2021 | `late`Verbesserungen, vorzeichenlose Ganzzahlen |
| 2,15 | 2021 | Konstruktor reißt stabile, generische Funktionstypen ab |
| 2.17 | 2022 | **Super-Parameter**, erweiterte Aufzählungen |
| 2,18 | 2022 | Erweiterte Typinferenz |
| 2,19 | 2023 | Datensätze und Muster (Vorschau) |
| 3,0 | 2023 | **Major**: Datensätze, Muster, Klassenmodifikatoren, `switch`-Ausdrücke |
| 3.1 | 2023 | Musterverbesserungen, versiegelte Klassen |
| 3.2 | 2023 | Verbesserungen der statischen Analyse |
| 3.3 | 2024 | Erweiterungstypen, `switch`-Ausdrucksverbesserungen |
| 3,4 | 2024 |  `if`-Elemente, `case`-Verbesserungen |
| 3,5 | 2024 | Makros (Vorschau), weitere Sprachverfeinerungen |
| 3,6 | 2025 | Kontinuierliche Entwicklung |
## Wichtige Meilensteine
### Dart 1.x – Die frühen Jahre (2013–2017)
- **2013**: Google veröffentlicht Dart – entwickelt für strukturierte Webprogrammierung
- **Ziel**: JavaScript für die Webentwicklung ersetzen (Ambition später geändert)
- **1.0**: Klassen, Schnittstellen, Isolate, optionale Typisierung
- **1.3**:`async`/ `await`-Unterstützung
- **1.9**: Starker Modus (Opt-in, strikte Eingabe)
– Dart VM wurde kurz in Chromium verwendet und dann entfernt
### Der Flutter Pivot (2017–2018)
- **2017**: Flutter-Framework angekündigt – Dart wird zur UI-Sprache
- Dart findet seinen Zweck: plattformübergreifende Mobil-/Desktop-/Webentwicklung
- **2.0 (2018)**: Vollständige Neufassung – Soundtypensystem, moderne Sammlungen
### Dart 2.x – Modern Dart (2018–2023)
- **2.0**: Soundtypsystem, standardmäßig nicht mehr `dynamic`
- **2.3**: Sammlung`if`/ `for`, Spread-Operator – ideal für Flutter-Widget-Bäume
- **2.6**: Erweiterungsmethoden
- **2.10**: Solide Null-Sicherheit (Opt-in)
- **2.12**: **Nullsicherheit standardmäßig aktiviert** –`?`nullfähige Typen
- **2.17**: Super-Parameter (`super.x`), erweiterte Aufzählungen
### Dart 3.x – Aufzeichnungen und Muster (2023–heute)
- **3.0 (2023)**: **Datensätze** (anonyme Datenträger), **Muster** (Destrukturierung), **Klassenmodifikatoren** ( `sealed`, `final`, `interface`, `base`), `switch`-Ausdrücke
- **3.3 (2024)**: Erweiterungstypen (kostenlose Wrapper)
- **3.5 (2024)**: Makrovorschau – Metaprogrammierung zur Kompilierungszeit
## Syntaxentwicklung
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

## Typsystementwicklung
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

## Wichtige Designprinzipien
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Ökosystemwachstum
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
