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

# R — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 에스 | 1976년 | Bell Labs(Becker, Chambers, Wilks)에서 만든 S 언어 |
| 에스플러스 | 1988 | 상업용 S 구현(StatSci) |
| R 0.10 | 1995 | 첫 번째 R 출시(Ihaka & Gentleman, 오클랜드) |
| R 1.0 | 2000 | **첫 번째 안정 릴리스** |
| R 1.4 | 2002 | S4 클래스 및 메소드 |
| R 2.0 | 2004년 | 정규식,`R.home()`|
| R 2.1 | 2005년 | UTF-8 지원 |
| R 2.5 | 2007년 | 메모리 관리 개선 |
| R 2.8 | 2008 | 참조 클래스(초기 OOP) |
| R 2.14 | 2011 |  `loadNamespace`, 병렬 패키지 |
| R 2.15 | 2012 | `stringsAsFactors = FALSE`옵션 |
| R 3.0 | 2013 | **64비트 지원**, 참조 클래스 안정 |
| R 3.1 | 2014 | `vapply`개선 |
| R 3.2 | 2015 | `readRDS`/ `saveRDS`, 샘플링 개선 |
| R 3.3 | 2016 | `xz`압축,`person()`개선 |
| R 3.4 | 2017 | 직렬화 병렬화,`switch`개선 |
| R 3.5 | 2018 | 기본`stringsAsFactors`경고 |
| R 3.6 | 2019 | 난수 생성기 개선 |
| R 4.0 | 2020 | **주요**:`stringsAsFactors = FALSE`기본값 |
| R 4.1 | 2021 | **파이프`|>`**, 익명 함수`\(x) ...`|
| R 4.2 | 2022 |  `|>`는 `on.exit`에서 자리 표시자`_`,`after`인수를 얻습니다.
| R 4.3 | 2023년 | `R_cmd`개선, 더 나은 오류 메시지 |
| R 4.4 | 2024 | `find()`개선,`deparse1()`기본값 |
| R 4.5 | 2025 | 지속적인 개선 |
## 주요 이정표
### S와 S-PLUS(1976~1994)
- **1976**: John Chambers가 Bell Labs에서 S를 만듭니다 — 언어로서의 통계 프로그래밍
- **1988**: S-PLUS — StatSci(이후 TIBCO)에 의한 상용 구현
- S 소개: 데이터 프레임, 공식(`y ~ x`), 지연 평가
### R 탄생(1995~2000)
- **1995**: Ross Ihaka와 Robert Gentleman이 오클랜드 대학에서 R을 만들었습니다.
- "R" = Ross와 Robert의 첫 글자
- 무료 오픈 소스 S 구현으로 설계되었습니다.
- **2000**: R 1.0 — 첫 번째 안정 릴리스; CRAN(Comprehensive R Archive Network) 구축
### R 성숙기(2000~2012)
- **1.4 (2002)**: S4 클래스 — 공식 OOP 시스템
- **2.0 (2004)**: 정규식, 개선된 내부 기능
- **2.8 (2008)**: 참조 클래스 — 초기 현대 OOP
- **2.14(2011)**:`parallel`패키지(멀티코어 지원)
### R 3.x — 데이터 과학 시대(2013~2019)
- **3.0(2013)**: 64비트 지원 — 대규모 데이터세트 처리
- **3.1~3.6**: 점진적인 개선
- **2013–2015**: "R 혁명" — ggplot2, dplyr, tidyverse 변환 데이터 과학
### R 4.x — 최신 R(2020~현재)
- **4.0(2020)**: 기본적으로`stringsAsFactors = FALSE`— 수십 년 된 문제점 수정
- **4.1(2021)**: **네이티브 파이프`|>`**, 익명 함수 약어`\(x) x + 1`
- **4.2(2022)**: 파이프 자리 표시자`_`,`\(x, y)`축약형 안정화
- **4.3(2023)**: 오류 메시지 개선(수정 제안)
- **4.4–4.5**: 지속적인 개선
## 구문 진화
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

## 패키지 생태계의 진화
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

## OOP 진화
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## 주요 디자인 원칙
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## 생태계 성장
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
