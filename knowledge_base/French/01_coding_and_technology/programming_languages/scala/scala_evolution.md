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

# Scala — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| 1.0 | 2004 | Version initiale (Martin Odersky, EPFL) |
| 2.0 | 2006 | Types structurels, améliorations de la correspondance de modèles |
| 2.7 | 2009 | Bibliothèque d'acteurs, inférence de type améliorée |
| 2.8 | 2010 | **Arguments nommés/par défaut**, objets de package, refonte des collections |
| 2.9 | 2011 | Collections parallèles, interpolation de chaînes |
| 2.10 | 2013 | **Classes de valeurs**, améliorations implicites, interpolation de chaînes |
| 2.11 | 2014 | Interpolation de chaînes, collections améliorées |
| 2.12 | 2016 | **Types SAM** (Java 8 lambdas), collections sur Strawman |
| 2.13 | 2019 | **Refonte des collections**, paramètres implicites par nom |
| 3.0 | 2021 | **Majeur** : Nouveau compilateur (Dotty),`enum`,`given`/`using`, méthodes d'extension |
| 3.1 | 2022 | Clauses d'export, alias de type`opaque`|
| 3.2 | 2022 |  Améliorations `inline`, mot-clé`erased`|
| 3.3 | 2023 | **Version LTS** — valeurs nulles explicites, clause`derives`|
| 3.4 | 2024 | Arguments de type nommé, annotation`@experimental`|
| 3.5 | 2024 | Vérificateur de capture, messages d'erreur améliorés |
| 3.6 | 2025 | Améliorations supplémentaires, améliorations des performances |
## Étapes majeures
### Début Scala (2004-2010)
- **2004** : Martin Odersky lance Scala — combinant POO et FP sur la JVM
- **2.0–2.7** : types structurels, acteurs, inférence de type améliorée
- **2.8 (2010)** : arguments nommés/par défaut, objets de package, refonte des collections — "Le Scala moderne commence"
### Maturité Scala 2.x (2011-2020)
- **2.9** : Collections parallèles
- **2.10** : Classes de valeurs, interpolation de chaînes, améliorations implicites
- **2.12** : types SAM — interopérabilité transparente avec Java 8
- **2.13** : Refonte de la bibliothèque des collections majeures (immuable par défaut)
### Scala 3 — La Renaissance (2021-présent)
- **3.0 (2021)** : Réécriture complète du compilateur (Dotty → Scala 3)
  -`enum`remplace le trait scellé + le passe-partout de classe de cas
  -`given`/`using`remplace les paramètres implicites
  - Les méthodes d'extension remplacent les classes implicites
  - Types `match`, types d'union, types d'intersection
  - Syntaxe simplifiée (accolades facultatives, moins de mots-clés)
- **3.3 (2023)** : Premier LTS — valeurs nulles explicites, clause `derives`
- **3.4–3.6** : arguments de type nommé, vérificateur de capture, performances
## Évolution de la syntaxe
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

## Évolution du système de types
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

## Évolution de la concurrence
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Principes de conception clés
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Croissance de l'écosystème
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
