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
# Delphi / Object Pascal: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Pasquale | 1970 | **Niklaus Wirth** crea Pascal (ETH Zurigo) |
| Turbo Pascal 1 | 1983 | **Borland**: veloce, economico, basato su IDE (Anders Hejlsberg) |
| Turbo Pascal 3 | 1986 | Unità, supporto sovrapposto |
| Turbo Pascal 5 | 1988 | **Debugger integrato**, miglioramenti all'IDE |
| Turbo Pascal 5.5 | 1989 | **Pascal orientato agli oggetti** — oggetti, ereditarietà |
| Turbo Pascal 6 | 1989 | Miglioramenti OOP, unità |
| Turbo Pascal 7 | 1992 | Ultimo Turbo Pascal basato su DOS |
| Delfi 1 | 1995 | **Programmazione visiva**: VCL, componenti, GUI di Windows |
| Delfi 2 | 1996 | Windows a 32 bit |
| Delfi 3 | 1997 | Supporto COM/ActiveX |
| Delfi 4 | 1998 | Array dinamici, sovraccarico di funzioni |
| Delfi 5 | 1999 | **ADO**, WebSnap |
| Delfi 6 | 2001 | **Servizi Web**, CLX (multipiattaforma) |
| Delfi 7 | 2002| **Versione più popolare**: stabile, veloce |
| Delfi 8 | 2003| Supporto .NET |
| Delfi 2005 | 2005| Unicode (parziale), generici |
| Delfi 2006 | 2006| **Generici**, metodi anonimi |
| Delfi 2007 | 2007| Supporto Unicode (completo), Vista |
| Delfi 2009 | 2008| **Unicode completo** (UTF-16), miglioramenti RTTI |
| Delfi 2010 | 2009| RTTI, record potenziati |
| Delphi XE | 2010| Preparazione multipiattaforma |
| Delphi XE2 | 2011 | **FireMonkey** — multipiattaforma (Windows, macOS) |
| Delphi XE3 | 2012| **Supporto iOS** |
| Delphi XE4 | 2013| **Supporto Android** |
| Delphi XE7 | 2014| Miglioramenti multi-dispositivo |
| Delfi 10 Seattle | 2015| Supporto per Windows 10 |
| Delfi 10.4 Sydney | 2020 | **DPI elevato**, RTL migliorato |
| Delfi 11 Alessandria | 2021 | **macOS a 64 bit**, Android a 64 bit |
| Delfi 12 Atene | 2023 | **IDE moderno**, compilatore migliorato |
| Delfi 12.2 | 2024 | Ulteriori miglioramenti |
## Traguardi importanti
### Pascal (1970–1982)
- **1970**: Niklaus Wirth crea Pascal al Politecnico federale di Zurigo
- **Obiettivo**: insegnare la programmazione strutturata: pulita e sicura per i tipi
- Caratteristiche principali:`record`,`procedure`,`function`,`begin`/`end`, digitazione forte
- UCSD Pascal (1978) — macchina portatile con codice P
### Turbo Pascal (1983-1992)
- **1983**: Anders Hejlsberg crea Turbo Pascal per Borland
- **Rivoluzionario**: compilatore veloce, IDE integrato, economico ($49,95)
- **5.5 (1989)**: Oggetti - OOP in Pascal (`object`, ereditarietà)
- **7 (1992)**: ultima versione DOS: velocità e affidabilità leggendarie
### Delfi 1–7: L'età dell'oro (1995–2002)
- **1995**: Delphi 1 — programmazione visuale, VCL (Visual Component Library)
- **2 (1996)**: Windows a 32 bit
- **7 (2002)**: versione più popolare: veloce, stabile, ampiamente utilizzata
- Sviluppo rapido di applicazioni (RAD): GUI drag-and-drop
### Delphi 2005–XE: funzionalità moderne (2005–2010)
- **2006**: Generici, metodi anonimi
- **2009**: Unicode completo (stringhe UTF-16)
- **2010**: RTTI migliorato (riflessione)
### Delphi XE2+: multipiattaforma (2011-oggi)
- **XE2 (2011)**: FireMonkey — framework multipiattaforma (Windows, macOS)
- **XE3 (2012)**: supporto iOS
- **XE4 (2013)**: supporto Android
- **11 (2021)**: macOS a 64 bit, Android a 64 bit
- **12 (2023)**: IDE moderno, compilatore migliorato
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
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

## Principi chiave di progettazione
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Crescita dell'ecosistema
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
