---
# Metadata
title: "Kotlin — Version History & Evolution"
description: "Comprehensive version history and evolution of Kotlin from 1.0 to modern Kotlin."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [kotlin, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Kotlin — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 1.0 | 2016 | Bản phát hành ổn định đầu tiên (JetBrains) |
| 1.1 | 2017 | Coroutines, gõ bí danh, phá hủy trong lambdas |
| 1.2 | 2017 | Trải rộng mảng,`lateinit`cấp cao nhất, dấu phẩy ở cuối |
| 1.3 | 2018 | `inline class`,`contracts`(thử nghiệm) |
| 1.4 | 2020 |  Chuyển đổi`@JvmDefault`, SAM cho giao diện Kotlin |
| 1,5 | 2021 |  Chú thích`value class`, `OptIn`, chữ biểu thức chính quy |
| 1.6 | 2021 | `when`đầy đủ, tối ưu hóa lợi nhuận`Unit`|
| 1.7 | 2022 |  Các mục `enum`, các lớp giá trị`@JvmInline`|
| 1.8 | 2022 | `@SubclassOptInRequired`, xem trước trình biên dịch K2 |
| 1.9 | 2023 | **Trình biên dịch K2**, các đối tượng`@ConsistentCopyVisibility`,`data`|
| 2.0 | 2024 | **Trình biên dịch K2 ổn định**, `@SubclassOptInRequired`, cải tiến về tính năng truyền thông minh |
| 2.1 | 2024 |  Đối tượng `when`, cải tiến ủy quyền tài sản |
| 2.2 | 2025 | (dự kiến) Cải tiến thêm K2 |
## Các cột mốc quan trọng
### Sự khởi đầu (2011–2016)
- **2011**: JetBrains công bố Kotlin (được đặt theo tên đảo Kotlin gần St. Petersburg)
- **2012**: Kotlin có nguồn mở
- **2016**: **Kotlin 1.0** — sẵn sàng sản xuất cho JVM và Android
### Sử dụng Android (2017–2019)
- **2017**: Google công bố hỗ trợ Kotlin hạng nhất tại Google I/O
- **1.1 (2017)**: **Coroutines** — lập trình không đồng bộ nhẹ
- **1.2 (2017)**: Dự án đa nền tảng (Kotlin/Native, Kotlin/JS)
- **1.3 (2018)**:`inline class`, hợp đồng
### Những năm tăng trưởng (2020–2023)
- **1.5 (2021)**: Chú thích`value class`, `OptIn`, kiểu số nguyên không dấu
- **1.7 (2022)**: Mục `enum`, bản xem trước trình biên dịch K2
- **1.9 (2023)**: Trình biên dịch K2 (giao diện người dùng mới, biên dịch nhanh hơn 30%), đối tượng `data`
### Kotlin hiện đại (2024–nay)
- **2.0 (2024)**: **Trình biên dịch K2 ổn định** — cải tiến hiệu suất lớn, phân tích tốt hơn
- **2.1 (2024)**:`when`nâng cao, ủy quyền thuộc tính
## Tiến hóa Coroutine
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## Tiến hóa đa nền tảng
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## Tiến hóa tính năng ngôn ngữ
```
Null Safety:
  1.0:  Nullable types (String?), safe calls (?.), Elvis (?:)
  1.5:  OptIn annotation for experimental APIs
  2.0:  Smart cast improvements

Pattern Matching:
  1.0:  when expression, is/as operators
  1.7:  when exhaustiveness checking
  2.1:  Enhanced when subjects

Data Classes:
  1.0:  data class (equals, hashCode, toString, copy, componentN)
  1.9:  data object
  2.0:  @ConsistentCopyVisibility

Value Classes:
  1.3:  inline class (experimental)
  1.5:  value class (renamed)
  1.7:  @JvmInline value class
```

## Kotlin trên các nền tảng khác nhau
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## Tăng trưởng hệ sinh thái
```
2016: Kotlin 1.0 — JetBrains IDE plugin
2017: Google I/O — first-class Android support
2018: Android KTX, Spring Framework 5 Kotlin support
2019: Kotlin 1.3 — coroutines stable
2021: Kotlin 1.5 — multiplatform matures
2023: Kotlin 1.9 — K2 compiler
2024: Kotlin 2.0 — K2 stable, Compose Multiplatform
2025: Kotlin — top 15 most used language; dominant in Android
```

## Nguyên tắc thiết kế chính
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
