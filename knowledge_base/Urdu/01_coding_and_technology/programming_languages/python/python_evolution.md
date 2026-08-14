---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# ازگر - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | ریلیز کی تاریخ | کلیدی تھیم |
|---------|------------|------------|
| 1.0 | جنوری 1994 | ابتدائی ریلیز |
| 1.5 | دسمبر 1997 | کلاسز، مستثنیات، ماڈیولز |
| 2.0 | اکتوبر 2000 | فہم کی فہرست، کوڑا کرکٹ جمع کرنا |
| 2.2 | دسمبر 2001 | متحد اقسام (قسم/کلاسز)، جنریٹرز |
| 2.5 | ستمبر 2006 | `with`بیان،`yield`اظہار کے طور پر |
| 2.6 | اکتوبر 2008 | `bytes`,`future`درآمدات، 3 میں منتقلی |
| 2.7 | جولائی 2010 | ڈکٹ/سیٹ فہم،`argparse`|
| 3.0 | دسمبر 2008 | **بریکنگ**:`print()`,`str`/`bytes`, تکرار کرنے والے |
| 3.3 | ستمبر 2012 | `yield from`, نام کی جگہ پیکیجز |
| 3.4 | مارچ 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | ستمبر 2015 |  `async/await`، قسم کے اشارے (PEP 484)،`**`پیک کھولنا |
| 3.6 | دسمبر 2016 | f-strings,`async`compreh, آرڈر شدہ حکم |
| 3.7 | جون 2018 | `dataclasses`,`contextvars`, محفوظ`async`|
| 3.8 | اکتوبر 2019 | والرس آپریٹر`:=`, صرف پوزیشنی پیرامز |
| 3.9 | اکتوبر 2020 | Dict یونین`|`, عام اقسام`list[int]`|
| 3.10 | اکتوبر 2021 | `match/case`, ساختی پیٹرن کی مماثلت |
| 3.11 | اکتوبر 2022 | استثنائی گروپ،`Self`قسم، تیز تر CPython |
| 3.12 | اکتوبر 2023 | فی مترجم GIL پریپ، ٹائپ پیرامیٹر نحو |
| 3.13 | اکتوبر 2024 | فری تھریڈڈ موڈ (تجرباتی)، بہتر REPL |
| 3.14 | اکتوبر 2025 | No-GIL مستحکم، تشریحات کی موخر تشخیص |
## اہم سنگ میل
### Python 2.x Era (2000–2020)
- **2.0**: ہاسکل سے متاثر فہمیوں کی فہرست؛ سائیکلک جی سی
- **2.2**:`object`بیس کلاس؛ `yield`مطلوبہ لفظ (جنریٹرز)
- **2.5**:`with`بیان؛ `yield`اظہار بن جاتا ہے۔
- **2.7**: فائنل 2.x ریلیز؛ ڈکٹ فہمیاں؛ `argparse`
- **زندگی کا اختتام**: یکم جنوری 2020
### Python 3.x Revolution (2008–موجودہ)
- **3.0**: کلین بریک —`print`بطور فنکشن،`str`بمقابلہ `bytes`، تمام تکرار کرنے والے آراء واپس کرتے ہیں
- **3.5**:`async`/`await`نحو؛`typing`ماڈیول کے ساتھ اشارے ٹائپ کریں۔
- **3.6**: f-strings (سب سے زیادہ درخواست کردہ خصوصیت)؛ `asyncio`مستحکم
- **3.8**: ان لائن اسائنمنٹ کے لیے والرس آپریٹر
- **3.10**: ساختی پیٹرن کی مماثلت (`match` / `case`)
- **3.11**: 10-60% تیز؛`except*`کے ساتھ استثنائی گروپ 
- **3.13**: تجرباتی فری تھریڈڈ موڈ (کوئی GIL نہیں)
## ڈیزائن فلسفہ ارتقاء
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## کلیدی PEPs جنہوں نے ازگر کی شکل دی۔
| پی ای پی | سال | خصوصیت |
|------|------|---------|
| 20 | 2004 | Zen of Python |
| 257 | 2001 | Docstring کنونشنز |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | جنریٹر اظہار |
| 342 | 2005 | `yield`اظہار کے طور پر،`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | قسم کے اشارے |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-strings |
| 572 | 2018 | والرس آپریٹر`:=`|
| 622 | 2020 | ساختی پیٹرن کے ملاپ |
| 654 | 2021 | استثنائی گروپس |
| 684 | 2022 | فی مترجم GIL |
| 703 | 2023 | GIL کو اختیاری بنانا |
## کارکردگی کا ارتقا
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## کمیونٹی اور ایکو سسٹم کی نمو
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
