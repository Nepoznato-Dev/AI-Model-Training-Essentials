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
# Go — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | تاريخ الإصدار | الموضوع الرئيسي |
|---------|------------|-----------|
| 1.0 | مارس 2012 | أول إصدار مستقر |
| 1.1 | مايو 2013 | الأداء، كاشف السباق |
| 1.3 | يونيو 2014 | استطلاع الشبكة، التشفير/TLS |
| 1.4 | ديسمبر 2014 | Bootstrap مع Go (استضافة ذاتية) |
| 1.5 | أغسطس 2015 | **GC المتزامنة**، حواجز الكتابة |
| 1.7 | أغسطس 2016 |  حزمة `context`، اختبارات`testing`الفرعية |
| 1.8 | فبراير 2017 |  `http.Server.Shutdown`، الإضافات |
| 1.9 | أغسطس 2017 | اكتب الأسماء المستعارة، بالتوازي مع`make`|
| 1.10 | فبراير 2018 |  تجمع اتصال`database/sql`|
| 1.11 | أغسطس 2018 | **وحدات Go**،`go mod`|
| 1.12 | فبراير 2019 | TLS 1.3، إصدار الوحدة |
| 1.13 | سبتمبر 2019 | `errors.Is/As`, الأرقام الحرفية`0b`,`0o`|
| 1.14 | فبراير 2020 | **الإدخال/الإخراج المتراكب على نظام التشغيل Windows**، الإجراءات الوقائية اللازمة |
| 1.15 | أغسطس 2020 |  إعادة تعيين`time.Ticker`/ `Timer`، وكيل الوحدة |
| 1.16 | فبراير 2021 |  حزمة `embed`، `io/fs`، مدركة للوحدة بشكل افتراضي |
| 1.17 | أغسطس 2021 | تحويل شريحة إلى صفيف،`unsafe.Slice`|
| 1.18 | مارس 2022 | **الأدوية العامة**، التشويش، مساحات العمل |
| 1.19 | أغسطس 2022 | تعليقات الوثيقة، مراجعة نموذج الذاكرة |
| 1.20 | فبراير 2023 |  `errors.Join`، التحسين الموجه بالملف الشخصي |
| 1.21 | أغسطس 2023 | **`slog`**،`min/max`المدمج،`maps/slices`|
| 1.22 | فبراير 2024 | النطاق على الأعداد الصحيحة، التوجيه المحسن |
| 1.23 | أغسطس 2024 | حزمة Iterator (`iter`) ، تغييرات المؤقت |
| 1.24 | فبراير 2025 |  حزمة `weak`، خرائط محسنة |
## المعالم الرئيسية
### البداية (2009-2012)
- **2009**: أعلنت Google عن Go (روبرت غريسمير، روب بايك، كين طومسون)
- **2012**: **Go 1.0** — "وعد التوافق مع Go 1"
### الأداء والأدوات (2012-2018)
- **1.1**: 30%+ تحسن في الأداء؛ كاشف السباق
- **1.5**: أداة تجميع البيانات المهملة المتزامنة (تنخفض فترات توقف GC مؤقتًا من المللي ثانية إلى الميكروثانية)
- **1.5**: تم تشغيل مترجم Go - مكتوب بلغة Go (لا مزيد من لغة C)
- **1.7**: أصبحت حزمة`context`قياسية
### الوحدات والنظام البيئي (2018-2021)
- **1.11**: **وحدات Go** — إدارة التبعية الرسمية
- **1.13**:`errors.Is/As`— يصبح التفاف الأخطاء اصطلاحيًا
- **1.16**: حزمة`embed`- تضمين الملفات في وقت الترجمة
### مودرن جو (2022 إلى الوقت الحاضر)
- **1.18**: **الأدوية العامة** — اكتب المعلمات مع القيود
- **1.21**:`slog`— تسجيل منظم في stdlib؛  بنيات `min/max`
- **1.22**: النطاق على الأعداد الصحيحة (`for i := range 10`)
- **1.23**: حزمة التكرار — التقييم البطيء في stdlib
## رحلة الأدوية الجنيسة
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## فلسفة التعامل مع الأخطاء
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## تطور التزامن
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

## اذهب إلى وعد التوافق
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

## نمو النظام البيئي
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## تطور الأداء
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
