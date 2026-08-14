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

# Visual Basic — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème Visual Basic (.NET).
---

## Versions Visual Basic
| Version | Remarques |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Actuel, .NET 8+ |
| **VB6** | Visual Basic classique (hérité) |
| **VBA** | Visual Basic pour applications (Office) |
| **VBScript** | Langage de script (obsolète) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Outils de création
| Outil | Objectif |
|------|--------------|
| **CLI dotnet** | .NET construire, tester, publier |
| **MSBuild** | Construire le moteur |
| **Studio visuel** | EDI complet |
| **NuGet** | Gestion des paquets |
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

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **ASP.NET Core** | Pile complète | API, MVC, pages Razor |
| **API minimales** | Léger | API simples |
| **Blazer** | Interface utilisateur Web | Interface utilisateur basée sur des composants |
| **SignalR** | En temps réel | WebSockets |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **Noyau du cadre d'entité** | ORM complet |
| **Pimpant** | Micro-ORM |
| **ADO.NET** | Accès aux données de bas niveau |
| **OleDb** | Accès aux données héritées |
| **MySql.Data** | Connecteur MySQL |
| **Npgsql** | Connecteur PostgreSQL |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **xUnité** | Cadre de tests |
| **NUnité** | Cadre de tests |
| **MSTest** | Cadre de tests Microsoft |
| **Moq** | Moqueur |
| **NSubstitut** | Moqueur |
| **FluentAssertions** | Affirmations fluides |
| **BenchmarkDotNet** | Analyse comparative |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **Analyseurs Roslyn** | Analyse intégrée |
| **SonarAnalyzer** | Règles SonarQube |
| **format dotnet** | Formatage des codes |
| **EditeurConfig** | Style cohérent |
| **SonarQube** | Plateforme qualité du code |
---

## Bureau (WinForms / WPF)
| Cadre | Objectif |
|-----------|---------|
| **WinForms** | Formulaires Windows classiques |
| **WPF** | Interface utilisateur Windows moderne (XAML) |
| **MAUI** | Multiplateforme (successeur de Xamarin) |
| **Avalonie** | Multiplateforme de type WPF |
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

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Système.Text.Json** | Sérialisation JSON |
| **Newtonsoft.Json** | JSON (ancien) |
| **Sérilogue** | Journalisation |
| **Polly** | Politiques de résilience |
| **AutoMapper** | Mappage d'objets |
| **Validation fluide** | Validation |
| **Transport de masse** | Bus de messages |
| **Hangfire** | Emplois en arrière-plan |
| **Spectre.Console** | Interface utilisateur de la console |
---

## Bureautique (VBA)
| Technologie | Objectif |
|------------|---------|
| **Excel VBA** | Automatisation Excel |
| **Mot VBA** | Automatisation des mots |
| **Accéder à VBA** | Automatisation des accès |
| **Outlook VBA** | Automatisation d'Outlook |
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

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Studio visuel** | IDE VB.NET complet (Communauté/Pro/Entreprise) |
| **Code VS** | Léger avec les extensions .NET |
| **Éditeur VBA** | Intégré aux applications Office |
| **Cavalier** | JetBrains (prise en charge VB limitée) |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Autonome** | Bundles d'exécution .NET |
| **Dépend du framework** | Nécessite l'installation de .NET |
| **Fichier unique** | `PublishSingleFile`|
| **Docker** | Conteneurisé |
| **MSI / ClickOnce** | Programme d'installation Windows |
| **Azure App Service** | Hébergement cloud |
| **IIS** | Hébergement Windows |
---

## Résumé
L'écosystème de Visual Basic partage la vaste infrastructure de .NET. La pile standard est : **.NET 8+** comme environnement d'exécution, **Visual Studio** comme IDE, **ASP.NET Core** pour le Web, **Entity Framework Core** ou **Dapper** pour l'accès aux données, **xUnit** pour les tests et **NuGet** pour les packages. VB.NET est idéal pour les développeurs familiarisés avec la syntaxe BASIC qui ont besoin d'accéder à l'écosystème .NET. **VBA** reste essentiel pour la bureautique : des millions d'utilisateurs professionnels s'appuient sur les macros Excel et Access. L'écosystème est particulièrement adapté aux applications de bureau Windows, à la bureautique et aux applications métiers d'entreprise.