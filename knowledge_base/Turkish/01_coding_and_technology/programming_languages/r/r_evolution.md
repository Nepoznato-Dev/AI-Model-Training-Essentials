<!--
---
# Metadata
title: "R — Version History & Evolution"
description: "Comprehensive version history and evolution of R from S-Plus origins to modern R."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [r, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# R — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| S | 1976 | S dili Bell Laboratuvarlarında (Becker, Chambers, Wilks) oluşturuldu |
| S-PLUS | 1988 | Ticari S uygulaması (StatSci) |
| R 0.10 | 1995 | İlk R sürümü (Ihaka & Gentleman, Auckland) |
| R1.0 | 2000 | **İlk kararlı sürüm** |
| R1.4 | 2002 | S4 sınıfları ve yöntemleri |
| R2.0 | 2004 | Düzenli ifadeler,`R.home()`|
| R2.1 | 2005 | UTF-8 desteği |
| R2.5 | 2007 | Bellek yönetimi iyileştirmeleri |
| R2.8 | 2008 | Referans sınıfları (erken OOP) |
| R2.14 | 2011 | `loadNamespace`, paralel paket |
| R2.15 | 2012 | `stringsAsFactors = FALSE`seçeneği |
| R3.0 | 2013 | **64 bit desteği**, referans sınıfları kararlı |
| R3.1 | 2014 | `vapply`iyileştirmeleri |
| R3.2 | 2015 | `readRDS`/ `saveRDS`, örnekleme iyileştirmeleri |
| R3.3 | 2016 | `xz`sıkıştırma,`person()`iyileştirmeleri |
| R3.4 | 2017 | Serileştirmeyi paralelleştirme,`switch`iyileştirmeleri |
| R3.5 | 2018 | Varsayılan`stringsAsFactors`uyarısı |
| R3.6 | 2019 | Rastgele sayı üreteci iyileştirmeleri |
| R4.0 | 2020 | **Binbaşı**:`stringsAsFactors = FALSE`varsayılan |
| R4.1 | 2021 | **Boru`|>`**, anonim işlevler`\(x) ...`|
| R4.2 | 2022 |  `|>`,`on.exit`|
| R4.3 | 2023 | `R_cmd`iyileştirmeleri, daha iyi hata mesajları |
| R4.4 | 2024 | `find()`iyileştirmeleri,`deparse1()`varsayılan |
| R4.5 | 2025 | Devam eden iyileştirmeler |
## Önemli Kilometre Taşları
### S ve S-PLUS (1976–1994)
- **1976**: John Chambers, Bell Laboratuvarlarında S'yi yarattı — dil olarak istatistiksel programlama
- **1988**: S-PLUS — StatSci (daha sonra TIBCO) tarafından ticari uygulama
- S şunları sunar: veri çerçeveleri, formüller (`y ~ x`), tembel değerlendirme
### R'nin Doğuşu (1995–2000)
- **1995**: Ross Ihaka ve Robert Gentleman, Auckland Üniversitesi'nde R'yi yarattı
- "R" = Ross ve Robert'ın baş harfleri
- Ücretsiz, açık kaynaklı bir S uygulaması olarak tasarlandı
- **2000**: R 1.0 — ilk kararlı sürüm; CRAN (Kapsamlı R Arşiv Ağı) kuruldu
### R Olgunlaşır (2000–2012)
- **1.4 (2002)**: S4 sınıfları — resmi OOP sistemi
- **2.0 (2004)**: Düzenli ifadeler, geliştirilmiş dahili özellikler
- **2.8 (2008)**: Referans sınıfları — erken modern OOP
- **2.14 (2011)**:`parallel`paketi (çoklu çekirdek desteği)
### R 3.x — Veri Bilimi Çağı (2013–2019)
- **3.0 (2013)**: 64 bit desteği — büyük veri kümelerini yönetin
- **3,1–3,6**: Artan iyileştirmeler
- **2013–2015**: "R Devrimi" — ggplot2, dplyr, tidyverse dönüşüm veri bilimi
### R 4.x — Modern R (2020-günümüz)
- **4.0 (2020)**: Varsayılan olarak`stringsAsFactors = FALSE`— onlarca yıllık sorun noktasını düzeltir
- **4.1 (2021)**: **Yerel kanal`|>`**, anonim işlev kısayolu`\(x) x + 1`
- **4.2 (2022)**: Boru yer tutucusu`_`,`\(x, y)`kısaltılmış olarak stabilize edilmiş
- **4.3 (2023)**: Daha iyi hata mesajları (düzeltme önerileri)
- **4,4–4,5**: Devam eden iyileştirmeler
## Söz Dizimi Gelişimi
```r
# S / early R: Basic statistics
x <- c(1, 2, 3, 4, 5)
mean(x)
lm(y ~ x, data = df)

# R 3.x: tidyverse revolution (2013+)
library(dplyr)
library(ggplot2)
df %>%
  filter(age > 18) %>%
  group_by(category) %>%
  summarise(mean_age = mean(age))

# R 4.0: stringsAsFactors default changes
df <- read.csv("data.csv")  # strings no longer auto-converted to factors

# R 4.1: Native pipe and lambda shorthand
df |>
  filter(age > 18) |>
  mutate(label = \(x) paste(x$name, x$age))

# R 4.2: Pipe placeholder
result |> (\(x) x[is.na(x)] <- 0)()
# With placeholder:
x |> f(y = _)

# R 4.3+: Better error messages
mean("hello")
# Warning: In mean.default("hello") : argument is not numeric or logical: returning NA
```

## Paket Ekosistem Evrimi
```
1995: R launches with basic stats packages
2000: CRAN established — centralized package repository
2001: Bioconductor — bioinformatics packages
2007: ggplot2 released (Hadley Wickham) — grammar of graphics
2008: reshape2 — data reshaping
2012: dplyr released — fast data manipulation
2014: tidyr, readr — complete data science toolkit
2015: tidyverse meta-package — unified ecosystem
2016: RMarkdown — literate programming
2019: Quarto — next-gen documents
2020: RStudio → Posit — company rebrands, broader tooling
2025: 20,000+ packages on CRAN; R is the #1 statistical language
```

## OOP Evrimi
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Temel Tasarım İlkeleri
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Ekosistem Büyümesi
```
1995: R created at University of Auckland
2000: CRAN established — package repository
2003: Bioconductor — bioinformatics ecosystem
2007: ggplot2 — revolutionizes data visualization
2012: dplyr — modern data manipulation
2014: tidyverse — unified data science toolkit
2015: RMarkdown — reproducible research
2020: R 4.0 — modern defaults
2021: R 4.1 — native pipe |>
2025: R remains dominant in statistics, bioinformatics, and academia
       20,000+ CRAN packages; used by pharma, finance, research
```
