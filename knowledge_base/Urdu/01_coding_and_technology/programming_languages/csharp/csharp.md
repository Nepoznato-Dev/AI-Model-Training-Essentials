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
C# (تلفظ "C-sharp") ایک جدید، آبجیکٹ پر مبنی، ٹائپ سیف پروگرامنگ زبان ہے جسے مائیکرو سافٹ نے اینڈرس ہیجلسبرگ کی قیادت میں تیار کیا اور پہلی بار 2002 میں ریلیز کیا گیا۔ یہ .NET پلیٹ فارم پر چلتا ہے اور اسے C++ کی طاقت کو Visual Basic کی پیداواری صلاحیت کے ساتھ ملانے کے لیے ڈیزائن کیا گیا تھا۔ آج، C# ایک ورسٹائل، کراس پلیٹ فارم زبان ہے جو ویب ایپلیکیشنز (ASP.NET)، ڈیسک ٹاپ سافٹ ویئر (ونڈوز)، گیم ڈویلپمنٹ (یونٹی)، موبائل ایپس (MAUI)، کلاؤڈ سروسز (Azure) اور مزید کے لیے استعمال ہوتی ہے۔
C# نے مستقل طور پر دوسری زبانوں کے بہترین خیالات کو جذب کیا ہے — LINQ, async/await, ریکارڈز، پیٹرن میچنگ — اسے سب سے زیادہ فیچر سے بھرپور اور ڈویلپر کے لیے موزوں زبانوں میں سے ایک بنا دیا ہے۔
---

## کیوں C# اہمیت رکھتا ہے۔
- **یونٹی گیم انجن**: یونٹی کی بنیادی زبان، ڈویلپر کی تعداد کے لحاظ سے دنیا کا سب سے مشہور گیم انجن۔
- **انٹرپرائز ڈویلپمنٹ**: ASP.NET کور دستیاب تیز ترین ویب فریم ورکس میں سے ایک ہے (مسلسل TechEmpower بینچ مارکس میں سرفہرست ہے)۔
- **کراس پلیٹ فارم**: .NET 5+ Windows، macOS اور Linux پر چلتا ہے۔ اب صرف ونڈوز نہیں ہے۔
- **پیداواری**: بہترین IDE سپورٹ (بصری اسٹوڈیو، رائڈر)، مضبوط قسم کا نظام، اور جدید نحو خصوصیات۔
- **async/await pioneer**: C# نے 2012 میں async/await متعارف کرایا — دیگر زبانوں کے پیٹرن کو اپنانے سے کئی سال پہلے۔
- **لنق**: زبان سے مربوط سوال آپ کو کسی بھی ڈیٹا سورس کے خلاف براہ راست C# میں SQL جیسے سوالات لکھنے دیتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **ونڈوز ایسوسی ایشن** | تاریخی طور پر ونڈوز سے منسلک؛ تصور حقیقت سے پیچھے ہے | .NET 6+ مکمل طور پر کراس پلیٹ فارم ہے |
| **جاوا سے چھوٹا ماحولیاتی نظام** | Maven/PyPI سے کم تھرڈ پارٹی لائبریریاں | NuGet بڑھ رہا ہے؛ بہت سی جاوا لائبریریوں میں C# مساوی ہیں |
| **شروعات میں کم عام** | سلیکن ویلی کے مقابلے انٹرپرائز میں زیادہ مقبول | کلاؤڈ مقامی مائیکرو سروسز کے لیے Go, Rust, Node.js |
| **موبائل (MAUI)** | Xamarin/MAUI مقامی یا Flutter | سے کم بالغ ہے۔ پیچیدہ موبائل ایپس کے لیے مقامی Swift/Kotlin یا Flutter استعمال کریں۔
| **Linux GUI** | لینکس پر محدود مقامی GUI اختیارات | ویب پر مبنی UIs (Blazor) یا Avalonia | استعمال کریں۔
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
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

### آبجیکٹ اورینٹڈ پروگرامنگ
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

### ریکارڈز (C# 9+) — ناقابل تغیر ڈیٹا کی اقسام
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

### LINQ — زبان سے مربوط سوال
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

### Async/انتظار کریں۔
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

### پیٹرن میچنگ (C# 7-13)
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

## اعلی درجے کی نحو اور نمونے۔
### عام
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

### مندوبین، واقعات، اور لیمبڈا اظہار
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

### اپنی مرضی کے استثنائی درجہ بندی
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

### آپریٹر اوورلوڈنگ
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

## ہم آہنگی اور ہم آہنگی
### async/انتظار اندرونی
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

### متوازی LINQ اور ٹاسک متوازی لائبریری
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ
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

### .csproj فائل
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

### xUnit کے ساتھ ٹیسٹنگ
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

### CI/CD پائپ لائن
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

## انٹرآپریبلٹی
### P/Invoke — C لائبریریوں کو کال کرنا
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

### C++/CLI انٹراپ
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

## ڈیزائن پیٹرن
### بلڈر پیٹرن (فلوئنٹ API)
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

### مندوبین کے ساتھ حکمت عملی کا نمونہ
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

## تعیناتی۔
### ڈاکر فائل
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

### پلیٹ فارم کے لیے مخصوص تعیناتی۔
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

## .NET ایکو سسٹم
### فریم ورک اور پلیٹ فارم
| فریم ورک | ڈومین | تفصیل |
|------------|---------|------------|
| **ASP.NET کور** | ویب | APIs اور ویب ایپس کے لیے اعلیٰ کارکردگی والا ویب فریم ورک |
| **بلیزر** | ویب (فرنٹ اینڈ) | JavaScript کے بجائے C# کے ساتھ انٹرایکٹو ویب UIs بنائیں |
| **اینٹیٹی فریم ورک کور** | ORM | LINQ کے ساتھ ڈیٹا بیس تک رسائی؛ کوڈ-پہلی منتقلی |
| **اتحاد** | گیمز | دنیا کا سب سے مشہور گیم انجن (C# اسکرپٹنگ) |
| **.NET MAUI** | موبائل/ڈیسک ٹاپ | iOS، Android، macOS، Windows کے لیے کراس پلیٹ فارم ایپس |
| **ایولونیا** | ڈیسک ٹاپ | کراس پلیٹ فارم ڈیسک ٹاپ UI (جیسے تمام پلیٹ فارمز کے لیے WPF) |
### تعمیر اور پیکیج کا انتظام
| ٹول | مقصد |
|------|---------|
| **ڈاٹ نیٹ CLI** | کمانڈ لائن سے بنائیں، چلائیں، ٹیسٹ کریں، شائع کریں۔
| **NuGet** | پیکیج مینیجر |
| **MSBuild** | بنیادی تعمیراتی نظام |
| **بصری اسٹوڈیو / رائڈر** | IDEs |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# زبان کے ورژن
| ورژن | سال | اہم خصوصیات |
|---------|------|------------|
| C# 7 | 2017 | پیٹرن میچنگ، ٹیپلز،`out`متغیرات، مقامی افعال |
| C# 8 | 2019 | کالعدم حوالہ جات کی اقسام،`switch`اظہار، async اسٹریمز |
| C# 9 | 2020 | **ریکارڈ**، اعلی درجے کے بیانات،`init`خصوصیات |
| C# 10 | 2021 | ریکارڈ سٹرکٹس، عالمی `using`، فائل کے دائرہ کار والے نام کی جگہیں |
| C# 11 | 2022 | خام سٹرنگ لٹریلز، فہرست پیٹرن،`required`اراکین، عام ریاضی |
| C# 12 | 2023 | پرائمری کنسٹرکٹرز، کلیکشن ایکسپریشنز، ان لائن ارے |
| C# 13 | 2024 | `params`مجموعہ، نئی قسم کے تالے، فرسٹ کلاس اسپین |
---

## کب استعمال کریں C#
| منظر نامہ | کیوں C# | بہتر متبادل |
|------------|---------|-------------------|
| گیم ڈویلپمنٹ (اتحاد) | معیاری یونٹی اسکرپٹنگ زبان | -- |
| انٹرپرائز ویب بیک اینڈز | ASP.NET کور تیز، بالغ، اچھی طرح سے تعاون یافتہ ہے | جاوا (اسپرنگ بوٹ) |
| ونڈوز ڈیسک ٹاپ ایپلی کیشنز | WPF، WinForms، WinUI بالغ ہیں | -- |
| کراس پلیٹ فارم ڈیسک ٹاپ | Avalonia یا MAUI | الیکٹران (ویب پر مبنی) |
| ویب فرنٹ اینڈ (بلیزر) | مکمل اسٹیک C# - جاوا اسکرپٹ کی ضرورت نہیں ہے۔ امیر SPA ماحولیاتی نظام کے لیے رد عمل/Vue/Angular |
| کلاؤڈ سروسز (Azure) | گہری Azure انضمام | -- |
| موبائل ایپس (MAUI) | C# کے ساتھ کراس پلیٹ فارم | پھڑپھڑانا، مقامی ردعمل ظاہر کرنا، یا مقامی Swift/Kotlin |
| AI/ML | ML.NET کے ساتھ ممکن ہے | ازگر (زبردست ترجیح) |
| CLI ٹولز / اسکرپٹس | ممکن لیکن لفظی | جاؤ، زنگ آلود، ازگر |
---

## مصنوعی سوال و جواب
### Q1: C# میں`class`اور`record`میں کیا فرق ہے؟
**A:** A`class`ایک حوالہ کی قسم ہے جس میں بطور ڈیفالٹ تغیر پذیر خصوصیات ہیں — دو متغیرات ایک ہی چیز کا حوالہ دے سکتے ہیں۔ ایک`record`(C# 9+) قدر پر مبنی مساوات کے ساتھ حوالہ کی قسم ہے — ایک ہی ڈیٹا والے دو ریکارڈز کو برابر سمجھا جاتا ہے۔ ریکارڈز میں صرف ابتدائی خصوصیات ہیں، ایک بلٹ ان `ToString`، اور غیر تباہ کن تغیر کے لیے`with`اظہار کی حمایت کرتے ہیں۔ ڈیٹا کیریئرز کے لیے ریکارڈ استعمال کریں (DTOs، ویلیو آبجیکٹ)؛ شناخت کے ساتھ طرز عمل سے بھرپور اداروں کے لیے کلاسز استعمال کریں۔
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

### Q2: async/await اور`Task`اندرونی طور پر کیسے کام کرتے ہیں؟
**A:**`async/await`کمپائلر کے ذریعہ تیار کردہ ریاستی مشین پر مصنوعی شوگر ہے۔ جب آپ`await`کو ایک`Task`کرتے ہیں، تو طریقہ انتظار کے مقام پر تقسیم ہو جاتا ہے: اس سے پہلے کی ہر چیز کو ہم آہنگی سے انجام دیا جاتا ہے، پھر بقیہ کو تسلسل کے طور پر رجسٹر کیا جاتا ہے۔ دھاگے کو دوسرے کام کرنے کے لیے آزاد کر دیا گیا ہے۔ `Task<T>`مستقبل کی قدر کی نمائندگی کرتا ہے۔ `ValueTask<T>`ہاٹ پاتھز کے لیے ایک ڈھانچہ متبادل ہے جو نتیجہ پہلے سے دستیاب ہونے پر ہیپ ایلوکیشن سے گریز کرتا ہے۔
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

### Q3: توسیع کے طریقے کیا ہیں، اور مجھے انہیں کب استعمال کرنا چاہیے؟
**A:** توسیع کے طریقے موجودہ اقسام میں ترمیم کیے بغیر طریقوں کو شامل کرتے ہیں۔ یہ ایک جامد کلاس میں جامد طریقے ہیں، پہلے پیرامیٹر پر`this`کلیدی لفظ کے ساتھ۔ وہ ایک روانی، چین کے قابل API کو فعال کرتے ہیں۔ یوٹیلیٹی طریقوں کو ان اقسام میں شامل کرنے کے لیے ان کا استعمال کریں جو آپ کے پاس نہیں ہیں (جیسے`string`یا`IEnumerable<T>`)۔ ان کے زیادہ استعمال سے گریز کریں - وہ کوڈ کو دریافت کرنا مشکل بنا سکتے ہیں۔
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

### Q4: جدید C# میں پیٹرن میچنگ کیسے کام کرتی ہے؟
**A:** C# نے بتدریج مزید طاقتور پیٹرن میچنگ کو شامل کیا ہے۔ سوئچ ایکسپریشنز (C# 8)، ٹائپ پیٹرن، پراپرٹی پیٹرن، رشتہ دار پیٹرن، اور فہرست پیٹرن (C# 11) مختصر، اظہار کن مشروط منطق کی اجازت دیتے ہیں۔ پیٹرن کی مماثلت لمبی if/else زنجیروں کی جگہ لے لیتی ہے اور کمپائلر کے ذریعے مکمل جانچ پڑتال کی جاتی ہے۔
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

### Q5: .NET میں انحصار انجیکشن کیا ہے، اور میں اسے کیسے استعمال کروں؟
**A:** .NET میں`Microsoft.Extensions.DependencyInjection`کے ذریعے بلٹ ان DI سپورٹ ہے۔ آپ خدمات کو ان کے لائف ٹائم (سنگلٹن، اسکوپڈ، عارضی) کے ساتھ رجسٹر کرتے ہیں، اور کنٹینر کنسٹرکٹر پیرامیٹرز کے ذریعے انہیں انجیکشن لگاتا ہے۔ سنگلٹن: ایپ کے لیے ایک مثال۔ دائرہ کار: ایک فی HTTP درخواست۔ عارضی: ہر بار نئی مثال۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: کیشنگ کے ساتھ ایک عام ذخیرہ بنائیں
**مسئلہ کا بیان:** ڈیکوریٹر کے ساتھ ایک عام ریپوزٹری پیٹرن کو لاگو کریں جو کیچنگ کا اضافہ کرتا ہے۔ ریپوزٹری کو CRUD آپریشنز کو سپورٹ کرنا چاہیے، اور کیشنگ ڈیکوریٹر کو ریڈز کو کیش کرنا چاہیے اور تحریروں پر باطل کرنا چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ایک عام`IRepository<T>`انٹرفیس، (2) ایک ٹھوس عمل درآمد (جیسے، میموری میں)، (3) ایک کیشنگ ڈیکوریٹر جو کسی بھی ذخیرہ کو لپیٹتا ہے، (4) تحریری کارروائیوں پر کیشے کی غلط کاری۔ ڈیکوریٹر پیٹرن ڈیٹا تک رسائی کی منطق کو آرتھوگونل کیش کرتا رہتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`IRepository<T>`کی وضاحت `Get`، `GetAll`، `Add`، `Update`،`Delete`کے ساتھ کریں۔
-`CachingRepository<T>`بنائیں جو`IRepository<T>`کو لپیٹے اور`IMemoryCache`استعمال کرے۔
- کیش کلید:`typeof(T).Name:{id}`۔
- تحریری کارروائیوں پر، کیشے کے اندراج کو باطل کر دیں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- خدشات کی علیحدگی: کیشنگ ایک ڈیکوریٹر ہے، مخزن میں نہیں ملایا جاتا۔
- DI رجسٹریشن:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(اسکروٹر کا استعمال کرتے ہوئے)۔
- پروڈکشن: ملٹی سرور منظرناموں کے لیے`IDistributedCache`(Redis) کا استعمال کریں، اور`CacheStampede`تحفظ کے ساتھ کیش-سائیڈ پیٹرن شامل کریں۔
### مسئلہ 2: ایک مڈل ویئر پائپ لائن لاگو کریں۔
**مسئلہ کا بیان:** ASP.NET کور کی درخواست پائپ لائن کی طرح ایک مڈل ویئر پائپ لائن بنائیں۔ ہر مڈل ویئر درخواست پر کارروائی کرسکتا ہے، اگلے مڈل ویئر کو کال کرسکتا ہے، اور جواب پر کارروائی کرسکتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) پائپ لائن کی نمائندگی کرنے والی ایک`RequestDelegate`قسم، (2) مڈل ویئر جو اگلے مندوب کو لپیٹتا ہے، (3) مڈل ویئر کمپوز کرنے کے لیے ایک بلڈر API۔ یہ ذمہ داری کا سلسلہ ہے جو مندوبین کے ساتھ نافذ کیا گیا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`RequestDelegate``Func<Context, RequestDelegate, Task>` ہے۔
- ہر مڈل ویئر کو سیاق و سباق اور ایک`next`فنکشن ملتا ہے۔
-`Use`مڈل ویئر کا اضافہ کرتا ہے۔ `Build`انہیں ایک ہی مندوب میں مرتب کرتا ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- مڈل ویئر آرڈر کے معاملات: پہلے شامل کیا گیا = سب سے باہر (درخواست پر پہلے پھانسی دی گئی، جواب پر آخری)۔
- ٹرمینل مڈل ویئر (کوئی`next`کال نہیں) پائپ لائن کو شارٹ سرکٹ کرتا ہے۔
- پیداوار: ASP.NET کور کی پائپ لائن بالکل اسی طرز کی ہے، جو صفر مختص کرنے کے لیے مرتب کردہ اظہار کے درختوں کے ساتھ بہتر ہے۔
---

## خلاصہ
C# بہترین ٹولنگ اور ایک مضبوط ماحولیاتی نظام کے ساتھ ایک پالش، جدید، عام مقصد کی زبان ہے۔ یہ انٹرپرائز ڈویلپمنٹ، گیم ڈویلپمنٹ (یونٹی) اور کراس پلیٹ فارم ایپلی کیشنز میں بہترین ہے۔ زبان تیزی سے تیار ہوئی ہے — جدید C# جامع، اظہار خیال، اور ٹائپ سیف ہے۔ اگرچہ اس میں جاوا یا Python کے ماحولیاتی نظام کا سائز نہیں ہے، .NET کا معیار اور مستقل مزاجی C# کو ایپلی کیشنز کی ایک وسیع رینج کے لیے ایک پیداواری اور خوشگوار زبان بناتی ہے۔