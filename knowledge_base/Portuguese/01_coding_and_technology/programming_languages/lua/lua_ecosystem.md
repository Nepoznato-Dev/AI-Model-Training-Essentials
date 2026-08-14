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

# Lua — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, bibliotecas e infraestrutura essenciais do ecossistema Lua.
---

## Versões e implementações de Lua
| Implementação | Notas |
|---------------|-------|
| **Lua 5.4** | Versão estável atual |
| **LuaJIT** | Compilador JIT de alto desempenho |
| **Lua 5.1** | Amplamente utilizado (compatível com LuaJIT) |
| **Ravi** | JIT com digitação opcional |
| **Teal** | Dialeto digitado de Lua |
| **funcho** | Lisp que compila para Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **LuaRocks** | Gerenciador de pacotes padrão |
| **luarocks.org** | Repositório de pacotes |
| **aceso** | Gerenciador de pacotes LuaJIT |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **OpenResty** | Nginx + Lua | Teia de alto desempenho |
| **Luvit** | semelhante a Node.js | E/S assíncrona (libuv) |
| **Órbita** | Rede MVC | Aplicativos web simples |
| **Marinheiro** | Pilha completa | Estrutura MVC |
| **lápis** | Baseado em OpenResty | MoonScript/Lua web |
| **Pégaso** | Leve | Servidor HTTP simples |
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

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **luasql** | Ligações de banco de dados (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Ligações SQLite3 |
| **pgmoon** | PostgreSQL (Lua pura) |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| ** preso ** | Teste estilo BDD (mais popular) |
| **luassert** | Biblioteca de asserções (quebrada) |
| **luxúria** | Testes mínimos |
| **lunata** | Teste estilo xUnit |
| **azul-petróleo** | Verificação de tipo (dialeto Teal) |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **luacheck** | Linting e análise estática |
| **formato lua** | Formatação de código |
| **estilo** | Formatador de código (baseado em Rust, rápido) |
| **azul-petróleo** | Dialeto Lua digitado |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **luasocket** | Rede TCP/UDP/HTTP |
| **lua-cjson / cjson** | Análise JSON |
| **lpeg** | Correspondência de padrões (baseada em PEG) |
| **Lanterna (pl)** | Biblioteca de utilitários (como Python stdlib) |
| **copas** | Soquete baseado em corrotina |
| **coxpcall** | Chamadas protegidas |
| **lua-resty-* | Ecossistema OpenResty |
| **se** | Acesso ao sistema de arquivos |
| **lzlib** | Compressão |
| **lbase64** | Codificação Base64 |
| **inspecionar** | Impressão bonita de mesa |
| **clássico** | Sistema de classes OOP |
| **classe média** | Biblioteca OOP |
| **luxúria** | Modelos de bigode |
| **argparse** | Análise de argumento CLI |
---

## Desenvolvimento de jogos
| Motor | Notas |
|-------|-------|
| **AMOR (Love2D)** | Estrutura de jogo 2D (mais popular) |
| **Desdobrar** | Motor de jogo (script Lua) |
| **SDK Corona** | Motor de jogo móvel |
| **Roblox** | Plataforma de jogo (dialeto Luau) |
| **World of Warcraft** | Script de UI (Lua) |
| **Neovim** | Editor (script Lua) |
| **Redes** | Script Lua em Redis |
| **Nginx/OpenResty** | Script Lua no Nginx |
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

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + Lua (sumneko)** | Melhor Lua LSP |
| **Estúdio ZeroBrane** | IDE específico para Lua |
| **Neovim** | Configuração Lua (primeira classe) |
| **IntelliJ + EmmyLua** | Suporte JetBrains Lua |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Independente** | Pacote Lua com aplicativo |
| **LuaRocks** | Embalar e distribuir |
| **OpenResty** | Implantação Nginx + Lua |
| **Docker** | Contentorizado |
| **Incorporado** | Em aplicativos C/C++ |
| **Plataformas de jogos** | AMOR, Defold, Roblox |
---

## Resumo
O ecossistema de Lua é pequeno, mas focado em incorporação e scripts. O conjunto de ferramentas padrão é: **Lua 5.4** ou **LuaJIT** como tempo de execução, **LuaRocks** para pacotes, **busted** para teste, **luacheck** para linting, **stylua** para formatação. Lua se destaca como linguagem embarcada em jogos (LÖVE, Defold, Roblox), servidores (OpenResty, Nginx), bancos de dados (Redis) e editores (Neovim). LuaJIT fornece desempenho próximo ao C para scripts de uso intensivo de computação. Os pontos fortes de Lua são seu tamanho reduzido (~25 KB), sintaxe simples e excelente API de incorporação para integração C/C++.