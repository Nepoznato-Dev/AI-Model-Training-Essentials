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
# Delphi / Object Pascal - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| ปาสคาล | 1970 | **Niklaus Wirth** สร้าง Pascal (ETH Zurich) |
| เทอร์โบ ปาสคาล 1 | 1983 | **Borland** — รวดเร็ว ราคาถูก อิง IDE (Anders Hejlsberg) |
| เทอร์โบ ปาสคาล 3 | 1986 | หน่วยสนับสนุนการซ้อนทับ |
| เทอร์โบ ปาสคาล 5 | 1988 | **ดีบักเกอร์แบบรวม** การปรับปรุง IDE |
| เทอร์โบ ปาสคาล 5.5 | 1989 | **ปาสคาลเชิงวัตถุ** — อ็อบเจ็กต์, การสืบทอด |
| เทอร์โบ ปาสคาล 6 | 1989 | การปรับปรุง OOP หน่วย |
| เทอร์โบ ปาสคาล 7 | 1992 | Turbo Pascal บน DOS ล่าสุด |
| เดลฟี 1 | 1995 | **การเขียนโปรแกรมด้วยภาพ** — VCL, ส่วนประกอบ, Windows GUI |
| เดลฟี 2 | 1996 | Windows 32 บิต |
| เดลฟี 3 | 1997 | รองรับ COM/ActiveX |
| เดลฟี 4 | 1998 | อาร์เรย์แบบไดนามิก ฟังก์ชันโอเวอร์โหลด |
| เดลฟี 5 | 1999 | **ADO**, WebSnap |
| เดลฟี 6 | 2544 | **บริการบนเว็บ**, CLX (ข้ามแพลตฟอร์ม) |
| เดลฟี 7 | 2545 | **เวอร์ชันยอดนิยม** — เสถียร รวดเร็ว |
| เดลฟี 8 | 2546 | รองรับ .NET |
| เดลฟี 2005 | 2548 | Unicode (บางส่วน) ข้อมูลทั่วไป |
| เดลฟี 2006 | 2549 | **ทั่วไป** วิธีการที่ไม่ระบุชื่อ |
| เดลฟี 2007 | 2550 | Unicode (เต็ม) รองรับ Vista |
| เดลฟี 2009 | 2551 | **Unicode แบบเต็ม** (UTF-16), การปรับปรุง RTTI |
| เดลฟี 2010 | 2552 | RTTI บันทึกที่ได้รับการปรับปรุง |
| เดลฟี XE | 2010 | การเตรียมข้ามแพลตฟอร์ม |
| เดลฟี XE2 | 2554 | **FireMonkey** — ข้ามแพลตฟอร์ม (Windows, macOS) |
| เดลฟี XE3 | 2555 | **รองรับ iOS** |
| เดลฟี XE4 | 2013 | **รองรับระบบปฏิบัติการ Android** |
| เดลฟี XE7 | 2014 | การปรับปรุงหลายอุปกรณ์ |
| เดลฟี 10 ซีแอตเทิล | 2558 | รองรับ Windows 10 |
| Delphi 10.4 ซิดนีย์ | 2020 | **DPI สูง** ปรับปรุง RTL |
| เดลฟี 11 อเล็กซานเดรีย | 2021 | **MacOS 64 บิต**, Android 64 บิต |
| เดลฟี 12 เอเธนส์ | 2023 | **Modern IDE** คอมไพเลอร์ที่ได้รับการปรับปรุง |
| เดลฟี 12.2 | 2024 | การปรับปรุงเพิ่มเติม |
## เหตุการณ์สำคัญที่สำคัญ
### ปาสกาล (1970–1982)
- **1970**: Niklaus Wirth สร้าง Pascal ที่ ETH Zurich
- **เป้าหมาย**: การสอนการเขียนโปรแกรมแบบมีโครงสร้าง — สะอาด ปลอดภัยกับการพิมพ์
- คุณสมบัติที่สำคัญ:`record`,`procedure`,`function`,`begin`/`end`, การพิมพ์ที่แข็งแกร่ง
- UCSD Pascal (1978) — เครื่อง p-code แบบพกพา
### เทอร์โบ ปาสคาล (1983–1992)
- **1983**: Anders Hejlsberg สร้าง Turbo Pascal ให้กับ Borland
- **การปฏิวัติ**: คอมไพเลอร์ที่รวดเร็ว บูรณาการ IDE ราคาถูก ($49.95)
- **5.5 (1989)**: วัตถุ - OOP ในภาษาปาสคาล (`object`, การสืบทอด)
- **7 (1992)**: เวอร์ชัน DOS ล่าสุด — ความเร็วและความน่าเชื่อถือระดับตำนาน
### เดลฟี 1–7: ยุคทอง (1995–2002)
- **1995**: Delphi 1 — การเขียนโปรแกรมภาพ, VCL (ไลบรารีส่วนประกอบภาพ)
- **2 (1996)**: Windows 32 บิต
- **7 (2002)**: เวอร์ชันยอดนิยม — รวดเร็ว เสถียร มีการใช้กันอย่างแพร่หลาย
- Rapid Application Development (RAD) - GUI แบบลากและวาง
### Delphi 2005–XE: คุณสมบัติสมัยใหม่ (2005–2010)
- **2006**: วิธีทั่วไป วิธีการที่ไม่ระบุชื่อ
- **2009**: Unicode แบบเต็ม (สตริง UTF-16)
- **2010**: RTTI ที่ปรับปรุงแล้ว (การสะท้อนกลับ)
### Delphi XE2+: ข้ามแพลตฟอร์ม (2011–ปัจจุบัน)
- **XE2 (2011)**: FireMonkey — เฟรมเวิร์กข้ามแพลตฟอร์ม (Windows, macOS)
- **XE3 (2012)**: รองรับ iOS
- **XE4 (2013)**: รองรับระบบปฏิบัติการ Android
- **11 (2021)**: macOS 64 บิต, Android 64 บิต
- **12 (2023)**: IDE สมัยใหม่ คอมไพเลอร์ที่ได้รับการปรับปรุง
## วิวัฒนาการไวยากรณ์
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

## วิวัฒนาการคุณสมบัติ
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

## หลักการออกแบบที่สำคัญ
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## การเติบโตของระบบนิเวศ
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
