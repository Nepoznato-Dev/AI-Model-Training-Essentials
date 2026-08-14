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
# টাইপস্ক্রিপ্ট — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | মুক্তির তারিখ | মূল থিম |
|---------|---------------|------------|
| 0.8 | অক্টোবর 2012 | প্রাথমিক প্রকাশ্য প্রকাশ (Anders Hejlsberg) |
| 0.9 | এপ্রিল 2013 | জেনেরিক |
| 1.0 | এপ্রিল 2014 | প্রথম স্থিতিশীল মুক্তি |
| 1.1 | নভেম্বর 2014 | কম্পাইলার কর্মক্ষমতা |
| 1.4 | জানুয়ারী 2015 | টেমপ্লেট আক্ষরিক প্রকার (মৌলিক),`let`|
| 1.5 | জুলাই 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | সেপ্টেম্বর 2015 | `abstract`ক্লাস, JSX সমর্থন |
| 1.7 | নভেম্বর 2015 | `async/await`(ES2017 টার্গেট) |
| 1.8 | ফেব্রুয়ারী 2016 | ট্যাগ করা টেমপ্লেট স্ট্রিং,`--strictNullChecks`|
| 2.0 | সেপ্টেম্বর 2016 | **প্রধান**: ইউনিয়ন/ছেদের ধরন,`never`,`keyof`,`protected`|
| 2.1 | ডিসেম্বর 2016 | `keyof`, ম্যাপ করা প্রকার,`async`জেনারেটর |
| 2.2 | ফেব্রুয়ারী 2017 | `object`প্রকার, উন্নত`this`|
| 2.3 | এপ্রিল 2017 | জেনেরিক ডিফল্ট,`--strict`মোড |
| 2.4 | জুন 2017 | দুর্বল প্রকার, স্ট্রিং enums |
| 2.5 | সেপ্টেম্বর 2017 | ঐচ্ছিক ধরা বাঁধাই |
| 2.6 | অক্টোবর 2017 | কঠোর ফাংশন প্রকার,`--strictFunctionTypes`|
| 2.7 | জানুয়ারী 2018 | নির্দিষ্ট অ্যাসাইনমেন্ট (`!`),`const`enums |
| 2.8 | মার্চ 2018 | **শর্তগত প্রকার**,`Exclude`,`Extract`|
| 2.9 | জুন 2018 |  সাংখ্যিক/প্রতীকের জন্য `keyof`,`import()`প্রকার |
| 3.0 | জুলাই 2018 | **মেজর**: টিপলস ইন বিশ্রাম,`unknown`, প্রকল্পের উল্লেখ |
| 3.1 | সেপ্টেম্বর 2018 | টিপলে ম্যাপ করা প্রকার,`readonly`অ্যারে |
| 3.2 | নভেম্বর 2018 | `bigint`,`object`বিস্তার |
| 3.4 | মার্চ 2019 | `const`দাবী, উচ্চ-ক্রম প্রকার অনুমান |
| 3.5 | মে 2019 | `Omit`সাহায্যকারী প্রকার |
| 3.7 | নভেম্বর 2019 | **ঐচ্ছিক চেইনিং**, নালিশ কোলেসিং, রিকারসিভ প্রকার |
| 3.8 | ফেব্রুয়ারী 2020 | `type-only`আমদানি/রপ্তানি,`#private`ক্ষেত্র |
| 3.9 | মে 2020 | `// @ts-expect-error`, উন্নত অনুমান |
| 4.0 | আগস্ট 2020 | **মেজর**: ভ্যারিয়াডিক টিপল, লেবেলযুক্ত টিপল, টেমপ্লেট আক্ষরিক প্রকার |
| 4.1 | নভেম্বর 2020 | **টেমপ্লেট আক্ষরিক প্রকার**, কী রিম্যাপিং, পুনরাবৃত্তিমূলক শর্তাধীন |
| 4.2 | ফেব্রুয়ারী 2021 | বিমূর্ত বৈশিষ্ট্য, ম্যাপ করা প্রকারে`~`|
| 4.3 | জুন 2021 | আলাদা লেখার ধরন,`override`কীওয়ার্ড |
| 4.4 | আগস্ট 2021 | প্রতীক/সূচী স্বাক্ষর, নিয়ন্ত্রণ প্রবাহ সংকীর্ণ |
| 4.5 | নভেম্বর 2021 | `.js`থেকে `.d.ts`, `.d.ts`-এ`await`|
| 4.6 | ফেব্রুয়ারী 2022 | ব্লক-স্কোপড ফাংশন চেক, অবজেক্ট বিশ্রাম সঠিক প্রকার |
| 4.7 | মে 2022 | `extends``infer` , `.ts`-এ ESM-এর সীমাবদ্ধতা |
| 4.8 | আগস্ট 2022 | উন্নত ছেদ হ্রাস,`--strictNullChecks`সংশোধন |
| 4.9 | নভেম্বর 2022 | **`satisfies`অপারেটর**,`in`সংকীর্ণ |
| 5.0 | মার্চ 2023 | **মেজর**:`const`টাইপ প্যারাম, ডেকোরেটর,`enum`ওভারহল |
| 5.1 | জুন 2023 | সম্পর্কহীন টাইপ সেটার্স,`--exactOptionalPropertyTypes`|
| 5.2 | আগস্ট 2023 | `using`ঘোষণা (স্পষ্ট সম্পদ ব্যবস্থাপনা) |
| 5.3 | নভেম্বর 2023 | গুণাবলী আমদানি করুন,`switch true`সংকীর্ণ |
| 5.4 | মার্চ 2024 | `NoInfer`ইউটিলিটি, সংকীর্ণ ক্লোজার প্যারামস |
| 5.5 | জুন 2024 | অনুমিত প্রকারের পূর্বাভাস, regex এর জন্য`@`|
| 5.6 | সেপ্টেম্বর 2024 | `--erasableSyntaxOnly`, পুনরাবৃত্তিকারী সাহায্যকারী |
| 5.7 | নভেম্বর 2024 | `--noCheck`, পথ সমাপ্তি |
| 5.8 | ফেব্রুয়ারী 2025 | উন্নত`isolatedDeclarations`|
## প্রধান মাইলফলক
### প্রারম্ভিক দিন (2012-2015)
- **0.8 (2012): Anders Hejlsberg (C# creator) Microsoft-এ TypeScript এর নেতৃত্ব দিচ্ছেন
- **1.0 (2014): স্থিতিশীল প্রকাশ; ক্লাস, ইন্টারফেস, মৌলিক প্রকার
- **1.5 (2015): ES6 বৈশিষ্ট্য — ধ্বংস, নামস্থান, `for...of`
### টাইপ বিপ্লব (2016-2018)
- **2.0 (2016): ইউনিয়নের ধরন, ছেদের ধরন,`never`,`keyof`— টাইপস্ক্রিপ্টের টাইপ সিস্টেম অনন্য হয়ে ওঠে
- **2.8 (2018)**: শর্তসাপেক্ষ প্রকার — উন্নত টাইপ-লেভেল প্রোগ্রামিংয়ের ভিত্তি
- **3.0 (2018)**: বিশ্রামের প্যারামিটারে টিপলস,`unknown`প্রকার, প্রকল্পের উল্লেখ
### আধুনিক টাইপস্ক্রিপ্ট (2019-বর্তমান)
- **3.7 (2019)**: ঐচ্ছিক চেইনিং`?.`এবং শূন্য কোলেসিং`??`(JS স্ট্যান্ডার্ডের আগে!)
- **4.0 (2020)**: ভ্যারিয়াডিক টিপল, টেমপ্লেট আক্ষরিক প্রকার
- **4.1 (2020): টেমপ্লেট আক্ষরিক প্রকারগুলি — টাইপ-লেভেল স্ট্রিং ম্যানিপুলেশন
- **4.9 (2022):`satisfies`অপারেটর — প্রশস্ত না করে টাইপ চেকিং
- **5.0 (2023):`const`টাইপ প্যারামিটার, ডেকোরেটর (পর্যায় 3)
- **5.2 (2023):`using`ঘোষণা — সুস্পষ্ট সম্পদ ব্যবস্থাপনা
## টাইপ সিস্টেম বিবর্তন
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

## ডেকোরেটর বিবর্তন
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## কনফিগারেশন বিবর্তন
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## ইকোসিস্টেম বৃদ্ধি
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## মূল ডিজাইনের সিদ্ধান্ত
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
