---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C++ — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| واجهة | 1983 | "C مع الفئات" — الطبقات والميراث |
| سي++98 | 1998 | معيار ISO الأول؛ المحكمة الخاصة بلبنان، القوالب، الاستثناءات |
| سي++03 | 2003 | إصلاحات الخلل |
| سي++11 | 2011 | **التخصص**: نقل الدلالات، لامدا، `auto`، المؤشرات الذكية،`nullptr`|
| سي++14 | 2014 | لامدا عامة، عودة `auto`،`std::make_unique`|
| سي ++ 17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, روابط منظمة |
| سي++20 | 2020 | **التخصص**: المفاهيم، النطاقات، الكورتينات، الوحدات النمطية، `std::span`، مقارنة ثلاثية |
| سي++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, استنتاج`this`|
| سي++26 | ~2026 |  `std::execution`، الانعكاس (المتوقع)، العقود |
## المعالم الرئيسية
### عصر ما قبل المعيار (1983-1998)
- **1983**: ابتكر بيارن ستروستروب "C with Classes" في Bell Labs
- **1985**: تمت إعادة تسميتها بـ C++; الطبعة الأولى من "لغة البرمجة C++"
- **1989**: القوالب والاستثناءات ومساحات الأسماء المقترحة
- **1990**: STL (مكتبة النماذج القياسية) بقلم ألكسندر ستيبانوف
- **1991**: توحيد القوالب؛ "الدليل المرجعي المشروح لـ C++"
### C++98 — المؤسسة (1998)
- الطبقات والميراث والوظائف الافتراضية
- القوالب (الوظائف، الفئات، التخصص)
- المحكمة الخاصة بلبنان: `vector`، `map`، `set`، `algorithm`،`iterator`
- الاستثناءات (`try/catch/throw`)
- `namespace`، `bool`، `const_cast`،`dynamic_cast`
- منشئو`explicit`وأعضاء `mutable`
- رتي ( `typeid`،`dynamic_cast`)
### C++11 — عصر النهضة (2011)
- **نقل الدلالات**: مراجع قيمة `&&`،`std::move`
- **المؤشرات الذكية**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: اكتب الاستدلال
- **`nullptr`**: يحل محل`NULL`
- **لامدا**:`[](int x) { return x * 2; }`
- **النطاق لـ**:`for (auto& x : container)`
- **`constexpr`**: حساب وقت الترجمة
- **`static_assert`**: تأكيدات وقت الترجمة
- **`using`**: كتابة الأسماء المستعارة (استبدال`typedef`)
- **قوالب متغيرة**:`template<typename... Args>`
- **`enum class`**: التعدادات المكتوبة بقوة
- **`override`/`final`**: التحكم في الوظيفة الافتراضية
- **`std::thread`**: الترابط الأصلي
- **`std::atomic`**: برمجة خالية من القفل
- **`std::function`/`std::bind`**: وظائف من الدرجة الأولى
### C++17 — التحسين (2017)
- `std::optional<T>`، `std::variant<T...>`،`std::any`
-`if constexpr`— تفرع وقت الترجمة
- الارتباطات المنظمة:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- الخوارزميات المتوازية:`std::execution::par`
- مساحات الأسماء المتداخلة:`namespace A::B::C {}`
- `[[nodiscard]]`، `[[maybe_unused]]`، `[[fallthrough]]`
### C++20 — اللغة الحديثة (2020)
- **المفاهيم**:`template<std::integral T>`— قوالب مقيدة
- **النطاقات**:`views::filter`,`views::transform`— خطوط الأنابيب البطيئة
- **كوروتين**:`co_await`,`co_yield`,`co_return`
- **الوحدات**:`import`/`export`— تجميع أسرع
- **`std::span`**: عرض عدم امتلاك البيانات المتجاورة
- **مقارنة ثلاثية**:`<=>`(مشغل سفينة الفضاء)
- **`std::format`**: تنسيق بنمط بايثون
- **`consteval`/`constinit`**: فرض وقت الترجمة
- **المهيئات المعينة**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: موضوع الانضمام التلقائي مع رمز التوقف
### C++23 - تحسينات عملية (2024)
-`std::expected<T, E>`— معالجة الأخطاء المستوحاة من الصدأ
-`std::print`/`std::println`— إخراج سريع التنسيق
- `std::flat_map`،`std::flat_set`
- استنتاج`this`— معلمة كائن صريحة
-`std::mdspan`— امتداد متعدد الأبعاد
-`std::generator`— مولد متزامن
-`#include <debugging>`— نقطة توقف، تفريغ
## تطور الأنماط الرئيسية
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

## عملية المعايير
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

## تأثير النظام البيئي
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
