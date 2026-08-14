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

# Visual Basic – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| BÁSICO | 1964 | **BASIC Original** (Kemeny & Kurtz, Dartmouth) |
| GW-BASIC | 1983 | BASIC da Microsoft para IBM PC |
| QuickBASIC | 1985 | BASIC estruturado, IDE, compilador |
| VB 1.0 | 1991 | **Visual Basic 1.0** — programação visual para Windows |
| VB 2.0 | 1992 | Formulários mais rápidos e baseados em objetos |
| VB 3.0 | 1993 | **Suporte a banco de dados** (Controle de Dados), Motor Jet |
| VB 4.0 | 1995 | Classes de 32 bits (sem herança) |
| VB 5.0 | 1997 | **Componentes COM**, controles desenhados pelo usuário |
| VB 6.0 | 1998 | **Principais**: COM, ADO, DCOM, WebClass — o clássico VB |
| VB.NET | 2002 | **Principal**: .NET Framework — OOP, herança, GC |
| VB.NET 2003 | 2003 | .NET 1.1, IDE aprimorado |
| VB 2005 | 2005 | **Meu namespace**,`Using`,`Continue`, editar e continuar |
| VB 2008 | 2008 | **LINQ**, literais XML, tipos anônimos, operador`If`|
| VB 2010 | 2010 | Lambdas multilinhas, dinâmicas, co/contravariância |
| VB 2012 | 2012 | `Async`/`Await`, iteradores |
| VB 2015 | 2015 | Interpolação de string`$""`,`?.`condicional nulo , nameof |
| VB 2017 | 2017 | Tuplas, retornos de referência, correspondência de padrões |
| VB 15.3 | 2017 | Desconstrução não tupla |
| VB 15.5 | 2017 | Ref locais, membros somente leitura |
| VB 16.0 | 2019 | **Tipos de referência anuláveis**, expressões`Switch`|
| VB 16.9 | 2021 |  Melhorias`OrElse`|
| VB 17.0 | 2022 | **Literais de string brutos**, estruturas de padrão automático, melhorias em`Module`|
| VB 17.7 | 2024 | Outros refinamentos |
## Marcos importantes
### Origens BÁSICAS (1964–1990)
- **1964**: John Kemeny e Thomas Kurtz criam o BASIC no Dartmouth College
- **Objetivo**: Tornar a programação acessível a estudantes que não são de ciências
- **1983**: GW-BASIC — BASIC da Microsoft para IBM PC
- **1985**: QuickBASIC — programação estruturada, IDE, compilador
- Principais recursos: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: A Era Clássica (1991–2001)
- **1.0 (1991)**: Programação visual — construtor de GUI de arrastar e soltar para Windows
- **2.0 (1992)**: Formulários mais rápidos e baseados em objetos
- **3.0 (1993)**: Suporte a banco de dados — Controle de dados, motor a jato
- **4.0 (1995)**: 32 bits (Windows 95), classes
- **5.0 (1997)**: componentes COM, controles desenhados pelo usuário
- **6.0 (1998)**: **O clássico VB** — COM, ADO, DCOM, WebClass
  - Versão mais utilizada
  - Desenvolvimento Rápido de Aplicativos (RAD)
  - Ainda executa milhões de aplicativos legados
### VB.NET: A Revolução .NET (2002-presente)
- **2002**: VB.NET — reescrita completa no .NET Framework
  - True OOP — herança, interfaces, polimorfismo
  - Coleta de lixo
  - Acesso a toda a biblioteca de classes .NET
- **2005**: namespace`My`(fácil acesso a operações comuns)
- **2008**: **LINQ** — sintaxe de consulta integrada à linguagem
- **2012**:`Async`/`Await`— programação assíncrona
- **2015**: interpolação de string`$""`,`?.`condicional nulo 
- **2017**: Tuplas, correspondência de padrões
- **2019**: tipos de referência anuláveis
- **2022**: literais de string brutos, sintaxe moderna
## Evolução da Sintaxe
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

## Evolução de recursos
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

## Princípios-chave de design
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Crescimento do Ecossistema
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
