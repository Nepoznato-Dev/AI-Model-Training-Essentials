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

# Lua — Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, bibliotecas e infraestructura esenciales en el ecosistema Lua.
---

## Versiones e implementaciones de Lua
| Implementación | Notas |
|---------------|-------|
| **Lua 5.4** | Versión estable actual |
| **LuaJIT** | Compilador JIT de alto rendimiento |
| **Lua 5.1** | Ampliamente utilizado (compatible con LuaJIT) |
| **Ravi** | JIT con escritura opcional |
| **Verde azulado** | Dialecto mecanografiado de Lua |
| **hinojo** | Lisp que compila en Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **LuaRocks** | Administrador de paquetes estándar |
| **luarocks.org** | Repositorio de paquetes |
| **encendido** | Administrador de paquetes LuaJIT |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | Web de alto rendimiento |
| **Luvita** | Tipo Node.js | E/S asíncrona (libuv) |
| **Órbita** | Web MVC | Aplicaciones web sencillas |
| **Marinero** | Pila completa | Marco MVC |
| **lapis** | Basado en OpenResty | Web MoonScript/Lua |
| **Pegaso** | Ligero | Servidor HTTP sencillo |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **luasql** | Enlaces de bases de datos (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Enlaces SQLite3 |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **arrestado** | Pruebas estilo BDD (más populares) |
| **luassert** | Biblioteca de afirmaciones (reventada) |
| **lujuria** | Pruebas mínimas |
| **prueba lunar** | xPruebas de estilo unitario |
| **verde azulado** | Comprobación de tipos (dialecto verde azulado) |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **luacheck** | Linting y análisis estático |
| **formato lua** | Formato de código |
| **estilo** | Formateador de código (basado en Rust, rápido) |
| **verde azulado** | Dialecto Lua escrito |
| **luacov** | Cobertura de código |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **luasocket** | Redes TCP/UDP/HTTP |
| **lua-cjson / cjson** | Análisis JSON |
| **lpeg** | Coincidencia de patrones (basada en PEG) |
| **Linterna (pl)** | Biblioteca de utilidades (como Python stdlib) |
| **copas** | Socket basado en rutinas |
| **coxpcall** | Llamadas protegidas |
| **lua-resty-* | Ecosistema OpenResty |
| **lfs** | Acceso al sistema de archivos |
| **lzlib** | Compresión |
| **lbase64** | Codificación Base64 |
| **inspeccionar** | Mesa bonita-impresión |
| **clásico** | Sistema de clases POO |
| **clase media** | Biblioteca de programación orientada a objetos |
| **bigote** | Plantillas de bigote |
| **argparse** | Análisis de argumentos CLI |
---

## Desarrollo de juegos
| Motor | Notas |
|--------|-------|
| **AMOR (Love2D)** | Marco de juego 2D (el más popular) |
| **Desplegar** | Motor de juego (secuencias de comandos Lua) |
| **Corona SDK** | Motor de juegos para móviles |
| **Roblox** | Plataforma de juego (dialecto Luau) |
| **Mundo de Warcraft** | Secuencias de comandos de interfaz de usuario (Lua) |
| **Neovim** | Editor (secuencias de comandos Lua) |
| **Redis** | Secuencias de comandos Lua en Redis |
| **Nginx/OpenResty** | Secuencias de comandos Lua en Nginx |
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

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + Lua (sumneko)** | Mejor LSP de Lua |
| **Estudio ZeroBrane** | IDE específico de Lua |
| **Neovim** | Configuración Lua (primera clase) |
| **IntelliJ + EmmyLua** | Soporte de JetBrains Lua |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Independiente** | Combina Lua con la aplicación |
| **LuaRocks** | Empaquetar y distribuir |
| **OpenResty** | Implementación de Nginx + Lua |
| **Acoplador** | En contenedores |
| **Integrado** | En aplicaciones C/C++ |
| **Plataformas de juego** | AMOR, Defold, Roblox |
---

## Resumen
El ecosistema de Lua es pequeño pero se centra en la integración y la creación de secuencias de comandos. La cadena de herramientas estándar es: **Lua 5.4** o **LuaJIT** como tiempo de ejecución, **LuaRocks** para paquetes, **busted** para pruebas, **luacheck** para linting, **stylua** para formateo. Lua destaca como lenguaje integrado en juegos (LÖVE, Defold, Roblox), servidores (OpenResty, Nginx), bases de datos (Redis) y editores (Neovim). LuaJIT proporciona un rendimiento cercano a C para scripts con uso intensivo de computación. Los puntos fuertes de Lua son su pequeño tamaño (~25 KB), su sintaxis simple y su excelente API de integración para la integración C/C++.