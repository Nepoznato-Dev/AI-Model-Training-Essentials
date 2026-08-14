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
# R — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| S | 1976 |贝尔实验室（Becker、Chambers、Wilks）创建的 S 语言 |
| S-PLUS | 1988 |商业 S 实施 (StatSci) |
| R 0.10 | 1995 |第一个 R 版本（Ihaka & Gentleman，奥克兰）|
| R 1.0 | 2000 | 2000 **第一个稳定版本** |
| R 1.4 | 2002 | S4 类和方法 |
| R 2.0 | 2004 |正则表达式，`R.home()` |
| R 2.1 | 2005 | UTF-8 支持 |
| R 2.5 | 2007 |内存管理改进|
| R 2.8 | 2008 |参考类（早期 OOP）|
| R 2.14 | 2011 |  `loadNamespace`，并行封装|
| R 2.15 | 2012 | `stringsAsFactors = FALSE`选项 |
| R 3.0 | 2013 | **64 位支持**，参考类稳定 |
| R 3.1 | 2014年| `vapply`改进 |
| R 3.2 | 2015 | 2015 `readRDS`/`saveRDS`，采样改进 |
| R 3.3 | 2016 | 2016 `xz`压缩、`person()` 改进 |
| R 3.4 | 2017 | 2017并行化序列化、`switch` 改进 |
| R 3.5 | 2018 |默认`stringsAsFactors`警告 |
| R 3.6 | 2019 | 2019随机数生成器改进 |
| R 4.0 | 2020 | **主要**：`stringsAsFactors = FALSE` 默认 |
| R 4.1 | 2021 | **管道`|>`**，匿名函数`\(x) ...`|
| R 4.2 | 2022 | 2022 `|>`在`on.exit`中获得占位符`_`、`after`参数 |
| R 4.3 | 2023 | `R_cmd`改进，更好的错误消息 |
| R 4.4 | 2024 | 2024 `find()`改进，`deparse1()` 默认 |
| R 4.5 | 2025 | 2025持续改进|
## 主要里程碑
### S 和 S-PLUS (1976–1994)
- **1976**：John Chambers 在贝尔实验室创建了 S — 统计编程作为一种语言
- **1988**：S-PLUS — 由 StatSci（后来的 TIBCO）商业实施
- S 介绍：数据框、公式（`y ~ x`）、惰性求值
### R 的诞生（1995–2000）
- **1995**：Ross Ihaka 和 Robert Gentleman 在奥克兰大学创建了 R
- “R”=罗斯和罗伯特的首字母
- 设计为免费、开源 S 实施
- **2000**：R 1.0 — 第一个稳定版本； CRAN（综合R档案网络）成立
### R 成熟 (2000–2012)
- **1.4 (2002)**：S4 类 — 正式的 OOP 系统
- **2.0 (2004)**：正则表达式，改进的内部结构
- **2.8 (2008)**：参考类 — 早期现代 OOP
- **2.14 (2011)**：`parallel` 软件包（多核支持）
### R 3.x — 数据科学时代（2013-2019）
- **3.0 (2013)**：64 位支持 — 处理大型数据集
- **3.1–3.6**：渐进式改进
- **2013–2015**：“R 革命”——ggplot2、dplyr、tidyverse 变换数据科学
### R 4.x — 现代 R（2020 年至今）
- **4.0 (2020)**：默认情况下`stringsAsFactors = FALSE`— 修复了数十年之久的痛点
- **4.1 (2021)**：**原生管道`|>`**，匿名函数简写`\(x) x + 1`
- **4.2 (2022)**：管道占位符`_`、`\(x, y)`速记稳定
- **4.3 (2023)**：更好的错误消息（建议更正）
- **4.4–4.5**：持续完善
## 语法演变
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

## 包生态系统的演变
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

## 面向对象编程的演变
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## 关键设计原则
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## 生态系统增长
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
