<!--
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

-->
# सी - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| के एंड आर सी | 1972-78 | मूल सी (कर्निघन और रिची) |
| C89/C90 | 1989/90 | पहला एएनएसआई/आईएसओ मानक |
| C95 | 1995 | संशोधन 1: `wchar.h`, डिग्राफ |
| C99 | 1999 | `//`टिप्पणियाँ,`inline`,`bool`, VLAs, नामित इनिशियलाइज़र |
| सी11 | 2011 | परमाणु, धागे, `_Static_assert`, अनाम संरचनाएं/संघ |
| सी17 | 2018 | दोष सुधार (कोई नई सुविधाएँ नहीं) |
| सी23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, विशेषताएँ |
## प्रमुख मील के पत्थर
### के एंड आर सी (1972-1989)
- **1972**: डेनिस रिची ने यूनिक्स के लिए बेल लैब्स में सी बनाया
- **1978**: कर्निघन और रिची ने "द सी प्रोग्रामिंग लैंग्वेज" प्रकाशित की
- मुख्य विशेषताएं: `struct`, `int`, `char`, पॉइंटर्स, फ़ंक्शन,`#include`
- कोई`void`नहीं, कोई`enum`नहीं, कोई`unsigned`नहीं, कोई`const`नहीं
### C89/C90 - द स्टैंडर्ड (1989)
- पहला ANSI मानक (ANSI X3.159-1989)
- जोड़ा गया: `void`, `enum`, `const`, `volatile`, फ़ंक्शन प्रोटोटाइप,`signed`
- "स्वर्ण युग" - पोर्टेबल, व्यापक रूप से अपनाया गया
- अभी भी कई एम्बेडेड सिस्टम के लिए आधार रेखा है
### सी99 - मॉडर्न सी (1999)
-`//`एकल-पंक्ति टिप्पणियाँ
-`inline`फ़ंक्शन
-`bool`के माध्यम से`<stdbool.h>`
- परिवर्तनीय-लंबाई सरणियाँ (वीएलए)
- नामित इनिशियलाइज़र:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`- लूप में घोषणाएँ
-`<stdint.h>`:`int32_t`,`uint64_t`, आदि।
-`restrict`कीवर्ड
- वैरिएडिक मैक्रोज़
- यौगिक शाब्दिक
### C11 - सुरक्षा एवं समवर्ती (2011)
-`<stdatomic.h>`- परमाणु संचालन
-`<threads.h>`- थ्रेड समर्थन
-`_Static_assert`- संकलन-समय दावे
- नेस्टेड संरचनाओं में अनाम संरचनाएं/यूनियन
-`_Alignof`,`_Alignas`- संरेखण नियंत्रण
- सामान्य चयन:`_Generic(x, int: ..., default: ...)`
- यूनिकोड समर्थन:`<uchar.h>`
- वैकल्पिक वीएलए समर्थन (एम्बेडेड चिंताओं के कारण वैकल्पिक बनाया गया)
### C23 - द रेनेसां (2024)
-`nullptr`- शून्य सूचक स्थिरांक (`NULL` मैक्रो की जगह)
-`typeof`- प्रकार अनुमान
-`constexpr`- स्थिर अभिव्यक्ति
-`#embed`- संकलन समय पर बाइनरी डेटा एम्बेड करें
-`[[attribute]]`सिंटैक्स (C23-शैली विशेषताएँ)
-`true`/`false`कीवर्ड के रूप में (अब`<stdbool.h>`की आवश्यकता नहीं है)
-`auto`प्रकार का अनुमान
-`static_assert`(अंडरस्कोर के बिना)
-`alignof`(अंडरस्कोर के बिना)
- डिफ़ॉल्ट`int`रिटर्न हटा दिया गया
## मानक प्रक्रिया
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## अनुकूलता दर्शन
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## प्रीप्रोसेसर इवोल्यूशन
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## टाइप सिस्टम इवोल्यूशन
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## पारिस्थितिकी तंत्र पर प्रभाव
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
