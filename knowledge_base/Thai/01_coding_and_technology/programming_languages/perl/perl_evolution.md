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

# Perl - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 1.0 | 1987 | การเปิดตัวครั้งแรก (แลร์รี่ วอลล์) |
| 2.0 | 1988 |  ฟังก์ชัน `study`, regex |
| 3.0 | 1989 |  ตัวแปร`my`(การกำหนดขอบเขตคำศัพท์) |
| 4.0 | 1991 | `O'Reilly`"การเขียนโปรแกรม Perl" (หนังสืออูฐ) |
| 5.0 | 1994 | **หลัก**: โมดูล, ข้อมูลอ้างอิง, การปิด,`use strict`|
| 5.6 | 2000 | `our`,`state`(ภายหลัง),`v-strings`,`y2k`แก้ไข |
| 5.8 | 2545 | **รองรับ Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2550 | `say`,`//`กำหนดหรือ`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(ญาดา-ญาดา), Unicode 5.2 |
| 5.14 | 2554 | `s///r`(การทดแทนแบบไม่ทำลาย), การปรับปรุง`package`|
| 5.16 | 2555 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | คำศัพท์`$_`, การสุ่มแฮช,`my`ในเงื่อนไข |
| 5.20 | 2014 | **ลายเซ็นรูทีนย่อย** (ทดลอง), การแบ่งส่วน`%hash`|
| 5.22 | 2558 |  การอ้างอิง `&`,`<<>>`(เปิดอย่างปลอดภัย) |
| 5.24 | 2559 | การยกเลิกการอ้างอิง Postfix เสถียร |
| 5.26 | 2017 | **คำศัพท์`$_`ใน`while`**,`.`ใน`@INC`ถูกลบออก (ความปลอดภัย) |
| 5.28 | 2018 | Unicode 10.0,`delete`บนส่วนของคีย์/ค่า |
| 5.30 | 2019 | `my`ในเงื่อนไข`for`/`while`|
| 5.32 | 2020 |  ตัวดำเนินการ `isa`, Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(ทดลอง),`defer`บล็อก |
| 5.36 | 2022 | **`use v5.36`**: เปิดใช้งานลายเซ็น, ค่าเริ่มต้น `$_`,`defer`|
| 5.38 | 2023 | `class`คำหลัก (ทดลอง),`try`/`catch`เสถียร |
| 5.40 | 2024 | `^`ตัวดำเนินการระดับบิต การปรับปรุงรายการ`for`|
| 5.42 | 2025 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### Perl 1–4: ยุคการเขียนสคริปต์ (1987–1993)
- **1987**: Larry Wall เผยแพร่ Perl — "Practical Extraction and Report Language"
- **เป้าหมาย**: รวม sed, awk, grep, shell ไว้ในเครื่องมือเขียนสคริปต์อันทรงพลังเครื่องมือเดียว
- **3.0**: การกำหนดขอบเขตคำศัพท์ (`my`)
- **4.0**: The Camel Book — Perl ถูกนำมาใช้กันอย่างแพร่หลายสำหรับงานดูแลระบบ
### Perl 5: ยุคทอง (1994–2019)
- **5.0 (1994)**: เขียนใหม่ทั้งหมด — **โมดูล**, **ข้อมูลอ้างอิง**, **การปิด**, **วัตถุ**
- **5.6 (2000)**:`our`, วีสตริง
- **5.8 (2002)**: **รองรับ Unicode**, เธรดล่าม (`ithreads`)
- **5.10 (2007)**:`say`,`//`(กำหนดไว้หรือ),`given`/`when`(สวิตช์), smartmatch
- **5.12–5.28**: การปรับปรุงเพิ่มเติม การอัพเกรด Unicode
### Perl สมัยใหม่ (2020–ปัจจุบัน)
- **5.32 (2020)**: ตัวดำเนินการ`isa`(การตรวจสอบประเภทน้ำยาทำความสะอาด)
- **5.34 (2021)**:`try`/`catch`(ทดลอง), บล็อก `defer`
- **5.36 (2022)**: **`use v5.36`** — ลายเซ็นเปิดใช้งานตามค่าเริ่มต้น, ค่าเริ่มต้น `$_`,`defer`
- **5.38 (2023)**: คีย์เวิร์ด`class`(ทดลอง — OOP ในตัว),`try`/`catch`เสถียร
- **5.40 (2024)**: การปรับปรุงตัวดำเนินการระดับบิต
## วิวัฒนาการไวยากรณ์
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

## ระบบนิเวศน์ของซีพีเอ็น
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## หลักการออกแบบที่สำคัญ
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## การเติบโตของระบบนิเวศ
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
