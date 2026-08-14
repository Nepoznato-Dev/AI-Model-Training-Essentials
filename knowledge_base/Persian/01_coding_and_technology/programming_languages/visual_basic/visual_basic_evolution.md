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
# ویژوال بیسیک - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| پایه | 1964 | **Original BASIC** (Kemeny & Kurtz, Dartmouth) |
| GW-BASIC | 1983 | مایکروسافت BASIC برای IBM PC |
| QuickBASIC | 1985 | Structured BASIC، IDE، کامپایلر |
| VB 1.0 | 1991 | **Visual Basic 1.0** — برنامه نویسی بصری برای ویندوز |
| VB 2.0 | 1992 | فرم های سریعتر و مبتنی بر شی |
| VB 3.0 | 1993 | **پشتیبانی از پایگاه داده** (کنترل داده)، موتور جت |
| VB 4.0 | 1995 | 32 بیتی، کلاس ها (بدون ارث بردن) |
| VB 5.0 | 1997 | **کامپوننت های COM**، کنترل های ترسیم شده توسط کاربر |
| VB 6.0 | 1998 | **رشته**: COM، ADO، DCOM، WebClass — VB کلاسیک |
| VB.NET | 2002 | **رشته**: .NET Framework — OOP، inheritance، GC |
| VB.NET 2003 | 2003 | NET 1.1، IDE بهبود یافته |
| VB 2005 | 2005 | **My namespace**، `Using`، `Continue`، ویرایش و ادامه |
| VB 2008 | 2008 | **LINQ**، حرف XML، انواع ناشناس، اپراتور`If`|
| VB 2010 | 2010 | لامبداهای چند خطی، پویا، co/contra-variance |
| VB 2012 | 2012 | `Async`/`Await`, تکرار کننده |
| VB 2015 | 2015 | درون یابی رشته ای `$""`، شرطی تهی `?.`، نام |
| VB 2017 | 2017 | تاپل ها، بازگرداندن رف، تطبیق الگو |
| VB 15.3 | 2017 | ساختارشکنی غیر تاپل |
| VB 15.5 | 2017 | مراجع محلی، اعضای فقط خواندنی |
| VB 16.0 | 2019 | **انواع مرجع تهی‌شونده**، عبارات`Switch`|
| VB 16.9 | 2021 |  بهبودهای`OrElse`|
| VB 17.0 | 2022 | **حرفهای رشته ای خام**، ساختارهای پیش فرض خودکار، بهبودهای`Module`|
| VB 17.7 | 2024 | اصلاحات بیشتر |
## نقاط عطف اصلی
### ریشه های اساسی (1964-1990)
- **1964**: جان کمنی و توماس کورتز BASIC را در کالج دارتموث ایجاد کردند
- **هدف**: برنامه نویسی را برای دانشجویان غیرعلمی در دسترس قرار دهید
- **1983**: GW-BASIC - مایکروسافت بیسیک برای IBM PC
- **1985**: QuickBASIC - برنامه نویسی ساخت یافته، IDE، کامپایلر
- ویژگی های کلیدی:`GOTO`,`GOSUB`,`LET`,`INPUT`,`PRINT`,`FOR`/ `NEXT`
### Visual Basic 1-6: The Classic Era (1991-2001)
- **1.0 (1991)**: برنامه نویسی بصری - سازنده رابط کاربری گرافیکی با کشیدن و رها کردن برای ویندوز
- **2.0 (1992)**: فرم های سریعتر و مبتنی بر شی
- **3.0 (1993)**: پشتیبانی از پایگاه داده - کنترل داده، موتور جت
- **4.0 (1995)**: 32 بیتی (ویندوز 95)، کلاس ها
- **5.0 (1997)**: اجزای COM، کنترل های ترسیم شده توسط کاربر
- **6.0 (1998)**: **VB کلاسیک** — COM، ADO، DCOM، WebClass
  - پرکاربردترین نسخه
  - توسعه سریع برنامه (RAD)
  - هنوز میلیون ها برنامه قدیمی را اجرا می کند
### VB.NET: انقلاب دات نت (2002–اکنون)
- **2002**: VB.NET - بازنویسی کامل در .NET Framework
  - OOP واقعی - وراثت، رابط ها، چندشکلی
  - جمع آوری زباله
  - دسترسی به کل کتابخانه کلاس دات نت
- **2005**: فضای نام`My`(دسترسی آسان به عملیات رایج)
- **2008**: **LINQ** - نحو پرس و جو در زبان یکپارچه شده است
- **2012**:`Async`/`Await`- برنامه نویسی ناهمزمان
- **2015**: درونیابی رشته ای `$""`، شرطی تهی`?.`
- **2017**: تاپلی، تطبیق الگو
- **2019**: انواع مرجع باطل
- **2022**: حرف های رشته ای خام، نحو مدرن
## تکامل نحو
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

## تکامل ویژگی
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

## اصول کلیدی طراحی
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## رشد اکوسیستم
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
