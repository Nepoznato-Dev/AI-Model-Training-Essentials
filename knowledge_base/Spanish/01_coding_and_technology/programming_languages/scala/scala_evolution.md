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

# Scala: historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| 1.0 | 2004 | Lanzamiento inicial (Martin Odersky, EPFL) |
| 2.0 | 2006 | Tipos estructurales, mejoras en la coincidencia de patrones |
| 2.7 | 2009 | Biblioteca de actores, inferencia de tipos mejorada |
| 2.8 | 2010 | **Argumentos con nombre/predeterminados**, objetos de paquete, rediseño de colecciones |
| 2.9 | 2011 | Colecciones paralelas, interpolación de cadenas |
| 2.10 | 2013 | **Clases de valores**, mejoras implícitas, interpolación de cadenas |
| 2.11 | 2014 | Interpolación de cadenas, colecciones mejoradas |
| 2.12 | 2016 | **Tipos SAM** (Java 8 lambdas), colecciones en Strawman |
| 2.13 | 2019 | **Rediseño de colecciones**, parámetros de nombre implícitos |
| 3.0 | 2021 | **Principal**: Nuevo compilador (Dotty), `enum`, `given`/`using`, métodos de extensión |
| 3.1 | 2022 | Cláusulas de exportación, alias tipo`opaque`|
| 3.2 | 2022 |  Mejoras `inline`, palabra clave`erased`|
| 3.3 | 2023 | **Lanzamiento LTS**: nulos explícitos, cláusula`derives`|
| 3.4 | 2024 | Argumentos de tipo con nombre, anotación`@experimental`|
| 3.5 | 2024 | Comprobador de captura, mensajes de error mejorados |
| 3.6 | 2025 | Más mejoras, mejoras de rendimiento |
## Hitos importantes
### Escala temprana (2004-2010)
- **2004**: Martin Odersky lanza Scala, que combina programación orientada a objetos y FP en JVM
- **2.0–2.7**: tipos estructurales, actores, inferencia de tipos mejorada
- **2.8 (2010)**: Argumentos con nombre/predeterminados, objetos de paquete, rediseño de colecciones: "comienza Scala moderno"
### Madurez de Scala 2.x (2011-2020)
- **2.9**: Colecciones paralelas
- **2.10**: clases de valores, interpolación de cadenas, mejoras implícitas
- **2.12**: tipos SAM: interoperabilidad perfecta con Java 8
- **2.13**: Rediseño de la biblioteca de colecciones principales (valor predeterminado inmutable)
### Scala 3 — El Renacimiento (2021-presente)
- **3.0 (2021)**: reescritura completa del compilador (Dotty → Scala 3)
  -`enum`reemplaza el rasgo sellado + modelo estándar de clase de caja
  -`given`/`using`reemplaza los parámetros implícitos
  - Los métodos de extensión reemplazan las clases implícitas.
  - Tipos `match`, tipos de unión, tipos de intersección
  - Sintaxis simplificada (llaves opcionales, menos palabras clave)
- **3.3 (2023)**: Primera LTS: nulos explícitos, cláusula `derives`
- **3.4–3.6**: argumentos de tipo con nombre, verificador de captura, rendimiento
## Evolución de la sintaxis
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

## Evolución del sistema tipo
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

## Evolución de la concurrencia
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Principios clave de diseño
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Crecimiento del ecosistema
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
