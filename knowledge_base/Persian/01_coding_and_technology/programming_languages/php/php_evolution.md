---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# PHP - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| PHP/FI | 1995 | ابزارهای صفحه اصلی شخصی (راسموس لردورف) |
| PHP 3.0 | 1998 | اولین PHP مدرن. Zeev Suraski و Andi Gutmans بازنویسی می کنند |
| PHP 4.0 | 2000 | Zend Engine، پشتیبانی جلسه، بافر خروجی |
| PHP 5.0 | 2004 | **مدل OOP**، PDO، SQLite، SOAP، تکرار کننده |
| PHP 5.1 | 2005 | پسوند PDO، بهبود عملکرد |
| PHP 5.2 | 2006 |  پسوند`json_encode`/`json_decode`,`filter`|
| PHP 5.3 | 2009 | ** فضای نام**، پیوندهای استاتیک دیررس، بسته شدن |
| PHP 5.4 | 2012 | نحو آرایه کوتاه `[]`، صفات، وب سرور داخلی |
| PHP 5.5 | 2013 | ژنراتور`yield`,`list()`روی اشیاء,`::class`|
| PHP 5.6 | 2014 | توابع متغیر، عبارات اسکالر ثابت |
| PHP 7.0 | 2015 | **عمده**: Zend Engine 3، نکات نوع اسکالر، انواع بازگشت،`??`|
| PHP 7.1 | 2016 | انواع باطل، بازگشت `void`، قابل تکرار، مشاهده ثابت کلاس |
| PHP 7.2 | 2017 |  اشاره نوع `object`، نوع پارامتر تعریض |
| PHP 7.3 | 2018 | کاماهای دنباله دار در فراخوانی تابع،`JsonException`|
| PHP 7.4 | 2019 | **ویژگی های تایپ شده**، توابع پیکان، تخصیص ادغام تهی |
| PHP 8.0 | 2020 | **Major**: JIT، آرگومان های نامگذاری شده، عبارت تطبیق، انواع اتحادیه، ویژگی ها |
| PHP 8.1 | 2021 | Enums، الیاف، خواص `readonly`، انواع تقاطع |
| PHP 8.2 | 2022 |  کلاس های `readonly`، انواع DNF،`null`/`false`/`true`به عنوان انواع مستقل |
| PHP 8.3 | 2023 | ثابت های کلاس تایپ شده، ویژگی `#[\Override]`،`json_validate`|
| PHP 8.4 | 2024 | قلاب های دارایی، ویژگی `#[\Deprecated]`، دید نامتقارن |
## نقاط عطف اصلی
### PHP/FI و PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf "Personal Home Page Tools" را منتشر کرد
- **1998**: PHP 3 - بازنویسی کامل توسط Suraski & Gutmans. تبدیل به یک زبان برنامه نویسی می شود
- ویژگی های کلیدی: تعبیه شده در HTML، مدیریت فرم، پشتیبانی از پایگاه داده
### PHP 4 - Zend Engine (2000–2004)
- **Zend Engine 1**: بایت کد کامپایل شده، بسیار سریعتر
- رسیدگی به جلسه، بافر خروجی، PEAR
- اولین دوره چارچوب توسعه وب واقعی
### PHP 5 - PHP شی گرا (2004-2014)
- **5.0**: بازنویسی کامل OOP - کلاس ها، رابط ها، استثناها، PDO
- **5.3**: فضاهای نام (برای PHP مدرن حیاتی)، بسته شدن، پیوندهای استاتیک دیرهنگام
- **5.4**: صفات، نحو آرایه کوتاه `[]`، وب سرور داخلی
- **5.5**: ژنراتورها (`yield`)، `finally`
### PHP 7 - انقلاب عملکرد (2015–2019)
- **7.0**: Zend Engine 3 — **2 برابر سریعتر**، اعلان های نوع اسکالر، اعلان های نوع برگشتی
- **7.1**: انواع باطل (`?int`)، نوع بازگشت بی اعتبار
- **7.4**: خصوصیات تایپ شده، توابع پیکان `fn() =>`، تخصیص ادغام تهی `??=`
### PHP 8 - PHP مدرن (2020–اکنون)
- **8.0**: کامپایلر JIT، آرگومان های نامگذاری شده، عبارت مطابقت، انواع اتحادیه، ویژگی ها (`#[...]`)، اپراتور nullsafe`?->`
- **8.1**: Enums، الیاف (همگامی سبک)، خواص فقط خواندنی، انواع تقاطع
- **8.2**: کلاس های فقط خواندنی، انواع DNF،`null`/`false`/`true`به عنوان انواع مستقل
- **8.3**: ثابت های کلاس تایپ شده، `#[\Override]`،`json_validate()`
- **8.4**: قلاب های دارایی، `#[\Deprecated]`، دید نامتقارن
## تایپ سیستم تکامل
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

## تکامل نحو
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

## اصول کلیدی طراحی
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## رشد اکوسیستم
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
