---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 0,95 | 1995 | İlk sürüm (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | İlk kararlı sürüm |
| 1.2 | 1998 | İlk İngilizce belgeler |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Çöp toplama iyileştirmeleri |
| 1.8 | 2003 | $KCODE, oniguruma normal ifade motoru |
| 1.9 | 2007 | **Binbaşı**: M17N (çok dilli), yeni karma sözdizimi, lifler |
| 2.0 | 2013 | Anahtar kelime bağımsız değişkenleri,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Geliştirilmiş yöntem çağrıları,`frozen_string_literal`|
| 2.2 | 2014 | Sembol GC, artımlı GC |
| 2.3 | 2015 | Dondurulmuş dize değişmez pragma,`&.`güvenli navigasyon |
| 2.4 | 2016 | `Integer`birleştirilmiş,`String`Unicode durum eşleme |
| 2.5 | 2017 | `yield_self`,`rescue`/ `ensure`'deki bloklar |
| 2.6 | 2018 | **JIT derleyicisi (MJIT)**, sonsuz aralık`1..`|
| 2.7 | 2019 | Desen eşleştirme (deneysel), numaralandırılmış blok parametreleri |
| 3.0 | 2020 | **Ana**: Ractor (eşzamanlılık), Fiber Zamanlayıcı, RBS türleri |
| 3.1 | 2021 | `Anonymous`blok yönlendirme,`Hash#compact`|
| 3.2 | 2022 | `Data`sınıfı,`File.realpath`iyileştirmeleri, YJIT üretimi |
| 3.3 | 2023 | **YJIT** önemli iyileştirmeler,`it`blok parametresi |
| 3.4 | 2024 | Prizma ayrıştırıcı varsayılanı, varsayılan blok parametresi olarak`it`|
## Önemli Kilometre Taşları
### Erken Yakut (1995–2003)
- **1995**: Matz, Perl, Smalltalk ve Lisp'i harmanlayarak Ruby'yi yarattı
- **1.0 (1996)**: İlk kararlı sürüm
- **1.8 (2003)**: "Klasik" Ruby — hızlı, kararlı, geniş çapta benimsenmiş
### Raylar Çağı (2004–2013)
- **2004**: Ruby on Rails piyasaya sürüldü — web geliştirmede devrim
- **1.9 (2007)**: M17N (çok dilli dizeler), yeni karma sözdizimi `{key: value}`, lifler
- **2.0 (2013)**: Anahtar kelime argümanları, tembel numaralandırıcılar, `Module#prepend`
### Modern Yakut (2015 – günümüz)
- **2.6 (2018)**: JIT derleyicisi (MJIT) — ilk performans aktarımı
- **2.7 (2019)**: Desen eşleştirme (deneysel), numaralı blok parametreleri`_1`
- **3.0 (2020)**: **Ractor** (Aktör-model eşzamanlılığı), **Fiber Scheduler** (eşzamansız G/Ç), **RBS** (imza türü)
- **3.2 (2022)**:`Data`sınıfı (değişmez değer nesneleri), YJIT üretime hazır
- **3,3 (2023)**: YJIT büyük hızlanmalar (3 kata kadar daha hızlı),`it`blok parametresi
- **3.4 (2024)**: Prizma ayrıştırıcı varsayılan hale gelir
## Performans Gelişimi
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## Eşzamanlılık Gelişimi
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Desen Eşleştirme Evrimi
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Temel Tasarım İlkeleri
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Ekosistem Büyümesi
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
