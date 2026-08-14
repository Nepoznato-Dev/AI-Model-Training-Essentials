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
# R - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ แพ็คเกจ และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ R
---

## R การใช้งาน
| การนำไปปฏิบัติ | หมายเหตุ |
|---------|-------|
| **R (GNU R)** | มาตรฐานที่ใช้กันอย่างแพร่หลายที่สุด |
| **อาร์สตูดิโอ** | IDE พร้อมด้วย R |
| **โพซิตรอน** | IDE รุ่นต่อไป (ตำแหน่ง) |
| **ไมโครซอฟต์ อาร์ โอเพ่น** | ปรับให้เหมาะสม (เก็บถาวร) |
| **pqR** | ขนาน R |
| **เรนจิน** | R | ที่ใช้ JVM
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **install.packages()** | แพ็คเกจ CRAN |
| **แครน** | เครือข่ายการเก็บถาวร R ที่ครอบคลุม (มากกว่า 19,000 แพ็คเกจ) |
| **ตัวนำชีวภาพ** | แพ็คเกจจีโนมิกส์/ชีววิทยา |
| **รีโมท** | ติดตั้งจาก GitHub |
| **ปาก** | ตัวติดตั้งแพ็คเกจสมัยใหม่ |
| **เรโนล** | สภาพแวดล้อมภายในโปรเจ็กต์ |
| **แพ็ครัต** | การจัดการการพึ่งพา (ดั้งเดิม) |
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

## เดอะไทดี้เวิร์ส
| แพ็คเกจ | วัตถุประสงค์ |
|---------|---------|
| **dplyr** | การจัดการข้อมูล |
| **เป็นระเบียบเรียบร้อย** | การจัดระเบียบข้อมูล |
| **ggplot2** | การแสดงข้อมูลเป็นภาพ |
| **อ่าน** | การอ่าน CSV/ไฟล์ที่รวดเร็ว |
| **แป๊บ** | การเขียนโปรแกรมเชิงฟังก์ชัน |
| **tibble** | กรอบข้อมูลสมัยใหม่ |
| **stringr** | การจัดการสตริง |
| **ฟอร์กัต** | การจัดการปัจจัย |
| **หล่อลื่น** | การจัดการวันที่/เวลา |
| **มากริตเตอร์** | ผู้ปฏิบัติงานท่อ (%>%) |
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

## วิทยาศาสตร์ข้อมูลและสถิติ
| แพ็คเกจ | วัตถุประสงค์ |
|---------|---------|
| **tidymodels** | กรอบการสร้างแบบจำลอง (แทนที่คาเร็ต) |
| **คาเร็ต** | การเรียนรู้ของเครื่อง (แบบเดิม) |
| **ป่าสุ่ม** | ป่าสุ่ม |
| **xgboost** | การเร่งการไล่ระดับสี |
| **glmnet** | การถดถอยแบบสม่ำเสมอ |
| **การอยู่รอด** | การวิเคราะห์การอยู่รอด |
| **lme4** | โมเดลเอฟเฟกต์ผสม |
| **brms** | การถดถอยแบบเบย์ (สแตน) |
| **เริ่มต้น** | อินเตอร์เฟซสแตน |
| **พยากรณ์** | การพยากรณ์อนุกรมเวลา |
| **tsibble** | ข้อมูลอนุกรมเวลา |
| **นิทาน** | โมเดลอนุกรมเวลา |
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

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **ดีบีไอ** | มาตรฐานอินเตอร์เฟสฐานข้อมูล |
| **dbplyr** | แบ็กเอนด์ dplyr สำหรับฐานข้อมูล |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | การเชื่อมต่อ ODBC |
| **bigrquery** | Google BigQuery |
| **ประกายไฟ** | อาปาเช่ สปาร์ค |
| **ลูกศร** | อาปาเช่ แอร์โรว์ / ไม้ปาร์เก้ |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **ทดสอบว่า** | การทดสอบหน่วย (ยอดนิยม) |
| **เล็กที่สุด** | การทดสอบแบบน้ำหนักเบา |
| **lintr** | รหัสขุย |
| **covr** | ความครอบคลุมของโค้ด |
| **การเยาะเย้ย** | ล้อเลียน |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **lintr** | รหัสขุย |
| **อุปกรณ์จัดแต่งทรงผม** | การจัดรูปแบบโค้ด |
| **แนวปฏิบัติที่ดี** | การตรวจสอบคุณภาพบรรจุภัณฑ์ |
| **covr** | ความครอบคลุมของโค้ด |
| **ไซโคลคอมป์** | ความซับซ้อนแบบไซโคลมาติก |
| **แพ็คลง** | เว็บไซต์เอกสารแพ็คเกจ |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## การวิจัยที่สามารถทำซ้ำได้
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **รมาร์กดาวน์** | รายงานที่ทำซ้ำได้ |
| **ควอโต** | สำนักพิมพ์ยุคต่อไป |
| **ถัก** | การสร้างรายงานแบบไดนามิก |
| **เป้าหมาย** | การจัดการไปป์ไลน์ |
| **เดรก** | ไปป์ไลน์ที่เหมือนจริง (ดั้งเดิม) |
| **จองดาวน์** | หนังสือจาก R Markdown |
| **บล็อกดาวน์** | บล็อกจาก R Markdown |
| **กลั่น** | บทความทางวิทยาศาสตร์ |
| **แวววาว** | เว็บแอปแบบโต้ตอบ |
| **แดชบอร์ดแบบยืดหยุ่น** | แดชบอร์ด |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **data.table** | การจัดการข้อมูลอย่างรวดเร็ว |
| **R6** | คลาสอ้างอิง (OOP) |
| **ภาษา** | เครื่องมือการเขียนโปรแกรม R |
| **vctrs** | คลาสเวกเตอร์ |
| **กาว** | การแก้ไขสตริง |
| **คลิ้ก** | อินเทอร์เฟซบรรทัดคำสั่ง |
| **กับ** | สถานะชั่วคราว |
| **fs** | การทำงานของระบบไฟล์ |
| **httr2** | ไคลเอ็นต์ HTTP |
| **jsonlite** | การแยกวิเคราะห์ JSON |
| **xml2** | การแยกวิเคราะห์ XML/HTML |
| **ลงทุน** | การขูดเว็บ |
| **ขนาน** | ความเท่าเทียมในตัว |
| **อนาคต** | ความเท่าเทียมแบบครบวงจร |
| **ฟู่** | purrr + อนาคต |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **อาร์สตูดิโอ** | มาตรฐาน R IDE |
| **โพซิตรอน** | IDE รุ่นต่อไป (ตำแหน่ง) |
| **รหัส VS + ส่วนขยาย R** | น้ำหนักเบา R LSP |
| **นีโอวิม + nvim-r** | บนเทอร์มินัล |
| **Jupyter + IRkernel** | อินเตอร์เฟซโน๊ตบุ๊ค |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **เซิร์ฟเวอร์เงา** | โฮสต์แอป Shiny |
| **วางตำแหน่งเชื่อมต่อ** | การปรับใช้ Enterprise R |
| **ช่างประปา** | REST API จาก R |
| **นักเทียบท่า** | Containerized (ภาพโยก) |
| **Quarto + Netlify** | ไซต์แบบคงที่ |
| **AWS แลมบ์ดา** | ไร้เซิร์ฟเวอร์ R |
| **เป้าหมาย** | การจัดวางท่อ |
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

## สรุป
ระบบนิเวศของ R คือมาตรฐานทองคำสำหรับการคำนวณทางสถิติและวิทยาศาสตร์ข้อมูล สแต็กมาตรฐานคือ **R 4.3+** เป็นรันไทม์, **RStudio** เป็น IDE, **tidyverse** สำหรับการจัดการข้อมูลและการแสดงภาพ, **tidymodels** สำหรับแมชชีนเลิร์นนิง, **ggplot2** สำหรับการวางแผน, **testthat** สำหรับการทดสอบ, **lintr** สำหรับ Linting และ **Quarto** สำหรับรายงานที่ทำซ้ำได้ R เป็นเลิศในด้านสถิติ การสร้างภาพข้อมูล ชีวสารสนเทศศาสตร์ (ตัวนำไฟฟ้าชีวภาพ) และการวิจัยที่สามารถทำซ้ำได้ ระบบนิเวศ CRAN มีแพ็คเกจมากกว่า 19,000 รายการ สำหรับการใช้งานจริง **Plumber** เปลี่ยนสคริปต์ R เป็น API และ **Shiny** จะสร้างเว็บแอปพลิเคชันเชิงโต้ตอบ