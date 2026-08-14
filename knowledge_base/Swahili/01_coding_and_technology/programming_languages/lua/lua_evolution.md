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
# Lua - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| 1.0 | 1994 | Toleo la kwanza (PUC-Rio, Brazili) |
| 2.1 | 1995 | Majedwali huwa muundo pekee wa data |
| 3.0 | 1997 | C API, mbinu tag (mbinu za mapema) |
| 3.1 | 1998 | Vidhibiti vya kisemantiki (maadili bora) |
| 4.0 | 2000 | **Lua 4**: kuhesabu upya + GC, API ya C iliyoboreshwa |
| 5.0 | 2003 | **Kubwa**: upeo sahihi wa kileksika, ratibu, metatable, Booleans |
| 5.1 | 2006 | **GC ya Ziada**, mwendeshaji urefu wa `#`,`goto`imeondolewa,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`mabadiliko,`goto`imeongezwa nyuma, meza za ephemeron |
| 5.3 | 2015 | **Aina kamili**, waendeshaji kwa busara kidogo, usaidizi wa UTF-8 |
| 5.4 | 2020 | **Vigezo vya GC vya Kizazi**,`const`/`close`vigezo, mbinu ya`tostring`|
| 5.4.x | 2020–25 | Maboresho ya kuongezeka, mfumo wa onyo |
| 5.5 | TBD | (baadaye) Maboresho zaidi ya GC |
## Mafanikio Makuu
### Lua 1–3: Miaka ya Mapema (1994–1999)
- **1994**: Iliundwa katika PUC-Rio (Chuo Kikuu cha Kipapa cha Kikatoliki cha Rio de Janeiro) na Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Lengo**: Lugha ya uandishi inayoweza kupachikwa kwa uwekaji data (sio lugha inayojitegemea)
- **2.1**: Majedwali huwa muundo pekee wa data - usahili mkubwa
- **3.0**: C API imeimarishwa - hufanya Lua kupachikwa katika programu za C/C++
- **3.1**: Viwango vya juu - upeo wa kileksia kwa ajili ya kufungwa
### Lua 4: Kukomaa (2000)
- Kuhesabu marejeleo + mkusanyiko wa takataka (mseto)
- API iliyoboreshwa ya C - maktaba msaidizi ya `luaL_*`
- Bado hakuna upeo sahihi wa kileksika kwa ulimwengu
### Lua 5.0: Modern Lua (2003)
- **Upeo sahihi wa kileksika** - Vigezo vya `local`
- **Coroutines** - shughuli nyingi za ushirika
- **Metatables** — upakiaji wa opereta kupita kiasi, tabia maalum
- **Booleans** —`true`/`false`kama maadili sahihi
- **Kufungwa** kumefanywa vizuri - viwango vya juu vimejumlishwa
- Hili ni toleo ambalo lilifanya Lua kupitishwa sana katika michezo
### Lua 5.1: The Standard (2006)
- **Mkusanyaji takataka wa ziada**
- Mwendeshaji wa urefu wa `#`
- Kitendaji cha `module()`
- Iliyopita jinsi mazingira ya kimataifa yanavyofanya kazi
- **Toleo hili linakuwa toleo lililopachikwa kwa upana zaidi** (LuaJIT inalenga 5.1)
### Lua 5.2: Marekebisho (2011)
-`_ENV`- mazingira ya kila sehemu (ulimwengu safi)
- Taarifa ya`goto`inarudi
- Jedwali la Ephemeron (uboreshaji wa GC)
- Maboresho ya mfumo wa kifurushi
### Lua 5.3: Integer & Bits (2015)
- **Aina ndogo kamili** - tofauti na kuelea
- **Waendeshaji Bitwise** —`&`,`|`,`~`,`<<`,`>>`
** Msaada wa UTF-8** — maktaba ya`utf8`iliyojengwa ndani
- Sehemu ya sakafu`//`
- Kamba`pack`/`unpack`kwa data ya binary
### Lua 5.4: GC ya Kizazi (2020)
- **Mkusanya takataka wa kizazi** - kusitisha kwa GC bora zaidi
- ** Vigeu vya`<const>`** - vibadilishi vya kweli
- ** Vigezo vya `<close>`** — vigeu vya-kufungwa (usimamizi wa rasilimali, kama`defer`au`with`)
Mbinu ya `tostring`
- Aina ndogo za kamba (nyuzi fupi dhidi ya ndefu zilizoboreshwa tofauti)
## Mageuzi ya Sintaksia
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

## Mageuzi ya Kipengele
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

## Lua katika Michezo ya Kubahatisha
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

## Kanuni Muhimu za Usanifu
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Ukuaji wa Mfumo ikolojia
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
