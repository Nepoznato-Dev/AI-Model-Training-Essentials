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
# Visual Basic: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema de Visual Basic (.NET).
---

## Versiones de Visual Basic
| Versión | Notas |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Actual, .NET 8+ |
| **VB6** | Visual Basic clásico (heredado) |
| **VBA** | Visual Basic para Aplicaciones (Office) |
| **VBScript** | Lenguaje de scripting (obsoleto) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Herramientas de construcción
| Herramienta | Propósito |
|------|---------|
| ** CLI puntonet ** | .NET compila, prueba y publica |
| **MSBuild** | Construir motor |
| **Estudio visual** | IDE completo |
| **NuGet** | Gestión de paquetes |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Núcleo ASP.NET** | Pila completa | API, MVC, páginas Razor |
| **API mínimas** | Ligero | API simples |
| **Blazor** | Interfaz de usuario web | UI basada en componentes |
| **SeñalR** | En tiempo real | WebSockets |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **Núcleo de Entity Framework** | ORM completo |
| **Apuesto** | Micro-ORM |
| **ADO.NET** | Acceso a datos de bajo nivel |
| **OleDb** | Acceso a datos heredados |
| **MySql.Datos** | Conector MySQL |
| **Npgsql** | Conector PostgreSQL |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **xUnidad** | Marco de prueba |
| **NUnidad** | Marco de prueba |
| **Prueba MST** | Marco de prueba de Microsoft |
| **Pedido mínimo** | Burlarse |
| **NSustituto** | Burlarse |
| **Afirmaciones fluidas** | Afirmaciones fluidas |
| **Parámetro de referenciaDotNet** | Evaluación comparativa |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **Analizadores Roslyn** | Análisis incorporado |
| **Analizador de sonda** | Reglas de SonarQube |
| **formato dotnet** | Formato de código |
| **EditorConfiguración** | Estilo consistente |
| **SónarQube** | Plataforma de calidad de código |
---

## Escritorio (WinForms/WPF)
| Marco | Propósito |
|-----------|------------------|
| **WinForms** | Formularios clásicos de Windows |
| **WPF** | Interfaz de usuario moderna de Windows (XAML) |
| **MAUI** | Multiplataforma (sucesor de Xamarin) |
| **Avalonia** | Tipo WPF multiplataforma |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Sistema.Texto.Json** | Serialización JSON |
| **Newtonsoft.Json** | JSON (heredado) |
| **Serilog** | Registro |
| **Polly** | Políticas de resiliencia |
| **AutoMapeador** | Mapeo de objetos |
| **Validación de fluidez** | Validación |
| **Tránsito masivo** | Autobús de mensajes |
| **Hangfire** | Trabajos en segundo plano |
| **Spectre.Consola** | Interfaz de usuario de la consola |
---

## Ofimática (VBA)
| Tecnología | Propósito |
|------------|---------|
| **Excel VBA** | Automatización de Excel |
| **Palabra VBA** | Automatización de palabras |
| **Acceder a VBA** | Automatización de accesos |
| **Perspectiva VBA** | Automatización de Outlook |
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

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Estudio visual** | IDE VB.NET completo (Comunidad/Pro/Empresa) |
| **Código VS** | Ligero con extensiones .NET |
| **Editor VBA** | Integrado en aplicaciones de Office |
| **Jinete** | JetBrains (soporte VB limitado) |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Autónomo** | Paquetes de tiempo de ejecución .NET |
| **Depende del marco** | Requiere .NET instalado |
| **Fila única** | `PublishSingleFile`|
| **Acoplador** | En contenedores |
| **MSI / Haga clic una vez** | Instalador de Windows |
| **Servicio de aplicaciones Azure** | Alojamiento en la nube |
| **IIS** | Alojamiento de Windows |
---

## Resumen
El ecosistema de Visual Basic comparte la vasta infraestructura de .NET. La pila estándar es: **.NET 8+** como tiempo de ejecución, **Visual Studio** como IDE, **ASP.NET Core** para web, **Entity Framework Core** o **Dapper** para acceso a datos, **xUnit** para pruebas y **NuGet** para paquetes. VB.NET es ideal para desarrolladores que se sienten cómodos con la sintaxis BÁSICA y necesitan acceso al ecosistema .NET. **VBA** sigue siendo esencial para la automatización de Office: millones de usuarios empresariales confían en las macros de Excel y Access. El ecosistema es más adecuado para aplicaciones de escritorio de Windows, automatización de oficina y aplicaciones de línea de negocio empresarial.