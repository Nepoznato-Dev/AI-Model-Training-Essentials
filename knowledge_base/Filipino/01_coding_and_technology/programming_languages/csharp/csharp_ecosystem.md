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
# C# — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa C# / .NET ecosystem.
---

## .NET SDK at Toolchain
| Tool | Layunin |
|------|---------|
| **dotnet CLI** | Bumuo, tumakbo, subukan, i-publish |
| **MSBuild** | Pinagbabatayan na build engine |
| **NuGet CLI** | Pamamahala ng package |
| **dotnet-format** | Pag-format ng code |
| **dotnet-ef** | Mga tool sa Entity Framework |
| **dotnet-outdated** | Maghanap ng mga lumang package |
| **dotnet-script** | Patakbuhin ang mga C# script (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Mga Runtime at Pagpapatupad
| Runtime | Mga Tala |
|---------|-------|
| **.NET 8/9** | Kasalukuyang LTS / STS, cross-platform |
| **.NET Framework** | Windows-only, legacy (4.8.x) |
| **Mono** | Open-source .NET Framework (Xamarin) |
| **Pagkakaisa (IL2CPP/Mono)** | Runtime ng engine ng laro |
| **Godot (.NET)** | Game engine na may suporta sa C# |
---

## Pamamahala ng Package
| Pinagmulan | Layunin |
|--------|---------|
| **NuGet.org** | Opisyal na pagpapatala ng package |
| **dotnet add package** | Pag-install ng CLI package |
| **PackageReference** | Modernong .csproj na format |
| **Mga pribadong feed** | Mga Azure Artifact, Mga Pakete ng GitHub, MyGet |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **ASP.NET Core** | Full-stack na web | Mga API, MVC, Blazor |
| **Mga Minimal na API** | Magaan | Mga Simpleng API |
| **Server ng Blazor** | Interactive na UI | SPA na ibinigay ng server |
| **Blazor WebAssembly** | Client-side | SPA na nakabatay sa browser |
| **gRPC** | RPC | Mga serbisyong may mataas na pagganap |
| **SignalR** | Real-time | WebSockets, itulak |
| **OData** | REST extension | Mga Natatanong na API |
| **FastEndpoints** | API framework | Mabilis, minimal na boilerplate |
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

## Database at ORM
| Teknolohiya | Uri |
|------------|------|
| **Entity Framework Core** | Buong ORM, paglilipat |
| **Dapper** | Micro-ORM, raw SQL |
| **NHibernate** | Mature ORM |
| **FreeSql** | Magaang ORM |
| **Marten** | PostgreSQL na dokumento DB |
| **StackExchange.Redis** | Redis client |
| **MongoDB.Driver** | MongoDB client |
| **Npgsql** | PostgreSQL driver |
| **MySqlConnector** | MySQL driver |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **xUnit** | Pinakatanyag na balangkas ng pagsubok |
| **NUnit** | Klasikong balangkas ng pagsubok |
| **MSTest** | Ang balangkas ng pagsubok ng Microsoft |
| **Moq** | Mapanuksong library |
| **NShalili** | Friendly na panunuya |
| **FluentAssertions** | Mga matatas na pahayag |
| **Dapat** | Mga nababasang paninindigan |
| **Bogus** | Pagbuo ng pekeng data |
| **AutoFixture** | Pag-aautomat ng data ng pagsubok |
| **Mga Testcontainer** | Docker-based integration tests |
| **BenchmarkDotNet** | Microbenchmarking |
| **coverlet** | Saklaw ng code |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **Roslyn Analyzers** | Built-in na pagsusuri ng code |
| **SonarAnalyzer.CSharp** | Mga panuntunan sa SonarQube |
| **StyleCop** | Pagpapatupad ng istilo ng coding |
| **dotnet-format** | Pag-format ng code |
| **EditorConfig** | Cross-editor consistency |
| **SonarQube / SonarCloud** | Platform ng kalidad ng code |
| **ReSharper** | Pagsusuri ng JetBrains + refactoring |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **Visual Studio** | Full-feature na Windows IDE (Community/Pro/Enterprise) |
| **Rider** | Cross-platform na JetBrains C# IDE |
| **VS Code + C# Dev Kit** | Magaan, Microsoft extension |
| **Visual Studio para sa Mac** | Ang pagiging retirado (gamitin ang Rider o VS Code) |
---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **System.Text.Json** | Built-in na JSON serialization |
| **Newtonsoft.Json** | Legacy JSON (malawakang ginagamit pa rin) |
| **Serilog** | Structured logging |
| **NLog** | Balangkas ng pag-log |
| **Polly** | Mga patakaran sa katatagan at subukang muli |
| **MediatR** | Pattern ng tagapamagitan (CQRS) |
| **AutoMapper** | Object-to-object mapping |
| **FluentValidation** | Aklatan ng pagpapatunay |
| **MassTransit** | Mensahe bus (RabbitMQ, Azure SB) |
| **Hangfire** | Pagproseso ng trabaho sa background |
| **Quartz.NET** | Pag-iiskedyul ng trabaho |
| **Spectre.Console** | Magagandang console app |
| **CommandLineParser** | CLI argument parsing |
---

## Pagsasama ng Cloud at Azure
| Serbisyo | Layunin |
|---------|---------|
| **Azure Function** | Walang server |
| **Azure SDK para sa .NET** | Lahat ng serbisyo ng Azure |
| **AWS SDK para sa .NET** | Mga serbisyo ng AWS |
| **Google Cloud .NET** | Mga serbisyo ng GCP |
| **Azure Cosmos DB** | database ng NoSQL |
| **Azure Service Bus** | Pagmemensahe |
| **Azure Key Vault** | Pamamahala ng mga lihim |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Makasarili** | Mga Bundle .NET runtime |
| **nakadepende sa framework** | Nangangailangan ng .NET na naka-install |
| **Single-file publish** | `dotnet publish /p:PublishSingleFile=true`|
| **Native AOT** | `PublishAot=true`(walang JIT na kailangan) |
| **Docker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Serbisyo ng Azure App** | Pag-deploy ng PaaS |
| **AWS Lambda** | Walang server |
| **IIS** | Windows hosting |
| **Kestrel** | Built-in na cross-platform na web server |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Buod
Ang C# at .NET ay nag-aalok ng isa sa mga pinaka-produktibong ecosystem. Ang karaniwang stack ay: **.NET 8+** bilang runtime, **ASP.NET Core** para sa web, **Entity Framework Core** o **Dapper** para sa pag-access ng data, **xUnit + Moq** para sa pagsubok, **Visual Studio** o **Rider** bilang IDE, at **NuGet** para sa mga package. Ang modernong C# na may mga tala, pagtutugma ng pattern, mga nullable na uri ng sanggunian, at kaunting mga API ay maikli at nagpapahayag. Ang **Native AOT** compilation ay nagbibigay-daan sa napakabilis na pagsisimula at maliliit na binary. Ang ecosystem ay mahusay sa enterprise, cloud (Azure), pagbuo ng laro (Unity, Godot), at mga cross-platform na application.