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

# Lua – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 1,0 | 1994 | Erstveröffentlichung (PUC-Rio, Brasilien) |
| 2.1 | 1995 | Tabellen werden zur einzigen Datenstruktur |
| 3,0 | 1997 | C-API, Tag-Methoden (frühe Metamethoden) |
| 3.1 | 1998 | Semantische Controller (Upvalues) |
| 4,0 | 2000 | **Lua 4**: Ref-Zählung + GC, verbesserte C-API |
| 5,0 | 2003 | **Hauptfach**: Richtiges lexikalisches Scoping, Coroutinen, Metatabellen, Boolesche Werte |
| 5.1 | 2006 | **Inkrementeller GC**,`#`Längenoperator,`goto`entfernt,`module()`|
| 5.2 | 2011 |  `_ENV`,`_G`Änderungen,`goto`wieder hinzugefügt, Ephemeron-Tabellen |
| 5,3 | 2015 | **Integer-Typ**, bitweise Operatoren, UTF-8-Unterstützung |
| 5,4 | 2020 | **Generational GC**,`const`/ `close`-Variablen, `tostring`-Metamethode |
| 5.4.x | 2020–25 | Inkrementelle Verbesserungen, Warnsystem |
| 5,5 | TBD | (zukünftig) Weitere GC-Verbesserungen |
## Wichtige Meilensteine
### Lua 1–3: Die frühen Jahre (1994–1999)
- **1994**: Erstellt an der PUC-Rio (Päpstliche Katholische Universität von Rio de Janeiro) von Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Ziel**: Einbettbare Skriptsprache für die Dateneingabe (keine eigenständige Sprache)
- **2.1**: Tabellen werden zur einzigen Datenstruktur – radikale Einfachheit
- **3.0**: C-API verfestigt – macht Lua in C/C++-Anwendungen einbettbar
- **3.1**: Upvalues – lexikalisches Scoping für Abschlüsse
### Lua 4: Reifung (2000)
- Referenzzählung + Garbage Collection (Hybrid)
- Verbesserte C-API – Hilfsbibliothek `luaL_*`
- Immer noch kein richtiger lexikalischer Geltungsbereich für Globals
### Lua 5.0: Modernes Lua (2003)
- **Richtige lexikalische Festlegung** – `local`-Variablen
- **Koroutinen** – kooperatives Multitasking
- **Metatables** – Operatorüberladung, benutzerdefiniertes Verhalten
- **Boolesche Werte** –`true`/`false`als richtige Werte
- **Schließungen** richtig durchgeführt – Aufwertungen verallgemeinert
– Dies ist die Version, die Lua in Spielen weit verbreitet gemacht hat
### Lua 5.1: Der Standard (2006)
- **Inkrementeller Garbage Collector**
-`#`Längenoperator
- `module()`-Funktion
- Die Funktionsweise der globalen Umgebung wurde geändert
- **Diese Version wird die am weitesten verbreitete eingebettete Version** (LuaJIT zielt auf 5.1 ab)
### Lua 5.2: Verfeinerungen (2011)
-`_ENV`– Pro-Chunk-Umgebung (sauberere Globals)
- Die Anweisung`goto`wird zurückgegeben
- Ephemeron-Tabellen (GC-Verbesserung)
- Verbesserungen des Paketsystems
### Lua 5.3: Ganzzahl und Bits (2015)
- **Integer-Subtyp** – verschieden von Float
- **Bitweise Operatoren** – `&`, `|`, `~`, `<<`,`>>`
- **UTF-8-Unterstützung** – integrierte `utf8`-Bibliothek
- Bodeneinteilung`//`
- String`pack`/`unpack`für Binärdaten
### Lua 5.4: Generations-GC (2020)
- **Generation Garbage Collector** – viel bessere GC-Pausen
- **`<const>`-Variablen** – echte Konstanten
- ** `<close>`-Variablen** – zu schließende Variablen (Ressourcenverwaltung, wie`defer`oder `with`)
- `tostring`-Metamethode
- String-Subtypen (kurze vs. lange Strings unterschiedlich optimiert)
## Syntaxentwicklung
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

## Feature-Entwicklung
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

## Lua im Gaming
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

## Wichtige Designprinzipien
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Ökosystemwachstum
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
