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

#লুয়া
Lua হল একটি হালকা ওজনের, এম্বেডযোগ্য স্ক্রিপ্টিং ভাষা যা অ্যাপ্লিকেশন প্রসারিত করার জন্য ডিজাইন করা হয়েছে। ব্রাজিলের রিও ডি জেনিরোর পন্টিফিকাল ক্যাথলিক বিশ্ববিদ্যালয়ে 1993 সালে তৈরি, লুয়া হল দ্রুততম স্ক্রিপ্টিং ভাষাগুলির মধ্যে একটি। এর ছোট পদচিহ্ন (দোভাষী হল ~120KB) এবং সরলতা এটিকে গেম ডেভেলপমেন্ট স্ক্রিপ্টিং, এমবেডেড সিস্টেম এবং কনফিগারেশনের জন্য পছন্দের পছন্দ করে তোলে।
লুয়া রবলক্স (200M+ মাসিক ব্যবহারকারীদের সাথে গেমিং প্ল্যাটফর্ম), ওয়ার্ল্ড অফ ওয়ারক্রাফ্ট অ্যাডঅন এবং অসংখ্য গেম ইঞ্জিন (লাভ2ডি, ডিফোল্ড, করোনা SDK) এর পিছনে স্ক্রিপ্টিং ভাষা হিসাবে পরিচিত। এটি Nginx (OpenResty), Redis এবং Wireshark-এও ব্যবহৃত হয়।
---

## কেন লুয়া ব্যাপার
- **এম্বেডযোগ্য**: অন্যান্য অ্যাপ্লিকেশনে এম্বেড করার জন্য ডিজাইন করা হয়েছে — হোস্ট কার্যকারিতা প্রদান করে।
- **ক্ষুদ্র পদচিহ্ন**: সম্পূর্ণ দোভাষী ~120KB-এ ফিট করে। এমবেডেড সিস্টেমের জন্য আদর্শ।
- **দ্রুত**: দ্রুততম ব্যাখ্যা করা স্ক্রিপ্টিং ভাষাগুলির মধ্যে একটি।
- **সহজ**: শুধুমাত্র ~20 কীওয়ার্ড। শিখতে এবং সংহত করা সহজ।
- **গেম ডেভেলপমেন্ট**: অনেক গেম ইঞ্জিন এবং প্ল্যাটফর্মের জন্য আদর্শ স্ক্রিপ্টিং ভাষা।
- **Roblox**: সমগ্র Roblox ইকোসিস্টেমকে শক্তিশালী করে — লক্ষ লক্ষ ব্যবহারকারীর তৈরি গেম।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **সীমিত স্ট্যান্ডার্ড লাইব্রেরি** | ন্যূনতম অন্তর্নির্মিত কার্যকারিতা | C/C++ দিয়ে প্রসারিত করুন অথবা LuaRocks প্যাকেজ ব্যবহার করুন |
| **1-ভিত্তিক ইন্ডেক্সিং** | অ্যারেগুলি সূচী 1 থেকে শুরু হয় (প্রোগ্রামারদের জন্য অস্বাভাবিক) | একটি নকশা পছন্দ হিসাবে গ্রহণ; সামঞ্জস্যপূর্ণ |
| **কোন ক্লাস নেই** | শুধুমাত্র টেবিল এবং মেটাটেবল — OOP অবশ্যই ম্যানুয়ালি প্রয়োগ করতে হবে | মেটাটেবল বা OOP লাইব্রেরি ব্যবহার করুন |
| **কুলুঙ্গি বাইরের গেম** | ওয়েব, ডেটা সায়েন্স বা এন্টারপ্রাইজে সীমিত ব্যবহার | স্ক্রিপ্টিং/এম্বেডিংয়ের জন্য ব্যবহার করুন; অ্যাপ্লিকেশনের জন্য অন্যান্য ভাষা |
| **ছোট কাজের বাজার** | বেশিরভাগই গেম ডেভেলপমেন্ট এবং এমবেডেড ভূমিকা | Roblox উন্নয়ন একটি ক্রমবর্ধমান কুলুঙ্গি |
---

## সিনট্যাক্স মৌলিক
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### মেটাটেবলস — লুয়ার শক্তির ভিত্তি
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

### বন্ধ এবং কার্যকরী নিদর্শন
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

### একাধিক রিটার্ন মান এবং ধ্বংস
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

### স্ট্রিং প্যাটার্নস (লুয়ার রেজেক্স বিকল্প)
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

## সামঞ্জস্য এবং সমান্তরালতা
### Coroutines — সমবায় মাল্টিটাস্কিং
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

### করোটিন-ভিত্তিক ইটারেটর প্যাটার্ন
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
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

### LuaRocks — প্যাকেজ ব্যবস্থাপনা
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### রকস্পেক — প্যাকেজ স্পেসিফিকেশন
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

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### ভাঙ্গা — টেস্টিং ফ্রেমওয়ার্ক
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

### লুয়াসার্ট দিয়ে উপহাস করা
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

### টেস্ট কমান্ড
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## ইন্টারঅপারেবিলিটি
### C API — সি-তে লুয়া এম্বেড করা
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

### LuaJIT FFI — সরাসরি সি কল
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

## ডিজাইন প্যাটার্ন
### মডিউল প্যাটার্ন (সিঙ্গলটন)
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

### পর্যবেক্ষক/ইভেন্ট সিস্টেম
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

### কমান্ড প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
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

## স্থাপনা
### ডকার স্থাপনা
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## কখন লুয়া ব্যবহার করবেন
| দৃশ্যকল্প | কেন লুয়া | ভাল বিকল্প |
|------------|---------|---------|
| খেলার স্ক্রিপ্টিং | লাইটওয়েট, দ্রুত, এম্বেডযোগ্য | — |
| রোবলক্স ডেভেলপমেন্ট | একমাত্র বিকল্প | — |
| এমবেডেড সিস্টেম | ক্ষুদ্র পায়ের ছাপ | সি, মাইক্রোপাইথন |
| অ্যাপ্লিকেশন এক্সটেনশন | এমবেডিংয়ের জন্য ডিজাইন করা হয়েছে | পাইথন (বৃহত্তর), জাভাস্ক্রিপ্ট (V8) |
| কনফিগারেশন ফাইল | সহজ এবং দ্রুত | JSON, TOML, YAML |
| ওয়েব ডেভেলপমেন্ট | OpenResty বিদ্যমান কিন্তু কুলুঙ্গি | JavaScript, Python, Go |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | স্বতন্ত্র অ্যাপের জন্য ডিজাইন করা হয়নি | পাইথন, গো, জাভা |
| তথ্য বিজ্ঞান | বাস্তুতন্ত্র নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: কেন Lua 0-ভিত্তিক এর পরিবর্তে 1-ভিত্তিক ইন্ডেক্সিং ব্যবহার করে?
**A:** Lua নন-প্রোগ্রামার ব্যবহারকারীদের জন্য ডিজাইন করা হয়েছে এবং স্বাভাবিক গণনা নিয়ম অনুসরণ করে।`#`অপারেটর,`ipairs`এবং স্ট্রিং ফাংশনগুলি সমস্ত 1-ভিত্তিক ইন্ডেক্সিং ব্যবহার করে:
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

এটি স্ট্যান্ডার্ড লাইব্রেরি জুড়ে সামঞ্জস্যপূর্ণ। C (0-ভিত্তিক) এর সাথে ইন্টারফেস করার সময়, অফসেট সম্পর্কে সচেতন হন।
### প্রশ্ন 2: আমি কীভাবে লুয়াতে অবজেক্ট-ওরিয়েন্টেড প্যাটার্ন প্রয়োগ করব?
**A:** Lua OOP এর জন্য টেবিল এবং মেটাটেবল ব্যবহার করে।`__index`মেটামেথড প্রোটোটাইপগুলিতে পদ্ধতির সন্ধান সক্ষম করে:
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

### প্রশ্ন 3: কোরোটিনগুলি কীভাবে কাজ করে এবং আমার কখন সেগুলি ব্যবহার করা উচিত?
**A:** Coroutines হল সমবায় থ্রেড যা স্থগিত এবং পুনরায় শুরু করতে পারে। এগুলি পুনরাবৃত্তিকারী, অ্যাসিঙ্ক প্যাটার্ন এবং গেম লজিকের জন্য আদর্শ:
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

### প্রশ্ন 4: লুয়াতে ত্রুটিগুলি পরিচালনা করার সর্বোত্তম উপায় কী?
**A:** ত্রুটি ধরতে`pcall`/`xpcall`ব্যবহার করুন এবং সাফল্য/ব্যর্থতার নিদর্শনগুলির জন্য একাধিক মান ফেরত দিন:
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

### প্রশ্ন 5: আমি কীভাবে গেম এবং এমবেডেড সিস্টেমের জন্য লুয়া পারফরম্যান্সকে অপ্টিমাইজ করব?
**A:** মূল অনুশীলন:
- সমস্ত ভেরিয়েবলের জন্য`local`ব্যবহার করুন — বিশ্বব্যাপী অ্যাক্সেস উল্লেখযোগ্যভাবে ধীর
- স্থানীয়দের মধ্যে ক্যাশে ঘন ঘন টেবিল ক্ষেত্র অ্যাক্সেস করা হয়
- আকার পরিচিত হলে পূর্ব-বরাদ্দ টেবিল:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- গরম লুপগুলিতে অস্থায়ী টেবিল তৈরি করা এড়িয়ে চলুন
- অনেক স্ট্রিং যোগ করার জন্য`..`এর পরিবর্তে`table.concat`ব্যবহার করুন
-`os.clock()`বা ডিবাগ হুক সহ প্রোফাইল৷
- LuaJIT-এ C API-এর পরিবর্তে C ইন্টারপ-এর জন্য FFI ব্যবহার করুন
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি কনফিগারেশন পার্সার তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি সাধারণ কী-মান কনফিগারেশন ফাইল পার্স করুন যেখানে প্রতিটি লাইন হল `key = value`।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
লাইন পড়ুন,`=`এ বিভক্ত করুন, হোয়াইটস্পেস ট্রিম করুন এবং একটি টেবিলে সংরক্ষণ করুন।
**ধাপ 3: প্রয়োগ করুন**```lua
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

**ধাপ 4: প্রসারিত করুন**
বিভাগ সমর্থন যোগ করুন (`[section]`), টাইপ জবরদস্তি (সংখ্যা, বুলিয়ান), এবং নেস্টেড টেবিল।
### সমস্যা 2: একটি সাধারণ ইভেন্ট সিস্টেম বাস্তবায়ন করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি ইভেন্ট ইমিটার তৈরি করুন যা সাবস্ক্রাইব করা এবং নামযুক্ত ইভেন্টগুলি নির্গত করা সমর্থন করে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
হ্যান্ডলার ফাংশনগুলির তালিকায় একটি টেবিল ম্যাপিং ইভেন্টের নাম ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```lua
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

**পদক্ষেপ 4: যাচাই করুন**
হ্যান্ডলারে একাধিক ইভেন্ট, অপসারণ এবং ত্রুটি পরিচালনার সাথে পরীক্ষা করুন।
### সমস্যা 3: একটি করোটিন-ভিত্তিক পাইপলাইন তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি ডেটা প্রসেসিং পাইপলাইন তৈরি করুন যেখানে প্রতিটি স্টেজ ডেটা ফিল্টার বা রূপান্তর করে, কোরোটিনের মাধ্যমে সংযুক্ত।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
পাইপলাইন পর্যায় হিসাবে coroutines ব্যবহার করুন — প্রতিটি পর্যায় আগের থেকে টেনে পরের দিকে ঠেলে দেয়।
**ধাপ 3: প্রয়োগ করুন**```lua
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

**ধাপ ৪: অপ্টিমাইজ**
এই পুল-ভিত্তিক পাইপলাইনটি ন্যূনতম মেমরি ওভারহেড সহ এক সময়ে একটি উপাদান প্রক্রিয়া করে — বড় বা অসীম স্ট্রিমগুলির জন্য আদর্শ।
---

## সারাংশ
লুয়া হল সর্বোত্তম এম্বেডিং ভাষা। এটি ছোট, দ্রুত এবং সহজ — অন্যান্য অ্যাপ্লিকেশনের ভিতরে থাকার জন্য এবং তাদের স্ক্রিপ্টিং ক্ষমতা প্রদান করার জন্য ডিজাইন করা হয়েছে। গেম ডেভেলপমেন্ট, রোবলক্স এবং এমবেডেড সিস্টেমের জন্য, লুয়া একটি চমৎকার পছন্দ। এটি একটি সাধারণ-উদ্দেশ্যের ভাষা নয়, তবে এর নির্দিষ্ট কুলুঙ্গির জন্য (স্ক্রিপ্টিং এবং এম্বেডিং), এটি প্রায় অতুলনীয়।