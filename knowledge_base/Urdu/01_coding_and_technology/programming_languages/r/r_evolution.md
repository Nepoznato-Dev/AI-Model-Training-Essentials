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
# R - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| ایس | 1976 | بیل لیبز (بیکر، چیمبرز، ولکس) میں بنائی گئی زبان |
| ایس پلس | 1988 | کمرشل S کا نفاذ (StatSci) |
| R 0.10 | 1995 | پہلی R ریلیز (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **پہلی مستحکم ریلیز** |
| R 1.4 | 2002 | S4 کلاسز اور طریقے |
| R 2.0 | 2004 | باقاعدہ اظہار،`R.home()`|
| R 2.1 | 2005 | UTF-8 سپورٹ |
| R 2.5 | 2007 | یادداشت کے انتظام میں بہتری |
| R 2.8 | 2008 | حوالہ کلاسز (ابتدائی OOP) |
| R 2.14 | 2011 | `loadNamespace`, متوازی پیکج |
| R 2.15 | 2012 | `stringsAsFactors = FALSE`آپشن |
| R 3.0 | 2013 | **64 بٹ سپورٹ**، حوالہ کلاسز مستحکم |
| R 3.1 | 2014 | `vapply`بہتری |
| R 3.2 | 2015 | `readRDS`/ `saveRDS`، نمونے لینے میں بہتری |
| R 3.3 | 2016 | `xz`کمپریشن،`person()`بہتری |
| R 3.4 | 2017 | متوازی سیریلائزیشن،`switch`بہتری |
| R 3.5 | 2018 | پہلے سے طے شدہ`stringsAsFactors`وارننگ |
| R 3.6 | 2019 | بے ترتیب نمبر جنریٹر میں بہتری |
| R 4.0 | 2020 | **میجر**:`stringsAsFactors = FALSE`ڈیفالٹ |
| R 4.1 | 2021 | **پائپ`|>`**، گمنام فنکشنز`\(x) ...`|
| R 4.2 | 2022 | `|>`پلیس ہولڈر`_`حاصل کرتا ہے ,`after``on.exit` میں دلیل |
| R 4.3 | 2023 | `R_cmd`بہتری، بہتر خرابی کے پیغامات |
| R 4.4 | 2024 | `find()`بہتری،`deparse1()`ڈیفالٹ |
| R 4.5 | 2025 | جاری بہتری |
## اہم سنگ میل
### S اور S-PLUS (1976–1994)
- **1976**: جان چیمبرز نے بیل لیبز میں ایس تخلیق کیا — شماریاتی پروگرامنگ بطور زبان
- **1988**: S-PLUS — StatSci کے ذریعے تجارتی نفاذ (بعد میں TIBCO)
- S متعارف کراتا ہے: ڈیٹا فریم، فارمولے ( `y ~ x`)، سست تشخیص
### R کی پیدائش (1995–2000)
- **1995**: راس ایہاکا اور رابرٹ جنٹلمین نے آکلینڈ یونیورسٹی میں R تخلیق کیا۔
- "R" = راس اور رابرٹ کے پہلے حروف
- ایک مفت، اوپن سورس S کے نفاذ کے طور پر ڈیزائن کیا گیا ہے۔
- **2000**: R 1.0 - پہلی مستحکم ریلیز؛ CRAN (جامع آر آرکائیو نیٹ ورک) قائم کیا
### R بالغ (2000–2012)
- **1.4 (2002)**: S4 کلاسز - رسمی OOP سسٹم
- **2.0 (2004): ریگولر ایکسپریشنز، بہتر انٹرنلز
- **2.8 (2008)**: حوالہ کلاسز - ابتدائی جدید OOP
- **2.14 (2011)**:`parallel`پیکیج (ملٹی کور سپورٹ)
### R 3.x — ڈیٹا سائنس کا دور (2013–2019)
- **3.0 (2013)**: 64 بٹ سپورٹ — بڑے ڈیٹا سیٹس کو ہینڈل کریں۔
- **3.1–3.6**: بڑھتی ہوئی بہتری
- **2013–2015**: The "R Revolution" — ggplot2, dplyr, tidyverse transform data Science
### R 4.x — جدید R (2020–موجودہ)
- **4.0 (2020)**:`stringsAsFactors = FALSE`بذریعہ ڈیفالٹ — دہائیوں پرانے درد کے نقطہ کو ٹھیک کرتا ہے
- **4.1 (2021)**: **آبائی پائپ `|>`**، گمنام فنکشن شارٹ ہینڈ`\(x) x + 1`
- **4.2 (2022)**: پائپ پلیس ہولڈر `_`،`\(x, y)`شارٹ ہینڈ مستحکم
- **4.3 (2023)**: بہتر خرابی کے پیغامات (تصحیح کی تجویز کرتا ہے)
- **4.4–4.5**: مسلسل تطہیر
## نحوی ارتقاء
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

## پیکیج ماحولیاتی نظام ارتقاء
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

## OOP ارتقاء
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## ڈیزائن کے کلیدی اصول
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## ماحولیاتی نظام کی نمو
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
