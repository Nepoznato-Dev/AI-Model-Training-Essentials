---
# البيانات الوصفية
العنوان: "لوا"
الوصف: "مرجع شامل للغة برمجة Lua يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [lua، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "26 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
# لوا
Lua هي لغة برمجة نصية خفيفة الوزن وقابلة للتضمين مصممة لتوسيع التطبيقات. تم إنشاء لغة Lua عام 1993 في الجامعة البابوية الكاثوليكية في ريو دي جانيرو بالبرازيل، وهي واحدة من أسرع لغات البرمجة النصية المتاحة. حجمه الصغير (المترجم هو ~ 120 كيلو بايت) وبساطته تجعله الخيار الأمثل للبرمجة النصية لتطوير الألعاب والأنظمة المدمجة والتكوين.
تشتهر Lua بأنها لغة البرمجة النصية وراء Roblox (منصة الألعاب التي تضم أكثر من 200 مليون مستخدم شهريًا)، وإضافات World of Warcraft، والعديد من محركات الألعاب (Love2D، وDefold، وCorona SDK). كما يتم استخدامه في Nginx (OpenResty)، وRedis، وWireshark.
---

## لماذا يهم لوا
- **قابل للتضمين**: مصمم ليتم تضمينه في تطبيقات أخرى — يوفر المضيف الوظيفة.
- **مساحة صغيرة جدًا**: يصل حجم المترجم الفوري بأكمله إلى 120 كيلو بايت تقريبًا. مثالية للأنظمة المدمجة.
- **سريع**: واحدة من أسرع لغات البرمجة النصية المترجمة.
- **بسيط**: حوالي 20 كلمة رئيسية فقط. سهلة التعلم والاندماج.
- **تطوير اللعبة**: لغة البرمجة النصية القياسية للعديد من محركات ومنصات الألعاب.
- **Roblox**: يعمل على تشغيل نظام Roblox البيئي بأكمله — ملايين الألعاب التي أنشأها المستخدمون.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **مكتبة قياسية محدودة** | الحد الأدنى من الوظائف المضمنة | قم بالتوسيع باستخدام C/C++ أو استخدم حزم LuaRocks |
| **الفهرسة المستندة إلى 1** | تبدأ المصفوفات عند الفهرس 1 (غير عادي للمبرمجين) | قبول كخيار التصميم؛ متسقة في جميع أنحاء |
| **لا توجد فصول** | الجداول والجداول الوصفية فقط - يجب تنفيذ OOP يدويًا | استخدم الجداول الوصفية أو مكتبات OOP |
| **الألعاب الخارجية المتخصصة** | استخدام محدود في الويب أو علوم البيانات أو المؤسسات | تستخدم للبرمجة النصية/التضمين؛ لغات أخرى للتطبيقات |
| **سوق العمل الصغير** | في الغالب تطوير اللعبة والأدوار المضمنة | يعد تطوير Roblox مجالًا متناميًا |
---

## أساسيات بناء الجملة
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

## بناء الجملة والأنماط المتقدمة
### الجداول الوصفية — أساس قوة لوا
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

### الإغلاقات والأنماط الوظيفية
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

### قيم الإرجاع المتعددة والتدمير
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

### أنماط السلسلة (بديل Lua's Regex)
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

## التزامن والتوازي
### Coroutines — تعدد المهام التعاوني
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

### نمط التكرار القائم على Coroutine
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

## تكوين المشروع ونظام البناء
### هيكل المشروع
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

### LuaRocks — إدارة الحزم
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — مواصفات الحزمة
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

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### تم الضبط - إطار الاختبار
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

### السخرية مع luassert
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

### أوامر الاختبار
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## إمكانية التشغيل البيني
### واجهة برمجة تطبيقات C — تضمين Lua في لغة C
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

### LuaJIT FFI — مكالمات C المباشرة
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

## أنماط التصميم
### نمط الوحدة (مفردة)
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

### نظام المراقب / الحدث
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

### نمط الأوامر
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

## الأداء والتحسين
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

## النشر
### نشر عامل الميناء
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## متى تستخدم لوا
| السيناريو | لماذا لوا | البديل الأفضل |
|----------|--------|------------------|
| لعبة البرمجة النصية | خفيفة الوزن وسريعة وقابلة للتضمين | — |
| تطوير روبلوكس | الخيار الوحيد | — |
| الأنظمة المدمجة | بصمة صغيرة | سي، ميكروبايثون |
| ملحق التطبيق | مصممة للتضمين | بايثون (أكبر)، جافا سكريبت (V8) |
| ملفات التكوين | بسيطة وسريعة | جسون، تومل، يامل |
| تطوير الويب | OpenResty موجود ولكنه متخصص | جافا سكريبت، بايثون، اذهب |
| تطوير التطبيقات العامة | غير مصمم للتطبيقات المستقلة | بايثون، جو، جافا |
| علم البيانات | ليس النظام البيئي | بايثون، ر |
---

## ملخص
Lua هي لغة التضمين المثالية. إنه صغير وسريع وبسيط - مصمم للعيش داخل التطبيقات الأخرى وتزويدها بإمكانيات البرمجة النصية. بالنسبة لتطوير الألعاب وRoblox والأنظمة المدمجة، يعد Lua خيارًا ممتازًا. إنها ليست لغة ذات أغراض عامة، ولكن بالنسبة لمكانتها المحددة (البرمجة النصية والتضمين)، فهي لا مثيل لها تقريبًا.