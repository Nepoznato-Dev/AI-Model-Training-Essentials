<!--
---
# Metadata
title: "R — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the R ecosystem including tools, packages, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [r, ecosystem, tooling, cran, tidyverse, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# R — 생태계 및 툴링 가이드
이 가이드에서는 R 생태계의 필수 도구, 패키지 및 인프라를 다룹니다.
---

## R 구현
| 구현 | 메모 |
|---------------|-------|
| **R(GNU R)** | 표준, 가장 널리 사용됨 |
| **RStudio** | R이 통합된 IDE |
| **양전자** | 차세대 IDE(Posit) |
| **마이크로소프트 R 오픈** | 최적화(보관) |
| **pqR** | 병렬 R |
| **렌진** | JVM 기반 R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **install.packages()** | CRAN 패키지 |
| **크랜** | 포괄적인 R 아카이브 네트워크(19,000+ 패키지) |
| **바이오컨덕터** | 유전체학/생물학 패키지 |
| **원격** | GitHub에서 설치 |
| **박** | 최신 패키지 설치 프로그램 |
| **렌브** | 프로젝트-로컬 환경 |
| **팩랫** | 종속성 관리(레거시) |
```r
# Install from CRAN
install.packages("dplyr")
install.packages(c("ggplot2", "tidyr", "stringr"))

# Install from GitHub
remotes::install_github("tidyverse/dplyr")

# renv for reproducibility
renv::init()              # initialize project
renv::snapshot()          # save state
renv::restore()           # restore state
```

---

## 타이디버스
| 패키지 | 목적 |
|---------|---------|
| **dplyr** | 데이터 조작 |
| **정리** | 데이터 정리 |
| **ggplot2** | 데이터 시각화 |
| **독자** | 빠른 CSV/파일 읽기 |
| **푸르르** | 함수형 프로그래밍 |
| **티블** | 최신 데이터 프레임 |
| **문자열** | 문자열 조작 |
| **고양이를 위한** | 요인 처리 |
| **윤활** | 날짜/시간 처리 |
| **마그리트** | 파이프 연산자(%>%) |
```r
library(tidyverse)

# Data pipeline
result <- starwars %>%
  filter(!is.na(height)) %>%
  group_by(gender) %>%
  summarise(
    avg_height = mean(height),
    avg_mass = mean(mass, na.rm = TRUE),
    count = n()
  ) %>%
  arrange(desc(avg_height))

# Visualization
ggplot(starwars, aes(x = height, y = mass, color = gender)) +
  geom_point(alpha = 0.7) +
  facet_wrap(~ species) +
  theme_minimal() +
  labs(title = "Star Wars Character Dimensions",
       x = "Height (cm)", y = "Mass (kg)")
```

---

## 데이터 과학 및 통계
| 패키지 | 목적 |
|---------|---------|
| **정리모델** | 모델링 프레임워크(캐럿 대체) |
| **캐럿** | 기계 학습(레거시) |
| **랜덤포레스트** | 랜덤 포레스트 |
| **xgboost** | 그라데이션 부스팅 |
| **글름넷** | 정규화된 회귀 |
| **생존** | 생존 분석 |
| **lme4** | 혼합 효과 모델 |
| **brms** | 베이지안 회귀(Stan) |
| **르스탄** | 스탠 인터페이스 |
| **예측** | 시계열 예측 |
| **한숨** | 시계열 데이터 |
| **우화** | 시계열 모델 |
```r
library(tidymodels)

# Modeling workflow
model_spec <- linear_reg() %>% set_engine("lm")
recipe <- recipe(mpg ~ ., data = mtcars) %>%
  step_normalize(all_numeric_predictors())

workflow <- workflow() %>%
  add_model(model_spec) %>%
  add_recipe(recipe)

fit <- workflow %>% fit(data = mtcars)
tidy(fit)
augment(fit, new_data = mtcars)
```

---

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **DBI** | 데이터베이스 인터페이스 표준 |
| **dbplyr** | 데이터베이스용 dplyr 백엔드 |
| **RSQLite** | SQLite |
| **RPostgres** | 포스트그레SQL |
| **RMariaDB** | MySQL/마리아DB |
| **ODBC** | ODBC 연결 |
| **큰 쿼리** | 구글 빅쿼리 |
| **반짝반짝** | 아파치 스파크 |
| **화살표** | 아파치 애로우 / 쪽모이 세공 |
```r
library(DBI)
library(dbplyr)

con <- dbConnect(RSQLite::SQLite(), "mydb.sqlite")
users_tbl <- tbl(con, "users")

# dplyr syntax translates to SQL
users_tbl %>%
  filter(age > 18) %>%
  group_by(city) %>%
  summarise(count = n()) %>%
  show_query()  # shows generated SQL
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **테스트해 보세요** | 단위 테스트(가장 인기 있음) |
| **가장 작은** | 경량 테스트 |
| **린트** | 코드 린팅 |
| **커버** | 코드 적용 범위 |
| **조롱** | 조롱 |
```r
# testthat example
library(testthat)

test_that("calculate_mean works", {
  expect_equal(calculate_mean(c(1, 2, 3)), 2)
  expect_equal(calculate_mean(c(10, 20)), 15)
  expect_error(calculate_mean(numeric(0)))
})

test_that("format_output handles NA", {
  result <- format_output(c(1, NA, 3))
  expect_type(result, "character")
  expect_length(result, 3)
})
```

```bash
Rscript -e "devtools::test()"    # run tests
Rscript -e "devtools::check()"   # full R CMD check
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **린트** | 코드 린팅 |
| **스타일러** | 코드 서식 |
| **좋은 실천** | 패키지 품질 점검 |
| **커버** | 코드 적용 범위 |
| **사이클로컴프** | 순환적 복잡성 |
| **패키지다운** | 패키지 문서 웹사이트 |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## 재현 가능한 연구
| 도구 | 목적 |
|------|---------|
| **R 마크다운** | 재현 가능한 보고서 |
| **쿼토** | 차세대 출판 |
| **니트** | 동적 보고서 생성 |
| **대상** | 파이프라인 관리 |
| **드레이크** | 유사 파이프라인(레거시) |
| **예약 취소** | R Markdown의 책 |
| **블로그다운** | R Markdown의 블로그 |
| **증류** | 과학 기사 |
| **반짝이는** | 대화형 웹 앱 |
| **플렉스대시보드** | 대시보드 |
```r
# Shiny app example
library(shiny)

ui <- fluidPage(
  sliderInput("n", "Number of bins:", 1, 50, 30),
  plotOutput("distPlot")
)

server <- function(input, output) {
  output$distPlot <- renderPlot({
    x <- rnorm(input$n * 100)
    hist(x, breaks = input$n, col = "steelblue", border = "white")
  })
}

shinyApp(ui, server)
```

---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **데이터.테이블** | 빠른 데이터 조작 |
| **R6** | 참조 클래스(OOP) |
| **rlang** | R 프로그래밍 도구 |
| **vctrs** | 벡터 클래스 |
| **접착제** | 문자열 보간 |
| **클리** | 명령줄 인터페이스 |
| **함께** | 임시 상태 |
| **fs** | 파일 시스템 작업 |
| **httr2** | HTTP 클라이언트 |
| **jsonlite** | JSON 구문 분석 |
| **xml2** | XML/HTML 구문 분석 |
| **최고** | 웹 스크래핑 |
| **병렬** | 내장 병렬성 |
| **미래** | 통합 병렬성 |
| **퍼르르** | 푸르르 + 미래 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **RStudio** | 표준 R IDE |
| **양전자** | 차세대 IDE(Posit) |
| **VS 코드 + R 확장** | 경량, R LSP |
| **Neovim + nvim-r** | 터미널 기반 |
| **Jupyter + IRkernel** | 노트북 인터페이스 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **빛나는 서버** | 빛나는 앱 호스트 |
| **포지트 커넥트** | 엔터프라이즈 R 배포 |
| **배관공** | R의 REST API |
| **도커** | 컨테이너화(로커 이미지) |
| **콰르토 + 넷리파이** | 정적 사이트 |
| **AWS 람다** | 서버리스 R |
| **대상** | 파이프라인 오케스트레이션 |
```r
# Plumber API
library(plumber)

#* @get /predict
#* @param x numeric input
function(x = 5) {
  list(prediction = x * 2 + 1)
}
```

---

## 요약
R의 생태계는 통계 컴퓨팅 및 데이터 과학의 표준입니다. 표준 스택은 런타임용 **R 4.3+**, IDE용 **RStudio**, 데이터 조작 및 시각화용 **tidyverse**, 기계 학습용 **tidymodels**, 플로팅용 **ggplot2**, 테스트용 **testthat**, 린팅용 **lintr**, 재현 가능한 보고서용 **Quarto**입니다. R은 통계, 데이터 시각화, 생물정보학(Bioconductor) 및 재현 가능한 연구에 탁월합니다. CRAN 생태계에는 19,000개 이상의 패키지가 있습니다. 프로덕션 배포의 경우 **Plumber**는 R 스크립트를 API로 변환하고 **Shiny**는 대화형 웹 애플리케이션을 만듭니다.