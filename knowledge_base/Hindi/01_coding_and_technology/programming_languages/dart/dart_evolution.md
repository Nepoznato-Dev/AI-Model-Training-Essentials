---
# Metadata
title: "Dart — Version History & Evolution"
description: "Comprehensive version history and evolution of Dart from 1.0 to modern Dart."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [dart, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# डार्ट - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| 1.0 | 2013 | आरंभिक रिलीज़ (गूगल, लार्स बाक और कैस्पर लुंड) |
| 1.2 | 2014 | Dart2JS कंपाइलर सुधार |
| 1.3 | 2014 | `async`/`await`समर्थन |
| 1.4 | 2014 |  `enum`, मिश्रण सुधार |
| 1.5 | 2014 | जेनरेटर (`sync*`, `async*`) |
| 1.6 | 2014 | `Future`सुधार |
| 1.8 | 2014 | `dart:io`सुधार |
| 1.9 | 2015 | सशक्त मोड (ऑप्ट-इन) |
| 1.11 | 2015 | `Future.then`सुधार |
| 1.12 | 2015 | **मजबूत मोड** लागू |
| 2.0 | 2018 | **प्रमुख**: ध्वनि प्रकार प्रणाली,`null`सुरक्षा तैयारी, संग्रह पुनर्लेखन |
| 2.1 | 2018 | `int`/`double`एकीकरण,`await for`|
| 2.2 | 2019 | `Set`शाब्दिक,`const`संग्रह में सुधार |
| 2.3 | 2019 | संग्रह `if`, संग्रह `for`, स्प्रेड ऑपरेटर`...`|
| 2.6 | 2019 | विस्तार विधियाँ |
| 2.7 | 2020 | डिफ़ॉल्ट नामित पैरामीटर |
| 2.10 | 2020 | **ध्वनि शून्य सुरक्षा** (ऑप्ट-इन) |
| 2.12 | 2021 | **डिफ़ॉल्ट रूप से शून्य सुरक्षा सक्षम** |
| 2.13 | 2021 | कंस्ट्रक्टर टियर-ऑफ़ |
| 2.14 | 2021 | `late`सुधार, अहस्ताक्षरित पूर्णांक |
| 2.15 | 2021 | कंस्ट्रक्टर टियर-ऑफ़ स्थिर, सामान्य फ़ंक्शन प्रकार |
| 2.17 | 2022 | **सुपर पैरामीटर**, उन्नत एनम |
| 2.18 | 2022 | उन्नत प्रकार का अनुमान |
| 2.19 | 2023 | रिकॉर्ड और पैटर्न (पूर्वावलोकन) |
| 3.0 | 2023 | **प्रमुख**: रिकॉर्ड, पैटर्न, वर्ग संशोधक,`switch`अभिव्यक्ति |
| 3.1 | 2023 | पैटर्न में सुधार, सीलबंद कक्षाएं |
| 3.2 | 2023 | स्थैतिक विश्लेषण सुधार |
| 3.3 | 2024 | एक्सटेंशन प्रकार,`switch`अभिव्यक्ति सुधार |
| 3.4 | 2024 | `if`तत्व,`case`सुधार |
| 3.5 | 2024 | मैक्रोज़ (पूर्वावलोकन), आगे भाषा परिशोधन |
| 3.6 | 2025 | निरंतर विकास |
## प्रमुख मील के पत्थर
### डार्ट 1.x - प्रारंभिक वर्ष (2013-2017)
- **2013**: Google ने डार्ट जारी किया - जो संरचित वेब प्रोग्रामिंग के लिए डिज़ाइन किया गया है
- **लक्ष्य**: वेब विकास के लिए जावास्क्रिप्ट बदलें (महत्वाकांक्षा बाद में बदल गई)
- **1.0**: कक्षाएं, इंटरफेस, आइसोलेट्स, वैकल्पिक टाइपिंग
- **1.3**:`async`/`await`समर्थन
- **1.9**: सशक्त मोड (ऑप्ट-इन सख्त टाइपिंग)
- डार्ट वीएम का क्रोमियम में कुछ समय के लिए उपयोग किया गया, फिर हटा दिया गया
### द फ़्लटर पिवोट (2017-2018)
- **2017**: फ़्लटर फ्रेमवर्क की घोषणा - डार्ट यूआई भाषा बन गई
- डार्ट को अपना उद्देश्य मिल गया: क्रॉस-प्लेटफ़ॉर्म मोबाइल/डेस्कटॉप/वेब विकास
- **2.0 (2018)**: पूर्ण पुनर्लेखन - ध्वनि प्रकार प्रणाली, आधुनिक संग्रह
### डार्ट 2.x — मॉडर्न डार्ट (2018–2023)
- **2.0**: ध्वनि प्रकार प्रणाली, डिफ़ॉल्ट रूप से अब`dynamic`नहीं
- **2.3**: संग्रह`if`/ `for`, स्प्रेड ऑपरेटर - फ़्लटर विजेट ट्री के लिए बढ़िया
- **2.6**: विस्तार विधियाँ
- **2.10**: ध्वनि शून्य सुरक्षा (ऑप्ट-इन)
- **2.12**: **डिफ़ॉल्ट रूप से अशक्त सुरक्षा सक्षम** -`?`अशक्त प्रकार
- **2.17**: सुपर पैरामीटर (`super.x`), उन्नत एनम
### डार्ट 3.x - रिकॉर्ड्स और पैटर्न (2023-वर्तमान)
- **3.0 (2023)**: **रिकॉर्ड्स** (गुमनाम डेटा वाहक), **पैटर्न** (डिस्ट्रक्चरिंग), **क्लास संशोधक** (`sealed`,`final`,`interface`,`base`),
- **3.3 (2024)**: एक्सटेंशन प्रकार (शून्य-लागत रैपर)
- **3.5 (2024)**: मैक्रोज़ पूर्वावलोकन - संकलन-समय मेटाप्रोग्रामिंग
## सिंटेक्स इवोल्यूशन
```dart
// Dart 1.x: Verbose, JavaScript-like
class Person {
  String name;
  int age;
  Person(this.name, this.age);
}

// Dart 2.0: Sound types
Person createPerson(String name, int age) {
  return Person(name, age);
}

// Dart 2.3: Collection if/for, spread
var widgets = [
  if (showHeader) HeaderWidget(),
  for (var item in items) ItemWidget(item),
  ...otherWidgets,
];

// Dart 2.6: Extension methods
extension StringX on String {
  String get shout => toUpperCase() + '!';
}

// Dart 2.12: Null safety
String? nullable;     // can be null
String nonNullable;   // cannot be null (enforced)

// Dart 2.17: Super parameters, enhanced enums
class NamedPerson extends Person {
  NamedPerson({super.name, super.age});  // pass to super constructor
}

enum Status {
  active('Active'),
  inactive('Inactive');
  final String label;
  const Status(this.label);
}

// Dart 3.0: Records and patterns
(String, int) getNameAndAge() => ('Alice', 30);

sealed class Shape {}
class Circle extends Shape { final double radius; Circle(this.radius); }
class Rect extends Shape { final double w, h; Rect(this.w, this.h); }

String describe(Shape s) => switch (s) {
  Circle(radius: var r) => 'Circle($r)',
  Rect(w: var w, h: var h) => 'Rect(${w}x${h})',
};
```

## टाइप सिस्टम इवोल्यूशन
```
Dart 1.0:  Optional types (annotations only)
Dart 1.9:  Strong mode (opt-in)
Dart 2.0:  Sound type system (enforced)
Dart 2.10: Sound null safety (opt-in)
Dart 2.12: Null safety by default (? nullable, ! assert)
Dart 2.15: Generic function types
Dart 3.0:  Records, sealed classes, patterns, class modifiers
Dart 3.3:  Extension types (zero-cost wrappers)
Dart 3.5:  Macros (compile-time metaprogramming)
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## पारिस्थितिकी तंत्र का विकास
```
2013: Dart 1.0 released by Google
2015: AngularDart — Google uses Dart internally
2017: Flutter announced — Dart finds its purpose
2018: Dart 2.0 — sound type system
2021: Dart 2.12 — null safety
2022: Flutter 3 — iOS, Android, Web, Desktop, Embedded
2023: Dart 3.0 — records, patterns, sealed classes
2025: Flutter + Dart power apps from BMW, Alibaba, Google Pay, Toyota
       pub.dev hosts 30,000+ packages
       Dart runs on: mobile (Flutter), web (dart2wasm), server (dart:io), embedded
```
