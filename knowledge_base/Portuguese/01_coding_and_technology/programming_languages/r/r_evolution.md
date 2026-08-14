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
# R — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| S | 1976 | Linguagem S criada no Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Implementação Comercial S (StatSci) |
| R 0,10 | 1995 | Primeiro lançamento R (Ihaka & Gentleman, Auckland) |
| R 1,0 | 2000 | **Primeira versão estável** |
| R1.4 | 2002 | Classes e métodos S4 |
| R 2,0 | 2004 | Expressões regulares,`R.home()`|
| R2.1 | 2005 | Suporte UTF-8 |
| R 2,5 | 2007 | Melhorias no gerenciamento de memória |
| R 2,8 | 2008 | Classes de referência (OOP inicial) |
| R2.14 | 2011 | `loadNamespace`, pacote paralelo |
| R 2,15 | 2012 |  Opção`stringsAsFactors = FALSE`|
| R 3,0 | 2013 | **Suporte a 64 bits**, classes de referência estáveis ​​|
| R3.1 | 2014 |  Melhorias`vapply`|
| R3.2 | 2015 |  `readRDS`/`saveRDS`, melhorias de amostragem |
| R3.3 | 2016 |  Compressão `xz`, melhorias`person()`|
| R3.4 | 2017 | Paralelizar serialização, melhorias`switch`|
| R 3,5 | 2018 | Aviso`stringsAsFactors`padrão |
| R3.6 | 2019 | Melhorias no gerador de números aleatórios |
| R 4,0 | 2020 | **Principal**: padrão`stringsAsFactors = FALSE`|
| R4.1 | 2021 | **Pipe`|>`**, funções anônimas`\(x) ...`|
| R4.2 | 2022 | `|>`ganha espaço reservado`_`, argumento`after`em`on.exit`|
| R4.3 | 2023 |  Melhorias no `R_cmd`, melhores mensagens de erro |
| R4.4 | 2024 |  Melhorias `find()`, padrão`deparse1()`|
| R 4,5 | 2025 | Melhorias contínuas |
## Marcos importantes
### S e S-PLUS (1976–1994)
- **1976**: John Chambers cria S no Bell Labs — programação estatística como linguagem
- **1988**: S-PLUS — implementação comercial pela StatSci (mais tarde TIBCO)
- S apresenta: frames de dados, fórmulas (`y ~ x`), avaliação lenta
### Nascimento de R (1995–2000)
- **1995**: Ross Ihaka e Robert Gentleman criam R na Universidade de Auckland
- "R" = primeiras letras de Ross e Robert
- Projetado como uma implementação S gratuita e de código aberto
- **2000**: R 1.0 — primeira versão estável; CRAN (Comprehensive R Archive Network) estabelecida
### R amadurece (2000–2012)
- **1.4 (2002)**: Classes S4 — sistema OOP formal
- **2.0 (2004)**: Expressões regulares, melhorias internas
- **2.8 (2008)**: Classes de referência — POO moderno
- **2.14 (2011)**: pacote`parallel`(suporte multicore)
### R 3.x — A era da ciência de dados (2013–2019)
- **3.0 (2013)**: suporte a 64 bits — lida com grandes conjuntos de dados
- **3.1–3.6**: Melhorias incrementais
- **2013–2015**: A "Revolução R" — ggplot2, dplyr, tidyverse transformam a ciência de dados
### R 4.x - R moderno (2020-presente)
- **4.0 (2020)**:`stringsAsFactors = FALSE`por padrão — corrige um problema de décadas
- **4.1 (2021)**: **Tubo nativo`|>`**, abreviação de função anônima`\(x) x + 1`
- **4.2 (2022)**: Espaço reservado para tubo `_`, taquigrafia`\(x, y)`estabilizada
- **4.3 (2023)**: Melhores mensagens de erro (sugere correções)
- **4,4–4,5**: Refinamentos contínuos
## Evolução da Sintaxe
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

## Evolução do ecossistema de pacotes
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

## Evolução OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Princípios-chave de design
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Crescimento do Ecossistema
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
