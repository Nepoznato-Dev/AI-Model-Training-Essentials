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
# লুয়া — ইডিওম্যাটিক প্যাটার্ন এবং সর্বোত্তম অভ্যাস
এই নির্দেশিকাটি পরিচ্ছন্ন, ইডিওম্যাটিক লুয়া কোড লেখার জন্য বাহাদুরি প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## টেবিল এবং ডেটা
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

## ফাংশন
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

## মেটাটেবল সহ OOP
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

## ত্রুটি হ্যান্ডলিং
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

## পুনরাবৃত্তি
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

## মডিউল
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

## সারাংশ
লুয়া ইডিয়মগুলি জোর দেয়: সার্বজনীন ডেটা স্ট্রাকচার, স্থানীয় ভেরিয়েবল, রাষ্ট্রের জন্য বন্ধ, OOP-এর জন্য মেটাটেবল এবং 1-ভিত্তিক সূচী হিসাবে টেবিলগুলি। লিন্টিং এর জন্য luacheck এবং বিন্যাস করার জন্য stylua অনুসরণ করুন। লুয়া সরলতা এবং ন্যূনতমতাকে মূল্য দেয় — ভাষাটি ইচ্ছাকৃতভাবে ছোট, তাই রচনা থেকে নিদর্শনগুলি উদ্ভূত হয়।