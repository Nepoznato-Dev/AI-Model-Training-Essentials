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
#Lua
Lua ni lugha nyepesi, inayoweza kupachikwa iliyoundwa kwa kupanua programu. Lugha ya Lua iliundwa mwaka wa 1993 katika Chuo Kikuu cha Kipapa cha Kikatoliki cha Rio de Janeiro nchini Brazili. Alama yake ndogo (mkalimani ni ~120KB) na unyenyekevu huifanya chaguo-msingi kwa uandishi wa ukuzaji wa mchezo, mifumo iliyopachikwa na usanidi.
Lua inajulikana zaidi kama lugha ya uandishi nyuma ya Roblox (jukwaa la michezo la kubahatisha lenye watumiaji 200M+ kila mwezi), nyongeza za World of Warcraft, na injini nyingi za mchezo (Love2D, Defold, Corona SDK). Inatumika pia katika Nginx (OpenResty), Redis, na Wireshark.
---

## Kwa nini Lua Mambo
- **Inaweza kupachikwa**: Imeundwa ili kupachikwa katika programu zingine - seva pangishi hutoa utendakazi.
- **Alama ndogo**: Mkalimani mzima anafaa ~120KB. Inafaa kwa mifumo iliyoingia.
- **Haraka**: Mojawapo ya lugha zinazotafsiriwa haraka sana za uandishi.
- ** Rahisi **: ~ ~ 20 maneno muhimu. Rahisi kujifunza na kuunganisha.
- **Kukuza mchezo**: Lugha ya kawaida ya uandishi kwa injini na mifumo mingi ya mchezo.
- **Roblox**: Huimarisha mfumo mzima wa ikolojia wa Roblox - mamilioni ya michezo iliyoundwa na watumiaji.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Maktaba ya kawaida yenye kikomo** | Utendaji mdogo uliojengwa ndani | Panua kwa C/C++ au utumie vifurushi vya LuaRocks |
| **Uorodheshaji wa msingi 1** | Mkusanyiko huanza katika faharasa 1 (isiyo ya kawaida kwa watengeneza programu) | Kubali kama chaguo la kubuni; thabiti kote |
| **Hakuna madarasa** | Majedwali na metatable pekee - OOP lazima itekelezwe wewe mwenyewe | Tumia metatable au maktaba za OOP |
| **Niche michezo ya nje** | Matumizi machache katika wavuti, sayansi ya data, au biashara | Tumia kwa uandishi/upachikaji; lugha zingine za programu |
| **Soko dogo la ajira** | Hasa maendeleo ya mchezo na majukumu yaliyopachikwa | Ukuzaji wa Roblox ni niche inayokua |
---

## Misingi ya Sintaksia
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

## Sintaksia na Miundo ya Kina
### Metatables — Msingi wa Nguvu za Lua
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

### Kufungwa na Miundo ya Utendaji
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

### Thamani Nyingi za Kurejesha na Uharibifu
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

### Miundo ya Kamba (Mbadala wa Regex ya Lua)
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

## Concurrency & Usambamba
### Coroutines - Ushirikiano wa Multitasking
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

### Mchoro wa Kiigaji Kinachotokana na Corutine
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi
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

### LuaRocks — Usimamizi wa Kifurushi
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec - Maelezo ya Kifurushi
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

### CI/CD Bomba (Vitendo vya GitHub)
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

##Upimaji
### Iliyopigwa - Mfumo wa Kujaribu
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

### Kudhihaki kwa luassert
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

### Amri za Mtihani
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## Kuingiliana
### C API — Inapachika Lua katika C
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

### LuaJIT FFI — Simu za Moja kwa Moja za C
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

## Miundo ya Kubuni
### Muundo wa Moduli (Singleton)
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

### Mfumo wa Mtazamaji / Tukio
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

### Amri Muundo
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

## Utendaji na Uboreshaji
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

## Usambazaji
### Usambazaji wa Docker
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Wakati wa Kutumia Lua
| Hali | Kwa nini Lua | Mbadala Bora |
|----------|---------|-------------------|
| Uandishi wa mchezo | Nyepesi, haraka, inayoweza kupachikwa | - |
| Maendeleo ya Roblox | Chaguo pekee | - |
| Mifumo iliyopachikwa | Alama ndogo ya miguu | C, MicroPython |
| Ugani wa programu | Imeundwa kwa ajili ya kupachika | Chatu (kubwa), JavaScript (V8) |
| Faili za usanidi | Rahisi na ya haraka | JSON, TOML, YAML |
| Ukuzaji wa wavuti | OpenResty ipo lakini niche | JavaScript, Python, Nenda |
| Maendeleo ya maombi ya jumla | Haijaundwa kwa programu zinazojitegemea | Python, Nenda, Java |
| Sayansi ya data | Sio mfumo wa ikolojia | Chatu, R |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kwa nini Lua hutumia faharasa ya msingi-1 badala ya msingi 0?
**J:** Lua iliundwa kwa ajili ya watumiaji wasio na programu na inafuata kanuni za asili za kuhesabu. Opereta wa `#`,`ipairs`, na utendakazi wa kamba zote hutumia uorodheshaji wa msingi 1:
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

Hii ni sawa katika maktaba ya kawaida. Unapoingiliana na C (0-msingi), kumbuka kukabiliana.
### Q2: Je, ninawezaje kutekeleza mifumo inayolenga kitu katika Lua?
**J:** Lua hutumia majedwali na metatable kwa OOP. Mbinu ya`__index`huwezesha uchunguzi wa mbinu kwenye prototypes:
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

### Q3: Je, coroutines hufanya kazi vipi na ninapaswa kuzitumia lini?
**Jibu:** Coroutines ni nyuzi za ushirika ambazo zinaweza kusimamisha na kuendelea na utekelezaji. Ni bora kwa warudiaji, mifumo isiyolingana, na mantiki ya mchezo:
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

### Q4: Ni ipi njia bora ya kushughulikia makosa katika Lua?
**J:** Tumia`pcall`/`xpcall`ili kunasa makosa, na kurudisha thamani nyingi kwa mifumo ya kufaulu/kufeli:
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

### Q5: Je, ninawezaje kuboresha utendaji wa Lua kwa michezo na mifumo iliyopachikwa?
**J:** Mbinu kuu:
- Tumia`local`kwa anuwai zote - ufikiaji wa kimataifa ni polepole sana
- Akiba ya sehemu za meza zinazopatikana mara kwa mara katika wenyeji
- Tenga jedwali mapema wakati ukubwa unajulikana:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- Epuka kuunda meza za muda katika vitanzi vya moto
- Tumia`table.concat`badala ya`..`kwa kuunganisha nyuzi nyingi
- Profaili iliyo na`os.clock()`au ndoano za utatuzi
- Katika LuaJIT, tumia FFI kwa C interop badala ya C API
---

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Kuunda Kichanganuzi cha Usanidi
**Hatua ya 1: Elewa Tatizo**
Changanua faili rahisi ya usanidi wa thamani ya ufunguo ambapo kila mstari ni`key = value`.
**Hatua ya 2: Tambua Mbinu**
Soma mistari, gawanyika kwenye`=`, punguza nafasi nyeupe, na uhifadhi kwenye jedwali.
**Hatua ya 3: Tekeleza**```lua
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

**Hatua ya 4: Panua**
Ongeza usaidizi wa sehemu (`[section]`), aina ya kulazimisha (nambari, booleans), na majedwali yaliyowekwa.
### Tatizo la 2: Utekelezaji wa Mfumo Rahisi wa Tukio
**Hatua ya 1: Elewa Tatizo**
Unda mtumaji wa tukio anayeauni kujiandikisha na kutoa matukio yaliyotajwa.
**Hatua ya 2: Tambua Mbinu**
Tumia majina ya matukio ya kuorodhesha kwenye orodha ya vidhibiti.
**Hatua ya 3: Tekeleza**```lua
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

**Hatua ya 4: Thibitisha**
Jaribu na matukio mengi, uondoaji na ushughulikiaji wa hitilafu katika vidhibiti.
### Tatizo la 3: Kutengeneza Bomba Linalotokana na Corutine
**Hatua ya 1: Elewa Tatizo**
Tengeneza bomba la kuchakata data ambapo kila hatua huchuja au kubadilisha data, iliyounganishwa kupitia njia.
**Hatua ya 2: Tambua Mbinu**
Tumia coroutines kama hatua za bomba - kila hatua huchota kutoka ya awali na kusukuma hadi inayofuata.
**Hatua ya 3: Tekeleza**```lua
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

**Hatua ya 4: Boresha **
Bomba hili linalotegemea kuvuta huchakata kipengele kimoja kwa wakati kikiwa na kumbukumbu ndogo zaidi - bora kwa mitiririko mikubwa au isiyo na kikomo.
---

## Muhtasari
Lua ni lugha muhimu ya kupachika. Ni ndogo, haraka, na rahisi - iliyoundwa ili kuishi ndani ya programu zingine na kuzipa uwezo wa kuandika. Kwa ukuzaji wa mchezo, Roblox, na mifumo iliyopachikwa, Lua ni chaguo bora. Sio lugha ya kusudi la jumla, lakini kwa niche yake maalum (hati na upachikaji), karibu hailinganishwi.