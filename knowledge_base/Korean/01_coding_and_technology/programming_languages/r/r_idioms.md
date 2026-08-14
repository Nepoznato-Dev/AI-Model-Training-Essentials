---
# Metadata
title: "R — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic R code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [r, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# R — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔하고 관용적인 R 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 타이디버스 스타일
```r
# ✅ Pipe operator (|> in R 4.1+, or magrittr %>%)
result <- data |>
  filter(age > 18) |>
  mutate(category = if_else(salary > 50000, "high", "low")) |>
  group_by(category) |>
  summarise(
    count = n(),
    avg_salary = mean(salary, na.rm = TRUE)
  ) |>
  arrange(desc(avg_salary))

# ✅ Assignment with <-
name <- "Alice"
result <- compute(x, y)

# ✅ Naming conventions
snake_case <- function() { }  # functions and variables
CamelCase <- function() { }   # S4 classes
UPPER_CASE  # constants
```

---

## 벡터화
```r
# ✅ Vectorized operations (avoid loops)
squares <- x^2
adults <- ages >= 18
total <- sum(values)
mean_val <- mean(values, na.rm = TRUE)

# ✅ Vectorized conditionals
categories <- ifelse(scores > 90, "A",
              ifelse(scores > 80, "B", "C"))

# ✅ Vectorized string operations (stringr)
library(stringr)
cleaned <- str_trim(names)
upper_names <- str_to_upper(names)
has_email <- str_detect(text, "\\S+@\\S+")
```

---

## 기능
```r
# ✅ Early return for validation
process_data <- function(data) {
  if (is.null(data)) return(NULL)
  if (nrow(data) == 0) return(tibble())
  
  # main logic
  data |> filter(!is.na(value))
}

# ✅ Default arguments
plot_histogram <- function(x, bins = 30, title = "Distribution") {
  ggplot(data.frame(x = x), aes(x)) +
    geom_histogram(bins = bins) +
    ggtitle(title)
}

# ✅ ... for extra arguments
my_wrapper <- function(data, ...) {
  data |> summarise(across(everything(), mean, na.rm = TRUE), ...)
}
```

---

## tidyverse 패턴
```r
# ✅ dplyr verbs
result <- df |>
  select(name, age, salary) |>
  filter(age >= 18, !is.na(salary)) |>
  mutate(bonus = salary * 0.1) |>
  arrange(desc(salary)) |>
  slice_head(n = 10)

# ✅ tidyr for reshaping
wide <- df |> pivot_wider(names_from = year, values_from = score)
long <- df |> pivot_longer(cols = starts_with("year"), names_to = "year")

# ✅ purrr for iteration
results <- map(data_list, process_function)
lengths <- map_int(data_list, nrow)
combined <- reduce(list_of_dfs, full_join)
```

---

## 오류 처리
```r
# ✅ stop for errors
if (nrow(data) == 0) stop("Data is empty")

# ✅ warning for warnings
if (any(is.na(values))) warning("NA values found")

# ✅ message for information
message("Processing ", nrow(data), " rows")

# ✅ tryCatch for error handling
result <- tryCatch(
  risky_operation(),
  error = function(e) {
    message("Error: ", conditionMessage(e))
    default_value
  },
  warning = function(w) {
    message("Warning: ", conditionMessage(w))
    suppressWarnings(risky_operation())
  }
)
```

---

## 요약
R 관용구는 벡터화(루프 방지), tidyverse 파이프(`|>`), 할당을 위한 `<-`, snake_case 이름 지정 및 `purrr`를 사용한 함수형 프로그래밍을 강조합니다. Tidyverse 스타일 가이드를 따르고, 린팅에는 lintr을 사용하고, 서식 지정에는 styler를 사용하세요. R 값은 벡터화된 작업과 읽을 수 있는 데이터 변환을 위한 파이프입니다.