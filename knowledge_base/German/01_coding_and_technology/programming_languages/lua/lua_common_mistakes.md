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
# Lua – Häufige Fehler und Anti-Patterns
Dieses Dokument katalogisiert die häufigsten Fehler, Fallstricke und Anti-Patterns in Lua mit Korrekturen.
---

## 1. 1-basierte Indizierung
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

## 2.`nil`vs.`false`in Bedingungen
```lua
-- ❌ WRONG — assuming 0 is falsy
if 0 then
    print("0 is truthy in Lua!")  -- this runs
end

-- In Lua, only nil and false are falsy
-- Everything else (0, "", empty table) is truthy
```

---

## 3. Tabellenreferenzsemantik
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

## 4. Globale Variablen standardmäßig
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

## 5.`pairs`vs. `ipairs`
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

## 6. String-Verkettung in Schleifen
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

## 7. Keine Verwendung von Metatabellen für OOP
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

## Zusammenfassung
Luas Minimalismus schafft Fallen: 1-basierte Indizierung, nur`nil`und`false`sind falsch, Tabellen sind Referenzen (keine Werte), Variablen sind standardmäßig global und`pairs`ist ungeordnet, während`ipairs`geordnet ist. Der Lua-Weg ist: Verwenden Sie immer `local`, verwenden Sie`ipairs`für Arrays und`pairs`für Wörterbücher, verwenden Sie`table.concat`für die Zeichenfolgenerstellung und verwenden Sie Metatabellen für OOP. Luas Einfachheit ist seine Stärke – aber respektieren Sie die Randfälle.