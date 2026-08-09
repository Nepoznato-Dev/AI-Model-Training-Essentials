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

#หลัว
Lua เป็นภาษาสคริปต์แบบฝังน้ำหนักเบาที่ออกแบบมาเพื่อการขยายแอปพลิเคชัน Lua สร้างขึ้นในปี 1993 ที่ Pontifical Catholic University of Rio de Janeiro ในบราซิล เป็นหนึ่งในภาษาสคริปต์ที่เร็วที่สุดที่มีอยู่ ด้วยขนาดที่เล็ก (ตัวแปล ~ 120KB) และความเรียบง่ายทำให้เป็นตัวเลือกที่เหมาะสมสำหรับการเขียนสคริปต์การพัฒนาเกม ระบบฝังตัว และการกำหนดค่า
Lua เป็นที่รู้จักเป็นอย่างดีในฐานะภาษาสคริปต์ที่อยู่เบื้องหลัง Roblox (แพลตฟอร์มเกมที่มีผู้ใช้มากกว่า 200 ล้านคนต่อเดือน), ส่วนเสริมของ World of Warcraft และเอ็นจิ้นเกมมากมาย (Love2D, Defold, Corona SDK) นอกจากนี้ยังใช้ใน Nginx (OpenResty), Redis และ Wireshark
---

## ทำไมลัวะถึงสำคัญ
- **ฝังได้**: ออกแบบมาเพื่อฝังในแอปพลิเคชันอื่น — โฮสต์มีฟังก์ชันการทำงาน
- **รอยเท้าขนาดเล็ก**: ล่ามทั้งหมดมีขนาดประมาณ ~120KB เหมาะสำหรับระบบฝังตัว
- **เร็ว**: หนึ่งในภาษาสคริปต์ที่ตีความได้เร็วที่สุด
- **เรียบง่าย**: คำหลักประมาณ 20 คำเท่านั้น ง่ายต่อการเรียนรู้และบูรณาการ
- **การพัฒนาเกม**: ภาษาสคริปต์มาตรฐานสำหรับเอ็นจิ้นเกมและแพลตฟอร์มต่างๆ
- **Roblox**: ขับเคลื่อนระบบนิเวศ Roblox ทั้งหมด — เกมที่ผู้ใช้สร้างขึ้นนับล้านเกม
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ไลบรารี่มาตรฐานมีจำนวนจำกัด** | ฟังก์ชั่นในตัวน้อยที่สุด | ขยายด้วย C/C++ หรือใช้แพ็คเกจ LuaRocks |
| **การจัดทำดัชนีตาม 1** | อาร์เรย์เริ่มต้นที่ดัชนี 1 (ผิดปกติสำหรับโปรแกรมเมอร์) | ยอมรับเป็นตัวเลือกการออกแบบ สม่ำเสมอตลอด |
| **ไม่มีเรียน** | เฉพาะตารางและเมตาเทเบิลเท่านั้น — OOP ต้องดำเนินการด้วยตนเอง | ใช้ metatables หรือไลบรารี OOP |
| **เฉพาะกลุ่มเกมนอก** | การใช้งานที่จำกัดในเว็บ วิทยาศาสตร์ข้อมูล หรือองค์กร | ใช้สำหรับการเขียนสคริปต์/การฝัง ภาษาอื่น ๆ สำหรับแอปพลิเคชัน |
| **ตลาดงานเล็กๆ** | ส่วนใหญ่เป็นการพัฒนาเกมและบทบาทที่ฝังตัว | การพัฒนา Roblox เป็นช่องทางที่กำลังเติบโต |
---

## พื้นฐานไวยากรณ์
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

## ไวยากรณ์และรูปแบบขั้นสูง
### Metatables — รากฐานแห่งพลังของ Lua
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

### การปิดและรูปแบบการทำงาน
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

### ค่าส่งคืนหลายค่าและการทำลายโครงสร้าง
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

### รูปแบบสตริง (ทางเลือก Regex ของ Lua)
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### Coroutines — มัลติทาสกิ้งแบบร่วมมือ
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

### รูปแบบตัววนซ้ำที่ใช้ Coroutine
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ
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

### LuaRocks — การจัดการแพ็คเกจ
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — ข้อมูลจำเพาะของแพ็คเกจ
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

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### ถูกจับ — กรอบการทดสอบ
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

### ล้อเลียนกับ luassert
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

### คำสั่งทดสอบ
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## การทำงานร่วมกัน
### C API — การฝัง Lua ใน C
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

### LuaJIT FFI - โทร C โดยตรง
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

## รูปแบบการออกแบบ
### รูปแบบโมดูล (ซิงเกิลตัน)
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

### ผู้สังเกตการณ์ / ระบบเหตุการณ์
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

### รูปแบบคำสั่ง
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### การปรับใช้นักเทียบท่า
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## เมื่อใดควรใช้ Lua
| สถานการณ์ | ทำไมต้องหลัว | ทางเลือกที่ดีกว่า |
|----------|---------|-------------------|
| การเขียนสคริปต์เกม | น้ำหนักเบา รวดเร็ว ฝังได้ | — |
| การพัฒนา Roblox | ตัวเลือกเดียว | — |
| ระบบสมองกลฝังตัว | รอยเท้าเล็กๆ | C, MicroPython |
| ส่วนขยายแอปพลิเคชัน | ออกแบบมาเพื่อการฝัง | Python (ใหญ่กว่า), JavaScript (V8) |
| ไฟล์การกำหนดค่า | ง่ายและรวดเร็ว | JSON, TOML, YAML |
| การพัฒนาเว็บ | OpenResty มีอยู่แต่เฉพาะ | จาวาสคริปต์, ไพธอน, ไป |
| การพัฒนาแอพพลิเคชั่นทั่วไป | ไม่ได้ออกแบบมาสำหรับแอปแบบสแตนด์อโลน | Python, Go, Java |
| วิทยาศาสตร์ข้อมูล | ไม่ใช่ระบบนิเวศ | หลาม, อาร์ |
---

## สรุป
Lua เป็นภาษาฝังที่เป็นแก่นสาร มีขนาดเล็ก รวดเร็วและเรียบง่าย — ออกแบบมาเพื่อใช้งานภายในแอปพลิเคชันอื่นๆ และมอบความสามารถในการเขียนสคริปต์ สำหรับการพัฒนาเกม Roblox และระบบฝังตัว Lua เป็นตัวเลือกที่ยอดเยี่ยม ภาษานี้ไม่ใช่ภาษาที่มีวัตถุประสงค์ทั่วไป แต่สำหรับกลุ่มเฉพาะ (การเขียนสคริปต์และการฝัง) ภาษานี้แทบจะไม่มีใครเทียบได้