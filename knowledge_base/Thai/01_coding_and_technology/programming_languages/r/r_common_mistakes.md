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

# R - ข้อผิดพลาดทั่วไปและการต่อต้านรูปแบบ
เอกสารนี้รวบรวมข้อผิดพลาด กับดัก และรูปแบบการต่อต้านที่พบบ่อยที่สุดใน R พร้อมการแก้ไข
---

## 1. การขยายเฟรมข้อมูลในลูป
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

## 2. ใช้`=`แทน `<-`
```r
# ❌ WRONG — confusing assignment in function calls
mean(x = 1:10)  # works but confusing
x = 5           # works but not idiomatic

# ✅ CORRECT — use <- for assignment, = for arguments
x <- 5
mean(x = 1:10)  # = is fine for named arguments
```

---

## 3. ไม่เข้าใจเรื่องการรีไซเคิลเวกเตอร์
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

## 4.`T`และ`F`เทียบกับ`TRUE`และ `FALSE`
```r
# ❌ WRONG — T and F can be overwritten
T <- FALSE  # this works! Now T is FALSE
TRUE <- FALSE  # Error: cannot change TRUE

# ✅ CORRECT — always use TRUE/FALSE
if (x == TRUE) { ... }
```

---

## 5. ไม่ได้ใช้ `stringsAsFactors = FALSE`
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

## 6.`apply`ครอบครัว vs Tidyverse
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

## 7. ไม่จัดการค่า `NA`
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

## 8. การมอบหมายระดับโลกด้วย `<<-`
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

## สรุป
ลักษณะการโต้ตอบของ R จะสร้างกับดัก: การเพิ่มเฟรมข้อมูลในลูป (จัดสรรล่วงหน้าหรือเวกเตอร์), การรีไซเคิลเวกเตอร์ที่น่าประหลาดใจ, การแพร่กระจาย`NA`และ`T`/`F`ที่ถูกเขียนทับได้ วิธี R คือ: การดำเนินการ vectorize, จัดสรรล่วงหน้าเมื่อวนซ้ำ, จัดการ`NA`อย่างชัดเจน, ใช้ tidyverse สำหรับการจัดการข้อมูล และหลีกเลี่ยง`<<-`R ให้รางวัลแก่ผู้ที่คิดเรื่องเวกเตอร์และใช้ระบบนิเวศของแพ็คเกจที่หลากหลาย