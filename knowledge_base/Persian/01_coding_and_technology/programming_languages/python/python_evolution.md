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

# Python - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | تاریخ انتشار | تم کلید |
|---------|-------------|-----------|
| 1.0 | ژانویه 1994 | انتشار اولیه |
| 1.5 | دسامبر 1997 | کلاس ها، استثناها، ماژول ها |
| 2.0 | اکتبر 2000 | درک فهرست، جمع آوری زباله |
| 2.2 | دسامبر 2001 | انواع یکپارچه (انواع/کلاس ها)، ژنراتور |
| 2.5 | سپتامبر 2006 |  عبارت `with`،`yield`به عنوان عبارت |
| 2.6 | اکتبر 2008 |  واردات `bytes`، `future`، انتقال به 3 |
| 2.7 | جولای 2010 | درک دیکت/مجموعه،`argparse`|
| 3.0 | دسامبر 2008 | **شکستن**:`print()`,`str`/`bytes`, تکرار کننده |
| 3.3 | سپتامبر 2012 |  `yield from`، بسته های فضای نام |
| 3.4 | مارس 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | سپتامبر 2015 |  `async/await`، نکات نوع (PEP 484)، باز کردن بسته بندی`**`|
| 3.6 | دسامبر 2016 | f-strings,`async`compreh, ordered dicts |
| 3.7 | ژوئن 2018 | `dataclasses`,`contextvars`, رزرو شده`async`|
| 3.8 | اکتبر 2019 | اپراتور Walrus `:=`، پارامترهای فقط موقعیتی |
| 3.9 | اکتبر 2020 | دیکت اتحادیه`|`, انواع ژنریک`list[int]`|
| 3.10 | اکتبر 2021 |  `match/case`، تطبیق الگوی ساختاری |
| 3.11 | اکتبر 2022 | گروه های استثنایی، نوع `Self`، CPython سریعتر |
| 3.12 | اکتبر 2023 | آماده سازی GIL برای هر مترجم، نحو پارامتر نوع |
| 3.13 | اکتبر 2024 | حالت رشته آزاد (تجربی)، بهبود یافته REPL |
| 3.14 | اکتبر 2025 | بدون GIL پایدار، ارزیابی معوق حاشیه نویسی |
## نقاط عطف اصلی
### Python 2.x Era (2000–2020)
- **2.0**: فهرستی از مفاهیم الهام گرفته از هاسکل. GC حلقوی
- **2.2**: کلاس پایه `object`؛  کلمه کلیدی`yield`(مولدها)
- **2.5**: بیانیه `with`؛ `yield`تبدیل به بیان می شود
- **2.7**: نسخه نهایی 2.x. دیکته درک. `argparse`
- **پایان عمر**: 1 ژانویه 2020
### Python 3.x Revolution (2008–اکنون)
- **3.0**: Clean break —`print`به عنوان تابع،`str`در مقابل `bytes`، همه تکرار کننده ها نماها را برمی گرداند
- **3.5**: نحو`async`/ `await`؛ نکات را با ماژول`typing`تایپ کنید
- **3.6**: رشته های f (ویژگی درخواستی ترین)؛ `asyncio`تثبیت شد
- **3.8**: اپراتور Walrus برای انتساب درون خطی
- **3.10**: تطبیق الگوی ساختاری (`match` / `case`)
- **3.11**: 10-60٪ سریعتر؛ گروه های استثنایی با`except*`
- **3.13**: حالت آزاد تجربی (بدون GIL)
## تکامل فلسفه طراحی
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP های کلیدی که پایتون را شکل دادند
| PEP | سال | ویژگی |
|------|------|---------|
| 20 | 2004 | ذن پایتون |
| 257 | 2001 | قراردادهای مستندسازی |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | عبارات مولد |
| 342 | 2005 | `yield`به عنوان عبارت،`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | نکات تایپ |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | رشته های f |
| 572 | 2018 | اپراتور Walrus`:=`|
| 622 | 2020 | تطبیق الگوی ساختاری |
| 654 | 2021 | گروه های استثنایی |
| 684 | 2022 | هر مترجم GIL |
| 703 | 2023 | اختیاری کردن GIL |
## تکامل عملکرد
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## رشد جامعه و اکوسیستم
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
