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

# Visual Basic — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| BASE | 1964 | **Basique original** (Kemeny & Kurtz, Dartmouth) |
| GW-BASIQUE | 1983 | BASIC de Microsoft pour IBM PC |
| QuickBASIC | 1985 | BASIC structuré, IDE, compilateur |
| VB 1.0 | 1991 | **Visual Basic 1.0** — programmation visuelle pour Windows |
| VB 2.0 | 1992 | Formulaires plus rapides basés sur des objets |
| VB 3.0 | 1993 | **Support de base de données** (Contrôle des données), moteur Jet |
| VB 4.0 | 1995 | 32 bits, classes (pas d'héritage) |
| VB 5.0 | 1997 | **Composants COM**, contrôles dessinés par l'utilisateur |
| VB 6.0 | 1998 | **Majeur** : COM, ADO, DCOM, WebClass — le VB classique |
| VB.NET | 2002 | **Majeur** : .NET Framework — POO, héritage, GC |
| VB.NET 2003 | 2003 | .NET 1.1, IDE amélioré |
| VB 2005 | 2005 | **Mon espace de noms**,`Using`,`Continue`, modifier et continuer |
| VB 2008 | 2008 | **LINQ**, littéraux XML, types anonymes, opérateur`If`|
| VB 2010 | 2010 | Lambdas multilignes, dynamiques, co/contra-variance |
| VB 2012 | 2012 | `Async`/`Await`, itérateurs |
| VB 2015 | 2015 | Interpolation de chaîne`$""`, condition nulle`?.`, nom de |
| VB 2017 | 2017 | Tuples, retours de référence, correspondance de modèles |
| VB 15.3 | 2017 | Déconstruction sans tuple |
| VB 15.5 | 2017 | Réf sections locales, membres en lecture seule |
| VB 16.0 | 2019 | **Types de référence nullables**, expressions`Switch`|
| VB 16.9 | 2021 |  Améliorations`OrElse`|
| VB 17.0 | 2022 | ** Littéraux de chaîne brute **, structures par défaut automatiques, améliorations`Module`|
| VB 17.7 | 2024 | Autres améliorations |
## Étapes majeures
### Origines BASIC (1964-1990)
- **1964** : John Kemeny et Thomas Kurtz créent BASIC au Dartmouth College
- **Objectif** : Rendre la programmation accessible aux étudiants non scientifiques
- **1983** : GW-BASIC — le BASIC de Microsoft pour IBM PC
- **1985** : QuickBASIC — programmation structurée, IDE, compilateur
- Principales caractéristiques : `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/ `NEXT`
### Visual Basic 1-6 : L'ère classique (1991-2001)
- **1.0 (1991)** : Programmation visuelle — Générateur d'interface graphique par glisser-déposer pour Windows
- **2.0 (1992)** : formulaires plus rapides basés sur des objets
- **3.0 (1993)** : Prise en charge des bases de données — Contrôle des données, moteur Jet
- **4.0 (1995)** : 32 bits (Windows 95), classes
- **5.0 (1997)** : composants COM, contrôles dessinés par l'utilisateur
- **6.0 (1998)** : **Le VB classique** — COM, ADO, DCOM, WebClass
  - Version la plus utilisée
  - Développement rapide d'applications (RAD)
  - Exécute toujours des millions d'applications existantes
### VB.NET : la révolution .NET (depuis 2002)
- **2002** : VB.NET — réécriture complète sur .NET Framework
  - True POO — héritage, interfaces, polymorphisme
  - Collecte des déchets
  - Accès à toute la bibliothèque de classes .NET
- **2005** : espace de noms`My`(accès facile aux opérations courantes)
- **2008** : **LINQ** — syntaxe de requête intégrée au langage
- **2012** :`Async`/`Await`— programmation asynchrone
- **2015** : interpolation de chaîne `$""`, condition nulle`?.`
- **2017** : Tuples, correspondance de motifs
- **2019** : types de référence nullables
- **2022** : Littéraux de chaîne bruts, syntaxe moderne
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
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

## Principes de conception clés
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Croissance de l'écosystème
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
