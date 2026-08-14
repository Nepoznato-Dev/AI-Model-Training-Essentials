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
# Lua — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| 1.0 | 1994 | Paunang release (PUC-Rio, Brazil) |
| 2.1 | 1995 | Ang mga talahanayan ay naging ang tanging istraktura ng data |
| 3.0 | 1997 | C API, mga pamamaraan ng tag (mga maagang metamethod) |
| 3.1 | 1998 | Mga semantic controller (mga upvalue) |
| 4.0 | 2000 | **Lua 4**: ref-counting + GC, pinahusay na C API |
| 5.0 | 2003 | **Major**: wastong lexical scoping, coroutines, metatables, Booleans |
| 5.1 | 2006 | **Incremental GC**,`#`haba operator,`goto`inalis,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`pagbabago,`goto`idinagdag pabalik, ephemeron tables |
| 5.3 | 2015 | **Integer type**, bitwise operators, UTF-8 support |
| 5.4 | 2020 | **Generational GC**,`const`/`close`na mga variable,`tostring`metamethod |
| 5.4.x | 2020–25 | Mga karagdagang pagpapabuti, sistema ng babala |
| 5.5 | TBD | (kinabukasan) Karagdagang pagpapabuti ng GC |
## Mga Pangunahing Milestone
### Lua 1–3: Ang Mga Unang Taon (1994–1999)
- **1994**: Nilikha sa PUC-Rio (Pontifical Catholic University of Rio de Janeiro) ni Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Layunin**: Nai-embed na scripting language para sa data entry (hindi isang standalone na wika)
- **2.1**: Nagiging nag-iisang istruktura ng data ang mga talahanayan — radikal na pagiging simple
- **3.0**: Pinatibay ng C API — ginagawang na-embed ang Lua sa mga C/C++ na application
- **3.1**: Mga upvalue — lexical scoping para sa mga pagsasara
### Lua 4: Pagkahinog (2000)
- Pagbibilang ng reference + koleksyon ng basura (hybrid)
- Pinahusay na C API —`luaL_*`auxiliary library
- Wala pa ring wastong lexical scoping para sa mga global
### Lua 5.0: Makabagong Lua (2003)
- **Tamang lexical scoping** —`local`variable
- **Coroutine** — cooperative multitasking
- **Metatables** — overloading ng operator, custom na gawi
- **Booleans** —`true`/`false`bilang mga wastong halaga
- **Ang mga pagsasara** ay ginawa nang tama — ang mga upvalue ay pangkalahatan
- Ito ang bersyon na ginawa Lua malawak na pinagtibay sa mga laro
### Lua 5.1: The Standard (2006)
- **Incremental na kolektor ng basura**
- Operator sa haba ng `#`
-`module()`function
- Binago kung paano gumagana ang pandaigdigang kapaligiran
- **Ang bersyon na ito ay naging ang pinakalawak na naka-embed na bersyon** (LuaJIT target 5.1)
### Lua 5.2: Mga Pagpipino (2011)
-`_ENV`— per-chunk environment (mas malinis na globals)
- Nagbabalik ang`goto`statement
- Mga talahanayan ng Ephemeron (pagpapabuti ng GC)
- Mga pagpapahusay ng sistema ng package
### Lua 5.3: Integer & Bits (2015)
- **Integer subtype** — naiiba sa float
- **Bitwise operator** —`&`,`|`,`~`,`<<`,`>>`
- **Suporta sa UTF-8** — built-in na`utf8`library
- Floor division`//`
- String`pack`/`unpack`para sa binary data
### Lua 5.4: Generational GC (2020)
- **Generational garbage collector** — mas magandang pag-pause ng GC
- **`<const>`variable** — totoong mga constant
- **`<close>`variable** — to-be-closed variable (resource management, tulad ng`defer`o`with`)
-`tostring`metamethod
- Mga subtype ng string (maikli vs. mahahabang string na na-optimize nang iba)
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

## Ebolusyon ng Tampok
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

## Lua sa Paglalaro
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Paglago ng Ecosystem
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
