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

# Ада — История версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Ада 83 | 1983 | **Первый стандарт** (MIL-STD-1815A) — назван в честь Ады Лавлейс |
| Ада 87 | 1987 | Небольшая доработка (точность, правила доступности) |
| Ада 95 | 1995 | **Основное**: ООП (тегированные типы), защищенные объекты, улучшения задач |
| Ада 2005 | 2005 | **Интерфейсы**, типы анонимного доступа, улучшения цикла`for`/`while`|
| Ада 2012 | 2012 | **Аспектно-ориентированное программирование**, контракты (предварительные/постусловия),`iterator`|
| Ада 2022 | 2022 | **`with ghost`**, параллельные конструкции, улучшения в реальном времени |
## Основные вехи
### Ада 83 — Рождение (1983)
- **1983**: Министерство обороны США требует использования единого языка для встроенных систем.
- Жан Ишбиа возглавляет дизайн в CII Honeywell Bull (Франция)
- Назван в честь Ады Лавлейс — первой программистки.
- Ключевые особенности: строгая типизация, пакеты, задачи (параллелизм), дженерики, исключения.
- **Цель**: критически важные для безопасности системы — авиация, оборона, космос.
### Ада 95 — Объектно-ориентированная Ада (1995)
- **Первый объектно-ориентированный язык, стандартизованный ISO** (до стандартизации Java)
- Тегированные типы (классы), общеклассовые типы, динамическая отправка
- Защищенные объекты (безопасный одновременный доступ к данным)
- Дочерние пакеты (иерархическая библиотека)
- Конфигурация на основе Pragma
###Ада 2005 — Уточнения (2005)
- Интерфейсы (множественное наследование интерфейса)
- Анонимные типы доступа (упрощенные указатели)
- Улучшения цикла `for`.
- Библиотеки контейнеров (двухсвязные списки, векторы, карты)
- Расширенный оператор `return`.
### Ада 2012 — Контракты и аспекты (2012)
- **Аспектно-ориентированное программирование**: предложения `aspect`, прикрепленные к объявлениям.
- **Контракты**:`Pre`,`Post`,`Type_Invariant`— встроенная формальная проверка.
- Поддержка итератора (`for X of Container loop`)
- Индикатор `overriding`
- Функции выражения: `function F(X: Integer) return Integer is (X * 2);`.
### Ада 2022 — Параллель и Призрак (2022)
- **`with ghost`**: Призрачный код для проверки (составлен в производстве)
- **Параллельные конструкции**: циклы `parallel`, блоки `parallel`.
- Улучшения в реальном времени
- Улучшения контейнера
- Уточнения аспектов `Iterator`.
## Эволюция синтаксиса
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

## Эволюция функций
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Ключевые принципы проектирования
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Рост экосистемы
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
