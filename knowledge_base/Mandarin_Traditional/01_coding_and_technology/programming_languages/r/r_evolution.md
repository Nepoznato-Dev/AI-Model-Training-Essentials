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
# R — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| S | 1976 |貝爾實驗室（Becker、Chambers、Wilks）創建的 S 語言 |
| S-PLUS | 1988 |商業 S 實施 (StatSci) |
| R 0.10 | 1995 |第一個 R 版本（Ihaka & Gentleman，奧克蘭）|
| R 1.0 | 2000 | 2000 **第一個穩定版本** |
| R 1.4 | 2002 | S4 類別與方法 |
| R 2.0 | 2004 |正規表達式，`R.home()` |
| R 2.1 | 2005 | UTF-8 支援 |
| R 2.5 | 2007 |記憶體管理改進|
| R 2.8 | 2008 |參考類（早期 OOP）|
| R 2.14 | 2011 | `loadNamespace`，並行封裝|
| R 2.15 | 2012 |`stringsAsFactors = FALSE`選項 |
| R 3.0 | 2013 | **64 位元支援**，參考類別穩定 |
| R 3.1 | 2014年|`vapply`改進 |
| R 3.2 | 2015 | 2015`readRDS`/`saveRDS`，採樣改進 |
| R 3.3 | 2016 | 2016`xz`壓縮、`person()` 改進 |
| R 3.4 | 2017 | 2017並行化序列化、`switch` 改進 |
| R 3.5 | 2018 |預設`stringsAsFactors`警告 |
| R 3.6 | 2019 | 2019隨機數產生器改進 |
| R 4.0 | 2020 | **主要**：`stringsAsFactors = FALSE` 預設 |
| R 4.1 | 2021 | **管道`|>`**，匿名函數`\(x) ...`|
| R 4.2 | 2022 | 2022`|>`在`on.exit`中取得佔位符`_`、`after`參數 |
| R 4.3 | 2023 |`R_cmd`改進，更好的錯誤訊息 |
| R 4.4 | 2024 | 2024`find()`改進，`deparse1()` 預設 |
| R 4.5 | 2025 | 2025持續改進|
## 主要里程碑
### S 與 S-PLUS (1976–1994)
- **1976**：John Chambers 在貝爾實驗室創建了 S — 統計程式設計作為一種語言
- **1988**：S-PLUS — 由 StatSci（後來的 TIBCO）商業實施
- S 介紹：資料框、公式（`y ~ x`）、惰性求值
### R 的誕生（1995–2000）
- **1995**：Ross Ihaka 和 Robert Gentleman 在奧克蘭大學創立了 R
- “R”=羅斯和羅伯特的首字母
- 設計為免費、開源 S 實施
- **2000**：R 1.0 — 第一穩定版； CRAN（綜合R檔案網）成立
### R 成熟 (2000–2012)
- **1.4 (2002)**：S4 類 — 正式的 OOP 系統
- **2.0 (2004)**：正規表示式，改進的內部結構
- **2.8 (2008)**：參考類 — 早期現代 OOP
- **2.14 (2011)**：`parallel` 軟體包（多核心支援）
### R 3.x — 資料科學時代（2013-2019）
- **3.0 (2013)**：64 位元支援 — 處理大型資料集
- **3.1–3.6**：漸進式改進
- **2013–2015**：「R 革命」—ggplot2、dplyr、tidyverse 變換資料科學
### R 4.x — 現代 R（2020 年至今）
- **4.0 (2020)**：預設情況下`stringsAsFactors = FALSE`— 修正了數十年之久的痛點
- **4.1 (2021)**：**原生管道`|>`**，匿名函數簡寫 `\(x) x + 1`
- **4.2 (2022)**：管道佔位符`_`、`\(x, y)`速記穩定
- **4.3 (2023)**：更好的錯誤訊息（建議更正）
- **4.4–4.5**：持續完善
## 語法演變
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

## 套件生態系的演變
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

## 物件導向程式設計的演變
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## 關鍵設計原則
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## 生態系成長
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
