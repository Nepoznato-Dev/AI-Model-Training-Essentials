---
# Metadata
title: "Julia — Version History & Evolution"
description: "Comprehensive version history and evolution of Julia from 0.1 to modern Julia."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [julia, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# جولیا - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 0.1 | 2013 | انتشار اولیه (Bezanson، Karpinski، Viral Shah، Jeff Bezanson) |
| 0.2 | 2013 | مدیر بسته، بهبود REPL |
| 0.3 | 2014 | آرایه ها، جبر خطی،`Nullable`|
| 0.4 | 2015 | **برنامه نویسی عملکردی**: بسته شدن، درک، انواع پیچیده |
| 0.5 | 2016 | **عمده**: برابری عملکرد با C برای بسیاری از معیارها |
| 0.6 | 2017 |  انواع `Union`، نحو `where`، سیستم نوع بهبود یافته |
| 0.7 | 2018 | **پاکسازی گسترده**: منسوخ شدن، نوع `Missing`، `nothing`،`stderr`|
| 1.0 | 2018 | **اولین انتشار پایدار**: API پایدار، پشتیبانی طولانی مدت شروع می شود |
| 1.1 | 2019 |  بهبودهای`adjoint`,`copy!`,`LinearAlgebra`|
| 1.2 | 2019 | تاپل های نامگذاری شده، بهبود آرگومان کلمات کلیدی |
| 1.3 | 2019 | **سرور بسته**، پایه های`async`/`await`|
| 1.4 | 2020 |  بهبودهای `import`،`LazyModule`|
| 1.5 | 2020 | **عمده**: راه اندازی سریعتر، `--compiled-modules`، کامپایل دو فاز |
| 1.6 | 2021 | **نسخه LTS**: راه اندازی سریعتر، REPL جدید،`Base64`|
| 1.7 | 2021 |  بلوک های `let`، بهبود`@kwdef`|
| 1.8 | 2022 | **موضوعات وظیفه** (وظایف موازی)،`@constprop`|
| 1.9 | 2023 | **بومی`@threads`**، پیش کامپایل بسته،`@assume_effects`|
| 1.10 | 2023 | **عمده**: `@ccallable`، استنتاج نوع بهبود یافته،`@constprop :aggressive`|
| 1.11 | 2024 | بهبود عملکرد بیشتر،`@assume_effects`|
| 2.0 | TBD | (آینده) شکستن تغییرات مورد انتظار |
## نقاط عطف اصلی
### جولیا 0.x - نمونه اولیه (2012–2018)
- **2012**: جف بزانسون، استفان کارپینسکی، ویرال شاه و آلن ادلمن جولیا را در MIT آغاز کردند.
- **هدف**: "مانند پایتون راه بروید، مانند C اجرا کنید" - نحو سطح بالا با عملکرد سطح پایین
- **0.1 (2013)**: اولین نسخه عمومی - ارسال چندگانه، JIT مبتنی بر LLVM
- **0.4 (2015)**: ویژگی های برنامه نویسی کاربردی - بسته شدن، درک مطلب
- **0.5 (2016)**: نقطه عطف عملکرد - مطابق با C در بسیاری از معیارها
- **0.6 (2017)**: انواع `Union`، نحو `where`
- **0.7 (2018)**: پاکسازی گسترده — نوع `Missing`،`nothing`جایگزین `nothing`، حذف منسوخ شدن
### جولیا 1.0 — ثبات (2018)
- **اولین API پایدار** - سازگاری با نسخه تضمین شده در 1.x
- ارسال چندگانه، انواع پارامتریک، فرابرنامه ریزی، کوروتین ها
- مدیر بسته داخلی (Pkg)
- رشته های سبز (وظایف)
### جولیا 1.x — عملکرد و موازی سازی (2019–اکنون)
- **1.5 (2020)**: زمان راه اندازی سریعتر (برای استفاده از CLI حیاتی است)
- **1.6 (2021)**: LTS — REPL جدید، راه اندازی سریعتر، سیستم مصنوع
- **1.8 (2022)**: **رشته های وظیفه** — اجرای Tasks در چندین رشته سیستم عامل
- **1.9 (2023)**:`@threads`بومی با زمان‌بندی`:static`و `:dynamic`
- **1.10 (2023) **: بهبود عملکرد عمده، استنتاج نوع بهتر
- **1.11 (2024)**: بهینه سازی مداوم
## تکامل اعزام چندگانه
```julia
# Julia's core feature: multiple dispatch
# Method selection based on ALL argument types

# Basic methods
function area(shape)
    error("Unknown shape")
end

area(c::Circle) = π * c.r^2
area(r::Rectangle) = r.w * r.h

# Parametric types
struct Point{T <: Real}
    x::T
    y::T
end

# Dispatch on type parameters
distance(p1::Point{T}, p2::Point{T}) where {T} =
    sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)

# Union types (0.6+)
process(x::Union{Int, Float64}) = x * 2

# Julia 1.0+: Clean type system
function solve(A::AbstractMatrix{T}, b::AbstractVector{T}) where {T <: Number}
    # Works for any numeric type
    A \ b
end
```

## تکامل عملکرد
```
Julia 0.1:  JIT via LLVM — promising but inconsistent
Julia 0.5:  "C-competitive" on many benchmarks (177 benchmarks)
Julia 1.0:  Stable, fast startup
Julia 1.5:  Faster startup (critical for CLI tools)
Julia 1.8:  Task threads — multi-core parallelism
Julia 1.9:  Native @threads, package precompilation
Julia 1.10: Major type inference improvements
Julia 1.11: Further optimizations
Target:     Sub-millisecond startup, C-competitive throughput
```

## همزمانی و موازی
```
0.1:  Tasks (green threads, cooperative)
0.5:  Channel (producer-consumer)
1.0:  Distributed computing (Distributed stdlib)
1.3:  Package server, async foundations
1.8:  Task threads — Tasks run on OS threads
1.9:  @threads :static / :dynamic
1.10: Improved thread safety
2.0+: (planned) Better async/await, effect handlers
```

## اصول کلیدی طراحی
```
1. "Walk like Python, run like C" — high-level syntax, low-level speed
2. "Multiple dispatch is king" — functions dispatch on all argument types
3. "No performance cliffs" — generic code should be fast
4. "Composable" — small primitives, compose freely
5. "Interactive" — REPL-first, notebook-friendly
6. "Scientific" — built for numerical/scientific computing
```

## رشد اکوسیستم
```
2012: Julia development begins at MIT
2013: Julia 0.1 released publicly
2014: JuliaCon first held
2016: Julia 0.5 — performance milestone
2017: Julia 0.6 — type system improvements
2018: Julia 1.0 — first stable release
2019: JuliaHub founded — commercial support
2020: Julia 1.5 — faster startup
2021: Julia 1.6 — LTS release
2022: Julia 1.8 — task threads
2025: Julia powers scientific computing, climate modeling (CliMA),
       astronomy (Celeste), bioinformatics, quantitative finance
       10,000+ registered packages
       Used by: NASA, MIT, Stanford, Pfizer, Aviva, Federal Reserve
```
