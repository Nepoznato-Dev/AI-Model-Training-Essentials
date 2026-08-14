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
# R — Guide de l'écosystème et des outils
Ce guide couvre les outils, packages et infrastructures essentiels de l'écosystème R.
---

## Implémentations R
| Mise en œuvre | Remarques |
|---------------|-------|
| **R (GNU R)** | Standard, le plus utilisé |
| **RStudio** | IDE avec R intégré |
| **Positron** | IDE de nouvelle génération (Posit) |
| **Microsoft R Ouvert** | Optimisé (archivé) |
| **pqR** | Parallèle R |
| **Renjin** | R basé sur JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **install.packages()** | Forfaits CRAN |
| **CRAN** | Réseau d'archives R complet (plus de 19 000 packages) |
| **Bioconducteur** | Forfaits génomique/biologie |
| **télécommandes** | Installer depuis GitHub |
| **pak** | Installateur de packages moderne |
| **renv** | Environnements locaux du projet |
| **packrat** | Gestion des dépendances (hérité) |
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

## Le Tidyverse
| Forfait | Objectif |
|---------|---------|
| **dplyr** | Manipulation de données |
| **rangement** | Rangement des données |
| **ggplot2** | Visualisation des données |
| **lire** | Lecture rapide de fichiers CSV/fichier |
| **ronronner** | Programmation fonctionnelle |
| **tibble** | Trames de données modernes |
| **stringr** | Manipulation de chaînes |
| **forcats** | Gestion des facteurs |
| **lubrifier** | Gestion date/heure |
| **magrittr** | Opérateur de canalisations (%>%) |
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

## Science des données et statistiques
| Forfait | Objectif |
|---------|---------|
| **modèles rangés** | Cadre de modélisation (remplace le curseur) |
| **caret** | Apprentissage automatique (hérité) |
| **forêt aléatoire** | Forêts aléatoires |
| **xgboost** | Augmentation du dégradé |
| **glmnet** | Régression régularisée |
| **survie** | Analyse de survie |
| **lme4** | Modèles à effets mixtes |
| **brms** | Régression bayésienne (Stan) |
| **istan** | Interface Stan |
| **prévision** | Prévisions de séries chronologiques |
| **tsibble** | Données de séries chronologiques |
| **fable** | Modèles de séries chronologiques |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **DBI** | Norme d'interface de base de données |
| **dbplyr** | backend dplyr pour les bases de données |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Connexions ODBC |
| **grande requête** | Google BigQuery |
| **étincelle** | Apache Spark |
| **flèche** | Flèche Apache / Parquet |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **testez cela** | Tests unitaires (les plus populaires) |
| **petit test** | Tests légers |
| **lintr** | Pelucheux de code |
| **cvr** | Couverture du code |
| **moquerie** | Moqueur |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **lintr** | Pelucheux de code |
| **styleur** | Formatage des codes |
| **bonne pratique** | Contrôles de qualité des colis |
| **cvr** | Couverture du code |
| **cyclocomp** | Complexité cyclomatique |
| **pkgdown** | Site Web de documentation des packages |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Recherche reproductible
| Outil | Objectif |
|------|--------------|
| **R Markdown** | Rapports reproductibles |
| **Quarto** | Publication de nouvelle génération |
| **tricot** | Génération de rapports dynamiques |
| **cibles** | Gestion des pipelines |
| **canard** | Pipelines de type Make-like (hérités) |
| **répertoire** | Livres de R Markdown |
| **blog** | Blogs de R Markdown |
| **distiller** | Articles scientifiques |
| **brillant** | Applications Web interactives |
| **tableau de bord flexible** | Tableaux de bord |
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

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **données.table** | Manipulation rapide des données |
| **R6** | Classes de référence (POO) |
| **rlang** | Outils de programmation R |
| **magnétoscopes** | Classes de vecteurs |
| **colle** | Interpolation de chaînes |
| **cli** | Interfaces de ligne de commande |
| **avecr** | État temporaire |
| **fs** | Opérations du système de fichiers |
| **httr2** | Client HTTP |
| **jsonlite** | Analyse JSON |
| **xml2** | Analyse XML/HTML |
| **rvest** | Grattage Web |
| **parallèle** | Parallélisme intégré |
| **futur** | Parallélisme unifié |
| **furr** | ronronnement + futur |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **RStudio** | Le RIDE standard |
| **Positron** | IDE de nouvelle génération (Posit) |
| **Code VS + extension R** | Léger, R LSP |
| **Neovim + nvim-r** | Basé sur un terminal |
| **Jupyter + IRkernel** | Interface du bloc-notes |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Serveur brillant** | Héberger des applications Shiny |
| **Posit Connect** | Déploiement Entreprise R |
| **Plombier** | API REST de R |
| **Docker** | Conteneurisé (images rocker) |
| **Quarto + Netlify** | Sites statiques |
| **AWS Lambda** | R sans serveur |
| **cibles** | Orchestration des pipelines |
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

## Résumé
L'écosystème de R est la référence en matière de calcul statistique et de science des données. La pile standard est : **R 4.3+** comme environnement d'exécution, **RStudio** comme IDE, **tidyverse** pour la manipulation et la visualisation des données, **tidymodels** pour l'apprentissage automatique, **ggplot2** pour le traçage, **testthat** pour les tests, **lintr** pour le peluchage et **Quarto** pour les rapports reproductibles. R excelle dans les statistiques, la visualisation de données, la bioinformatique (Bioconducteur) et la recherche reproductible. L'écosystème CRAN compte plus de 19 000 packages. Pour le déploiement en production, **Plumber** transforme les scripts R en API et **Shiny** crée des applications Web interactives.