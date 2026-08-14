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
# Visual Basic: historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| BÁSICO | 1964 | **BÁSICO original** (Kemeny & Kurtz, Dartmouth) |
| GW-BÁSICO | 1983 | BASIC de Microsoft para PC IBM |
| BÁSICO Rápido | 1985 | BASIC estructurado, IDE, compilador |
| VB 1.0 | 1991 | **Visual Basic 1.0** — programación visual para Windows |
| VB 2.0 | 1992 | Formularios más rápidos basados ​​en objetos |
| VB 3.0 | 1993 | **Soporte de base de datos** (Control de datos), Motor Jet |
| VB 4.0 | 1995 | Clases de 32 bits (sin herencia) |
| VB 5.0 | 1997 | **Componentes COM**, controles dibujados por el usuario |
| VB 6.0 | 1998 | **Principales**: COM, ADO, DCOM, WebClass: el VB clásico |
| VB.NET | 2002 | **Principal**: .NET Framework: programación orientada a objetos, herencia, GC |
| VB.NET 2003 | 2003 | .NET 1.1, IDE mejorado |
| VB 2005 | 2005 | **Mi espacio de nombres**, `Using`, `Continue`, editar y continuar |
| VB 2008 | 2008 | **LINQ**, literales XML, tipos anónimos, operador`If`|
| VB 2010 | 2010 | Lambdas multilínea, dinámicas, co/contravarianza |
| VB 2012 | 2012 | `Async`/`Await`, iteradores |
| VB 2015 | 2015 | Interpolación de cadenas `$""`, condicional nulo `?.`, nombre de |
| VB 2017 | 2017 | Tuplas, retornos de referencia, coincidencia de patrones |
| VB 15.3 | 2017 | Deconstrucción no tupla |
| VB 15.5 | 2017 | Ref locales, miembros de solo lectura |
| VB 16.0 | 2019 | **Tipos de referencia que admiten valores NULL**, expresiones`Switch`|
| VB 16.9 | 2021 |  Mejoras`OrElse`|
| VB 17.0 | 2022 | **Literales de cadena sin formato**, estructuras predeterminadas automáticamente, mejoras en`Module`|
| VB 17.7 | 2024 | Otras mejoras |
## Hitos importantes
### Orígenes BÁSICOS (1964-1990)
- **1964**: John Kemeny y Thomas Kurtz crean BASIC en Dartmouth College
- **Objetivo**: hacer que la programación sea accesible para estudiantes que no son de ciencias.
- **1983**: GW-BASIC: BASIC de Microsoft para PC IBM
- **1985**: QuickBASIC: programación estructurada, IDE, compilador
- Características clave: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`, `FOR`/`NEXT`
### Visual Basic 1–6: La era clásica (1991–2001)
- **1.0 (1991)**: Programación visual: generador de GUI de arrastrar y soltar para Windows
- **2.0 (1992)**: formularios más rápidos basados en objetos
- **3.0 (1993)**: soporte de base de datos: control de datos, motor Jet
- **4.0 (1995)**: 32 bits (Windows 95), clases
- **5.0 (1997)**: componentes COM, controles dibujados por el usuario
- **6.0 (1998)**: **El VB clásico**: COM, ADO, DCOM, WebClass
  - Versión más utilizada
  - Desarrollo rápido de aplicaciones (RAD)
  - Todavía ejecuta millones de aplicaciones heredadas
### VB.NET: La revolución .NET (2002-presente)
- **2002**: VB.NET: reescritura completa en .NET Framework
  - True POO: herencia, interfaces, polimorfismo
  - Recolección de basura
  - Acceso a toda la biblioteca de clases .NET
- **2005**: espacio de nombres`My`(fácil acceso a operaciones comunes)
- **2008**: **LINQ** — sintaxis de consulta integrada en el lenguaje
- **2012**:`Async`/`Await`— programación asincrónica
- **2015**: interpolación de cadenas `$""`,`?.`condicional nulo 
- **2017**: Tuplas, coincidencia de patrones
- **2019**: tipos de referencia que aceptan valores NULL
- **2022**: literales de cadena sin formato, sintaxis moderna
## Evolución de la sintaxis
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

## Evolución de funciones
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

## Principios clave de diseño
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Crecimiento del ecosistema
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
