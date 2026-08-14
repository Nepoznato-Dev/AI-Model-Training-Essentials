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
# Visual Basic — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, frameworks, at imprastraktura sa Visual Basic (.NET) ecosystem.
---

## Mga Visual Basic na Bersyon
| Bersyon | Mga Tala |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Kasalukuyan, .NET 8+ |
| **VB6** | Classic Visual Basic (legacy) |
| **VBA** | Visual Basic para sa Mga Application (Opisina) |
| **VBScript** | Wika ng scripting (hindi na ginagamit) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Bumuo ng Mga Tool
| Tool | Layunin |
|------|---------|
| **dotnet CLI** | .NET build, test, publish |
| **MSBuild** | Bumuo ng makina |
| **Visual Studio** | Buong IDE |
| **NuGet** | Pamamahala ng package |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **ASP.NET Core** | Full-stack | Mga API, MVC, Razor Pages |
| **Mga Minimal na API** | Magaan | Mga Simpleng API |
| **Blazor** | Web UI | Component-based UI |
| **SignalR** | Real-time | Mga WebSocket |
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
| Teknolohiya | Uri |
|------------|------|
| **Entity Framework Core** | Buong ORM |
| **Dapper** | Micro-ORM |
| **ADO.NET** | Mababang antas ng pag-access sa data |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **xUnit** | Balangkas ng pagsubok |
| **NUnit** | Balangkas ng pagsubok |
| **MSTest** | Microsoft test framework |
| **Moq** | Nanunuya |
| **NShalili** | Nanunuya |
| **FluentAssertions** | Mga matatas na pahayag |
| **BenchmarkDotNet** | Pag-benchmark |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **Roslyn Analyzers** | Built-in na pagsusuri |
| **SonarAnalyzer** | Mga panuntunan sa SonarQube |
| **dotnet-format** | Pag-format ng code |
| **EditorConfig** | Pare-parehong istilo |
| **SonarQube** | Platform ng kalidad ng code |
---

## Desktop (WinForms / WPF)
| Balangkas | Layunin |
|-----------|---------|
| **WinForms** | Mga klasikong Windows form |
| **WPF** | Makabagong Windows UI (XAML) |
| **MAUI** | Cross-platform (kapalit ng Xamarin) |
| **Avalonia** | Cross-platform na parang WPF |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **System.Text.Json** | JSON serialization |
| **Newtonsoft.Json** | JSON (legacy) |
| **Serilog** | Pag-log |
| **Polly** | Mga patakaran sa katatagan |
| **AutoMapper** | Pagmamapa ng bagay |
| **FluentValidation** | Pagpapatunay |
| **MassTransit** | Mensahe bus |
| **Hangfire** | Mga trabaho sa background |
| **Spectre.Console** | Console UI |
---

## Office Automation (VBA)
| Teknolohiya | Layunin |
|------------|---------|
| **Excel VBA** | Excel automation |
| **Salita VBA** | Word automation |
| **I-access ang VBA** | I-access ang automation |
| **Outlook VBA** | automation ng Outlook |
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

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **Visual Studio** | Buong VB.NET IDE (Community/Pro/Enterprise) |
| **VS Code** | Magaan na may .NET extension |
| **VBA Editor** | Built in na Office app |
| **Rider** | JetBrains (limitadong suporta sa VB) |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Makasarili** | Mga Bundle .NET runtime |
| **nakadepende sa framework** | Nangangailangan ng .NET na naka-install |
| **Single-file** | `PublishSingleFile`|
| **Docker** | Naka-container |
| **MSI / ClickOnce** | Windows installer |
| **Serbisyo ng Azure App** | Cloud hosting |
| **IIS** | Windows hosting |
---

## Buod
Ibinabahagi ng ecosystem ng Visual Basic ang malawak na imprastraktura ng .NET. Ang karaniwang stack ay: **.NET 8+** bilang runtime, **Visual Studio** bilang IDE, **ASP.NET Core** para sa web, **Entity Framework Core** o **Dapper** para sa pag-access ng data, **xUnit** para sa pagsubok, at **NuGet** para sa mga package. Ang VB.NET ay mainam para sa mga developer na kumportable sa BASIC syntax na nangangailangan ng access sa .NET ecosystem. Nananatiling mahalaga ang **VBA** para sa automation ng Office — milyon-milyong user ng negosyo ang umaasa sa Excel at Access macros. Ang ecosystem ay pinakaangkop para sa Windows desktop application, Office automation, at enterprise line-of-business application.