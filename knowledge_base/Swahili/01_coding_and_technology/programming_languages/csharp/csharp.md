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

#C#
C# (inayotamkwa "C-mkali") ni lugha ya kisasa, inayolenga kitu, na aina-salama ya programu iliyotengenezwa na Microsoft chini ya uongozi wa Anders Hejlsberg na iliyotolewa kwa mara ya kwanza mwaka wa 2002. Inaendeshwa kwenye jukwaa la .NET na iliundwa kuchanganya nguvu ya C++ na tija ya Visual Basic. Leo, C# ni lugha yenye matumizi mengi, ya jukwaa tofauti inayotumika kwa programu za wavuti (ASP.NET), programu ya kompyuta ya mezani (Windows), ukuzaji wa mchezo (Umoja), programu za rununu (MAUI), huduma za wingu (Azure), na zaidi.
C# imechukua kwa kasi mawazo bora kutoka kwa lugha zingine - LINQ, usawazishaji/ngoja, rekodi, kulinganisha muundo - kuifanya kuwa mojawapo ya lugha zenye vipengele vingi na zinazofaa wasanidi programu zinazopatikana.
---

## Kwa nini C# ni muhimu
- **Injini ya mchezo wa Umoja**: Lugha ya msingi kwa Unity, injini ya mchezo maarufu zaidi duniani kwa idadi ya wasanidi programu.
- **Uendelezaji wa biashara**: ASP.NET Core ni mojawapo ya mifumo ya mtandao yenye kasi zaidi inayopatikana (huongoza mara kwa mara alama za TechEmpower).
- **Cross-platform**: .NET 5+ inaendeshwa kwenye Windows, macOS, na Linux. Sio Windows pekee.
- **Tija**: Usaidizi bora kabisa wa IDE (Visual Studio, Rider), mfumo thabiti wa aina, na vipengele vya kisasa vya sintaksia.
- **async/wait pioneer**: C# ilianzisha async/ait mwaka wa 2012 — miaka kabla ya lugha zingine kupitisha muundo.
- **LINQ**: Hoja Iliyounganishwa kwa Lugha hukuwezesha kuandika maswali yanayofanana na SQL moja kwa moja katika C# dhidi ya chanzo chochote cha data.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Chama cha Windows** | Kihistoria imefungwa kwa Windows; mtazamo uko nyuma ya ukweli | .NET 6+ ni jukwaa mtambuka kabisa |
| **Mfumo mdogo wa ikolojia kuliko Java** | Maktaba chache za wahusika wengine kuliko Maven/PyPI | NuGet inakua; maktaba nyingi za Java zina C # sawa |
| **Inapungua sana katika uanzishaji** | Maarufu zaidi katika biashara kuliko katika Silicon Valley | Nenda, Rust, Node.js kwa huduma ndogo za asili za wingu |
| **Simu ya Mkononi (MAUI)** | Xamarin/MAUI haijakomaa kuliko ya asili au Flutter | Tumia Swift/Kotlin asilia au Flutter kwa programu changamano za rununu |
| **Linux GUI** | Chaguo chache za asili za GUI kwenye Linux | Tumia violesura vya wavuti (Blazor) au Avalonia |
---

## Misingi ya Sintaksia
### Muundo Msingi
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

### Upangaji Unaoelekezwa na Kitu
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

### Rekodi (C# 9+) — Aina za Data Zisizobadilika
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

### LINQ — Hoja Iliyounganishwa kwa Lugha
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

### Async/Subiri
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

### Ulinganishaji wa Muundo (C# 7-13)
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

## Sintaksia na Miundo ya Kina
### Jenerali
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

### Wajumbe, Matukio, na Maneno ya Lambda
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

### Daraja za Vighairi Maalum
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

### Kupakia kwa Opereta
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

## Concurrency & Usambamba
### kusawazisha/kungoja za Ndani
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

### LINQ Sambamba na Maktaba Sambamba ya Task
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi
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

### .csproj Faili
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

### Kujaribu kwa xUnit
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

### CI/CD Bomba
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

## Kuingiliana
### P/Omba — Kupigia simu Maktaba za C
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

### C++/CLI Interop
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

## Miundo ya Kubuni
### Muundo wa Wajenzi (API ya Fasaha)
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

### Muundo wa Mkakati na Wajumbe
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
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

## Usambazaji
### Dockerfile
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

### Usambazaji Mahususi wa Mfumo
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

## Mfumo wa Ikolojia wa .NET
### Mifumo na Majukwaa
| Mfumo | Kikoa | Maelezo |
|-----------|--------|-------------|
| **ASP.NET Msingi** | Mtandao | Mfumo wa wavuti wa utendaji wa juu wa API na programu za wavuti |
| **Blazor** | Wavuti (mbele) | Unda kiolesura shirikishi cha wavuti ukitumia C# badala ya JavaScript |
| **Kiini cha Mfumo wa Taasisi** | ORM | Ufikiaji wa hifadhidata na LINQ; uhamiaji wa nambari-kwanza |
| **Umoja** | Michezo | Injini ya mchezo maarufu zaidi duniani ( C# scripting) |
| **.NET MAUI** | Simu/Desktop | Programu za jukwaa tofauti za iOS, Android, macOS, Windows |
| **Avalonia** | Kompyuta ya mezani | UI ya eneo-kazi la majukwaa mbalimbali (kama vile WPF kwa majukwaa yote) |
### Kuunda na Usimamizi wa Kifurushi
| Zana | Kusudi |
|------|----------|
| **dotnet CLI** | Jenga, endesha, jaribu, uchapishe kutoka kwa safu ya amri |
| **NuGet** | Kidhibiti kifurushi |
| **MSBuild** | Mfumo wa ujenzi wa msingi |
| **Studio ya Visual / Rider** | Vitambulisho |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# Matoleo ya Lugha
| Toleo | Mwaka | Sifa Muhimu |
|---------|------|-------------|
| C# 7 | 2017 | Ulinganishaji wa muundo, nakala, vigeu vya `out`, utendaji wa ndani |
| C#8 | 2019 | Aina za marejeleo zinazoweza kubatilishwa, misemo ya `switch`, mitiririko isiyosawazishwa |
| C#9 | 2020 | **Rekodi**, taarifa za kiwango cha juu, mali za`init`|
| C#10 | 2021 | Miundo ya rekodi,`using`ya kimataifa , nafasi za majina zilizo na faili |
| C#11 | 2022 | Kamba mbichi, ruwaza za orodha, wanachama wa `required`, hesabu za jumla |
| C# 12 | 2023 | Wajenzi msingi, maneno ya mkusanyiko, safu za ndani |
| C#13 | 2024 |  Mikusanyiko ya `params`, aina mpya za kufuli, nafasi za daraja la kwanza |
---

## Wakati wa kutumia C#
| Hali | Kwa nini C# | Mbadala Bora |
|----------|----------------------------|
| Maendeleo ya mchezo (Umoja) | Lugha ya kawaida ya uandishi ya Unity | -- |
| Usaidizi wa nyuma wa wavuti wa biashara | Msingi wa ASP.NET ni wa haraka, ukomavu, unaoungwa mkono vyema | Java (Spring Boot) |
| Programu za kompyuta za mezani za Windows | WPF, WinForms, WinUI zimekomaa | -- |
| Eneo-kazi la jukwaa-mbali | Avalonia au MAUI | Elektroni (kulingana na wavuti) |
| Sehemu ya mbele ya wavuti (Blazor) | Rafu kamili ya C# — JavaScript haihitajiki | React/Vue/Angular kwa mifumo tajiri ya ikolojia ya SPA |
| Huduma za wingu (Azure) | Ushirikiano wa kina wa Azure | -- |
| Programu za simu (MAUI) | Jukwaa mtambuka na C# | Flutter, React Native, au Swift/Kotlin asilia |
| AI/ML | Inawezekana na ML.NET | Chatu (inapendelewa sana) |
| Zana / maandishi ya CLI | Inawezekana lakini kitenzi | Nenda, Rust, Python |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`class`na`record`katika C#?
**J:**`class`ni aina ya marejeleo yenye sifa zinazoweza kubadilika kwa chaguo-msingi - vigeu viwili vinaweza kurejelea kitu kimoja.`record`(C# 9+) ni aina ya marejeleo yenye usawa unaotegemea thamani - rekodi mbili zilizo na data sawa huchukuliwa kuwa sawa. Rekodi zina sifa za init-pekee,`ToString`iliyojengewa ndani, na zinaauni misemo ya`with`kwa ubadilishaji usioharibu. Tumia rekodi kwa watoa huduma za data (DTO, vitu vya thamani); tumia madarasa kwa huluki zenye kitabia zenye utambulisho.
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

### Q2: Je, async/inasubiri na`Task`hufanyaje kazi ndani?
**J:**`async/await`ni sukari ya kisintaksia juu ya mashine ya serikali inayozalishwa na mkusanyaji. Unapotumia`await`a`Task`, njia inagawanywa katika sehemu ya kusubiri: kila kitu kilichotangulia kinatekelezwa kwa usawa, kisha salio husajiliwa kama mwendelezo. Uzi umeachiliwa kufanya kazi nyingine. `Task<T>`inawakilisha thamani ya siku zijazo. `ValueTask<T>`ni muundo mbadala wa njia motomoto ambazo huepuka mgao wa lundo wakati matokeo tayari yanapatikana.
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

### Q3: Mbinu za upanuzi ni zipi, na ninapaswa kuzitumia lini?
**J:** Mbinu za upanuzi huongeza mbinu kwa aina zilizopo bila kuzirekebisha. Ni njia tuli katika darasa tuli, na neno kuu la`this`kwenye kigezo cha kwanza. Wanawezesha API fasaha, inayoweza kuunganishwa. Zitumie kuongeza mbinu za matumizi kwa aina usizomiliki (kama`string`au`IEnumerable<T>`). Epuka kuzitumia kupita kiasi - zinaweza kufanya msimbo kuwa mgumu kugundua.
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

### Q4: Je, ulinganishaji wa muundo hufanyaje kazi katika C# ya kisasa?
**A:** C# imeongeza hatua kwa hatua ulinganishaji wa muundo wenye nguvu zaidi. Badili misemo (C# 8), ruwaza za aina, muundo wa sifa, ruwaza za uhusiano, na ruwaza za orodha (C# 11) huruhusu mantiki ya masharti mafupi na ya kueleza. Ulinganishaji wa ruwaza huchukua nafasi ya minyororo mirefu kama/vingine na inakaguliwa kikamilifu na mkusanyaji.
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

### Q5: Sindano ya utegemezi katika .NET ni nini, na ninaitumiaje?
**A:** .NET ina usaidizi wa ndani wa DI kupitia`Microsoft.Extensions.DependencyInjection`. Unasajili huduma kwa muda wa maisha yao (Singleton, Scoped, Transient), na kontena huzidunga kupitia vigezo vya kijenzi. Singleton: mfano mmoja kwa programu. Upeo: moja kwa ombi la HTTP. Muda mfupi: mfano mpya kila wakati.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tengeneza Hifadhi ya Jumla yenye Uakibishaji
**Taarifa ya Tatizo:** Tekeleza muundo wa hazina wa jumla na kipamba kinachoongeza akiba. Hifadhi inapaswa kuunga mkono shughuli za CRUD, na mpambaji wa kache anapaswa kuweka akiba ya usomaji na kubatilisha maandishi.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) kiolesura cha kawaida cha `IRepository<T>`, (2) utekelezaji thabiti (k.m., kumbukumbu), (3) kipambo cha kache ambacho hufunika hazina yoyote, (4) kubatilisha akiba kwenye shughuli za uandishi. Mchoro wa mpambaji huweka akiba kwenye mantiki ya ufikiaji wa data.
**Hatua ya 2 — Tambua Mbinu:**
- Fafanua`IRepository<T>`ukitumia`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Unda`CachingRepository<T>`inayofunika`IRepository<T>`na kutumia`IMemoryCache`.
- Kitufe cha Cache:`typeof(T).Name:{id}`.
- Kwenye shughuli za uandishi, batilisha ingizo la akiba.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Mgawanyo wa wasiwasi: caching ni mapambo, si kuchanganywa katika hazina.
- Usajili wa DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(kwa kutumia Scrutor).
- Uzalishaji: tumia`IDistributedCache`(Redis) kwa matukio ya seva nyingi, na uongeze mifumo ya kando ya kache kwa ulinzi wa `CacheStampede`.
### Tatizo la 2: Tekeleza Bomba la Vifaa vya Kati
**Taarifa ya Tatizo:** Tengeneza bomba la vifaa vya kati sawa na bomba la ombi la ASP.NET Core. Kila kifaa cha kati kinaweza kuchakata ombi, piga simu kifaa cha kati kinachofuata, na kushughulikia jibu.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) aina ya`RequestDelegate`inayowakilisha bomba, (2) vifaa vya kati vinavyomfunika mjumbe anayefuata, (3) API ya kijenzi ya kutunga vifaa vya kati. Huu ni muundo wa Msururu wa Wajibu unaotekelezwa na wajumbe.
**Hatua ya 2 — Tambua Mbinu:**
`RequestDelegate` ni`Func<Context, RequestDelegate, Task>`.
- Kila kifaa cha kati hupokea muktadha na kitendakazi cha `next`.
-`Use`inaongeza vifaa vya kati; `Build`inazijumuisha kuwa mjumbe mmoja.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Mambo ya mpangilio wa vifaa vya kati: kwanza imeongezwa = ya nje (inatekelezwa kwanza kwa ombi, mwisho kwa jibu).
- Vifaa vya kati vya terminal (hakuna simu ya `next`) hupunguza bomba.
- Uzalishaji: Bomba la ASP.NET Core ni muundo huu haswa, ulioboreshwa na miti ya kujieleza iliyokusanywa kwa mgao sifuri.
---

## Muhtasari
C# ni lugha iliyoboreshwa, ya kisasa, yenye madhumuni ya jumla yenye zana bora na mfumo thabiti wa ikolojia. Inafaulu katika ukuzaji wa biashara, ukuzaji wa mchezo (Umoja), na utumizi wa majukwaa mtambuka. Lugha imebadilika haraka - C# ya kisasa ni mafupi, ya kueleza, na salama ya aina. Ingawa haina saizi ya mfumo ikolojia wa Java au Python, ubora na uthabiti wa NET hufanya C# kuwa lugha yenye tija na ya kufurahisha kwa anuwai ya programu.