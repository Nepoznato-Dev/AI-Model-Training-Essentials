---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| K&R C | 1972–78 | Bản gốc C (Kernighan & Ritchie) |
| C89/C90 | 1989/90 | Tiêu chuẩn ANSI/ISO đầu tiên |
| C95 | 1995 | Sửa đổi 1:`wchar.h`, chữ ghép |
| C99 | 1999 |  Nhận xét `//`,`inline`,`bool`, VLA, công cụ khởi tạo được chỉ định |
| C11 | 2011 | Nguyên tử, chủ đề, `_Static_assert`, cấu trúc/công đoàn ẩn danh |
| C17 | 2018 | Sửa lỗi (không có tính năng mới) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, thuộc tính |
## Các cột mốc quan trọng
### K&R C (1972–1989)
- **1972**: Dennis Ritchie tạo C tại Bell Labs cho Unix
- **1978**: Kernighan & Ritchie xuất bản "Ngôn ngữ lập trình C"
- Các tính năng chính:`struct`,`int`,`char`, con trỏ, hàm,`#include`
- Không có`void`, không có`enum`, không có`unsigned`, không có `const`
### C89/C90 — Tiêu chuẩn (1989)
- Tiêu chuẩn ANSI đầu tiên (ANSI X3.159-1989)
- Đã thêm:`void`,`enum`,`const`,`volatile`, nguyên mẫu chức năng,`signed`
- “Thời hoàng kim” — di động, được áp dụng rộng rãi
- Vẫn là nền tảng cho nhiều hệ thống nhúng
### C99 — C hiện đại (1999)
- Nhận xét một dòng `//`
- Chức năng `inline`
-`bool`qua`<stdbool.h>`
- Mảng có độ dài thay đổi (VLA)
- Công cụ khởi tạo được chỉ định:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— khai báo trong vòng lặp
-`<stdint.h>`:`int32_t`,`uint64_t`, v.v.
- Từ khóa `restrict`
- Macro đa dạng
- Chữ ghép
### C11 — An toàn & Đồng thời (2011)
-`<stdatomic.h>`- hoạt động nguyên tử
-`<threads.h>`- hỗ trợ luồng
-`_Static_assert`— xác nhận tại thời điểm biên dịch
- Cấu trúc/liên kết ẩn danh trong cấu trúc lồng nhau
-`_Alignof`,`_Alignas`— điều khiển căn chỉnh
- Lựa chọn chung:`_Generic(x, int: ..., default: ...)`
- Hỗ trợ Unicode:`<uchar.h>`
- Hỗ trợ VLA tùy chọn (được thực hiện tùy chọn do các mối quan tâm được nhúng)
### C23 — Thời Phục Hưng (2024)
-`nullptr`- hằng số con trỏ null (thay thế macro `NULL`)
-`typeof`— kiểu suy luận
-`constexpr`— biểu thức hằng số
-`#embed`- nhúng dữ liệu nhị phân tại thời điểm biên dịch
- Cú pháp`[[attribute]]`(thuộc tính kiểu C23)
- `true`/`false` làm từ khóa (không cần`<stdbool.h>`nữa)
- Suy luận kiểu `auto`
-`static_assert`(không có dấu gạch dưới)
-`alignof`(không có dấu gạch dưới)
- Đã xóa trả về`int`mặc định
## Quy trình tiêu chuẩn
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Triết lý tương thích
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Tiến hóa tiền xử lý
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Loại tiến hóa hệ thống
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

##Tác động đến hệ sinh thái
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
