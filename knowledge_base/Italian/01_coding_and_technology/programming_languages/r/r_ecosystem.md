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
# R: Guida all'ecosistema e agli strumenti
Questa guida illustra gli strumenti, i pacchetti e l'infrastruttura essenziali nell'ecosistema R.
---

## Implementazioni R
| Attuazione | Note |
|---------------|-------|
| **R (GNU R)** | Standard, più utilizzato |
| **RStudio** | IDE con R integrato |
| **Positrone** | IDE di nuova generazione (Posit) |
| **Microsoft R Open** | Ottimizzato (archiviato) |
| **pqR** | Parallelo R |
| **Renjin** | R basato su JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **install.packages()** | Pacchetti CRAN |
| **CRAN** | Rete di archivi R completa (oltre 19.000 pacchetti) |
| **Bioconduttore** | Pacchetti genomica/biologia |
| **telecomandi** | Installa da GitHub |
| **pacco** | Programma di installazione del pacchetto moderno |
| **renv** | Ambienti locali di progetto |
| **pacchetto** | Gestione delle dipendenze (legacy) |
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

## Il Tidyverse
| Pacchetto | Scopo |
|---------|---------|
| **dplir** | Manipolazione dei dati |
| **ordina** | Riordino dei dati |
| **ggplot2** | Visualizzazione dei dati |
| **leggi** | Lettura veloce di file/CSV |
| **fa le fusa** | Programmazione funzionale |
| **tibble** | Moderni frame di dati |
| **stringr** | Manipolazione delle stringhe |
| **forzature** | Gestione dei fattori |
| **lubrificare** | Gestione data/ora |
| **magrittr** | Operatore tubazione (%>%) |
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

## Scienza dei dati e statistica
| Pacchetto | Scopo |
|---------|---------|
| **modelli ordinati** | Framework di modellazione (sostituisce il cursore) |
| **accento circonflesso** | Apprendimento automatico (legacy) |
| **foresta casuale** | Foreste casuali |
| **xgboost** | Aumento del gradiente |
| **glmnet** | Regressione regolarizzata |
| **sopravvivenza** | Analisi di sopravvivenza |
| **lme4** | Modelli a effetti misti |
| **brms** | Regressione bayesiana (Stan) |
| **rstan** | Interfaccia Stan |
| **previsione** | Previsione delle serie temporali |
| **tsibble** | Dati delle serie temporali |
| **favola** | Modelli di serie storiche |
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

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **DBI** | Standard di interfaccia del database |
| **dbplyr** | Backend dplyr per database |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Connessioni ODBC |
| **grandequery** | Google BigQuery |
| **scintillante** | Apache Spark |
| **freccia** | Apache Freccia / Parquet |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **provache** | Test unitari (più popolari) |
| **piccolotest** | Test leggero |
| **lintr** | Linting del codice |
| **copertina** | Copertura del codice |
| **schernitura** | Beffardo |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **lintr** | Linting del codice |
| **stilatrice** | Formattazione del codice |
| **buona pratica** | Controlli di qualità del pacchetto |
| **copertina** | Copertura del codice |
| **ciclocomp** | Complessità ciclomatica |
| **pkgdown** | Sito web della documentazione del pacchetto |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Ricerca riproducibile
| Strumento | Scopo |
|------|---------|
| **Ribasso R** | Rapporti riproducibili |
| **Quarto** | Pubblicazione di nuova generazione |
| **maglia** | Generazione di report dinamici |
| **obiettivi** | Gestione della pipeline |
| **Drake** | Pipeline simili (legacy) |
| **prenota** | Libri di R Markdown |
| **blogdown** | Blog di R Markdown |
| **distillare** | Articoli scientifici |
| **lucido** | App Web interattive |
| **cruscotto flessibile** | Cruscotti |
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

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **data.tabella** | Manipolazione veloce dei dati |
| **R6** | Classi di riferimento (OOP) |
| **lingua** | Strumenti di programmazione R |
| **vctrs** | Classi vettoriali |
| **colla** | Interpolazione di stringhe |
| **cli** | Interfacce della riga di comando |
| **con** | Stato temporaneo |
| **fs** | Operazioni sul file system |
| **httr2** | Client HTTP |
| **jsonlite** | Analisi JSON |
| **xml2** | Analisi XML/HTML |
| **rvest** | Raschiamento Web |
| **parallelo** | Parallelismo incorporato |
| **futuro** | Parallelismo unificato |
| **furrr** | fusa + futuro |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **RStudio** | L'IDE R standard |
| **Positrone** | IDE di nuova generazione (Posit) |
| **Codice VS + estensione R** | Leggero, R LSP |
| **Neovim + nvim-r** | Basato su terminale |
| **Jupyter + IRkernel** | Interfaccia notebook |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Server brillante** | Ospita app brillanti |
| **Posiziona Connetti** | Distribuzione di Enterprise R |
| **Idraulico** | API REST da R |
| **Docker** | Containerizzato (immagini rocker) |
| **Quarto + Netlify** | Siti statici |
| **AWS Lambda** | Senza server R |
| **obiettivi** | Orchestrazione della pipeline |
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

## Riepilogo
L'ecosistema di R è il gold standard per il calcolo statistico e la scienza dei dati. Lo stack standard è: **R 4.3+** come runtime, **RStudio** come IDE, **tidyverse** per la manipolazione e la visualizzazione dei dati, **tidymodels** per l'apprendimento automatico, **ggplot2** per la stampa, **testthat** per i test, **lintr** per l'linting e **Quarto** per i report riproducibili. R eccelle in statistica, visualizzazione dei dati, bioinformatica (bioconduttore) e ricerca riproducibile. L'ecosistema CRAN ha oltre 19.000 pacchetti. Per la distribuzione in produzione, **Plumber** trasforma gli script R in API e **Shiny** crea applicazioni Web interattive.