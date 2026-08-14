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
# Scala — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 1.0 | 2004 | Rilis awal (Martin Odersky, EPFL) |
| 2.0 | 2006 | Tipe struktural, peningkatan pencocokan pola |
| 2.7 | 2009 | Pustaka aktor, inferensi tipe yang ditingkatkan |
| 2.8 | 2010 | **Argumen yang diberi nama/default**, objek paket, desain ulang koleksi |
| 2.9 | 2011 | Koleksi paralel, interpolasi string |
| 2.10 | 2013 | **Kelas nilai**, peningkatan implisit, interpolasi string |
| 2.11 | 2014 | Interpolasi string, peningkatan koleksi |
| 2.12 | 2016 | **Jenis SAM** (Java 8 lambda), koleksi di Strawman |
| 2.13 | 2019 | **Desain ulang koleksi**, parameter nama implisit |
| 3.0 | 2021 | **Mayor**: Kompiler baru (Dotty),`enum`,`given`/`using`, metode ekstensi |
| 3.1 | 2022 | Klausa ekspor, alias tipe`opaque`|
| 3.2 | 2022 |  Peningkatan `inline`, kata kunci`erased`|
| 3.3 | 2023 | **Rilis LTS** — null eksplisit, klausa`derives`|
| 3.4 | 2024 | Argumen tipe bernama, anotasi`@experimental`|
| 3,5 | 2024 | Tangkap pemeriksa, pesan kesalahan yang ditingkatkan |
| 3.6 | 2025 | Penyempurnaan lebih lanjut, peningkatan kinerja |
## Tonggak Penting
### Scala Awal (2004–2010)
- **2004**: Martin Odersky merilis Scala — menggabungkan OOP dan FP di JVM
- **2.0–2.7**: Tipe struktural, aktor, inferensi tipe yang ditingkatkan
- **2.8 (2010)**: Argumen yang diberi nama/default, objek paket, desain ulang koleksi — "Scala modern dimulai"
### Scala 2.x Kedewasaan (2011–2020)
- **2.9**: Koleksi paralel
- **2.10**: Kelas nilai, interpolasi string, peningkatan implisit
- **2.12**: Jenis SAM — interop Java 8 yang mulus
- **2.13**: Desain ulang perpustakaan koleksi utama (default tidak dapat diubah)
### Scala 3 — Renaisans (2021–sekarang)
- **3.0 (2021)**: Penulisan ulang kompiler lengkap (Dotty → Scala 3)
  -`enum`menggantikan sifat tersegel + pelat kelas casing
  -`given`/`using`menggantikan parameter implisit
  - Metode ekstensi menggantikan kelas implisit
  - Tipe `match`, tipe gabungan, tipe persimpangan
  - Sintaks yang disederhanakan (kurung kurawal opsional, kata kunci lebih sedikit)
- **3.3 (2023)**: LTS pertama — null eksplisit, klausa `derives`
- **3.4–3.6**: Argumen tipe yang diberi nama, pemeriksa pengambilan, performa
## Evolusi Sintaks
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

## Ketik Evolusi Sistem
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

## Evolusi Konkurensi
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Prinsip Desain Utama
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Pertumbuhan Ekosistem
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
