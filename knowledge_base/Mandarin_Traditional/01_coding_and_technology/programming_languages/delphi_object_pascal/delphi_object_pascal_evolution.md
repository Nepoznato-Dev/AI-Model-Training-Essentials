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
# Delphi / Object Pascal — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|帕斯卡| 1970 | **Niklaus Wirth** 創建 Pascal（蘇黎世聯邦理工學院）|
|渦輪帕斯卡 1 | 1983 | **Borland** — 快速、廉價、基於 IDE (Anders Hejlsberg) |
|渦輪帕斯卡 3 | 1986 |單位，疊加支援|
|渦輪帕斯卡 5 | 1988 | **整合式調試器**，IDE 改進 |
|渦輪帕斯卡 5.5 | 1989 | **物件導向的 Pascal** — 物件、繼承 |
|渦輪帕斯卡 6 | 1989 | OOP 改進，單位 |
|渦輪帕斯卡 7 | 1992 |最後一個基於 DOS 的 Turbo Pascal |
|德爾福1 | 1995 | **視覺化程式設計** — VCL、元件、Windows GUI |
|德爾福2 | 1996 | 32 位元 Windows |
|德爾福3 | 1997 | COM/ActiveX 支援 |
|德爾福4 | 1998 |動態陣列、函數重載 |
|德爾福5 | 1999 | **ADO**、WebSnap |
|德爾福6 | 2001 | **網路服務**，CLX（跨平台）|
|德爾福7 | 2002 | **最受歡迎的版本** — 穩定、快速 |
|德爾福8 | 2003 | .NET 支援 |
|德爾福2005 | 2005 | Unicode（部分）、泛型 |
|德爾福2006 | 2006 | **泛型**，匿名方法 |
|德爾福2007 | 2007 | Unicode（完整），Vista 支援 |
|德爾福2009 | 2008 | **完整 Unicode** (UTF-16)、RTTI 改進 |
|德爾福2010 | 2009 | RTTI，增強記錄|
|德爾福XE | 2010 |跨平台準備|
|德爾福XE2 | 2011 | **FireMonkey** — 跨平台（Windows、macOS）|
|德爾福XE3 | 2012 | **iOS 支援** |
|德爾福XE4 | 2013 | **安卓支援** |
|德爾福XE7 | 2014年|多設備改良 |
|德爾福 10 西雅圖 | 2015 | 2015 Windows 10 支援 |
|德爾福 10.4 雪梨 | 2020 | **高 DPI**，改進的 RTL |
|德爾福 11 亞歷山大 | 2021 | **64 位元 macOS**、Android 64 位元 |
|德爾福 12 雅典 | 2023 | **現代 IDE**，改進的編譯器 |
|德爾福12.2 | 2024 | 2024進一步改進|
## 主要里程碑
### 帕斯卡 (1970–1982)
- **1970**：Niklaus Wirth 在蘇黎世聯邦理工學院創建 Pascal
- **目標**：教導結構化程式設計－乾淨、型別安全
- 主要功能：`record`、`procedure`、`function`、`begin` / `end`、強型
- UCSD Pascal (1978) — 手提 p 代碼機
### 渦輪帕斯卡 (1983–1992)
- **1983**：Anders Hejlsberg 為 Borland 創建 Turbo Pascal
- **革命性**：快速編譯器、整合 IDE、便宜（49.95 美元）
- **5.5 (1989)**：物件 — Pascal 中的 OOP（`object`，繼承）
- **7 (1992)**：最後一個 DOS 版本 — 傳奇般的速度和可靠性
### Delphi 1–7：黃金時代（1995–2002）
- **1995**：Delphi 1 — 視覺化編程，VCL（視覺化元件庫）
- **2 (1996)**：32 位元 Windows
- **7 (2002)**：最受歡迎的版本 — 快速、穩定、廣泛使用
- 快速應用程式開發 (RAD) — 拖放 GUI
### Delphi 2005–XE：現代功能（2005–2010）
- **2006**：泛型、匿名方法
- **2009**：完整的 Unicode（UTF-16 字串）
- **2010**：增強型 RTTI（反射）
### Delphi XE2+：跨平台（2011 年至今）
- **XE2 (2011)**：FireMonkey — 跨平台框架（Windows、macOS）
- **XE3 (2012)**：iOS 支持
- **XE4 (2013)**：Android 支持
- **11 (2021)**：64 位元 macOS、Android 64 位元
- **12 (2023)**：現代 IDE，改良的編譯器
## 語法演變
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

## 功能演變
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

## 關鍵設計原則
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## 生態系成長
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
