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

# Visual Basic – Ecossistema e Guia de Ferramentas
Este guia aborda as ferramentas, estruturas e infraestrutura essenciais no ecossistema Visual Basic (.NET).
---

## Versões do Visual Basic
| Versão | Notas |
|--------|-------|
| **VB.NET (Visual Basic 2022)** | Atual, .NET 8+ |
| **VB6** | Visual Basic clássico (legado) |
| **VBA** | Visual Basic para Aplicativos (Escritório) |
| **VBScript** | Linguagem de script (obsoleta) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Ferramentas de construção
| Ferramenta | Finalidade |
|------|---------|
| **CLI dotnet** | .NET construir, testar, publicar |
| **MSBuild** | Construir motor |
| **Estúdio Visual** | IDE completo |
| **NuGet** | Gestão de pacotes |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **ASP.NET Core** | Pilha completa | APIs, MVC, páginas Razor |
| **APIs mínimas** | Leve | APIs simples |
| **Blazor** | IU da Web | UI baseada em componentes |
| **SinalR** | Em tempo real | WebSockets |
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

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **Núcleo do Entity Framework** | ORM completo |
| **Elegante** | Micro-ORM |
| **ADO.NET** | Acesso a dados de baixo nível |
| **OleDb** | Acesso a dados legados |
| **MySql.Dados** | Conector MySQL |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **xUnidade** | Estrutura de teste |
| **NUunidade** | Estrutura de teste |
| **MSTest** | Estrutura de teste da Microsoft |
| **Quantidade mínima** | Zombando |
| **NSubstituto** | Zombando |
| **Asserções Fluentes** | Afirmações fluentes |
| **BenchmarkDotNet** | Comparativo de mercado |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **Analisadores Roslyn** | Análise integrada |
| **SonarAnalyzer** | Regras do SonarQube |
| **formato dotnet** | Formatação de código |
| **EditorConfig** | Estilo consistente |
| **SonarQube** | Plataforma de qualidade de código |
---

## Desktop (WinForms/WPF)
| Estrutura | Finalidade |
|-----------|---------|
| **WinForms** | Formulários clássicos do Windows |
| **WPF** | UI moderna do Windows (XAML) |
| **MAUI** | Plataforma cruzada (sucessor do Xamarin) |
| **Avalônia** | Plataforma cruzada semelhante a WPF |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **System.Text.Json** | Serialização JSON |
| **Newtonsoft.Json** | JSON (legado) |
| **Serilog** | Registro |
| **Polly** | Políticas de resiliência |
| **AutoMapper** | Mapeamento de objetos |
| **Validação Fluente** | Validação |
| **Trânsito de massa** | Barramento de mensagens |
| **Hangfire** | Trabalhos em segundo plano |
| **Spectre.Console** | IU do console |
---

## Automação de escritório (VBA)
| Tecnologia | Finalidade |
|------------|---------|
| **Excel VBA** | Automação Excel |
| **Palavra VBA** | Automação de palavras |
| **Acessar VBA** | Automação de acesso |
| **Outlook VBA** | Automação do Outlook |
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

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Estúdio Visual** | IDE VB.NET completo (Community/Pro/Enterprise) |
| **Código VS** | Leve com extensões .NET |
| **Editor VBA** | Integrado em aplicativos do Office |
| **Cavaleiro** | JetBrains (suporte VB limitado) |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Autônomo** | Pacotes de tempo de execução .NET |
| **Dependente da estrutura** | Requer .NET instalado |
| **Arquivo único** | `PublishSingleFile`|
| **Docker** | Contentorizado |
| **MSI/ClickOnce** | Instalador do Windows |
| **Serviço de Aplicativo do Azure** | Hospedagem em nuvem |
| **IIS** | Hospedagem Windows |
---

## Resumo
O ecossistema do Visual Basic compartilha a vasta infraestrutura do .NET. A pilha padrão é: **.NET 8+** como tempo de execução, **Visual Studio** como IDE, **ASP.NET Core** para web, **Entity Framework Core** ou **Dapper** para acesso a dados, **xUnit** para testes e **NuGet** para pacotes. VB.NET é ideal para desenvolvedores familiarizados com a sintaxe BASIC que precisam de acesso ao ecossistema .NET. O **VBA** continua essencial para a automação do Office: milhões de usuários empresariais confiam nas macros do Excel e do Access. O ecossistema é mais adequado para aplicativos de desktop Windows, automação de escritório e aplicativos empresariais de linha de negócios.