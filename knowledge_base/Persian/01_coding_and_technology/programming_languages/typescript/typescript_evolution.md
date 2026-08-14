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
# TypeScript - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | تاریخ انتشار | تم کلید |
|---------|-------------|-----------|
| 0.8 | اکتبر 2012 | انتشار عمومی اولیه (آندرس هیلسبرگ) |
| 0.9 | آوریل 2013 | ژنریک |
| 1.0 | آوریل 2014 | اولین انتشار پایدار |
| 1.1 | نوامبر 2014 | عملکرد کامپایلر |
| 1.4 | ژانویه 2015 | انواع تحت اللفظی الگو (پایه)،`let`|
| 1.5 | جولای 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | سپتامبر 2015 |  کلاس های `abstract`، پشتیبانی JSX |
| 1.7 | نوامبر 2015 | `async/await`(هدف ES2017) |
| 1.8 | فوریه 2016 | رشته های قالب برچسب شده،`--strictNullChecks`|
| 2.0 | سپتامبر 2016 | **عمده**: انواع اتحاد/تقاطع، `never`، `keyof`،`protected`|
| 2.1 | دسامبر 2016 |  `keyof`، انواع نقشه برداری، ژنراتور`async`|
| 2.2 | فوریه 2017 |  نوع `object`، بهبود یافته`this`|
| 2.3 | آوریل 2017 | پیش فرض های عمومی، حالت`--strict`|
| 2.4 | ژوئن 2017 | انواع ضعیف، رشته ها |
| 2.5 | سپتامبر 2017 | صید اختیاری |
| 2.6 | اکتبر 2017 | انواع عملکرد دقیق،`--strictFunctionTypes`|
| 2.7 | ژانویه 2018 | تخصیص قطعی (`!`),`const`enums |
| 2.8 | مارس 2018 | **انواع شرطی**,`Exclude`,`Extract`|
| 2.9 | ژوئن 2018 | `keyof`برای عددی/نماد، انواع`import()`|
| 3.0 | جولای 2018 | **عمده**: تاپل ها در حالت استراحت، `unknown`، منابع پروژه |
| 3.1 | سپتامبر 2018 | انواع نگاشت شده روی تاپل ها، آرایه های`readonly`|
| 3.2 | نوامبر 2018 |  اسپرد`bigint`,`object`|
| 3.4 | مارس 2019 |  ادعاهای `const`، استنتاج نوع مرتبه بالاتر |
| 3.5 | می 2019 |  نوع کمکی`Omit`|
| 3.7 | نوامبر 2019 | **زنجیره سازی اختیاری**، ادغام بی اثر، انواع بازگشتی |
| 3.8 | فوریه 2020 | `type-only`واردات/صادرات، زمینه های`#private`|
| 3.9 | می 2020 |  `// @ts-expect-error`، استنتاج بهبود یافته |
| 4.0 | آگوست 2020 | **عمده**: تاپل های متغیر، تاپل های برچسب دار، انواع تحت اللفظی قالب |
| 4.1 | نوامبر 2020 | **انواع تحت اللفظی الگو**، نقشه برداری مجدد کلید، بازگشتی شرطی |
| 4.2 | فوریه 2021 | ویژگی های انتزاعی،`~`در انواع نقشه برداری |
| 4.3 | ژوئن 2021 | انواع نوشتار جداگانه، کلمه کلیدی`override`|
| 4.4 | آگوست 2021 | امضاهای نماد/شاخص، باریک شدن جریان کنترل |
| 4.5 | نوامبر 2021 | `.d.ts`از`.js`,`await`در`.d.ts`|
| 4.6 | فوریه 2022 | بررسی عملکرد با محدوده بلوک، انواع دقیق استراحت شی |
| 4.7 | می 2022 |  محدودیت های`extends`برای `infer`، ESM در`.ts`|
| 4.8 | آگوست 2022 | کاهش تقاطع بهبود یافته، رفع`--strictNullChecks`|
| 4.9 | نوامبر 2022 | ** اپراتور `satisfies`**،`in`باریک |
| 5.0 | مارس 2023 | **عمده**: پارام های نوع `const`، دکوراتورها، تعمیرات اساسی`enum`|
| 5.1 | ژوئن 2023 | تنظیم کننده نوع نامرتبط،`--exactOptionalPropertyTypes`|
| 5.2 | آگوست 2023 |  اعلامیه های`using`(مدیریت منابع صریح) |
| 5.3 | نوامبر 2023 | ویژگی های وارداتی، باریک شدن`switch true`|
| 5.4 | مارس 2024 |  ابزار `NoInfer`، پارامترهای بسته شدن باریک |
| 5.5 | ژوئن 2024 | محمولات نوع استنباط شده،`@`برای regex |
| 5.6 | سپتامبر 2024 |  `--erasableSyntaxOnly`، یاران تکرار کننده |
| 5.7 | نوامبر 2024 |  `--noCheck`، تکمیل مسیر |
| 5.8 | فوریه 2025 |`isolatedDeclarations`بهبود یافته |
## نقاط عطف اصلی
### روزهای اولیه (2012–2015)
- **0.8 (2012)**: آندرس هیلسبرگ (خالق C#) پیشتاز TypeScript در مایکروسافت است
- **1.0 (2014)**: انتشار پایدار؛ کلاس ها، رابط ها، انواع پایه
- **1.5 (2015)**: ویژگی های ES6 - تخریب ساختار، فضاهای نام، `for...of`
### انقلاب نوع (2016–2018)
- **2.0 (2016)**: انواع اتحادیه، انواع تقاطع، `never`،`keyof`- سیستم نوع TypeScript منحصر به فرد می شود
- **2.8 (2018)**: انواع مشروط - پایه و اساس برنامه نویسی در سطح نوع پیشرفته
- **3.0 (2018)**: تاپل ها در پارامترهای استراحت، نوع `unknown`، منابع پروژه
### TypeScript مدرن (2019–اکنون)
- **3.7 (2019)**: زنجیره اختیاری`?.`و خنثی کردن ادغام`??`(قبل از استاندارد JS!)
- **4.0 (2020)**: تاپل های متغیر، انواع تحت اللفظی الگو
- **4.1 (2020)**: انواع تحت اللفظی الگو - دستکاری رشته در سطح نوع
- **4.9 (2022)**: اپراتور`satisfies`— بررسی نوع بدون باز کردن
- **5.0 (2023)**: پارامترهای نوع `const`، دکوراتورها (مرحله 3)
- **5.2 (2023)**: اعلامیه های`using`- مدیریت منابع صریح
## تایپ سیستم تکامل
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

## تکامل دکوراتور
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## تکامل پیکربندی
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## رشد اکوسیستم
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## تصمیمات کلیدی طراحی
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
