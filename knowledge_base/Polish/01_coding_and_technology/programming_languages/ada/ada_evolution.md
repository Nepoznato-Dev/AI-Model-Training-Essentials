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
# Ada — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Ada 83 | 1983 | **Pierwszy standard** (MIL-STD-1815A) — nazwany na cześć Ady Lovelace |
| Ada 87 | 1987 | Drobna rewizja (precyzja, zasady dostępności) |
| Ada 95 | 1995 | **Główne**: OOP (oznaczone typy), chronione obiekty, ulepszenia zadań |
| Ada 2005 | 2005 | **Interfejsy**, anonimowe typy dostępu, ulepszenia pętli`for`/`while`|
| Ada 2012 | 2012 | **Programowanie aspektowe**, kontrakty (warunki wstępne/końcowe),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, konstrukcje równoległe, ulepszenia w czasie rzeczywistym |
## Główne kamienie milowe
### Ada 83 — Narodziny (1983)
- **1983**: Departament Obrony Stanów Zjednoczonych nakłada obowiązek stosowania jednego języka dla systemów wbudowanych
– Jean Ichbiah kieruje projektowaniem w CII Honeywell Bull (Francja)
- Nazwany na cześć Ady Lovelace — pierwszej programistki komputerowej
- Kluczowe cechy: silne pisanie, pakiety, zadania (współbieżność), typy generyczne, wyjątki
- **Cel**: Systemy krytyczne dla bezpieczeństwa — lotnictwo, obrona, przestrzeń kosmiczna
### Ada 95 — Ada obiektowa (1995)
- **Pierwszy język OO zgodny ze standardem ISO** (przed standaryzacją Java)
- Typy oznaczone (klasy), typy ogólnoklasowe, dynamiczna wysyłka
- Obiekty chronione (bezpieczny, współbieżny dostęp do danych)
- Pakiety podrzędne (biblioteka hierarchiczna)
- Konfiguracja oparta na Pragmie
### Ada 2005 — Udoskonalenia (2005)
- Interfejsy (wielokrotne dziedziczenie interfejsu)
- Anonimowe typy dostępu (uproszczone wskaźniki)
— Ulepszenia pętli `for`
- Biblioteki kontenerowe (podwójnie połączone listy, wektory, mapy)
- Rozszerzona instrukcja `return`
### Ada 2012 — Kontrakty i aspekty (2012)
- **Programowanie aspektowe**: Klauzule`aspect`dołączane do deklaracji
- **Kontrakty**:`Pre`,`Post`,`Type_Invariant`— wbudowana weryfikacja formalna
- Obsługa iteratorów (`for X of Container loop`)
- Wskaźnik `overriding`
- Funkcje wyrażeń: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Równolegle i Duch (2022)
- **`with ghost`**: Kod Ghost do weryfikacji (skompilowany w środowisku produkcyjnym)
- **Konstrukcje równoległe**: pętle `parallel`, bloki `parallel`
- Ulepszenia w czasie rzeczywistym
- Ulepszenia kontenerów
- Udoskonalenia aspektu `Iterator`
## Ewolucja składni
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

## Ewolucja funkcji
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Kluczowe zasady projektowania
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Rozwój ekosystemu
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
