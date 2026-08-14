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

# Lua — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| 1.0 | 1994 | الإصدار الأولي (PUC-ريو، البرازيل) |
| 2.1 | 1995 | تصبح الجداول هي بنية البيانات الوحيدة |
| 3.0 | 1997 | واجهة برمجة تطبيقات C، طرق العلامات (الطرق الوصفية المبكرة) |
| 3.1 | 1998 | المتحكمات الدلالية (القيم الأعلى) |
| 4.0 | 2000 | **Lua 4**: عد المرجع + GC، تحسين واجهة برمجة تطبيقات C |
| 5.0 | 2003 | **التخصص الرئيسي**: تحديد النطاق المعجمي المناسب، والكوروتينات، والجداول الوصفية، والمنطقيات |
| 5.1 | 2006 | **تزايدي GC**، عامل طول `#`، إزالة `goto`،`module()`|
| 5.2 | 2011 |  `_ENV`، تغييرات `_G`، إضافة`goto`مرة أخرى، جداول الزوال |
| 5.3 | 2015 | **نوع عدد صحيح**، عوامل تشغيل البت، دعم UTF-8 |
| 5.4 | 2020 | **جيل GC**، متغيرات`const`/ `close`، طريقة`tostring`|
| 5.4.x | 2020–25 | تحسينات تدريجية، نظام إنذار |
| 5.5 | سيتم تحديده لاحقًا | (المستقبل) مزيد من التحسينات على GC |
## المعالم الرئيسية
### لوا 1-3: السنوات الأولى (1994-1999)
- **1994**: تم إنشاؤها في PUC-Rio (الجامعة البابوية الكاثوليكية في ريو دي جانيرو) من قبل روبرتو إيروساليمشي، وفالديمار سيليس، ولويز هنريكي دي فيغيريدو
- **الهدف**: لغة برمجة نصية قابلة للتضمين لإدخال البيانات (وليست لغة مستقلة)
- **2.1**: تصبح الجداول هي بنية البيانات الوحيدة - البساطة الجذرية
- **3.0**: تم تعزيز C API — مما يجعل Lua قابلة للتضمين في تطبيقات C/C++
- **3.1**: القيم الأعلى — النطاق المعجمي للإغلاقات
### لوا 4: النضج (2000)
- عد المراجع + جمع البيانات المهملة (الهجين)
- تحسين C API — مكتبة`luaL_*`المساعدة
- لا يوجد حتى الآن نطاق معجمي مناسب للكلوبات
### لوا 5.0: لوا الحديثة (2003)
- **النطاق المعجمي المناسب** — متغيرات `local`
- **Coroutines** — تعدد المهام التعاونية
- **الجداول الوصفية** — التحميل الزائد على المشغل، سلوك مخصص
- **المنطقية** —`true`/`false`كقيم مناسبة
- **عمليات الإغلاق** تمت بشكل صحيح — تم تعميم القيم الأعلى
- هذه هي النسخة التي جعلت Lua معتمدة على نطاق واسع في الألعاب
### لوا 5.1: المعيار (2006)
- ** جامع القمامة المتزايد **
- عامل طول `#`
- وظيفة `module()`
- تغير كيفية عمل البيئة العالمية
- **يصبح هذا الإصدار هو الإصدار المضمن الأكثر انتشارًا** (يستهدف LuaJIT 5.1)
### لوا 5.2: التحسينات (2011)
-`_ENV`— بيئة القطعة الواحدة (المجموعات العالمية الأنظف)
- إرجاع بيان `goto`
- الجداول الفلكية (تحسين GC)
- تحسينات نظام الحزمة
### Lua 5.3: عدد صحيح وبت (2015)
- **النوع الفرعي الصحيح** — يختلف عن النوع العائم
- **معاملات البت** —`&`,`|`,`~`,`<<`,`>>`
- **دعم UTF-8** — مكتبة`utf8`مدمجة
- تقسيم الارضيات`//`
- سلسلة`pack`/`unpack`للبيانات الثنائية
### Lua 5.4: أجيال GC (2020)
- **جامع البيانات المهملة للأجيال** — توقف GC مؤقتًا بشكل أفضل بكثير
- ** متغيرات`<const>`** — ثوابت حقيقية
- ** متغيرات`<close>`** — المتغيرات التي سيتم إغلاقها (إدارة الموارد، مثل`defer`أو `with`)
- الطريقة الوصفية `tostring`
- أنواع السلسلة الفرعية (السلاسل القصيرة مقابل السلاسل الطويلة المحسنة بشكل مختلف)
## تطور بناء الجملة
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

## تطور الميزة
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

## لوا في الألعاب
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

## مبادئ التصميم الرئيسية
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## نمو النظام البيئي
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
