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
# Visual Basic — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie Visual Basic (.NET).
---

## Wersje Visual Basic
| Wersja | Notatki |
|--------|-------|
| **VB.NET (Visual Basic 2022)** | Aktualny, .NET 8+ |
| **VB6** | Klasyczny Visual Basic (starsza wersja) |
| **VBA** | Visual Basic dla aplikacji (biuro) |
| **Skrypt VB** | Język skryptowy (przestarzały) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Narzędzia do tworzenia
| Narzędzie | Cel |
|------|-------------|
| **Dotnet CLI** | Kompiluj, testuj, publikuj .NET |
| **MSBuild** | Zbuduj silnik |
| **Studio wizualne** | Pełne IDE |
| **NuGet** | Zarządzanie pakietami |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **ASP.NET Core** | Pełny stos | API, MVC, strony Razor |
| **Minimalne API** | Lekki | Proste API |
| **Blazor** | Interfejs sieciowy | Interfejs użytkownika oparty na komponentach |
| **SygnałR** | W czasie rzeczywistym | WebSockety |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **Rdzeń Entity Framework** | Pełny ORM |
| **Wytworny** | Mikro-ORM |
| **ADO.NET** | Dostęp do danych niskiego poziomu |
| **OleDb** | Dostęp do starszych danych |
| **Dane MySql** | Złącze MySQL |
| **Npgsql** | Złącze PostgreSQL |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **xJednostka** | Struktura testowa |
| **NUjednostka** | Struktura testowa |
| **MTest** | Struktura testowa Microsoft |
| **Moq** | Kpiąco |
| **NZastępstwo** | Kpiąco |
| **Płynne twierdzenia** | Płynne twierdzenia |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **Analizatory Roslyn** | Wbudowana analiza |
| **Analizator sonaru** | Zasady SonarQube |
| **format dotnet** | Formatowanie kodu |
| **Konfiguracja edytora** | Spójny styl |
| **SonarQube** | Platforma jakości kodu |
---

## Pulpit (WinForms / WPF)
| Ramy | Cel |
|---------------|--------|
| **WinForm** | Klasyczne formularze Windows |
| **WPF** | Nowoczesny interfejs użytkownika systemu Windows (XAML) |
| **MAUI** | Wieloplatformowy (następca Xamarin) |
| **Awalonia** | Wieloplatformowy podobny do WPF |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **System.Text.Json** | Serializacja JSON |
| **Newtonsoft.Json** | JSON (starsza wersja) |
| **Serylog** | Rejestrowanie |
| **Polly** | Polityka odporności |
| **AutoMaper** | Mapowanie obiektów |
| **Płynna weryfikacja** | Walidacja |
| **Transport zbiorowy** | Autobus wiadomości |
| **Zawieszenie** | Zadania w tle |
| **Spectre.Konsola** | Interfejs konsoli |
---

## Automatyzacja biura (VBA)
| Technologia | Cel |
|------------|------------|
| **Excel VBA** | Automatyzacja Excela |
| **Word VBA** | Automatyzacja słów |
| **Dostęp do VBA** | Automatyzacja dostępu |
| **Outlook VBA** | Automatyzacja Outlooka |
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

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Studio wizualne** | Pełne IDE VB.NET (Społeczność/Pro/Enterprise) |
| **Kod VS** | Lekki z rozszerzeniami .NET |
| **Edytor VBA** | Wbudowane w aplikacje pakietu Office |
| **Jeździec** | JetBrains (ograniczona obsługa VB) |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Samodzielny** | Pakiety środowiska uruchomieniowego .NET |
| **Zależne od platformy** | Wymaga zainstalowanej platformy .NET |
| **Pojedynczy plik** | `PublishSingleFile`|
| **Doker** | Kontenerowy |
| **MSI / ClickOnce** | Instalator Windows |
| **Usługa aplikacji Azure** | Hosting w chmurze |
| **IIS** | Hosting Windowsa |
---

## Streszczenie
Ekosystem Visual Basic współdzieli ogromną infrastrukturę .NET. Standardowy stos to: **.NET 8+** jako środowisko wykonawcze, **Visual Studio** jako IDE, **ASP.NET Core** dla Internetu, **Entity Framework Core** lub **Dapper** dla dostępu do danych, **xUnit** dla testowania i **NuGet** dla pakietów. VB.NET jest idealnym rozwiązaniem dla programistów znających składnię BASIC, którzy potrzebują dostępu do ekosystemu .NET. **VBA** pozostaje niezbędny do automatyzacji pakietu Office — miliony użytkowników biznesowych polega na makrach Excela i Accessa. Ekosystem najlepiej nadaje się do aplikacji komputerowych systemu Windows, automatyzacji pakietu Office i aplikacji biznesowych dla przedsiębiorstw.