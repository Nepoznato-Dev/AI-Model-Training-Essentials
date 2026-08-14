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
# Lua — Przewodnik po ekosystemie i narzędziach
W tym przewodniku opisano podstawowe narzędzia, biblioteki i infrastrukturę w ekosystemie Lua.
---

## Wersje i implementacje Lua
| Wdrożenie | Notatki |
|--------------|-------|
| **Lua 5.4** | Aktualna stabilna wersja |
| **LuaJIT** | Wysokowydajny kompilator JIT |
| **Lua 5.1** | Szeroko stosowany (kompatybilny z LuaJIT) |
| **Ravi** | JIT z opcjonalnym wpisywaniem |
| **Turkusowy** | Wpisany dialekt Lua |
| **koper** | Lisp kompilujący do Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **LuaRock** | Menedżer pakietów standardowych |
| **luarocks.org** | Repozytorium pakietów |
| **świeci** | Menedżer pakietów LuaJIT |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **OpenResty** | Nginx + Lua | Sieć o wysokiej wydajności |
| **Luvit** | Podobny do Node.js | Asynchroniczne we/wy (libuv) |
| **Orbita** | Sieć MVC | Proste aplikacje internetowe |
| **Żeglarz** | Pełny stos | framework MVC |
| **lapis** | Oparte na OpenResty | Sieć MoonScript/Lua |
| **Pegaz** | Lekki | Prosty serwer HTTP |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **luasql** | Powiązania z bazami danych (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Powiązania SQLite3 |
| **pgmoon** | PostgreSQL (czysty Lua) |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **przyłapany** | Testowanie w stylu BDD (najpopularniejsze) |
| **luasert** | Biblioteka asercji (odpadła) |
| **pożądanie** | Minimalne testowanie |
| **najbardziej lunatyczny** | Testowanie w stylu xUnit |
| **turkusowy** | Sprawdzanie typu (dialekt turkusowy) |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **luacheck** | Linting i analiza statyczna |
| **format lua** | Formatowanie kodu |
| **stylu** | Formater kodu (oparty na rdzy, szybki) |
| **turkusowy** | Wpisano dialekt Lua |
| **luakov** | Pokrycie kodu |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **luasocket** | Sieci TCP/UDP/HTTP |
| **lua-cjson / cjson** | Analiza JSON |
| **LPEG** | Dopasowywanie wzorców (oparte na PEG) |
| **Lampa ołówkowa** | Biblioteka narzędziowa (jak Python stdlib) |
| **kopa** | Gniazdo oparte na współprogramie |
| **coxpcall** | Połączenia chronione |
| **lua-resty-* | Ekosystem OpenResty |
| **lfs** | Dostęp do systemu plików |
| **lzlib** | Kompresja |
| **lbase64** | Kodowanie Base64 |
| **sprawdź** | Stół ładny-drukowanie |
| **klasyczny** | System klasy OOP |
| **klasa średnia** | Biblioteka OOP |
| **lusta** | Szablony wąsów |
| **analiza arg** | Analiza argumentów CLI |
---

## Tworzenie gier
| Silnik | Notatki |
|------------|-------|
| **MIŁOŚĆ (Love2D)** | Framework do gier 2D (najpopularniejszy) |
| **Rozłóż** | Silnik gry (skrypty Lua) |
| **Korona SDK** | Silnik gier mobilnych |
| **Roblox** | Platforma gier (dialekt Luau) |
| **Świat Warcraft** | Skrypty interfejsu użytkownika (Lua) |
| **Neovim** | Edytor (skrypty Lua) |
| **Redis** | Skrypty Lua w Redis |
| **Nginx/OpenResty** | Skrypty Lua w Nginx |
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

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + Lua (sumneko)** | Najlepszy Lua LSP |
| **Studio ZeroBrane** | IDE specyficzne dla Lua |
| **Neovim** | Konfiguracja Lua (pierwsza klasa) |
| **IntelliJ + EmmyLua** | Obsługa JetBrains Lua |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Samodzielny** | Połącz Lua z aplikacją |
| **LuaRock** | Pakuj i dystrybuuj |
| **OpenResty** | Wdrożenie Nginx + Lua |
| **Doker** | Kontenerowy |
| **Wbudowany** | Do aplikacji C/C++ |
| **Platformy gier** | MIŁOŚĆ, Defold, Roblox |
---

## Streszczenie
Ekosystem Lua jest mały, ale koncentruje się na osadzaniu i pisaniu skryptów. Standardowy zestaw narzędzi to: **Lua 5.4** lub **LuaJIT** jako środowisko wykonawcze, **LuaRocks** dla pakietów, **busted** do testowania, **luacheck** do lintingu, **stylua** do formatowania. Lua doskonale sprawdza się jako język osadzony w grach (LÖVE, Defold, Roblox), serwerach (OpenResty, Nginx), bazach danych (Redis) i edytorach (Neovim). LuaJIT zapewnia wydajność zbliżoną do C w przypadku skryptów wymagających dużej mocy obliczeniowej. Mocnymi stronami Lua są niewielkie rozmiary (~25 KB), prosta składnia i doskonałe API do osadzania dla integracji C/C++.