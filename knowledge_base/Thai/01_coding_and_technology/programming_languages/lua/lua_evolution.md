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
# Lua — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 1.0 | 1994 | การเปิดตัวครั้งแรก (PUC-สนามบินริโอ บราซิล) |
| 2.1 | 1995 | ตารางกลายเป็นโครงสร้างข้อมูลเดียว |
| 3.0 | 1997 | C API วิธีการแท็ก (เมตาวิธีการเริ่มต้น) |
| 3.1 | 1998 | ตัวควบคุมความหมาย (ค่าเพิ่ม) |
| 4.0 | 2000 | **Lua 4**: การนับซ้ำ + GC, ปรับปรุง C API |
| 5.0 | 2546 | **หลัก**: การกำหนดขอบเขตคำศัพท์ที่เหมาะสม, โครูทีน, เมตาเทเบิล, บูลีน |
| 5.1 | 2549 | **GC ที่เพิ่มขึ้น**, ตัวดำเนินการความยาว `#`,`goto`ถูกลบออก,`module()`|
| 5.2 | 2554 | `_ENV`,`_G`การเปลี่ยนแปลง,`goto`เพิ่มกลับ, ตารางชั่วคราว |
| 5.3 | 2558 | **ประเภทจำนวนเต็ม** ตัวดำเนินการระดับบิต รองรับ UTF-8 |
| 5.4 | 2020 | **Generational GC**, ตัวแปร`const`/ `close`, วิธีการเมตา`tostring`|
| 5.4.x | 2563–25 | การปรับปรุงที่เพิ่มขึ้นระบบเตือน |
| 5.5 | จะแจ้งภายหลัง | (อนาคต) การปรับปรุง GC เพิ่มเติม |
## เหตุการณ์สำคัญที่สำคัญ
### ลัวะ 1–3: ช่วงปีแรก ๆ (1994–1999)
- **1994**: สร้างที่ PUC-Rio (Pontifical Catholic University of Rio de Janeiro) โดย Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **เป้าหมาย**: ภาษาสคริปต์แบบฝังได้สำหรับการป้อนข้อมูล (ไม่ใช่ภาษาสแตนด์อโลน)
- **2.1**: ตารางกลายเป็นโครงสร้างข้อมูลเพียงอย่างเดียว — ความเรียบง่ายสุดขั้ว
- **3.0**: C API แข็งตัว — ทำให้ Lua สามารถฝังได้ในแอปพลิเคชัน C/C++
- **3.1**: Upvalues — การกำหนดขอบเขตคำศัพท์สำหรับการปิด
### ลัวะ 4: การสุก (2000)
- การนับอ้างอิง + การเก็บขยะ (ไฮบริด)
- ปรับปรุง C API - ไลบรารีเสริม `luaL_*`
- ยังไม่มีการกำหนดขอบเขตคำศัพท์ที่เหมาะสมสำหรับโกลบอล
### ลัวะ 5.0: ลัวะสมัยใหม่ (2003)
- **การกำหนดขอบเขตคำศัพท์ที่เหมาะสม** — ตัวแปร `local`
- **Coroutines** — การทำงานร่วมกันหลายอย่างพร้อมกัน
- **Metatables** — โอเปอเรเตอร์โอเวอร์โหลด พฤติกรรมแบบกำหนดเอง
- **บูลีน** —`true`/`false`เป็นค่าที่เหมาะสม
- **ปิด** ถูกต้อง — เพิ่มค่าทั่วไป
- นี่คือเวอร์ชันที่ทำให้ Lua ได้รับการยอมรับอย่างกว้างขวางในเกม
### ลัวะ 5.1: มาตรฐาน (2549)
- **คนเก็บขยะเพิ่มขึ้น**
- ตัวดำเนินการความยาว `#`
- ฟังก์ชัน `module()`
- เปลี่ยนวิธีการทำงานของสภาพแวดล้อมทั่วโลก
- **เวอร์ชันนี้กลายเป็นเวอร์ชันที่ฝังอย่างกว้างขวางที่สุด** (LuaJIT เป้าหมาย 5.1)
### ลัวะ 5.2: การปรับแต่ง (2011)
-`_ENV`— สภาพแวดล้อมต่อชิ้น (globals ที่สะอาดกว่า)
- ส่งคืนคำสั่ง `goto`
- ตาราง Ephemeron (ปรับปรุง GC)
- ปรับปรุงระบบแพ็คเกจ
### Lua 5.3: จำนวนเต็มและบิต (2015)
- **ชนิดย่อยจำนวนเต็ม** — แตกต่างจากโฟลต
- **ตัวดำเนินการระดับบิต** —`&`,`|`,`~`,`<<`,`>>`
- **รองรับ UTF-8** — ไลบรารี`utf8`ในตัว
- หมวดชั้น`//`
- สตริง`pack`/`unpack`สำหรับข้อมูลไบนารี
### Lua 5.4: Generational GC (2020)
- **คนเก็บขยะทั่วไป** — GC หยุดชั่วคราวได้ดีขึ้นมาก
- ** ตัวแปร `<const>`** — ค่าคงที่จริง
- ** ตัวแปร `<close>`** — ตัวแปรที่จะปิด (การจัดการทรัพยากร เช่น`defer`หรือ`with`)
- วิธีการเมตา `tostring`
- ประเภทย่อยของสตริง (สตริงแบบสั้นและแบบยาวได้รับการปรับให้เหมาะสมแตกต่างกัน)
## วิวัฒนาการไวยากรณ์
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

## วิวัฒนาการคุณสมบัติ
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

## ลัวะในเกม
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

## หลักการออกแบบที่สำคัญ
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## การเติบโตของระบบนิเวศ
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
