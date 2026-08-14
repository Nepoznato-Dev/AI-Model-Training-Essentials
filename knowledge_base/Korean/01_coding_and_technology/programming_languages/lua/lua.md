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
# 루아
Lua는 애플리케이션 확장을 위해 설계된 가볍고 내장 가능한 스크립팅 언어입니다. 1993년 브라질 리우데자네이루의 교황청 가톨릭 대학교에서 만들어진 Lua는 가장 빠른 스크립팅 언어 중 하나입니다. 작은 설치 공간(인터프리터는 ~120KB)과 단순성으로 인해 게임 개발 스크립팅, 임베디드 시스템 및 구성에 적합한 선택입니다.
Lua는 Roblox(2억 명 이상의 월간 사용자를 보유한 게임 플랫폼), World of Warcraft 애드온 및 수많은 게임 엔진(Love2D, Defold, Corona SDK)을 뒷받침하는 스크립팅 언어로 가장 잘 알려져 있습니다. Nginx(OpenResty), Redis 및 Wireshark에서도 사용됩니다.
---

## 루아가 중요한 이유
- **임베딩 가능**: 다른 애플리케이션에 내장되도록 설계되었으며 호스트가 기능을 제공합니다.
- **작은 설치 공간**: 전체 인터프리터는 ~120KB에 맞습니다. 임베디드 시스템에 이상적입니다.
- **빠름**: 가장 빠른 해석 스크립트 언어 중 하나입니다.
- **단순**: 최대 20개의 키워드만 가능합니다. 배우고 통합하기 쉽습니다.
- **게임 개발**: 많은 게임 엔진 및 플랫폼을 위한 표준 스크립팅 언어입니다.
- **Roblox**: 전체 Roblox 생태계, 즉 수백만 개의 사용자 제작 게임을 지원합니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **제한된 표준 라이브러리** | 최소한의 내장 기능 | C/C++로 확장하거나 LuaRocks 패키지 사용 |
| **1 기반 색인 생성** | 배열은 인덱스 1에서 시작합니다(프로그래머에게는 일반적이지 않음) | 디자인 선택으로 받아들입니다. 전체적으로 일관된 |
| **수업 없음** | 테이블과 메타테이블만 — OOP는 수동으로 구현되어야 합니다 | 메타테이블 또는 OOP 라이브러리 사용 |
| **틈새 게임 외부** | 웹, 데이터 과학 또는 기업에서의 제한된 사용 | 스크립팅/임베딩에 사용합니다. 응용 프로그램을 위한 다른 언어 |
| **작은 취업 시장** | 주로 게임 개발 및 임베디드 역할 | Roblox 개발은 성장하는 틈새 시장입니다 |
---

## 구문 기본 사항
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

## 고급 구문 및 패턴
### 메타테이블 — Lua 성능의 기초
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

### 클로저와 기능적 패턴
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

### 다중 반환 값 및 구조 분해
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

### 문자열 패턴(Lua의 정규식 대안)
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

## 동시성 및 병렬성
### 코루틴 — 협력적 멀티태스킹
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

### 코루틴 기반 반복자 패턴
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조
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

### LuaRocks — 패키지 관리
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — 패키지 사양
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

### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### 파열 — 테스트 프레임워크
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

### luassert로 조롱하기
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

### 테스트 명령
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## 상호 운용성
### C API — C에 Lua 내장
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

### LuaJIT FFI — 직접 C 호출
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

## 디자인 패턴
### 모듈 패턴(싱글톤)
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

### 옵저버 / 이벤트 시스템
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

### 명령 패턴
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

## 성능 및 최적화
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

## 배포
### 도커 배포
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Lua를 사용해야 하는 경우
| 시나리오 | 왜 루아인가 | 더 나은 대안 |
|----------|---------|------|
| 게임 스크립팅 | 가볍고 빠르며 내장 가능 | — |
| Roblox 개발 | 유일한 옵션 | — |
| 임베디드 시스템 | 작은 발자국 | C, 마이크로파이썬 |
| 애플리케이션 확장 | 임베딩용으로 설계됨 | Python(대형), JavaScript(V8) |
| 구성 파일 | 간단하고 빠릅니다 | JSON, TOML, YAML |
| 웹 개발 | OpenResty가 존재하지만 틈새 시장 | 자바스크립트, 파이썬, Go |
| 일반 애플리케이션 개발 | 독립형 앱용으로 설계되지 않음 | 파이썬, 바둑, 자바 |
| 데이터 과학 | 생태계가 아니다 | 파이썬, R |
---

## 종합 Q&A
### Q1: Lua는 왜 0 기반 인덱싱 대신 1 기반 인덱싱을 사용합니까?
**답:** Lua는 프로그래머가 아닌 사용자를 위해 설계되었으며 자연 계산 규칙을 ​​따릅니다.`#`연산자,`ipairs`및 문자열 함수는 모두 1 기반 인덱싱을 사용합니다.
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

이는 표준 라이브러리 전체에서 일관됩니다. C(0 기반)와 인터페이스할 때 오프셋에 주의하세요.
### Q2: Lua에서 객체 지향 패턴을 어떻게 구현하나요?
**답:** Lua는 OOP에 테이블과 메타테이블을 사용합니다.`__index`메타메서드는 프로토타입에서 메소드 조회를 가능하게 합니다.
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

### Q3: 코루틴은 어떻게 작동하며 언제 사용해야 합니까?
**답변:** 코루틴은 실행을 일시 중지하고 재개할 수 있는 협력 스레드입니다. 반복자, 비동기 패턴 및 게임 논리에 이상적입니다.
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

### Q4: Lua에서 오류를 처리하는 가장 좋은 방법은 무엇입니까?
**A:**`pcall`/ `xpcall`를 사용하여 오류를 포착하고 성공/실패 패턴에 대해 여러 값을 반환합니다.
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

### Q5: 게임 및 임베디드 시스템의 Lua 성능을 어떻게 최적화합니까?
**답:** 주요 사례:
- 모든 변수에 `local`를 사용합니다. 전역 액세스가 상당히 느립니다.
- 로컬에서 자주 액세스하는 테이블 필드를 캐시합니다.
- 크기가 알려진 경우 테이블 사전 할당:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- 핫 루프에 임시 테이블을 생성하지 마세요.
- 여러 문자열을 결합하려면`..`대신 `table.concat`를 사용하세요.
-`os.clock()`또는 디버그 후크가 있는 프로파일
- LuaJIT에서는 C API 대신 C interop에 FFI를 사용합니다.
---

## 사고 사슬 문제 해결
### 문제 1: 구성 파서 구축
**1단계: 문제 이해**
각 줄이`key = value`인 간단한 키-값 구성 파일을 구문 분석합니다.
**2단계: 접근 방식 파악**
줄을 읽고,`=`에서 분할하고, 공백을 자르고, 테이블에 저장합니다.
**3단계: 구현**```lua
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

**4단계: 확장**
섹션 지원(`[section]`), 유형 강제(숫자, 부울) 및 중첩 테이블을 추가합니다.
### 문제 2: 간단한 이벤트 시스템 구현
**1단계: 문제 이해**
명명된 이벤트 구독 및 생성을 지원하는 이벤트 이미터를 만듭니다.
**2단계: 접근 방식 파악**
핸들러 함수 목록에 이벤트 이름을 매핑하는 테이블을 사용합니다.
**3단계: 구현**```lua
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

**4단계: 확인**
핸들러에서 여러 이벤트, 제거 및 오류 처리를 테스트합니다.
### 문제 3: 코루틴 기반 파이프라인 만들기
**1단계: 문제 이해**
각 단계에서 코루틴을 통해 연결된 데이터를 필터링하거나 변환하는 데이터 처리 파이프라인을 구축합니다.
**2단계: 접근 방식 파악**
코루틴을 파이프라인 단계로 사용합니다. 각 단계는 이전 단계에서 가져와서 다음 단계로 푸시합니다.
**3단계: 구현**```lua
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

**4단계: 최적화**
이 풀 기반 파이프라인은 최소한의 메모리 오버헤드로 한 번에 하나의 요소를 처리하므로 대규모 또는 무한 스트림에 이상적입니다.
---

## 요약
Lua는 전형적인 임베딩 언어입니다. 작고 빠르며 간단합니다. 다른 애플리케이션 내부에서 작동하고 스크립팅 기능을 제공하도록 설계되었습니다. 게임 개발, Roblox 및 임베디드 시스템의 경우 Lua는 탁월한 선택입니다. 범용 언어는 아니지만 특정 틈새(스크립팅 및 임베딩) 측면에서 거의 타의 추종을 불허합니다.