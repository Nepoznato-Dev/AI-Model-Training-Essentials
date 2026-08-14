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
# सी#
C# (उच्चारण "सी-शार्प") एक आधुनिक, ऑब्जेक्ट-ओरिएंटेड, टाइप-सुरक्षित प्रोग्रामिंग भाषा है जिसे माइक्रोसॉफ्ट द्वारा एंडर्स हेजलबर्ग के नेतृत्व में विकसित किया गया था और पहली बार 2002 में जारी किया गया था। यह .NET प्लेटफ़ॉर्म पर चलता है और इसे विज़ुअल बेसिक की उत्पादकता के साथ C++ की शक्ति को संयोजित करने के लिए डिज़ाइन किया गया था। आज, C# एक बहुमुखी, क्रॉस-प्लेटफ़ॉर्म भाषा है जिसका उपयोग वेब एप्लिकेशन (ASP.NET), डेस्कटॉप सॉफ़्टवेयर (Windows), गेम डेवलपमेंट (यूनिटी), मोबाइल ऐप्स (MAUI), क्लाउड सर्विसेज (Azure) और बहुत कुछ के लिए किया जाता है।
C# ने लगातार अन्य भाषाओं - LINQ, async/await, रिकॉर्ड्स, पैटर्न मिलान - से सर्वोत्तम विचारों को अवशोषित किया है, जिससे यह उपलब्ध सबसे अधिक सुविधा संपन्न और डेवलपर-अनुकूल भाषाओं में से एक बन गई है।
---

## सी# क्यों मायने रखता है
- **यूनिटी गेम इंजन**: यूनिटी के लिए प्राथमिक भाषा, डेवलपर गणना के अनुसार दुनिया का सबसे लोकप्रिय गेम इंजन।
- **उद्यम विकास**: ASP.NET कोर उपलब्ध सबसे तेज़ वेब फ्रेमवर्क में से एक है (टेकएम्पॉवर बेंचमार्क में लगातार शीर्ष पर है)।
- **क्रॉस-प्लेटफ़ॉर्म**: .NET 5+ विंडोज़, मैकओएस और लिनक्स पर चलता है। अब केवल विंडोज़ नहीं।
- **उत्पादकता**: उत्कृष्ट आईडीई समर्थन (विजुअल स्टूडियो, राइडर), मजबूत प्रकार की प्रणाली और आधुनिक सिंटैक्स विशेषताएं।
- **async/await अग्रणी**: C# ने 2012 में async/await की शुरुआत की - अन्य भाषाओं द्वारा इस पैटर्न को अपनाने से कई साल पहले।
- **LINQ**: भाषा-एकीकृत क्वेरी आपको किसी भी डेटा स्रोत के विरुद्ध सीधे C# में SQL जैसी क्वेरी लिखने की सुविधा देती है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **विंडोज एसोसिएशन** | ऐतिहासिक रूप से विंडोज़ से जुड़ा हुआ; धारणा वास्तविकता से पीछे है | .NET 6+ पूरी तरह से क्रॉस-प्लेटफॉर्म है |
| **जावा से छोटा पारिस्थितिकी तंत्र** | Maven/PyPI | की तुलना में कम तृतीय-पक्ष लाइब्रेरीज़ नुगेट बढ़ रहा है; कई जावा पुस्तकालयों में C# समकक्ष हैं |
| **स्टार्टअप में कम आम** | सिलिकॉन वैली की तुलना में उद्यम में अधिक लोकप्रिय | क्लाउड-नेटिव माइक्रोसर्विसेज के लिए गो, रस्ट, नोड.जेएस |
| **मोबाइल (MAUI)** | Xamarin/MAUI देशी या फ़्लटर | की तुलना में कम परिपक्व है जटिल मोबाइल ऐप्स के लिए देशी स्विफ्ट/कोटलिन या फ़्लटर का उपयोग करें |
| **लिनक्स जीयूआई** | Linux पर सीमित देशी GUI विकल्प | वेब-आधारित यूआई (ब्लेज़र) या एवलोनिया | का उपयोग करें
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
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

### ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग
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

### रिकॉर्ड्स (सी# 9+) - अपरिवर्तनीय डेटा प्रकार
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

### LINQ - भाषा-एकीकृत क्वेरी
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

### एसिंक/प्रतीक्षा करें
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

### पैटर्न मिलान (सी# 7-13)
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

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक
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

### प्रतिनिधि, घटनाएँ, और लैम्ब्डा अभिव्यक्तियाँ
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

### कस्टम अपवाद पदानुक्रम
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

### ऑपरेटर ओवरलोडिंग
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

## समवर्ती एवं समांतरता
### एसिंक/प्रतीक्षा आंतरिक
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

### समानांतर LINQ और कार्य समानांतर लाइब्रेरी
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### .csproj फ़ाइल
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

### xUnit के साथ परीक्षण
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

### सीआई/सीडी पाइपलाइन
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

## अंतरसंचालनीयता
### पी/इनवोक - सी लाइब्रेरीज़ को कॉल करना
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

### सी++/सीएलआई इंटरऑप
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

## डिज़ाइन पैटर्न
### बिल्डर पैटर्न (धाराप्रवाह एपीआई)
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

### प्रतिनिधियों के साथ रणनीति पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

## तैनाती
### डॉकरफ़ाइल
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

### प्लेटफ़ॉर्म-विशिष्ट परिनियोजन
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

## .NET पारिस्थितिकी तंत्र
### फ्रेमवर्क और प्लेटफार्म
| ढाँचा | डोमेन | विवरण |
|----|-------|----|
| **एएसपी.नेट कोर** | वेब | एपीआई और वेब ऐप्स के लिए उच्च-प्रदर्शन वेब फ्रेमवर्क |
| **ब्लेज़र** | वेब (फ्रंटएंड) | जावास्क्रिप्ट | के बजाय C# के साथ इंटरैक्टिव वेब यूआई बनाएं
| **एंटिटी फ्रेमवर्क कोर** | ओआरएम | LINQ के साथ डेटाबेस का उपयोग; कोड-प्रथम माइग्रेशन |
| **एकता** | गेम्स | दुनिया का सबसे लोकप्रिय गेम इंजन (सी# स्क्रिप्टिंग) |
| **.नेट माउई** | मोबाइल/डेस्कटॉप | iOS, Android, macOS, Windows के लिए क्रॉस-प्लेटफ़ॉर्म ऐप्स |
| **एवलोनिया** | डेस्कटॉप | क्रॉस-प्लेटफ़ॉर्म डेस्कटॉप यूआई (जैसे सभी प्लेटफ़ॉर्म के लिए WPF) |
### निर्माण और पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **डॉटनेट सीएलआई** | कमांड लाइन से बनाएं, चलाएं, परीक्षण करें, प्रकाशित करें |
| **नुगेट** | पैकेज मैनेजर |
| **एमएसबिल्ड** | अंतर्निहित निर्माण प्रणाली |
| **विजुअल स्टूडियो/राइडर** | आईडीई |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## सी# भाषा संस्करण
| संस्करण | वर्ष | प्रमुख विशेषताएँ |
|------|------|----------------|
| सी# 7 | 2017 | पैटर्न मिलान, टुपल्स,`out`वेरिएबल, स्थानीय फ़ंक्शन |
| सी# 8 | 2019 | अशक्त संदर्भ प्रकार,`switch`अभिव्यक्ति, एसिंक स्ट्रीम |
| सी#9 | 2020 | **रिकॉर्ड**, शीर्ष-स्तरीय विवरण,`init`गुण |
| सी#10 | 2021 | रिकॉर्ड संरचनाएं, वैश्विक `using`, फ़ाइल-स्कोप्ड नेमस्पेस |
| सी#11 | 2022 | कच्चे स्ट्रिंग अक्षर, सूची पैटर्न,`required`सदस्य, सामान्य गणित |
| सी#12 | 2023 | प्राथमिक कंस्ट्रक्टर, संग्रह अभिव्यक्ति, इनलाइन सरणियाँ |
| सी#13 | 2024 | `params`संग्रह, नए लॉक प्रकार, प्रथम श्रेणी स्पैन |
---

## सी# का उपयोग कब करें
| परिदृश्य | सी# क्यों | बेहतर विकल्प |
|---|--------|-----|
| खेल विकास (एकता) | मानक यूनिटी स्क्रिप्टिंग भाषा | -- |
| एंटरप्राइज़ वेब बैकएंड | ASP.NET कोर तेज़, परिपक्व, अच्छी तरह से समर्थित है | जावा (स्प्रिंग बूट) |
| विंडोज़ डेस्कटॉप अनुप्रयोग | WPF, WinForms, WinUI परिपक्व हैं | -- |
| क्रॉस-प्लेटफ़ॉर्म डेस्कटॉप | एवलोनिया या माउई | इलेक्ट्रॉन (वेब-आधारित) |
| वेब फ्रंटएंड (ब्लेज़र) | पूर्ण-स्टैक C# - कोई जावास्क्रिप्ट की आवश्यकता नहीं | समृद्ध एसपीए पारिस्थितिकी तंत्र के लिए प्रतिक्रिया/व्यू/कोणीय |
| क्लाउड सेवाएँ (एज़्योर) | डीप एज़्योर एकीकरण | -- |
| मोबाइल ऐप्स (MAUI) | C# | के साथ क्रॉस-प्लेटफ़ॉर्म फ़्लटर, रिएक्ट नेटिव, या नेटिव स्विफ्ट/कोटलिन |
| एआई/एमएल | ML.NET के साथ संभव | पायथन (अत्यधिक पसंदीदा) |
| सीएलआई उपकरण/स्क्रिप्ट | संभव लेकिन क्रियात्मक | जाओ, जंग, अजगर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: C# में`class`और`record`के बीच क्या अंतर है?
**ए:** एक`class`एक संदर्भ प्रकार है जिसमें डिफ़ॉल्ट रूप से परिवर्तनशील गुण होते हैं - दो चर एक ही ऑब्जेक्ट को संदर्भित कर सकते हैं।`record`(C# 9+) मूल्य-आधारित समानता वाला एक संदर्भ प्रकार है - समान डेटा वाले दो रिकॉर्ड समान माने जाते हैं। रिकॉर्ड्स में केवल init गुण हैं, एक अंतर्निहित`ToString`है, और गैर-विनाशकारी उत्परिवर्तन के लिए`with`अभिव्यक्तियों का समर्थन करता है। डेटा वाहक (डीटीओ, मूल्य ऑब्जेक्ट) के लिए रिकॉर्ड का उपयोग करें; पहचान के साथ व्यवहार-समृद्ध संस्थाओं के लिए कक्षाओं का उपयोग करें।
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

### Q2: async/await और`Task`आंतरिक रूप से कैसे काम करते हैं?
**ए:**`async/await`कंपाइलर द्वारा उत्पन्न एक राज्य मशीन पर वाक्यात्मक चीनी है। जब आप`await`को`Task`करते हैं, तो विधि प्रतीक्षा बिंदु पर विभाजित हो जाती है: पहले सब कुछ समकालिक रूप से निष्पादित होता है, फिर शेष को निरंतरता के रूप में पंजीकृत किया जाता है। धागा अन्य कार्य करने के लिए स्वतंत्र है। `Task<T>`भविष्य के मूल्य का प्रतिनिधित्व करता है। `ValueTask<T>`हॉट पाथ के लिए एक संरचनात्मक विकल्प है जो परिणाम पहले से ही उपलब्ध होने पर ढेर आवंटन से बचता है।
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

### प्रश्न 3: विस्तार विधियाँ क्या हैं, और मुझे उनका उपयोग कब करना चाहिए?
**ए:** एक्सटेंशन विधियां मौजूदा प्रकारों को संशोधित किए बिना उनमें विधियां जोड़ती हैं। वे एक स्थिर वर्ग में स्थिर विधियाँ हैं, पहले पैरामीटर पर`this`कीवर्ड के साथ। वे एक धाराप्रवाह, श्रृंखलाबद्ध एपीआई सक्षम करते हैं। उन प्रकारों में उपयोगिता विधियां जोड़ने के लिए उनका उपयोग करें जो आपके पास नहीं हैं (जैसे`string`या `IEnumerable<T>`)। उनका अत्यधिक उपयोग करने से बचें - वे कोड को खोजना कठिन बना सकते हैं।
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

### Q4: आधुनिक C# में पैटर्न मिलान कैसे काम करता है?
**ए:** सी# ने उत्तरोत्तर अधिक शक्तिशाली पैटर्न मिलान जोड़ा है। स्विच अभिव्यक्ति (सी # 8), प्रकार पैटर्न, संपत्ति पैटर्न, संबंधपरक पैटर्न, और सूची पैटर्न (सी # 11) संक्षिप्त, अभिव्यंजक सशर्त तर्क की अनुमति देते हैं। पैटर्न मिलान लंबी if/else श्रृंखलाओं को प्रतिस्थापित करता है और कंपाइलर द्वारा इसकी संपूर्ण जांच की जाती है।
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

### Q5: .NET में निर्भरता इंजेक्शन क्या है, और मैं इसका उपयोग कैसे करूँ?
**ए:** .NET में`Microsoft.Extensions.DependencyInjection`के माध्यम से अंतर्निहित DI समर्थन है। आप सेवाओं को उनके जीवनकाल (सिंगलटन, स्कोप्ड, ट्रांसिएंट) के साथ पंजीकृत करते हैं, और कंटेनर उन्हें कंस्ट्रक्टर मापदंडों के माध्यम से इंजेक्ट करता है। सिंगलटन: ऐप के लिए एक उदाहरण। दायरा: प्रति HTTP अनुरोध एक। क्षणिक: हर बार नया उदाहरण।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: कैशिंग के साथ एक सामान्य रिपॉजिटरी बनाएं
**समस्या कथन:** एक डेकोरेटर के साथ एक सामान्य रिपॉजिटरी पैटर्न लागू करें जो कैशिंग जोड़ता है। रिपॉजिटरी को सीआरयूडी संचालन का समर्थन करना चाहिए, और कैशिंग डेकोरेटर को पढ़ने को कैश करना चाहिए और लिखने पर अमान्य करना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) एक सामान्य`IRepository<T>`इंटरफ़ेस, (2) एक ठोस कार्यान्वयन (उदाहरण के लिए, इन-मेमोरी), (3) एक कैशिंग डेकोरेटर जो किसी भी रिपॉजिटरी को लपेटता है, (4) लिखने के संचालन पर कैश अमान्यकरण। डेकोरेटर पैटर्न डेटा एक्सेस लॉजिक के लिए ऑर्थोगोनल कैशिंग रखता है।
**चरण 2 - दृष्टिकोण को पहचानें:**
-`Get`,`GetAll`,`Add`,`Update`,`Delete`के साथ`IRepository<T>`को परिभाषित करें।
-`CachingRepository<T>`बनाएं जो`IRepository<T>`को लपेटता है और`IMemoryCache`का उपयोग करता है।
- कैश कुंजी: `typeof(T).Name:{id}`।
- लिखने के संचालन पर, कैश प्रविष्टि को अमान्य करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- चिंताओं का पृथक्करण: कैशिंग एक डेकोरेटर है, रिपॉजिटरी में मिश्रित नहीं।
- डीआई पंजीकरण:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(स्क्रूटर का उपयोग करके)।
- उत्पादन: मल्टी-सर्वर परिदृश्यों के लिए`IDistributedCache`(Redis) का उपयोग करें, और`CacheStampede`सुरक्षा के साथ कैश-साइड पैटर्न जोड़ें।
### समस्या 2: एक मिडलवेयर पाइपलाइन लागू करें
**समस्या कथन:** ASP.NET कोर के अनुरोध पाइपलाइन के समान एक मिडलवेयर पाइपलाइन बनाएं। प्रत्येक मिडलवेयर अनुरोध को संसाधित कर सकता है, अगले मिडलवेयर को कॉल कर सकता है और प्रतिक्रिया को संसाधित कर सकता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) पाइपलाइन का प्रतिनिधित्व करने वाला एक`RequestDelegate`प्रकार, (2) मिडलवेयर जो अगले प्रतिनिधि को लपेटता है, (3) मिडलवेयर बनाने के लिए एक बिल्डर एपीआई। यह प्रतिनिधियों के साथ क्रियान्वित उत्तरदायित्व श्रृंखला पैटर्न है।
**चरण 2 - दृष्टिकोण को पहचानें:**
-`RequestDelegate``Func<Context, RequestDelegate, Task>` है।
- प्रत्येक मिडलवेयर को संदर्भ और एक`next`फ़ंक्शन प्राप्त होता है।
-`Use`मिडलवेयर जोड़ता है; `Build`उन्हें एक एकल प्रतिनिधि में संयोजित करता है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- मिडलवेयर ऑर्डर मायने रखता है: सबसे पहले जोड़ा गया = सबसे बाहरी (अनुरोध पर पहले निष्पादित, प्रतिक्रिया पर अंतिम)।
- टर्मिनल मिडलवेयर (कोई`next`कॉल नहीं) पाइपलाइन को शॉर्ट-सर्किट करता है।
- उत्पादन: ASP.NET कोर की पाइपलाइन बिल्कुल इसी पैटर्न पर है, जो शून्य आवंटन के लिए संकलित अभिव्यक्ति पेड़ों के साथ अनुकूलित है।
---

## सारांश
C# उत्कृष्ट टूलींग और एक मजबूत पारिस्थितिकी तंत्र के साथ एक परिष्कृत, आधुनिक, सामान्य प्रयोजन वाली भाषा है। यह उद्यम विकास, खेल विकास (यूनिटी), और क्रॉस-प्लेटफ़ॉर्म अनुप्रयोगों में उत्कृष्टता प्राप्त करता है। भाषा तेजी से विकसित हुई है - आधुनिक C# संक्षिप्त, अभिव्यंजक और प्रकार-सुरक्षित है। हालाँकि इसमें जावा या पायथन का पारिस्थितिकी तंत्र आकार नहीं है, .NET की गुणवत्ता और स्थिरता C# को अनुप्रयोगों की एक विस्तृत श्रृंखला के लिए एक उत्पादक और आनंददायक भाषा बनाती है।