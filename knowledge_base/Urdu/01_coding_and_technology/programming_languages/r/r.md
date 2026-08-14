<!--
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

-->
#ر
R ایک پروگرامنگ زبان اور ماحول ہے جو خاص طور پر شماریاتی کمپیوٹنگ اور ڈیٹا کے تجزیہ کے لیے ڈیزائن کیا گیا ہے۔ 1993 میں آکلینڈ یونیورسٹی میں راس ایہاکا اور رابرٹ جنٹلمین کے ذریعہ تخلیق کیا گیا (اس وجہ سے "R")، یہ اہم توسیعات کے ساتھ ایس زبان کا نفاذ ہے۔ R اوپن سورس ہے اور اسے R کور ٹیم کے ذریعے برقرار رکھا جاتا ہے۔ یہ ماہرینِ شماریات، ڈیٹا تجزیہ کاروں، اور اکیڈمیا، ہیلتھ کیئر، فنانس اور حکومت کے محققین کے لیے معیاری ٹول ہے۔
آر ڈیٹا ہیرا پھیری، شماریاتی ماڈلنگ، ویژولائزیشن اور رپورٹنگ میں مہارت رکھتا ہے۔ اس کے پیکج ایکو سسٹم (CRAN) میں 20,000 سے زیادہ پیکجز ہیں جن میں عملی طور پر ہر شماریاتی طریقہ وضع کیا گیا ہے۔
---

## R کیوں اہمیت رکھتا ہے۔
- **شماریاتی کمپیوٹنگ**: کسی بھی زبان میں شماریاتی طریقوں کا سب سے زیادہ جامع مجموعہ۔
- **ڈیٹا ویژولائزیشن**: ggplot2 اشاعت کے معیار کے گرافکس تیار کرتا ہے۔ گرافکس پیراڈائم کی گرامر بے مثال ہے۔
- **ری پروڈیکیبل ریسرچ**: R Markdown/Quarto آپ کو کوڈ، نتائج اور بیانیہ کو ایک دستاویز میں یکجا کرنے دیتا ہے۔
- **تعلیمی معیار**: شماریات، بایو انفارمیٹکس، وبائی امراض، ماحولیات، معاشیات، اور سماجی علوم میں استعمال کیا جاتا ہے۔
- **Tidyverse**: پیکجوں کا ایک مربوط سیٹ (dplyr, ggplot2, tidyr, readr) جو ڈیٹا کے تجزیہ کو خوبصورت اور مستقل بناتا ہے۔
- **مفت اور اوپن سورس**: لائسنس کی کوئی قیمت نہیں؛ ایک عالمی برادری کے ذریعہ فعال طور پر برقرار رکھا گیا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کارکردگی** | پہلے سے طے شدہ سنگل تھریڈڈ؛ بڑے ڈیٹا سیٹس کے لیے سست | C++ انضمام کے لیے `data.table`، متوازی پیکجز، یا Rcpp استعمال کریں |
| **میموری کا استعمال** | پورے ڈیٹا سیٹس کو RAM میں لوڈ کرتا ہے۔`data.table::fread`استعمال کریں، آؤٹ آف کور پروسیسنگ کے لیے تیر کا پیکج |
| **عام مقصد کی زبان نہیں** | ویب ڈویلپمنٹ، سسٹم پروگرامنگ، یا ایپس کے لیے عجیب | غیر شماریاتی کاموں کے لیے Python، Go، یا JavaScript استعمال کریں۔
| **متضاد نحو** | بیس R میں نرالا ہے؛ مختلف پیکیجز مختلف کنونشنز کا استعمال کرتے ہیں۔ مستقل مزاجی کے لیے tidyverse استعمال کریں۔
| **ملازمت کی منڈی** | زیادہ تر علمی/ تحقیقی کردار | ڈیٹا سائنس کے کردار تیزی سے ازگر کو ترجیح دیتے ہیں۔
---

## نحوی بنیادی باتیں
### بنیادی آپریشنز
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

### صاف ستھرا (جدید R)
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

### ggplot2 کے ساتھ تصور
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

### شماریاتی ماڈلنگ
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

## اعلی درجے کی نحو اور نمونے۔
### S3 اور S4 آبجیکٹ سسٹمز
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

### R6 ریفرنس کلاسز
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

### غیر معیاری تشخیص اور میٹا پروگرامنگ
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

### آپریٹر اوورلوڈنگ
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

## ہم آہنگی اور ہم آہنگی
### متوازی پیکیج
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

### مستقبل کا پیکیج
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

### foreach/do Parallel
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پیکیج کا ڈھانچہ
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

### DESCRIPTION فائل
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

### renv کے ساتھ انحصار کا انتظام
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### CI/CD GitHub ایکشن کے ساتھ
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

## ٹیسٹنگ
### ٹیسٹ کہ فریم ورک
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

## انٹرآپریبلٹی
### Rcpp کے ساتھ C/C++ انٹیگریشن
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

### R سے ازگر کو کال کرنا
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

## ڈیزائن پیٹرن
### پیٹرن 1: لچکدار افعال کے لیے صاف ستھری تشخیص
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

### پیٹرن 2: purrr کے ساتھ فنکشنل پروگرامنگ
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

### پیٹرن 3: رپورٹ جنریشن پائپ لائن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

### ویکٹرائزیشن اور ڈیٹا ٹیبل
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

### میموری آپٹیمائزیشن
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

## تعیناتی۔
### CRAN پر پیکیج کی اشاعت
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### چمکدار ایپلی کیشن
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

### کنٹینر کی تعیناتی۔
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## R کب استعمال کریں۔
| منظر نامہ | کیوں آر | بہتر متبادل |
|------------|---------|-------------------|
| شماریاتی تجزیہ | سب سے زیادہ جامع شماریاتی طریقے | Python (statsmodels, scipy) |
| ڈیٹا ویژولائزیشن | ggplot2 اشاعت کے معیار کے لیے بے مثال ہے | انٹرایکٹو کے لیے ازگر (matplotlib، seaborn) |
| علمی تحقیق | بہت سے شعبوں میں معیاری | - |
| بایو انفارمیٹکس | بایو کنڈکٹر کے پاس 2,000+ خصوصی پیکجز ہیں۔ پروڈکشن پائپ لائنز کے لیے ازگر |
| رپورٹنگ (R Markdown/Quarto) | مربوط تجزیہ + بیانیہ | Jupyter (Python) |
| پیداوار ایم ایل سسٹمز | تعیناتی کے لیے ڈیزائن نہیں کیا گیا | ازگر، جاوا |
| ویب ڈویلپمنٹ | مناسب نہیں | جاوا اسکرپٹ، ازگر |
| بڑے پیمانے پر ڈیٹا پروسیسنگ | یادداشت سے منسلک | Python (PySpark)، SQL |
---

## مصنوعی سوال و جواب
### Q1: اسائنمنٹ کے لیے`<-`اور`=`میں کیا فرق ہے؟
**A:** دونوں قدریں تفویض کرتے ہیں، لیکن`<-`محاورہ R اسائنمنٹ آپریٹر ہے۔ یہ تمام سیاق و سباق میں کام کرتا ہے، بشمول اندرونی فنکشن کالز:
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

### Q2: میں R میں گمشدہ ڈیٹا کو کیسے ہینڈل کروں؟
**A:** R غائب اقدار کے لیے`NA`استعمال کرتا ہے۔ زیادہ تر فنکشنز میں`na.rm`پیرامیٹر ہوتا ہے:
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

### Q3: مجھے`lapply`بمقابلہ`sapply`بمقابلہ`vapply`کب استعمال کرنا چاہیے؟
**A:** سبھی فہرست/ویکٹر پر فنکشن کا اطلاق کرتے ہیں، لیکن آؤٹ پٹ میں مختلف ہوتے ہیں:
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

### Q4: میں ggplot2 کے ساتھ مؤثر تصورات کیسے بنا سکتا ہوں؟
**A:** گرافکس کے گرائمر پر عمل کریں — نقشہ ڈیٹا جمالیات کو بصری خصوصیات میں:
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

### Q5: میں بڑے ڈیٹا سیٹس کے لیے موثر R کوڈ کیسے لکھ سکتا ہوں؟
**A:** کلیدی مشقیں:
- پہلے سے مختص ویکٹرز:`c()`کے ساتھ بڑھنے کے بجائے`x <- numeric(n)`
- بڑے ڈیٹا سیٹس کے لیے`data.table`استعمال کریں (data.frame سے 100x تیز)
- ویکٹرائز آپریشنز - جہاں ممکن ہو لوپس سے گریز کریں۔
- قسم کی حفاظت کے لیے`sapply`پر`vapply`استعمال کریں۔
-`Rprof()`یا`profvis`کے ساتھ پروفائل 
- آؤٹ آف کور ڈیٹا کے لیے`arrow`پیکیج پر غور کریں۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: گندے ڈیٹا سیٹ کو صاف کرنا اور تجزیہ کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
ہمارے پاس لاپتہ اقدار، متضاد قسموں اور آؤٹ لیرز کے ساتھ ڈیٹا فریم ہے۔ ہمیں اسے صاف کرنے اور خلاصہ کے اعدادوشمار کی گنتی کرنے کی ضرورت ہے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
متضاد فعل استعمال کریں: `filter`، `mutate`، `summarize`، اور`group_by`۔
**مرحلہ 3: نافذ کریں**```r
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

**مرحلہ 4: تصدیق کریں**
پہلے/بعد میں قطار کی گنتی چیک کریں، رینجز کی توثیق کریں، اور سورس ڈیٹا کے خلاف ٹوٹل کراس چیک کریں۔
### مسئلہ 2: لکیری ریگریشن ماڈل بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
متعدد پیش گوئوں سے مسلسل نتائج کے متغیر کی پیش گوئی کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
لکیری رجعت کے لیے`lm()`استعمال کریں، مفروضوں کی جانچ کریں، اور ماڈل فٹ کا اندازہ کریں۔
**مرحلہ 3: نافذ کریں**```r
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

**مرحلہ 4: اندازہ کریں**
نمونوں کے لیے R-squared، بقایا پلاٹ اور ماڈل کے مقابلے کے لیے AIC چیک کریں۔
### مسئلہ 3: دوبارہ پیش کرنے کے قابل رپورٹ بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ایک رپورٹ بنائیں جو تجزیے، تصورات، اور بیانیہ متن کو دوبارہ پیش کرنے کے قابل فارمیٹ میں یکجا کرے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
متن کے ساتھ کوڈ کے ٹکڑوں کو جوڑنے کے لیے R Markdown (یا Quarto) کا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```markdown
---
title: "Analysis Report"
output: html_document
---

## Data Overview

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE، وارننگ = FALSE)
لائبریری (صاف ستھری)
ڈیٹا <- read_csv("data.csv")```

The dataset contains `r nrow(data)` observations.

## Results

```{r plot}
ggplot(data, aes(x, y)) + geom_point() + geom_smooth()```
```

**مرحلہ 4: رینڈر**
`rmarkdown::render("report.Rmd")`ایک خود ساختہ HTML دستاویز تیار کرتا ہے۔
---

## خلاصہ
R اعداد و شمار کی زبان ہے۔ اعداد و شمار کے تجزیہ، تصور، اور شماریاتی ماڈلنگ کے لیے، یہ گہرائی اور وسعت میں بے مثال ہے۔ tidyverse نے زبان کو جدید بنایا ہے، اور R Markdown/Quarto نے تولیدی تحقیق کو سیدھا بنایا ہے۔ اگرچہ Python نے عام طور پر ڈیٹا سائنس میں کامیابی حاصل کی ہے، R سخت شماریاتی کام کے لیے ماہر کا آلہ بنا ہوا ہے۔ مقداری تحقیق کرنے والے ہر فرد کے لیے، R سیکھنا ضروری ہے۔
---

## ایڈوانسڈ ڈیٹا رینگلنگ
### ڈیٹا ٹیبل ڈیپ ڈائیو
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

### صاف ستھرا اور متحرک کالم
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

## شماریاتی ماڈلنگ ڈیپ ڈائیو
### اعلی درجے کی رجعت
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

### ٹائم سیریز کا تجزیہ
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

### ٹیڈی ماڈلز کے ساتھ مشین لرننگ
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
