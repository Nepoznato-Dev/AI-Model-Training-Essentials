---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Rust — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Ngày phát hành | Chủ đề chính |
|----------|-------------|----------|
| 0,1 | Tháng 1 năm 2012 | Trình biên dịch đầu tiên (rustc), đồng thời dựa trên tác vụ |
| 0,5 | 2012 | Hệ thống loại dựa trên đặc điểm hình thành |
| 0,6 | 2012 | Loại bỏ các hộp được quản lý`@`|
| 0,7 | 2013 | `@`đã bị xóa,`~`cho các hộp sở hữu |
| 0,8 | 2013 | Chú thích trọn đời,`&mut`|
| 0,9 | Tháng 1 năm 2014 | Dọn dẹp cuối cùng trước 1.0 |
| 0,10 | Tháng 2 năm 2014 | Bản phát hành trước 1.0 cuối cùng |
| 0,11 | Tháng 4 năm 2014 | `Box<T>`thay thế`~T`|
| 0,12 | Tháng 5 năm 2014 |  Bắt đầu viết lại mô-đun`io`|
| 1.0 | Ngày 15 tháng 5 năm 2015 | **Bản phát hành ổn định** — "Rust 1.0" |
| 1.10 | Tháng 8 năm 2016 |  Lan truyền lỗi`?`(dưới dạng`try!`→`?`) |
| 1.15 | Tháng 2 năm 2017 | Rust đầu tiên ổn định với bản chuẩn bị`impl Trait`|
| 1.18 | Tháng 6 năm 2017 | `pub(crate)`, biên dịch gia tăng |
| 1,20 | Tháng 10 năm 2017 | Các hằng số liên kết |
| 1,26 | Tháng 5 năm 2018 | `impl Trait`ở vị trí đối số/trả về |
| 1,28 | Tháng 9 năm 2018 | Nhà phân bổ toàn cầu |
| 1.31 | Tháng 12 năm 2018 | **Phiên bản Rust 2018** — mô-đun,`dyn Trait`|
| 1,34 | Tháng 4 năm 2019 | Cơ quan đăng ký thay thế |
| 1,39 | Tháng 11 năm 2019 | `async/await`ổn định |
| 1,44 | Tháng 7 năm 2020 | Cải tiến chẩn đoán |
| 1,51 | Tháng 4 năm 2021 |  Thuốc generic`const`(MVP) |
| 1,56 | Tháng 10 năm 2021 | **Phiên bản Rust 2021** — đóng cửa, IntoIterator |
| 1,59 | Tháng 2 năm 2022 | Lắp ráp nội tuyến |
| 1,62 | Tháng 6 năm 2022 | `#[default]`cho enum |
| 1,65 | Tháng 12 năm 2022 | `let else`|
| 1,68 | Tháng 3 năm 2023 | `#[ffi_pure]`, tối ưu hóa theo hướng dẫn hồ sơ |
| 1,70 | Tháng 6 năm 2023 | Phụ thuộc`crates.io`bị cô lập |
| 1,74 | Tháng 11 năm 2023 | Chế độ ngoại tuyến chở hàng |
| 1,76 | Tháng 2 năm 2024 | **Phiên bản Rust 2024** — Khối `gen`,`unsafe extern`|
| 1,79 | Tháng 6 năm 2024 | `LazyCell`,`LazyLock`|
| 1,82 | Tháng 10 năm 2024 |  Cần có`unsafe`trong khối`extern`|
| 1,85 | Tháng 2 năm 2025 | Phiên bản Rust 2024 ổn định |
## Các cột mốc quan trọng
### Trước 1.0 (2010–2015)
- **2010**: Dự án phụ của Graydon Hoare tại Mozilla thu hút được sự chú ý
- **2012**: Trình biên dịch công khai đầu tiên; hệ thống loại trải qua thiết kế lại lớn
- **2013**: Mô hình sở hữu được kết tinh;  Đã xóa hộp `@`
- **2014**: Quy trình Rust RFC được chính thức hóa; cộng đồng phát triển
- **2015**: **1.0** — đảm bảo độ ổn định; "trừu tượng không tốn phí"
### Những năm tăng trưởng (2015–2019)
- **2015**: Cargo trở thành nhà quản lý gói hàng tiêu chuẩn
- **2018**: **Phiên bản Rust 2018** — đại tu hệ thống mô-đun,`dyn Trait`,`impl Trait`
- **2019**:`async/await`ổn định — hệ sinh thái không đồng bộ bắt đầu
### Trưởng thành (2020–nay)
- **2021**: **Phiên bản Rust 2021** — phân biệt các trường trong phần đóng,`IntoIterator`cho mảng
- **2024**: **Phiên bản Rust 2024** — Khối `gen`, yêu cầu về `unsafe extern`
- **2025**: Rust trong nhân Linux, cơ sở hạ tầng Android, Windows, AWS
## Hệ thống phiên bản
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Tiến hóa quyền sở hữu
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## Tiến hóa không đồng bộ
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Tăng trưởng hệ sinh thái
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## RFC chính
| RFC | Năm | Tính năng |
|------|------|----------|
| 25 | 2013 | Khớp mẫu |
| 153 | 2014 |  Loại`Result`|
| 217 | 2014 |  Toán tử`?`(thử) |
| 460 | 2016 | `?`thay thế`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Phiên bản Rust 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 |  Thuốc generic`const`|
| 3013 | 2020 | Kiểm tra việc biên dịch có điều kiện |
| 3517 | 2023 |  Khối`gen`|