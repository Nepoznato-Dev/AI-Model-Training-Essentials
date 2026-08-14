<!--
---
# Metadata
title: "Lua"
description: "Comprehensive reference for the Lua programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
#لوا
Lua یک زبان برنامه نویسی سبک و قابل جاسازی است که برای توسعه برنامه ها طراحی شده است. Lua که در سال 1993 در دانشگاه کاتولیک پاپی ریودوژانیرو در برزیل ایجاد شد، یکی از سریع ترین زبان های برنامه نویسی موجود است. ردپای کوچک آن (مفسر ~ 120 کیلوبایت است) و سادگی آن را به گزینه ای برای برنامه نویسی توسعه بازی، سیستم های تعبیه شده و پیکربندی تبدیل کرده است.
Lua بیشتر به عنوان زبان برنامه نویسی پشت Roblox (پلتفرم بازی با بیش از 200 میلیون کاربر ماهانه)، افزونه های World of Warcraft و موتورهای بازی متعدد (Love2D، Defold، Corona SDK) شناخته می شود. همچنین در Nginx (OpenResty)، Redis و Wireshark استفاده می شود.
---

## چرا لوا مهم است
- **Embeddable**: طراحی شده برای جاسازی در سایر برنامه ها - میزبان عملکرد را ارائه می دهد.
- ** جای پای کوچک **: کل مترجم در ~ 120 کیلوبایت قرار می گیرد. ایده آل برای سیستم های تعبیه شده
- **سریع**: یکی از سریع ترین زبان های اسکریپت نویسی تفسیر شده.
- **ساده**: فقط 20 کلمه کلیدی. آسان برای یادگیری و ادغام.
- **توسعه بازی**: زبان برنامه نویسی استاندارد برای بسیاری از موتورها و پلتفرم های بازی.
- **Roblox**: کل اکوسیستم Roblox را تقویت می کند - میلیون ها بازی ساخته شده توسط کاربر.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **کتابخانه استاندارد محدود** | حداقل عملکرد داخلی | با C/C++ گسترش دهید یا از بسته های LuaRocks |
| ** نمایه سازی مبتنی بر 1 ** | آرایه ها با شاخص 1 شروع می شوند (برای برنامه نویسان غیر معمول) | به عنوان یک انتخاب طراحی بپذیرید؛ سازگار در سراسر |
| **بدون کلاس** | فقط جداول و جدول های متا - OOP باید به صورت دستی پیاده سازی شود | از متاتبل ها یا کتابخانه های OOP |
| **بازی های بیرون طاقچه ** | استفاده محدود در وب، علم داده یا سازمانی | استفاده برای اسکریپت / تعبیه. زبان های دیگر برای برنامه های کاربردی |
| **بازار کار کوچک** | بیشتر بازی سازی و نقش های تعبیه شده | توسعه Roblox در حال رشد است |
---

## اصول نحو
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

## نحو و الگوهای پیشرفته
### Metatables - بنیاد قدرت Lua
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

### بسته ها و الگوهای عملکردی
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

### چندین ارزش بازگشتی و تخریب
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

### الگوهای رشته (جایگزین Regex Lua)
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

## همزمانی و موازی
### کوروتین ها - چندوظیفه ای مشارکتی
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

### الگوی تکرارکننده مبتنی بر کوروتین
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### LuaRocks - مدیریت بسته
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec - مشخصات بسته
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### خراب شده - چارچوب تست
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

### تمسخر با لواسرت
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

### دستورات تست
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## قابلیت همکاری
### C API - جاسازی Lua در C
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

### LuaJIT FFI - تماس مستقیم C
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

## الگوهای طراحی
### الگوی ماژول (Singleton)
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

### ناظر / سیستم رویداد
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

### الگوی فرمان
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

## عملکرد و بهینه سازی
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

## استقرار
### استقرار داکر
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## چه زمانی از Lua استفاده کنیم
| سناریو | چرا لوا | جایگزین بهتر |
|----------|---------|-------------------|
| برنامه نویسی بازی | سبک، سریع، قابل جاسازی | — |
| توسعه Roblox | تنها گزینه | — |
| سیستم های تعبیه شده | رد پای کوچک | سی، میکروپایتون |
| پسوند برنامه | طراحی شده برای تعبیه | پایتون (بزرگتر)، جاوا اسکریپت (V8) |
| فایل های پیکربندی | ساده و سریع | JSON، TOML، YAML |
| توسعه وب | OpenResty وجود دارد اما جایگاه | جاوا اسکریپت، پایتون، برو |
| توسعه برنامه عمومی | برای برنامه های مستقل طراحی نشده است | پایتون، برو، جاوا |
| علم داده | نه اکوسیستم | پایتون، R |
---

## پرسش و پاسخ مصنوعی
### Q1: چرا Lua از نمایه سازی مبتنی بر 1 به جای 0 مبتنی بر استفاده می کند؟
**A:** Lua برای کاربران غیر برنامه نویس طراحی شده است و از قراردادهای شمارش طبیعی پیروی می کند. عملگر `#`،`ipairs`و توابع رشته ای همگی از نمایه سازی مبتنی بر 1 استفاده می کنند:
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

این در سراسر کتابخانه استاندارد سازگار است. هنگام ارتباط با C (بر اساس 0)، مراقب افست باشید.
### Q2: چگونه الگوهای شی گرا را در Lua پیاده سازی کنم؟
**A:** Lua از جداول و متاتبل برای OOP استفاده می کند. متاموتد`__index`جستجوی روش را در نمونه های اولیه فعال می کند:
```lua
-- Class-like pattern
local Animal = {}
Animal.__index = Animal

function Animal.new(name, sound)
  return setmetatable({name = name, sound = sound}, Animal)
end

function Animal:speak()
  print(self.name .. " says " .. self.sound)
end

-- Inheritance
local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
  return Animal.new(name, "Woof!")
end

function Dog:fetch()
  print(self.name .. " fetches the ball!")
end

local rex = Dog.new("Rex")
rex:speak()   -- "Rex says Woof!"
rex:fetch()   -- "Rex fetches the ball!"
```

### Q3: کوروتین ها چگونه کار می کنند و چه زمانی باید از آنها استفاده کنم؟
**A:** Coroutineها رشته های همکاری هستند که می توانند اجرا را به حالت تعلیق درآورند و از سر بگیرند. آنها برای تکرار کننده ها، الگوهای غیر همگام و منطق بازی ایده آل هستند:
```lua
-- Producer coroutine
function produce()
  for i = 1, 5 do
    coroutine.yield(i)  -- suspend, returning value
  end
end

local co = coroutine.create(produce)
print(coroutine.resume(co))  -- true, 1
print(coroutine.resume(co))  -- true, 2
print(coroutine.resume(co))  -- true, 3

-- Iterator pattern
function range(from, to)
  return coroutine.wrap(function()
    for i = from, to do
      coroutine.yield(i)
    end
  end)
end

for n in range(1, 5) do
  print(n)  -- 1, 2, 3, 4, 5
end
```

### Q4: بهترین راه برای رسیدگی به خطاها در Lua چیست؟
**A:** از`pcall`/`xpcall`برای تشخیص خطاها استفاده کنید و چندین مقدار را برای الگوهای موفقیت/شکست برگردانید:
```lua
-- pcall — protected call
local ok, result = pcall(function()
  return risky_operation()
end)
if not ok then
  print("Error: " .. result)  -- result is the error message
end

-- xpcall — with custom error handler
local ok, result = xpcall(
  function() return process() end,
  function(err) return debug.traceback(err) end
)

-- Idiomatic: return nil + message on failure
function read_config(path)
  local f = io.open(path, "r")
  if not f then return nil, "Cannot open: " .. path end
  local content = f:read("*a")
  f:close()
  return content
end

local config, err = read_config("app.conf")
if not config then error(err) end
```

### Q5: چگونه می توانم عملکرد Lua را برای بازی ها و سیستم های تعبیه شده بهینه کنم؟
**A:** شیوه های کلیدی:
- از`local`برای همه متغیرها استفاده کنید - دسترسی جهانی به طور قابل توجهی کندتر است
- فیلدهای جدولی که اغلب در افراد محلی به آن ها دسترسی پیدا می کند، کش
- زمانی که اندازه مشخص است جداول را از قبل تخصیص دهید:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- از ایجاد جداول موقت در هات لوپ خودداری کنید
- از`table.concat`به جای`..`برای اتصال بسیاری از رشته ها استفاده کنید
- نمایه با قلاب های`os.clock()`یا اشکال زدایی
- در LuaJIT از FFI برای C interop به جای C API استفاده کنید
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: ساختن یک تجزیه کننده پیکربندی
**مرحله 1: مشکل را درک کنید**
یک فایل پیکربندی کلید-مقدار ساده را که در آن هر خط`key = value`است، تجزیه کنید.
**مرحله 2: رویکرد را شناسایی کنید**
خطوط را بخوانید، روی`=`تقسیم کنید، فضای خالی را کوتاه کنید و در جدول ذخیره کنید.
**مرحله 3: پیاده سازی **```lua
function parse_config(filename)
  local config = {}
  local f = assert(io.open(filename, "r"))
  for line in f:lines() do
    -- Skip comments and empty lines
    line = line:match("^%s*(.-)%s*$")  -- trim
    if line ~= "" and not line:match("^#") then
      local key, value = line:match("^([^=]+)=(.*)$")
      if key and value then
        -- Trim key and value
        key = key:match("^%s*(.-)%s*$")
        value = value:match("^%s*(.-)%s*$")
        config[key] = value
      end
    end
  end
  f:close()
  return config
end

-- Usage: config = parse_config("app.conf")
-- config["host"] => "localhost"
```

**مرحله 4: تمدید**
پشتیبانی بخش (`[section]`)، نوع اجبار (اعداد، بولیان)، و جداول تودرتو را اضافه کنید.
### مسئله 2: پیاده سازی یک سیستم رویداد ساده
**مرحله 1: مشکل را درک کنید**
ارسال کننده رویدادی ایجاد کنید که از اشتراک و انتشار رویدادهای نامگذاری شده پشتیبانی کند.
**مرحله 2: رویکرد را شناسایی کنید**
از نام رویدادهای نگاشت جدول برای لیست توابع کنترل کننده استفاده کنید.
**مرحله 3: پیاده سازی **```lua
local EventBus = {}
EventBus.__index = EventBus

function EventBus.new()
  return setmetatable({listeners = {}}, EventBus)
end

function EventBus:on(event, handler)
  if not self.listeners[event] then
    self.listeners[event] = {}
  end
  table.insert(self.listeners[event], handler)
  return self  -- chainable
end

function EventBus:emit(event, ...)
  local handlers = self.listeners[event] or {}
  for _, handler in ipairs(handlers) do
    handler(...)
  end
end

function EventBus:off(event, handler)
  local handlers = self.listeners[event] or {}
  for i, h in ipairs(handlers) do
    if h == handler then
      table.remove(handlers, i)
      break
    end
  end
end

-- Usage
local bus = EventBus.new()
bus:on("data", function(msg) print("Got: " .. msg) end)
bus:on("data", function(msg) print("Also: " .. msg) end)
bus:emit("data", "hello")  -- Got: hello / Also: hello
```

**مرحله 4: تایید **
تست با چندین رویداد، حذف و مدیریت خطا در کنترلرها.
### مسئله 3: ایجاد یک خط لوله مبتنی بر کوروتین
**مرحله 1: مشکل را درک کنید**
یک خط لوله پردازش داده بسازید که در آن هر مرحله داده ها را فیلتر یا تبدیل می کند و از طریق کوروتین ها به هم متصل می شوند.
**مرحله 2: رویکرد را شناسایی کنید**
از کوروتین ها به عنوان مراحل خط لوله استفاده کنید - هر مرحله از مرحله قبلی کشیده می شود و به مرحله بعدی می رود.
**مرحله 3: پیاده سازی **```lua
-- Source: generates values
function source(t)
  return coroutine.wrap(function()
    for _, v in ipairs(t) do
      coroutine.yield(v)
    end
  end)
end

-- Filter: passes through values matching predicate
function filter(pred, input)
  return coroutine.wrap(function()
    for v in input do
      if pred(v) then coroutine.yield(v) end
    end
  end)
end

-- Map: transforms values
function map(fn, input)
  return coroutine.wrap(function()
    for v in input do
      coroutine.yield(fn(v))
    end
  end)
end

-- Compose pipeline
local data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
local pipeline = map(
  function(x) return x * x end,
  filter(
    function(x) return x % 2 == 0 end,
    source(data)
  )
)

for v in pipeline do
  print(v)  -- 4, 16, 36, 64, 100
end
```

**مرحله 4: بهینه سازی**
این خط لوله مبتنی بر کشش یک عنصر را در یک زمان با حداقل سربار حافظه پردازش می کند - ایده آل برای جریان های بزرگ یا بی نهایت.
---

## خلاصه
Lua زبان اصلی جاسازی است. این برنامه کوچک، سریع و ساده است — طوری طراحی شده است که در داخل سایر برنامه ها زندگی کند و قابلیت های برنامه نویسی را برای آنها فراهم کند. برای توسعه بازی، Roblox و سیستم های جاسازی شده، Lua یک انتخاب عالی است. این یک زبان همه منظوره نیست، اما به دلیل جایگاه خاص خود (اسکریپت نویسی و جاسازی)، تقریباً بی همتا است.