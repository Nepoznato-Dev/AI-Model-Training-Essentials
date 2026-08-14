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
# C# — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie C#/.NET.
---

## Zestaw SDK i zestaw narzędzi .NET
| Narzędzie | Cel |
|------|-------------|
| **Dotnet CLI** | Kompiluj, uruchamiaj, testuj, publikuj |
| **MSBuild** | Podstawowy silnik kompilacji |
| **NuGet CLI** | Zarządzanie pakietami |
| **format dotnet** | Formatowanie kodu |
| **dotnet-ef** | Narzędzia Entity Framework |
| **dotnet-przestarzały** | Znajdź nieaktualne pakiety |
| **skrypt dotnet** | Uruchom skrypty C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Środowiska wykonawcze i implementacje
| Czas wykonania | Notatki |
|--------|-------|
| **.NET 8/9** | Aktualny LTS/STS, wieloplatformowy |
| **.NET Framework** | Tylko system Windows, starsza wersja (4.8.x) |
| **Mono** | .NET Framework typu open source (Xamarin) |
| **Jedność (IL2CPP/Mono)** | Czas działania silnika gry |
| **Godot (.NET)** | Silnik gry z obsługą C# |
---

## Zarządzanie pakietami
| Źródło | Cel |
|------------|--------|
| **NuGet.org** | Oficjalny rejestr pakietów |
| **dotnet dodaj pakiet** | Instalacja pakietu CLI |
| **Odniesienie do pakietu** | Nowoczesny format .csproj |
| **Prywatne kanały** | Artefakty platformy Azure, pakiety GitHub, MyGet |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **ASP.NET Core** | Sieć z pełnym stosem | API, MVC, Blazor |
| **Minimalne API** | Lekki | Proste API |
| **Serwer Blazor** | Interaktywny interfejs użytkownika | SPA renderowane przez serwer |
| **Blazor WebAssembly** | Po stronie klienta | SPA oparte na przeglądarce |
| **gRPC** | RPC | Usługi o wysokiej wydajności |
| **SygnałR** | W czasie rzeczywistym | WebSockets, push |
| **ODane** | Rozszerzenia REST | Zapytania API |
| **FastEndpoints** | Struktura API | Szybki, minimalny szablon |
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

## Baza danych i ORM
| Technologia | Wpisz |
|------------|------|
| **Rdzeń Entity Framework** | Pełny ORM, migracje |
| **Wytworny** | Micro-ORM, surowy SQL |
| **NHibernacja** | Dojrzały ORM |
| **FreeSql** | Lekki ORM |
| **Kuna** | Dokument PostgreSQL DB |
| **StackExchange.Redis** | Klient Redisa |
| **Sterownik MongoDB.** | Klient MongoDB |
| **Npgsql** | Sterownik PostgreSQL |
| **Łącznik MySql** | Sterownik MySQL |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **xJednostka** | Najpopularniejszy framework testowy |
| **NUjednostka** | Klasyczny framework testowy |
| **MTest** | Framework testowy Microsoftu |
| **Moq** | Kpiąca biblioteka |
| **NZastępstwo** | Przyjazne kpiny |
| **Płynne twierdzenia** | Płynne twierdzenia |
| **Powinienem** | Czytelne twierdzenia |
| **Błąd** | Fałszywe generowanie danych |
| **Autoustawianie** | Automatyzacja danych testowych |
| **Kontenery testowe** | Testy integracyjne oparte na Dockerze |
| **BenchmarkDotNet** | Mikrobenchmarking |
| **narzuta** | Pokrycie kodu |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **Analizatory Roslyn** | Wbudowana analiza kodu |
| **SonarAnalyzer.CSharp** | Zasady SonarQube |
| **Stylowy policjant** | Egzekwowanie stylu kodowania |
| **format dotnet** | Formatowanie kodu |
| **Konfiguracja edytora** | Spójność między redaktorami |
| **SonarQube / SonarCloud** | Platforma jakości kodu |
| **Wyostrzanie** | Analiza JetBrains + refaktoryzacja |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Studio wizualne** | W pełni funkcjonalne środowisko IDE systemu Windows (Społeczność/Pro/Enterprise) |
| **Jeździec** | Wieloplatformowe IDE JetBrains C# |
| **Kod VS + zestaw deweloperski C#** | Lekkie, rozszerzenie Microsoft |
| **Visual Studio dla komputerów Mac** | Będąc na emeryturze (użyj Ridera lub VS Code) |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **System.Text.Json** | Wbudowana serializacja JSON |
| **Newtonsoft.Json** | Starsza wersja JSON (wciąż szeroko stosowana) |
| **Serylog** | Logowanie strukturalne |
| **NLog** | Struktura rejestrowania |
| **Polly** | Zasady dotyczące odporności i ponownych prób |
| **MediatR** | Wzór mediatora (CQRS) |
| **AutoMaper** | Mapowanie obiekt-obiekt |
| **Płynna weryfikacja** | Biblioteka walidacyjna |
| **Transport zbiorowy** | Magistrala komunikatów (RabbitMQ, Azure SB) |
| **Zawieszenie** | Przetwarzanie zadań w tle |
| **Kwarc.NET** | Planowanie pracy |
| **Spectre.Konsola** | Piękne aplikacje konsolowe |
| **Parser Linii Poleceń** | Analiza argumentów CLI |
---

## Integracja z chmurą i platformą Azure
| Usługa | Cel |
|--------|---------|
| **Funkcje platformy Azure** | Bezserwerowy |
| **Azure SDK dla .NET** | Wszystkie usługi Azure |
| **SDK AWS dla .NET** | Usługi AWS |
| **Google Cloud .NET** | Usługi GCP |
| **Azure Cosmos DB** | Baza danych NoSQL |
| **Azure Service Bus** | Wiadomości |
| **Azure Key Vault** | Zarządzanie tajemnicami |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Samodzielny** | Pakiety środowiska uruchomieniowego .NET |
| **Zależne od platformy** | Wymaga zainstalowanej platformy .NET |
| **Publikacja w jednym pliku** | `dotnet publish /p:PublishSingleFile=true`|
| **Natywny AOT** | `PublishAot=true`(nie jest potrzebny JIT) |
| **Doker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Usługa aplikacji Azure** | Wdrożenie PaaS |
| **AWS Lambda** | Bezserwerowy |
| **IIS** | Hosting Windowsa |
| **Pustułka** | Wbudowany wieloplatformowy serwer WWW |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Streszczenie
C# i .NET oferują jeden z najbardziej produktywnych ekosystemów. Standardowy stos to: **.NET 8+** jako środowisko wykonawcze, **ASP.NET Core** dla Internetu, **Entity Framework Core** lub **Dapper** dla dostępu do danych, **xUnit + Moq** dla testowania, **Visual Studio** lub **Rider** jako IDE i **NuGet** dla pakietów. Nowoczesny język C# z rekordami, dopasowywaniem wzorców, typami referencyjnymi dopuszczającymi wartość null i minimalnymi interfejsami API jest zwięzły i wyrazisty. **Natywna kompilacja AOT** umożliwia niesamowicie szybkie uruchamianie i małe pliki binarne. Ekosystem wyróżnia się w zastosowaniach korporacyjnych, chmurowych (Azure), tworzeniu gier (Unity, Godot) i aplikacjach wieloplatformowych.