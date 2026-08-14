<!--
---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ruby — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 0,95 | 1995 | Bản phát hành đầu tiên (Yukihiro "Matz" Matsumoto) |
| 1.0 | 1996 | Bản phát hành ổn định đầu tiên |
| 1.2 | 1998 | Tài liệu tiếng Anh đầu tiên |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | Cải tiến việc thu gom rác |
| 1.8 | 2003 | $KCODE, công cụ biểu thức chính quy oniguruma |
| 1.9 | 2007 | **Chính**: M17N (đa ngôn ngữ), cú pháp băm mới, sợi |
| 2.0 | 2013 | Đối số từ khóa,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | Cuộc gọi phương thức tinh tế,`frozen_string_literal`|
| 2.2 | 2014 | Ký hiệu GC, GC tăng dần |
| 2.3 | 2015 | Pragma theo nghĩa đen chuỗi đông lạnh,`&.`điều hướng an toàn |
| 2.4 | 2016 | `Integer`hợp nhất, ánh xạ trường hợp Unicode`String`|
| 2,5 | 2017 | `yield_self`, khối trong`rescue`/`ensure`|
| 2.6 | 2018 | **Trình biên dịch JIT (MJIT)**, phạm vi vô tận`1..`|
| 2.7 | 2019 | Khớp mẫu (thử nghiệm), thông số khối được đánh số |
| 3.0 | 2020 | **Chính**: Ractor (đồng thời), Bộ lập lịch sợi, các loại RBS |
| 3.1 | 2021 |  Chuyển tiếp khối `Anonymous`,`Hash#compact`|
| 3.2 | 2022 |  Lớp `Data`, cải tiến `File.realpath`, sản xuất YJIT |
| 3.3 | 2023 | **YJIT** cải tiến lớn, tham số khối`it`|
| 3,4 | 2024 | Trình phân tích cú pháp lăng kính mặc định,`it`làm thông số khối mặc định |
## Các cột mốc quan trọng
### Ruby sơ khai (1995–2003)
- **1995**: Matz tạo ra Ruby — pha trộn Perl, Smalltalk, Lisp
- **1.0 (1996)**: Bản phát hành ổn định đầu tiên
- **1.8 (2003)**: Ruby "cổ điển" — nhanh, ổn định, được áp dụng rộng rãi
### Kỷ nguyên Rails (2004–2013)
- **2004**: Ruby on Rails được phát hành — cuộc cách mạng phát triển web
- **1.9 (2007)**: M17N (chuỗi đa ngôn ngữ), cú pháp băm mới`{key: value}`, Fibers
- **2.0 (2013)**: Đối số từ khóa, bộ liệt kê lười biếng, `Module#prepend`
### Ruby hiện đại (2015–nay)
- **2.6 (2018)**: Trình biên dịch JIT (MJIT) — lần đẩy hiệu suất đầu tiên
- **2.7 (2019)**: Khớp mẫu (thử nghiệm), thông số khối được đánh số`_1`
- **3.0 (2020)**: **Ractor** (Đồng thời mô hình diễn viên), **Bộ lập lịch sợi** (I/O không đồng bộ), **RBS** (chữ ký loại)
- **3.2 (2022)**: Lớp`Data`(đối tượng có giá trị bất biến), sẵn sàng sản xuất YJIT
- **3.3 (2023)**: Tăng tốc chính của YJIT (nhanh hơn tới 3 lần), tham số khối `it`
- **3.4 (2024)**: Trình phân tích cú pháp lăng kính trở thành mặc định
## Tiến hóa hiệu suất
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## Tiến hóa đồng thời
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## Tiến hóa khớp mẫu
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## Nguyên tắc thiết kế chính
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## Tăng trưởng hệ sinh thái
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
