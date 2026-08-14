---
# Metadata
title: "Lua — Syntax Reference"
description: "Detailed syntax reference for Lua covering tables, metatables, coroutines, modules, closures, and embedding patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [lua, syntax-reference, tables, metatables, coroutines, closures, embedding, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Lua — 구문 참조
이 문서는 Lua(5.4)에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, 테이블 및 메타테이블, 코루틴, Lua의 독특한 디자인 철학에 초점을 맞춰 주요 Lua 참조를 보완합니다.
---

## 연산자 및 표현식
### 핵심 운영자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `+``-``*``/``%``^` | 산술 | `2 ^ 10`|  `^`는 지수화입니다 |
| `//`| 층 구분 | `7 // 2`| 3을 반환합니다(Lua 5.3+) |
| `==``~=` | 평등 | `a == b`|  `~=`는 "같지 않음" |
| `<``>``<=``>=` | 비교 | `a >= b`| |
| `and``or``not`| 논리적 | `a and b`| 부울이 아닌 피연산자를 반환합니다. |
| `..`| 연결 | `"hello" .. " world"`| |
| `#`| 길이 | `#t`| 문자열 또는 테이블의 길이 |
| `&``\|``~``<<``>>`| 비트별 | `a & b`| Lua 5.3+(정수 연산) |
### 논리 연산자 - 부울이 아닌 반환
```lua
-- and returns first falsy value, or last value
print(true and "hello")    -- "hello"
print(nil and "hello")     -- nil
print(false and "hello")   -- false
print("a" and "b")         -- "b"

-- or returns first truthy value
print(false or "default")  -- "default"
print(nil or "fallback")   -- "fallback"
print("" or "fallback")    -- "" (empty string is truthy!)

-- Common idioms
local x = a or b           -- default value
local y = obj and obj.prop -- safe access (like ?. in other languages)
local name = input or "Anonymous"

-- not always returns boolean
print(not nil)    -- true
print(not false)  -- true
print(not 0)      -- false (0 is truthy in Lua!)
print(not "")     -- false (empty string is truthy!)
```

### 우선순위(가장 높은 것에서 가장 낮은 것까지)
| 우선순위 | 운영자 |
|------------|------------|
| 1(가장 높음) | `^`|
| 2 | `not``#` `-`(단항) |
| 3 | `*``/``//``%` |
| 4 | `+``-` |
| 5 |  `..`(오른쪽 연관) |
| 6 | `<<``>>` |
| 7 | `&`|
| 8 |  `~`(바이너리 XOR) |
| 9 | `\|`|
| 10 | `==``~=``<``>``<=``>=` |
| 11 | `and`|
| 12(최저) | `or`|
---

## 제어 흐름
### 조건부
```lua
-- if / elseif / else
if score >= 90 then
  grade = "A"
elseif score >= 80 then
  grade = "B"
elseif score >= 70 then
  grade = "C"
else
  grade = "F"
end

-- Single-line if
if debug then print("debug mode") end

-- Ternary-like pattern (Lua has no ternary operator)
local status = (age >= 18) and "adult" or "minor"
-- Caution: fails if the "true" value is false/nil
-- Safe version:
local result = condition and true_value or fallback
```

### 루프
```lua
-- while
local i = 1
while i <= 10 do
  print(i)
  i = i + 1
end

-- repeat-until (do-while equivalent)
repeat
  line = io.read()
  process(line)
until line == "quit"

-- numeric for
for i = 1, 10 do         -- 1 to 10, step 1
  print(i)
end

for i = 10, 1, -1 do     -- 10 down to 1
  print(i)
end

for i = 0, 100, 10 do    -- 0, 10, 20, ..., 100
  print(i)
end

-- generic for (iterator)
for key, value in pairs(t) do
  print(key, value)
end

for index, value in ipairs(list) do
  print(index, value)
end

-- Loop control
for i = 1, 100 do
  if i % 2 == 0 then goto continue end
  if i > 20 then break end
  print(i)
  ::continue::
end
```

---

## 테이블 — 범용 데이터 구조
```lua
-- Table as array (1-based indexing)
local fruits = {"apple", "banana", "cherry"}
fruits[1]           -- "apple"
#fruits             -- 3
table.insert(fruits, "date")
table.remove(fruits, 2)  -- removes "banana"

-- Table as dictionary
local user = {
  name = "Alice",
  age = 30,
  email = "alice@example.com",
}
user.name           -- "Alice"
user["name"]        -- "Alice" (equivalent)
user.role = "admin" -- add new field

-- Mixed usage
local config = {
  host = "localhost",
  port = 8080,
  "first",           -- [1] = "first"
  "second",          -- [2] = "second"
  debug = true,
}

-- Table constructor with computed keys
local key = "dynamic"
local t = {
  [key] = "value",
  [1 + 2] = "three",
  ["with spaces"] = true,
}

-- Nested tables
local matrix = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9},
}
matrix[2][3]  -- 6

-- Table functions
table.sort(list)
table.sort(list, function(a, b) return a.name < b.name end)
table.concat({"a", "b", "c"}, ", ")  -- "a, b, c"
table.insert(list, pos, value)
table.remove(list, pos)
table.move(src, from, to, target_pos, dst)
table.unpack(list)  -- returns all elements

-- Shallow copy
local copy = {}
for k, v in pairs(original) do copy[k] = v end

-- Table as set
local set = {apple = true, banana = true, cherry = true}
if set["apple"] then print("has apple") end
```

---

## 기능
```lua
-- Function definition
function add(a, b)
  return a + b
end

-- Functions are first-class values
local multiply = function(a, b) return a * b end

-- Multiple return values
function divide(a, b)
  if b == 0 then return nil, "division by zero" end
  return a / b, nil
end

local result, err = divide(10, 0)
if err then print("Error: " .. err) end

-- Variadic functions
function sum(...)
  local total = 0
  for _, v in ipairs({...}) do
    total = total + v
  end
  return total
end

-- Select — access varargs by index
function first_three(...)
  return select(1, ...), select(2, ...), select(3, ...)
end

-- Functions as arguments
function map(t, fn)
  local result = {}
  for i, v in ipairs(t) do
    result[i] = fn(v)
  end
  return result
end

local doubled = map({1, 2, 3}, function(x) return x * 2 end)

-- Closures
function counter()
  local count = 0
  return function()
    count = count + 1
    return count
  end
end

local inc = counter()
print(inc())  -- 1
print(inc())  -- 2
print(inc())  -- 3

-- Tail calls (proper tail calls — no stack overflow)
function factorial(n, acc)
  acc = acc or 1
  if n <= 1 then return acc end
  return factorial(n - 1, n * acc)  -- tail call
end

-- Method syntax (syntactic sugar for self parameter)
local obj = {}
function obj:greet(name)
  print("Hello, " .. name .. "! I'm " .. self.name)
end
-- Equivalent to:
function obj.greet(self, name)
  print("Hello, " .. name .. "! I'm " .. self.name)
end
```

---

## 메타테이블 및 메타메서드
```lua
-- Metatable — customize table behavior
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
  return setmetatable({x = x, y = y}, Vector)
end

function Vector:__add(other)
  return Vector.new(self.x + other.x, self.y + other.y)
end

function Vector:__mul(scalar)
  return Vector.new(self.x * scalar, self.y * scalar)
end

function Vector:__tostring()
  return string.format("(%g, %g)", self.x, self.y)
end

function Vector:__eq(other)
  return self.x == other.x and self.y == other.y
end

function Vector:length()
  return math.sqrt(self.x^2 + self.y^2)
end

local v1 = Vector.new(3, 4)
local v2 = Vector.new(1, 2)
print(v1 + v2)        -- (4, 6)
print(v1 * 2)         -- (6, 8)
print(v1:length())    -- 5
print(v1 == v2)       -- false

-- Common metamethods
-- __index    — lookup when key not found
-- __newindex — assignment of new keys
-- __call     — call table as function
-- __tostring — string conversion
-- __concat   — .. operator
-- __len      — # operator
-- __eq __lt __le — comparison operators
-- __add __sub __mul __div __mod __pow — arithmetic
-- __unm      — unary minus
-- __metatable — protect metatable

-- __newindex for read-only tables
local function readonly(t)
  local proxy = {}
  local mt = {
    __index = t,
    __newindex = function() error("attempt to modify read-only table") end,
  }
  return setmetatable(proxy, mt)
end

local config = readonly({host = "localhost", port = 8080})
print(config.host)   -- "localhost"
config.host = "x"    -- error!

-- __call — callable tables
local function make_accumulator(initial)
  local value = initial or 0
  return setmetatable({}, {
    __call = function(self, n)
      value = value + (n or 1)
      return value
    end,
  })
end

local acc = make_accumulator(0)
print(acc())      -- 1
print(acc(5))     -- 6
print(acc())      -- 7
```

---

## 모듈 및 오류 처리
```lua
-- Module pattern (module.lua)
local M = {}

local private_var = "hidden"

function M.public_function()
  return "visible"
end

function M.create(name)
  return setmetatable({name = name}, {__index = M})
end

return M

-- Requiring modules
local mymodule = require("mymodule")
local json = require("json")

-- Error handling with pcall/xpcall
local ok, result = pcall(function()
  return risky_operation()
end)

if not ok then
  print("Error: " .. tostring(result))
end

-- xpcall with message handler
local ok, result = xpcall(
  function() return process() end,
  function(err) return debug.traceback(err) end
)

-- Error levels
function validate(input)
  if not input then
    error("input is nil", 2)  -- level 2 = caller's line
  end
end

-- Assert — error if condition is false
local file = assert(io.open("data.txt", "r"))

-- Protected environment
local ok, result = pcall(function()
  -- sandboxed code
end)
```

---

## 코루틴
```lua
-- Basic coroutine
local co = coroutine.create(function()
  print("step 1")
  coroutine.yield()
  print("step 2")
  coroutine.yield(42)
  print("step 3")
  return "done"
end)

coroutine.resume(co)       -- step 1
coroutine.resume(co)       -- step 2
local ok, val = coroutine.resume(co)  -- step 3; ok=true, val=42
coroutine.resume(co)       -- ok=true, val="done"

-- Coroutine as iterator
function list_iter(t)
  return coroutine.wrap(function()
    for i, v in ipairs(t) do
      coroutine.yield(v)
    end
  end)
end

for item in list_iter({10, 20, 30}) do
  print(item)
end

-- Producer-consumer pattern
function producer()
  return coroutine.wrap(function()
    while true do
      local data = fetch_data()
      if data == nil then break end
      coroutine.yield(data)
    end
  end)
end

-- Coroutine-based pipeline
function filter(pred, input)
  return coroutine.wrap(function()
    for value in input do
      if pred(value) then
        coroutine.yield(value)
      end
    end
  end)
end

function map(fn, input)
  return coroutine.wrap(function()
    for value in input do
      coroutine.yield(fn(value))
    end
  end)
end

-- Compose pipeline
local pipeline = map(
  function(x) return x * x end,
  filter(
    function(x) return x > 5 end,
    list_iter({1, 2, 3, 4, 5, 6, 7, 8})
  )
)

for v in pipeline do print(v) end  -- 36, 49, 64
```

---

## 문자열 패턴(Lua의 정규식 대안)
```lua
-- String patterns (simpler than regex)
string.find("hello world", "world")      -- 7, 11
string.match("user@example.com", "(%w+)@(%w+)")  -- "user", "example"
string.gsub("hello world", "(%w+)", "%1-%1")     -- "hello-hello world-world"
string.gmatch("one two three", "%a+")     -- iterator: "one", "two", "three"

-- Pattern classes
-- %a  letters    %d  digits     %w  alphanumeric
-- %s  spaces     %p  punctuation
-- %l  lowercase  %u  uppercase
-- %c  control    %x  hex digits

-- Character sets
string.match("abc123", "[%d%l]+")   -- "abc123"
string.match("ABC", "[^%d]+")       -- "ABC" (non-digits)

-- Repetition
-- *  0 or more (greedy)
-- +  1 or more (greedy)
-- -  0 or more (lazy)
-- ?  0 or 1

string.match("  hello  ", "%s*%a+%s*")  -- "  hello  "
string.match("a1b2c3", "%a-")            -- "" (lazy)

-- Captures
local date = "2026-08-09"
local year, month, day = date:match("(%d+)-(%d+)-(%d+)")

-- Anchors
string.find("hello", "^hello")   -- 1 (starts with)
string.find("hello", "lo$")      -- 4 (ends with)
```

---

## 요약
Lua의 구문은 의도적으로 최소화되었습니다. 전체 언어를 한 페이지에 설명할 수 있습니다. 테이블은 범용 데이터 구조(배열, 사전, 개체, 모듈) 역할을 합니다. 메타테이블은 언어 복잡성 없이 확장성을 제공합니다. 코루틴은 협동적인 멀티태스킹과 우아한 반복자 패턴을 가능하게 합니다. 언어의 힘은 내장 가능성에서 비롯됩니다. Lua는 호스트 애플리케이션 내부에서 작동하도록 설계되어 최소한의 오버헤드로 스크립팅 기능을 제공합니다. 게임 개발, 구성 및 임베디드 시스템의 경우 Lua의 단순성은 가장 큰 장점입니다. 필요한 작업을 정확하게 수행하는 작은 언어일 뿐 그 이상은 아닙니다.