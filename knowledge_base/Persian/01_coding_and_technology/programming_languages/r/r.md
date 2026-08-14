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

# آر
R یک زبان برنامه نویسی و محیطی است که به طور خاص برای محاسبات آماری و تجزیه و تحلیل داده ها طراحی شده است. این زبان توسط راس ایهاکا و رابرت جنتلمن در دانشگاه اوکلند در سال 1993 ایجاد شد (از این رو "R")، اجرای زبان S با پسوندهای قابل توجه است. R منبع باز است و توسط تیم R Core نگهداری می شود. این ابزار استاندارد برای آماردانان، تحلیلگران داده، و محققان در دانشگاه، مراقبت های بهداشتی، مالی و دولت است.
R در دستکاری داده ها، مدل سازی آماری، تجسم و گزارش دهی برتر است. اکوسیستم بسته آن (CRAN) دارای بیش از 20000 بسته است که تقریباً هر روش آماری ابداع شده را پوشش می دهد.
---

## چرا R مهم است
- **محاسبات آماری**: جامع ترین مجموعه روش های آماری در هر زبان.
- **تجسم داده**: ggplot2 گرافیک با کیفیت انتشار تولید می کند. گرامر پارادایم گرافیک بی بدیل است.
- **تحقیق قابل تکرار**: R Markdown / Quarto به شما امکان می دهد کد، نتایج و روایت را در یک سند واحد ترکیب کنید.
- **استاندارد آکادمیک**: مورد استفاده در آمار، بیوانفورماتیک، اپیدمیولوژی، اکولوژی، اقتصاد و علوم اجتماعی.
- **Tidyverse**: مجموعه ای منسجم از بسته ها (dplyr، ggplot2، tidyr، readr) که تجزیه و تحلیل داده ها را زیبا و سازگار می کند.
- **رایگان و منبع باز **: بدون هزینه مجوز. به طور فعال توسط یک جامعه جهانی نگهداری می شود.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **عملکرد** | بصورت پیش فرض تک رشته ای. کند برای مجموعه داده های بزرگ | استفاده از `data.table`، بسته های موازی، یا Rcpp برای یکپارچه سازی C++ |
| **استفاده از حافظه** | کل مجموعه داده ها را در RAM بارگیری می کند | استفاده از `data.table::fread`، بسته فلش برای پردازش خارج از هسته |
| **زبان همه منظوره نیست** | برای توسعه وب، برنامه نویسی سیستم ها یا برنامه ها ناخوشایند | برای کارهای غیر آماری از Python، Go یا JavaScript استفاده کنید
| ** نحو ناسازگار ** | پایه R دارای ویژگی های عجیب و غریب است. بسته های مختلف از قراردادهای مختلف استفاده می کنند | از tidyverse برای قوام استفاده کنید |
| **بازار کار** | نقش های عمدتاً آکادمیک/پژوهشی | نقش های علم داده به طور فزاینده ای پایتون |
---

## اصول نحو
### عملیات اساسی
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

### Tidyverse (R مدرن)
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

### تجسم با ggplot2
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

### مدلسازی آماری
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

## نحو و الگوهای پیشرفته
### S3 و S4 Object Systems
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

### کلاس های مرجع R6
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

### ارزیابی غیر استاندارد و فرابرنامه ریزی
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

### بارگذاری بیش از حد اپراتور
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

## همزمانی و موازی
### بسته موازی
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

### بسته آینده
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

## پیکربندی پروژه و سیستم ساخت
### ساختار بسته
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

### فایل توضیحات
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

### مدیریت وابستگی با renv
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### CI/CD با GitHub Actions
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

## تست
### تست چارچوب
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

## قابلیت همکاری
### C/C++ ادغام با Rcpp
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

### فراخوانی پایتون از R
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

## الگوهای طراحی
### الگوی 1: ارزیابی مرتب برای عملکردهای انعطاف پذیر
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

### الگوی 2: برنامه نویسی کاربردی با purrr
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

### الگوی 3: خط لوله تولید گزارش
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### بردارسازی و جدول داده ها
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

### بهینه سازی حافظه
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

## استقرار
### انتشار بسته به CRAN
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### اپلیکیشن براق
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

### استقرار کانتینر
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## چه زمانی از R استفاده کنیم
| سناریو | چرا R | جایگزین بهتر |
|----------|-------|-------------------|
| تجزیه و تحلیل آماری | جامع ترین روش های آماری | پایتون (statsmodels, scipy) |
| تجسم داده ها | ggplot2 از نظر کیفیت انتشار بی نظیر است | پایتون (matplotlib، seaborn) برای تعاملی |
| تحقیقات دانشگاهی | استاندارد در بسیاری از زمینه ها | — |
| بیوانفورماتیک | Bioconductor دارای 2000+ بسته تخصصی | پایتون برای خطوط لوله تولید |
| گزارش (R Markdown/Quarto) | تحلیل تلفیقی + روایت | ژوپیتر (پایتون) |
| تولید سیستم های ML | برای استقرار طراحی نشده است | پایتون، جاوا |
| توسعه وب | مناسب نیست | جاوا اسکریپت، پایتون |
| پردازش داده در مقیاس بزرگ | محدود به حافظه | Python (PySpark)، SQL |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت`<-`و`=`برای انتساب چیست؟
**A:** هر دو مقدار را اختصاص می دهند، اما`<-`عملگر انتساب اصطلاحی R است. در همه زمینه ها از جمله فراخوانی های تابع درونی کار می کند:
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

### Q2: چگونه داده های از دست رفته در R را مدیریت کنم؟
**A:** R برای مقادیر از دست رفته از`NA`استفاده می کند. اکثر توابع دارای یک پارامتر`na.rm`هستند:
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

### Q3: چه زمانی باید از`lapply`در مقابل`sapply`در مقابل`vapply`استفاده کنم؟
**A:** همه یک تابع را روی یک لیست/بردار اعمال می کنند، اما در خروجی متفاوت هستند:
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

### Q4: چگونه با ggplot2 تجسم های موثر ایجاد کنم؟
**A:** دستور زبان گرافیک را دنبال کنید - زیبایی شناسی داده ها را به ویژگی های بصری نگاشت:
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

### Q5: چگونه کد R کارآمد را برای مجموعه داده های بزرگ بنویسم؟
**A:** شیوه های کلیدی:
- بردارها را از قبل تخصیص دهید:`x <- numeric(n)`به جای رشد با`c()`
- استفاده از`data.table`برای مجموعه داده های بزرگ (100 برابر سریعتر از data.frame)
- عملیات برداری - تا حد امکان از حلقه ها اجتناب کنید
- برای ایمنی نوع از`vapply`نسبت به`sapply`استفاده کنید
- نمایه با`Rprof()`یا`profvis`
- بسته`arrow`را برای داده های خارج از هسته در نظر بگیرید
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: تمیز کردن و تجزیه و تحلیل یک مجموعه داده کثیف
**مرحله 1: مشکل را درک کنید**
ما یک چارچوب داده با مقادیر گمشده، انواع ناسازگار، و نقاط پرت داریم. ما باید آن را تمیز کنیم و آمار خلاصه را محاسبه کنیم.
**مرحله 2: رویکرد را شناسایی کنید**
از افعال مرتب استفاده کنید: `filter`، `mutate`، `summarize`، و `group_by`.
**مرحله 3: پیاده سازی **```r
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

**مرحله 4: تایید **
تعداد سطرها را قبل و بعد از آن بررسی کنید، محدوده ها را اعتبارسنجی کنید و مجموع ها را با داده های منبع بررسی کنید.
### مسئله 2: ساخت یک مدل رگرسیون خطی
**مرحله 1: مشکل را درک کنید**
یک متغیر نتیجه پیوسته را از پیش بینی کننده های متعدد پیش بینی کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از`lm()`برای رگرسیون خطی، بررسی مفروضات و ارزیابی تناسب مدل استفاده کنید.
**مرحله 3: پیاده سازی **```r
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

**مرحله 4: ارزیابی**
مربع R، نمودارهای باقیمانده برای الگوها و AIC را برای مقایسه مدل بررسی کنید.
### مشکل 3: ایجاد یک گزارش قابل تکرار
**مرحله 1: مشکل را درک کنید**
گزارشی ایجاد کنید که تجزیه و تحلیل، تجسم ها و متن روایی را در قالبی تکرارپذیر ترکیب کند.
**مرحله 2: رویکرد را شناسایی کنید**
از R Markdown (یا Quarto) برای در هم آمیختن تکه های کد با متن استفاده کنید.
**مرحله 3: پیاده سازی **```markdown
---
title: "Analysis Report"
output: html_document
---

## Data Overview

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE، هشدار = FALSE)
کتابخانه (Tidyverse)
داده <- read_csv("data.csv")```

The dataset contains `r nrow(data)` observations.

## Results

```{r plot}
ggplot(داده، aes(x، y)) + geom_point() + geom_smooth()```
```

**مرحله 4: رندر**
`rmarkdown::render("report.Rmd")`یک سند HTML مستقل تولید می کند.
---

## خلاصه
R زبان آمار است. برای تجزیه و تحلیل داده ها، تجسم، و مدل سازی آماری، از نظر عمق و وسعت بی بدیل باقی می ماند. نظم و ترتیب زبان را مدرن کرده است و R Markdown/Quarto تحقیقات قابل تکرار را ساده کرده است. در حالی که پایتون به طور کلی در علم داده به دست آورده است، R همچنان ابزار متخصص برای کارهای آماری دقیق است. برای هر کسی که تحقیقات کمی انجام می دهد، یادگیری R ضروری است.
---

## کشمکش داده های پیشرفته
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

### ستون های مرتب و مرتب و پویا
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

## مدلسازی آماری Deep Dive
### رگرسیون پیشرفته
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

### تجزیه و تحلیل سری زمانی
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

### یادگیری ماشینی با مدل های tidymodels
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
