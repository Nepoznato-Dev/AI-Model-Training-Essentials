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
# Visual Basic – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| BASIC | 1964 | **Original BASIC** (Kemeny & Kurtz, Dartmouth) |
| GW-BASIC | 1983 | Microsofts BASIC für IBM PC |
| QuickBASIC | 1985 | Strukturiertes BASIC, IDE, Compiler |
| VB 1.0 | 1991 | **Visual Basic 1.0** – visuelle Programmierung für Windows |
| VB 2.0 | 1992 | Schnellere, objektbasierte Formulare |
| VB 3.0 | 1993 | **Datenbankunterstützung** (Datenkontrolle), Jet-Engine |
| VB 4.0 | 1995 | 32-Bit, Klassen (keine Vererbung) |
| VB 5.0 | 1997 | **COM-Komponenten**, vom Benutzer erstellte Steuerelemente |
| VB 6.0 | 1998 | **Major**: COM, ADO, DCOM, WebClass – das klassische VB |
| VB.NET | 2002 | **Major**: .NET Framework – OOP, Vererbung, GC |
| VB.NET 2003 | 2003 | .NET 1.1, verbesserte IDE |
| VB 2005 | 2005 | **Mein Namespace**, `Using`, `Continue`, Bearbeiten und Fortfahren |
| VB 2008 | 2008 | **LINQ**, XML-Literale, anonyme Typen, `If`-Operator |
| VB 2010 | 2010 | Mehrzeilige Lambdas, dynamisch, Ko-/Kontra-Varianz |
| VB 2012 | 2012 | `Async`/`Await`, Iteratoren |
| VB 2015 | 2015 | String-Interpolation`$""`, nullbedingte`?.`, nameof |
| VB 2017 | 2017 | Tupel, Ref-Returns, Mustervergleich |
| VB 15.3 | 2017 | Nicht-Tupel-Dekonstruktion |
| VB 15.5 | 2017 | Ref-Lokale, schreibgeschützte Mitglieder |
| VB 16.0 | 2019 | **Nullable-Referenztypen**, `Switch`-Ausdrücke |
| VB 16.9 | 2021 | `OrElse`Verbesserungen |
| VB 17.0 | 2022 | **Unformatierte String-Literale**, automatische Standardstrukturen, `Module`-Verbesserungen |
| VB 17.7 | 2024 | Weitere Verfeinerungen |
## Wichtige Meilensteine
### BASIC Origins (1964–1990)
- **1964**: John Kemeny und Thomas Kurtz erstellen BASIC am Dartmouth College
- **Ziel**: Programmieren auch für Studierende außerhalb der Naturwissenschaften zugänglich machen
- **1983**: GW-BASIC – Microsofts BASIC für IBM PC
- **1985**: QuickBASIC – strukturierte Programmierung, IDE, Compiler
- Hauptmerkmale: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/
### Visual Basic 1–6: Die klassische Ära (1991–2001)
- **1.0 (1991)**: Visuelle Programmierung – Drag-and-Drop-GUI-Builder für Windows
- **2.0 (1992)**: Schnellere, objektbasierte Formulare
- **3.0 (1993)**: Datenbankunterstützung – Datenkontrolle, Jet-Engine
- **4.0 (1995)**: 32-Bit (Windows 95), Klassen
- **5.0 (1997)**: COM-Komponenten, vom Benutzer erstellte Steuerelemente
- **6.0 (1998)**: **Das klassische VB** – COM, ADO, DCOM, WebClass
  - Am weitesten verbreitete Version
  - Schnelle Anwendungsentwicklung (RAD)
  - Läuft immer noch Millionen von Legacy-Anwendungen
### VB.NET: Die .NET-Revolution (2002–heute)
- **2002**: VB.NET – vollständige Neufassung des .NET Frameworks
  - Echtes OOP – Vererbung, Schnittstellen, Polymorphismus
  - Müllabfuhr
  - Zugriff auf die gesamte .NET-Klassenbibliothek
- **2005**: `My`-Namespace (einfacher Zugriff auf allgemeine Vorgänge)
- **2008**: **LINQ** – in die Sprache integrierte Abfragesyntax
- **2012**:`Async`/`Await`– asynchrone Programmierung
- **2015**: String-Interpolation `$""`, nullbedingte`?.`
- **2017**: Tupel, Mustervergleich
- **2019**: Nullable-Referenztypen
- **2022**: Rohe String-Literale, moderne Syntax
## Syntaxentwicklung
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

## Feature-Entwicklung
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

## Wichtige Designprinzipien
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Ökosystemwachstum
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
