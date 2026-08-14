<!--
---
# Metadata
title: "R — Cheat Sheet"
description: "Quick-reference cheat sheet for R syntax, data manipulation, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [r, statistics, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# R — Aide-mémoire
## Bases
```r
# Variables
name <- "Alice"
age <- 30
pi <- 3.14159
active <- TRUE
nothing <- NULL

# Types
class(name)       # "character"
class(42)         # "numeric"
class(42L)        # "integer"
class(TRUE)       # "logical"
class(NULL)       # "NULL"
class(NaN)        # "numeric"
class(NA)         # "logical"

# Type checking
is.character(name)
is.numeric(age)
is.logical(active)
is.null(nothing)
is.na(NA)

# String operations
nchar(name)                    # 5
toupper(name)                  # "ALICE"
tolower(name)                  # "alice"
trimws("  hello  ")            # "hello"
grepl("lic", name)             # TRUE
gsub("Alice", "Bob", name)
substr(name, 1, 3)             # "Ali"
paste("Hello", name, sep=" ")  # "Hello Alice"
sprintf("Hello, %s!", name)
strsplit("a,b,c", ",")         # list of "a" "b" "c"
```

## Vecteurs et structures de données
```r
# Vectors
v <- c(1, 2, 3, 4, 5)
v[1]              # 1 (1-indexed!)
v[c(1, 3)]        # c(1, 3)
v[2:4]            # c(2, 3, 4)
v[v > 3]          # c(4, 5) — logical indexing
length(v)
sum(v)
mean(v)
sd(v)
min(v)
max(v)
sort(v)
rev(v)
unique(v)
which(v > 3)      # indices where TRUE
any(v > 3)
all(v > 0)

# Sequences
1:10                # 1 to 10
seq(0, 1, by=0.1)
seq_len(10)
rep(0, times=5)     # c(0,0,0,0,0)
rep(c(1,2), each=3) # c(1,1,1,2,2,2)

# Matrix
m <- matrix(1:6, nrow=2, ncol=3)
m[1, 2]
m[, 1]              # first column
m[1, ]              # first row

# Data frame
df <- data.frame(
  name = c("Alice", "Bob"),
  age = c(30, 25),
  active = c(TRUE, FALSE)
)
df$name
df[["name"]]
df[df$age > 28, ]
df$name <- toupper(df$name)
nrow(df)
ncol(df)
str(df)
summary(df)

# List
lst <- list(name = "Alice", scores = c(90, 85), active = TRUE)
lst$name
lst[["scores"]]
lst[[2]]
```

## Flux de contrôle
```r
if (condition) {
  # ...
} else if (other) {
  # ...
} else {
  # ...
}

# Vectorized ifelse
result <- ifelse(x > 0, "positive", "non-positive")

# Loops
for (i in 1:10) { print(i) }
for (item in vector) { print(item) }
for (i in seq_along(vector)) { ... }
for (row in seq_len(nrow(df))) { ... }

while (condition) { ... }
repeat { if (condition) break }

# apply family
sapply(1:10, function(x) x^2)
lapply(1:10, function(x) x^2)
apply(matrix, 1, sum)     # row sums
apply(matrix, 2, mean)    # column means
vapply(1:10, function(x) x^2, numeric(1))
```

## Fonctions
```r
# Basic function
add <- function(a, b) {
  a + b
}

# Default args
greet <- function(name, greeting = "Hello") {
  paste(greeting, name)
}

# Variadic (dots)
flexible <- function(x, ...) {
  args <- list(...)
  print(args)
}

# Return multiple values
stats <- function(x) {
  list(mean = mean(x), sd = sd(x), n = length(x))
}
result <- stats(c(1, 2, 3, 4, 5))
result$mean

# Anonymous function
sapply(1:10, \(x) x^2)  # R 4.1+ shorthand
sapply(1:10, function(x) x^2)

# Pipe (R 4.1+)
result <- data |>
  filter(age > 18) |>
  select(name, age) |>
  arrange(name)
```

## Tidyverse
```r
library(tidyverse)

# dplyr verbs
result <- df |>
  filter(age >= 18) |>
  mutate(name = toupper(name)) |>
  select(name, age) |>
  arrange(desc(age)) |>
  summarise(avg_age = mean(age))

# Group by
df |>
  group_by(department) |>
  summarise(
    avg_salary = mean(salary),
    count = n()
  ) |>
  ungroup()

# tidyr
df |> pivot_wider(names_from = key, values_from = value)
df |> pivot_longer(cols = starts_with("score"), names_to = "subject")
df |> separate(col, into = c("first", "last"), sep = " ")
df |> unite("full", first, last, sep = " ")

# readr
read_csv("data.csv")
write_csv(df, "output.csv")
read_rds("data.rds")
```

## Traçage
```r
# Base R
plot(x, y, main = "Title", xlab = "X", ylab = "Y")
hist(data, breaks = 20)
boxplot(data ~ group)
barplot(table(category))

# ggplot2
library(ggplot2)
ggplot(df, aes(x = age, y = salary, color = department)) +
  geom_point() +
  geom_smooth(method = "lm") +
  facet_wrap(~ department) +
  theme_minimal() +
  labs(title = "Salary vs Age", x = "Age", y = "Salary")
```

## Gestion des erreurs
```r
# tryCatch
result <- tryCatch({
  risky_operation()
}, error = function(e) {
  message("Error: ", conditionMessage(e))
  NULL
}, warning = function(w) {
  message("Warning: ", conditionMessage(w))
}, finally = {
  cleanup()
})

# stop / warning / message
stop("Fatal error")
warning("Something suspicious")
message("Informational")

# stopifnot
stopifnot(length(x) > 0, is.numeric(x))
```
