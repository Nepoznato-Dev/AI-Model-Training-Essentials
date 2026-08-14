<!--
---
# Metadata
title: "R"
description: "Comprehensive reference for the R programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# R
R là ngôn ngữ lập trình và môi trường được thiết kế dành riêng cho tính toán thống kê và phân tích dữ liệu. Được tạo bởi Ross Ihaka và Robert Gentleman tại Đại học Auckland vào năm 1993 (do đó là "R"), đây là một triển khai của ngôn ngữ S với những phần mở rộng đáng kể. R là nguồn mở và được duy trì bởi Nhóm R Core. Đây là công cụ tiêu chuẩn dành cho các nhà thống kê, nhà phân tích dữ liệu và nhà nghiên cứu trong giới học thuật, y tế, tài chính và chính phủ.
R vượt trội trong thao tác dữ liệu, mô hình thống kê, trực quan hóa và báo cáo. Hệ sinh thái gói (CRAN) của nó có hơn 20.000 gói bao gồm hầu hết mọi phương pháp thống kê từng được nghĩ ra.
---

## Tại sao R lại quan trọng
- **Tính toán thống kê**: Bộ sưu tập các phương pháp thống kê toàn diện nhất bằng bất kỳ ngôn ngữ nào.
- **Trực quan hóa dữ liệu**: ggplot2 tạo ra đồ họa có chất lượng xuất bản. Ngữ pháp của mô hình đồ họa là chưa từng có.
- **Nghiên cứu có thể tái tạo**: R Markdown / Quarto cho phép bạn kết hợp mã, kết quả và tường thuật trong một tài liệu duy nhất.
- **Tiêu chuẩn học thuật**: Được sử dụng trong thống kê, tin sinh học, dịch tễ học, sinh thái học, kinh tế và khoa học xã hội.
- **Tidyverse**: Một tập hợp các gói gắn kết (dplyr, ggplot2,tidyr, readr) giúp việc phân tích dữ liệu trở nên tinh tế và nhất quán.
- **Nguồn mở và miễn phí**: Không có chi phí cấp phép; được duy trì tích cực bởi một cộng đồng toàn cầu.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Hiệu suất** | Đơn luồng theo mặc định; chậm đối với tập dữ liệu lớn | Sử dụng `data.table`, các gói song song hoặc Rcpp để tích hợp C++ |
| **Sử dụng bộ nhớ** | Tải toàn bộ tập dữ liệu vào RAM | Sử dụng`data.table::fread`, gói mũi tên để xử lý ngoài lõi |
| **Không phải ngôn ngữ có mục đích chung** | Lúng túng khi phát triển web, lập trình hệ thống hoặc ứng dụng | Sử dụng Python, Go hoặc JavaScript cho các tác vụ phi thống kê |
| **Cú pháp không nhất quán** | Cơ sở R có những điểm kỳ quặc; các gói khác nhau sử dụng các quy ước khác nhau | Sử dụng gọn gàng để đảm bảo tính nhất quán |
| **Thị trường việc làm** | Chủ yếu là vai trò học thuật/nghiên cứu | Vai trò khoa học dữ liệu ngày càng thích Python |
---

##Cơ bản về cú pháp
### Các thao tác cơ bản
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

### Tidyverse (R hiện đại)
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

### Trực quan hóa bằng ggplot2
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

### Mô hình thống kê
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

## Cú pháp & Mẫu nâng cao
### Hệ thống đối tượng S3 và S4
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

### Các lớp tham khảo R6
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

### Đánh giá phi tiêu chuẩn và lập trình meta
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

### Quá tải toán tử
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

## Đồng thời & Song song
###Gói song song
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

###Gói tương lai
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

### foreach/doParallel
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc gói
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

### Tệp MÔ TẢ
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

### Quản lý phụ thuộc với renv
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### CI/CD với Tác vụ GitHub
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

##Thử nghiệm
### testthat Framework
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

## Khả năng tương tác
### Tích hợp C/C++ với Rcpp
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

### Gọi Python từ R
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

## Mẫu thiết kế
### Mẫu 1: Đánh giá gọn gàng cho các chức năng linh hoạt
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

### Mẫu 2: Lập trình hàm với purrr
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

### Mẫu 3: Đường dẫn tạo báo cáo
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

### Vector hóa và data.table
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

### Tối ưu hóa bộ nhớ
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

## Triển khai
### Xuất bản gói lên CRAN
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### Ứng dụng sáng bóng
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

### Triển khai vùng chứa
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## Khi nào nên sử dụng R
| Kịch bản | Tại sao R | Thay thế tốt hơn |
|----------|-------|-------------------|
| Phân tích thống kê | Phương pháp thống kê toàn diện nhất | Python (mô hình thống kê, scipy) |
| Trực quan hóa dữ liệu | ggplot2 chưa từng có về chất lượng xuất bản | Python (matplotlib, seaborn) để tương tác |
| Nghiên cứu học thuật | Chuẩn trong nhiều lĩnh vực | — |
| Tin sinh học | Bioconductor có hơn 2.000 gói chuyên dụng | Python cho đường ống sản xuất |
| Báo cáo (R Markdown/Quarto) | Phân tích tổng hợp + tường thuật | Jupyter (Python) |
| Hệ thống ML sản xuất | Không được thiết kế để triển khai | Python, Java |
| Phát triển web | Không phù hợp | JavaScript, Python |
| Xử lý dữ liệu quy mô lớn | Bị ràng buộc bởi bộ nhớ | Python (PySpark), SQL |
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`<-`và`=`trong bài tập là gì?
**A:** Cả hai đều gán giá trị, nhưng`<-`là toán tử gán R đặc trưng. Nó hoạt động trong mọi ngữ cảnh, bao gồm cả các lệnh gọi hàm bên trong:
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

### Q2: Làm cách nào để xử lý dữ liệu bị thiếu trong R?
**A:** R sử dụng`NA`cho các giá trị bị thiếu. Hầu hết các hàm đều có tham số `na.rm`:
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

### Câu 3: Khi nào tôi nên sử dụng`lapply`so với`sapply`so với`vapply`?
**A:** Tất cả đều áp dụng một hàm trên danh sách/vectơ, nhưng khác nhau về đầu ra:
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

### Q4: Làm cách nào để tạo hình ảnh trực quan hiệu quả với ggplot2?
**A:** Tuân theo ngữ pháp của đồ họa — ánh xạ tính thẩm mỹ của dữ liệu tới các thuộc tính hình ảnh:
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

### Câu 5: Làm cách nào để viết mã R hiệu quả cho các tập dữ liệu lớn?
**Đ:** Các phương pháp chính:
- Phân bổ trước các vectơ:`x <- numeric(n)`thay vì phát triển với`c()`
- Sử dụng`data.table`cho tập dữ liệu lớn (nhanh hơn 100 lần so với data.frame)
- Vectorize các hoạt động - tránh các vòng lặp nếu có thể
- Sử dụng`vapply`thay vì`sapply`để đảm bảo an toàn về loại
- Hồ sơ với`Rprof()`hoặc`profvis`
- Xem xét gói`arrow`cho dữ liệu ngoài lõi
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Làm sạch và phân tích tập dữ liệu lộn xộn
**Bước 1: Tìm hiểu vấn đề**
Chúng tôi có khung dữ liệu thiếu các giá trị, loại không nhất quán và các giá trị ngoại lệ. Chúng ta cần làm sạch nó và tính toán số liệu thống kê tóm tắt.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng các động từ gọn gàng:`filter`,`mutate`,`summarize`và`group_by`.
**Bước 3: Thực hiện**```r
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

**Bước 4: Xác minh**
Kiểm tra số lượng hàng trước/sau, xác thực phạm vi và kiểm tra chéo tổng số so với dữ liệu nguồn.
### Bài toán 2: Xây dựng mô hình hồi quy tuyến tính
**Bước 1: Tìm hiểu vấn đề**
Dự đoán một biến kết quả liên tục từ nhiều yếu tố dự đoán.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`lm()`để hồi quy tuyến tính, kiểm tra các giả định và đánh giá mức độ phù hợp của mô hình.
**Bước 3: Thực hiện**```r
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

**Bước 4: Đánh giá**
Kiểm tra các ô dư, bình phương R để tìm các mẫu và AIC để so sánh mô hình.
### Vấn đề 3: Tạo một báo cáo có thể tái tạo
**Bước 1: Tìm hiểu vấn đề**
Tạo một báo cáo kết hợp phân tích, trực quan hóa và văn bản tường thuật ở định dạng có thể tái tạo.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng R Markdown (hoặc Quarto) để xen kẽ các đoạn mã với văn bản.
**Bước 3: Thực hiện**```markdown
---
title: "Analysis Report"
output: html_document
---

## Data Overview

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, cảnh báo = FALSE)
thư viện(tidyverse)
dữ liệu <- read_csv("data.csv")```

The dataset contains `r nrow(data)` observations.

## Results

```{r plot}
ggplot(data, aes(x, y)) + geom_point() + geom_smooth()```
```

**Bước 4: Kết xuất**
`rmarkdown::render("report.Rmd")`tạo ra một tài liệu HTML độc lập.
---

## Bản tóm tắt
R là ngôn ngữ của thống kê. Đối với phân tích dữ liệu, trực quan hóa và mô hình thống kê, nó vẫn có chiều sâu và chiều rộng chưa từng có. Tidyverse đã hiện đại hóa ngôn ngữ và R Markdown/Quarto giúp cho việc nghiên cứu có thể lặp lại trở nên đơn giản. Mặc dù Python đã có được chỗ đứng trong khoa học dữ liệu nói chung, nhưng R vẫn là công cụ chuyên dụng cho công việc thống kê nghiêm ngặt. Đối với bất kỳ ai thực hiện nghiên cứu định lượng, việc học R là điều cần thiết.
---

## Sắp xếp dữ liệu nâng cao
### data.table Tìm hiểu sâu
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

### Đánh giá gọn gàng và Cột động
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

## Tìm hiểu sâu về mô hình thống kê
### Hồi quy nâng cao
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

### Phân tích chuỗi thời gian
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

### Machine Learning với mô hình gọn gàng
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
