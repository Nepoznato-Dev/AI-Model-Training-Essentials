---
# Metadata
title: "R — Syntax Reference"
description: "Detailed syntax reference for R covering vectors, data frames, tidyverse, ggplot2, statistical modeling, and R programming idioms."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [r, syntax-reference, vectors, data-frames, tidyverse, ggplot2, statistics, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# आर - सिंटैक्स संदर्भ
यह दस्तावेज़ R (4.x) के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, सुव्यवस्थित पारिस्थितिकी तंत्र, डेटा हेरफेर, सांख्यिकीय मॉडलिंग और विज़ुअलाइज़ेशन पर ध्यान केंद्रित करके मुख्य आर संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
### कोर ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `+``-``*``/``^`| अंकगणित | `2^10`| |
| `%%`| मापांक | `7 %% 3`| रिटर्न 1 |
| `%/%`| पूर्णांक विभाजन | `7 %/% 3`| रिटर्न 2 |
| `==``!=` | समानता | `x == y`| सदिशकृत |
| `<``>``<=``>=` | तुलना | `x >= y`| सदिशकृत |
| `&``\|``!`| तार्किक (वेक्टरीकृत) | `x & y`| तत्त्वानुसार |
| `&&``\|\|` | तार्किक (अदिश) | `x && y`| केवल पहला तत्व |
| `%in%`| सदस्यता | `x %in% y`| |
| `<-``=` | असाइनमेंट | `x <- 10`| `<-`मुहावरेदार है |
| `->`| सही असाइन करें | `10 -> x`| शायद ही कभी इस्तेमाल किया जाता है |
| `<<-`| ग्लोबल असाइन | `x <<- 10`| मूल वातावरण में असाइन करें |
| `$`| तत्व निकालें | `df$column`| |
| `[``[[` | अनुक्रमण | `x[1]`/`x[[1]]`| `[`एक ही प्रकार का रिटर्न देता है; `[[`अर्क |
| `%>%`| पाइप (मैग्रिट्र) | `x %>% f()`| |
| `\|>`| पाइप (आधार आर 4.1+) | `x \|> f()`| देशी पाइप |
### वेक्टरकृत संचालन
```r
# Everything is vectorized — no loops needed
x <- c(1, 2, 3, 4, 5)
x * 2              # c(2, 4, 6, 8, 10)
x > 3              # FALSE FALSE FALSE TRUE TRUE
x[x > 3]           # 4 5
ifelse(x > 3, "big", "small")  # "small" "small" "small" "big" "big"

# Recycling — shorter vector is repeated
c(1, 2, 3) + c(10, 20, 30)   # 11 22 33
c(1, 2, 3) + 10               # 11 12 13

# NA handling
mean(c(1, 2, NA, 4))           # NA
mean(c(1, 2, NA, 4), na.rm = TRUE)  # 2.333

# Sequence generation
1:10                            # 1 2 3 ... 10
seq(0, 1, by = 0.1)            # 0.0 0.1 0.2 ... 1.0
seq_len(5)                      # 1 2 3 4 5
rep(0, times = 5)               # 0 0 0 0 0
rep(c(1, 2), each = 3)          # 1 1 1 2 2 2
```

---

## डेटा प्रकार और संरचनाएँ
```r
# Atomic vectors (single type)
numeric_vec <- c(1.5, 2.7, 3.14)
integer_vec <- 1:10
char_vec <- c("a", "b", "c")
logical_vec <- c(TRUE, FALSE, NA)

# Lists (mixed types)
my_list <- list(name = "Alice", age = 30, scores = c(95, 87))
my_list$name        # "Alice"
my_list[["age"]]    # 30
my_list[[3]]        # c(95, 87)

# Data frame
df <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(30, 25, 35),
  score = c(95.5, 87.3, 92.1)
)

# Tibble (modern data frame)
library(tibble)
tbl <- tibble(
  name = c("Alice", "Bob", "Charlie"),
  age = c(30, 25, 35),
  score = c(95.5, 87.3, 92.1)
)

# Matrix
mat <- matrix(1:12, nrow = 3, ncol = 4)
mat[1, 2]             # element at row 1, col 2
mat[, "col1"]         # entire column

# Factors (categorical data)
status <- factor(c("low", "high", "medium", "low"),
                 levels = c("low", "medium", "high"),
                 ordered = TRUE)
```

---

## प्रवाह को नियंत्रित करें
```r
# if / else if / else
if (x > 0) {
  "positive"
} else if (x < 0) {
  "negative"
} else {
  "zero"
}

# Vectorized conditional
result <- ifelse(x > 0, "positive", "non-positive")

# for loop
for (i in 1:10) {
  print(i)
}

# Iterate over vector
for (item in my_vector) {
  process(item)
}

# while
while (condition) {
  do_something()
}

# repeat (infinite loop with break)
repeat {
  if (done()) break
  process()
}

# next (skip iteration)
for (i in 1:10) {
  if (i %% 2 == 0) next
  print(i)  # prints odd numbers
}
```

---

## कार्य
```r
# Basic function
add <- function(x, y) {
  x + y
}

# Default arguments
greet <- function(name, greeting = "Hello") {
  paste(greeting, name)
}

# Variadic arguments
custom_mean <- function(x, ...) {
  mean(x, na.rm = TRUE, ...)
}

# Return multiple values
describe <- function(x) {
  list(mean = mean(x), sd = sd(x), n = length(x))
}
result <- describe(c(1, 2, 3, 4, 5))
result$mean

# Anonymous functions (lambda)
sapply(1:5, function(x) x^2)

# Shorthand (R 4.1+)
sapply(1:5, \(x) x^2)

# Closures
make_counter <- function(start = 0) {
  count <- start
  function() {
    count <<- count + 1
    count
  }
}
counter <- make_counter()
counter()  # 1
counter()  # 2

# do.call — call function with list of arguments
do.call(paste, list("a", "b", "c", sep = "-"))  # "a-b-c"
```

---

## टिडीवर्स / डीपीएलआईआर
```r
library(dplyr)

# Pipe chain
result <- df %>%
  filter(age > 18) %>%
  mutate(
    age_group = cut(age, breaks = c(18, 30, 50, 100),
                    labels = c("young", "middle", "senior")),
    name_upper = toupper(name)
  ) %>%
  group_by(age_group) %>%
  summarize(
    n = n(),
    avg_score = mean(score, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  arrange(desc(avg_score))

# Key dplyr verbs
filter(df, condition)        # rows
select(df, col1, col2)       # columns
mutate(df, new_col = expr)   # add/modify columns
summarize(df, stat = expr)   # aggregate
arrange(df, col)             # sort
group_by(df, col)            # grouping
left_join(df1, df2, by = "key")  # join

# Across — apply function to multiple columns
df %>%
  summarize(across(where(is.numeric), mean, na.rm = TRUE))

df %>%
  mutate(across(starts_with("score_"), ~ .x / max(.x, na.rm = TRUE)))
```

---

## ggplot2 के साथ विज़ुअलाइज़ेशन
```r
library(ggplot2)

# Basic scatter plot
ggplot(mtcars, aes(x = wt, y = mpg, color = cyl)) +
  geom_point(size = 3) +
  geom_smooth(method = "lm") +
  facet_wrap(~gear) +
  labs(title = "Weight vs MPG", x = "Weight", y = "MPG") +
  theme_minimal()

# Bar chart
ggplot(diamonds, aes(x = cut, fill = color)) +
  geom_bar(position = "dodge") +
  coord_flip()

# Histogram + density
ggplot(data, aes(x = value)) +
  geom_histogram(aes(y = after_stat(density)), bins = 30) +
  geom_density(color = "red")

# Box plot
ggplot(data, aes(x = group, y = value, fill = group)) +
  geom_boxplot() +
  stat_summary(fun = mean, geom = "point", shape = 20, size = 3)

# Line chart with multiple series
ggplot(long_data, aes(x = date, y = value, color = series)) +
  geom_line() +
  geom_point(size = 1) +
  scale_x_date(date_labels = "%Y-%m") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

---

## सांख्यिकीय मॉडलिंग
```r
# Linear regression
model <- lm(mpg ~ wt + hp + cyl, data = mtcars)
summary(model)
confint(model)
predict(model, newdata = data.frame(wt = 3, hp = 150, cyl = 6))

# Logistic regression
logit <- glm(am ~ wt + hp, data = mtcars, family = binomial)
summary(logit)
predict(logit, type = "response")

# T-test
t.test(group1, group2)
t.test(value ~ group, data = df)

# ANOVA
anova_result <- aov(mpg ~ factor(cyl), data = mtcars)
summary(anova_result)
TukeyHSD(anova_result)

# Correlation
cor(df$x, df$y, method = "spearman")
cor.test(df$x, df$y)

# Principal Component Analysis
pca <- prcomp(df[, numeric_cols], scale = TRUE)
summary(pca)
biplot(pca)
```

---

## सारांश
आर का सिंटैक्स सांख्यिकीय कंप्यूटिंग और डेटा विश्लेषण के लिए डिज़ाइन किया गया है। संचालन की वेक्टरकृत प्रकृति अधिकांश कार्यों के लिए लूप को समाप्त कर देती है। टिडीवर्स इकोसिस्टम (dplyr, ggplot2, tidyr) डेटा हेरफेर और विज़ुअलाइज़ेशन के लिए एक सुसंगत, पठनीय व्याकरण प्रदान करता है। आर की सांख्यिकीय मॉडलिंग क्षमताएं - बुनियादी टी-परीक्षणों से लेकर मिश्रित-प्रभाव वाले मॉडल तक - गहराई में बेजोड़ हैं। डेटा विज्ञान, सांख्यिकी और प्रतिलिपि प्रस्तुत करने योग्य अनुसंधान के लिए, आर एक आवश्यक उपकरण बना हुआ है।