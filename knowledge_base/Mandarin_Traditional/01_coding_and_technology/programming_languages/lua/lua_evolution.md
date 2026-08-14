<!--
---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lua, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Lua — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 1.0 | 1994 |初始版本（巴西里約 PUC）|
| 2.1 | 2.1 1995 |表成為唯一的資料結構|
| 3.0 | 1997 | C API，標記方法（早期元方法）|
| 3.1| 1998 |語意控制器（上位數）|
| 4.0 | 2000 | 2000 **Lua 4**：引用計數+ GC，改進的C API |
| 5.0 | 2003 | **主要**：正確的詞法範圍、協程、元表、布林值 |
| 5.1 | 2006 | **增量 GC**、`#` 長度運算子、`goto` 已刪除、`module()` |
| 5.2 | 5.2 2011 |`_ENV`、`_G`變更、`goto` 新增回來、星曆表 |
| 5.3 | 2015 | 2015 **整數類型**、位元運算子、UTF-8 支援 |
| 5.4 | 5.4 2020 | **分代 GC**、`const` /`close`變數、`tostring` 元方法 |
| 5.4.x | 2020–25 |漸進改進、預警系統|
| 5.5 | 5.5待定 | （未來）進一步的 GC 改進 |
## 主要里程碑
### Lua 1–3：早年（1994–1999）
- **1994**：由 Roberto Ierusalimschy、Waldemar Celes、Luiz Henrique de Figueiredo 在 PUC-Rio（裡約熱內盧天主教大學）創建
- **目標**：用於資料輸入的嵌入式腳本語言（不是獨立語言）
- **2.1**：表格成為唯一的資料結構－極為簡單
- **3.0**：C API 固化 — 使 Lua 可嵌入到 C/C++ 應用程式中
- **3.1**：Upvalues — 閉包的詞法作用域
### Lua 4：成熟 (2000)
- 引用數+垃圾收集（混合）
- 改進的 C API —`luaL_*`輔助庫
- 仍然沒有適當的全域詞法範圍
### Lua 5.0：現代 Lua (2003)
- **正確的詞法範圍** —`local`變量
- **協程** — 協作多工處理
- **元表** — 運算子重載、自訂行為
- **布林值** —`true`/`false`作為正確值
- **關閉**做得正確 - 普遍升值
- 這是讓Lua在遊戲中廣泛採用的版本
### Lua 5.1：標準 (2006)
- **增量垃圾收集器**
-`#`長度運算符
- `module()`功能
- 改變了全球環境的運作方式
- **此版本成為最廣泛嵌入的版本**（LuaJIT 目標為 5.1）
### Lua 5.2：改進（2011）
-`_ENV`— 每個區塊環境（更乾淨的全域變數）
-`goto`語句傳回
- Ephemeron 表（GC 改進）
- 軟體包系統改進
### Lua 5.3：整數和位元 (2015)
- **整數子類型** — 與浮點數不同
- **位元運算子** — `&`、`|`、`~`、`<<`、`>>`
- **UTF-8 支援** — 內建`utf8`庫
- 地板劃分`//`
- 二進位資料的字串`pack`/ `unpack`
### Lua 5.4：分代GC（2020）
- **分代垃圾收集器** - 更好的 GC 暫停
- **`<const>`變數** — 真正的常數
- **`<close>`變數** — 待關閉變數（資源管理，如`defer`或`with`）
-`tostring`元方法
- 字串子類型（短字串和長字串的最佳化方式不同）
## 語法演變
```lua
-- Lua 4.0: No local scoping for globals
x = 10  -- always global unless in a function

-- Lua 5.0: Proper lexical scoping
local x = 10  -- local to block
do
  local y = 20
  print(x + y)  -- 30
end

-- Lua 5.1: Length operator, module
local t = {1, 2, 3}
print(#t)  -- 3
module("mymodule", package.seeall)

-- Lua 5.3: Integer type, bitwise
local a = 10    -- integer
local b = 10.0  -- float
print(a & 0xFF) -- bitwise AND: 10
print(a >> 1)   -- right shift: 5

-- Lua 5.4: const and close variables
local x <const> = 42  -- constant, cannot change
local f <close> = io.open("file.txt")  -- auto-closed at scope end
```

## 功能演變
```
Lua 1.0:  Tables, functions, strings, numbers, C API
Lua 2.1:  Tables as only data structure
Lua 3.0:  Tag methods (predecessor to metatables)
Lua 3.1:  Upvalues (closures)
Lua 4.0:  Hybrid GC (ref counting + cycle collection)
Lua 5.0:  Coroutines, metatables, proper lexical scoping, booleans
Lua 5.1:  Incremental GC, # operator, module()
Lua 5.2:  _ENV, goto, ephemeron tables
Lua 5.3:  Integer type, bitwise ops, UTF-8, //, pack/unpack
Lua 5.4:  Generational GC, <const>, <close>, tostring metamethod
```

## Lua 在遊戲中的應用
```
1997: LucasArts uses Lua in game scripting (Grim Fandango)
2003: Lua 5.0 — game industry adoption accelerates
2005: World of Warcraft uses Lua for UI addons
2006: LuaJIT (Mike Pall) — JIT-compiled Lua 5.1, extremely fast
2010: Love2D game framework (Lua-based)
2012: Defold game engine (Lua scripting)
2015: Roblox adopts Luau (Lua dialect with types)
2020: Lua 5.4 — continued game engine integration
2025: Lua remains the #1 embedded scripting language in games
       Used in: Unity (via plugins), WoW, Garry's Mod, Factorio,
       Civilization, Adobe Lightroom, Nginx (OpenResty), Redis
```

## 關鍵設計原則
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## 生態系成長
```
1994: Lua created at PUC-Rio (Brazil)
1997: First game industry use (LucasArts)
2003: Lua 5.0 — widespread game adoption
2005: LuaJIT — JIT-compiled Lua
2006: Lua 5.1 — the "standard" embedded version
2010: OpenResty (Nginx + Lua) — web development
2015: Luau (Roblox) — typed Lua dialect
2020: Lua 5.4 — modern GC, resource management
2025: Lua is the dominant embedded scripting language
       Powers: games, Nginx, Redis, Wireshark, Lightroom, more
```
