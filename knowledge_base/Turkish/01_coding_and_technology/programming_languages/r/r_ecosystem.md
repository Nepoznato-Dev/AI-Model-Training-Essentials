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
# R — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz, R ekosistemindeki temel araçları, paketleri ve altyapıyı kapsar.
---

## R Uygulamaları
| Uygulama | Notlar |
|---------------|----------|
| **R (GNU R)** | Standart, en yaygın kullanılan |
| **RStudio** | Entegre R'li IDE |
| **Pozitron** | Yeni nesil IDE (Posit) |
| **Microsoft R Açık** | Optimize edilmiş (arşivlenmiş) |
| **pqR** | Paralel R |
| **Renjin** | JVM tabanlı R |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **install.packages()** | CRAN paketleri |
| **CRAN** | Kapsamlı R Arşiv Ağı (19.000+ paket) |
| **Biyoiletken** | Genomik/biyoloji paketleri |
| **uzaktan kumandalar** | GitHub'dan yükleyin |
| **pak** | Modern paket yükleyici |
| **renv** | Proje yerel ortamları |
| **paket sıçanı** | Bağımlılık yönetimi (eski) |
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

## Düzenli Evren
| Paket | Amaç |
|-----------|-----------|
| **dplyr** | Veri manipülasyonu |
| **düzenli** | Veri düzenleme |
| **ggplot2** | Veri görselleştirme |
| **okuyucu** | Hızlı CSV/dosya okuma |
| **mırıldamak** | Fonksiyonel programlama |
| **tibble** | Modern veri çerçeveleri |
| **stringr** | Dize manipülasyonu |
| **kediler için** | Faktör yönetimi |
| **yağlayın** | Tarih/saat kullanımı |
| **magrittr** | Boru operatörü (%>%) |
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

## Veri Bilimi ve İstatistik
| Paket | Amaç |
|-----------|-----------|
| **düzenli modeller** | Modelleme çerçevesi (şapkanın yerine geçer) |
| **şapka** | Makine öğrenimi (eski) |
| **rastgele Orman** | Rastgele ormanlar |
| **xgboost** | Gradyan artırma |
| **glmnet** | Düzenli regresyon |
| **hayatta kalma** | Hayatta kalma analizi |
| **lme4** | Karışık efektli modeller |
| **brms** | Bayes regresyonu (Stan) |
| **rstan** | Stan'in arayüzü |
| **tahmin** | Zaman serisi tahmini |
| **tsibble** | Zaman serisi verileri |
| **masal** | Zaman serisi modelleri |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **DBI** | Veritabanı arayüzü standardı |
| **dbplyr** | veritabanları için dplyr arka ucu |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | ODBC bağlantıları |
| **büyük sorgu** | Google BigQuery |
| **parıltılı** | Apache Kıvılcımı |
| **ok** | Apache Oku / Parke |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **bunu test edin** | Birim testi (en popüler) |
| **minik test** | Hafiflik testi |
| **lintr** | Kod astarlama |
| **covr** | Kod kapsamı |
| **alay etme** | Alaycı |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **lintr** | Kod astarlama |
| **şekillendirici** | Kod biçimlendirme |
| **iyi uygulama** | Paket kalite kontrolleri |
| **covr** | Kod kapsamı |
| **döngüsel bilgisayar** | Döngüsel karmaşıklık |
| **pkgdown** | Paket dokümantasyon web sitesi |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Tekrarlanabilir Araştırma
| Araç | Amaç |
|------|------------|
| **R İndirimi** | Tekrarlanabilir raporlar |
| **Quarto** | Yeni nesil yayıncılık |
| **örgü** | Dinamik rapor oluşturma |
| **hedefler** | Boru hattı yönetimi |
| **ejderha** | Make-like boru hatları (eski) |
| **kitap indirme** | R Markdown'dan Kitaplar |
| **blog yazısı** | R Markdown'dan Bloglar |
| **damıtma** | Bilimsel makaleler |
| **parlak** | Etkileşimli web uygulamaları |
| **esnek kontrol paneli** | Kontrol Panelleri |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **veri.tablo** | Hızlı veri işleme |
| **R6** | Referans sınıfları (OOP) |
| **rlang** | R programlama araçları |
| **vctrs** | Vektör sınıfları |
| **tutkal** | Dize enterpolasyonu |
| **cli** | Komut satırı arayüzleri |
| **ile** | Geçici durum |
| **fs** | Dosya sistemi işlemleri |
| **httr2** | HTTP istemcisi |
| **jsonlite** | JSON ayrıştırma |
| **xml2** | XML/HTML ayrıştırma |
| **yatırım** | Web kazıma |
| **paralel** | Yerleşik paralellik |
| **gelecek** | Birleşik paralellik |
| **furrr** | mırıltı + gelecek |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **RStudio** | Standart R IDE |
| **Pozitron** | Yeni nesil IDE (Posit) |
| **VS Kodu + R uzantısı** | Hafif, R LSP |
| **Neovim + nvim-r** | Terminal tabanlı |
| **Jüpyter + IRkernel** | Dizüstü bilgisayar arayüzü |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Parlak Sunucu** | Shiny uygulamalarını barındırın |
| **Posit Connect** | Kurumsal R dağıtımı |
| **Tesisatçı** | R'den REST API |
| **Docker** | Containerized (rocker görüntüleri) |
| **Quarto + Netlify** | Statik siteler |
| **AWS Lambda** | Sunucusuz R |
| **hedefler** | Boru hattı orkestrasyonu |
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

## Özet
R'nin ekosistemi istatistiksel hesaplama ve veri bilimi için altın standarttır. Standart yığın şudur: Çalışma zamanı olarak **R 4.3+**, IDE olarak **RStudio**, veri işleme ve görselleştirme için **tidyverse**, makine öğrenimi için **tidymodels**, çizim için **ggplot2**, test için **testthat**, linting için **lintr** ve tekrarlanabilir raporlar için **Quarto**. R istatistik, veri görselleştirme, biyoenformatik (Biyokondüktör) ve tekrarlanabilir araştırmalarda üstün bir konuma sahiptir. CRAN ekosisteminde 19.000'den fazla paket bulunmaktadır. Üretim dağıtımı için **Plumber**, R komut dosyalarını API'lere dönüştürür ve **Shiny** etkileşimli web uygulamaları oluşturur.