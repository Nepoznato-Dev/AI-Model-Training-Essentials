<!--
---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ada, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ada — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| Ada 83 | 1983 | **Première norme** (MIL-STD-1815A) — nommée d'après Ada Lovelace |
| Ada 87 | 1987 | Révision mineure (précision, règles d'accessibilité) |
| Ada 95 | 1995 | **Majeur** : POO (types balisés), objets protégés, améliorations des tâches |
| Ada2005 | 2005 | **Interfaces**, types d'accès anonymes, améliorations des boucles`for`/`while`|
| Ada 2012 | 2012 | **Programmation orientée aspect**, contrats (pré/postconditions),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, constructions parallèles, améliorations en temps réel |
## Étapes majeures
### Ada 83 — La Naissance (1983)
- **1983** : le Département américain de la Défense impose un langage unique pour les systèmes embarqués
- Jean Ichbiah dirige le design chez CII Honeywell Bull (France)
- Nommé d'après Ada Lovelace - première programmeuse informatique
- Fonctionnalités clés : typage fort, packages, tâches (concurrence), génériques, exceptions
- **Objectif** : Systèmes critiques pour la sécurité – aviation, défense, espace
### Ada 95 — Ada orienté objet (1995)
- **Premier langage OO normalisé ISO** (avant la standardisation de Java)
- Types balisés (classes), types à l'échelle de la classe, répartition dynamique
- Objets protégés (accès simultané sécurisé aux données)
- Packages enfants (bibliothèque hiérarchique)
- Configuration basée sur Pragma
### Ada 2005 — Raffinements (2005)
- Interfaces (héritage multiple d'interface)
- Types d'accès anonymes (pointeurs simplifiés)
- Améliorations de la boucle `for`
- Bibliothèques de conteneurs (listes doublement liées, vecteurs, cartes)
- Instruction`return`étendue
### Ada 2012 — Contrats & Aspects (2012)
- **Programmation orientée aspect** : clauses`aspect`attachées aux déclarations
- **Contrats** :`Pre`,`Post`,`Type_Invariant`— vérification formelle intégrée
- Prise en charge des itérateurs (`for X of Container loop`)
- Indicateur `overriding`
- Fonctions d'expression : `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Parallèle et fantôme (2022)
- **`with ghost`** : Code fantôme pour vérification (compilé en production)
- **Constructions parallèles** : boucles `parallel`, blocs `parallel`
- Améliorations en temps réel
- Améliorations des conteneurs
- Affinements d'aspect `Iterator`
## Évolution de la syntaxe
```ada
-- Ada 83: Package-based design
package Stack is
   procedure Push(Item : in Integer);
   function Pop return Integer;
   Stack_Empty : exception;
end Stack;

package body Stack is
   Max : constant := 100;
   Data : array(1..Max) of Integer;
   Top : Integer range 0..Max := 0;

   procedure Push(Item : in Integer) is
   begin
      Top := Top + 1;
      Data(Top) := Item;
   end Push;

   function Pop return Integer is
      Result : Integer;
   begin
      if Top = 0 then raise Stack_Empty; end if;
      Result := Data(Top);
      Top := Top - 1;
      return Result;
   end Pop;
end Stack;

-- Ada 95: Object-oriented
type Shape is tagged record
   X, Y : Float;
end record;

function Area(S : Shape) return Float is
begin
   return 0.0;
end Area;

type Circle is new Shape with record
   Radius : Float;
end record;

function Area(C : Circle) return Float is
begin
   return 3.14159 * C.Radius ** 2;
end Area;

-- Ada 2012: Contracts and aspects
type Temperature is new Float
   with Dynamic_Predicate => Temperature >= -273.15;

procedure Set_Temp(T : in out Temperature)
   with Pre  => T >= -273.15,
        Post => T'Old < T;  -- temperature must increase

-- Expression functions (Ada 2012)
function Double(X : Integer) return Integer is (X * 2);

-- Ada 2022: Parallel constructs
parallel
   for I in Data'Range loop
      Data(I) := Compute(I);
   end loop;

-- Ada 2022: Ghost code for verification
procedure Process(X : in out Integer)
   with Ghost => True,
        Pre   => X > 0,
        Post  => X > X'Old;
```

## Évolution des fonctionnalités
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Principes de conception clés
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Croissance de l'écosystème
```
1983: Ada 83 — DoD mandate, defense/aviation adoption
1987: Ada 87 — minor fixes
1995: Ada 95 — OOP, ISO standard
1995: GNAT (GNU NYU Ada Translator) — open source compiler
2005: Ada 2005 — interfaces, containers
2012: Ada 2012 — contracts, aspects
2015: SPARK 2014 — formal verification for Ada
2022: Ada 2022 — parallel, ghost code
2025: Ada used in: aviation (DO-178C), space (ESA), rail, defense
       Compilers: GNAT (open source), ObjectAda, AdaCore tools
       SPARK subset used for formal verification of critical code
```
