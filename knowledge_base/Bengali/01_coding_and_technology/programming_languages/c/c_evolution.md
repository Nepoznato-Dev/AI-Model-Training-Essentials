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

# সি — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| K&R C | 1972-78 | অরিজিনাল সি (কার্নিগান ও রিচি) |
| C89/C90 | 1989/90 | প্রথম ANSI/ISO মান |
| C95 | 1995 | সংশোধনী 1:`wchar.h`, ডিগ্রাফ |
| C99 | 1999 | `//`মন্তব্য,`inline`,`bool`, VLAs, মনোনীত ইনিশিয়ালাইজার |
| C11 | 2011 | পরমাণু, থ্রেড,`_Static_assert`, বেনামী কাঠামো/ইউনিয়ন |
| C17 | 2018 | ত্রুটি সংশোধন (কোন নতুন বৈশিষ্ট্য নেই) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, গুণাবলী |
## প্রধান মাইলফলক
### K&R C (1972-1989)
- **1972**: ডেনিস রিচি ইউনিক্সের জন্য বেল ল্যাবসে সি তৈরি করেন
- **1978**: কার্নিঘান এবং রিচি "দ্য সি প্রোগ্রামিং ল্যাঙ্গুয়েজ" প্রকাশ করেন
- মূল বৈশিষ্ট্য:`struct`,`int`,`char`, পয়েন্টার, ফাংশন,`#include`
-`void`নেই,`enum`নেই,`unsigned`নেই,`const`নেই
### C89/C90 — দ্য স্ট্যান্ডার্ড (1989)
- প্রথম ANSI মান (ANSI X3.159-1989)
- যোগ করা হয়েছে:`void`,`enum`,`const`,`volatile`, ফাংশন প্রোটোটাইপ,`signed`
- "স্বর্ণযুগ" — বহনযোগ্য, ব্যাপকভাবে গৃহীত
- এখনও অনেক এমবেডেড সিস্টেমের জন্য বেসলাইন
### C99 — আধুনিক C (1999)
-`//`একক-লাইন মন্তব্য
-`inline`ফাংশন
-`<stdbool.h>`এর মাধ্যমে`bool`
- পরিবর্তনশীল দৈর্ঘ্যের অ্যারে (VLAs)
- মনোনীত ইনিশিয়ালাইজার:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— লুপে ঘোষণা
-`<stdint.h>`: `int32_t`, `uint64_t`, ইত্যাদি।
-`restrict`কীওয়ার্ড
- ভ্যারিয়াডিক ম্যাক্রো
- যৌগিক আক্ষরিক
### C11 — নিরাপত্তা ও সমঝোতা (2011)
-`<stdatomic.h>`- পারমাণবিক অপারেশন
-`<threads.h>`- থ্রেড সমর্থন
-`_Static_assert`— কম্পাইল-টাইম দাবী
- নেস্টেড স্ট্রাকটে বেনামী স্ট্রাকস/ইউনিয়ন
-`_Alignof`,`_Alignas`- প্রান্তিককরণ নিয়ন্ত্রণ
- জেনেরিক নির্বাচন:`_Generic(x, int: ..., default: ...)`
- ইউনিকোড সমর্থন:`<uchar.h>`
- ঐচ্ছিক VLA সমর্থন (এমবেডেড উদ্বেগের কারণে ঐচ্ছিক করা হয়েছে)
### C23 — দ্য রেনেসাঁ (2024)
-`nullptr`— নাল পয়েন্টার ধ্রুবক (`NULL` ম্যাক্রো প্রতিস্থাপন করে)
-`typeof`— টাইপ ইনফারেন্স
-`constexpr`— ধ্রুবক অভিব্যক্তি
-`#embed`— কম্পাইলের সময় বাইনারি ডেটা এম্বেড করুন
-`[[attribute]]`সিনট্যাক্স (C23-শৈলী বৈশিষ্ট্য)
-`true`/`false`কীওয়ার্ড হিসাবে (আর প্রয়োজন নেই `<stdbool.h>`)
-`auto`প্রকার অনুমান
-`static_assert`(আন্ডারস্কোর ছাড়া)
-`alignof`(আন্ডারস্কোর ছাড়া)
- ডিফল্ট`int`রিটার্ন সরানো হয়েছে
## স্ট্যান্ডার্ড প্রক্রিয়া
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## সামঞ্জস্য দর্শন
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## প্রিপ্রসেসর বিবর্তন
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## টাইপ সিস্টেম বিবর্তন
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## ইকোসিস্টেমের প্রভাব
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
