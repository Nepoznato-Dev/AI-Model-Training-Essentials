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
Lua to lekki, osadzany język skryptowy przeznaczony do rozszerzania aplikacji. Utworzony w 1993 roku na Papieskim Uniwersytecie Katolickim w Rio de Janeiro w Brazylii, Lua jest jednym z najszybszych dostępnych języków skryptowych. Jego niewielkie rozmiary (interpreter ma ~120 KB) i prostota sprawiają, że jest to doskonały wybór do tworzenia skryptów gier, systemów wbudowanych i konfiguracji.
Lua jest najbardziej znana jako język skryptowy Robloxa (platformy gier z ponad 200 milionami użytkowników miesięcznie), dodatków do World of Warcraft i licznych silników gier (Love2D, Defold, Corona SDK). Jest również używany w Nginx (OpenResty), Redis i Wireshark.
---

## Dlaczego Lua ma znaczenie
- **Możliwość wbudowania**: Zaprojektowany do osadzenia w innych aplikacjach — host zapewnia tę funkcjonalność.
- **Mała powierzchnia**: Cały interpreter mieści się w ~120 KB. Idealny do systemów wbudowanych.
- **Szybki**: Jeden z najszybciej interpretowanych języków skryptowych.
- **Proste**: tylko ~20 słów kluczowych. Łatwy do nauki i integracji.
- **Tworzenie gier**: Standardowy język skryptowy dla wielu silników i platform gier.
- **Roblox**: Obsługuje cały ekosystem Roblox — miliony gier tworzonych przez użytkowników.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Ograniczona biblioteka standardowa** | Minimalna wbudowana funkcjonalność | Rozszerz o C/C++ lub użyj pakietów LuaRocks |
| **Indeksowanie oparte na 1** | Tablice zaczynają się od indeksu 1 (nietypowe dla programistów) | Zaakceptuj jako wybór projektu; spójne w całym |
| **Brak zajęć** | Tylko tabele i metatabele — OOP należy zaimplementować ręcznie | Użyj metatabel lub bibliotek OOP |
| **Niszowe gry zewnętrzne** | Ograniczone zastosowanie w sieci, nauce danych i przedsiębiorstwach | Używaj do pisania skryptów/osadzania; inne języki aplikacji |
| **Mały rynek pracy** | Głównie tworzenie gier i wbudowane role | Rozwój Roblox to rosnąca nisza |
---

## Podstawy składni
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

## Zaawansowana składnia i wzorce
### Metatabele — podstawa mocy Lui
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

### Zamknięcia i wzorce funkcjonalne
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

### Wiele zwracanych wartości i destrukturyzacja
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

### Wzory ciągów (alternatywa dla wyrażeń regularnych Lui)
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

## Współbieżność i równoległość
### Współprogramy — wielozadaniowość w trybie współpracy
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

### Wzorzec iteratora oparty na współprogramie
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

## Konfiguracja projektu i budowanie systemu
### Struktura projektu
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

### LuaRocks — zarządzanie pakietami
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — specyfikacja pakietu
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

### Potok CI/CD (akcje w GitHub)
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

## Testowanie
### Busted — środowisko testowania
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

### Kpiny z luassert
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

### Polecenia testowe
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## Interoperacyjność
### C API — Osadzanie Lua w C
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

### LuaJIT FFI — bezpośrednie połączenia C
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

## Wzorce projektowe
### Wzorzec modułu (Singleton)
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

### Obserwator/System zdarzeń
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

### Wzorzec poleceń
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

## Wydajność i optymalizacja
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

## Zastosowanie
### Wdrożenie Dockera
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Kiedy używać Lua
| Scenariusz | Dlaczego Lua | Lepsza alternatywa |
|---------|---------|--------------------------------|
| Skrypty gier | Lekki, szybki, do osadzania | — |
| Rozwój Robloxa | Jedyna opcja | — |
| Systemy wbudowane | Mały ślad | C, MicroPython |
| Rozszerzenie aplikacji | Przeznaczony do osadzania | Python (większy), JavaScript (V8) |
| Pliki konfiguracyjne | Prosto i szybko | JSON, TOML, YAML |
| Tworzenie stron internetowych | OpenResty istnieje, ale jest niszowy | JavaScript, Python, Go |
| Ogólne tworzenie aplikacji | Nie przeznaczony dla samodzielnych aplikacji | Python, Go, Java |
| Nauka o danych | Nie ekosystem | Python, R |
---

## Syntetyczne pytania i odpowiedzi
### P1: Dlaczego Lua używa indeksowania opartego na 1 zamiast na 0?
**O:** Lua został zaprojektowany dla użytkowników niebędących programistami i stosuje się do naturalnych konwencji liczenia. Operator `#`,`ipairs`i funkcje łańcuchowe korzystają z indeksowania opartego na 1:
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

Jest to spójne w całej bibliotece standardowej. Podczas łączenia się z C (opartym na 0) należy pamiętać o przesunięciu.
### P2: Jak zaimplementować wzorce obiektowe w Lua?
**A:** Lua używa tabel i metatabel do OOP. Metametoda`__index`umożliwia wyszukiwanie metod na prototypach:
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

### P3: Jak działają współprogramy i kiedy powinienem ich używać?
**O:** Współprogramy to wątki kooperacyjne, które mogą zawieszać i wznawiać wykonywanie. Są idealne do iteratorów, wzorców asynchronicznych i logiki gry:
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

### P4: Jaki jest najlepszy sposób obsługi błędów w Lua?
**A:** Użyj`pcall`/ `xpcall`, aby wychwycić błędy i zwrócić wiele wartości dla wzorców powodzenia/porażki:
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

### P5: Jak zoptymalizować wydajność Lua pod kątem gier i systemów wbudowanych?
**O:** Kluczowe praktyki:
- Użyj`local`dla wszystkich zmiennych — dostęp globalny jest znacznie wolniejszy
- Buforuj często używane pola tabeli w ustawieniach lokalnych
- Wstępnie przydziel tabele, gdy rozmiar jest znany:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- Unikaj tworzenia tabel tymczasowych w gorących pętlach
- Użyj`table.concat`zamiast`..`do łączenia wielu ciągów
- Profil z hakami`os.clock()`lub debugowaniem
- W LuaJIT użyj FFI dla współdziałania C zamiast API C
---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Budowanie parsera konfiguracji
**Krok 1: Zrozum problem**
Przeanalizuj prosty plik konfiguracyjny klucz-wartość, w którym każda linia to`key = value`.
**Krok 2: Zidentyfikuj podejście**
Przeczytaj linie, podziel na `=`, przytnij białe znaki i zapisz w tabeli.
**Krok 3: Wdróż**```lua
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

**Krok 4: Przedłuż**
Dodaj obsługę sekcji (`[section]`), wymuszenie typu (liczby, wartości logiczne) i zagnieżdżone tabele.
### Problem 2: Implementacja prostego systemu zdarzeń
**Krok 1: Zrozum problem**
Utwórz emiter zdarzeń, który obsługuje subskrybowanie nazwanych zdarzeń i emitowanie ich.
**Krok 2: Zidentyfikuj podejście**
Użyj tabeli mapującej nazwy zdarzeń na listy funkcji obsługi.
**Krok 3: Wdróż**```lua
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

**Krok 4: Zweryfikuj**
Testuj z wieloma zdarzeniami, usuwaniem i obsługą błędów w programach obsługi.
### Problem 3: Tworzenie potoku opartego na współprogramie
**Krok 1: Zrozum problem**
Zbuduj potok przetwarzania danych, w którym każdy etap filtruje lub przekształca dane połączone za pomocą współprogramów.
**Krok 2: Zidentyfikuj podejście**
Używaj współprogramów jako etapów potoku — każdy etap łączy się z poprzednim i przechodzi do następnego.
**Krok 3: Wdróż**```lua
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

**Krok 4: Optymalizacja**
Ten potok oparty na ściąganiu przetwarza jeden element na raz przy minimalnym obciążeniu pamięci — jest to idealne rozwiązanie w przypadku dużych lub nieskończonych strumieni.
---

## Streszczenie
Lua jest kwintesencją języka osadzania. Jest mały, szybki i prosty — zaprojektowany do działania w innych aplikacjach i zapewniania im możliwości tworzenia skryptów. Do tworzenia gier, Roblox i systemów wbudowanych Lua jest doskonałym wyborem. Nie jest to język ogólnego przeznaczenia, ale w swojej specyficznej niszy (pisanie skryptów i osadzanie) nie ma sobie równych.