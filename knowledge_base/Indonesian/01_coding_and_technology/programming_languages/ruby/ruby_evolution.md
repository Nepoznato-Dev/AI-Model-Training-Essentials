<!--
---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Ruby — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 0,95 | 1995 | Rilis awal (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Rilis stabil pertama |
| 1.2 | 1998 | Dokumentasi bahasa Inggris pertama |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Perbaikan pengumpulan sampah |
| 1.8 | 2003 | $KCODE, mesin regex oniguruma |
| 1.9 | 2007 | **Mayor**: M17N (multibahasa), sintaksis hash baru, serat |
| 2.0 | 2013 | Argumen kata kunci,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Panggilan metode yang disempurnakan,`frozen_string_literal`|
| 2.2 | 2014 | Simbol GC, GC tambahan |
| 2.3 | 2015 | Pragma literal string beku, navigasi aman`&.`|
| 2.4 | 2016 | `Integer`terpadu, pemetaan kasus Unicode`String`|
| 2.5 | 2017 | `yield_self`, blok di`rescue`/`ensure`|
| 2.6 | 2018 | **Kompilator JIT (MJIT)**, rentang tak berujung`1..`|
| 2.7 | 2019 | Pencocokan pola (eksperimental), parameter blok bernomor |
| 3.0 | 2020 | **Mayor**: Ractor (konkurensi), Penjadwal Fiber, tipe RBS |
| 3.1 | 2021 |  Penerusan blok `Anonymous`,`Hash#compact`|
| 3.2 | 2022 |  Kelas `Data`, peningkatan `File.realpath`, produksi YJIT |
| 3.3 | 2023 | **YJIT** peningkatan besar, parameter blok`it`|
| 3.4 | 2024 | Parser prisma default,`it`sebagai parameter blok default |
## Tonggak Penting
### Ruby Awal (1995–2003)
- **1995**: Matz menciptakan Ruby — memadukan Perl, Smalltalk, Lisp
- **1.0 (1996)**: Rilis stabil pertama
- **1.8 (2003)**: Ruby "klasik" — cepat, stabil, diadopsi secara luas
### Era Rel (2004–2013)
- **2004**: Ruby on Rails dirilis — revolusi pengembangan web
- **1.9 (2007)**: M17N (string multibahasa), sintaksis hash baru`{key: value}`, serat
- **2.0 (2013)**: Argumen kata kunci, enumerator malas, `Module#prepend`
### Ruby Modern (2015–sekarang)
- **2.6 (2018)**: Kompiler JIT (MJIT) — peningkatan kinerja pertama
- **2.7 (2019)**: Pencocokan pola (eksperimental), parameter blok bernomor`_1`
- **3.0 (2020)**: **Ractor** (konkurensi model aktor), **Fiber Scheduler** (async I/O), **RBS** (ketik tanda tangan)
- **3.2 (2022)**: Kelas`Data`(objek nilai yang tidak dapat diubah), siap produksi YJIT
- **3.3 (2023)**: Peningkatan kecepatan mayor YJIT (hingga 3x lebih cepat), parameter blok `it`
- **3.4 (2024)**: Pengurai prisma menjadi default
## Evolusi Kinerja
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

## Evolusi Konkurensi
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Evolusi Pencocokan Pola
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Prinsip Desain Utama
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Pertumbuhan Ekosistem
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
