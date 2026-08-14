---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [perl, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# पर्ल - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| 1.0 | 1987 | आरंभिक रिलीज़ (लैरी वॉल) |
| 2.0 | 1988 | `study`फ़ंक्शन, बेहतर रेगेक्स |
| 3.0 | 1989 | `my`वेरिएबल्स (लेक्सिकल स्कोपिंग) |
| 4.0 | 1991 | `O'Reilly`"प्रोग्रामिंग पर्ल" (कैमल बुक) |
| 5.0 | 1994 | **प्रमुख**: मॉड्यूल, संदर्भ, समापन,`use strict`|
| 5.6 | 2000 | `our`,`state`(बाद में),`v-strings`,`y2k`फिक्स |
| 5.8 | 2002 | **यूनिकोड समर्थन**,`ithreads`,`open`प्रगति |
| 5.10 | 2007 | `say`,`//`परिभाषित-या,`given`/`when`,`~~`स्मार्टमैच |
| 5.12 | 2010 | `package NAME VERSION`,`...`(यदा-यदा), यूनिकोड 5.2 |
| 5.14 | 2011 | `s///r`(गैर-विनाशकारी प्रतिस्थापन),`package`सुधार |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | लेक्सिकल `$_`, हैश रैंडमाइजेशन, सशर्त में`my`|
| 5.20 | 2014 | **सबरूटीन हस्ताक्षर** (प्रायोगिक),`%hash`स्लाइसिंग |
| 5.22 | 2015 | `&`डीरेफ़रेंसिंग,`<<>>`(सुरक्षित खुला) |
| 5.24 | 2016 | पोस्टफ़िक्स डीरेफ़रेंसिंग स्थिर |
| 5.26 | 2017 | **`while` में लेक्सिकल`$_`**,`@INC`में`.`हटा दिया गया (सुरक्षा) |
| 5.28 | 2018 | कुंजी/मूल्य स्लाइस पर यूनिकोड 10.0,`delete`|
| 5.30 | 2019 | `my``for` /`while`स्थितियों में |
| 5.32 | 2020 | `isa`ऑपरेटर, यूनिकोड 13.0 |
| 5.34 | 2021 | `try`/`catch`(प्रायोगिक),`defer`ब्लॉक |
| 5.36 | 2022 | **`use v5.36`**: हस्ताक्षर सक्षम,`$_`डिफ़ॉल्ट,`defer`|
| 5.38 | 2023 | `class`कीवर्ड (प्रायोगिक),`try`/`catch`स्थिर |
| 5.40 | 2024 | `^`बिटवाइज़ ऑपरेटर,`for`सूची में सुधार |
| 5.42 | 2025 | निरंतर विकास |
## प्रमुख मील के पत्थर
### पर्ल 1-4: द स्क्रिप्टिंग एरा (1987-1993)
- **1987**: लैरी वॉल ने पर्ल जारी किया - "प्रैक्टिकल एक्सट्रैक्शन एंड रिपोर्ट लैंग्वेज"
- **लक्ष्य**: sed, awk, grep,shell को एक शक्तिशाली स्क्रिप्टिंग टूल में संयोजित करें
- **3.0**: लेक्सिकल स्कोपिंग (`my`)
- **4.0**: द कैमल बुक - सिस्टम एडमिन कार्यों के लिए पर्ल को व्यापक रूप से अपनाया जाता है
### पर्ल 5: द गोल्डन एज (1994-2019)
- **5.0 (1994)**: पूर्ण पुनर्लेखन - **मॉड्यूल**, **संदर्भ**, **क्लोजर**, **ऑब्जेक्ट**
- **5.6 (2000)**: `our`, वी-स्ट्रिंग्स
- **5.8 (2002)**: **यूनिकोड समर्थन**, दुभाषिया धागे (`ithreads`)
- **5.10 (2007)**:`say`,`//`(परिभाषित-या),`given`/`when`(स्विच), स्मार्टमैच
- **5.12–5.28**: वृद्धिशील सुधार, यूनिकोड उन्नयन
### मॉडर्न पर्ल (2020–मौजूदा)
- **5.32 (2020)**:`isa`ऑपरेटर (क्लीनर टाइप चेकिंग)
- **5.34 (2021)**:`try`/`catch`(प्रयोगात्मक),`defer`ब्लॉक
- **5.36 (2022)**: **`use v5.36`** - हस्ताक्षर डिफ़ॉल्ट रूप से सक्षम,`$_`डिफ़ॉल्ट,`defer`
- **5.38 (2023)**:`class`कीवर्ड (प्रयोगात्मक - अंतर्निहित OOP),`try`/`catch`स्थिर
- **5.40 (2024)**: बिटवाइज़ ऑपरेटर सुधार
## सिंटेक्स इवोल्यूशन
```perl
# Perl 1-4: Basic scripting
#!/usr/bin/perl
$name = "World";
print "Hello, $name\n";

# Perl 5.0: References, closures, modules
use strict;
use warnings;
my $greeting = sub { "Hello, $_[0]" };
print $greeting->("World");

# Perl 5.8: Unicode
use utf8;
my $text = "café";

# Perl 5.10: say, defined-or
use v5.10;
say "Hello!";
my $value = $input // 'default';

# Perl 5.20: Subroutine signatures (experimental)
use experimental 'signatures';
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.36: Modern Perl
use v5.36;
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.38: class keyword (experimental)
use experimental 'class';
class Dog {
    field $name :param;
    field $breed :param;
    method bark { say "$name says Woof!" }
}
my $dog = Dog->new(name => "Rex", breed => "Lab");
```

## सीपीएएन पारिस्थितिकी तंत्र
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## पारिस्थितिकी तंत्र का विकास
```
1987: Perl 1.0 — sysadmin scripting
1994: Perl 5.0 — modules, OOP, the web CGI era
1995: CPAN launched — module ecosystem
2000: Perl powers the early web (CGI scripts)
2002: Perl 5.8 — Unicode, ithreads
2005: Catalyst, Dancer — web frameworks
2007: Perl 5.10 — modern syntax additions
2010: Moose — modern OOP (meta-object protocol)
2022: Perl 5.36 — modern defaults
2025: Perl still powers sysadmin, bioinformatics, legacy web apps
       CPAN: 200,000+ modules; used by cPanel, DuckDuckGo
```
