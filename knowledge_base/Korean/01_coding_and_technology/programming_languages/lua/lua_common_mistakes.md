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

# Lua — 일반적인 실수 및 안티 패턴
이 문서는 Lua에서 가장 흔히 발생하는 실수, 함정, 안티패턴을 수정 사항과 함께 나열합니다.
---

## 1. 1 기반 인덱싱
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

## 2.`nil`대`false`조건
```lua
-- ❌ WRONG — assuming 0 is falsy
if 0 then
    print("0 is truthy in Lua!")  -- this runs
end

-- In Lua, only nil and false are falsy
-- Everything else (0, "", empty table) is truthy
```

---

## 3. 테이블 참조 의미론
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

## 4. 기본적으로 전역 변수
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

## 5.`pairs`대 `ipairs`
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

## 6. 루프의 문자열 연결
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

## 7. OOP에 메타테이블을 사용하지 않음
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

## 요약
Lua의 미니멀리즘은 함정을 만듭니다. 1 기반 인덱싱,`nil`및 `false`만 거짓이고, 테이블은 참조(값 아님)이고, 변수는 기본적으로 전역적이며, `pairs`는 순서가 없지만 `ipairs`는 순서가 지정되지 않습니다. Lua 방식은 항상 `local`를 사용하고, 배열에는 `ipairs`를, 사전에는 `pairs`를 사용하고, 문자열 작성에는 `table.concat`를 사용하고, OOP에는 메타테이블을 사용하는 것입니다. Lua의 단순성은 그 힘입니다. 하지만 극단적인 경우를 존중하세요.