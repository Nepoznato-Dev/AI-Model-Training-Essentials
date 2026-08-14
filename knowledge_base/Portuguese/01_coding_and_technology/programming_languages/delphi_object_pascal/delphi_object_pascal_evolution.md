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
# Delphi / Object Pascal — Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Pascal | 1970 | **Niklaus Wirth** cria Pascal (ETH Zurique) |
| TurboPascal 1 | 1983 | **Borland** — rápido, barato e baseado em IDE (Anders Hejlsberg) |
| TurboPascal 3 | 1986 | Unidades, suporte de sobreposição |
| TurboPascal 5 | 1988 | **Depurador integrado**, melhorias no IDE |
| Turbo Pascal 5.5 | 1989 | **Pascal orientado a objetos** — objetos, herança |
| TurboPascal 6 | 1989 | Melhorias OOP, unidades |
| TurboPascal 7 | 1992 | Último Turbo Pascal baseado em DOS |
| Delfos 1 | 1995 | **Programação visual** — VCL, componentes, GUI do Windows |
| Delfos 2 | 1996 | Windows de 32 bits |
| Delfos 3 | 1997 | Suporte COM/ActiveX |
| Delfos 4 | 1998 | Matrizes dinâmicas, sobrecarga de funções |
| Delfos 5 | 1999 | **ADO**, WebSnap |
| Delfos 6 | 2001 | **Serviços Web**, CLX (plataforma cruzada) |
| Delfos 7 | 2002 | **Versão mais popular** — estável, rápida |
| Delfos 8 | 2003 | Suporte .NET |
| Delfos 2005 | 2005 | Unicode (parcial), genéricos |
| Delfos 2006 | 2006 | **Genéricos**, métodos anônimos |
| Delfos 2007 | 2007 | Unicode (completo), suporte para Vista |
| Delfos 2009 | 2008 | **Unicode completo** (UTF-16), melhorias no RTTI |
| Delfos 2010 | 2009 | RTTI, registros aprimorados |
| DelphiXE | 2010 | Preparação multiplataforma |
| DelphiXE2 | 2011 | **FireMonkey** — plataforma cruzada (Windows, macOS) |
| DelphiXE3 | 2012 | **Suporte para iOS** |
| Delphi XE4 | 2013 | **Suporte para Android** |
| Delphi XE7 | 2014 | Melhorias em vários dispositivos |
| Delphi 10 Seattle | 2015 | Suporte para Windows 10 |
| Delphi 10.4 Sydney | 2020 | **Alto DPI**, RTL aprimorado |
| Delphi 11 Alexandria | 2021 | **MacOS de 64 bits**, Android de 64 bits |
| Delphi 12 Atenas | 2023 | **IDE moderno**, compilador aprimorado |
| Delphi 12.2 | 2024 | Outras melhorias |
## Marcos importantes
### Pascal (1970–1982)
- **1970**: Niklaus Wirth cria Pascal na ETH Zurique
- **Objetivo**: Ensinar programação estruturada — limpa e com segurança de digitação
- Principais recursos: `record`, `procedure`, `function`,`begin`/ `end`, digitação forte
- UCSD Pascal (1978) — máquina portátil de código p
###Turbo Pascal (1983–1992)
- **1983**: Anders Hejlsberg cria Turbo Pascal para Borland
- **Revolucionário**: compilador rápido, IDE integrado, barato (US$ 49,95)
- **5.5 (1989)**: Objetos — OOP em Pascal (`object`, herança)
- **7 (1992)**: Última versão DOS – velocidade e confiabilidade lendárias
### Delphi 1–7: A Era de Ouro (1995–2002)
- **1995**: Delphi 1 — programação visual, VCL (Visual Component Library)
- **2 (1996)**: Windows de 32 bits
- **7 (2002)**: Versão mais popular — rápida, estável, amplamente utilizada
- Desenvolvimento Rápido de Aplicativos (RAD) — GUI de arrastar e soltar
### Delphi 2005–XE: recursos modernos (2005–2010)
- **2006**: Genéricos, métodos anônimos
- **2009**: Unicode completo (strings UTF-16)
- **2010**: RTTI aprimorado (reflexão)
### Delphi XE2+: plataforma cruzada (2011-presente)
- **XE2 (2011)**: FireMonkey — estrutura multiplataforma (Windows, macOS)
- **XE3 (2012)**: suporte para iOS
- **XE4 (2013)**: suporte para Android
- **11 (2021)**: macOS de 64 bits, Android de 64 bits
- **12 (2023)**: IDE moderno, compilador aprimorado
## Evolução da Sintaxe
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

## Evolução de recursos
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

## Princípios-chave de design
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Crescimento do Ecossistema
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
