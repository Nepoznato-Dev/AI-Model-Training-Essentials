---
# Métadonnées
titre : "R"
description : "Référence complète sur le langage de programmation R couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [r, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "31 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
#R
R est un langage et un environnement de programmation spécialement conçus pour le calcul statistique et l'analyse de données. Créé par Ross Ihaka et Robert Gentleman à l'Université d'Auckland en 1993 (d'où « R »), il s'agit d'une implémentation du langage S avec des extensions importantes. R est open source et maintenu par la R Core Team. Il s'agit de l'outil standard destiné aux statisticiens, aux analystes de données et aux chercheurs du monde universitaire, de la santé, de la finance et du gouvernement.
R excelle dans la manipulation des données, la modélisation statistique, la visualisation et le reporting. Son écosystème de packages (CRAN) compte plus de 20 000 packages couvrant pratiquement toutes les méthodes statistiques jamais conçues.
---

## Pourquoi R est important
- **Calcul statistique** : la collection la plus complète de méthodes statistiques dans n'importe quelle langue.
- **Visualisation des données** : ggplot2 produit des graphiques de qualité publication. La grammaire du paradigme graphique est inégalée.
- **Recherche reproductible** : R Markdown / Quarto vous permet de combiner le code, les résultats et la narration dans un seul document.
- **Norme académique** : Utilisé en statistiques, bioinformatique, épidémiologie, écologie, économie et sciences sociales.
- **Tidyverse** : un ensemble cohérent de packages (dplyr, ggplot2, Tidyr, readr) qui rendent l'analyse des données élégante et cohérente.
- **Gratuit et open source** : Aucun frais de licence ; activement entretenu par une communauté mondiale.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Performances** | Monothread par défaut ; lent pour les grands ensembles de données | Utilisez`data.table`, des packages parallèles ou Rcpp pour l'intégration C++ |
| **Utilisation de la mémoire** | Charge des ensembles de données entiers dans la RAM | Utilisez`data.table::fread`, package arrow pour le traitement hors noyau |
| **Pas un langage à usage général** | Gênant pour le développement Web, la programmation système ou les applications | Utilisez Python, Go ou JavaScript pour les tâches non statistiques |
| **Syntaxe incohérente** | La base R a des bizarreries ; différents packages utilisent des conventions différentes | Utilisez Tidyverse pour plus de cohérence |
| **Marché du travail** | Postes principalement universitaires/de recherche | Les postes en science des données préfèrent de plus en plus Python |
---

## Fondamentaux de la syntaxe
### Opérations de base
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

### Tidyverse (Modern R)
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

### Visualisation avec ggplot2
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

### Modélisation statistique
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

## Syntaxe et modèles avancés
### Systèmes d'objets S3 et S4
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

### Classes de référence R6
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

### Évaluation non standard et métaprogrammation
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

### Surcharge des opérateurs
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

## Concurrence et parallélisme
### Le package parallèle
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

### Le futur Forfait
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

### foreach/doParallèle
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

## Configuration du projet et système de construction
### Structure du paquet
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

### DESCRIPTION Fichier
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

### Gestion des dépendances avec renv
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### CI/CD avec actions GitHub
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

## Tests
### tester ce framework
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

## Interopérabilité
### Intégration C/C++ avec Rcpp
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

### Appeler Python depuis R
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

## Modèles de conception
### Modèle 1 : évaluation soignée pour des fonctions flexibles
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

### Modèle 2 : Programmation fonctionnelle avec ronronnement
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

### Modèle 3 : Pipeline de génération de rapports
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

## Performances et optimisation
### Outils de profilage
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

### Vectorisation et data.table
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

### Optimisation de la mémoire
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

## Déploiement
### Publication de packages sur CRAN
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### Application brillante
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

### Déploiement de conteneurs
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## Quand utiliser R
| Scénario | Pourquoi R | Meilleure alternative |
|--------------|-------|---------|
| Analyse statistique | Méthodes statistiques les plus complètes | Python (modèles de statistiques, scipy) |
| Visualisation des données | ggplot2 est inégalé en termes de qualité de publication | Python (matplotlib, seaborn) pour l'interactivité |
| Recherche académique | Standard dans de nombreux domaines | — |
| Bioinformatique | Bioconductor propose plus de 2 000 packages spécialisés | Python pour les pipelines de production |
| Rapports (R Markdown/Quarto) | Analyse intégrée + récit | Jupyter (Python) |
| Systèmes de production ML | Non conçu pour le déploiement | Python, Java |
| Développement Web | Ne convient pas | Javascript, Python |
| Traitement de données à grande échelle | Lié à la mémoire | Python (PySpark), SQL |
---

## Résumé
R est le langage des statistiques. Pour l'analyse des données, la visualisation et la modélisation statistique, il reste inégalé en termes de profondeur et d'étendue. Le Tidyverse a modernisé le langage et R Markdown/Quarto simplifie la recherche reproductible. Si Python a gagné du terrain dans la science des données de manière générale, R reste l'outil du spécialiste du travail statistique rigoureux. Pour quiconque effectue des recherches quantitatives, l’apprentissage de R est essentiel.
---

## Gestion avancée des données
### data.table Analyse approfondie
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

### Évaluation soignée et colonnes dynamiques
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

## Analyse approfondie de la modélisation statistique
### Régression avancée
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

### Analyse des séries chronologiques
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

### Apprentissage automatique avec des modèles rangés
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
