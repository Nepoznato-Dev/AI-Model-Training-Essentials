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

# PHP — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| PHP/FI | 1995 | أدوات الصفحة الرئيسية الشخصية (راسموس ليردورف) |
| بي إتش بي 3.0 | 1998 | أول لغة PHP حديثة؛ إعادة كتابة زئيف سوراسكي وأندي جوتمانز |
| بي إتش بي 4.0 | 2000 | محرك Zend، دعم الجلسة، التخزين المؤقت للإخراج |
| بي إتش بي 5.0 | 2004 | **نموذج OOP**، PDO، SQLite، SOAP، التكرارات |
| بي إتش بي 5.1 | 2005 | ملحق PDO، تحسينات في الأداء |
| بي إتش بي 5.2 | 2006 | `json_encode`/`json_decode`, امتداد`filter`|
| بي إتش بي 5.3 | 2009 | **مساحات الأسماء**، الارتباطات الثابتة المتأخرة، عمليات الإغلاق |
| بي إتش بي 5.4 | 2012 | بناء الجملة القصير `[]`، السمات، خادم الويب المدمج |
| PHP 5.5 | 2013 | مولدات، `yield`،`list()`على الكائنات،`::class`|
| PHP 5.6 | 2014 | الدوال المتغيرة، التعبيرات العددية الثابتة |
| بي إتش بي 7.0 | 2015 | **التخصص**: Zend Engine 3، تلميحات النوع العددي، أنواع الإرجاع،`??`|
| بي إتش بي 7.1 | 2016 | الأنواع الخالية، إرجاع `void`، القابل للتكرار، رؤية ثابتة للفئة |
| بي إتش بي 7.2 | 2017 |  تلميح نوع `object`، توسيع نوع المعلمة |
| بي إتش بي 7.3 | 2018 | الفواصل الزائدة في استدعاءات الوظائف،`JsonException`|
| بي إتش بي 7.4 | 2019 | **الخصائص المكتوبة**، وظائف الأسهم، مهمة الدمج الفارغة |
| بي إتش بي 8.0 | 2020 | **التخصص**: JIT، الوسائط المسماة، تعبير المطابقة، أنواع الاتحاد، السمات |
| بي إتش بي 8.1 | 2021 | التعدادات، الألياف، خواص `readonly`، أنواع التقاطعات |
| بي إتش بي 8.2 | 2022 |  فئات`readonly`وأنواع DNF و`null` /`false`/`true`كأنواع مستقلة |
| بي إتش بي 8.3 | 2023 | ثوابت الفئة المكتوبة، سمة `#[\Override]`،`json_validate`|
| بي إتش بي 8.4 | 2024 | خطافات الخاصية، سمة `#[\Deprecated]`، الرؤية غير المتماثلة |
## المعالم الرئيسية
### PHP/FI وPHP 3 (1995-1999)
- **1995**: أصدر راسموس ليردورف "أدوات الصفحة الرئيسية الشخصية"
- **1998**: PHP 3 — إعادة كتابة كاملة بواسطة Suraski & Gutmans؛ تصبح لغة البرمجة النصية
- الميزات الرئيسية: مضمن في HTML، ومعالجة النماذج، ودعم قاعدة البيانات
### PHP 4 — محرك Zend (2000-2004)
- **Zend Engine 1**: كود ثانوي مُجمَّع، أسرع بكثير
- التعامل مع الجلسة، والتخزين المؤقت للإخراج، والكمثرى
- أول عصر حقيقي لإطار تطوير الويب
### PHP 5 — PHP كائنية التوجه (2004–2014)
- **5.0**: إعادة كتابة OOP كاملة — الفئات، الواجهات، الاستثناءات، PDO
- **5.3**: مساحات الأسماء (بالغة الأهمية لـ PHP الحديثة)، وعمليات الإغلاق، والارتباطات الثابتة المتأخرة
- **5.4**: السمات، بناء جملة المصفوفة القصيرة `[]`، خادم الويب المدمج
- **5.5**: المولدات (`yield`)، `finally`
### PHP 7 — ثورة الأداء (2015-2019)
- **7.0**: Zend Engine 3 — **أسرع مرتين**، وإعلانات النوع العددي، وإعلانات نوع الإرجاع
- **7.1**: الأنواع الخالية (`?int`)، نوع الإرجاع الفارغ
- **7.4**: الخصائص المكتوبة، وظائف الأسهم `fn() =>`، مهمة الدمج الخالية `??=`
### PHP 8 — لغة PHP الحديثة (2020 إلى الوقت الحاضر)
- **8.0**: مترجم JIT، الوسائط المسماة، تعبير المطابقة، أنواع الاتحاد، السمات (`#[...]`)، عامل التشغيل nullsafe`?->`
- **8.1**: التعدادات، والألياف (تزامن خفيف الوزن)، وخصائص القراءة فقط، وأنواع التقاطع
- **8.2**: فئات للقراءة فقط، وأنواع DNF، و`null` /`false`/`true`كأنواع مستقلة
- **8.3**: ثوابت الفئة المكتوبة،`#[\Override]`،`json_validate()`
- **8.4**: خطافات الملكية، `#[\Deprecated]`، الرؤية غير المتماثلة
## نوع تطور النظام
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

## تطور بناء الجملة
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

## مبادئ التصميم الرئيسية
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## نمو النظام البيئي
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
