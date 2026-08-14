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

# R - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| ส | 1976 | ภาษา S สร้างขึ้นที่ Bell Labs (Becker, Chambers, Wilks) |
| เอส-พลัส | 1988 | การใช้งานเชิงพาณิชย์ S (StatSci) |
| ฿ 0.10 | 1995 | R รุ่นแรก (Ihaka & Gentleman, โอ๊คแลนด์) |
| ฿ 1.0 | 2000 | **การเปิดตัวที่เสถียรครั้งแรก** |
| อาร์ 1.4 | 2545 | คลาสและวิธีการ S4 |
| อาร์ 2.0 | 2547 | นิพจน์ทั่วไป`R.home()`|
| ร 2.1 | 2548 | รองรับ UTF-8 |
| ฿ 2.5 | 2550 | การปรับปรุงการจัดการหน่วยความจำ |
| ฿ 2.8 | 2551 | คลาสอ้างอิง (OOP ก่อนกำหนด) |
| ฿ 2.14 | 2554 | `loadNamespace`แพ็คเกจขนาน |
| ฿ 2.15 | 2555 | `stringsAsFactors = FALSE`ตัวเลือก |
| ฿ 3.0 | 2013 | ** รองรับ 64 บิต ** คลาสอ้างอิงเสถียร |
| ร 3.1 | 2014 |  การปรับปรุง`vapply`|
| ร 3.2 | 2558 | `readRDS`/`saveRDS`การปรับปรุงการสุ่มตัวอย่าง |
| R 3.3 | 2559 |  การบีบอัด `xz`, การปรับปรุง`person()`|
| ฿ 3.4 | 2017 | การทำซีเรียลไลซ์แบบขนาน การปรับปรุง `switch`
| ฿ 3.5 | 2018 | คำเตือน`stringsAsFactors`เริ่มต้น |
| ฿ 3.6 | 2019 | การปรับปรุงตัวสร้างตัวเลขสุ่ม |
| ฿ 4.0 | 2020 | **หลัก**:`stringsAsFactors = FALSE`ค่าเริ่มต้น |
| ฿ 4.1 | 2021 | **ไปป์`|>`** ฟังก์ชันที่ไม่ระบุชื่อ`\(x) ...`|
| ฿ 4.2 | 2022 | `|>`ได้รับตัวยึดตำแหน่ง`_`อาร์กิวเมนต์`after`ใน`on.exit`|
| ฿ 4.3 | 2023 |  การปรับปรุง`R_cmd`ข้อความแสดงข้อผิดพลาดที่ดีขึ้น |
| ฿ 4.4 | 2024 |  การปรับปรุง `find()`, ค่าเริ่มต้น`deparse1()`|
| ฿ 4.5 | 2025 | การปรับปรุงอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### เอส และ เอส-พลัส (1976–1994)
- **1976**: John Chambers สร้าง S ที่ Bell Labs — การเขียนโปรแกรมเชิงสถิติเป็นภาษาหนึ่ง
- **1988**: S-PLUS — การนำไปใช้เชิงพาณิชย์โดย StatSci (ภายหลัง TIBCO)
- S แนะนำ: กรอบข้อมูล, สูตร (`y ~ x`), การประเมินแบบ Lazy
### กำเนิดอาร์ (1995–2000)
- **1995**: Ross Ihaka และ Robert Gentleman สร้างผลงาน R ที่มหาวิทยาลัยโอ๊คแลนด์
- "R" = ตัวอักษรตัวแรกของ Ross และ Robert
- ออกแบบให้เป็นการใช้งาน S แบบโอเพ่นซอร์สฟรี
- **2000**: R 1.0 — เปิดตัวเสถียรครั้งแรก; ก่อตั้ง CRAN (เครือข่ายเก็บถาวร R ที่ครอบคลุม)
### R ครบกำหนดไถ่ถอน (2000–2012)
- **1.4 (2002)**: คลาส S4 — ระบบ OOP อย่างเป็นทางการ
- **2.0 (2004)**: นิพจน์ทั่วไป การปรับปรุงภายใน
- **2.8 (2008)**: คลาสอ้างอิง — OOP สมัยใหม่ตอนต้น
- **2.14 (2011)**: แพ็คเกจ`parallel`(รองรับมัลติคอร์)
### R 3.x - ยุควิทยาศาสตร์ข้อมูล (2013–2019)
- **3.0 (2013)**: รองรับ 64 บิต — จัดการชุดข้อมูลขนาดใหญ่
- **3.1–3.6**: การปรับปรุงเพิ่มเติมแบบค่อยเป็นค่อยไป
- **2013–2015**: "การปฏิวัติ R" — ggplot2, dplyr, tidyverse แปลงวิทยาการข้อมูล
### R 4.x — โมเดิร์น R (2020–ปัจจุบัน)
- **4.0 (2020)**:`stringsAsFactors = FALSE`โดยค่าเริ่มต้น — แก้ไขปัญหาที่เกิดขึ้นเมื่อหลายสิบปี
- **4.1 (2021)**: **เนทิฟไปป์`|>`**, ชวเลขฟังก์ชันแบบไม่ระบุชื่อ`\(x) x + 1`
- **4.2 (2022)**: ตัวยึดท่อ`_`,`\(x, y)`ชวเลขแบบเสถียร
- **4.3 (2023)**: ข้อความแสดงข้อผิดพลาดที่ดีขึ้น (แนะนำการแก้ไข)
- **4.4–4.5**: การปรับปรุงอย่างต่อเนื่อง
## วิวัฒนาการไวยากรณ์
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

## วิวัฒนาการระบบนิเวศแพ็คเกจ
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

## วิวัฒนาการ OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## หลักการออกแบบที่สำคัญ
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## การเติบโตของระบบนิเวศ
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
