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
# R — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang kasangkapan, pakete, at imprastraktura sa R ​​ecosystem.
---

## R Mga Pagpapatupad
| Pagpapatupad | Mga Tala |
|--------------|-------|
| **R (GNU R)** | Karaniwan, pinaka-malawakang ginagamit |
| **RStudio** | IDE na may pinagsamang R |
| **Positron** | Next-gen IDE (Posit) |
| **Microsoft R Open** | Na-optimize (naka-archive) |
| **pqR** | Parallel R |
| **Renji** | JVM-based na R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **install.packages()** | Mga pakete ng CRAN |
| **CRAN** | Comprehensive R Archive Network (19,000+ package) |
| **Bioconductor** | Genomics/biology packages |
| **mga remote** | I-install mula sa GitHub |
| **pak** | Makabagong package installer |
| **renv** | Proyekto-lokal na kapaligiran |
| **packrat** | Pamamahala ng dependency (legacy) |
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

## Ang Tidyverse
| Package | Layunin |
|---------|---------|
| **dplyr** | Pagmamanipula ng data |
| **maglinis** | Pag-aayos ng data |
| **ggplot2** | Visualization ng data |
| **readr** | Mabilis na pagbabasa ng CSV/file |
| **purrr** | Functional na programming |
| **kiliti** | Mga modernong data frame |
| **stringr** | Pagmamanipula ng string |
| **forcats** | Factor handling |
| **lubridate** | Petsa/oras ng pangangasiwa |
| **magrittr** | Operator ng tubo (%>%) |
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

## Data Science at Istatistika
| Package | Layunin |
|---------|---------|
| **mga tidymodel** | Modeling framework (pinapalitan ang caret) |
| **caret** | Machine learning (legacy) |
| **randomForest** | Random na kagubatan |
| **xgboost** | Pagpapalakas ng gradient |
| **glmnet** | Regularized regression |
| **kaligtasan** | Survival analysis |
| **lme4** | Mixed-effects na mga modelo |
| **brms** | Bayesian regression (Stan) |
| **rstan** | Stan interface |
| **pagtataya** | Pagtataya ng serye ng oras |
| **tsibble** | Data ng serye ng oras |
| **pabula** | Mga modelo ng serye ng oras |
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
| Teknolohiya | Uri |
|------------|------|
| **DBI** | Pamantayan ng interface ng database |
| **dbplyr** | dplyr backend para sa mga database |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Mga koneksyon sa ODBC |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **testthat** | Unit testing (pinakatanyag) |
| **tinytest** | Magaan na pagsubok |
| **lintr** | Code linting |
| **covr** | Saklaw ng code |
| **pangungutya** | Nanunuya |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **lintr** | Code linting |
| **styler** | Pag-format ng code |
| **magandang pagsasanay** | Mga pagsusuri sa kalidad ng package |
| **covr** | Saklaw ng code |
| **cyclocomp** | Cyclomatic complexity |
| **pkgdown** | Website ng dokumentasyon ng package |
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
| Tool | Layunin |
|------|---------|
| **R Markdown** | Mga reproducible na ulat |
| **Quarto** | Next-gen publishing |
| **knitr** | Pagbuo ng dinamikong ulat |
| **mga target** | Pamamahala ng pipeline |
| **drake** | Mga parang pipeline (legacy) |
| **bookdown** | Mga aklat mula sa R ​​Markdown |
| **blogdown** | Mga Blog mula sa R ​​Markdown |
| **distill** | Mga artikulong pang-agham |
| **makintab** | Mga interactive na web app |
| **flexdashboard** | Mga Dashboard |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **data.table** | Mabilis na pagmamanipula ng data |
| **R6** | Mga reference na klase (OOP) |
| **rlang** | R programming tools |
| **vctrs** | Mga klase ng vector |
| **pandikit** | String interpolation |
| **cli** | Mga interface ng command-line |
| **withr** | Pansamantalang estado |
| **fs** | Mga pagpapatakbo ng file system |
| **httr2** | HTTP client |
| **jsonlite** | Pag-parse ng JSON |
| **xml2** | XML/HTML na pag-parse |
| **rvest** | Web scraping |
| **parallel** | Built-in na paralelismo |
| **kinabukasan** | Pinag-isang paralelismo |
| **furrr** | purrr + hinaharap |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **RStudio** | Ang karaniwang R IDE |
| **Positron** | Next-gen IDE (Posit) |
| **VS Code + R extension** | Magaan, R LSP |
| **Neovim + nvim-r** | Nakabatay sa terminal |
| **Jupyter + IRkernel** | Interface ng notebook |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Makintab na Server** | Mag-host ng Shiny apps |
| **Posit Connect** | Enterprise R deployment |
| **Tubero** | REST API mula sa R ​​|
| **Docker** | Containerized (rocker images) |
| **Quarto + Netlify** | Mga static na site |
| **AWS Lambda** | Walang Server R |
| **mga target** | Orkestrasyon ng pipeline |
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

## Buod
Ang ecosystem ng R ay ang gold standard para sa statistical computing at data science. Ang karaniwang stack ay: **R 4.3+** bilang runtime, **RStudio** bilang IDE, **tidyverse** para sa manipulasyon at visualization ng data, **tidymodels** para sa machine learning, **ggplot2** para sa pag-plot, **testthat** para sa pagsubok, **lintr** para sa linting, at **Quarto** para sa mga reproducible na ulat. Ang R ay mahusay sa mga istatistika, visualization ng data, bioinformatics (Bioconductor), at reproducible na pananaliksik. Ang CRAN ecosystem ay may 19,000+ package. Para sa deployment ng produksyon, ginagawa ng **Plumber** ang mga R script sa mga API, at ang **Shiny** ay gumagawa ng mga interactive na web application.