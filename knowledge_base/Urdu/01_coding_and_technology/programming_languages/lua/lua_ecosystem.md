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
# Lua — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ Lua ماحولیاتی نظام میں ضروری آلات، لائبریریوں اور بنیادی ڈھانچے کا احاطہ کرتا ہے۔
---

## Lua ورژن اور نفاذ
| نفاذ | نوٹس |
|---------------|---------|
| **لوا 5.4** | موجودہ مستحکم ورژن |
| **لواجیت** | اعلی کارکردگی کا جے آئی ٹی کمپائلر |
| **لوا 5.1** | بڑے پیمانے پر استعمال کیا جاتا ہے (LuaJIT ہم آہنگ) |
| **راوی** | اختیاری ٹائپنگ کے ساتھ JIT |
| **ٹیل** | لوا کی ٹائپ شدہ بولی |
| **سونف** | Lisp جو Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **LuaRocks** | معیاری پیکیج مینیجر |
| **luarocks.org** | پیکیج ذخیرہ |
| **روشن** | LuaJIT پیکیج مینیجر |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **اوپن ریسٹی** | Nginx + Lua | ہائی پرفارمنس ویب |
| **لویت** | Node.js کی طرح | Async I/O (libuv) |
| **مدار** | MVC ویب | سادہ ویب ایپس |
| **نااخت** | مکمل اسٹیک | MVC فریم ورک |
| **لیپیس** | OpenResty پر مبنی | مون اسکرپٹ/لوا ویب |
| **پیگاسس** | ہلکا پھلکا | سادہ HTTP سرور |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **luasql** | ڈیٹا بیس بائنڈنگز (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | SQLite3 بائنڈنگز |
| **pgmoon** | PostgreSQL (خالص Lua) |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **بھکا دیا** | BDD طرز کی جانچ (سب سے زیادہ مقبول) |
| **لواسرٹ** | اسسرشن لائبریری (برسٹڈ) |
| **شہوت** | کم سے کم جانچ |
| **پاگل ترین** | xUnit طرز کی جانچ |
| **ٹیل** | ٹائپ چیکنگ (ٹیلی بولی) |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **لوچیک** | لنٹنگ اور جامد تجزیہ |
| **لوا فارمیٹ** | کوڈ فارمیٹنگ |
| **سٹائلوا** | کوڈ فارمیٹر (زنگ پر مبنی، تیز) |
| **ٹیل** | ٹائپ شدہ لوا بولی |
| **luacov** | کوڈ کوریج |
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

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **luasocket** | TCP/UDP/HTTP نیٹ ورکنگ |
| **lua-cjson / cjson** | JSON پارسنگ |
| **lpeg** | پیٹرن میچنگ (پی ای جی پر مبنی) |
| **پین لائٹ (pl)** | یوٹیلیٹی لائبریری (جیسے Python stdlib) |
| **copas** | کوروٹین پر مبنی ساکٹ |
| **coxpcall** | پروٹیکٹڈ کالز |
| **lua-resty-* | OpenResty ماحولیاتی نظام |
| **lfs** | فائل سسٹم تک رسائی |
| **lzlib** | کمپریشن |
| **lbase64** | بیس 64 انکوڈنگ |
| **معائنہ کریں** | ٹیبل خوبصورت پرنٹنگ |
| **کلاسیکی** | OOP کلاس سسٹم |
| **مڈل کلاس** | OOP لائبریری |
| **شہوت** | مونچھوں کے سانچے |
| **آرگ پارس** | CLI دلیل کی تجزیہ |
---

## گیم ڈویلپمنٹ
| انجن | نوٹس |
|---------|-------|
| **لوو (محبت 2 ڈی)** | 2D گیم فریم ورک (سب سے زیادہ مقبول) |
| **ڈفولڈ** | گیم انجن (لوا اسکرپٹنگ) |
| **کورونا SDK** | موبائل گیم انجن |
| **روبلوکس** | گیم پلیٹ فارم (لواؤ بولی) |
| ** وار کرافٹ کی دنیا** | UI اسکرپٹنگ (Lua) |
| **نیوم** | ایڈیٹر (لوا اسکرپٹنگ) |
| **ریڈیس** | Redis میں Lua سکرپٹ |
| **Nginx/OpenResty** | Nginx میں Lua اسکرپٹنگ |
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

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + Lua (sumneko)** | بہترین Lua LSP |
| **زیرو برین اسٹوڈیو** | Lua مخصوص IDE |
| **نیوم** | لوا کنفیگریشن (فرسٹ کلاس) |
| **IntelliJ + EmmyLua** | JetBrains Lua کی حمایت |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **اسٹینڈ ** | ایپ کے ساتھ لوا بنڈل |
| **LuaRocks** | پیکیج اور تقسیم |
| **اوپن ریسٹی** | Nginx + Lua کی تعیناتی |
| **ڈوکر** | کنٹینرائزڈ |
| **ایمبیڈڈ** | C/C++ ایپلی کیشنز میں |
| **گیم پلیٹ فارم** | LÖVE, Defold, Roblox |
---

## خلاصہ
Lua کا ماحولیاتی نظام چھوٹا ہے لیکن سرایت کرنے اور اسکرپٹنگ پر مرکوز ہے۔ معیاری ٹول چین یہ ہے: **Lua 5.4** یا **LuaJIT** بطور رن ٹائم، **LuaRocks** پیکجز کے لیے، **بسٹڈ** ٹیسٹنگ کے لیے، **luacheck** linting کے لیے، **stylua** فارمیٹنگ کے لیے۔ Lua گیمز (LÖVE، Defold، Roblox)، سرورز (OpenResty، Nginx)، ڈیٹا بیس (Redis) اور ایڈیٹرز (Neovim) میں سرایت شدہ زبان کے طور پر سبقت لے جاتا ہے۔ LuaJIT کمپیوٹ-انٹینسیو اسکرپٹس کے لیے قریب-C کارکردگی فراہم کرتا ہے۔ Lua کی خوبیاں اس کے چھوٹے نقش (~25KB)، سادہ نحو، اور C/C++ انضمام کے لیے بہترین ایمبیڈنگ API ہیں۔