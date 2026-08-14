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

# Visual Basic — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| БАЗОВЫЙ | 1964 | **Оригинальный BASIC** (Кемени и Курц, Дартмут) |
| GW-БЕЙСИК | 1983 | BASIC от Microsoft для IBM PC |
| QuickBASIC | 1985 | Структурированный BASIC, IDE, компилятор |
| ВБ 1.0 | 1991 | **Visual Basic 1.0** — визуальное программирование для Windows |
| ВБ 2.0 | 1992 | Более быстрые объектно-ориентированные формы |
| ВБ 3.0 | 1993 | **Поддержка баз данных** (Управление данными), Реактивный двигатель |
| ВБ 4.0 | 1995 | 32-разрядная версия, классы (без наследования) |
| ВБ 5.0 | 1997 | **COM-компоненты**, элементы управления, нарисованные пользователем |
| ВБ 6.0 | 1998 | **Основные**: COM, ADO, DCOM, WebClass — классический VB |
| ВБ.НЕТ | 2002 | **Основные**: .NET Framework — ООП, наследование, сборщик мусора |
| ВБ.НЕТ 2003 | 2003 | .NET 1.1, улучшенная IDE |
| ВБ 2005 | 2005 | **Мое пространство имен**,`Using`,`Continue`, изменить и продолжить |
| ВБ 2008 | 2008 | **LINQ**, литералы XML, анонимные типы, оператор`If`|
| ВБ 2010 | 2010 | Многострочные лямбды, динамические, ко/контравариантность |
| ВБ 2012 | 2012 |  `Async`/`Await`, итераторы |
| ВБ 2015 | 2015 | Интерполяция строк`$""`, условное значение NULL`?.`, nameof |
| ВБ 2017 | 2017 | Кортежи, возврат ссылок, сопоставление с образцом |
| ВБ 15.3 | 2017 | Некортежная деконструкция |
| ВБ 15,5 | 2017 | Ссылка на местных жителей, участников только для чтения |
| ВБ 16.0 | 2019 | **Ссылочные типы, допускающие значение NULL**, выражения`Switch`|
| ВБ 16,9 | 2021 |  Улучшения`OrElse`|
| ВБ 17.0 | 2022 | **Необработанные строковые литералы**, структуры по умолчанию, улучшения`Module`|
| ВБ 17,7 | 2024 | Дальнейшие усовершенствования |
## Основные вехи
### БАЗОВОЕ ПРОИСХОЖДЕНИЕ (1964–1990)
- **1964**: Джон Кемени и Томас Курц создают BASIC в Дартмутском колледже.
- **Цель**: сделать программирование доступным для студентов, не изучающих естественные науки.
- **1983**: GW-BASIC — BASIC от Microsoft для IBM PC.
- **1985**: QuickBASIC — структурное программирование, IDE, компилятор.
- Ключевые особенности: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/ `NEXT`.
### Visual Basic 1–6: Классическая эра (1991–2001)
- **1.0 (1991)**: Визуальное программирование — конструктор графического интерфейса с возможностью перетаскивания для Windows.
- **2.0 (1992 г.)**: более быстрые объектно-ориентированные формы.
- **3.0 (1993 г.)**: Поддержка базы данных — управление данными, реактивный двигатель.
- **4.0 (1995 г.)**: 32-разрядная версия (Windows 95), классы
- **5.0 (1997 г.)**: COM-компоненты, элементы управления, нарисованные пользователем.
- **6.0 (1998)**: **Классический VB** — COM, ADO, DCOM, WebClass.
  - Самая распространенная версия
  - Быстрая разработка приложений (RAD)
  - По-прежнему работают миллионы устаревших приложений.
### VB.NET: революция .NET (2002 – настоящее время)
- **2002**: VB.NET — полная переработка .NET Framework.
  - Истинное ООП — наследование, интерфейсы, полиморфизм.
  - Сбор мусора
  - Доступ ко всей библиотеке классов .NET.
- **2005**: пространство имен`My`(легкий доступ к общим операциям)
- **2008**: **LINQ** — синтаксис запросов интегрирован в язык.
- **2012**:`Async`/`Await`— асинхронное программирование.
- **2015**: строковая интерполяция `$""`, нулевое условие`?.`
- **2017**: кортежи, сопоставление с образцом.
- **2019**: ссылочные типы, допускающие значение NULL.
- **2022**: необработанные строковые литералы, современный синтаксис.
## Эволюция синтаксиса
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

## Эволюция функций
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

## Ключевые принципы проектирования
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Рост экосистемы
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
