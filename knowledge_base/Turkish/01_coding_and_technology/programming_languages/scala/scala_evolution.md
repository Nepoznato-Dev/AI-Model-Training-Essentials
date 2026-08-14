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
# Scala — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 1.0 | 2004 | İlk sürüm (Martin Odersky, EPFL) |
| 2.0 | 2006 | Yapısal tipler, desen eşleştirme iyileştirmeleri |
| 2.7 | 2009 | Aktörler kitaplığı, geliştirilmiş tür çıkarımı |
| 2.8 | 2010 | **Adlandırılmış/varsayılan bağımsız değişkenler**, paket nesneleri, koleksiyonların yeniden tasarımı |
| 2.9 | 2011 | Paralel koleksiyonlar, dize enterpolasyonu |
| 2.10 | 2013 | **Değer sınıfları**, örtülü iyileştirmeler, dize enterpolasyonu |
| 2.11 | 2014 | Dize enterpolasyonu, geliştirilmiş koleksiyonlar |
| 2.12 | 2016 | **SAM türleri** (Java 8 lambdalar), Strawman'daki koleksiyonlar |
| 2.13 | 2019 | **Koleksiyonların yeniden tasarlanması**, gizli ad parametreleri |
| 3.0 | 2021 | **Major**: Yeni derleyici (Dotty),`enum`,`given`/`using`, genişletme yöntemleri |
| 3.1 | 2022 | Dışa aktarma cümleleri,`opaque`türü takma adlar |
| 3.2 | 2022 | `inline`iyileştirmeleri,`erased`anahtar kelime |
| 3.3 | 2023 | **LTS sürümü** — açık boş değerler,`derives`yan tümcesi |
| 3.4 | 2024 | Adlandırılmış tür bağımsız değişkenleri,`@experimental`ek açıklaması |
| 3.5 | 2024 | Yakalama denetleyicisi, iyileştirilmiş hata mesajları |
| 3.6 | 2025 | Daha fazla iyileştirme, performans iyileştirmeleri |
## Önemli Kilometre Taşları
### Erken Scala (2004–2010)
- **2004**: Martin Odersky, OOP ve FP'yi JVM'de birleştiren Scala'yı piyasaya sürdü
- **2,0–2,7**: Yapısal türler, aktörler, geliştirilmiş tür çıkarımı
- **2.8 (2010)**: Adlandırılmış/varsayılan bağımsız değişkenler, paket nesneleri, koleksiyonların yeniden tasarımı — "modern Scala başlıyor"
### Scala 2.x Olgunluğu (2011–2020)
- **2,9**: Paralel koleksiyonlar
- **2.10**: Değer sınıfları, dize enterpolasyonu, örtülü iyileştirmeler
- **2.12**: SAM türleri — kesintisiz Java 8 birlikte çalışma
- **2.13**: Önemli koleksiyon kitaplığı yeniden tasarımı (değişmez varsayılan)
### Scala 3 — Rönesans (2021-günümüz)
- **3.0 (2021)**: Derleyicinin tamamen yeniden yazılması (Dotty → Scala 3)
  - `enum`, mühürlü özellik + kasa sınıfı standartlarının yerini alır
  -`given`/`using`örtülü parametrelerin yerini alır
  - Uzatma yöntemleri örtülü sınıfların yerini alır
  -`match`türleri, birleşim türleri, kesişim türleri
  - Basitleştirilmiş sözdizimi (isteğe bağlı parantez, daha az anahtar kelime)
- **3.3 (2023)**: İlk LTS — açık boş değerler,`derives`yan tümcesi
- **3,4–3,6**: Adlandırılmış tür bağımsız değişkenleri, yakalama denetleyicisi, performans
## Söz Dizimi Gelişimi
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

## Tür Sistem Gelişimi
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

## Eşzamanlılık Gelişimi
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Temel Tasarım İlkeleri
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Ekosistem Büyümesi
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
