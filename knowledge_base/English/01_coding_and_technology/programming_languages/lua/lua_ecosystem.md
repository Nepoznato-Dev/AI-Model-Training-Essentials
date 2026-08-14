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
# Lua — Ecosystem & Tooling Guide

This guide covers the essential tools, libraries, and infrastructure in the Lua ecosystem.

---

## Lua Versions & Implementations

| Implementation | Notes |
|---------------|-------|
| **Lua 5.4** | Current stable version |
| **LuaJIT** | High-performance JIT compiler |
| **Lua 5.1** | Widely used (LuaJIT compatible) |
| **Ravi** | JIT with optional typing |
| **Teal** | Typed dialect of Lua |
| **fennel** | Lisp that compiles to Lua |

```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Package Management

| Tool | Purpose |
|------|---------|
| **LuaRocks** | Standard package manager |
| **luarocks.org** | Package repository |
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

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | High-performance web |
| **Luvit** | Node.js-like | Async I/O (libuv) |
| **Orbit** | MVC web | Simple web apps |
| **Sailor** | Full-stack | MVC framework |
| **lapis** | OpenResty-based | MoonScript/Lua web |
| **Pegasus** | Lightweight | Simple HTTP server |

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

| Technology | Type |
|------------|------|
| **luasql** | Database bindings (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | SQLite3 bindings |
| **pgmoon** | PostgreSQL (pure Lua) |

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

## Testing

| Framework | Purpose |
|-----------|---------|
| **busted** | BDD-style testing (most popular) |
| **luassert** | Assertion library (busted) |
| **lust** | Minimal testing |
| **lunatest** | xUnit-style testing |
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

## Code Quality

| Tool | Purpose |
|------|---------|
| **luacheck** | Linting and static analysis |
| **lua-format** | Code formatting |
| **stylua** | Code formatter (Rust-based, fast) |
| **teal** | Typed Lua dialect |
| **luacov** | Code coverage |

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

## Key Libraries

| Library | Purpose |
|---------|---------|
| **luasocket** | TCP/UDP/HTTP networking |
| **lua-cjson / cjson** | JSON parsing |
| **lpeg** | Pattern matching (PEG-based) |
| **Penlight (pl)** | Utility library (like Python stdlib) |
| **copas** | Coroutine-based socket |
| **coxpcall** | Protected calls |
| **lua-resty-* | OpenResty ecosystem |
| **lfs** | File system access |
| **lzlib** | Compression |
| **lbase64** | Base64 encoding |
| **inspect** | Table pretty-printing |
| **classical** | OOP class system |
| **middleclass** | OOP library |
| **lustache** | Mustache templates |
| **argparse** | CLI argument parsing |

---

## Game Development

| Engine | Notes |
|--------|-------|
| **LÖVE (Love2D)** | 2D game framework (most popular) |
| **Defold** | Game engine (Lua scripting) |
| **Corona SDK** | Mobile game engine |
| **Roblox** | Game platform (Luau dialect) |
| **World of Warcraft** | UI scripting (Lua) |
| **Neovim** | Editor (Lua scripting) |
| **Redis** | Lua scripting in Redis |
| **Nginx/OpenResty** | Lua scripting in Nginx |

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

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + Lua (sumneko)** | Best Lua LSP |
| **ZeroBrane Studio** | Lua-specific IDE |
| **Neovim** | Lua configuration (first-class) |
| **IntelliJ + EmmyLua** | JetBrains Lua support |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Standalone** | Bundle Lua with app |
| **LuaRocks** | Package and distribute |
| **OpenResty** | Nginx + Lua deployment |
| **Docker** | Containerized |
| **Embedded** | Into C/C++ applications |
| **Game platforms** | LÖVE, Defold, Roblox |

---

## Summary

Lua's ecosystem is small but focused on embedding and scripting. The standard toolchain is: **Lua 5.4** or **LuaJIT** as runtime, **LuaRocks** for packages, **busted** for testing, **luacheck** for linting, **stylua** for formatting. Lua excels as an embedded language in games (LÖVE, Defold, Roblox), servers (OpenResty, Nginx), databases (Redis), and editors (Neovim). LuaJIT provides near-C performance for compute-intensive scripts. Lua's strengths are its tiny footprint (~25KB), simple syntax, and excellent embedding API for C/C++ integration.
