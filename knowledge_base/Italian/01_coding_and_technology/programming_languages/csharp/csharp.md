---
# Metadata
title: "C#"
description: "Comprehensive reference for the C# programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# C#
C# (pronunciato "C-sharp") è un linguaggio di programmazione moderno, orientato agli oggetti e indipendente dai tipi sviluppato da Microsoft sotto la guida di Anders Hejlsberg e rilasciato per la prima volta nel 2002. Funziona sulla piattaforma .NET ed è stato progettato per combinare la potenza del C++ con la produttività di Visual Basic. Oggi C# è un linguaggio versatile e multipiattaforma utilizzato per applicazioni Web (ASP.NET), software desktop (Windows), sviluppo di giochi (Unity), app mobili (MAUI), servizi cloud (Azure) e altro ancora.
C# ha costantemente assorbito le migliori idee da altri linguaggi (LINQ, async/await, records, pattern match) rendendolo uno dei linguaggi più ricchi di funzionalità e facili da usare per gli sviluppatori disponibili.
---

## Perché C# è importante
- **Motore di gioco Unity**: il linguaggio principale di Unity, il motore di gioco più popolare al mondo per numero di sviluppatori.
- **Sviluppo aziendale**: ASP.NET Core è uno dei framework Web più veloci disponibili (supera costantemente i benchmark TechEmpower).
- **Multipiattaforma**: .NET 5+ funziona su Windows, macOS e Linux. Non più solo per Windows.
- **Produttività**: eccellente supporto IDE (Visual Studio, Rider), sistema di tipizzazione avanzato e funzionalità di sintassi moderne.
- **Pioniere di async/await**: C# ha introdotto async/await nel 2012, anni prima che altri linguaggi adottassero il modello.
- **LINQ**: Language-Integrated Query ti consente di scrivere query di tipo SQL direttamente in C# su qualsiasi origine dati.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Associazione Windows** | Storicamente legato a Windows; la percezione è in ritardo rispetto alla realtà | .NET 6+ è completamente multipiattaforma |
| **Ecosistema più piccolo di Java** | Meno librerie di terze parti rispetto a Maven/PyPI | NuGet è in crescita; molte librerie Java hanno equivalenti C# |
| **Meno comune nelle startup** | Più popolare nelle imprese che nella Silicon Valley | Vai, Rust, Node.js per microservizi nativi del cloud |
| **Cellulare (MAUI)** | Xamarin/MAUI è meno maturo di quello nativo o di Flutter | Utilizza Swift/Kotlin o Flutter nativi per app mobili complesse |
| **GUI Linux** | Opzioni GUI native limitate su Linux | Utilizza interfacce utente basate sul Web (Blazor) o Avalonia |
---

## Fondamenti di sintassi
### Struttura di base
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

### Programmazione orientata agli oggetti
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

### Records (C# 9+): tipi di dati immutabili
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

### LINQ: query integrate nel linguaggio
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

### Asincrono/Aspetta
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

### Corrispondenza dei modelli (C# 7-13)
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

## Sintassi e modelli avanzati
### Generici
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

### Delegati, eventi ed espressioni Lambda
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

### Gerarchie di eccezioni personalizzate
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

### Sovraccarico operatore
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

## Concorrenza e parallelismo
### asincrono/attendono componenti interni
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

### Libreria parallela LINQ e Task Parallel
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

## Configurazione del progetto e sistema di creazione
### Struttura del progetto
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

### File .csproj
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

### Test con xUnit
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

### Pipeline CI/CD
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

## Interoperabilità
### P/Invoke: chiamata alle librerie C
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

### Interoperabilità C++/CLI
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

## Modelli di progettazione
### Modello di creazione (API Fluent)
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

### Modello strategico con i delegati
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

## Prestazioni e ottimizzazione
### Strumenti di profilazione
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

## Distribuzione
###Dockerfile
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

### Distribuzione specifica della piattaforma
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

## L'ecosistema .NET
### Framework e piattaforme
| Quadro | Dominio | Descrizione |
|-----------|--------|-----|
| **ASP.NET Core** | Rete | Framework Web ad alte prestazioni per API e app Web |
| **Blazor** | Web (frontend) | Crea interfacce utente Web interattive con C# anziché JavaScript |
| **Entity Framework Core** | ORMA | Accesso al database con LINQ; migrazioni code-first |
| **Unità** | Giochi | Il motore di gioco più popolare al mondo (scripting C#) |
| **.NET MAUI** | Cellulare/Desktop | App multipiattaforma per iOS, Android, macOS, Windows |
| **Avalonia** | Scrivania | Interfaccia utente desktop multipiattaforma (come WPF per tutte le piattaforme) |
### Gestione di build e pacchetti
| Strumento | Scopo |
|------|---------|
| **CLI puntonet** | Costruisci, esegui, testa, pubblica dalla riga di comando |
| **NuGet** | Gestore pacchetti |
| **MSBuild** | Sistema di build sottostante |
| **Studio visivo / Pilota** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## Versioni del linguaggio C#
| Versione | Anno | Caratteristiche principali |
|---------|------|-----|
| Do#7 | 2017 | Corrispondenza di modelli, tuple, variabili `out`, funzioni locali |
| Do#8 | 2019 | Tipi di riferimento nullable, espressioni `switch`, flussi asincroni |
| Do#9 | 2020 | **Record**, istruzioni di primo livello, proprietà`init`|
| Do#10 | 2021 | Strutture di record,`using`globale, spazi dei nomi con ambito file |
| Do#11 | 2022 | Valori letterali di stringa grezza, modelli di elenco, membri `required`, matematica generica |
| Do#12 | 2023 | Costruttori primari, espressioni di raccolta, array inline |
| Do#13 | 2024 |  Collezioni `params`, nuove tipologie di serrature, campate di prima classe |
---

##Quando utilizzare C#
| Scenario | Perché C# | Alternativa migliore |
|----------|--------|-------------|
| Sviluppo di giochi (Unity) | Il linguaggio di scripting standard di Unity | -- |
| Backend web aziendali | ASP.NET Core è veloce, maturo e ben supportato | Java (avvio primaverile) |
| Applicazioni desktop Windows | WPF, WinForms, WinUI sono maturi | -- |
| Desktop multipiattaforma | Avalonia o MAUI | Elettrone (basato sul web) |
| Front-end Web (Blazor) | C# full-stack: non è necessario JavaScript | React/Vue/Angular per ecosistemi SPA più ricchi |
| Servizi cloud (Azure) | Integrazione profonda con Azure | -- |
| App mobili (MAUI) | Multipiattaforma con C# | Flutter, React Native o Swift/Kotlin nativo |
| AI/ML | Possibile con ML.NET | Python (preferibilmente preferito) |
| Strumenti/script CLI | Possibile ma prolisso | Vai, Ruggine, Python |
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra`class`e`record`in C#?
**R:**`class`è un tipo di riferimento con proprietà modificabili per impostazione predefinita: due variabili possono fare riferimento allo stesso oggetto. Un`record`(C# 9+) è un tipo di riferimento con uguaglianza basata sul valore: due record con gli stessi dati sono considerati uguali. I record hanno proprietà di solo init, un`ToString`integrato e supportano le espressioni`with`per la mutazione non distruttiva. Utilizzare record per supporti dati (DTO, oggetti di valore); utilizzare le classi per entità ricche di comportamento con identità.
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

### D2: Come funzionano internamente async/await e `Task`?
**R:**`async/await`è zucchero sintattico su una macchina a stati generata dal compilatore. Quando si`await`a`Task`, il metodo viene suddiviso nel punto di attesa: tutto prima viene eseguito in modo sincrono, quindi il resto viene registrato come continuazione. Il thread è libero di svolgere altro lavoro. `Task<T>`rappresenta un valore futuro. `ValueTask<T>`è una struttura alternativa per i percorsi attivi che evita l'allocazione dell'heap quando il risultato è già disponibile.
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

### D3: Quali sono i metodi di estensione e quando dovrei utilizzarli?
**R:** I metodi di estensione aggiungono metodi ai tipi esistenti senza modificarli. Sono metodi statici in una classe statica, con la parola chiave`this`sul primo parametro. Consentono un'API fluida e concatenabile. Usali per aggiungere metodi di utilità ai tipi che non possiedi (come`string`o`IEnumerable<T>`). Evita di abusarne: possono rendere difficile la scoperta del codice.
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

### D4: Come funziona la corrispondenza dei modelli nel C# moderno?
**R:** C# ha progressivamente aggiunto modelli di corrispondenza più potenti. Le espressioni di commutazione (C# 8), i modelli di tipo, i modelli di proprietà, i modelli relazionali e i modelli di elenco (C# 11) consentono una logica condizionale concisa ed espressiva. La corrispondenza dei modelli sostituisce le lunghe catene if/else ed è controllata in modo esaustivo dal compilatore.
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

### D5: Cos'è l'inserimento delle dipendenze in .NET e come posso utilizzarlo?
**R:** .NET dispone del supporto DI integrato tramite`Microsoft.Extensions.DependencyInjection`. Si registrano i servizi con la loro durata (Singleton, Scoped, Transient) e il contenitore li inserisce tramite parametri del costruttore. Singleton: un'istanza per l'app. Ambito: uno per richiesta HTTP. Transitorio: nuova istanza ogni volta.
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

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: creare un repository generico con memorizzazione nella cache
**Dichiarazione del problema:** Implementa un modello di repository generico con un decoratore che aggiunge la memorizzazione nella cache. Il repository dovrebbe supportare le operazioni CRUD e il decoratore della memorizzazione nella cache dovrebbe memorizzare nella cache le letture e invalidare le scritture.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) un'interfaccia`IRepository<T>`generica, (2) un'implementazione concreta (ad esempio, in memoria), (3) un decoratore di caching che avvolge qualsiasi repository, (4) invalidazione della cache sulle operazioni di scrittura. Il modello decoratore mantiene la memorizzazione nella cache ortogonale alla logica di accesso ai dati.
**Passaggio 2: identificare l'approccio:**
- Definisci`IRepository<T>`con`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Crea`CachingRepository<T>`che avvolge`IRepository<T>`e utilizza`IMemoryCache`.
- Chiave cache:`typeof(T).Name:{id}`.
- Durante le operazioni di scrittura, invalidare la voce della cache.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Separazione degli interessi: il caching è un decoratore, non mescolato nel repository.
- Registrazione DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(usando Scrutor).
- Produzione: utilizza`IDistributedCache`(Redis) per scenari multi-server e aggiungi modelli cache-aside con la protezione `CacheStampede`.
### Problema 2: implementare una pipeline middleware
**Dichiarazione del problema:** creare una pipeline middleware simile alla pipeline delle richieste di ASP.NET Core. Ogni middleware può elaborare la richiesta, chiamare il middleware successivo ed elaborare la risposta.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) un tipo`RequestDelegate`che rappresenti la pipeline, (2) un middleware che racchiuda il delegato successivo, (3) un'API di creazione per la composizione del middleware. Questo è il modello di Catena di Responsabilità implementato con i delegati.
**Passaggio 2: identificare l'approccio:**
-`RequestDelegate`è`Func<Context, RequestDelegate, Task>`.
- Ogni middleware riceve il contesto e una funzione `next`.
-`Use`aggiunge il middleware; `Build`li compone in un unico delegato.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- L'ordine del middleware è importante: primo aggiunto = più esterno (eseguito per primo su richiesta, ultimo su risposta).
- Il middleware del terminale (nessuna chiamata `next`) cortocircuita la pipeline.
- Produzione: la pipeline di ASP.NET Core è esattamente questo modello, ottimizzato con alberi delle espressioni compilati per un'allocazione pari a zero.
---

## Riepilogo
C# è un linguaggio raffinato, moderno e di uso generale con strumenti eccellenti e un forte ecosistema. Eccelle nello sviluppo aziendale, nello sviluppo di giochi (Unity) e nelle applicazioni multipiattaforma. Il linguaggio si è evoluto rapidamente: il C# moderno è conciso, espressivo e indipendente dai tipi. Sebbene non abbia le dimensioni dell'ecosistema di Java o Python, la qualità e la coerenza di .NET rendono C# un linguaggio produttivo e divertente per un'ampia gamma di applicazioni.