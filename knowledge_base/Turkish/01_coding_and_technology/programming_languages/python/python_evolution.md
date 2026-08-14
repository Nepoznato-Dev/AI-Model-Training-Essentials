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
# Python — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Çıkış Tarihi | Anahtar Tema |
|-----------|---------------|-----------|
| 1.0 | Ocak 1994 | İlk sürüm |
| 1.5 | Aralık 1997 | Sınıflar, istisnalar, modüller |
| 2.0 | Ekim 2000 | Liste anlamaları, çöp toplama |
| 2.2 | Aralık 2001 | Birleşik türler (türler/sınıflar), oluşturucular |
| 2.5 | Eylül 2006 | `with`ifadesi, ifade olarak`yield`|
| 2.6 | Ekim 2008 | `bytes`,`future`içe aktarma, 3'e geçiş |
| 2.7 | Temmuz 2010 | Söyleme/ayarlama anlamaları,`argparse`|
| 3.0 | Aralık 2008 | **Kırılma**:`print()`,`str`/`bytes`, yineleyiciler |
| 3.3 | Eylül 2012 | `yield from`, ad alanı paketleri |
| 3.4 | Mart 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | Eylül 2015 | `async/await`, tür ipuçları (PEP 484),`**`paketi açma |
| 3.6 | Aralık 2016 | f-string'ler,`async`compreh, sıralı dikteler |
| 3.7 | Haziran 2018 | `dataclasses`,`contextvars`, ayrılmış`async`|
| 3.8 | Ekim 2019 | Mors operatörü `:=`, yalnızca konumsal parametreler |
| 3.9 | Ekim 2020 | Dikt birliği`|`, genel türler`list[int]`|
| 3.10 | Ekim 2021 |  `match/case`, yapısal model eşleştirme |
| 3.11 | Ekim 2022 | İstisna grupları,`Self`tipi, daha hızlı CPython |
| 3.12 | Ekim 2023 | Tercüman başına GIL hazırlığı, parametre söz dizimini yazın |
| 3.13 | Ekim 2024 | Serbest iş parçacıklı mod (deneysel), geliştirilmiş REPL |
| 3.14 | Ekim 2025 | No-GIL, ek açıklamaların istikrarlı, ertelenmiş değerlendirmesi |
## Önemli Kilometre Taşları
### Python 2.x Dönemi (2000–2020)
- **2.0**: Haskell'den ilham alan anlayışların listesi; döngüsel GC
- **2.2**:`object`temel sınıfı; `yield`anahtar kelimesi (jeneratörler)
- **2,5**:`with`ifadesi; `yield`ifadeye dönüşür
- **2.7**: Son 2.x sürümü; dikte anlamaları; `argparse`
- **Yaşam sonu**: 1 Ocak 2020
### Python 3.x Devrimi (2008 – günümüz)
- **3.0**: Temiz ara — işlev olarak `print`,`str`ve`bytes`karşılaştırması, tüm yineleyiciler görünümleri döndürür
- **3.5**:`async`/`await`sözdizimi;`typing`modülüyle ipuçları yazın
- **3.6**: f-dizeleri (en çok istenen özellik); `asyncio`stabilize edildi
- **3,8**: Satır içi atama için Mors operatörü
- **3.10**: Yapısal model eşleştirme (`match`/`case`)
- **3,11**: %10-60 daha hızlı;`except*`ile istisna grupları 
- **3.13**: Deneysel serbest iş parçacıklı mod (GIL yok)
## Tasarım Felsefesinin Evrimi
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## Python'u Şekillendiren Önemli PEP'ler
| PEP | Yıl | Özellik |
|------|------|-----------|
| 20 | 2004 | Python'un Zen'i |
| 257 | 2001 | Belgesel sözleşmeler |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Jeneratör ifadeleri |
| 342 | 2005 |  İfade olarak `yield`,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | İpuçları yazın |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-dizeleri |
| 572 | 2018 | Mors operatörü`:=`|
| 622 | 2020 | Yapısal model eşleştirme |
| 654 | 2021 | İstisna grupları |
| 684 | 2022 | Tercüman başına GIL |
| 703 | 2023 | GIL'i isteğe bağlı hale getirme |
## Performans Gelişimi
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Topluluk ve Ekosistem Büyümesi
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
