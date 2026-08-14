<!--
---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [haskell, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Haskell — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Haskell 1.0 | 1990 | Phát hành lần đầu (nỗ lực của ủy ban) |
| Haskell 1.2 | 1992 | Thí nghiệm hệ thống đối tượng |
| Haskell 1.3 | 1996 | Loại lớp được giới thiệu |
| Haskell 1.4 | 1997 |  Đơn nguyên`IO`được làm rõ |
| Haskell 98 | 1998 | **Tiêu chuẩn ổn định đầu tiên** |
| Haskell 2010 | 2010 | **Tiêu chuẩn sửa đổi**, Cabal, mô-đun |
| GHC 7.0 | 2011 | Họ kiểu, kiểu dữ liệu |
| GHC 7.4 | 2012 | Đề xuất ứng dụng-Monad bắt đầu |
| GHC 7.6 | 2013 | Loại cải tiến gia đình |
| GHC 7.8 | 2014 | Từ đồng nghĩa mẫu,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Đề xuất đơn ứng dụng (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**,`MonadFail`, lỗi loại tùy chỉnh |
| GHC 8.2 | 2017 | Số tiền chưa đóng hộp, ba lô (hệ thống mô-đun) |
| GHC 8.4 | 2018 | Đường dẫn cơ sở trừu tượng,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail trong khúc dạo đầu |
| GHC 8.10 | 2020 | Ký hiệu`do`thống nhất, loại đa hình |
| GHC 9.0 | 2021 | **Đa hình lực hút**, loại tuyến tính |
| GHC 9.2 | 2022 |`do`đủ tiêu chuẩn, thông báo lỗi được cải thiện |
| GHC 9.4 | 2022 | **GHC2021** bộ mở rộng ngôn ngữ,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Đối số loại bắt buộc,`TypeAbstractions`|
| GHC 9,8 | 2024 | `TypeAbstractions`ổn định, thông báo lỗi được cải thiện |
| GHC 9.10 | 2024 | Cải tiến thêm, hiệu suất |
| GHC 9.12 | 2025 | Đang phát triển |
## Các cột mốc quan trọng
### Haskell 1.x — Những năm của Ủy ban (1990–1998)
- **1990**: Haskell 1.0 — ngôn ngữ chức năng lười biếng do ủy ban thiết kế
- **1.3 (1996)**: Loại lớp — tính năng xác định của Haskell
- **1.4 (1997)**: Đơn nguyên`IO`được làm rõ — cách xử lý thuần túy các tác dụng phụ
- **Haskell 98**: Tiêu chuẩn ổn định đầu tiên; vẫn được nhắc đến ngày hôm nay
### Haskell 2010 — Tiêu chuẩn hiện đại
- **2010**: Tiêu chuẩn sửa đổi — Cabal (hệ thống gói), cải tiến hệ thống mô-đun
- GHC trở thành trình biên dịch thực tế
- Cabal + Hackage = Hệ sinh thái trọn gói của Haskell
### GHC 7.x — Loại Sức mạnh hệ thống (2011–2015)
- Họ kiểu, kiểu dữ liệu, đa hình kiểu
- Đề xuất ứng dụng-Monad (AMP) - sửa chữa hệ thống phân cấp lớp loại
- Từ đồng nghĩa mẫu, phần mở rộng `Strict`
### GHC 8.x — Haskell hiện đại (2016–2020)
-`TypeApplications`— đối số loại rõ ràng tại các trang web cuộc gọi
- Lỗi loại tùy chỉnh - thông báo trình biên dịch tốt hơn
- Ba lô — hệ thống mô-đun cho thiết kế dựa trên thành phần
-`DerivingVia`— chiến lược phái sinh linh hoạt
### GHC 9.x — Cuộc cách mạng về khả năng sử dụng (2021–nay)
- **9.0**: Tính đa hình Levity, kiểu tuyến tính (an toàn tài nguyên)
- **9.2**:`do`đủ điều kiện, thông báo lỗi được cải thiện
- **9.4**: **GHC2021** — tiện ích mở rộng mặc định hiện đại; `OverloadedRecordDot`(truy cập trường bằng`.`)
- **9.6**: Đối số loại bắt buộc,`TypeAbstractions`
- **9,8–9,12**: Tiếp tục cải tiến thông báo lỗi, hiệu suất
## Tiến hóa cú pháp
```haskell
-- Haskell 98: Basic type classes
class Eq a where
  (==) :: a -> a -> Bool

-- GHC extensions: Type applications (GHC 8.0)
-- Before:
read "[1,2,3]" :: [Int]
-- After:
read @[Int] "[1,2,3]"

-- GHC 9.4: OverloadedRecordDot
-- Before:
name (getPerson user)
-- After:
user.person.name

-- GHC 9.0: Linear types
-- Before:
processFile :: FilePath -> IO Result
-- After:
processFile :: FilePath %1 -> IO Result  -- file handle used exactly once

-- GHC 8.0: Custom type errors
type family ErrorMessage (a :: Type) :: ErrorMessage where
  ErrorMessage (NotSerializable a) =
    'Text "Cannot serialize type " ':<>: 'ShowType a
```

## Loại tiến hóa hệ thống
```
Haskell 1.0:  Basic types, algebraic data types, pattern matching
Haskell 1.3:  Type classes
Haskell 98:   Multi-parameter type classes, functional dependencies
GHC 6.x:     GADTs, type families, rank-N types
GHC 7.0:     Data kinds, kind polymorphism
GHC 7.10:    Applicative-Monad Proposal
GHC 8.0:     TypeApplications, custom type errors
GHC 8.2:     Unboxed sums
GHC 9.0:     Levity polymorphism, linear types
GHC 9.4:     OverloadedRecordDot, GHC2021
GHC 9.6:     Required type arguments, TypeAbstractions
```

## Đồng thời & Song song
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Nguyên tắc thiết kế chính
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Tăng trưởng hệ sinh thái
```
1990: Haskell 1.0 — academic curiosity
1998: Haskell 98 — stable standard
2007: Cabal + Hackage — package ecosystem
2010: Haskell 2010 — revised standard
2012: Stack build tool — reproducible builds
2015: Haskell in industry — Facebook, Standard Chartered, Well-Typed
2021: GHC 9.0 — levity polymorphism, linear types
2023: GHC 9.6 — type abstractions
2025: Haskell used in finance, compilers, formal verification,
       blockchain (Cardano), and academic research
       GHC, Stack, Cabal; key libraries: lens, aeson, servant, yesod
```
