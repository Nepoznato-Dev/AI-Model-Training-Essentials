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

# Dart — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 1,0 | 2013 | Pierwsza wersja (Google, Lars Bak i Kasper Lund) |
| 1.2 | 2014 | Ulepszenia kompilatora Dart2JS |
| 1.3 | 2014 |  Obsługa`async`/`await`|
| 1,4 | 2014 | `enum`, ulepszenia miksów |
| 1,5 | 2014 | Generatory (`sync*`,`async*`) |
| 1,6 | 2014 |  Ulepszenia`Future`|
| 1,8 | 2014 |  Ulepszenia`dart:io`|
| 1,9 | 2015 | Tryb silny (opcja) |
| 1.11 | 2015 |  Ulepszenia`Future.then`|
| 1.12 | 2015 | **Tryb silny** wymuszony |
| 2,0 | 2018 | **Główne**: System typu dźwięku, przygotowanie bezpieczeństwa `null`, przepisanie kolekcji |
| 2.1 | 2018 |  Ujednolicenie`int`/ `double`,`await for`|
| 2.2 | 2019 |  Dosłowny `Set`, ulepszenia kolekcji`const`|
| 2.3 | 2019 | Kolekcja`if`, kolekcja`for`, operator rozprzestrzeniania`...`|
| 2.6 | 2019 | Metody rozszerzania |
| 2.7 | 2020 | Domyślne nazwane parametry |
| 2.10 | 2020 | **Bezbronne bezpieczeństwo** (opcja) |
| 2.12 | 2021 | **Domyślnie włączone bezpieczeństwo zerowe** |
| 2.13 | 2021 | Odrywanie konstruktora |
| 2.14 | 2021 |  Ulepszenia `late`, liczby całkowite bez znaku |
| 2.15 | 2021 | Konstruktor oderwania stabilnych, ogólnych typów funkcji |
| 2.17 | 2022 | **Super parametry**, ulepszone wyliczenia |
| 2.18 | 2022 | Ulepszone wnioskowanie o typie |
| 2.19 | 2023 | Rekordy i wzorce (zapowiedź) |
| 3,0 | 2023 | **Główne**: Rekordy, wzorce, modyfikatory klas, wyrażenia`switch`|
| 3.1 | 2023 | Ulepszenia wzorców, zapieczętowane zajęcia |
| 3.2 | 2023 | Ulepszenia analizy statycznej |
| 3.3 | 2024 | Typy rozszerzeń, ulepszenia wyrażeń`switch`|
| 3.4 | 2024 |  Elementy `if`, ulepszenia`case`|
| 3,5 | 2024 | Makra (podgląd), dalsze udoskonalenia języka |
| 3,6 | 2025 | Ciągły rozwój |
## Główne kamienie milowe
### Dart 1.x — wczesne lata (2013–2017)
- **2013**: Google wypuszcza Dart — przeznaczony do programowania strukturalnego w Internecie
- **Cel**: Zamień JavaScript na potrzeby tworzenia stron internetowych (ambicje później zmieniono)
- **1.0**: Klasy, interfejsy, izolaty, opcjonalne typowanie
- **1.3**: obsługa`async`/ `await`
- **1.9**: Tryb silny (zgoda na ścisłe pisanie)
- Dart VM używany krótko w Chromium, a następnie usunięty
### Flutter Pivot (2017–2018)
- **2017**: Ogłoszono framework Flutter — Dart staje się językiem interfejsu użytkownika
- Dart znajduje swój cel: tworzenie aplikacji mobilnych/komputerów stacjonarnych/internetowych na wielu platformach
- **2.0 (2018)**: Całkowite przepisanie — system typów dźwięku, nowoczesne kolekcje
### Dart 2.x — Modern Dart (2018–2023)
- **2.0**: System typu dźwięku, domyślnie nie ma już `dynamic`
- **2.3**: Kolekcja`if`/`for`, operator rozprzestrzeniania — świetny dla drzew widżetów Flutter
- **2.6**: Metody rozszerzające
- **2.10**: Bezpieczeństwo zerowe (opcja)
- **2.12**: **Bezpieczeństwo zerowe włączone domyślnie** — Typy zerowe `?`
- **2.17**: Super parametry (`super.x`), ulepszone wyliczenia
### Dart 3.x — rekordy i wzory (2023 – obecnie)
- **3.0 (2023)**: **Rekordy** (anonimowe nośniki danych), **wzorce** (destrukturyzacja), **modyfikatory klas** (`sealed`,`final`,`interface`,`base`),`switch`wyrażenia
- **3.3 (2024)**: Typy rozszerzeń (opakowania o zerowym koszcie)
- **3.5 (2024)**: Podgląd makr — metaprogramowanie w czasie kompilacji
## Ewolucja składni
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

## Wpisz ewolucję systemu
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

## Kluczowe zasady projektowania
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Rozwój ekosystemu
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
