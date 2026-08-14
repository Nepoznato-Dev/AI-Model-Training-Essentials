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
# R — Ecosystem & Tooling Guide

This guide covers the essential tools, packages, and infrastructure in the R ecosystem.

---

## R Implementations

| Implementation | Notes |
|---------------|-------|
| **R (GNU R)** | Standard, most widely used |
| **RStudio** | IDE with integrated R |
| **Positron** | Next-gen IDE (Posit) |
| **Microsoft R Open** | Optimized (archived) |
| **pqR** | Parallel R |
| **Renjin** | JVM-based R |

```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Package Management

| Tool | Purpose |
|------|---------|
| **install.packages()** | CRAN packages |
| **CRAN** | Comprehensive R Archive Network (19,000+ packages) |
| **Bioconductor** | Genomics/biology packages |
| **remotes** | Install from GitHub |
| **pak** | Modern package installer |
| **renv** | Project-local environments |
| **packrat** | Dependency management (legacy) |

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

## The Tidyverse

| Package | Purpose |
|---------|---------|
| **dplyr** | Data manipulation |
| **tidyr** | Data tidying |
| **ggplot2** | Data visualization |
| **readr** | Fast CSV/file reading |
| **purrr** | Functional programming |
| **tibble** | Modern data frames |
| **stringr** | String manipulation |
| **forcats** | Factor handling |
| **lubridate** | Date/time handling |
| **magrittr** | Pipe operator (%>%) |

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

## Data Science & Statistics

| Package | Purpose |
|---------|---------|
| **tidymodels** | Modeling framework (replaces caret) |
| **caret** | Machine learning (legacy) |
| **randomForest** | Random forests |
| **xgboost** | Gradient boosting |
| **glmnet** | Regularized regression |
| **survival** | Survival analysis |
| **lme4** | Mixed-effects models |
| **brms** | Bayesian regression (Stan) |
| **rstan** | Stan interface |
| **forecast** | Time series forecasting |
| **tsibble** | Time series data |
| **fable** | Time series models |

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

## Database

| Technology | Type |
|------------|------|
| **DBI** | Database interface standard |
| **dbplyr** | dplyr backend for databases |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC connections |
| **bigrquery** | Google BigQuery |
| **sparklyr** | Apache Spark |
| **arrow** | Apache Arrow / Parquet |

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

## Testing

| Framework | Purpose |
|-----------|---------|
| **testthat** | Unit testing (most popular) |
| **tinytest** | Lightweight testing |
| **lintr** | Code linting |
| **covr** | Code coverage |
| **mockery** | Mocking |

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

## Code Quality

| Tool | Purpose |
|------|---------|
| **lintr** | Code linting |
| **styler** | Code formatting |
| **goodpractice** | Package quality checks |
| **covr** | Code coverage |
| **cyclocomp** | Cyclomatic complexity |
| **pkgdown** | Package documentation website |

```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Reproducible Research

| Tool | Purpose |
|------|---------|
| **R Markdown** | Reproducible reports |
| **Quarto** | Next-gen publishing |
| **knitr** | Dynamic report generation |
| **targets** | Pipeline management |
| **drake** | Make-like pipelines (legacy) |
| **bookdown** | Books from R Markdown |
| **blogdown** | Blogs from R Markdown |
| **distill** | Scientific articles |
| **shiny** | Interactive web apps |
| **flexdashboard** | Dashboards |

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

## Key Libraries

| Library | Purpose |
|---------|---------|
| **data.table** | Fast data manipulation |
| **R6** | Reference classes (OOP) |
| **rlang** | R programming tools |
| **vctrs** | Vector classes |
| **glue** | String interpolation |
| **cli** | Command-line interfaces |
| **withr** | Temporary state |
| **fs** | File system operations |
| **httr2** | HTTP client |
| **jsonlite** | JSON parsing |
| **xml2** | XML/HTML parsing |
| **rvest** | Web scraping |
| **parallel** | Built-in parallelism |
| **future** | Unified parallelism |
| **furrr** | purrr + future |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **RStudio** | The standard R IDE |
| **Positron** | Next-gen IDE (Posit) |
| **VS Code + R extension** | Lightweight, R LSP |
| **Neovim + nvim-r** | Terminal-based |
| **Jupyter + IRkernel** | Notebook interface |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Shiny Server** | Host Shiny apps |
| **Posit Connect** | Enterprise R deployment |
| **Plumber** | REST API from R |
| **Docker** | Containerized (rocker images) |
| **Quarto + Netlify** | Static sites |
| **AWS Lambda** | Serverless R |
| **targets** | Pipeline orchestration |

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

## Summary

R's ecosystem is the gold standard for statistical computing and data science. The standard stack is: **R 4.3+** as runtime, **RStudio** as IDE, **tidyverse** for data manipulation and visualization, **tidymodels** for machine learning, **ggplot2** for plotting, **testthat** for testing, **lintr** for linting, and **Quarto** for reproducible reports. R excels at statistics, data visualization, bioinformatics (Bioconductor), and reproducible research. The CRAN ecosystem has 19,000+ packages. For production deployment, **Plumber** turns R scripts into APIs, and **Shiny** creates interactive web applications.
