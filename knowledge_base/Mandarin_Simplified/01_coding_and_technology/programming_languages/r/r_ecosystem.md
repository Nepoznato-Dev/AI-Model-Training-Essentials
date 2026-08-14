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
# R — 生态系统和工具指南
本指南涵盖了 R 生态系统中的基本工具、包和基础设施。
---

## R 实现
|实施 |笔记|
|----------------|--------|
| **R (GNU R)** |标准，应用最广泛|
| **RStudio** |集成 R 的 IDE |
| **正电子** |下一代 IDE（正面）|
| **微软 R 开放** |优化（已存档）|
| **pqR** |并行 R |
| **人金** |基于 JVM 的 R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## 包管理
|工具|目的|
|------|---------|
| **安装.packages()** | CRAN 包 |
| **克兰** |综合 R 存档网络（19,000 多个包）|
| **生物导体** |基因组学/生物学包 |
| **遥控器** |从 GitHub 安装 |
| **帕克** |现代软件包安装程序 |
| **租金** |项目本地环境 |
| **Packrat** |依赖管理（遗留）|
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

## 整洁宇宙
|套餐 |目的|
|---------|---------|
| **dplyr** |数据处理 |
| **整洁** |数据整理 |
| **ggplot2** |数据可视化|
| **读者** |快速读取 CSV/文件 |
| **咕噜** |函数式编程 |
| **小标题** |现代数据框|
| **字符串** |字符串操作 |
| **福猫** |因素处理|
| **润滑** |日期/时间处理 |
| **马格里特** |管道运算符 (%>%) |
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

## 数据科学与统计学
|套餐 |目的|
|---------|---------|
| **整洁的模型** |建模框架（替换插入符号）|
| **插入符号** |机器学习（遗留）|
| **随机森林** |随机森林 |
| **xgboost** |梯度提升|
| **glmnet** |正则化回归 |
| **生存** |生存分析|
| **lme4** |混合效应模型|
| **brms** |贝叶斯回归 (Stan) |
| **斯坦** |斯坦接口|
| **预测** |时间序列预测|
| **tsibble** |时间序列数据 |
| **寓言** |时间序列模型|
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **DBI** |数据库接口标准|
| **dbplyr** |数据库的 dplyr 后端 |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC 连接 |
| **大查询** |谷歌 BigQuery |
| **sparklyr** |阿帕奇火花|
| **箭头** |阿帕奇箭头/镶木地板|
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

## 测试
|框架|目的|
|------------|---------|
| **测试** |单元测试（最流行）|
| **微小测试** |轻量级测试|
| **林特尔** |代码检查 |
| **covr** |代码覆盖率|
| **嘲讽** |嘲笑|
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

## 代码质量
|工具|目的|
|------|---------|
| **林特尔** |代码检查 |
| **造型器** |代码格式化 |
| **良好实践** |包装质量检查 |
| **covr** |代码覆盖率|
| **环化合物** |圈复杂度|
| **pkgdown** |包文档网站 |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## 可重复的研究
|工具|目的|
|------|---------|
| **R Markdown** |可重复的报告 |
| **四开本** |下一代出版 |
| **针织** |动态报告生成 |
| **目标** |管道管理|
| **德雷克** |类似 Make 的管道（遗留）|
| **预订** | R Markdown 书籍 |
| **博客下载** |来自 R Markdown 的博客 |
| **蒸馏** |科学文章 |
| **闪亮** |交互式网络应用程序 |
| **弹性仪表板** |仪表板 |
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

## 关键库
|图书馆 |目的|
|---------|---------|
| **数据.表** |快速数据操作 |
| **R6** |参考类（OOP）|
| **rlang** | R 编程工具 |
| **vctrs** |向量类 |
| **胶水** |字符串插值|
| **cli** |命令行界面 |
| **与r** |临时状态 |
| **FS** |文件系统操作|
| **httr2** | HTTP 客户端 |
| **jsonlite** | JSON解析|
| **xml2** | XML/HTML 解析 |
| **旅行** |网页抓取 |
| **平行** |内置并行性|
| **未来** |统一并行|
| **呜呜** |咕噜+未来|
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **RStudio** |标准 R IDE |
| **正电子** |下一代 IDE（正面）|
| **VS Code + R 扩展** |轻量级，R LSP |
| **Neovim + nvim-r** |基于终端 |
| **Jupyter + IRkernel** |笔记本接口 |
---

## 部署
|方法|笔记|
|--------|--------|
| **闪亮服务器** |托管闪亮的应用程序 |
| **定位连接** |企业 R 部署 |
| **水管工** | R 中的 REST API |
| **码头工人** |集装箱化（摇杆图像）|
| **四开 + Netlify** |静态站点|
| **AWS Lambda** |无服务器 R |
| **目标** |管道编排|
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
R 的生态系统是统计计算和数据科学的黄金标准。标准堆栈是：**R 4.3+** 作为运行时，**RStudio** 作为 IDE，**tidyverse** 用于数据操作和可视化，**tidymodels** 用于机器学习，**ggplot2** 用于绘图，**testthat** 用于测试，**lintr** 用于 linting，**Quarto** 用于可重现报告。 R 擅长统计、数据可视化、生物信息学 (Bioconductor) 和可重复研究。 CRAN 生态系统拥有 19,000 多个软件包。对于生产部署，**Plumber** 将 R 脚本转换为 API，而 **Shiny** 创建交互式 Web 应用程序。