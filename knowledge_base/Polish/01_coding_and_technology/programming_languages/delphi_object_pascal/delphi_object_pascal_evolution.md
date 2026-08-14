---
# Metadata
title: "Delphi / Object Pascal — Version History & Evolution"
description: "Comprehensive version history and evolution of Delphi/Object Pascal from Turbo Pascal to modern Delphi."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Delphi / Object Pascal — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Pascal | 1970 | **Niklaus Wirth** tworzy Pascala (ETH Zurich) |
| Turbo Pascal 1 | 1983 | **Borland** — szybki, tani, oparty na IDE (Anders Hejlsberg) |
| TurboPascal 3 | 1986 | Jednostki, obsługa nakładek |
| TurboPascal 5 | 1988 | **Zintegrowany debuger**, ulepszenia IDE |
| TurboPascal 5.5 | 1989 | **Obiektowy Pascal** — obiekty, dziedziczenie |
| Turbo Pascal 6 | 1989 | Ulepszenia OOP, jednostki |
| TurboPascal 7 | 1992 | Ostatni Turbo Pascal oparty na systemie DOS |
| Delphi 1 | 1995 | **Programowanie wizualne** — VCL, komponenty, GUI systemu Windows |
| Delphi 2 | 1996 | 32-bitowy system Windows |
| Delphi 3 | 1997 | Obsługa COM/ActiveX |
| Delphi 4 | 1998 | Tablice dynamiczne, przeciążenie funkcji |
| Delphi 5 | 1999 | **ADO**, WebSnap |
| Delfy 6 | 2001 | **Usługi internetowe**, CLX (wieloplatformowe) |
| Delphi 7 | 2002 | **Najpopularniejsza wersja** — stabilna, szybka |
| Delphi 8 | 2003 | Obsługa .NET |
| Delfy 2005 | 2005 | Unicode (częściowy), generyczny |
| Delfy 2006 | 2006 | **Ogólne**, metody anonimowe |
| Delfy 2007 | 2007 | Unicode (pełny), obsługa Vista |
| Delfy 2009 | 2008 | **Pełny Unicode** (UTF-16), ulepszenia RTTI |
| Delfy 2010 | 2009 | RTTI, ulepszone rekordy |
| Delphi XE | 2010 | Przygotowanie na wiele platform |
| Delphi XE2 | 2011 | **FireMonkey** — wieloplatformowy (Windows, macOS) |
| Delphi XE3 | 2012 | **Obsługa iOS** |
| Delphi XE4 | 2013 | **Wsparcie Androida** |
| Delphi XE7 | 2014 | Udoskonalenia dotyczące wielu urządzeń |
| Delphi 10 Seattle | 2015 | Obsługa systemu Windows 10 |
| Delphi 10.4 Sydney | 2020 | **Wysoka rozdzielczość**, ulepszony RTL |
| Delfy 11 Aleksandria | 2021 | **64-bitowy system macOS**, Android 64-bitowy |
| Delfy 12 Ateny | 2023 | **Nowoczesne IDE**, ulepszony kompilator |
| Delphi 12.2 | 2024 | Dalsze ulepszenia |
## Główne kamienie milowe
### Pascal (1970–1982)
- **1970**: Niklaus Wirth tworzy Pascala w ETH Zurich
- **Cel**: Nauczanie programowania strukturalnego — czystego i bezpiecznego dla typów
- Kluczowe funkcje: `record`, `procedure`, `function`,`begin`/ `end`, mocne pisanie
- UCSD Pascal (1978) — przenośna maszyna z kodem p
### Turbo Pascal (1983–1992)
- **1983**: Anders Hejlsberg tworzy Turbo Pascal dla firmy Borland
- **Rewolucyjny**: Szybki kompilator, zintegrowane IDE, tani (49,95 USD)
- **5,5 (1989)**: Obiekty — OOP w Pascalu (`object`, dziedziczenie)
- **7 (1992)**: Ostatnia wersja DOS — legendarna szybkość i niezawodność
### Delfy 1–7: Złoty wiek (1995–2002)
- **1995**: Delphi 1 — programowanie wizualne, VCL (Biblioteka komponentów wizualnych)
- **2 (1996)**: 32-bitowy system Windows
- **7 (2002)**: Najpopularniejsza wersja — szybka, stabilna, szeroko stosowana
- Rapid Application Development (RAD) — graficzny interfejs użytkownika typu „przeciągnij i upuść”.
### Delphi 2005–XE: Nowoczesne funkcje (2005–2010)
- **2006**: Generics, anonimowe metody
- **2009**: Pełny Unicode (ciągi UTF-16)
- **2010**: Ulepszone RTTI (odbicie)
### Delphi XE2+: wieloplatformowy (2011 – obecnie)
- **XE2 (2011)**: FireMonkey — framework wieloplatformowy (Windows, macOS)
- **XE3 (2012)**: obsługa iOS
- **XE4 (2013)**: obsługa Androida
- **11 (2021)**: 64-bitowy system macOS, Android 64-bitowy
- **12 (2023)**: Nowoczesne IDE, ulepszony kompilator
## Ewolucja składni
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

## Ewolucja funkcji
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

## Kluczowe zasady projektowania
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Rozwój ekosystemu
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
