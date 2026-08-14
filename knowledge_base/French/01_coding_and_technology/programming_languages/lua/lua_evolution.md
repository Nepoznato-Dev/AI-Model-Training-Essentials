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
# Lua — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| 1.0 | 1994 | Version initiale (PUC-Rio, Brésil) |
| 2.1 | 1995 | Les tables deviennent la seule structure de données |
| 3.0 | 1997 | API C, méthodes de balise (premières métaméthodes) |
| 3.1 | 1998 | Contrôleurs sémantiques (upvalues) |
| 4.0 | 2000 | **Lua 4** : comptage de références + GC, API C améliorée |
| 5.0 | 2003 | **Majeur** : portée lexicale appropriée, coroutines, métatables, booléens |
| 5.1 | 2006 | **GC incrémentiel**, opérateur de longueur `#`,`goto`supprimé,`module()`|
| 5.2 | 2011 |  `_ENV`, modifications de `_G`,`goto`ajouté, tables d'éphémères |
| 5.3 | 2015 | **Type entier**, opérateurs au niveau du bit, prise en charge UTF-8 |
| 5.4 | 2020 | **GC générationnel**, variables`const`/ `close`, métaméthode`tostring`|
| 5.4.x | 2020-25 | Améliorations incrémentielles, système d'alerte |
| 5.5 | À déterminer | (à venir) Autres améliorations du GC |
## Étapes majeures
### Lua 1-3 : Les premières années (1994-1999)
- **1994** : Créée à la PUC-Rio (Université Pontificale Catholique de Rio de Janeiro) par Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Objectif** : langage de script intégrable pour la saisie de données (pas un langage autonome)
- **2.1** : Les tableaux deviennent l'unique structure de données — simplicité radicale
- **3.0** : API C solidifiée — rend Lua intégrable dans les applications C/C++
- **3.1** : Upvalues — portée lexicale pour les fermetures
### Lua 4 : Maturation (2000)
- Comptage de références + garbage collection (hybride)
- API C améliorée — Bibliothèque auxiliaire `luaL_*`
- Toujours pas de portée lexicale appropriée pour les globals
### Lua 5.0 : Lua moderne (2003)
- **Portée lexicale appropriée** — Variables `local`
- **Coroutines** — multitâche coopératif
- **Metatables** — surcharge d'opérateurs, comportement personnalisé
- **Booléens** —`true`/`false`comme valeurs appropriées
- **Fermetures** bien faites – valorisations généralisées
- C'est la version qui a permis à Lua d'être largement adopté dans les jeux
### Lua 5.1 : La norme (2006)
- **Récupérateur de mémoire incrémentiel**
- Opérateur de longueur `#`
-Fonction `module()`
- Modification du fonctionnement de l'environnement mondial
- **Cette version devient la version la plus largement intégrée** (LuaJIT cible 5.1)
### Lua 5.2 : raffinements (2011)
-`_ENV`— environnement par morceau (globaux plus propres)
- L'instruction`goto`renvoie
- Tables d'éphémères (amélioration GC)
- Améliorations du système de packages
### Lua 5.3 : Entiers et bits (2015)
- **Sous-type entier** — distinct de float
- **Opérateurs au niveau du bit** —`&`,`|`,`~`,`<<`,`>>`
- **Prise en charge UTF-8** — bibliothèque`utf8`intégrée
- Division d'étage`//`
- Chaîne`pack`/`unpack`pour les données binaires
### Lua 5.4 : GC générationnel (2020)
- **Goublier générationnel** — de bien meilleures pauses GC
- ** Variables `<const>`** — vraies constantes
- ** Variables `<close>`** — variables à fermer (gestion des ressources, comme`defer`ou`with`)
- Métaméthode `tostring`
- Sous-types de chaînes (chaînes courtes ou longues optimisées différemment)
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
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

## Lua dans les jeux
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

## Principes de conception clés
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Croissance de l'écosystème
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
