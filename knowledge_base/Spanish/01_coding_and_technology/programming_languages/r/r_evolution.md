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

# R - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| S | 1976 | Lenguaje S creado en Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Implementación comercial S (StatSci) |
| 0,10 rands | 1995 | Primer lanzamiento de R (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **Primera versión estable** |
| R 1.4 | 2002 | Clases y métodos de S4 |
| R 2.0 | 2004 | Expresiones regulares,`R.home()`|
| R 2.1 | 2005 | Soporte UTF-8 |
| R 2,5 | 2007 | Mejoras en la gestión de la memoria |
| R 2,8 | 2008 | Clases de referencia (POO temprana) |
| R 2,14 | 2011 |  `loadNamespace`, paquete paralelo |
| 2,15 rands | 2012 |  Opción`stringsAsFactors = FALSE`|
| R3.0 | 2013 | **Soporte de 64 bits**, clases de referencia estables |
| R 3.1 | 2014 |  Mejoras`vapply`|
| R 3.2 | 2015 | `readRDS`/`saveRDS`, mejoras de muestreo |
| R 3.3 | 2016 |  Compresión `xz`, mejoras`person()`|
| R3.4 | 2017 | Paralelizar serialización, mejoras`switch`|
| R 3,5 | 2018 | Advertencia`stringsAsFactors`predeterminada |
| R3.6 | 2019 | Mejoras en el generador de números aleatorios |
| R4.0 | 2020 | **Principal**:`stringsAsFactors = FALSE`predeterminado |
| R 4.1 | 2021 | **Tubería`|>`**, funciones anónimas`\(x) ...`|
| R 4.2 | 2022 | `|>`gana el argumento `_`,`after`en`on.exit`|
| R 4.3 | 2023 |  Mejoras `R_cmd`, mejores mensajes de error |
| R 4.4 | 2024 |  Mejoras `find()`,`deparse1()`predeterminado |
| R 4,5 | 2025 | Mejoras continuas |
## Hitos importantes
### S y S-PLUS (1976–1994)
- **1976**: John Chambers crea S en Bell Labs: programación estadística como lenguaje
- **1988**: S-PLUS — implementación comercial por StatSci (más tarde TIBCO)
- S introduce: marcos de datos, fórmulas (`y ~ x`), evaluación diferida
### Nacimiento de R (1995-2000)
- **1995**: Ross Ihaka y Robert Gentleman crean R en la Universidad de Auckland
- "R" = primeras letras de Ross y Robert
- Diseñado como una implementación S gratuita y de código abierto.
- **2000**: R 1.0 — primera versión estable; Se establece CRAN (Red integral de archivos R)
### R madura (2000-2012)
- **1.4 (2002)**: Clases S4: sistema formal de programación orientada a objetos
- **2.0 (2004)**: Expresiones regulares, componentes internos mejorados
- **2.8 (2008)**: Clases de referencia: programación orientada a objetos moderna temprana
- **2.14 (2011)**: paquete`parallel`(soporte multinúcleo)
### R 3.x: la era de la ciencia de datos (2013-2019)
- **3.0 (2013)**: compatibilidad con 64 bits: maneja grandes conjuntos de datos
- **3.1–3.6**: mejoras incrementales
- **2013–2015**: La "Revolución R": ggplot2, dplyr y tidyverse transforman la ciencia de datos
### R 4.x — R moderno (2020-presente)
- **4.0 (2020)**:`stringsAsFactors = FALSE`de forma predeterminada: soluciona un problema de décadas de antigüedad
- **4.1 (2021)**: **Tubería nativa`|>`**, abreviatura de función anónima`\(x) x + 1`
- **4.2 (2022)**: Marcador de posición de tubería `_`,`\(x, y)`estabilizado taquigráficamente
- **4.3 (2023)**: Mejores mensajes de error (sugiere correcciones)
- **4.4–4.5**: mejoras continuas
## Evolución de la sintaxis
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

## Evolución del ecosistema del paquete
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

## Evolución de la programación orientada a objetos
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Principios clave de diseño
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Crecimiento del ecosistema
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
