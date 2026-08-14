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
# 盧阿
Lua 是一種輕量級、可嵌入的腳本語言，專為擴展應用程式而設計。 Lua 於 1993 年在巴西里約熱內盧天主教大學創建，是最快的腳本語言之一。它佔用空間小（解釋器約為 120KB）且簡單，使其成為遊戲開發腳本、嵌入式系統和配置的首選。
Lua 最為人所知的是 Roblox（每月超過 2 億用戶的遊戲平台）、魔獸世界插件和眾多遊戲引擎（Love2D、Defold、Corona SDK）背後的腳本語言。它也用於 Nginx (OpenResty)、Redis 和 Wireshark。
---

## 為什麼 Lua 很重要
- **可嵌入**：設計為嵌入其他應用程式 - 主機提供功能。
- **佔用空間小**：整個解釋器大小約 120KB。非常適合嵌入式系統。
- **快速**：最快的解釋腳本語言之一。
- **簡單**：只有約 20 個關鍵字。易於學習和整合。
- **遊戲開發**：許多遊戲引擎和平台的標準腳本語言。
- **Roblox**：為整個 Roblox 生態系統提供動力 - 數以百萬計的用戶創建的遊戲。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **標準函式庫有限** |最少的內建功能 |使用 C/C++ 擴充或使用 LuaRocks 套件 |
| **基於 1 的索引** |陣列從索引 1 開始（對於程式設計師來說不常見）|接受作為設計選擇；一致 |
| **沒有課程** |只有表格和元表－OOP必須手動實作|使用元表或 OOP 函式庫 |
| **遊戲之外的利基** |在網路、資料科學或企業中的有限使用 |用於腳本/嵌入；其他語言的應用程式 |
| **就業市場小** |主要是遊戲開發和嵌入式角色 | Roblox 開發是一個不斷增長的利基市場 |
---

## 文法基礎知識
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

## 進階語法和模式
### 元表 — Lua 強大的基礎
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

### 閉包與函數模式
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

### 多個回傳值和解構
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

### 字串模式（Lua 的正規表示式替代方案）
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

## 並發與平行
### 協程 — 協作多工處理
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

### 基於協程的迭代器模式
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

## 專案配置與建置系統
### 專案結構
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

### LuaRocks — 套件管理
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — 封裝規格
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

### CI/CD 管道 (GitHub Actions)
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

## 測試
### 失敗－測試框架
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

### 用 luassert 進行嘲笑
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

### 測試命令
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## 互通性
### C API — 在 C 中嵌入 Lua
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

### LuaJIT FFI — 直接 C 調用
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

## 設計模式
### 模組模式（單例）
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

### 觀察者/事件系統
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

### 命令模式
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

## 效能與最佳化
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

## 部署
### Docker 部署
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## 何時使用 Lua
|場景|為什麼選擇 Lua |更好的選擇|
|----------|---------|--------------------|
|遊戲腳本|輕量、快速、可嵌入 | — |
| Roblox 開發 |唯一的選擇| — |
|嵌入式系統|微小的足跡| C、MicroPython |
|應用擴充|專為嵌入設計| Python（較大）、JavaScript (V8) |
|設定檔|簡單快速| JSON、TOML、YAML |
|網頁開發| OpenResty 存在但小眾 | JavaScript、Python、Go |
|通用應用程式開發 |不是為獨立應用程式設計的 | Python、Go、Java |
|資料科學|不是生態系| Python、R |
---

## 綜合問答
### Q1：為什麼Lua使用基於1的索引而不是基於0的索引？
**答：** Lua 是為非程式設計師使用者設計的，遵循自然計數約定。`#`運算子、`ipairs`和字串函數都使用從 1 開始的索引：
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

這在整個標準庫中都是一致的。與 C（從 0 開始）介面時，請注意偏移量。
### Q2：如何在Lua中實現物件導向模式？
**答：** Lua 使用表格和元表進行 OOP。`__index`元方法支援在原型上進行方法查找：
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

### Q3：協程如何運作以及何時應該使用它們？
**A:** 協程是可以暫停和恢復執行的協作執行緒。它們非常適合迭代器、非同步模式和遊戲邏輯：
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

### Q4：Lua 中處理錯誤的最佳方式是什麼？
**A:** 使用`pcall`/`xpcall`擷取錯誤，並傳回成功/失敗模式的多個值：
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

### Q5：如何優化遊戲和嵌入式系統的 Lua 效能？
**答：** 關鍵做法：
- 對所有變數使用`local`— 全域存取速度明顯變慢
- 在本機快取經常存取的表格字段
- 大小已知時預先分配表：`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- 避免在熱循環中建立臨時表
- 使用`table.concat`而不是`..`來連接多個字串
- 使用`os.clock()`或偵錯掛鉤進行設定檔
- 在 LuaJIT 中，使用 FFI 進行 C 互通而非 C API
---

## 解決問題的思路
### 問題 1：建構設定解析器
**第 1 步：了解問題**
解析一個簡單的鍵值設定文件，其中每一行都是`key = value`。
**第 2 步：確定方法**
讀取行，在`=`上拆分，修剪空格，然後儲存在表中。
**步驟 3：實施**```lua
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

**第 4 步：擴充**
新增節支援 (`[section]`)、類型強制（數字、布林值）和巢狀表。
### 問題 2：實作一個簡單的事件系統
**第 1 步：了解問題**
建立一個支援訂閱和發出命名事件的事件發射器。
**第 2 步：確定方法**
使用將事件名稱對應到處理程序函數清單的表。
**步驟 3：實施**```lua
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

**第 4 步：驗證**
在處理程序中測試多個事件、刪除和錯誤處理。
### 問題 3：建立基於協程的管道
**第 1 步：了解問題**
建立一個數據處理管道，其中每個階段都會過濾或轉換數據，並透過協程連接。
**第 2 步：確定方法**
使用協程作為管道階段 - 每個階段從前一個階段拉出並推送到下一個階段。
**步驟 3：實施**```lua
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

**第 4 步：優化**
這種基於拉取的管道一次以最小的記憶體開銷處理一個元素 - 非常適合大型或無限流。
---

＃＃ 概括
Lua 是典型的嵌入語言。它體積小、速度快且簡單，旨在駐留在其他應用程式中並為它們提供腳本編寫功能。對於遊戲開發、Roblox 和嵌入式系統，Lua 是一個絕佳的選擇。它不是一種通用語言，但就其特定的利基（腳本和嵌入）而言，它幾乎是無與倫比的。