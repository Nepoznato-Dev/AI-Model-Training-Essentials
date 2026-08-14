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
# R - تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| س | 1976 | تم إنشاء لغة S في Bell Labs (Becker, Chambers, Wilks) |
| اس بلس | 1988 | تنفيذ S التجاري (StatSci) |
| ص 0.10 | 1995 | أول إصدار R (Ihaka & Gentleman، أوكلاند) |
| ص 1.0 | 2000 | **الإصدار المستقر الأول** |
| ص 1.4 | 2002 | فئات وطرق S4 |
| ص 2.0 | 2004 | التعابير العادية،`R.home()`|
| ص 2.1 | 2005 | دعم UTF-8 |
| ص 2.5 | 2007 | تحسينات إدارة الذاكرة |
| ص 2.8 | 2008 | الفصول المرجعية (OOP المبكر) |
| ص 2.14 | 2011 | `loadNamespace`الحزمة المتوازية |
| ص 2.15 | 2012 |  خيار`stringsAsFactors = FALSE`|
| ص 3.0 | 2013 | **دعم 64 بت**، فئات مرجعية مستقرة |
| ص 3.1 | 2014 |  تحسينات`vapply`|
| ص 3.2 | 2015 | `readRDS`/`saveRDS`, تحسينات العينات |
| ص 3.3 | 2016 |  ضغط `xz`، تحسينات`person()`|
| ص 3.4 | 2017 | توازي التسلسل، تحسينات`switch`|
| ص 3.5 | 2018 | تحذير`stringsAsFactors`الافتراضي |
| ص 3.6 | 2019 | تحسينات مولد الأرقام العشوائية |
| ص 4.0 | 2020 | **الرئيسي**:`stringsAsFactors = FALSE`الافتراضي |
| ص 4.1 | 2021 | **الأنبوب`|>`**، وظائف مجهولة`\(x) ...`|
| ص 4.2 | 2022 | `|>`يحصل على العنصر النائب`_`ووسيطة`after`في`on.exit`|
| ص 4.3 | 2023 |  تحسينات`R_cmd`ورسائل خطأ أفضل |
| ص 4.4 | 2024 |  تحسينات `find()`،`deparse1()`الافتراضي |
| ص 4.5 | 2025 | التحسينات المستمرة |
## المعالم الرئيسية
### إس و إس-بلس (1976-1994)
- **1976**: ابتكر جون تشامبرز لغة S في Bell Labs — البرمجة الإحصائية كلغة
- **1988**: S-PLUS — التنفيذ التجاري بواسطة StatSci (لاحقًا TIBCO)
- يقدم S: إطارات البيانات، والصيغ (`y ~ x`)، والتقييم البطيء
### ميلاد آر (1995-2000)
- **1995**: قام روس إيهكا وروبرت جنتلمان بإنشاء R في جامعة أوكلاند
- "R" = الحروف الأولى من روس وروبرت
- تم تصميمه كتطبيق S مجاني ومفتوح المصدر
- **2000**: R 1.0 — الإصدار المستقر الأول؛ إنشاء CRAN (شبكة أرشيف R الشاملة).
### مرحلة النضج (2000-2012)
- **1.4 (2002)**: فئات S4 — نظام OOP الرسمي
- **2.0 (2004)**: التعبيرات العادية، وتحسين العناصر الداخلية
- **2.8 (2008)**: الطبقات المرجعية - بداية العصر الحديث OOP
- **2.14 (2011)**: حزمة`parallel`(دعم متعدد النواة)
### R 3.x — عصر علم البيانات (2013-2019)
- **3.0 (2013)**: دعم 64 بت — التعامل مع مجموعات البيانات الكبيرة
- **3.1–3.6**: تحسينات تدريجية
- **2013-2015**: "ثورة البحث والتطوير" — ggplot2، dplyr، tidyverse تحويل علم البيانات
### R 4.x — الحديث R (2020 إلى الوقت الحاضر)
- **4.0 (2020)**:`stringsAsFactors = FALSE`بشكل افتراضي - يعمل على إصلاح مشكلة عمرها عقود من الزمن
- **4.1 (2021)**: ** الأنبوب الأصلي`|>`**، اختصار دالة مجهولة`\(x) x + 1`
- **4.2 (2022)**: العنصر النائب للأنبوب `_`، تم تثبيت الاختصار `\(x, y)`
- **4.3 (2023)**: رسائل خطأ أفضل (تقترح تصحيحات)
- **4.4–4.5**: التحسينات المستمرة
## تطور بناء الجملة
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

## تطور النظام البيئي للحزمة
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

## تطور OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## مبادئ التصميم الرئيسية
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## نمو النظام البيئي
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
