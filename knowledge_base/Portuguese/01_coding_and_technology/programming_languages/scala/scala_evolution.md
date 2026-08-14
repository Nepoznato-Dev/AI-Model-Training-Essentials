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

# Scala – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 2004 | Lançamento inicial (Martin Odersky, EPFL) |
| 2.0 | 2006 | Tipos estruturais, melhorias na correspondência de padrões |
| 2.7 | 2009 | Biblioteca de atores, inferência de tipo aprimorada |
| 2.8 | 2010 | **Argumentos nomeados/padrão**, objetos de pacote, redesenho de coleções |
| 2.9 | 2011 | Coleções paralelas, interpolação de strings |
| 2.10 | 2013 | **Classes de valor**, melhorias implícitas, interpolação de strings |
| 2.11 | 2014 | Interpolação de strings, coleções aprimoradas |
| 2.12 | 2016 | **Tipos SAM** (Java 8 lambdas), coleções no Strawman |
| 2.13 | 2019 | **Redesenho de coleções**, parâmetros implícitos de nome |
| 3.0 | 2021 | **Principal**: Novo compilador (Dotty),`enum`,`given`/`using`, métodos de extensão |
| 3.1 | 2022 | Cláusulas de exportação, aliases do tipo`opaque`|
| 3.2 | 2022 |  Melhorias `inline`, palavra-chave`erased`|
| 3.3 | 2023 | **Lançamento LTS** — nulos explícitos, cláusula`derives`|
| 3.4 | 2024 | Argumentos de tipo nomeado, anotação`@experimental`|
| 3.5 | 2024 | Verificador de captura, mensagens de erro aprimoradas |
| 3.6 | 2025 | Mais refinamentos, melhorias de desempenho |
## Marcos importantes
### Scala inicial (2004–2010)
- **2004**: Martin Odersky lança Scala — combinando OOP e FP na JVM
- **2,0–2,7**: tipos estruturais, atores, inferência de tipo aprimorada
- **2.8 (2010)**: Argumentos nomeados/padrão, objetos de pacote, redesenho de coleções — "o Scala moderno começa"
### Scala 2.x Maturidade (2011–2020)
- **2.9**: coleções paralelas
- **2.10**: Classes de valor, interpolação de strings, melhorias implícitas
- **2.12**: tipos SAM — interoperabilidade perfeita com Java 8
- **2.13**: Redesenho da biblioteca de coleções principais (padrão imutável)
### Scala 3 — A Renascença (2021-presente)
- **3.0 (2021)**: Reescrita completa do compilador (Dotty → Scala 3)
  -`enum`substitui traço selado + padrão de classe de caso
  -`given`/`using`substitui parâmetros implícitos
  - Métodos de extensão substituem classes implícitas
  - Tipos `match`, tipos de união, tipos de interseção
  - Sintaxe simplificada (chaves opcionais, menos palavras-chave)
- **3.3 (2023)**: Primeiro LTS — nulos explícitos, cláusula `derives`
- **3.4–3.6**: argumentos de tipo nomeado, verificador de captura, desempenho
## Evolução da Sintaxe
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

## Tipo Evolução do Sistema
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

## Evolução da simultaneidade
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Princípios-chave de design
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Crescimento do Ecossistema
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
