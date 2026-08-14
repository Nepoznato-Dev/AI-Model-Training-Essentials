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

# Dart - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| 1.0 | 2013 | Lanzamiento inicial (Google, Lars Bak y Kasper Lund) |
| 1.2 | 2014 | Mejoras en el compilador Dart2JS |
| 1.3 | 2014 |  Soporte`async`/`await`|
| 1.4 | 2014 |  `enum`, mejoras en los mixins |
| 1.5 | 2014 | Generadores (`sync*`, `async*`) |
| 1.6 | 2014 |  Mejoras`Future`|
| 1.8 | 2014 |  Mejoras`dart:io`|
| 1.9 | 2015 | Modo fuerte (optar por participar) |
| 1.11 | 2015 |  Mejoras`Future.then`|
| 1.12 | 2015 | **Modo fuerte** aplicado |
| 2.0 | 2018 | **Principal**: Sistema de tipo de sonido, preparación de seguridad `null`, reescritura de colecciones |
| 2.1 | 2018 |  Unificación`int`/ `double`,`await for`|
| 2.2 | 2019 | `Set`literal, mejoras en la colección`const`|
| 2.3 | 2019 | Colección `if`, colección `for`, operador de extensión`...`|
| 2.6 | 2019 | Métodos de extensión |
| 2.7 | 2020 | Parámetros con nombre predeterminados |
| 2.10 | 2020 | **Sonido nulo de seguridad** (optar por participar) |
| 2.12 | 2021 | **Seguridad nula habilitada de forma predeterminada** |
| 2.13 | 2021 | Arranques de constructores |
| 2.14 | 2021 |  Mejoras `late`, enteros sin signo |
| 2.15 | 2021 | Constructor separa tipos de funciones genéricas y estables |
| 2.17 | 2022 | **Superparámetros**, enumeraciones mejoradas |
| 2.18 | 2022 | Inferencia de tipos mejorada |
| 2.19 | 2023 | Registros y patrones (vista previa) |
| 3.0 | 2023 | **Principal**: Registros, patrones, modificadores de clase, expresiones`switch`|
| 3.1 | 2023 | Mejoras de patrones, clases selladas |
| 3.2 | 2023 | Mejoras en el análisis estático |
| 3.3 | 2024 | Tipos de extensión, mejoras en la expresión`switch`|
| 3.4 | 2024 |  Elementos `if`, mejoras`case`|
| 3.5 | 2024 | Macros (vista previa), mayores mejoras del idioma |
| 3.6 | 2025 | Desarrollo continuo |
## Hitos importantes
### Dart 1.x - Los primeros años (2013-2017)
- **2013**: Google lanza Dart, diseñado para programación web estructurada.
- **Objetivo**: Reemplazar JavaScript para el desarrollo web (la ambición luego cambió)
- **1.0**: clases, interfaces, aislamientos, escritura opcional
- **1.3**: compatibilidad con`async`/ `await`
- **1.9**: Modo fuerte (optar escritura estricta)
- Dart VM se usó brevemente en Chromium y luego se eliminó
### El pivote del aleteo (2017-2018)
- **2017**: Se anuncia el marco Flutter: Dart se convierte en el lenguaje de interfaz de usuario
- Dart encuentra su propósito: desarrollo multiplataforma móvil/escritorio/web
- **2.0 (2018)**: reescritura completa: sistema de tipo de sonido, colecciones modernas
### Dart 2.x — Dardo moderno (2018-2023)
- **2.0**: Sistema de tipo de sonido, no más`dynamic`por defecto
- **2.3**: Colección`if`/ `for`, operador de extensión: ideal para árboles de widgets de Flutter
- **2.6**: Métodos de extensión
- **2.10**: Seguridad nula de sonido (optar por participar)
- **2.12**: **Seguridad nula habilitada de forma predeterminada** — Tipos anulables `?`
- **2.17**: Superparámetros (`super.x`), enumeraciones mejoradas
### Dart 3.x: Registros y patrones (2023-presente)
- **3.0 (2023)**: **Registros** (soportes de datos anónimos), **patrones** (desestructuración), **modificadores de clase** (`sealed`,`final`,`interface`,`base`), expresiones `switch`
- **3.3 (2024)**: Tipos de extensión (envoltorios de costo cero)
- **3.5 (2024)**: Vista previa de macros: metaprogramación en tiempo de compilación
## Evolución de la sintaxis
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

## Evolución del sistema tipo
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

## Principios clave de diseño
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Crecimiento del ecosistema
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
