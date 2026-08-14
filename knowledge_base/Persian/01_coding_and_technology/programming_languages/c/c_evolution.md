---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| K&R C | 1972–78 | C اصلی (کرنیگان و ریچی) |
| C89/C90 | 1989/90 | اولین استاندارد ANSI/ISO |
| C95 | 1995 | اصلاحیه 1: `wchar.h`، نمودارها |
| C99 | 1999 |  نظرات `//`، `inline`، `bool`، VLA ها، اولیه سازهای تعیین شده |
| C11 | 2011 | Atomics، Threads، `_Static_assert`، ساختارها/اتحادیه های ناشناس |
| C17 | 2018 | رفع نقص (بدون ویژگی جدید) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, ویژگی های |
## نقاط عطف اصلی
### K&R C (1972–1989)
- **1972**: دنیس ریچی C را در آزمایشگاه های بل برای یونیکس ایجاد می کند
- **1978**: کرنیگان و ریچی "زبان برنامه نویسی C" را منتشر کردند
- ویژگی های کلیدی: `struct`، `int`، `char`، اشاره گرها، توابع،`#include`
- بدون `void`، بدون `enum`، بدون `unsigned`، بدون `const`
### C89/C90 - استاندارد (1989)
- اولین استاندارد ANSI (ANSI X3.159-1989)
- اضافه شده: `void`، `enum`، `const`، `volatile`، نمونه های اولیه عملکرد،`signed`
- "عصر طلایی" - قابل حمل، به طور گسترده ای پذیرفته شده است
- هنوز خط پایه برای بسیاری از سیستم های تعبیه شده است
### C99 - مدرن C (1999)
- نظرات تک خطی `//`
- توابع `inline`
-`bool`از طریق`<stdbool.h>`
- آرایه های با طول متغیر (VLA)
- اولیه سازهای تعیین شده:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`- اعلانات در حلقه
- `<stdint.h>`: `int32_t`، `uint64_t`، و غیره
- کلمه کلیدی `restrict`
- ماکروهای متنوع
- لفظ مرکب
### C11 - ایمنی و همزمانی (2011)
-`<stdatomic.h>`- عملیات اتمی
-`<threads.h>`- پشتیبانی از موضوع
-`_Static_assert`- اظهارات در زمان کامپایل
- ساختارها/اتحادیه های ناشناس در ساختارهای تودرتو
- `_Alignof`،`_Alignas`- کنترل تراز
- انتخاب های عمومی:`_Generic(x, int: ..., default: ...)`
- پشتیبانی از یونیکد:`<uchar.h>`
- پشتیبانی از VLA اختیاری (به دلیل نگرانی های تعبیه شده اختیاری شده است)
### C23 - رنسانس (2024)
-`nullptr`- ثابت نشانگر تهی (جایگزین ماکرو `NULL`)
-`typeof`- استنتاج نوع
-`constexpr`- عبارات ثابت
-`#embed`- داده های باینری را در زمان کامپایل جاسازی کنید
- نحو`[[attribute]]`(ویژگی های سبک C23)
-`true`/`false`به عنوان کلمات کلیدی (دیگر نیازی به`<stdbool.h>`نیست)
- استنتاج نوع `auto`
-`static_assert`(بدون خط زیر)
-`alignof`(بدون خط زیر)
- بازگشت پیش فرض`int`حذف شد
## فرآیند استاندارد
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## فلسفه سازگاری
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## تکامل پیش پردازنده
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## تایپ سیستم تکامل
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## تاثیر اکوسیستم
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
