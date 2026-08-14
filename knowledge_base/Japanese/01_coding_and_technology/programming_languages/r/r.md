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

#R
R は、統計コンピューティングとデータ分析のために特別に設計されたプログラミング言語および環境です。 1993 年にオークランド大学の Ross Ihaka と Robert Gentleman によって作成された (したがって「R」)、大幅な拡張を加えた S 言語の実装です。 R はオープンソースであり、R コア チームによって保守されています。これは、学界、医療、金融、政府の統計学者、データ アナリスト、研究者にとっての標準ツールです。
R は、データ操作、統計モデリング、視覚化、レポート作成に優れています。そのパッケージ エコシステム (CRAN) には、これまでに考案されたほぼすべての統計手法をカバーする 20,000 を超えるパッケージがあります。
---

## なぜ R が重要なのか
- **統計コンピューティング**: あらゆる言語における統計手法の最も包括的なコレクション。
- **データ視覚化**: ggplot2 は出版品質のグラフィックスを生成します。グラフィックパラダイムの文法は他に類を見ません。
- **再現可能な研究**: R Markdown / Quarto を使用すると、コード、結果、説明を 1 つのドキュメントに結合できます。
- **学術標準**: 統計、生物情報学、疫学、生態学、経済学、社会科学で使用されます。
- **Tidyverse**: データ分析をエレガントかつ一貫性のあるものにする、まとまったパッケージのセット (dplyr、ggplot2、tidyr、readr)。
- **無料およびオープンソース**: ライセンス費用はかかりません。グローバルコミュニティによって積極的に維持されています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **パフォーマンス** |デフォルトではシングルスレッドです。大規模なデータセットでは遅い | C++ 統合には`data.table`、並列パッケージ、または Rcpp を使用します。
| **メモリ使用量** |データセット全体を RAM にロードします |`data.table::fread`、コア外処理用の arrow パッケージを使用する |
| **汎用言語ではありません** | Web 開発、システム プログラミング、またはアプリにはぎこちない |非統計タスクには Python、Go、または JavaScript を使用する |
| **一貫性のない構文** | Base R には癖があります。異なるパッケージでは異なる規則が使用されます。一貫性を保つために Tidyverse を使用する |
| **雇用市場** |主に学術/研究職 |データ サイエンスの役割では Python が好まれることが増えています |
---

## 構文の基礎
### 基本操作
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

### Tidyverse (モダンR)
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

### ggplot2 による視覚化
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

### 統計モデリング
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

## 高度な構文とパターン
### S3 および S4 オブジェクト システム
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

### R6 参照クラス
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

### 非標準の評価とメタプログラミング
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

### 演算子のオーバーロード
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

## 同時実行性と並列処理
### パラレルパッケージ
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

### 未来のパッケージ
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

## プロジェクトの構成とシステムの構築
### パッケージ構造
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

### 説明ファイル
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

### renv を使用した依存関係管理
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### GitHub アクションを使用した CI/CD
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

## テスト
### testthat フレームワーク
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

## 相互運用性
### C/C++ と Rcpp の統合
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

### R から Python を呼び出す
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

## デザインパターン
### パターン 1: 柔軟な機能の適切な評価
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

### パターン 2: purrr を使用した関数型プログラミング
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

### パターン 3: レポート生成パイプライン
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

## パフォーマンスと最適化
### プロファイリングツール
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

### ベクトル化と data.table
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

### メモリの最適化
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

## デプロイメント
### CRAN へのパッケージの公開
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### 光沢のあるアプリケーション
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

### コンテナのデプロイメント
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## R を使用する場合
|シナリオ |なぜ R |より良い代替案 |
|----------|------|----------|
|統計分析 |最も包括的な統計手法 | Python (統計モデル、scipy) |
|データの視覚化 | ggplot2 は出版品質において比類のないものです。インタラクティブな Python (matplotlib、seaborn) |
|学術研究 |多くの分野の標準 | — |
|バイオインフォマティクス | Bioconductor には 2,000 以上の特殊なパッケージがあります |実稼働パイプライン用の Python |
|レポート (R Markdown/Quarto) |統合分析 + ナラティブ |ジュピター (Python) |
|プロダクション ML システム |導入用に設計されていません | Python、Java |
|ウェブ開発 |適さない | JavaScript、Python |
|大規模データ処理 |メモリバウンド | Python (PySpark)、SQL |
---

## 総合的な Q&A
### Q1: 割り当ての`<-`と`=`の違いは何ですか?
**A:** どちらも値を割り当てますが、`<-` は慣用的な R 代入演算子です。これは、関数呼び出し内を含むすべてのコンテキストで機能します。
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

### Q2: R で欠落したデータはどのように処理すればよいですか?
**A:** R は欠損値に`NA`を使用します。ほとんどの関数には`na.rm`パラメータがあります。
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

### Q3: `lapply`、`sapply`、`vapply` をどのような場合に使用する必要がありますか?
**A:** すべてリスト/ベクトルに関数を適用しますが、出力が異なります。
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

### Q4: ggplot2 を使用して効果的なビジュアライゼーションを作成するにはどうすればよいですか?
**A:** グラフィックスの文法に従い、データの美しさを視覚的なプロパティにマッピングします。
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

### Q5: 大規模なデータセットに対して効率的な R コードを作成するにはどうすればよいですか?
**A:** 主な実践方法:
- ベクトルの事前割り当て:`c()`で拡張する代わりに`x <- numeric(n)`
- 大規模なデータセットには`data.table`を使用します (data.frame より 100 倍高速)
- 操作をベクトル化 — 可能な限りループを回避します
- タイプ セーフティのために`sapply`ではなく`vapply`を使用します
-`Rprof()`または`profvis`を使用したプロファイル 
- コア外のデータには`arrow`パッケージを検討してください
---

## 思考連鎖による問題解決
### 問題 1: 乱雑なデータセットのクリーニングと分析
**ステップ 1: 問題を理解する**
欠損値、一貫性のない型、および外れ値を含むデータ フレームがあります。これをクリーンアップして、要約統計を計算する必要があります。
**ステップ 2: アプローチを特定する**
tinyverse 動詞を使用します:`filter`、`mutate`、`summarize`、および`group_by`。
**ステップ 3: 実装**```r
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

**ステップ 4: 確認**
前後の行数を確認し、範囲を検証し、合計をソース データと照合します。
### 問題 2: 線形回帰モデルの構築
**ステップ 1: 問題を理解する**
複数の予測子から連続結果変数を予測します。
**ステップ 2: アプローチを特定する**
線形回帰には`lm()`を使用し、仮定を確認し、モデルの適合性を評価します。
**ステップ 3: 実装**```r
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

**ステップ 4: 評価**
R 二乗、パターンの残差プロット、モデル比較の AIC を確認します。
### 問題 3: 再現可能なレポートの作成
**ステップ 1: 問題を理解する**
分析、視覚化、説明テキストを再現可能な形式で組み合わせたレポートを作成します。
**ステップ 2: アプローチを特定する**
R Markdown (または Quarto) を使用して、コード チャンクとテキストをインターリーブします。
**ステップ 3: 実装**```markdown
---
title: "Analysis Report"
output: html_document
---

## Data Overview

```{r setup, include=FALSE}
Knitr::opts_chunk$set(エコー = FALSE、警告 = FALSE)
ライブラリ(整頓)
データ <- read_csv("data.csv")```

The dataset contains `r nrow(data)` observations.

## Results

```{r plot}
ggplot(data, aes(x, y)) + geom_point() + geom_smooth()```
```

**ステップ 4: レンダリング**
`rmarkdown::render("report.Rmd")`は、自己完結型の HTML ドキュメントを生成します。
---

＃＃ まとめ
R は統計の言語です。データ分析、視覚化、統計モデリングに関しては、その深さと広さにおいて他に類を見ないものです。 Tidyverse は言語を最新化し、R Markdown/Quarto により再現可能な研究が簡単になります。 Python はデータ サイエンス全般で地位を確立しましたが、R は依然として厳密な統計作業のための専門家向けのツールです。定量的研究を行う人にとって、R の学習は不可欠です。
---

## 高度なデータ ラングリング
### data.table の詳細
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

### 整然とした評価と動的列
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

## 統計モデリングの詳細
### 高度な回帰
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

### 時系列分析
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

### tinymodels による機械学習
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
