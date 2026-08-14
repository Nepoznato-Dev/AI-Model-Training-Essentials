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

# Visual Basic – Ökosystem- und Werkzeughandbuch
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Visual Basic (.NET)-Ökosystem.
---

## Visual Basic-Versionen
| Version | Notizen |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Aktuell, .NET 8+ |
| **VB6** | Klassisches Visual Basic (Legacy) |
| **VBA** | Visual Basic für Anwendungen (Office) |
| **VBScript** | Skriptsprache (veraltet) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Build-Tools
| Werkzeug | Zweck |
|------|---------|
| **dotnet CLI** | .NET erstellen, testen, veröffentlichen |
| **MSBuild** | Engine erstellen |
| **Visual Studio** | Vollständige IDE |
| **NuGet** | Paketverwaltung |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **ASP.NET Core** | Full-Stack | APIs, MVC, Razor-Seiten |
| **Minimale APIs** | Leicht | Einfache APIs |
| **Blazer** | Web-Benutzeroberfläche | Komponentenbasierte Benutzeroberfläche |
| **SignalR** | Echtzeit | WebSockets |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **Entity Framework Core** | Vollständiges ORM |
| **Dapper** | Mikro-ORM |
| **ADO.NET** | Low-Level-Datenzugriff |
| **OleDb** | Zugriff auf Altdaten |
| **MySql.Data** | MySQL-Connector |
| **Npgsql** | PostgreSQL-Connector |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **xUnit** | Test-Framework |
| **NUnit** | Test-Framework |
| **MSTest** | Microsoft-Testframework |
| **Moq** | Spott |
| **NSubstitute** | Spott |
| **FluentAssertions** | Fließende Aussagen |
| **BenchmarkDotNet** | Benchmarking |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **Roslyn-Analysatoren** | Integrierte Analyse |
| **SonarAnalyzer** | SonarQube-Regeln |
| **dotnet-format** | Codeformatierung |
| **EditorConfig** | Konsistenter Stil |
| **SonarQube** | Code-Qualitätsplattform |
---

## Desktop (WinForms / WPF)
| Rahmen | Zweck |
|-----------|---------|
| **WinForms** | Klassische Windows-Formulare |
| **WPF** | Moderne Windows-Benutzeroberfläche (XAML) |
| **MAUI** | Plattformübergreifend (Nachfolger von Xamarin) |
| **Avalonia** | Plattformübergreifendes WPF-ähnliches |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **System.Text.Json** | JSON-Serialisierung |
| **Newtonsoft.Json** | JSON (alt) |
| **Serilog** | Protokollierung |
| **Polly** | Resilienzrichtlinien |
| **AutoMapper** | Objektzuordnung |
| **FluentValidation** | Validierung |
| **Massentransport** | Nachrichtenbus |
| **Hangfire** | Hintergrundjobs |
| **Spectre.Console** | Konsolen-Benutzeroberfläche |
---

## Büroautomatisierung (VBA)
| Technologie | Zweck |
|------------|---------|
| **Excel VBA** | Excel-Automatisierung |
| **Word VBA** | Wortautomatisierung |
| **Zugriff auf VBA** | Zugriffsautomatisierung |
| **Outlook VBA** | Outlook-Automatisierung |
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

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **Visual Studio** | Vollständige VB.NET-IDE (Community/Pro/Enterprise) |
| **VS-Code** | Leichtgewichtig mit .NET-Erweiterungen |
| **VBA-Editor** | In Office-Apps integriert |
| **Reiter** | JetBrains (eingeschränkte VB-Unterstützung) |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Eigenständig** | Bündelt .NET-Laufzeit |
| **Framework-abhängig** | Erfordert die Installation von .NET |
| **Einzeldatei** | `PublishSingleFile`|
| **Docker** | Containerisiert |
| **MSI / ClickOnce** | Windows-Installer |
| **Azure App Service** | Cloud-Hosting |
| **IIS** | Windows-Hosting |
---

## Zusammenfassung
Das Ökosystem von Visual Basic teilt sich die umfangreiche Infrastruktur von .NET. Der Standard-Stack ist: **.NET 8+** als Laufzeit, **Visual Studio** als IDE, **ASP.NET Core** für das Web, **Entity Framework Core** oder **Dapper** für den Datenzugriff, **xUnit** für Tests und **NuGet** für Pakete. VB.NET ist ideal für Entwickler, die mit der BASIC-Syntax vertraut sind und Zugriff auf das .NET-Ökosystem benötigen. **VBA** bleibt für die Office-Automatisierung unverzichtbar – Millionen von Geschäftsanwendern verlassen sich auf Excel- und Access-Makros. Das Ökosystem eignet sich am besten für Windows-Desktopanwendungen, Büroautomatisierung und Branchenanwendungen für Unternehmen.