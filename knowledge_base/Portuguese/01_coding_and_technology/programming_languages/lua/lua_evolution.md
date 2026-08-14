---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lua, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Lua — Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 1994 | Lançamento inicial (PUC-Rio, Brasil) |
| 2.1 | 1995 | As tabelas tornam-se a única estrutura de dados |
| 3.0 | 1997 | API C, métodos de tag (primeiros metamétodos) |
| 3.1 | 1998 | Controladores semânticos (upvalues) |
| 4,0 | 2000 | **Lua 4**: contagem de referências + GC, API C aprimorada |
| 5,0 | 2003 | **Principal**: escopo lexical adequado, corrotinas, metatabelas, booleanos |
| 5.1 | 2006 | **GC incremental**, operador de comprimento `#`,`goto`removido,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`alterações,`goto`adicionado novamente, tabelas efêmeras |
| 5.3 | 2015 | **Tipo inteiro**, operadores bit a bit, suporte a UTF-8 |
| 5.4 | 2020 | **GC geracional**, variáveis ​​`const`/`close`, metamétodo`tostring`|
| 5.4.x | 2020–25 | Melhorias incrementais, sistema de alerta |
| 5.5 | A definir | (futuro) Outras melhorias no GC |
## Marcos importantes
### Lua 1–3: Os primeiros anos (1994–1999)
- **1994**: Criado na PUC-Rio (Pontifícia Universidade Católica do Rio de Janeiro) por Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Objetivo**: Linguagem de script incorporável para entrada de dados (não uma linguagem independente)
- **2.1**: As tabelas se tornam a única estrutura de dados — simplicidade radical
- **3.0**: API C solidificada — torna Lua incorporável em aplicações C/C++
- **3.1**: Upvalues — escopo léxico para fechamentos
### Lua 4: Maturação (2000)
- Contagem de referência + coleta de lixo (híbrido)
- API C aprimorada — biblioteca auxiliar `luaL_*`
- Ainda não há escopo lexical adequado para globais
### Lua 5.0: Lua Moderna (2003)
- **Escopo léxico adequado** — Variáveis `local`
- **Corrotinas** — multitarefa cooperativa
- **Metatabelas** — sobrecarga de operador, comportamento personalizado
- **Booleanos** —`true`/`false`como valores próprios
- **Fechamentos** bem feitos - valores positivos generalizados
- Essa é a versão que fez com que Lua fosse amplamente adotada nos games
### Lua 5.1: O Padrão (2006)
- **Coletor de lixo incremental**
- Operador de comprimento `#`
- Função `module()`
- Mudou a forma como o ambiente global funciona
- **Esta versão se torna a versão mais amplamente incorporada** (LuaJIT tem como alvo 5.1)
### Lua 5.2: Refinamentos (2011)
-`_ENV`— ambiente por pedaço (globais mais limpos)
- A instrução`goto`retorna
- Tabelas Ephemeron (melhoria de GC)
- Melhorias no sistema de pacotes
### Lua 5.3: Inteiros e Bits (2015)
- **Subtipo inteiro** — distinto de float
- **Operadores bit a bit** —`&`,`|`,`~`,`<<`,`>>`
- **Suporte UTF-8** — biblioteca`utf8`integrada
- Divisão de piso`//`
- String`pack`/`unpack`para dados binários
### Lua 5.4: GC Geracional (2020)
- **Coletor de lixo geracional** — pausas de GC muito melhores
- ** Variáveis `<const>`** — constantes verdadeiras
- ** Variáveis `<close>`** — variáveis a serem fechadas (gerenciamento de recursos, como`defer`ou`with`)
- Metamétodo `tostring`
- Subtipos de strings (strings curtas versus longas otimizadas de maneira diferente)
## Evolução da Sintaxe
```lua
-- Lua 4.0: No local scoping for globals
x = 10  -- always global unless in a function

-- Lua 5.0: Proper lexical scoping
local x = 10  -- local to block
do
  local y = 20
  print(x + y)  -- 30
end

-- Lua 5.1: Length operator, module
local t = {1, 2, 3}
print(#t)  -- 3
module("mymodule", package.seeall)

-- Lua 5.3: Integer type, bitwise
local a = 10    -- integer
local b = 10.0  -- float
print(a & 0xFF) -- bitwise AND: 10
print(a >> 1)   -- right shift: 5

-- Lua 5.4: const and close variables
local x <const> = 42  -- constant, cannot change
local f <close> = io.open("file.txt")  -- auto-closed at scope end
```

## Evolução de recursos
```
Lua 1.0:  Tables, functions, strings, numbers, C API
Lua 2.1:  Tables as only data structure
Lua 3.0:  Tag methods (predecessor to metatables)
Lua 3.1:  Upvalues (closures)
Lua 4.0:  Hybrid GC (ref counting + cycle collection)
Lua 5.0:  Coroutines, metatables, proper lexical scoping, booleans
Lua 5.1:  Incremental GC, # operator, module()
Lua 5.2:  _ENV, goto, ephemeron tables
Lua 5.3:  Integer type, bitwise ops, UTF-8, //, pack/unpack
Lua 5.4:  Generational GC, <const>, <close>, tostring metamethod
```

## Lua em jogos
```
1997: LucasArts uses Lua in game scripting (Grim Fandango)
2003: Lua 5.0 — game industry adoption accelerates
2005: World of Warcraft uses Lua for UI addons
2006: LuaJIT (Mike Pall) — JIT-compiled Lua 5.1, extremely fast
2010: Love2D game framework (Lua-based)
2012: Defold game engine (Lua scripting)
2015: Roblox adopts Luau (Lua dialect with types)
2020: Lua 5.4 — continued game engine integration
2025: Lua remains the #1 embedded scripting language in games
       Used in: Unity (via plugins), WoW, Garry's Mod, Factorio,
       Civilization, Adobe Lightroom, Nginx (OpenResty), Redis
```

## Princípios-chave de design
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Crescimento do Ecossistema
```
1994: Lua created at PUC-Rio (Brazil)
1997: First game industry use (LucasArts)
2003: Lua 5.0 — widespread game adoption
2005: LuaJIT — JIT-compiled Lua
2006: Lua 5.1 — the "standard" embedded version
2010: OpenResty (Nginx + Lua) — web development
2015: Luau (Roblox) — typed Lua dialect
2020: Lua 5.4 — modern GC, resource management
2025: Lua is the dominant embedded scripting language
       Powers: games, Nginx, Redis, Wireshark, Lightroom, more
```
