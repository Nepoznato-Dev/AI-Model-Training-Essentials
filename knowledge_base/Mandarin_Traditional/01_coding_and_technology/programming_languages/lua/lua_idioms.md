---
# Metadata
title: "Lua — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Lua code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Lua — 慣用模式與最佳實踐
本指南涵蓋了編寫乾淨、慣用的 Lua 程式碼的慣用模式和最佳實踐。
---

## 表格和數據
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

## 函數
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

## OOP 與元表
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

## 錯誤處理
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

## 迭代
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

## 模組
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

＃＃ 概括
Lua 慣用語強調：表格作為通用資料結構、局部變數、狀態閉包、OOP 元表以及基於 1 的索引。依照 luacheck 進行 linting，依照 stylua 進行格式化。 Lua 重視簡單性和極簡主義——語言故意很小，因此模式是從組合中顯現出來的。