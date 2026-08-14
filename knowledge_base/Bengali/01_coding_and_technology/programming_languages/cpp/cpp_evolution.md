<!--
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

-->
# C++ — সংস্করণ ইতিহাস ও বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| Cfront | 1983 | "C সহ ক্লাস" — ক্লাস, উত্তরাধিকার |
| C++98 | 1998 | প্রথম আইএসও স্ট্যান্ডার্ড; STL, টেমপ্লেট, ব্যতিক্রম |
| C++03 | 2003 | ত্রুটি সংশোধন |
| C++11 | 2011 | **মেজর**: শব্দার্থবিদ্যা, ল্যাম্বডাস,`auto`, স্মার্ট পয়েন্টার,`nullptr`|
| C++14 | 2014 | জেনেরিক ল্যাম্বডাস,`auto`রিটার্ন,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, কাঠামোবদ্ধ বাঁধাই |
| C++20 | 2020 | **মেজর**: ধারণা, রেঞ্জ, কোরোটিন, মডিউল,`std::span`, ত্রিমুখী তুলনা |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`,`this`ডিডিউসিং |
| C++26 | ~2026 | `std::execution`, প্রতিফলন (প্রত্যাশিত), চুক্তি |
## প্রধান মাইলফলক
### প্রাক-মানক যুগ (1983-1998)
- **1983**: Bjarne Stroustrup বেল ল্যাবসে "C সহ ক্লাস" তৈরি করে
- **1985**: C++ নামকরণ করা হয়েছে; "C++ প্রোগ্রামিং ভাষা" এর প্রথম সংস্করণ
- **1989**: টেমপ্লেট, ব্যতিক্রম, নামস্থান প্রস্তাবিত
- **1990**: আলেকজান্ডার স্টেপানোভের STL (স্ট্যান্ডার্ড টেমপ্লেট লাইব্রেরি)
- **1991**: টেমপ্লেট মানসম্মত; "টীকাযুক্ত C++ রেফারেন্স ম্যানুয়াল"
### C++98 — দ্য ফাউন্ডেশন (1998)
- ক্লাস, উত্তরাধিকার, ভার্চুয়াল ফাংশন
- টেমপ্লেট (ফাংশন, ক্লাস, বিশেষীকরণ)
- STL: `vector`, `map`, `set`, `algorithm`,`iterator`
- ব্যতিক্রম (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
-`explicit`কনস্ট্রাক্টর,`mutable`সদস্য
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — দ্য রেনেসাঁ (2011)
- **অর্থতত্ত্ব সরান**:`&&`rvalue রেফারেন্স,`std::move`
- **স্মার্ট পয়েন্টার**: `unique_ptr`, `shared_ptr`,`weak_ptr`
- **`auto`**: টাইপ ইনফারেন্স
- **`nullptr`**:`NULL`প্রতিস্থাপন করে 
- **ল্যাম্বডাস**:`[](int x) { return x * 2; }`
- **পরিসীমা-এর জন্য**:`for (auto& x : container)`
- **`constexpr`**: কম্পাইল-টাইম গণনা
- **`static_assert`**: কম্পাইল-টাইম দাবী
- **`using`**: টাইপ উপনাম (`typedef` প্রতিস্থাপন)
- **ভ্যারিয়াডিক টেমপ্লেট**:`template<typename... Args>`
- **`enum class`**: দৃঢ়ভাবে টাইপ করা enums
- **`override`/`final`**: ভার্চুয়াল ফাংশন নিয়ন্ত্রণ
- **`std::thread`**: নেটিভ থ্রেডিং
- **`std::atomic`**: লক-মুক্ত প্রোগ্রামিং
- **`std::function`/`std::bind`**: প্রথম শ্রেণীর ফাংশন
### C++17 — পরিমার্জন (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— কম্পাইল-টাইম ব্রাঞ্চিং
- স্ট্রাকচার্ড বাইন্ডিং:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- সমান্তরাল অ্যালগরিদম:`std::execution::par`
- নেস্টেড নেমস্পেস:`namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — আধুনিক ভাষা (2020)
- **ধারণা**:`template<std::integral T>`— সীমাবদ্ধ টেমপ্লেট
- **পরিসীমা**:`views::filter`,`views::transform`— অলস পাইপলাইন
- **করোটিন**: `co_await`, `co_yield`,`co_return`
- **মডিউল**:`import`/`export`— দ্রুত সংকলন
- **`std::span`**: সংলগ্ন ডেটার মালিকানাহীন দৃশ্য
- **থ্রি-ওয়ে তুলনা**:`<=>`(স্পেসশিপ অপারেটর)
- **`std::format`**: পাইথন-স্টাইল ফর্ম্যাটিং
- **`consteval`/`constinit`**: কম্পাইল-টাইম এনফোর্সমেন্ট
- **নির্ধারিত ইনিশিয়ালাইজার**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: স্টপ টোকেন সহ স্বয়ংক্রিয়ভাবে যুক্ত হওয়া থ্রেড
### C++23 — ব্যবহারিক উন্নতি (2024)
-`std::expected<T, E>`— মরিচা-অনুপ্রাণিত ত্রুটি পরিচালনা
-`std::print`/`std::println`- দ্রুত ফর্ম্যাট করা আউটপুট
- `std::flat_map`,`std::flat_set`
-`this`- স্পষ্ট বস্তুর প্যারামিটার
-`std::mdspan`— বহুমাত্রিক স্প্যান
-`std::generator`— সিঙ্ক্রোনাস জেনারেটর
-`#include <debugging>`— ব্রেকপয়েন্ট, ডাম্প
## মূল প্যাটার্নের বিবর্তন
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

## স্ট্যান্ডার্ড প্রক্রিয়া
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

## ইকোসিস্টেমের প্রভাব
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
