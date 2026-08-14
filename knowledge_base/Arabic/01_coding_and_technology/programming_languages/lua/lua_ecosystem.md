<!--
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

-->
# لوا - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والمكتبات والبنية التحتية الأساسية في نظام Lua البيئي.
---

## إصدارات وتطبيقات Lua
| التنفيذ | ملاحظات |
|---------------|-------|
| ** لوا 5.4 ** | النسخة المستقرة الحالية |
| ** لواجيت ** | مترجم JIT عالي الأداء |
| ** لوا 5.1 ** | يستخدم على نطاق واسع (متوافق مع LuaJIT) |
| ** رافي ** | JIT مع الكتابة الاختيارية |
| ** البط البري ** | لهجة لوا المكتوبة |
| **الشمر** | اللثغة التي تجمع لوا |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| ** لوا روكس ** | مدير الحزم القياسية |
| **luarocks.org** | مستودع الحزمة |
| **مضاءة** | مدير الحزم LuaJIT |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **أوبن ريستي** | إنجينكس + لوا | ويب عالي الأداء |
| **لوفيت** | Node.js يشبه | الإدخال/الإخراج غير المتزامن (libuv) |
| **المدار** | ويب إم في سي | تطبيقات ويب بسيطة |
| **بحار** | مكدس كامل | إطار عمل MVC |
| **اللازورد** | مبني على OpenResty | مونسكريبت/لوا ويب |
| **بيغاسوس** | خفيف الوزن | خادم HTTP بسيط |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| **لواسقل** | ربط قواعد البيانات (SQLite، PostgreSQL، MySQL) |
| **lua-resty-mysql** | ماي إس كيو إل (أوبن ريستي) |
| ** لوا-ريستي-ريديس** | ريديس (أوبن ريستي) |
| **لسكليتي3** | روابط SQLite3 |
| **بجمون** | PostgreSQL (Lua النقي) |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| ** ضبطت ** | اختبار نمط BDD (الأكثر شيوعًا) |
| **لواسرت** | مكتبة التوكيد (ضبطت) |
| **الشهوة** | الحد الأدنى من الاختبار |
| **الأكثر جنونا** | اختبار نمط xUnit |
| ** البط البري ** | التحقق من النوع (لهجة البط البري) |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **لواتشيك** | البطانة والتحليل الساكن |
| **تنسيق لوا** | تنسيق الكود |
| ** ستايلا ** | منسق الكود (يعتمد على الصدأ، سريع) |
| ** البط البري ** | لهجة لوا المكتوبة |
| ** لواكوف ** | تغطية الكود |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| ** لواسوكيت ** | شبكات TCP/UDP/HTTP |
| ** لوا-cjson / cjson** | تحليل JSON |
| **لبيج** | مطابقة الأنماط (المعتمدة على PEG) |
| **بن لايت (رر)** | مكتبة المرافق (مثل Python stdlib) |
| **كوباس** | المقبس القائم على كوروتين |
| **coxpcall** | المكالمات المحمية |
| **لوا-ريستي-* | النظام البيئي OpenResty |
| **لفس** | الوصول إلى نظام الملفات |
| **الزليب** | ضغط |
| **lbase64** | ترميز Base64 |
| **فحص** | طباعة طاولة جميلة |
| **كلاسيكي** | نظام فئة OOP |
| **الطبقة الوسطى** | مكتبة OOP |
| **شهوة** | قوالب شارب |
| **أرجبارس** | تحليل وسيطة CLI |
---

## تطوير اللعبة
| المحرك | ملاحظات |
|--------|------|
| **الحب (Love2D)** | إطار اللعبة ثنائي الأبعاد (الأكثر شهرة) |
| ** ديفولد ** | محرك اللعبة (برمجة لوا) |
| **كورونا SDK** | محرك لعبة الجوال |
| **روبلوكس** | منصة اللعبة (لهجة لواو) |
| **عالم علب** | البرمجة النصية لواجهة المستخدم (Lua) |
| **نيوفيم** | محرر (برمجة لوا) |
| **ريديس** | البرمجة النصية Lua في Redis |
| ** نجينكس / أوبن ريستي ** | برمجة Lua في Nginx |
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

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **رمز VS + لوا (سومنيكو)** | أفضل لوا LSP |
| ** استوديو ZeroBrane ** | IDE الخاص بلوا |
| **نيوفيم** | تكوين لوا (درجة أولى) |
| **IntelliJ + EmmyLua** | دعم JetBrains لوا |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| ** مستقل ** | حزمة Lua مع التطبيق |
| ** لوا روكس ** | التعبئة والتوزيع |
| **أوبن ريستي** | نشر Nginx + Lua |
| ** عامل الميناء ** | في حاويات |
| **مضمن** | في تطبيقات C/C++ |
| **منصات اللعبة** | الحب، ديفولد، روبلوكس |
---

## ملخص
نظام Lua البيئي صغير ولكنه يركز على التضمين والبرمجة النصية. سلسلة الأدوات القياسية هي: **Lua 5.4** أو **LuaJIT** كوقت تشغيل، **LuaRocks** للحزم، **busted** للاختبار، **luacheck** للفحص، **stylua** للتنسيق. تتفوق Lua كلغة مدمجة في الألعاب (LÖVE، وDefold، وRoblox)، والخوادم (OpenResty، وNginx)، وقواعد البيانات (Redis)، والمحررين (Neovim). يوفر LuaJIT أداء قريب من لغة C للبرامج النصية التي تتطلب حوسبة مكثفة. تتمثل نقاط قوة Lua في حجمها الصغير (حوالي 25 كيلو بايت)، وبناء الجملة البسيط، وواجهة برمجة تطبيقات التضمين الممتازة لتكامل C/C++.