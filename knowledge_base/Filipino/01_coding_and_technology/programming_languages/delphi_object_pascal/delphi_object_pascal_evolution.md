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
# Delphi / Object Pascal — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Pascal | 1970 | **Niklaus Wirth** ay lumikha ng Pascal (ETH Zurich) |
| Turbo Pascal 1 | 1983 | **Borland** — mabilis, mura, IDE-based (Anders Hejlsberg) |
| Turbo Pascal 3 | 1986 | Mga yunit, suporta sa overlay |
| Turbo Pascal 5 | 1988 | **Integrated debugger**, mga pagpapahusay ng IDE |
| Turbo Pascal 5.5 | 1989 | **Object-oriented Pascal** — mga bagay, pamana |
| Turbo Pascal 6 | 1989 | Mga pagpapahusay sa OOP, mga yunit |
| Turbo Pascal 7 | 1992 | Huling DOS-based na Turbo Pascal |
| Delphi 1 | 1995 | **Visual programming** — VCL, mga bahagi, Windows GUI |
| Delphi 2 | 1996 | 32-bit na Windows |
| Delphi 3 | 1997 | Suporta sa COM/ActiveX |
| Delphi 4 | 1998 | Mga dynamic na array, overloading ng function |
| Delphi 5 | 1999 | **ADO**, WebSnap |
| Delphi 6 | 2001 | **Mga Serbisyo sa Web**, CLX (cross-platform) |
| Delphi 7 | 2002 | **Pinakasikat na bersyon** — stable, mabilis |
| Delphi 8 | 2003 | .NET na suporta |
| Delphi 2005 | 2005 | Unicode (partial), generics |
| Delphi 2006 | 2006 | **Generics**, anonymous na mga pamamaraan |
| Delphi 2007 | 2007 | Unicode (buo), suporta sa Vista |
| Delphi 2009 | 2008 | **Buong Unicode** (UTF-16), mga pagpapahusay sa RTTI |
| Delphi 2010 | 2009 | RTTI, pinahusay na mga tala |
| Delphi XE | 2010 | Cross-platform prep |
| Delphi XE2 | 2011 | **FireMonkey** — cross-platform (Windows, macOS) |
| Delphi XE3 | 2012 | **iOS support** |
| Delphi XE4 | 2013 | **Suporta sa Android** |
| Delphi XE7 | 2014 | Mga pagpapahusay sa maraming device |
| Delphi 10 Seattle | 2015 | Suporta sa Windows 10 |
| Delphi 10.4 Sydney | 2020 | **Mataas na DPI**, pinahusay na RTL |
| Delphi 11 Alexandria | 2021 | **64-bit macOS**, Android 64-bit |
| Delphi 12 Athens | 2023 | **Modernong IDE**, pinahusay na compiler |
| Delphi 12.2 | 2024 | Mga karagdagang pagpapabuti |
## Mga Pangunahing Milestone
### Pascal (1970–1982)
- **1970**: Nilikha ni Niklaus Wirth si Pascal sa ETH Zurich
- **Layunin**: Pagtuturo ng structured programming — malinis, ligtas sa uri
- Mga pangunahing tampok:`record`,`procedure`,`function`,`begin`/`end`, malakas na pagta-type
- UCSD Pascal (1978) — portable, p-code machine
### Turbo Pascal (1983–1992)
- **1983**: Lumilikha si Anders Hejlsberg ng Turbo Pascal para sa Borland
- **Rebolusyonaryo**: Mabilis na compiler, pinagsamang IDE, mura ($49.95)
- **5.5 (1989)**: Mga Bagay — OOP sa Pascal (`object`, mana)
- **7 (1992)**: Huling bersyon ng DOS — maalamat na bilis at pagiging maaasahan
### Delphi 1–7: The Golden Age (1995–2002)
- **1995**: Delphi 1 — visual programming, VCL (Visual Component Library)
- **2 (1996)**: 32-bit na Windows
- **7 (2002)**: Pinakatanyag na bersyon — mabilis, matatag, malawakang ginagamit
- Rapid Application Development (RAD) — drag-and-drop GUI
### Delphi 2005–XE: Mga Makabagong Tampok (2005–2010)
- **2006**: Mga generic, hindi kilalang pamamaraan
- **2009**: Buong Unicode (UTF-16 string)
- **2010**: Pinahusay na RTTI (reflection)
### Delphi XE2+: Cross-Platform (2011–kasalukuyan)
- **XE2 (2011)**: FireMonkey — cross-platform framework (Windows, macOS)
- **XE3 (2012)**: suporta sa iOS
- **XE4 (2013)**: Suporta sa Android
- **11 (2021)**: 64-bit macOS, Android 64-bit
- **12 (2023)**: Modern IDE, pinahusay na compiler
## Syntax Evolution
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

## Ebolusyon ng Tampok
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Paglago ng Ecosystem
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
