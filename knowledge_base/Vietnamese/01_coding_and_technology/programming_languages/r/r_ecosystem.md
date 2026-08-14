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

# R — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, gói và cơ sở hạ tầng thiết yếu trong hệ sinh thái R.
---

## Triển khai R
| Thực hiện | Ghi chú |
|--------------|-------|
| **R (GNU R)** | Tiêu chuẩn, được sử dụng rộng rãi nhất |
| **RStudio** | IDE tích hợp R |
| **Positron** | IDE thế hệ tiếp theo (Posit) |
| **Mở Microsoft R** | Tối ưu hóa (đã lưu trữ) |
| **pqR** | Song song R |
| **Renjin** | R dựa trên JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **install.packages()** | gói CRAN |
| **CRAN** | Mạng lưu trữ R toàn diện (hơn 19.000 gói) |
| **Chất dẫn sinh học** | Gói gen/sinh học |
| **điều khiển từ xa** | Cài đặt từ GitHub |
| **pak** | Trình cài đặt gói hiện đại |
| **renv** | Môi trường dự án cục bộ |
| **gói** | Quản lý phụ thuộc (cũ) |
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

## Vũ trụ ngăn nắp
| Trọn gói | Mục đích |
|----------|----------|
| **dplyr** | Thao tác dữ liệu |
| **gọn gàng** | Dọn dẹp dữ liệu |
| **ggplot2** | Trực quan hóa dữ liệu |
| **người đọc** | Đọc CSV/tệp nhanh |
| **gừ gừ** | Lập trình chức năng |
| **tibble** | Khung dữ liệu hiện đại |
| **chuỗi** | Thao tác chuỗi |
| **cho mèo** | Xử lý yếu tố |
| **bôi trơn** | Xử lý ngày/giờ |
| **magrittr** | Toán tử đường ống (%>%) |
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

## Khoa học dữ liệu & Thống kê
| Trọn gói | Mục đích |
|----------|----------|
| **mô hình gọn gàng** | Khung mô hình hóa (thay thế dấu mũ) |
| **dấu mũ** | Học máy (cũ) |
| **Rừng ngẫu nhiên** | Rừng ngẫu nhiên |
| **xgboost** | Tăng cường độ dốc |
| **glmnet** | Hồi quy chính quy |
| **sống sót** | Phân tích sinh tồn |
| **lme4** | Mô hình hiệu ứng hỗn hợp |
| **brms** | Hồi quy Bayes (Stan) |
| **rstan** | Giao diện Stan |
| **dự báo** | Dự báo chuỗi thời gian |
| **Tsibble** | Dữ liệu chuỗi thời gian |
| **truyện ngụ ngôn** | Mô hình chuỗi thời gian |
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

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **DBI** | Chuẩn giao diện cơ sở dữ liệu |
| **dbplyr** | phụ trợ dplyr cho cơ sở dữ liệu |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Kết nối ODBC |
| **truy vấn lớn** | Google BigQuery |
| **lấp lánh** | Apache Spark |
| **mũi tên** | Mũi tên Apache / Sàn gỗ |
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

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **kiểm tra điều đó** | Kiểm tra đơn vị (phổ biến nhất) |
| **nhỏ nhất** | Thử nghiệm nhẹ |
| **lintr** | Mã linting |
| **covr** | Bảo hiểm mã |
| **chế nhạo** | Chế giễu |
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

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **lintr** | Mã linting |
| **người tạo kiểu tóc** | Định dạng mã |
| **thực hành tốt** | Kiểm tra chất lượng gói hàng |
| **covr** | Bảo hiểm mã |
| **cyclocomp** | Độ phức tạp theo chu kỳ |
| **pkgdown** | Trang web tài liệu trọn gói |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Nghiên cứu có thể tái tạo
| Công cụ | Mục đích |
|------|----------|
| **Giảm giá R** | Báo cáo có thể tái tạo |
| **Quarto** | Xuất bản thế hệ tiếp theo |
| **đan** | Tạo báo cáo động |
| **mục tiêu** | Quản lý đường ống |
| **drake** | Đường ống giống như (cũ) |
| **hạ sách** | Sách từ R Markdown |
| **dừng blog** | Blog từ R Markdown |
| **chưng cất** | Bài báo khoa học |
| **sáng bóng** | Ứng dụng web tương tác |
| **bảng điều khiển linh hoạt** | Trang tổng quan |
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

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **data.table** | Thao tác dữ liệu nhanh |
| **R6** | Các lớp tham khảo (OOP) |
| **rlang** | Công cụ lập trình R |
| **vctrs** | Lớp vectơ |
| **keo** | Nội suy chuỗi |
| **cli** | Giao diện dòng lệnh |
| **kéo** | Trạng thái tạm thời |
| **fs** | Hoạt động của hệ thống tập tin |
| **httr2** | Máy khách HTTP |
| **jsonlite** | Phân tích cú pháp JSON |
| **xml2** | Phân tích cú pháp XML/HTML |
| **đầu tư** | Quét web |
| **song song** | Tích hợp song song |
| **tương lai** | Song song thống nhất |
| **furrr** | gừ gừ + tương lai |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **RStudio** | IDE R tiêu chuẩn |
| **Positron** | IDE thế hệ tiếp theo (Posit) |
| **Mã VS + tiện ích mở rộng R** | Nhẹ, R LSP |
| **Neovim + nvim-r** | Dựa trên thiết bị đầu cuối |
| **Jupyter + IRkernel** | Giao diện sổ tay |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Máy chủ sáng bóng** | Lưu trữ ứng dụng sáng bóng |
| **Kết nối tích cực** | Triển khai Enterprise R |
| **Thợ sửa ống nước** | API REST từ R |
| **Docker** | Được container hóa (hình ảnh rocker) |
| **Quarto + Netlify** | Trang web tĩnh |
| **AWS Lambda** | R không có máy chủ |
| **mục tiêu** | Điều phối đường ống |
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

## Bản tóm tắt
Hệ sinh thái của R là tiêu chuẩn vàng cho tính toán thống kê và khoa học dữ liệu. Ngăn xếp tiêu chuẩn là: **R 4.3+** làm thời gian chạy, **RStudio** làm IDE, **tidyverse** để thao tác và trực quan hóa dữ liệu, **tidymodels** cho máy học, **ggplot2** cho vẽ đồ thị, **testthat** cho thử nghiệm, **lintr** cho linting và **Quarto** cho các báo cáo có thể tái tạo. R vượt trội về số liệu thống kê, trực quan hóa dữ liệu, tin sinh học (Bioconductor) và nghiên cứu có thể tái tạo. Hệ sinh thái CRAN có hơn 19.000 gói. Để triển khai sản xuất, **Plumber** biến tập lệnh R thành API và **Shiny** tạo các ứng dụng web tương tác.