<!--
---
# Metadata
title: "Visual Basic — Version History & Evolution"
description: "Comprehensive version history and evolution of Visual Basic from VB 1.0 to modern VB.NET."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [visual-basic, vb6, vbdotnet, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Visual Basic - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| พื้นฐาน | 2507 | **ต้นฉบับ BASIC** (Kemeny & Kurtz, Dartmouth) |
| GW-พื้นฐาน | 1983 | พื้นฐานของ Microsoft สำหรับ IBM PC |
| QuickBASIC | 1985 | โครงสร้าง BASIC, IDE, คอมไพเลอร์ |
| VB 1.0 | 1991 | **Visual Basic 1.0** — การเขียนโปรแกรมภาพสำหรับ Windows |
| VB 2.0 | 1992 | แบบฟอร์มตามวัตถุที่เร็วขึ้น |
| VB 3.0 | 1993 | **รองรับฐานข้อมูล** (การควบคุมข้อมูล), เครื่องยนต์ไอพ่น |
| VB 4.0 | 1995 | คลาส 32 บิต (ไม่มีการสืบทอด) |
| VB 5.0 | 1997 | **ส่วนประกอบ COM** การควบคุมที่ผู้ใช้วาด |
| VB 6.0 | 1998 | **หลัก**: COM, ADO, DCOM, WebClass — VB แบบคลาสสิก |
| VB.NET | 2545 | **หลัก**: .NET Framework — OOP, การสืบทอด, GC |
| VB.NET 2003 | 2546 | .NET 1.1, IDE ที่ปรับปรุงแล้ว |
| ว.บ.2548 | 2548 | **เนมสเปซของฉัน**,`Using`,`Continue`, แก้ไขและดำเนินการต่อ |
| วีบี 2008 | 2551 | **LINQ**, ตัวอักษร XML, ประเภทที่ไม่ระบุชื่อ, ตัวดำเนินการ`If`|
| วีบี 2010 | 2010 | แลมบ์ดาหลายบรรทัด ไดนามิก co/contra-variance |
| วีบี 2012 | 2555 | `Async`/`Await`ตัววนซ้ำ |
| วีบี 2015 | 2558 | การแก้ไขสตริง`$""`,`?.`แบบมีเงื่อนไข null , nameof |
| วีบี 2017 | 2017 | สิ่งอันดับ, การส่งคืนการอ้างอิง, การจับคู่รูปแบบ |
| VB 15.3 | 2017 | การถอดรหัสที่ไม่ใช่สิ่งอันดับ |
| VB 15.5 | 2017 | อ้างอิงคนในพื้นที่ สมาชิกแบบอ่านอย่างเดียว |
| VB 16.0 | 2019 | **ประเภทการอ้างอิงที่เป็น Nullable**, นิพจน์`Switch`|
| VB 16.9 | 2021 |  การปรับปรุง`OrElse`|
| VB 17.0 | 2022 | **ตัวอักษรสตริงดิบ**, โครงสร้างเริ่มต้นอัตโนมัติ, การปรับปรุง`Module`|
| VB 17.7 | 2024 | การปรับแต่งเพิ่มเติม |
## เหตุการณ์สำคัญที่สำคัญ
### ต้นกำเนิดพื้นฐาน (พ.ศ. 2507–2533)
- **1964**: John Kemeny และ Thomas Kurtz สร้าง BASIC ที่ Dartmouth College
- **เป้าหมาย**: ทำให้นักเรียนที่ไม่มีความรู้ด้านวิทยาศาสตร์สามารถเข้าถึงการเขียนโปรแกรมได้
- **1983**: GW-BASIC — BASIC ของ Microsoft สำหรับพีซี IBM
- **1985**: QuickBASIC — การเขียนโปรแกรมแบบมีโครงสร้าง, IDE, คอมไพเลอร์
- คุณสมบัติที่สำคัญ:`GOTO`,`GOSUB`,`LET`,`INPUT`,`PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: ยุคคลาสสิก (พ.ศ. 2534–2544)
- **1.0 (1991)**: การเขียนโปรแกรมด้วยภาพ — ตัวสร้าง GUI แบบลากและวางสำหรับ Windows
- **2.0 (1992)**: รูปแบบที่เร็วขึ้นตามวัตถุ
- **3.0 (1993)**: รองรับฐานข้อมูล — การควบคุมข้อมูล เครื่องยนต์ไอพ่น
- **4.0 (1995)**: 32 บิต (Windows 95) คลาส
- **5.0 (1997)**: ส่วนประกอบ COM, การควบคุมที่ผู้ใช้วาดเอง
- **6.0 (1998)**: **VB แบบคลาสสิก** — COM, ADO, DCOM, WebClass
  - รุ่นที่ใช้กันอย่างแพร่หลาย
  - การพัฒนาแอปพลิเคชั่นอย่างรวดเร็ว (RAD)
  - ยังคงรันแอปพลิเคชั่นรุ่นเก่านับล้าน
### VB.NET: การปฏิวัติ .NET (2545–ปัจจุบัน)
- **2002**: VB.NET — เขียนใหม่ทั้งหมดบน .NET Framework
  - True OOP — การสืบทอด, อินเทอร์เฟซ, ความหลากหลาย
  - เก็บขยะ
  - เข้าถึงไลบรารีคลาส .NET ทั้งหมด
- **2005**: เนมสเปซ`My`(เข้าถึงการดำเนินการทั่วไปได้ง่าย)
- **2008**: **LINQ** — ไวยากรณ์คิวรีที่ผสานรวมเข้ากับภาษา
- **2012**:`Async`/`Await`— การเขียนโปรแกรมแบบอะซิงโครนัส
- **2015**: การแก้ไขสตริง`$""`,`?.`แบบมีเงื่อนไข null 
- **2017**: สิ่งอันดับ การจับคู่รูปแบบ
- **2019**: ประเภทการอ้างอิงที่เป็นโมฆะ
- **2022**: ตัวอักษรสตริงดิบ ไวยากรณ์สมัยใหม่
## วิวัฒนาการไวยากรณ์
```vb
' GW-BASIC (1983): Line numbers, GOTO
10 INPUT "Name: "; N$
20 PRINT "Hello, "; N$
30 GOTO 10

' QuickBASIC (1985): Structured programming
INPUT "Name: "; N$
PRINT "Hello, "; N$
FOR I = 1 TO 10
    PRINT I
NEXT I

' Visual Basic 6.0 (1998): Event-driven, GUI
Private Sub Command1_Click()
    Dim name As String
    name = Text1.Text
    MsgBox "Hello, " & name & "!"
End Sub

' VB.NET 2002: OOP, .NET
Class Person
    Public Name As String
    Public Age As Integer

    Sub New(ByVal n As String, ByVal a As Integer)
        Name = n
        Age = a
    End Sub
End Class

' VB 2008: LINQ
Dim query = From p In people
            Where p.Age > 18
            Select p.Name

' VB 2015: String interpolation, null-conditional
Dim message = $"Hello, {person?.Name ?? "Unknown"}!"

' VB 2017: Tuples, pattern matching
Dim result = (Name:="Alice", Age:=30)
Select Case result
    Case ("Alice", 30)
        Console.WriteLine("Found Alice!")
End Select

' VB 17.0 (2022): Raw string literals
Dim json = """
    {
        "name": "Alice",
        "age": 30
    }
    """

' Modern VB.NET: Async/Await
Async Function GetDataAsync() As Task(Of String)
    Dim client As New HttpClient()
    Dim result = Await client.GetStringAsync("https://api.example.com/data")
    Return result
End Function
```

## วิวัฒนาการคุณสมบัติ
```
BASIC (1964):    INPUT, PRINT, LET, FOR/NEXT, GOTO, GOSUB
QuickBASIC (1985): Structured programming, SUB/FUNCTION, TYPE
VB 1.0 (1991):   Visual programming, event-driven, GUI builder
VB 3.0 (1993):   Database (Data Control, Jet)
VB 4.0 (1995):   32-bit, classes
VB 6.0 (1998):   COM, ADO, DCOM, WebClass
VB.NET (2002):   OOP, GC, .NET Framework
VB 2005:         My namespace, Using, edit-and-continue
VB 2008:         LINQ, XML literals, anonymous types
VB 2012:         Async/Await, iterators
VB 2015:         String interpolation, null-conditional
VB 2017:         Tuples, pattern matching
VB 16.0 (2019):  Nullable reference types
VB 17.0 (2022):  Raw string literals, auto-default structs
```

## หลักการออกแบบที่สำคัญ
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## การเติบโตของระบบนิเวศ
```
1964: BASIC created at Dartmouth College
1983: GW-BASIC — Microsoft BASIC for PC
1985: QuickBASIC — structured programming
1991: Visual Basic 1.0 — visual programming
1998: VB 6.0 — classic VB, COM, ADO
2002: VB.NET — .NET Framework, OOP
2008: VB 2008 — LINQ
2012: VB 2012 — async/await
2022: VB 17.0 — raw string literals, modern syntax
2025: Visual Basic (.NET) used in:
       - Windows desktop applications (WinForms, WPF)
       - Legacy VB6 applications (still running in businesses)
       - Office automation (VBA — Visual Basic for Applications)
       - ASP.NET web applications
       Microsoft continues VB.NET alongside C# on .NET
       VBA still embedded in Excel, Word, Access, Outlook
```
