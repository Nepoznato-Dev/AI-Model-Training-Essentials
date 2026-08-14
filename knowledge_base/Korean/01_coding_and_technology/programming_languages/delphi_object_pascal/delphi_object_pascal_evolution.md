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
# 델파이/오브젝트 파스칼 — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 파스칼 | 1970 | **Niklaus Wirth**가 파스칼(ETH Zurich)을 창설함 |
| 터보 파스칼 1 | 1983년 | **Borland** — 빠르고 저렴하며 IDE 기반(Anders Hejlsberg) |
| 터보 파스칼 3 | 1986 | 단위, 오버레이 지원 |
| 터보 파스칼 5 | 1988 | **통합 디버거**, IDE 개선 |
| 터보 파스칼 5.5 | 1989 | **객체 지향 파스칼** — 객체, 상속 |
| 터보 파스칼 6 | 1989 | OOP 개선, 단위 |
| 터보 파스칼 7 | 1992 | 마지막 DOS 기반 터보 파스칼 |
| 델파이 1 | 1995 | **시각적 프로그래밍** — VCL, 구성 요소, Windows GUI |
| 델파이 2 | 1996 | 32비트 Windows |
| 델파이 3 | 1997 | COM/ActiveX 지원 |
| 델파이 4 | 1998 | 동적 배열, 함수 오버로딩 |
| 델파이 5 | 1999 | **ADO**, WebSnap |
| 델파이 6 | 2001 | **웹 서비스**, CLX(크로스 플랫폼) |
| 델파이 7 | 2002 | **가장 인기 있는 버전** — 안정적이고 빠릅니다 |
| 델파이 8 | 2003년 | .NET 지원 |
| 델파이 2005 | 2005년 | 유니코드(부분), 제네릭 |
| 델파이 2006 | 2006년 | **제네릭**, 익명 메서드 |
| 델파이 2007 | 2007년 | 유니코드(전체), Vista 지원 |
| 델파이 2009 | 2008 | **전체 유니코드**(UTF-16), RTTI 개선 |
| 델파이 2010 | 2009 | RTTI, 향상된 기록 |
| 델파이 XE | 2010 | 크로스 플랫폼 준비 |
| 델파이 XE2 | 2011 | **FireMonkey** — 크로스 플랫폼(Windows, macOS) |
| 델파이 XE3 | 2012 | **iOS 지원** |
| 델파이 XE4 | 2013 | **안드로이드 지원** |
| 델파이 XE7 | 2014 | 다중 장치 개선 |
| 델파이 10 시애틀 | 2015 | Windows 10 지원 |
| 델파이 10.4 시드니 | 2020 | **높은 DPI**, 향상된 RTL |
| 델파이 11 알렉산드리아 | 2021 | **64비트 macOS**, Android 64비트 |
| 델파이 12 아테네 | 2023년 | **최신 IDE**, 향상된 컴파일러 |
| 델파이 12.2 | 2024 | 추가 개선 |
## 주요 이정표
### 파스칼(1970~1982)
- **1970**: Niklaus Wirth가 ETH Zurich에서 Pascal을 창설함
- **목표**: 구조화된 프로그래밍 교육 - 깔끔하고 형식이 안전함
- 주요 기능:`record`,`procedure`,`function`,`begin`/`end`, 강력한 타이핑
- UCSD Pascal (1978) — 휴대용 p-코드 머신
### 터보 파스칼(1983~1992)
- **1983**: Anders Hejlsberg가 Borland를 위해 Turbo Pascal을 만듭니다.
- **혁신적**: 빠른 컴파일러, 통합 IDE, 저렴함($49.95)
- **5.5 (1989)**: 객체 — 파스칼의 OOP(`object`, 상속)
- **7(1992)**: 마지막 DOS 버전 — 전설적인 속도와 안정성
### 델파이 1~7장: 황금시대(1995~2002)
- **1995**: Delphi 1 — 시각적 프로그래밍, VCL(Visual Component Library)
- **2(1996)**: 32비트 Windows
- **7(2002)**: 가장 인기 있는 버전 — 빠르고 안정적이며 널리 사용됨
- 신속한 애플리케이션 개발(RAD) — 드래그 앤 드롭 GUI
### Delphi 2005–XE: 최신 기능(2005–2010)
- **2006**: 제네릭, 익명 메서드
- **2009**: 전체 유니코드(UTF-16 문자열)
- **2010**: 향상된 RTTI(반사)
### Delphi XE2+: 크로스 플랫폼(2011~현재)
- **XE2(2011)**: FireMonkey — 크로스 플랫폼 프레임워크(Windows, macOS)
- **XE3(2012)**: iOS 지원
- **XE4(2013)**: 안드로이드 지원
- **11(2021)**: 64비트 macOS, Android 64비트
- **12(2023)**: 최신 IDE, 향상된 컴파일러
## 구문 진화
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

## 기능 진화
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

## 주요 디자인 원칙
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## 생태계 성장
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
