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
# Lua — Ekosistem ve Takımlama Kılavuzu
Bu kılavuz Lua ekosistemindeki temel araçları, kitaplıkları ve altyapıyı kapsar.
---

## Lua Sürümleri ve Uygulamaları
| Uygulama | Notlar |
|---------------|----------|
| **Lua 5.4** | Güncel kararlı sürüm |
| **LuaJIT** | Yüksek performanslı JIT derleyicisi |
| **Lua 5.1** | Yaygın olarak kullanılır (LuaJIT uyumlu) |
| **Ravi** | İsteğe bağlı yazma özelliğiyle JIT |
| **Turuncu** | Lua'nın yazılı lehçesi |
| **rezene** | Lua'ya derlenen Lisp |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **LuaRocks** | Standart paket yöneticisi |
| **luarocks.org** | Paket deposu |
| **yandı** | LuaJIT paket yöneticisi |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **AçıkResty** | Nginx + Lua | Yüksek performanslı web |
| **Lüvit** | Node.js benzeri | Zaman uyumsuz G/Ç (libuv) |
| **Yörünge** | MVC ağı | Basit web uygulamaları |
| **Denizci** | Tam yığın | MVC çerçevesi |
| **lapis** | OpenResty tabanlı | MoonScript/Lua web |
| **Pegasus** | Hafif | Basit HTTP sunucusu |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **luasql** | Veritabanı bağlamaları (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | SQLite3 bağlamaları |
| **pgmoon** | PostgreSQL (saf Lua) |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **basıldı** | BDD tarzı testler (en popüler) |
| **luassert** | İddia kitaplığı (bastırıldı) |
| **şehvet** | Minimum test |
| **lunatest** | xUnit tarzı test |
| **turuncu** | Tip kontrolü (Turuncu lehçesi) |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **luacheck** | Linting ve statik analiz |
| **lua-formatı** | Kod biçimlendirme |
| **stylua** | Kod biçimlendirici (Pas tabanlı, hızlı) |
| **turuncu** | Yazılan Lua lehçesi |
| **luacov** | Kod kapsamı |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **luasocket** | TCP/UDP/HTTP ağı |
| **lua-cjson / cjson** | JSON ayrıştırma |
| **lpeg** | Desen eşleştirme (PEG tabanlı) |
| **Kalem ışığı (pl)** | Yardımcı program kitaplığı (Python stdlib gibi) |
| **copas** | Coroutine tabanlı soket |
| **coxpcall** | Korumalı aramalar |
| **lua-resty-* | OpenResty ekosistemi |
| **lfs** | Dosya sistemi erişimi |
| **lzlib** | Sıkıştırma |
| **lbase64** | Base64 kodlaması |
| **inceleme** | Tablo güzel baskı |
| **klasik** | OOP sınıf sistemi |
| **orta sınıf** | OOP kütüphanesi |
| **şehvet** | Bıyık şablonları |
| **argparse** | CLI bağımsız değişkeni ayrıştırma |
---

## Oyun Geliştirme
| Motor | Notlar |
|----------|----------|
| **AŞK (Aşk2D)** | 2D oyun çerçevesi (en popüler) |
| **Katlama** | Oyun motoru (Lua komut dosyası oluşturma) |
| **Corona SDK'sı** | Mobil oyun motoru |
| **Roblox** | Oyun platformu (Luau lehçesi) |
| **World of Warcraft** | Kullanıcı arayüzü komut dosyası oluşturma (Lua) |
| **Neovim** | Editör (Lua komut dosyası oluşturma) |
| **Redis** | Redis'te Lua komut dosyası oluşturma |
| **Nginx/OpenResty** | Nginx'te Lua komut dosyası oluşturma |
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

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + Lua (toplam)** | En İyi Lua LSP |
| **ZeroBrane Stüdyosu** | Lua'ya özgü IDE |
| **Neovim** | Lua konfigürasyonu (birinci sınıf) |
| **IntelliJ + EmmyLua** | JetBrains Lua desteği |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Bağımsız** | Lua'yı uygulamayla paketle |
| **LuaRocks** | Paketleyin ve dağıtın |
| **AçıkResty** | Nginx + Lua dağıtımı |
| **Docker** | Konteynerde |
| **Gömülü** | C/C++ uygulamalarına |
| **Oyun platformları** | AŞK, Defold, Roblox |
---

## Özet
Lua'nın ekosistemi küçüktür ancak yerleştirme ve komut dosyası oluşturmaya odaklanmıştır. Standart araç zinciri şu şekildedir: Çalışma zamanı olarak **Lua 5.4** veya **LuaJIT**, paketler için **LuaRocks**, test için **busted**, astarlama için **luacheck**, biçimlendirme için **stylua**. Lua, oyunlarda (LÖVE, Defold, Roblox), sunucularda (OpenResty, Nginx), veritabanlarında (Redis) ve editörlerde (Neovim) yerleşik bir dil olarak öne çıkıyor. LuaJIT, yoğun bilgi işlem gerektiren komut dosyaları için C'ye yakın performans sağlar. Lua'nın güçlü yönleri, küçük kaplama alanı (~25KB), basit sözdizimi ve C/C++ entegrasyonu için mükemmel yerleştirme API'sidir.