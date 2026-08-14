<!--
---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# بايثون — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | تاريخ الإصدار | الموضوع الرئيسي |
|---------|------------|-----------|
| 1.0 | يناير 1994 | الإصدار الأولي |
| 1.5 | ديسمبر 1997 | الفئات والاستثناءات والوحدات |
| 2.0 | أكتوبر 2000 | قائمة الفهم وجمع القمامة |
| 2.2 | ديسمبر 2001 | الأنواع الموحدة (أنواع/فئات)، المولدات |
| 2.5 | سبتمبر 2006 |  عبارة `with`،`yield`كتعبير |
| 2.6 | أكتوبر 2008 |  واردات `bytes`، `future`، الانتقال إلى 3 |
| 2.7 | يوليو 2010 | الإملاء/مجموعة الفهم،`argparse`|
| 3.0 | ديسمبر 2008 | **الفاصل**:`print()`,`str`/`bytes`, التكرارات |
| 3.3 | سبتمبر 2012 | `yield from`حزم مساحة الاسم |
| 3.4 | مارس 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | سبتمبر 2015 |  `async/await`، اكتب تلميحات (PEP 484)، تفريغ`**`|
| 3.6 | ديسمبر 2016 | f-strings،`async`فهم، الإملاءات المطلوبة |
| 3.7 | يونيو 2018 | `dataclasses`,`contextvars`, محفوظة`async`|
| 3.8 | أكتوبر 2019 | مشغل Walrus `:=`، المعلمات الموضعية فقط |
| 3.9 | أكتوبر 2020 | Dict union`|`, الأنواع العامة`list[int]`|
| 3.10 | أكتوبر 2021 |  `match/case`، مطابقة النمط الهيكلي |
| 3.11 | أكتوبر 2022 | مجموعات الاستثناء، نوع `Self`، أسرع CPython |
| 3.12 | أكتوبر 2023 | إعداد GIL لكل مترجم، اكتب بناء جملة المعلمة |
| 3.13 | أكتوبر 2024 | وضع الخيوط الحرة (تجريبي)، تحسين REPL |
| 3.14 | أكتوبر 2025 | No-GIL تقييم مستقر ومؤجل للتعليقات التوضيحية |
## المعالم الرئيسية
### عصر بايثون 2.x (2000-2020)
- **2.0**: قائمة بالمفاهيم المستوحاة من هاسكل؛ GC دوري
- **2.2**: الفئة الأساسية `object`؛  الكلمة الأساسية`yield`(المولدات)
- **2.5**: بيان `with`؛  يصبح`yield`تعبيرًا
- **2.7**: الإصدار 2.x النهائي؛ إملاء الفهم. `argparse`
- **نهاية الحياة**: 1 يناير 2020
### ثورة بايثون 3.x (2008 إلى الوقت الحاضر)
- **3.0**: فاصل نظيف —`print`كدالة،`str`مقابل `bytes`، جميع التكرارات تعيد المشاهدات
- **3.5**: بناء الجملة`async`/ `await`؛ اكتب تلميحات باستخدام وحدة `typing`
- **3.6**: f-strings (الميزة الأكثر طلبًا)؛  استقر `asyncio`
- **3.8**: مشغل Walrus للمهمة المضمنة
- **3.10**: مطابقة الأنماط الهيكلية (`match`/`case`)
- **3.11**: أسرع بنسبة 10-60%؛ مجموعات الاستثناء مع`except*`
- **3.13**: الوضع التجريبي الحر (بدون GIL)
## تطور فلسفة التصميم
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## الشخصيات الرئيسية التي شكلت لغة بايثون
| بيب | سنة | ميزة |
|------|------|---------|
| 20 | 2004 | زن بايثون |
| 257 | 2001 | اتفاقيات Docstring |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | تعبيرات المولد |
| 342 | 2005 | `yield`كتعبير،`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | اكتب تلميحات |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | سلاسل f |
| 572 | 2018 | مشغل الفظ`:=`|
| 622 | 2020 | مطابقة الأنماط الهيكلية |
| 654 | 2021 | مجموعات الاستثناء |
| 684 | 2022 | لكل مترجم فوري GIL |
| 703 | 2023 | جعل GIL اختياريًا |
## تطور الأداء
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## نمو المجتمع والنظام البيئي
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
