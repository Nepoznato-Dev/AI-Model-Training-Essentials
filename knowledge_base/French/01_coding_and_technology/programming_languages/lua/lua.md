---
# Métadonnées
titre : "Lua"
description : "Référence complète sur le langage de programmation Lua couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [lua, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "26 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Lua
Lua est un langage de script léger et intégrable conçu pour étendre les applications. Créé en 1993 à l'Université pontificale catholique de Rio de Janeiro au Brésil, Lua est l'un des langages de script les plus rapides disponibles. Son faible encombrement (l'interpréteur fait environ 120 Ko) et sa simplicité en font le choix incontournable pour les scripts de développement de jeux, les systèmes embarqués et la configuration.
Lua est surtout connu comme le langage de script derrière Roblox (la plate-forme de jeu avec plus de 200 millions d'utilisateurs mensuels), les modules complémentaires de World of Warcraft et de nombreux moteurs de jeu (Love2D, Defold, Corona SDK). Il est également utilisé dans Nginx (OpenResty), Redis et Wireshark.
---

## Pourquoi Lua est important
- **Embeddable** : conçu pour être intégré dans d'autres applications — l'hôte fournit la fonctionnalité.
- **Petite empreinte** : l'interprète entier tient dans environ 120 Ko. Idéal pour les systèmes embarqués.
- **Fast** : l'un des langages de script interprétés les plus rapides.
- **Simple** : seulement environ 20 mots-clés. Facile à apprendre et à intégrer.
- **Développement de jeux** : langage de script standard pour de nombreux moteurs et plates-formes de jeux.
- **Roblox** : alimente l'ensemble de l'écosystème Roblox : des millions de jeux créés par les utilisateurs.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Bibliothèque standard limitée** | Fonctionnalité intégrée minimale | Étendez avec C/C++ ou utilisez les packages LuaRocks |
| **Indexation basée sur 1** | Les tableaux commencent à l'index 1 (inhabituel pour les programmeurs) | Accepter comme choix de conception ; cohérent partout |
| **Pas de cours** | Uniquement les tables et métatables — La POO doit être implémentée manuellement | Utiliser des métatables ou des bibliothèques POO |
| **Niche en dehors des jeux** | Utilisation limitée dans le Web, la science des données ou l'entreprise | Utiliser pour les scripts/l'intégration ; autres langues pour les applications |
| **Petit marché du travail** | Principalement développement de jeux et rôles intégrés | Le développement de Roblox est un créneau en pleine croissance |
---

## Fondamentaux de la syntaxe
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

## Syntaxe et modèles avancés
### Metatables — Le fondement du pouvoir de Lua
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

### Fermetures et modèles fonctionnels
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

### Valeurs de retour multiples et déstructuration
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

### Modèles de chaînes (alternative Regex de Lua)
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

## Concurrence et parallélisme
### Coroutines — Multitâche coopératif
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

### Modèle d'itérateur basé sur la coroutine
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

## Configuration du projet et système de construction
### Structure du projet
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

### LuaRocks — Gestion des paquets
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — Spécification du package
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

### Pipeline CI/CD (actions GitHub)
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

## Tests
### Busted - Cadre de test
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

### Se moquer de Luassert
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

### Tester les commandes
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## Interopérabilité
### API C — Intégration de Lua dans C
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

### LuaJIT FFI — Appels C directs
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

## Modèles de conception
### Modèle de module (singleton)
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

### Observateur / Système d'événements
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

### Modèle de commande
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

## Performances et optimisation
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

## Déploiement
### Déploiement de Docker
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Quand utiliser Lua
| Scénario | Pourquoi Lua | Meilleure alternative |
|--------------|---------|-------------------|
| Script de jeu | Léger, rapide, intégrable | — |
| Développement Roblox | La seule option | — |
| Systèmes embarqués | Petite empreinte | C, MicroPython |
| Extension de candidature | Conçu pour l'intégration | Python (plus grand), JavaScript (V8) |
| Fichiers de configuration | Simple et rapide | JSON, TOML, YAML |
| Développement Web | OpenResty existe mais niche | JavaScript, Python, Aller |
| Développement d'applications générales | Non conçu pour les applications autonomes | Python, Go, Java |
| Science des données | Pas l'écosystème | Python, R |
---

## Résumé
Lua est le langage d'intégration par excellence. Il est petit, rapide et simple – conçu pour s'intégrer à d'autres applications et leur fournir des fonctionnalités de script. Pour le développement de jeux, Roblox et les systèmes embarqués, Lua est un excellent choix. Ce n'est pas un langage à usage général, mais pour son créneau spécifique (script et intégration), il est presque inégalé.