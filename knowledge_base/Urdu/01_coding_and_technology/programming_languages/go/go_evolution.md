<!--
---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# جاؤ - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | ریلیز کی تاریخ | کلیدی تھیم |
|---------|------------|------------|
| 1.0 | مارچ 2012 | پہلی مستحکم رہائی |
| 1.1 | مئی 2013 | کارکردگی، ریس پکڑنے والا |
| 1.3 | جون 2014 | نیٹ ورک پولنگ، crypto/tls |
| 1.4 | دسمبر 2014 | گو کے ساتھ بوٹسٹریپ (سیلف ہوسٹنگ) |
| 1.5 | اگست 2015 | **کنکرنٹ GC**، رکاوٹیں لکھیں |
| 1.7 | اگست 2016 | `context`پیکیج،`testing`ذیلی ٹیسٹ |
| 1.8 | فروری 2017 | `http.Server.Shutdown`, پلگ انز |
| 1.9 | اگست 2017 | قسم کے عرفی نام، متوازی`make`|
| 1.10 | فروری 2018 | `database/sql`کنکشن پول |
| 1.11 | اگست 2018 | **گو ماڈیولز**،`go mod`|
| 1.12 | فروری 2019 | TLS 1.3، ماڈیول ورژننگ |
| 1.13 | ستمبر 2019 | `errors.Is/As`, نمبر لٹریلز`0b`,`0o`|
| 1.14 | فروری 2020 | **ونڈوز پر اوورلیپڈ I/O**، گوروٹین پریمپشن |
| 1.15 | اگست 2020 | `time.Ticker`/`Timer`ری سیٹ، ماڈیول پراکسی |
| 1.16 | فروری 2021 | `embed`پیکیج، `io/fs`، ماڈیول سے آگاہی بذریعہ ڈیفالٹ |
| 1.17 | اگست 2021 | سلائس سے صف میں تبدیلی،`unsafe.Slice`|
| 1.18 | مارچ 2022 | **جنرک**، مبہم، ورک اسپیس |
| 1.19 | اگست 2022 | دستاویز کے تبصرے، میموری ماڈل پر نظر ثانی |
| 1.20 | فروری 2023 |  `errors.Join`، پروفائل گائیڈڈ آپٹیمائزیشن |
| 1.21 | اگست 2023 | **`slog`**،`min/max`بلٹ ان،`maps/slices`|
| 1.22 | فروری 2024 | انٹیجرز پر رینج، بہتر روٹنگ |
| 1.23 | اگست 2024 | Iterator (`iter`) پیکیج، ٹائمر تبدیلیاں |
| 1.24 | فروری 2025 | `weak`پیکیج، بہتر نقشے |
## اہم سنگ میل
### The Beginning (2009–2012)
- **2009**: گوگل نے اعلان کیا (رابرٹ گریزیمر، روب پائیک، کین تھامسن)
- **2012**: **Go 1.0** — "The Go 1 مطابقت کا وعدہ"
### کارکردگی اور ٹولنگ (2012–2018)
- **1.1**: 30%+ کارکردگی میں بہتری؛ ریس پکڑنے والا
- **1.5**: ہم آہنگی کوڑا اٹھانے والا (GC ملی سیکنڈ سے مائیکرو سیکنڈ تک گرنے کو روکتا ہے)
- **1.5**: Go compiler bootstrapped — Go میں لکھا گیا (مزید C نہیں)
- **1.7**:`context`پیکیج معیاری ہو جاتا ہے۔
### ماڈیولز اور ایکو سسٹم (2018–2021)
- **1.11**: **گو ماڈیولز** — سرکاری انحصار کا انتظام
- **1.13**:`errors.Is/As`— غلطی کو لپیٹنا محاورہ بن جاتا ہے
- **1.16**:`embed`پیکیج — مرتب وقت پر فائلوں کو سرایت کریں
### ماڈرن گو (2022–موجودہ)
- **1.18**: **Generics** — رکاوٹوں کے ساتھ پیرامیٹرز ٹائپ کریں۔
- **1.21**:`slog`— stdlib میں ساختی لاگنگ؛ `min/max`بلٹ ان
- **1.22**: عدد سے زیادہ رینج (`for i := range 10`)
- **1.23**: Iterator پیکیج — stdlib میں سست تشخیص
## عام سفر
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## فلسفہ سے نمٹنے میں غلطی
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## ہم آہنگی ارتقاء
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## مطابقت کا وعدہ کریں۔
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## ماحولیاتی نظام کی نمو
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## کارکردگی کا ارتقا
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
