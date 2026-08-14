---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Python — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Ngày phát hành | Chủ đề chính |
|----------|-------------|----------|
| 1.0 | Tháng 1 năm 1994 | Phát hành lần đầu |
| 1,5 | Tháng 12 năm 1997 | Lớp học, ngoại lệ, mô-đun |
| 2.0 | Tháng 10 năm 2000 | Danh sách hiểu, thu gom rác |
| 2.2 | Tháng 12 năm 2001 | Các loại thống nhất (loại/lớp), máy phát điện |
| 2,5 | Tháng 9 năm 2006 |  Câu lệnh `with`,`yield`dưới dạng biểu thức |
| 2.6 | Tháng 10 năm 2008 | `bytes`,`future`nhập khẩu, chuyển sang 3 |
| 2.7 | Tháng 7 năm 2010 | Hiểu chính tả/bộ,`argparse`|
| 3.0 | Tháng 12 năm 2008 | **Phá vỡ**:`print()`,`str`/`bytes`, các vòng lặp |
| 3.3 | Tháng 9 năm 2012 | `yield from`, gói không gian tên |
| 3,4 | Tháng 3 năm 2014 | `asyncio`,`pathlib`,`enum`|
| 3,5 | Tháng 9 năm 2015 | `async/await`, gợi ý gõ (PEP 484), giải nén`**`|
| 3.6 | Tháng 12 năm 2016 | chuỗi f,`async`hiểu, ký tự theo thứ tự |
| 3,7 | Tháng 6 năm 2018 | `dataclasses`,`contextvars`, dành riêng`async`|
| 3,8 | Tháng 10 năm 2019 | Toán tử Walrus`:=`, thông số chỉ có vị trí |
| 3,9 | Tháng 10 năm 2020 | Liên hiệp Dict`|`, các loại chung`list[int]`|
| 3.10 | Tháng 10 năm 2021 | `match/case`, khớp mẫu cấu trúc |
| 3.11 | Tháng 10 năm 2022 | Nhóm ngoại lệ, loại `Self`, CPython nhanh hơn |
| 3.12 | Tháng 10 năm 2023 | Chuẩn bị GIL cho mỗi thông dịch viên, cú pháp tham số loại |
| 3.13 | Tháng 10 năm 2024 | Chế độ luồng tự do (thử nghiệm), REPL được cải tiến |
| 3.14 | Tháng 10 năm 2025 | Đánh giá chú thích ổn định, không có GIL |
## Các cột mốc quan trọng
### Kỷ nguyên Python 2.x (2000–2020)
- **2.0**: Khả năng hiểu danh sách lấy cảm hứng từ Haskell; GC tuần hoàn
- **2.2**: Lớp cơ sở `object`;  Từ khóa`yield`(máy phát điện)
- **2.5**: Câu lệnh `with`; `yield`trở thành biểu thức
- **2.7**: Bản phát hành 2.x cuối cùng; hiểu chính tả; `argparse`
- **Kết thúc cuộc đời**: 01/01/2020
### Cách mạng Python 3.x (2008–nay)
- **3.0**: Ngắt rõ ràng —`print`là hàm,`str`so với`bytes`, tất cả các trình vòng lặp đều trả về lượt xem
- **3.5**: Cú pháp `async`/`await`; gõ gợi ý với mô-đun `typing`
- **3.6**: chuỗi f (tính năng được yêu cầu nhiều nhất); `asyncio`đã ổn định
- **3.8**: Toán tử Walrus để gán nội tuyến
- **3.10**: Khớp mẫu cấu trúc (`match`/`case`)
- **3,11**: nhanh hơn 10-60%; nhóm ngoại lệ với`except*`
- **3.13**: Chế độ phân luồng tự do thử nghiệm (không có GIL)
## Sự phát triển của triết lý thiết kế
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## PEP chính đã định hình Python
| PEP | Năm | Tính năng |
|------|------|----------|
| 20 | 2004 | Thiền của Python |
| 257 | 2001 | Quy ước chuỗi tài liệu |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Biểu thức tạo |
| 342 | 2005 | `yield`dưới dạng biểu thức,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Gõ gợi ý |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | dây f |
| 572 | 2018 | Nhà điều hành hải mã`:=`|
| 622 | 2020 | Khớp mẫu cấu trúc |
| 654 | 2021 | Nhóm ngoại lệ |
| 684 | 2022 | Phiên dịch viên GIL |
| 703 | 2023 | Làm GIL tùy chọn |
## Tiến hóa hiệu suất
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Tăng trưởng cộng đồng & hệ sinh thái
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
