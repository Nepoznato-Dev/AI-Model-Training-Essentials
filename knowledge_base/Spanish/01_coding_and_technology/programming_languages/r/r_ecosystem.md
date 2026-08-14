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
# R — Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los paquetes y la infraestructura esenciales en el ecosistema R.
---

## Implementaciones de R
| Implementación | Notas |
|---------------|-------|
| **R (GNUR)** | Estándar, más utilizado |
| **RStudio** | IDE con R integrado |
| **Positrones** | IDE de próxima generación (Posit) |
| **Microsoft R Abierto** | Optimizado (archivado) |
| **pqR** | Paralelo R |
| **Renjin** | R basado en JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **instalar.paquetes()** | Paquetes CRAN |
| **GRAN** | Red integral de archivos R (más de 19 000 paquetes) |
| **Bioconductor** | Paquetes de genómica/biología |
| **mandos a distancia** | Instalar desde GitHub |
| **paquete** | Instalador de paquetes moderno |
| **renv** | Entornos locales de proyecto |
| **paquete** | Gestión de dependencias (heredado) |
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

## El ordenadoverso
| Paquete | Propósito |
|---------|---------|
| **dplyr** | Manipulación de datos |
| **ordenado** | Ordenamiento de datos |
| **ggplot2** | Visualización de datos |
| **leer** | Lectura rápida de archivos/CSV |
| **ronroneo** | Programación funcional |
| **tibble** | Marcos de datos modernos |
| **cadena** | Manipulación de cadenas |
| **forgatos** | Manejo de factores |
| **lubricar** | Manejo de fecha/hora |
| **magrittr** | Operador de tubería (%>%) |
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

## Ciencia de datos y estadística
| Paquete | Propósito |
|---------|---------|
| **modelos ordenados** | Marco de modelado (reemplaza el cursor) |
| **intercalación** | Aprendizaje automático (heredado) |
| **Bosque aleatorio** | Bosques aleatorios |
| **xgimpulso** | Aumento de gradiente |
| **glmnet** | Regresión regularizada |
| **supervivencia** | Análisis de supervivencia |
| **lme4** | Modelos de efectos mixtos |
| **brms** | Regresión bayesiana (Stan) |
| **rstan** | Interfaz Stan |
| **pronóstico** | Previsión de series temporales |
| **tsibble** | Datos de series temporales |
| **fábula** | Modelos de series temporales |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **DBI** | Estándar de interfaz de base de datos |
| **dbplyr** | backend dplyr para bases de datos |
| **RSQLite** | SQLite |
| **RPosgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Conexiones ODBC |
| **gran consulta** | Google Big Query |
| **brillante** | Chispa Apache |
| **flecha** | Flecha Apache / Parquet |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **prueba que** | Pruebas unitarias (más populares) |
| **pequeño** | Pruebas ligeras |
| **lintr** | Eliminación de código |
| **cubierta** | Cobertura de código |
| **burla** | Burlarse |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **lintr** | Eliminación de código |
| **estilista** | Formato de código |
| **buenas prácticas** | Controles de calidad del paquete |
| **cubierta** | Cobertura de código |
| **ciclocomp** | Complejidad ciclomática |
| **paquete reducido** | Sitio web de documentación del paquete |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Investigación reproducible
| Herramienta | Propósito |
|------|---------|
| **Rebaja R** | Informes reproducibles |
| **Cuarto** | Publicación de próxima generación |
| **tejer** | Generación de informes dinámicos |
| **objetivos** | Gestión de oleoductos |
| **draco** | Tuberías similares (heredadas) |
| **liquidación** | Libros de R Markdown |
| **blogdown** | Blogs de R Markdown |
| **destilar** | Artículos científicos |
| **brillante** | Aplicaciones web interactivas |
| **tablero flexible** | Paneles de control |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **tabla.de.datos** | Manipulación rápida de datos |
| **R6** | Clases de referencia (OOP) |
| **rlang** | Herramientas de programación R |
| **vctr** | Clases de vectores |
| **pegamento** | Interpolación de cadenas |
| **cli** | Interfaces de línea de comandos |
| **con** | Estado temporal |
| **fs** | Operaciones del sistema de archivos |
| **httr2** | Cliente HTTP |
| **jsonlite** | Análisis JSON |
| **xml2** | Análisis XML/HTML |
| **chaleco** | Raspado web |
| **paralelo** | Paralelismo incorporado |
| **futuro** | Paralelismo unificado |
| **furr** | ronroneo + futuro |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **RStudio** | El estándar R IDE |
| **Positrones** | IDE de próxima generación (Posit) |
| **Código VS + extensión R** | Ligero, R LSP |
| **Neovim + nvim-r** | Basado en terminal |
| **Jupyter + IRkernel** | Interfaz del portátil |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Servidor brillante** | Alojar aplicaciones Shiny |
| **Positar Conectar** | Implementación de Enterprise R |
| **Fontanero** | API REST de R |
| **Acoplador** | En contenedores (imágenes rockeras) |
| **Cuarto + Netlify** | Sitios estáticos |
| **AWS Lambda** | R sin servidor |
| **objetivos** | Orquestación de tuberías |
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

## Resumen
El ecosistema de R es el estándar de oro para la informática estadística y la ciencia de datos. La pila estándar es: **R 4.3+** como tiempo de ejecución, **RStudio** como IDE, **tidyverse** para manipulación y visualización de datos, **tidymodels** para aprendizaje automático, **ggplot2** para trazar, **testthat** para pruebas, **lintr** para linting y **Quarto** para informes reproducibles. R destaca en estadística, visualización de datos, bioinformática (Bioconductor) e investigación reproducible. El ecosistema CRAN tiene más de 19.000 paquetes. Para la implementación en producción, **Plumber** convierte scripts R en API y **Shiny** crea aplicaciones web interactivas.