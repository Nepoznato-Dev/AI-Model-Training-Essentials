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
# C++ - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| Cfront | 1983 | "C کے ساتھ کلاسز" - کلاسز، وراثت |
| C++98 | 1998 | پہلا ISO معیار؛ STL، ٹیمپلیٹس، استثناء |
| C++03 | 2003 | خرابی کی اصلاح |
| C++11 | 2011 | **میجر**: سیمنٹکس کو منتقل کریں، لیمبڈاس، `auto`، سمارٹ پوائنٹرز،`nullptr`|
| C++14 | 2014 | عام لیمبڈاس،`auto`واپسی،`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, ساختی پابندیاں |
| C++20 | 2020 | **بڑا**: تصورات، رینجز، کوروٹینز، ماڈیولز، `std::span`، تین طرفہ موازنہ |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, deducing`this`|
| C++26 | ~2026 |  `std::execution`، عکاسی (متوقع)، معاہدے |
## اہم سنگ میل
### The Pre-Standard Era (1983–1998)
- **1983**: Bjarne Stroustrup بیل لیبز میں "C کے ساتھ کلاسز" بناتا ہے۔
- **1985**: C++ کا نام تبدیل کر دیا گیا؛ "C++ پروگرامنگ لینگویج" کا پہلا ایڈیشن
- **1989**: ٹیمپلیٹس، مستثنیات، نام کی جگہیں تجویز کردہ
- **1990**: STL (معیاری ٹیمپلیٹ لائبریری) از الیگزینڈر سٹیپانوف
- **1991**: ٹیمپلیٹس معیاری؛ "تشریح شدہ C++ حوالہ جات"
### C++98 — دی فاؤنڈیشن (1998)
- کلاسز، وراثت، ورچوئل فنکشنز
- ٹیمپلیٹس (فنکشنز، کلاسز، اسپیشلائزیشن)
- STL: `vector`، `map`، `set`، `algorithm`،`iterator`
- مستثنیات (`try/catch/throw`)
- `namespace`، `bool`، `const_cast`،`dynamic_cast`
-`explicit`کنسٹرکٹرز،`mutable`ممبران
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — The Renaissance (2011)
- **سمینٹکس کو منتقل کریں**:`&&`rvalue حوالہ جات،`std::move`
- **سمارٹ پوائنٹرز**: `unique_ptr`، `shared_ptr`،`weak_ptr`
- **`auto`**: قسم کا اندازہ
- **`nullptr`**:`NULL`کی جگہ لے لیتا ہے 
- **لیمبڈاس**:`[](int x) { return x * 2; }`
- **حد کے لیے**:`for (auto& x : container)`
- **`constexpr`**: مرتب وقت کی گنتی
- **`static_assert`**: مرتب وقت کے دعوے
- **`using`**: عرفی نام ٹائپ کریں (`typedef` کی جگہ لے کر)
- **متغیر ٹیمپلیٹس**:`template<typename... Args>`
- **`enum class`**: مضبوطی سے ٹائپ شدہ enums
- **`override`/`final`**: ورچوئل فنکشن کنٹرول
- **`std::thread`**: مقامی تھریڈنگ
- **`std::atomic`**: لاک فری پروگرامنگ
- **`std::function`/`std::bind`**: فرسٹ کلاس فنکشنز
### C++17 — تطہیر (2017)
- `std::optional<T>`، `std::variant<T...>`،`std::any`
-`if constexpr`- کمپائل ٹائم برانچنگ
- سٹرکچرڈ بائنڈنگز:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- متوازی الگورتھم:`std::execution::par`
- گھریلو نام کی جگہیں:`namespace A::B::C {}`
-`[[nodiscard]]`,`[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — جدید زبان (2020)
- **تصورات**:`template<std::integral T>`— محدود ٹیمپلیٹس
- **رینجز**: `views::filter`،`views::transform`— سست پائپ لائنز
- **کورٹائنز**: `co_await`، `co_yield`،`co_return`
- **ماڈیول**:`import`/`export`— تیز تر تالیف
- **`std::span`**: متصل ڈیٹا کا غیر مالکانہ نظارہ
- **تین طرفہ موازنہ**:`<=>`(خلائی جہاز آپریٹر)
- **`std::format`**: ازگر کی طرز کی فارمیٹنگ
- **`consteval`/`constinit`**: مرتب وقت کا نفاذ
- **نامزد ابتدائی **:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: اسٹاپ ٹوکن کے ساتھ تھریڈ کو خود بخود جوائن کرنا
### C++23 — عملی بہتری (2024)
-`std::expected<T, E>`- زنگ سے متاثر غلطی سے نمٹنے
-`std::print`/`std::println`- تیز فارمیٹ شدہ آؤٹ پٹ
- `std::flat_map`،`std::flat_set`
-`this`کو کم کرنا - واضح آبجیکٹ پیرامیٹر
-`std::mdspan`- کثیر جہتی دورانیہ
-`std::generator`- ہم وقت ساز جنریٹر
-`#include <debugging>`- بریک پوائنٹ، ڈمپ
## کلیدی نمونوں کا ارتقاء
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

## معیاری عمل
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

## ماحولیاتی نظام کا اثر
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
