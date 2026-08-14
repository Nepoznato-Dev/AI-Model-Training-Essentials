---
# Metadata
title: "Visual Basic — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Visual Basic ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [visual-basic, vbnet, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Visual Basic: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e l'infrastruttura essenziali nell'ecosistema Visual Basic (.NET).
---

## Versioni di Visual Basic
| Versione | Note |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Corrente, .NET 8+ |
| **VB6** | Visual Basic classico (legacy) |
| **VBA** | Visual Basic per applicazioni (Ufficio) |
| **VBScript** | Linguaggio di scripting (obsoleto) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Strumenti di creazione
| Strumento | Scopo |
|------|---------|
| **CLI puntonet** | Compilazione, test, pubblicazione di .NET |
| **MSBuild** | Costruisci motore |
| **Studio visivo** | IDE completo |
| **NuGet** | Gestione dei pacchetti |
```xml
<!-- .vbproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <RootNamespace>MyApp</RootNamespace>
    <TargetFramework>net8.0</TargetFramework>
    <OptionStrict>On</OptionStrict>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  </ItemGroup>
</Project>
```

---

## Framework Web
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **ASP.NET Core** | Stack completo | API, MVC, pagine Razor |
| **API minime** | Leggero | API semplici |
| **Blazor** | Interfaccia utente Web | Interfaccia utente basata su componenti |
| **SegnaleR** | In tempo reale | WebSocket |
```vb
' ASP.NET Core Minimal API
Imports Microsoft.AspNetCore.Builder
Imports Microsoft.Extensions.DependencyInjection

Dim builder = WebApplication.CreateBuilder(args)
Dim app = builder.Build()

app.MapGet("/hello", Function() "Hello, World!")

app.MapGet("/users/{id}", Async Function(id As Integer)
    Dim user = Await UserService.FindById(id)
    If user Is Nothing Then
        Return Results.NotFound()
    End If
    Return Results.Ok(user)
End Function)

app.Run()
```

---

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **Entity Framework Core** | ORM completo |
| **Azzeccato** | Micro-ORM |
| **ADO.NET** | Accesso ai dati di basso livello |
| **OleDb** | Accesso ai dati legacy |
| **MySql.Data** | Connettore MySQL |
| **Npgsql** | Connettore PostgreSQL |
```vb
' Dapper example
Imports Dapper
Imports System.Data.SqlClient

Using conn As New SqlConnection("connection-string")
    Dim users = Await conn.QueryAsync(Of User)(
        "SELECT Id, Name, Email FROM Users WHERE Age > @Age",
        New With {.Age = 18}
    )
    For Each user In users
        Console.WriteLine($"{user.Name} ({user.Email})")
    Next
End Using
```

---

## Test
| Quadro | Scopo |
|-----------|---------|
| **xUnità** | Quadro di prova |
| **NUnità** | Quadro di prova |
| **MSTest** | Quadro di prova Microsoft |
| **Moq** | Beffardo |
| **NSostituisci** | Beffardo |
| **FluentAssertions** | Affermazioni fluenti |
| **BenchmarkDotNet** | Analisi comparativa |
```vb
' xUnit test
Imports Xunit
Imports NSubstitute

Public Class UserServiceTests
    <Fact>
    Public Async Function FindUser_ReturnsUser() As Task
        ' Arrange
        Dim repo = Substitute.For(Of IUserRepository)()
        repo.GetByIdAsync(1).Returns(New User("Alice"))
        Dim service = New UserService(repo)

        ' Act
        Dim user = Await service.FindByIdAsync(1)

        ' Assert
        Assert.Equal("Alice", user.Name)
    End Function
End Class
```

---

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **Analizzatori Roslyn** | Analisi integrata |
| **SonarAnalyzer** | Regole SonarQube |
| **formato dotnet** | Formattazione del codice |
| **Configurazione editor** | Stile coerente |
| **SonarQube** | Piattaforma di qualità del codice |
---

## Desktop (WinForms/WPF)
| Quadro | Scopo |
|-----------|---------|
| **WinForms** | Moduli Windows classici |
| **WPF** | Moderna interfaccia utente di Windows (XAML) |
| **MAUI** | Multipiattaforma (successore di Xamarin) |
| **Avalonia** | Multipiattaforma simile a WPF |
```vb
' WinForms example
Public Class MainForm
    Inherits Form

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim name = TextBox1.Text
        MessageBox.Show($"Hello, {name}!", "Greeting")
    End Sub
End Class
```

---

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **System.Text.Json** | Serializzazione JSON |
| **Newtonsoft.Json** | JSON (precedente) |
| **Serilog** | Registrazione |
| **Polly** | Politiche di resilienza |
| **AutoMapper** | Mappatura oggetti |
| **Validazione fluente** | Convalida |
| **Trasporto di massa** | Bus dei messaggi |
| **Hangfire** | Lavori in background |
| **Spectre.Console** | Interfaccia utente della console |
---

## Automazione d'ufficio (VBA)
| Tecnologia | Scopo |
|------------|---------|
| **VBA Excel** | Automazione di Excel |
| **Parola VBA** | Automazione delle parole |
| **Accedi a VBA** | Automazione degli accessi |
| **VBA Outlook** | Automazione di Outlook |
```vb
' Excel VBA example
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")
    
    ws.Range("A1:D1").Font.Bold = True
    ws.Range("A1:D1").Interior.Color = RGB(0, 112, 192)
    
    ws.Columns("A:D").AutoFit
    
    MsgBox "Report formatted successfully!"
End Sub
```

---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Studio visivo** | IDE VB.NET completo (Community/Pro/Enterprise) |
| **Codice VS** | Leggero con estensioni .NET |
| **Editor VBA** | Integrato nelle app di Office |
| **Cavaliere** | JetBrains (supporto VB limitato) |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Autonomo** | Bundle runtime .NET |
| **Dipendente dal framework** | Richiede .NET installato |
| **File singolo** | `PublishSingleFile`|
| **Docker** | Containerizzato |
| **MSI/ClickOnce** | Programma di installazione di Windows |
| **Servizio app Azure** | Hosting sul cloud |
| **IIS** | Hosting Windows |
---

## Riepilogo
L'ecosistema di Visual Basic condivide la vasta infrastruttura di .NET. Lo stack standard è: **.NET 8+** come runtime, **Visual Studio** come IDE, **ASP.NET Core** per il Web, **Entity Framework Core** o **Dapper** per l'accesso ai dati, **xUnit** per i test e **NuGet** per i pacchetti. VB.NET è ideale per gli sviluppatori che hanno dimestichezza con la sintassi BASIC e che necessitano di accedere all'ecosistema .NET. **VBA** rimane essenziale per l'automazione di Office: milioni di utenti aziendali si affidano alle macro di Excel e Access. L'ecosistema è più adatto per le applicazioni desktop Windows, l'automazione di Office e le applicazioni line-of-business aziendali.