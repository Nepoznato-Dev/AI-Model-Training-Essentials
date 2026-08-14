---
# Metadata
title: "Visual Basic — Version History & Evolution"
description: "Comprehensive version history and evolution of Visual Basic from VB 1.0 to modern VB.NET."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Visual Basic — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|基本 | 1964 | **原始 BASIC**（Kemeny & Kurtz，达特茅斯）|
| GW-基本 | 1983 |微软为 IBM PC 设计的 BASIC |
|快速基本 | 1985 |结构化 BASIC、IDE、编译器 |
| VB 1.0 | 1991 | **Visual Basic 1.0** — Windows 可视化编程 |
| VB 2.0 | 1992 |更快、基于对象的表单 |
| VB 3.0 | 1993 | **数据库支持**（数据控制）、Jet 引擎 |
| VB 4.0 | 1995 | 32 位，类（无继承）|
| VB 5.0 | 1997 | **COM组件**，用户绘制控件|
| VB 6.0 | 1998 | **专业**：COM、ADO、DCOM、WebClass——经典VB |
| VB.NET | 2002 | **专业**：.NET Framework — OOP、继承、GC |
| VB.NET 2003 | 2003 | .NET 1.1，改进的IDE |
| VB 2005 | 2005 | **我的命名空间**，`Using`，`Continue`，编辑并继续 |
| VB 2008 | 2008 | **LINQ**、XML 文字、匿名类型、`If` 运算符 |
| VB 2010 | 2010 |多行 lambda、动态、协变/逆变 |
| VB 2012 | 2012 | `Async`/`Await`，迭代器 |
| VB 2015 | 2015 | 2015字符串插值`$""`，空条件`?.`，nameof |
| VB 2017 | 2017 | 2017元组、引用返回、模式匹配 |
| VB 15.3 | 2017 | 2017非元组解构|
| VB 15.5 | 2017 | 2017参考当地人，只读会员|
| VB 16.0 | 2019 | 2019 **可空引用类型**，`Switch` 表达式 |
| VB 16.9 | 2021 | `OrElse`改进 |
| VB 17.0 | 2022 | 2022 **原始字符串文字**、自动默认结构、`Module` 改进 |
| VB 17.7 | 2024 | 2024进一步完善|
## 主要里程碑
### 基本起源（1964–1990）
- **1964**：John Kemeny 和 Thomas Kurtz 在达特茅斯学院创建了 BASIC
- **目标**：让非理科学生也能接触到编程
- **1983**：GW-BASIC — Microsoft 用于 IBM PC 的 BASIC
- **1985**：QuickBASIC — 结构化编程、IDE、编译器
- 主要功能：`GOTO`、`GOSUB`、`LET`、`INPUT`、`PRINT`、`FOR` / `NEXT`
### Visual Basic 1–6：经典时代（1991–2001）
- **1.0 (1991)**：可视化编程 — 适用于 Windows 的拖放式 GUI 构建器
- **2.0 (1992)**：更快、基于对象的表单
- **3.0 (1993)**：数据库支持 — 数据控制、Jet 引擎
- **4.0 (1995)**：32 位 (Windows 95)，类
- **5.0 (1997)**：COM 组件、用户绘制控件
- **6.0 (1998)**：**经典 VB** — COM、ADO、DCOM、WebClass
  - 使用最广泛的版本
  - 快速应用程序开发（RAD）
  - 仍然运行数百万遗留应用程序
### VB.NET：.NET 革命（2002 年至今）
- **2002**：VB.NET — 在 .NET Framework 上完全重写
  - 真正的 OOP — 继承、接口、多态性
  - 垃圾收集
  - 访问整个.NET类库
- **2005**：`My` 命名空间（轻松访问常用操作）
- **2008**：**LINQ** — 查询语法集成到语言中
- **2012**：`Async` /`Await`— 异步编程
- **2015**：字符串插值`$""`，空条件`?.`
- **2017**：元组、模式匹配
- **2019**：可为空的引用类型
- **2022**：原始字符串文字，现代语法
## 语法演变
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

## 功能演变
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

## 关键设计原则
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## 生态系统增长
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
