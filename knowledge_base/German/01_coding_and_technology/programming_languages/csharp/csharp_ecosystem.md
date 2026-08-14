<!--
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

-->
# C# – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im C#/.NET-Ökosystem.
---

## .NET SDK und Toolchain
| Werkzeug | Zweck |
|------|---------|
| **dotnet CLI** | Erstellen, ausführen, testen, veröffentlichen |
| **MSBuild** | Zugrundeliegende Build-Engine |
| **NuGet-CLI** | Paketverwaltung |
| **dotnet-format** | Codeformatierung |
| **dotnet-ef** | Entity Framework-Tools |
| **dotnet-veraltet** | Finden Sie veraltete Pakete |
| **dotnet-script** | Führen Sie C#-Skripts (.csx) aus |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Laufzeiten und Implementierungen
| Laufzeit | Notizen |
|---------|-------|
| **.NET 8/9** | Aktuelles LTS/STS, plattformübergreifend |
| **.NET Framework** | Nur Windows, Legacy (4.8.x) |
| **Mono** | Open-Source-.NET Framework (Xamarin) |
| **Einheit (IL2CPP/Mono)** | Laufzeit der Spiel-Engine |
| **Godot (.NET)** | Spiel-Engine mit C#-Unterstützung |
---

## Paketverwaltung
| Quelle | Zweck |
|--------|---------|
| **NuGet.org** | Offizielle Paketregistrierung |
| **dotnet-Paket hinzufügen** | CLI-Paketinstallation |
| **Paketreferenz** | Modernes .csproj-Format |
| **Private Feeds** | Azure-Artefakte, GitHub-Pakete, MyGet |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **ASP.NET Core** | Full-Stack-Web | APIs, MVC, Blazor |
| **Minimale APIs** | Leicht | Einfache APIs |
| **Blazor-Server** | Interaktive Benutzeroberfläche | Vom Server gerendertes SPA |
| **Blazor WebAssembly** | Clientseitig | Browserbasiertes SPA |
| **gRPC** | RPC | Hochleistungsdienstleistungen |
| **SignalR** | Echtzeit | WebSockets, Push |
| **OData** | REST-Erweiterungen | Abfragbare APIs |
| **FastEndpoints** | API-Framework | Schnelle, minimale Boilerplate |
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

## Datenbank und ORM
| Technologie | Geben Sie | ein
|------------|------|
| **Entity Framework Core** | Vollständiges ORM, Migrationen |
| **Dapper** | Mikro-ORM, Roh-SQL |
| **NHibernate** | Reifes ORM |
| **FreeSql** | Leichtes ORM |
| **Marten** | PostgreSQL-Dokument-DB |
| **StackExchange.Redis** | Redis-Client |
| **MongoDB.Driver** | MongoDB-Client |
| **Npgsql** | PostgreSQL-Treiber |
| **MySqlConnector** | MySQL-Treiber |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **xUnit** | Beliebtestes Test-Framework |
| **NUnit** | Klassisches Testframework |
| **MSTest** | Testframework von Microsoft |
| **Moq** | Verspottungsbibliothek |
| **NSubstitute** | Freundlicher Spott |
| **FluentAssertions** | Fließende Aussagen |
| **Sollte** | Lesbare Behauptungen |
| **Falsch** | Gefälschte Datengenerierung |
| **AutoFixture** | Testdatenautomatisierung |
| **Testcontainer** | Docker-basierte Integrationstests |
| **BenchmarkDotNet** | Mikrobenchmarking |
| **Bettdecke** | Codeabdeckung |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **Roslyn-Analysatoren** | Integrierte Code-Analyse |
| **SonarAnalyzer.CSharp** | SonarQube-Regeln |
| **StyleCop** | Durchsetzung des Codierungsstils |
| **dotnet-format** | Codeformatierung |
| **EditorConfig** | Herausgeberübergreifende Konsistenz |
| **SonarQube / SonarCloud** | Code-Qualitätsplattform |
| **ReSharper** | JetBrains-Analyse + Refactoring |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **Visual Studio** | Voll ausgestattete Windows-IDE (Community/Pro/Enterprise) |
| **Reiter** | Plattformübergreifende JetBrains C#-IDE |
| **VS-Code + C#-Entwicklungskit** | Leicht, Microsoft-Erweiterung |
| **Visual Studio für Mac** | Im Ruhestand sein (Rider oder VS-Code verwenden) |
---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **System.Text.Json** | Integrierte JSON-Serialisierung |
| **Newtonsoft.Json** | Legacy-JSON (immer noch weit verbreitet) |
| **Serilog** | Strukturierte Protokollierung |
| **NLog** | Protokollierungsframework |
| **Polly** | Ausfallsicherheits- und Wiederholungsrichtlinien |
| **MediatR** | Mediatormuster (CQRS) |
| **AutoMapper** | Objekt-zu-Objekt-Zuordnung |
| **FluentValidation** | Validierungsbibliothek |
| **Massentransport** | Nachrichtenbus (RabbitMQ, Azure SB) |
| **Hangfire** | Hintergrundverarbeitung von Jobs |
| **Quartz.NET** | Jobplanung |
| **Spectre.Console** | Wunderschöne Konsolen-Apps |
| **CommandLineParser** | CLI-Argumentanalyse |
---

## Cloud- und Azure-Integration
| Service | Zweck |
|---------|---------|
| **Azure-Funktionen** | Serverlos |
| **Azure SDK für .NET** | Alle Azure-Dienste |
| **AWS SDK für .NET** | AWS-Dienste |
| **Google Cloud .NET** | GCP-Dienste |
| **Azure Cosmos DB** | NoSQL-Datenbank |
| **Azure Service Bus** | Nachrichten |
| **Azure Key Vault** | Geheimnismanagement |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Eigenständig** | Bündelt .NET-Laufzeit |
| **Framework-abhängig** | Erfordert die Installation von .NET |
| **Einzeldateiveröffentlichung** | `dotnet publish /p:PublishSingleFile=true`|
| **Native AOT** | `PublishAot=true`(kein JIT erforderlich) |
| **Docker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure App Service** | PaaS-Bereitstellung |
| **AWS Lambda** | Serverlos |
| **IIS** | Windows-Hosting |
| **Turmfalke** | Integrierter plattformübergreifender Webserver |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Zusammenfassung
C# und .NET bieten eines der produktivsten Ökosysteme. Der Standard-Stack ist: **.NET 8+** als Laufzeit, **ASP.NET Core** für das Web, **Entity Framework Core** oder **Dapper** für den Datenzugriff, **xUnit + Moq** zum Testen, **Visual Studio** oder **Rider** als IDE und **NuGet** für Pakete. Modernes C# mit Datensätzen, Mustervergleich, nullbaren Referenztypen und minimalen APIs ist prägnant und ausdrucksstark. **Native AOT**-Kompilierung ermöglicht einen blitzschnellen Start und kleine Binärdateien. Das Ökosystem zeichnet sich durch Unternehmens-, Cloud- (Azure), Spieleentwicklung (Unity, Godot) und plattformübergreifende Anwendungen aus.