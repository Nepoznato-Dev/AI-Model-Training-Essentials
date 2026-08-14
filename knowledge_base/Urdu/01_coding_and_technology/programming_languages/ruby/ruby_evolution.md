<!--
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

-->
# روبی - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 0.95 | 1995 | ابتدائی ریلیز (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | پہلی مستحکم رہائی |
| 1.2 | 1998 | پہلی انگریزی دستاویزات |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | کوڑا اٹھانے میں بہتری |
| 1.8 | 2003 | $KCODE، oniguruma regex انجن |
| 1.9 | 2007 | **میجر**: M17N (کثیر لسانی)، نیا ہیش نحو، فائبرز |
| 2.0 | 2013 | مطلوبہ الفاظ کے دلائل،`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | بہتر طریقہ کالز،`frozen_string_literal`|
| 2.2 | 2014 | علامت GC، اضافہ GC |
| 2.3 | 2015 | منجمد سٹرنگ لفظی پراگما،`&.`محفوظ نیویگیشن |
| 2.4 | 2016 | `Integer`متحد،`String`یونیکوڈ کیس میپنگ |
| 2.5 | 2017 | `yield_self`,`rescue`/`ensure`میں بلاکس |
| 2.6 | 2018 | **JIT کمپائلر (MJIT)**، لامتناہی رینج`1..`|
| 2.7 | 2019 | پیٹرن کی مماثلت (تجرباتی)، نمبر والے بلاک پیرامز |
| 3.0 | 2020 | **میجر**: ریکٹر (کنکرنسی)، فائبر شیڈیولر، آر بی ایس کی اقسام |
| 3.1 | 2021 | `Anonymous`بلاک فارورڈنگ،`Hash#compact`|
| 3.2 | 2022 | `Data`کلاس،`File.realpath`بہتری، YJIT پیداوار |
| 3.3 | 2023 | **YJIT** اہم بہتری،`it`بلاک پیرامیٹر |
| 3.4 | 2024 | پریزم پارسر ڈیفالٹ،`it`بطور ڈیفالٹ بلاک پیرام |
## اہم سنگ میل
### ابتدائی روبی (1995–2003)
- **1995**: میٹز روبی تخلیق کرتا ہے - پرل، سمال ٹاک، لِسپ کو ملانا
- **1.0 (1996): پہلی مستحکم ریلیز
- **1.8 (2003)**: "کلاسک" روبی — تیز، مستحکم، وسیع پیمانے پر اپنایا گیا
### ریل کا دور (2004–2013)
- **2004**: روبی آن ریلز جاری - ویب ڈویلپمنٹ انقلاب
- **1.9 (2007)**: M17N (کثیر لسانی تار)، نیا ہیش نحو `{key: value}`، فائبرز
- **2.0 (2013): کلیدی الفاظ کے دلائل، سست شمار کنندگان، `Module#prepend`
### ماڈرن روبی (2015–موجودہ)
- **2.6 (2018)**: جے آئی ٹی کمپائلر (MJIT) - پہلا پرفارمنس پش
- **2.7 (2019)**: پیٹرن کی مماثلت (تجرباتی)، نمبر والے بلاک پیرامز`_1`
- **3.0 (2020)**: **ریکٹر** (ایکٹر ماڈل کنکرنسی)، **فائبر شیڈیولر** (async I/O)، **RBS** (قسم کے دستخط)
- **3.2 (2022)**:`Data`کلاس (غیر متغیر ویلیو آبجیکٹ)، YJIT پروڈکشن کے لیے تیار
- **3.3 (2023)**: YJIT اہم اسپیڈ اپس (3x تک تیز)،`it`بلاک پیرامیٹر
- **3.4 (2024)**: پرزم پارسر ڈیفالٹ ہو جاتا ہے۔
## کارکردگی کا ارتقا
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

## ہم آہنگی ارتقاء
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## پیٹرن مماثل ارتقاء
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## ڈیزائن کے کلیدی اصول
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## ماحولیاتی نظام کی نمو
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
