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
# برو - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | تاریخ انتشار | تم کلید |
|---------|-------------|-----------|
| 1.0 | مارس 2012 | اولین انتشار پایدار |
| 1.1 | می 2013 | عملکرد، آشکارساز مسابقه |
| 1.3 | ژوئن 2014 | نظرسنجی شبکه، رمزنگاری/tls |
| 1.4 | دسامبر 2014 | بوت استرپ با Go (خود میزبانی) |
| 1.5 | آگوست 2015 | **GC همزمان**، نوشتن موانع |
| 1.7 | آگوست 2016 |  بسته `context`، خرده آزمون های`testing`|
| 1.8 | فوریه 2017 |  `http.Server.Shutdown`، افزونه ها |
| 1.9 | آگوست 2017 | نام مستعار را تایپ کنید، موازی`make`|
| 1.10 | فوریه 2018 |  استخر اتصال`database/sql`|
| 1.11 | آگوست 2018 | **به ماژول ها**،`go mod`|
| 1.12 | فوریه 2019 | TLS 1.3، نسخه ماژول |
| 1.13 | سپتامبر 2019 | `errors.Is/As`, اعداد بالفظ`0b`,`0o`|
| 1.14 | فوریه 2020 | **ورودی/خروجی همپوشانی در ویندوز**، پیش‌دستی کلی |
| 1.15 | آگوست 2020 |  بازنشانی`time.Ticker`/ `Timer`، پراکسی ماژول |
| 1.16 | فوریه 2021 |  بسته `embed`، `io/fs`، ماژول آگاه به طور پیش فرض |
| 1.17 | آگوست 2021 | تبدیل قطعه به آرایه،`unsafe.Slice`|
| 1.18 | مارس 2022 | **عمومی**، fuzzing، فضاهای کاری |
| 1.19 | آگوست 2022 | نظرات سند، بازنگری مدل حافظه |
| 1.20 | فوریه 2023 |  `errors.Join`، بهینه سازی هدایت شده توسط پروفایل |
| 1.21 | آگوست 2023 | **`slog`**، توکار `min/max`،`maps/slices`|
| 1.22 | فوریه 2024 | محدوده بیش از اعداد صحیح، مسیریابی پیشرفته |
| 1.23 | آگوست 2024 | بسته Iterator (`iter`) ، تغییرات تایمر |
| 1.24 | فوریه 2025 |  بسته `weak`، نقشه های بهبود یافته |
## نقاط عطف اصلی
### آغاز (2009–2012)
- **2009**: Go توسط گوگل اعلام شد (رابرت گریزمر، راب پایک، کن تامپسون)
- **2012**: **Go 1.0** — "وعده سازگاری Go 1"
### عملکرد و ابزار (2012–2018)
- **1.1**: 30%+ بهبود عملکرد؛ آشکارساز مسابقه
- **1.5**: زباله جمع کننده همزمان (مکث GC از میلی ثانیه به میکروثانیه کاهش می یابد)
- **1.5**: Go compiler bootstrapped - نوشته شده در Go (دیگر C نیست)
- **1.7**: بسته`context`استاندارد می شود
### ماژول ها و اکوسیستم (2018–2021)
- **1.11**: **به ماژول ها** — مدیریت وابستگی رسمی
- **1.13**:`errors.Is/As`- بسته بندی خطا اصطلاحی می شود
- **1.16**: بسته`embed`- جاسازی فایل ها در زمان کامپایل
### مدرن برو (2022–اکنون)
- **1.18**: **عمومی** — نوع پارامترها با محدودیت
- **1.21**:`slog`- ورود ساختار یافته در stdlib.  داخلی های `min/max`
- **1.22**: محدوده بیش از اعداد صحیح (`for i := range 10`)
- **1.23**: بسته Iterator - ارزیابی تنبل در stdlib
## سفر ژنریک
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## فلسفه رسیدگی به خطا
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## تکامل همزمان
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

## Go Compatibility Promise
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

## رشد اکوسیستم
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## تکامل عملکرد
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
