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
# R — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| S | 1976 | Ngôn ngữ S được tạo tại Bell Labs (Becker, Chambers, Wilks) |
| S-PLUS | 1988 | Triển khai S thương mại (StatSci) |
| R 0,10 | 1995 | Bản phát hành R đầu tiên (Ihaka & Gentleman, Auckland) |
| R 1.0 | 2000 | **Bản phát hành ổn định đầu tiên** |
| R 1.4 | 2002 | Các lớp và phương thức S4 |
| R 2.0 | 2004 | Biểu thức chính quy,`R.home()`|
| R 2.1 | 2005 | Hỗ trợ UTF-8 |
| R 2,5 | 2007 | Cải tiến quản lý bộ nhớ |
| R 2.8 | 2008 | Các lớp tham khảo (OOP sớm) |
| R 2,14 | 2011 | `loadNamespace`, gói song song |
| R 2,15 | 2012 |  Tùy chọn`stringsAsFactors = FALSE`|
| R 3.0 | 2013 | **Hỗ trợ 64-bit**, các lớp tham chiếu ổn định |
| R 3.1 | 2014 |  Cải tiến`vapply`|
| R 3.2 | 2015 | `readRDS`/`saveRDS`, cải tiến việc lấy mẫu |
| R 3.3 | 2016 |  Nén `xz`, cải tiến`person()`|
| R 3,4 | 2017 | Song song hóa tuần tự hóa, cải tiến`switch`|
| R 3,5 | 2018 | Cảnh báo`stringsAsFactors`mặc định |
| R 3.6 | 2019 | Cải tiến trình tạo số ngẫu nhiên |
| R 4.0 | 2020 | **Chính**:`stringsAsFactors = FALSE`mặc định |
| R 4.1 | 2021 | **Ống`|>`**, chức năng ẩn danh`\(x) ...`|
| R 4.2 | 2022 | `|>`giành được đối số giữ chỗ`_`,`after`trong`on.exit`|
| R 4.3 | 2023 | `R_cmd`cải tiến, thông báo lỗi tốt hơn |
| R 4.4 | 2024 |  Cải tiến `find()`, mặc định`deparse1()`|
| R 4,5 | 2025 | Cải tiến liên tục |
## Các cột mốc quan trọng
### S và S-PLUS (1976–1994)
- **1976**: John Chambers tạo ra S tại Bell Labs — lập trình thống kê dưới dạng ngôn ngữ
- **1988**: S-PLUS — do StatSci triển khai thương mại (sau này là TIBCO)
- S giới thiệu: khung dữ liệu, công thức (`y ~ x`), đánh giá lười biếng
### Sự ra đời của R (1995–2000)
- **1995**: Ross Ihaka và Robert Gentleman tạo ra R tại Đại học Auckland
- "R" = chữ cái đầu tiên của Ross và Robert
- Được thiết kế dưới dạng triển khai S mã nguồn mở, miễn phí
- **2000**: R 1.0 — bản phát hành ổn định đầu tiên; CRAN (Mạng lưu trữ R toàn diện) được thành lập
### R trưởng thành (2000–2012)
- **1.4 (2002)**: Lớp S4 — hệ thống OOP chính thức
- **2.0 (2004)**: Biểu thức chính quy, nội bộ được cải tiến
- **2.8 (2008)**: Các lớp tham khảo — OOP thời kỳ đầu hiện đại
- **2.14 (2011)**: Gói`parallel`(hỗ trợ đa lõi)
### R 3.x — Kỷ nguyên khoa học dữ liệu (2013–2019)
- **3.0 (2013)**: Hỗ trợ 64-bit — xử lý các tập dữ liệu lớn
- **3.1–3.6**: Cải tiến gia tăng
- **2013–2015**: "Cuộc cách mạng R" — ggplot2, dplyr, gọn gàng biến đổi khoa học dữ liệu
### R 4.x — R hiện đại (2020–nay)
- **4.0 (2020)**:`stringsAsFactors = FALSE`theo mặc định — khắc phục điểm yếu đã tồn tại hàng thập kỷ
- **4.1 (2021)**: **Ống gốc`|>`**, viết tắt hàm ẩn danh`\(x) x + 1`
- **4.2 (2022)**: Phần giữ chỗ ống`_`, tốc ký`\(x, y)`đã ổn định
- **4.3 (2023)**: Thông báo lỗi tốt hơn (đề xuất sửa)
- **4.4–4.5**: Tiếp tục sàng lọc
## Tiến hóa cú pháp
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

## Tiến hóa hệ sinh thái trọn gói
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

## Tiến hóa OOP
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## Nguyên tắc thiết kế chính
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## Tăng trưởng hệ sinh thái
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
