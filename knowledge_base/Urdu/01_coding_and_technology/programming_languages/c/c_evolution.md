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
# C - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| K&R C | 1972-78 | اصل سی (کرنیگھن اور رچی) |
| C89/C90 | 1989/90 | پہلا ANSI/ISO معیار |
| C95 | 1995 | ترمیم 1:`wchar.h`, digraphs |
| C99 | 1999 | `//`تبصرے،`inline`,`bool`, VLAs، نامزد ابتدائی کار |
| C11 | 2011 | جوہری، دھاگے،`_Static_assert`, گمنام ڈھانچے/یونینز |
| C17 | 2018 | خرابی کی اصلاح (کوئی نئی خصوصیات نہیں) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, صفات |
## اہم سنگ میل
### K&R C (1972–1989)
- **1972**: ڈینس رچی نے بیل لیبز میں یونکس کے لیے سی تخلیق کیا۔
- **1978**: کرنیگھن اور رچی نے "دی سی پروگرامنگ لینگویج" شائع کیا۔
- کلیدی خصوصیات: `struct`، `int`، `char`، پوائنٹرز، فنکشنز،`#include`
-`void`نہیں،`enum`نہیں،`unsigned`نہیں،`const`نہیں
### C89/C90 — دی اسٹینڈرڈ (1989)
- پہلا ANSI معیار (ANSI X3.159-1989)
- شامل کیا گیا: `void`، `enum`، `const`، `volatile`، فنکشن پروٹو ٹائپس،`signed`
- "سنہری دور" - پورٹیبل، وسیع پیمانے پر اپنایا گیا۔
- اب بھی بہت سے ایمبیڈڈ سسٹمز کے لیے بنیادی لائن ہے۔
### C99 — جدید C (1999)
-`//`سنگل لائن تبصرے۔
-`inline`فنکشنز
-`bool`بذریعہ`<stdbool.h>`
- متغیر لمبائی کی صفیں (VLAs)
- نامزد ابتدائی کنندگان:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`- لوپ میں اعلانات
-`<stdint.h>`: `int32_t`، `uint64_t`، وغیرہ۔
-`restrict`کلیدی لفظ
- متغیر میکرو
- مرکب لٹریلز
### C11 — حفاظت اور ہم آہنگی (2011)
-`<stdatomic.h>`- جوہری آپریشن
-`<threads.h>`- تھریڈ سپورٹ
-`_Static_assert`- مرتب وقت کے دعوے
- نیسٹڈ سٹرکٹس میں گمنام سٹرکٹس/یونینز
- `_Alignof`،`_Alignas`- سیدھ کنٹرول
- عام انتخاب:`_Generic(x, int: ..., default: ...)`
- یونیکوڈ سپورٹ:`<uchar.h>`
- اختیاری VLA سپورٹ (ایمبیڈڈ خدشات کی وجہ سے اختیاری بنایا گیا)
### C23 — The Renaissance (2024)
-`nullptr`- صفر پوائنٹر مستقل (`NULL` میکرو کی جگہ لے لیتا ہے)
-`typeof`- قسم کا اندازہ
-`constexpr`- مستقل اظہار
-`#embed`— مرتب وقت پر بائنری ڈیٹا کو سرایت کریں۔
-`[[attribute]]`نحو (C23 طرز کی خصوصیات)
-`true`/`false`بطور مطلوبہ الفاظ (اب`<stdbool.h>`کی ضرورت نہیں ہے)
-`auto`قسم کا اندازہ
-`static_assert`(بغیر انڈر سکور)
-`alignof`(بغیر انڈر سکور)
- پہلے سے طے شدہ`int`واپسی کو ہٹا دیا گیا۔
## معیاری عمل
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## مطابقت کا فلسفہ
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## پری پروسیسر ارتقاء
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## ٹائپ سسٹم ارتقاء
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## ماحولیاتی نظام کا اثر
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
