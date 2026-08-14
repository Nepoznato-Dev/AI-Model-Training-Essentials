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
# R — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| S | 1976 | Langage S créé aux Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Implémentation commerciale S (StatSci) |
| R 0,10 | 1995 | Première version R (Ihaka & Gentleman, Auckland) |
| R1.0 | 2000 | **Première version stable** |
| R 1.4 | 2002 | Cours et méthodes S4 |
| R2.0 | 2004 | Expressions régulières,`R.home()`|
| R 2.1 | 2005 | Prise en charge UTF-8 |
| R 2,5 | 2007 | Améliorations de la gestion de la mémoire |
| R 2.8 | 2008 | Classes de référence (début POO) |
| R 2.14 | 2011 | `loadNamespace`, package parallèle |
| R 2.15 | 2012 |  Option`stringsAsFactors = FALSE`|
| R3.0 | 2013 | **Prise en charge 64 bits**, classes de référence stables |
| R 3.1 | 2014 |  Améliorations`vapply`|
| R 3.2 | 2015 | `readRDS`/`saveRDS`, améliorations de l'échantillonnage |
| R 3.3 | 2016 |  Compression `xz`, améliorations`person()`|
| R 3.4 | 2017 | Paralléliser la sérialisation, améliorations`switch`|
| R 3,5 | 2018 | Avertissement`stringsAsFactors`par défaut |
| R 3.6 | 2019 | Améliorations du générateur de nombres aléatoires |
| R4.0 | 2020 | **Majeur** :`stringsAsFactors = FALSE`par défaut |
| R 4.1 | 2021 | **Tuyau`|>`**, fonctions anonymes`\(x) ...`|
| R 4.2 | 2022 | `|>`obtient l'argument fictif`_`,`after`dans`on.exit`|
| R 4.3 | 2023 |  Améliorations `R_cmd`, meilleurs messages d'erreur |
| R 4.4 | 2024 |  Améliorations de `find()`,`deparse1()`par défaut |
| R4.5 | 2025 | Améliorations continues |
## Étapes majeures
### S et S-PLUS (1976-1994)
- **1976** : John Chambers crée S aux Bell Labs — la programmation statistique comme langage
- **1988** : S-PLUS — implémentation commerciale par StatSci (plus tard TIBCO)
- S introduit : trames de données, formules (`y ~ x`), évaluation paresseuse
### Naissance de R (1995-2000)
- **1995** : Ross Ihaka et Robert Gentleman créent R à l'Université d'Auckland
- "R" = premières lettres de Ross et Robert
- Conçu comme une implémentation S gratuite et open source
- **2000** : R 1.0 — première version stable ; Création du CRAN (Comprehensive R Archive Network)
### R Mûrit (2000-2012)
- **1.4 (2002)** : classes S4 — système POO formel
- **2.0 (2004)** : expressions régulières, composants internes améliorés
- **2.8 (2008)** : Classes de référence — POO moderne
- **2.14 (2011)** : package`parallel`(support multicœur)
### R 3.x — L'ère de la science des données (2013-2019)
- **3.0 (2013)** : prise en charge 64 bits – gérer de grands ensembles de données
- **3.1–3.6** : améliorations incrémentielles
- **2013-2015** : La « Révolution R » — ggplot2, dplyr, spiceverse transforme la science des données
### R 4.x — R moderne (2020-présent)
- **4.0 (2020)** :`stringsAsFactors = FALSE`par défaut – corrige un problème vieux de plusieurs décennies
- **4.1 (2021)** : **Tube natif`|>`**, raccourci de fonction anonyme`\(x) x + 1`
- **4.2 (2022)** : espace réservé au tuyau `_`, raccourci`\(x, y)`stabilisé
- **4.3 (2023)** : Meilleurs messages d'erreur (suggère des corrections)
- **4.4–4.5** : améliorations continues
## Évolution de la syntaxe
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

## Évolution de l'écosystème des packages
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

## Évolution de la POO
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Principes de conception clés
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Croissance de l'écosystème
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
