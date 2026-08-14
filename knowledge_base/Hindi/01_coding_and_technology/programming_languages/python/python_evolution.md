<!--
---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# पायथन - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | रिलीज की तारीख | मुख्य विषय |
|--|----|----|
| 1.0 | जनवरी 1994 | आरंभिक रिलीज |
| 1.5 | दिसंबर 1997 | कक्षाएं, अपवाद, मॉड्यूल |
| 2.0 | अक्टूबर 2000 | सूची समझ, कचरा संग्रहण |
| 2.2 | दिसम्बर 2001 | एकीकृत प्रकार (प्रकार/वर्ग), जेनरेटर |
| 2.5 | सितम्बर 2006 | `with`कथन, अभिव्यक्ति के रूप में`yield`|
| 2.6 | अक्टूबर 2008 | `bytes`,`future`आयात, 3 में संक्रमण |
| 2.7 | जुलाई 2010 | डिक्ट/सेट समझ,`argparse`|
| 3.0 | दिसम्बर 2008 | **ब्रेकिंग**:`print()`,`str`/`bytes`, इटरेटर |
| 3.3 | सितम्बर 2012 | `yield from`, नेमस्पेस पैकेज |
| 3.4 | मार्च 2014 | `asyncio`,`pathlib`,`enum`|
| 3.5 | सितम्बर 2015 |  `async/await`, प्रकार संकेत (PEP 484),`**`अनपैकिंग |
| 3.6 | दिसंबर 2016 | एफ-स्ट्रिंग्स,`async`समझ, ऑर्डर किए गए निर्देश |
| 3.7 | जून 2018 | `dataclasses`,`contextvars`, आरक्षित`async`|
| 3.8 | अक्टूबर 2019 | वालरस ऑपरेटर `:=`, स्थितीय-केवल पैरामीटर |
| 3.9 | अक्टूबर 2020 | डिक्ट यूनियन `|`, सामान्य प्रकार`list[int]`|
| 3.10 | अक्टूबर 2021 |  `match/case`, संरचनात्मक पैटर्न मिलान |
| 3.11 | अक्टूबर 2022 | अपवाद समूह,`Self`प्रकार, तेज़ CPython |
| 3.12 | अक्टूबर 2023 | प्रति-दुभाषिया जीआईएल तैयारी, प्रकार पैरामीटर सिंटैक्स |
| 3.13 | अक्टूबर 2024 | फ्री-थ्रेडेड मोड (प्रायोगिक), बेहतर आरईपीएल |
| 3.14 | अक्टूबर 2025 | नो-जीआईएल स्थिर, एनोटेशन का स्थगित मूल्यांकन |
## प्रमुख मील के पत्थर
### पायथन 2.x युग (2000-2020)
- **2.0**: हास्केल से प्रेरित समझ की सूची बनाएं; चक्रीय जीसी
- **2.2**:`object`बेस क्लास; `yield`कीवर्ड (जनरेटर)
- **2.5**:`with`कथन; `yield`अभिव्यक्ति बन जाता है
- **2.7**: अंतिम 2.x रिलीज़; तानाशाही समझ; `argparse`
- **जीवन का अंत**: 1 जनवरी, 2020
### पायथन 3.x रेवोल्यूशन (2008-वर्तमान)
- **3.0**: क्लीन ब्रेक - फ़ंक्शन के रूप में `print`,`str`बनाम `bytes`, सभी पुनरावर्तक दृश्य लौटाते हैं
- **3.5**:`async`/`await`सिंटैक्स;`typing`मॉड्यूल के साथ संकेत टाइप करें
- **3.6**: एफ-स्ट्रिंग्स (सर्वाधिक अनुरोधित सुविधा); `asyncio`स्थिर
- **3.8**: इनलाइन असाइनमेंट के लिए वालरस ऑपरेटर
- **3.10**: संरचनात्मक पैटर्न मिलान (`match` / `case`)
- **3.11**: 10-60% तेज;`except*`के साथ अपवाद समूह 
- **3.13**: प्रायोगिक फ्री-थ्रेडेड मोड (कोई जीआईएल नहीं)
## डिज़ाइन दर्शन विकास
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## प्रमुख पीईपी जिन्होंने अजगर को आकार दिया
| पीईपी | वर्ष | फ़ीचर |
|------|------|------|
| 20 | 2004 | पाइथॉन का ज़ेन |
| 257 | 2001 | डॉकस्ट्रिंग कन्वेंशन |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | जेनरेटर भाव |
| 342 | 2005 |  अभिव्यक्ति के रूप में `yield`,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | संकेत टाइप करें |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | एफ-स्ट्रिंग्स |
| 572 | 2018 | वालरस ऑपरेटर`:=`|
| 622 | 2020 | संरचनात्मक पैटर्न मिलान |
| 654 | 2021 | अपवाद समूह |
| 684 | 2022 | प्रति-दुभाषिया जीआईएल |
| 703 | 2023 | जीआईएल को वैकल्पिक बनाना |
## प्रदर्शन विकास
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## सामुदायिक एवं पारिस्थितिकी तंत्र विकास
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
