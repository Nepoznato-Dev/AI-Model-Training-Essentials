<!--
---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [php, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# PHP - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| पीएचपी/एफआई | 1995 | व्यक्तिगत होम पेज टूल्स (रासमस लेरडोर्फ) |
| पीएचपी 3.0 | 1998 | पहला आधुनिक PHP; ज़ीव सुरस्की और एंडी गुटमैन फिर से लिखते हैं |
| पीएचपी 4.0 | 2000 | ज़ेंड इंजन, सत्र समर्थन, आउटपुट बफ़रिंग |
| पीएचपी 5.0 | 2004 | **OOP मॉडल**, PDO, SQLite, SOAP, इटरेटर्स |
| पीएचपी 5.1 | 2005 | पीडीओ विस्तार, प्रदर्शन में सुधार |
| पीएचपी 5.2 | 2006 | `json_encode`/`json_decode`,`filter`एक्सटेंशन |
| पीएचपी 5.3 | 2009 | **नामस्थान**, देर से स्थैतिक बाइंडिंग, समापन |
| पीएचपी 5.4 | 2012 | लघु सरणी सिंटैक्स `[]`, लक्षण, अंतर्निहित वेब सर्वर |
| पीएचपी 5.5 | 2013 | जेनरेटर,`yield`, वस्तुओं पर `list()`,`::class`|
| पीएचपी 5.6 | 2014 | विविध फलन, स्थिर अदिश व्यंजक |
| पीएचपी 7.0 | 2015 | **प्रमुख**: ज़ेंड इंजन 3, स्केलर प्रकार संकेत, रिटर्न प्रकार,`??`|
| पीएचपी 7.1 | 2016 | निरर्थक प्रकार,`void`वापसी, पुनरावर्तनीय, वर्ग स्थिर दृश्यता |
| पीएचपी 7.2 | 2017 | `object`प्रकार संकेत, पैरामीटर प्रकार चौड़ीकरण |
| पीएचपी 7.3 | 2018 | फ़ंक्शन कॉल में अनुगामी अल्पविराम,`JsonException`|
| पीएचपी 7.4 | 2019 | **टाइप किए गए गुण**, एरो फ़ंक्शंस, शून्य कोलेस्सिंग असाइनमेंट |
| पीएचपी 8.0 | 2020 | **प्रमुख**: JIT, नामित तर्क, मिलान अभिव्यक्ति, संघ प्रकार, विशेषताएँ |
| पीएचपी 8.1 | 2021 | एनम, फाइबर,`readonly`गुण, प्रतिच्छेदन प्रकार |
| पीएचपी 8.2 | 2022 | `readonly`कक्षाएं, DNF प्रकार,`null`/`false`/`true`स्टैंडअलोन प्रकार के रूप में |
| पीएचपी 8.3 | 2023 | टाइप किए गए वर्ग स्थिरांक,`#[\Override]`विशेषता,`json_validate`|
| पीएचपी 8.4 | 2024 | संपत्ति हुक,`#[\Deprecated]`विशेषता, असममित दृश्यता |
## प्रमुख मील के पत्थर
### PHP/FI और PHP 3 (1995-1999)
- **1995**: रैस्मस लेरडोर्फ ने "पर्सनल होम पेज टूल्स" जारी किया
- **1998**: PHP 3 — सुरस्की और गुटमैन्स द्वारा पूर्ण पुनर्लेखन; एक स्क्रिप्टिंग भाषा बन जाती है
- मुख्य विशेषताएं: HTML में एम्बेडेड, फॉर्म हैंडलिंग, डेटाबेस समर्थन
### PHP 4 - ज़ेंड इंजन (2000-2004)
- **ज़ेंड इंजन 1**: संकलित बाइटकोड, बहुत तेज़
- सत्र प्रबंधन, आउटपुट बफ़रिंग, नाशपाती
- पहला वास्तविक वेब डेवलपमेंट फ्रेमवर्क युग
### PHP 5 — ऑब्जेक्ट-ओरिएंटेड PHP (2004-2014)
- **5.0**: पूर्ण ओओपी पुनर्लेखन - कक्षाएं, इंटरफेस, अपवाद, पीडीओ
- **5.3**: नेमस्पेस (आधुनिक PHP के लिए महत्वपूर्ण), क्लोजर, लेट स्टैटिक बाइंडिंग
- **5.4**: लक्षण, लघु सरणी सिंटैक्स `[]`, अंतर्निहित वेब सर्वर
- **5.5**: जेनरेटर (`yield`), `finally`
### PHP 7 - प्रदर्शन क्रांति (2015-2019)
- **7.0**: ज़ेंड इंजन 3 - **2x तेज़**, स्केलर प्रकार की घोषणाएँ, रिटर्न प्रकार की घोषणाएँ
- **7.1**: अशक्त प्रकार (`?int`), शून्य रिटर्न प्रकार
- **7.4**: टाइप किए गए गुण, तीर फ़ंक्शन `fn() =>`, शून्य कोलेसिंग असाइनमेंट `??=`
### PHP 8 — आधुनिक PHP (2020–मौजूदा)
- **8.0**: JIT कंपाइलर, नामित तर्क, मिलान अभिव्यक्ति, यूनियन प्रकार, विशेषताएँ (`#[...]`), नलसेफ ऑपरेटर`?->`
- **8.1**: एनम, फाइबर (हल्के समवर्ती), केवल पढ़ने योग्य गुण, प्रतिच्छेदन प्रकार
- **8.2**: केवल पढ़ने योग्य कक्षाएं, डीएनएफ प्रकार,`null`/`false`/`true`स्टैंडअलोन प्रकार के रूप में
- **8.3**: टाइप किए गए वर्ग स्थिरांक,`#[\Override]`,`json_validate()`
- **8.4**: संपत्ति हुक, `#[\Deprecated]`, असममित दृश्यता
## टाइप सिस्टम इवोल्यूशन
```
PHP 4:    No type hints
PHP 5.0:  Class type hints
PHP 5.1:  Array type hint
PHP 7.0:  Scalar types (int, string, float, bool), return types
PHP 7.1:  Nullable types (?int), void, iterable
PHP 7.2:  object type
PHP 7.4:  Typed properties
PHP 8.0:  Union types (int|string), mixed
PHP 8.1:  Intersection types (A&B), never, first-class callable syntax
PHP 8.2:  DNF types ((A&B)|C), null/false/true standalone
PHP 8.3:  Typed class constants
PHP 8.4:  Property hooks (get/set)
```

## सिंटेक्स इवोल्यूशन
```php
// PHP 3/4: Basic scripting
$users = array(1, 2, 3);

// PHP 5.4: Short array syntax
$users = [1, 2, 3];

// PHP 5.3: Namespaces
namespace App\Models;

// PHP 7.0: Scalar types
function add(int $a, int $b): int { return $a + $b; }

// PHP 7.4: Arrow functions
$doubled = array_map(fn($x) => $x * 2, $numbers);

// PHP 8.0: Named arguments, match
$result = process(value: $input, strict: true);
$label = match($status) { 0 => 'inactive', 1 => 'active', default => 'unknown' };

// PHP 8.1: Enums
enum Status: string { case Active = 'active'; case Inactive = 'inactive'; }

// PHP 8.4: Property hooks
class User {
    public string $name { get => strtoupper($this->name); set; }
}
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## पारिस्थितिकी तंत्र का विकास
```
1995: PHP/FI — personal tool
2000: PHP 4 + PEAR — package management begins
2004: PHP 5 + OOP — enterprise adoption
2008: Composer (dependency management) — modern PHP ecosystem
2011: Laravel framework — elegant PHP
2015: PHP 7 — performance revolution
2020: PHP 8 — JIT, modern features
2025: PHP powers ~75% of websites with known server-side language
       WordPress, Wikipedia, Slack, Mailchimp all run on PHP
```
