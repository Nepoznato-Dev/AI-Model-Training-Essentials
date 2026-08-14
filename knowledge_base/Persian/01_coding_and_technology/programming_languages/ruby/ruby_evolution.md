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
# روبی - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 0.95 | 1995 | انتشار اولیه (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | اولین انتشار پایدار |
| 1.2 | 1998 | اولین مستندات انگلیسی |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | بهبود جمع آوری زباله |
| 1.8 | 2003 | $KCODE، موتور regex oniguruma |
| 1.9 | 2007 | ** عمده **: M17N (چند زبانه)، نحو جدید هش، فیبرها |
| 2.0 | 2013 | آرگومان های کلیدواژه`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | فراخوانی روش تصفیه شده،`frozen_string_literal`|
| 2.2 | 2014 | نماد GC، GC افزایشی |
| 2.3 | 2015 | رشته منجمد پراگما، ناوبری ایمن`&.`|
| 2.4 | 2016 | `Integer`یکپارچه،`String`نقشه برداری یونیکد |
| 2.5 | 2017 | `yield_self`, بلوک در`rescue`/`ensure`|
| 2.6 | 2018 | **کامپایلر JIT (MJIT)**، محدوده بی پایان`1..`|
| 2.7 | 2019 | تطبیق الگو (تجربی)، پارامترهای بلوک شماره‌دار |
| 3.0 | 2020 | **رشته**: راکتور (همزمان)، فیبر زمانبند، انواع RBS |
| 3.1 | 2021 |  حمل و نقل بلوک `Anonymous`،`Hash#compact`|
| 3.2 | 2022 | `Data`کلاس، بهبود `File.realpath`، تولید YJIT |
| 3.3 | 2023 | **YJIT** بهبودهای عمده، پارامتر بلوک`it`|
| 3.4 | 2024 | پیش فرض تجزیه کننده منشور،`it`به عنوان پارامتر بلوک پیش فرض |
## نقاط عطف اصلی
### یاقوت اولیه (1995-2003)
- **1995**: Matz Ruby را ایجاد می کند - Perl، Smalltalk، Lisp را ترکیب می کند.
- **1.0 (1996)**: اولین نسخه پایدار
- **1.8 (2003)**: یاقوت "کلاسیک" - سریع، پایدار، به طور گسترده پذیرفته شده است
### عصر ریل (2004–2013)
- **2004**: Ruby on Rails منتشر شد - انقلاب توسعه وب
- **1.9 (2007)**: M17N (رشته های چند زبانه)، نحو هش جدید `{key: value}`، فیبرها
- **2.0 (2013)**: آرگومان های کلیدواژه، شمارشگرهای تنبل، `Module#prepend`
### روبی مدرن (2015–اکنون)
- **2.6 (2018)**: کامپایلر JIT (MJIT) — اولین فشار عملکرد
- **2.7 (2019)**: تطبیق الگو (تجربی)، پارامترهای بلوک شماره گذاری شده`_1`
- **3.0 (2020)**: **Ractor** (همزمان بازیگر-مدل)، **Fiber Scheduler** (I/O غیرهمگام)، **RBS** (امضای نوع)
- **3.2 (2022)**: کلاس`Data`(اشیاء ارزش تغییرناپذیر)، آماده تولید YJIT
- **3.3 (2023)**: افزایش سرعت اصلی YJIT (تا 3 برابر سریعتر)، پارامتر بلوک `it`
- **3.4 (2024)**: تجزیه کننده منشور پیش فرض می شود
## تکامل عملکرد
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

## تکامل همزمان
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## تکامل تطبیق الگو
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## اصول کلیدی طراحی
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## رشد اکوسیستم
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
