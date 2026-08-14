<!--
---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Python — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tanggal Rilis | Tema Utama |
|---------|-------------|-----------|
| 1.0 | Januari 1994 | Rilis awal |
| 1.5 | Desember 1997 | Kelas, pengecualian, modul |
| 2.0 | Oktober 2000 | Pemahaman daftar, pengumpulan sampah |
| 2.2 | Desember 2001 | Tipe terpadu (tipe/kelas), generator |
| 2.5 | September 2006 |  Pernyataan `with`,`yield`sebagai ekspresi |
| 2.6 | Oktober 2008 | `bytes`,`future`impor, transisi ke 3 |
| 2.7 | Juli 2010 | Pemahaman dikte/set,`argparse`|
| 3.0 | Desember 2008 | **Melanggar**:`print()`,`str`/`bytes`, iterator |
| 3.3 | September 2012 | `yield from`, paket namespace |
| 3.4 | Maret 2014 | `asyncio`,`pathlib`,`enum`|
| 3,5 | September 2015 | `async/await`, ketik petunjuk (PEP 484),`**`membongkar |
| 3.6 | Desember 2016 | f-string, pemahaman `async`, dicts terurut |
| 3.7 | Juni 2018 | `dataclasses`,`contextvars`, dipesan`async`|
| 3.8 | Oktober 2019 | Operator Walrus`:=`, parameter khusus posisi |
| 3.9 | Oktober 2020 | Persatuan dict`|`, tipe generik`list[int]`|
| 3.10 | Oktober 2021 |  `match/case`, pencocokan pola struktural |
| 3.11 | Oktober 2022 | Grup pengecualian, tipe `Self`, CPython |
| 3.12 | Oktober 2023 | Persiapan GIL per juru bahasa, ketik sintaks parameter |
| 3.13 | Oktober 2024 | Mode berulir bebas (eksperimental), REPL | yang ditingkatkan
| 3.14 | Oktober 2025 | Evaluasi anotasi yang stabil dan ditangguhkan tanpa GIL |
## Tonggak Penting
### Python 2.x Era (2000–2020)
- **2.0**: Daftar pemahaman yang terinspirasi oleh Haskell; GC siklik
- **2.2**: kelas dasar `object`;  Kata kunci`yield`(generator)
- **2.5**: pernyataan `with`; `yield`menjadi ekspresi
- **2.7**: Rilis 2.x terakhir; pemahaman dikte; `argparse`
- **Akhir masa pakai**: 1 Januari 2020
### Revolusi Python 3.x (2008–sekarang)
- **3.0**: Clean break —`print`sebagai fungsi,`str`vs`bytes`, semua iterator mengembalikan tampilan
- **3.5**: Sintaks`async`/ `await`; ketik petunjuk dengan modul `typing`
- **3.6**: f-string (fitur yang paling banyak diminta); `asyncio`stabil
- **3.8**: Operator Walrus untuk penugasan inline
- **3.10**: Pencocokan pola struktural (`match`/`case`)
- **3.11**: 10-60% lebih cepat; grup pengecualian dengan`except*`
- **3.13**: Mode thread bebas eksperimental (tanpa GIL)
## Evolusi Filsafat Desain
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP Kunci yang Membentuk Python
| PEP | Tahun | Fitur |
|------|------|---------|
| 20 | 2004 | Zen dari Python |
| 257 | 2001 | Konvensi Docstring |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Ekspresi pembangkit |
| 342 | 2005 | `yield`sebagai ekspresi,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Ketik petunjuk |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-string |
| 572 | 2018 | Operator Walrus`:=`|
| 622 | 2020 | Pencocokan pola struktural |
| 654 | 2021 | Grup pengecualian |
| 684 | 2022 | Per-penerjemah GIL |
| 703 | 2023 | Menjadikan GIL opsional |
## Evolusi Kinerja
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Pertumbuhan Komunitas & Ekosistem
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
