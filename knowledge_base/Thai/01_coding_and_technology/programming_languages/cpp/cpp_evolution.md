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
# C++ — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| เบื้องหน้า | 1983 | "C with Classes" — คลาส, การสืบทอด |
| ค++98 | 1998 | มาตรฐาน ISO ฉบับแรก STL เทมเพลต ข้อยกเว้น |
| ค++03 | 2546 | แก้ไขข้อบกพร่อง |
| ค++11 | 2554 | **หลัก**: ย้ายความหมาย, lambdas,`auto`, ตัวชี้อัจฉริยะ,`nullptr`|
| ค++14 | 2014 | แลมบ์ดาทั่วไป, การส่งคืน `auto`,`std::make_unique`|
| ค++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, การเชื่อมโยงแบบมีโครงสร้าง |
| ค++20 | 2020 | **หลัก**: แนวคิด ช่วง โครูทีน โมดูล`std::span`การเปรียบเทียบสามทาง |
| ค++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, อนุมาน`this`|
| ค++26 | ~2026 | `std::execution`, การสะท้อน (คาดว่า), สัญญา |
## เหตุการณ์สำคัญที่สำคัญ
### ยุคก่อนมาตรฐาน (พ.ศ. 2526-2541)
- **1983**: Bjarne Stroustrup สร้างสรรค์ "C with Classes" ที่ Bell Labs
- **1985**: เปลี่ยนชื่อเป็น C++; ฉบับพิมพ์ครั้งแรกของ "ภาษาการเขียนโปรแกรม C++"
- **1989**: เทมเพลต ข้อยกเว้น เนมสเปซที่เสนอ
- **1990**: STL (ไลบรารีเทมเพลตมาตรฐาน) โดย Alexander Stepanov
- **1991**: เทมเพลตที่ได้มาตรฐาน "คู่มืออ้างอิง C++ ที่มีคำอธิบายประกอบ"
### C++98 — มูลนิธิ (1998)
- คลาส, มรดก, ฟังก์ชันเสมือน
- เทมเพลต (ฟังก์ชัน, คลาส, ความเชี่ยวชาญ)
- STL:`vector`,`map`,`set`,`algorithm`,`iterator`
- ข้อยกเว้น (`try/catch/throw`)
-`namespace`,`bool`,`const_cast`,`dynamic_cast`
- ตัวสร้าง`explicit`สมาชิก `mutable`
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — ยุคฟื้นฟูศิลปวิทยา (2011)
- **ย้ายความหมาย**: การอ้างอิงค่า `&&`,`std::move`
- **พอยน์เตอร์อัจฉริยะ**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: ประเภทการอนุมาน
- **`nullptr`**: แทนที่`NULL`
- **แลมบ์ดา**:`[](int x) { return x * 2; }`
- **ช่วงสำหรับ**:`for (auto& x : container)`
- **`constexpr`**: การคำนวณเวลาคอมไพล์
- **`static_assert`**: การยืนยันเวลาคอมไพล์
- **`using`**: พิมพ์นามแฝง (แทนที่`typedef`)
- **เทมเพลตที่หลากหลาย**:`template<typename... Args>`
- **`enum class`**: พิมพ์ enum อย่างแน่นหนา
- **`override`/`final`**: การควบคุมฟังก์ชันเสมือน
- **`std::thread`**: การทำเธรดแบบเนทิฟ
- **`std::atomic`**: การโปรแกรมแบบไม่มีการล็อค
- **`std::function`/`std::bind`**: ฟังก์ชันชั้นหนึ่ง
### C++17 — การปรับแต่ง (2017)
-`std::optional<T>`,`std::variant<T...>`,`std::any`
-`if constexpr`- การแตกแขนงเวลาคอมไพล์
- การผูกแบบมีโครงสร้าง:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- อัลกอริธึมแบบขนาน:`std::execution::par`
- เนมสเปซที่ซ้อนกัน:`namespace A::B::C {}`
-`[[nodiscard]]`,`[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — ภาษาสมัยใหม่ (2020)
- **แนวคิด**:`template<std::integral T>`— เทมเพลตที่มีข้อจำกัด
- **ช่วง**:`views::filter`,`views::transform`— ไปป์ไลน์แบบ Lazy
- **โครูทีน**:`co_await`,`co_yield`,`co_return`
- **โมดูล**:`import`/`export`— การรวบรวมที่เร็วขึ้น
- **`std::span`**: มุมมองข้อมูลที่ต่อเนื่องกันโดยไม่ได้เป็นเจ้าของ
- **การเปรียบเทียบสามทาง**:`<=>`(ผู้ให้บริการยานอวกาศ)
- **`std::format`**: การจัดรูปแบบแบบ Python
- **`consteval`/`constinit`**: การบังคับใช้เวลาคอมไพล์
- **ตัวเริ่มต้นที่กำหนด**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: เข้าร่วมเธรดอัตโนมัติพร้อมโทเค็นหยุด
### C++23 — การปรับปรุงเชิงปฏิบัติ (2024)
-`std::expected<T, E>`— การจัดการข้อผิดพลาดที่ได้แรงบันดาลใจจากสนิม
-`std::print`/`std::println`— เอาต์พุตที่มีรูปแบบรวดเร็ว
-`std::flat_map`,`std::flat_set`
- การลด`this`— พารามิเตอร์วัตถุที่ชัดเจน
-`std::mdspan`— ช่วงหลายมิติ
-`std::generator`— เครื่องกำเนิดไฟฟ้าแบบซิงโครนัส
-`#include <debugging>`— เบรกพอยต์, ดัมพ์
## วิวัฒนาการของรูปแบบที่สำคัญ
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

## กระบวนการมาตรฐาน
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

## ผลกระทบต่อระบบนิเวศ
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
