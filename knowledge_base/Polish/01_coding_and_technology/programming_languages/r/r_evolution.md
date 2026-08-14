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
# R — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| S | 1976 | Język S stworzony w Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Komercyjne wdrożenie S (StatSci) |
| R 0,10 | 1995 | Pierwsze wydanie R (Ihaka & Gentleman, Auckland) |
| R 1,0 | 2000 | **Pierwsza stabilna wersja** |
| R 1,4 | 2002 | Klasy i metody S4 |
| R 2,0 | 2004 | Wyrażenia regularne,`R.home()`|
| R 2.1 | 2005 | Obsługa UTF-8 |
| R 2,5 | 2007 | Ulepszenia zarządzania pamięcią |
| R 2,8 | 2008 | Klasy referencyjne (wczesne OOP) |
| R 2.14 | 2011 | `loadNamespace`, pakiet równoległy |
| R 2,15 | 2012 |  Opcja`stringsAsFactors = FALSE`|
| R 3,0 | 2013 | **Obsługa 64-bitowa**, klasy referencyjne stabilne |
| R 3.1 | 2014 |  Ulepszenia`vapply`|
| R 3.2 | 2015 | `readRDS`/`saveRDS`, ulepszenia próbkowania |
| R 3.3 | 2016 |  Kompresja `xz`, ulepszenia`person()`|
| R 3,4 | 2017 | Serializacja równoległa, ulepszenia`switch`|
| R 3,5 | 2018 | Domyślne ostrzeżenie`stringsAsFactors`|
| R 3,6 | 2019 | Ulepszenia generatora liczb losowych |
| R 4,0 | 2020 | **Główny**: domyślny`stringsAsFactors = FALSE`|
| R 4.1 | 2021 | **Rura`|>`**, funkcje anonimowe`\(x) ...`|
| R 4.2 | 2022 | `|>`zyskuje symbol zastępczy`_`, argument`after`w`on.exit`|
| R 4.3 | 2023 |  Ulepszenia `R_cmd`, lepsze komunikaty o błędach |
| R 4,4 | 2024 |  Ulepszenia `find()`, domyślne`deparse1()`|
| R 4,5 | 2025 | Ciągłe ulepszenia |
## Główne kamienie milowe
### S i S-PLUS (1976–1994)
- **1976**: John Chambers tworzy S w Bell Labs — programowanie statystyczne jako język
- **1988**: S-PLUS — wdrożenie komercyjne przez StatSci (później TIBCO)
- S wprowadza: ramki danych, formuły (`y ~ x`), leniwą ocenę
### Narodziny R (1995–2000)
- **1995**: Ross Ihaka i Robert Gentleman tworzą R na Uniwersytecie w Auckland
- „R” = pierwsze litery Rossa i Roberta
- Zaprojektowany jako darmowa implementacja S o otwartym kodzie źródłowym
- **2000**: R 1.0 — pierwsze wydanie stabilne; Utworzono CRAN (kompleksową sieć archiwów R).
### R Dojrzewa (2000–2012)
- **1,4 (2002)**: Klasy S4 — formalny system OOP
- **2.0 (2004)**: Wyrażenia regularne, ulepszone elementy wewnętrzne
- **2,8 (2008)**: Klasy referencyjne — wczesne nowożytne OOP
- **2.14 (2011)**: Pakiet`parallel`(obsługa wielu rdzeni)
### R 3.x — era nauki o danych (2013–2019)
- **3.0 (2013)**: obsługa wersji 64-bitowej — obsługa dużych zbiorów danych
- **3,1–3,6**: Stopniowe ulepszenia
- **2013–2015**: „Rewolucja R” — ggplot2, dplyr, tidyverse transformacja analityki danych
### R 4.x — Modern R (2020 – obecnie)
- **4.0 (2020)**: domyślnie`stringsAsFactors = FALSE`— naprawia problem występujący od kilkudziesięciu lat
- **4.1 (2021)**: **Natywny potok`|>`**, skrót funkcji anonimowej`\(x) x + 1`
- **4.2 (2022)**: Symbol zastępczy rury `_`, `\(x, y)`, stabilizowany w skrócie
- **4.3 (2023)**: Lepsze komunikaty o błędach (sugerują poprawki)
- **4,4–4,5**: Dalsze udoskonalenia
## Ewolucja składni
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

## Ewolucja ekosystemu pakietu
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

## Ewolucja OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Kluczowe zasady projektowania
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Rozwój ekosystemu
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
