<!--
---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Haskell — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Haskell 1.0 | 1990 | İlk sürüm (komite çalışması) |
| Haskell 1.2 | 1992 | Nesne sistemi deneyleri |
| Haskell 1.3 | 1996 | Tür sınıfları tanıtıldı |
| Haskell 1.4 | 1997 | `IO`monad netleştirildi |
| Haskell 98 | 1998 | **İlk kararlı standart** |
| Haskell 2010 | 2010 | **Revize edilmiş standart**, Cabal, modüller |
| GHC 7.0 | 2011 | Tip aileleri, veri türleri |
| GHC 7.4 | 2012 | Uygulamalı-Monad teklifi başlıyor |
| GHC 7.6 | 2013 | Tür aileleri iyileştirmeleri |
| GHC 7.8 | 2014 | Desen eş anlamlıları,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Uygulamalı-Monad Teklifi (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**, `MonadFail`, özel tür hataları |
| GHC 8.2 | 2017 | Kutusuz meblağlar, sırt çantası (modül sistemi) |
| GHC 8.4 | 2018 | Soyut temel yol,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | Prelüd'de MonadFail |
| GHC 8.10 | 2020 | Birleşik`do`notasyonu, tür polimorfizmi |
| GHC 9.0 | 2021 | **Levite polimorfizmi**, doğrusal türler |
| GHC 9.2 | 2022 | Nitelikli `do`, iyileştirilmiş hata mesajları |
| GHC 9.4 | 2022 | **GHC2021** dil uzantısı seti,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Gerekli tür bağımsız değişkenleri,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`kararlı, geliştirilmiş hata mesajları |
| GHC 9.10 | 2024 | Daha fazla iyileştirme, performans |
| GHC 9.12 | 2025 | Devam eden geliştirme |
## Önemli Kilometre Taşları
### Haskell 1.x — Komite Yılları (1990–1998)
- **1990**: Haskell 1.0 — komite tarafından tasarlanmış tembel işlevsel dil
- **1.3 (1996)**: Tür sınıfları — Haskell'in tanımlayıcı özelliği
- **1.4 (1997)**:`IO`monad açıklandı — yan etkilerle tamamen nasıl başa çıkılacağı
- **Haskell 98**: İlk kararlı standart; bugün hala referans veriliyor
### Haskell 2010 — Modern Standart
- **2010**: Revize edilmiş standart — Cabal (paket sistemi), modül sistemi iyileştirmeleri
- GHC fiili derleyici haline gelir
- Cabal + Hackage = Haskell'in paket ekosistemi
### GHC 7.x — Sistem Gücü Türü (2011–2015)
- Tip aileleri, veri türleri, tür polimorfizmi
- Uygulamalı-Monad Teklifi (AMP) — tür sınıfı hiyerarşisinin düzeltilmesi
- Desen eş anlamlıları,`Strict`uzantısı
### GHC 8.x — Modern Haskell (2016–2020)
-`TypeApplications`— çağrı sitelerinde açık tür argümanları
- Özel tür hataları — daha iyi derleyici mesajları
- Sırt Çantası — bileşen bazlı tasarım için modül sistemi
-`DerivingVia`— esnek türetme stratejileri
### GHC 9.x — Kullanılabilirlik Devrimi (2021-günümüz)
- **9.0**: Levity polimorfizmi, doğrusal türler (kaynak güvenliği)
- **9.2**: Nitelikli `do`, iyileştirilmiş hata mesajları
- **9.4**: **GHC2021** — modern varsayılan uzantılar; `OverloadedRecordDot`(`.` ile saha erişimi)
- **9.6**: Gerekli tür bağımsız değişkenleri,`TypeAbstractions`
- **9.8–9.12**: Devam eden hata mesajı iyileştirmeleri, performans
## Söz Dizimi Gelişimi
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

## Tür Sistem Gelişimi
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

## Eşzamanlılık ve Paralellik
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Temel Tasarım İlkeleri
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Ekosistem Büyümesi
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
