---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [csharp, ecosystem, tooling, dotnet, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C# — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème C#/.NET.
---

## SDK et chaîne d'outils .NET
| Outil | Objectif |
|------|--------------|
| **CLI dotnet** | Construire, exécuter, tester, publier |
| **MSBuild** | Moteur de build sous-jacent |
| **CLI NuGet** | Gestion des paquets |
| **format dotnet** | Formatage des codes |
| **dotnet-ef** | Outils Entity Framework |
| **dotnet-obsolète** | Trouver des packages obsolètes |
| **dotnet-script** | Exécuter des scripts C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Exécutions et implémentations
| Durée d'exécution | Remarques |
|---------|-------|
| **.NET 8/9** | LTS / STS actuels, multiplateforme |
| **.NET Framework** | Windows uniquement, ancien (4.8.x) |
| **Mono** | .NET Framework open source (Xamarin) |
| **Unité (IL2CPP/Mono)** | Durée d'exécution du moteur de jeu |
| **Godot (.NET)** | Moteur de jeu avec support C# |
---

## Gestion des paquets
| Source | Objectif |
|--------|---------|
| **NuGet.org** | Registre officiel des packages |
| **package d'ajout dotnet** | Installation du package CLI |
| **Référence du package** | Format .csproj moderne |
| **Flux privés** | Artefacts Azure, packages GitHub, MyGet |
```xml
<!-- .csproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Dapper" Version="2.1.0" />
  </ItemGroup>
</Project>
```

---

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **ASP.NET Core** | Web complet | API, MVC, Blazor |
| **API minimales** | Léger | API simples |
| **Serveur Blazor** | Interface utilisateur interactive | SPA rendu par le serveur |
| **Blazor WebAssembly** | Côté client | SPA basé sur un navigateur |
| **gRPC** | RPC | Des prestations performantes |
| **SignalR** | En temps réel | WebSockets, pousser |
| **ODonnées** | Extensions REST | API interrogeables |
| **FastEndpoints** | Cadre API | Passe-partout rapide et minimal |
```csharp
// Minimal API example
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/hello", () => "Hello, World!");
app.MapGet("/users/{id}", async (int id, UserDb db) =>
    await db.Users.FindAsync(id) is User u ? Results.Ok(u) : Results.NotFound());

app.Run();
```

---

## Base de données et ORM
| Technologie | Tapez |
|------------|------|
| **Noyau du cadre d'entité** | ORM complet, migrations |
| **Pimpant** | Micro-ORM, SQL brut |
| **NHiberner** | ORM mature |
| **FreeSql** | ORM léger |
| **Martre** | Base de données de documents PostgreSQL |
| **StackExchange.Redis** | Client Redis |
| **MongoDB.Driver** | Client MongoDB |
| **Npgsql** | Pilote PostgreSQL |
| **MySqlConnecteur** | Pilote MySQL |
```csharp
// EF Core example
public class AppDbContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    protected override void OnConfiguring(DbContextOptionsBuilder o)
        => o.UseSqlServer("connection-string");
}

var users = await db.Users
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name)
    .ToListAsync();
```

---

## Tests
| Cadre | Objectif |
|-----------|---------|
| **xUnité** | Cadre de test le plus populaire |
| **NUnité** | Cadre de test classique |
| **MSTest** | Le framework de test de Microsoft |
| **Moq** | Bibliothèque moqueuse |
| **NSubstitut** | Moquerie amicale |
| **FluentAssertions** | Affirmations fluides |
| **Devrait** | Affirmations lisibles |
| **Faux** | Génération de fausses données |
| **Fixation automatique** | Automatisation des données de test |
| **Conteneurs de test** | Tests d'intégration basés sur Docker |
| **BenchmarkDotNet** | Microbenchmarking |
| **couverture** | Couverture du code |
```csharp
// xUnit + FluentAssertions
public class UserServiceTests
{
    [Fact]
    public async Task Should_Find_User_By_Id()
    {
        var mockRepo = Substitute.For<IUserRepository>();
        mockRepo.GetByIdAsync(1).Returns(new User("Alice"));
        var service = new UserService(mockRepo);

        var user = await service.GetByIdAsync(1);

        user.Name.Should().Be("Alice");
    }
}
```

---

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **Analyseurs Roslyn** | Analyse de code intégrée |
| **SonarAnalyzer.CSharp** | Règles SonarQube |
| **StyleCop** | Application du style de codage |
| **format dotnet** | Formatage des codes |
| **EditeurConfig** | Cohérence entre éditeurs |
| **SonarQube / SonarCloud** | Plateforme qualité du code |
| **ReSharper** | Analyse JetBrains + refactorisation |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Studio visuel** | IDE Windows complet (Communauté/Pro/Entreprise) |
| **Cavalier** | IDE JetBrains C# multiplateforme |
| **VS Code + Kit de développement C#** | Extension Microsoft légère |
| **Visual Studio pour Mac** | Être à la retraite (utiliser Rider ou VS Code) |
---

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Système.Text.Json** | Sérialisation JSON intégrée |
| **Newtonsoft.Json** | Legacy JSON (encore largement utilisé) |
| **Sérilogue** | Journalisation structurée |
| **NLog** | Cadre de journalisation |
| **Polly** | Politiques de résilience et de nouvelle tentative |
| **MédiatR** | Modèle médiateur (CQRS) |
| **AutoMapper** | Mappage objet à objet |
| **Validation fluide** | Bibliothèque de validation |
| **Transport de masse** | Bus de messages (RabbitMQ, Azure SB) |
| **Hangfire** | Traitement des tâches en arrière-plan |
| **Quartz.NET** | Planification des travaux |
| **Spectre.Console** | De belles applications de console |
| **CommandLineParser** | Analyse des arguments CLI |
---

## Intégration Cloud et Azure
| Services | Objectif |
|---------|---------|
| **Fonctions Azure** | Sans serveur |
| **SDK Azure pour .NET** | Tous les services Azure |
| **Kit SDK AWS pour .NET** | Services AWS |
| **Google Cloud.NET** | Services GCP |
| **Azure Cosmos DB** | Base de données NoSQL |
| **Azure Service Bus** | Messagerie |
| **Coffre de clés Azure** | Gestion des secrets |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Autonome** | Bundles d'exécution .NET |
| **Dépend du framework** | Nécessite l'installation de .NET |
| **Publication d'un fichier unique** | `dotnet publish /p:PublishSingleFile=true`|
| **AOT natif** | `PublishAot=true`(pas de JIT nécessaire) |
| **Docker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure App Service** | Déploiement PaaS |
| **AWS Lambda** | Sans serveur |
| **IIS** | Hébergement Windows |
| **Crécerelle** | Serveur Web multiplateforme intégré |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Résumé
C# et .NET offrent l'un des écosystèmes les plus productifs. La pile standard est : **.NET 8+** comme environnement d'exécution, **ASP.NET Core** pour le Web, **Entity Framework Core** ou **Dapper** pour l'accès aux données, **xUnit + Moq** pour les tests, **Visual Studio** ou **Rider** comme IDE et **NuGet** pour les packages. Le C# moderne avec des enregistrements, une correspondance de modèles, des types de référence nullables et un minimum d'API est concis et expressif. La compilation **AOT native** permet un démarrage ultra-rapide et de petits binaires. L'écosystème excelle dans les applications d'entreprise, cloud (Azure), de jeux (Unity, Godot) et multiplateformes.