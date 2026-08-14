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
# Ada - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Ada 83 | 1983 | **Primer estándar** (MIL-STD-1815A): lleva el nombre de Ada Lovelace |
| Ada 87 | 1987 | Revisión menor (precisión, reglas de accesibilidad) |
| Ada 95 | 1995 | **Principal**: programación orientada a objetos (tipos etiquetados), objetos protegidos, mejoras en las tareas |
| Ada 2005 | 2005 | **Interfaces**, tipos de acceso anónimo, mejoras en el bucle `for`/`while` |
| Ada 2012 | 2012 | **Programación orientada a aspectos**, contratos (pre/poscondiciones),`iterator`|
| Año 2022 | 2022 | **`with ghost`**, construcciones paralelas, mejoras en tiempo real |
## Hitos importantes
### Ada 83 — El nacimiento (1983)
- **1983**: El Departamento de Defensa de EE. UU. exige un lenguaje único para los sistemas integrados
- Jean Ichbiah lidera el diseño en CII Honeywell Bull (Francia)
- Nombrado en honor a Ada Lovelace, primera programadora informática.
- Características clave: tipificación segura, paquetes, tareas (concurrencia), genéricos, excepciones
- **Objetivo**: Sistemas críticos para la seguridad: aviación, defensa, espacio
### Ada 95 - Ada orientada a objetos (1995)
- **Primer lenguaje OO estandarizado ISO** (antes de que se estandarizara Java)
- Tipos etiquetados (clases), tipos para toda la clase, despacho dinámico
- Objetos protegidos (acceso seguro a datos concurrentes)
- Paquetes secundarios (biblioteca jerárquica)
- Configuración basada en Pragma
### Ada 2005 — Refinamientos (2005)
- Interfaces (herencia múltiple de interfaz)
- Tipos de acceso anónimo (punteros simplificados)
- Mejoras en el bucle `for`
- Bibliotecas de contenedores (listas doblemente enlazadas, vectores, mapas)
- Declaración`return`extendida
### Ada 2012 — Contratos y aspectos (2012)
- **Programación orientada a aspectos**: cláusulas`aspect`adjuntas a las declaraciones
- **Contratos**: `Pre`, `Post`, `Type_Invariant`: verificación formal integrada
- Soporte de iterador (`for X of Container loop`)
- Indicador `overriding`
- Funciones de expresión: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Paralelo y fantasma (2022)
- **`with ghost`**: Código fantasma para verificación (compilado en producción)
- **Construcciones paralelas**: bucles `parallel`, bloques `parallel`
- Mejoras en tiempo real
- Mejoras en los contenedores.
- Refinamientos de aspecto `Iterator`
## Evolución de la sintaxis
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

## Evolución de funciones
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Principios clave de diseño
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Crecimiento del ecosistema
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
