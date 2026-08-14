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
# زنگ - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | تاریخ انتشار | تم کلید |
|---------|-------------|-----------|
| 0.1 | ژانویه 2012 | اولین کامپایلر (rustc)، همزمانی مبتنی بر وظیفه |
| 0.5 | 2012 | سیستم نوع مبتنی بر صفت شکل می گیرد |
| 0.6 | 2012 | حذف جعبه های مدیریت شده`@`|
| 0.7 | 2013 | `@`حذف شد،`~`برای جعبه های متعلق به |
| 0.8 | 2013 | حاشیه نویسی مادام العمر،`&mut`|
| 0.9 | ژانویه 2014 | پاکسازی نهایی قبل از 1.0 |
| 0.10 | فوریه 2014 | آخرین نسخه قبل از 1.0 |
| 0.11 | آوریل 2014 | `Box<T>`جایگزین`~T`|
| 0.12 | می 2014 |  بازنویسی ماژول`io`آغاز می شود |
| 1.0 | 15 مه 2015 | **نسخه پایدار** — "Rust 1.0" |
| 1.10 | آگوست 2016 |  انتشار خطای`?`(به عنوان`try!`→`?`) |
| 1.15 | فوریه 2017 | اولین Rust روی استیبل با آماده سازی`impl Trait`|
| 1.18 | ژوئن 2017 |  `pub(crate)`، کامپایل افزایشی |
| 1.20 | اکتبر 2017 | ثابت های مرتبط |
| 1.26 | می 2018 | `impl Trait`در موقعیت آرگومان/بازگشت |
| 1.28 | سپتامبر 2018 | تخصیص دهندگان جهانی |
| 1.31 | دسامبر 2018 | **Rust 2018 Edition** — ماژول ها،`dyn Trait`|
| 1.34 | آوریل 2019 | ثبت های جایگزین |
| 1.39 | نوامبر 2019 | `async/await`روی پایدار |
| 1.44 | ژوئیه 2020 | بهبودهای تشخیصی |
| 1.51 | آوریل 2021 | `const`ژنریک (MVP) |
| 1.56 | اکتبر 2021 | **Rust 2021 Edition** — بسته شدن، IntoIterator |
| 1.59 | فوریه 2022 | مونتاژ درون خطی |
| 1.62 | ژوئن 2022 | `#[default]`برای enums |
| 1.65 | دسامبر 2022 | `let else`|
| 1.68 | مارس 2023 |  `#[ffi_pure]`، بهینه سازی هدایت شده توسط پروفایل |
| 1.70 | ژوئن 2023 | وابستگی های جدا شده`crates.io`|
| 1.74 | نوامبر 2023 | حالت آفلاین بار |
| 1.76 | فوریه 2024 | **Rust 2024 Edition** — بلوک های `gen`،`unsafe extern`|
| 1.79 | ژوئن 2024 | `LazyCell`,`LazyLock`|
| 1.82 | اکتبر 2024 | `unsafe`در بلوک های`extern`مورد نیاز |
| 1.85 | فوریه 2025 | Rust 2024 edition تثبیت شد |
## نقاط عطف اصلی
### Pre-1.0 (2010–2015)
- **2010**: پروژه جانبی گریدون هور در موزیلا مورد توجه قرار گرفت
- **2012**: اولین کامپایلر عمومی; سیستم نوع تحت طراحی مجدد عمده ای قرار می گیرد
- **2013**: مدل مالکیت متبلور می شود.  جعبه های`@`حذف شدند
- **2014**: فرآیند Rust RFC رسمی شد. جامعه رشد می کند
- **2015**: **1.0** — تضمین ثبات؛ "انتزاعات با هزینه صفر"
### سالهای رشد (2015–2019)
- **2015**: باربری مدیر بسته استاندارد می شود
- **2018**: **Rust 2018 Edition** — تعمیرات اساسی سیستم ماژول، `dyn Trait`،`impl Trait`
- **2019**:`async/await`روی پایدار فرود می آید — اکوسیستم ناهمگام آغاز می شود
### سررسید (2020–اکنون)
- **2021**: **Rust 2021 Edition** - رفع ابهام فیلدها در بسته شدن،`IntoIterator`برای آرایه ها
- **2024**: **Rust 2024 Edition** — بلوک های `gen`، نیازمندی های `unsafe extern`
- **2025**: زنگ زدگی در هسته لینوکس، اندروید، زیرساخت ویندوز، AWS
سیستم نسخه ##
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## تکامل مالکیت
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

## تکامل Async
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## رشد اکوسیستم
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## کلید RFC
| RFC | سال | ویژگی |
|------|------|---------|
| 25 | 2013 | تطبیق الگو |
| 153 | 2014 |  نوع`Result`|
| 217 | 2014 |  اپراتور`?`(تلاش کنید) |
| 460 | 2016 | `?`جایگزین`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Rust 2018 edition |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`ژنریک |
| 3013 | 2020 | بررسی کامپایل مشروط |
| 3517 | 2023 |  بلوک های`gen`|