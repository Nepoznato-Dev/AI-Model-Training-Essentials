---
# Metadata
title: "Lua"
description: "Comprehensive reference for the Lua programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [lua, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "26 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Lua
Lua là một ngôn ngữ kịch bản nhẹ, có thể nhúng được thiết kế để mở rộng các ứng dụng. Được tạo ra vào năm 1993 tại Đại học Công giáo Giáo hoàng Rio de Janeiro ở Brazil, Lua là một trong những ngôn ngữ lập trình nhanh nhất hiện có. Dung lượng nhỏ của nó (trình thông dịch là ~ 120KB) và tính đơn giản khiến nó trở thành lựa chọn phù hợp cho việc viết kịch bản, hệ thống nhúng và cấu hình phát triển trò chơi.
Lua được biết đến nhiều nhất là ngôn ngữ kịch bản đằng sau Roblox (nền tảng chơi game có hơn 200 triệu người dùng hàng tháng), tiện ích bổ sung World of Warcraft và nhiều công cụ trò chơi (Love2D, Defold, Corona SDK). Nó cũng được sử dụng trong Nginx (OpenResty), Redis và Wireshark.
---

## Tại sao Lua lại quan trọng
- **Có thể nhúng**: Được thiết kế để nhúng vào các ứng dụng khác — máy chủ cung cấp chức năng.
- **Dấu chân nhỏ**: Toàn bộ trình thông dịch có kích thước ~120KB. Lý tưởng cho các hệ thống nhúng.
- **Nhanh**: Một trong những ngôn ngữ viết kịch bản được diễn giải nhanh nhất.
- **Đơn giản**: Chỉ ~20 từ khóa. Dễ dàng học hỏi và hòa nhập.
- **Phát triển trò chơi**: Ngôn ngữ kịch bản tiêu chuẩn cho nhiều công cụ và nền tảng trò chơi.
- **Roblox**: Cung cấp năng lượng cho toàn bộ hệ sinh thái Roblox — hàng triệu trò chơi do người dùng tạo.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Thư viện tiêu chuẩn có giới hạn** | Chức năng tích hợp tối thiểu | Mở rộng bằng C/C++ hoặc sử dụng gói LuaRocks |
| **Lập chỉ mục dựa trên 1** | Mảng bắt đầu từ chỉ số 1 (không bình thường đối với các lập trình viên) | Chấp nhận như một sự lựa chọn thiết kế; nhất quán xuyên suốt |
| **Không có lớp học** | Chỉ các bảng và siêu dữ liệu - OOP phải được triển khai thủ công | Sử dụng siêu dữ liệu hoặc thư viện OOP |
| **Trò chơi thích hợp bên ngoài** | Sử dụng hạn chế trong web, khoa học dữ liệu hoặc doanh nghiệp | Sử dụng để viết/nhúng; ngôn ngữ khác cho ứng dụng |
| **Thị trường việc làm nhỏ** | Chủ yếu là phát triển trò chơi và các vai trò nhúng | Sự phát triển của Roblox là một lĩnh vực đang phát triển |
---

##Cơ bản về cú pháp
```lua
-- Variables
local name = "Alice"
local age = 30
local score = 9.5

-- Tables (the only data structure — used as arrays, maps, objects)
local user = {name = "Alice", age = 30}
local fruits = {"apple", "banana", "cherry"}  -- Array (1-indexed!)

print(user.name)        -- "Alice"
print(fruits[1])        -- "apple" (Lua arrays start at 1)

-- Functions
local function greet(name, greeting)
    greeting = greeting or "Hello"  -- Default value
    return greeting .. ", " .. name .. "!"
end

-- Higher-order functions
local function apply(fn, value)
    return fn(value)
end

local double = function(x) return x * 2 end
print(apply(double, 5))  -- 10

-- Conditionals and loops
if age >= 18 then
    print("Adult")
elseif age >= 13 then
    print("Teenager")
else
    print("Child")
end

for i = 1, 10 do
    print(i)
end

for index, fruit in ipairs(fruits) do
    print(index, fruit)
end

-- Metatables (OOP-like behaviour)
local Animal = {}
Animal.__index = Animal

function Animal.new(name)
    local self = setmetatable({}, Animal)
    self.name = name
    return self
end

function Animal:speak()
    return self.name .. " makes a sound"
end

local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
    local self = Animal.new(name)
    return setmetatable(self, Dog)
end

function Dog:speak()
    return self.name .. " says woof"
end

local rex = Dog.new("Rex")
print(rex:speak())  -- "Rex says woof"
```

---

## Cú pháp & Mẫu nâng cao
### Metatables — Nền tảng sức mạnh của Lua
```lua
-- Metatables allow custom behaviour for tables
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable({x = x, y = y}, Vector)
end

-- Operator overloading via metamethods
function Vector.__add(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end

function Vector.__mul(a, b)
    if type(b) == "number" then
        return Vector.new(a.x * b, a.y * b)
    end
    return a.x * b.x + a.y * b.y  -- Dot product
end

function Vector.__tostring(v)
    return string.format("Vector(%.1f, %.1f)", v.x, v.y)
end

function Vector.__eq(a, b)
    return a.x == b.x and a.y == b.y
end

function Vector:magnitude()
    return math.sqrt(self.x^2 + self.y^2)
end

local v1 = Vector.new(3, 4)
local v2 = Vector.new(1, 2)
print(v1 + v2)          -- Vector(4.0, 6.0)
print(v1 * 2)           -- Vector(6.0, 8.0)
print(v1 * v2)          -- 11 (dot product)
print(v1:magnitude())   -- 5.0
print(v1 == Vector.new(3, 4))  -- true
```

### Đóng cửa và các mẫu chức năng
```lua
-- Closures — functions capture upvalues
local function make_counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

local counter = make_counter()
print(counter())  -- 1
print(counter())  -- 2
print(counter())  -- 3

-- Functional utilities
local function map(t, fn)
    local result = {}
    for i, v in ipairs(t) do
        result[i] = fn(v)
    end
    return result
end

local function filter(t, fn)
    local result = {}
    for _, v in ipairs(t) do
        if fn(v) then result[#result + 1] = v end
    end
    return result
end

local function reduce(t, fn, init)
    local acc = init
    for _, v in ipairs(t) do
        acc = fn(acc, v)
    end
    return acc
end

local numbers = {1, 2, 3, 4, 5}
local doubled = map(numbers, function(x) return x * 2 end)
local evens = filter(numbers, function(x) return x % 2 == 0 end)
local sum = reduce(numbers, function(a, b) return a + b end, 0)
```

### Nhiều giá trị trả về và phá hủy
```lua
-- Lua functions can return multiple values
local function minmax(t)
    local min, max = math.huge, -math.huge
    for _, v in ipairs(t) do
        if v < min then min = v end
        if v > max then max = v end
    end
    return min, max
end

local lo, hi = minmax({5, 2, 8, 1, 9, 3})
print(lo, hi)  -- 1  9

-- Variadic functions
local function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end

print(sum(1, 2, 3, 4, 5))  -- 15

-- Table unpacking
local a, b, c = table.unpack({10, 20, 30})
print(a, b, c)  -- 10  20  30
```

### Mẫu chuỗi (Thay thế Regex của Lua)
```lua
-- Lua patterns — simpler than regex but powerful
local text = "Error 404: Page not found on 2024-01-15"

-- Basic matching
local code, msg = text:match("Error (%d+): (.+)")
print(code)  -- "404"
print(msg)   -- "Page not found on 2024-01-15"

-- Find and replace
local replaced = text:gsub("not found", "missing")

-- Pattern character classes
-- %a = letters, %d = digits, %w = alphanumeric
-- %s = whitespace, %p = punctuation
local email = "user@example.com"
local valid = email:match("^[%w%.%-]+@[%w%.%-]+%.%a+$")

-- Capture groups
local date = "2024-01-15"
local year, month, day = date:match("(%d+)-(%d+)-(%d+)")
```

---

## Đồng thời & Song song
### Coroutines — Đa nhiệm hợp tác
```lua
-- Coroutines — Lua's built-in cooperative concurrency
local function producer()
    local items = {"apple", "banana", "cherry"}
    for _, item in ipairs(items) do
        print("Producing: " .. item)
        coroutine.yield(item)
    end
    return "done"
end

local co = coroutine.create(producer)

print(coroutine.status(co))  -- "suspended"
local ok, value = coroutine.resume(co)
print("Got:", value)         -- Got: apple
print(coroutine.status(co))  -- "suspended"

coroutine.resume(co)  -- banana
coroutine.resume(co)  -- cherry
print(coroutine.status(co))  -- "dead"
```

### Mẫu lặp dựa trên Coroutine
```lua
-- Coroutine wrapping for clean iteration
local function coroutine_iterator(body)
    local co = coroutine.create(body)
    return function()
        local ok, value = coroutine.resume(co)
        if not ok or coroutine.status(co) == "dead" then
            return nil
        end
        return value
    end
end

-- Usage: generate fibonacci numbers lazily
local fib = coroutine_iterator(function()
    local a, b = 0, 1
    while true do
        coroutine.yield(a)
        a, b = b, a + b
    end
end)

for i = 1, 10 do
    io.write(fib() .. " ")  -- 0 1 1 2 3 5 8 13 21 34
end

-- Coroutine-based async I/O (with Copas or OpenResty)
local copas = require("copas")

local function fetch_url(url)
    local sock = copas.tcp()
    sock:connect(url, 80)
    sock:send("GET / HTTP/1.1\r\nHost: " .. url .. "\r\n\r\n")
    local response = sock:receive("*a")
    sock:close()
    return response
end

-- Multiple concurrent connections
copas.addthread(fetch_url, "example.com")
copas.addthread(fetch_url, "example.org")
copas.loop()
```

---

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
```
my-lua-project/
├── src/
│   ├── main.lua
│   ├── config.lua
│   ├── models/
│   ├── utils/
│   └── game/
├── spec/
│   └── test_main.lua
├── rocks/           -- LuaRocks packages
├── .luacheckrc      -- Linting config
├── Makefile
└── rockspec         -- Package spec
```

### LuaRocks — Quản lý gói
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — Đặc tả gói
```lua
-- myproject-1.0-1.rockspec
package = "myproject"
version = "1.0-1"

source = {
    url = "git+https://github.com/user/myproject.git",
    tag = "v1.0",
}

dependencies = {
    "lua >= 5.3",
    "luasocket",
    "lua-cjson",
}

build = {
    type = "builtin",
    modules = {
        ["myproject.core"] = "src/core.lua",
        ["myproject.utils"] = "src/utils.lua",
    },
}
```

### Đường dẫn CI/CD (Hành động trên GitHub)
```yaml
name: Lua CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    strategy:
      matrix:
        lua-version: ['5.3', '5.4', 'luajit']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: leafo/gh-actions-lua@v10
        with:
          luaVersion: ${{ matrix.lua-version }}
      - uses: leafo/gh-actions-luarocks@v4
      - run: luarocks install busted
      - run: luarocks install luacheck
      - run: luacheck src/
      - run: busted spec/
```
---

##Thử nghiệm
### Busted — Khung kiểm tra
```lua
-- spec/utils_spec.lua
local utils = require("src.utils")

describe("utils", function()
    describe("add", function()
        it("adds two positive numbers", function()
            assert.are.equal(utils.add(2, 3), 5)
        end)
        it("handles negative numbers", function()
            assert.are.equal(utils.add(-1, 1), 0)
        end)
    end)
    describe("format_name", function()
        it("capitalizes first letter", function()
            assert.are.equal(utils.format_name("alice"), "Alice")
        end)
    end)
end)
```

### Chế nhạo bằng luassert
```lua
describe("UserService", function()
    local service, mock_repo
    before_each(function()
        mock_repo = {
            save = spy.new(function() return true end),
            find = spy.new(function(id) return {id=id, name="Alice"} end),
        }
        service = require("src.user_service").new(mock_repo)
    end)
    it("saves user via repository", function()
        service:create("Alice", "alice@example.com")
        assert.spy(mock_repo.save).was_called(1)
    end)
end)
```

### Lệnh kiểm tra
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## Khả năng tương tác
### C API — Nhúng Lua vào C
```c
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

int main(void) {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    luaL_dofile(L, "script.lua");
    lua_getglobal(L, "greet");
    lua_pushstring(L, "World");
    lua_pcall(L, 1, 1, 0);
    printf("Lua says: %s\n", lua_tostring(L, -1));
    lua_close(L);
    return 0;
}
// Compile: gcc -o host host.c -llua5.4
```

### LuaJIT FFI — Cuộc gọi C trực tiếp
```lua
local ffi = require("ffi")
ffi.cdef[[
    double sqrt(double x);
    int abs(int n);
]]
local C = ffi.C
print(C.sqrt(144))   -- 12.0
print(C.abs(-42))    -- 42
```

---

## Mẫu thiết kế
### Mẫu mô-đun (Singleton)
```lua
-- config.lua — modules are singletons by design
local config = {
    debug = false,
    version = "1.0.0",
}
function config.get(key) return config[key] end
function config.set(key, value) config[key] = value end
return config
```

### Hệ thống quan sát/sự kiện
```lua
local EventBus = {}
EventBus.__index = EventBus

function EventBus.new()
    return setmetatable({listeners = {}}, EventBus)
end

function EventBus:on(event, callback)
    self.listeners[event] = self.listeners[event] or {}
    table.insert(self.listeners[event], callback)
end

function EventBus:emit(event, ...)
    if self.listeners[event] then
        for _, cb in ipairs(self.listeners[event]) do cb(...) end
    end
end

local bus = EventBus.new()
bus:on("player_died", function(p) print(p.name .. " died!") end)
bus:emit("player_died", {name = "Hero"})
```

### Mẫu lệnh
```lua
local Command = {}
Command.__index = Command

function Command.new(name, exec, undo)
    return setmetatable({name=name, execute=exec, undo=undo}, Command)
end

local history = {}
local cmd = Command.new("move",
    function() print("Moving") end,
    function() print("Undoing move") end)
cmd.execute()
table.insert(history, cmd)
if #history > 0 then table.remove(history).undo() end
```
---

## Hiệu suất và Tối ưu hóa
```bash
luajit -jp=v script.lua
luajit -jv script.lua
```

```lua
local sqrt = math.sqrt
local tconcat = table.concat
local parts = {}
for i = 1, 1000 do parts[#parts + 1] = tostring(i) end
local result = tconcat(parts, ',')
```

---

## Triển khai
### Triển khai Docker
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Khi nào nên sử dụng Lua
| Kịch bản | Tại sao Lua | Thay thế tốt hơn |
|----------|----------|-------------------|
| Kịch bản trò chơi | Nhẹ, nhanh, có thể nhúng | — |
| Phát triển Roblox | Lựa chọn duy nhất | — |
| Hệ thống nhúng | Dấu chân nhỏ | C, MicroPython |
| Gia hạn ứng dụng | Được thiết kế để nhúng | Python (lớn hơn), JavaScript (V8) |
| Tệp cấu hình | Đơn giản và nhanh chóng | JSON, TOML, YAML |
| Phát triển web | OpenResty tồn tại nhưng thích hợp | JavaScript, Python, Đi |
| Phát triển ứng dụng chung | Không được thiết kế cho các ứng dụng độc lập | Python, Go, Java |
| Khoa học dữ liệu | Không phải hệ sinh thái | Python, R |
---

## Bản tóm tắt
Lua là ngôn ngữ nhúng tinh túy. Nó nhỏ, nhanh và đơn giản — được thiết kế để hoạt động bên trong các ứng dụng khác và cung cấp cho chúng khả năng tạo tập lệnh. Để phát triển trò chơi, Roblox và hệ thống nhúng, Lua là một lựa chọn tuyệt vời. Nó không phải là một ngôn ngữ có mục đích chung, nhưng đối với lĩnh vực cụ thể của nó (viết kịch bản và nhúng), nó gần như không thể so sánh được.