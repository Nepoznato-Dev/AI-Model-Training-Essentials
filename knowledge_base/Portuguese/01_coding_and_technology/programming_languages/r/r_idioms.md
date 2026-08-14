<!--
---
# Metadata
title: "R — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic R code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# R — Padrões Idiomáticos e Melhores Práticas
Este guia aborda padrões idiomáticos e práticas recomendadas para escrever código R idiomático e limpo.
---

## Estilo Tidyverso
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

## Vetorização
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

## Funções
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

## Padrões arrumados
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

## Tratamento de erros
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

## Resumo
Os idiomas R enfatizam: vetorização (evitar loops), tubos tidyverse (`|>`),`<-`para atribuição, nomeação de Snake_case e programação funcional com`purrr`. Siga o Guia de estilo do Tidyverse, use lintr para linting e styler para formatação. R valoriza as operações vetorizadas e o canal para transformações de dados legíveis.