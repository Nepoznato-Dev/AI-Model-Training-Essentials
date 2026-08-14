<!--
---
# Metadata
title: "Visual Basic — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Visual Basic ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Visual Basic — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Visual Basic (.NET) ecosystem.

---

## Visual Basic Versions

| Version | Notes |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Current, .NET 8+ |
| **VB6** | Classic Visual Basic (legacy) |
| **VBA** | Visual Basic for Applications (Office) |
| **VBScript** | Scripting language (deprecated) |

```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Build Tools

| Tool | Purpose |
|------|---------|
| **dotnet CLI** | .NET build, test, publish |
| **MSBuild** | Build engine |
| **Visual Studio** | Full IDE |
| **NuGet** | Package management |

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

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **ASP.NET Core** | Full-stack | APIs, MVC, Razor Pages |
| **Minimal APIs** | Lightweight | Simple APIs |
| **Blazor** | Web UI | Component-based UI |
| **SignalR** | Real-time | WebSockets |

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

## Database

| Technology | Type |
|------------|------|
| **Entity Framework Core** | Full ORM |
| **Dapper** | Micro-ORM |
| **ADO.NET** | Low-level data access |
| **OleDb** | Legacy data access |
| **MySql.Data** | MySQL connector |
| **Npgsql** | PostgreSQL connector |

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

## Testing

| Framework | Purpose |
|-----------|---------|
| **xUnit** | Test framework |
| **NUnit** | Test framework |
| **MSTest** | Microsoft test framework |
| **Moq** | Mocking |
| **NSubstitute** | Mocking |
| **FluentAssertions** | Fluent assertions |
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

## Code Quality

| Tool | Purpose |
|------|---------|
| **Roslyn Analyzers** | Built-in analysis |
| **SonarAnalyzer** | SonarQube rules |
| **dotnet-format** | Code formatting |
| **EditorConfig** | Consistent style |
| **SonarQube** | Code quality platform |

---

## Desktop (WinForms / WPF)

| Framework | Purpose |
|-----------|---------|
| **WinForms** | Classic Windows forms |
| **WPF** | Modern Windows UI (XAML) |
| **MAUI** | Cross-platform (successor to Xamarin) |
| **Avalonia** | Cross-platform WPF-like |

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

## Key Libraries

| Library | Purpose |
|---------|---------|
| **System.Text.Json** | JSON serialization |
| **Newtonsoft.Json** | JSON (legacy) |
| **Serilog** | Logging |
| **Polly** | Resilience policies |
| **AutoMapper** | Object mapping |
| **FluentValidation** | Validation |
| **MassTransit** | Message bus |
| **Hangfire** | Background jobs |
| **Spectre.Console** | Console UI |

---

## Office Automation (VBA)

| Technology | Purpose |
|------------|---------|
| **Excel VBA** | Excel automation |
| **Word VBA** | Word automation |
| **Access VBA** | Access automation |
| **Outlook VBA** | Outlook automation |

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

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **Visual Studio** | Full VB.NET IDE (Community/Pro/Enterprise) |
| **VS Code** | Lightweight with .NET extensions |
| **VBA Editor** | Built into Office apps |
| **Rider** | JetBrains (limited VB support) |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Self-contained** | Bundles .NET runtime |
| **Framework-dependent** | Requires .NET installed |
| **Single-file** | `PublishSingleFile` |
| **Docker** | Containerized |
| **MSI / ClickOnce** | Windows installer |
| **Azure App Service** | Cloud hosting |
| **IIS** | Windows hosting |

---

## Summary

Visual Basic's ecosystem shares .NET's vast infrastructure. The standard stack is: **.NET 8+** as runtime, **Visual Studio** as IDE, **ASP.NET Core** for web, **Entity Framework Core** or **Dapper** for data access, **xUnit** for testing, and **NuGet** for packages. VB.NET is ideal for developers comfortable with BASIC syntax who need access to the .NET ecosystem. **VBA** remains essential for Office automation — millions of business users rely on Excel and Access macros. The ecosystem is best suited for Windows desktop applications, Office automation, and enterprise line-of-business applications.
