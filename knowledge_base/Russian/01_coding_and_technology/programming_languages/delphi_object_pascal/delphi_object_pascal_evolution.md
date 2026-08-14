---
# Metadata
title: "Delphi / Object Pascal — Version History & Evolution"
description: "Comprehensive version history and evolution of Delphi/Object Pascal from Turbo Pascal to modern Delphi."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [delphi, object-pascal, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Delphi/Object Pascal — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Паскаль | 1970 | **Никлаус Вирт** создает Паскаль (ETH Zurich) |
| Турбо Паскаль 1 | 1983 | **Borland** — быстрый, дешевый, на базе IDE (Андерс Хейлсберг) |
| Турбо Паскаль 3 | 1986 | Единицы измерения, поддержка наложения |
| Турбо Паскаль 5 | 1988 | **Встроенный отладчик**, улучшения IDE |
| Турбо Паскаль 5.5 | 1989 | **Объектно-ориентированный Паскаль** — объекты, наследование |
| Турбо Паскаль 6 | 1989 | Улучшения ООП, ед. |
| Турбо Паскаль 7 | 1992 | Последний Turbo Pascal на базе DOS |
| Дельфи 1 | 1995 | **Визуальное программирование** — VCL, компоненты, графический интерфейс Windows |
| Дельфи 2 | 1996 | 32-битная Windows |
| Дельфи 3 | 1997 | Поддержка COM/ActiveX |
| Дельфи 4 | 1998 | Динамические массивы, перегрузка функций |
| Дельфи 5 | 1999 | **ADO**, WebSnap |
| Дельфи 6 | 2001 | **Веб-службы**, CLX (кросс-платформенный) |
| Дельфи 7 | 2002 | **Самая популярная версия** — стабильная, быстрая |
| Дельфи 8 | 2003 | Поддержка .NET |
| Дельфи 2005 | 2005 | Юникод (частичный), дженерики |
| Дельфи 2006 | 2006 | **Обобщенные**, анонимные методы |
| Дельфи 2007 | 2007 | Unicode (полная версия), поддержка Vista |
| Дельфи 2009 | 2008 | **Полный Unicode** (UTF-16), улучшения RTTI |
| Дельфи 2010 | 2009 | RTTI, расширенные записи |
| Делфи XE | 2010 | Кроссплатформенная подготовка |
| Делфи ХЕ2 | 2011 | **FireMonkey** — кроссплатформенность (Windows, macOS) |
| Делфи XE3 | 2012 | **Поддержка iOS** |
| Делфи XE4 | 2013 | **Поддержка Android** |
| Делфи XE7 | 2014 | Улучшения для нескольких устройств |
| Делфи 10 Сиэтл | 2015 | Поддержка Windows 10 |
| Делфи 10.4 Сидней | 2020 | **Высокое разрешение**, улучшенное отображение справа налево |
| Дельфи 11 Александрия | 2021 | **64-разрядная версия macOS**, 64-разрядная версия Android |
| Дельфи 12 Афины | 2023 | **Современная IDE**, улучшенный компилятор |
| Дельфи 12.2 | 2024 | Дальнейшие улучшения |
## Основные вехи
### Паскаль (1970–1982)
- **1970**: Никлаус Вирт создает Паскаль в ETH Zurich.
- **Цель**: обучение структурному программированию — чистому и типобезопасному.
- Ключевые особенности: `record`, `procedure`, `function`,`begin`/ `end`, строгая типизация.
- UCSD Pascal (1978) — портативная машина с p-кодом.
### Турбо Паскаль (1983–1992)
- **1983**: Андерс Хейлсберг создает Turbo Pascal для Borland.
- **Революция**: быстрый компилятор, интегрированная среда разработки, дешево (49,95 долларов США).
- **5.5 (1989)**: Объекты — ООП в Паскале (`object`, наследование)
- **7 (1992 г.)**: Последняя версия DOS — легендарная скорость и надежность.
### Дельфи 1–7: Золотой век (1995–2002)
- **1995**: Delphi 1 — визуальное программирование, VCL (библиотека визуальных компонентов).
- **2 (1996)**: 32-разрядная версия Windows.
- **7 (2002 г.)**: Самая популярная версия — быстрая, стабильная, широко используемая.
- Быстрая разработка приложений (RAD) — графический интерфейс с возможностью перетаскивания.
### Delphi 2005–XE: современные возможности (2005–2010 гг.)
- **2006**: дженерики, анонимные методы.
- **2009**: Полный Юникод (строки UTF-16).
- **2010**: улучшенный RTTI (отражение)
### Delphi XE2+: кроссплатформенность (2011 – настоящее время)
- **XE2 (2011 г.)**: FireMonkey — кроссплатформенная платформа (Windows, macOS)
- **XE3 (2012 г.)**: поддержка iOS.
- **XE4 (2013 г.)**: поддержка Android.
- **11 (2021 г.)**: 64-разрядная версия macOS, 64-разрядная версия Android.
- **12 (2023 г.)**: Современная IDE, улучшенный компилятор.
## Эволюция синтаксиса
```pascal
{ Pascal (1970): Structured programming }
program Hello;
var
  Name: string;
begin
  Write('Enter name: ');
  ReadLn(Name);
  WriteLn('Hello, ', Name, '!');
end.

{ Turbo Pascal 5.5 (1989): Objects }
type
  PAnimal = ^TAnimal;
  TAnimal = object
    Name: string;
    procedure Speak; virtual;
  end;

  PDog = ^TDog;
  TDog = object(TAnimal)
    procedure Speak; virtual;
  end;

procedure TDog.Speak;
begin
  WriteLn('Woof!');
end;

{ Delphi 1 (1995): Visual programming, VCL }
type
  TForm1 = class(TForm)
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello, Delphi!');
end;

{ Delphi 2006: Generics }
type
  TPair<TKey, TValue> = class
    Key: TKey;
    Value: TValue;
    constructor Create(const AKey: TKey; const AValue: TValue);
  end;

{ Delphi 2009: Unicode strings }
var
  S: string;  { UTF-16 UnicodeString }
begin
  S := 'Hello, 世界!';  { Unicode works natively }
end;

{ Delphi 12 (2023): Modern Delphi }
type
  TMyClass = class
    class function Create: TMyClass; static;
    procedure DoSomething; virtual; abstract;
  end;

  TRecord = record
    Value: Integer;
    class operator Implicit(V: Integer): TRecord;
  end;
```

## Эволюция функций
```
Pascal (1970):     Records, procedures, strong typing, begin/end
Turbo Pascal (1983): Integrated IDE, fast compiler, units
TP 5.5 (1989):     Objects, inheritance, virtual methods
Delphi 1 (1995):   VCL, visual programming, components
Delphi 4 (1998):   Dynamic arrays, overloading
Delphi 2006:       Generics, anonymous methods
Delphi 2009:       Full Unicode (UTF-16)
Delphi XE2 (2011): FireMonkey (cross-platform)
Delphi XE3 (2012): iOS support
Delphi XE4 (2013): Android support
Delphi 11 (2021):  64-bit macOS, Android 64-bit
Delphi 12 (2023):  Modern IDE, improved compiler
```

## Ключевые принципы проектирования
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Рост экосистемы
```
1970: Pascal created by Niklaus Wirth (ETH Zurich)
1983: Turbo Pascal — Borland, Anders Hejlsberg
1989: Turbo Pascal 5.5 — OOP in Pascal
1995: Delphi 1 — visual programming, VCL
2002: Delphi 7 — golden age, most popular version
2006: Generics, anonymous methods
2009: Full Unicode
2011: FireMonkey — cross-platform
2013: Android support
2023: Delphi 12 — modern IDE
2025: Delphi used in:
       - Windows desktop applications (enterprise)
       - Database applications (FireDAC)
       - Cross-platform mobile apps (iOS, Android)
       - Legacy systems (Turbo Pascal, Delphi 7)
       Embarcadero maintains Delphi; Free Pascal (Lazarus) is open source
```
