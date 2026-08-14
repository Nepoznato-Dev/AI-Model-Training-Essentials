<!--
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

-->
# R — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ R-এ সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1. লুপগুলিতে ডেটা ফ্রেম বৃদ্ধি করা
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

## 2.`<-`এর পরিবর্তে`=`ব্যবহার করা
```r
# ❌ WRONG — confusing assignment in function calls
mean(x = 1:10)  # works but confusing
x = 5           # works but not idiomatic

# ✅ CORRECT — use <- for assignment, = for arguments
x <- 5
mean(x = 1:10)  # = is fine for named arguments
```

---

## 3. ভেক্টর রিসাইক্লিং না বোঝা
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

## 4.`T`এবং`F`বনাম`TRUE`এবং `FALSE`
```r
# ❌ WRONG — T and F can be overwritten
T <- FALSE  # this works! Now T is FALSE
TRUE <- FALSE  # Error: cannot change TRUE

# ✅ CORRECT — always use TRUE/FALSE
if (x == TRUE) { ... }
```

---

## 5.`stringsAsFactors = FALSE`ব্যবহার করছেন না
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

## 6.`apply`পরিবার বনাম টিডাইভার্স
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

## 7.`NA`মানগুলি পরিচালনা করা হচ্ছে না
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

## 8.`<<-`এর সাথে গ্লোবাল অ্যাসাইনমেন্ট
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

## সারাংশ
R-এর ইন্টারেক্টিভ প্রকৃতি ফাঁদ তৈরি করে: লুপগুলিতে ডেটা ফ্রেম বাড়ানো (প্রি-অ্যালোকেট বা ভেক্টরাইজ), ভেক্টর রিসাইক্লিং বিস্ময়,`NA`প্রচার, এবং`T`/`F`ওভাররাইটযোগ্য। R উপায় হল: অপারেশনগুলি ভেক্টরাইজ করুন, লুপ করার সময় আগে থেকে বরাদ্দ করুন,`NA`স্পষ্টভাবে পরিচালনা করুন, ডেটা ম্যানিপুলেশনের জন্য পরিপাটি ব্যবহার করুন এবং`<<-`এড়িয়ে চলুন। R তাদের পুরস্কৃত করে যারা ভেক্টরে চিন্তা করে এবং প্যাকেজের সমৃদ্ধ ইকোসিস্টেম ব্যবহার করে।