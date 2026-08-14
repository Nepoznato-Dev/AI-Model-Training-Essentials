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
# टाइपस्क्रिप्ट - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | रिलीज की तारीख | मुख्य विषय |
|--|----|----|
| 0.8 | अक्टूबर 2012 | आरंभिक सार्वजनिक रिलीज़ (एंडर्स हेज्ल्सबर्ग) |
| 0.9 | अप्रैल 2013 | जेनेरिक |
| 1.0 | अप्रैल 2014 | पहली स्थिर रिलीज़ |
| 1.1 | नवंबर 2014 | कंपाइलर प्रदर्शन |
| 1.4 | जनवरी 2015 | टेम्पलेट शाब्दिक प्रकार (बुनियादी),`let`|
| 1.5 | जुलाई 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | सितम्बर 2015 | `abstract`कक्षाएं, JSX समर्थन |
| 1.7 | नवंबर 2015 | `async/await`(ES2017 लक्ष्य) |
| 1.8 | फरवरी 2016 | टैग किए गए टेम्प्लेट स्ट्रिंग्स,`--strictNullChecks`|
| 2.0 | सितम्बर 2016 | **प्रमुख**: संघ/प्रतिच्छेदन प्रकार,`never`,`keyof`,`protected`|
| 2.1 | दिसंबर 2016 |  `keyof`, मैप किए गए प्रकार,`async`जनरेटर |
| 2.2 | फरवरी 2017 | `object`प्रकार, बेहतर`this`|
| 2.3 | अप्रैल 2017 | सामान्य डिफ़ॉल्ट,`--strict`मोड |
| 2.4 | जून 2017 | कमजोर प्रकार, स्ट्रिंग एनम |
| 2.5 | सितंबर 2017 | वैकल्पिक कैच बाइंडिंग |
| 2.6 | अक्टूबर 2017 | सख्त फ़ंक्शन प्रकार,`--strictFunctionTypes`|
| 2.7 | जनवरी 2018 | निश्चित असाइनमेंट (`!`),`const`एनम |
| 2.8 | मार्च 2018 | **सशर्त प्रकार**,`Exclude`,`Extract`|
| 2.9 | जून 2018 |  संख्यात्मक/प्रतीक के लिए `keyof`,`import()`प्रकार |
| 3.0 | जुलाई 2018 | **प्रमुख**: आराम में टुपल्स, `unknown`, परियोजना संदर्भ |
| 3.1 | सितंबर 2018 | टुपल्स पर मैप किए गए प्रकार,`readonly`सरणियाँ |
| 3.2 | नवंबर 2018 | `bigint`,`object`स्प्रेड |
| 3.4 | मार्च 2019 | `const`दावे, उच्च-क्रम प्रकार का अनुमान |
| 3.5 | मई 2019 | `Omit`सहायक प्रकार |
| 3.7 | नवंबर 2019 | **वैकल्पिक श्रृखंला**, अशक्त सहसंयोजन, पुनरावर्ती प्रकार |
| 3.8 | फरवरी 2020 | `type-only`आयात/निर्यात,`#private`फ़ील्ड |
| 3.9 | मई 2020 |  `// @ts-expect-error`, बेहतर अनुमान |
| 4.0 | अगस्त 2020 | **प्रमुख**: विविध टुपल्स, लेबल वाले टुपल्स, टेम्पलेट शाब्दिक प्रकार |
| 4.1 | नवंबर 2020 | **टेम्पलेट शाब्दिक प्रकार**, कुंजी रीमैपिंग, पुनरावर्ती सशर्त |
| 4.2 | फरवरी 2021 | सार गुण, मैप किए गए प्रकारों में`~`|
| 4.3 | जून 2021 | अलग लिखने के प्रकार,`override`कीवर्ड |
| 4.4 | अगस्त 2021 | प्रतीक/सूचकांक हस्ताक्षर, नियंत्रण प्रवाह संकुचन |
| 4.5 | नवंबर 2021 | `.d.ts`से`.js`,`await`से`.d.ts`|
| 4.6 | फरवरी 2022 | ब्लॉक-स्कोप्ड फ़ंक्शन जांच, ऑब्जेक्ट बाकी सटीक प्रकार |
| 4.7 | मई 2022 | `infer`के लिए`extends`बाधाएं,`.ts`में ESM |
| 4.8 | अगस्त 2022 | बेहतर चौराहे की कमी,`--strictNullChecks`को ठीक किया गया |
| 4.9 | नवंबर 2022 | **`satisfies`ऑपरेटर**,`in`संकुचन |
| 5.0 | मार्च 2023 | **प्रमुख**:`const`प्रकार के पैरामीटर, डेकोरेटर,`enum`ओवरहाल |
| 5.1 | जून 2023 | असंबद्ध प्रकार सेटर्स,`--exactOptionalPropertyTypes`|
| 5.2 | अगस्त 2023 | `using`घोषणाएँ (स्पष्ट संसाधन प्रबंधन) |
| 5.3 | नवंबर 2023 | आयात विशेषताएँ,`switch true`संकुचन |
| 5.4 | मार्च 2024 | `NoInfer`उपयोगिता, संकुचित समापन पैरामीटर |
| 5.5 | जून 2024 | अनुमानित प्रकार विधेय है, रेगेक्स के लिए`@`|
| 5.6 | सितंबर 2024 |  `--erasableSyntaxOnly`, पुनरावर्तक सहायक |
| 5.7 | नवंबर 2024 |  `--noCheck`, पथ पूर्णता |
| 5.8 | फ़रवरी 2025 | बेहतर`isolatedDeclarations`|
## प्रमुख मील के पत्थर
### शुरुआती दिन (2012-2015)
- **0.8 (2012)**: एंडर्स हेजलबर्ग (सी# निर्माता) माइक्रोसॉफ्ट में टाइपस्क्रिप्ट का नेतृत्व करते हैं
- **1.0 (2014)**: स्थिर रिलीज़; कक्षाएं, इंटरफ़ेस, बुनियादी प्रकार
- **1.5 (2015)**: ES6 विशेषताएं - डिस्ट्रक्चरिंग, नेमस्पेस, `for...of`
### प्रकार क्रांति (2016-2018)
- **2.0 (2016)**: यूनियन प्रकार, प्रतिच्छेदन प्रकार, `never`,`keyof`- टाइपस्क्रिप्ट का प्रकार सिस्टम अद्वितीय हो जाता है
- **2.8 (2018)**: सशर्त प्रकार - उन्नत प्रकार-स्तरीय प्रोग्रामिंग की नींव
- **3.0 (2018)**: बाकी मापदंडों में टुपल्स,`unknown`प्रकार, परियोजना संदर्भ
### आधुनिक टाइपस्क्रिप्ट (2019–मौजूदा)
- **3.7 (2019)**: वैकल्पिक चेनिंग`?.`और नलिश कोलेसिंग`??`(JS मानक से पहले!)
- **4.0 (2020)**: विविध टुपल्स, टेम्पलेट शाब्दिक प्रकार
- **4.1 (2020)**: टेम्पलेट शाब्दिक प्रकार - प्रकार-स्तरीय स्ट्रिंग हेरफेर
- **4.9 (2022)**:`satisfies`ऑपरेटर - बिना चौड़ीकरण के टाइप चेकिंग
- **5.0 (2023)**:`const`प्रकार के पैरामीटर, डेकोरेटर (चरण 3)
- **5.2 (2023)**:`using`घोषणाएँ - स्पष्ट संसाधन प्रबंधन
## टाइप सिस्टम इवोल्यूशन
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

## डेकोरेटर इवोल्यूशन
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## कॉन्फ़िगरेशन विकास
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## पारिस्थितिकी तंत्र का विकास
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## मुख्य डिज़ाइन निर्णय
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
