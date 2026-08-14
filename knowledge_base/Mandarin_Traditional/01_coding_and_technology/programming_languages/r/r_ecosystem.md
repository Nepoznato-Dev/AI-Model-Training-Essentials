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
# R — 生態系與工具指南
本指南涵蓋了 R 生態系統中的基本工具、套件和基礎設施。
---

## R 實現
|實施 |筆記|
|----------------|--------|
| **R (GNU R)** |標準，應用最廣泛|
| **RStudio** |整合 R 的 IDE |
| **正電子** |下一代 IDE（正面）|
| **微軟 R 開放** |優化（已存檔）|
| **pqR** |並行 R |
| **人金** |基於 JVM 的 R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## 套件管理
|工具|目的|
|------|---------|
| **安裝.packages()** | CRAN 套件 |
| **克蘭** |綜合 R 存檔網路（19,000 多個套件）|
| **生物導體** |基因組學/生物學包 |
| **遙控器** |從 GitHub 安裝 |
| **帕克** |現代軟體包安裝程式 |
| **租金** |專案本地環境 |
| **Packrat** |依賴管理（遺留）|
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

## 整潔宇宙
|套餐 |目的|
|---------|---------|
| **dplyr** |資料處理 |
| **整潔** |資料整理 |
| **ggplot2** |資料視覺化|
| **讀者** |快速讀取 CSV/檔案 |
| **咕嚕** |函數式程式設計 |
| **小標題** |現代資料框|
| **字串** |字串操作 |
| **福貓** |因素處理|
| **潤滑** |日期/時間處理 |
| **馬格里特** |管道運算符 (%>%) |
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

## 數據科學與統計學
|套餐 |目的|
|---------|---------|
| **整潔的模型** |建模框架（替換插入符號）|
| **插入符號** |機器學習（遺留）|
| **隨機森林** |隨機森林 |
| **xgboost** |梯度提升|
| **glmnet** |正規化迴歸 |
| **生存** |存活分析|
| **lme4** |混合效應模型|
| **brms** |貝葉斯回歸 (Stan) |
| **斯坦** |斯坦介面|
| **預測** |時間序列預測|
| **tsibble** |時間序列資料 |
| **寓言** |時間序列模型|
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

## 資料庫
|技術 |類型 |
|------------|------|
| **DBI** |資料庫介面標準|
| **dbplyr** |資料庫的 dplyr 後端 |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC 連線 |
| **大查詢** |Google BigQuery |
| **sparklyr** |阿帕契火花|
| **箭頭** |阿帕契箭頭/鑲木地板|
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

## 測試
|框架|目的|
|------------|---------|
| **測試** |單元測試（最受歡迎）|
| **微小測試** |輕量級測試|
| **林特爾** |代碼檢查 |
| **covr** |程式碼覆蓋率|
| **嘲諷** |嘲笑|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **林特爾** |代碼檢查 |
| **造型器** |程式碼格式化 |
| **良好實踐** |包裝品質檢查 |
| **covr** |程式碼覆蓋率|
| **環化合物** |圈複雜度|
| **pkgdown** |包文檔網站 |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## 可重複的研究
|工具|目的|
|------|---------|
| **R Markdown** |可重複的報告 |
| **四開本** |下一代出版 |
| **針織** |動態報告產生 |
| **目標** |管道管理|
| **德雷克** |類似 Make 的管道（遺留）|
| **預訂** | R Markdown 書籍 |
| **博客下載** |來自 R Markdown 的博客 |
| **蒸餾** |科學文章 |
| **閃亮** |互動式網路應用程式 |
| **彈性儀表板** |儀表板 |
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **資料.表** |快速資料操作 |
| **R6** |參考類別（OOP）|
| **rlang** | R 程式設計工具 |
| **vctrs** |向量類別 |
| **膠水** |字串插值|
| **cli** |命令列介面 |
| **與r** |臨時狀態 |
| **FS** |檔案系統操作|
| **httr2** | HTTP 用戶端 |
| **jsonlite** | JSON解析|
| **xml2** | XML/HTML 解析 |
| **旅行** |網頁抓取 |
| **平行** |內建並行性|
| **未來** |統一並行|
| **嗚嗚嗚** |咕嚕+未來|
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **RStudio** |標準 R IDE |
| **正電子** |下一代 IDE（正面）|
| **VS Code + R 擴充** |輕量級，R LSP |
| **Neovim + nvim-r** |基於終端 |
| **Jupyter + IRkernel** |筆記本介面 |
---

## 部署
|方法|筆記|
|--------|--------|
| **閃亮伺服器** |託管閃亮的應用程式 |
| **定位連線** |企業 R 部署 |
| **水電工** | R 中的 REST API |
| **碼頭工人** |貨櫃化（搖桿圖像）|
| **四開 + Netlify** |靜態網站|
| **AWS Lambda** |無伺服器 R |
| **目標** |管道編排|
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

＃＃ 概括
R 的生態系統是統計計算和資料科學的黃金標準。標準堆疊是：**R 4.3+** 作為運行時，**RStudio** 作為 IDE，**tidyverse** 用於數據操作和可視化，**tidymodels** 用於機器學習，**ggplot2** 用於繪圖，**testthat** 用於測試，**lintr** 用於 linting，**Quarto** 用於可重現報告。 R 擅長統計、資料視覺化、生物資訊學 (Bioconductor) 和可重複研究。 CRAN 生態系統擁有 19,000 多個軟體套件。對於生產部署，**Plumber** 將 R 腳本轉換為 API，而 **Shiny** 會建立互動式 Web 應用程式。