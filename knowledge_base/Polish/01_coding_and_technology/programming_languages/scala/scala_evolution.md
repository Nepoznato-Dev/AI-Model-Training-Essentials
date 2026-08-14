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

# Scala — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 1,0 | 2004 | Wersja pierwsza (Martin Odersky, EPFL) |
| 2,0 | 2006 | Typy strukturalne, ulepszenia dopasowywania wzorców |
| 2.7 | 2009 | Biblioteka aktorów, ulepszone wnioskowanie o typach |
| 2.8 | 2010 | **Nazwane/domyślne argumenty**, obiekty pakietów, przeprojektowanie kolekcji |
| 2.9 | 2011 | Zbiory równoległe, interpolacja ciągów |
| 2.10 | 2013 | **Klasy wartości**, ukryte ulepszenia, interpolacja ciągów |
| 2.11 | 2014 | Interpolacja ciągów, ulepszone kolekcje |
| 2.12 | 2016 | **Typy SAM** (lamby Java 8), kolekcje na Strawmanie |
| 2.13 | 2019 | **Przeprojektowanie kolekcji**, ukryte parametry według nazwy |
| 3,0 | 2021 | **Główny**: Nowy kompilator (Dotty),`enum`,`given`/`using`, metody rozszerzenia |
| 3.1 | 2022 | Klauzule eksportowe, aliasy typu`opaque`|
| 3.2 | 2022 |  Ulepszenia `inline`, słowo kluczowe`erased`|
| 3.3 | 2023 | **Wersja LTS** — jawne wartości null, klauzula`derives`|
| 3.4 | 2024 | Argumenty typu nazwanego, adnotacja`@experimental`|
| 3,5 | 2024 | Sprawdzanie przechwytywania, ulepszone komunikaty o błędach |
| 3,6 | 2025 | Dalsze udoskonalenia, ulepszenia wydajności |
## Główne kamienie milowe
### Wczesna Scala (2004–2010)
- **2004**: Martin Odersky wydaje Scalę — łączącą OOP i FP na JVM
- **2,0–2,7**: Typy strukturalne, aktorzy, ulepszone wnioskowanie o typach
- **2.8 (2010)**: Argumenty nazwane/domyślne, obiekty pakietów, przeprojektowanie kolekcji — „początek nowoczesnej Scali”
### Dojrzałość Scala 2.x (2011–2020)
- **2.9**: Zbiory równoległe
- **2.10**: Klasy wartości, interpolacja ciągów, ukryte ulepszenia
- **2.12**: Typy SAM — płynna współpraca z Java 8
- **2.13**: Przeprojektowanie bibliotek głównych kolekcji (domyślne niezmienne)
### Scala 3 — Renesans (2021 – obecnie)
- **3.0 (2021)**: Całkowite przepisanie kompilatora (Dotty → Scala 3)
  -`enum`zastępuje tablicę znamionową cechy zapieczętowanej + klasy obudowy
  -`given`/`using`zastępuje parametry ukryte
  - Metody rozszerzeń zastępują klasy niejawne
  - Typy `match`, typy unii, typy skrzyżowań
  - Uproszczona składnia (opcjonalne nawiasy klamrowe, mniej słów kluczowych)
- **3.3 (2023)**: First LTS — jawne wartości null, klauzula `derives`
- **3,4–3,6**: Argumenty typu nazwanego, moduł sprawdzania przechwytywania, wydajność
## Ewolucja składni
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

## Wpisz ewolucję systemu
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

## Ewolucja współbieżności
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Kluczowe zasady projektowania
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Rozwój ekosystemu
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
