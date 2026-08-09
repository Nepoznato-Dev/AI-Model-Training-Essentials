---
# मेटाडेटा
शीर्षक: "आर"
विवरण: "आर प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [आर, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "31 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# आर
आर एक प्रोग्रामिंग भाषा और वातावरण है जिसे विशेष रूप से सांख्यिकीय कंप्यूटिंग और डेटा विश्लेषण के लिए डिज़ाइन किया गया है। 1993 में ऑकलैंड विश्वविद्यालय में रॉस इहाका और रॉबर्ट जेंटलमैन द्वारा बनाया गया (इसलिए "आर"), यह महत्वपूर्ण विस्तार के साथ एस भाषा का कार्यान्वयन है। R खुला स्रोत है और इसका रखरखाव R कोर टीम द्वारा किया जाता है। यह शिक्षा, स्वास्थ्य देखभाल, वित्त और सरकार में सांख्यिकीविदों, डेटा विश्लेषकों और शोधकर्ताओं के लिए मानक उपकरण है।
आर डेटा हेरफेर, सांख्यिकीय मॉडलिंग, विज़ुअलाइज़ेशन और रिपोर्टिंग में उत्कृष्टता प्राप्त करता है। इसके पैकेज इकोसिस्टम (CRAN) में 20,000 से अधिक पैकेज हैं जो अब तक तैयार की गई लगभग हर सांख्यिकीय पद्धति को कवर करते हैं।
---

## आर क्यों मायने रखता है
- **सांख्यिकीय कंप्यूटिंग**: किसी भी भाषा में सांख्यिकीय तरीकों का सबसे व्यापक संग्रह।
- **डेटा विज़ुअलाइज़ेशन**: ggplot2 प्रकाशन-गुणवत्ता वाले ग्राफ़िक्स तैयार करता है। ग्राफ़िक्स प्रतिमान का व्याकरण बेजोड़ है।
- **पुनरुत्पादित अनुसंधान**: आर मार्कडाउन / क्वार्टो आपको एक ही दस्तावेज़ में कोड, परिणाम और कथा को संयोजित करने देता है।
- **शैक्षणिक मानक**: सांख्यिकी, जैव सूचना विज्ञान, महामारी विज्ञान, पारिस्थितिकी, अर्थशास्त्र और सामाजिक विज्ञान में उपयोग किया जाता है।
- **टिडीवर्स**: पैकेजों का एक समेकित सेट (dplyr, ggplot2, tidyr, readr) जो डेटा विश्लेषण को सुरुचिपूर्ण और सुसंगत बनाता है।
- **निःशुल्क और खुला स्रोत**: कोई लाइसेंस शुल्क नहीं; वैश्विक समुदाय द्वारा सक्रिय रूप से बनाए रखा गया।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **प्रदर्शन** | डिफ़ॉल्ट रूप से सिंगल-थ्रेडेड; बड़े डेटासेट के लिए धीमा | C++ एकीकरण के लिए`data.table`, समानांतर पैकेज या Rcpp का उपयोग करें |
| **मेमोरी उपयोग** | संपूर्ण डेटासेट को RAM में लोड करता है | आउट-ऑफ-कोर प्रोसेसिंग के लिए `data.table::fread`, एरो पैकेज का उपयोग करें
| **सामान्य प्रयोजन वाली भाषा नहीं** | वेब डेवलपमेंट, सिस्टम प्रोग्रामिंग, या ऐप्स के लिए अजीब | गैर-सांख्यिकीय कार्यों के लिए पायथन, गो या जावास्क्रिप्ट का उपयोग करें |
| **असंगत वाक्यविन्यास** | बेस आर में विचित्रताएं हैं; विभिन्न पैकेज विभिन्न सम्मेलनों का उपयोग करते हैं | एकरूपता के लिए टिडीवर्स का प्रयोग करें |
| **नौकरी बाज़ार** | अधिकतर शैक्षणिक/अनुसंधान भूमिकाएँ | डेटा विज्ञान भूमिकाएँ तेजी से पायथन को पसंद कर रही हैं |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संचालन
```r
# Assignment
name <- "Alice"
age <- 30
scores <- c(9.5, 8.0, 7.5, 9.0)

# Vectors (the fundamental data structure)
numbers <- 1:10
letters_vec <- c("a", "b", "c")
logical_vec <- c(TRUE, FALSE, TRUE)

# Data frames (the workhorse for tabular data)
df <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(30, 25, 35),
  score = c(9.5, 8.0, 7.5)
)

# Access columns
df$name
df[, "age"]
df$score[df$age > 28]  # Scores where age > 28
```

### टिडीवर्स (आधुनिक आर)
```r
library(tidyverse)

# Read data
data <- read_csv("data.csv")

# Pipe operator (%>%) chains operations
result <- data %>%
  filter(age >= 18) %>%
  mutate(grade = case_when(
    score >= 90 ~ "A",
    score >= 80 ~ "B",
    score >= 70 ~ "C",
    TRUE ~ "F"
  )) %>%
  group_by(department) %>%
  summarise(
    avg_score = mean(score, na.rm = TRUE),
    count = n()
  ) %>%
  arrange(desc(avg_score))

# Native pipe (R 4.1+)
result <- data |>
  filter(age >= 18) |>
  mutate(grade = if_else(score >= 90, "A", "B"))
```

### ggplot2 के साथ विज़ुअलाइज़ेशन
```r
library(ggplot2)

# Scatter plot
ggplot(data = df, aes(x = age, y = score, colour = name)) +
  geom_point(size = 3) +
  labs(title = "Age vs Score", x = "Age", y = "Score") +
  theme_minimal()

# Histogram with facets
ggplot(data = survey_data, aes(x = income)) +
  geom_histogram(bins = 30, fill = "steelblue", colour = "white") +
  facet_wrap(~ education_level) +
  theme_bw()
```

### सांख्यिकीय मॉडलिंग
```r
# Linear regression
model <- lm(score ~ age + education + experience, data = df)
summary(model)
confint(model)

# Logistic regression
logit_model <- glm(passed ~ gpa + study_hours, data = students, family = binomial)

# ANOVA
anova_result <- aov(score ~ group, data = experiment_data)
TukeyHSD(anova_result)

# Principal Component Analysis
pca_result <- prcomp(scale(data_matrix))
plot(pca_result)
```

---

## उन्नत सिंटैक्स और पैटर्न
### S3 और S4 ऑब्जेक्ट सिस्टम
```r
# S3 classes (informal, most common)
new_person <- function(name, age) {
  structure(list(name = name, age = age), class = "person")
}

print.person <- function(x, ...) {
  cat("Person:", x$name, "| Age:", x$age, "\n")
}

p <- new_person("Alice", 30)
print(p)       # Uses print.person

# S4 classes (formal, with validation)
setClass("Matrix2x2",
  representation(data = "matrix"),
  validity = function(object) {
    if (!is.matrix(object@data) || !all(dim(object@data) == c(2, 2)))
      return("Matrix must be 2x2")
    TRUE
  }
)

setGeneric("determinant", function(x) standardGeneric("determinant"))
setMethod("determinant", "Matrix2x2", function(x) {
  d <- x@data
  d[1,1] * d[2,2] - d[1,2] * d[2,1]
})

m <- new("Matrix2x2", data = matrix(c(1, 3, 2, 4), nrow = 2))
determinant(m)  # -2
```

### R6 संदर्भ कक्षाएं
```r
library(R6)
Stack <- R6Class("Stack",
  private = list(data = list()),
  public = list(
    push = function(item) { private$data <- c(private$data, list(item)) },
    pop = function() {
      n <- length(private$data)
      if (n == 0) stop("Stack is empty")
      item <- private$data[[n]]
      private$data <- private$data[-n]
      item
    },
    size = function() length(private$data)
  )
)
s <- Stack$new()
s$push(10); s$push(20)
s$pop()    # 20
```

### गैर-मानक मूल्यांकन और मेटाप्रोग्रामिंग
```r
library(rlang)

# Quasiquotation
my_filter <- function(data, var, value) {
  var_expr <- enquo(var)
  data %>% filter(!!var_expr > value)
}
mtcars %>% my_filter(mpg, 25)

# Building expressions programmatically
expr <- expr(mean(!!sym("mpg"), na.rm = TRUE))
eval_tidy(expr, data = mtcars)
```

### ऑपरेटर ओवरलोडिंग
```r
`+.person` <- function(e1, e2) {
  if (inherits(e2, "person")) {
    new_person(paste(e1$name, "&", e2$name), (e1$age + e2$age) / 2)
  } else stop("Can only add two persons")
}
p1 <- new_person("Alice", 30); p2 <- new_person("Bob", 25)
p3 <- p1 + p2
p3$name  # "Alice & Bob"
```

---

## समवर्ती एवं समांतरता
### समानांतर पैकेज
```r
library(parallel)
n_cores <- detectCores()

# mclapply (Unix/macOS — fork-based)
results <- mclapply(1:100, function(i) {
  mean(rnorm(10000))
}, mc.cores = 4)

# parLapply (Windows-compatible — socket-based)
cl <- makeCluster(4)
results <- parLapply(cl, 1:100, function(i) {
  mean(rnorm(10000))
})
stopCluster(cl)
```

### भविष्य का पैकेज
```r
library(future); library(future.apply)
plan(multisession)

results <- future_lapply(1:1000, function(i) {
  summary(lm(mpg ~ wt, data = mtcars[sample(1:32, 20), ]))
})

# With purrr
library(purrr)
plan(multisession, workers = 4)
results <- future_map_dbl(1:100, ~ mean(rnorm(1000)))
```

### foreach/doParallel
```r
library(doParallel); library(foreach)
cl <- makeCluster(4)
registerDoParallel(cl)

results <- foreach(i = 1:100, .combine = rbind,
                   .packages = c("dplyr")) %dopar% {
  df <- data.frame(x = rnorm(100), y = rnorm(100))
  df %>% summarise(correlation = cor(x, y))
}
stopCluster(cl)
```

---

## परियोजना विन्यास एवं निर्माण प्रणाली
### पैकेज संरचना
```
myanalysis/
+-- DESCRIPTION           # Package metadata
+-- NAMESPACE             # Exports/imports (roxygen2)
+-- R/
|   +-- analysis.R
|   +-- plotting.R
+-- man/                  # Documentation (.Rd files)
+-- tests/testthat/
|   +-- test-analysis.R
+-- vignettes/
|   +-- introduction.Rmd
+-- renv.lock             # Dependency lock file
```

### विवरण फ़ाइल
```
Package: myanalysis
Title: Advanced Statistical Analysis Toolkit
Version: 0.2.1
Authors@R: person("Jane", "Doe", email = "jane@example.com",
    role = c("aut", "cre"))
License: MIT + file LICENSE
Depends: R (>= 4.1.0)
Imports: dplyr (>= 1.1.0), ggplot2, tidyr, rlang, purrr
Suggests: testthat (>= 3.0.0), knitr, rmarkdown
Config/testthat/edition: 3
```

### रेनव के साथ निर्भरता प्रबंधन
```r
renv::init()                    # Initialize renv
renv::snapshot()                # Capture exact versions
renv::restore()                 # Restore from lock file
renv::install("dplyr@1.1.0")   # Specific version
```

### GitHub क्रियाओं के साथ CI/CD
```yaml
name: R-CMD-check
on:
  push: {branches: [main]}
  pull_request: {branches: [main]}
jobs:
  R-CMD-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: r-lib/actions/setup-r@v2
      - uses: r-lib/actions/setup-r-dependencies@v2
        with: {extra-packages: any::rcmdcheck}
      - uses: r-lib/actions/check-r-package@v2
```

---

## परीक्षण
### उस ढांचे का परीक्षण करें
```r
library(testthat)

test_that("mean calculation works", {
  expect_equal(mean(c(1, 2, 3, 4, 5)), 3)
  expect_type(mean(1:100), "double")
})

test_that("normalize centers and scales", {
  x <- c(10, 20, 30, 40, 50)
  result <- normalize(x)
  expect_equal(mean(result), 0, tolerance = 1e-10)
  expect_equal(sd(result), 1, tolerance = 1e-10)
})

test_that("error handling works", {
  expect_error(log("a"), "non-numeric argument")
  expect_warning(log(-1), "NaN")
  expect_silent(1 + 1)
})

# Snapshot testing (testthat 3e)
test_that("output matches snapshot", {
  expect_snapshot(summary(lm(mpg ~ wt, data = mtcars)))
})

# Run: devtools::test() or R CMD check
# Coverage: covr::package_coverage()
```

---

## अंतरसंचालनीयता
### आरसीपीपी के साथ सी/सी++ एकीकरण
```r
library(Rcpp)

# Inline C++ function
cppFunction('
  double fast_mean(NumericVector x) {
    int n = x.size();
    double sum = 0.0;
    for (int i = 0; i < n; i++) sum += x[i];
    return sum / n;
  }
')
fast_mean(c(1.0, 2.0, 3.0, 4.0, 5.0))  # 3.0

# C++ with Rcpp sugar (vectorized)
cppFunction('
  NumericVector fast_normalize(NumericVector x) {
    double m = mean(x);
    double s = sd(x);
    return (x - m) / s;
  }
')
```

### आर से पायथन को कॉल करना
```r
library(reticulate)

np <- import("numpy")
pd <- import("pandas")
sklearn <- import("sklearn.linear_model")

arr <- np$array(c(1, 2, 3, 4, 5))
result <- np$mean(arr)

# Convert between R and Python
r_df <- data.frame(x = 1:5, y = c(2, 4, 5, 4, 5))
py_df <- r_to_py(r_df)
back_to_r <- py_to_r(py_df)

# Use scikit-learn
model <- sklearn$LinearRegression()
X <- np$array(matrix(c(1,2,3,4,5), ncol=1))
y <- np$array(c(2, 4, 5, 4, 5))
model$fit(X, y)
```

---

## डिज़ाइन पैटर्न
### पैटर्न 1: लचीले कार्यों के लिए सुव्यवस्थित मूल्यांकन
```r
library(rlang); library(dplyr)

compute_stats <- function(data, group_var, value_var) {
  group_var <- enquo(group_var)
  value_var <- enquo(value_var)
  data %>%
    group_by(!!group_var) %>%
    summarise(
      mean = mean(!!value_var, na.rm = TRUE),
      sd = sd(!!value_var, na.rm = TRUE),
      n = n(), .groups = "drop"
    )
}
mtcars %>% compute_stats(cyl, mpg)
```

### पैटर्न 2: गड़गड़ाहट के साथ कार्यात्मक प्रोग्रामिंग
```r
library(purrr)

# Map over grouped data
models <- mtcars %>%
  split(.$cyl) %>%
  map(~ lm(mpg ~ wt, data = .x))

models %>%
  map_dbl(~ summary(.x)$r.squared) %>%
  enframe(name = "cylinders", value = "r_squared")

# Safely handle errors
safe_log <- safely(log)
results <- map(c(1, -1, 10, "a"), safe_log)
results %>% keep(~ is.null(.x$error)) %>% map("result")
```

### पैटर्न 3: रिपोर्ट जनरेशन पाइपलाइन
```r
library(rmarkdown)

render_report <- function(data_path, output_dir, params) {
  rmarkdown::render(
    input = "templates/analysis.Rmd",
    output_dir = output_dir,
    params = params, quiet = TRUE
  )
}

groups <- unique(sales_data$region)
walk(groups, function(region) {
  render_report("data/sales.csv", "reports/",
    params = list(region = region, year = 2024))
})
```

---

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
```r
# Base R profiling
Rprof("profile.out")
result <- heavy_computation()
Rprof(NULL)
summaryRprof("profile.out")

# Line-by-line profiling
library(profvis)
profvis({
  df <- read_csv("large_data.csv")
  result <- df %>% group_by(category) %>%
    summarise(mean_val = mean(value))
})

# Microbenchmarking
library(microbenchmark)
microbenchmark(
  base_mean = mean(x),
  manual_sum = sum(x) / length(x),
  Rcpp_mean = fast_mean(x),
  times = 1000
)
```

### वेक्टरीकरण और डेटा.टेबल
```r
library(data.table)
dt <- as.data.table(mtcars)

# Fast aggregation (modifies by reference)
dt[, mean_mpg := mean(mpg), by = cyl]

# Fast grouping
result <- dt[, .(avg_mpg = mean(mpg), avg_hp = mean(hp),
  count = .N), by = .(cyl, gear)]

# fread — 10-100x faster than read.csv
data <- fread("large_file.csv", nThread = 4)

# Key-based joins (like database indexes)
setkey(dt, cyl)
dt[.(6)]  # Fast binary search lookup
```

### मेमोरी अनुकूलन
```r
# Monitor memory
cat("Memory (MB):", pryr::mem_used() / 1e6, "\n")

# arrow for out-of-core processing
library(arrow)
ds <- open_dataset("large_data/", format = "parquet")
result <- ds %>% filter(year >= 2020) %>%
  summarise(total = sum(revenue)) %>% collect()

# data.table set() modifies by reference (no copy)
for (j in 1:ncol(dt)) {
  set(dt, j = j, value = as.numeric(dt[[j]]))
}
gc()  # Force garbage collection
```

---

## तैनाती
### CRAN में पैकेज प्रकाशन
```r
devtools::check()
devtools::document()
devtools::build()
devtools::release()
```

### चमकदार अनुप्रयोग
```r
library(shiny)
ui <- fluidPage(
  sliderInput("n", "N:", 10, 1000, 100),
  plotOutput("histPlot")
)
server <- function(input, output) {
  output$histPlot <- renderPlot(hist(rnorm(input$n)))
}
shinyApp(ui, server)
```

### कंटेनर परिनियोजन
```dockerfile
FROM rocker/r-ver:4.3.2
COPY . /app/
RUN R CMD INSTALL /app
EXPOSE 3838
CMD ["R","-e","shiny::runApp('/app',port=3838)"]
```

---

## आर का उपयोग कब करें
| परिदृश्य | क्यों आर | बेहतर विकल्प |
|---|-------|-------------------|
| सांख्यिकीय विश्लेषण | सबसे व्यापक सांख्यिकीय विधियाँ | पायथन (स्टैट्समॉडल, स्काइपी) |
| डेटा विज़ुअलाइज़ेशन | ggplot2 प्रकाशन गुणवत्ता के मामले में बेजोड़ है | इंटरैक्टिव के लिए पायथन (मैटप्लोटलिब, सीबॉर्न) |
| अकादमिक शोध | कई क्षेत्रों में मानक | — |
| जैव सूचना विज्ञान | बायोकंडक्टर के पास 2,000+ विशेष पैकेज हैं | उत्पादन पाइपलाइनों के लिए पायथन |
| रिपोर्टिंग (आर मार्कडाउन/क्वार्टो) | एकीकृत विश्लेषण + कथा | ज्यूपिटर (पायथन) |
| उत्पादन एमएल सिस्टम | तैनाती के लिए डिज़ाइन नहीं किया गया | पायथन, जावा |
| वेब विकास | अनुकूल नहीं | जावास्क्रिप्ट, पायथन |
| बड़े पैमाने पर डेटा प्रोसेसिंग | स्मृति-बद्ध | पायथन (पाइस्पार्क), एसक्यूएल |
---

## सारांश
आर सांख्यिकी की भाषा है. डेटा विश्लेषण, विज़ुअलाइज़ेशन और सांख्यिकीय मॉडलिंग के लिए, यह गहराई और चौड़ाई में बेजोड़ है। टिडीवर्स ने भाषा का आधुनिकीकरण किया है, और आर मार्कडाउन/क्वार्टो ने प्रतिलिपि प्रस्तुत करने योग्य शोध को सरल बना दिया है। जबकि पायथन ने आम तौर पर डेटा विज्ञान में बढ़त हासिल कर ली है, आर कठोर सांख्यिकीय कार्य के लिए विशेषज्ञ का उपकरण बना हुआ है। मात्रात्मक शोध करने वाले किसी भी व्यक्ति के लिए, आर सीखना आवश्यक है।
---

## उन्नत डेटा गड़बड़ी
### डेटा.टेबल डीप डाइव
```r
library(data.table)

# Create data.table
dt <- data.table(
  id = 1:1000,
  group = rep(LETTERS[1:5], 200),
  value = rnorm(1000),
  category = sample(c("X", "Y", "Z"), 1000, replace = TRUE)
)

# Chained operations
result <- dt[group == "A" & value > 0,
  .(mean_val = mean(value), count = .N),
  by = category][order(-mean_val)]

# Rolling joins
dt1 <- data.table(time = c(1, 5, 10, 15), val = c("a", "b", "c", "d"))
dt2 <- data.table(time = c(2, 7, 12))
dt1[dt2, on = "time", roll = "nearest"]

# Non-equi joins
dt1[dt2, on = .(time >= time)]

# Update by reference (no copy)
dt[, new_col := value * 2]
dt[value < 0, value := NA]
```

### साफ सुथरा और गतिशील कॉलम
```r
library(dplyr)
library(rlang)

# Programmatic column access
my_col <- "mpg"
mtcars %>% select(all_of(my_col))

# Dynamic summarise
compute_summary <- function(data, group, measure) {
  data %>%
    group_by(across({{ group }})) %>%
    summarise(across({{ measure }}, list(
      mean = mean,
      sd = sd,
      median = median
    ), .names = "{.col}_{.fn}"))
}

mtcars %>% compute_summary(cyl, mpg)

# Across multiple columns
mtcars %>%
  summarise(across(where(is.numeric), list(
    mean = mean, sd = sd
  ), .names = "{.col}_{.fn}"))
```

---

## सांख्यिकीय मॉडलिंग डीप डाइव
### उन्नत प्रतिगमन
```r
# Mixed-effects models
library(lme4)
model <- lmer(score ~ age + experience + (1 | department), data = df)
summary(model)
ranef(model)  # Random effects

# Generalised additive models
library(mgcv)
gam_model <- gam(y ~ s(x1) + s(x2) + factor(group), data = df)
summary(gam_model)
plot(gam_model)

# Survival analysis
library(survival)
cox_model <- coxph(Surv(time, status) ~ age + treatment, data = patients)
summary(cox_model)
survfit_obj <- survfit(Surv(time, status) ~ treatment, data = patients)
plot(survfit_obj, col = c("blue", "red"))

# Bayesian inference
library(rstanarm)
bayes_model <- stan_glm(mpg ~ wt + hp, data = mtcars, family = gaussian)
summary(bayes_model)
plot(posterior_vs_prior(bayes_model))
```

### समय श्रृंखला विश्लेषण
```r
# ARIMA models
library(forecast)
ts_data <- ts(rnorm(120, mean = 100, sd = 10), frequency = 12)
arima_model <- auto.arima(ts_data)
forecast_vals <- forecast(arima_model, h = 12)
plot(forecast_vals)

# Decomposition
decomp <- decompose(ts_data)
plot(decomp)

# Exponential smoothing
ets_model <- ets(ts_data)
forecast(ets_model, h = 12)
```

### साफ-सुथरे मॉडल के साथ मशीन लर्निंग
```r
library(tidymodels)

# Define recipe (preprocessing)
recipe_obj <- recipe(mpg ~ ., data = mtcars) %>%
  step_normalize(all_numeric_predictors()) %>%
  step_corr(all_numeric_predictors(), threshold = 0.8)

# Define model specification
model_spec <- linear_reg() %>% set_engine("lm")

# Create workflow
wf <- workflow() %>%
  add_recipe(recipe_obj) %>%
  add_model(model_spec)

# Train with cross-validation
folds <- vfold_cv(mtcars, v = 10)
cv_results <- fit_resamples(wf, resamples = folds,
  metrics = metric_set(rmse, rsq, mae))
collect_metrics(cv_results)

# Final fit and predict
final_fit <- fit(wf, data = mtcars)
predict(final_fit, new_data = mtcars[1:5, ])
```
