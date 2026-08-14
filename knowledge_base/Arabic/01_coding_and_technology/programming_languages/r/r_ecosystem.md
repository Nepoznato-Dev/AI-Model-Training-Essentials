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
# R - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والحزم والبنية التحتية الأساسية في نظام R البيئي.
---

## تطبيقات البحث
| التنفيذ | ملاحظات |
|---------------|-------|
| **ر (جنو آر)** | قياسي، الأكثر استخدامًا على نطاق واسع |
| **ارستوديو** | IDE مع R متكامل |
| **بوزيترون** | IDE من الجيل التالي (وضعي) |
| **مايكروسوفت آر مفتوح** | الأمثل (المؤرشفة) |
| **pqR** | الموازي R |
| **رينجين** | R القائم على JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| **install.packages()** | حزم CRAN |
| **كران** | شبكة أرشيف R الشاملة (+19,000 حزمة) |
| ** موصل حيوي ** | حزم الجينوم / الأحياء |
| ** أجهزة التحكم عن بعد ** | التثبيت من جيثب |
| **باك** | مثبت الحزمة الحديثة |
| **رينف** | البيئات المحلية للمشروع |
| **باكرات** | إدارة التبعية (القديمة) |
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

## تايديفيرس
| الحزمة | الغرض |
|---------|--------|
| **dplyr** | معالجة البيانات |
| **ترتيب** | ترتيب البيانات |
| ** ggplot2 ** | تصور البيانات |
| **القارئ** | قراءة سريعة لملف CSV/|
| ** بور ** | البرمجة الوظيفية |
| ** تيبل ** | إطارات البيانات الحديثة |
| **سترينجر** | التلاعب بالسلسلة |
| **فوركات** | التعامل مع العوامل |
| ** تليين ** | التعامل مع التاريخ/الوقت |
| **ماجريتر** | مشغل الأنابيب (%>%) |
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

## علوم البيانات والإحصاء
| الحزمة | الغرض |
|---------|--------|
| **عارضات الأزياء** | إطار النمذجة (يستبدل علامة الإقحام) |
| **علامة الإقحام** | التعلم الآلي (تراث) |
| ** غابة عشوائية ** | غابات عشوائية |
| **xgboost** | تعزيز التدرج |
| **جلمنت** | الانحدار المنظم |
| **البقاء** | تحليل البقاء على قيد الحياة |
| **lme4** | نماذج التأثيرات المختلطة |
| **برمس** | الانحدار البايزي (ستان) |
| **رستان** | واجهة ستان |
| **التوقعات** | التنبؤ بالسلاسل الزمنية |
| **تسيبل** | بيانات السلاسل الزمنية |
| **خرافة** | نماذج السلاسل الزمنية |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| ** دي بي آي ** | واجهة قاعدة البيانات القياسية |
| **دببلير** | الواجهة الخلفية dplyr لقواعد البيانات |
| ** رسيكليتي ** | سكليتي |
| **RPostgres** | بوستجرس كيو ال |
| **RMariaDB** | ماي إس كيو إل/ماريا دي بي |
| **ودبك** | اتصالات ODBC |
| ** استعلام كبير ** | جوجل بيج كويري |
| **سباركلي** | أباتشي سبارك |
| **السهم** | سهم اباتشي / باركيه |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **اختبار ذلك** | اختبار الوحدة (الأكثر شهرة) |
| **الأصغر** | اختبار الوزن الخفيف |
| **لينتر** | فحص الكود |
| **التغطية** | تغطية الكود |
| **استهزاء** | استهزاء |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **لينتر** | فحص الكود |
| ** الطراز ** | تنسيق الكود |
| **ممارسة جيدة** | فحوصات جودة الحزمة |
| **التغطية** | تغطية الكود |
| **سيكلوكومب** | التعقيد الدوري |
| **pkgdown** | موقع توثيق الحزمة |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## بحث قابل للتكرار
| أداة | الغرض |
|------|---------|
| ** تخفيض السعر R ** | تقارير قابلة للتكرار |
| **الربع** | نشر الجيل القادم |
| **الحياكة** | توليد التقارير الديناميكية |
| **الأهداف** | إدارة خطوط الأنابيب |
| ** دريك ** | خطوط الأنابيب الشبيهة (تراثية) |
| **حجز** | كتب من R Markdown |
| **مدونة** | مدونات من R Markdown |
| **التقطير** | مقالات علمية |
| **لامعة** | تطبيقات الويب التفاعلية |
| **لوحة القيادة المرنة** | لوحات المعلومات |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **جدول البيانات** | معالجة سريعة للبيانات |
| **R6** | الفئات المرجعية (OOP) |
| **رلنج** | أدوات برمجة R |
| **vctrs** | فئات المتجهات |
| **الغراء** | استيفاء السلسلة |
| **كلي** | واجهات سطر الأوامر |
| **مع** | حالة مؤقتة |
| **خس** | عمليات نظام الملفات |
| **httr2** | عميل HTTP |
| ** جيسونلايت ** | تحليل JSON |
| **xml2** | تحليل XML/HTML |
| **رفست** | تجريف الويب |
| ** الموازي ** | التوازي المدمج |
| **المستقبل** | التوازي الموحد |
| **فررر** | بور + المستقبل |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **ارستوديو** | معيار R IDE |
| **بوزيترون** | IDE من الجيل التالي (وضعي) |
| ** رمز VS + امتداد R ** | خفيف الوزن، R LSP |
| ** نيوفيم + nvim-r** | القائم على المحطة الطرفية |
| **جوبيتر + IRkernel** | واجهة المفكرة |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **الخادم اللامع** | استضافة تطبيقات لامعة |
| **وضعية الاتصال** | نشر المؤسسة R |
| ** سباك ** | REST API من R |
| ** عامل الميناء ** | في حاويات (صور الروك) |
| ** كوارتو + نيتليفي ** | المواقع الثابتة |
| **AWS لامدا** | R بدون خادم |
| **الأهداف** | تنسيق خطوط الأنابيب |
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

## ملخص
يعد النظام البيئي لـ R هو المعيار الذهبي للحوسبة الإحصائية وعلوم البيانات. المكدس القياسي هو: **R 4.3+** كوقت تشغيل، **RStudio** كـ IDE، **tidyverse** لمعالجة البيانات وتصورها، **tidymodels** للتعلم الآلي، **ggplot2** للتخطيط، **testthat** للاختبار، **lintr** للفحص، و **Quarto** للتقارير القابلة للتكرار. يتفوق R في الإحصاء، وتصور البيانات، والمعلوماتية الحيوية (الموصل الحيوي)، والأبحاث القابلة للتكرار. يحتوي نظام CRAN البيئي على أكثر من 19000 حزمة. لنشر الإنتاج، يقوم **Plumber** بتحويل نصوص R النصية إلى واجهات برمجة التطبيقات (APIs)، ويقوم **Shiny** بإنشاء تطبيقات ويب تفاعلية.