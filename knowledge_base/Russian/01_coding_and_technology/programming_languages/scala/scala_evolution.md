---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [scala, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Scala — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 1.0 | 2004 | Первоначальный выпуск (Мартин Одерски, EPFL) |
| 2.0 | 2006 | Структурные типы, улучшения сопоставления с образцом |
| 2,7 | 2009 | Библиотека актеров, улучшенный вывод типов |
| 2,8 | 2010 | **Именованные аргументы/аргументы по умолчанию**, объекты пакета, новый дизайн коллекций |
| 2,9 | 2011 | Параллельные коллекции, интерполяция строк |
| 2.10 | 2013 | **Классы значений**, неявные улучшения, интерполяция строк |
| 2.11 | 2014 | Интерполяция строк, улучшенные коллекции |
| 2.12 | 2016 | **Типы SAM** (лямбда-выражения Java 8), коллекции на Strawman |
| 2.13 | 2019 | **Редизайн коллекций**, неявные параметры по имени |
| 3.0 | 2021 | **Основное**: Новый компилятор (Dotty),`enum`,`given`/`using`, методы расширения |
| 3.1 | 2022 | Предложения экспорта, псевдонимы типа`opaque`|
| 3.2 | 2022 |  Улучшения `inline`, ключевое слово`erased`|
| 3.3 | 2023 | **LTS-версия** — явные значения NULL, предложение`derives`|
| 3,4 | 2024 | Аргументы именованного типа, аннотация`@experimental`|
| 3,5 | 2024 | Средство проверки захвата, улучшенные сообщения об ошибках |
| 3,6 | 2025 | Дальнейшие доработки и улучшения производительности |
## Основные вехи
### Ранняя Scala (2004–2010)
- **2004**: Мартин Одерски выпускает Scala — сочетание ООП и ФП на JVM.
- **2.0–2.7**: Структурные типы, действующие лица, улучшенный вывод типов.
- **2.8 (2010 г.)**: именованные аргументы/аргументы по умолчанию, объекты пакетов, редизайн коллекций — «начинается современная Scala»
### Зрелость Scala 2.x (2011–2020 гг.)
- **2.9**: Параллельные коллекции.
- **2.10**: классы значений, интерполяция строк, неявные улучшения.
- **2.12**: типы SAM — бесшовное взаимодействие с Java 8.
- **2.13**: Обновлен дизайн библиотеки основных коллекций (неизменяемый по умолчанию).
### Scala 3 — Возрождение (2021 – настоящее время)
- **3.0 (2021 г.)**: Полная переработка компилятора (Dotty → Scala 3).
  -`enum`заменяет шаблон «запечатанная черта + класс класса».
  - `given`/`using` заменяет неявные параметры.
  — Методы расширения заменяют неявные классы.
  - Типы `match`, типы объединения, типы пересечений.
  - Упрощенный синтаксис (необязательные фигурные скобки, меньше ключевых слов)
- **3.3 (2023 г.)**: первый LTS — явные значения NULL, предложение `derives`.
- **3.4–3.6**: аргументы именованного типа, средство проверки захвата, производительность.
## Эволюция синтаксиса
```scala
// Scala 2: Implicit class for extension methods
implicit class StringOps(val s: String) extends AnyVal {
  def shout: String = s.toUpperCase + "!"
}

// Scala 3: Extension methods
extension (s: String)
  def shout: String = s.toUpperCase + "!"

// Scala 2: Sealed trait + case class (ADT)
sealed trait Color
case object Red extends Color
case object Blue extends Color

// Scala 3: enum
enum Color:
  case Red, Blue, Green

// Scala 2: Implicit parameters
def greet(implicit ctx: Context): String = ctx.name

// Scala 3: given/using
given ctx: Context = Context("Alice")
def greet(using ctx: Context): String = ctx.name

// Scala 3: Union types
def process(input: String | Int): String = input.toString

// Scala 3: Match types
type Elem[X] = X match
  case String => Char
  case List[t] => t
  case _ => X
```

## Эволюция системы типов
```
Scala 2.0:  Structural types, refinements
Scala 2.7:  Existential types
Scala 2.8:  Implicit resolution rules
Scala 2.10: Value classes, macro annotations
Scala 2.12: SAM conversion, Java 8 interop
Scala 2.13: Implicit by-name, literal types
Scala 3.0:  Union types, intersection types, match types,
            opaque types, enum, given/using, extension methods
Scala 3.3:  Explicit nulls, derives clause
Scala 3.4:  Named type arguments
Scala 3.5:  Capture checker (experimental)
```

## Эволюция параллелизма
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Ключевые принципы проектирования
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Рост экосистемы
```
2004: Scala released by Martin Odersky (EPFL)
2009: Twitter adopts Scala — puts Scala on the map
2011: Akka framework — distributed computing
2012: Play Framework 2.0 — web development
2014: Apache Spark — big data processing in Scala
2016: sbt becomes standard build tool
2021: Scala 3 — modernized language
2025: Scala powers LinkedIn, Twitter, Netflix, The Guardian, Stripe
       sbt, Mill build tools; Akka, ZIO, Cats Effect ecosystems
```
