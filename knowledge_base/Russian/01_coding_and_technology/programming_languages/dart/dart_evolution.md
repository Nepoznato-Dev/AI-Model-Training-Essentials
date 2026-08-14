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
# Дарт — История версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 1.0 | 2013 | Первоначальный выпуск (Google, Ларс Бак и Каспер Лунд) |
| 1,2 | 2014 | Улучшения компилятора Dart2JS |
| 1,3 | 2014 |  Поддержка`async`/`await`|
| 1,4 | 2014 | `enum`, улучшения миксинов |
| 1,5 | 2014 | Генераторы (`sync*`,`async*`) |
| 1,6 | 2014 |  Улучшения`Future`|
| 1,8 | 2014 |  Улучшения`dart:io`|
| 1,9 | 2015 | Строгий режим (по желанию) |
| 1.11 | 2015 |  Улучшения`Future.then`|
| 1.12 | 2015 | **Сильный режим** включен |
| 2.0 | 2018 | **Основное**: система звукового типа, подготовка к безопасности `null`, переписывание коллекций |
| 2.1 | 2018 |  Объединение `int`/`double`,`await for`|
| 2.2 | 2019 |  Литерал `Set`, улучшения коллекции`const`|
| 2.3 | 2019 | Коллекция `if`, коллекция `for`, оператор распространения`...`|
| 2,6 | 2019 | Методы расширения |
| 2,7 | 2020 | Именованные параметры по умолчанию |
| 2.10 | 2020 | **Надежная нулевая безопасность** (согласие) |
| 2.12 | 2021 | **Нулевая безопасность включена по умолчанию** |
| 2.13 | 2021 | Конструктор-обрывки |
| 2.14 | 2021 |  Улучшения `late`, целые числа без знака |
| 2.15 | 2021 | Конструктор отделяет стабильные, универсальные типы функций |
| 2.17 | 2022 | **Суперпараметры**, расширенные перечисления |
| 2.18 | 2022 | Расширенный вывод типов |
| 2.19 | 2023 | Рекорды и закономерности (превью) |
| 3.0 | 2023 | **Основные**: записи, шаблоны, модификаторы классов, выражения`switch`|
| 3.1 | 2023 | Улучшения шаблонов, запечатанные классы |
| 3.2 | 2023 | Улучшения статического анализа |
| 3.3 | 2024 | Типы расширений, улучшения выражений`switch`|
| 3,4 | 2024 |  Элементы `if`, улучшения`case`|
| 3,5 | 2024 | Макросы (предварительная версия), дальнейшие усовершенствования языка |
| 3,6 | 2025 | Постоянное развитие |
## Основные вехи
### Dart 1.x — Ранние годы (2013–2017)
- **2013**: Google выпускает Dart, предназначенный для структурированного веб-программирования.
- **Цель**: заменить JavaScript для веб-разработки (позже цель будет изменена).
- **1.0**: классы, интерфейсы, изоляты, необязательная типизация.
- **1.3**: поддержка `async`/`await`.
- **1.9**: строгий режим (включение строгой типизации)
- Dart VM некоторое время использовался в Chromium, затем был удален.
### Поворот флаттера (2017–2018)
- **2017**: анонсирован фреймворк Flutter — Dart становится языком пользовательского интерфейса.
- Dart находит свою цель: кроссплатформенная мобильная/десктопная/веб-разработка.
- **2.0 (2018)**: Полная переработка — система звуковых типов, современные коллекции.
### Дарт 2.x — Современный дартс (2018–2023)
- **2.0**: система типа звука, по умолчанию не более `dynamic`.
- **2.3**: Коллекция`if`/ `for`, оператор расширения — отлично подходит для деревьев виджетов Flutter.
- **2.6**: Методы расширения.
- **2.10**: Надежная нулевая безопасность (согласно согласию)
- **2.12**: **Нулевая безопасность включена по умолчанию** —`?`типы, допускающие нулевые значения
- **2.17**: суперпараметры (`super.x`), расширенные перечисления.
### Dart 3.x — Пластинки и паттерны (2023 – настоящее время)
- **3.0 (2023 г.)**: **Записи** (анонимные носители данных), **шаблоны** (деструктуризация), **модификаторы классов** (`sealed`,`final`,`interface`,`base`), выражения `switch`.
- **3.3 (2024 г.)**: типы расширений (обертки с нулевой стоимостью).
- **3.5 (2024 г.)**: Предварительный просмотр макросов — метапрограммирование во время компиляции.
## Эволюция синтаксиса
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

## Эволюция системы типов
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

## Ключевые принципы проектирования
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Рост экосистемы
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
