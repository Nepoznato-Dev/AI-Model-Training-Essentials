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
# Dart: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 2013| Versione iniziale (Google, Lars Bak e Kasper Lund) |
| 1.2 | 2014| Miglioramenti al compilatore Dart2JS |
| 1.3 | 2014|  Supporto`async`/`await`|
| 1.4 | 2014| `enum`, miglioramenti ai mixin |
| 1,5 | 2014| Generatori (`sync*`,`async*`) |
| 1.6 | 2014| `Future`miglioramenti |
| 1.8 | 2014| `dart:io`miglioramenti |
| 1.9 | 2015| Modalità forte (attivazione) |
| 1.11 | 2015| `Future.then`miglioramenti |
| 1.12 | 2015| **Modalità forte** applicata |
| 2.0 | 2018 | **Maggiore**: sistema di tipo audio, preparazione alla sicurezza `null`, riscrittura delle collezioni |
| 2.1 | 2018 |  Unificazione`int`/ `double`,`await for`|
| 2.2 | 2019 | `Set`letterale, miglioramenti della raccolta`const`|
| 2.3 | 2019 | Collezione`if`, collezione`for`, operatore diffusione`...`|
| 2.6 | 2019 | Metodi di estensione |
| 2.7 | 2020 | Parametri con nome predefinito |
| 2.10| 2020 | **Sicurezza nulla** (attivazione) |
| 2.12 | 2021 | **Sicurezza nulla abilitata per impostazione predefinita** |
| 2.13 | 2021 | Strappi del costruttore |
| 2.14 | 2021 |  Miglioramenti `late`, interi senza segno |
| 2.15| 2021 | Il costruttore separa tipi di funzioni generiche e stabili |
| 2.17 | 2022 | **Super parametri**, enumerazioni migliorate |
| 2.18 | 2022 | Inferenza di tipo migliorata |
| 2.19 | 2023 | Record e modelli (anteprima) |
| 3.0 | 2023 | **Maggiore**: record, modelli, modificatori di classe, espressioni`switch`|
| 3.1 | 2023 | Miglioramenti del modello, classi sigillate |
| 3.2 | 2023 | Miglioramenti dell'analisi statica |
| 3.3 | 2024 | Tipi di estensione, miglioramenti dell'espressione`switch`|
| 3.4 | 2024 |  Elementi `if`, miglioramenti`case`|
| 3,5 | 2024 | Macro (anteprima), ulteriori perfezionamenti linguistici |
| 3.6 | 2025 | Sviluppo continuo |
## Traguardi importanti
### Dart 1.x - I primi anni (2013-2017)
- **2013**: Google rilascia Dart, progettato per la programmazione web strutturata
- **Obiettivo**: sostituire JavaScript per lo sviluppo web (ambizione successivamente modificata)
- **1.0**: classi, interfacce, isolati, tipizzazione opzionale
- **1.3**: supporto`async`/ `await`
- **1.9**: modalità forte (attivazione della digitazione rigorosa)
- Dart VM utilizzata brevemente in Chromium, quindi rimossa
### Il perno del flutter (2017-2018)
- **2017**: annunciato il framework Flutter: Dart diventa il linguaggio dell'interfaccia utente
- Dart trova il suo scopo: sviluppo mobile/desktop/web multipiattaforma
- **2.0 (2018)**: riscrittura completa: sistema di tipi di suono, collezioni moderne
### Dart 2.x — Freccetta moderna (2018-2023)
- **2.0**: sistema di tipo audio, non più`dynamic`per impostazione predefinita
- **2.3**: Raccolta`if`/ `for`, operatore di diffusione: ottimo per gli alberi dei widget Flutter
- **2.6**: Metodi di estensione
- **2.10**: Sicurezza audio nulla (attivazione)
- **2.12**: **Sicurezza nulla abilitata per impostazione predefinita** — Tipi nullable `?`
- **2.17**: Super parametri (`super.x`), enumerazioni migliorate
### Dart 3.x: record e modelli (2023-oggi)
- **3.0 (2023)**: **Record** (supporti dati anonimi), **modelli** (destrutturazione), **modificatori di classe** (`sealed`,`final`,`interface`,`base`), espressioni `switch`
- **3.3 (2024)**: Tipi di estensioni (wrapper a costo zero)
- **3.5 (2024)**: anteprima delle macro: metaprogrammazione in fase di compilazione
## Evoluzione della sintassi
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

## Digitare Evoluzione del sistema
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

## Principi chiave di progettazione
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Crescita dell'ecosistema
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
