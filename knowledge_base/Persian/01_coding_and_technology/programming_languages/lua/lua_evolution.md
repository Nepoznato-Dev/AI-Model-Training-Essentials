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
# Lua - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 1994 | انتشار اولیه (PUC-Rio، برزیل) |
| 2.1 | 1995 | جداول تبدیل به تنها ساختار داده |
| 3.0 | 1997 | C API، روش‌های برچسب (روش‌های اولیه) |
| 3.1 | 1998 | کنترل کننده های معنایی (بالا ارزش ها) |
| 4.0 | 2000 | **Lua 4**: ref-counting + GC، C API بهبود یافته |
| 5.0 | 2003 | **عناوین**: محدوده واژگانی مناسب، کوروتین ها، جدول های فرعی، بولی |
| 5.1 | 2006 | **GC افزایشی**، عملگر طول `#`، حذف `goto`،`module()`|
| 5.2 | 2011 |  تغییرات `_ENV`، `_G`، اضافه شدن `goto`، جداول زودگذر |
| 5.3 | 2015 | **نوع عدد صحیح**، عملگرهای بیتی، پشتیبانی از UTF-8 |
| 5.4 | 2020 | **متغیرهای GC** نسلی،`const`/ `close`، متام روش`tostring`|
| 5.4.x | 2020–25 | بهبودهای افزایشی، سیستم هشدار |
| 5.5 | TBD | (آینده) بهبودهای بیشتر GC |
## نقاط عطف اصلی
### Lua 1-3: The Early Years (1994-1999)
- **1994**: ایجاد شده در PUC-Rio (دانشگاه پاپی کاتولیک ریودوژانیرو) توسط روبرتو ایروسالیمشی، والدمار سلس، لوئیز هنریکه دی فیگوئرادو
- **هدف**: زبان برنامه نویسی قابل جاسازی برای ورود داده ها (نه یک زبان مستقل)
- **2.1**: جداول به تنها ساختار داده تبدیل می شوند - سادگی رادیکال
- **3.0**: C API یکپارچه - Lua را در برنامه های C/C++ قابل جاسازی می کند
- **3.1**: افزایش ارزش - محدوده واژگانی برای بسته شدن
### Lua 4: Maturation (2000)
- شمارش مرجع + جمع آوری زباله (هیبرید)
- بهبود یافته C API — کتابخانه کمکی `luaL_*`
- هنوز محدوده واژگانی مناسبی برای جهانیان وجود ندارد
### Lua 5.0: Modern Lua (2003)
- ** محدوده واژگانی مناسب ** — متغیرهای `local`
- **کوروتین** - چندوظیفه ای مشارکتی
- ** Metatables ** - بارگذاری بیش از حد اپراتور، رفتار سفارشی
- **Booleans** —`true`/`false`به عنوان مقادیر مناسب
- **بسته شدن** درست انجام شد - ارزش های بالا تعمیم یافت
- این نسخه ای است که لوا را به طور گسترده در بازی ها پذیرفته است
### Lua 5.1: The Standard (2006)
- ** زباله جمع کن افزایشی **
- عملگر طول `#`
- عملکرد `module()`
- نحوه عملکرد محیط جهانی را تغییر داد
- **این نسخه به گسترده ترین نسخه تعبیه شده تبدیل می شود ** (LuaJIT targets 5.1)
### Lua 5.2: Refinements (2011)
-`_ENV`- محیط به ازای هر تکه (جهانی تمیزتر)
- عبارت`goto`برمی گردد
- جداول Ephemeron (بهبود GC)
- بهبود سیستم بسته
### Lua 5.3: Integer & Bits (2015)
- ** زیرنوع عدد صحیح ** - متمایز از float
- **اپراتورهای بیتی** —`&`,`|`,`~`,`<<`,`>>`
- ** پشتیبانی UTF-8 ** - کتابخانه داخلی `utf8`
- تقسیم طبقه`//`
- رشته`pack`/`unpack`برای داده های باینری
### Lua 5.4: نسل GC (2020)
- ** جمع آوری زباله نسلی ** - مکث بسیار بهتر GC
- ** متغیرهای`<const>`** - ثابت های واقعی
- ** متغیرهای`<close>`** - متغیرهای بسته شدنی (مدیریت منابع، مانند`defer`یا `with`)
- روش `tostring`
- انواع زیر رشته (رشته های کوتاه در مقابل رشته های بلند به طور متفاوت بهینه شده اند)
## تکامل نحو
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

## تکامل ویژگی
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

## لوا در بازی
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

## اصول کلیدی طراحی
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## رشد اکوسیستم
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
