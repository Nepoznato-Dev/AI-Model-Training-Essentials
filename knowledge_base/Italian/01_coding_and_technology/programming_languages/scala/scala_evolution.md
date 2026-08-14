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
# Scala: storia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 2004| Versione iniziale (Martin Odersky, EPFL) |
| 2.0 | 2006| Tipi strutturali, miglioramenti alla corrispondenza dei modelli |
| 2.7 | 2009| Libreria di attori, inferenza di tipo migliorata |
| 2.8 | 2010| **Argomenti denominati/predefiniti**, oggetti del pacchetto, riprogettazione delle raccolte |
| 2.9 | 2011 | Collezioni parallele, interpolazione di stringhe |
| 2.10| 2013| **Classi di valori**, miglioramenti impliciti, interpolazione di stringhe |
| 2.11 | 2014| Interpolazione di stringhe, raccolte migliorate |
| 2.12 | 2016| **Tipi SAM** (Java 8 lambda), raccolte su Strawman |
| 2.13 | 2019 | **Riprogettazione delle raccolte**, parametri impliciti per nome |
| 3.0 | 2021 | **Maggiore**: Nuovo compilatore (Dotty),`enum`,`given`/`using`, metodi di estensione |
| 3.1 | 2022 | Clausole di esportazione, alias di tipo`opaque`|
| 3.2 | 2022 |  Miglioramenti `inline`, parola chiave`erased`|
| 3.3 | 2023 | **Versione LTS**: valori null espliciti, clausola`derives`|
| 3.4 | 2024 | Argomenti di tipo denominato, annotazione`@experimental`|
| 3,5 | 2024 | Controllo acquisizione, messaggi di errore migliorati |
| 3.6 | 2025 | Ulteriori perfezionamenti, miglioramenti delle prestazioni |
## Traguardi importanti
### Prima Scala (2004–2010)
- **2004**: Martin Odersky pubblica Scala, combinando OOP e FP sulla JVM
- **2.0–2.7**: tipi strutturali, attori, inferenza dei tipi migliorata
- **2.8 (2010)**: argomenti con nome/predefiniti, oggetti pacchetto, riprogettazione di raccolte — "inizia Scala moderna"
### Maturità Scala 2.x (2011–2020)
- **2.9**: Collezioni parallele
- **2.10**: Classi di valore, interpolazione di stringhe, miglioramenti impliciti
- **2.12**: tipi SAM: interoperabilità Java 8 senza interruzioni
- **2.13**: riprogettazione della libreria delle raccolte principali (impostazione predefinita immutabile)
### Scala 3 — Il Rinascimento (2021-oggi)
- **3.0 (2021)**: riscrittura completa del compilatore (Dotty → Scala 3)
  -`enum`sostituisce tratto sigillato + boilerplate di classe case
  -`given`/`using`sostituisce i parametri impliciti
  - I metodi di estensione sostituiscono le classi implicite
  - Tipi `match`, tipi di unione, tipi di intersezione
  - Sintassi semplificata (parentesi graffe opzionali, meno parole chiave)
- **3.3 (2023)**: Primo LTS: null espliciti, clausola `derives`
- **3.4–3.6**: argomenti di tipo con nome, controllo di acquisizione, prestazioni
## Evoluzione della sintassi
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

## Digitare Evoluzione del sistema
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

## Evoluzione della concorrenza
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Principi chiave di progettazione
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Crescita dell'ecosistema
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
