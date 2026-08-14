---
# Metadata
title: "R — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in R with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [r, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# R — Erreurs courantes et anti-modèles
Ce document répertorie les erreurs, pièges et anti-modèles les plus courants dans R avec des corrections.
---

## 1. Développer des trames de données en boucles
```r
# ❌ WRONG — O(n²) growth
result <- data.frame()
for (i in 1:1000) {
    result <- rbind(result, data.frame(x = i, y = i^2))
}

# ✅ CORRECT — pre-allocate
result <- data.frame(x = integer(1000), y = integer(1000))
for (i in 1:1000) {
    result$x[i] <- i
    result$y[i] <- i^2
}

# ✅ BEST — use vectorized operations
result <- data.frame(x = 1:1000, y = (1:1000)^2)
```

---

## 2. Utiliser`=`au lieu de `<-`
```r
# ❌ WRONG — confusing assignment in function calls
mean(x = 1:10)  # works but confusing
x = 5           # works but not idiomatic

# ✅ CORRECT — use <- for assignment, = for arguments
x <- 5
mean(x = 1:10)  # = is fine for named arguments
```

---

## 3. Ne pas comprendre le recyclage des vecteurs
```r
# ❌ WRONG — silent recycling
a <- c(1, 2, 3, 4, 5)
b <- c(1, 2)
a + b  # c(2, 4, 4, 6, 6) — recycled with warning

# ✅ CORRECT — ensure matching lengths
stopifnot(length(a) == length(b))
a + b
```

---

## 4.`T`et`F`contre`TRUE`et `FALSE`
```r
# ❌ WRONG — T and F can be overwritten
T <- FALSE  # this works! Now T is FALSE
TRUE <- FALSE  # Error: cannot change TRUE

# ✅ CORRECT — always use TRUE/FALSE
if (x == TRUE) { ... }
```

---

## 5. Ne pas utiliser `stringsAsFactors = FALSE`
```r
# ❌ WRONG — pre-R 4.0 default
df <- data.frame(name = c("Alice", "Bob"), stringsAsFactors = TRUE)
df$name  # Factor, not character!

# ✅ CORRECT — R 4.0+ default is FALSE
df <- data.frame(name = c("Alice", "Bob"))  # character by default

# ✅ CORRECT — explicit for older R
df <- read.csv("data.csv", stringsAsFactors = FALSE)
```

---

## 6. Famille`apply`contre Tidyverse
```r
# ❌ WRONG — nested apply calls (hard to read)
result <- sapply(split(df, df$group), function(g) {
    sapply(g$values, function(v) v * 2)
})

# ✅ CORRECT — use dplyr/tidyverse
library(dplyr)
result <- df %>%
    group_by(group) %>%
    mutate(values = values * 2)
```

---

## 7. Ne pas gérer les valeurs `NA`
```r
# ❌ WRONG — NA propagates silently
mean(c(1, 2, NA, 4))  # NA
sum(c(1, 2, NA, 4))   # NA

# ✅ CORRECT — use na.rm
mean(c(1, 2, NA, 4), na.rm = TRUE)  # 2.33
sum(c(1, 2, NA, 4), na.rm = TRUE)   # 7

# ✅ CORRECT — check for NA
is.na(x)
complete.cases(df)
```

---

## 8. Affectation globale avec `<<-`
```r
# ❌ WRONG — modifies parent scope
counter <- 0
increment <- function() {
    counter <<- counter + 1
}

# ✅ CORRECT — use environments or return values
counter <- 0
increment <- function(counter) {
    counter + 1
}
counter <- increment(counter)
```

---

## Résumé
La nature interactive de R crée des pièges : croissance des trames de données en boucles (pré-allocation ou vectorisation), surprises de recyclage vectoriel, propagation de`NA`et`T`/`F`étant écrasés. La méthode R est la suivante : vectoriser les opérations, pré-allouer lors de la boucle, gérer explicitement `NA`, utiliser spiceverse pour la manipulation des données et éviter`<<-`. R récompense ceux qui pensent en vecteurs et utilisent son riche écosystème de packages.