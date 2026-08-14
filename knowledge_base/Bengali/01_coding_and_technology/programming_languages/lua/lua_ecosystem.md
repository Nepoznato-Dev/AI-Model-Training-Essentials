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
# লুয়া — ইকোসিস্টেম এবং টুলিং গাইড
এই গাইডটি লুয়া ইকোসিস্টেমের প্রয়োজনীয় টুলস, লাইব্রেরি এবং অবকাঠামো কভার করে।
---

## লুয়া সংস্করণ এবং বাস্তবায়ন
| বাস্তবায়ন | নোট |
|---------------|---------|
| **লুয়া ৫.৪** | বর্তমান স্থিতিশীল সংস্করণ |
| **লুয়াজিট** | উচ্চ-কর্মক্ষমতা JIT কম্পাইলার |
| **লুয়া ৫.১** | ব্যাপকভাবে ব্যবহৃত (LuaJIT সামঞ্জস্যপূর্ণ) |
| **রবি** | ঐচ্ছিক টাইপিং সহ JIT |
| **টিল** | লুয়ার টাইপ করা উপভাষা |
| **মৌরি** | লিস্প যে লুয়াতে কম্পাইল করে |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **LuaRocks** | স্ট্যান্ডার্ড প্যাকেজ ম্যানেজার |
| **luarocks.org** | প্যাকেজ ভান্ডার |
| **আলো** | LuaJIT প্যাকেজ ম্যানেজার |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **ওপেনরেস্টি** | Nginx + Lua | হাই-পারফরম্যান্স ওয়েব |
| **লুভিট** | Node.js-এর মতো | Async I/O (libuv) |
| **কক্ষপথ** | MVC ওয়েব | সহজ ওয়েব অ্যাপস |
| **নাবিক** | ফুল-স্ট্যাক | MVC ফ্রেমওয়ার্ক |
| **লাপিস** | OpenResty-ভিত্তিক | মুনস্ক্রিপ্ট/লুয়া ওয়েব |
| **পেগাসাস** | লাইটওয়েট | সহজ HTTP সার্ভার |
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

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **luasql** | ডাটাবেস বাইন্ডিং (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | মাইএসকিউএল (ওপেনরেস্টি) |
| **লুয়া-রেস্টি-রেডিস** | রেডিস (ওপেনরেস্টি) |
| **lsqlite3** | SQLite3 বাইন্ডিং |
| **pgmoon** | PostgreSQL (বিশুদ্ধ লুয়া) |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **ভাঙ্গা* | বিডিডি-স্টাইল টেস্টিং (সবচেয়ে জনপ্রিয়) |
| **লাসার্ট** | অ্যাসারশন লাইব্রেরি (বাস্টেড) |
| **লালসা** | ন্যূনতম পরীক্ষা |
| **পাগলতম** | xUnit-শৈলী পরীক্ষা |
| **টিল** | টাইপ চেকিং (টিল উপভাষা) |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **লুচেক** | লিন্টিং এবং স্ট্যাটিক বিশ্লেষণ |
| **লুয়া-ফরম্যাট** | কোড ফরম্যাটিং |
| **স্টাইলুয়া** | কোড ফরম্যাটার (মরিচা-ভিত্তিক, দ্রুত) |
| **টিল** | টাইপ করা লুয়া উপভাষা |
| **লুকভ** | কোড কভারেজ |
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

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **লুয়াসকেট** | TCP/UDP/HTTP নেটওয়ার্কিং |
| **lua-cjson / cjson** | JSON পার্সিং |
| **lpeg** | প্যাটার্ন ম্যাচিং (PEG-ভিত্তিক) |
| **পেনলাইট (pl)** | ইউটিলিটি লাইব্রেরি (যেমন পাইথন stdlib) |
| **কপাস** | Coroutine-ভিত্তিক সকেট |
| **কক্সপকল** | সুরক্ষিত কল |
| **লুয়া-রেস্টি-* | OpenResty ইকোসিস্টেম |
| **lfs** | ফাইল সিস্টেম অ্যাক্সেস |
| **lzlib** | কম্প্রেশন |
| **lbase64** | Base64 এনকোডিং |
| **পরিদর্শন** | টেবিল সুন্দর-মুদ্রণ |
| **শাস্ত্রীয়** | ওওপি ক্লাস সিস্টেম |
| **মধ্যবিত্ত** | OOP লাইব্রেরি |
| **লালসা** | গোঁফ টেমপ্লেট |
| **আর্গপার্স** | CLI যুক্তি পার্সিং |
---

## গেম ডেভেলপমেন্ট
| ইঞ্জিন | নোট |
|---------|-------|
| **লাভ (লাভ2ডি)** | 2D গেম ফ্রেমওয়ার্ক (সবচেয়ে জনপ্রিয়) |
| **ফোল্ড** | গেম ইঞ্জিন (লুয়া স্ক্রিপ্টিং) |
| **করোনা SDK** | মোবাইল গেম ইঞ্জিন |
| **রোবলক্স** | গেম প্ল্যাটফর্ম (লুয়াউ উপভাষা) |
| **ওয়ারক্র্যাফটের বিশ্ব** | UI স্ক্রিপ্টিং (Lua) |
| **নিওভিম** | সম্পাদক (লুয়া স্ক্রিপ্টিং) |
| **রেডিস** | রেডিসে লুয়া স্ক্রিপ্টিং |
| **এনগিনেক্স/ওপেনরেস্টি** | Nginx এ লুয়া স্ক্রিপ্টিং |
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

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ভিএস কোড + লুয়া (সুমনেকো)** | সেরা লুয়া এলএসপি |
| **জিরোব্রেন স্টুডিও** | লুয়া-নির্দিষ্ট IDE |
| **নিওভিম** | লুয়া কনফিগারেশন (প্রথম-শ্রেণী) |
| **IntelliJ + EmmyLua** | JetBrains লুয়া সমর্থন |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **স্বতন্ত্র** | অ্যাপ সহ লুয়া বান্ডিল |
| **LuaRocks** | প্যাকেজ এবং বিতরণ |
| **ওপেনরেস্টি** | Nginx + Lua স্থাপনা |
| **ডকার** | কন্টেইনারাইজড |
| **এম্বেড করা** | C/C++ অ্যাপ্লিকেশনে |
| **গেম প্ল্যাটফর্ম** | LÖVE, Defold, Roblox |
---

## সারাংশ
লুয়ার ইকোসিস্টেম ছোট কিন্তু এমবেডিং এবং স্ক্রিপ্টিংয়ের উপর দৃষ্টি নিবদ্ধ করে। স্ট্যান্ডার্ড টুলচেন হল: **Lua 5.4** বা **LuaJIT** রানটাইম হিসাবে, **প্যাকেজের জন্য **LuaRocks**, পরীক্ষার জন্য **বাস্টেড**, লিন্টিংয়ের জন্য **লুচেক**, বিন্যাস করার জন্য **স্টাইলুয়া**। লুয়া গেমস (LÖVE, Defold, Roblox), সার্ভার (OpenResty, Nginx), ডেটাবেস (Redis) এবং সম্পাদক (Neovim) এ এমবেডেড ভাষা হিসেবে পারদর্শী। LuaJIT কম্পিউট-ইনটেনসিভ স্ক্রিপ্টগুলির জন্য কাছাকাছি-সি কর্মক্ষমতা প্রদান করে। লুয়ার শক্তি হল এর ক্ষুদ্র পদচিহ্ন (~25KB), সাধারণ সিনট্যাক্স, এবং C/C++ ইন্টিগ্রেশনের জন্য চমৎকার এম্বেডিং API।