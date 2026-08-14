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
# Visual Basic — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|基本 | 1964 | **原始 BASIC**（Kemeny & Kurtz，達特茅斯）|
| GW-基本 | 1983 |微軟為 IBM PC 設計的 BASIC |
|快速基本 | 1985 |結構化 BASIC、IDE、編譯器 |
| VB 1.0 | 1991 | **Visual Basic 1.0** — Windows 視覺化程式設計 |
| VB 2.0 | 1992 |更快、基於物件的表單 |
| VB 3.0 | 1993 | **資料庫支援**（資料控制）、Jet 引擎 |
| VB 4.0 | 1995 | 32 位，類別（無繼承）|
| VB 5.0 | 1997 | **COM組件**，使用者繪製控制項|
| VB 6.0 | 1998 | **專業**：COM、ADO、DCOM、WebClass－經典VB |
| VB.NET | 2002 | **專業**：.NET Framework — OOP、繼承、GC |
| VB.NET 2003 | 2003 | .NET 1.1，改良的IDE |
| VB 2005 | 2005 | **我的命名空間**，`Using`，`Continue`，編輯並繼續 |
| VB 2008 | 2008 | **LINQ**、XML 文字、匿名型別、`If` 運算子 |
| VB 2010 | 2010 |多行 lambda、動態、協變/逆變 |
| VB 2012 | 2012 |`Async`/`Await`，迭代器 |
| VB 2015 | 2015 | 2015字串內插`$""`，空條件`?.`，nameof |
| VB 2017 | 2017 | 2017元組、引用回傳、模式比對 |
| VB 15.3 | 2017 | 2017非元組解構|
| VB 15.5 | 2017 | 2017參考當地人，只讀會員|
| VB 16.0 | 2019 | 2019 **可空引用型別**，`Switch` 表達式 |
| VB 16.9 | 2021 |`OrElse`改進 |
| VB 17.0 | 2022 | 2022 **原始字串文字**、自動預設結構、`Module` 改進 |
| VB 17.7 | 2024 | 2024進一步完善|
## 主要里程碑
### 基本起源（1964–1990）
- **1964**：John Kemeny 和 Thomas Kurtz 在達特茅斯學院創立了 BASIC
- **目標**：讓非理科學生也能接觸到程式設計
- **1983**：GW-BASIC — Microsoft 用於 IBM PC 的 BASIC
- **1985**：QuickBASIC — 結構化程式設計、IDE、編譯器
- 主要功能：`GOTO`、`GOSUB`、`LET`、`INPUT`、`PRINT`、`FOR`/ `NEXT`
### Visual Basic 1–6：經典時代（1991–2001）
- **1.0 (1991)**：視覺化程式設計 — 適用於 Windows 的拖曳式 GUI 建構器
- **2.0 (1992)**：更快、基於物件的表單
- **3.0 (1993)**：資料庫支援 — 資料控制、Jet 引擎
- **4.0 (1995)**：32 位元 (Windows 95)，類
- **5.0 (1997)**：COM 組件、使用者繪製控件
- **6.0 (1998)**：**經典 VB** — COM、ADO、DCOM、WebClass
  - 使用最廣泛的版本
  - 快速應用程式開發（RAD）
  - 仍然運行數百萬遺留應用程式
### VB.NET：.NET 革命（2002 年至今）
- **2002**：VB.NET — 在 .NET Framework 上完全重寫
  - 真正的 OOP — 繼承、介面、多態性
  - 垃圾收集
  - 存取整個.NET類別庫
- **2005**：`My` 命名空間（輕鬆存取常用操作）
- **2008**：**LINQ** — 查詢語法整合到語言中
- **2012**：`Async` /`Await`— 非同步編程
- **2015**：字串內插`$""`，空條件 `?.`
- **2017**：元組、模式匹配
- **2019**：可為空的引用型
- **2022**：原始字串文字，現代語法
## 語法演變
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

## 功能演變
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

## 關鍵設計原則
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## 生態系成長
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
