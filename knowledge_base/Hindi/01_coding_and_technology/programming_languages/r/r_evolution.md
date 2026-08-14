---
# Metadata
title: "R — Version History & Evolution"
description: "Comprehensive version history and evolution of R from S-Plus origins to modern R."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [r, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# आर - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| एस | 1976 | बेल लैब्स (बेकर, चेम्बर्स, विल्क्स) में बनाई गई एस भाषा |
| एस-प्लस | 1988 | वाणिज्यिक एस कार्यान्वयन (स्टेटसाइंस) |
| आर 0.10 | 1995 | पहली आर रिलीज़ (इहाका एंड जेंटलमैन, ऑकलैंड) |
| आर 1.0 | 2000 | **पहली स्थिर रिलीज़** |
| आर 1.4 | 2002 | S4 कक्षाएं और विधियाँ |
| आर 2.0 | 2004 | रेगुलर एक्सप्रेशन,`R.home()`|
| आर 2.1 | 2005 | यूटीएफ-8 समर्थन |
| आर 2.5 | 2007 | मेमोरी प्रबंधन में सुधार |
| आर 2.8 | 2008 | संदर्भ कक्षाएं (प्रारंभिक ओओपी) |
| आर 2.14 | 2011 |  `loadNamespace`, समानांतर पैकेज |
| आर 2.15 | 2012 | `stringsAsFactors = FALSE`विकल्प |
| आर 3.0 | 2013 | **64-बिट समर्थन**, संदर्भ वर्ग स्थिर |
| आर 3.1 | 2014 | `vapply`सुधार |
| आर 3.2 | 2015 | `readRDS`/ `saveRDS`, नमूना सुधार |
| आर 3.3 | 2016 | `xz`संपीड़न,`person()`सुधार |
| आर 3.4 | 2017 | समानांतर क्रमांकन,`switch`सुधार |
| आर 3.5 | 2018 | डिफ़ॉल्ट`stringsAsFactors`चेतावनी |
| आर 3.6 | 2019 | यादृच्छिक संख्या जनरेटर में सुधार |
| आर 4.0 | 2020 | **प्रमुख**:`stringsAsFactors = FALSE`डिफ़ॉल्ट |
| आर 4.1 | 2021 | **पाइप`|>`**, अनाम फ़ंक्शन`\(x) ...`|
| आर 4.2 | 2022 | `|>`को`on.exit`में प्लेसहोल्डर `_`,`after`तर्क प्राप्त हुआ |
| आर 4.3 | 2023 | `R_cmd`सुधार, बेहतर त्रुटि संदेश |
| आर 4.4 | 2024 | `find()`सुधार,`deparse1()`डिफ़ॉल्ट |
| आर 4.5 | 2025 | निरंतर सुधार |
## प्रमुख मील के पत्थर
### एस और एस-प्लस (1976-1994)
- **1976**: जॉन चैम्बर्स ने बेल लैब्स में एस बनाया - एक भाषा के रूप में सांख्यिकीय प्रोग्रामिंग
- **1988**: एस-प्लस - स्टेटसाइंस द्वारा वाणिज्यिक कार्यान्वयन (बाद में टीआईबीसीओ)
- एस परिचय: डेटा फ्रेम, सूत्र (`y ~ x`), आलसी मूल्यांकन
### आर का जन्म (1995-2000)
- **1995**: रॉस इहाका और रॉबर्ट जेंटलमैन ने ऑकलैंड विश्वविद्यालय में आर बनाया
- "आर" = रॉस और रॉबर्ट का पहला अक्षर
- एक मुफ़्त, ओपन-सोर्स एस कार्यान्वयन के रूप में डिज़ाइन किया गया
- **2000**: आर 1.0 — पहली स्थिर रिलीज़; सीआरएएन (कॉम्प्रिहेंसिव आर आर्काइव नेटवर्क) की स्थापना की गई
### आर परिपक्व (2000-2012)
- **1.4 (2002)**: एस4 कक्षाएं - औपचारिक ओओपी प्रणाली
- **2.0 (2004)**: नियमित अभिव्यक्ति, बेहतर आंतरिक
- **2.8 (2008)**: संदर्भ कक्षाएं - प्रारंभिक आधुनिक ओओपी
- **2.14 (2011)**:`parallel`पैकेज (मल्टीकोर सपोर्ट)
### आर 3.एक्स - डेटा साइंस युग (2013-2019)
- **3.0 (2013)**: 64-बिट समर्थन - बड़े डेटासेट को संभालें
- **3.1–3.6**: वृद्धिशील सुधार
- **2013-2015**: "आर रेवोल्यूशन" - जीजीप्लॉट2, डीपीएलआईआर, टिडीवर्स ट्रांसफॉर्म डेटा साइंस
### आर 4.एक्स - मॉडर्न आर (2020–मौजूदा)
- **4.0 (2020)**:`stringsAsFactors = FALSE`डिफ़ॉल्ट रूप से - दशकों पुराने दर्द बिंदु को ठीक करता है
- **4.1 (2021)**: **नेटिव पाइप`|>`**, अनाम फ़ंक्शन शॉर्टहैंड`\(x) x + 1`
- **4.2 (2022)**: पाइप प्लेसहोल्डर `_`,`\(x, y)`शॉर्टहैंड स्थिर
- **4.3 (2023)**: बेहतर त्रुटि संदेश (सुधार सुझाते हैं)
- **4.4–4.5**: निरंतर परिशोधन
## सिंटेक्स इवोल्यूशन
```r
# S / early R: Basic statistics
x <- c(1, 2, 3, 4, 5)
mean(x)
lm(y ~ x, data = df)

# R 3.x: tidyverse revolution (2013+)
library(dplyr)
library(ggplot2)
df %>%
  filter(age > 18) %>%
  group_by(category) %>%
  summarise(mean_age = mean(age))

# R 4.0: stringsAsFactors default changes
df <- read.csv("data.csv")  # strings no longer auto-converted to factors

# R 4.1: Native pipe and lambda shorthand
df |>
  filter(age > 18) |>
  mutate(label = \(x) paste(x$name, x$age))

# R 4.2: Pipe placeholder
result |> (\(x) x[is.na(x)] <- 0)()
# With placeholder:
x |> f(y = _)

# R 4.3+: Better error messages
mean("hello")
# Warning: In mean.default("hello") : argument is not numeric or logical: returning NA
```

## पैकेज इकोसिस्टम इवोल्यूशन
```
1995: R launches with basic stats packages
2000: CRAN established — centralized package repository
2001: Bioconductor — bioinformatics packages
2007: ggplot2 released (Hadley Wickham) — grammar of graphics
2008: reshape2 — data reshaping
2012: dplyr released — fast data manipulation
2014: tidyr, readr — complete data science toolkit
2015: tidyverse meta-package — unified ecosystem
2016: RMarkdown — literate programming
2019: Quarto — next-gen documents
2020: RStudio → Posit — company rebrands, broader tooling
2025: 20,000+ packages on CRAN; R is the #1 statistical language
```

## ओओपी विकास
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## पारिस्थितिकी तंत्र का विकास
```
1995: R created at University of Auckland
2000: CRAN established — package repository
2003: Bioconductor — bioinformatics ecosystem
2007: ggplot2 — revolutionizes data visualization
2012: dplyr — modern data manipulation
2014: tidyverse — unified data science toolkit
2015: RMarkdown — reproducible research
2020: R 4.0 — modern defaults
2021: R 4.1 — native pipe |>
2025: R remains dominant in statistics, bioinformatics, and academia
       20,000+ CRAN packages; used by pharma, finance, research
```
