<!--
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

-->
# Delphi / Object Pascal – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Pascal | 1970 | **Niklaus Wirth** gründet Pascal (ETH Zürich) |
| Turbo Pascal 1 | 1983 | **Borland** – schnell, günstig, IDE-basiert (Anders Hejlsberg) |
| Turbo Pascal 3 | 1986 | Einheiten, Overlay-Unterstützung |
| Turbo Pascal 5 | 1988 | **Integrierter Debugger**, IDE-Verbesserungen |
| Turbo Pascal 5.5 | 1989 | **Objektorientiertes Pascal** – Objekte, Vererbung |
| Turbo Pascal 6 | 1989 | OOP-Verbesserungen, Einheiten |
| Turbo Pascal 7 | 1992 | Letzter DOS-basierter Turbo Pascal |
| Delphi 1 | 1995 | **Visuelle Programmierung** – VCL, Komponenten, Windows GUI |
| Delphi 2 | 1996 | 32-Bit-Windows |
| Delphi 3 | 1997 | COM/ActiveX-Unterstützung |
| Delphi 4 | 1998 | Dynamische Arrays, Funktionsüberladung |
| Delphi 5 | 1999 | **ADO**, WebSnap |
| Delphi 6 | 2001 | **Webdienste**, CLX (plattformübergreifend) |
| Delphi 7 | 2002 | **Beliebteste Version** – stabil, schnell |
| Delphi 8 | 2003 | .NET-Unterstützung |
| Delphi 2005 | 2005 | Unicode (teilweise), Generika |
| Delphi 2006 | 2006 | **Generika**, anonyme Methoden |
| Delphi 2007 | 2007 | Unicode (vollständig), Vista-Unterstützung |
| Delphi 2009 | 2008 | **Vollständiger Unicode** (UTF-16), RTTI-Verbesserungen |
| Delphi 2010 | 2009 | RTTI, erweiterte Aufzeichnungen |
| Delphi XE | 2010 | Plattformübergreifende Vorbereitung |
| Delphi XE2 | 2011 | **FireMonkey** – plattformübergreifend (Windows, macOS) |
| Delphi XE3 | 2012 | **iOS-Unterstützung** |
| Delphi XE4 | 2013 | **Android-Unterstützung** |
| Delphi XE7 | 2014 | Verbesserungen bei mehreren Geräten |
| Delphi 10 Seattle | 2015 | Windows 10-Unterstützung |
| Delphi 10.4 Sydney | 2020 | **Hohe DPI**, verbessertes RTL |
| Delphi 11 Alexandria | 2021 | **64-Bit-MacOS**, Android 64-Bit |
| Delphi 12 Athen | 2023 | **Moderne IDE**, verbesserter Compiler |
| Delphi 12.2 | 2024 | Weitere Verbesserungen |
## Wichtige Meilensteine
### Pascal (1970–1982)
- **1970**: Niklaus Wirth kreiert Pascal an der ETH Zürich
- **Ziel**: Strukturierte Programmierung lehren – sauber, typsicher
- Hauptmerkmale: `record`, `procedure`, `function`,`begin`/ `end`, starkes Tippen
- UCSD Pascal (1978) – tragbares P-Code-Gerät
### Turbo Pascal (1983–1992)
- **1983**: Anders Hejlsberg kreiert Turbo Pascal für Borland
- **Revolutionär**: Schneller Compiler, integrierte IDE, günstig (49,95 $)
- **5.5 (1989)**: Objekte – OOP in Pascal (`object`, Vererbung)
- **7 (1992)**: Letzte DOS-Version – legendäre Geschwindigkeit und Zuverlässigkeit
### Delphi 1–7: Das Goldene Zeitalter (1995–2002)
- **1995**: Delphi 1 – visuelle Programmierung, VCL (Visual Component Library)
- **2 (1996)**: 32-Bit-Windows
- **7 (2002)**: Beliebteste Version – schnell, stabil, weit verbreitet
- Rapid Application Development (RAD) – Drag-and-Drop-GUI
### Delphi 2005–XE: Moderne Funktionen (2005–2010)
- **2006**: Generics, anonyme Methoden
- **2009**: Vollständiger Unicode (UTF-16-Strings)
- **2010**: Verbessertes RTTI (Reflexion)
### Delphi XE2+: Plattformübergreifend (2011–heute)
- **XE2 (2011)**: FireMonkey – plattformübergreifendes Framework (Windows, macOS)
- **XE3 (2012)**: iOS-Unterstützung
- **XE4 (2013)**: Android-Unterstützung
- **11 (2021)**: 64-Bit-MacOS, Android 64-Bit
- **12 (2023)**: Moderne IDE, verbesserter Compiler
## Syntaxentwicklung
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

## Feature-Entwicklung
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

## Wichtige Designprinzipien
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Ökosystemwachstum
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
