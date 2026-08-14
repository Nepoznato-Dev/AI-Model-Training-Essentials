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
#ج#
C# (تُنطق "C-sharp") هي لغة برمجة حديثة موجهة للكائنات وآمنة للنوع، طورتها شركة Microsoft تحت قيادة Anders Hejlsberg وتم إصدارها لأول مرة في عام 2002. وهي تعمل على النظام الأساسي .NET وقد تم تصميمها للجمع بين قوة C++ وإنتاجية Visual Basic. اليوم، تعد لغة C# لغة متعددة المنصات تستخدم لتطبيقات الويب (ASP.NET)، وبرامج سطح المكتب (Windows)، وتطوير الألعاب (Unity)، وتطبيقات الهاتف المحمول (MAUI)، والخدمات السحابية (Azure)، والمزيد.
لقد استوعبت لغة C# بشكل ثابت أفضل الأفكار من اللغات الأخرى - LINQ، والمزامنة/الانتظار، والسجلات، ومطابقة الأنماط - مما يجعلها واحدة من أكثر اللغات المتوفرة ثراءً بالميزات وأكثرها ملاءمةً للمطورين.
---

## لماذا تعتبر C# مهمة؟
- **محرك ألعاب Unity**: اللغة الأساسية لـ Unity، محرك الألعاب الأكثر شهرة في العالم حسب عدد المطورين.
- **تطوير المؤسسات**: يعد ASP.NET Core واحدًا من أسرع أطر عمل الويب المتوفرة (يتفوق باستمرار على معايير TechEmpower).
- **الأنظمة الأساسية المشتركة**: يعمل الإصدار .NET 5+ على أنظمة التشغيل Windows، وmacOS، وLinux. لم يعد يعمل بنظام Windows فقط.
- **الإنتاجية**: دعم ممتاز لـ IDE (Visual Studio وRider)، ونظام كتابة قوي، وميزات تركيبية حديثة.
- **غير المتزامن/الانتظار الرائد**: قدمت لغة C# المزامنة/الانتظار في عام 2012 — قبل سنوات من اعتماد اللغات الأخرى لهذا النمط.
- **LINQ**: يتيح لك الاستعلام المدمج باللغة أن تكتب استعلامات تشبه SQL مباشرةً في لغة C# مقابل أي مصدر بيانات.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** اقتران ويندوز ** | مرتبط تاريخياً بنظام Windows؛ التصور يتخلف عن الواقع | .NET 6+ عبارة عن منصة مشتركة بالكامل |
| ** نظام بيئي أصغر من Java ** | مكتبات خارجية أقل من Maven/PyPI | NuGet ينمو. تحتوي العديد من مكتبات Java على مكافئات C# |
| **أقل شيوعًا في الشركات الناشئة** | أكثر شعبية في المؤسسات مما كانت عليه في وادي السيليكون | Go وRust وNode.js للخدمات السحابية الصغيرة الأصلية |
| **الجوال (MAUI)** | Xamarin/MAUI أقل نضجًا من اللغة الأصلية أو Flutter | استخدم Swift/Kotlin أو Flutter الأصلي لتطبيقات الهاتف المحمول المعقدة |
| ** واجهة المستخدم الرسومية لنظام التشغيل Linux ** | خيارات واجهة المستخدم الرسومية الأصلية محدودة على Linux | استخدم واجهات المستخدم المستندة إلى الويب (Blazor) أو Avalonia |
---

## أساسيات بناء الجملة
### البنية الأساسية
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

### البرمجة الشيئية
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

### السجلات (C# 9+) — أنواع البيانات غير القابلة للتغيير
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

### LINQ — استعلام متكامل اللغة
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

### غير متزامن/انتظار
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

### مطابقة الأنماط (C# 7-13)
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة
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

### المندوبون والأحداث وتعبيرات Lambda
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

### التسلسلات الهرمية للاستثناءات المخصصة
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

### التحميل الزائد على المشغل
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

## التزامن والتوازي
### غير متزامن/في انتظار العناصر الداخلية
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

### LINQ الموازي والمكتبة الموازية للمهام
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

## تكوين المشروع ونظام البناء
### هيكل المشروع
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

### ملف .csproj
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

### الاختبار باستخدام xUnit
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

### خط أنابيب CI/CD
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

## إمكانية التشغيل البيني
### P/Invoc — استدعاء مكتبات C
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

## أنماط التصميم
### نمط البناء (واجهة برمجة التطبيقات بطلاقة)
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

### نمط الإستراتيجية مع المندوبين
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

## الأداء والتحسين
### أدوات التنميط
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

## النشر
### ملف دوكر
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

### النشر الخاص بالمنصة
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

## النظام البيئي .NET
### الأطر والمنصات
| الإطار | المجال | الوصف |
|-----------|-------|-------------|
| ** ASP.NET كور ** | ويب | إطار ويب عالي الأداء لواجهات برمجة التطبيقات وتطبيقات الويب |
| **بلازور** | الويب (الواجهة الأمامية) | أنشئ واجهات مستخدم ويب تفاعلية باستخدام لغة C# بدلاً من JavaScript |
| ** إطار عمل الكيان ** | أو آر إم | الوصول إلى قاعدة البيانات باستخدام LINQ؛ هجرات الكود الأول |
| **الوحدة** | العاب | محرك الألعاب الأكثر شهرة في العالم (برمجة C#) |
| **.نت ماوي** | الجوال/سطح المكتب | تطبيقات متعددة المنصات لأنظمة iOS وAndroid وmacOS وWindows |
| **أفالونيا** | سطح المكتب | واجهة مستخدم سطح المكتب عبر الأنظمة الأساسية (مثل WPF لجميع الأنظمة الأساسية) |
### إدارة البناء والحزم
| أداة | الغرض |
|------|---------|
| **دوت نت سطر الأوامر** | البناء والتشغيل والاختبار والنشر من سطر الأوامر |
| ** نوجيت ** | مدير الحزم |
| **MSBuild** | نظام البناء الأساسي |
| ** فيجوال ستوديو / رايدر ** | بيئة تطوير متكاملة |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## إصدارات لغة C#
| النسخة | سنة | الميزات الرئيسية |
|---------|------|-------------|
| ج#7 | 2017 | مطابقة الأنماط، الصفوف، متغيرات `out`، الدوال المحلية |
| ج#8 | 2019 | أنواع المراجع الخالية، وتعبيرات `switch`، والتدفقات غير المتزامنة |
| ج#9 | 2020 | **السجلات**، بيانات المستوى الأعلى، خصائص`init`|
| ج#10 | 2021 | بنيات التسجيل،`using`العالمية، ومساحات الأسماء ذات نطاق الملف |
| ج#11 | 2022 | حرفية السلسلة الأولية، أنماط القائمة، أعضاء `required`، الرياضيات العامة |
| ج#12 | 2023 | المنشئون الأساسيون، تعبيرات المجموعة، المصفوفات المضمنة |
| ج#13 | 2024 |  مجموعات `params`، أنواع الأقفال الجديدة، امتدادات من الدرجة الأولى |
---

## متى تستخدم لغة C#
| السيناريو | لماذا C# | البديل الأفضل |
|----------|-------|------------------|
| تطوير اللعبة (الوحدة) | لغة البرمجة النصية القياسية للوحدة | -- |
| الواجهات الخلفية للويب الخاصة بالمؤسسة | ASP.NET Core سريع وناضج ومدعوم جيدًا | جافا (التمهيد الربيعي) |
| تطبيقات سطح المكتب ويندوز | WPF وWinForms وWinUI أصبحت ناضجة | -- |
| سطح المكتب عبر منصة | أفالونيا أو ماوي | الإلكترون (على شبكة الإنترنت) |
| واجهة الويب (بلازور) | مكدس كامل C# - لا حاجة لجافا سكريبت | React/Vue/Angular لأنظمة SPA الأكثر ثراءً |
| الخدمات السحابية (أزور) | التكامل العميق أزور | -- |
| تطبيقات الجوال (MAUI) | منصة مشتركة مع C# | Flutter أو React Native أو Swift/Kotlin الأصلي |
| الذكاء الاصطناعي/التعلم الآلي | ممكن مع ML.NET | بايثون (يفضل بأغلبية ساحقة) |
| أدوات / البرامج النصية لـ CLI | ممكن ولكن مطول | اذهب يا رست، بايثون |
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين`class`و`record` في لغة C#؟
**A:**`class`هو نوع مرجعي ذو خصائص قابلة للتغيير افتراضيًا — يمكن أن يشير متغيران إلى نفس الكائن. يعد`record`(C# 9+) نوعًا مرجعيًا يتمتع بالمساواة على أساس القيمة - حيث يعتبر السجلان اللذان لهما نفس البيانات متساويين. تحتوي السجلات على خصائص init فقط، و`ToString` مضمنة، وتدعم تعبيرات`with`للطفرات غير المدمرة. استخدام السجلات لحاملات البيانات (DTOs، وكائنات القيمة)؛ استخدم الفئات للكيانات الغنية بالسلوك ذات الهوية.
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

### السؤال الثاني: كيف يعمل المزامنة/الانتظار و`Task` داخليًا؟
**A:**`async/await`عبارة عن سكر نحوي على آلة الحالة التي تم إنشاؤها بواسطة المترجم. عندما تقوم بإنشاء`await`و`Task`، يتم تقسيم الطريقة عند نقطة الانتظار: يتم تنفيذ كل شيء قبله بشكل متزامن، ثم يتم تسجيل الباقي كاستمرار. يتم تحرير الخيط للقيام بأعمال أخرى.  يمثل`Task<T>`قيمة مستقبلية.  يعد`ValueTask<T>`بديلاً هيكليًا للمسارات الساخنة التي تتجنب تخصيص الكومة عندما تكون النتيجة متاحة بالفعل.
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

### س3: ما هي طرق الإرشاد ومتى يجب استخدامها؟
**أ:** تضيف طرق الامتداد طرقًا إلى الأنواع الموجودة دون تعديلها. إنها طرق ثابتة في فئة ثابتة، مع الكلمة الأساسية`this`في المعلمة الأولى. إنها تتيح واجهة برمجة التطبيقات (API) بطلاقة وقابلة للتسلسل. استخدمها لإضافة أساليب مساعدة إلى الأنواع التي لا تمتلكها (مثل`string`أو`IEnumerable<T>`). تجنب الإفراط في استخدامها، لأنها يمكن أن تجعل من الصعب اكتشاف التعليمات البرمجية.
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

### س4: كيف تعمل مطابقة الأنماط في لغة C# الحديثة؟
**أ:** أضافت لغة C# تدريجيًا المزيد من مطابقة الأنماط القوية. تتيح تعبيرات التبديل (C# 8)، وأنماط الكتابة، وأنماط الخصائص، والأنماط العلائقية، وأنماط القائمة (C# 11) منطقًا شرطيًا موجزًا ​​ومعبرًا. تحل مطابقة الأنماط محل سلاسل if/else الطويلة ويتم فحصها بشكل شامل بواسطة المترجم.
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

### س5: ما هو حقن التبعية في .NET، وكيف أستخدمه؟
**أ:** يحتوي .NET على دعم DI مدمج عبر `Microsoft.Extensions.DependencyInjection`. تقوم بتسجيل الخدمات مع عمرها الافتراضي (Singleton، Scoped، Transient)، وتقوم الحاوية بإدخالها عبر معلمات المُنشئ. Singleton: مثيل واحد للتطبيق. النطاق: واحد لكل طلب HTTP. عابر: مثيل جديد في كل مرة.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة 1: إنشاء مستودع عام مع التخزين المؤقت
**بيان المشكلة:** قم بتنفيذ نمط مستودع عام باستخدام مصمم يضيف التخزين المؤقت. يجب أن يدعم المستودع عمليات CRUD، ويجب أن يقوم مصمم التخزين المؤقت بتخزين عمليات القراءة وإبطال عمليات الكتابة.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) واجهة`IRepository<T>`عامة، (2) تنفيذ ملموس (على سبيل المثال، في الذاكرة)، (3) ديكور تخزين مؤقت يغلف أي مستودع، (4) إبطال ذاكرة التخزين المؤقت في عمليات الكتابة. يحافظ نمط الديكور على التخزين المؤقت بشكل متعامد مع منطق الوصول إلى البيانات.
**الخطوة الثانية — تحديد النهج:**
- حدد`IRepository<T>`باستخدام`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- قم بإنشاء`CachingRepository<T>`الذي يلتف حول`IRepository<T>`ويستخدم`IMemoryCache`.
- مفتاح ذاكرة التخزين المؤقت:`typeof(T).Name:{id}`.
- في عمليات الكتابة، قم بإبطال إدخال ذاكرة التخزين المؤقت.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- فصل الاهتمامات: التخزين المؤقت هو أداة تزيين، ولا يتم دمجه في المستودع.
- تسجيل DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(باستخدام Scrutor).
- الإنتاج: استخدم`IDistributedCache`(Redis) لسيناريوهات الخوادم المتعددة، وأضف أنماط التخزين المؤقت جانبًا مع حماية `CacheStampede`.
### المشكلة الثانية: تنفيذ مسار البرامج الوسيطة
**بيان المشكلة:** قم بإنشاء مسار برامج وسيطة مشابه لخط أنابيب طلب ASP.NET Core. يمكن لكل برنامج وسيط معالجة الطلب واستدعاء البرنامج الوسيط التالي ومعالجة الاستجابة.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) نوع`RequestDelegate`يمثل المسار، (2) برنامج وسيط يغلف المندوب التالي، (3) واجهة برمجة تطبيقات منشئة لإنشاء البرامج الوسيطة. هذا هو نمط سلسلة المسؤولية الذي يتم تطبيقه مع المندوبين.
**الخطوة الثانية — تحديد النهج:**
-`RequestDelegate`هو`Func<Context, RequestDelegate, Task>`.
- يتلقى كل برنامج وسيط السياق ووظيفة `next`.
- يضيف`Use`برامج وسيطة؛  يقوم`Build`بتأليفها في مندوب واحد.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- ترتيب البرامج الوسيطة مهم: تتم الإضافة أولاً = الأبعد (يتم تنفيذه أولاً عند الطلب، وآخر عند الاستجابة).
- تعمل البرامج الوسيطة الطرفية (بدون استدعاء `next`) على قصر خط الأنابيب.
- الإنتاج: خط أنابيب ASP.NET Core هو هذا النمط تمامًا، وقد تم تحسينه باستخدام أشجار التعبير المجمعة بدون تخصيص.
---

## ملخص
C# هي لغة مصقولة وحديثة ذات أغراض عامة مع أدوات ممتازة ونظام بيئي قوي. إنه يتفوق في تطوير المؤسسات، وتطوير الألعاب (Unity)، والتطبيقات عبر الأنظمة الأساسية. لقد تطورت اللغة بسرعة - أصبحت لغة C# الحديثة موجزة ومعبرة وآمنة للكتابة. على الرغم من أنها لا تتمتع بحجم النظام البيئي مثل Java أو Python، إلا أن جودة .NET واتساقها يجعلان لغة C# لغة منتجة وممتعة لمجموعة واسعة من التطبيقات.