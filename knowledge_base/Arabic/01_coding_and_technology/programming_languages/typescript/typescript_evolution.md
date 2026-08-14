<!--
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

-->
# TypeScript — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | تاريخ الإصدار | الموضوع الرئيسي |
|---------|------------|-----------|
| 0.8 | أكتوبر 2012 | الإصدار العام الأولي (أندرس هيجلسبيرج) |
| 0.9 | أبريل 2013 | الأدوية العامة |
| 1.0 | أبريل 2014 | أول إصدار مستقر |
| 1.1 | نوفمبر 2014 | أداء المترجم |
| 1.4 | يناير 2015 | أنواع القوالب الحرفية (الأساسية)،`let`|
| 1.5 | يوليو 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | سبتمبر 2015 |  فئات `abstract`، دعم JSX |
| 1.7 | نوفمبر 2015 | `async/await`(هدف ES2017) |
| 1.8 | فبراير 2016 | سلاسل القالب الموسومة،`--strictNullChecks`|
| 2.0 | سبتمبر 2016 | **التخصص**: أنواع الاتحاد/التقاطع،`never`,`keyof`,`protected`|
| 2.1 | ديسمبر 2016 | `keyof`, أنواع الخرائط , مولدات`async`|
| 2.2 | فبراير 2017 |  نوع `object`،`this`المحسن |
| 2.3 | أبريل 2017 | الإعدادات الافتراضية العامة، وضع`--strict`|
| 2.4 | يونيو 2017 | الأنواع الضعيفة، تعدادات السلسلة |
| 2.5 | سبتمبر 2017 | ربط الصيد الاختياري |
| 2.6 | أكتوبر 2017 | أنواع الوظائف الصارمة،`--strictFunctionTypes`|
| 2.7 | يناير 2018 | تعيين محدد (`!`)، تعدادات`const`|
| 2.8 | مارس 2018 | **الأنواع الشرطية**,`Exclude`,`Extract`|
| 2.9 | يونيو 2018 | `keyof`للأرقام/الرموز، أنواع`import()`|
| 3.0 | يوليو 2018 | **التخصص**: الصفوف في السكون، `unknown`، مراجع المشروع |
| 3.1 | سبتمبر 2018 | الأنواع المعينة على صفوف، صفائف`readonly`|
| 3.2 | نوفمبر 2018 |  انتشار `bigint`،`object`|
| 3.4 | مارس 2019 |  تأكيدات `const`، استدلال النوع ذو الترتيب الأعلى |
| 3.5 | مايو 2019 | `Omit`نوع المساعد |
| 3.7 | نوفمبر 2019 | **التسلسل الاختياري**، والدمج الفارغ، والأنواع العودية |
| 3.8 | فبراير 2020 |  واردات/صادرات `type-only`، حقول`#private`|
| 3.9 | مايو 2020 |  `// @ts-expect-error`، الاستدلال المحسن |
| 4.0 | أغسطس 2020 | **التخصص**: الصف المتغير، الصف المسمى، الأنواع الحرفية للقالب |
| 4.1 | نوفمبر 2020 | **أنواع النماذج الحرفية**، إعادة تعيين المفاتيح، الشرطية العودية |
| 4.2 | فبراير 2021 | الخصائص المجردة،`~`في الأنواع المعينة |
| 4.3 | يونيو 2021 | أنواع كتابة منفصلة، ​​الكلمة الأساسية`override`|
| 4.4 | أغسطس 2021 | توقيعات الرمز/الفهرس، تضييق تدفق التحكم |
| 4.5 | نوفمبر 2021 | `.d.ts`من`.js`،`await`في`.d.ts`|
| 4.6 | فبراير 2022 | اختبارات الوظائف ذات النطاق الكتلي، والأنواع الدقيقة لباقي الكائنات |
| 4.7 | مايو 2022 |  قيود`extends`لـ`infer`و ESM في`.ts`|
| 4.8 | أغسطس 2022 | تحسين تقليل التقاطع، إصلاحات`--strictNullChecks`|
| 4.9 | نوفمبر 2022 | ** مشغل `satisfies`**، تضييق`in`|
| 5.0 | مارس 2023 | **التخصص**: معلمات النوع `const`، والديكورات، وإصلاح`enum`|
| 5.1 | يونيو 2023 | أدوات ضبط النوع غير المرتبطة،`--exactOptionalPropertyTypes`|
| 5.2 | أغسطس 2023 |  إعلانات`using`(إدارة الموارد الصريحة) |
| 5.3 | نوفمبر 2023 | سمات الاستيراد، تضييق`switch true`|
| 5.4 | مارس 2024 |  الأداة المساعدة `NoInfer`، معلمات الإغلاق الضيقة |
| 5.5 | يونيو 2024 | مسندات النوع المستنتجة،`@`للتعبير العادي |
| 5.6 | سبتمبر 2024 |  `--erasableSyntaxOnly`، مساعدين التكرار |
| 5.7 | نوفمبر 2024 |  `--noCheck`، إكمال المسار |
| 5.8 | فبراير 2025 | تحسين`isolatedDeclarations`|
## المعالم الرئيسية
### الأيام الأولى (2012-2015)
- **0.8 (2012)**: أندرس هيجلسبيرج (منشئ C#) يقود TypeScript في Microsoft
- **1.0 (2014)**: إصدار مستقر؛ الطبقات والواجهات والأنواع الأساسية
- **1.5 (2015)**: ميزات ES6 — التدمير، مساحات الأسماء، `for...of`
### ثورة النوع (2016-2018)
- **2.0 (2016)**: أنواع الاتحاد، وأنواع التقاطع،`never`،`keyof`— يصبح نظام الكتابة في TypeScript فريدًا
- **2.8 (2018)**: الأنواع الشرطية — الأساس للبرمجة المتقدمة على مستوى النوع
- **3.0 (2018)**: صفوف في معلمات الراحة، نوع `unknown`، مراجع المشروع
### الآلة الكاتبة الحديثة (2019 إلى الوقت الحاضر)
- **3.7 (2019)**: تسلسل اختياري`?.`والدمج الفارغ`??`(قبل معيار JS!)
- **4.0 (2020)**: صفوف متغيرة، أنواع القوالب الحرفية
- **4.1 (2020)**: الأنواع الحرفية للقالب - معالجة السلسلة على مستوى النوع
- **4.9 (2022)**: عامل التشغيل`satisfies`- التحقق من الكتابة دون توسيع
- **5.0 (2023)**: معلمات النوع `const`، وأدوات الديكور (المرحلة 3)
- **5.2 (2023)**: إعلانات`using`- إدارة صريحة للموارد
## نوع تطور النظام
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

## تطور الديكور
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## تطور التكوين
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## نمو النظام البيئي
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## قرارات التصميم الرئيسية
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
