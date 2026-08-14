---
# Metadata
title: "Lua — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lua ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Lua - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، کتابخانه‌ها و زیرساخت‌های ضروری در اکوسیستم Lua را پوشش می‌دهد.
---

## نسخه‌ها و پیاده‌سازی‌های Lua
| پیاده سازی | یادداشت ها |
|---------------|-------|
| **Lua 5.4** | نسخه پایدار فعلی |
| **LuaJIT** | کامپایلر JIT با کارایی بالا |
| **Lua 5.1** | پرکاربرد (سازگار با LuaJIT) |
| **راوی** | JIT با تایپ اختیاری |
| **آب سبزی** | گویش تایپ شده لوا |
| **رازیانه** | Lisp که به Lua کامپایل می شود |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **LuaRocks** | مدیر بسته استاندارد |
| **luarocks.org** | مخزن بسته |
| **روشن** | مدیر بسته LuaJIT |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | وب با کارایی بالا |
| **لوویت** | Node.js-like | Async I/O (libuv) |
| **مدار** | وب MVC | برنامه های وب ساده |
| **ملوان** | تمام پشته | چارچوب MVC |
| **لاپیس** | مبتنی بر OpenResty | MoonScript/Lua web |
| **پگاسوس** | سبک | سرور HTTP ساده |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **luasql** | اتصالات پایگاه داده (SQLite، PostgreSQL، MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | اتصالات SQLite3 |
| **pgmoon** | PostgreSQL (لوا خالص) |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **شکسته** | تست سبک BDD (محبوب ترین) |
| **لواسرت** | کتابخانه ادعا (خراب شده) |
| **شهوت** | تست حداقل |
| **دیوانه ترین** | تست xUnit-style |
| **آبی** | بررسی تایپ (گویش سبز) |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **لواچک** | لینتینگ و آنالیز استاتیک |
| **lua-format** | قالب بندی کد |
| **استایلو** | فرمت کننده کد (مبتنی بر زنگ زدگی، سریع) |
| **آبی** | تایپ شده لهجه Lua |
| **luacov** | پوشش کد |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **luasocket** | شبکه TCP/UDP/HTTP |
| **lua-cjson / cjson** | تجزیه JSON |
| **lpeg** | تطبیق الگو (بر اساس PEG) |
| **Penlight (pl)** | کتابخانه ابزار (مانند Python stdlib) |
| **کوپاس** | سوکت مبتنی بر کوروتین |
| **coxpcall** | تماس های محافظت شده |
| **lua-resty-* | اکوسیستم OpenResty |
| **lfs** | دسترسی به سیستم فایل |
| **لزلیب** | فشرده سازی |
| **base64** | کدگذاری Base64 |
| **بازرسی** | چاپ رومیزی زیبا |
| **کلاسیک** | سیستم کلاس OOP |
| **طبقه متوسط** | کتابخانه OOP |
| **لباس** | قالب های سبیل |
| **argparse** | تجزیه آرگومان CLI |
---

## توسعه بازی
| موتور | یادداشت ها |
|--------|-------|
| **LÖVE (Love2D)** | چارچوب بازی دوبعدی (محبوب ترین) |
| **فولد** | موتور بازی (Lua scripting) |
| **Corona SDK** | موتور بازی موبایل |
| **روبلوکس** | پلتفرم بازی (گویش Luau) |
| **World of Warcraft** | اسکریپت UI (Lua) |
| **Neovim** | ویرایشگر (Lua scripting) |
| **ردیس** | اسکریپت نویسی Lua در Redis |
| **Nginx/OpenResty** | اسکریپت نویسی Lua در Nginx |
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

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + Lua (sumneko)** | بهترین Lua LSP |
| **استودیو ZeroBrane** | IDE خاص Lua |
| **Neovim** | پیکربندی Lua (کلاس اول) |
| **IntelliJ + EmmyLua** | پشتیبانی JetBrains Lua |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **مستقل** | بسته نرم افزاری Lua با برنامه |
| **LuaRocks** | بسته بندی و توزیع |
| **OpenResty** | استقرار Nginx + Lua |
| **داکر** | کانتینری |
| **جاسازی شده** | به برنامه های C/C++ |
| **پلتفرم های بازی** | LÖVE، Defold، Roblox |
---

## خلاصه
اکوسیستم Lua کوچک است اما بر روی تعبیه و فیلمنامه متمرکز است. زنجیره ابزار استاندارد عبارتند از: **Lua 5.4** یا **LuaJIT** به عنوان زمان اجرا، **LuaRocks** برای بسته ها، **busted** برای آزمایش، **luacheck** برای پرده زدن، **stylua** برای قالب بندی. Lua به عنوان یک زبان جاسازی شده در بازی ها (LÖVE، Defold، Roblox)، سرورها (OpenResty، Nginx)، پایگاه های داده (Redis) و ویرایشگرها (Neovim) برتری دارد. LuaJIT عملکرد نزدیک به C را برای اسکریپت های محاسباتی فشرده ارائه می دهد. نقاط قوت Lua ردپای کوچک آن (~25KB)، نحو ساده و API تعبیه‌شده عالی برای یکپارچه‌سازی C/C++ است.