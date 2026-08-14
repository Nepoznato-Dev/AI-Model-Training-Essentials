---
# Metadata
title: "Lua — Cheat Sheet"
description: "Quick-reference cheat sheet for Lua syntax, tables, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [lua, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# لوا - ورقة الغش
## الأساسيات
```lua
-- Variables
local name = "Alice"       -- always use local!
local age = 30
local pi = 3.14159
local active = true
local nothing = nil

-- Types
type(name)        -- "string"
type(42)          -- "number"
type(true)        -- "boolean"
type(nil)         -- "nil"
type({})          -- "table"
type(print)       -- "function"

-- Strings
"Hello, " .. name           -- concatenation
#name                       -- length
string.upper(name)          -- "ALICE"
string.lower(name)          -- "alice"
string.len(name)            -- 5
string.sub(name, 1, 3)     -- "Ali"
string.find(name, "lic")   -- 2, 4
string.gsub(name, "Alice", "Bob")
string.format("Hello, %s!", name)
string.rep("ha", 3)         -- "hahaha"
string.reverse("hello")     -- "olleh"
tostring(42)
tonumber("42")

-- String interpolation (Lua 5.4+ not native, use format)
string.format("Hello, %s! Age: %d", name, age)
```

## الجداول
```lua
-- Array-like table
local arr = {1, 2, 3}
arr[1]              -- 1 (1-indexed!)
#arr                -- 3
table.insert(arr, 4)
table.insert(arr, 1, 0)  -- insert at position 1
table.remove(arr)        -- remove last
table.remove(arr, 1)     -- remove at position
table.sort(arr)
table.concat(arr, ", ")

-- Dictionary-like table
local user = {name = "Alice", age = 30}
user.name             -- "Alice"
user["name"]          -- "Alice"
user.email = "a@b.com"
user.phone            -- nil

-- Mixed table
local data = {
    [1] = "first",
    [2] = "second",
    name = "Alice",
    ["key with spaces"] = 42,
}

-- Table as module
local M = {}
function M.greet(name)
    return "Hello, " .. name
end
return M
```

## التحكم في التدفق
```lua
if condition then
    -- ...
elseif other then
    -- ...
else
    -- ...
end

-- Ternary (Lua idiom)
local result = condition and "yes" or "no"

-- Loops
for i = 1, 10 do
    print(i)
end

for i = 10, 1, -1 do  -- step -1
    print(i)
end

for i, v in ipairs(arr) do
    print(i, v)
end

for k, v in pairs(user) do
    print(k, v)
end

while condition do
    -- ...
end

repeat
    -- ...
until condition

-- Break
for i = 1, 100 do
    if i > 10 then break end
end
```

## الوظائف
```lua
-- Basic function
local function add(a, b)
    return a + b
end

-- Multiple return values
local function divide(a, b)
    if b == 0 then return nil, "division by zero" end
    return a / b
end
local result, err = divide(10, 0)

-- Variadic
local function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end

-- Closures
local function counter()
    local n = 0
    return function()
        n = n + 1
        return n
    end
end
local inc = counter()
inc()  -- 1
inc()  -- 2

-- Table as function
local t = setmetatable({}, {
    __call = function(self, x) return x * 2 end
})
t(5)  -- 10
```

## الجداول التعريفية و OOP
```lua
-- Metatable
local mt = {
    __tostring = function(self)
        return self.name .. " (" .. self.age .. ")"
    end,
    __index = function(self, key)
        return "default"
    end,
    __newindex = function(self, key, value)
        rawset(self, key, value)
    end,
}

-- Class pattern
local Animal = {}
Animal.__index = Animal

function Animal.new(name, sound)
    local self = setmetatable({}, Animal)
    self.name = name
    self.sound = sound
    return self
end

function Animal:speak()
    return self.name .. " says " .. self.sound
end

-- Inheritance
local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
    return Animal.new(name, "Woof")
end
```

## الوحدات ومعالجة الأخطاء
```lua
-- Module
-- mymodule.lua
local M = {}
function M.hello() print("Hello!") end
return M

-- Require
local mymod = require("mymodule")
mymod.hello()

-- pcall (protected call)
local ok, err = pcall(function()
    error("something failed")
end)
if not ok then
    print("Error: " .. err)
end

-- xpcall (with error handler)
local ok, err = xpcall(function()
    error("fail")
end, debug.traceback)

-- error()
error("message", level)
assert(condition, "error message")
```

## الأنماط الشائعة
```lua
-- Safe navigation
local city = user and user.address and user.address.city

-- Default values
local value = input or "default"

-- Unpacking
local a, b, c = table.unpack({1, 2, 3})

-- String split
local function split(str, sep)
    local result = {}
    for word in str:gmatch("([^" .. sep .. "]+)") do
        table.insert(result, word)
    end
    return result
end

-- Shallow copy
local function copy(t)
    local result = {}
    for k, v in pairs(t) do result[k] = v end
    return result
end
```
