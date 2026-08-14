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

# PHP — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| PHP/FI | 1995 | Công cụ Trang chủ Cá nhân (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | PHP hiện đại đầu tiên; Zeev Suraski & Andi Gutmans viết lại |
| PHP 4.0 | 2000 | Zend Engine, hỗ trợ phiên, đệm đầu ra |
| PHP 5.0 | 2004 | **Mô hình OOP**, PDO, SQLite, SOAP, trình vòng lặp |
| PHP 5.1 | 2005 | Tiện ích mở rộng PDO, cải tiến hiệu suất |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`, phần mở rộng`filter`|
| PHP 5.3 | 2009 | **Không gian tên**, liên kết tĩnh muộn, đóng cửa |
| PHP 5.4 | 2012 | Cú pháp mảng ngắn`[]`, đặc điểm, máy chủ web tích hợp |
| PHP 5.5 | 2013 | Máy phát điện,`yield`,`list()`trên các đối tượng,`::class`|
| PHP 5.6 | 2014 | Hàm biến phân, biểu thức vô hướng hằng số |
| PHP 7.0 | 2015 | **Chính**: Zend Engine 3, gợi ý kiểu vô hướng, kiểu trả về,`??`|
| PHP 7.1 | 2016 | Các loại có thể rỗng, trả về `void`, có thể lặp lại, khả năng hiển thị không đổi của lớp |
| PHP 7.2 | 2017 |  Gợi ý loại `object`, mở rộng loại tham số |
| PHP 7.3 | 2018 | Dấu phẩy ở cuối trong lệnh gọi hàm,`JsonException`|
| PHP 7.4 | 2019 | **Thuộc tính đã nhập**, hàm mũi tên, phép gán hợp nhất null |
| PHP 8.0 | 2020 | **Chính**: JIT, đối số được đặt tên, biểu thức so khớp, kiểu kết hợp, thuộc tính |
| PHP 8.1 | 2021 | Enums, sợi, thuộc tính `readonly`, loại giao lộ |
| PHP 8.2 | 2022 |  Các lớp `readonly`, loại DNF,`null`/`false`/`true`là loại độc lập |
| PHP 8.3 | 2023 | Các hằng số lớp được gõ, thuộc tính `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Móc thuộc tính, thuộc tính `#[\Deprecated]`, khả năng hiển thị bất đối xứng |
## Các cột mốc quan trọng
### PHP/FI và PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf phát hành "Công cụ trang chủ cá nhân"
- **1998**: PHP 3 — được viết lại hoàn toàn bởi Suraski & Gutmans; trở thành một ngôn ngữ kịch bản
- Các tính năng chính: nhúng trong HTML, xử lý biểu mẫu, hỗ trợ cơ sở dữ liệu
### PHP 4 — Công cụ Zend (2000–2004)
- **Zend Engine 1**: Mã byte được biên dịch, nhanh hơn nhiều
- Xử lý phiên, đệm đầu ra, PEAR
- Kỷ nguyên khung phát triển web thực sự đầu tiên
### PHP 5 — PHP hướng đối tượng (2004–2014)
- **5.0**: Viết lại OOP hoàn chỉnh — các lớp, giao diện, ngoại lệ, PDO
- **5.3**: Không gian tên (quan trọng đối với PHP hiện đại), các phần đóng, các liên kết tĩnh muộn
- **5.4**: Đặc điểm, cú pháp mảng ngắn`[]`, máy chủ web tích hợp
- **5.5**: Máy phát điện (`yield`), `finally`
### PHP 7 — Cuộc cách mạng hiệu suất (2015–2019)
- **7.0**: Zend Engine 3 — **nhanh gấp 2 lần**, khai báo kiểu vô hướng, khai báo kiểu trả về
- **7.1**: Loại có thể rỗng (`?int`), loại trả về void
- **7.4**: Thuộc tính được nhập, hàm mũi tên`fn() =>`, gán kết hợp null `??=`
### PHP 8 — PHP hiện đại (2020–nay)
- **8.0**: Trình biên dịch JIT, đối số được đặt tên, biểu thức so khớp, kiểu kết hợp, thuộc tính (`#[...]`), toán tử nullsafe`?->`
- **8.1**: Enums, Fibers (đồng thời nhẹ), thuộc tính chỉ đọc, loại giao lộ
- **8.2**: Các lớp chỉ đọc, loại DNF,`null`/`false`/`true`là loại độc lập
- **8.3**: Các hằng số lớp được gõ,`#[\Override]`,`json_validate()`
- **8.4**: Móc thuộc tính,`#[\Deprecated]`, khả năng hiển thị không đối xứng
## Loại tiến hóa hệ thống
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

## Tiến hóa cú pháp
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

## Nguyên tắc thiết kế chính
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Tăng trưởng hệ sinh thái
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
