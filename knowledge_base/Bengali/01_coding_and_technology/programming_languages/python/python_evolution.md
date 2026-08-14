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
# পাইথন — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | মুক্তির তারিখ | মূল থিম |
|---------|---------------|------------|
| 1.0 | জানুয়ারী 1994 | প্রাথমিক প্রকাশ |
| 1.5 | ডিসেম্বর 1997 | ক্লাস, ব্যতিক্রম, মডিউল |
| 2.0 | অক্টোবর 2000 | তালিকা বোঝা, আবর্জনা সংগ্রহ |
| 2.2 | ডিসেম্বর 2001 | একীভূত প্রকার (প্রকার/শ্রেণী), জেনারেটর |
| 2.5 | সেপ্টেম্বর 2006 | `with`স্টেটমেন্ট, এক্সপ্রেশন হিসাবে`yield`|
| 2.6 | অক্টোবর 2008 | `bytes`,`future`আমদানি, 3 তে রূপান্তর |
| 2.7 | জুলাই 2010 | ডিক্ট/সেট কম্প্রিহেনশন,`argparse`|
| 3.0 | ডিসেম্বর 2008 | **ব্রেকিং**:`print()`,`str`/`bytes`, পুনরাবৃত্তিকারী |
| 3.3 | সেপ্টেম্বর 2012 | `yield from`, নেমস্পেস প্যাকেজ |
| 3.4 | মার্চ 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | সেপ্টেম্বর 2015 | `async/await`, টাইপ ইঙ্গিত (PEP 484),`**`আনপ্যাকিং |
| 3.6 | ডিসেম্বর 2016 | f-স্ট্রিংস,`async`compreh, আদেশকৃত নির্দেশাবলী |
| 3.7 | জুন 2018 | `dataclasses`,`contextvars`, সংরক্ষিত`async`|
| 3.8 | অক্টোবর 2019 | ওয়ালরাস অপারেটর`:=`, অবস্থানগত-শুধু প্যারামস |
| 3.9 | অক্টোবর 2020 | ডিক্ট ইউনিয়ন`|`, জেনেরিক প্রকার`list[int]`|
| 3.10 | অক্টোবর 2021 | `match/case`, স্ট্রাকচারাল প্যাটার্ন ম্যাচিং |
| 3.11 | অক্টোবর 2022 | ব্যতিক্রম গোষ্ঠী,`Self`প্রকার, দ্রুত CPython |
| 3.12 | অক্টোবর 2023 | প্রতি-দোভাষী GIL প্রিপ, টাইপ প্যারামিটার সিনট্যাক্স |
| 3.13 | অক্টোবর 2024 | ফ্রি-থ্রেডেড মোড (পরীক্ষামূলক), উন্নত REPL |
| 3.14 | অক্টোবর 2025 | No-GIL স্থিতিশীল, টীকাগুলির মূল্যায়ন বিলম্বিত |
## প্রধান মাইলফলক
### Python 2.x Era (2000–2020)
- **2.0**: হাস্কেল দ্বারা অনুপ্রাণিত বোঝার তালিকা; চক্রাকার GC
- **2.2**:`object`বেস ক্লাস; `yield`কীওয়ার্ড (জেনারেটর)
- **2.5**:`with`স্টেটমেন্ট; `yield`এক্সপ্রেশনে পরিণত হয়
- **2.7**: চূড়ান্ত 2.x প্রকাশ; dict বোধগম্যতা; `argparse`
- **জীবনের সমাপ্তি**: জানুয়ারী 1, 2020
### পাইথন 3.x বিপ্লব (2008-বর্তমান)
- **3.0**: ক্লিন ব্রেক —`print`ফাংশন হিসাবে,`str`বনাম`bytes`, সমস্ত পুনরাবৃত্তিকারী ভিউ প্রদান করে
- **3.5**:`async`/`await`সিনট্যাক্স;`typing`মডিউল দিয়ে ইঙ্গিত টাইপ করুন
- **3.6**: f-স্ট্রিং (সবচেয়ে অনুরোধ করা বৈশিষ্ট্য); `asyncio`স্থিতিশীল
- **3.8**: ইনলাইন অ্যাসাইনমেন্টের জন্য ওয়ালরাস অপারেটর
- **3.10**: স্ট্রাকচারাল প্যাটার্ন ম্যাচিং (`match` / `case`)
- **3.11**: 10-60% দ্রুত;`except*`সহ ব্যতিক্রম গোষ্ঠী 
- **3.13**: পরীক্ষামূলক ফ্রি-থ্রেডেড মোড (কোনও জিআইএল নেই)
## ডিজাইন দর্শন বিবর্তন
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## মূল PEPগুলি যা পাইথনকে আকৃতি দেয়
| পিইপি | বছর | বৈশিষ্ট্য |
|------|------|---------|
| 20 | 2004 | Python এর জেন |
| 257 | 2001 | ডকস্ট্রিং কনভেনশন |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | জেনারেটর এক্সপ্রেশন |
| 342 | 2005 |  এক্সপ্রেশন হিসাবে `yield`,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | টাইপ ইঙ্গিত |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-স্ট্রিংস |
| 572 | 2018 | ওয়ালরাস অপারেটর`:=`|
| 622 | 2020 | স্ট্রাকচারাল প্যাটার্ন ম্যাচিং |
| 654 | 2021 | ব্যতিক্রম গ্রুপ |
| 684 | 2022 | প্রতি-দোভাষী GIL |
| 703 | 2023 | GIL ঐচ্ছিক করা |
## কর্মক্ষমতা বিবর্তন
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## সম্প্রদায় এবং ইকোসিস্টেম বৃদ্ধি
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
