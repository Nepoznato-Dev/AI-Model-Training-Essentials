---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cpp, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C++ — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Mặt trận | 1983 | "C with Class" — lớp, kế thừa |
| C++98 | 1998 | Tiêu chuẩn ISO đầu tiên; STL, mẫu, ngoại lệ |
| C++03 | 2003 | Sửa lỗi |
| C++11 | 2011 | **Chính**: Di chuyển ngữ nghĩa, lambdas,`auto`, con trỏ thông minh,`nullptr`|
| C++14 | 2014 | Lambda chung, trả về `auto`,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, các liên kết có cấu trúc |
| C++20 | 2020 | **Chính**: Khái niệm, phạm vi, coroutine, mô-đun, `std::span`, so sánh ba chiều |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, suy ra`this`|
| C++26 | ~2026 | `std::execution`, phản ánh (dự kiến), hợp đồng |
## Các cột mốc quan trọng
### Thời kỳ tiền tiêu chuẩn (1983–1998)
- **1983**: Bjarne Stroustrup tạo ra "C with Class" tại Bell Labs
- **1985**: Đổi tên thành C++; ấn bản đầu tiên của "Ngôn ngữ lập trình C++"
- **1989**: Mẫu, ngoại lệ, không gian tên được đề xuất
- **1990**: STL (Thư viện mẫu tiêu chuẩn) của Alexander Stepanov
- **1991**: Mẫu được chuẩn hóa; "Hướng dẫn tham khảo C++ có chú thích"
### C++98 — Nền tảng (1998)
- Lớp, kế thừa, hàm ảo
- Mẫu (chức năng, lớp học, chuyên môn)
- STL:`vector`,`map`,`set`,`algorithm`,`iterator`
- Ngoại lệ (`try/catch/throw`)
-`namespace`,`bool`,`const_cast`,`dynamic_cast`
- Nhà xây dựng `explicit`, thành viên `mutable`
-RTTI (`typeid`, `dynamic_cast`)
### C++11 — Thời kỳ Phục hưng (2011)
- **Ngữ nghĩa di chuyển**: Tham chiếu giá trị `&&`,`std::move`
- **Con trỏ thông minh**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: suy luận kiểu
- **`nullptr`**: thay thế`NULL`
- **Lambda**:`[](int x) { return x * 2; }`
- **Phạm vi dành cho**:`for (auto& x : container)`
- **`constexpr`**: tính toán thời gian biên dịch
- **`static_assert`**: xác nhận tại thời điểm biên dịch
- **`using`**: gõ bí danh (thay thế`typedef`)
- **Mẫu đa dạng**:`template<typename... Args>`
- **`enum class`**: enum được gõ mạnh
- **`override`/`final`**: điều khiển chức năng ảo
- **`std::thread`**: luồng gốc
- **`std::atomic`**: lập trình không khóa
- **`std::function`/`std::bind`**: chức năng hạng nhất
### C++17 — Tinh chỉnh (2017)
-`std::optional<T>`,`std::variant<T...>`,`std::any`
-`if constexpr`— phân nhánh thời gian biên dịch
- Liên kết có cấu trúc:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Thuật toán song song:`std::execution::par`
- Không gian tên lồng nhau:`namespace A::B::C {}`
-`[[nodiscard]]`,`[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — Ngôn ngữ hiện đại (2020)
- **Khái niệm**:`template<std::integral T>`— các mẫu bị ràng buộc
- **Phạm vi**:`views::filter`,`views::transform`— đường dẫn lười biếng
- **Coroutine**:`co_await`,`co_yield`,`co_return`
- **Mô-đun**:`import`/`export`— biên dịch nhanh hơn
- **`std::span`**: chế độ xem không sở hữu dữ liệu liền kề
- **So sánh ba chiều**:`<=>`(người điều khiển tàu vũ trụ)
- **`std::format`**: Định dạng kiểu Python
- **`consteval`/`constinit`**: thực thi thời gian biên dịch
- **Công cụ khởi tạo được chỉ định**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: tự động tham gia chuỗi bằng mã thông báo dừng
### C++23 — Những cải tiến thực tế (2024)
-`std::expected<T, E>`— Xử lý lỗi lấy cảm hứng từ rỉ sét
-`std::print`/`std::println`— đầu ra được định dạng nhanh
-`std::flat_map`,`std::flat_set`
- Suy ra`this`— tham số đối tượng tường minh
-`std::mdspan`— nhịp đa chiều
-`std::generator`— máy phát điện đồng bộ
-`#include <debugging>`- điểm dừng, kết xuất
## Sự phát triển của các mẫu chính
```
Memory Management:
  1998: Raw pointers, manual new/delete
  2011: Smart pointers (unique_ptr, shared_ptr)
  2020: std::span, views (zero-copy abstractions)
  2023: std::expected (error without exceptions)

Error Handling:
  1998: Exceptions (try/catch)
  2011: noexcept, error codes
  2023: std::expected (Rust-inspired)
  2026: Contracts (expected)

Concurrency:
  1998: None (OS threads)
  2011: std::thread, std::mutex, std::atomic
  2017: Parallel algorithms
  2020: Coroutines, std::jthread

Abstraction:
  1998: Templates (unconstrained)
  2011: Move semantics, perfect forwarding
  2020: Concepts (constrained templates)
```

## Quy trình tiêu chuẩn
```
1998: C++98 (ISO/IEC 14882:1998)
2003: C++03 (defect fixes)
2011: C++11 — "modern C++" begins
2014: C++14 — incremental
2017: C++17 — incremental
2020: C++20 — another revolution
2024: C++23 — practical improvements
2026: C++26 — reflection, contracts (expected)

3-year release cycle since C++11
```

##Tác động đến hệ sinh thái
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
