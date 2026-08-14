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
# Lua — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, perpustakaan, dan infrastruktur penting dalam ekosistem Lua.
---

## Versi & Implementasi Lua
| Implementasi | Catatan |
|---------------|-------|
| **Lua 5.4** | Versi stabil saat ini |
| **LuaJIT** | Kompiler JIT berkinerja tinggi |
| **Lua 5.1** | Banyak digunakan (kompatibel dengan LuaJIT) |
| **Ravi** | JIT dengan pengetikan opsional |
| **Teal** | Dialek yang diketik dari Lua |
| **adas** | Cadel yang dikompilasi ke Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **LuaRocks** | Manajer paket standar |
| **luarocks.org** | Repositori paket |
| **menyala** | Manajer paket LuaJIT |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | Web berkinerja tinggi |
| **Luvit** | Seperti Node.js | I/O asinkron (libuv) |
| **Orbit** | web MVC | Aplikasi web sederhana |
| **Pelaut** | Tumpukan penuh | Kerangka kerja MVC |
| **lapis** | Berbasis OpenResty | MoonScript/Lua web |
| **Pegasus** | Ringan | Server HTTP sederhana |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **luasql** | Pengikatan basis data (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Pengikatan SQLite3 |
| **pgbulan** | PostgreSQL (Lua murni) |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **rusak** | Pengujian gaya BDD (paling populer) |
| **luassert** | Perpustakaan pernyataan (rusak) |
| **nafsu** | Minimal pengujian |
| **paling gila** | pengujian gaya xUnit |
| **teal** | Pemeriksaan jenis (dialek Teal) |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **luacheck** | Analisis linting dan statis |
| **format lua** | Pemformatan kode |
| **gaya** | Pemformat kode (berbasis karat, cepat) |
| **teal** | Dialek Lua yang diketik |
| **luacov** | Cakupan kode |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **luasocket** | Jaringan TCP/UDP/HTTP |
| **lua-cjson / cjson** | Penguraian JSON |
| **lpeg** | Pencocokan pola (berbasis PEG) |
| **Penlight (pl)** | Pustaka utilitas (seperti Python stdlib) |
| **copas** | Soket berbasis coroutine |
| **panggilan coxp** | Panggilan dilindungi |
| **lua-resty-* | Ekosistem OpenResty |
| **lfs** | Akses sistem file |
| **lzlib** | Kompresi |
| **lbase64** | Pengkodean Base64 |
| **periksa** | Meja cantik-cetakan |
| **klasik** | sistem kelas OOP |
| **kelas menengah** | perpustakaan OOP |
| **sakit nafsu makan** | Templat kumis |
| **argparse** | Penguraian argumen CLI |
---

## Pengembangan Game
| Mesin | Catatan |
|--------|-------|
| **CINTA (Cinta2D)** | Kerangka permainan 2D (paling populer) |
| **Buka lipatannya** | Mesin permainan (skrip Lua) |
| **SDK Korona** | Mesin game seluler |
| **Roblox** | Platform permainan (dialek Luau) |
| **Dunia Warcraft** | Skrip UI (Lua) |
| **Neovim** | Editor (skrip Lua) |
| **Redis** | Skrip Lua di Redis |
| **Nginx/OpenResty** | Skrip Lua di Nginx |
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

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + Lua (sumneko)** | Lua LSP Terbaik |
| **ZeroBrane Studio** | IDE khusus Lua |
| **Neovim** | Konfigurasi Lua (kelas satu) |
| **IntelliJ + EmmyLua** | Dukungan JetBrains Lua |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Mandiri** | Bundel Lua dengan aplikasi |
| **LuaRocks** | Kemas dan distribusikan |
| **OpenResty** | Penerapan Nginx + Lua |
| **Buruh pelabuhan** | dalam kontainer |
| **Tertanam** | Ke dalam aplikasi C/C++ |
| **Platform permainan** | CINTA, Buka lipatan, Roblox |
---

## Ringkasan
Ekosistem Lua kecil namun fokus pada penyematan dan pembuatan skrip. Toolchain standarnya adalah: **Lua 5.4** atau **LuaJIT** sebagai runtime, **LuaRocks** untuk paket, **rusak** untuk pengujian, **luacheck** untuk linting, **stylua** untuk pemformatan. Lua unggul sebagai bahasa yang tertanam dalam game (LÖVE, Defold, Roblox), server (OpenResty, Nginx), database (Redis), dan editor (Neovim). LuaJIT memberikan kinerja mendekati C untuk skrip komputasi intensif. Kekuatan Lua adalah ukurannya yang kecil (~25KB), sintaksis yang sederhana, dan API penyematan yang sangat baik untuk integrasi C/C++.