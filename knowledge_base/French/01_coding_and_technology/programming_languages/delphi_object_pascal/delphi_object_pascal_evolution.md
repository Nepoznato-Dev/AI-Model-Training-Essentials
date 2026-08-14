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
# Delphi / Object Pascal — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| Pascal | 1970 | **Niklaus Wirth** crée Pascal (ETH Zurich) |
| TurboPascal 1 | 1983 | **Borland** — rapide, bon marché, basé sur IDE (Anders Hejlsberg) |
| TurboPascal 3 | 1986 | Unités, support de superposition |
| TurboPascal 5 | 1988 | **Débogueur intégré**, améliorations de l'IDE |
| TurboPascal 5.5 | 1989 | **Pascal orienté objet** — objets, héritage |
| TurboPascal 6 | 1989 | Améliorations de la POO, unités |
| TurboPascal 7 | 1992 | Dernier Turbo Pascal basé sur DOS |
| Delphes 1 | 1995 | **Programmation visuelle** — VCL, composants, interface graphique Windows |
| Delphes 2 | 1996 | Windows 32 bits |
| Delphes 3 | 1997 | Prise en charge COM/ActiveX |
| Delphes 4 | 1998 | Tableaux dynamiques, surcharge de fonctions |
| Delphes 5 | 1999 | **ADO**, WebSnap |
| Delphes 6 | 2001 | **Services Web**, CLX (multiplateforme) |
| Delphes 7 | 2002 | **Version la plus populaire** — stable, rapide |
| Delphes 8 | 2003 | Prise en charge .NET |
| Delphes 2005 | 2005 | Unicode (partiel), génériques |
| Delphes 2006 | 2006 | **Génériques**, méthodes anonymes |
| Delphes 2007 | 2007 | Unicode (complet), prise en charge de Vista |
| Delphes 2009 | 2008 | **Unicode complet** (UTF-16), améliorations RTTI |
| Delphes 2010 | 2009 | RTTI, enregistrements améliorés |
| Delphi XE | 2010 | Préparation multiplateforme |
| Delphes XE2 | 2011 | **FireMonkey** — multiplateforme (Windows, macOS) |
| Delphes XE3 | 2012 | **Prise en charge iOS** |
| Delphes XE4 | 2013 | **Support Android** |
| Delphes XE7 | 2014 | Améliorations multi-appareils |
| Delphes 10 Seattle | 2015 | Prise en charge de Windows 10 |
| Delphes 10.4 Sydney | 2020 | **Haute résolution**, RTL amélioré |
| Delphes 11 Alexandrie | 2021 | **MacOS 64 bits**, Android 64 bits |
| Delphes 12 Athènes | 2023 | **IDE moderne**, compilateur amélioré |
| Delphes 12.2 | 2024 | Autres améliorations |
## Étapes majeures
###Pascal (1970-1982)
- **1970** : Niklaus Wirth crée Pascal à l'ETH Zurich
- **Objectif** : Enseigner la programmation structurée — propre et sécurisée
- Principales caractéristiques : `record`, `procedure`, `function`,`begin`/ `end`, typage fort
- UCSD Pascal (1978) — machine portable à code P
### TurboPascal (1983-1992)
- **1983** : Anders Hejlsberg crée Turbo Pascal pour Borland
- **Révolutionnaire** : compilateur rapide, IDE intégré, bon marché (49,95 $)
- **5.5 (1989)** : Objets — POO en Pascal (`object`, héritage)
- **7 (1992)** : Dernière version DOS — vitesse et fiabilité légendaires
### Delphi 1-7 : L'âge d'or (1995-2002)
- **1995** : Delphi 1 — programmation visuelle, VCL (Visual Component Library)
- **2 (1996)** : Windows 32 bits
- **7 (2002)** : version la plus populaire — rapide, stable, largement utilisée
- Développement rapide d'applications (RAD) - interface graphique glisser-déposer
### Delphi 2005–XE : fonctionnalités modernes (2005–2010)
- **2006** : Génériques, méthodes anonymes
- **2009** : Unicode complet (chaînes UTF-16)
- **2010** : RTTI amélioré (réflexion)
### Delphi XE2+ : multiplateforme (depuis 2011)
- **XE2 (2011)** : FireMonkey — framework multiplateforme (Windows, macOS)
- **XE3 (2012)** : prise en charge iOS
- **XE4 (2013)** : prise en charge d'Android
- **11 (2021)** : macOS 64 bits, Android 64 bits
- **12 (2023)** : IDE moderne, compilateur amélioré
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
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

## Principes de conception clés
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Croissance de l'écosystème
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
