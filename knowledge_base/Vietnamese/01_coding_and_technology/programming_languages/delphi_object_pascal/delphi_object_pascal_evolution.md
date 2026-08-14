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
# Delphi / Object Pascal — Lịch sử và tiến hóa phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Pascal | 1970 | **Niklaus Wirth** tạo Pascal (ETH Zurich) |
| Turbo Pascal 1 | 1983 | **Borland** — nhanh, rẻ, dựa trên IDE (Anders Hejlsberg) |
| Turbo Pascal 3 | 1986 | Đơn vị, hỗ trợ lớp phủ |
| Turbo Pascal 5 | 1988 | **Trình gỡ lỗi tích hợp**, cải tiến IDE |
| Turbo Pascal 5.5 | 1989 | **Pascal hướng đối tượng** — đối tượng, kế thừa |
| Turbo Pascal 6 | 1989 | Cải tiến OOP, đơn vị |
| Turbo Pascal 7 | 1992 | Turbo Pascal dựa trên DOS cuối cùng |
| Delphi 1 | 1995 | **Lập trình trực quan** — VCL, các thành phần, GUI Windows |
| Delphi 2 | 1996 | Windows 32-bit |
| Delphi 3 | 1997 | Hỗ trợ COM/ActiveX |
| Delphi 4 | 1998 | Mảng động, nạp chồng hàm |
| Delphi 5 | 1999 | **ADO**, WebSnap |
| Delphi 6 | 2001 | **Dịch vụ web**, CLX (đa nền tảng) |
| Delphi 7 | 2002 | **Phiên bản phổ biến nhất** — ổn định, nhanh chóng |
| Delphi 8 | 2003 | Hỗ trợ .NET |
| Delphi 2005 | 2005 | Unicode (một phần), generics |
| Delphi 2006 | 2006 | **Generics**, phương pháp ẩn danh |
| Delphi 2007 | 2007 | Unicode (đầy đủ), hỗ trợ Vista |
| Delphi 2009 | 2008 | **Unicode đầy đủ** (UTF-16), cải tiến RTTI |
| Delphi 2010 | 2009 | RTTI, hồ sơ nâng cao |
| Delphi XE | 2010 | Chuẩn bị đa nền tảng |
| Delphi XE2 | 2011 | **FireMonkey** — đa nền tảng (Windows, macOS) |
| Delphi XE3 | 2012 | **Hỗ trợ iOS** |
| Delphi XE4 | 2013 | **Hỗ trợ Android** |
| Delphi XE7 | 2014 | Cải tiến đa thiết bị |
| Delphi 10 Seattle | 2015 | Hỗ trợ Windows 10 |
| Delphi 10.4 Sydney | 2020 | **DPI cao**, RTL được cải tiến |
| Delphi 11 Alexandria | 2021 | **MacOS 64-bit**, Android 64-bit |
| Delphi 12 Athens | 2023 | **IDE hiện đại**, trình biên dịch cải tiến |
| Delphi 12.2 | 2024 | Cải tiến hơn nữa |
## Các cột mốc quan trọng
### Pascal (1970–1982)
- **1970**: Niklaus Wirth tạo Pascal tại ETH Zurich
- **Mục tiêu**: Dạy lập trình có cấu trúc — rõ ràng, an toàn kiểu
- Tính năng chính:`record`,`procedure`,`function`,`begin`/`end`, gõ mạnh
- UCSD Pascal (1978) — máy mã p di động
### Turbo Pascal (1983–1992)
- **1983**: Anders Hejlsberg tạo Turbo Pascal cho Borland
- **Cách mạng**: Trình biên dịch nhanh, IDE tích hợp, giá rẻ ($49,95)
- **5.5 (1989)**: Đối tượng — OOP trong Pascal (`object`, kế thừa)
- **7 (1992)**: Phiên bản DOS cuối cùng — tốc độ và độ tin cậy huyền thoại
### Delphi 1–7: Thời đại hoàng kim (1995–2002)
- **1995**: Delphi 1 — lập trình trực quan, VCL (Thư viện thành phần trực quan)
- **2 (1996)**: Windows 32-bit
- **7 (2002)**: Phiên bản phổ biến nhất — nhanh, ổn định, được sử dụng rộng rãi
- Phát triển ứng dụng nhanh (RAD) — GUI kéo và thả
### Delphi 2005–XE: Tính năng hiện đại (2005–2010)
- **2006**: Generics, phương pháp ẩn danh
- **2009**: Unicode đầy đủ (chuỗi UTF-16)
- **2010**: RTTI nâng cao (phản ánh)
### Delphi XE2+: Đa nền tảng (2011–nay)
- **XE2 (2011)**: FireMonkey — khung đa nền tảng (Windows, macOS)
- **XE3 (2012)**: Hỗ trợ iOS
- **XE4 (2013)**: Hỗ trợ Android
- **11 (2021)**: macOS 64-bit, Android 64-bit
- **12 (2023)**: IDE hiện đại, trình biên dịch cải tiến
## Tiến hóa cú pháp
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

## Tiến hóa tính năng
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

## Nguyên tắc thiết kế chính
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Tăng trưởng hệ sinh thái
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
