---
# Metadata
title: "R"
description: "Comprehensive reference for the R programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [r, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#R
R ni lugha ya programu na mazingira iliyoundwa mahsusi kwa ajili ya kompyuta ya takwimu na uchambuzi wa data. Iliundwa na Ross Ihaka na Robert Gentleman katika Chuo Kikuu cha Auckland mnamo 1993 (kwa hivyo "R"), ni utekelezaji wa lugha ya S yenye viendelezi muhimu. R ni chanzo wazi na hudumishwa na Timu ya R Core. Ni zana ya kawaida ya wanatakwimu, wachambuzi wa data na watafiti katika taaluma, huduma za afya, fedha na serikali.
R hufaulu katika upotoshaji wa data, muundo wa takwimu, taswira, na kuripoti. Mfumo wake wa ikolojia wa kifurushi (CRAN) una zaidi ya vifurushi 20,000 vinavyofunika karibu kila mbinu ya takwimu iliyowahi kubuniwa.
---

## Kwa nini R ni muhimu
- **Takwimu Kompyuta**: Mkusanyiko wa kina zaidi wa mbinu za takwimu katika lugha yoyote.
- **Taswira ya data**: ggplot2 hutoa picha za ubora wa uchapishaji. Sarufi ya dhana ya michoro hailingani.
- **Utafiti unaoweza kurudiwa**: R Markdown / Quarto hukuruhusu uchanganye msimbo, matokeo na masimulizi katika hati moja.
- **Kiwango cha kitaaluma**: Hutumika katika takwimu, habari za kibayolojia, epidemiolojia, ikolojia, uchumi na sayansi ya jamii.
- **Tidyverse**: Seti iliyounganishwa ya vifurushi (dplyr, ggplot2, tidyr, readr) ambayo hufanya uchanganuzi wa data kuwa mzuri na thabiti.
- **Chanzo huria na huria**: Hakuna gharama za leseni; inayodumishwa kikamilifu na jumuiya ya kimataifa.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Utendaji** | Threaded moja kwa chaguo-msingi; polepole kwa hifadhidata kubwa | Tumia`data.table`, vifurushi sambamba, au Rcpp kwa ushirikiano wa C++ |
| **Matumizi ya kumbukumbu** | Hupakia seti nzima za data kwenye RAM | Tumia`data.table::fread`, kifurushi cha mshale kwa usindikaji wa nje ya msingi |
| **Si lugha ya kusudi la jumla** | Si rahisi kwa ukuzaji wa wavuti, upangaji wa mifumo, au programu | Tumia Python, Go, au JavaScript kwa kazi zisizo za takwimu |
| **Sintaksia isiyolingana** | Base R ina quirks; vifurushi tofauti hutumia mikusanyiko tofauti | Tumia tidyverse kwa uthabiti |
| **Soko la ajira** | Mara nyingi majukumu ya kitaaluma/utafiti | Majukumu ya sayansi ya data yanazidi kupendelea Python |
---

## Misingi ya Sintaksia
### Shughuli za Msingi
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

### Tidyverse (R ya kisasa)
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

### Taswira na ggplot2
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

### Uundaji wa Kitakwimu
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

## Sintaksia na Miundo ya Kina
### Mifumo ya Kitu cha S3 na S4
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

### Madarasa ya Marejeleo ya R6
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

### Tathmini Isiyo ya Kawaida na Upangaji programu
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

### Kupakia kwa Opereta
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

## Concurrency & Usambamba
### Kifurushi sambamba
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

### Kifurushi cha siku zijazo
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

### foreach/fanyaSambamba
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Kifurushi
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

### MAELEZO Faili
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

### Usimamizi wa Utegemezi na rev
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### CI/CD yenye Vitendo vya GitHub
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

##Upimaji
### jaribu Mfumo huo
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

## Kuingiliana
### C/C++ Ushirikiano na Rcpp
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

### Inapigia simu Python kutoka kwa R
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

## Miundo ya Kubuni
### Mchoro wa 1: Tathmini Nadhifu kwa Kazi Zinazobadilika
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

### Muundo wa 2: Upangaji Utendaji na purrr
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

### Mchoro wa 3: Bomba la Uzalishaji wa Ripoti
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
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

### Vectorization na data.table
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

### Uboreshaji wa Kumbukumbu
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

## Usambazaji
### Uchapishaji wa Kifurushi kwa CRAN
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### Shiny Application
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

### Usambazaji wa Kontena
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## Wakati wa Kutumia R
| Hali | Kwa nini R | Mbadala Bora |
|----------|-------|-------------------|
| Uchambuzi wa takwimu | Mbinu za kina zaidi za takwimu | Python (mifano ya takwimu, scipy) |
| Taswira ya data | ggplot2 haiwezi kulinganishwa kwa ubora wa uchapishaji | Python (matplotlib, seaborn) kwa maingiliano |
| Utafiti wa kitaaluma | Kawaida katika nyanja nyingi | - |
| Bioinformatics | Bioconductor ina vifurushi 2,000+ maalum | Python kwa mabomba ya uzalishaji |
| Kuripoti (R Markdown/Quarto) | Uchambuzi jumuishi + simulizi | Jupyter (Python) |
| Uzalishaji mifumo ya ML | Haijaundwa kwa ajili ya kupelekwa | Chatu, Java |
| Ukuzaji wa wavuti | Haifai | JavaScript, Chatu |
| Usindikaji wa data kwa kiwango kikubwa | Kumbukumbu iliyofungwa | Python (PySpark), SQL |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`<-`na`=`kwa kazi?
**J:** Zote mbili zinagawia thamani, lakini`<-`ndiye opereta wa mgawo wa nahau wa R. Inafanya kazi katika muktadha wote, pamoja na simu za kazi za ndani:
```r
# Both work
x <- 10
x = 10

# <- works inside function argument lists (rare but valid)
mean(x <- 1:10)  # assigns AND computes mean

# = is required for named function arguments
mean(x = 1:10)   # named argument, NOT assignment

# Convention: use <- for assignment, = for function arguments
```

### Q2: Je, ninashughulikiaje kukosa data katika R?
**J:** R hutumia`NA`kwa thamani zinazokosekana. Kazi nyingi zina parameta ya `na.rm`:
```r
x <- c(1, 2, NA, 4, 5)
mean(x)              # NA — NA propagates
mean(x, na.rm = TRUE) # 3 — removes NAs first

# Check for NA
is.na(x)             # FALSE FALSE TRUE FALSE FALSE

# Remove NAs
clean <- na.omit(x)  # 1 2 4 5 (with attributes)

# Replace NAs
x[is.na(x)] <- 0

# NaN, NULL, Inf
is.nan(0/0)          # TRUE
is.null(NULL)        # TRUE
is.infinite(1/0)     # TRUE
```

### Q3: Ni lini ninapaswa kutumia`lapply`vs`sapply`vs`vapply`?
**J:** Zote zinatumia chaguo la kukokotoa juu ya orodha/vekta, lakini hutofautiana katika matokeo:
```r
# lapply — always returns a list
lapply(1:5, function(x) x^2)  # list(1, 4, 9, 16, 25)

# sapply — simplifies to vector/matrix if possible
sapply(1:5, function(x) x^2)  # c(1, 4, 9, 16, 25)

# vapply — like sapply but you specify the output type (safer)
vapply(1:5, function(x) x^2, numeric(1))  # c(1, 4, 9, 16, 25)

# Best practice: use vapply for safety, or purrr::map variants
library(purrr)
map_dbl(1:5, ~ .x^2)  # type-safe, returns double vector
```

### Q4: Je, ninawezaje kuunda taswira bora na ggplot2?
**J:** Fuata sarufi ya michoro - data ya ramani ya uzuri kwa sifa zinazoonekana:
```r
library(ggplot2)

# Layered approach
ggplot(data = mtcars, aes(x = wt, y = mpg, color = cyl)) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = FALSE) +
  facet_wrap(~gear) +
  labs(title = "Weight vs MPG", x = "Weight (1000 lbs)", y = "Miles per Gallon") +
  theme_minimal()
```

### Q5: Ninawezaje kuandika msimbo bora wa R kwa seti kubwa za data?
**J:** Mbinu kuu:
- Tenga vekta:`x <- numeric(n)`badala ya kukua na`c()`
- Tumia`data.table`kwa hifadhidata kubwa (mara 100 haraka kuliko data.frame)
- Vectorize shughuli - epuka vitanzi inapowezekana
- Tumia`vapply`juu ya`sapply`kwa usalama wa aina
- Profaili iliyo na`Rprof()`au`profvis`
- Zingatia kifurushi cha`arrow`kwa data isiyo ya msingi
---

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Kusafisha na Kuchanganua Seti ya Data Iliyoharibika
**Hatua ya 1: Elewa Tatizo**
Tunayo fremu ya data iliyo na thamani zinazokosekana, aina zisizolingana na viambajengo. Tunahitaji kuisafisha na kukokotoa takwimu za muhtasari.
**Hatua ya 2: Tambua Mbinu**
Tumia vitenzi vyenye mpangilio mzuri:`filter`,`mutate`,`summarize`, na`group_by`.
**Hatua ya 3: Tekeleza**```r
library(tidyverse)

# Load and inspect
df <- read_csv("data.csv")
glimpse(df)

# Clean: remove rows with all NA, fix types, filter outliers
clean_df <- df %>%
  drop_na() %>%
  mutate(
    age = as.integer(age),
    income = as.numeric(income),
    date = as.Date(date)
  ) %>%
  filter(between(age, 18, 120), income > 0)

# Summarize
summary_stats <- clean_df %>%
  group_by(region) %>%
  summarize(
    n = n(),
    mean_income = mean(income),
    median_age = median(age),
    sd_income = sd(income)
  ) %>%
  arrange(desc(mean_income))
```

**Hatua ya 4: Thibitisha**
Angalia hesabu za safu mlalo kabla/baada, thibitisha masafa na angalia jumla dhidi ya data chanzo.
### Tatizo la 2: Kuunda Muundo wa Urejeshaji wa Mstari
**Hatua ya 1: Elewa Tatizo**
Tabiri mabadiliko yanayoendelea ya matokeo kutoka kwa watabiri wengi.
**Hatua ya 2: Tambua Mbinu**
Tumia`lm()`kwa urejeshaji wa mstari, angalia dhana, na utathmini ufaafu wa modeli.
**Hatua ya 3: Tekeleza**```r
# Fit model
model <- lm(mpg ~ wt + hp + cyl, data = mtcars)
summary(model)

# Check assumptions
par(mfrow = c(2, 2))
plot(model)

# Predictions
new_data <- data.frame(wt = 3, hp = 150, cyl = 6)
predict(model, newdata = new_data, interval = "prediction")

# Compare models
model2 <- lm(mpg ~ wt * hp + cyl, data = mtcars)
AIC(model, model2)
```

**Hatua ya 4: Tathmini**
Angalia viwanja vya R-mraba, mabaki ya ruwaza, na AIC kwa ulinganisho wa kielelezo.
### Tatizo la 3: Kuunda Ripoti Inayoweza Kuzaliana
**Hatua ya 1: Elewa Tatizo**
Unda ripoti inayochanganya uchanganuzi, taswira na maandishi ya simulizi katika umbizo linaloweza kuzalishwa tena.
**Hatua ya 2: Tambua Mbinu**
Tumia R Markdown (au Quarto) ili kutenganisha vipande vya msimbo na maandishi.
**Hatua ya 3: Tekeleza**```markdown
---
title: "Analysis Report"
output: html_document
---

## Data Overview

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, onyo = FALSE)
maktaba (tidyverse)
data <- read_csv("data.csv")```

The dataset contains `r nrow(data)` observations.

## Results

```{r plot}
ggplot(data, aes(x, y)) + geom_point() + geom_smooth()```
```

**Hatua ya 4: Toa**
`rmarkdown::render("report.Rmd")`inazalisha hati ya HTML inayojitosheleza.
---

## Muhtasari
R ni lugha ya takwimu. Kwa uchanganuzi wa data, taswira, na uundaji wa takwimu, bado haulinganishwi kwa kina na mapana. Uboreshaji umefanya lugha kuwa ya kisasa, na R Markdown/Quarto hufanya utafiti unaoweza kurudiwa moja kwa moja. Wakati Python imepata msingi katika sayansi ya data kwa ujumla, R inabaki kuwa zana ya mtaalamu kwa kazi ngumu ya takwimu. Kwa mtu yeyote anayefanya utafiti wa kiasi, kujifunza R ni muhimu.
---

## Ugomvi wa data wa hali ya juu
### data.table Deep Dive
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

### Safu Nadhifu na Safu Inayobadilika
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

## Kuiga Kitakwimu Dive ya kina
### Urejeshaji wa Hali ya Juu
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

Uchambuzi wa Mfululizo wa ###
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

### Kujifunza kwa Mashine kwa kutumia miundo safi
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
