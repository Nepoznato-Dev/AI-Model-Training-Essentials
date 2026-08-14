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
# زنگ - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | ریلیز کی تاریخ | کلیدی تھیم |
|---------|------------|------------|
| 0.1 | جنوری 2012 | پہلا مرتب کرنے والا (rustc)، ٹاسک پر مبنی کنکرنسی |
| 0.5 | 2012 | خاصیت پر مبنی قسم کا نظام شکل اختیار کرتا ہے |
| 0.6 | 2012 |`@`کے زیر انتظام خانوں کو ہٹانا |
| 0.7 | 2013 | `@`کو ہٹا دیا گیا،`~`ملکیت والے خانوں کے لیے |
| 0.8 | 2013 | تاحیات تشریحات،`&mut`|
| 0.9 | جنوری 2014 | فائنل پری 1.0 صفائی |
| 0.10 | فروری 2014 | آخری پری 1.0 ریلیز |
| 0.11 | اپریل 2014 | `Box<T>``~T` کی جگہ لے لیتا ہے |
| 0.12 | مئی 2014 | `io`ماڈیول دوبارہ لکھنا شروع ہوتا ہے |
| 1.0 | 15 مئی 2015 | **مستحکم ریلیز** — "Rust 1.0" |
| 1.10 | اگست 2016 | `?`خرابی کی تبلیغ (بطور`try!`→`?`) |
| 1.15 | فروری 2017 |`impl Trait`پریپ کے ساتھ مستحکم پر پہلا زنگ |
| 1.18 | جون 2017 | `pub(crate)`, اضافی تالیف |
| 1.20 | اکتوبر 2017 | وابستہ مستقل |
| 1.26 | مئی 2018 | `impl Trait`دلیل/واپسی پوزیشن میں |
| 1.28 | ستمبر 2018 | عالمی مختص کرنے والے |
| 1.31 | دسمبر 2018 | **زنگ 2018 ایڈیشن** — ماڈیولز،`dyn Trait`|
| 1.34 | اپریل 2019 | متبادل رجسٹریاں |
| 1.39 | نومبر 2019 | `async/await`مستحکم پر |
| 1.44 | جولائی 2020 | تشخیصی بہتری |
| 1.51 | اپریل 2021 | `const`generics (MVP) |
| 1.56 | اکتوبر 2021 | **رسٹ 2021 ایڈیشن** — بندشیں، IntoIterator |
| 1.59 | فروری 2022 | ان لائن اسمبلی |
| 1.62 | جون 2022 | `#[default]`enums کے لیے |
| 1.65 | دسمبر 2022 | `let else`|
| 1.68 | مارچ 2023 |  `#[ffi_pure]`، پروفائل گائیڈڈ آپٹیمائزیشن |
| 1.70 | جون 2023 | الگ تھلگ`crates.io`انحصار |
| 1.74 | نومبر 2023 | کارگو آف لائن موڈ |
| 1.76 | فروری 2024 | **رسٹ 2024 ایڈیشن** —`gen`بلاکس،`unsafe extern`|
| 1.79 | جون 2024 | `LazyCell`,`LazyLock`|
| 1.82 | اکتوبر 2024 | `unsafe`میں`extern`بلاکس کی ضرورت ہے |
| 1.85 | فروری 2025 | مورچا 2024 ایڈیشن مستحکم |
## اہم سنگ میل
### پری-1.0 (2010–2015)
- **2010**: Mozilla میں Graydon Hoare کے سائیڈ پروجیکٹ نے توجہ حاصل کی۔
- **2012**: پہلا عوامی مرتب؛ قسم کا نظام بڑے نئے ڈیزائن سے گزرتا ہے۔
- **2013**: ملکیت کا ماڈل کرسٹلائز کرتا ہے۔ `@`بکس ہٹا دیے گئے۔
- **2014**: مورچا RFC عمل کو باقاعدہ بنا دیا گیا؛ کمیونٹی بڑھتی ہے
- **2015**: **1.0** — استحکام کی ضمانت؛ "صفر لاگت خلاصہ"
### ترقی کے سال (2015–2019)
- **2015**: کارگو معیاری پیکیج مینیجر بن جاتا ہے۔
- **2018**: **رسٹ 2018 ایڈیشن** — ماڈیول سسٹم اوور ہال، `dyn Trait`،`impl Trait`
- **2019**:`async/await`مستحکم پر اترتا ہے — async ماحولیاتی نظام شروع ہوتا ہے
### پختگی (2020–موجودہ)
- **2021**: **رسٹ 2021 ایڈیشن** — بند ہونے والے فیلڈز کو غیر واضح کریں، صفوں کے لیے `IntoIterator`
- **2024**: **رسٹ 2024 ایڈیشن** —`gen`بلاکس،`unsafe extern`کے تقاضے
- **2025**: لینکس کرنل، اینڈرائیڈ، ونڈوز، AWS انفراسٹرکچر میں زنگ
## ایڈیشن سسٹم
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## ملکیت کا ارتقاء
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

## Async ارتقاء
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## ماحولیاتی نظام کی نمو
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## کلیدی RFCs
| آر ایف سی | سال | خصوصیت |
|------|------|---------|
| 25 | 2013 | پیٹرن ملاپ |
| 153 | 2014 | `Result`قسم |
| 217 | 2014 | `?`(کوشش کریں) آپریٹر |
| 460 | 2016 | `?``try!` کی جگہ لے لیتا ہے |
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | مورچا 2018 ایڈیشن |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`generics |
| 3013 | 2020 | مشروط تالیف کی جانچ کر رہا ہے |
| 3517 | 2023 | `gen`بلاکس |