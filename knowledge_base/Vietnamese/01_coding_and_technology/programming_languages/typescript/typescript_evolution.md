---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# TypeScript - Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Ngày phát hành | Chủ đề chính |
|----------|-------------|----------|
| 0,8 | Tháng 10 năm 2012 | Phát hành lần đầu ra công chúng (Anders Hejlsberg) |
| 0,9 | Tháng 4 năm 2013 | Thuốc gốc |
| 1.0 | Tháng 4 năm 2014 | Bản phát hành ổn định đầu tiên |
| 1.1 | Tháng 11 năm 2014 | Hiệu suất trình biên dịch |
| 1.4 | Tháng 1 năm 2015 | Các loại chữ mẫu (cơ bản),`let`|
| 1,5 | Tháng 7 năm 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | Tháng 9 năm 2015 |  Các lớp `abstract`, hỗ trợ JSX |
| 1.7 | Tháng 11 năm 2015 | `async/await`(mục tiêu ES2017) |
| 1.8 | Tháng 2 năm 2016 | Được gắn thẻ chuỗi mẫu,`--strictNullChecks`|
| 2.0 | Tháng 9 năm 2016 | **Chính**: Các loại liên kết/ngã tư,`never`,`keyof`,`protected`|
| 2.1 | Tháng 12 năm 2016 | `keyof`, các loại được ánh xạ, máy phát điện`async`|
| 2.2 | Tháng 2 năm 2017 |  Loại `object`,`this`cải tiến |
| 2.3 | Tháng 4 năm 2017 | Mặc định chung, chế độ`--strict`|
| 2.4 | Tháng 6 năm 2017 | Kiểu yếu, enum chuỗi |
| 2,5 | Tháng 9 năm 2017 | Ràng buộc bắt tùy chọn |
| 2.6 | Tháng 10 năm 2017 | Các loại hàm nghiêm ngặt,`--strictFunctionTypes`|
| 2.7 | Tháng 1 năm 2018 | Phân công xác định (`!`),`const`enum |
| 2,8 | Tháng 3 năm 2018 | **Các loại có điều kiện**,`Exclude`,`Extract`|
| 2.9 | Tháng 6 năm 2018 | `keyof`cho số/ký hiệu, loại`import()`|
| 3.0 | Tháng 7 năm 2018 | **Chính**: Các bộ dữ liệu còn lại, `unknown`, tài liệu tham khảo dự án |
| 3.1 | Tháng 9 năm 2018 | Các loại được ánh xạ trên bộ dữ liệu, mảng`readonly`|
| 3.2 | Tháng 11 năm 2018 | `bigint`,`object`lan truyền |
| 3,4 | Tháng 3 năm 2019 |  Khẳng định `const`, suy luận kiểu bậc cao |
| 3,5 | Tháng 5 năm 2019 |  Loại trợ giúp`Omit`|
| 3,7 | Tháng 11 năm 2019 | **Xâu chuỗi tùy chọn**, kết hợp vô hiệu, các loại đệ quy |
| 3,8 | Tháng 2 năm 2020 |  Nhập/xuất `type-only`, trường`#private`|
| 3,9 | Tháng 5 năm 2020 | `// @ts-expect-error`, suy luận được cải thiện |
| 4.0 | Tháng 8 năm 2020 | **Chính**: Bộ dữ liệu biến đổi, bộ dữ liệu được gắn nhãn, kiểu chữ mẫu |
| 4.1 | Tháng 11 năm 2020 | **Các kiểu chữ mẫu**, ánh xạ lại khóa, điều kiện đệ quy |
| 4.2 | Tháng 2 năm 2021 | Thuộc tính trừu tượng,`~`trong các loại được ánh xạ |
| 4.3 | Tháng 6 năm 2021 | Các kiểu ghi riêng biệt, từ khóa`override`|
| 4.4 | Tháng 8 năm 2021 | Chữ ký biểu tượng/chỉ mục, thu hẹp luồng điều khiển |
| 4,5 | Tháng 11 năm 2021 | `.d.ts`từ `.js`,`await`trong`.d.ts`|
| 4.6 | Tháng 2 năm 2022 | Kiểm tra chức năng theo phạm vi khối, loại chính xác phần còn lại của đối tượng |
| 4.7 | Tháng 5 năm 2022 |  Các ràng buộc`extends`cho`infer`, ESM trong`.ts`|
| 4,8 | Tháng 8 năm 2022 | Cải thiện việc giảm giao lộ, sửa lỗi`--strictNullChecks`|
| 4,9 | Tháng 11 năm 2022 | ** Toán tử `satisfies`**, thu hẹp`in`|
| 5.0 | Tháng 3 năm 2023 | **Chính**: Thông số loại `const`, công cụ trang trí, đại tu`enum`|
| 5.1 | Tháng 6 năm 2023 | Bộ định kiểu không liên quan,`--exactOptionalPropertyTypes`|
| 5.2 | Tháng 8 năm 2023 |  Khai báo`using`(quản lý tài nguyên rõ ràng) |
| 5.3 | Tháng 11 năm 2023 | Nhập thuộc tính, thu hẹp`switch true`|
| 5.4 | Tháng 3 năm 2024 |  Tiện ích `NoInfer`, thông số đóng được thu hẹp |
| 5,5 | Tháng 6 năm 2024 | Vị từ loại được suy ra,`@`cho biểu thức chính quy |
| 5.6 | Tháng 9 năm 2024 | `--erasableSyntaxOnly`, người trợ giúp trình vòng lặp |
| 5,7 | Tháng 11 năm 2024 | `--noCheck`, hoàn thành đường dẫn |
| 5,8 | Tháng 2 năm 2025 |`isolatedDeclarations`được cải tiến |
## Các cột mốc quan trọng
### Những ngày đầu (2012–2015)
- **0.8 (2012)**: Anders Hejlsberg (người sáng tạo C#) dẫn đầu TypeScript tại Microsoft
- **1.0 (2014)**: Bản phát hành ổn định; lớp, giao diện, kiểu cơ bản
- **1.5 (2015)**: Tính năng ES6 — phá hủy, không gian tên, `for...of`
### Cuộc cách mạng kiểu chữ (2016–2018)
- **2.0 (2016)**: Các loại liên kết, các loại giao lộ,`never`,`keyof`— Hệ thống loại của TypeScript trở nên độc nhất
- **2.8 (2018)**: Loại có điều kiện — nền tảng cho lập trình cấp loại nâng cao
- **3.0 (2018)**: Bộ dữ liệu trong tham số phần còn lại, loại `unknown`, tham chiếu dự án
### TypeScript hiện đại (2019–nay)
- **3.7 (2019)**:`?.`tùy chọn và vô hiệu hóa kết hợp`??`(trước tiêu chuẩn JS!)
- **4.0 (2020)**: Bộ dữ liệu biến đổi, kiểu chữ mẫu
- **4.1 (2020)**: Kiểu chữ mẫu — thao tác chuỗi cấp loại
- **4.9 (2022)**: Toán tử`satisfies`— kiểm tra loại mà không mở rộng
- **5.0 (2023)**: Tham số loại `const`, trang trí (giai đoạn 3)
- **5.2 (2023)**: Khai báo`using`— quản lý tài nguyên rõ ràng
## Loại tiến hóa hệ thống
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## Tiến hóa trang trí
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Tiến hóa cấu hình
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Tăng trưởng hệ sinh thái
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Các quyết định thiết kế chính
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
