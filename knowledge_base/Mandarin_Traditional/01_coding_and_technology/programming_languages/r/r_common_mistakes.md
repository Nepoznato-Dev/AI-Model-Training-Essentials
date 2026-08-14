---
# Metadata
title: "R — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in R with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# R — 常見錯誤與反模式
本文檔列出了 R 中最常見的錯誤、陷阱和反模式，並進行了修正。
---

## 1. 在循環中成長資料幀
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

## 2. 使用`=`取代 `<-`
```r
# ❌ WRONG — confusing assignment in function calls
mean(x = 1:10)  # works but confusing
x = 5           # works but not idiomatic

# ✅ CORRECT — use <- for assignment, = for arguments
x <- 5
mean(x = 1:10)  # = is fine for named arguments
```

---

## 3. 不理解向量回收
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

## 4.`T`和`F`與`TRUE`和 `FALSE`
```r
# ❌ WRONG — T and F can be overwritten
T <- FALSE  # this works! Now T is FALSE
TRUE <- FALSE  # Error: cannot change TRUE

# ✅ CORRECT — always use TRUE/FALSE
if (x == TRUE) { ... }
```

---

## 5. 不使用 `stringsAsFactors = FALSE`
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

## 6.`apply`家族 vs Tidyverse
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

## 7. 不處理`NA`值
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

## 8. 使用`<<-`進行全域分配
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

＃＃ 概括
R 的交互性质会造成陷阱：循环中不断增长的数据帧（预分配或向量化）、向量回收意外、`NA` 传播以及`T`/`F`可重写。 R 方式是：向量化操作，循环时预分配，显式处理`NA`，使用 tidyverse 进行数据操作，并避免`<<-`。 R 獎勵那些用向量思考並使用其豐富的包生態系統的人。