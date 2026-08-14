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
# R – Leitfaden für Ökosysteme und Werkzeuge
Dieser Leitfaden behandelt die wesentlichen Tools, Pakete und Infrastruktur im R-Ökosystem.
---

## R-Implementierungen
| Umsetzung | Notizen |
|---------------|-------|
| **R (GNU R)** | Standard, am weitesten verbreitet |
| **RStudio** | IDE mit integriertem R |
| **Positron** | IDE der nächsten Generation (Posit) |
| **Microsoft R Open** | Optimiert (archiviert) |
| **pqR** | Parallel R |
| **Renjin** | JVM-basiertes R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **install.packages()** | CRAN-Pakete |
| **KRAN** | Umfassendes R-Archivnetzwerk (über 19.000 Pakete) |
| **Bioleiter** | Genomik/Biologie-Pakete |
| **Fernbedienungen** | Von GitHub installieren |
| **pak** | Moderner Paketinstaller |
| **renv** | Projektlokale Umgebungen |
| **Packrat** | Abhängigkeitsmanagement (Legacy) |
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

## Das Tidyverse
| Paket | Zweck |
|---------|---------|
| **dplyr** | Datenmanipulation |
| **aufgeräumt** | Datenbereinigung |
| **ggplot2** | Datenvisualisierung |
| **readr** | Schnelles Lesen von CSV/Dateien |
| **schnurr** | Funktionale Programmierung |
| **Tibble** | Moderne Datenrahmen |
| **stringr** | String-Manipulation |
| **forcats** | Faktorbehandlung |
| **schmieren** | Datums-/Uhrzeitverarbeitung |
| **magrittr** | Pipe-Operator (%>%) |
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

## Datenwissenschaft und Statistik
| Paket | Zweck |
|---------|---------|
| **ordentliche Modelle** | Modellierungsrahmen (ersetzt Caret) |
| **Caret** | Maschinelles Lernen (alt) |
| **randomForest** | Zufällige Wälder |
| **xgboost** | Steigungsverstärkung |
| **glmnet** | Regularisierte Regression |
| **Überleben** | Überlebensanalyse |
| **lme4** | Modelle mit gemischten Effekten |
| **brms** | Bayesianische Regression (Stan) |
| **rstan** | Stan-Schnittstelle |
| **Prognose** | Zeitreihenvorhersage |
| **tsibble** | Zeitreihendaten |
| **Fabel** | Zeitreihenmodelle |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **DBI** | Datenbankschnittstellenstandard |
| **dbplyr** | dplyr Backend für Datenbanken |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC-Verbindungen |
| **bigrquery** | Google BigQuery |
| **funkelnd** | Apache Spark |
| **Pfeil** | Apache-Pfeil / Parkett |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **testdas** | Unit-Tests (am beliebtesten) |
| **winzigtest** | Leichtbauprüfung |
| **lintr** | Code-Linting |
| **cover** | Codeabdeckung |
| **Spott** | Spott |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **lintr** | Code-Linting |
| **Styler** | Codeformatierung |
| **gute Praxis** | Paketqualitätsprüfungen |
| **cover** | Codeabdeckung |
| **Cyclocomp** | Zyklomatische Komplexität |
| **Paketdown** | Website zur Paketdokumentation |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Reproduzierbare Forschung
| Werkzeug | Zweck |
|------|---------|
| **R-Abschlag** | Reproduzierbare Berichte |
| **Quarto** | Publishing der nächsten Generation |
| **strick** | Dynamische Berichtserstellung |
| **Ziele** | Pipeline-Management |
| **Drake** | Make-like-Pipelines (alt) |
| **Bookdown** | Bücher von R Markdown |
| **Blogdown** | Blogs von R Markdown |
| **destillieren** | Wissenschaftliche Artikel |
| **glänzend** | Interaktive Web-Apps |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Datentabelle** | Schnelle Datenmanipulation |
| **R6** | Referenzklassen (OOP) |
| **rlang** | R-Programmiertools |
| **vctrs** | Vektorklassen |
| **Kleber** | String-Interpolation |
| **cli** | Befehlszeilenschnittstellen |
| **mitr** | Temporärer Zustand |
| **fs** | Dateisystemoperationen |
| **httr2** | HTTP-Client |
| **jsonlite** | JSON-Analyse |
| **xml2** | XML/HTML-Analyse |
| **rvest** | Web-Scraping |
| **parallel** | Eingebaute Parallelität |
| **Zukunft** | Einheitliche Parallelität |
| **furrr** | Schnurren + Zukunft |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **RStudio** | Die Standard-R-IDE |
| **Positron** | IDE der nächsten Generation (Posit) |
| **VS-Code + R-Erweiterung** | Leicht, R LSP |
| **Neovim + nvim-r** | Terminalbasiert |
| **Jupyter + IRkernel** | Notebook-Schnittstelle |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Shiny Server** | Shiny-Apps hosten |
| **Posit Connect** | Enterprise R-Bereitstellung |
| **Klempner** | REST-API von R |
| **Docker** | Containerisiert (Rockerbilder) |
| **Quarto + Netlify** | Statische Websites |
| **AWS Lambda** | Serverloses R |
| **Ziele** | Pipeline-Orchestrierung |
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

## Zusammenfassung
Das Ökosystem von R ist der Goldstandard für statistische Berechnungen und Datenwissenschaft. Der Standard-Stack ist: **R 4.3+** als Laufzeit, **RStudio** als IDE, **tidyverse** für Datenmanipulation und Visualisierung, **tidymodels** für maschinelles Lernen, **ggplot2** für Plotting, **testthat** für Tests, **lintr** für Linting und **Quarto** für reproduzierbare Berichte. R zeichnet sich durch Statistik, Datenvisualisierung, Bioinformatik (Bioconductor) und reproduzierbare Forschung aus. Das CRAN-Ökosystem umfasst mehr als 19.000 Pakete. Für die Produktionsbereitstellung wandelt **Plumber** R-Skripte in APIs um und **Shiny** erstellt interaktive Webanwendungen.