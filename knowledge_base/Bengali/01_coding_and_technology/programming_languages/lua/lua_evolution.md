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
# লুয়া — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 1.0 | 1994 | প্রাথমিক প্রকাশ (PUC-Rio, Brazil) |
| 2.1 | 1995 | টেবিল শুধুমাত্র তথ্য কাঠামো হয়ে ওঠে |
| 3.0 | 1997 | C API, ট্যাগ পদ্ধতি (প্রাথমিক মেটামেথড) |
| 3.1 | 1998 | শব্দার্থক নিয়ন্ত্রক (উচ্চমূল্য) |
| 4.0 | 2000 | **Lua 4**: ref-counting + GC, উন্নত C API |
| 5.0 | 2003 | **মেজর**: সঠিক আভিধানিক স্কোপিং, কোরোটিন, মেটাটেবল, বুলিয়ানস |
| 5.1 | 2006 | **বর্ধিত GC**,`#`দৈর্ঘ্য অপারেটর,`goto`সরানো হয়েছে,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`পরিবর্তন,`goto`আবার যোগ করা হয়েছে, এফিমেরন টেবিল |
| 5.3 | 2015 | **পূর্ণসংখ্যার ধরন**, বিটওয়াইজ অপারেটর, UTF-8 সমর্থন |
| 5.4 | 2020 | **জেনারেশনাল GC**,`const`/`close`ভেরিয়েবল,`tostring`মেটামেথড |
| 5.4.x | 2020-25 | ক্রমবর্ধমান উন্নতি, সতর্কতা ব্যবস্থা |
| 5.5 | টিবিডি | (ভবিষ্যত) আরও GC উন্নতি |
## প্রধান মাইলফলক
### লুয়া 1-3: দ্য আর্লি ইয়ারস (1994-1999)
- **1994**: PUC-রিও (রিও ডি জেনিরোর পন্টিফিক্যাল ক্যাথলিক ইউনিভার্সিটি) রবার্তো ইরুসালিমসচি, ওয়াল্ডেমার সেলস, লুইজ হেনরিক ডি ফিগুইরেডো দ্বারা তৈরি
- **লক্ষ্য**: ডেটা এন্ট্রির জন্য এমবেডযোগ্য স্ক্রিপ্টিং ভাষা (একটি স্বতন্ত্র ভাষা নয়)
- **2.1**: টেবিলগুলি একমাত্র ডেটা স্ট্রাকচারে পরিণত হয় — আমূল সরলতা
- **3.0**: C API সলিফাইড — লুয়াকে C/C++ অ্যাপ্লিকেশনে এম্বেডযোগ্য করে তোলে
- **3.1**: উচ্চমূল্য — বন্ধের জন্য আভিধানিক সুযোগ
### লুয়া 4: পরিপক্কতা (2000)
- রেফারেন্স গণনা + আবর্জনা সংগ্রহ (হাইব্রিড)
- উন্নত C API —`luaL_*`অক্জিলিয়ারী লাইব্রেরি
- এখনও বিশ্ববাসীর জন্য কোন সঠিক আভিধানিক সুযোগ নেই
### লুয়া 5.0: আধুনিক লুয়া (2003)
- **যথাযথ আভিধানিক স্কোপিং** —`local`ভেরিয়েবল
- **করোটিন** — সমবায় মাল্টিটাস্কিং
- **মেটাটেবল** — অপারেটর ওভারলোডিং, কাস্টম আচরণ
- **বুলিয়ানস** — সঠিক মান হিসাবে`true`/ `false`
- **বন্ধ** সঠিকভাবে সম্পন্ন হয়েছে — উচ্চমূল্য সাধারণীকৃত
- এটি সেই সংস্করণ যা লুয়াকে গেমগুলিতে ব্যাপকভাবে গৃহীত করেছে
### লুয়া 5.1: দ্য স্ট্যান্ডার্ড (2006)
- **বর্ধিত আবর্জনা সংগ্রহকারী**
-`#`দৈর্ঘ্য অপারেটর
-`module()`ফাংশন
- বৈশ্বিক পরিবেশ কীভাবে কাজ করে তা পরিবর্তিত হয়েছে
- **এই সংস্করণটি সবচেয়ে ব্যাপকভাবে এম্বেড করা সংস্করণ হয়ে উঠেছে** (LuaJIT টার্গেট 5.1)
### Lua 5.2: পরিশোধন (2011)
-`_ENV`— প্রতি খণ্ড পরিবেশ (ক্লিনার গ্লোবাল)
-`goto`বিবৃতি প্রদান করে
- Ephemeron টেবিল (GC উন্নতি)
- প্যাকেজ সিস্টেম উন্নতি
### Lua 5.3: পূর্ণসংখ্যা এবং বিট (2015)
- **পূর্ণসংখ্যা সাবটাইপ** — ফ্লোট থেকে আলাদা
- **বিটওয়াইজ অপারেটর** — `&`, `|`, `~`, `<<`,`>>`
- **UTF-8 সমর্থন** — অন্তর্নির্মিত`utf8`লাইব্রেরি
- ফ্লোর ডিভিশন`//`
- বাইনারি ডেটার জন্য`pack`/`unpack`স্ট্রিং
### Lua 5.4: জেনারেশনাল GC (2020)
- **জেনারেশনাল গারবেজ কালেক্টর** — অনেক ভালো জিসি পজ
- **`<const>`ভেরিয়েবল** — সত্য ধ্রুবক
- **`<close>`ভেরিয়েবল** — বন্ধ হওয়া ভেরিয়েবল (সম্পদ ব্যবস্থাপনা, যেমন`defer`বা `with`)
-`tostring`মেটামেথড
- স্ট্রিং সাবটাইপ (ছোট বনাম দীর্ঘ স্ট্রিং ভিন্নভাবে অপ্টিমাইজ করা হয়েছে)
## সিনট্যাক্স বিবর্তন
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

## বৈশিষ্ট্য বিবর্তন
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

## লুয়া ইন গেমিং
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

## মূল ডিজাইনের নীতি
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## ইকোসিস্টেম বৃদ্ধি
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
