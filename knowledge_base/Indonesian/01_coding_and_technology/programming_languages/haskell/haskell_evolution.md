---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [haskell, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Haskell — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Haskell 1.0 | 1990 | Rilis awal (usaha panitia) |
| Haskell 1.2 | 1992 | Eksperimen sistem objek |
| Haskell 1.3 | 1996 | Ketik kelas yang diperkenalkan |
| Haskell 1.4 | 1997 |  Monad`IO`diklarifikasi |
| Haskell 98 | 1998 | **Standar stabil pertama** |
| Haskell 2010 | 2010 | **Revisi standar**, Cabal, modul |
| GHC 7.0 | 2011 | Tipe keluarga, tipe data |
| GHC 7.4 | 2012 | Proposal Aplikatif-Monad dimulai |
| GHC 7.6 | 2013 | Ketik perbaikan keluarga |
| GHC 7.8 | 2014 | Sinonim pola,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Proposal Monad Aplikatif (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, kesalahan jenis khusus |
| GHC 8.2 | 2017 | Jumlah tanpa kotak, ransel (sistem modul) |
| GHC 8.4 | 2018 | Jalur dasar abstrak,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | Tipe Bintang,`DerivingVia`|
| GHC 8.8 | 2019 | MonadGagal di Pendahuluan |
| GHC 8.10 | 2020 | Notasi`do`terpadu, jenis polimorfisme |
| GHC 9.0 | 2021 | **Polimorfisme Levity**, tipe linier |
| GHC 9.2 | 2022 |`do`yang memenuhi syarat, pesan kesalahan yang ditingkatkan |
| GHC 9.4 | 2022 | **GHC2021** kumpulan ekstensi bahasa,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Argumen tipe yang diperlukan,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`stabil, pesan kesalahan ditingkatkan |
| GHC 9.10 | 2024 | Penyempurnaan lebih lanjut, kinerja |
| GHC 9.12 | 2025 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Haskell 1.x - Tahun Komite (1990–1998)
- **1990**: Haskell 1.0 — bahasa fungsional malas yang dirancang oleh komite
- **1.3 (1996)**: Kelas tipe — fitur penentu Haskell
- **1.4 (1997)**: Monad`IO`diklarifikasi — cara menangani efek samping secara murni
- **Haskell 98**: Standar stabil pertama; masih menjadi referensi hingga saat ini
### Haskell 2010 — Standar Modern
- **2010**: Standar yang direvisi — Komplotan rahasia (sistem paket), peningkatan sistem modul
- GHC menjadi kompiler de facto
- Cabal + Hackage = ekosistem paket Haskell
### GHC 7.x — Ketik Daya Sistem (2011–2015)
- Jenis keluarga, jenis data, jenis polimorfisme
- Applicative-Monad Proposal (AMP) — memperbaiki hierarki kelas tipe
- Pola sinonim, ekstensi `Strict`
### GHC 8.x — Haskell Modern (2016–2020)
-`TypeApplications`— argumen tipe eksplisit di situs panggilan
- Kesalahan tipe khusus — pesan kompiler yang lebih baik
- Backpack — sistem modul untuk desain berbasis komponen
-`DerivingVia`— strategi penurunan yang fleksibel
### GHC 9.x — Revolusi Kegunaan (2021–sekarang)
- **9.0**: Polimorfisme Levity, tipe linier (keamanan sumber daya)
- **9.2**:`do`yang memenuhi syarat, pesan kesalahan yang ditingkatkan
- **9.4**: **GHC2021** — ekstensi default modern; `OverloadedRecordDot`(akses lapangan dengan`.`)
- **9.6**: Argumen tipe yang diperlukan,`TypeAbstractions`
- **9.8–9.12**: Peningkatan pesan kesalahan lanjutan, kinerja
## Evolusi Sintaks
```haskell
-- Haskell 98: Basic type classes
class Eq a where
  (==) :: a -> a -> Bool

-- GHC extensions: Type applications (GHC 8.0)
-- Before:
read "[1,2,3]" :: [Int]
-- After:
read @[Int] "[1,2,3]"

-- GHC 9.4: OverloadedRecordDot
-- Before:
name (getPerson user)
-- After:
user.person.name

-- GHC 9.0: Linear types
-- Before:
processFile :: FilePath -> IO Result
-- After:
processFile :: FilePath %1 -> IO Result  -- file handle used exactly once

-- GHC 8.0: Custom type errors
type family ErrorMessage (a :: Type) :: ErrorMessage where
  ErrorMessage (NotSerializable a) =
    'Text "Cannot serialize type " ':<>: 'ShowType a
```

## Ketik Evolusi Sistem
```
Haskell 1.0:  Basic types, algebraic data types, pattern matching
Haskell 1.3:  Type classes
Haskell 98:   Multi-parameter type classes, functional dependencies
GHC 6.x:     GADTs, type families, rank-N types
GHC 7.0:     Data kinds, kind polymorphism
GHC 7.10:    Applicative-Monad Proposal
GHC 8.0:     TypeApplications, custom type errors
GHC 8.2:     Unboxed sums
GHC 9.0:     Levity polymorphism, linear types
GHC 9.4:     OverloadedRecordDot, GHC2021
GHC 9.6:     Required type arguments, TypeAbstractions
```

## Konkurensi & Paralelisme
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Prinsip Desain Utama
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Pertumbuhan Ekosistem
```
1990: Haskell 1.0 — academic curiosity
1998: Haskell 98 — stable standard
2007: Cabal + Hackage — package ecosystem
2010: Haskell 2010 — revised standard
2012: Stack build tool — reproducible builds
2015: Haskell in industry — Facebook, Standard Chartered, Well-Typed
2021: GHC 9.0 — levity polymorphism, linear types
2023: GHC 9.6 — type abstractions
2025: Haskell used in finance, compilers, formal verification,
       blockchain (Cardano), and academic research
       GHC, Stack, Cabal; key libraries: lens, aeson, servant, yesod
```
