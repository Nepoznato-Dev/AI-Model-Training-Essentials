---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Go — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Ngày phát hành | Chủ đề chính |
|----------|-------------|----------|
| 1.0 | Tháng 3 năm 2012 | Bản phát hành ổn định đầu tiên |
| 1.1 | Tháng 5 năm 2013 | Hiệu suất, máy dò chủng tộc |
| 1.3 | Tháng 6 năm 2014 | Thăm dò mạng, tiền điện tử/tls |
| 1.4 | Tháng 12 năm 2014 | Bootstrap với Go (tự lưu trữ) |
| 1,5 | Tháng 8 năm 2015 | **GC đồng thời**, rào cản viết |
| 1.7 | Tháng 8 năm 2016 |  Gói `context`, bài kiểm tra phụ`testing`|
| 1.8 | Tháng 2 năm 2017 | `http.Server.Shutdown`, plugin |
| 1.9 | Tháng 8 năm 2017 | Nhập bí danh, song song`make`|
| 1.10 | Tháng 2 năm 2018 |  Nhóm kết nối`database/sql`|
| 1.11 | Tháng 8 năm 2018 | **Đi mô-đun**,`go mod`|
| 1.12 | Tháng 2 năm 2019 | TLS 1.3, phiên bản mô-đun |
| 1.13 | Tháng 9 năm 2019 | `errors.Is/As`, chữ số`0b`,`0o`|
| 1.14 | Tháng 2 năm 2020 | **I/O chồng chéo trên Windows**, ưu tiên goroutine |
| 1.15 | Tháng 8 năm 2020 |  Đặt lại`time.Ticker`/ `Timer`, proxy mô-đun |
| 1.16 | Tháng 2 năm 2021 |  Gói `embed`, `io/fs`, nhận biết mô-đun theo mặc định |
| 1.17 | Tháng 8 năm 2021 | Chuyển đổi lát thành mảng,`unsafe.Slice`|
| 1.18 | Tháng 3 năm 2022 | **Generics**, làm mờ, không gian làm việc |
| 1.19 | Tháng 8 năm 2022 | Nhận xét tài liệu, sửa đổi mô hình bộ nhớ |
| 1,20 | Tháng 2 năm 2023 | `errors.Join`, tối ưu hóa theo hướng dẫn hồ sơ |
| 1,21 | Tháng 8 năm 2023 | **`slog`**, nội dung `min/max`,`maps/slices`|
| 1,22 | Tháng 2 năm 2024 | Phạm vi trên số nguyên, định tuyến nâng cao |
| 1.23 | Tháng 8 năm 2024 | Gói Iterator (`iter`), thay đổi bộ đếm thời gian |
| 1,24 | Tháng 2 năm 2025 |  Gói `weak`, bản đồ được cải tiến |
## Các cột mốc quan trọng
### Sự khởi đầu (2009–2012)
- **2009**: Go được Google công bố (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "Lời hứa tương thích với Go 1"
### Hiệu suất & Công cụ (2012–2018)
- **1.1**: Cải thiện hiệu suất hơn 30%; máy dò cuộc đua
- **1,5**: Trình thu gom rác đồng thời (GC tạm dừng giảm từ mili giây xuống micro giây)
- **1.5**: Trình biên dịch Go được khởi động — viết bằng Go (không còn C)
- **1.7**: Gói`context`trở thành gói tiêu chuẩn
### Mô-đun & Hệ sinh thái (2018–2021)
- **1.11**: **Go module** — quản lý phần phụ thuộc chính thức
- **1.13**:`errors.Is/As`— việc gói lỗi trở thành thành ngữ
- **1.16**: Gói`embed`— nhúng tệp tại thời điểm biên dịch
### Cờ vây hiện đại (2022–nay)
- **1.18**: **Generics** — nhập tham số có ràng buộc
- **1.21**:`slog`— ghi nhật ký có cấu trúc trong stdlib;  Nội dung `min/max`
- **1.22**: Phạm vi trên số nguyên (`for i := range 10`)
- **1.23**: Gói Iterator — đánh giá lười biếng trong stdlib
## Hành trình Generics
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Triết lý xử lý lỗi
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Tiến hóa đồng thời
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Cam kết tương thích
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## Tăng trưởng hệ sinh thái
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Tiến hóa hiệu suất
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
