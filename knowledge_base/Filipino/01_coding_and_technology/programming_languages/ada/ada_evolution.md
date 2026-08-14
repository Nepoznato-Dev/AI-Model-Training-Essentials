---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Ada — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Ada 83 | 1983 | **Unang pamantayan** (MIL-STD-1815A) — ipinangalan kay Ada Lovelace |
| Ada 87 | 1987 | Maliit na rebisyon (katumpakan, mga panuntunan sa pagiging naa-access) |
| Ada 95 | 1995 | **Major**: OOP (mga naka-tag na uri), mga protektadong bagay, mga pagpapahusay sa gawain |
| Ada 2005 | 2005 | **Mga Interface**, anonymous na mga uri ng access,`for`/`while`loop improvements |
| Ada 2012 | 2012 | **Aspect-oriented programming**, mga kontrata (pre/postconditions),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, parallel constructs, real-time na mga pagpapabuti |
## Mga Pangunahing Milestone
### Ada 83 — The Birth (1983)
- **1983**: Ang US Department of Defense ay nag-uutos ng isang wika para sa mga naka-embed na system
- Pinangunahan ni Jean Ichbiah ang disenyo sa CII Honeywell Bull (France)
- Pinangalanan pagkatapos ng Ada Lovelace — unang computer programmer
- Mga pangunahing tampok: malakas na pag-type, mga pakete, mga gawain (concurrency), mga generic, mga pagbubukod
- **Layunin**: Mga sistemang kritikal sa kaligtasan — aviation, defense, space
### Ada 95 — Object-Oriented Ada (1995)
- **Unang ISO-standardized na OO na wika** (bago na-standardize ang Java)
- Mga naka-tag na uri (mga klase), uri sa buong klase, dynamic na dispatch
- Mga protektadong bagay (ligtas kasabay na pag-access ng data)
- Mga pakete ng bata (hierarchical library)
- Pragma-based na pagsasaayos
### Ada 2005 — Mga Pagpipino (2005)
- Mga Interface (multiple inheritance ng interface)
- Anonymous na mga uri ng access (pinasimpleng mga pointer)
-`for`mga pagpapabuti ng loop
- Mga aklatan ng lalagyan (double-linked na mga listahan, vector, mapa)
- Extended`return`na pahayag
### Ada 2012 — Mga Kontrata at Aspekto (2012)
- **Aspect-oriented programming**:`aspect`clause na naka-attach sa mga deklarasyon
- **Mga Kontrata**:`Pre`,`Post`,`Type_Invariant`— built in na pormal na pag-verify
- Suporta sa Iterator (`for X of Container loop`)
-`overriding`indicator
- Mga function ng expression: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Parallel & Ghost (2022)
- **`with ghost`**: Ghost code para sa pag-verify (compile out sa production)
- **Parallel constructs**:`parallel`loops,`parallel`blocks
- Real-time na mga pagpapabuti
- Mga pagpapahusay sa lalagyan
- Mga pagpipino ng aspeto ng `Iterator`
## Syntax Evolution
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

## Ebolusyon ng Tampok
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Pangunahing Prinsipyo ng Disenyo
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Paglago ng Ecosystem
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
