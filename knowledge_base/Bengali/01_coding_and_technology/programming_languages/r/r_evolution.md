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
# R — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| এস | 1976 | বেল ল্যাবসে তৈরি S ভাষা (বেকার, চেম্বার্স, উইল্কস) |
| এস-প্লাস | 1988 | বাণিজ্যিক এস বাস্তবায়ন (StatSci) |
| আর 0.10 | 1995 | প্রথম আর রিলিজ (ইহাকা অ্যান্ড জেন্টলম্যান, অকল্যান্ড) |
| আর 1.0 | 2000 | **প্রথম স্থিতিশীল প্রকাশ** |
| আর 1.4 | 2002 | S4 ক্লাস এবং পদ্ধতি |
| আর 2.0 | 2004 | রেগুলার এক্সপ্রেশন,`R.home()`|
| আর 2.1 | 2005 | UTF-8 সমর্থন |
| আর 2.5 | 2007 | মেমরি ব্যবস্থাপনা উন্নতি |
| আর 2.8 | 2008 | রেফারেন্স ক্লাস (প্রাথমিক OOP) |
| আর 2.14 | 2011 | `loadNamespace`, সমান্তরাল প্যাকেজ |
| আর 2.15 | 2012 | `stringsAsFactors = FALSE`বিকল্প |
| আর 3.0 | 2013 | **64-বিট সমর্থন**, রেফারেন্স ক্লাস স্থিতিশীল |
| আর 3.1 | 2014 | `vapply`উন্নতি |
| আর 3.2 | 2015 | `readRDS`/`saveRDS`, স্যাম্পলিং উন্নতি |
| আর 3.3 | 2016 | `xz`কম্প্রেশন,`person()`উন্নতি |
| আর 3.4 | 2017 | সমান্তরাল ক্রমিককরণ,`switch`উন্নতি |
| আর 3.5 | 2018 | ডিফল্ট`stringsAsFactors`সতর্কতা |
| আর 3.6 | 2019 | এলোমেলো সংখ্যা জেনারেটরের উন্নতি |
| আর 4.0 | 2020 | **মেজর**:`stringsAsFactors = FALSE`ডিফল্ট |
| আর 4.1 | 2021 | **পাইপ`|>`**, বেনামী ফাংশন`\(x) ...`|
| আর 4.2 | 2022 | `|>`স্থানধারক`_`, `on.exit`-এ`after`আর্গুমেন্ট লাভ করেছে |
| আর 4.3 | 2023 | `R_cmd`উন্নতি, আরও ভাল ত্রুটি বার্তা |
| আর 4.4 | 2024 | `find()`উন্নতি,`deparse1()`ডিফল্ট |
| আর 4.5 | 2025 | চলমান উন্নতি |
## প্রধান মাইলফলক
### S এবং S-PLUS (1976-1994)
- **1976**: জন চেম্বার্স বেল ল্যাবসে এস তৈরি করেছেন — একটি ভাষা হিসাবে পরিসংখ্যানগত প্রোগ্রামিং
- **1988**: S-PLUS — StatSci দ্বারা বাণিজ্যিক বাস্তবায়ন (পরে TIBCO)
- এস পরিচয় করিয়ে দেয়: ডেটা ফ্রেম, সূত্র (`y ~ x`), অলস মূল্যায়ন
### R এর জন্ম (1995-2000)
- **1995**: রস ইহাকা এবং রবার্ট জেন্টলম্যান অকল্যান্ড বিশ্ববিদ্যালয়ে R তৈরি করেন
- "R" = রস এবং রবার্টের প্রথম অক্ষর
- একটি বিনামূল্যে, ওপেন সোর্স এস বাস্তবায়ন হিসাবে ডিজাইন করা হয়েছে৷
- **2000**: R 1.0 — প্রথম স্থিতিশীল প্রকাশ; CRAN (comprehensive R Archive Network) প্রতিষ্ঠিত
### আর পরিপক্ক (2000-2012)
- **1.4 (2002): S4 ক্লাস - আনুষ্ঠানিক OOP সিস্টেম
- **2.0 (2004): নিয়মিত এক্সপ্রেশন, উন্নত অভ্যন্তরীণ
- **2.8 (2008): রেফারেন্স ক্লাস - প্রাথমিক আধুনিক OOP
- **2.14 (2011):`parallel`প্যাকেজ (মাল্টিকোর সমর্থন)
### R 3.x — দ্য ডেটা সায়েন্স এরা (2013–2019)
- **3.0 (2013): 64-বিট সমর্থন — বড় ডেটাসেট পরিচালনা করে
- **3.1–3.6**: ক্রমবর্ধমান উন্নতি
- **2013–2015**: "আর বিপ্লব" — ggplot2, dplyr, tidyverse transform data Science
### R 4.x — আধুনিক R (2020-বর্তমান)
- **4.0 (2020)**: ডিফল্টরূপে`stringsAsFactors = FALSE`— এক দশক পুরনো ব্যথার বিন্দু ঠিক করে
- **4.1 (2021): **নেটিভ পাইপ`|>`**, বেনামী ফাংশন শর্টহ্যান্ড`\(x) x + 1`
- **4.2 (2022)**: পাইপ প্লেসহোল্ডার`_`,`\(x, y)`শর্টহ্যান্ড স্থিতিশীল
- **4.3 (2023): আরও ভাল ত্রুটি বার্তা (সংশোধনের পরামর্শ দেয়)
- **4.4–4.5**: ক্রমাগত পরিশোধন
## সিনট্যাক্স বিবর্তন
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

## প্যাকেজ ইকোসিস্টেম বিবর্তন
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

## OOP বিবর্তন
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## মূল ডিজাইনের নীতি
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## ইকোসিস্টেম বৃদ্ধি
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
