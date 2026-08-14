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
# রুবি — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 0.95 | 1995 | প্রাথমিক প্রকাশ (ইউকিহিরো "ম্যাটজ" মাতসুমোতো) |
| 1.0 | 1996 | প্রথম স্থিতিশীল মুক্তি |
| 1.2 | 1998 | প্রথম ইংরেজি ডকুমেন্টেশন |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | আবর্জনা সংগ্রহের উন্নতি |
| 1.8 | 2003 | $KCODE, oniguruma regex ইঞ্জিন |
| 1.9 | 2007 | **মেজর**: M17N (বহুভাষিক), নতুন হ্যাশ সিনট্যাক্স, ফাইবার |
| 2.0 | 2013 | কীওয়ার্ড আর্গুমেন্ট,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | পরিমার্জিত পদ্ধতি কল,`frozen_string_literal`|
| 2.2 | 2014 | প্রতীক GC, ক্রমবর্ধমান GC |
| 2.3 | 2015 | হিমায়িত স্ট্রিং আক্ষরিক pragma,`&.`নিরাপদ নেভিগেশন |
| 2.4 | 2016 | `Integer`ইউনিফাইড,`String`ইউনিকোড কেস ম্যাপিং |
| 2.5 | 2017 | `yield_self`,`rescue`/`ensure`এ ব্লক
| 2.6 | 2018 | **JIT কম্পাইলার (MJIT)**, অন্তহীন পরিসর`1..`|
| 2.7 | 2019 | প্যাটার্ন ম্যাচিং (পরীক্ষামূলক), সংখ্যাযুক্ত ব্লক প্যারাম |
| 3.0 | 2020 | **মেজর**: র্যাক্টর (একসঙ্গে), ফাইবার শিডিউলার, আরবিএস প্রকার |
| 3.1 | 2021 | `Anonymous`ব্লক ফরওয়ার্ডিং,`Hash#compact`|
| 3.2 | 2022 | `Data`ক্লাস,`File.realpath`উন্নতি, YJIT উৎপাদন |
| 3.3 | 2023 | **YJIT** বড় উন্নতি,`it`ব্লক প্যারামিটার |
| 3.4 | 2024 | প্রিজম পার্সার ডিফল্ট, ডিফল্ট ব্লক প্যারাম হিসাবে`it`|
## প্রধান মাইলফলক
### প্রারম্ভিক রুবি (1995-2003)
- **1995**: ম্যাটজ রুবি তৈরি করে — পার্ল, স্মলটক, লিস্পকে মিশ্রিত করে
- **1.0 (1996): প্রথম স্থিতিশীল প্রকাশ
- **1.8 (2003)**: "ক্লাসিক" রুবি — দ্রুত, স্থিতিশীল, ব্যাপকভাবে গৃহীত
### দ্য রেল যুগ (2004-2013)
- **2004**: রুবি অন রেল প্রকাশিত হয়েছে — ওয়েব ডেভেলপমেন্ট বিপ্লব
- **1.9 (2007): M17N (বহুভাষিক স্ট্রিং), নতুন হ্যাশ সিনট্যাক্স`{key: value}`, ফাইবার
- **2.0 (2013): কীওয়ার্ড আর্গুমেন্ট, অলস গণনাকারী, `Module#prepend`
### আধুনিক রুবি (2015-বর্তমান)
- **2.6 (2018): JIT কম্পাইলার (MJIT) — প্রথম পারফরম্যান্স পুশ
- **2.7 (2019)**: প্যাটার্ন ম্যাচিং (পরীক্ষামূলক), নম্বরযুক্ত ব্লক প্যারামগুলি`_1`
- **3.0 (2020)**: **র্যাক্টর** (অভিনেতা-মডেল সঙ্গতি), **ফাইবার শিডিউলার** (অ্যাসিঙ্ক I/O), **RBS** (টাইপ স্বাক্ষর)
- **3.2 (2022)**:`Data`ক্লাস (অপরিবর্তনীয় মানের বস্তু), YJIT উৎপাদনের জন্য প্রস্তুত
- **3.3 (2023)**: YJIT প্রধান গতি (3x দ্রুততর পর্যন্ত),`it`ব্লক প্যারামিটার
- **3.4 (2024): প্রিজম পার্সার ডিফল্ট হয়ে যায়
## কর্মক্ষমতা বিবর্তন
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

## কনকারেন্সি বিবর্তন
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## প্যাটার্ন ম্যাচিং বিবর্তন
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## মূল ডিজাইনের নীতি
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## ইকোসিস্টেম বৃদ্ধি
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
