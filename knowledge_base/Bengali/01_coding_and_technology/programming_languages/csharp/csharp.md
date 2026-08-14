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
# সি#
C# (উচ্চারিত "C-sharp") একটি আধুনিক, অবজেক্ট-ওরিয়েন্টেড, টাইপ-নিরাপদ প্রোগ্রামিং ভাষা অ্যান্ডার্স হেজলসবার্গের নেতৃত্বে মাইক্রোসফ্ট দ্বারা বিকাশ করা হয়েছে এবং 2002 সালে প্রথম প্রকাশিত হয়েছে। এটি .NET প্ল্যাটফর্মে চলে এবং ভিজ্যুয়াল বেসিকের উত্পাদনশীলতার সাথে C++ এর শক্তিকে একত্রিত করার জন্য ডিজাইন করা হয়েছিল। আজ, C# হল একটি বহুমুখী, ক্রস-প্ল্যাটফর্ম ভাষা যা ওয়েব অ্যাপ্লিকেশন (ASP.NET), ডেস্কটপ সফ্টওয়্যার (উইন্ডোজ), গেম ডেভেলপমেন্ট (ইউনিটি), মোবাইল অ্যাপস (MAUI), ক্লাউড পরিষেবা (Azure) এবং আরও অনেক কিছুর জন্য ব্যবহৃত হয়।
C# অবিচ্ছিন্নভাবে অন্যান্য ভাষার সেরা ধারণাগুলিকে শোষণ করেছে — LINQ, async/await, রেকর্ড, প্যাটার্ন ম্যাচিং — এটিকে উপলব্ধ সবচেয়ে বৈশিষ্ট্য সমৃদ্ধ এবং বিকাশকারী-বান্ধব ভাষাগুলির মধ্যে একটি করে তুলেছে।
---

## কেন C# ব্যাপার
- **ইউনিটি গেম ইঞ্জিন**: ইউনিটির প্রাথমিক ভাষা, ডেভেলপারের সংখ্যা অনুসারে বিশ্বের সবচেয়ে জনপ্রিয় গেম ইঞ্জিন।
- **এন্টারপ্রাইজ ডেভেলপমেন্ট**: ASP.NET কোর হল সবচেয়ে দ্রুত উপলব্ধ ওয়েব ফ্রেমওয়ার্কগুলির মধ্যে একটি (সঙ্গতভাবে TechEmpower বেঞ্চমার্কের শীর্ষে)।
- **ক্রস-প্ল্যাটফর্ম**: .NET 5+ Windows, macOS এবং Linux-এ চলে। আর শুধুমাত্র উইন্ডোজ নয়।
- **উৎপাদনশীলতা**: চমৎকার IDE সমর্থন (ভিজ্যুয়াল স্টুডিও, রাইডার), শক্তিশালী টাইপ সিস্টেম এবং আধুনিক সিনট্যাক্স বৈশিষ্ট্য।
- **async/await pioneer**: C# 2012 সালে async/await চালু করেছিল — অন্যান্য ভাষা প্যাটার্নটি গ্রহণ করার কয়েক বছর আগে।
- **LINQ**: ভাষা-ইন্টিগ্রেটেড ক্যোয়ারী আপনাকে যেকোন ডেটা উৎসের বিপরীতে সরাসরি C# এ SQL-এর মতো প্রশ্ন লিখতে দেয়।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **উইন্ডোজ এসোসিয়েশন** | ঐতিহাসিকভাবে উইন্ডোজের সাথে আবদ্ধ; উপলব্ধি বাস্তবতা থেকে পিছিয়ে | .NET 6+ সম্পূর্ণ ক্রস-প্ল্যাটফর্ম |
| **জাভার থেকে ছোট ইকোসিস্টেম** | Maven/PyPI এর চেয়ে কম তৃতীয় পক্ষের লাইব্রেরি | NuGet বাড়ছে; অনেক জাভা লাইব্রেরিতে C# সমতুল্য আছে |
| **স্টার্টআপে কম সাধারণ** | সিলিকন ভ্যালির চেয়ে এন্টারপ্রাইজে বেশি জনপ্রিয় | ক্লাউড-নেটিভ মাইক্রোসার্ভিসের জন্য Go, Rust, Node.js |
| **মোবাইল (MAUI)** | Xamarin/MAUI নেটিভ বা ফ্লটারের চেয়ে কম পরিপক্ক | জটিল মোবাইল অ্যাপের জন্য নেটিভ সুইফট/কোটলিন বা ফ্লটার ব্যবহার করুন
| **লিনাক্স GUI** | লিনাক্সে সীমিত নেটিভ GUI বিকল্প | ওয়েব-ভিত্তিক UIs (Blazor) বা Avalonia | ব্যবহার করুন
---

## সিনট্যাক্স মৌলিক
### মৌলিক কাঠামো
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

### অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং
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

### রেকর্ড (C# 9+) — অপরিবর্তনীয় ডেটা টাইপ
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

### LINQ — ভাষা-সমন্বিত প্রশ্ন
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

### অ্যাসিঙ্ক/অপেক্ষা করুন
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

### প্যাটার্ন ম্যাচিং (C# 7-13)
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক
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

### প্রতিনিধি, ইভেন্ট এবং ল্যাম্বডা এক্সপ্রেশন
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

### কাস্টম ব্যতিক্রম শ্রেণিবিন্যাস
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

### অপারেটর ওভারলোডিং
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

## সামঞ্জস্য এবং সমান্তরালতা
### অ্যাসিঙ্ক/অভ্যন্তরীণ অপেক্ষা করুন
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

### সমান্তরাল LINQ এবং টাস্ক সমান্তরাল লাইব্রেরি
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
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

### .csproj ফাইল
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

### xUnit দিয়ে পরীক্ষা করা হচ্ছে
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

### CI/CD পাইপলাইন
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

## ইন্টারঅপারেবিলিটি
### পি/ইনভোক — কলিং সি লাইব্রেরি
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

### C++/CLI ইন্টারপ
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

## ডিজাইন প্যাটার্ন
### বিল্ডার প্যাটার্ন (ফ্লুয়েন্ট এপিআই)
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

### প্রতিনিধিদের সাথে কৌশল প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

## স্থাপনা
### ডকারফাইল
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

### প্ল্যাটফর্ম-নির্দিষ্ট স্থাপনা
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

## .নেট ইকোসিস্টেম
### ফ্রেমওয়ার্ক এবং প্ল্যাটফর্ম
| ফ্রেমওয়ার্ক | ডোমেন | বর্ণনা |
|------------|---------|---------------|
| **ASP.NET কোর** | ওয়েব | API এবং ওয়েব অ্যাপের জন্য উচ্চ-পারফরম্যান্স ওয়েব ফ্রেমওয়ার্ক |
| **ব্লেজার** | ওয়েব (ফ্রন্টেন্ড) | JavaScript এর পরিবর্তে C# দিয়ে ইন্টারেক্টিভ ওয়েব UI তৈরি করুন |
| **এন্টিটি ফ্রেমওয়ার্ক কোর** | ORM | LINQ এর সাথে ডেটাবেস অ্যাক্সেস; কোড-প্রথম মাইগ্রেশন |
| **ঐক্য** | গেমস | বিশ্বের সবচেয়ে জনপ্রিয় গেম ইঞ্জিন (C# স্ক্রিপ্টিং) |
| **.নেট মাউই** | মোবাইল/ডেস্কটপ | iOS, Android, macOS, Windows এর জন্য ক্রস-প্ল্যাটফর্ম অ্যাপ
| **অ্যাভালোনিয়া** | ডেস্কটপ | ক্রস-প্ল্যাটফর্ম ডেস্কটপ UI (যেমন সব প্ল্যাটফর্মের জন্য WPF) |
### বিল্ড এবং প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **ডটনেট CLI** | কমান্ড লাইন থেকে তৈরি করুন, চালান, পরীক্ষা করুন, প্রকাশ করুন |
| **নুগেট** | প্যাকেজ ম্যানেজার |
| **MSBuild** | অন্তর্নিহিত বিল্ড সিস্টেম |
| **ভিজ্যুয়াল স্টুডিও / রাইডার** | IDEs |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# ভাষার সংস্করণ
| সংস্করণ | বছর | মূল বৈশিষ্ট্য |
|---------|------|---------------|
| C# 7 | 2017 | প্যাটার্ন ম্যাচিং, টিপলস,`out`ভেরিয়েবল, স্থানীয় ফাংশন |
| C# 8 | 2019 | বাতিলযোগ্য রেফারেন্স প্রকার,`switch`এক্সপ্রেশন, অ্যাসিঙ্ক স্ট্রীম |
| C# 9 | 2020 | **রেকর্ড**, শীর্ষ-স্তরের বিবৃতি,`init`বৈশিষ্ট্য |
| C# 10 | 2021 | রেকর্ড স্ট্রাকস, গ্লোবাল`using`, ফাইল-স্কোপড নেমস্পেস |
| C# 11 | 2022 | কাঁচা স্ট্রিং আক্ষরিক, তালিকা প্যাটার্ন,`required`সদস্য, জেনেরিক গণিত |
| সি# 12 | 2023 | প্রাথমিক কনস্ট্রাক্টর, সংগ্রহ এক্সপ্রেশন, ইনলাইন অ্যারে |
| C# 13 | 2024 | `params`সংগ্রহ, নতুন লক প্রকার, প্রথম শ্রেণীর স্প্যান |
---

## কখন C# ব্যবহার করবেন
| দৃশ্যকল্প | কেন C# | ভাল বিকল্প |
|------------|---------|---------|
| গেম ডেভেলপমেন্ট (ইউনিটি) | স্ট্যান্ডার্ড ইউনিটি স্ক্রিপ্টিং ভাষা | -- |
| এন্টারপ্রাইজ ওয়েব ব্যাকএন্ড | ASP.NET কোর দ্রুত, পরিপক্ক, ভাল-সমর্থিত | জাভা (স্প্রিং বুট) |
| উইন্ডোজ ডেস্কটপ অ্যাপ্লিকেশন | WPF, WinForms, WinUI পরিপক্ক | -- |
| ক্রস-প্ল্যাটফর্ম ডেস্কটপ | অ্যাভালোনিয়া বা MAUI | ইলেক্ট্রন (ওয়েব-ভিত্তিক) |
| ওয়েব ফ্রন্টএন্ড (ব্লেজার) | ফুল-স্ট্যাক C# — কোনো জাভাস্ক্রিপ্টের প্রয়োজন নেই আরও সমৃদ্ধ এসপিএ ইকোসিস্টেমের জন্য প্রতিক্রিয়া/ভ্যু/কৌণিক |
| ক্লাউড পরিষেবা (আজিউর) | ডিপ অ্যাজুর ইন্টিগ্রেশন | -- |
| মোবাইল অ্যাপস (MAUI) | C# এর সাথে ক্রস-প্ল্যাটফর্ম | ফ্লটার, রিঅ্যাক্ট নেটিভ বা নেটিভ সুইফট/কোটলিন |
| AI/ML | ML.NET এর সাথে সম্ভব | পাইথন (অপ্রতিরোধ্যভাবে পছন্দ করা) |
| CLI টুলস / স্ক্রিপ্ট | সম্ভাব্য কিন্তু শব্দসমৃদ্ধ | যান, মরিচা, পাইথন |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: C# এ`class`এবং`record`এর মধ্যে পার্থক্য কী?
**A:** একটি`class`হল একটি রেফারেন্স টাইপ যার মধ্যে ডিফল্টভাবে পরিবর্তনযোগ্য বৈশিষ্ট্য রয়েছে — দুটি ভেরিয়েবল একই বস্তুকে উল্লেখ করতে পারে। একটি`record`(C# 9+) হল মান-ভিত্তিক সমতা সহ একটি রেফারেন্স টাইপ — একই ডেটা সহ দুটি রেকর্ড সমান বলে বিবেচিত হয়। রেকর্ডগুলিতে শুধুমাত্র-ইনিট বৈশিষ্ট্য রয়েছে, একটি অন্তর্নির্মিত `ToString`, এবং অ-ধ্বংসাত্মক মিউটেশনের জন্য`with`এক্সপ্রেশন সমর্থন করে। ডেটা ক্যারিয়ারের জন্য রেকর্ড ব্যবহার করুন (ডিটিও, মান অবজেক্ট); পরিচয় সহ আচরণ সমৃদ্ধ সত্ত্বার জন্য ক্লাস ব্যবহার করুন।
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

### প্রশ্ন 2: কিভাবে async/await এবং`Task`অভ্যন্তরীণভাবে কাজ করে?
**A:**`async/await`হল কম্পাইলার দ্বারা উত্পন্ন একটি স্টেট মেশিনের উপর সিনট্যাকটিক চিনি। আপনি যখন`await`একটি `Task`, পদ্ধতিটি অপেক্ষমাণ বিন্দুতে বিভক্ত করা হয়: আগে সবকিছু সিঙ্ক্রোনাসভাবে কার্যকর করা হয়, তারপর অবশিষ্টাংশ একটি ধারাবাহিকতা হিসাবে নিবন্ধিত হয়। থ্রেড অন্য কাজ করতে মুক্ত হয়. `Task<T>`একটি ভবিষ্যত মান উপস্থাপন করে। `ValueTask<T>`হল হট পাথের জন্য একটি স্ট্রাকট বিকল্প যা ফলাফল ইতিমধ্যে উপলব্ধ হলে হিপ বরাদ্দ এড়িয়ে যায়।
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

### প্রশ্ন 3: এক্সটেনশন পদ্ধতি কি এবং কখন সেগুলি ব্যবহার করব?
**A:** এক্সটেনশন পদ্ধতিগুলি বিদ্যমান প্রকারগুলিকে পরিবর্তন না করেই পদ্ধতিগুলিকে যুক্ত করে৷ তারা একটি স্ট্যাটিক ক্লাসে স্ট্যাটিক পদ্ধতি, প্রথম প্যারামিটারে`this`কীওয়ার্ড রয়েছে। তারা একটি সাবলীল, চেইনযোগ্য API সক্ষম করে। আপনার মালিকানাধীন নয় (যেমন`string`বা `IEnumerable<T>`) ধরনের ইউটিলিটি পদ্ধতি যোগ করতে সেগুলি ব্যবহার করুন। তাদের অতিরিক্ত ব্যবহার করা এড়িয়ে চলুন - তারা কোড আবিষ্কার করা কঠিন করতে পারে।
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

### প্রশ্ন 4: আধুনিক C# এ প্যাটার্ন ম্যাচিং কিভাবে কাজ করে?
**A:** C# ক্রমান্বয়ে আরও শক্তিশালী প্যাটার্ন ম্যাচিং যোগ করেছে। স্যুইচ এক্সপ্রেশন (C# 8), টাইপ প্যাটার্ন, প্রপার্টি প্যাটার্ন, রিলেশনাল প্যাটার্ন, এবং লিস্ট প্যাটার্ন (C# 11) সংক্ষিপ্ত, এক্সপ্রেসিভ কন্ডিশনাল লজিক মঞ্জুরি দেয়। প্যাটার্ন ম্যাচিং লং if/else চেইন প্রতিস্থাপন করে এবং কম্পাইলার দ্বারা সম্পূর্ণ-চেক করা হয়।
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

### প্রশ্ন 5: .NET-এ নির্ভরতা ইনজেকশন কী এবং আমি কীভাবে এটি ব্যবহার করব?
**A:** .NET-এ`Microsoft.Extensions.DependencyInjection`এর মাধ্যমে বিল্ট-ইন DI সমর্থন রয়েছে। আপনি তাদের জীবনকালের (সিঙ্গেলটন, স্কোপড, ক্ষণস্থায়ী) সাথে পরিষেবাগুলি নিবন্ধন করেন এবং কন্টেইনারটি কনস্ট্রাক্টর প্যারামিটারের মাধ্যমে তাদের ইনজেকশন দেয়। সিঙ্গেলটন: অ্যাপের জন্য একটি উদাহরণ। স্কোপড: প্রতি HTTP অনুরোধে একটি। ক্ষণস্থায়ী: প্রতিবার নতুন উদাহরণ।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: ক্যাশিং সহ একটি জেনেরিক রিপোজিটরি তৈরি করুন
**সমস্যা বিবৃতি:** একটি ডেকোরেটরের সাথে একটি জেনেরিক রিপোজিটরি প্যাটার্ন প্রয়োগ করুন যা ক্যাশিং যোগ করে। সংগ্রহস্থলের CRUD ক্রিয়াকলাপগুলিকে সমর্থন করা উচিত, এবং ক্যাশিং ডেকোরেটরকে ক্যাশে পড়া এবং লেখার উপর বাতিল করা উচিত।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) একটি জেনেরিক`IRepository<T>`ইন্টারফেস, (2) একটি কংক্রিট বাস্তবায়ন (যেমন, ইন-মেমরি), (3) একটি ক্যাশিং ডেকোরেটর যা যেকোনো সংগ্রহস্থলকে মোড়ানো, (4) লেখার ক্রিয়াকলাপে ক্যাশে অবৈধকরণ। ডেকোরেটর প্যাটার্ন ডেটা অ্যাক্সেস লজিকের জন্য অর্থোগোনাল ক্যাশিং রাখে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- `IRepository<T>`-কে `Get`, `GetAll`, `Add`, `Update`,`Delete`দিয়ে সংজ্ঞায়িত করুন।
-`CachingRepository<T>`তৈরি করুন যা`IRepository<T>`মোড়ানো এবং`IMemoryCache`ব্যবহার করে৷
- ক্যাশে কী: `typeof(T).Name:{id}`।
- লেখার ক্রিয়াকলাপে, ক্যাশে এন্ট্রি বাতিল করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- উদ্বেগের বিচ্ছেদ: ক্যাশিং একটি ডেকোরেটর, ভান্ডারে মিশ্রিত নয়।
- DI নিবন্ধন:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(স্ক্রুটার ব্যবহার করে)।
- উৎপাদন: মাল্টি-সার্ভার পরিস্থিতির জন্য`IDistributedCache`(Redis) ব্যবহার করুন এবং`CacheStampede`সুরক্ষা সহ ক্যাশে-সাইড প্যাটার্ন যোগ করুন।
### সমস্যা 2: একটি মিডলওয়্যার পাইপলাইন প্রয়োগ করুন
**সমস্যা বিবৃতি:** ASP.NET কোরের অনুরোধ পাইপলাইনের মতো একটি মিডলওয়্যার পাইপলাইন তৈরি করুন। প্রতিটি মিডলওয়্যার অনুরোধ প্রক্রিয়া করতে পারে, পরবর্তী মিডলওয়্যারকে কল করতে পারে এবং প্রতিক্রিয়া প্রক্রিয়া করতে পারে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) একটি`RequestDelegate`টাইপ পাইপলাইন প্রতিনিধিত্ব করে, (2) মিডলওয়্যার যা পরবর্তী প্রতিনিধিকে মোড়ানো, (3) মিডলওয়্যার রচনা করার জন্য একটি নির্মাতা API। এটি হল চেইন অফ রেসপনসিবিলিটি প্যাটার্ন যা প্রতিনিধিদের সাথে প্রয়োগ করা হয়েছে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
-`RequestDelegate`হল `Func<Context, RequestDelegate, Task>`।
- প্রতিটি মিডলওয়্যার প্রসঙ্গ এবং একটি`next`ফাংশন গ্রহণ করে।
-`Use`মিডলওয়্যার যোগ করে; `Build`তাদের একটি একক প্রতিনিধিতে রচনা করে।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- মিডলওয়্যার অর্ডারের বিষয়: প্রথম যোগ করা = বাইরেরতম (অনুরোধে প্রথমে কার্যকর করা হয়, প্রতিক্রিয়ায় শেষ)।
- টার্মিনাল মিডলওয়্যার (কোনও`next`কল নেই) পাইপলাইনে শর্ট-সার্কিট করে।
- উত্পাদন: ASP.NET কোরের পাইপলাইনটি ঠিক এই প্যাটার্ন, শূন্য বরাদ্দের জন্য সংকলিত এক্সপ্রেশন ট্রিগুলির সাথে অপ্টিমাইজ করা হয়েছে।
---

## সারাংশ
C# চমৎকার টুলিং এবং একটি শক্তিশালী ইকোসিস্টেম সহ একটি পালিশ, আধুনিক, সাধারণ-উদ্দেশ্যের ভাষা। এটি এন্টারপ্রাইজ ডেভেলপমেন্ট, গেম ডেভেলপমেন্ট (ইউনিটি), এবং ক্রস-প্ল্যাটফর্ম অ্যাপ্লিকেশনে উৎকর্ষ। ভাষাটি দ্রুত বিকশিত হয়েছে — আধুনিক C# সংক্ষিপ্ত, অভিব্যক্তিপূর্ণ এবং টাইপ-নিরাপদ। যদিও এটিতে জাভা বা পাইথনের বাস্তুতন্ত্রের আকার নেই, .NET-এর গুণমান এবং ধারাবাহিকতা C# কে বিস্তৃত অ্যাপ্লিকেশনের জন্য একটি উত্পাদনশীল এবং উপভোগ্য ভাষা করে তোলে।