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

# R — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, pacotes e infraestrutura essenciais no ecossistema R.
---

## Implementações R
| Implementação | Notas |
|---------------|-------|
| **R (GNU R)** | Padrão, mais utilizado |
| **RStudio** | IDE com R integrado |
| **Pósitron** | IDE de próxima geração (Posit) |
| **Microsoft R Open** | Otimizado (arquivado) |
| **pqR** | Paralelo R |
| **Renjin** | R baseado em JVM |
```bash
R --version             # check version
Rscript script.R        # run script
R                       # interactive REPL
R -e "summary(cars)"    # inline execution
```

---

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **instalar.packages()** | Pacotes CRAN |
| **CRAN** | Rede abrangente de arquivos R (mais de 19.000 pacotes) |
| **Biocondutor** | Pacotes de genômica/biologia |
| **controles remotos** | Instalar do GitHub |
| **pacote** | Instalador de pacote moderno |
| **renv** | Ambientes locais do projeto |
| **pacote** | Gerenciamento de dependências (legado) |
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

## O Universo Organizado
| Pacote | Finalidade |
|--------|---------|
| **dplyr** | Manipulação de dados |
| **arrumado** | Organização de dados |
| **ggplot2** | Visualização de dados |
| **ler** | Leitura rápida de CSV/arquivo |
| **ronronar** | Programação funcional |
| **tadinha** | Quadros de dados modernos |
| **string** | Manipulação de strings |
| **forcados** | Tratamento de fatores |
| **lubrificar** | Tratamento de data/hora |
| **magrittr** | Operador de tubulação (%>%) |
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

## Ciência de dados e estatística
| Pacote | Finalidade |
|--------|---------|
| **modelos arrumados** | Estrutura de modelagem (substitui o sinal de intercalação) |
| **caret** | Aprendizado de máquina (legado) |
| **floresta aleatória** | Florestas aleatórias |
| **xgboost** | Aumento de gradiente |
| **glmnet** | Regressão regularizada |
| **sobrevivência** | Análise de sobrevivência |
| **lme4** | Modelos de efeitos mistos |
| **brms** | Regressão bayesiana (Stan) |
| **rstan** | Interface Stan |
| **previsão** | Previsão de séries temporais |
| **tsibble** | Dados de séries temporais |
| **fábula** | Modelos de séries temporais |
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

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **DBI** | Padrão de interface de banco de dados |
| **dbplyr** | back-end dplyr para bancos de dados |
| **RSQLite** | SQLite |
| **RPostgres** | PostgreSQL |
| **RMariaDB** | MySQL/MariaDB |
| **odbc** | Conexões ODBC |
| **bigconsulta** | GoogleBigQuery |
| **brilhante** | Apache Faísca |
| **seta** | Seta Apache / Parquet |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **teste isso** | Testes unitários (mais populares) |
| **pequenoteste** | Teste leve |
| **lintr** | Linting de código |
| **cobertura** | Cobertura de código |
| **zombaria** | Zombando |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **lintr** | Linting de código |
| **estilista** | Formatação de código |
| **boas práticas** | Verificações de qualidade das embalagens |
| **cobertura** | Cobertura de código |
| **ciclocomp** | Complexidade ciclomática |
| **pacote** | Site de documentação do pacote |
```r
# lintr configuration (.lintr)
linters: linters_with_defaults(
    line_length_linter(120),
    object_name_linter(styles = c("snake_case", "camelCase"))
  )
encoding: "UTF-8"
```

---

## Pesquisa reproduzível
| Ferramenta | Finalidade |
|------|---------|
| **Redução R** | Relatórios reproduzíveis |
| **Quarto** | Publicação de próxima geração |
| **tricô** | Geração de relatórios dinâmicos |
| **alvos** | Gerenciamento de pipeline |
| **draco** | Pipelines semelhantes a make-like (herdados) |
| **registro** | Livros de R Markdown |
| **blogdown** | Blogs do R Markdown |
| **destilar** | Artigos científicos |
| **brilhante** | Aplicativos web interativos |
| **painel flexível** | Painéis |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **dados.tabela** | Manipulação rápida de dados |
| **R6** | Classes de referência (OOP) |
| **rlang** | Ferramentas de programação R |
| **videocassete** | Aulas de vetores |
| **cola** | Interpolação de strings |
| **clique** | Interfaces de linha de comando |
| **com** | Estado temporário |
| **fs** | Operações do sistema de arquivos |
| **httr2** | Cliente HTTP |
| **jsonlite** | Análise JSON |
| **xml2** | Análise XML/HTML |
| **vestido** | Raspagem na Web |
| **paralelo** | Paralelismo integrado |
| **futuro** | Paralelismo unificado |
| **furrr** | ronronar + futuro |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **RStudio** | O R IDE padrão |
| **Pósitron** | IDE de próxima geração (Posit) |
| **Código VS + extensão R** | Leve, R LSP |
| **Neovim + nvim-r** | Baseado em terminal |
| **Jupyter + IRkernel** | Interface do notebook |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Servidor Brilhante** | Hospedar aplicativos brilhantes |
| **Posit Connect** | Implantação do Enterprise R |
| **Encanador** | API REST de R |
| **Docker** | Contentorizado (imagens rocker) |
| **Quarto + Netlify** | Sites estáticos |
| **AWS Lambda** | R sem servidor |
| **alvos** | Orquestração de pipeline |
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

## Resumo
O ecossistema de R é o padrão ouro para computação estatística e ciência de dados. A pilha padrão é: **R 4.3+** como tempo de execução, **RStudio** como IDE, **tidyverse** para manipulação e visualização de dados, **tidymodels** para aprendizado de máquina, **ggplot2** para plotagem, **testthat** para teste, **lintr** para linting e **Quarto** para relatórios reproduzíveis. R é excelente em estatística, visualização de dados, bioinformática (Bioconductor) e pesquisa reproduzível. O ecossistema CRAN possui mais de 19.000 pacotes. Para implantação de produção, o **Plumber** transforma scripts R em APIs e o **Shiny** cria aplicativos Web interativos.