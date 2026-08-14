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
# Lua — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang kasangkapan, aklatan, at imprastraktura sa ecosystem ng Lua.
---

## Mga Bersyon at Pagpapatupad ng Lua
| Pagpapatupad | Mga Tala |
|--------------|-------|
| **Lua 5.4** | Kasalukuyang stable na bersyon |
| **LuaJIT** | Mataas na pagganap ng JIT compiler |
| **Lua 5.1** | Malawakang ginagamit (LuaJIT compatible) |
| **Ravi** | JIT na may opsyonal na pag-type |
| **Teal** | Type na dialect ng Lua |
| ** haras** | Lisp na nag-compile sa Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **LuaRocks** | Karaniwang tagapamahala ng pakete |
| **luarocks.org** | Imbakan ng package |
| **lit** | LuaJIT package manager |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | Mataas na pagganap ng web |
| **Luvit** | Node.js-like | Async I/O (libuv) |
| **Orbit** | MVC web | Mga simpleng web app |
| **Sailor** | Full-stack | MVC framework |
| **lapis** | Nakabatay sa OpenResty | MoonScript/Lua web |
| **Pegasus** | Magaan | Simpleng HTTP server |
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

## Database
| Teknolohiya | Uri |
|------------|------|
| **luasql** | Mga binding ng database (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | SQLite3 bindings |
| **pgmoon** | PostgreSQL (purong Lua) |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **busted** | BDD-style na pagsubok (pinakatanyag) |
| **luassert** | Assertion library (busted) |
| **pagnanasa** | Minimal na pagsubok |
| **lunatest** | xUnit-style na pagsubok |
| **teal** | Type checking (Teal dialect) |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **luacheck** | Linting at static na pagsusuri |
| **lua-format** | Pag-format ng code |
| **stylua** | Taga-format ng code (Batay sa kalawang, mabilis) |
| **teal** | Nag-type ng Lua dialect |
| **luacov** | Saklaw ng code |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **luasocket** | TCP/UDP/HTTP networking |
| **lua-cjson / cjson** | Pag-parse ng JSON |
| **lpeg** | Pagtutugma ng pattern (batay sa PEG) |
| **Penlight (pl)** | Utility library (tulad ng Python stdlib) |
| **copas** | Coroutine-based na socket |
| **coxpcall** | Mga protektadong tawag |
| **lua-resty-* | OpenResty ecosystem |
| **lfs** | Access sa file system |
| **lzlib** | Compression |
| **lbase64** | Base64 encoding |
| **siyasatin** | Table pretty-printing |
| **klasikal** | Sistema ng klase ng OOP |
| **middleclass** | OOP library |
| **lustache** | Mga template ng bigote |
| **argparse** | CLI argument parsing |
---

## Pagbuo ng Laro
| Makina | Mga Tala |
|--------|-------|
| **LÖVE (Love2D)** | 2D game framework (pinakatanyag) |
| **Defold** | Game engine (Lua scripting) |
| **Corona SDK** | Mobile game engine |
| **Roblox** | Platform ng laro (dialect ng Luau) |
| **Mundo ng Warcraft** | UI scripting (Lua) |
| **Neovim** | Editor (Lua scripting) |
| **Redis** | Lua scripting sa Redis |
| **Nginx/OpenResty** | Lua scripting sa Nginx |
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

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + Lua (sumneko)** | Pinakamahusay na Lua LSP |
| **ZeroBrane Studio** | IDE na partikular sa Lua |
| **Neovim** | Lua configuration (first-class) |
| **IntelliJ + EmmyLua** | Suporta ng JetBrains Lua |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Standalone** | Bundle ang Lua gamit ang app |
| **LuaRocks** | I-package at ipamahagi |
| **OpenResty** | Pag-deploy ng Nginx + Lua |
| **Docker** | Naka-container |
| **Naka-embed** | Sa mga C/C++ na application |
| **Mga platform ng laro** | LÖVE, Defold, Roblox |
---

## Buod
Maliit ang ecosystem ni Lua ngunit nakatutok sa pag-embed at pag-script. Ang karaniwang toolchain ay: **Lua 5.4** o **LuaJIT** bilang runtime, **LuaRocks** para sa mga package, **busted** para sa pagsubok, **luacheck** para sa linting, **stylua** para sa pag-format. Napakahusay ng Lua bilang isang naka-embed na wika sa mga laro (LÖVE, Defold, Roblox), mga server (OpenResty, Nginx), mga database (Redis), at mga editor (Neovim). Nagbibigay ang LuaJIT ng malapit-C na pagganap para sa mga script na masinsinang mag-compute. Ang mga kalakasan ni Lua ay ang maliit nitong footprint (~25KB), simpleng syntax, at mahusay na pag-embed ng API para sa pagsasama ng C/C++.