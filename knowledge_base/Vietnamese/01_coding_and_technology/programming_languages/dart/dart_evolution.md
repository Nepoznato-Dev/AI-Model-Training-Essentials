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

# Dart — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 1.0 | 2013 | Bản phát hành lần đầu (Google, Lars Bak & Kasper Lund) |
| 1.2 | 2014 | Cải tiến trình biên dịch Dart2JS |
| 1.3 | 2014 |  Hỗ trợ`async`/`await`|
| 1.4 | 2014 | `enum`, cải tiến mixins |
| 1,5 | 2014 | Máy phát điện (`sync*`,`async*`) |
| 1.6 | 2014 |  Cải tiến`Future`|
| 1.8 | 2014 |  Cải tiến`dart:io`|
| 1.9 | 2015 | Chế độ mạnh (chọn tham gia) |
| 1.11 | 2015 |  Cải tiến`Future.then`|
| 1.12 | 2015 | **Chế độ mạnh** được thực thi |
| 2.0 | 2018 | **Chính**: Hệ thống loại âm thanh, chuẩn bị an toàn `null`, viết lại bộ sưu tập |
| 2.1 | 2018 |  Hợp nhất`int`/ `double`,`await for`|
| 2.2 | 2019 | `Set`theo nghĩa đen, cải tiến bộ sưu tập`const`|
| 2.3 | 2019 | Bộ sưu tập`if`, bộ sưu tập`for`, nhà điều hành trải rộng`...`|
| 2.6 | 2019 | Phương pháp mở rộng |
| 2.7 | 2020 | Tham số được đặt tên mặc định |
| 2.10 | 2020 | **An toàn về âm thanh** (chọn tham gia) |
| 2.12 | 2021 | **Không an toàn được bật theo mặc định** |
| 2.13 | 2021 | Nhà xây dựng xé bỏ |
| 2.14 | 2021 |  Cải tiến `late`, số nguyên không dấu |
| 2,15 | 2021 | Các loại chức năng chung, ổn định của hàm tạo |
| 2.17 | 2022 | **Siêu tham số**, enum nâng cao |
| 2.18 | 2022 | Suy luận kiểu nâng cao |
| 2.19 | 2023 | Bản ghi và mẫu (xem trước) |
| 3.0 | 2023 | **Chính**: Bản ghi, mẫu, công cụ sửa đổi lớp, biểu thức`switch`|
| 3.1 | 2023 | Cải tiến mẫu, lớp kín |
| 3.2 | 2023 | Cải tiến phân tích tĩnh |
| 3.3 | 2024 | Các loại tiện ích mở rộng, cải tiến biểu thức`switch`|
| 3,4 | 2024 |  Các phần tử `if`, cải tiến`case`|
| 3,5 | 2024 | Macro (xem trước), cải tiến thêm ngôn ngữ |
| 3.6 | 2025 | Đang phát triển |
## Các cột mốc quan trọng
### Phi tiêu 1.x — Những năm đầu (2013–2017)
- **2013**: Google phát hành Dart — được thiết kế để lập trình web có cấu trúc
- **Mục tiêu**: Thay thế JavaScript để phát triển web (tham vọng sau này sẽ được chuyển hướng)
- **1.0**: Lớp, giao diện, cách ly, kiểu gõ tùy chọn
- **1.3**: Hỗ trợ`async`/ `await`
- **1.9**: Chế độ mạnh (chọn tham gia gõ nghiêm ngặt)
- Dart VM được sử dụng trong Chrome một thời gian ngắn, sau đó bị xóa
### Flutter Pivot (2017–2018)
- **2017**: Flutter framework được công bố — Dart trở thành ngôn ngữ UI
- Dart tìm thấy mục đích của mình: phát triển thiết bị di động/máy tính để bàn/web đa nền tảng
- **2.0 (2018)**: Viết lại hoàn chỉnh — hệ thống loại âm thanh, bộ sưu tập hiện đại
### Phi tiêu 2.x — Phi tiêu hiện đại (2018–2023)
- **2.0**: Hệ thống loại âm thanh, không còn`dynamic`theo mặc định
- **2.3**: Bộ sưu tập`if`/`for`, toán tử trải rộng — tuyệt vời cho cây widget Flutter
- **2.6**: Phương thức mở rộng
- **2.10**: Không có âm thanh an toàn (chọn tham gia)
- **2.12**: **Không an toàn được bật theo mặc định** — Các loại`?`có thể rỗng
- **2.17**: Siêu tham số (`super.x`), enum nâng cao
### Dart 3.x — Bản ghi & Mẫu (2023–nay)
- **3.0 (2023)**: **Bản ghi** (người mang dữ liệu ẩn danh), **mẫu** (phá hủy), **công cụ sửa đổi lớp** (`sealed`,`final`,`interface`,`base`), biểu thức `switch`
- **3.3 (2024)**: Loại tiện ích mở rộng (trình bao bọc không tốn phí)
- **3.5 (2024)**: Xem trước macro — siêu lập trình tại thời điểm biên dịch
## Tiến hóa cú pháp
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

## Loại tiến hóa hệ thống
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

## Nguyên tắc thiết kế chính
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Tăng trưởng hệ sinh thái
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
