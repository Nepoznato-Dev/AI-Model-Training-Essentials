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
# Lua — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| 1.0     | 1994 | Initial release (PUC-Rio, Brazil) |
| 2.1     | 1995 | Tables become the only data structure |
| 3.0     | 1997 | C API, tag methods (early metamethods) |
| 3.1     | 1998 | Semantic controllers (upvalues) |
| 4.0     | 2000 | **Lua 4**: ref-counting + GC, improved C API |
| 5.0     | 2003 | **Major**: proper lexical scoping, coroutines, metatables, Booleans |
| 5.1     | 2006 | **Incremental GC**, `#` length operator, `goto` removed, `module()` |
| 5.2     | 2011 | `_ENV`, `_G` changes, `goto` added back, ephemeron tables |
| 5.3     | 2015 | **Integer type**, bitwise operators, UTF-8 support |
| 5.4     | 2020 | **Generational GC**, `const`/`close` variables, `tostring` metamethod |
| 5.4.x   | 2020–25 | Incremental improvements, warning system |
| 5.5     | TBD  | (future) Further GC improvements |

## Major Milestones

### Lua 1–3: The Early Years (1994–1999)
- **1994**: Created at PUC-Rio (Pontifical Catholic University of Rio de Janeiro) by Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Goal**: Embeddable scripting language for data entry (not a standalone language)
- **2.1**: Tables become the sole data structure — radical simplicity
- **3.0**: C API solidified — makes Lua embeddable in C/C++ applications
- **3.1**: Upvalues — lexical scoping for closures

### Lua 4: Maturation (2000)
- Reference counting + garbage collection (hybrid)
- Improved C API — `luaL_*` auxiliary library
- Still no proper lexical scoping for globals

### Lua 5.0: Modern Lua (2003)
- **Proper lexical scoping** — `local` variables
- **Coroutines** — cooperative multitasking
- **Metatables** — operator overloading, custom behavior
- **Booleans** — `true`/`false` as proper values
- **Closures** done right — upvalues generalized
- This is the version that made Lua widely adopted in games

### Lua 5.1: The Standard (2006)
- **Incremental garbage collector**
- `#` length operator
- `module()` function
- Changed how global environment works
- **This version becomes the most widely embedded version** (LuaJIT targets 5.1)

### Lua 5.2: Refinements (2011)
- `_ENV` — per-chunk environment (cleaner globals)
- `goto` statement returns
- Ephemeron tables (GC improvement)
- Package system improvements

### Lua 5.3: Integer & Bits (2015)
- **Integer subtype** — distinct from float
- **Bitwise operators** — `&`, `|`, `~`, `<<`, `>>`
- **UTF-8 support** — built-in `utf8` library
- Floor division `//`
- String `pack`/`unpack` for binary data

### Lua 5.4: Generational GC (2020)
- **Generational garbage collector** — much better GC pauses
- **`<const>` variables** — true constants
- **`<close>` variables** — to-be-closed variables (resource management, like `defer` or `with`)
- `tostring` metamethod
- String subtypes (short vs. long strings optimized differently)

## Syntax Evolution

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

## Feature Evolution

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

## Lua in Gaming

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

## Key Design Principles

```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Ecosystem Growth

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
