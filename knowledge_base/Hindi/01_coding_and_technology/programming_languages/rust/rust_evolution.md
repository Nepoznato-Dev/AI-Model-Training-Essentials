---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# जंग - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | रिलीज की तारीख | मुख्य विषय |
|--|----|----|
| 0.1 | जनवरी 2012 | पहला कंपाइलर (रस्टसी), कार्य-आधारित समवर्ती |
| 0.5 | 2012 | गुण आधारित प्रकार प्रणाली आकार लेती है |
| 0.6 | 2012 |`@`प्रबंधित बक्सों को हटाना |
| 0.7 | 2013 | `@`हटा दिया गया, स्वामित्व वाले बक्सों के लिए`~`|
| 0.8 | 2013 | लाइफटाइम एनोटेशन,`&mut`|
| 0.9 | जनवरी 2014 | अंतिम प्री-1.0 सफ़ाई |
| 0.10 | फ़रवरी 2014 | अंतिम प्री-1.0 रिलीज़ |
| 0.11 | अप्रैल 2014 |  `Box<T>`,`~T`का स्थान लेता है |
| 0.12 | मई 2014 | `io`मॉड्यूल पुनः लिखना शुरू होता है |
| 1.0 | 15 मई 2015 | **स्थिर रिलीज़** — "रस्ट 1.0" |
| 1.10 | अगस्त 2016 | `?`त्रुटि प्रसार (`try!` →`?`के रूप में) |
| 1.15 | फरवरी 2017 |`impl Trait`तैयारी के साथ स्थिर पर पहला जंग |
| 1.18 | जून 2017 |  `pub(crate)`, वृद्धिशील संकलन |
| 1.20 | अक्टूबर 2017 | संबद्ध स्थिरांक |
| 1.26 | मई 2018 | `impl Trait`तर्क/वापसी स्थिति में |
| 1.28 | सितंबर 2018 | वैश्विक आवंटनकर्ता |
| 1.31 | दिसंबर 2018 | **रस्ट 2018 संस्करण** — मॉड्यूल,`dyn Trait`|
| 1.34 | अप्रैल 2019 | वैकल्पिक रजिस्ट्रियां |
| 1.39 | नवंबर 2019 | `async/await`स्थिर पर |
| 1.44 | जुलाई 2020 | निदान में सुधार |
| 1.51 | अप्रैल 2021 | `const`जेनरिक (एमवीपी) |
| 1.56 | अक्टूबर 2021 | **रस्ट 2021 संस्करण** — समापन, IntoIterator |
| 1.59 | फरवरी 2022 | इनलाइन असेंबली |
| 1.62 | जून 2022 |  गणनाओं के लिए`#[default]`|
| 1.65 | दिसंबर 2022 | `let else`|
| 1.68 | मार्च 2023 |  `#[ffi_pure]`, प्रोफ़ाइल-निर्देशित अनुकूलन |
| 1.70 | जून 2023 | पृथक`crates.io`निर्भरताएँ |
| 1.74 | नवंबर 2023 | कार्गो ऑफ़लाइन मोड |
| 1.76 | फ़रवरी 2024 | **रस्ट 2024 संस्करण** —`gen`ब्लॉक,`unsafe extern`|
| 1.79 | जून 2024 | `LazyCell`,`LazyLock`|
| 1.82 | अक्टूबर 2024 | `unsafe`में`extern`ब्लॉक आवश्यक |
| 1.85 | फ़रवरी 2025 | जंग 2024 संस्करण स्थिर |
## प्रमुख मील के पत्थर
### प्री-1.0 (2010-2015)
- **2010**: मोज़िला में ग्रेडन होरे के साइड प्रोजेक्ट को गति मिली
- **2012**: पहला सार्वजनिक कंपाइलर; टाइप सिस्टम को बड़े पैमाने पर नया स्वरूप दिया गया है
- **2013**: स्वामित्व मॉडल स्पष्ट हुआ; `@`बक्से हटा दिए गए
- **2014**: रस्ट आरएफसी प्रक्रिया औपचारिक हो गई; समुदाय बढ़ता है
- **2015**: **1.0** — स्थिरता की गारंटी; "शून्य-लागत सार"
### विकास वर्ष (2015-2019)
- **2015**: कार्गो मानक पैकेज मैनेजर बन गया
- **2018**: **रस्ट 2018 संस्करण** — मॉड्यूल सिस्टम ओवरहाल, `dyn Trait`,`impl Trait`
- **2019**:`async/await`स्थिर स्थिति में है - एसिंक पारिस्थितिकी तंत्र शुरू होता है
### परिपक्वता (2020–मौजूदा)
- **2021**: **रस्ट 2021 संस्करण** - क्लोजर में फ़ील्ड को स्पष्ट करें, सरणियों के लिए `IntoIterator`
- **2024**: **रस्ट 2024 संस्करण** —`gen`ब्लॉक,`unsafe extern`आवश्यकताएँ
- **2025**: लिनक्स कर्नेल, एंड्रॉइड, विंडोज, एडब्ल्यूएस इंफ्रास्ट्रक्चर में जंग
## संस्करण प्रणाली
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## स्वामित्व विकास
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## एसिंक इवोल्यूशन
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## पारिस्थितिकी तंत्र का विकास
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## प्रमुख आरएफसी
| आरएफसी | वर्ष | फ़ीचर |
|------|------|------|
| 25 | 2013 | पैटर्न मिलान |
| 153 | 2014 | `Result`प्रकार |
| 217 | 2014 | `?`(कोशिश करें) ऑपरेटर |
| 460 | 2016 |  `?`,`try!`का स्थान लेता है |
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | रस्ट 2018 संस्करण |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`जेनेरिक |
| 3013 | 2020 | सशर्त संकलन की जाँच |
| 3517 | 2023 | `gen`ब्लॉक |