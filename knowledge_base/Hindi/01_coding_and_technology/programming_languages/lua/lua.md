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
# लुआ
लुआ एक हल्की, एम्बेड करने योग्य स्क्रिप्टिंग भाषा है जिसे अनुप्रयोगों के विस्तार के लिए डिज़ाइन किया गया है। 1993 में ब्राज़ील में रियो डी जनेरियो के पोंटिफ़िकल कैथोलिक विश्वविद्यालय में बनाई गई, लुआ सबसे तेज़ स्क्रिप्टिंग भाषाओं में से एक है। इसका छोटा पदचिह्न (दुभाषिया ~120KB है) और सरलता इसे गेम डेवलपमेंट स्क्रिप्टिंग, एम्बेडेड सिस्टम और कॉन्फ़िगरेशन के लिए पसंदीदा विकल्प बनाती है।
लुआ को रोब्लॉक्स (200 मिलियन से अधिक मासिक उपयोगकर्ताओं वाला गेमिंग प्लेटफ़ॉर्म), वर्ल्ड ऑफ वॉरक्राफ्ट ऐडऑन और कई गेम इंजन (लव2डी, डिफोल्ड, कोरोना एसडीके) के पीछे की स्क्रिप्टिंग भाषा के रूप में जाना जाता है। इसका उपयोग Nginx (OpenResty), रेडिस और वायरशार्क में भी किया जाता है।
---

## लुआ क्यों मायने रखता है
- **एम्बेड करने योग्य**: अन्य अनुप्रयोगों में एम्बेड करने के लिए डिज़ाइन किया गया - होस्ट कार्यक्षमता प्रदान करता है।
- **छोटे पदचिह्न**: संपूर्ण दुभाषिया ~120KB में फिट बैठता है। एंबेडेड सिस्टम के लिए आदर्श.
- **तेज**: सबसे तेजी से व्याख्या की जाने वाली स्क्रिप्टिंग भाषाओं में से एक।
- **सरल**: केवल ~20 कीवर्ड। सीखना और एकीकृत करना आसान है।
- **गेम डेवलपमेंट**: कई गेम इंजनों और प्लेटफार्मों के लिए मानक स्क्रिप्टिंग भाषा।
- **Roblox**: संपूर्ण Roblox पारिस्थितिकी तंत्र को शक्ति प्रदान करता है - लाखों उपयोगकर्ता-निर्मित गेम।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सीमित मानक पुस्तकालय** | न्यूनतम अंतर्निहित कार्यक्षमता | C/C++ के साथ विस्तार करें या LuaRocks पैकेज का उपयोग करें |
| **1-आधारित अनुक्रमण** | सारणियाँ सूचकांक 1 से शुरू होती हैं (प्रोग्रामर के लिए असामान्य) | डिज़ाइन विकल्प के रूप में स्वीकार करें; भर में सुसंगत |
| **कोई कक्षा नहीं** | केवल टेबल और मेटाटेबल्स - OOP को मैन्युअल रूप से लागू किया जाना चाहिए | मेटाटेबल्स या ओओपी लाइब्रेरीज़ का उपयोग करें |
| **आला बाहरी खेल** | वेब, डेटा विज्ञान, या उद्यम में सीमित उपयोग | स्क्रिप्टिंग/एम्बेडिंग के लिए उपयोग करें; अनुप्रयोगों के लिए अन्य भाषाएँ |
| **लघु नौकरी बाज़ार** | अधिकतर खेल विकास और एम्बेडेड भूमिकाएँ | रोबॉक्स विकास एक बढ़ती हुई जगह है |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### मेटाटेबल्स - लुआ की शक्ति का आधार
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

### क्लोजर और कार्यात्मक पैटर्न
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

### एकाधिक रिटर्न मान और डिस्ट्रक्चरिंग
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

### स्ट्रिंग पैटर्न (लुआ का रेगेक्स वैकल्पिक)
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

## समवर्ती एवं समांतरता
### कोरआउटिंस - सहकारी मल्टीटास्किंग
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

### कोरटाइन-आधारित इटरेटर पैटर्न
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### लुआरॉक्स - पैकेज प्रबंधन
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### रॉकस्पेक - पैकेज विशिष्टता
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### भंडाफोड़ - परीक्षण ढांचा
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

### लुअस्सर्ट के साथ मजाक करना
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

### टेस्ट कमांड
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## अंतरसंचालनीयता
### सी एपीआई - सी में लुआ को एम्बेड करना
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

### लुआजित एफएफआई - डायरेक्ट सी कॉल्स
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

## डिज़ाइन पैटर्न
### मॉड्यूल पैटर्न (सिंगलटन)
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

### प्रेक्षक/घटना प्रणाली
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

### कमांड पैटर्न
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

## प्रदर्शन और अनुकूलन
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

## तैनाती
### डॉकर परिनियोजन
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## लुआ का उपयोग कब करें
| परिदृश्य | क्यों लुआ | बेहतर विकल्प |
|---|---|-----|
| गेम स्क्रिप्टिंग | हल्का, तेज़, एम्बेड करने योग्य | — |
| रोबोक्स विकास | एकमात्र विकल्प | — |
| एंबेडेड सिस्टम | छोटे पदचिह्न | सी, माइक्रोपायथन |
| एप्लीकेशन एक्सटेंशन | एम्बेडिंग के लिए डिज़ाइन किया गया | पायथन (बड़ा), जावास्क्रिप्ट (V8) |
| कॉन्फ़िगरेशन फ़ाइलें | सरल और तेज़ | JSON, TOML, YAML |
| वेब विकास | OpenResty मौजूद है लेकिन आला | जावास्क्रिप्ट, पायथन, गो |
| सामान्य अनुप्रयोग विकास | स्टैंडअलोन ऐप्स के लिए डिज़ाइन नहीं किया गया | पायथन, गो, जावा |
| डेटा विज्ञान | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: लुआ 0-आधारित के बजाय 1-आधारित अनुक्रमणिका का उपयोग क्यों करता है?
**ए:** लुआ को गैर-प्रोग्रामर उपयोगकर्ताओं के लिए डिज़ाइन किया गया था और यह प्राकृतिक गिनती परंपराओं का पालन करता है।`#`ऑपरेटर,`ipairs`और स्ट्रिंग फ़ंक्शन सभी 1-आधारित अनुक्रमण का उपयोग करते हैं:
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

यह पूरे मानक पुस्तकालय में सुसंगत है। C (0-आधारित) के साथ इंटरफ़ेस करते समय, ऑफसेट का ध्यान रखें।
### Q2: मैं लुआ में ऑब्जेक्ट-ओरिएंटेड पैटर्न कैसे लागू करूं?
**ए:** लुआ ओओपी के लिए तालिकाओं और मेटाटेबल्स का उपयोग करता है।`__index`मेटामेथोड प्रोटोटाइप पर विधि लुकअप को सक्षम बनाता है:
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

### Q3: कोरआउट्स कैसे काम करते हैं और मुझे उनका उपयोग कब करना चाहिए?
**ए:** कॉरआउट्स सहकारी धागे हैं जो निष्पादन को निलंबित और फिर से शुरू कर सकते हैं। वे इटरेटर, एसिंक पैटर्न और गेम लॉजिक के लिए आदर्श हैं:
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

### Q4: लुआ में त्रुटियों से निपटने का सबसे अच्छा तरीका क्या है?
**ए:** त्रुटियों को पकड़ने के लिए`pcall`/`xpcall`का उपयोग करें, और सफलता/असफलता पैटर्न के लिए एकाधिक मान लौटाएं:
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

### Q5: मैं गेम और एम्बेडेड सिस्टम के लिए लुआ प्रदर्शन को कैसे अनुकूलित करूं?
**ए:** मुख्य अभ्यास:
- सभी वेरिएबल्स के लिए`local`का उपयोग करें - वैश्विक पहुंच काफी धीमी है
- स्थानीय लोगों में बार-बार एक्सेस किए गए टेबल फ़ील्ड को कैश करें
- आकार ज्ञात होने पर तालिकाओं को पूर्व-आवंटित करें:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- हॉट लूप्स में अस्थायी टेबल बनाने से बचें
- कई स्ट्रिंग्स को जोड़ने के लिए`..`के बजाय`table.concat`का उपयोग करें
-`os.clock()`या डिबग हुक के साथ प्रोफ़ाइल
- LuaJIT में, C API के बजाय C इंटरऑप के लिए FFI का उपयोग करें
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक कॉन्फ़िगरेशन पार्सर का निर्माण
**चरण 1: समस्या को समझें**
एक साधारण कुंजी-मान कॉन्फ़िगरेशन फ़ाइल को पार्स करें जहां प्रत्येक पंक्ति`key = value`है।
**चरण 2: दृष्टिकोण को पहचानें**
पंक्तियाँ पढ़ें,`=`पर विभाजित करें, रिक्त स्थान को ट्रिम करें, और एक तालिका में संग्रहीत करें।
**चरण 3: कार्यान्वयन**```lua
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

**चरण 4: विस्तार करें**
अनुभाग समर्थन (`[section]`) जोड़ें, जबरदस्ती टाइप करें (संख्याएं, बूलियन), और नेस्टेड टेबल।
### समस्या 2: एक सरल इवेंट सिस्टम लागू करना
**चरण 1: समस्या को समझें**
एक ईवेंट एमिटर बनाएं जो नामित ईवेंट की सदस्यता लेने और उन्हें उत्सर्जित करने का समर्थन करता है।
**चरण 2: दृष्टिकोण को पहचानें**
हैंडलर फ़ंक्शंस की सूचियों के लिए टेबल मैपिंग इवेंट नामों का उपयोग करें।
**चरण 3: कार्यान्वयन**```lua
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

**चरण 4: सत्यापित करें**
हैंडलर में एकाधिक घटनाओं, निष्कासन और त्रुटि प्रबंधन के साथ परीक्षण करें।
### समस्या 3: कोरटाइन-आधारित पाइपलाइन बनाना
**चरण 1: समस्या को समझें**
एक डेटा प्रोसेसिंग पाइपलाइन बनाएं जहां प्रत्येक चरण कोरआउट्स के माध्यम से जुड़े डेटा को फ़िल्टर या परिवर्तित करता है।
**चरण 2: दृष्टिकोण को पहचानें**
पाइपलाइन चरणों के रूप में कोरटाइन का उपयोग करें - प्रत्येक चरण पिछले से खींचता है और अगले की ओर धकेलता है।
**चरण 3: कार्यान्वयन**```lua
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

**चरण 4: अनुकूलन करें**
यह पुल-आधारित पाइपलाइन न्यूनतम मेमोरी ओवरहेड के साथ एक समय में एक तत्व को संसाधित करती है - बड़ी या अनंत धाराओं के लिए आदर्श।
---

## सारांश
लुआ सर्वोत्कृष्ट एम्बेडिंग भाषा है। यह छोटा, तेज़ और सरल है - अन्य अनुप्रयोगों के अंदर रहने और उन्हें स्क्रिप्टिंग क्षमताएं प्रदान करने के लिए डिज़ाइन किया गया है। गेम डेवलपमेंट, रोबॉक्स और एम्बेडेड सिस्टम के लिए, लुआ एक उत्कृष्ट विकल्प है। यह एक सामान्य-उद्देश्य वाली भाषा नहीं है, लेकिन अपने विशिष्ट क्षेत्र (स्क्रिप्टिंग और एम्बेडिंग) के लिए, यह लगभग बेजोड़ है।