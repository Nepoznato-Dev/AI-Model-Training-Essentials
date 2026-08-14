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

# R - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، بسته‌ها و زیرساخت‌های ضروری در اکوسیستم R را پوشش می‌دهد.
---

## پیاده سازی R
| پیاده سازی | یادداشت ها |
|---------------|-------|
| **R (GNU R)** | استاندارد، پرکاربردترین |
| **RStudio** | IDE با R یکپارچه |
| **پوزیترون** | نسل بعدی IDE (موقعیت) |
| **Microsoft R Open** | بهینه شده (بایگانی شده) |
| **pqR** | R موازی |
| **رجین** | R مبتنی بر JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **install.packages()** | بسته های کران |
| **کرن** | شبکه آرشیو جامع R (19000+ بسته) |
| **بیو رسانا** | بسته های ژنومیک/زیست شناسی |
| **ریموت** | نصب از GitHub |
| **پک** | نصب کننده پکیج مدرن |
| **رنو** | محیط های پروژه-محلی |
| **پاکرات** | مدیریت وابستگی (میراث) |
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

## The Tidyverse
| پکیج | هدف |
|---------|---------|
| **dplyr** | دستکاری داده ها |
| **تیدیر** | مرتب سازی داده ها |
| **ggplot2** | تجسم داده ها |
| **خواندن** | خواندن سریع CSV/فایل |
| **خخخ** | برنامه نویسی کاربردی |
| ** تیبل ** | فریم های داده مدرن |
| **stringr** | دستکاری رشته |
| **فورکات** | مدیریت عامل |
| **روغن کاری** | رسیدگی به تاریخ/زمان |
| **ماگریتر** | اپراتور لوله (%>%) |
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

## علم داده و آمار
| پکیج | هدف |
|---------|---------|
| **tidymodels** | چارچوب مدلسازی (جایگزین کارت) |
| **کارت** | یادگیری ماشینی (میراث) |
| **جنگل تصادفی** | جنگل های تصادفی |
| **xgboost** | افزایش گرادیان |
| **glmnet** | رگرسیون منظم |
| **بقا** | تجزیه و تحلیل بقا |
| **lme4** | مدل های با جلوه های ترکیبی |
| **brms** | رگرسیون بیزی (Stan) |
| **رستان** | رابط Stan |
| **پیش بینی** | پیش بینی سری های زمانی |
| **سیبل** | داده های سری زمانی |
| **افسانه** | مدل های سری زمانی |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **DBI** | استاندارد رابط پایگاه داده |
| **dbplyr** | dplyr backend برای پایگاه های داده |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | اتصالات ODBC |
| **bigrquery** | Google BigQuery |
| **درخشنده** | آپاچی اسپارک |
| **پیکان** | پیکان آپاچی / پارکت |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **تست که** | تست واحد (محبوب ترین) |
| **کوچکترین** | تست سبک وزن |
| **لینتر** | کد لینتینگ |
| ** جلد ** | پوشش کد |
| **مسخره** | تمسخر |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **لینتر** | کد لینتینگ |
| **استایلر** | قالب بندی کد |
| **عمل خوب** | بررسی کیفیت بسته بندی |
| ** جلد ** | پوشش کد |
| **cyclocomp** | پیچیدگی سیکلوماتیک |
| **pkgdown** | وب سایت مستندات بسته |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## تحقیق تکرارپذیر
| ابزار | هدف |
|------|---------|
| **R Markdown** | گزارش های تکراری |
| **Quarto** | انتشارات نسل بعدی |
| **نیتر** | تولید گزارش پویا |
| **اهداف** | مدیریت خط لوله |
| **دریک** | خطوط لوله مانند (میراث) |
| **کتاب پایین** | کتاب های R Markdown |
| **بلاگ داون** | وبلاگ ها از R Markdown |
| **تقطیر** | مقالات علمی |
| **براق** | برنامه های وب تعاملی |
| **فلکس داشبورد** | داشبورد |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **داده.جدول** | دستکاری سریع داده ها |
| **R6** | کلاس های مرجع (OOP) |
| **رلنگ** | ابزار برنامه نویسی R |
| **vctrs** | کلاس های وکتور |
| **چسب** | درون یابی رشته ای |
| **کلی** | رابط های خط فرمان |
| **با** | حالت موقت |
| **fs** | عملیات سیستم فایل |
| **httr2** | سرویس گیرنده HTTP |
| **jsonlite** | تجزیه JSON |
| **xml2** | تجزیه XML/HTML |
| **rvest** | خراش دادن وب |
| **موازی** | موازی سازی داخلی |
| **آینده** | توازی یکپارچه |
| **فورر** | purrr + آینده |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **RStudio** | استاندارد R IDE |
| **پوزیترون** | نسل بعدی IDE (موقعیت) |
| **پسوند VS Code + R** | سبک، R LSP |
| **Neovim + nvim-r** | مبتنی بر ترمینال |
| **ژوپیتر + IRkernel** | رابط نوت بوک |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **سرور براق** | میزبانی برنامه های درخشان |
| **Posit Connect** | استقرار Enterprise R |
| **لوله کش** | REST API از R |
| **داکر** | کانتینریزه (تصاویر سنگی) |
| **Quarto + Netlify** | سایت های استاتیک |
| **AWS Lambda** | R بدون سرور |
| **اهداف** | ارکستراسیون خط لوله |
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

## خلاصه
اکوسیستم R استاندارد طلایی برای محاسبات آماری و علم داده است. پشته استاندارد عبارتند از: **R 4.3+** به عنوان زمان اجرا، **RStudio** به عنوان IDE، **tidyverse** برای دستکاری و تجسم داده، **tidymodels** برای یادگیری ماشین، **ggplot2** برای ترسیم، **testthat** برای آزمایش، **lintr** برای linting، و **گزارش های Quarto** برای تولید مجدد. R در آمار، تجسم داده ها، بیوانفورماتیک (Bioconductor) و تحقیقات تکرارپذیر برتر است. اکوسیستم CRAN دارای بیش از 19000 بسته است. برای استقرار تولید، **Plumber** اسکریپت های R را به API تبدیل می کند و **Shiny** برنامه های کاربردی وب تعاملی ایجاد می کند.