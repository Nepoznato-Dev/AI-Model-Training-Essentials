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

# Lua - مرجع نحو
این سند یک مرجع نحوی ساختار یافته و جامع برای Lua (5.4) ارائه می کند. این مرجع اصلی Lua را با تمرکز بر الگوهای نحوی جامع، جداول و جدول‌های متا، کوروتین‌ها و فلسفه طراحی منحصربه‌فرد Lua تکمیل می‌کند.
---

## اپراتورها و عبارات
### اپراتورهای اصلی
| اپراتور | نام | مثال | یادداشت ها |
|----------|------|---------|-------|
| `+``-``*``/``%``^` | حسابی | `2 ^ 10`| `^`قدرت است |
| `//`| تقسیم طبقات | `7 // 2`| بازگشت 3 (Lua 5.3+) |
| `==``~=` | برابری | `a == b`| `~=`"برابر نیست" |
| `<``>``<=``>=` | مقایسه | `a >= b`| |
| `and``or``not`| منطقی | `a and b`| عملوندها را برمی گرداند، نه بولی ها |
| `..`| الحاق | `"hello" .. " world"`| |
| `#`| طول | `#t`| طول رشته یا میز |
| `&``\|``~``<<``>>`| بیتی | `a & b`| Lua 5.3+ (عملیات عدد صحیح) |
### عملگرهای منطقی - بازده غیر بولی
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

### اولویت (بیشترین به کمترین)
| تقدم | اپراتورها |
|------------|-----------|
| 1 (بالاترین) | `^`|
| 2 | `not``#``-`(یوناری) |
| 3 | `*``/``//``%` |
| 4 | `+``-` |
| 5 | `..`(راست انجمنی) |
| 6 | `<<``>>` |
| 7 | `&`|
| 8 | `~`(XOR باینری) |
| 9 | `\|`|
| 10 | `==``~=``<``>``<=``>=` |
| 11 | `and`|
| 12 (کمترین) | `or`|
---

## جریان را کنترل کنید
### شرایط
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

### حلقه ها
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

## جداول - ساختار داده جهانی
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

## توابع
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

## Metatables و Metamethods
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

## ماژول ها و مدیریت خطا
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

## روتین ها
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

## الگوهای رشته (جایگزین Regex Lua)
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

## خلاصه
نحو Lua عمدا حداقل است - کل زبان را می توان در یک صفحه توصیف کرد. جداول به عنوان ساختار داده جهانی (آرایه ها، فرهنگ لغت، اشیا، ماژول ها) عمل می کنند. Metatable ها توسعه پذیری را بدون پیچیدگی زبان ارائه می دهند. برنامه‌های کاری چندوظیفه‌ای مشترک و الگوهای تکرارکننده ظریف را امکان‌پذیر می‌کنند. قدرت این زبان از قابلیت جاسازی آن ناشی می‌شود: Lua برای زندگی در داخل برنامه‌های میزبان طراحی شده است و قابلیت‌های اسکریپت نویسی با حداقل هزینه را ارائه می‌کند. برای توسعه بازی، پیکربندی و سیستم‌های تعبیه‌شده، سادگی Lua بزرگ‌ترین نقطه قوت آن است – یک زبان کوچک که دقیقاً همان چیزی را که نیاز دارد انجام می‌دهد و نه بیشتر.