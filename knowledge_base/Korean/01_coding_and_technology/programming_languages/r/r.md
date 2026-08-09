---
# Metadata
title: "R"
description: "Comprehensive reference for the R programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [r, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#R
R은 통계 컴퓨팅 및 데이터 분석을 위해 특별히 설계된 프로그래밍 언어 및 환경입니다. 1993년 오클랜드 대학의 Ross Ihaka와 Robert Gentleman(따라서 "R")이 만든 이 언어는 상당한 확장이 포함된 S 언어를 구현한 것입니다. R은 오픈 소스이며 R Core Team에서 유지 관리합니다. 이는 학계, 의료, 금융 및 정부 분야의 통계학자, 데이터 분석가 및 연구원을 위한 표준 도구입니다.
R은 데이터 조작, 통계 모델링, 시각화 및 보고에 탁월합니다. CRAN(패키지 생태계)에는 지금까지 고안된 거의 모든 통계 방법을 포괄하는 20,000개 이상의 패키지가 있습니다.
---

## R이 중요한 이유
- **통계 컴퓨팅**: 모든 언어에서 가장 포괄적인 통계 방법 모음입니다.
- **데이터 시각화**: ggplot2는 출판 품질의 그래픽을 생성합니다. 그래픽 패러다임의 문법은 타의 추종을 불허합니다.
- **재현 가능한 연구**: R Markdown/Quarto를 사용하면 코드, 결과 및 설명을 단일 문서에 결합할 수 있습니다.
- **학업표준**: 통계학, 생물정보학, 역학, 생태학, 경제학, 사회과학 분야에서 사용됩니다.
- **Tidyverse**: 데이터 분석을 우아하고 일관되게 만드는 응집력 있는 패키지 세트(dplyr, ggplot2, tidyr, readr)입니다.
- **무료 오픈 소스**: 라이선스 비용이 없습니다. 글로벌 커뮤니티에 의해 적극적으로 유지 관리됩니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **성능** | 기본적으로 단일 스레드입니다. 대규모 데이터 세트의 경우 느림 | C++ 통합을 위해 `data.table`, 병렬 패키지 또는 Rcpp 사용 |
| **메모리 사용량** | 전체 데이터 세트를 RAM에 로드 | 코어 외부 처리를 위해`data.table::fread`화살표 패키지 사용 |
| **범용 언어가 아님** | 웹 개발, 시스템 프로그래밍 또는 앱에 적합하지 않음 | 비통계 작업에 Python, Go 또는 JavaScript 사용 |
| **일관되지 않은 구문** | 기본 R에는 특이한 점이 있습니다. 다른 패키지는 다른 규칙을 사용합니다 | 일관성을 위해 tidyverse를 사용하세요 |
| **취업 시장** | 주로 학술/연구 역할 | 데이터 과학 역할에서는 점점 더 Python을 선호합니다 |
---

## 구문 기본 사항
### 기본 작업
```r
# Assignment
name <- "Alice"
age <- 30
scores <- c(9.5, 8.0, 7.5, 9.0)

# Vectors (the fundamental data structure)
numbers <- 1:10
letters_vec <- c("a", "b", "c")
logical_vec <- c(TRUE, FALSE, TRUE)

# Data frames (the workhorse for tabular data)
df <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(30, 25, 35),
  score = c(9.5, 8.0, 7.5)
)

# Access columns
df$name
df[, "age"]
df$score[df$age > 28]  # Scores where age > 28
```

### Tidyverse(모던 R)
```r
library(tidyverse)

# Read data
data <- read_csv("data.csv")

# Pipe operator (%>%) chains operations
result <- data %>%
  filter(age >= 18) %>%
  mutate(grade = case_when(
    score >= 90 ~ "A",
    score >= 80 ~ "B",
    score >= 70 ~ "C",
    TRUE ~ "F"
  )) %>%
  group_by(department) %>%
  summarise(
    avg_score = mean(score, na.rm = TRUE),
    count = n()
  ) %>%
  arrange(desc(avg_score))

# Native pipe (R 4.1+)
result <- data |>
  filter(age >= 18) |>
  mutate(grade = if_else(score >= 90, "A", "B"))
```

### ggplot2를 사용한 시각화
```r
library(ggplot2)

# Scatter plot
ggplot(data = df, aes(x = age, y = score, colour = name)) +
  geom_point(size = 3) +
  labs(title = "Age vs Score", x = "Age", y = "Score") +
  theme_minimal()

# Histogram with facets
ggplot(data = survey_data, aes(x = income)) +
  geom_histogram(bins = 30, fill = "steelblue", colour = "white") +
  facet_wrap(~ education_level) +
  theme_bw()
```

### 통계 모델링
```r
# Linear regression
model <- lm(score ~ age + education + experience, data = df)
summary(model)
confint(model)

# Logistic regression
logit_model <- glm(passed ~ gpa + study_hours, data = students, family = binomial)

# ANOVA
anova_result <- aov(score ~ group, data = experiment_data)
TukeyHSD(anova_result)

# Principal Component Analysis
pca_result <- prcomp(scale(data_matrix))
plot(pca_result)
```

---

## 고급 구문 및 패턴
### S3 및 S4 객체 시스템
```r
# S3 classes (informal, most common)
new_person <- function(name, age) {
  structure(list(name = name, age = age), class = "person")
}

print.person <- function(x, ...) {
  cat("Person:", x$name, "| Age:", x$age, "\n")
}

p <- new_person("Alice", 30)
print(p)       # Uses print.person

# S4 classes (formal, with validation)
setClass("Matrix2x2",
  representation(data = "matrix"),
  validity = function(object) {
    if (!is.matrix(object@data) || !all(dim(object@data) == c(2, 2)))
      return("Matrix must be 2x2")
    TRUE
  }
)

setGeneric("determinant", function(x) standardGeneric("determinant"))
setMethod("determinant", "Matrix2x2", function(x) {
  d <- x@data
  d[1,1] * d[2,2] - d[1,2] * d[2,1]
})

m <- new("Matrix2x2", data = matrix(c(1, 3, 2, 4), nrow = 2))
determinant(m)  # -2
```

### R6 참조 클래스
```r
library(R6)
Stack <- R6Class("Stack",
  private = list(data = list()),
  public = list(
    push = function(item) { private$data <- c(private$data, list(item)) },
    pop = function() {
      n <- length(private$data)
      if (n == 0) stop("Stack is empty")
      item <- private$data[[n]]
      private$data <- private$data[-n]
      item
    },
    size = function() length(private$data)
  )
)
s <- Stack$new()
s$push(10); s$push(20)
s$pop()    # 20
```

### 비표준 평가 및 메타프로그래밍
```r
library(rlang)

# Quasiquotation
my_filter <- function(data, var, value) {
  var_expr <- enquo(var)
  data %>% filter(!!var_expr > value)
}
mtcars %>% my_filter(mpg, 25)

# Building expressions programmatically
expr <- expr(mean(!!sym("mpg"), na.rm = TRUE))
eval_tidy(expr, data = mtcars)
```

### 연산자 오버로딩
```r
`+.person` <- function(e1, e2) {
  if (inherits(e2, "person")) {
    new_person(paste(e1$name, "&", e2$name), (e1$age + e2$age) / 2)
  } else stop("Can only add two persons")
}
p1 <- new_person("Alice", 30); p2 <- new_person("Bob", 25)
p3 <- p1 + p2
p3$name  # "Alice & Bob"
```

---

## 동시성 및 병렬성
### 병렬 패키지
```r
library(parallel)
n_cores <- detectCores()

# mclapply (Unix/macOS — fork-based)
results <- mclapply(1:100, function(i) {
  mean(rnorm(10000))
}, mc.cores = 4)

# parLapply (Windows-compatible — socket-based)
cl <- makeCluster(4)
results <- parLapply(cl, 1:100, function(i) {
  mean(rnorm(10000))
})
stopCluster(cl)
```

### 미래 패키지
```r
library(future); library(future.apply)
plan(multisession)

results <- future_lapply(1:1000, function(i) {
  summary(lm(mpg ~ wt, data = mtcars[sample(1:32, 20), ]))
})

# With purrr
library(purrr)
plan(multisession, workers = 4)
results <- future_map_dbl(1:100, ~ mean(rnorm(1000)))
```

### foreach/doParallel
```r
library(doParallel); library(foreach)
cl <- makeCluster(4)
registerDoParallel(cl)

results <- foreach(i = 1:100, .combine = rbind,
                   .packages = c("dplyr")) %dopar% {
  df <- data.frame(x = rnorm(100), y = rnorm(100))
  df %>% summarise(correlation = cor(x, y))
}
stopCluster(cl)
```

---

## 프로젝트 구성 및 빌드 시스템
### 패키지 구조
```
myanalysis/
+-- DESCRIPTION           # Package metadata
+-- NAMESPACE             # Exports/imports (roxygen2)
+-- R/
|   +-- analysis.R
|   +-- plotting.R
+-- man/                  # Documentation (.Rd files)
+-- tests/testthat/
|   +-- test-analysis.R
+-- vignettes/
|   +-- introduction.Rmd
+-- renv.lock             # Dependency lock file
```

### 설명 파일
```
Package: myanalysis
Title: Advanced Statistical Analysis Toolkit
Version: 0.2.1
Authors@R: person("Jane", "Doe", email = "jane@example.com",
    role = c("aut", "cre"))
License: MIT + file LICENSE
Depends: R (>= 4.1.0)
Imports: dplyr (>= 1.1.0), ggplot2, tidyr, rlang, purrr
Suggests: testthat (>= 3.0.0), knitr, rmarkdown
Config/testthat/edition: 3
```

### renov를 사용한 종속성 관리
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### GitHub Actions가 포함된 CI/CD
```yaml
name: R-CMD-check
on:
  push: {branches: [main]}
  pull_request: {branches: [main]}
jobs:
  R-CMD-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: r-lib/actions/setup-r@v2
      - uses: r-lib/actions/setup-r-dependencies@v2
        with: {extra-packages: any::rcmdcheck}
      - uses: r-lib/actions/check-r-package@v2
```

---

## 테스트
### 프레임워크 테스트
```r
library(testthat)

test_that("mean calculation works", {
  expect_equal(mean(c(1, 2, 3, 4, 5)), 3)
  expect_type(mean(1:100), "double")
})

test_that("normalize centers and scales", {
  x <- c(10, 20, 30, 40, 50)
  result <- normalize(x)
  expect_equal(mean(result), 0, tolerance = 1e-10)
  expect_equal(sd(result), 1, tolerance = 1e-10)
})

test_that("error handling works", {
  expect_error(log("a"), "non-numeric argument")
  expect_warning(log(-1), "NaN")
  expect_silent(1 + 1)
})

# Snapshot testing (testthat 3e)
test_that("output matches snapshot", {
  expect_snapshot(summary(lm(mpg ~ wt, data = mtcars)))
})

# Run: devtools::test() or R CMD check
# Coverage: covr::package_coverage()
```

---

## 상호 운용성
### Rcpp와 C/C++ 통합
```r
library(Rcpp)

# Inline C++ function
cppFunction('
  double fast_mean(NumericVector x) {
    int n = x.size();
    double sum = 0.0;
    for (int i = 0; i < n; i++) sum += x[i];
    return sum / n;
  }
')
fast_mean(c(1.0, 2.0, 3.0, 4.0, 5.0))  # 3.0

# C++ with Rcpp sugar (vectorized)
cppFunction('
  NumericVector fast_normalize(NumericVector x) {
    double m = mean(x);
    double s = sd(x);
    return (x - m) / s;
  }
')
```

### R에서 Python 호출하기
```r
library(reticulate)

np <- import("numpy")
pd <- import("pandas")
sklearn <- import("sklearn.linear_model")

arr <- np$array(c(1, 2, 3, 4, 5))
result <- np$mean(arr)

# Convert between R and Python
r_df <- data.frame(x = 1:5, y = c(2, 4, 5, 4, 5))
py_df <- r_to_py(r_df)
back_to_r <- py_to_r(py_df)

# Use scikit-learn
model <- sklearn$LinearRegression()
X <- np$array(matrix(c(1,2,3,4,5), ncol=1))
y <- np$array(c(2, 4, 5, 4, 5))
model$fit(X, y)
```

---

## 디자인 패턴
### 패턴 1: 유연한 기능에 대한 깔끔한 평가
```r
library(rlang); library(dplyr)

compute_stats <- function(data, group_var, value_var) {
  group_var <- enquo(group_var)
  value_var <- enquo(value_var)
  data %>%
    group_by(!!group_var) %>%
    summarise(
      mean = mean(!!value_var, na.rm = TRUE),
      sd = sd(!!value_var, na.rm = TRUE),
      n = n(), .groups = "drop"
    )
}
mtcars %>% compute_stats(cyl, mpg)
```

### 패턴 2: purrr를 사용한 함수형 프로그래밍
```r
library(purrr)

# Map over grouped data
models <- mtcars %>%
  split(.$cyl) %>%
  map(~ lm(mpg ~ wt, data = .x))

models %>%
  map_dbl(~ summary(.x)$r.squared) %>%
  enframe(name = "cylinders", value = "r_squared")

# Safely handle errors
safe_log <- safely(log)
results <- map(c(1, -1, 10, "a"), safe_log)
results %>% keep(~ is.null(.x$error)) %>% map("result")
```

### 패턴 3: 보고서 생성 파이프라인
```r
library(rmarkdown)

render_report <- function(data_path, output_dir, params) {
  rmarkdown::render(
    input = "templates/analysis.Rmd",
    output_dir = output_dir,
    params = params, quiet = TRUE
  )
}

groups <- unique(sales_data$region)
walk(groups, function(region) {
  render_report("data/sales.csv", "reports/",
    params = list(region = region, year = 2024))
})
```

---

## 성능 및 최적화
### 프로파일링 도구
```r
# Base R profiling
Rprof("profile.out")
result <- heavy_computation()
Rprof(NULL)
summaryRprof("profile.out")

# Line-by-line profiling
library(profvis)
profvis({
  df <- read_csv("large_data.csv")
  result <- df %>% group_by(category) %>%
    summarise(mean_val = mean(value))
})

# Microbenchmarking
library(microbenchmark)
microbenchmark(
  base_mean = mean(x),
  manual_sum = sum(x) / length(x),
  Rcpp_mean = fast_mean(x),
  times = 1000
)
```

### 벡터화 및 data.table
```r
library(data.table)
dt <- as.data.table(mtcars)

# Fast aggregation (modifies by reference)
dt[, mean_mpg := mean(mpg), by = cyl]

# Fast grouping
result <- dt[, .(avg_mpg = mean(mpg), avg_hp = mean(hp),
  count = .N), by = .(cyl, gear)]

# fread — 10-100x faster than read.csv
data <- fread("large_file.csv", nThread = 4)

# Key-based joins (like database indexes)
setkey(dt, cyl)
dt[.(6)]  # Fast binary search lookup
```

### 메모리 최적화
```r
# Monitor memory
cat("Memory (MB):", pryr::mem_used() / 1e6, "\n")

# arrow for out-of-core processing
library(arrow)
ds <- open_dataset("large_data/", format = "parquet")
result <- ds %>% filter(year >= 2020) %>%
  summarise(total = sum(revenue)) %>% collect()

# data.table set() modifies by reference (no copy)
for (j in 1:ncol(dt)) {
  set(dt, j = j, value = as.numeric(dt[[j]]))
}
gc()  # Force garbage collection
```

---

## 배포
### CRAN에 패키지 게시
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### 빛나는 애플리케이션
```r
library(shiny)
ui <- fluidPage(
  sliderInput("n", "N:", 10, 1000, 100),
  plotOutput("histPlot")
)
server <- function(input, output) {
  output$histPlot <- renderPlot(hist(rnorm(input$n)))
}
shinyApp(ui, server)
```

### 컨테이너 배포
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## R을 사용해야 하는 경우
| 시나리오 | 왜 R | 더 나은 대안 |
|----------|-------|------|
| 통계분석 | 가장 포괄적인 통계 방법 | Python(통계 모델, scipy) |
| 데이터 시각화 | ggplot2는 출판 품질 면에서 타의 추종을 불허합니다 | 대화형을 위한 Python(matplotlib, seaborn) |
| 학술연구 | 다양한 분야의 표준 | — |
| 생물정보학 | Bioconductor에는 2,000개 이상의 전문 패키지가 있습니다 | 프로덕션 파이프라인용 Python |
| 보고(R Markdown/Quarto) | 통합분석 + 내러티브 | 주피터(파이썬) |
| 프로덕션 ML 시스템 | 배포용으로 설계되지 않음 | 파이썬, 자바 |
| 웹 개발 | 적합하지 않음 | 자바스크립트, 파이썬 |
| 대규모 데이터 처리 | 메모리 바인딩 | Python(PySpark), SQL |
---

## 요약
R은 통계의 언어입니다. 데이터 분석, 시각화 및 통계 모델링의 경우 깊이와 폭이 타의 추종을 불허합니다. tidyverse는 언어를 현대화했으며 R Markdown/Quarto는 재현 가능한 연구를 간단하게 만듭니다. Python은 일반적으로 데이터 과학 분야에서 기반을 확보했지만 R은 여전히 ​​엄격한 통계 작업을 위한 전문가 도구로 남아 있습니다. 정량적 연구를 수행하는 사람이라면 R을 배우는 것이 필수적입니다.
---

## 고급 데이터 랭글링
### data.table 심층 분석
```r
library(data.table)

# Create data.table
dt <- data.table(
  id = 1:1000,
  group = rep(LETTERS[1:5], 200),
  value = rnorm(1000),
  category = sample(c("X", "Y", "Z"), 1000, replace = TRUE)
)

# Chained operations
result <- dt[group == "A" & value > 0,
  .(mean_val = mean(value), count = .N),
  by = category][order(-mean_val)]

# Rolling joins
dt1 <- data.table(time = c(1, 5, 10, 15), val = c("a", "b", "c", "d"))
dt2 <- data.table(time = c(2, 7, 12))
dt1[dt2, on = "time", roll = "nearest"]

# Non-equi joins
dt1[dt2, on = .(time >= time)]

# Update by reference (no copy)
dt[, new_col := value * 2]
dt[value < 0, value := NA]
```

### 깔끔한 평가 및 동적 열
```r
library(dplyr)
library(rlang)

# Programmatic column access
my_col <- "mpg"
mtcars %>% select(all_of(my_col))

# Dynamic summarise
compute_summary <- function(data, group, measure) {
  data %>%
    group_by(across({{ group }})) %>%
    summarise(across({{ measure }}, list(
      mean = mean,
      sd = sd,
      median = median
    ), .names = "{.col}_{.fn}"))
}

mtcars %>% compute_summary(cyl, mpg)

# Across multiple columns
mtcars %>%
  summarise(across(where(is.numeric), list(
    mean = mean, sd = sd
  ), .names = "{.col}_{.fn}"))
```

---

## 통계 모델링 심층 분석
### 고급 회귀
```r
# Mixed-effects models
library(lme4)
model <- lmer(score ~ age + experience + (1 | department), data = df)
summary(model)
ranef(model)  # Random effects

# Generalised additive models
library(mgcv)
gam_model <- gam(y ~ s(x1) + s(x2) + factor(group), data = df)
summary(gam_model)
plot(gam_model)

# Survival analysis
library(survival)
cox_model <- coxph(Surv(time, status) ~ age + treatment, data = patients)
summary(cox_model)
survfit_obj <- survfit(Surv(time, status) ~ treatment, data = patients)
plot(survfit_obj, col = c("blue", "red"))

# Bayesian inference
library(rstanarm)
bayes_model <- stan_glm(mpg ~ wt + hp, data = mtcars, family = gaussian)
summary(bayes_model)
plot(posterior_vs_prior(bayes_model))
```

### 시계열 분석
```r
# ARIMA models
library(forecast)
ts_data <- ts(rnorm(120, mean = 100, sd = 10), frequency = 12)
arima_model <- auto.arima(ts_data)
forecast_vals <- forecast(arima_model, h = 12)
plot(forecast_vals)

# Decomposition
decomp <- decompose(ts_data)
plot(decomp)

# Exponential smoothing
ets_model <- ets(ts_data)
forecast(ets_model, h = 12)
```

### 깔끔한 모델을 사용한 머신러닝
```r
library(tidymodels)

# Define recipe (preprocessing)
recipe_obj <- recipe(mpg ~ ., data = mtcars) %>%
  step_normalize(all_numeric_predictors()) %>%
  step_corr(all_numeric_predictors(), threshold = 0.8)

# Define model specification
model_spec <- linear_reg() %>% set_engine("lm")

# Create workflow
wf <- workflow() %>%
  add_recipe(recipe_obj) %>%
  add_model(model_spec)

# Train with cross-validation
folds <- vfold_cv(mtcars, v = 10)
cv_results <- fit_resamples(wf, resamples = folds,
  metrics = metric_set(rmse, rsq, mae))
collect_metrics(cv_results)

# Final fit and predict
final_fit <- fit(wf, data = mtcars)
predict(final_fit, new_data = mtcars[1:5, ])
```
