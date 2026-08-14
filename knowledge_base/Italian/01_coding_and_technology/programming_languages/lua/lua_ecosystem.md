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
# Lua: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, le librerie e le infrastrutture essenziali nell'ecosistema Lua.
---

## Versioni e implementazioni Lua
| Attuazione | Note |
|---------------|-------|
| **Lua 5.4** | Versione stabile attuale |
| **LuaJIT** | Compilatore JIT ad alte prestazioni |
| **Lua 5.1** | Ampiamente usato (compatibile con LuaJIT) |
| **Ravi** | JIT con digitazione opzionale |
| **Alzavola** | Dialetto digitato di Lua |
| **finocchio** | Lisp che compila in Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **LuaRocks** | Gestore pacchetti standard |
| **luarocks.org** | Repository dei pacchetti |
| **acceso** | Gestore pacchetti LuaJIT |
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

## Framework Web
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | Rete ad alte prestazioni |
| **Luvit** | Simile a Node.js | I/O asincrono (libuv) |
| **Orbita** | Web MVC | App Web semplici |
| **Marinaio** | Stack completo | Quadro MVC |
| **lapis** | Basato su OpenResty | MoonScript/Lua web |
| **Pegaso** | Leggero | Server HTTP semplice |
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

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **luasql** | Collegamenti al database (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Associazioni SQLite3 |
| **pgluna** | PostgreSQL (Lua puro) |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **sballato** | Test in stile BDD (più popolari) |
| **luassert** | Libreria di asserzioni (rotta) |
| **lussuria** | Test minimi |
| **lunatest** | Test in stile xUnit |
| **verde acqua** | Controllo del tipo (dialetto verde acqua) |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **luacheck** | Linting e analisi statica |
| **formato lua** | Formattazione del codice |
| **stile** | Formattatore di codice (basato su Rust, veloce) |
| **verde acqua** | Digitato dialetto Lua |
| **luacov** | Copertura del codice |
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

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **luasocket** | Reti TCP/UDP/HTTP |
| **lua-cjson / cjson** | Analisi JSON |
| **lpeg** | Corrispondenza di modelli (basata su PEG) |
| **Penlight (pl)** | Libreria di utilità (come Python stdlib) |
| **copa** | Socket basato su coroutine |
| **coxpcall** | Chiamate protette |
| **lua-resty-* | Ecosistema OpenResty |
| **lfs** | Accesso al file system |
| **lzlib** | Compressione |
| **lbase64** | Codifica Base64 |
| **ispezionare** | Tabella bella stampa |
| **classico** | Sistema di classi OOP |
| **classe media** | Libreria OOP |
| **baffi** | Modelli di baffi |
| **argparse** | Analisi degli argomenti CLI |
---

## Sviluppo di giochi
| Motore | Note |
|--------|-------|
| **AMORE (Amore2D)** | Quadro di gioco 2D (il più popolare) |
| **Defold** | Motore di gioco (scripting Lua) |
| **SDK Corona** | Motore di gioco mobile |
| **Roblox** | Piattaforma di gioco (dialetto Luau) |
| **Mondo di Warcraft** | Script dell'interfaccia utente (Lua) |
| **Neovim** | Editor (scripting Lua) |
| **Redis** | Scripting Lua in Redis |
| **Nginx/OpenResty** | Scripting Lua in Nginx |
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

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + Lua (sumneko)** | Miglior Lua LSP |
| **ZeroBrane Studio** | IDE specifico per Lua |
| **Neovim** | Configurazione Lua (prima classe) |
| **IntelliJ + EmmyLua** | Supporto JetBrains Lua |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Indipendente** | Pacchetto Lua con l'app |
| **LuaRocks** | Imballa e distribuisci |
| **OpenResty** | Distribuzione Nginx + Lua |
| **Docker** | Containerizzato |
| **Incorporato** | Nelle applicazioni C/C++ |
| **Piattaforme di gioco** | AMORE, Defold, Roblox |
---

## Riepilogo
L'ecosistema di Lua è piccolo ma focalizzato sull'incorporamento e sullo scripting. La toolchain standard è: **Lua 5.4** o **LuaJIT** come runtime, **LuaRocks** per i pacchetti, **busted** per i test, **luacheck** per linting, **stylua** per la formattazione. Lua eccelle come linguaggio incorporato nei giochi (LÖVE, Defold, Roblox), server (OpenResty, Nginx), database (Redis) ed editor (Neovim). LuaJIT fornisce prestazioni quasi C per script ad alta intensità di calcolo. I punti di forza di Lua sono il suo ingombro ridotto (~25KB), la sintassi semplice e l'eccellente API di incorporamento per l'integrazione C/C++.