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
C#（發音為「C-sharp」）是一種現代的、物件導向的、類型安全的程式語言，由 Microsoft 在 Anders Hejlsberg 的領導下開發，並於 2002 年首次發布。它運行在 .NET 平台上，旨在將 C++ 的強大功能與 Visual Basic 的生產力結合。如今，C# 是一種多功能、跨平台語言，用於 Web 應用程式 (ASP.NET)、桌面軟體 (Windows)、遊戲開發 (Unity)、行動應用程式 (MAUI)、雲端服務 (Azure) 等。
C# 不斷吸收其他語言的最佳想法——LINQ、非同步/等待、記錄、模式匹配——使其成為功能最豐富、對開發人員最友善的語言之一。
---

## 為什麼 C# 很重要
- **Unity 遊戲引擎**：Unity 的主要語言，以開發人員數量計算，Unity 是世界上最受歡迎的遊戲引擎。
- **企業開發**：ASP.NET Core 是可用的最快的 Web 框架之一（始終位居 TechEmpower 基準測試之上）。
- **跨平台**：.NET 5+ 在 Windows、macOS 和 Linux 上運作。不再僅限於 Windows。
- **生產力**：出色的 IDE 支援（Visual Studio、Rider）、強大的類型系統和現代語法功能。
- **async/await 先驅者**：C# 在 2012 年引入了 async/await，比其他語言採用該模式早了很多年。
- **LINQ**：語言整合查詢讓您可以直接在 C# 中針對任何資料來源撰寫類似 SQL 的查詢。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **Windows 協會** |歷史上與 Windows 密切相關；認知落後於現實| .NET 6+ 完全跨平台 |
| **比 Java 更小的生態系統** |比 Maven/PyPI 更少的第三方庫 | NuGet 正在成長；許多 Java 庫都有 C# 等效項 |
| **在新創公司中較不常見** |在企業中比在矽谷更受歡迎 |用於雲端原生微服務的 Go、Rust、Node.js |
| **行動（毛伊島）** | Xamarin/MAUI 不如原生或 Flutter 成熟 |使用原生 Swift/Kotlin 或 Flutter 來建立複雜的行動應用程式 |
| **Linux 圖形使用者介面** | Linux 上有限的本機 GUI 選項使用基於 Web 的 UI (Blazor) 或 Avalonia |
---

## 文法基礎知識
### 基本結構
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

### 物件導向編程
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

### 記錄 (C# 9+) — 不可變資料型別
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

### LINQ — 語言整合查詢
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

### 非同步/等待
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

## 進階語法和模式
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

### 委託、事件與 Lambda 表達式
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

### 自訂異常層次結構
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

### 運算子重載
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

## 並發與平行
### 非同步/等待內部
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

### 並行 LINQ 和任務並行庫
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

## 專案配置與建置系統
### 專案結構
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

### 使用 xUnit 進行測試
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

## 互通性
### P/Invoke — 呼叫 C 函式庫
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

### C++/CLI 互通
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

## 設計模式
### 建構器模式（Fluent API）
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

## 效能與最佳化
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

### 特定於平台的部署
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

## .NET 生態系統
### 框架和平台
|框架|網域 |描述 |
|------------|--------|-------------|
| **ASP.NET 核心** |網頁 |適用於 API 和 Web 應用程式的高效能 Web 框架 |
| **開拓者** |網頁（前端）|使用 C# 而不是 JavaScript 建立互動式 Web UI |
| **實體框架核心** |物件關係管理 |使用 LINQ 存取資料庫；程式碼優先遷移 |
| **團結** |遊戲 |世界上最受歡迎的遊戲引擎（C#腳本）|
| **.NET 毛伊島** |行動/桌面 |適用於 iOS、Android、macOS、Windows 的跨平台應用程式 |
| **阿瓦隆尼亞** |桌面|跨平台桌面 UI（如適用於所有平台的 WPF）|
### 建置與套件管理
|工具|目的|
|------|---------|
| **dotnet CLI** |從命令列建置、執行、測試、發布 |
| **NuGet** |套件管理器 |
| **MSBuild** |底層建置系統|
| **視覺工作室/騎士** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# 語言版本
|版本 |年份|主要特點|
|---------|------|-------------|
| C# 7 | 2017 | 2017模式匹配、元組、`out` 變數、局部函數 |
| C# 8 | 2019 | 2019可空引用型別、`switch` 表達式、非同步流 |
| C# 9 | 2020 | **記錄**、頂層語句、`init` 屬性 |
| C# 10 | 2021 |記錄結構、全域`using`、檔案範圍的命名空間 |
| C# 11 | 2022 | 2022原始字串文字、列表模式、`required` 成員、通用數學 |
| C# 12 | 2023 |主建構子、集合表達式、內聯數組 |
| C# 13 | 2024 | 2024 `params`系列，新鎖類型，一流跨度|
---

## 何時使用 C#
|場景 |為什麼選擇 C# |更好的選擇|
|----------|--------|--------------------|
|遊戲開發（Unity）|標準Unity腳本語言| --|
|企業網路後端 | ASP.NET Core 快速、成熟、支援良好 | Java（Spring Boot）|
| Windows 桌面應用程式 | WPF、WinForms、WinUI 已成熟 | --|
|跨平台桌面|阿瓦洛尼亞或毛伊島 | Electron（基於網路）|
| Web 前端 (Blazor) |全端 C# — 無需 JavaScript | React/Vue/Angular 打造更豐富的 SPA 生態系統 |
|雲端服務 (Azure) |深度 Azure 整合 | --|
|行動應用程式 (毛伊島) |使用 C# 跨平台 | Flutter、React Native 或原生 Swift/Kotlin |
|人工智慧/機器學習 | ML.NET 成為可能 | Python（壓倒性首選）|
| CLI 工具/腳本 |可能但冗長 | Go、Rust、Python |
---

＃＃ 概括
C# 是一種精美的、現代的通用語言，具有出色的工具和強大的生態系統。它在企業開發、遊戲開發（Unity）和跨平台應用程式方面表現出色。該語言發展迅速 - 現代 C# 簡潔、富有表現力且類型安全。雖然它不具備 Ja​​va 或 Python 的生態系統規模，但 .NET 的品質和一致性使 C# 成為適用於各種應用程式的高效且令人愉悅的語言。