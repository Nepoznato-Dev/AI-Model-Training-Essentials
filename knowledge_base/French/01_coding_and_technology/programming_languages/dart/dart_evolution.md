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

# Dart — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| 1.0 | 2013 | Version initiale (Google, Lars Bak et Kasper Lund) |
| 1.2 | 2014 | Améliorations du compilateur Dart2JS |
| 1.3 | 2014 |  Prise en charge`async`/`await`|
| 1.4 | 2014 | `enum`, améliorations des mixins |
| 1.5 | 2014 | Générateurs (`sync*`,`async*`) |
| 1.6 | 2014 |  Améliorations`Future`|
| 1.8 | 2014 |  Améliorations`dart:io`|
| 1.9 | 2015 | Mode fort (opt-in) |
| 1.11 | 2015 |  Améliorations`Future.then`|
| 1.12 | 2015 | **Mode fort** appliqué |
| 2.0 | 2018 | **Majeur** : Système de type sonore, préparation de sécurité `null`, réécriture des collections |
| 2.1 | 2018 |  Unification`int`/ `double`,`await for`|
| 2.2 | 2019 |  Littéral `Set`, améliorations de la collection`const`|
| 2.3 | 2019 | Collection`if`, collection`for`, opérateur d'épandage`...`|
| 2.6 | 2019 | Méthodes d'extension |
| 2.7 | 2020 | Paramètres nommés par défaut |
| 2.10 | 2020 | **Sécurité sonore nulle** (opt-in) |
| 2.12 | 2021 | **Sécurité nulle activée par défaut** |
| 2.13 | 2021 | Détachements constructeur |
| 2.14 | 2021 |  Améliorations `late`, entiers non signés |
| 2.15 | 2021 | Le constructeur supprime les types de fonctions stables et génériques |
| 2.17 | 2022 | **Super paramètres**, énumérations améliorées |
| 2.18 | 2022 | Inférence de type améliorée |
| 2.19 | 2023 | Enregistrements et modèles (aperçu) |
| 3.0 | 2023 | **Majeur** : enregistrements, modèles, modificateurs de classe, expressions`switch`|
| 3.1 | 2023 | Améliorations des modèles, classes scellées |
| 3.2 | 2023 | Améliorations de l'analyse statique |
| 3.3 | 2024 | Types d'extensions, améliorations des expressions`switch`|
| 3.4 | 2024 |  Éléments `if`, améliorations`case`|
| 3.5 | 2024 | Macros (aperçu), autres améliorations du langage |
| 3.6 | 2025 | Développement en cours |
## Étapes majeures
### Dart 1.x — Les premières années (2013-2017)
- **2013** : Google lance Dart, conçu pour la programmation Web structurée.
- **Objectif** : Remplacer JavaScript pour le développement Web (l'ambition a ensuite changé)
- **1.0** : Classes, interfaces, isolats, typage optionnel
- **1.3** : prise en charge de`async`/ `await`
- **1.9** : mode fort (saisie stricte opt-in)
- Dart VM utilisée brièvement dans Chromium, puis supprimée
### Le pivot Flutter (2017-2018)
- **2017** : Annonce du framework Flutter — Dart devient le langage de l'interface utilisateur
- Dart trouve sa vocation : développement multiplateforme mobile/ordinateur de bureau/web
- **2.0 (2018)** : Réécriture complète — système de type sonore, collections modernes
### Dart 2.x — Dart moderne (2018-2023)
- **2.0** : Système de type son, plus de`dynamic`par défaut
- **2.3** : Collection`if`/`for`, opérateur de diffusion — idéal pour les arbres de widgets Flutter
- **2.6** : Méthodes d'extension
- **2.10** : Sécurité sonore nulle (opt-in)
- **2.12** : **Sécurité nulle activée par défaut** — Types nullables `?`
- **2.17** : Super paramètres (`super.x`), énumérations améliorées
### Dart 3.x — Enregistrements et modèles (2023-présent)
- **3.0 (2023)** : **Enregistrements** (supports de données anonymes), **modèles** (déstructuration), **modificateurs de classe** (`sealed`,`final`,`interface`,`base`), expressions `switch`
- **3.3 (2024)** : types d'extensions (wrappers à coût nul)
- **3.5 (2024)** : Aperçu des macros — métaprogrammation au moment de la compilation
## Évolution de la syntaxe
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

## Évolution du système de types
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

## Principes de conception clés
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Croissance de l'écosystème
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
