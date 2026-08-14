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

# Ada — Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Ada 83 | 1983 | **Primeiro padrão** (MIL-STD-1815A) — em homenagem a Ada Lovelace |
| Ada 87 | 1987 | Pequena revisão (precisão, regras de acessibilidade) |
| Ada 95 | 1995 | **Principal**: OOP (tipos marcados), objetos protegidos, melhorias nas tarefas |
| Ada 2005 | 2005 | **Interfaces**, tipos de acesso anônimo, melhorias de loop`for`/`while`|
| Ada 2012 | 2012 | **Programação orientada a aspectos**, contratos (pré/pós-condições),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, construções paralelas, melhorias em tempo real |
## Marcos importantes
### Ada 83 — O Nascimento (1983)
- **1983**: Departamento de Defesa dos EUA exige uma linguagem única para sistemas embarcados
- Jean Ichbiah lidera design na CII Honeywell Bull (França)
- Nomeado em homenagem a Ada Lovelace — primeira programadora de computador
- Principais recursos: digitação forte, pacotes, tarefas (simultaneidade), genéricos, exceções
- **Objetivo**: Sistemas críticos para a segurança — aviação, defesa, espaço
### Ada 95 — Ada Orientada a Objetos (1995)
- **Primeira linguagem OO padronizada pela ISO** (antes da padronização do Java)
- Tipos marcados (classes), tipos para toda a classe, despacho dinâmico
- Objetos protegidos (acesso seguro a dados simultâneos)
- Pacotes filhos (biblioteca hierárquica)
- Configuração baseada em Pragma
### Ada 2005 — Refinamentos (2005)
- Interfaces (herança múltipla de interface)
- Tipos de acesso anônimos (ponteiros simplificados)
- Melhorias no loop `for`
- Bibliotecas de contêineres (listas duplamente vinculadas, vetores, mapas)
- Instrução`return`estendida
### Ada 2012 — Contratos e Aspectos (2012)
- **Programação orientada a aspectos**: cláusulas`aspect`anexadas a declarações
- **Contratos**:`Pre`,`Post`,`Type_Invariant`— verificação formal integrada
- Suporte ao iterador (`for X of Container loop`)
- Indicador `overriding`
- Funções de expressão: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Paralelo e Fantasma (2022)
- **`with ghost`**: Código fantasma para verificação (compilado em produção)
- **Construções paralelas**: loops `parallel`, blocos `parallel`
- Melhorias em tempo real
- Melhorias nos contêineres
- Refinamentos de aspecto `Iterator`
## Evolução da Sintaxe
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

## Evolução de recursos
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Princípios-chave de design
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Crescimento do Ecossistema
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
