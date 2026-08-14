<!--
---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# الصدأ - تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | تاريخ الإصدار | الموضوع الرئيسي |
|---------|------------|-----------|
| 0.1 | يناير 2012 | المترجم الأول (rustc)، التزامن القائم على المهام |
| 0.5 | 2012 | نظام الكتابة القائم على السمات يتشكل |
| 0.6 | 2012 | إزالة الصناديق المُدارة`@`|
| 0.7 | 2013 |  تمت إزالة `@`،`~`للصناديق المملوكة |
| 0.8 | 2013 | التعليقات التوضيحية مدى الحياة،`&mut`|
| 0.9 | يناير 2014 | التنظيف النهائي قبل 1.0 |
| 0.10 | فبراير 2014 | الإصدار الأخير قبل 1.0 |
| 0.11 | أبريل 2014 | `Box<T>`يستبدل`~T`|
| 0.12 | مايو 2014 |  تبدأ إعادة كتابة وحدة`io`|
| 1.0 | 15 مايو 2015 | **إصدار مستقر** — "Rust 1.0" |
| 1.10 | أغسطس 2016 |  انتشار الخطأ`?`(مثل`try!`→`?`) |
| 1.15 | فبراير 2017 | أول صدأ على الإسطبل باستخدام`impl Trait`الإعدادية |
| 1.18 | يونيو 2017 |  `pub(crate)`، التجميع التزايدي |
| 1.20 | أكتوبر 2017 | الثوابت المرتبطة |
| 1.26 | مايو 2018 | `impl Trait`في موضع الوسيطة/الإرجاع |
| 1.28 | سبتمبر 2018 | المخصصون العالميون |
| 1.31 | ديسمبر 2018 | **إصدار Rust 2018** — الوحدات النمطية،`dyn Trait`|
| 1.34 | أبريل 2019 | السجلات البديلة |
| 1.39 | نوفمبر 2019 | `async/await`على مستقر |
| 1.44 | يوليو 2020 | تحسينات التشخيص |
| 1.51 | أبريل 2021 |  الأدوية العامة`const`(MVP) |
| 1.56 | أكتوبر 2021 | **إصدار Rust 2021** — عمليات الإغلاق، IntoIterator |
| 1.59 | فبراير 2022 | التجميع المضمن |
| 1.62 | يونيو 2022 | `#[default]`للتعدادات |
| 1.65 | ديسمبر 2022 | `let else`|
| 1.68 | مارس 2023 |  `#[ffi_pure]`، التحسين الموجه بالملف الشخصي |
| 1.70 | يونيو 2023 | تبعيات`crates.io`المعزولة |
| 1.74 | نوفمبر 2023 | وضع الشحن دون اتصال |
| 1.76 | فبراير 2024 | **إصدار Rust 2024** — كتل `gen`،`unsafe extern`|
| 1.79 | يونيو 2024 | `LazyCell`,`LazyLock`|
| 1.82 | أكتوبر 2024 | `unsafe`في كتل`extern`مطلوبة |
| 1.85 | فبراير 2025 | استقرت نسخة الصدأ 2024 |
## المعالم الرئيسية
### ما قبل الإصدار 1.0 (2010-2015)
- **2010**: مشروع Graydon Hoare الجانبي في Mozilla يكتسب زخمًا
- **2012**: أول مترجم عام؛ يخضع نظام الكتابة لإعادة تصميم كبيرة
- **2013**: تبلور نموذج الملكية؛  تمت إزالة صناديق `@`
- **2014**: إضفاء الطابع الرسمي على عملية Rust RFC؛ المجتمع ينمو
- **2015**: **1.0** — ضمان الاستقرار؛ "تجريدات بدون تكلفة"
### سنوات النمو (2015-2019)
- **2015**: أصبح Cargo هو مدير الحزم القياسي
- **2018**: **Rust 2018 Edition** — إصلاح نظام الوحدة النمطية،`dyn Trait`،`impl Trait`
- **2019**: وصول`async/await`إلى نظام بيئي مستقر وغير متزامن
### النضج (2020 إلى الوقت الحاضر)
- **2021**: **Rust 2021 Edition** — إزالة الغموض عن الحقول في عمليات الإغلاق،`IntoIterator`للمصفوفات
- **2024**: **إصدار Rust 2024** — كتل `gen`، متطلبات `unsafe extern`
- **2025**: صدأ في بنية Linux kernel وAndroid وWindows وAWS
## نظام الإصدار
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## تطور الملكية
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## التطور غير المتزامن
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## نمو النظام البيئي
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## طلبات RFC الرئيسية
| آر إف سي | سنة | ميزة |
|------|------|---------|
| 25 | 2013 | مطابقة الأنماط |
| 153 | 2014 |  نوع`Result`|
| 217 | 2014 |  مشغل`?`(محاولة) |
| 460 | 2016 | `?`يستبدل`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | الصدأ طبعة 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 |  الأدوية`const`|
| 3013 | 2020 | التحقق من التجميع الشرطي |
| 3517 | 2023 |  كتل`gen`|