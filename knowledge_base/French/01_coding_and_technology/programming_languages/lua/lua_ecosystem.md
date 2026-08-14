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
# Lua — Guide de l'écosystème et des outils
Ce guide couvre les outils, bibliothèques et infrastructures essentiels de l'écosystème Lua.
---

## Versions et implémentations Lua
| Mise en œuvre | Remarques |
|---------------|-------|
| **Lua 5.4** | Version stable actuelle |
| **LuaJIT** | Compilateur JIT hautes performances |
| **Lua 5.1** | Largement utilisé (compatible LuaJIT) |
| **Ravi** | JIT avec saisie facultative |
| **Sarcelle** | Dialecte typé de Lua |
| **fenouil** | Lisp qui compile en Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **LuaRocks** | Gestionnaire de paquets standards |
| **luarocks.org** | Dépôt de packages |
| **allumé** | Gestionnaire de paquets LuaJIT |
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

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **OpenResty** | Nginx + Lua | Web haute performance |
| **Luvit** | De type Node.js | E/S asynchrones (libuv) |
| **Orbite** | Web MVC | Applications Web simples |
| **Marin** | Pile complète | Cadre MVC |
| **lapis** | Basé sur OpenResty | MoonScript/Lua web |
| **Pégase** | Léger | Serveur HTTP simple |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **luasql** | Liaisons de bases de données (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Liaisons SQLite3 |
| **pgmoon** | PostgreSQL (Lua pur) |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **éclaté** | Tests de style BDD (les plus populaires) |
| **luassert** | Bibliothèque d'assertions (éclatée) |
| **luxure** | Tests minimes |
| **le plus lunaire** | Tests de style xUnit |
| **sarcelle** | Vérification de type (dialecte sarcelle) |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **luacheck** | Pelluchage et analyse statique |
| **format lua** | Formatage des codes |
| **stylet** | Formateur de code (basé sur Rust, rapide) |
| **sarcelle** | Dialecte Lua tapé |
| **luacov** | Couverture du code |
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

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **luasocket** | Réseau TCP/UDP/HTTP |
| **lua-cjson / cjson** | Analyse JSON |
| **lpeg** | Correspondance de modèles (basée sur PEG) |
| **Lampe-stylo (pl)** | Bibliothèque d'utilitaires (comme Python stdlib) |
| **copas** | Socket basé sur Coroutine |
| **appel coxp** | Appels protégés |
| **lua-resty-* | Écosystème OpenResty |
| **lfs** | Accès au système de fichiers |
| **lzlib** | Compression |
| **lbase64** | Encodage Base64 |
| **inspecter** | Tableau joli-impression |
| **classique** | Système de classes POO |
| **classe moyenne** | Bibliothèque POO |
| **lustache** | Modèles de moustache |
| **argparse** | Analyse des arguments CLI |
---

## Développement de jeux
| Moteur | Remarques |
|--------|-------|
| **AMOUR (Love2D)** | Cadre de jeu 2D (le plus populaire) |
| **Déplier** | Moteur de jeu (script Lua) |
| **SDK Corona** | Moteur de jeu mobile |
| **Roblox** | Plateforme de jeu (dialecte Luau) |
| **Monde de Warcraft** | Scripts d'interface utilisateur (Lua) |
| **Néovim** | Éditeur (script Lua) |
| **Redis** | Scripts Lua dans Redis |
| **Nginx/OpenResty** | Scripts Lua dans Nginx |
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

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + Lua (sumneko)** | Meilleur Lua LSP |
| **ZéroBrane Studio** | IDE spécifique à Lua |
| **Néovim** | Configuration Lua (première classe) |
| **IntelliJ + EmmyLua** | Prise en charge de JetBrains Lua |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Autonome** | Regroupez Lua avec l’application |
| **LuaRocks** | Conditionner et distribuer |
| **OpenResty** | Déploiement Nginx + Lua |
| **Docker** | Conteneurisé |
| **Intégré** | Dans les applications C/C++ |
| **Plateformes de jeux** | LÖVE, Déplier, Roblox |
---

## Résumé
L'écosystème de Lua est petit mais axé sur l'intégration et les scripts. La chaîne d'outils standard est : **Lua 5.4** ou **LuaJIT** comme moteur d'exécution, **LuaRocks** pour les packages, **busted** pour les tests, **luacheck** pour le peluchage, **stylua** pour le formatage. Lua excelle en tant que langage intégré dans les jeux (LÖVE, Defold, Roblox), les serveurs (OpenResty, Nginx), les bases de données (Redis) et les éditeurs (Neovim). LuaJIT offre des performances proches du C pour les scripts gourmands en calcul. Les points forts de Lua sont sa petite empreinte (~ 25 Ko), sa syntaxe simple et son excellente API d'intégration pour l'intégration C/C++.