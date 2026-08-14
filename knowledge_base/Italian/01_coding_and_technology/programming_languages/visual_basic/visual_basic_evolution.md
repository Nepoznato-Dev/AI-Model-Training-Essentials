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
# Visual Basic: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| BASE | 1964 | **BASE originale** (Kemeny & Kurtz, Dartmouth) |
| GW-BASE | 1983 | BASIC di Microsoft per PC IBM |
| BASIC veloce | 1985 | BASIC strutturato, IDE, compilatore |
| VB1.0 | 1991 | **Visual Basic 1.0** — programmazione visiva per Windows |
| VB2.0 | 1992 | Moduli più veloci e basati su oggetti |
| VB3.0 | 1993 | **Supporto database** (controllo dati), motore Jet |
| VB4.0 | 1995 | 32 bit, classi (nessuna ereditarietà) |
| VB5.0 | 1997 | **Componenti COM**, controlli disegnati dall'utente |
| VB6.0 | 1998 | **Maggiore**: COM, ADO, DCOM, WebClass: il classico VB |
| VB.NET | 2002| **Principale**: .NET Framework: OOP, ereditarietà, GC |
| VB.NET 2003 | 2003| .NET 1.1, IDE migliorato |
| VB2005 | 2005| **Il mio spazio dei nomi**,`Using`,`Continue`, modifica e continua |
| VB2008 | 2008| **LINQ**, valori letterali XML, tipi anonimi, operatore`If`|
| VB2010 | 2010| Lambda multilinea, dinamici, co/contro-varianza |
| VB2012 | 2012| `Async`/`Await`, iteratori |
| VB2015 | 2015| Interpolazione di stringhe`$""`,`?.`condizionale nullo , nome |
| VB2017 | 2017 | Tuple, ritorni di riferimento, corrispondenza di modelli |
| VB15.3 | 2017 | Decostruzione non tupla |
| VB15.5 | 2017 | Rif locali, membri di sola lettura |
| VB16.0 | 2019 | **Tipi di riferimento nullable**, espressioni`Switch`|
| VB16.9 | 2021 | `OrElse`miglioramenti |
| VB17.0 | 2022 | **Valori letterali stringa grezza**, strutture predefinite automatiche, miglioramenti`Module`|
| VB17.7 | 2024 | Ulteriori perfezionamenti |
## Traguardi importanti
### Origini BASIC (1964–1990)
- **1964**: John Kemeny e Thomas Kurtz creano il BASIC al Dartmouth College
- **Obiettivo**: rendere la programmazione accessibile agli studenti non scientifici
- **1983**: GW-BASIC — BASIC di Microsoft per PC IBM
- **1985**: QuickBASIC: programmazione strutturata, IDE, compilatore
- Caratteristiche principali: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: L'era classica (1991–2001)
- **1.0 (1991)**: programmazione visiva: builder GUI drag-and-drop per Windows
- **2.0 (1992)**: moduli più veloci e basati su oggetti
- **3.0 (1993)**: supporto database: controllo dati, motore Jet
- **4.0 (1995)**: 32 bit (Windows 95), classi
- **5.0 (1997)**: componenti COM, controlli disegnati dall'utente
- **6.0 (1998)**: **Il classico VB**: COM, ADO, DCOM, WebClass
  - Versione più utilizzata
  - Sviluppo rapido di applicazioni (RAD)
  - Esegue ancora milioni di applicazioni legacy
### VB.NET: la rivoluzione .NET (2002-oggi)
- **2002**: VB.NET: riscrittura completa su .NET Framework
  - True OOP: ereditarietà, interfacce, polimorfismo
  - Raccolta dei rifiuti
  - Accesso all'intera libreria di classi .NET
- **2005**: spazio dei nomi`My`(facile accesso alle operazioni comuni)
- **2008**: **LINQ**: sintassi delle query integrata nel linguaggio
- **2012**:`Async`/`Await`— programmazione asincrona
- **2015**: interpolazione di stringhe `$""`,`?.`nullo condizionale 
- **2017**: tuple, corrispondenza di modelli
- **2019**: tipi di riferimento Nullable
- **2022**: stringhe letterali grezze, sintassi moderna
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
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

## Principi chiave di progettazione
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Crescita dell'ecosistema
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
