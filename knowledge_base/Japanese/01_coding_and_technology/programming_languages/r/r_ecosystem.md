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
# R — エコシステムとツールのガイド
このガイドでは、R エコシステムの重要なツール、パッケージ、インフラストラクチャについて説明します。
---

## R の実装
|実装 |メモ |
|---------------|------|
| **R (GNU R)** |標準、最も広く使用されている |
| **RStudio** | R | 統合された IDE
| **ポジトロン** |次世代 IDE (Posit) |
| **Microsoft R オープン** |最適化 (アーカイブ) |
| **pqR** |平行R |
| **蓮人** | JVM ベースの R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **install.packages()** | CRAN パッケージ |
| **クラン** |包括的な R アーカイブ ネットワーク (19,000 以上のパッケージ) |
| **生体伝導体** |ゲノミクス/生物学パッケージ |
| **リモコン** | GitHub からインストール |
| **パク** |最新のパッケージ インストーラー |
| **renv** |プロジェクトのローカル環境 |
| **パックラット** |依存関係管理 (レガシー) |
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

## 整理整頓
|パッケージ |目的 |
|----------|----------|
| **dplyr** |データ操作 |
| **整理整頓** |データ整理 |
| **ggplot2** |データの視覚化 |
| **読者** | CSV/ファイルの高速読み取り |
| **ゴロゴロ** |関数型プログラミング |
| **ティブル** |最新のデータ フレーム |
| **ストリング** |文字列操作 |
| **フォーキャッツ** |係数の処理 |
| **潤滑剤** |日付/時刻の処理 |
| **マグリット** |パイプ演算子 (%>%) |
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

## データサイエンスと統計
|パッケージ |目的 |
|----------|----------|
| **tidymodels** |モデリング フレームワーク (キャレットを置き換えます) |
| **キャレット** |機械学習 (レガシー) |
| **ランダムフォレスト** |ランダムフォレスト |
| **xgboost** |勾配ブースティング |
| **glmnet** |正規化回帰 |
| **サバイバル** |生存分析 |
| **lme4** |混合効果モデル |
| **brms** |ベイジアン回帰 (スタン) |
| **ルスタン** |スタンインターフェース |
| **予測** |時系列予測 |
| **ツィブル** |時系列データ |
| **寓話** |時系列モデル |
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

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **DBI** |データベースインターフェース標準 |
| **dbplyr** |データベース用の dplyr バックエンド |
| **RSQLite** | SQLite |
| **RPostgres** |ポストグレSQL |
| **RMariaDB** | MySQL/マリアDB |
| **odbc** | ODBC 接続 |
| **ビッグクエリ** | Google BigQuery |
| **キラキラ** |アパッチスパーク |
| **矢印** | Apache Arrow / 寄木細工 |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **テストザット** |単体テスト (最も人気のある) |
| **小さなテスト** |軽量テスト |
| **lintr** |コードリンティング |
| **covr** |コードカバレッジ |
| **嘲笑** |嘲笑 |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **lintr** |コードリンティング |
| **スタイラー** |コードのフォーマット |
| **良い実践** |パッケージの品質検査 |
| **covr** |コードカバレッジ |
| **サイクロコンプ** |循環的複雑さ |
| **pkgdown** |パッケージドキュメントの Web サイト |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## 再現可能な研究
|ツール |目的 |
|-----|----------|
| **R マークダウン** |再現可能なレポート |
| **クアルト** |次世代出版 |
| **ニット** |動的レポート生成 |
| **ターゲット** |パイプライン管理 |
| **ドレイク** | Make-like パイプライン (レガシー) |
| **ブックダウン** | R Markdown の書籍 |
| **ブログダウン** | R Markdown のブログ |
| **蒸留** |科学記事 |
| **光沢のある** |インタラクティブな Web アプリ |
| **フレックスダッシュボード** |ダッシュボード |
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

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **データテーブル** |高速データ操作 |
| **R6** |参照クラス (OOP) |
| **rlang** | R プログラミング ツール |
| **vctrs** |ベクトルクラス |
| **接着剤** |文字列補間 |
| **クリ** |コマンドラインインターフェイス |
| **ウィザー** |一時的な状態 |
| **fs** |ファイル システムの操作 |
| **httr2** | HTTPクライアント |
| **jsonlite** | JSON 解析 |
| **xml2** | XML/HTML 解析 |
| **ベスト** | Webスクレイピング |
| **平行** |組み込みの並列処理 |
| **将来** |統合並列処理 |
| **ファール** |ゴロゴロ+未来 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **RStudio** |標準の R IDE |
| **ポジトロン** |次世代 IDE (Posit) |
| **VS コード + R 拡張機能** |軽量、R LSP |
| **Neovim + nvim-r** |ターミナルベース |
| **Jupyter + IRkernel** |ノートブックのインターフェイス |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **光沢のあるサーバー** | Shiny アプリをホストする |
| **ポジットコネクト** |エンタープライズ R の展開 |
| **配管工** | R の REST API |
| **ドッカー** |コンテナ化（ロッカーイメージ） |
| **Quarto + Netlify** |静的サイト |
| **AWS Lambda** |サーバーレス R |
| **ターゲット** |パイプライン オーケストレーション |
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

＃＃ まとめ
R のエコシステムは、統計コンピューティングとデータ サイエンスのゴールド スタンダードです。標準スタックは次のとおりです: ランタイムとして **R 4.3+**、IDE として **RStudio**、データ操作と視覚化に **tidyverse**、機械学習に **tidymodels**、プロットに **ggplot2**、テストに **testthat**、lint に**lintr**、再現可能なレポートに **Quarto**。 R は、統計、データ視覚化、バイオインフォマティクス (生体伝導体)、再現可能な研究を得意としています。 CRAN エコシステムには 19,000 以上のパッケージがあります。運用環境のデプロイでは、**Plumber** が R スクリプトを API に変換し、**Shiny** がインタラクティブな Web アプリケーションを作成します。