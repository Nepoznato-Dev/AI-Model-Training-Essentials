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
# Lua – Leitfaden für Ökosysteme und Werkzeuge
Dieser Leitfaden behandelt die wesentlichen Tools, Bibliotheken und Infrastruktur im Lua-Ökosystem.
---

## Lua-Versionen und -Implementierungen
| Umsetzung | Notizen |
|---------------|-------|
| **Lua 5.4** | Aktuelle stabile Version |
| **LuaJIT** | Hochleistungs-JIT-Compiler |
| **Lua 5.1** | Weit verbreitet (LuaJIT-kompatibel) |
| **Ravi** | JIT mit optionaler Typisierung |
| **Blaugrün** | Typisierter Dialekt von Lua |
| **Fenchel** | Lisp, das zu Lua | kompiliert wird
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **LuaRocks** | Standardpaketmanager |
| **luarocks.org** | Paket-Repository |
| **beleuchtet** | LuaJIT-Paketmanager |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | Hochleistungs-Web |
| **Luvit** | Node.js-ähnlich | Asynchrone E/A (libuv) |
| **Umlaufbahn** | MVC-Web | Einfache Web-Apps |
| **Matrose** | Full-Stack | MVC-Framework |
| **Lapis** | OpenResty-basiert | MoonScript/Lua-Web |
| **Pegasus** | Leicht | Einfacher HTTP-Server |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **luaql** | Datenbankbindungen (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | SQLite3-Bindungen |
| **pgmoon** | PostgreSQL (reines Lua) |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **kaputt** | Tests im BDD-Stil (am beliebtesten) |
| **luassert** | Assertion-Bibliothek (kaputt) |
| **Lust** | Minimale Tests |
| **wahnsinnig** | Tests im xUnit-Stil |
| **blaugrün** | Typprüfung (Teal-Dialekt) |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **luacheck** | Flusen- und statische Analyse |
| **Lua-Format** | Codeformatierung |
| **Stift** | Codeformatierer (Rust-basiert, schnell) |
| **blaugrün** | Typisierter Lua-Dialekt |
| **luacov** | Codeabdeckung |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Luasocket** | TCP/UDP/HTTP-Netzwerk |
| **lua-cjson / cjson** | JSON-Analyse |
| **lpeg** | Mustervergleich (PEG-basiert) |
| **Taschenlampe (pl)** | Dienstprogrammbibliothek (wie Python stdlib) |
| **Copas** | Coroutine-basierter Socket |
| **coxpcall** | Geschützte Anrufe |
| **lua-resty-* | OpenResty-Ökosystem |
| **lfs** | Dateisystemzugriff |
| **lzlib** | Komprimierung |
| **lbase64** | Base64-Kodierung |
| **inspizieren** | Tabelle hübsch-drucken |
| **klassisch** | OOP-Klassensystem |
| **Mittelklasse** | OOP-Bibliothek |
| **Lustschmerz** | Schnurrbart-Vorlagen |
| **argparse** | CLI-Argumentanalyse |
---

## Spieleentwicklung
| Motor | Notizen |
|--------|-------|
| **LIEBE (Love2D)** | 2D-Spiel-Framework (am beliebtesten) |
| **Entfalten** | Spiel-Engine (Lua-Scripting) |
| **Corona SDK** | Mobile Spiel-Engine |
| **Roblox** | Spielplattform (Luau-Dialekt) |
| **World of Warcraft** | UI-Skripting (Lua) |
| **Neovim** | Editor (Lua-Skripting) |
| **Redis** | Lua-Skripting in Redis |
| **Nginx/OpenResty** | Lua-Skripting in Nginx |
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

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + Lua (Sumneko)** | Bester Lua-LSP |
| **ZeroBrane Studio** | Lua-spezifische IDE |
| **Neovim** | Lua-Konfiguration (erstklassig) |
| **IntelliJ + EmmyLua** | JetBrains Lua-Unterstützung |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Standalone** | Lua mit App bündeln |
| **LuaRocks** | Verpacken und verteilen |
| **OpenResty** | Nginx + Lua-Bereitstellung |
| **Docker** | Containerisiert |
| **Eingebettet** | In C/C++-Anwendungen |
| **Spielplattformen** | LÖVE, Defold, Roblox |
---

## Zusammenfassung
Das Ökosystem von Lua ist klein, konzentriert sich aber auf Einbettung und Skripterstellung. Die Standard-Toolchain ist: **Lua 5.4** oder **LuaJIT** als Laufzeit, **LuaRocks** für Pakete, **busted** zum Testen, **luacheck** für Linting, **Stylua** für die Formatierung. Lua zeichnet sich als eingebettete Sprache in Spielen (LÖVE, Defold, Roblox), Servern (OpenResty, Nginx), Datenbanken (Redis) und Editoren (Neovim) aus. LuaJIT bietet nahezu C-Leistung für rechenintensive Skripte. Die Stärken von Lua sind der geringe Platzbedarf (~25 KB), die einfache Syntax und die hervorragende Einbettungs-API für die C/C++-Integration.