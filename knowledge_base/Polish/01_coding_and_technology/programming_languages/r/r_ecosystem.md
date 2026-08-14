---
# Metadata
title: "R — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the R ecosystem including tools, packages, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# R — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, pakiety i infrastrukturę w ekosystemie R.
---

## Implementacje R
| Wdrożenie | Notatki |
|--------------|-------|
| **R (GNU R)** | Standardowy, najczęściej używany |
| **RStudio** | IDE ze zintegrowanym R |
| **Pozyton** | IDE nowej generacji (założenie) |
| **Microsoft R Otwórz** | Zoptymalizowany (zarchiwizowany) |
| **pqR** | Równolegle R |
| **Renjin** | R |. oparty na JVM
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **zainstaluj.pakiety()** | Pakiety CRAN |
| **ŻUR** | Kompleksowa sieć archiwów R (ponad 19 000 pakietów) |
| **Bioprzewodnik** | Pakiety genomika/biologia |
| **piloty** | Zainstaluj z GitHuba |
| **pak** | Nowoczesny instalator pakietów |
| **renv** | Środowiska projektowe |
| **pakrat** | Zarządzanie zależnościami (starsza wersja) |
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

## Uporządkowany świat
| Pakiet | Cel |
|--------|---------|
| **dplyr** | Manipulacja danymi |
| **posprzątaj** | Porządkowanie danych |
| **ggplot2** | Wizualizacja danych |
| **czytaj** | Szybki odczyt CSV/pliku |
| **mruczenie** | Programowanie funkcjonalne |
| **bełkot** | Nowoczesne ramki danych |
| **string** | Manipulacja ciągiem |
| **forkoty** | Obsługa czynników |
| **smarować** | Obsługa daty/godziny |
| **magrittr** | Operator rury (%>%) |
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

## Analiza danych i statystyka
| Pakiet | Cel |
|--------|---------|
| **porządne modele** | Ramy modelowania (zastępuje karetkę) |
| **kartka** | Uczenie maszynowe (starsze) |
| **losowy Las** | Losowe lasy |
| **xgboost** | Wzmocnienie gradientu |
| **glmnet** | Uregulowana regresja |
| **przetrwanie** | Analiza przeżycia |
| **lme4** | Modele z efektami mieszanymi |
| **brm** | Regresja bayesowska (Stan) |
| **pierwszy** | Interfejs Stana |
| **prognoza** | Prognozowanie szeregów czasowych |
| **tsibble** | Dane szeregów czasowych |
| **bajka** | Modele szeregów czasowych |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **DBI** | Standard interfejsu bazy danych |
| **dbplyr** | backend dplyr dla baz danych |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Połączenia ODBC |
| **wielkie zapytanie** | Google BigQuery |
| **błyszczący** | Apache Spark |
| **strzałka** | Strzałka Apache / Parkiet |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **przetestuj** | Testy jednostkowe (najpopularniejsze) |
| **małytest** | Lekkie testy |
| **lintr** | Linting kodu |
| **pokrycie** | Pokrycie kodu |
| **kpina** | Kpiąco |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **lintr** | Linting kodu |
| **stylizator** | Formatowanie kodu |
| **dobra praktyka** | Kontrole jakości opakowań |
| **pokrycie** | Pokrycie kodu |
| **cyklomp** | Złożoność cyklomatyczna |
| **pkgdown** | Witryna internetowa z dokumentacją pakietu |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Powtarzalne badania
| Narzędzie | Cel |
|------|-------------|
| **R Przecena** | Powtarzalne raporty |
| **Ćwiartka** | Publikacje nowej generacji |
| **dzierganie** | Dynamiczne generowanie raportów |
| **cele** | Zarządzanie rurociągami |
| **drak** | Rurociągi typu make (starsze) |
| **zarezerwuj** | Książki z R Markdown |
| **blog** | Blogi z R Markdown |
| **destyluj** | Artykuły naukowe |
| **błyszczące** | Interaktywne aplikacje internetowe |
| **elastyczny panel** | Panele |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **tabela danych** | Szybka manipulacja danymi |
| **R6** | Klasy referencyjne (OOP) |
| **rlang** | Narzędzia programistyczne R |
| **vctrs** | Klasy wektorowe |
| **klej** | Interpolacja ciągów |
| **kli** | Interfejsy wiersza poleceń |
| **z** | Stan tymczasowy |
| **fs** | Operacje na systemie plików |
| **httr2** | Klient HTTP |
| **jsonlite** | Analiza JSON |
| **xml2** | Analiza XML/HTML |
| **pozdrawiam** | Skrobanie sieci |
| **równolegle** | Wbudowana równoległość |
| **przyszłość** | Ujednolicona równoległość |
| **furrr** | mruczenie + przyszłość |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **RStudio** | Standardowe IDE R |
| **Pozyton** | IDE nowej generacji (założenie) |
| **Kod VS + rozszerzenie R** | Lekki, R LSP |
| **Neovim + nvim-r** | Oparte na terminalu |
| **Jupyter + jądro IR** | Interfejs notebooka |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Błyszczący serwer** | Hostuj aplikacje Shiny |
| **Połącz pozycję** | Wdrożenie Enterprise R |
| **Hydraulik** | API REST z R |
| **Doker** | Konteneryzowany (obrazy rockerów) |
| **Quarto + Netlify** | Strony statyczne |
| **AWS Lambda** | Bezserwerowy R |
| **cele** | Orkiestracja rurociągów |
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

## Streszczenie
Ekosystem R to złoty standard w obliczeniach statystycznych i nauce danych. Standardowy stos to: **R 4.3+** jako środowisko wykonawcze, **RStudio** jako IDE, **tidyverse** do manipulacji i wizualizacji danych, **tidymodels** do uczenia maszynowego, **ggplot2** do kreślenia, **testthat** do testowania, **lintr** do lintingu i **Quarto** do powtarzalnych raportów. R wyróżnia się statystyką, wizualizacją danych, bioinformatyką (Bioconductor) i powtarzalnymi badaniami. Ekosystem CRAN ma ponad 19 000 pakietów. W przypadku wdrożeń produkcyjnych **Hydraulik** zamienia skrypty R w interfejsy API, a **Shiny** tworzy interaktywne aplikacje internetowe.