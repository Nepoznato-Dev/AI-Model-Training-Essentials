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
# Ada - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| Ada 83 | 1983 | **Kiwango cha kwanza** (MIL-STD-1815A) - kilichopewa jina la Ada Lovelace |
| Ada 87 | 1987 | Marekebisho madogo (usahihi, sheria za ufikivu) |
| Ada 95 | 1995 | **Meja**: OOP (aina zilizotambulishwa), vitu vilivyolindwa, uboreshaji wa kazi |
| Ada 2005 | 2005 | **Violesura**, aina za ufikiaji zisizojulikana,`for`/`while`maboresho ya kitanzi |
| Ada 2012 | 2012 | **Upangaji wenye mwelekeo wa kipengele**, mikataba (kabla/masharti),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, miundo sambamba, uboreshaji wa wakati halisi |
## Mafanikio Makuu
### Ada 83 - Kuzaliwa (1983)
- **1983**: Idara ya Ulinzi ya Marekani inaidhinisha lugha moja kwa mifumo iliyopachikwa
- Jean Ichbiah anaongoza kubuni katika CII Honeywell Bull (Ufaransa)
- Imepewa jina la Ada Lovelace - programu ya kwanza ya kompyuta
- Vipengele muhimu: kuandika kwa nguvu, vifurushi, kazi (concurrency), jenetiki, isipokuwa
- **Lengo**: Mifumo muhimu kwa usalama - anga, ulinzi, nafasi
### Ada 95 - Ada Iliyoelekezwa kwa Kitu (1995)
- **Lugha ya OO iliyosawazishwa ya ISO** (kabla ya Java kusawazishwa)
- Aina zilizowekwa alama (madarasa), aina za darasa zima, utumaji wa nguvu
- Vitu vilivyolindwa (ufikiaji salama wa data wakati huo huo)
- Vifurushi vya watoto (maktaba ya uongozi)
- Usanidi wa msingi wa Pragma
### Ada 2005 - Marekebisho (2005)
- Maingiliano (urithi nyingi za kiolesura)
- Aina za ufikiaji zisizojulikana (viashiria vilivyorahisishwa)
- Maboresho ya kitanzi cha `for`
- Maktaba za vyombo (orodha zilizounganishwa mara mbili, vekta, ramani)
- Taarifa Iliyoongezwa ya `return`
### Ada 2012 — Mikataba na Vipengele (2012)
- **Upangaji wenye mwelekeo wa kipengele**:`aspect`vifungu vilivyoambatishwa kwenye matamko
- **Mikataba**:`Pre`,`Post`,`Type_Invariant`- uthibitishaji rasmi umejengwa ndani
- Msaada wa Iterator (`for X of Container loop`)
- Kiashiria cha `overriding`
- Kazi za kujieleza: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Sambamba & Ghost (2022)
- **`with ghost`**: Nambari ya Ghost ya uthibitishaji (iliyojumuishwa katika uzalishaji)
- ** Miundo sambamba **: vitanzi vya `parallel`, vitalu vya `parallel`
- Maboresho ya wakati halisi
- Uboreshaji wa vyombo
- Maboresho ya kipengele cha `Iterator`
## Mageuzi ya Sintaksia
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

## Mageuzi ya Kipengele
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Kanuni Muhimu za Usanifu
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Ukuaji wa Mfumo ikolojia
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
