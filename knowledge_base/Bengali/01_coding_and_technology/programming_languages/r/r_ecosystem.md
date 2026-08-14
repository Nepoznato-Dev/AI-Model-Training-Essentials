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
# R — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি R ইকোসিস্টেমের প্রয়োজনীয় সরঞ্জাম, প্যাকেজ এবং অবকাঠামো কভার করে।
---

## আর বাস্তবায়ন
| বাস্তবায়ন | নোট |
|---------------|---------|
| **R (GNU R)** | স্ট্যান্ডার্ড, সর্বাধিক ব্যবহৃত |
| **আর স্টুডিও** | সমন্বিত R সহ IDE |
| **পজিট্রন** | নেক্সট-জেনার IDE (পজিট) |
| **Microsoft R Open** | অপ্টিমাইজড (সংরক্ষিত) |
| **pqR** | সমান্তরাল আর |
| **রেনজিন** | JVM-ভিত্তিক R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **install.packages()** | CRAN প্যাকেজ |
| **CRAN** | ব্যাপক R আর্কাইভ নেটওয়ার্ক (19,000+ প্যাকেজ) |
| **বায়োকন্ডাক্টর** | জিনোমিক্স/বায়োলজি প্যাকেজ |
| **রিমোট** | GitHub থেকে ইনস্টল করুন |
| **পাক** | আধুনিক প্যাকেজ ইনস্টলার |
| **renv** | প্রকল্প-স্থানীয় পরিবেশ |
| **প্যাকরাত** | নির্ভরতা ব্যবস্থাপনা (উত্তরাধিকার) |
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

## টিডাইভার্স
| প্যাকেজ | উদ্দেশ্য |
|---------|---------|
| **dplyr** | ডেটা ম্যানিপুলেশন |
| **পরিচ্ছন্ন** | তথ্য পরিপাটি |
| **ggplot2** | ডেটা ভিজ্যুয়ালাইজেশন |
| **পাঠক** | দ্রুত CSV/ফাইল রিডিং |
| **পুরর** | কার্যকরী প্রোগ্রামিং |
| **টিবল** | আধুনিক ডেটা ফ্রেম |
| **স্ট্রিংর** | স্ট্রিং ম্যানিপুলেশন |
| **ফরকেট** | ফ্যাক্টর হ্যান্ডলিং |
| **লুব্রিডেট** | তারিখ/সময় পরিচালনা |
| **ম্যাগ্রিত্র** | পাইপ অপারেটর (%>%) |
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

## তথ্য বিজ্ঞান ও পরিসংখ্যান
| প্যাকেজ | উদ্দেশ্য |
|---------|---------|
| **পরিপাটি মডেল** | মডেলিং ফ্রেমওয়ার্ক (ক্যারেট প্রতিস্থাপন করে) |
| **ক্যারেট** | মেশিন লার্নিং (উত্তরাধিকার) |
| **এলোমেলো বন** | এলোমেলো বন |
| **xgboost** | গ্রেডিয়েন্ট বুস্টিং |
| **glmnet** | নিয়মিত রিগ্রেশন |
| **বেঁচে থাকা** | বেঁচে থাকার বিশ্লেষণ |
| **lme4** | মিশ্র প্রভাব মডেল |
| **brms** | বায়েসিয়ান রিগ্রেশন (স্ট্যান) |
| **আরস্তান** | স্ট্যান ইন্টারফেস |
| **পূর্বাভাস** | সময় সিরিজের পূর্বাভাস |
| **টিসিবল** | টাইম সিরিজ ডেটা |
| **কথা** | টাইম সিরিজ মডেল |
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

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **DBI** | ডাটাবেস ইন্টারফেস স্ট্যান্ডার্ড |
| **dbplyr** | ডাটাবেসের জন্য dplyr ব্যাকএন্ড |
| **আরএসকিউলাইট** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC সংযোগ |
| **বিগ্রক্যুরি** | Google BigQuery |
| **স্পর্কলার** | অ্যাপাচি স্পার্ক |
| **তীর** | অ্যাপাচি তীর / Parquet |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **পরীক্ষা যে** | ইউনিট পরীক্ষা (সবচেয়ে জনপ্রিয়) |
| ** ক্ষুদ্রতম** | লাইটওয়েট টেস্টিং |
| **লিন্টার** | কোড লিন্টিং |
| **কভার** | কোড কভারেজ |
| **বিদ্রুপ** | উপহাস |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **লিন্টার** | কোড লিন্টিং |
| **স্টাইলার** | কোড ফরম্যাটিং |
| **ভাল অনুশীলন** | প্যাকেজ গুণমান পরীক্ষা |
| **কভার** | কোড কভারেজ |
| **সাইক্লোকম্প** | সাইক্লোমেটিক জটিলতা |
| **pkgdown** | প্যাকেজ ডকুমেন্টেশন ওয়েবসাইট |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## প্রজননযোগ্য গবেষণা
| টুল | উদ্দেশ্য |
|------|---------|
| **আর মার্কডাউন** | পুনরুত্পাদনযোগ্য প্রতিবেদন |
| **কোয়ার্টো** | পরবর্তী প্রজন্মের প্রকাশনা |
| **নিটার** | ডায়নামিক রিপোর্ট প্রজন্ম |
| **লক্ষ্য** | পাইপলাইন ব্যবস্থাপনা |
| **ড্রেক** | মেক-লাইন পাইপলাইন (উত্তরাধিকার) |
| **বুকডাউন** | আর মার্কডাউন থেকে বই |
| **ব্লগডাউন** | আর মার্কডাউন থেকে ব্লগ |
| **পান** | বৈজ্ঞানিক নিবন্ধ |
| **চকচকে** | ইন্টারেক্টিভ ওয়েব অ্যাপস |
| **ফ্লেক্সড্যাশবোর্ড** | ড্যাশবোর্ড |
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

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **ডেটা টেবিল** | দ্রুত ডেটা ম্যানিপুলেশন |
| **R6** | রেফারেন্স ক্লাস (OOP) |
| **rlang** | আর প্রোগ্রামিং টুলস |
| **vctrs** | ভেক্টর ক্লাস |
| **আঠা** | স্ট্রিং ইন্টারপোলেশন |
| **cli** | কমান্ড লাইন ইন্টারফেস |
| **সহ** | অস্থায়ী অবস্থা |
| **fs** | ফাইল সিস্টেম অপারেশন |
| **httr2** | HTTP ক্লায়েন্ট |
| **jsonlite** | JSON পার্সিং |
| **xml2** | XML/HTML পার্সিং |
| **আরভেস্ট** | ওয়েব স্ক্র্যাপিং |
| **সমান্তরাল** | অন্তর্নির্মিত সমান্তরালতা |
| **ভবিষ্যত** | একীভূত সমান্তরাল |
| **ফুরর** | purrr + ভবিষ্যত |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **আর স্টুডিও** | স্ট্যান্ডার্ড R IDE |
| **পজিট্রন** | নেক্সট-জেনার IDE (পজিট) |
| **ভিএস কোড + আর এক্সটেনশন** | লাইটওয়েট, আর এলএসপি |
| **নিওভিম + এনভিম-আর** | টার্মিনাল ভিত্তিক |
| **বৃহস্পতি + IRkernel** | নোটবুক ইন্টারফেস |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **চকচকে সার্ভার** | চকচকে অ্যাপ হোস্ট করুন |
| **পজিট কানেক্ট** | এন্টারপ্রাইজ R স্থাপনা |
| **প্লাম্বার** | R থেকে REST API |
| **ডকার** | কন্টেইনারাইজড (রকার ইমেজ) |
| **কোয়ার্টো + নেটলিফাই** | স্ট্যাটিক সাইট |
| **AWS Lambda** | সার্ভারহীন আর |
| **লক্ষ্য** | পাইপলাইন অর্কেস্ট্রেশন |
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

## সারাংশ
R এর ইকোসিস্টেম হল পরিসংখ্যানগত কম্পিউটিং এবং ডেটা সায়েন্সের সোনার মান। স্ট্যান্ডার্ড স্ট্যাক হল: **R 4.3+** রানটাইম হিসাবে, **RStudio** IDE হিসাবে, **ডাটা ম্যানিপুলেশন এবং ভিজ্যুয়ালাইজেশনের জন্য **tidyverse**, মেশিন লার্নিং এর জন্য **tidymodels**, প্লট করার জন্য **ggplot2**, **টেস্টথ্যাট** পরীক্ষার জন্য, **লিন্টিং এর জন্য **লিন্টার** এবং **রিপোর্টের জন্য **প্রোউকার্ড** R পরিসংখ্যান, ডেটা ভিজ্যুয়ালাইজেশন, বায়োইনফরমেটিক্স (বায়োকন্ডাক্টর), এবং প্রজননযোগ্য গবেষণায় পারদর্শী। CRAN ইকোসিস্টেমে 19,000+ প্যাকেজ রয়েছে। প্রোডাকশন ডিপ্লয়মেন্টের জন্য, **প্লাম্বার** R স্ক্রিপ্টগুলিকে API এ পরিণত করে এবং **চকচকে** ইন্টারেক্টিভ ওয়েব অ্যাপ্লিকেশন তৈরি করে।