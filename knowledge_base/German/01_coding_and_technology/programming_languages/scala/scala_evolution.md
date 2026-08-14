<!--
---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Scala – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 1,0 | 2004 | Erstveröffentlichung (Martin Odersky, EPFL) |
| 2,0 | 2006 | Strukturtypen, Verbesserungen beim Mustervergleich |
| 2,7 | 2009 | Actors-Bibliothek, verbesserte Typinferenz |
| 2,8 | 2010 | **Benannte/Standardargumente**, Paketobjekte, Neugestaltung von Sammlungen |
| 2,9 | 2011 | Parallele Sammlungen, String-Interpolation |
| 2.10 | 2013 | **Wertklassen**, implizite Verbesserungen, String-Interpolation |
| 2.11 | 2014 | String-Interpolation, verbesserte Sammlungen |
| 2.12 | 2016 | **SAM-Typen** (Java 8 Lambdas), Sammlungen auf Strawman |
| 2.13 | 2019 | **Neugestaltung der Sammlungen**, implizite Parameter nach Namen |
| 3,0 | 2021 | **Major**: Neuer Compiler (Dotty), `enum`,`given`/ `using`, Erweiterungsmethoden |
| 3.1 | 2022 | Exportklauseln, Aliase vom Typ`opaque`|
| 3.2 | 2022 |  `inline`-Verbesserungen, `erased`-Schlüsselwort |
| 3.3 | 2023 | **LTS-Release** – explizite Nullen, `derives`-Klausel |
| 3,4 | 2024 | Benannte Typargumente, `@experimental`-Annotation |
| 3,5 | 2024 | Capture Checker, verbesserte Fehlermeldungen |
| 3,6 | 2025 | Weitere Verfeinerungen, Leistungsverbesserungen |
## Wichtige Meilensteine
### Frühe Scala (2004–2010)
- **2004**: Martin Odersky veröffentlicht Scala – eine Kombination aus OOP und FP auf der JVM
- **2.0–2.7**: Strukturtypen, Akteure, verbesserte Typinferenz
- **2.8 (2010)**: Benannte/Standardargumente, Paketobjekte, Neugestaltung von Sammlungen – „modernes Scala beginnt“
### Scala 2.x-Reife (2011–2020)
- **2.9**: Parallele Sammlungen
- **2.10**: Werteklassen, String-Interpolation, implizite Verbesserungen
- **2.12**: SAM-Typen – nahtlose Java 8-Interop
- **2.13**: Große Neugestaltung der Sammlungsbibliothek (unveränderlicher Standard)
### Scala 3 – Die Renaissance (2021–heute)
- **3.0 (2021)**: Vollständige Neufassung des Compilers (Dotty → Scala 3)
  –`enum`ersetzt versiegeltes Merkmal + Fallklassen-Boilerplate
  -`given`/`using`ersetzt implizite Parameter
  - Erweiterungsmethoden ersetzen implizite Klassen
  - `match`-Typen, Union-Typen, Schnittpunkttypen
  - Vereinfachte Syntax (optionale geschweifte Klammern, weniger Schlüsselwörter)
- **3.3 (2023)**: Erstes LTS – explizite Nullen, `derives`-Klausel
- **3.4–3.6**: Benannte Typargumente, Erfassungsprüfung, Leistung
## Syntaxentwicklung
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

## Typsystementwicklung
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

## Parallelitätsentwicklung
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Wichtige Designprinzipien
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Ökosystemwachstum
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
