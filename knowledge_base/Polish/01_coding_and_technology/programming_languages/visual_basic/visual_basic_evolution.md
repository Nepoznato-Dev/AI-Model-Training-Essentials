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
# Visual Basic — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| PODSTAWOWE | 1964 | **Oryginalny PODSTAWOWY** (Kemeny & Kurtz, Dartmouth) |
| GW-BASIC | 1983 | Microsoft BASIC dla IBM PC |
| SzybkiBASIC | 1985 | Strukturalny BASIC, IDE, kompilator |
| VB 1.0 | 1991 | **Visual Basic 1.0** — programowanie wizualne dla Windows |
| VB 2.0 | 1992 | Szybsze formularze obiektowe |
| VB 3.0 | 1993 | **Obsługa baz danych** (Kontrola danych), silnik Jet |
| VB 4.0 | 1995 | 32-bitowy, klasy (bez dziedziczenia) |
| VB 5.0 | 1997 | **Komponenty COM**, elementy sterujące narysowane przez użytkownika |
| VB 6.0 | 1998 | **Główne**: COM, ADO, DCOM, WebClass — klasyczny VB |
| VB.NET | 2002 | **Główny**: .NET Framework — OOP, dziedziczenie, GC |
| VB.NET 2003 | 2003 | .NET 1.1, ulepszone IDE |
| VB 2005 | 2005 | **Moja przestrzeń nazw**,`Using`,`Continue`, edytuj i kontynuuj |
| VB 2008 | 2008 | **LINQ**, literały XML, typy anonimowe, operator`If`|
| VB 2010 | 2010 | Wieloliniowe lambdy, dynamiczne, współ/kontrawariancja |
| VB 2012 | 2012 | `Async`/`Await`, iteratory |
| VB 2015 | 2015 | Interpolacja ciągów`$""`, warunek zerowy`?.`, nazwa |
| VB 2017 | 2017 | Krotki, zwroty ref, dopasowywanie wzorców |
| VB 15.3 | 2017 | Dekonstrukcja niekrotkowa |
| VB 15,5 | 2017 | Ref. lokalni, członkowie tylko do odczytu |
| VB 16.0 | 2019 | **Typy referencyjne dopuszczające wartość null**, wyrażenia`Switch`|
| VB 16,9 | 2021 |  Ulepszenia`OrElse`|
| VB 17.0 | 2022 | **Surowe literały łańcuchowe**, struktury automatycznie domyślne, ulepszenia`Module`|
| VB 17,7 | 2024 | Dalsze udoskonalenia |
## Główne kamienie milowe
### PODSTAWOWE Początki (1964–1990)
- **1964**: John Kemeny i Thomas Kurtz tworzą język BASIC w Dartmouth College
- **Cel**: Udostępnienie programowania studentom nie zajmującym się naukami ścisłymi
- **1983**: GW-BASIC — BASIC firmy Microsoft dla IBM PC
- **1985**: QuickBASIC — programowanie strukturalne, IDE, kompilator
- Kluczowe cechy: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: Era klasyczna (1991–2001)
- **1.0 (1991)**: Programowanie wizualne — kreator GUI typu „przeciągnij i upuść” dla systemu Windows
- **2.0 (1992)**: Szybsze formularze obiektowe
- **3.0 (1993)**: Obsługa baz danych — kontrola danych, silnik Jet
- **4.0 (1995)**: 32-bitowy (Windows 95), klasy
- **5.0 (1997)**: Komponenty COM, elementy sterujące rysowane przez użytkownika
- **6.0 (1998)**: **Klasyczny VB** — COM, ADO, DCOM, WebClass
  - Najczęściej używana wersja
  - Szybkie tworzenie aplikacji (RAD)
  - Nadal obsługuje miliony starszych aplikacji
### VB.NET: Rewolucja .NET (2002 – obecnie)
- **2002**: VB.NET — całkowite przepisanie na .NET Framework
  - True OOP — dziedziczenie, interfejsy, polimorfizm
  - Zbiórka śmieci
  - Dostęp do całej biblioteki klas .NET
- **2005**: przestrzeń nazw`My`(łatwy dostęp do typowych operacji)
- **2008**: **LINQ** — składnia zapytań zintegrowana z językiem
- **2012**:`Async`/`Await`— programowanie asynchroniczne
- **2015**: Interpolacja ciągów`$""`, warunek zerowy`?.`
- **2017**: Krotki, dopasowywanie wzorców
- **2019**: Typy referencyjne dopuszczające wartość null
- **2022**: Surowe literały łańcuchowe, nowoczesna składnia
## Ewolucja składni
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

## Ewolucja funkcji
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

## Kluczowe zasady projektowania
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Rozwój ekosystemu
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
