---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# TypeScript - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | ریلیز کی تاریخ | کلیدی تھیم |
|---------|------------|------------|
| 0.8 | اکتوبر 2012 | ابتدائی عوامی ریلیز (Anders Hejlsberg) |
| 0.9 | اپریل 2013 | عام |
| 1.0 | اپریل 2014 | پہلی مستحکم رہائی |
| 1.1 | نومبر 2014 | کمپائلر کی کارکردگی |
| 1.4 | جنوری 2015 | سانچہ لغوی اقسام (بنیادی)،`let`|
| 1.5 | جولائی 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | ستمبر 2015 | `abstract`کلاسز، JSX سپورٹ |
| 1.7 | نومبر 2015 | `async/await`(ES2017 ہدف) |
| 1.8 | فروری 2016 | ٹیگ شدہ سانچے کے تار،`--strictNullChecks`|
| 2.0 | ستمبر 2016 | **بڑا**: یونین/چوراہے کی اقسام،`never`,`keyof`,`protected`|
| 2.1 | دسمبر 2016 | `keyof`, نقشہ شدہ اقسام،`async`جنریٹرز |
| 2.2 | فروری 2017 | `object`قسم، بہتر`this`|
| 2.3 | اپریل 2017 | عام ڈیفالٹس،`--strict`وضع |
| 2.4 | جون 2017 | کمزور اقسام، سٹرنگ enums |
| 2.5 | ستمبر 2017 | اختیاری کیچ بائنڈنگ |
| 2.6 | اکتوبر 2017 | سخت فنکشن کی اقسام،`--strictFunctionTypes`|
| 2.7 | جنوری 2018 | ڈیفینیٹ اسائنمنٹ (`!`) ,`const`enums |
| 2.8 | مارچ 2018 | **مشروط اقسام**،`Exclude`,`Extract`|
| 2.9 | جون 2018 | `keyof`عددی/علامت کے لیے،`import()`اقسام |
| 3.0 | جولائی 2018 | **میجر**: آرام میں ٹیپلز،`unknown`, پروجیکٹ حوالہ جات |
| 3.1 | ستمبر 2018 | ٹیپلز،`readonly`صفوں پر نقشہ شدہ اقسام |
| 3.2 | نومبر 2018 | `bigint`,`object`پھیلاؤ |
| 3.4 | مارچ 2019 | `const`دعوے، اعلیٰ ترتیب کی قسم کا اندازہ |
| 3.5 | مئی 2019 | `Omit`مددگار کی قسم |
| 3.7 | نومبر 2019 | **اختیاری زنجیریں**، nullish coalescing، recursive اقسام |
| 3.8 | فروری 2020 | `type-only`درآمدات/برآمدات،`#private`فیلڈز |
| 3.9 | مئی 2020 | `// @ts-expect-error`, بہتر اندازہ |
| 4.0 | اگست 2020 | **بڑا**: متغیر ٹیپلز، لیبل والے ٹیپلس، سانچے کی لغوی اقسام |
| 4.1 | نومبر 2020 | **ٹیمپلیٹ کی لغوی اقسام**، کلیدی ری میپنگ، تکرار کنڈیشنل |
| 4.2 | فروری 2021 | خلاصہ خصوصیات، نقشہ بندی کی اقسام میں`~`|
| 4.3 | جون 2021 | الگ الگ لکھنے کی اقسام،`override`کلیدی لفظ |
| 4.4 | اگست 2021 | علامت/اشاریہ کے دستخط، کنٹرول بہاؤ کو کم کرنا |
| 4.5 | نومبر 2021 | `.d.ts`سے`.js`,`await``.d.ts` میں |
| 4.6 | فروری 2022 | بلاک اسکوپڈ فنکشن چیکس، آبجیکٹ ریسٹ درست اقسام |
| 4.7 | مئی 2022 | `extends``infer` , ESM کے لیے`.ts`میں رکاوٹیں |
| 4.8 | اگست 2022 | بہتر انٹرسیکشن کمی،`--strictNullChecks`اصلاحات |
| 4.9 | نومبر 2022 | **`satisfies`آپریٹر**،`in`تنگ کرنا |
| 5.0 | مارچ 2023 | **میجر**:`const`قسم کے پیرامز، ڈیکوریٹرز،`enum`اوور ہال |
| 5.1 | جون 2023 | غیر متعلقہ قسم کے سیٹرز،`--exactOptionalPropertyTypes`|
| 5.2 | اگست 2023 | `using`اعلانات (واضح وسائل کا انتظام) |
| 5.3 | نومبر 2023 | امپورٹ اوصاف،`switch true`تنگ کرنا |
| 5.4 | مارچ 2024 | `NoInfer`افادیت، تنگ بندش پیرامیز |
| 5.5 | جون 2024 | تخمینہ شدہ قسم کی پیش گوئیاں،`@`برائے regex |
| 5.6 | ستمبر 2024 | `--erasableSyntaxOnly`, iterator مددگار |
| 5.7 | نومبر 2024 | `--noCheck`, راستے کی تکمیل |
| 5.8 | فروری 2025 | بہتر`isolatedDeclarations`|
## اہم سنگ میل
### ابتدائی دن (2012–2015)
- **0.8 (2012)**: اینڈرس ہیجلسبرگ (C# تخلیق کار) مائیکروسافٹ میں ٹائپ اسکرپٹ کی قیادت کرتے ہیں
- **1.0 (2014): مستحکم رہائی؛ کلاسز، انٹرفیس، بنیادی اقسام
- **1.5 (2015)**: ES6 خصوصیات — تخریب کاری، نام کی جگہیں، `for...of`
### قسم کا انقلاب (2016–2018)
- **2.0 (2016): یونین کی قسمیں، چوراہا کی قسمیں، `never`،`keyof`— TypeScript کا ٹائپ سسٹم منفرد ہو جاتا ہے
- **2.8 (2018)**: مشروط قسمیں - اعلی درجے کی قسم کی سطح کے پروگرامنگ کی بنیاد
- **3.0 (2018)**: باقی پیرامیٹرز میں ٹیپلز،`unknown`قسم، پروجیکٹ حوالہ جات
### جدید ٹائپ اسکرپٹ (2019–موجودہ)
- **3.7 (2019)**: اختیاری سلسلہ بندی`?.`اور`??`کو ختم کرنا (JS معیار سے پہلے!)
- **4.0 (2020)**: متغیر ٹیپلز، ٹیمپلیٹ کی لغوی اقسام
- **4.1 (2020)**: سانچے کی لغوی قسمیں — قسم کی سطح کے سٹرنگ ہیرا پھیری
- **4.9 (2022)**:`satisfies`آپریٹر — چوڑا کیے بغیر چیکنگ ٹائپ کریں
- **5.0 (2023)**:`const`قسم کے پیرامیٹرز، ڈیکوریٹر (مرحلہ 3)
- **5.2 (2023)**:`using`اعلانات — وسائل کا واضح انتظام
## ٹائپ سسٹم ارتقاء
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## ڈیکوریٹر ارتقاء
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## ترتیب ارتقاء
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## ماحولیاتی نظام کی نمو
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## ڈیزائن کے کلیدی فیصلے
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
