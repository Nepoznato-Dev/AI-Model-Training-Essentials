---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cpp, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C++ - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| Cfront | 1983 | "C با کلاس ها" — کلاس ها، وراثت |
| C++98 | 1998 | اولین استاندارد ISO; STL، الگوها، استثناها |
| C++03 | 2003 | رفع نقص |
| C++11 | 2011 | **عمده**: معانی حرکت، لامبدا، `auto`، اشاره گرهای هوشمند،`nullptr`|
| C++14 | 2014 | لامبداهای عمومی، بازگشت `auto`،`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, اتصالات ساختاری |
| C++20 | 2020 | **عمده**: مفاهیم، ​​محدوده ها، روال ها، ماژول ها، `std::span`، مقایسه سه طرفه |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, استنتاج`this`|
| C++26 | ~2026 |  `std::execution`، بازتاب (مورد انتظار)، قراردادها |
## نقاط عطف اصلی
### دوران پیش از استاندارد (1983-1998)
- **1983**: Bjarne Stroustrup "C with Classes" را در آزمایشگاه Bell ایجاد کرد.
- **1985**: تغییر نام به C++؛ اولین نسخه "زبان برنامه نویسی C++"
- **1989**: الگوها، استثناها، فضاهای نام پیشنهادی
- **1990**: STL (کتابخانه الگوی استاندارد) توسط الکساندر استپانوف
- **1991**: الگوهای استاندارد شده. "راهنمای مرجع C++ مشروح"
### C++98 - The Foundation (1998)
- کلاس ها، وراثت، توابع مجازی
- الگوها (توابع، کلاس ها، تخصص)
- STL: `vector`، `map`، `set`، `algorithm`،`iterator`
- استثناها (`try/catch/throw`)
- `namespace`، `bool`، `const_cast`،`dynamic_cast`
- سازندگان `explicit`، اعضای `mutable`
- RTTI (`typeid`، `dynamic_cast`)
### C++11 - رنسانس (2011)
- **معناشناسی حرکت**: ارجاعات rvalue `&&`،`std::move`
- **نشانگرهای هوشمند**: `unique_ptr`، `shared_ptr`،`weak_ptr`
- **`auto`**: استنتاج نوع
- **`nullptr`**: جایگزین`NULL`می شود 
- **لامبداس**:`[](int x) { return x * 2; }`
- ** محدوده برای **:`for (auto& x : container)`
- **`constexpr`**: محاسبه زمان کامپایل
- **`static_assert`**: اظهارات در زمان کامپایل
- **`using`**: نام مستعار نوع (به جای `typedef`)
- **قالب های متنوع**:`template<typename... Args>`
- **`enum class`**: enums به شدت تایپ شده است
- **`override`/`final`**: کنترل عملکرد مجازی
- **`std::thread`**: نخ بومی
- **`std::atomic`**: برنامه نویسی بدون قفل
- **`std::function`/`std::bind`**: توابع درجه یک
### C++17 - پالایش (2017)
- `std::optional<T>`، `std::variant<T...>`،`std::any`
-`if constexpr`- انشعاب در زمان کامپایل
- اتصالات ساختاری:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- الگوریتم های موازی:`std::execution::par`
- فضاهای نام تو در تو:`namespace A::B::C {}`
- `[[nodiscard]]`، `[[maybe_unused]]`، `[[fallthrough]]`
### C++20 - زبان مدرن (2020)
- **مفاهیم**:`template<std::integral T>`- الگوهای محدود
- **محدوده**: `views::filter`،`views::transform`- خطوط لوله تنبل
- **کوروتین**:`co_await`,`co_yield`,`co_return`
- ** ماژول ها **:`import`/`export`- تدوین سریعتر
- **`std::span`**: نمای غیر مالکیت داده های پیوسته
- ** مقایسه سه طرفه **:`<=>`(اپراتور سفینه فضایی)
- **`std::format`**: قالب بندی به سبک پایتون
- **`consteval`/`constinit`**: اجرای زمان کامپایل
- ** راه اندازی کننده های تعیین شده **:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: اتصال خودکار رشته با توکن توقف
### C++23 - بهبودهای عملی (2024)
-`std::expected<T, E>`- مدیریت خطای زنگ زدگی
-`std::print`/`std::println`- خروجی با فرمت سریع
- `std::flat_map`،`std::flat_set`
- استنتاج`this`- پارامتر شی صریح
-`std::mdspan`- دهانه چند بعدی
-`std::generator`- ژنراتور همزمان
-`#include <debugging>`- نقطه شکست، تخلیه
## تکامل الگوهای کلیدی
```
Memory Management:
  1998: Raw pointers, manual new/delete
  2011: Smart pointers (unique_ptr, shared_ptr)
  2020: std::span, views (zero-copy abstractions)
  2023: std::expected (error without exceptions)

Error Handling:
  1998: Exceptions (try/catch)
  2011: noexcept, error codes
  2023: std::expected (Rust-inspired)
  2026: Contracts (expected)

Concurrency:
  1998: None (OS threads)
  2011: std::thread, std::mutex, std::atomic
  2017: Parallel algorithms
  2020: Coroutines, std::jthread

Abstraction:
  1998: Templates (unconstrained)
  2011: Move semantics, perfect forwarding
  2020: Concepts (constrained templates)
```

## فرآیند استاندارد
```
1998: C++98 (ISO/IEC 14882:1998)
2003: C++03 (defect fixes)
2011: C++11 — "modern C++" begins
2014: C++14 — incremental
2017: C++17 — incremental
2020: C++20 — another revolution
2024: C++23 — practical improvements
2026: C++26 — reflection, contracts (expected)

3-year release cycle since C++11
```

## تاثیر اکوسیستم
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
