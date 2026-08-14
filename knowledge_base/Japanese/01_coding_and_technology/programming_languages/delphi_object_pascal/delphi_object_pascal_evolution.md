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
# Delphi / Object Pascal — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|パスカル | 1970年 | **Niklaus Wirth** が Pascal を作成 (チューリッヒ工科大学) |
|ターボ パスカル 1 | 1983年 | **Borland** — 高速、安価、IDE ベース (Anders Hejlsberg) |
|ターボ パスカル 3 | 1986年 |ユニット、オーバーレイのサポート |
|ターボ パスカル 5 | 1988年 | **統合デバッガー**、IDE の改善 |
|ターボ パスカル 5.5 | 1989年 | **オブジェクト指向 Pascal** — オブジェクト、継承 |
|ターボ パスカル 6 | 1989年 | OOP の改善、ユニット |
|ターボ パスカル 7 | 1992年 |最後の DOS ベースの Turbo Pascal |
|デルフィ 1 | 1995年 | **ビジュアル プログラミング** — VCL、コンポーネント、Windows GUI |
|デルフィ 2 | 1996年 | 32 ビット Windows |
|デルフィ 3 | 1997年 | COM/ActiveX のサポート |
|デルフィ 4 | 1998年 |動的配列、関数のオーバーロード |
|デルフィ5 | 1999年 | **ADO**、ウェブスナップ |
|デルフィ 6 | 2001年 | **Web サービス**、CLX (クロスプラットフォーム) |
|デルフィ 7 | 2002年 | **最も人気のあるバージョン** — 安定性、高速性 |
|デルフィ 8 | 2003年 | .NET サポート |
|デルフィ 2005 | 2005年 | Unicode (部分)、ジェネリックス |
|デルフィ 2006 | 2006年 | **ジェネリック**、匿名メソッド |
|デルフィ 2007 | 2007年 | Unicode (完全)、Vista サポート |
|デルフィ 2009 | 2008年 | **完全な Unicode** (UTF-16)、RTTI の改善 |
|デルフィ 2010 | 2009年 | RTTI、拡張レコード |
|デルファイ XE | 2010年 |クロスプラットフォームの準備 |
|デルファイ XE2 | 2011年 | **FireMonkey** — クロスプラットフォーム (Windows、macOS) |
|デルファイ XE3 | 2012年 | **iOS サポート** |
|デルファイ XE4 | 2013年 | **Android のサポート** |
|デルファイ XE7 | 2014年 |マルチデバイスの改善 |
|デルフィ 10 シアトル | 2015年 | Windows 10 のサポート |
| Delphi 10.4 シドニー | 2020年 | **高 DPI**、改良された RTL |
|デルフィ 11 アレクサンドリア | 2021年 | **64 ビット macOS**、Android 64 ビット |
|デルフィ 12 アテネ | 2023年 | **最新の IDE**、改良されたコンパイラ |
|デルフィ 12.2 | 2024年 |さらなる改善 |
## 主要なマイルストーン
### パスカル (1970–1982)
- **1970**: ニクラウス・ヴィルトがチューリッヒ工科大学でパスカルを作成
- **目標**: 構造化プログラミングを教える — クリーンでタイプセーフ
- 主な機能:`record`、`procedure`、`function`、`begin`/`end`、強い型付け
- UCSD Pascal (1978) — ポータブルな P コード マシン
### ターボ パスカル (1983 ～ 1992)
- **1983**: Anders Hejlsberg が Borland のために Turbo Pascal を作成
- **革新的**: 高速コンパイラー、統合 IDE、安価 ($49.95)
- **5.5 (1989)**: オブジェクト — Pascal の OOP (`object`、継承)
- **7 (1992)**: 最後の DOS バージョン — 伝説的なスピードと信頼性
### デルフィ 1 ～ 7: 黄金時代 (1995 ～ 2002)
- **1995**: Delphi 1 — ビジュアル プログラミング、VCL (ビジュアル コンポーネント ライブラリ)
- **2 (1996)**: 32 ビット Windows
- **7 (2002)**: 最も人気のあるバージョン — 高速で安定しており、広く使用されています
- 高速アプリケーション開発 (RAD) — ドラッグ アンド ドロップ GUI
### Delphi 2005–XE: 最新の機能 (2005–2010)
- **2006**: ジェネリック、匿名メソッド
- **2009**: 完全な Unicode (UTF-16 文字列)
- **2010**: 強化された RTTI (リフレクション)
### Delphi XE2+: クロスプラットフォーム (2011–現在)
- **XE2 (2011)**: FireMonkey — クロスプラットフォーム フレームワーク (Windows、macOS)
- **XE3 (2012)**: iOS のサポート
- **XE4 (2013)**: Android のサポート
- **11 (2021)**: 64 ビット macOS、Android 64 ビット
- **12 (2023)**: 最新の IDE、改善されたコンパイラ
## 構文の進化
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

## 機能の進化
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

## 主要な設計原則
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## エコシステムの成長
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
