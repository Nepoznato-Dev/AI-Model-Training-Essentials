---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Lua: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 1994 | Versione iniziale (PUC-Rio, Brasile) |
| 2.1 | 1995 | Le tabelle diventano l'unica struttura dati |
| 3.0 | 1997 | API C, metodi tag (primi metametodi) |
| 3.1 | 1998 | Controllori semantici (upvalue) |
| 4.0 | 2000 | **Lua 4**: conteggio dei riferimenti + GC, API C migliorata |
| 5.0 | 2003| **Maggiore**: scoping lessicale corretto, coroutine, metatabelle, booleane |
| 5.1 | 2006| **GC incrementale**, operatore di lunghezza `#`,`goto`rimosso,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`cambia,`goto`aggiunto di nuovo, tabelle degli effemeri |
| 5.3 | 2015| **Tipo intero**, operatori bit a bit, supporto UTF-8 |
| 5.4 | 2020 | **GC generazionale**, variabili`const`/ `close`, metametodo`tostring`|
| 5.4.x | 2020–25 | Miglioramenti incrementali, sistema di allarme |
| 5,5 | Da definire | (futuro) Ulteriori miglioramenti GC |
## Traguardi importanti
### Lua 1–3: I primi anni (1994–1999)
- **1994**: Creato alla PUC-Rio (Pontificia Università Cattolica di Rio de Janeiro) da Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Obiettivo**: linguaggio di scripting incorporabile per l'immissione dei dati (non un linguaggio autonomo)
- **2.1**: le tabelle diventano l'unica struttura dati: semplicità radicale
- **3.0**: API C consolidata: rende Lua incorporabile nelle applicazioni C/C++
- **3.1**: Upvalues: ambito lessicale per le chiusure
### Lua 4: Maturazione (2000)
- Conteggio riferimenti + garbage collection (ibrido)
- API C migliorata: libreria ausiliaria `luaL_*`
- Ancora nessuna definizione lessicale adeguata per le globali
### Lua 5.0: Lua moderno (2003)
- **Ambito lessicale corretto**: variabili `local`
- **Coroutine**: multitasking cooperativo
- **Metatable**: sovraccarico degli operatori, comportamento personalizzato
- **Booleani** —`true`/`false`come valori corretti
- **Chiusure** fatte bene – rialzi generalizzati
- Questa è la versione che ha reso Lua ampiamente adottato nei giochi
### Lua 5.1: Lo standard (2006)
- **Garbage Collector incrementale**
- Operatore di lunghezza `#`
- Funzione `module()`
- Cambiato il funzionamento dell'ambiente globale
- **Questa versione diventa la versione più ampiamente incorporata** (LuaJIT punta alla 5.1)
### Lua 5.2: Perfezionamenti (2011)
- `_ENV`: ambiente per blocco (globali più puliti)
- L'istruzione`goto`restituisce
- Tabelle Ephemeron (miglioramento GC)
- Miglioramenti al sistema dei pacchetti
### Lua 5.3: Interi e bit (2015)
- **Sottotipo intero**: distinto da float
- **Operatori bit a bit** —`&`,`|`,`~`,`<<`,`>>`
- **Supporto UTF-8**: libreria`utf8`integrata
- Divisione del pavimento`//`
- Stringa`pack`/`unpack`per dati binari
### Lua 5.4: GC generazionale (2020)
- **Garbage Collector generazionale**: pause GC molto migliori
- **Variabili `<const>`**: costanti vere
- **Variabili `<close>`**: variabili da chiudere (gestione delle risorse, come`defer`o`with`)
- Metametodo `tostring`
- Sottotipi di stringhe (stringhe corte e lunghe ottimizzate in modo diverso)
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
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

## Lua nei giochi
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

## Principi chiave di progettazione
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Crescita dell'ecosistema
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
