---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Lua — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| 1.0 | 1994 |初始版本（巴西里约 PUC）|
| 2.1 | 2.1 1995 |表成为唯一的数据结构|
| 3.0 | 1997 | C API，标记方法（早期元方法）|
| 3.1| 1998 |语义控制器（上值）|
| 4.0 | 2000 | 2000 **Lua 4**：引用计数+ GC，改进的C API |
| 5.0 | 2003 | **主要**：正确的词法范围、协程、元表、布尔值 |
| 5.1 | 2006 | **增量 GC**、`#` 长度运算符、`goto` 已删除、`module()` |
| 5.2 | 5.2 2011 | `_ENV`、`_G`更改、`goto` 添加回来、星历表 |
| 5.3 | 2015 | 2015 **整数类型**、按位运算符、UTF-8 支持 |
| 5.4 | 5.4 2020 | **分代 GC**、`const` /`close`变量、`tostring` 元方法 |
| 5.4.x | 2020–25 |增量改进、预警系统|
| 5.5 | 5.5待定 | （未来）进一步的 GC 改进 |
## 主要里程碑
### Lua 1–3：早年（1994–1999）
- **1994**：由 Roberto Ierusalimschy、Waldemar Celes、Luiz Henrique de Figueiredo 在 PUC-Rio（里约热内卢天主教大学）创建
- **目标**：用于数据输入的嵌入式脚本语言（不是独立语言）
- **2.1**：表成为唯一的数据结构——极其简单
- **3.0**：C API 固化 — 使 Lua 可嵌入到 C/C++ 应用程序中
- **3.1**：Upvalues — 闭包的词法作用域
### Lua 4：成熟 (2000)
- 引用计数+垃圾收集（混合）
- 改进的 C API —`luaL_*`辅助库
- 仍然没有适当的全局词法范围
### Lua 5.0：现代 Lua (2003)
- **正确的词法范围** —`local`变量
- **协程** — 协作多任务处理
- **元表** — 运算符重载、自定义行为
- **布尔值** —`true`/`false`作为正确值
- **关闭**做得正确 - 普遍升值
- 这是让Lua在游戏中广泛采用的版本
### Lua 5.1：标准 (2006)
- **增量垃圾收集器**
-`#`长度运算符
- `module()`功能
- 改变了全球环境的运作方式
- **该版本成为最广泛嵌入的版本**（LuaJIT 目标为 5.1）
### Lua 5.2：改进（2011）
-`_ENV`— 每个块环境（更干净的全局变量）
-`goto`语句返回
- Ephemeron 表（GC 改进）
- 软件包系统改进
### Lua 5.3：整数和位 (2015)
- **整数子类型** — 与浮点数不同
- **按位运算符** — `&`、`|`、`~`、`<<`、`>>` 
- **UTF-8 支持** — 内置`utf8`库
- 地板划分`//` 
- 二进制数据的字符串`pack`/ `unpack`
### Lua 5.4：分代GC（2020）
- **分代垃圾收集器** - 更好的 GC 暂停
- **`<const>`变量** — 真正的常量
- **`<close>`变量** — 待关闭变量（资源管理，如`defer`或`with`）
-`tostring`元方法
- 字符串子类型（短字符串和长字符串的优化方式不同）
## 语法演变
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

## 功能演变
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

## Lua 在游戏中的应用
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

## 关键设计原则
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## 生态系统增长
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
