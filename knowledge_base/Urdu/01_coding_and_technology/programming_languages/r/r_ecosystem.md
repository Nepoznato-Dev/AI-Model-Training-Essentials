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
# R — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ R ماحولیاتی نظام میں ضروری ٹولز، پیکجز اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## R عمل درآمد
| نفاذ | نوٹس |
|---------------|---------|
| **R (GNU R)** | معیاری، سب سے زیادہ استعمال کیا جاتا ہے |
| **آر اسٹوڈیو** | انٹیگریٹڈ R کے ساتھ IDE |
| **پوزیٹرون** | Next-gen IDE (Posit) |
| **مائیکروسافٹ آر اوپن** | آپٹمائزڈ (محفوظ شدہ) |
| **pqR** | متوازی R |
| **رینجن** | JVM پر مبنی R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **install.packages()** | CRAN پیکجز |
| **CRAN** | جامع آر آرکائیو نیٹ ورک (19,000+ پیکجز) |
| **بائیو کنڈکٹر** | جینومکس/بیولوجی پیکجز |
| **ریموٹ** | GitHub سے انسٹال کریں |
| **پاک** | جدید پیکیج انسٹالر |
| **renv** | پروجیکٹ-مقامی ماحول |
| **پیکریٹ** | انحصار کا انتظام (وراثت) |
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

## Tidyverse
| پیکیج | مقصد |
|---------|---------|
| **dplyr** | ڈیٹا ہیرا پھیری |
| **تنظیم** | ڈیٹا کو صاف کرنا |
| **ggplot2** | ڈیٹا ویژولائزیشن |
| **قارئین** | تیز رفتار CSV/فائل پڑھنا |
| **purrr** | فنکشنل پروگرامنگ |
| **ٹبل** | جدید ڈیٹا فریم |
| **سٹرنگر** | سٹرنگ ہیرا پھیری |
| **فورکیٹس** | فیکٹر ہینڈلنگ |
| **چکنا** | تاریخ/وقت ہینڈلنگ |
| **magrittr** | پائپ آپریٹر (%>%) |
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

## ڈیٹا سائنس اور شماریات
| پیکیج | مقصد |
|---------|---------|
| **ٹیڈی ماڈل** | ماڈلنگ فریم ورک (کیریٹ کی جگہ لے لیتا ہے) |
| **کیریٹ** | مشین لرننگ (وراثت) |
| **رینڈم فاریسٹ** | بے ترتیب جنگلات |
| **xgboost** | گریڈینٹ بڑھانا |
| **glmnet** | باقاعدہ رجعت |
| **بقا** | بقا کا تجزیہ |
| **lme4** | مخلوط اثرات کے ماڈل |
| **brms** | بایسیئن رجعت (اسٹین) |
| **رستان** | اسٹین انٹرفیس |
| **پیش گوئی** | ٹائم سیریز کی پیشن گوئی |
| **سببل** | ٹائم سیریز ڈیٹا |
| **افسانہ** | ٹائم سیریز کے ماڈل |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **DBI** | ڈیٹا بیس انٹرفیس معیاری |
| **dbplyr** | ڈیٹا بیس کے لیے dplyr پسدید |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC کنکشنز |
| **بڑا سوال** | Google BigQuery |
| **sparklyr** | اپاچی اسپارک |
| **تیر** | اپاچی ایرو / پارکیٹ |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **ٹیسٹ کہ** | یونٹ ٹیسٹنگ (سب سے زیادہ مقبول) |
| **چھوٹا ترین** | ہلکا پھلکا ٹیسٹنگ |
| **لنٹر** | کوڈ linting |
| **covr** | کوڈ کوریج |
| **مذاق** | طنز |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **لنٹر** | کوڈ linting |
| **سٹائلر** | کوڈ فارمیٹنگ |
| **اچھی مشق** | پیکیج کے معیار کی جانچ پڑتال |
| **covr** | کوڈ کوریج |
| **سائیکلوکمپ** | سائکلومیٹک پیچیدگی |
| **pkgdown** | پیکیج دستاویزات کی ویب سائٹ |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## تولیدی تحقیق
| ٹول | مقصد |
|------|---------|
| **R مارک ڈاؤن** | تولیدی رپورٹس |
| **کوارٹو** | اگلی نسل کی اشاعت |
| **نیٹر** | متحرک رپورٹ جنریشن |
| **اہداف** | پائپ لائن مینجمنٹ |
| **ڈریک** | بنانے والی پائپ لائنز (وراثت) |
| **بک ڈاؤن** | آر مارک ڈاؤن کی کتابیں |
| **بلاگ ڈاؤن** | آر مارک ڈاؤن کے بلاگز |
| ** کشید** | سائنسی مضامین |
| **چمکدار** | انٹرایکٹو ویب ایپس |
| **فلیکس ڈیش بورڈ** | ڈیش بورڈز |
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

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **ڈیٹا ٹیبل** | تیز رفتار ڈیٹا ہیرا پھیری |
| **R6** | حوالہ کلاسز (OOP) |
| **rlang** | R پروگرامنگ ٹولز |
| **vctrs** | ویکٹر کلاسز |
| **گلو** | سٹرنگ انٹرپولیشن |
| **cli** | کمانڈ لائن انٹرفیس |
| **کے ساتھ** | عارضی حالت |
| **fs** | فائل سسٹم آپریشنز |
| **httr2** | HTTP کلائنٹ |
| **jsonlite** | JSON پارسنگ |
| **xml2** | XML/HTML پارسنگ |
| **rvest** | ویب سکریپنگ |
| **متوازی** | بلٹ میں متوازی |
| **مستقبل** | متحد متوازی |
| **فرار** | purrr + مستقبل |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **آر اسٹوڈیو** | معیاری R IDE |
| **پوزیٹرون** | Next-gen IDE (Posit) |
| **VS کوڈ + R توسیع** | ہلکا پھلکا، R LSP |
| **Neovim + nvim-r** | ٹرمینل پر مبنی |
| ** مشتری + IRkernel** | نوٹ بک انٹرفیس |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **چمکدار سرور** | چمکدار ایپس کی میزبانی کریں |
| **پوزٹ کنیکٹ** | انٹرپرائز R تعیناتی |
| **پلمبر** | R سے REST API |
| **ڈوکر** | کنٹینرائزڈ (راکر امیجز) |
| **Quarto + Netlify** | جامد سائٹس |
| **AWS Lambda** | سرور لیس R |
| **اہداف** | پائپ لائن آرکیسٹریشن |
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

## خلاصہ
R کا ماحولیاتی نظام شماریاتی کمپیوٹنگ اور ڈیٹا سائنس کے لیے سونے کا معیار ہے۔ معیاری اسٹیک یہ ہے: **R 4.3+** رن ٹائم کے طور پر، **RStudio** بطور IDE، **ٹیڈیورس** ڈیٹا کی ہیرا پھیری اور ویژولائزیشن کے لیے، **ٹائیڈ ماڈل** مشین لرننگ کے لیے، **ggplot2** پلاٹ کرنے کے لیے، **ٹیسٹتھٹ** ٹیسٹنگ کے لیے، **lintr** linting کے لیے، اور **Reportable Quarto** کے لیے۔ آر اعداد و شمار، ڈیٹا ویژولائزیشن، بایو انفارمیٹکس (بائیو کنڈکٹر) اور تولیدی تحقیق میں مہارت رکھتا ہے۔ CRAN ایکو سسٹم میں 19,000+ پیکجز ہیں۔ پروڈکشن کی تعیناتی کے لیے، **پلمبر** R اسکرپٹ کو APIs میں بدل دیتا ہے، اور **Shiny** انٹرایکٹو ویب ایپلیکیشنز تخلیق کرتا ہے۔