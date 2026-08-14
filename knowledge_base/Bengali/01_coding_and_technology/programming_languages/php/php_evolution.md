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
# পিএইচপি - সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| PHP/FI | 1995 | ব্যক্তিগত হোম পেজ টুলস (রাসমাস লারডর্ফ) |
| পিএইচপি 3.0 | 1998 | প্রথম আধুনিক পিএইচপি; জিভ সুরস্কি এবং অ্যান্ডি গুটম্যানস পুনর্লিখন |
| পিএইচপি 4.0 | 2000 | জেন্ড ইঞ্জিন, সেশন সমর্থন, আউটপুট বাফারিং |
| পিএইচপি 5.0 | 2004 | **OOP মডেল**, PDO, SQLite, SOAP, iterators |
| পিএইচপি 5.1 | 2005 | PDO এক্সটেনশন, কর্মক্ষমতা উন্নতি |
| পিএইচপি 5.2 | 2006 | `json_encode`/`json_decode`,`filter`এক্সটেনশন |
| পিএইচপি 5.3 | 2009 | **নেমস্পেস**, দেরিতে স্ট্যাটিক বাইন্ডিং, বন্ধ |
| পিএইচপি 5.4 | 2012 | সংক্ষিপ্ত অ্যারে সিনট্যাক্স`[]`, বৈশিষ্ট্য, অন্তর্নির্মিত ওয়েব সার্ভার |
| পিএইচপি 5.5 | 2013 | জেনারেটর,`yield`,`list()`বস্তুর উপর,`::class`|
| পিএইচপি 5.6 | 2014 | বৈচিত্র্যময় ফাংশন, ধ্রুবক স্কেলার এক্সপ্রেশন |
| পিএইচপি 7.0 | 2015 | **মেজর**: জেন্ড ইঞ্জিন 3, স্কেলার টাইপ ইঙ্গিত, রিটার্ন প্রকার,`??`|
| পিএইচপি 7.1 | 2016 | বাতিলযোগ্য প্রকার,`void`রিটার্ন, পুনরাবৃত্তিযোগ্য, ক্লাস ধ্রুবক দৃশ্যমানতা |
| পিএইচপি 7.2 | 2017 | `object`টাইপ ইঙ্গিত, প্যারামিটার টাইপ প্রশস্তকরণ |
| পিএইচপি 7.3 | 2018 | ফাংশন কলে ট্র্যালিং কমা,`JsonException`|
| পিএইচপি 7.4 | 2019 | **টাইপ করা বৈশিষ্ট্য**, তীর ফাংশন, নাল কোলেসিং অ্যাসাইনমেন্ট |
| পিএইচপি 8.0 | 2020 | **মেজর**: জেআইটি, নামযুক্ত আর্গুমেন্ট, মিল এক্সপ্রেশন, ইউনিয়নের ধরন, বৈশিষ্ট্য |
| পিএইচপি 8.1 | 2021 | Enums, fibers,`readonly`বৈশিষ্ট্য, ছেদ প্রকার |
| পিএইচপি 8.2 | 2022 | `readonly`ক্লাস, DNF প্রকার,`null`/`false`/`true`স্বতন্ত্র প্রকার হিসাবে |
| পিএইচপি 8.3 | 2023 | টাইপ করা ক্লাস কনস্ট্যান্ট,`#[\Override]`অ্যাট্রিবিউট,`json_validate`|
| পিএইচপি 8.4 | 2024 | প্রপার্টি হুক,`#[\Deprecated]`অ্যাট্রিবিউট, অ্যাসিমেট্রিক ভিজিবিলিটি |
## প্রধান মাইলফলক
### PHP/FI এবং PHP 3 (1995-1999)
- **1995**: রাসমাস লারডর্ফ "ব্যক্তিগত হোম পেজ টুলস" প্রকাশ করেছে
- **1998**: PHP 3 — সুরাস্কি এবং গুটম্যানস দ্বারা সম্পূর্ণ পুনর্লিখন; একটি স্ক্রিপ্টিং ভাষা হয়ে ওঠে
- মূল বৈশিষ্ট্য: HTML এ এমবেড করা, ফর্ম হ্যান্ডলিং, ডাটাবেস সমর্থন
### পিএইচপি 4 — জেন্ড ইঞ্জিন (2000-2004)
- **জেন্ড ইঞ্জিন 1**: কম্পাইল করা বাইটকোড, অনেক দ্রুত
- সেশন হ্যান্ডলিং, আউটপুট বাফারিং, PEAR
- প্রথম বাস্তব ওয়েব ডেভেলপমেন্ট ফ্রেমওয়ার্ক যুগ
### পিএইচপি 5 — অবজেক্ট-ওরিয়েন্টেড পিএইচপি (2004-2014)
- **5.0**: সম্পূর্ণ OOP পুনর্লিখন — ক্লাস, ইন্টারফেস, ব্যতিক্রম, PDO
- **5.3**: নামস্থান (আধুনিক PHP-এর জন্য গুরুত্বপূর্ণ), বন্ধ, দেরী স্ট্যাটিক বাইন্ডিং
- **5.4**: বৈশিষ্ট্য, সংক্ষিপ্ত অ্যারে সিনট্যাক্স`[]`, অন্তর্নির্মিত ওয়েব সার্ভার
- **5.5**: জেনারেটর (`yield`), `finally`
### PHP 7 — পারফরম্যান্স বিপ্লব (2015-2019)
- **7.0**: জেন্ড ইঞ্জিন 3 — **2x দ্রুত**, স্কেলার টাইপ ঘোষণা, রিটার্ন টাইপ ঘোষণা
- **7.1**: বাতিলযোগ্য প্রকার (`?int`), অকার্যকর রিটার্ন টাইপ
- **7.4**: টাইপ করা বৈশিষ্ট্য, তীর ফাংশন`fn() =>`, নাল কোলেসিং অ্যাসাইনমেন্ট `??=`
### পিএইচপি 8 — আধুনিক পিএইচপি (2020-বর্তমান)
- **8.0**: JIT কম্পাইলার, নামযুক্ত আর্গুমেন্ট, ম্যাচ এক্সপ্রেশন, ইউনিয়নের ধরন, বৈশিষ্ট্য (`#[...]`), নালসেফ অপারেটর`?->`
- **8.1**: এনাম, ফাইবার (হালকা একযোগে), শুধুমাত্র পঠনযোগ্য বৈশিষ্ট্য, ছেদ প্রকার
- **8.2**: শুধুমাত্র পঠনযোগ্য ক্লাস, DNF প্রকার,`null`/`false`/`true`স্বতন্ত্র প্রকার হিসাবে
- **8.3**: টাইপ করা ক্লাস ধ্রুবক,`#[\Override]`,`json_validate()`
- **8.4**: সম্পত্তির হুক,`#[\Deprecated]`, অসমমিত দৃশ্যমানতা
## টাইপ সিস্টেম বিবর্তন
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

## সিনট্যাক্স বিবর্তন
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

## মূল ডিজাইনের নীতি
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## ইকোসিস্টেম বৃদ্ধি
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
