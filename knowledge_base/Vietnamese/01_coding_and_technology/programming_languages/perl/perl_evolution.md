---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Perl — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 1.0 | 1987 | Bản phát hành đầu tiên (Larry Wall) |
| 2.0 | 1988 |  Hàm `study`, biểu thức chính quy tốt hơn |
| 3.0 | 1989 |  Biến`my`(phạm vi từ vựng) |
| 4.0 | 1991 | `O'Reilly`"Lập trình Perl" (Sách lạc đà) |
| 5.0 | 1994 | **Chính**: mô-đun, tài liệu tham khảo, phần đóng,`use strict`|
| 5.6 | 2000 | `our`,`state`(sau),`v-strings`,`y2k`sửa lỗi |
| 5,8 | 2002 | **Hỗ trợ Unicode**,`ithreads`,`open`pragma |
| 5.10 | 2007 | `say`,`//`được xác định-hoặc,`given`/`when`,`~~`Smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(thay thế không phá hủy), cải tiến`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 |`$_`từ vựng, ngẫu nhiên băm,`my`trong điều kiện |
| 5h20 | 2014 | **Chữ ký chương trình con** (thử nghiệm), cắt`%hash`|
| 5,22 | 2015 |  Hội thảo `&`,`<<>>`(mở an toàn) |
| 5,24 | 2016 | Postfix hội thảo ổn định |
| 5.26 | 2017 | **`$_` từ vựng trong`while`**,`.`trong`@INC`đã bị xóa (bảo mật) |
| 5,28 | 2018 | Unicode 10.0,`delete`trên các lát khóa/giá trị |
| 5h30 | 2019 | `my`trong điều kiện`for`/`while`|
| 5.32 | 2020 |  Toán tử `isa`, Unicode 13.0 |
| 5,34 | 2021 | `try`/`catch`(thử nghiệm), khối`defer`|
| 5.36 | 2022 | **`use v5.36`**: đã bật chữ ký,`$_`mặc định,`defer`|
| 5,38 | 2023 |  Từ khóa`class`(thử nghiệm),`try`/`catch`ổn định |
| 5h40 | 2024 |  Toán tử bitwise `^`, cải tiến danh sách`for`|
| 5,42 | 2025 | Đang phát triển |
## Các cột mốc quan trọng
### Perl 1–4: Kỷ nguyên viết kịch bản (1987–1993)
- **1987**: Larry Wall phát hành Perl — "Ngôn ngữ báo cáo và trích xuất thực tế"
- **Mục tiêu**: Kết hợp sed, awk, grep, shell thành một công cụ tạo tập lệnh mạnh mẽ
- **3.0**: Phạm vi từ vựng (`my`)
- **4.0**: The Camel Book — Perl được áp dụng rộng rãi cho các tác vụ quản trị hệ thống
### Perl 5: Thời đại hoàng kim (1994–2019)
- **5.0 (1994)**: Viết lại hoàn chỉnh — **mô-đun**, **tài liệu tham khảo**, **đóng**, **đối tượng**
- **5.6 (2000)**:`our`, chuỗi v
- **5.8 (2002)**: **Hỗ trợ Unicode**, chuỗi trình thông dịch (`ithreads`)
- **5.10 (2007)**:`say`,`//`(được xác định-hoặc),`given`/`when`(chuyển đổi), smartmatch
- **5.12–5.28**: Cải tiến dần dần, nâng cấp Unicode
### Perl hiện đại (2020–nay)
- **5.32 (2020)**: Toán tử`isa`(kiểm tra loại sạch hơn)
- **5,34 (2021)**:`try`/`catch`(thử nghiệm), khối `defer`
- **5.36 (2022)**: **`use v5.36`** — chữ ký được bật theo mặc định,`$_`mặc định,`defer`
- **5,38 (2023)**: Từ khóa`class`(thử nghiệm — OOP tích hợp),`try`/`catch`ổn định
- **5,40 (2024)**: Cải tiến toán tử bitwise
## Tiến hóa cú pháp
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

## Hệ sinh thái CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Nguyên tắc thiết kế chính
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Tăng trưởng hệ sinh thái
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
