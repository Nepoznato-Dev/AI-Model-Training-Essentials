<!--
---
# Metadata
title: "Lua — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Lua code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [lua, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Lua — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔하고 관용적인 Lua 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 테이블 및 데이터
```lua
-- ✅ Table constructors
local user = { name = "Alice", email = "alice@example.com", age = 30 }

-- ✅ Array-like tables (1-indexed!)
local items = { "first", "second", "third" }

-- ✅ Table length
local count = #items

-- ✅ Nested tables
local config = {
  server = { host = "localhost", port = 8080 },
  database = { name = "mydb" },
}

-- ✅ Table unpacking
local first, second = items[1], items[2]
```

---

## 기능
```lua
-- ✅ Local functions
local function helper(x)
    return x * 2
end

-- ✅ Multiple return values
local function divide(a, b)
    if b == 0 then return nil, "division by zero" end
    return a / b
end

local result, err = divide(10, 0)
if not result then print("Error:", err) end

-- ✅ Varargs
local function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end

-- ✅ Closures for state
local function counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

local inc = counter()
print(inc()) -- 1
print(inc()) -- 2
```

---

## 메타테이블을 사용한 OOP
```lua
-- ✅ Class pattern with metatables
local User = {}
User.__index = User

function User.new(name, email)
    local self = setmetatable({}, User)
    self.name = name
    self.email = email
    return self
end

function User:greet()
    return "Hello, I'm " .. self.name
end

-- ✅ Inheritance
local Admin = setmetatable({}, { __index = User })
Admin.__index = Admin

function Admin.new(name, email, role)
    local self = User.new(name, email)
    setmetatable(self, Admin)
    self.role = role
    return self
end
```

---

## 오류 처리
```lua
-- ✅ pcall for protected calls
local ok, result = pcall(function()
    return risky_operation()
end)

if not ok then
    print("Error:", result)
end

-- ✅ xpcall for error handlers
local ok, err = xpcall(function()
    error("something went wrong")
end, debug.traceback)

-- ✅ assert for preconditions
local file = assert(io.open("data.txt", "r"))
```

---

## 반복
```lua
-- ✅ ipairs for arrays (sequential)
for i, value in ipairs(items) do
    print(i, value)
end

-- ✅ pairs for tables (all keys)
for key, value in pairs(config) do
    print(key, value)
end

-- ✅ Numeric for
for i = 1, 10 do
    print(i)
end

-- ✅ Generic for with custom iterator
for line in io.lines("file.txt") do
    process(line)
end
```

---

## 모듈
```lua
-- ✅ Module pattern
local M = {}

function M.process(input)
    return input:upper()
end

M.VERSION = "1.0.0"

return M

-- ✅ Usage
local mymodule = require("mymodule")
print(mymodule.process("hello"))
```

---

## 요약
Lua 관용구는 범용 데이터 구조로서의 테이블, 지역 변수, 상태에 대한 클로저, OOP에 대한 메타테이블 및 1 기반 인덱싱을 강조합니다. 보푸라기에는 luacheck를 따르고 서식 지정에는 styua를 따르십시오. Lua는 단순성과 미니멀리즘을 중요하게 생각합니다. 언어는 의도적으로 작기 때문에 구성에서 패턴이 나타납니다.