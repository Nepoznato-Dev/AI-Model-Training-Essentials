---
# Metadata
title: "R"
description: "Comprehensive reference for the R programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# আর
R হল একটি প্রোগ্রামিং ভাষা এবং পরিবেশ যা পরিসংখ্যানগত কম্পিউটিং এবং ডেটা বিশ্লেষণের জন্য বিশেষভাবে ডিজাইন করা হয়েছে। 1993 সালে অকল্যান্ড বিশ্ববিদ্যালয়ে রস ইহাকা এবং রবার্ট জেন্টলম্যান দ্বারা তৈরি করা হয়েছে (অতএব "R"), এটি উল্লেখযোগ্য এক্সটেনশন সহ এস ভাষার একটি বাস্তবায়ন। R হল ওপেন সোর্স এবং R কোর টিম দ্বারা রক্ষণাবেক্ষণ করা হয়। এটি পরিসংখ্যানবিদ, ডেটা বিশ্লেষক এবং একাডেমিয়া, স্বাস্থ্যসেবা, অর্থ এবং সরকারের গবেষকদের জন্য আদর্শ হাতিয়ার।
R ডেটা ম্যানিপুলেশন, পরিসংখ্যানগত মডেলিং, ভিজ্যুয়ালাইজেশন এবং রিপোর্টিং-এ পারদর্শী। এর প্যাকেজ ইকোসিস্টেম (CRAN) এর 20,000 টিরও বেশি প্যাকেজ রয়েছে যা এখন পর্যন্ত তৈরি করা প্রতিটি পরিসংখ্যান পদ্ধতিকে কভার করে।
---

## কেন আর গুরুত্বপূর্ণ
- **পরিসংখ্যানগত কম্পিউটিং**: যেকোনো ভাষায় পরিসংখ্যানগত পদ্ধতির সবচেয়ে ব্যাপক সংগ্রহ।
- **ডেটা ভিজ্যুয়ালাইজেশন**: ggplot2 প্রকাশনা-মানের গ্রাফিক্স তৈরি করে। গ্রাফিক্স প্যারাডাইমের ব্যাকরণ অতুলনীয়।
- **পুনরুত্পাদনযোগ্য গবেষণা**: আর মার্কডাউন / কোয়ার্টো আপনাকে একটি নথিতে কোড, ফলাফল এবং বিবরণ একত্রিত করতে দেয়।
- **একাডেমিক স্ট্যান্ডার্ড**: পরিসংখ্যান, বায়োইনফরমেটিক্স, এপিডেমিওলজি, বাস্তুশাস্ত্র, অর্থনীতি এবং সামাজিক বিজ্ঞানে ব্যবহৃত হয়।
- **Tidyverse**: প্যাকেজগুলির একটি সমন্বিত সেট (dplyr, ggplot2, tidyr, readr) যা ডেটা বিশ্লেষণকে মার্জিত এবং সামঞ্জস্যপূর্ণ করে তোলে।
- **ফ্রি এবং ওপেন সোর্স**: লাইসেন্সিং খরচ নেই; সক্রিয়ভাবে একটি বিশ্ব সম্প্রদায় দ্বারা রক্ষণাবেক্ষণ করা হয়.
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **পারফরম্যান্স** | ডিফল্টরূপে একক-থ্রেডেড; বড় ডেটাসেটের জন্য ধীর | C++ ইন্টিগ্রেশনের জন্য`data.table`, সমান্তরাল প্যাকেজ বা Rcpp ব্যবহার করুন |
| **মেমরি ব্যবহার** | RAM এ সমগ্র ডেটাসেট লোড করে |`data.table::fread`ব্যবহার করুন, আউট-অফ-কোর প্রক্রিয়াকরণের জন্য তীর প্যাকেজ |
| **একটি সাধারণ-উদ্দেশ্যের ভাষা নয়** | ওয়েব ডেভেলপমেন্ট, সিস্টেম প্রোগ্রামিং বা অ্যাপের জন্য বিশ্রী | অ-পরিসংখ্যানগত কাজের জন্য পাইথন, গো, বা জাভাস্ক্রিপ্ট ব্যবহার করুন |
| **অসংলগ্ন বাক্য গঠন** | বেস R এর quirks আছে; বিভিন্ন প্যাকেজ বিভিন্ন নিয়ম ব্যবহার করে | ধারাবাহিকতার জন্য পরিপাটি ব্যবহার করুন |
| **চাকরীর বাজার** | বেশিরভাগই একাডেমিক/গবেষণার ভূমিকা | ডেটা বিজ্ঞানের ভূমিকা ক্রমশ পাইথনকে পছন্দ করে |
---

## সিনট্যাক্স মৌলিক
### বেসিক অপারেশন
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

### পরিপাটি (আধুনিক আর)
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

### ggplot2 সহ ভিজ্যুয়ালাইজেশন
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

### পরিসংখ্যান মডেলিং
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### S3 এবং S4 অবজেক্ট সিস্টেম
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

### R6 রেফারেন্স ক্লাস
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

### নন-স্ট্যান্ডার্ড ইভালুয়েশন এবং মেটাপ্রোগ্রামিং
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

### অপারেটর ওভারলোডিং
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

## সামঞ্জস্য এবং সমান্তরালতা
### সমান্তরাল প্যাকেজ
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

### ভবিষ্যতের প্যাকেজ
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্যাকেজ স্ট্রাকচার
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

### বর্ণনা ফাইল
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

### renv সহ নির্ভরশীলতা ব্যবস্থাপনা
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### গিটহাব অ্যাকশন সহ CI/CD
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

## পরীক্ষা
### যে ফ্রেমওয়ার্ক পরীক্ষা করুন
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

## ইন্টারঅপারেবিলিটি
### Rcpp-এর সাথে C/C++ ইন্টিগ্রেশন
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

### R থেকে পাইথন কল করা হচ্ছে
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: নমনীয় ফাংশনের জন্য পরিপাটি মূল্যায়ন
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

### প্যাটার্ন 2: purrr সহ কার্যকরী প্রোগ্রামিং
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

### প্যাটার্ন 3: রিপোর্ট জেনারেশন পাইপলাইন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### ভেক্টরাইজেশন এবং ডেটা টেবিল
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

### মেমরি অপ্টিমাইজেশান
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

## স্থাপনা
### CRAN-এ প্যাকেজ প্রকাশ করা হচ্ছে
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### চকচকে অ্যাপ্লিকেশন
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

### কন্টেইনার স্থাপনা
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## কখন আর ব্যবহার করবেন
| দৃশ্যকল্প | কেন আর | ভাল বিকল্প |
|------------|---------|-------------------|
| পরিসংখ্যানগত বিশ্লেষণ | সর্বাধিক ব্যাপক পরিসংখ্যান পদ্ধতি | Python (statsmodels, scipy) |
| ডেটা ভিজ্যুয়ালাইজেশন | ggplot2 প্রকাশনার মানের জন্য অতুলনীয় | ইন্টারেক্টিভের জন্য পাইথন (matplotlib, seaborn) |
| একাডেমিক গবেষণা | অনেক ক্ষেত্রে স্ট্যান্ডার্ড | — |
| বায়োইনফরমেটিক্স | বায়োকন্ডাক্টরের 2,000+ বিশেষ প্যাকেজ আছে | উত্পাদন পাইপলাইনের জন্য পাইথন |
| রিপোর্টিং (আর মার্কডাউন/কোয়ার্টো) | সমন্বিত বিশ্লেষণ + আখ্যান | জুপিটার (পাইথন) |
| উৎপাদন ML সিস্টেম | স্থাপনার জন্য ডিজাইন করা হয়নি | পাইথন, জাভা |
| ওয়েব ডেভেলপমেন্ট | উপযুক্ত নয় | জাভাস্ক্রিপ্ট, পাইথন |
| বড় আকারের ডেটা প্রসেসিং | স্মৃতি আবদ্ধ | পাইথন (PySpark), SQL |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: অ্যাসাইনমেন্টের জন্য`<-`এবং`=`এর মধ্যে পার্থক্য কী?
**A:** উভয়ই মান নির্ধারণ করে, কিন্তু`<-`হল ইডিওম্যাটিক R অ্যাসাইনমেন্ট অপারেটর। এটি ভিতরের ফাংশন কল সহ সমস্ত প্রসঙ্গে কাজ করে:
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

### প্রশ্ন 2: আমি কীভাবে R-এ হারিয়ে যাওয়া ডেটা পরিচালনা করব?
**A:** R অনুপস্থিত মানগুলির জন্য`NA`ব্যবহার করে। বেশিরভাগ ফাংশনের একটি`na.rm`প্যারামিটার থাকে:
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

### প্রশ্ন 3: কখন আমি`lapply`বনাম`sapply`বনাম`vapply`ব্যবহার করব?
**A:** সবাই একটি তালিকা/ভেক্টরের উপর একটি ফাংশন প্রয়োগ করে, কিন্তু আউটপুটে ভিন্ন:
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

### প্রশ্ন 4: আমি কিভাবে ggplot2 দিয়ে কার্যকর ভিজ্যুয়ালাইজেশন তৈরি করব?
**A:** গ্রাফিক্সের ব্যাকরণ অনুসরণ করুন — ভিজ্যুয়াল বৈশিষ্ট্যের সাথে মানচিত্র ডেটা নন্দনতত্ত্ব:
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

### প্রশ্ন 5: বড় ডেটাসেটের জন্য আমি কীভাবে দক্ষ R কোড লিখব?
**A:** মূল অনুশীলন:
- প্রি-অ্যালোকেট ভেক্টর:`c()`এর সাথে বৃদ্ধি না করে`x <- numeric(n)`
- বড় ডেটাসেটের জন্য`data.table`ব্যবহার করুন (data.frame থেকে 100x দ্রুত)
- ভেক্টরাইজ অপারেশন - যেখানে সম্ভব লুপ এড়িয়ে চলুন
- প্রকার নিরাপত্তার জন্য`sapply`এর উপর`vapply`ব্যবহার করুন
-`Rprof()`বা`profvis`সহ প্রোফাইল৷ 
- আউট-অফ-কোর ডেটার জন্য`arrow`প্যাকেজ বিবেচনা করুন৷
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি অগোছালো ডেটাসেট পরিষ্কার করা এবং বিশ্লেষণ করা
**ধাপ 1: সমস্যাটি বুঝুন**
আমাদের কাছে অনুপস্থিত মান, অসামঞ্জস্যপূর্ণ প্রকার এবং আউটলায়ার সহ একটি ডেটা ফ্রেম রয়েছে। আমাদের এটি পরিষ্কার করতে হবে এবং সংক্ষিপ্ত পরিসংখ্যান গণনা করতে হবে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
পরিপাটি ক্রিয়া ব্যবহার করুন:`filter`,`mutate`,`summarize`, এবং `group_by`৷
**ধাপ 3: প্রয়োগ করুন**```r
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

**পদক্ষেপ 4: যাচাই করুন**
আগে/পরে সারি গণনা পরীক্ষা করুন, ব্যাপ্তি যাচাই করুন এবং উৎস ডেটার বিপরীতে মোট ক্রস-চেক করুন।
### সমস্যা 2: একটি লিনিয়ার রিগ্রেশন মডেল তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একাধিক ভবিষ্যদ্বাণীকারী থেকে একটি ক্রমাগত ফলাফল পরিবর্তনশীল ভবিষ্যদ্বাণী করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
লিনিয়ার রিগ্রেশনের জন্য`lm()`ব্যবহার করুন, অনুমান চেক করুন এবং মডেল ফিট মূল্যায়ন করুন।
**ধাপ 3: প্রয়োগ করুন**```r
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

**ধাপ ৪: মূল্যায়ন**
মডেলের তুলনার জন্য R-স্কোয়ার, প্যাটার্নের জন্য অবশিষ্ট প্লট এবং AIC পরীক্ষা করুন।
### সমস্যা 3: একটি পুনরুত্পাদনযোগ্য প্রতিবেদন তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি পুনরুত্পাদনযোগ্য বিন্যাসে বিশ্লেষণ, ভিজ্যুয়ালাইজেশন এবং বর্ণনামূলক পাঠ্যকে একত্রিত করে এমন একটি প্রতিবেদন তৈরি করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
পাঠ্যের সাথে কোডের অংশগুলিকে আন্তঃলিভ করতে R Markdown (বা Quarto) ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```markdown
---
title: "Analysis Report"
output: html_document
---

## Data Overview

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, warning = FALSE)
লাইব্রেরি (পরিপাটি)
ডেটা <- read_csv("data.csv")```

The dataset contains `r nrow(data)` observations.

## Results

```{r plot}
ggplot(ডেটা, aes(x, y)) + geom_point() + geom_smooth()```
```

**ধাপ ৪: রেন্ডার**
`rmarkdown::render("report.Rmd")`একটি স্বয়ংসম্পূর্ণ HTML নথি তৈরি করে।
---

## সারাংশ
R হল পরিসংখ্যানের ভাষা। ডেটা বিশ্লেষণ, ভিজ্যুয়ালাইজেশন এবং পরিসংখ্যানগত মডেলিংয়ের জন্য, এটি গভীরতা এবং প্রস্থে অতুলনীয়। টাইডাইভার্স ভাষাকে আধুনিক করেছে এবং আর মার্কডাউন/কোয়ার্টো প্রজননযোগ্য গবেষণাকে সোজা করে তুলেছে। যদিও পাইথন সাধারণত ডেটা সায়েন্সে জায়গা করে নিয়েছে, R কঠোর পরিসংখ্যানগত কাজের জন্য বিশেষজ্ঞের হাতিয়ার রয়ে গেছে। যে কেউ পরিমাণগত গবেষণা করছেন তাদের জন্য, R শেখা অপরিহার্য।
---

## অ্যাডভান্সড ডেটা র‍্যাংলিং
### ডেটা.টেবিল ডিপ ডাইভ
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

### পরিপাটি eval এবং গতিশীল কলাম
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

## পরিসংখ্যানগত মডেলিং গভীর ডুব
### উন্নত রিগ্রেশন
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

### সময় সিরিজ বিশ্লেষণ
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

### পরিপাটি মডেলের সাথে মেশিন লার্নিং
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
