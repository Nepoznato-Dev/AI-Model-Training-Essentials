---
# Metadata
title: "Lua — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Lua with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# লুয়া — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ লুয়াতে সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1. 1-ভিত্তিক ইন্ডেক্সিং
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

## 2. শর্তে`nil`বনাম `false`
```lua
-- ❌ WRONG — assuming 0 is falsy
if 0 then
    print("0 is truthy in Lua!")  -- this runs
end

-- In Lua, only nil and false are falsy
-- Everything else (0, "", empty table) is truthy
```

---

## 3. টেবিল রেফারেন্স শব্দার্থবিদ্যা
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

## 4. ডিফল্টরূপে গ্লোবাল ভেরিয়েবল
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

## 5.`pairs`বনাম `ipairs`
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

## 6. লুপগুলিতে স্ট্রিং সংযোগ
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

## 7. OOP-এর জন্য Metatables ব্যবহার করছেন না
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

## সারাংশ
লুয়ার মিনিমালিজম ফাঁদ তৈরি করে: 1-ভিত্তিক সূচীকরণ, শুধুমাত্র`nil`এবং`false`মিথ্যা, টেবিলগুলি রেফারেন্স (মান নয়), ভেরিয়েবলগুলি ডিফল্টরূপে বিশ্বব্যাপী, এবং`pairs`অপরিবর্তিত যখন XQZMARKER3 ক্রমানুসারে। লুয়ার উপায় হল: সর্বদা`local`ব্যবহার করুন, অ্যারেগুলির জন্য`ipairs`এবং অভিধানগুলির জন্য`pairs`ব্যবহার করুন, স্ট্রিং বিল্ডিংয়ের জন্য`table.concat`ব্যবহার করুন এবং OOP-এর জন্য মেটাটেবল ব্যবহার করুন৷ লুয়ার সরলতা হল এর ক্ষমতা — তবে প্রান্তের ক্ষেত্রে সম্মান করুন।