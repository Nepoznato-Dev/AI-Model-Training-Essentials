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

# لوا - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 1994 | ابتدائی ریلیز (PUC-Rio, Brazil) |
| 2.1 | 1995 | میزیں واحد ڈیٹا ڈھانچہ بن جاتی ہیں |
| 3.0 | 1997 | C API، ٹیگ کے طریقے (ابتدائی میٹا میتھڈز) |
| 3.1 | 1998 | سیمنٹک کنٹرولرز (اعلی قدریں) |
| 4.0 | 2000 | **Lua 4**: ref-counting + GC، بہتر C API |
| 5.0 | 2003 | **میجر**: مناسب لغوی اسکوپنگ، کوروٹینز، میٹیٹیبلز، بولین |
| 5.1 | 2006 | **اضافہ شدہ GC**،`#`لمبائی آپریٹر،`goto`ہٹا دیا گیا،`module()`|
| 5.2 | 2011 | `_ENV`,`_G`تبدیلیاں،`goto`کو واپس شامل کیا گیا، ایفیمرون میزیں |
| 5.3 | 2015 | **انٹیجر کی قسم**، بٹ وائز آپریٹرز، UTF-8 سپورٹ |
| 5.4 | 2020 | **جنریشنل GC**،`const`/`close`متغیرات،`tostring`میٹا میتھڈ |
| 5.4.x | 2020-25 | بڑھتی ہوئی بہتری، انتباہی نظام |
| 5.5 | TBD | (مستقبل) GC میں مزید بہتری |
## اہم سنگ میل
### Lua 1–3: The Early Years (1994–1999)
- **1994**: PUC-Rio (ریو ڈی جنیرو کی پونٹیفیکل کیتھولک یونیورسٹی) میں Roberto Ierusalimschy، Waldemar Celes، Luiz Henrique de Figueiredo کے ذریعے تخلیق کیا گیا
- **مقصد**: ڈیٹا انٹری کے لیے ایمبیڈ ایبل اسکرپٹنگ لینگویج (اسٹینڈ اکیلی زبان نہیں)
- **2.1**: جدولیں ڈیٹا کا واحد ڈھانچہ بن جاتی ہیں — بنیادی سادگی
- **3.0**: C API مستحکم — Lua کو C/C++ ایپلی کیشنز میں سرایت کرنے کے قابل بناتا ہے۔
- **3.1**: اعلی قدریں — بندش کے لیے لغوی اسکوپنگ
### لوا 4: پختگی (2000)
- حوالہ گنتی + کچرا جمع کرنا (ہائبرڈ)
- بہتر C API —`luaL_*`معاون لائبریری
- اب بھی عالمیوں کے لیے کوئی مناسب لغوی دائرہ کار نہیں ہے۔
### Lua 5.0: Modern Lua (2003)
- **مناسب لغوی اسکوپنگ** —`local`متغیرات
- **کورٹائنز** — کوآپریٹو ملٹی ٹاسکنگ
- **میٹی ٹیبلز** — آپریٹر اوور لوڈنگ، حسب ضرورت سلوک
- **بولین** —`true`/`false`مناسب اقدار کے طور پر
- **بندش** صحیح ہو گئی — اوپر کی قدروں کو عام کیا گیا۔
- یہ وہ ورژن ہے جس نے لوا کو گیمز میں بڑے پیمانے پر اپنایا
### Lua 5.1: The Standard (2006)
- **بڑھتی ہوئی کچرا جمع کرنے والا**
-`#`لمبائی آپریٹر
-`module()`فنکشن
- عالمی ماحول کے کام کرنے کا طریقہ بدل گیا۔
- **یہ ورژن سب سے زیادہ سرایت شدہ ورژن بن جاتا ہے** (LuaJIT کے ہدف 5.1)
### Lua 5.2: ریفائنمنٹس (2011)
-`_ENV`- فی حصہ ماحول (کلینر گلوبل)
-`goto`بیان واپس آتا ہے۔
- ایفیمیرون ٹیبلز (جی سی میں بہتری)
- پیکیج سسٹم میں بہتری
### Lua 5.3: انٹیجر اور بٹس (2015)
- **انٹیجر ذیلی قسم** — فلوٹ سے الگ
- **Bitwise آپریٹرز** — `&`، `|`، `~`، `<<`،`>>`
- **UTF-8 سپورٹ** — بلٹ ان`utf8`لائبریری
- فلور ڈویژن`//`
- سٹرنگ`pack`/`unpack`بائنری ڈیٹا کے لیے
### Lua 5.4: جنریشنل GC (2020)
- **جنریشنل کوڑا اٹھانے والا** — بہت بہتر GC توقف
- **`<const>`متغیرات** — حقیقی مستقل
- **`<close>`متغیرات** — بند ہونے والے متغیرات (وسائل کا انتظام، جیسے`defer`یا `with`)
-`tostring`میٹا میتھڈ
- سٹرنگ کی ذیلی قسمیں (مختصر بمقابلہ لمبی تاریں مختلف طریقے سے بہتر کی گئی ہیں)
## نحوی ارتقاء
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

## فیچر ارتقاء
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

## گیمنگ میں Lua
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

## ڈیزائن کے کلیدی اصول
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## ماحولیاتی نظام کی نمو
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
