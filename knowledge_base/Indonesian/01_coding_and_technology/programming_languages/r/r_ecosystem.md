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
# R — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, paket, dan infrastruktur penting dalam ekosistem R.
---

## Implementasi R
| Implementasi | Catatan |
|---------------|-------|
| **R (GNU R)** | Standar, paling banyak digunakan |
| **RStudio** | IDE dengan R |
| **Positron** | IDE generasi berikutnya (Posisi) |
| **Microsoft R Terbuka** | Dioptimalkan (diarsipkan) |
| **pqR** | Paralel R |
| **Renjin** | R |. berbasis JVM
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **instal.paket()** | Paket CRAN |
| **CRAN** | Jaringan Arsip R Komprehensif (19.000+ paket) |
| **Biokonduktor** | Paket genomik/biologi |
| **jarak jauh** | Instal dari GitHub |
| **pak** | Pemasang paket modern |
| **renv** | Lingkungan proyek-lokal |
| **paket** | Manajemen ketergantungan (warisan) |
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

## Bagian yang Rapi
| Paket | Tujuan |
|---------|---------|
| **dplyr** | Manipulasi data |
| **rapi** | Rapikan data |
| **ggplot2** | Visualisasi data |
| **pembaca** | Pembacaan CSV/file cepat |
| **mendengkur** | Pemrograman fungsional |
| **tibble** | Bingkai data modern |
| **string** | Manipulasi string |
| **untuk kucing** | Penanganan faktor |
| **melumasi** | Penanganan tanggal/waktu |
| **magrittr** | Operator pipa (%>%) |
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

## Ilmu Data & Statistik
| Paket | Tujuan |
|---------|---------|
| **model rapi** | Kerangka pemodelan (menggantikan tanda sisipan) |
| **tanda sisipan** | Pembelajaran mesin (warisan) |
| **hutan acak** | Hutan acak |
| **xgboost** | Peningkatan gradien |
| **glnet** | Regresi teregulasi |
| **kelangsungan hidup** | Analisis kelangsungan hidup |
| **lme4** | Model efek campuran |
| **brms** | Regresi Bayesian (Stan) |
| **pertama** | Antarmuka Stan |
| **ramalan** | Perkiraan deret waktu |
| **saudara** | Data deret waktu |
| **fabel** | Model deret waktu |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **DBI** | Standar antarmuka basis data |
| **dbplyr** | dplyr backend untuk database |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Koneksi ODBC |
| **pertanyaan besar** | Google BigQuery |
| **sparklyr** | Apache Percikan |
| **panah** | Apache Panah / Parket |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **uji itu** | Pengujian unit (paling populer) |
| **terkecil** | Pengujian ringan |
| **lintr** | Linting kode |
| **covr** | Cakupan kode |
| **ejekan** | Mengejek |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **lintr** | Linting kode |
| **penata gaya** | Pemformatan kode |
| **latihan yang baik** | Pemeriksaan kualitas paket |
| **covr** | Cakupan kode |
| **siklokomp** | Kompleksitas siklomatik |
| **pkgdown** | Situs web dokumentasi paket |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Penelitian yang Dapat Direproduksi
| Alat | Tujuan |
|------|---------|
| **Penurunan Harga R** | Laporan yang dapat direproduksi |
| **Kuarto** | Penerbitan generasi berikutnya |
| **rajut** | Pembuatan laporan dinamis |
| **target** | Manajemen saluran pipa |
| **drake** | Saluran pipa serupa (warisan) |
| **pembukuan** | Buku dari R Markdown |
| **blogdown** | Blog dari R Markdown |
| **disuling** | Artikel ilmiah |
| **mengkilap** | Aplikasi web interaktif |
| **dasbor fleksibel** | Dasbor |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **data.tabel** | Manipulasi data cepat |
| **R6** | Kelas referensi (OOP) |
| **rlang** | Alat pemrograman R |
| **vctrs** | Kelas vektor |
| **lem** | Interpolasi string |
| **kli** | Antarmuka baris perintah |
| **dengan** | Keadaan sementara |
| **fs** | Operasi sistem file |
| **httr2** | Klien HTTP |
| **jsonlite** | Penguraian JSON |
| **xml2** | Penguraian XML/HTML |
| **rompi** | Pengikisan web |
| **paralel** | Paralelisme bawaan |
| **masa depan** | Paralelisme terpadu |
| **furrr** | mendengkur + masa depan |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **RStudio** | Standar R IDE |
| **Positron** | IDE generasi berikutnya (Posisi) |
| **Kode VS + ekstensi R** | Ringan, R LSP |
| **Neovim + nvim-r** | Berbasis terminal |
| **Jupyter + Kernel IR** | Antarmuka buku catatan |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Server Mengkilap** | Tuan rumah aplikasi Shiny |
| **Hubungkan Pos** | Penerapan R Perusahaan |
| **Tukang Ledeng** | REST API dari R |
| **Buruh pelabuhan** | Dalam container (gambar rocker) |
| **Kuarto + Netlify** | Situs statis |
| **AWS Lambda** | R tanpa server |
| **target** | Orkestrasi saluran pipa |
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

## Ringkasan
Ekosistem R adalah standar emas untuk komputasi statistik dan ilmu data. Tumpukan standarnya adalah: **R 4.3+** sebagai runtime, **RStudio** sebagai IDE, **tidyverse** untuk manipulasi dan visualisasi data, **tidymodels** untuk machine learning, **ggplot2** untuk pembuatan plot, **testthat** untuk pengujian, **lintr** untuk linting, dan **Quarto** untuk laporan yang dapat direproduksi. R unggul dalam statistik, visualisasi data, bioinformatika (Biokonduktor), dan penelitian yang dapat direproduksi. Ekosistem CRAN memiliki 19.000+ paket. Untuk penerapan produksi, **Tukang Ledeng** mengubah skrip R menjadi API, dan **Shiny** membuat aplikasi web interaktif.