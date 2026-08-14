<!--
---
# Metadata
title: "Java — Version History & Evolution"
description: "Comprehensive version history and evolution of Java from 1.0 to modern Java."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [java, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Java — история версий и эволюция
## Временная шкала
| Версия | Дата выпуска | Ключевая тема |
|---------|-------------|-----------|
| JDK 1.0 | Январь 1996 г. | Первоначальный выпуск («Дуб») |
| JDK 1.1 | февраль 1997 г. | Внутренние классы, JDBC, RMI |
| J2SE 1.2 | декабрь 1998 г. | Фреймворк коллекций, Swing,`strictfp`|
| J2SE 1.3 | май 2000 г. | JVM HotSpot,`assert`|
| J2SE 1.4 | февраль 2002 г. | `assert`, NIO, регулярное выражение,`java.net`|
| J2SE 5.0 | Сентябрь 2004 г. | **Основные**: дженерики, перечисления, аннотации, автоупаковка, varargs |
| Ява ЮВ 6 | декабрь 2006 г. | Скрипты, API компилятора,`@Override`на интерфейсах |
| Ява ЮВ 7 | июль 2011 г. | `try-with-resources`,`switch`в строке, NIO.2 |
| Ява ЮВ 8 | март 2014 г. | **Основные**: лямбды, потоки, `Optional`, `java.time`, методы по умолчанию |
| Ява 9 | Сентябрь 2017 г. | Модули (JPMS),`var`,`jshell`, методы частного интерфейса |
| Ява 10 | март 2018 г. | `var`для локальных переменных |
| Ява 11 | Сентябрь 2018 г. | **LTS**: методы `String`,`HttpClient`, запуск одного файла |
| Ява 12 | март 2019 г. | Переключение выражений (предварительная версия) |
| Ява 13 | Сентябрь 2019 г. | Текстовые блоки (предварительный просмотр) |
| Ява 14 | март 2020 г. | `record`(предварительная версия), выражения переключения, шаблон`instanceof`|
| Ява 15 | Сентябрь 2020 г. | Текстовые блоки, запечатанные классы (предварительный просмотр) |
| Ява 16 | март 2021 г. | `record`,`instanceof`сопоставление с образцом |
| Ява 17 | Сентябрь 2021 г. | **LTS**: запечатанные классы, сопоставление с образцом для`switch`|
| Ява 18 | март 2022 г. | Простой веб-сервер, UTF-8 по умолчанию |
| Ява 19 | Сентябрь 2022 г. | Виртуальные потоки (предварительная версия), сопоставление с образцом |
| Ява 20 | март 2023 г. | Ограниченные значения (инкубатор), шаблоны записи |
| Ява 21 | Сентябрь 2023 г. | **LTS**: **Виртуальные потоки**, сопоставление с образцом, шаблоны `switch`, упорядоченные коллекции |
| Ява 22 | март 2024 г. | Строковые шаблоны (предварительная версия), API внешней памяти |
| Ява 23 | Сентябрь 2024 г. | Примитивные типы в шаблонах (предварительный просмотр) |
| Ява 24 | март 2025 г. | Структурированный параллелизм (предварительная версия) |
| Ява 25 | Сентябрь 2025 г. | **LTS**: (ожидается) |
## Основные вехи
### Классическая эпоха (1996–2004)
- **1.0 (1996)**: «Напиши один раз, работай где угодно» — апплеты, AWT
- **1.2 (1998 г.)**: Структура коллекций (основа коллекций Java).
- **1.4 (2002 г.)**: NIO, ведение журнала, регулярное выражение, утверждения.
- **5.0 (2004 г.)**: самое большое обновление — дженерики, перечисления, аннотации, автоупаковка, улучшенный цикл for, varargs, `static import`.
### Эра предпринимательства (2006–2014 гг.)
- **6 (2006 г.)**: Поддержка сценариев, API компилятора.
- **7 (2011)**:`try-with-resources`, ромбический оператор,`switch`на строке, NIO.2
- **8 (2014 г.)**: Другой «большой взрыв» — лямбды, потоки,`Optional`,`java.time`, методы по умолчанию, `CompletableFuture`
### Современная эпоха (2017 – настоящее время)
- **9 (2017 г.)**: Система модулей (JPMS),`var`,`jshell`REPL
- **11 (2018 г.)**: первая долгосрочная версия с периодичностью выпуска менее 6 месяцев;  ХQZMARKER2XQZ ; Изменение лицензии Oracle JDK
- **17 (2021 г.)**: LTS — запечатанные классы, сопоставление с образцом.
- **21 (2023 г.)**: LTS — **виртуальные потоки** (Project Loom), сопоставление шаблонов, запись шаблонов.
## Периодичность выпуска 6-месячных выпусков
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Путешествие по дженерикам
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Эволюция функционального программирования
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Эволюция параллелизма
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Эволюция функций языка
```
Java 5:   Generics, enums, annotations, autoboxing, varargs
Java 7:   try-with-resources, diamond <>, switch on String
Java 8:   Lambdas, streams, default methods, Optional
Java 9:   var (local), modules, jshell
Java 14:  record (preview), switch expressions
Java 16:  record, instanceof pattern
Java 17:  sealed classes, switch pattern matching
Java 21:  virtual threads, pattern matching, record patterns
```

## Эволюция JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Рост экосистемы
```
1998: J2EE — enterprise Java begins
2001: Spring Framework
2004: Hibernate, Maven
2006: Java on Android (modified Java)
2010: Oracle acquires Sun (Java)
2014: Java 8 — Spring Boot era
2018: Java 11 — modular JDK, GraalVM
2023: Java 21 — virtual threads, Spring Boot 3
2025: Java remains #1 enterprise language
```
