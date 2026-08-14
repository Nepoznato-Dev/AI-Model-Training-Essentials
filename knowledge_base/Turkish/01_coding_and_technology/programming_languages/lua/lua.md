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
# Lua
Lua, uygulamaları genişletmek için tasarlanmış hafif, yerleştirilebilir bir kodlama dilidir. 1993 yılında Brezilya'daki Rio de Janeiro Papalık Katolik Üniversitesi'nde oluşturulan Lua, mevcut en hızlı kodlama dillerinden biridir. Küçük kaplama alanı (yorumlayıcı ~120 KB'dir) ve basitliği, onu oyun geliştirme komut dosyası oluşturma, gömülü sistemler ve yapılandırma için ilk tercih haline getirir.
Lua, Roblox'un (aylık 200 milyondan fazla kullanıcıya sahip oyun platformu), World of Warcraft eklentilerinin ve çok sayıda oyun motorunun (Love2D, Defold, Corona SDK) arkasındaki kodlama dili olarak bilinir. Ayrıca Nginx (OpenResty), Redis ve Wireshark'ta da kullanılır.
---

## Lua Neden Önemlidir
- **Gömülebilir**: Diğer uygulamalara gömülmek üzere tasarlanmıştır; işlevselliği ana bilgisayar sağlar.
- **Küçük ayak izi**: Yorumlayıcının tamamı ~120 KB'ye sığar. Gömülü sistemler için idealdir.
- **Hızlı**: En hızlı yorumlanan kodlama dillerinden biri.
- **Basit**: Yalnızca ~20 anahtar kelime. Öğrenmesi ve entegre etmesi kolaydır.
- **Oyun geliştirme**: Birçok oyun motoru ve platform için standart kodlama dili.
- **Roblox**: Kullanıcı tarafından oluşturulan milyonlarca oyundan oluşan tüm Roblox ekosistemine güç verir.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Sınırlı standart kütüphane** | Minimum yerleşik işlevsellik | C/C++ ile genişletin veya LuaRocks paketlerini kullanın |
| **1 tabanlı indeksleme** | Diziler dizin 1'den başlar (programcılar için alışılmadık bir durum) | Bir tasarım tercihi olarak kabul edin; baştan sona tutarlı |
| **Ders yok** | Yalnızca tablolar ve metatablolar — OOP manuel olarak uygulanmalıdır | Metatabloları veya OOP kitaplıklarını kullanın |
| **Niş dış mekan oyunları** | Web'de, veri biliminde veya kurumsal alanda sınırlı kullanım | Komut dosyası oluşturma/katıştırma için kullanın; uygulamalar için diğer diller |
| **Küçük iş piyasası** | Çoğunlukla oyun geliştirme ve gömülü roller | Roblox geliştirme büyüyen bir niş |
---

## Söz Diziminin Temelleri
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

## Gelişmiş Sözdizimi ve Desenler
### Metatablolar — Lua'nın Gücünün Temeli
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

### Kapanışlar ve İşlevsel Kalıplar
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

### Çoklu Dönüş Değerleri ve Yıkım
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

### Dize Desenleri (Lua'nın Regex Alternatifi)
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

## Eşzamanlılık ve Paralellik
### Eşyordamlar — İşbirliğine Dayalı Çoklu Görev
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

### Eşyordam Tabanlı Yineleyici Deseni
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
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

### LuaRocks — Paket Yönetimi
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — Paket Spesifikasyonu
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

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### Bozuldu — Çerçeveyi Test Etme
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

### Luassert ile alay etmek
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

### Test Komutları
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## Birlikte Çalışabilirlik
### C API — Lua'yı C'ye yerleştirme
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

### LuaJIT FFI — Doğrudan C Çağrıları
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

## Tasarım Desenleri
### Modül Deseni (Tek Tonlu)
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

### Gözlemci / Etkinlik Sistemi
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

### Komut Modeli
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

## Performans ve Optimizasyon
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

## Dağıtım
### Docker Dağıtımı
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Lua Ne Zaman Kullanılmalı?
| Senaryo | Neden Lua | Daha İyi Alternatif |
|----------|------------|-----------|
| Oyun komut dosyası oluşturma | Hafif, hızlı, yerleştirilebilir | — |
| Roblox geliştirme | Tek seçenek | — |
| Gömülü sistemler | Küçük ayak izi | C, MicroPython |
| Uygulama uzantısı | Yerleştirmek için tasarlandı | Python (daha büyük), JavaScript (V8) |
| Yapılandırma dosyaları | Basit ve hızlı | JSON, TOML, YAML |
| Web geliştirme | OpenResty var ama niş | JavaScript, Python, Git |
| Genel uygulama geliştirme | Bağımsız uygulamalar için tasarlanmamıştır | Python, Git, Java |
| Veri bilimi | Ekosistem değil | Python, R |
---

## Sentetik Soru-Cevap
### S1: Lua neden 0 tabanlı indeksleme yerine 1 tabanlı indekslemeyi kullanıyor?
**C:** Lua, programcı olmayan kullanıcılar için tasarlanmıştır ve doğal sayma kurallarına uyar.`#`operatörü,`ipairs`ve dize işlevlerinin tümü 1 tabanlı dizin oluşturmayı kullanır:
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

Bu, standart kitaplığın tamamında tutarlıdır. C (0 tabanlı) ile arayüz oluştururken ofsete dikkat edin.
### S2: Lua'da nesne yönelimli kalıpları nasıl uygularım?
**C:** Lua, OOP için tabloları ve metatabloları kullanıyor.`__index`meta yöntemi, prototiplerde yöntem aramayı etkinleştirir:
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

### S3: Eşyordamlar nasıl çalışır ve bunları ne zaman kullanmalıyım?
**C:** Eşyordamlar, yürütmeyi askıya alabilen ve devam ettirebilen ortak iş parçacıklarıdır. Yineleyiciler, eşzamansız kalıplar ve oyun mantığı için idealdirler:
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

### S4: Lua'daki hataları gidermenin en iyi yolu nedir?
**C:** Hataları yakalamak ve başarı/başarısızlık modelleri için birden fazla değer döndürmek için`pcall`/`xpcall`kullanın:
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

### S5: Lua performansını oyunlar ve gömülü sistemler için nasıl optimize edebilirim?
**C:** Temel uygulamalar:
- Tüm değişkenler için`local`kullanın — küresel erişim önemli ölçüde daha yavaştır
- Yerellerde sık erişilen tablo alanlarını önbelleğe alın
- Boyutu bilindiğinde tabloları önceden tahsis edin:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- Sıcak döngülerde geçici tablolar oluşturmaktan kaçının
- Birçok dizeyi birleştirmek için`..`yerine`table.concat`kullanın
-`os.clock()`veya hata ayıklama kancalarına sahip profil
- LuaJIT'te C API yerine C birlikte çalışma için FFI'yi kullanın
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Yapılandırma Ayrıştırıcı Oluşturma
**1. Adım: Sorunu Anlayın**
Her satırın`key = value`olduğu basit bir anahtar/değer yapılandırma dosyasını ayrıştırın.
**2. Adım: Yaklaşımı Belirleyin**
Satırları okuyun, `=`'ye bölün, boşlukları kırpın ve bir tabloda saklayın.
**3. Adım: Uygulama**```lua
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

**4. Adım: Genişletin**
Bölüm desteği (`[section]`), zorlama türü (sayılar, boolean'lar) ve iç içe tablolar ekleyin.
### Sorun 2: Basit Bir Olay Sisteminin Uygulanması
**1. Adım: Sorunu Anlayın**
Adlandırılmış etkinliklere abone olmayı ve bunları yayınlamayı destekleyen bir etkinlik yayıcı oluşturun.
**2. Adım: Yaklaşımı Belirleyin**
İşleyici işlevleri listelerine olay adlarını eşleyen bir tablo kullanın.
**3. Adım: Uygulama**```lua
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

**4. Adım: Doğrulayın**
İşleyicilerde birden fazla olay, kaldırma ve hata işleme ile test edin.
### Sorun 3: Eşyordam Tabanlı Ardışık Düzen Oluşturma
**1. Adım: Sorunu Anlayın**
Her aşamanın verileri filtrelediği veya dönüştürdüğü, eşyordamlar yoluyla bağlanan bir veri işleme hattı oluşturun.
**2. Adım: Yaklaşımı Belirleyin**
Eşyordamları işlem hattı aşamaları olarak kullanın; her aşama bir öncekinden çeker ve bir sonrakine iter.
**3. Adım: Uygulama**```lua
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

**4. Adım: Optimize edin**
Bu çekme tabanlı işlem hattı, minimum bellek yüküyle aynı anda bir öğeyi işler; büyük veya sonsuz akışlar için idealdir.
---

## Özet
Lua mükemmel bir yerleştirme dilidir. Küçük, hızlı ve basittir; diğer uygulamaların içinde barındırılacak ve onlara komut dosyası oluşturma yetenekleri sağlayacak şekilde tasarlanmıştır. Oyun geliştirme, Roblox ve gömülü sistemler için Lua mükemmel bir seçimdir. Genel amaçlı bir dil değildir, ancak kendine özgü alanı (komut dosyası oluşturma ve yerleştirme) açısından neredeyse eşsizdir.