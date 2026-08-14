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
# R: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| S | 1976 | Linguaggio S creato presso i Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Implementazione S commerciale (StatSci) |
| R 0,10 | 1995 | Prima uscita R (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **Prima versione stabile** |
| R1.4 | 2002| Classi e metodi S4 |
| R2.0 | 2004| Espressioni regolari,`R.home()`|
| R2.1 | 2005| Supporto UTF-8 |
| R 2,5 | 2007| Miglioramenti nella gestione della memoria |
| R2.8 | 2008| Classi di riferimento (inizio OOP) |
| R 2.14 | 2011 | `loadNamespace`, pacchetto parallelo |
| R 2,15 | 2012|  Opzione`stringsAsFactors = FALSE`|
| R3.0 | 2013| **Supporto a 64 bit**, classi di riferimento stabili |
| R3.1 | 2014| `vapply`miglioramenti |
| R3.2 | 2015| `readRDS`/`saveRDS`, miglioramenti al campionamento |
| R3.3 | 2016|  Compressione `xz`, miglioramenti`person()`|
| R3.4 | 2017 | Parallelizza la serializzazione, miglioramenti`switch`|
| R 3,5 | 2018 | Avviso`stringsAsFactors`predefinito |
| R3.6 | 2019 | Miglioramenti al generatore di numeri casuali |
| R4.0| 2020 | **Maggiore**:`stringsAsFactors = FALSE`predefinito |
| R4.1 | 2021 | **Pipa`|>`**, funzioni anonime`\(x) ...`|
| R4.2 | 2022 | `|>`ottiene l'argomento segnaposto`_`,`after`in`on.exit`|
| R4.3 | 2023 |  Miglioramenti `R_cmd`, migliori messaggi di errore |
| R4.4 | 2024 |  Miglioramenti `find()`,`deparse1()`predefinito |
| R 4,5 | 2025 | Miglioramenti continui |
## Traguardi importanti
### S e S-PLUS (1976-1994)
- **1976**: John Chambers crea S ai Bell Labs: programmazione statistica come linguaggio
- **1988**: S-PLUS — implementazione commerciale da parte di StatSci (poi TIBCO)
- S introduce: frame di dati, formule (`y ~ x`), valutazione pigra
### Nascita di R (1995–2000)
- **1995**: Ross Ihaka e Robert Gentleman creano R all'Università di Auckland
- "R" = prime lettere di Ross e Robert
- Progettato come implementazione S gratuita e open source
- **2000**: R 1.0 — prima versione stabile; Viene istituito il CRAN (Comprehensive R Archive Network).
### R matura (2000–2012)
- **1.4 (2002)**: classi S4 — sistema OOP formale
- **2.0 (2004)**: Espressioni regolari, interni migliorati
- **2.8 (2008)**: Classi di riferimento - OOP della prima età moderna
- **2.14 (2011)**: pacchetto`parallel`(supporto multicore)
### R 3.x — L'era della scienza dei dati (2013-2019)
- **3.0 (2013)**: supporto a 64 bit: gestisce set di dati di grandi dimensioni
- **3.1–3.6**: miglioramenti incrementali
- **2013–2015**: La "Rivoluzione R" — ggplot2, dplyr, tidyverse trasformano la scienza dei dati
### R 4.x - R moderna (2020-presente)
- **4.0 (2020)**:`stringsAsFactors = FALSE`per impostazione predefinita: risolve un punto dolente vecchio di decenni
- **4.1 (2021)**: **Pipe nativa`|>`**, abbreviazione di funzione anonima`\(x) x + 1`
- **4.2 (2022)**: segnaposto per tubi `_`,`\(x, y)`stabilizzato per abbreviazione
- **4.3 (2023)**: messaggi di errore migliorati (suggerisce correzioni)
- **4.4–4.5**: perfezionamenti continui
## Evoluzione della sintassi
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

## Pacchetto Evoluzione dell'ecosistema
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

## Evoluzione OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Principi chiave di progettazione
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Crescita dell'ecosistema
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
