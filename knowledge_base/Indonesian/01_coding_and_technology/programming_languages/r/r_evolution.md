---
# Metadata
title: "R — Version History & Evolution"
description: "Comprehensive version history and evolution of R from S-Plus origins to modern R."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# R — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| S | 1976 | Bahasa S dibuat di Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Implementasi S Komersial (StatSci) |
| R 0,10 | 1995 | Rilisan R pertama (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **Rilis stabil pertama** |
| R 1.4 | 2002 | Kelas dan metode S4 |
| R 2.0 | 2004 | Ekspresi reguler,`R.home()`|
| R 2.1 | 2005 | Dukungan UTF-8 |
| R 2.5 | 2007 | Peningkatan manajemen memori |
| R 2.8 | 2008 | Kelas referensi (OOP awal) |
| R 2.14 | 2011 | `loadNamespace`, paket paralel |
| R 2.15 | 2012 |  Opsi`stringsAsFactors = FALSE`|
| R 3.0 | 2013 | **Dukungan 64-bit**, kelas referensi stabil |
| R 3.1 | 2014 |  Peningkatan`vapply`|
| R 3.2 | 2015 | `readRDS`/`saveRDS`, peningkatan pengambilan sampel |
| R 3.3 | 2016 |  Kompresi `xz`, peningkatan`person()`|
| R 3.4 | 2017 | Paralelkan serialisasi, peningkatan`switch`|
| R 3,5 | 2018 | Peringatan`stringsAsFactors`bawaan |
| R 3.6 | 2019 | Peningkatan penghasil angka acak |
| R 4.0 | 2020 | **Mayor**:`stringsAsFactors = FALSE`default |
| R 4.1 | 2021 | **Pipa`|>`**, fungsi anonim`\(x) ...`|
| R 4.2 | 2022 | `|>`mendapatkan argumen placeholder`_`,`after`di`on.exit`|
| R 4.3 | 2023 |  Peningkatan `R_cmd`, pesan kesalahan yang lebih baik |
| R 4.4 | 2024 |  Peningkatan `find()`,`deparse1()`default |
| R 4.5 | 2025 | Perbaikan berkelanjutan |
## Tonggak Penting
### S dan S-PLUS (1976–1994)
- **1976**: John Chambers menciptakan S di Bell Labs — pemrograman statistik sebagai sebuah bahasa
- **1988**: S-PLUS — implementasi komersial oleh StatSci (kemudian TIBCO)
- S memperkenalkan: bingkai data, rumus (`y ~ x`), evaluasi malas
### Kelahiran R (1995–2000)
- **1995**: Ross Ihaka dan Robert Gentleman menciptakan R di Universitas Auckland
- "R" = huruf pertama Ross dan Robert
- Dirancang sebagai implementasi S sumber terbuka dan gratis
- **2000**: R 1.0 — rilis stabil pertama; CRAN (Jaringan Arsip R Komprehensif) didirikan
### R Jatuh Tempo (2000–2012)
- **1.4 (2002)**: Kelas S4 — sistem OOP formal
- **2.0 (2004)**: Ekspresi reguler, peningkatan internal
- **2.8 (2008)**: Kelas referensi — OOP modern awal
- **2.14 (2011)**: Paket`parallel`(dukungan multicore)
### R 3.x - Era Ilmu Data (2013–2019)
- **3.0 (2013)**: dukungan 64-bit — menangani kumpulan data besar
- **3.1–3.6**: Peningkatan bertahap
- **2013–2015**: "R Revolution" — ggplot2, dplyr, ilmu data transformasi rapiverse
### R 4.x — R Modern (2020–sekarang)
- **4.0 (2020)**:`stringsAsFactors = FALSE`secara default — memperbaiki masalah yang sudah berlangsung puluhan tahun
- **4.1 (2021)**: **Pipa asli`|>`**, singkatan fungsi anonim`\(x) x + 1`
- **4.2 (2022)**: Pengganti pipa`_`, singkatan`\(x, y)`distabilkan
- **4.3 (2023)**: Pesan kesalahan yang lebih baik (menyarankan koreksi)
- **4.4–4.5**: Penyempurnaan lanjutan
## Evolusi Sintaks
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

## Paket Evolusi Ekosistem
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

## Evolusi OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Prinsip Desain Utama
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Pertumbuhan Ekosistem
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
