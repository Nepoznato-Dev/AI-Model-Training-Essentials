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
C#（发音为“C-sharp”）是一种现代的、面向对象的、类型安全的编程语言，由 Microsoft 在 Anders Hejlsberg 的领导下开发，并于 2002 年首次发布。它运行在 .NET 平台上，旨在将 C++ 的强大功能与 Visual Basic 的生产力结合起来。如今，C# 是一种多功能、跨平台语言，用于 Web 应用程序 (ASP.NET)、桌面软件 (Windows)、游戏开发 (Unity)、移动应用程序 (MAUI)、云服务 (Azure) 等。
C# 不断吸收其他语言的最佳思想——LINQ、异步/等待、记录、模式匹配——使其成为功能最丰富、对开发人员最友好的语言之一。
---

## 为什么 C# 很重要
- **Unity 游戏引擎**：Unity 的主要语言，按开发人员数量计算，Unity 是世界上最受欢迎的游戏引擎。
- **企业开发**：ASP.NET Core 是可用的最快的 Web 框架之一（始终位居 TechEmpower 基准测试之上）。
- **跨平台**：.NET 5+ 在 Windows、macOS 和 Linux 上运行。不再仅限于 Windows。
- **生产力**：出色的 IDE 支持（Visual Studio、Rider）、强大的类型系统和现代语法功能。
- **async/await 先驱**：C# 在 2012 年引入了 async/await，比其他语言采用该模式早了很多年。
- **LINQ**：语言集成查询让您可以直接在 C# 中针对任何数据源编写类似 SQL 的查询。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **Windows 协会** |历史上与 Windows 密切相关；认知落后于现实| .NET 6+ 完全跨平台 |
| **比 Java 更小的生态系统** |比 Maven/PyPI 更少的第三方库 | NuGet 正在成长；许多 Java 库都有 C# 等效项 |
| **在初创公司中不太常见** |在企业中比在硅谷更受欢迎 |用于云原生微服务的 Go、Rust、Node.js |
| **移动（毛伊岛）** | Xamarin/MAUI 不如原生或 Flutter 成熟 |使用原生 Swift/Kotlin 或 Flutter 来构建复杂的移动应用程序 |
| **Linux 图形用户界面** | Linux 上有限的本机 GUI 选项使用基于 Web 的 UI (Blazor) 或 Avalonia |
---

## 语法基础知识
### 基本结构
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

### 面向对象编程
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

### 记录 (C# 9+) — 不可变数据类型
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

### LINQ — 语言集成查询
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

### 异步/等待
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

### 模式匹配 (C# 7-13)
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

## 高级语法和模式
### 泛型
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

### 委托、事件和 Lambda 表达式
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

### 自定义异常层次结构
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

### 运算符重载
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

## 并发与并行
### 异步/等待内部
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

### 并行 LINQ 和任务并行库
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

## 项目配置和构建系统
### 项目结构
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

### .csproj 文件
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

### 使用 xUnit 进行测试
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

### CI/CD 管道
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

## 互操作性
### P/Invoke — 调用 C 库
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

### C++/CLI 互操作
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

## 设计模式
### 构建器模式（Fluent API）
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

### 代表策略模式
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

## 性能与优化
### 分析工具
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

## 部署
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

### 特定于平台的部署
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

## .NET 生态系统
### 框架和平台
|框架|域名 |描述 |
|------------|--------|-------------|
| **ASP.NET 核心** |网页 |适用于 API 和 Web 应用程序的高性能 Web 框架 |
| **开拓者** |网页（前端）|使用 C# 而不是 JavaScript 构建交互式 Web UI |
| **实体框架核心** |对象关系管理 |使用 LINQ 访问数据库；代码优先迁移 |
| **团结** |游戏 |世界上最流行的游戏引擎（C#脚本）|
| **.NET 毛伊岛** |移动/桌面 |适用于 iOS、Android、macOS、Windows 的跨平台应用程序 |
| **阿瓦隆尼亚** |桌面|跨平台桌面 UI（如适用于所有平台的 WPF）|
### 构建和包管理
|工具|目的|
|------|---------|
| **dotnet CLI** |从命令行构建、运行、测试、发布 |
| **NuGet** |包管理器 |
| **MSBuild** |底层构建系统|
| **视觉工作室/骑手** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# 语言版本
|版本 |年份|主要特点|
|---------|------|-------------|
| C# 7 | 2017 | 2017模式匹配、元组、`out` 变量、局部函数 |
| C# 8 | 2019 | 2019可空引用类型、`switch` 表达式、异步流 |
| C# 9 | 2020 | **记录**、顶级语句、`init` 属性 |
| C# 10 | 2021 |记录结构、全局`using`、文件范围的命名空间 |
| C# 11 | 2022 | 2022原始字符串文字、列表模式、`required` 成员、通用数学 |
| C# 12 | 2023 |主构造函数、集合表达式、内联数组 |
| C# 13 | 2024 | 2024 `params`集合、新的锁类型、一流的跨度 |
---

## 何时使用 C#
|场景 |为什么选择 C# |更好的选择|
|----------|--------|--------------------|
|游戏开发（Unity）|标准Unity脚本语言| --|
|企业网络后端 | ASP.NET Core 快速、成熟、支持良好 | Java（Spring Boot）|
| Windows 桌面应用程序 | WPF、WinForms、WinUI 已成熟 | --|
|跨平台桌面|阿瓦洛尼亚或毛伊岛 | Electron（基于网络）|
| Web 前端 (Blazor) |全栈 C# — 无需 JavaScript | React/Vue/Angular 打造更丰富的 SPA 生态系统 |
|云服务 (Azure) |深度 Azure 集成 | --|
|移动应用程序 (毛伊岛) |使用 C# 跨平台 | Flutter、React Native 或原生 Swift/Kotlin |
|人工智能/机器学习 | ML.NET 成为可能 | Python（压倒性首选）|
| CLI 工具/脚本 |可能但很冗长 | Go、Rust、Python |
---

＃＃ 概括
C# 是一种精美的、现代的通用语言，具有出色的工具和强大的生态系统。它在企业开发、游戏开发（Unity）和跨平台应用程序方面表现出色。该语言发展迅速 - 现代 C# 简洁、富有表现力且类型安全。虽然它不具备 Java 或 Python 的生态系统规模，但 .NET 的质量和一致性使 C# 成为适用于各种应用程序的高效且令人愉悦的语言。