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
# C#
Ang C# (binibigkas na "C-sharp") ay isang moderno, object-oriented, type-safe na programming language na binuo ng Microsoft sa pamumuno ni Anders Hejlsberg at unang inilabas noong 2002. Gumagana ito sa .NET platform at idinisenyo upang pagsamahin ang kapangyarihan ng C++ sa pagiging produktibo ng Visual Basic. Ngayon, ang C# ay isang versatile, cross-platform na wika na ginagamit para sa mga web application (ASP.NET), desktop software (Windows), game development (Unity), mobile app (MAUI), cloud services (Azure), at higit pa.
Ang C# ay patuloy na nasisipsip ang pinakamahusay na mga ideya mula sa iba pang mga wika — LINQ, async/wait, mga tala, pagtutugma ng pattern — ginagawa itong isa sa mga pinaka-mayaman sa tampok at madaling gamitin na mga wika na magagamit.
---

## Bakit Mahalaga ang C#
- **Unity game engine**: Ang pangunahing wika para sa Unity, ang pinakasikat na game engine sa mundo ayon sa bilang ng developer.
- **Pagpapaunlad ng negosyo**: Ang ASP.NET Core ay isa sa pinakamabilis na web frameworks na magagamit (pare-parehong nangunguna sa mga benchmark ng TechEmpower).
- **Cross-platform**: Gumagana ang .NET 5+ sa Windows, macOS, at Linux. Hindi na Windows-only.
- **Productivity**: Napakahusay na suporta sa IDE (Visual Studio, Rider), malakas na uri ng system, at modernong mga tampok ng syntax.
- **async/wait pioneer**: Ipinakilala ng C# ang async/wait noong 2012 — mga taon bago pinagtibay ng ibang mga wika ang pattern.
- **LINQ**: Ang Language-Integrated na Query ay nagbibigay-daan sa iyong magsulat ng mga query na tulad ng SQL nang direkta sa C# laban sa anumang data source.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Pag-uugnay ng Windows** | Makasaysayang nakatali sa Windows; perception lags behind reality | Ang .NET 6+ ay ganap na cross-platform |
| **Mas maliit na ecosystem kaysa sa Java** | Mas kaunting mga third-party na aklatan kaysa sa Maven/PyPI | Lumalaki ang NuGet; maraming mga aklatan ng Java ang may katumbas na C# |
| **Hindi gaanong karaniwan sa mga startup** | Mas sikat sa enterprise kaysa sa Silicon Valley | Go, Rust, Node.js para sa cloud-native microservices |
| **Mobile (MAUI)** | Ang Xamarin/MAUI ay hindi gaanong mature kaysa sa native o Flutter | Gumamit ng katutubong Swift/Kotlin o Flutter para sa mga kumplikadong mobile app |
| **Linux GUI** | Limitadong mga opsyon sa katutubong GUI sa Linux | Gumamit ng mga web-based na UI (Blazor) o Avalonia |
---

## Syntax Fundamentals
### Pangunahing Istruktura
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

### Object-Oriented Programming
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

### Mga Tala (C# 9+) — Mga Hindi Nababagong Uri ng Data
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

### LINQ — Language-Integrated na Query
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

### Async/Await
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

### Pagtutugma ng Pattern (C# 7-13)
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

## Advanced na Syntax at Mga Pattern
### Generics
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

### Mga Delegado, Kaganapan, at Lambda Expression
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

### Custom Exception Hierarchies
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

### Overloading ng Operator
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

## Concurrency at Paralelismo
### async/naghihintay sa Mga Internal
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

### Parallel LINQ at Task Parallel Library
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

## Project Configuration at Build System
### Istraktura ng Proyekto
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

### .csproj File
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

### Pagsubok sa xUnit
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

### CI/CD Pipeline
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

## Interoperability
### P/Invoke — Pagtawag sa C Libraries
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

## Mga Pattern ng Disenyo
### Pattern ng Tagabuo (Fluent API)
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

### Pattern ng Diskarte sa Mga Delegado
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
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

## Deployment
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

### Deployment na Partikular sa Platform
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

## Ang .NET Ecosystem
### Mga Framework at Platform
| Balangkas | Domain | Paglalarawan |
|-----------|--------|-------------|
| **ASP.NET Core** | Web | Mataas na pagganap ng web framework para sa mga API at web app |
| **Blazor** | Web (frontend) | Bumuo ng mga interactive na web UI gamit ang C# sa halip na JavaScript |
| **Entity Framework Core** | ORM | Access sa database gamit ang LINQ; code-first migration |
| **Pagkakaisa** | Mga Laro | Ang pinakasikat na game engine sa mundo (C# scripting) |
| **.NET MAUI** | Mobile/Desktop | Cross-platform na apps para sa iOS, Android, macOS, Windows |
| **Avalonia** | Desktop | Cross-platform desktop UI (tulad ng WPF para sa lahat ng platform) |
### Pamamahala ng Build at Package
| Tool | Layunin |
|------|---------|
| **dotnet CLI** | Bumuo, tumakbo, sumubok, mag-publish mula sa command line |
| **NuGet** | Tagapamahala ng package |
| **MSBuild** | Pinagbabatayan ng build system |
| **Visual Studio / Rider** | Mga IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# Mga Bersyon ng Wika
| Bersyon | Taon | Mga Pangunahing Tampok |
|---------|------|-------------|
| C# 7 | 2017 | Pagtutugma ng pattern, tuple,`out`variable, lokal na function |
| C# 8 | 2019 | Mga nullable na uri ng reference,`switch`expression, async stream |
| C# 9 | 2020 | **Records**, top-level na mga statement,`init`property |
| C# 10 | 2021 | Record structs, global`using`, file-scoped namespaces |
| C# 11 | 2022 | Mga literal na string ng raw, mga pattern ng listahan, mga miyembro ng `required`, generic na matematika |
| C# 12 | 2023 | Pangunahing mga konstruktor, mga expression ng koleksyon, mga inline na array |
| C# 13 | 2024 | `params`na mga koleksyon, mga bagong uri ng lock, first-class span |
---

## Kailan Gamitin ang C#
| Sitwasyon | Bakit C# | Mas mahusay na Alternatibo |
|----------|--------|--------------------|
| Pagbuo ng laro (Unity) | Ang karaniwang Unity scripting language | -- |
| Mga backend sa web ng negosyo | Ang ASP.NET Core ay mabilis, mature, well-supported | Java (Spring Boot) |
| Windows desktop application | WPF, WinForms, WinUI ay mature na | -- |
| Cross-platform desktop | Avalonia o MAUI | Electron (batay sa web) |
| Web frontend (Blazor) | Full-stack C# — walang JavaScript na kailangan | React/Vue/Angular para sa mas mayayamang SPA ecosystem |
| Mga serbisyo sa ulap (Azure) | Deep Azure integration | -- |
| Mga mobile app (MAUI) | Cross-platform na may C# | Flutter, React Native, o native Swift/Kotlin |
| AI/ML | Posible sa ML.NET | Python (napakagusto) |
| Mga tool / script ng CLI | Posible ngunit verbose | Go, Rust, Python |
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba ng`class`at`record`sa C#?
**A:** Ang`class`ay isang uri ng sanggunian na may mga nababagong katangian bilang default — dalawang variable ang maaaring sumangguni sa parehong bagay. Ang`record`(C# 9+) ay isang uri ng sanggunian na may pagkakapantay-pantay na nakabatay sa halaga — dalawang talaan na may parehong data ang itinuturing na pantay. Ang mga record ay may init-only na mga katangian, isang built-in na`ToString`, at sumusuporta sa`with`na mga expression para sa hindi mapanirang mutation. Gumamit ng mga talaan para sa mga carrier ng data (mga DTO, value object); gumamit ng mga klase para sa mga entity na mayaman sa pag-uugali na may pagkakakilanlan.
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

### Q2: Paano gumagana ang async/wait at`Task`sa loob?
**A:** Ang`async/await`ay syntactic sugar sa isang state machine na binuo ng compiler. Kapag nag-`await` ka ng isang`Task`, ang pamamaraan ay nahahati sa punto ng paghihintay: lahat ng nauna ay isinagawa nang sabay-sabay, pagkatapos ay ang natitira ay nakarehistro bilang isang pagpapatuloy. Ang thread ay pinalaya na gumawa ng iba pang gawain.  Ang`Task<T>`ay kumakatawan sa isang hinaharap na halaga.  Ang`ValueTask<T>`ay isang struct alternative para sa mga maiinit na landas na umiiwas sa heap allocation kapag ang resulta ay available na.
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

### Q3: Ano ang mga paraan ng extension, at kailan ko dapat gamitin ang mga ito?
**A:** Ang mga paraan ng extension ay nagdaragdag ng mga pamamaraan sa mga umiiral nang uri nang hindi binabago ang mga ito. Ang mga ito ay mga static na pamamaraan sa isang static na klase, na may`this`na keyword sa unang parameter. Pinapagana nila ang isang matatas at nakaka-chainable na API. Gamitin ang mga ito upang magdagdag ng mga pamamaraan ng utility sa mga uri na hindi mo pagmamay-ari (tulad ng`string`o`IEnumerable<T>`). Iwasan ang labis na paggamit sa mga ito — maaari nilang gawing mahirap matuklasan ang code.
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

### Q4: Paano gumagana ang pagtutugma ng pattern sa modernong C#?
**A:** Ang C# ay unti-unting nagdagdag ng mas malakas na pagtutugma ng pattern. Ang mga switch expression (C# 8), type patterns, property patterns, relational patterns, at list patterns (C# 11) ay nagbibigay-daan sa maikli at nagpapahayag ng conditional logic. Pinapalitan ng pagtutugma ng pattern ang mahahabang if/else na mga kadena at lubusang sinusuri ng compiler.
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

### Q5: Ano ang dependency injection sa .NET, at paano ko ito gagamitin?
**A:** Ang .NET ay may built-in na suporta sa DI sa pamamagitan ng`Microsoft.Extensions.DependencyInjection`. Irerehistro mo ang mga serbisyo sa kanilang mga habambuhay (Singleton, Scoped, Transient), at ini-inject sila ng container sa pamamagitan ng mga parameter ng constructor. Singleton: isang instance para sa app. Saklaw: isa sa bawat kahilingan sa HTTP. Lumilipas: bagong pagkakataon sa bawat oras.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Generic Repository na may Caching
**Pahayag ng Problema:** Magpatupad ng generic na pattern ng repository na may dekorador na nagdaragdag ng caching. Dapat suportahan ng repository ang mga pagpapatakbo ng CRUD, at ang dekorador ng pag-cache ay dapat mag-cache ng mga pagbabasa at hindi wasto sa mga pagsusulat.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) isang generic na`IRepository<T>`interface, (2) isang konkretong pagpapatupad (hal., in-memory), (3) isang caching decorator na bumabalot sa anumang repository, (4) cache invalidation sa write operations. Ang pattern ng dekorador ay nagpapanatili ng pag-cache ng orthogonal sa logic ng pag-access ng data.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Tukuyin ang`IRepository<T>`gamit ang`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Lumikha ng`CachingRepository<T>`na bumabalot sa`IRepository<T>`at gumagamit ng`IMemoryCache`.
- Cache key:`typeof(T).Name:{id}`.
- Sa mga pagpapatakbo ng pagsulat, i-invalidate ang cache entry.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Paghihiwalay ng mga alalahanin: ang pag-cache ay isang dekorador, hindi pinaghalo sa repositoryo.
- Pagrehistro ng DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(gamit ang Scrutor).
- Produksyon: gumamit ng`IDistributedCache`(Redis) para sa mga sitwasyong multi-server, at magdagdag ng mga pattern sa cache-aside na may proteksyon ng `CacheStampede`.
### Problema 2: Magpatupad ng Middleware Pipeline
**Pahayag ng Problema:** Bumuo ng pipeline ng middleware na katulad ng pipeline ng kahilingan ng ASP.NET Core. Maaaring iproseso ng bawat middleware ang kahilingan, tawagan ang susunod na middleware, at iproseso ang tugon.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) isang uri ng`RequestDelegate`na kumakatawan sa pipeline, (2) middleware na bumabalot sa susunod na delegado, (3) isang builder API para sa pagbuo ng middleware. Ito ang Chain of Responsibility pattern na ipinatupad sa mga delegado.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Ang`RequestDelegate`ay`Func<Context, RequestDelegate, Task>`.
- Natatanggap ng bawat middleware ang konteksto at isang function na `next`.
- Nagdaragdag ang`Use`ng middleware;  Binubuo sila ng`Build`sa isang solong delegado.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Mahalaga ang pagkakasunud-sunod ng middleware: unang idinagdag = pinakalabas (unang isinagawa kapag hiniling, huli sa pagtugon).
- Terminal middleware (walang`next`na tawag) ay nag-short-circuit sa pipeline.
- Produksyon: Ang pipeline ng ASP.NET Core ay eksaktong pattern na ito, na-optimize na may pinagsama-samang mga expression tree para sa zero allocation.
---

## Buod
Ang C# ay isang makintab, moderno, pangkalahatang layunin na wika na may mahusay na tool at isang malakas na ecosystem. Mahusay ito sa pagbuo ng enterprise, pagbuo ng laro (Unity), at mga cross-platform na application. Mabilis na umunlad ang wika — ang modernong C# ay maigsi, nagpapahayag, at ligtas sa uri. Bagama't wala itong sukat ng ecosystem ng Java o Python, ang kalidad at pagkakapare-pareho ng .NET ay ginagawang isang produktibo at kasiya-siyang wika ang C# para sa malawak na hanay ng mga aplikasyon.