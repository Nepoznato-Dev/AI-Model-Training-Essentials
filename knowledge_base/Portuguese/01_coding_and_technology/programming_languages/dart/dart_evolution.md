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

# Dart – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 2013 | Lançamento inicial (Google, Lars Bak e Kasper Lund) |
| 1.2 | 2014 | Melhorias no compilador Dart2JS |
| 1.3 | 2014 |  Suporte `async`/`await` |
| 1.4 | 2014 | `enum`, melhorias nos mixins |
| 1,5 | 2014 | Geradores (`sync*`, `async*`) |
| 1.6 | 2014 |  Melhorias`Future`|
| 1.8 | 2014 |  Melhorias`dart:io`|
| 1,9 | 2015 | Modo forte (opt-in) |
| 1.11 | 2015 |  Melhorias`Future.then`|
| 1.12 | 2015 | **Modo forte** aplicado |
| 2.0 | 2018 | **Principal**: Sistema de tipo de som, preparação de segurança `null`, reescrita de coleções |
| 2.1 | 2018 |  Unificação`int`/ `double`,`await for`|
| 2.2 | 2019 |  Literal `Set`, melhorias na coleção`const`|
| 2.3 | 2019 | Coleção`if`, coleção`for`, operador de spread`...`|
| 2.6 | 2019 | Métodos de extensão |
| 2.7 | 2020 | Parâmetros nomeados padrão |
| 2.10 | 2020 | **Som de segurança nula** (opt-in) |
| 2.12 | 2021 | **Segurança nula habilitada por padrão** |
| 2.13 | 2021 | Destacamento do construtor |
| 2.14 | 2021 |  Melhorias em `late`, inteiros sem sinal |
| 2.15 | 2021 | Construtor separa tipos de funções genéricos e estáveis ​​|
| 2.17 | 2022 | **Superparâmetros**, enumerações aprimoradas |
| 2.18 | 2022 | Inferência de tipo aprimorada |
| 2.19 | 2023 | Registros e padrões (visualização) |
| 3.0 | 2023 | **Principal**: Registros, padrões, modificadores de classe, expressões`switch`|
| 3.1 | 2023 | Melhorias de padrão, classes seladas |
| 3.2 | 2023 | Melhorias na análise estática |
| 3.3 | 2024 | Tipos de extensão, melhorias na expressão`switch`|
| 3.4 | 2024 |  Elementos `if`, melhorias`case`|
| 3.5 | 2024 | Macros (pré-visualização), mais refinamentos de linguagem |
| 3.6 | 2025 | Desenvolvimento contínuo |
## Marcos importantes
### Dart 1.x – Os primeiros anos (2013–2017)
- **2013**: Google lança Dart — projetado para programação web estruturada
- **Objetivo**: Substituir JavaScript pelo desenvolvimento web (ambição posteriormente dinamizada)
- **1.0**: Classes, interfaces, isolados, digitação opcional
- **1.3**: suporte `async`/`await`
- **1.9**: Modo forte (digitação estrita opcional)
- Dart VM usado brevemente no Chromium e depois removido
### O pivô flutuante (2017–2018)
- **2017**: Anunciado o framework Flutter — Dart se torna a linguagem de UI
- Dart encontra seu propósito: desenvolvimento multiplataforma móvel/desktop/web
- **2.0 (2018)**: Reescrita completa — sistema de tipo de som, coleções modernas
### Dart 2.x — Dart moderno (2018–2023)
- **2.0**: Sistema de tipo de som, não mais`dynamic`por padrão
- **2.3**: Coleção`if`/`for`, operador spread — ótimo para árvores de widgets Flutter
- **2.6**: Métodos de extensão
- **2.10**: Segurança nula de som (opt-in)
- **2.12**: **Segurança nula habilitada por padrão** — tipos anuláveis `?`
- **2.17**: Superparâmetros (`super.x`), enumerações aprimoradas
### Dart 3.x – Registros e padrões (2023 – presente)
- **3.0 (2023)**: **Registros** (portadores de dados anônimos), **padrões** (desestruturação), **modificadores de classe** (`sealed`,`final`,`interface`,`base`), expressões `switch`
- **3.3 (2024)**: Tipos de extensão (wrappers de custo zero)
- **3.5 (2024)**: Visualização de macros — metaprogramação em tempo de compilação
## Evolução da Sintaxe
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

## Tipo Evolução do Sistema
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

## Princípios-chave de design
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Crescimento do Ecossistema
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
