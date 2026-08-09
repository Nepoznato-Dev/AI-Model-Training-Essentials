---
# Metadatos
título: "Lúa"
descripción: "Referencia completa para el lenguaje de programación Lua que cubre descripción general, compensaciones, fundamentos de sintaxis, ecosistema y cuándo usarlo".
categoría: "Codificación y tecnología"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de base de conocimientos de codificación y tecnología"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [lua, lenguaje-de-programación, sintaxis, ecosistema, codificación-y-tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "26 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# lua
Lua es un lenguaje de scripting ligero e integrable diseñado para ampliar aplicaciones. Creado en 1993 en la Pontificia Universidad Católica de Río de Janeiro en Brasil, Lua es uno de los lenguajes de programación más rápidos disponibles. Su pequeño tamaño (el intérprete pesa ~120 KB) y su simplicidad lo convierten en la opción ideal para el desarrollo de scripts, sistemas integrados y configuración de juegos.
Lua es mejor conocido como el lenguaje de programación detrás de Roblox (la plataforma de juegos con más de 200 millones de usuarios mensuales), complementos de World of Warcraft y numerosos motores de juegos (Love2D, Defold, Corona SDK). También se utiliza en Nginx (OpenResty), Redis y Wireshark.
---

## Por qué es importante Lua
- **Integrable**: Diseñado para integrarse en otras aplicaciones; el host proporciona la funcionalidad.
- **Pequeña huella**: todo el intérprete cabe en ~120 KB. Ideal para sistemas integrados.
- **Rápido**: Uno de los lenguajes de scripting interpretados más rápidos.
- **Simple**: Sólo ~20 palabras clave. Fácil de aprender e integrar.
- **Desarrollo de juegos**: el lenguaje de programación estándar para muchos motores y plataformas de juegos.
- **Roblox**: impulsa todo el ecosistema de Roblox: millones de juegos creados por usuarios.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Biblioteca estándar limitada** | Funcionalidad integrada mínima | Amplíe con C/C++ o utilice paquetes LuaRocks |
| **indexación basada en 1** | Los arreglos comienzan en el índice 1 (inusual para programadores) | Aceptar como opción de diseño; consistente en todo |
| **No hay clases** | Sólo tablas y metatablas: la programación orientada a objetos debe implementarse manualmente | Utilice metatablas o bibliotecas de programación orientada a objetos |
| **Juegos externos de nicho** | Uso limitado en web, ciencia de datos o empresa | Úselo para secuencias de comandos/incrustación; otros idiomas para aplicaciones |
| **Mercado laboral pequeño** | Principalmente desarrollo de juegos y roles integrados | El desarrollo de Roblox es un nicho en crecimiento |
---

## Fundamentos de sintaxis
```lua
-- Variables
local name = "Alice"
local age = 30
local score = 9.5

-- Tables (the only data structure — used as arrays, maps, objects)
local user = {name = "Alice", age = 30}
local fruits = {"apple", "banana", "cherry"}  -- Array (1-indexed!)

print(user.name)        -- "Alice"
print(fruits[1])        -- "apple" (Lua arrays start at 1)

-- Functions
local function greet(name, greeting)
    greeting = greeting or "Hello"  -- Default value
    return greeting .. ", " .. name .. "!"
end

-- Higher-order functions
local function apply(fn, value)
    return fn(value)
end

local double = function(x) return x * 2 end
print(apply(double, 5))  -- 10

-- Conditionals and loops
if age >= 18 then
    print("Adult")
elseif age >= 13 then
    print("Teenager")
else
    print("Child")
end

for i = 1, 10 do
    print(i)
end

for index, fruit in ipairs(fruits) do
    print(index, fruit)
end

-- Metatables (OOP-like behaviour)
local Animal = {}
Animal.__index = Animal

function Animal.new(name)
    local self = setmetatable({}, Animal)
    self.name = name
    return self
end

function Animal:speak()
    return self.name .. " makes a sound"
end

local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
    local self = Animal.new(name)
    return setmetatable(self, Dog)
end

function Dog:speak()
    return self.name .. " says woof"
end

local rex = Dog.new("Rex")
print(rex:speak())  -- "Rex says woof"
```

---

## Sintaxis y patrones avanzados
### Metatables: la base del poder de Lua
```lua
-- Metatables allow custom behaviour for tables
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable({x = x, y = y}, Vector)
end

-- Operator overloading via metamethods
function Vector.__add(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end

function Vector.__mul(a, b)
    if type(b) == "number" then
        return Vector.new(a.x * b, a.y * b)
    end
    return a.x * b.x + a.y * b.y  -- Dot product
end

function Vector.__tostring(v)
    return string.format("Vector(%.1f, %.1f)", v.x, v.y)
end

function Vector.__eq(a, b)
    return a.x == b.x and a.y == b.y
end

function Vector:magnitude()
    return math.sqrt(self.x^2 + self.y^2)
end

local v1 = Vector.new(3, 4)
local v2 = Vector.new(1, 2)
print(v1 + v2)          -- Vector(4.0, 6.0)
print(v1 * 2)           -- Vector(6.0, 8.0)
print(v1 * v2)          -- 11 (dot product)
print(v1:magnitude())   -- 5.0
print(v1 == Vector.new(3, 4))  -- true
```

### Cierres y Patrones Funcionales
```lua
-- Closures — functions capture upvalues
local function make_counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

local counter = make_counter()
print(counter())  -- 1
print(counter())  -- 2
print(counter())  -- 3

-- Functional utilities
local function map(t, fn)
    local result = {}
    for i, v in ipairs(t) do
        result[i] = fn(v)
    end
    return result
end

local function filter(t, fn)
    local result = {}
    for _, v in ipairs(t) do
        if fn(v) then result[#result + 1] = v end
    end
    return result
end

local function reduce(t, fn, init)
    local acc = init
    for _, v in ipairs(t) do
        acc = fn(acc, v)
    end
    return acc
end

local numbers = {1, 2, 3, 4, 5}
local doubled = map(numbers, function(x) return x * 2 end)
local evens = filter(numbers, function(x) return x % 2 == 0 end)
local sum = reduce(numbers, function(a, b) return a + b end, 0)
```

### Múltiples valores de retorno y desestructuración
```lua
-- Lua functions can return multiple values
local function minmax(t)
    local min, max = math.huge, -math.huge
    for _, v in ipairs(t) do
        if v < min then min = v end
        if v > max then max = v end
    end
    return min, max
end

local lo, hi = minmax({5, 2, 8, 1, 9, 3})
print(lo, hi)  -- 1  9

-- Variadic functions
local function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end

print(sum(1, 2, 3, 4, 5))  -- 15

-- Table unpacking
local a, b, c = table.unpack({10, 20, 30})
print(a, b, c)  -- 10  20  30
```

### Patrones de cuerdas (alternativa Regex de Lua)
```lua
-- Lua patterns — simpler than regex but powerful
local text = "Error 404: Page not found on 2024-01-15"

-- Basic matching
local code, msg = text:match("Error (%d+): (.+)")
print(code)  -- "404"
print(msg)   -- "Page not found on 2024-01-15"

-- Find and replace
local replaced = text:gsub("not found", "missing")

-- Pattern character classes
-- %a = letters, %d = digits, %w = alphanumeric
-- %s = whitespace, %p = punctuation
local email = "user@example.com"
local valid = email:match("^[%w%.%-]+@[%w%.%-]+%.%a+$")

-- Capture groups
local date = "2024-01-15"
local year, month, day = date:match("(%d+)-(%d+)-(%d+)")
```

---

## Concurrencia y paralelismo
### Corrutinas: multitarea cooperativa
```lua
-- Coroutines — Lua's built-in cooperative concurrency
local function producer()
    local items = {"apple", "banana", "cherry"}
    for _, item in ipairs(items) do
        print("Producing: " .. item)
        coroutine.yield(item)
    end
    return "done"
end

local co = coroutine.create(producer)

print(coroutine.status(co))  -- "suspended"
local ok, value = coroutine.resume(co)
print("Got:", value)         -- Got: apple
print(coroutine.status(co))  -- "suspended"

coroutine.resume(co)  -- banana
coroutine.resume(co)  -- cherry
print(coroutine.status(co))  -- "dead"
```

### Patrón de iterador basado en rutinas
```lua
-- Coroutine wrapping for clean iteration
local function coroutine_iterator(body)
    local co = coroutine.create(body)
    return function()
        local ok, value = coroutine.resume(co)
        if not ok or coroutine.status(co) == "dead" then
            return nil
        end
        return value
    end
end

-- Usage: generate fibonacci numbers lazily
local fib = coroutine_iterator(function()
    local a, b = 0, 1
    while true do
        coroutine.yield(a)
        a, b = b, a + b
    end
end)

for i = 1, 10 do
    io.write(fib() .. " ")  -- 0 1 1 2 3 5 8 13 21 34
end

-- Coroutine-based async I/O (with Copas or OpenResty)
local copas = require("copas")

local function fetch_url(url)
    local sock = copas.tcp()
    sock:connect(url, 80)
    sock:send("GET / HTTP/1.1\r\nHost: " .. url .. "\r\n\r\n")
    local response = sock:receive("*a")
    sock:close()
    return response
end

-- Multiple concurrent connections
copas.addthread(fetch_url, "example.com")
copas.addthread(fetch_url, "example.org")
copas.loop()
```

---

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto
```
my-lua-project/
├── src/
│   ├── main.lua
│   ├── config.lua
│   ├── models/
│   ├── utils/
│   └── game/
├── spec/
│   └── test_main.lua
├── rocks/           -- LuaRocks packages
├── .luacheckrc      -- Linting config
├── Makefile
└── rockspec         -- Package spec
```

### LuaRocks — Gestión de paquetes
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — Especificación del paquete
```lua
-- myproject-1.0-1.rockspec
package = "myproject"
version = "1.0-1"

source = {
    url = "git+https://github.com/user/myproject.git",
    tag = "v1.0",
}

dependencies = {
    "lua >= 5.3",
    "luasocket",
    "lua-cjson",
}

build = {
    type = "builtin",
    modules = {
        ["myproject.core"] = "src/core.lua",
        ["myproject.utils"] = "src/utils.lua",
    },
}
```

### Canalización de CI/CD (acciones de GitHub)
```yaml
name: Lua CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    strategy:
      matrix:
        lua-version: ['5.3', '5.4', 'luajit']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: leafo/gh-actions-lua@v10
        with:
          luaVersion: ${{ matrix.lua-version }}
      - uses: leafo/gh-actions-luarocks@v4
      - run: luarocks install busted
      - run: luarocks install luacheck
      - run: luacheck src/
      - run: busted spec/
```
---

## Pruebas
### Reventado: marco de prueba
```lua
-- spec/utils_spec.lua
local utils = require("src.utils")

describe("utils", function()
    describe("add", function()
        it("adds two positive numbers", function()
            assert.are.equal(utils.add(2, 3), 5)
        end)
        it("handles negative numbers", function()
            assert.are.equal(utils.add(-1, 1), 0)
        end)
    end)
    describe("format_name", function()
        it("capitalizes first letter", function()
            assert.are.equal(utils.format_name("alice"), "Alice")
        end)
    end)
end)
```

### Burlándose con luassert
```lua
describe("UserService", function()
    local service, mock_repo
    before_each(function()
        mock_repo = {
            save = spy.new(function() return true end),
            find = spy.new(function(id) return {id=id, name="Alice"} end),
        }
        service = require("src.user_service").new(mock_repo)
    end)
    it("saves user via repository", function()
        service:create("Alice", "alice@example.com")
        assert.spy(mock_repo.save).was_called(1)
    end)
end)
```

### Comandos de prueba
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## Interoperabilidad
### API de C: incrustar Lua en C
```c
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

int main(void) {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    luaL_dofile(L, "script.lua");
    lua_getglobal(L, "greet");
    lua_pushstring(L, "World");
    lua_pcall(L, 1, 1, 0);
    printf("Lua says: %s\n", lua_tostring(L, -1));
    lua_close(L);
    return 0;
}
// Compile: gcc -o host host.c -llua5.4
```

### LuaJIT FFI: llamadas directas C
```lua
local ffi = require("ffi")
ffi.cdef[[
    double sqrt(double x);
    int abs(int n);
]]
local C = ffi.C
print(C.sqrt(144))   -- 12.0
print(C.abs(-42))    -- 42
```

---

## Patrones de diseño
### Patrón de módulo (Singleton)
```lua
-- config.lua — modules are singletons by design
local config = {
    debug = false,
    version = "1.0.0",
}
function config.get(key) return config[key] end
function config.set(key, value) config[key] = value end
return config
```

### Observador / Sistema de eventos
```lua
local EventBus = {}
EventBus.__index = EventBus

function EventBus.new()
    return setmetatable({listeners = {}}, EventBus)
end

function EventBus:on(event, callback)
    self.listeners[event] = self.listeners[event] or {}
    table.insert(self.listeners[event], callback)
end

function EventBus:emit(event, ...)
    if self.listeners[event] then
        for _, cb in ipairs(self.listeners[event]) do cb(...) end
    end
end

local bus = EventBus.new()
bus:on("player_died", function(p) print(p.name .. " died!") end)
bus:emit("player_died", {name = "Hero"})
```

### Patrón de comando
```lua
local Command = {}
Command.__index = Command

function Command.new(name, exec, undo)
    return setmetatable({name=name, execute=exec, undo=undo}, Command)
end

local history = {}
local cmd = Command.new("move",
    function() print("Moving") end,
    function() print("Undoing move") end)
cmd.execute()
table.insert(history, cmd)
if #history > 0 then table.remove(history).undo() end
```
---

## Rendimiento y optimización
```bash
luajit -jp=v script.lua
luajit -jv script.lua
```

```lua
local sqrt = math.sqrt
local tconcat = table.concat
local parts = {}
for i = 1, 1000 do parts[#parts + 1] = tostring(i) end
local result = tconcat(parts, ',')
```

---

## Implementación
### Implementación de Docker
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Cuándo usar Lua
| Escenario | ¿Por qué Lua? Mejor alternativa |
|----------|---------|-------------------|
| Guiones de juegos | Ligero, rápido, integrable | — |
| Desarrollo de Roblox | La única opción | — |
| Sistemas integrados | Pequeña huella | C, MicroPython |
| Extensión de la aplicación | Diseñado para empotrar | Python (más grande), JavaScript (V8) |
| Archivos de configuración | Sencillo y rápido | JSON, TOML, YAML |
| Desarrollo web | OpenResty existe pero es un nicho | JavaScript, Python, Ir |
| Desarrollo de aplicaciones generales | No diseñado para aplicaciones independientes | Python, Ir, Java |
| Ciencia de datos | No el ecosistema | Pitón, R |
---

## Resumen
Lua es el lenguaje de incrustación por excelencia. Es pequeño, rápido y simple, diseñado para vivir dentro de otras aplicaciones y brindarles capacidades de secuencias de comandos. Para el desarrollo de juegos, Roblox y sistemas integrados, Lua es una excelente opción. No es un lenguaje de propósito general, pero para su nicho específico (scripting e incrustación), es casi incomparable.