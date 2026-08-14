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
# R — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| S | 1976 | S wika na nilikha sa Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Pagpapatupad ng Commercial S (StatSci) |
| R 0.10 | 1995 | Unang R release (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **Unang stable release** |
| R 1.4 | 2002 | Mga klase at pamamaraan ng S4 |
| R 2.0 | 2004 | Mga regular na expression,`R.home()`|
| R 2.1 | 2005 | Suporta sa UTF-8 |
| R 2.5 | 2007 | Mga pagpapahusay sa pamamahala ng memorya |
| R 2.8 | 2008 | Mga reference na klase (maagang OOP) |
| R 2.14 | 2011 | `loadNamespace`, parallel package |
| R 2.15 | 2012 | `stringsAsFactors = FALSE`opsyon |
| R 3.0 | 2013 | **64-bit na suporta**, stable ang mga reference class |
| R 3.1 | 2014 | `vapply`mga pagpapabuti |
| R 3.2 | 2015 | `readRDS`/`saveRDS`, mga pagpapahusay ng sampling |
| R 3.3 | 2016 | `xz`compression,`person()`mga pagpapabuti |
| R 3.4 | 2017 | Parallelize serialization,`switch`improvements |
| R 3.5 | 2018 | Default na`stringsAsFactors`babala |
| R 3.6 | 2019 | Random number generator improvements |
| R 4.0 | 2020 | **Major**:`stringsAsFactors = FALSE`default |
| R 4.1 | 2021 | **Pipe`|>`**, anonymous na mga function`\(x) ...`|
| R 4.2 | 2022 | `|>`nakakakuha ng placeholder`_`,`after`argument sa`on.exit`|
| R 4.3 | 2023 | `R_cmd`mga pagpapabuti, mas mahusay na mga mensahe ng error |
| R 4.4 | 2024 | `find()`mga pagpapabuti,`deparse1()`default |
| R 4.5 | 2025 | Patuloy na mga pagpapabuti |
## Mga Pangunahing Milestone
### S at S-PLUS (1976–1994)
- **1976**: Si John Chambers ay lumikha ng S sa Bell Labs — statistical programming bilang isang wika
- **1988**: S-PLUS — komersyal na pagpapatupad ng StatSci (mamaya TIBCO)
- S introduces: data frame, formula (`y ~ x`), tamad na pagsusuri
### Kapanganakan ni R (1995–2000)
- **1995**: Si Ross Ihaka at Robert Gentleman ay lumikha ng R sa University of Auckland
- "R" = unang titik ni Ross at Robert
- Dinisenyo bilang isang libre, open-source na pagpapatupad ng S
- **2000**: R 1.0 — unang stable release; Itinatag ang CRAN (Comprehensive R Archive Network).
### R Matures (2000–2012)
- **1.4 (2002)**: Mga klase sa S4 — pormal na OOP system
- **2.0 (2004)**: Mga regular na expression, pinahusay na internals
- **2.8 (2008)**: Mga reference na klase — maagang modernong OOP
- **2.14 (2011)**:`parallel`package (multicore support)
### R 3.x — The Data Science Era (2013–2019)
- **3.0 (2013)**: 64-bit na suporta — pangasiwaan ang malalaking dataset
- **3.1–3.6**: Mga karagdagang pagpapabuti
- **2013–2015**: Ang "R Revolution" — ggplot2, dplyr, tidyverse transform data science
### R 4.x — Modern R (2020–kasalukuyan)
- **4.0 (2020)**:`stringsAsFactors = FALSE`bilang default — inaayos ang ilang dekada nang masakit na punto
- **4.1 (2021)**: **Native pipe`|>`**, anonymous function shorthand`\(x) x + 1`
- **4.2 (2022)**: Pipe placeholder`_`,`\(x, y)`shorthand stabilized
- **4.3 (2023)**: Mas mahusay na mga mensahe ng error (nagmumungkahi ng mga pagwawasto)
- **4.4–4.5**: Mga patuloy na pagpipino
## Syntax Evolution
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

## Package Ecosystem Evolution
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

## Ebolusyon ng OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Pangunahing Prinsipyo ng Disenyo
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Paglago ng Ecosystem
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
