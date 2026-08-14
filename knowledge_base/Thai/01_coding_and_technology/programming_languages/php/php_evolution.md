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
# PHP — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| PHP/FI | 1995 | เครื่องมือโฮมเพจส่วนตัว (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | PHP สมัยใหม่ตัวแรก Zeev Suraski และ Andi Gutmans เขียนใหม่ |
| PHP 4.0 | 2000 | Zend Engine, การสนับสนุนเซสชัน, การบัฟเฟอร์เอาต์พุต |
| PHP 5.0 | 2547 | **โมเดล OOP**, PDO, SQLite, SOAP, ตัววนซ้ำ |
| PHP 5.1 | 2548 | ส่วนขยาย PDO การปรับปรุงประสิทธิภาพ |
| PHP 5.2 | 2549 | `json_encode`/`json_decode`,`filter`ส่วนขยาย |
| PHP 5.3 | 2552 | **เนมสเปซ**, การผูกแบบคงที่ล่าช้า, การปิด |
| PHP 5.4 | 2555 | ไวยากรณ์อาร์เรย์แบบสั้น`[]`ลักษณะ เว็บเซิร์ฟเวอร์ในตัว |
| PHP 5.5 | 2013 | เครื่องกำเนิดไฟฟ้า,`yield`,`list()`บนอ็อบเจ็กต์,`::class`|
| PHP 5.6 | 2014 | ฟังก์ชันแปรผัน นิพจน์สเกลาร์คงที่ |
| PHP 7.0 | 2558 | **หลัก**: Zend Engine 3, คำแนะนำประเภทสเกลาร์, ประเภทการส่งคืน,`??`|
| PHP 7.1 | 2559 | ประเภท Nullable,`void`return, ทำซ้ำได้, การมองเห็นคลาสคงที่ |
| PHP 7.2 | 2017 |  คำใบ้ประเภท `object`, การขยายประเภทพารามิเตอร์ |
| PHP 7.3 | 2018 | เครื่องหมายจุลภาคต่อท้ายในการเรียกใช้ฟังก์ชัน`JsonException`|
| PHP 7.4 | 2019 | **คุณสมบัติที่พิมพ์** ฟังก์ชันลูกศร การมอบหมายการรวมค่าว่าง |
| PHP 8.0 | 2020 | **หลัก**: JIT, อาร์กิวเมนต์ที่มีชื่อ, นิพจน์การจับคู่, ประเภทยูเนียน, คุณลักษณะ |
| PHP 8.1 | 2021 | อีนัม, ไฟเบอร์, คุณสมบัติ `readonly`, ประเภททางแยก |
| PHP 8.2 | 2022 |  คลาส `readonly`, ประเภท DNF,`null`/`false`/`true`เป็นประเภทสแตนด์อโลน |
| PHP 8.3 | 2023 | ค่าคงที่คลาสที่พิมพ์, แอ็ตทริบิวต์ `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | hooks คุณสมบัติ, คุณลักษณะ `#[\Deprecated]`, การมองเห็นไม่สมมาตร |
## เหตุการณ์สำคัญที่สำคัญ
### PHP/FI และ PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf เปิดตัว "Personal Home Page Tools"
- **1998**: PHP 3 — เขียนใหม่ทั้งหมดโดย Suraski & Gutmans; กลายเป็นภาษาสคริปต์
- คุณสมบัติหลัก: ฝังอยู่ใน HTML, การจัดการแบบฟอร์ม, การรองรับฐานข้อมูล
### PHP 4 — Zend Engine (2000–2004)
- **Zend Engine 1**: คอมไพล์โค้ดไบต์ได้เร็วกว่ามาก
- การจัดการเซสชัน, การบัฟเฟอร์เอาต์พุต, PEAR
- ยุคกรอบการพัฒนาเว็บจริงครั้งแรก
### PHP 5 — PHP เชิงวัตถุ (2004–2014)
- **5.0**: เขียน OOP ใหม่ให้สมบูรณ์ — คลาส, อินเทอร์เฟซ, ข้อยกเว้น, PDO
- **5.3**: เนมสเปซ (สำคัญสำหรับ PHP สมัยใหม่), การปิด, การเชื่อมโยงแบบคงที่ล่าช้า
- **5.4**: ลักษณะ ไวยากรณ์อาร์เรย์สั้น`[]`เว็บเซิร์ฟเวอร์ในตัว
- **5.5**: เครื่องกำเนิดไฟฟ้า (`yield`), `finally`
### PHP 7 — การปฏิวัติด้านประสิทธิภาพ (2015–2019)
- **7.0**: Zend Engine 3 — **เร็วขึ้น 2 เท่า**, การประกาศประเภทสเกลาร์, การประกาศประเภทส่งคืน
- **7.1**: ประเภท Nullable (`?int`) ประเภทการส่งคืนเป็นโมฆะ
- **7.4**: คุณสมบัติที่พิมพ์, ฟังก์ชันลูกศร`fn() =>`, การกำหนดการรวมค่า null `??=`
### PHP 8 — PHP สมัยใหม่ (2020–ปัจจุบัน)
- **8.0**: คอมไพเลอร์ JIT, อาร์กิวเมนต์ที่มีชื่อ, นิพจน์การจับคู่, ประเภทยูเนียน, คุณลักษณะ (`#[...]`), ตัวดำเนินการ nullsafe`?->`
- **8.1**: Enums, ไฟเบอร์ (การทำงานพร้อมกันแบบน้ำหนักเบา), คุณสมบัติแบบอ่านอย่างเดียว, ประเภททางแยก
- **8.2**: คลาสแบบอ่านอย่างเดียว, ประเภท DNF,`null`/`false`/`true`เป็นประเภทสแตนด์อโลน
- **8.3**: ค่าคงที่คลาสที่พิมพ์`#[\Override]`,`json_validate()`
- **8.4**: คุณสมบัติตะขอ`#[\Deprecated]`การมองเห็นไม่สมมาตร
## ประเภทวิวัฒนาการของระบบ
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

## วิวัฒนาการไวยากรณ์
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

## หลักการออกแบบที่สำคัญ
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## การเติบโตของระบบนิเวศ
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
