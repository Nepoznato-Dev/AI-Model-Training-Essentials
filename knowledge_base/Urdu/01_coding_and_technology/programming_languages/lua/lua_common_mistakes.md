<!--
---
# Metadata
title: "Lua — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Lua with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [lua, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Lua — عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز تصحیح کے ساتھ Lua میں سب سے عام غلطیوں، ٹریپس، اور مخالف پیٹرن کی فہرست بناتی ہے۔
---

## 1. 1-بیسڈ انڈیکسنگ
```lua
-- ❌ WRONG — expecting 0-based indexing
local arr = {"a", "b", "c"}
print(arr[0])  -- nil!
print(arr[1])  -- "a"

-- ✅ CORRECT — Lua arrays are 1-indexed
for i = 1, #arr do
    print(arr[i])
end
```

---

## 2.`nil`بمقابلہ`false`شرائط میں
```lua
-- ❌ WRONG — assuming 0 is falsy
if 0 then
    print("0 is truthy in Lua!")  -- this runs
end

-- In Lua, only nil and false are falsy
-- Everything else (0, "", empty table) is truthy
```

---

## 3. ٹیبل ریفرنس سیمنٹکس
```lua
-- ❌ WRONG — expecting value copy
local a = {1, 2, 3}
local b = a
b[1] = 99
print(a[1])  -- 99! (same table)

-- ✅ CORRECT — explicit deep copy
local function deep_copy(orig)
    local copy = {}
    for k, v in pairs(orig) do
        if type(v) == "table" then
            copy[k] = deep_copy(v)
        else
            copy[k] = v
        end
    end
    return copy
end

local b = deep_copy(a)
```

---

## 4. عالمی متغیرات بذریعہ ڈیفالٹ
```lua
-- ❌ WRONG — accidentally creating globals
function process()
    result = compute()  -- global variable!
end

-- ✅ CORRECT — always use local
function process()
    local result = compute()
end

-- ✅ CORRECT — strict mode at top of file
setmetatable(_G, {
    __newindex = function(_, k)
        error("Attempt to create global: " .. k)
    end
})
```

---

## 5.`pairs`بمقابلہ `ipairs`
```lua
-- ❌ WRONG — using pairs for array iteration
local arr = {"a", "b", "c"}
for k, v in pairs(arr) do  -- unordered!
    print(k, v)
end

-- ✅ CORRECT — ipairs for arrays (ordered)
for i, v in ipairs(arr) do
    print(i, v)
end

-- ✅ CORRECT — pairs for dictionaries
local dict = {name = "Alice", age = 30}
for k, v in pairs(dict) do
    print(k, v)
end
```

---

## 6. لوپس میں سٹرنگ کنکٹنیشن
```lua
-- ❌ WRONG — O(n²) concatenation
local result = ""
for i = 1, 1000 do
    result = result .. "x"
end

-- ✅ CORRECT — use table.concat
local parts = {}
for i = 1, 1000 do
    parts[#parts + 1] = "x"
end
local result = table.concat(parts)
```

---

## 7. OOP کے لیے میٹا ٹیبلز کا استعمال نہیں کرنا
```lua
-- ❌ WRONG — manual method passing
local obj = { value = 42 }
local function get_value(self)
    return self.value
end
get_value(obj)

-- ✅ CORRECT — metatables for OOP
local MyClass = {}
MyClass.__index = MyClass

function MyClass.new(value)
    local self = setmetatable({}, MyClass)
    self.value = value
    return self
end

function MyClass:getValue()
    return self.value
end

local obj = MyClass.new(42)
print(obj:getValue())  -- 42
```

---

## خلاصہ
Lua کی minimalism ٹریپس بناتی ہے: 1 پر مبنی اشاریہ سازی، صرف`nil`اور`false`غلط ہیں، میزیں حوالہ جات ہیں (قدریں نہیں)، متغیرات پہلے سے طے شدہ طور پر عالمی ہیں، اور`pairs`غیر ترتیب شدہ ہے جبکہ`pairs`کو ترتیب دیا گیا ہے۔ Lua طریقہ یہ ہے: ہمیشہ`local`استعمال کریں، اریوں کے لیے`ipairs`اور لغات کے لیے`pairs`استعمال کریں، سٹرنگ بنانے کے لیے`table.concat`استعمال کریں، اور OOP کے لیے میٹا ٹیبل استعمال کریں۔ Lua کی سادگی اس کی طاقت ہے — لیکن کنارے کے معاملات کا احترام کریں۔