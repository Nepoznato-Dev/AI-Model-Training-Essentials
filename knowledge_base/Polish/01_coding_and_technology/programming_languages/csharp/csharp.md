<!--
---
# Metadata
title: "C#"
description: "Comprehensive reference for the C# programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [csharp, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# C#
C# (wymawiane „C-sharp”) to nowoczesny, obiektowy, bezpieczny język programowania opracowany przez firmę Microsoft pod kierownictwem Andersa Hejlsberga i wydany po raz pierwszy w 2002 roku. Działa na platformie .NET i został zaprojektowany tak, aby połączyć moc C++ z produktywnością Visual Basic. Obecnie C# to wszechstronny, wieloplatformowy język używany w aplikacjach internetowych (ASP.NET), oprogramowaniu komputerowym (Windows), tworzeniu gier (Unity), aplikacjach mobilnych (MAUI), usługach w chmurze (Azure) i nie tylko.
C# stale wchłania najlepsze pomysły z innych języków — LINQ, async/await, rekordy, dopasowywanie wzorców — co czyni go jednym z najbardziej bogatych w funkcje i przyjaznych dla programistów dostępnych języków.
---

## Dlaczego C# ma znaczenie
- **Silnik gier Unity**: Podstawowy język Unity, najpopularniejszego na świecie silnika gier według liczby programistów.
- **Rozwój korporacyjny**: ASP.NET Core to jeden z najszybszych dostępnych frameworków internetowych (niezmiennie zajmuje czołowe miejsca w benchmarkach TechEmpower).
- **Międzyplatformowy**: .NET 5+ działa w systemach Windows, macOS i Linux. Już nie tylko dla systemu Windows.
- **Produktywność**: Doskonała obsługa IDE (Visual Studio, Rider), mocny system typów i nowoczesne funkcje składni.
- **async/await pionier**: C# wprowadził async/await w 2012 r. — lata przed przyjęciem tego wzorca w innych językach.
- **LINQ**: Zapytanie zintegrowane z językiem umożliwia pisanie zapytań przypominających SQL bezpośrednio w języku C# względem dowolnego źródła danych.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Skojarzenie Windows** | Historycznie związany z systemem Windows; percepcja pozostaje w tyle za rzeczywistością | .NET 6+ jest w pełni wieloplatformowy |
| **Mniejszy ekosystem niż Java** | Mniej bibliotek innych firm niż Maven/PyPI | NuGet rośnie; wiele bibliotek Java ma odpowiedniki w języku C# |
| **Rzadziej spotykane w startupach** | Bardziej popularny w przedsiębiorstwach niż w Dolinie Krzemowej | Go, Rust, Node.js dla mikrousług natywnych w chmurze |
| **Telefon komórkowy (MAUI)** | Xamarin/MAUI jest mniej dojrzały niż natywny lub Flutter | Użyj natywnego Swift/Kotlin lub Flutter dla złożonych aplikacji mobilnych |
| **GUI Linuksa** | Ograniczone natywne opcje GUI w systemie Linux | Użyj internetowych interfejsów użytkownika (Blazor) lub Avalonia |
---

## Podstawy składni
### Podstawowa struktura
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace MyApp;

// Top-level statements (C# 9+) — no Main method needed for simple programs
Console.WriteLine("Hello, World!");

var name = "Alice";
var age = 30;
var scores = new List<double> { 9.5, 8.0, 7.5 };

// String interpolation
Console.WriteLine($"Name: {name}, Age: {age}, Average: {scores.Average():F1}");
```

### Programowanie obiektowe
```csharp
public abstract class Animal
{
    public string Name { get; }
    protected Animal(string name) => Name = name;
    public abstract string Speak();
}

public class Dog : Animal
{
    public Dog(string name) : base(name) { }
    public override string Speak() => $"{Name} says woof";
}

public interface ISerializable
{
    string ToJson();
}

public class User : ISerializable, IComparable<User>
{
    public string Name { get; init; }
    public int Age { get; init; }
    
    public string ToJson() => $"{{\"name\":\"{Name}\",\"age\":{Age}}}";
    public int CompareTo(User? other) => Age.CompareTo(other?.Age ?? 0);
}
```

### Rekordy (C# 9+) — Niezmienne typy danych
```csharp
public record Point(double X, double Y)
{
    public double DistanceTo(Point other) =>
        Math.Sqrt(Math.Pow(X - other.X, 2) + Math.Pow(Y - other.Y, 2));
}

var p1 = new Point(3.0, 4.0);
var p2 = new Point(0.0, 0.0);
Console.WriteLine(p1.DistanceTo(p2));  // 5.0

var p3 = p1 with { X = 6.0 };  // New record: Point(6.0, 4.0)
Console.WriteLine(p1 == p3);   // False (different X)
```

### LINQ — zapytanie zintegrowane z językiem
```csharp
var users = new List<User>
{
    new User { Name = "Alice", Age = 30 },
    new User { Name = "Bob", Age = 25 },
    new User { Name = "Charlie", Age = 35 },
};

// Method syntax
var adults = users.Where(u => u.Age >= 28).OrderBy(u => u.Name).Select(u => u.Name).ToList();

// Query syntax (SQL-like)
var query = from u in users where u.Age >= 28 orderby u.Name select u.Name;

// Grouping and aggregation
var byAgeGroup = users.GroupBy(u => u.Age < 30 ? "Under 30" : "30 and over");
var averageAge = users.Average(u => u.Age);
```

### Asynchronizacja/Oczekiwanie
```csharp
public async Task<string> FetchPageAsync(string url)
{
    using var client = new HttpClient();
    return await client.GetStringAsync(url);
}

public async Task FetchAllAsync(IEnumerable<string> urls)
{
    var tasks = urls.Select(url => FetchPageAsync(url));
    var results = await Task.WhenAll(tasks);
    foreach (var result in results)
        Console.WriteLine($"Fetched {result.Length} characters");
}

public async Task DownloadAsync(string url, CancellationToken ct)
{
    using var client = new HttpClient();
    var data = await client.GetByteArrayAsync(url, ct);
    await File.WriteAllBytesAsync("download.bin", data, ct);
}
```

### Dopasowywanie wzorców (C# 7-13)
```csharp
public string Describe(object obj) => obj switch
{
    int n when n > 0 => $"Positive integer: {n}",
    int n => $"Non-positive integer: {n}",
    string s => $"String of length {s.Length}",
    null => "Nothing",
    _ => "Something else"
};

// Property patterns
public decimal CalculateDiscount(Customer c) => c switch
{
    { IsVip: true, TotalSpent: > 10000 } => 0.20m,
    { IsVip: true } => 0.10m,
    { TotalSpent: > 5000 } => 0.05m,
    _ => 0m
};

// List patterns (C# 11+)
public string Classify(int[] numbers) => numbers switch
{
    [] => "Empty",
    [var single] => $"Single: {single}",
    [var first, .., var last] => $"First: {first}, Last: {last}",
};
```

---

## Zaawansowana składnia i wzorce
### Ogólne
```csharp
// Generic class with constraints
public class Repository<T> where T : class, IEntity
{
    private readonly List<T> _items = new();
    
    public void Add(T item) => _items.Add(item);
    public T? FindById(int id) => _items.FirstOrDefault(i => i.Id == id);
    public IEnumerable<T> Find(Func<T, bool> predicate) => _items.Where(predicate);
}

// Generic constraints
public T Max<T>(T a, T b) where T : IComparable<T> => a.CompareTo(b) >= 0 ? a : b;

// Covariance and contravariance
public interface IProducer<out T>  // covariant — can return T or derived
{
    T Produce();
}

public interface IConsumer<in T>  // contravariant — can accept T or base
{
    void Consume(T item);
}
```

### Delegaty, zdarzenia i wyrażenia lambda
```csharp
// Delegate — type-safe function pointer
public delegate double MathOperation(double a, double b);

MathOperation add = (a, b) => a + b;
MathOperation multiply = (a, b) => a * b;
Console.WriteLine(add(3, 5));       // 8
Console.WriteLine(multiply(3, 5));  // 15

// Built-in delegates
Func<int, int, int> addFunc = (a, b) => a + b;
Action<string> print = s => Console.WriteLine(s);
Predicate<int> isPositive = n => n > 0;

// Events — type-safe pub/sub
public class Button
{
    public event EventHandler<ClickEventArgs>? Clicked;
    
    public void OnClick() => Clicked?.Invoke(this, new ClickEventArgs(DateTime.Now));
}

public class ClickEventArgs : EventArgs
{
    public DateTime Timestamp { get; }
    public ClickEventArgs(DateTime ts) => Timestamp = ts;
}

// Usage
var button = new Button();
button.Clicked += (sender, args) => Console.WriteLine($"Clicked at {args.Timestamp}");
button.OnClick();
```

### Niestandardowe hierarchie wyjątków
```csharp
public class AppException : Exception
{
    public string Code { get; }
    public AppException(string message, string code = "UNKNOWN")
        : base(message) { Code = code; }
}

public class ValidationException : AppException
{
    public string Field { get; }
    public ValidationException(string field, string message)
        : base($"Validation failed for '{field}': {message}", "VALIDATION")
    { Field = field; }
}

public class NotFoundException : AppException
{
    public NotFoundException(string resource, object id)
        : base($"{resource} not found: {id}", "NOT_FOUND") { }
}

// Usage
try { throw new ValidationException("email", "must contain @"); }
catch (ValidationException ex) { Console.WriteLine($"Bad input: {ex.Field}"); }
catch (AppException ex) { Console.WriteLine($"Error [{ex.Code}]: {ex.Message}"); }
```

### Przeciążenie operatora
```csharp
public record struct Vector2D(double X, double Y)
{
    public static Vector2D operator +(Vector2D a, Vector2D b) => new(a.X + b.X, a.Y + b.Y);
    public static Vector2D operator -(Vector2D a, Vector2D b) => new(a.X - b.X, a.Y - b.Y);
    public static Vector2D operator *(Vector2D v, double s) => new(v.X * s, v.Y * s);
    public static Vector2D operator *(double s, Vector2D v) => v * s;
    public static Vector2D operator -(Vector2D v) => new(-v.X, -v.Y);
    
    public double Magnitude => Math.Sqrt(X * X + Y * Y);
    
    public static implicit operator (double X, double Y)(Vector2D v) => (v.X, v.Y);
}

var v1 = new Vector2D(3, 4);
var v2 = new Vector2D(1, 2);
Console.WriteLine(v1 + v2);        // (4, 6)
Console.WriteLine(v1 * 2);         // (6, 8)
Console.WriteLine(v1.Magnitude);   // 5
```

---

## Współbieżność i równoległość
### asynchroniczne/czekające elementy wewnętrzne
```csharp
// The state machine behind async/await
// When you write async/await, the compiler generates a state machine
// that suspends and resumes the method at each await point.

// Parallel async with structured concurrency
public async Task ProcessBatchAsync(IEnumerable<string> urls)
{
    using var semaphore = new SemaphoreSlim(10);  // Limit concurrency to 10
    var tasks = urls.Select(async url =>
    {
        await semaphore.WaitAsync();
        try
        {
            using var client = new HttpClient();
            var data = await client.GetStringAsync(url);
            Console.WriteLine($"Fetched {data.Length} chars from {url}");
        }
        finally
        {
            semaphore.Release();
        }
    });
    await Task.WhenAll(tasks);
}

// Channels — producer/consumer pattern
public async Task ProcessWithChannel()
{
    var channel = Channel.CreateBounded<string>(new BoundedChannelOptions(100)
    {
        FullMode = BoundedChannelFullMode.Wait
    });

    // Producer
    _ = Task.Run(async () =>
    {
        for (int i = 0; i < 1000; i++)
        {
            await channel.Writer.WriteAsync($"item-{i}");
            await Task.Delay(10);
        }
        channel.Writer.Complete();
    });

    // Consumer
    await foreach (var item in channel.Reader.ReadAllAsync())
    {
        Console.WriteLine($"Processing: {item}");
    }
}
```

### Równoległy LINQ i biblioteka równoległa zadań
```csharp
// PLINQ — parallel data processing
var numbers = Enumerable.Range(1, 10_000_000);
var primes = numbers.AsParallel()
    .Where(n => IsPrime(n))
    .ToList();

// Parallel.ForEach — CPU-bound work across cores
Parallel.ForEach(files, new ParallelOptions { MaxDegreeOfParallelism = 4 }, file =>
{
    var content = File.ReadAllText(file);
    ProcessContent(content);
});

// ValueTask — allocation-free async for hot paths
public async ValueTask<int> GetCountAsync()
{
    if (_cache != null) return _cache.Count;  // Synchronous fast path
    return await LoadFromDatabaseAsync();      // Async slow path
}
```

---

## Konfiguracja projektu i budowanie systemu
### Struktura projektu
```
MyCSharpProject/
├── src/
│   ├── MyProject/
│   │   ├── MyProject.csproj
│   │   ├── Program.cs
│   │   ├── Models/
│   │   ├── Services/
│   │   └── Controllers/
│   └── MyProject.Tests/
│       ├── MyProject.Tests.csproj
│       └── Services/
├── MyProject.sln
├── .editorconfig
├── Directory.Build.props
├── .github/workflows/ci.yml
└── README.md
```

### Plik .csproj
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.Extensions.Logging" Version="8.0.0" />
  </ItemGroup>
</Project>
```

### Testowanie z xUnit
```csharp
public class UserServiceTests
{
    private readonly Mock<IUserRepository> _mockRepo;
    private readonly UserService _service;

    public UserServiceTests()
    {
        _mockRepo = new Mock<IUserRepository>();
        _service = new UserService(_mockRepo.Object);
    }

    [Fact]
    public void Create_ValidData_ReturnsUser()
    {
        _mockRepo.Setup(r => r.Save(It.IsAny<User>()))
            .ReturnsAsync(new User { Id = 1, Name = "Alice" });

        var user = _service.Create("Alice", "alice@example.com");

        Assert.Equal("Alice", user.Name);
        _mockRepo.Verify(r => r.Save(It.IsAny<User>()), Times.Once);
    }

    [Theory]
    [InlineData("")]
    [InlineData("  ")]
    [InlineData(null)]
    public void Create_InvalidName_Throws(string? name)
    {
        Assert.Throws<ArgumentException>(() => _service.Create(name!, "a@b.com"));
    }
}
```

### Rurociąg CI/CD
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: "8.0.x"
      - run: dotnet restore
      - run: dotnet build --no-restore
      - run: dotnet test --no-build --verbosity normal
      - run: dotnet publish src/MyProject -c Release -o publish
```

---

## Interoperacyjność
### P/Invoke — wywoływanie bibliotek C
```csharp
using System.Runtime.InteropServices;

// Call C functions from native libraries
[DllImport("libc", SetLastError = true)]
private static extern int getpid();

[DllImport("user32.dll", CharSet = CharSet.Unicode)]
private static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);

// Modern approach — LibraryImport (C# 12+, source-generated)
[LibraryImport("nativeLib.dll")]
private static partial int Add(int a, int b);

Console.WriteLine($"Process ID: {getpid()}");
```

### Współpraca C++/CLI
```csharp
// Using SWIG to wrap C++ for C#
// 1. Define interface file
// 2. Run SWIG to generate C# wrapper
// 3. Use the generated C# classes directly

// Example: wrapping a C++ class
// geometry.h: class Circle { public: double Area() const; };
// After SWIG:
// var circle = new Circle(5.0);
// Console.WriteLine(circle.Area());
```

---

## Wzorce projektowe
### Wzorzec konstruktora (Fluent API)
```csharp
public class HttpRequest
{
    public string Method { get; init; } = "GET";
    public string Url { get; init; } = "";
    public Dictionary<string, string> Headers { get; init; } = new();
    public string? Body { get; init; }
}

public class HttpRequestBuilder
{
    private string _method = "GET";
    private string _url = "";
    private readonly Dictionary<string, string> _headers = new();
    private string? _body;

    public HttpRequestBuilder Method(string m) { _method = m; return this; }
    public HttpRequestBuilder Url(string u) { _url = u; return this; }
    public HttpRequestBuilder Header(string k, string v) { _headers[k] = v; return this; }
    public HttpRequestBuilder Body(string b) { _body = b; return this; }
    public HttpRequest Build() => new() { Method = _method, Url = _url, Headers = _headers, Body = _body };
}

var request = new HttpRequestBuilder()
    .Method("POST").Url("/api/users")
    .Header("Content-Type", "application/json")
    .Body("{\"name\":\"Alice\"}")
    .Build();
```

### Wzorzec strategii z delegatami
```csharp
public class DataProcessor
{
    private readonly Func<string, string> _transform;

    public DataProcessor(Func<string, string> transform) => _transform = transform;

    public string Process(string input) => _transform(input);
}

// Usage — swap strategies with lambdas
var upper = new DataProcessor(s => s.ToUpper());
var reversed = new DataProcessor(s => new string(s.Reverse().ToArray()));

Console.WriteLine(upper.Process("hello"));     // "HELLO"
Console.WriteLine(reversed.Process("hello"));  // "olleh"
```

---

## Wydajność i optymalizacja
### Narzędzia do profilowania
```bash
# dotnet-trace — CPU and event tracing
dotnet tool install -g dotnet-trace
dotnet-trace collect --process-id <PID>

# dotnet-counters — real-time performance counters
dotnet-counters monitor --process-id <PID>

# BenchmarkDotNet — micro-benchmarking
dotnet add package BenchmarkDotNet
```

```csharp
// BenchmarkDotNet example
[MemoryDiagnoser]
public class StringBenchmarks
{
    [Benchmark(Baseline = true)]
    public string Concatenation()
    {
        string result = "";
        for (int i = 0; i < 100; i++) result += i.ToString();
        return result;
    }

    [Benchmark]
    public string StringBuilder()
    {
        var sb = new StringBuilder();
        for (int i = 0; i < 100; i++) sb.Append(i);
        return sb.ToString();
    }
}
// Run: dotnet run -c Release
```

---

## Zastosowanie
### Plik Dockera
```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish src/MyProject -c Release -o /app

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app .
EXPOSE 8080
ENTRYPOINT ["dotnet", "MyProject.dll"]
```

### Wdrożenie specyficzne dla platformy
```bash
# Self-contained deployment (no .NET runtime needed on target)
dotnet publish -c Release -r linux-x64 --self-contained true

# Single-file executable
dotnet publish -c Release -r win-x64 -p:PublishSingleFile=true

# Azure App Service
az webapp up --name my-app --runtime DOTNET:8.0

# AWS Lambda
dotnet lambda deploy-function my-function
```

---

## Ekosystem .NET
### Frameworki i platformy
| Ramy | Domena | Opis |
|---------------|--------|------------|
| **ASP.NET Core** | Sieć | Wysokowydajna platforma internetowa dla interfejsów API i aplikacji internetowych |
| **Blazor** | Sieć (frontend) | Twórz interaktywne interfejsy internetowe za pomocą języka C# zamiast JavaScript |
| **Rdzeń Entity Framework** | ORMO | Dostęp do bazy danych za pomocą LINQ; migracje oparte na kodzie |
| **Jedność** | Gry | Najpopularniejszy na świecie silnik gier (skrypty C#) |
| **.NET MAUI** | Telefon komórkowy/komputer stacjonarny | Aplikacje wieloplatformowe na iOS, Android, macOS, Windows |
| **Awalonia** | Pulpit | Wieloplatformowy interfejs użytkownika dla komputerów stacjonarnych (jak WPF dla wszystkich platform) |
### Zarządzanie kompilacją i pakietami
| Narzędzie | Cel |
|------|-------------|
| **Dotnet CLI** | Kompiluj, uruchamiaj, testuj, publikuj z wiersza poleceń |
| **NuGet** | Menedżer pakietów |
| **MSBuild** | Podstawowy system kompilacji |
| **Studio wizualne / Jeździec** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## Wersje językowe C#
| Wersja | Rok | Kluczowe funkcje |
|--------|------|------------|
| C#7 | 2017 | Dopasowywanie wzorców, krotki, zmienne `out`, funkcje lokalne |
| C#8 | 2019 | Typy referencyjne dopuszczające wartość null, wyrażenia `switch`, strumienie asynchroniczne |
| C#9 | 2020 | **Rekordy**, wyciągi najwyższego poziomu, właściwości`init`|
| C#10 | 2021 | Struktury rekordów, globalne`using`, przestrzenie nazw o zasięgu pliku |
| C#11 | 2022 | Surowe literały łańcuchowe, wzorce list, elementy `required`, ogólna matematyka |
| C#12 | 2023 | Konstruktory podstawowe, wyrażenia kolekcji, tablice wbudowane |
| C#13 | 2024 |  Kolekcje `params`, nowe typy zamków, przęsła najwyższej klasy |
---

## Kiedy używać C#
| Scenariusz | Dlaczego C# | Lepsza alternatywa |
|---------|--------|--------------------------------|
| Tworzenie gier (Unity) | Standardowy język skryptowy Unity | -- |
| Backendy internetowe dla przedsiębiorstw | ASP.NET Core jest szybki, dojrzały i dobrze obsługiwany | Java (rozruch wiosenny) |
| Aplikacje komputerowe dla systemu Windows | WPF, WinForm, WinUI są dojrzałe | -- |
| Pulpit wieloplatformowy | Avalonia lub MAUI | Elektron (internetowy) |
| Interfejs WWW (Blazor) | Pełny stos C# — nie wymaga JavaScript | React/Vue/Angular dla bogatszych ekosystemów SPA |
| Usługi w chmurze (Azure) | Głęboka integracja z platformą Azure | -- |
| Aplikacje mobilne (MAUI) | Wieloplatformowy z C# | Flutter, React Native lub natywny Swift/Kotlin |
| AI/ML | Możliwe z ML.NET | Python (zdecydowanie preferowany) |
| Narzędzia/skrypty CLI | Możliwe, ale szczegółowe | Idź, Rust, Python |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między`class`i`record`w języku C#?
**A:**`class`jest domyślnie typem referencyjnym z modyfikowalnymi właściwościami — dwie zmienne mogą odwoływać się do tego samego obiektu.`record`(C# 9+) to typ referencyjny z równością opartą na wartościach — dwa rekordy z tymi samymi danymi są uważane za równe. Rekordy mają właściwości tylko init, wbudowaną`ToString`i obsługują wyrażenia`with`dla nieniszczących mutacji. Użyj rekordów dla nośników danych (DTO, obiekty wartości); używaj klas dla jednostek bogatych w zachowania z tożsamością.
```csharp
// Class — reference equality, mutable
public class User { public string Name { get; set; } public int Age { get; set; } }
var u1 = new User { Name = "Alice", Age = 30 };
var u2 = u1;  // Same reference
u2.Name = "Bob";
Console.WriteLine(u1.Name);  // "Bob" — both point to same object

// Record — value equality, immutable by default
public record Person(string Name, int Age);
var p1 = new Person("Alice", 30);
var p2 = p1 with { Name = "Bob" };  // New record, p1 unchanged
Console.WriteLine(p1.Name);          // "Alice"
Console.WriteLine(p1 == new Person("Alice", 30));  // true — value equality
```

### P2: Jak wewnętrznie działają funkcje async/await i `Task`?
**A:**`async/await`to cukier syntaktyczny na maszynie stanu wygenerowanej przez kompilator. Kiedy`await`a`Task`metoda jest dzielona w punkcie oczekiwania: wszystko wcześniej jest wykonywane synchronicznie, a następnie pozostała część jest rejestrowana jako kontynuacja. Wątek może zająć się inną pracą. `Task<T>`reprezentuje wartość przyszłą. `ValueTask<T>`to alternatywa struktury dla gorących ścieżek, która pozwala uniknąć alokacji sterty, gdy wynik jest już dostępny.
```csharp
// Async method — returns Task<T>
public async Task<User> GetUserAsync(string id)
{
    using var client = new HttpClient();
    var response = await client.GetAsync($"/api/users/{id}");
    response.EnsureSuccessStatusCode();
    return await response.Content.ReadFromJsonAsync<User>();
}

// Concurrent execution
var userTask = GetUserAsync("1");
var postsTask = GetPostsAsync("1");
var user = await userTask;
var posts = await postsTask;
// Or: await Task.WhenAll(userTask, postsTask);

// ValueTask for high-performance scenarios
public ValueTask<int> GetCachedCount() =>
    _cached.HasValue ? new ValueTask<int>(_cached.Value) : new ValueTask<int>(ComputeCountAsync());
```

### P3: Jakie są metody rozszerzania i kiedy należy ich używać?
**O:** Metody rozszerzające dodają metody do istniejących typów bez ich modyfikowania. Są to metody statyczne w klasie statycznej, ze słowem kluczowym`this`na pierwszym parametrze. Umożliwiają płynny, łańcuchowy interfejs API. Użyj ich, aby dodać metody narzędziowe do typów, których nie posiadasz (takich jak`string`lub`IEnumerable<T>`). Unikaj ich nadużywania — mogą utrudniać odkrycie kodu.
```csharp
public static class StringExtensions
{
    public static string Truncate(this string s, int maxLength) =>
        s.Length <= maxLength ? s : s[..maxLength] + "...";

    public static bool IsEmail(this string s) =>
        s.Contains('@') && s.Contains('.');
}

// Usage — looks like a native method
"Hello, World!".Truncate(8);  // "Hello..."
"test@example.com".IsEmail();  // true

// LINQ is built entirely on extension methods
var adults = people.Where(p => p.Age >= 18).OrderBy(p => p.Name).ToList();
```

### P4: Jak działa dopasowywanie wzorców we współczesnym języku C#?
**O:** W języku C# stopniowo dodano skuteczniejsze dopasowywanie wzorców. Wyrażenia przełączników (C# 8), wzorce typów, wzorce właściwości, wzorce relacyjne i wzorce list (C# 11) umożliwiają zwięzłą, ekspresyjną logikę warunkową. Dopasowywanie wzorców zastępuje długie łańcuchy if/else i jest dokładnie sprawdzane przez kompilator.
```csharp
// Switch expression with patterns
string Describe(object obj) => obj switch
{
    null => "nothing",
    int n when n > 0 => $"positive integer: {n}",
    int n => $"non-positive integer: {n}",
    string { Length: 0 } => "empty string",
    string s => $"string of length {s.Length}",
    Person { Age: >= 18 } p => $"adult: {p.Name}",
    Person { Age: < 18 } p => $"minor: {p.Name}",
    int[] { Length: 0 } => "empty array",
    int[] [var first, ..] => $"array starting with {first}",
    _ => $"unknown: {obj.GetType().Name}"
};

// if with pattern matching
if (obj is Person { Age: >= 18 } adult)
{
    Console.WriteLine($"Adult: {adult.Name}");
}
```

### P5: Co to jest wstrzykiwanie zależności w .NET i jak z niego korzystać?
**A:** .NET ma wbudowaną obsługę DI poprzez `Microsoft.Extensions.DependencyInjection`. Rejestrujesz usługi z ich okresami istnienia (Singleton, Scoped, Transient), a kontener wstrzykuje je za pomocą parametrów konstruktora. Singleton: jedna instancja aplikacji. Zakres: jeden na żądanie HTTP. Przejściowe: za każdym razem nowa instancja.
```csharp
// Registration (Program.cs)
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddTransient<IEmailSender, SmtpEmailSender>();
builder.Services.AddScoped<IUserRepository, SqlUserRepository>();
builder.Services.AddSingleton<ICache, InMemoryCache>();

// Consumption via constructor injection
public class UserController : ControllerBase
{
    private readonly IUserRepository _users;
    private readonly IEmailSender _email;

    public UserController(IUserRepository users, IEmailSender email)
    {
        _users = users;
        _email = email;
    }

    [HttpPost]
    public async Task<IActionResult> Create(CreateUserDto dto)
    {
        var user = await _users.CreateAsync(dto);
        await _email.SendWelcomeAsync(user.Email);
        return Ok(user);
    }
}
```

---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zbuduj ogólne repozytorium z buforowaniem
**Opis problemu:** Zaimplementuj ogólny wzorzec repozytorium za pomocą dekoratora, który dodaje buforowanie. Repozytorium powinno obsługiwać operacje CRUD, a dekorator buforowania powinien buforować odczyty i unieważniać zapisy.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) ogólnego interfejsu `IRepository<T>`, (2) konkretnej implementacji (np. w pamięci), (3) dekoratora pamięci podręcznej, który otacza dowolne repozytorium, (4) unieważniania pamięci podręcznej podczas operacji zapisu. Wzorzec dekoratora utrzymuje buforowanie ortogonalne w stosunku do logiki dostępu do danych.
**Krok 2 — Zidentyfikuj podejście:**
- Zdefiniuj`IRepository<T>`za pomocą`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Utwórz `CachingRepository<T>`, który otacza`IRepository<T>`i używa`IMemoryCache`.
- Klucz pamięci podręcznej:`typeof(T).Name:{id}`.
- Podczas operacji zapisu unieważnij wpis w pamięci podręcznej.
**Krok 3 — Wdróż rozwiązanie:**
```csharp
public interface IRepository<T> where T : class
{
    Task<T?> GetByIdAsync(string id);
    Task<IReadOnlyList<T>> GetAllAsync();
    Task AddAsync(T entity);
    Task UpdateAsync(T entity);
    Task DeleteAsync(string id);
}

public interface IEntity { string Id { get; } }

public class CachingRepository<T> : IRepository<T> where T : class, IEntity
{
    private readonly IRepository<T> _inner;
    private readonly IMemoryCache _cache;
    private readonly TimeSpan _ttl;

    public CachingRepository(IRepository<T> inner, IMemoryCache cache,
                             TimeSpan? ttl = null)
    {
        _inner = inner;
        _cache = cache;
        _ttl = ttl ?? TimeSpan.FromMinutes(5);
    }

    public Task<T?> GetByIdAsync(string id)
    {
        var key = $"{typeof(T).Name}:{id}";
        return _cache.GetOrCreateAsync(key, entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = _ttl;
            return _inner.GetByIdAsync(id);
        })!;
    }

    public Task<IReadOnlyList<T>> GetAllAsync() =>
        _cache.GetOrCreateAsync($"{typeof(T).Name}:all", entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = _ttl;
            return _inner.GetAllAsync();
        })!;

    public async Task AddAsync(T entity)
    {
        await _inner.AddAsync(entity);
        Invalidate(entity.Id);
    }

    public async Task UpdateAsync(T entity)
    {
        await _inner.UpdateAsync(entity);
        Invalidate(entity.Id);
    }

    public async Task DeleteAsync(string id)
    {
        await _inner.DeleteAsync(id);
        Invalidate(id);
    }

    private void Invalidate(string id)
    {
        _cache.Remove($"{typeof(T).Name}:{id}");
        _cache.Remove($"{typeof(T).Name}:all");
    }
}
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Oddzielenie obaw: buforowanie jest dekoratorem, a nie mieszanym z repozytorium.
- Rejestracja DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(za pomocą Scrutora).
- Produkcja: użyj`IDistributedCache`(Redis) w scenariuszach z wieloma serwerami i dodaj wzorce odkładania pamięci podręcznej z ochroną `CacheStampede`.
### Problem 2: Zaimplementuj potok oprogramowania pośredniego
**Opis problemu:** Zbuduj potok oprogramowania pośredniego podobny do potoku żądań ASP.NET Core. Każde oprogramowanie pośredniczące może przetworzyć żądanie, wywołać kolejne oprogramowanie pośredniczące i przetworzyć odpowiedź.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) typu`RequestDelegate`reprezentującego potok, (2) oprogramowania pośredniego, które otacza następnego delegata, (3) interfejsu API konstruktora do tworzenia oprogramowania pośredniego. To jest wzorzec Łańcucha Odpowiedzialności wdrożony z delegatami.
**Krok 2 — Zidentyfikuj podejście:**
-`RequestDelegate`to`Func<Context, RequestDelegate, Task>`.
- Każde oprogramowanie pośredniczące otrzymuje kontekst i funkcję `next`.
-`Use`dodaje oprogramowanie pośrednie; `Build`łączy je w jednego delegata.
**Krok 3 — Wdróż rozwiązanie:**
```csharp
public class Context
{
    public string Method { get; init; } = "GET";
    public string Path { get; init; } = "/";
    public Dictionary<string, string> Headers { get; } = new();
    public int StatusCode { get; set; } = 200;
    public string Body { get; set; } = "";
}

public delegate Task RequestDelegate(Context context);

public class PipelineBuilder
{
    private readonly List<Func<RequestDelegate, RequestDelegate>> _middlewares = new();

    public PipelineBuilder Use(Func<Context, RequestDelegate, Task> middleware)
    {
        _middlewares.Add(next => async ctx => await middleware(ctx, next));
        return this;
    }

    public PipelineBuilder Use(Func<Context, Task> handler)
    {
        _middlewares.Add(next => async ctx =>
        {
            await handler(ctx);
            // Terminal middleware — does not call next
        });
        return this;
    }

    public RequestDelegate Build()
    {
        RequestDelegate app = _ => Task.CompletedTask;  // Terminal
        for (int i = _middlewares.Count - 1; i >= 0; i--)
        {
            app = _middlewares[i](app);
        }
        return app;
    }
}

// Usage
var pipeline = new PipelineBuilder()
    .Use(async (ctx, next) =>
    {
        Console.WriteLine($"[{DateTime.Now:HH:mm:ss}] {ctx.Method} {ctx.Path}");
        var sw = Stopwatch.StartNew();
        await next(ctx);
        Console.WriteLine($"Completed in {sw.ElapsedMilliseconds}ms — {ctx.StatusCode}");
    })
    .Use(async (ctx, next) =>
    {
        ctx.Headers["X-Powered-By"] = "MyFramework";
        await next(ctx);
    })
    .Use(async ctx =>
    {
        if (ctx.Path == "/hello")
            ctx.Body = "Hello, World!";
        else
        {
            ctx.StatusCode = 404;
            ctx.Body = "Not Found";
        }
    })
    .Build();

await pipeline(new Context { Method = "GET", Path = "/hello" });
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Kolejność oprogramowania pośredniego ma znaczenie: pierwszy dodany = najbardziej zewnętrzny (wykonany jako pierwszy na żądanie, ostatni w odpowiedzi).
- Oprogramowanie pośredniczące terminala (brak wywołania `next`) powoduje zwarcie potoku.
- Produkcja: Potok ASP.NET Core jest dokładnie tym wzorcem, zoptymalizowanym przy użyciu skompilowanych drzew wyrażeń pod kątem zerowej alokacji.
---

## Streszczenie
C# to dopracowany, nowoczesny język ogólnego przeznaczenia z doskonałymi narzędziami i silnym ekosystemem. Wyróżnia się rozwojem przedsiębiorstw, tworzeniem gier (Unity) i aplikacjami wieloplatformowymi. Język ewoluował szybko — nowoczesny C# jest zwięzły, wyrazisty i bezpieczny dla typów. Choć nie ma on rozmiaru ekosystemu takiego jak Java czy Python, jakość i spójność platformy .NET sprawiają, że C# jest produktywnym i przyjemnym językiem do szerokiego zakresu zastosowań.