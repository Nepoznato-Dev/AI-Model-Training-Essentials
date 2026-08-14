---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# रूबी - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| 0.95 | 1995 | आरंभिक रिलीज़ (युकिहिरो "मात्ज़" मात्सुमोतो) |
| 1.0 | 1996 | पहली स्थिर रिलीज़ |
| 1.2 | 1998 | पहला अंग्रेजी दस्तावेज़ीकरण |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | कचरा संग्रहण में सुधार |
| 1.8 | 2003 | $KCODE, ओनिगुरुमा रेगेक्स इंजन |
| 1.9 | 2007 | **प्रमुख**: M17N (बहुभाषी), नया हैश सिंटैक्स, फ़ाइबर |
| 2.0 | 2013 | कीवर्ड तर्क,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | परिष्कृत विधि कॉल,`frozen_string_literal`|
| 2.2 | 2014 | प्रतीक जीसी, वृद्धिशील जीसी |
| 2.3 | 2015 | फ्रोजन स्ट्रिंग शाब्दिक प्रगति,`&.`सुरक्षित नेविगेशन |
| 2.4 | 2016 | `Integer`एकीकृत,`String`यूनिकोड केस मैपिंग |
| 2.5 | 2017 |  `yield_self`,`rescue`/`ensure`में ब्लॉक |
| 2.6 | 2018 | **JIT कंपाइलर (MJIT)**, अंतहीन रेंज`1..`|
| 2.7 | 2019 | पैटर्न मिलान (प्रायोगिक), क्रमांकित ब्लॉक पैरामीटर |
| 3.0 | 2020 | **प्रमुख**: रेक्टर (संगामिति), फाइबर शेड्यूलर, आरबीएस प्रकार |
| 3.1 | 2021 | `Anonymous`ब्लॉक अग्रेषण,`Hash#compact`|
| 3.2 | 2022 | `Data`वर्ग,`File.realpath`सुधार, YJIT उत्पादन |
| 3.3 | 2023 | **YJIT** प्रमुख सुधार,`it`ब्लॉक पैरामीटर |
| 3.4 | 2024 | प्रिज्म पार्सर डिफ़ॉल्ट,`it`डिफ़ॉल्ट ब्लॉक परम के रूप में |
## प्रमुख मील के पत्थर
### अर्ली रूबी (1995-2003)
- **1995**: मैट्ज़ ने पर्ल, स्मॉलटॉक, लिस्प को मिलाकर रूबी बनाई
- **1.0 (1996)**: पहली स्थिर रिलीज़
- **1.8 (2003)**: "क्लासिक" रूबी - तेज़, स्थिर, व्यापक रूप से अपनाया गया
### द रेल्स एरा (2004-2013)
- **2004**: रूबी ऑन रेल्स जारी - वेब विकास क्रांति
- **1.9 (2007)**: M17N (बहुभाषी स्ट्रिंग्स), नया हैश सिंटैक्स `{key: value}`, फ़ाइबर
- **2.0 (2013)**: कीवर्ड तर्क, आलसी गणनाकार, `Module#prepend`
### मॉडर्न रूबी (2015-वर्तमान)
- **2.6 (2018)**: जेआईटी कंपाइलर (एमजेआईटी) - पहला प्रदर्शन पुश
- **2.7 (2019)**: पैटर्न मिलान (प्रयोगात्मक), क्रमांकित ब्लॉक पैरामीटर`_1`
- **3.0 (2020)**: **रैक्टर** (अभिनेता-मॉडल संगामिति), **फाइबर शेड्यूलर** (async I/O), **आरबीएस** (हस्ताक्षर टाइप करें)
- **3.2 (2022)**:`Data`वर्ग (अपरिवर्तनीय मूल्य वस्तुएं), YJIT उत्पादन के लिए तैयार
- **3.3 (2023)**: YJIT प्रमुख स्पीडअप (3x तक तेज),`it`ब्लॉक पैरामीटर
- **3.4 (2024)**: प्रिज्म पार्सर डिफ़ॉल्ट हो जाता है
## प्रदर्शन विकास
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## समवर्ती विकास
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## पैटर्न मिलान विकास
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## पारिस्थितिकी तंत्र का विकास
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
