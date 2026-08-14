---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lua, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Lua — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 1.0 | 1994 | Bản phát hành lần đầu (PUC-Rio, Brazil) |
| 2.1 | 1995 | Bảng trở thành cấu trúc dữ liệu duy nhất |
| 3.0 | 1997 | API C, phương thức gắn thẻ (siêu phương thức ban đầu) |
| 3.1 | 1998 | Bộ điều khiển ngữ nghĩa (giá trị nâng cao) |
| 4.0 | 2000 | **Lua 4**: đếm lại + GC, API C được cải tiến |
| 5.0 | 2003 | **Chính**: phạm vi từ vựng thích hợp, coroutines, metatables, Booleans |
| 5.1 | 2006 | **GC tăng dần**, toán tử độ dài `#`,`goto`đã bị xóa,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`thay đổi,`goto`được thêm lại, bảng phù du |
| 5.3 | 2015 | **Loại số nguyên**, toán tử bitwise, hỗ trợ UTF-8 |
| 5.4 | 2020 | **Biến GC thế hệ**,`const`/ `close`, siêu phương thức`tostring`|
| 5.4.x | 2020–25 | Cải tiến dần dần, hệ thống cảnh báo |
| 5,5 | TBD | (tương lai) Cải tiến GC hơn nữa |
## Các cột mốc quan trọng
### Lua 1–3: Những năm đầu (1994–1999)
- **1994**: Được tạo ra tại PUC-Rio (Đại học Công giáo Giáo hoàng Rio de Janeiro) bởi Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Mục tiêu**: Ngôn ngữ tập lệnh có thể nhúng để nhập dữ liệu (không phải ngôn ngữ độc lập)
- **2.1**: Bảng trở thành cấu trúc dữ liệu duy nhất — sự đơn giản triệt để
- **3.0**: C API được củng cố — giúp Lua có thể nhúng được trong các ứng dụng C/C++
- **3.1**: Giá trị tăng — phạm vi từ vựng cho các bao đóng
### Lua 4: Trưởng thành (2000)
- Đếm tham chiếu + thu gom rác (hybrid)
- API C được cải tiến - Thư viện phụ trợ `luaL_*`
- Vẫn chưa có phạm vi từ vựng phù hợp cho toàn cầu
### Lua 5.0: Lua hiện đại (2003)
- **Phạm vi từ vựng phù hợp** — Biến `local`
- **Coroutines** — đa nhiệm hợp tác
- **Siêu dữ liệu** — nạp chồng toán tử, hành vi tùy chỉnh
- **Booleans** —`true`/`false`làm giá trị phù hợp
- **Đóng cửa** được thực hiện đúng — nâng cao giá trị tổng quát
- Đây là phiên bản khiến Lua được áp dụng rộng rãi trong game
### Lua 5.1: Tiêu chuẩn (2006)
- **Bộ thu gom rác gia tăng**
- Toán tử độ dài `#`
- Chức năng `module()`
- Thay đổi cách hoạt động của môi trường toàn cầu
- **Phiên bản này trở thành phiên bản được nhúng rộng rãi nhất** (LuaJIT nhắm mục tiêu 5.1)
### Lua 5.2: Cải tiến (2011)
-`_ENV`- môi trường trên mỗi chunk (toàn cầu sạch hơn)
- Câu lệnh`goto`trả về
- Bảng phù du (cải thiện GC)
- Cải tiến hệ thống gói
### Lua 5.3: Số nguyên & Bit (2015)
- **Loại con số nguyên** — khác với float
- **Toán tử bitwise** —`&`,`|`,`~`,`<<`,`>>`
- **Hỗ trợ UTF-8** — thư viện`utf8`tích hợp
- Phân tầng`//`
- Chuỗi `pack`/`unpack` cho dữ liệu nhị phân
### Lua 5.4: GC thế hệ (2020)
- **Trình thu gom rác thế hệ** — tạm dừng GC tốt hơn nhiều
- ** Biến `<const>`** — hằng số thực
- ** Biến `<close>`** — các biến sắp đóng (quản lý tài nguyên, như`defer`hoặc`with`)
- Siêu phương pháp `tostring`
- Các kiểu con chuỗi (chuỗi ngắn và chuỗi dài được tối ưu hóa khác nhau)
## Tiến hóa cú pháp
```lua
-- Lua 4.0: No local scoping for globals
x = 10  -- always global unless in a function

-- Lua 5.0: Proper lexical scoping
local x = 10  -- local to block
do
  local y = 20
  print(x + y)  -- 30
end

-- Lua 5.1: Length operator, module
local t = {1, 2, 3}
print(#t)  -- 3
module("mymodule", package.seeall)

-- Lua 5.3: Integer type, bitwise
local a = 10    -- integer
local b = 10.0  -- float
print(a & 0xFF) -- bitwise AND: 10
print(a >> 1)   -- right shift: 5

-- Lua 5.4: const and close variables
local x <const> = 42  -- constant, cannot change
local f <close> = io.open("file.txt")  -- auto-closed at scope end
```

## Tiến hóa tính năng
```
Lua 1.0:  Tables, functions, strings, numbers, C API
Lua 2.1:  Tables as only data structure
Lua 3.0:  Tag methods (predecessor to metatables)
Lua 3.1:  Upvalues (closures)
Lua 4.0:  Hybrid GC (ref counting + cycle collection)
Lua 5.0:  Coroutines, metatables, proper lexical scoping, booleans
Lua 5.1:  Incremental GC, # operator, module()
Lua 5.2:  _ENV, goto, ephemeron tables
Lua 5.3:  Integer type, bitwise ops, UTF-8, //, pack/unpack
Lua 5.4:  Generational GC, <const>, <close>, tostring metamethod
```

## Lua trong game
```
1997: LucasArts uses Lua in game scripting (Grim Fandango)
2003: Lua 5.0 — game industry adoption accelerates
2005: World of Warcraft uses Lua for UI addons
2006: LuaJIT (Mike Pall) — JIT-compiled Lua 5.1, extremely fast
2010: Love2D game framework (Lua-based)
2012: Defold game engine (Lua scripting)
2015: Roblox adopts Luau (Lua dialect with types)
2020: Lua 5.4 — continued game engine integration
2025: Lua remains the #1 embedded scripting language in games
       Used in: Unity (via plugins), WoW, Garry's Mod, Factorio,
       Civilization, Adobe Lightroom, Nginx (OpenResty), Redis
```

## Nguyên tắc thiết kế chính
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Tăng trưởng hệ sinh thái
```
1994: Lua created at PUC-Rio (Brazil)
1997: First game industry use (LucasArts)
2003: Lua 5.0 — widespread game adoption
2005: LuaJIT — JIT-compiled Lua
2006: Lua 5.1 — the "standard" embedded version
2010: OpenResty (Nginx + Lua) — web development
2015: Luau (Roblox) — typed Lua dialect
2020: Lua 5.4 — modern GC, resource management
2025: Lua is the dominant embedded scripting language
       Powers: games, Nginx, Redis, Wireshark, Lightroom, more
```
