---
# Metadata
title: "Lua — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lua ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lua, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Lua - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ ไลบรารี และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ Lua
---

## เวอร์ชัน Lua และการนำไปใช้งาน
| การนำไปปฏิบัติ | หมายเหตุ |
|---------|-------|
| **ลัว 5.4** | เวอร์ชันเสถียรปัจจุบัน |
| **ลัวจิต** | คอมไพเลอร์ JIT ประสิทธิภาพสูง |
| **หลัว 5.1** | ใช้กันอย่างแพร่หลาย (เข้ากันได้กับ LuaJIT) |
| **ราวี** | JIT พร้อมการพิมพ์เพิ่มเติม |
| **นกเป็ดน้ำ** | พิมพ์ภาษาถิ่นของ Lua |
| **ยี่หร่า** | Lisp ที่คอมไพล์เป็น Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ลัวะร็อคส์** | ตัวจัดการแพ็คเกจมาตรฐาน |
| **luarocks.org** | พื้นที่เก็บข้อมูลแพ็กเกจ |
| **สว่าง** | LuaJIT ผู้จัดการแพ็คเกจ |
```bash
luarocks install luasocket  # install package
luarocks list               # installed packages
luarocks remove luasocket   # remove package
```

```lua
-- .luarocks configuration
-- luarocks config
rocks_servers = {
    "https://luarocks.org"
}
```

---

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **OpenResty** | Nginx + Lua | เว็บประสิทธิภาพสูง |
| **ลูวิท** | Node.js เหมือน | Async I/O (libuv) |
| **วงโคจร** | เว็บ MVC | เว็บแอปง่ายๆ |
| **กะลาสีเรือ** | เต็มกอง | กรอบงาน MVC |
| **ลาพิส** | | ที่ใช้ OpenResty เว็บ MoonScript/ลัวะ |
| **เพกาซัส** | น้ำหนักเบา | เซิร์ฟเวอร์ HTTP แบบธรรมดา |
```lua
-- OpenResty / Nginx Lua example
-- nginx.conf
location /hello {
    content_by_lua_block {
        ngx.say("Hello, World!")
    }
}

location /api/users {
    content_by_lua_block {
        local cjson = require "cjson"
        local id = ngx.var.arg_id
        local user = get_user(id)
        ngx.header.content_type = "application/json"
        ngx.say(cjson.encode(user))
    }
}
```

---

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **luasql** | การผูกฐานข้อมูล (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | การผูก SQLite3 |
| **พีจีมูน** | PostgreSQL (Lua ล้วนๆ) |
```lua
-- SQLite example
local lsqlite3 = require "lsqlite3"

local db = lsqlite3.open("mydb.sqlite")

db:exec[[
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
  )
]]

local stmt = db:prepare("SELECT * FROM users WHERE id = ?")
stmt:bind_values(1)
for row in stmt:nrows() do
    print(row.id, row.name, row.email)
end
```

---

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **ถูกจับ** | การทดสอบสไตล์ BDD (ยอดนิยมที่สุด) |
| **luassert** | ไลบรารีการยืนยัน (ถูกจับ) |
| **ตัณหา** | การทดสอบขั้นต่ำ |
| **คนบ้าที่สุด** | การทดสอบสไตล์ xUnit |
| **นกเป็ดน้ำ** | การตรวจสอบประเภท (ภาษานกเป็ดน้ำ) |
```lua
-- busted example
describe("UserService", function()
    local service

    before_each(function()
        service = UserService.new()
    end)

    describe("find", function()
        it("returns user when found", function()
            service:add(User.new(1, "Alice"))
            local user = service:find(1)
            assert.is_not_nil(user)
            assert.are.equal("Alice", user.name)
        end)

        it("returns nil when not found", function()
            local user = service:find(999)
            assert.is_nil(user)
        end)
    end)
end)
```

```bash
busted spec/              # run tests
busted --verbose spec/    # verbose output
```

---

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **หลัวเช็ค** | การวิเคราะห์ขุยและแบบคงที่ |
| **รูปแบบ lua** | การจัดรูปแบบโค้ด |
| **สไตล์** | ตัวจัดรูปแบบโค้ด (แบบสนิม รวดเร็ว) |
| **นกเป็ดน้ำ** | พิมพ์ภาษาลัวะ |
| **ลัวโคฟ** | ความครอบคลุมของโค้ด |
```lua
-- .luacheckrc
std = "lua54"
include_files = {"src/**/*.lua"}
exclude_files = {"spec/**"}

codes = true
ignore = {"631"}  -- ignore line length
```

```bash
luacheck src/           # lint
stylua src/             # format
```

---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **luasocket** | เครือข่าย TCP/UDP/HTTP |
| **lua-cjson / cjson** | การแยกวิเคราะห์ JSON |
| **lpeg** | การจับคู่รูปแบบ (ตาม PEG) |
| **ไฟฉาย (pl)** | ไลบรารียูทิลิตี้ (เช่น Python stdlib) |
| **โคปาส** | ซ็อกเก็ตที่ใช้ Coroutine
| **คอกซ์คอล** | ป้องกันการโทร |
| **lua-resty-* | ระบบนิเวศ OpenResty |
| **ลฟส์** | การเข้าถึงระบบไฟล์ |
| **lzlib** | การบีบอัด |
| **lbase64** | การเข้ารหัส Base64 |
| **ตรวจสอบ** | โต๊ะพริตตี้-พิมพ์ |
| **คลาสสิก** | ระบบคลาส OOP |
| **ชนชั้นกลาง** | ไลบรารี OOP |
| **ความหื่น** | แม่แบบหนวด |
| **แยกวิเคราะห์** | การแยกวิเคราะห์อาร์กิวเมนต์ CLI |
---

## การพัฒนาเกม
| เครื่องยนต์ | หมายเหตุ |
|--------|--------|
| **รัก (Love2D)** | เฟรมเวิร์กเกม 2D (ยอดนิยมที่สุด) |
| **ปลดแอก** | เอ็นจิ้นเกม (สคริปต์ Lua) |
| **โคโรนา SDK** | เอ็นจิ้นเกมมือถือ |
| **Roblox** | แพลตฟอร์มเกม (ภาษาถิ่น Luau) |
| **เวิลด์ออฟวอร์คราฟต์** | การเขียนสคริปต์ UI (Lua) |
| **นีโอวิม** | บรรณาธิการ (สคริปต์ลัวะ) |
| **เรดิส** | การเขียนสคริปต์ Lua ใน Redis |
| **Nginx/OpenResty** | การเขียนสคริปต์ Lua ใน Nginx |
```lua
-- LÖVE example
function love.load()
    x, y = 400, 300
end

function love.update(dt)
    if love.keyboard.isDown("left") then x = x - 200 * dt end
    if love.keyboard.isDown("right") then x = x + 200 * dt end
end

function love.draw()
    love.graphics.circle("fill", x, y, 50)
end
```

---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **VS Code + Lua (ซัมเนโกะ)** | สุดยอด Lua LSP |
| **ZeroBrane สตูดิโอ** | IDE เฉพาะ Lua |
| **นีโอวิม** | การกำหนดค่า Lua (ชั้นหนึ่ง) |
| **IntelliJ + EmmyLua** | การสนับสนุน JetBrains Lua |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **แบบสแตนด์อโลน** | รวม Lua กับแอป |
| **ลัวะร็อคส์** | บรรจุและจัดจำหน่าย |
| **OpenResty** | การปรับใช้ Nginx + Lua |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **ฝังตัว** | เข้าสู่แอปพลิเคชัน C/C++ |
| **แพลตฟอร์มเกม** | LÖVE, Defold, Roblox |
---

## สรุป
ระบบนิเวศของ Lua มีขนาดเล็ก แต่มุ่งเน้นไปที่การฝังและการเขียนสคริปต์ Toolchain มาตรฐานคือ: **Lua 5.4** หรือ **LuaJIT** เป็นรันไทม์, **LuaRocks** สำหรับแพ็คเกจ, **busted** สำหรับการทดสอบ, **luacheck** สำหรับผ้าสำลี, **stylua** สำหรับการจัดรูปแบบ Lua เก่งในฐานะภาษาที่ฝังอยู่ในเกม (LÖVE, Defold, Roblox), เซิร์ฟเวอร์ (OpenResty, Nginx), ฐานข้อมูล (Redis) และบรรณาธิการ (Neovim) LuaJIT มอบประสิทธิภาพที่ใกล้เคียง C สำหรับสคริปต์ที่เน้นการประมวลผล จุดแข็งของ Lua คือขนาดที่เล็ก (~25KB) ไวยากรณ์ที่เรียบง่าย และ API การฝังที่ยอดเยี่ยมสำหรับการผสานรวม C/C++