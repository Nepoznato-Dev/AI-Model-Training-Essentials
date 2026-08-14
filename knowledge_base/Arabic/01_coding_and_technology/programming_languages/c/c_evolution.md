---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| كيه آند آر سي | 1972–78 | الأصل C (كيرنيغان وريتشي) |
| C89/C90 | 1989/90 | أول معيار ANSI/ISO |
| C95 | 1995 | التعديل 1: `wchar.h`، الرسوم البيانية |
| C99 | 1999 |  تعليقات `//`، `inline`، `bool`، VLAs، المُهيئات المعينة |
| ج11 | 2011 | الذرات، الخيوط، `_Static_assert`، الهياكل/النقابات المجهولة |
| ج17 | 2018 | إصلاحات العيوب (لا توجد ميزات جديدة) |
| ج23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, السمات |
## المعالم الرئيسية
### كيه آند آر سي (1972–1989)
- **1972**: ابتكر دينيس ريتشي لغة C في Bell Labs لنظام Unix
- **1978**: نشر كيرنيغان وريتشي كتاب "لغة البرمجة C"
- الميزات الرئيسية: `struct`، `int`، `char`، المؤشرات، الوظائف،`#include`
- لا `void`، لا `enum`، لا `unsigned`، لا `const`
### C89/C90 — المعيار (1989)
- معيار ANSI الأول (ANSI X3.159-1989)
- تمت الإضافة: `void`، `enum`، `const`، `volatile`، نماذج الوظائف،`signed`
- "العصر الذهبي" - محمول ومعتمد على نطاق واسع
- لا يزال خط الأساس للعديد من الأنظمة المدمجة
### C99 — C الحديثة (1999)
- تعليقات`//`ذات السطر الواحد
- وظائف `inline`
-`bool`عبر`<stdbool.h>`
- صفائف متغيرة الطول (VLAs)
- المُهيئات المعينة:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— الإعلانات في الحلقة
-`<stdint.h>`: `int32_t`، `uint64_t`، إلخ.
- الكلمة الأساسية `restrict`
- وحدات الماكرو المتغيرة
- الحروف المركبة
### C11 — السلامة والتزامن (2011)
-`<stdatomic.h>`— العمليات الذرية
-`<threads.h>`— دعم الصفحات
-`_Static_assert`- تأكيدات وقت الترجمة
- الهياكل/النقابات المجهولة في الهياكل المتداخلة
-`_Alignof`,`_Alignas`— التحكم في المحاذاة
- التحديدات العامة:`_Generic(x, int: ..., default: ...)`
- دعم يونيكود:`<uchar.h>`
- دعم VLA اختياري (أصبح اختياريًا بسبب المخاوف المضمنة)
### C23 — عصر النهضة (2024)
-`nullptr`— ثابت المؤشر الفارغ (يحل محل الماكرو `NULL`)
-`typeof`— اكتب الاستدلال
-`constexpr`— التعبيرات الثابتة
-`#embed`- تضمين البيانات الثنائية في وقت الترجمة
- بناء جملة`[[attribute]]`(سمات نمط C23)
-`true`/`false`ككلمات رئيسية (لم تعد بحاجة إلى `<stdbool.h>`)
- استنتاج نوع `auto`
-`static_assert`(بدون شرطة سفلية)
-`alignof`(بدون شرطة سفلية)
- تمت إزالة الإرجاع الافتراضي `int`
## عملية المعايير
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## فلسفة التوافق
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## تطور المعالج
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## نوع تطور النظام
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## تأثير النظام البيئي
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
