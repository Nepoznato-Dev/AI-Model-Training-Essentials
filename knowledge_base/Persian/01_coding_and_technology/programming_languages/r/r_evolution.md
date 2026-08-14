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
# R - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| S | 1976 | زبان S ایجاد شده در آزمایشگاه های بل (Becker، Chambers، Wilks) |
| S-PLUS | 1988 | پیاده سازی Commercial S (StatSci) |
| R 0.10 | 1995 | اولین نسخه R (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **اولین انتشار پایدار** |
| R 1.4 | 2002 | کلاس ها و روش های S4 |
| R 2.0 | 2004 | عبارات منظم،`R.home()`|
| R 2.1 | 2005 | پشتیبانی UTF-8 |
| R 2.5 | 2007 | بهبود مدیریت حافظه |
| R 2.8 | 2008 | کلاس های مرجع (OOP اولیه) |
| R 2.14 | 2011 | `loadNamespace`, بسته موازی |
| R 2.15 | 2012 |  گزینه`stringsAsFactors = FALSE`|
| R 3.0 | 2013 | **پشتیبانی 64 بیتی**، کلاس های مرجع پایدار |
| R 3.1 | 2014 |  بهبودهای`vapply`|
| R 3.2 | 2015 | `readRDS`/ `saveRDS`، بهبود نمونه |
| R 3.3 | 2016 |  فشرده سازی `xz`، بهبود`person()`|
| R 3.4 | 2017 | موازی سازی سریال سازی، بهبودهای`switch`|
| R 3.5 | 2018 | هشدار پیش فرض`stringsAsFactors`|
| R 3.6 | 2019 | بهبود مولد اعداد تصادفی |
| R 4.0 | 2020 | **مهم**: پیش فرض`stringsAsFactors = FALSE`|
| R 4.1 | 2021 | **لوله`|>`**، توابع ناشناس`\(x) ...`|
| R 4.2 | 2022 | `|>`در`on.exit`جای‌بانی به دست آورد `_`، آرگومان`after`|
| R 4.3 | 2023 |  بهبود `R_cmd`، پیام های خطای بهتر |
| R 4.4 | 2024 |  بهبودهای `find()`، پیش فرض`deparse1()`|
| R 4.5 | 2025 | بهبودهای در حال انجام |
## نقاط عطف اصلی
### S و S-PLUS (1976–1994)
- **1976**: جان چمبرز S را در آزمایشگاه بل ایجاد کرد - برنامه نویسی آماری به عنوان یک زبان
- **1988**: S-PLUS - پیاده سازی تجاری توسط StatSci (بعدها TIBCO)
- S معرفی می کند: فریم های داده، فرمول ها (`y ~ x`)، ارزیابی تنبل
### تولد R (1995–2000)
- **1995**: راس ایهاکا و رابرت جنتلمن R را در دانشگاه اوکلند ایجاد کردند.
- "ر" = حروف اول راس و رابرت
- به عنوان یک پیاده سازی رایگان و منبع باز S طراحی شده است
- **2000**: R 1.0 — اولین نسخه پایدار. CRAN (شبکه آرشیو جامع R) تاسیس شد
### R Matures (2000–2012)
- **1.4 (2002)**: کلاس های S4 — سیستم OOP رسمی
- **2.0 (2004)**: عبارات منظم، داخلی های بهبود یافته
- **2.8 (2008)**: کلاس های مرجع - OOP مدرن اولیه
- **2.14 (2011)**: بسته`parallel`(پشتیبانی چند هسته ای)
### R 3.x - عصر علم داده (2013–2019)
- **3.0 (2013)**: پشتیبانی 64 بیتی - مدیریت مجموعه داده های بزرگ
- **3.1–3.6**: بهبودهای افزایشی
- **2013–2015**: "R Revolution" - ggplot2، dplyr، tidyverse transform Science Data
### R 4.x — مدرن R (2020–اکنون)
- **4.0 (2020)**:`stringsAsFactors = FALSE`به طور پیش فرض - یک نقطه درد چندین دهه را برطرف می کند
- **4.1 (2021)**: **لوله بومی`|>`**، مختصر تابع ناشناس`\(x) x + 1`
- **4.2 (2022)**: جای جای لوله `_`، مخفف`\(x, y)`تثبیت شد
- **4.3 (2023)**: پیام های خطای بهتر (اصلاحات را پیشنهاد می کند)
- **4.4–4.5**: اصلاحات ادامه دار
## تکامل نحو
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

## بسته تکامل اکوسیستم
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

## OOP Evolution
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## اصول کلیدی طراحی
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## رشد اکوسیستم
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
