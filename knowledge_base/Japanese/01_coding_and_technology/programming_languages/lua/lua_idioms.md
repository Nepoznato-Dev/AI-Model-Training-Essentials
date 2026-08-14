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
# Lua — 慣用的なパターンとベストプラクティス
このガイドでは、クリーンで慣用的な Lua コードを記述するための慣用的なパターンとベスト プラクティスについて説明します。
---

## テーブルとデータ
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

## 関数
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

## メタテーブルを使用した OOP
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

## エラー処理
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

## 反復
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

## モジュール
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

＃＃ まとめ
Lua のイディオムは、ユニバーサル データ構造としてのテーブル、ローカル変数、状態のクロージャ、OOP のメタテーブル、および 1 ベースのインデックスを強調します。 lint については luacheck に従い、フォーマットについては stylua に従ってください。 Lua はシンプルさとミニマリズムを重視します。言語は意図的に小さいため、構成からパターンが現れます。