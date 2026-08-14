---
# Metadata
title: "Lua — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lua ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lua, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Lua — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, thư viện và cơ sở hạ tầng thiết yếu trong hệ sinh thái Lua.
---

## Phiên bản và triển khai Lua
| Thực hiện | Ghi chú |
|--------------|-------|
| **Lua 5.4** | Phiên bản ổn định hiện tại |
| **LuaJIT** | Trình biên dịch JIT hiệu suất cao |
| **Lua 5.1** | Được sử dụng rộng rãi (tương thích với LuaJIT) |
| **Ravi** | JIT với kiểu gõ tùy chọn |
| **Màu xanh mòng két** | Phương ngữ đánh máy của Lua |
| **thì là** | Lisp biên dịch thành Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **LuaRocks** | Quản lý gói tiêu chuẩn |
| **luarocks.org** | Kho gói |
| **sáng** | Trình quản lý gói LuaJIT |
```bash
luarocks install luasocket  # install package
luarocks list               # installed packages
luarocks remove luasocket   # remove package
```

```lua
-- .luarocks configuration
-- luarocks config
rocks_servers = {
    "https://luarocks.org"
}
```

---

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **OpenResty** | Nginx + Lua | Web hiệu suất cao |
| **Luvit** | Giống như Node.js | I/O không đồng bộ (libuv) |
| **Quỹ đạo** | Web MVC | Ứng dụng web đơn giản |
| **Thủy thủ** | Toàn ngăn xếp | Khung MVC |
| **đá quý** | Dựa trên OpenResty | Trang web MoonScript/Lua |
| **Pegasus** | Nhẹ | Máy chủ HTTP đơn giản |
```lua
-- OpenResty / Nginx Lua example
-- nginx.conf
location /hello {
    content_by_lua_block {
        ngx.say("Hello, World!")
    }
}

location /api/users {
    content_by_lua_block {
        local cjson = require "cjson"
        local id = ngx.var.arg_id
        local user = get_user(id)
        ngx.header.content_type = "application/json"
        ngx.say(cjson.encode(user))
    }
}
```

---

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **luasql** | Liên kết cơ sở dữ liệu (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Ràng buộc SQLite3 |
| **pgmoon** | PostgreSQL (Lua thuần túy) |
```lua
-- SQLite example
local lsqlite3 = require "lsqlite3"

local db = lsqlite3.open("mydb.sqlite")

db:exec[[
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
  )
]]

local stmt = db:prepare("SELECT * FROM users WHERE id = ?")
stmt:bind_values(1)
for row in stmt:nrows() do
    print(row.id, row.name, row.email)
end
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **bị bắt** | Thử nghiệm kiểu BDD (phổ biến nhất) |
| **luassert** | Thư viện xác nhận (bị hỏng) |
| **ham muốn** | Kiểm tra tối thiểu |
| **điên rồ nhất** | thử nghiệm kiểu xUnit |
| **màu xanh mòng két** | Kiểm tra kiểu (phương ngữ Teal) |
```lua
-- busted example
describe("UserService", function()
    local service

    before_each(function()
        service = UserService.new()
    end)

    describe("find", function()
        it("returns user when found", function()
            service:add(User.new(1, "Alice"))
            local user = service:find(1)
            assert.is_not_nil(user)
            assert.are.equal("Alice", user.name)
        end)

        it("returns nil when not found", function()
            local user = service:find(999)
            assert.is_nil(user)
        end)
    end)
end)
```

```bash
busted spec/              # run tests
busted --verbose spec/    # verbose output
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **luacheck** | Linting và phân tích tĩnh |
| **định dạng lua** | Định dạng mã |
| **stylua** | Trình định dạng mã (Dựa trên Rust, nhanh) |
| **màu xanh mòng két** | Đã gõ phương ngữ Lua |
| **luacov** | Bảo hiểm mã |
```lua
-- .luacheckrc
std = "lua54"
include_files = {"src/**/*.lua"}
exclude_files = {"spec/**"}

codes = true
ignore = {"631"}  -- ignore line length
```

```bash
luacheck src/           # lint
stylua src/             # format
```

---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **luasocket** | Mạng TCP/UDP/HTTP |
| **lua-cjson / cjson** | Phân tích cú pháp JSON |
| **lpeg** | Khớp mẫu (dựa trên PEG) |
| **Đèn bút (pl)** | Thư viện tiện ích (như Python stdlib) |
| **copas** | Ổ cắm dựa trên Coroutine |
| **coxpcall** | Cuộc gọi được bảo vệ |
| **lua-resty-* | Hệ sinh thái OpenResty |
| **lfs** | Truy cập hệ thống tập tin |
| **lzlib** | Nén |
| **lbase64** | Mã hóa Base64 |
| **kiểm tra** | Bàn in đẹp |
| **cổ điển** | Hệ thống lớp OOP |
| **tầng lớp trung lưu** | Thư viện OOP |
| **ham muốn** | Mẫu ria mép |
| **argparse** | Phân tích đối số CLI |
---

## Phát triển trò chơi
| Động cơ | Ghi chú |
|--------|-------|
| **TÌNH YÊU (Love2D)** | Khung trò chơi 2D (phổ biến nhất) |
| **Giải trừ** | Công cụ trò chơi (Lua scripting) |
| **SDK Corona** | Công cụ trò chơi di động |
| **Roblox** | Nền tảng trò chơi (phương ngữ Luau) |
| **Thế giới Warcraft** | Kịch bản giao diện người dùng (Lua) |
| **Neovim** | Biên tập viên (Lua scripting) |
| **Làm lại** | Tập lệnh Lua trong Redis |
| **Nginx/OpenResty** | Tập lệnh Lua trong Nginx |
```lua
-- LÖVE example
function love.load()
    x, y = 400, 300
end

function love.update(dt)
    if love.keyboard.isDown("left") then x = x - 200 * dt end
    if love.keyboard.isDown("right") then x = x + 200 * dt end
end

function love.draw()
    love.graphics.circle("fill", x, y, 50)
end
```

---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + Lua (sumneko)** | Lua LSP tốt nhất |
| **ZeroBrane Studio** | IDE dành riêng cho Lua |
| **Neovim** | Cấu hình Lua (hạng nhất) |
| **IntelliJ + EmmyLua** | Hỗ trợ JetBrains Lua |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Độc lập** | Gói Lua với ứng dụng |
| **LuaRocks** | Đóng gói và phân phối |
| **OpenResty** | Triển khai Nginx + Lua |
| **Docker** | Được đóng gói |
| **Đã nhúng** | Vào các ứng dụng C/C++ |
| **Nền tảng trò chơi** | TÌNH YÊU, Defold, Roblox |
---

## Bản tóm tắt
Hệ sinh thái của Lua tuy nhỏ nhưng tập trung vào việc nhúng và viết kịch bản. Chuỗi công cụ tiêu chuẩn là: **Lua 5.4** hoặc **LuaJIT** làm thời gian chạy, **LuaRocks** cho các gói, **busted** để thử nghiệm, **luacheck** để tìm lỗi mã nguồn, **stylua** để định dạng. Lua vượt trội khi trở thành ngôn ngữ nhúng trong trò chơi (LÖVE, Defold, Roblox), máy chủ (OpenResty, Nginx), cơ sở dữ liệu (Redis) và trình soạn thảo (Neovim). LuaJIT cung cấp hiệu suất gần C cho các tập lệnh tính toán chuyên sâu. Điểm mạnh của Lua là dung lượng nhỏ (~25KB), cú pháp đơn giản và API nhúng tuyệt vời để tích hợp C/C++.