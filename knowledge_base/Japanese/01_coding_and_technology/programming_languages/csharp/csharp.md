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
#C#
C# (「C シャープ」と発音) は、Anders Hejlsberg のリーダーシップの下で Microsoft によって開発され、2002 年に初めてリリースされた、最新のオブジェクト指向のタイプセーフ プログラミング言語です。 C# は .NET プラットフォーム上で動作し、C++ の能力と Visual Basic の生産性を組み合わせるように設計されました。現在、C# は、Web アプリケーション (ASP.NET)、デスクトップ ソフトウェア (Windows)、ゲーム開発 (Unity)、モバイル アプリ (MAUI)、クラウド サービス (Azure) などに使用される多用途のクロスプラットフォーム言語です。
C# は、LINQ、async/await、レコード、パターン マッチングなど、他の言語から優れたアイデアを着実に吸収しており、利用可能な言語の中で最も機能が豊富で開発者に優しい言語の 1 つとなっています。
---

## C# が重要な理由
- **Unity ゲーム エンジン**: 開発者数で世界で最も人気のあるゲーム エンジンである Unity の主要言語です。
- **エンタープライズ開発**: ASP.NET Core は、利用可能な Web フレームワークの中で最も高速なフレームワークの 1 つです (TechEmpower ベンチマークで常に上位にあります)。
- **クロスプラットフォーム**: .NET 5 以降は Windows、macOS、Linux 上で動作します。 Windows のみではなくなりました。
- **生産性**: 優れた IDE サポート (Visual Studio、Rider)、強力な型システム、最新の構文機能。
- **async/await のパイオニア**: C# は 2012 年に async/await を導入しました。他の言語がこのパターンを採用する何年も前でした。
- **LINQ**: 統合言語クエリを使用すると、任意のデータ ソースに対して SQL のようなクエリを C# で直接作成できます。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **Windows の関連付け** |歴史的に Windows と結びついています。認識は現実よりも遅れています。 .NET 6 以降は完全にクロスプラットフォームです |
| **Java よりも小さいエコシステム** | Maven/PyPI よりもサードパーティ ライブラリが少ない | NuGet は成長しています。多くの Java ライブラリには C# と同等のものがあります。
| **スタートアップではあまり一般的ではありません** |シリコンバレーよりも企業で人気 |クラウドネイティブのマイクロサービスのための Go、Rust、Node.js |
| **モバイル (マウイ)** | Xamarin/MAUI はネイティブや Flutter よりも成熟度が低い |複雑なモバイル アプリにはネイティブの Swift/Kotlin または Flutter を使用する |
| **Linux GUI** | Linux 上の制限されたネイティブ GUI オプション | Web ベースの UI (Blazor) または Avalonia を使用します。
---

## 構文の基礎
### 基本構造
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

### オブジェクト指向プログラミング
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

### レコード (C# 9+) — 不変のデータ型
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

### LINQ — 統合言語クエリ
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

### 非同期/待機
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

### パターン マッチング (C# 7-13)
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

## 高度な構文とパターン
### ジェネリック医薬品
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

### デリゲート、イベント、ラムダ式
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

### カスタム例外階層
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

### 演算子のオーバーロード
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

## 同時実行性と並列処理
### async/await 内部構造
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

### 並列 LINQ およびタスク並列ライブラリ
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

## プロジェクトの構成とシステムの構築
### プロジェクトの構造
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

### .csproj ファイル
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

### xUnit を使用したテスト
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

### CI/CD パイプライン
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

## 相互運用性
### P/Invoke — C ライブラリの呼び出し
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

### C++/CLI 相互運用性
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

## デザインパターン
### ビルダー パターン (Fluent API)
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

### 参加者による戦略パターン
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

## パフォーマンスと最適化
### プロファイリングツール
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

## デプロイメント
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

### プラットフォーム固有の展開
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

## .NET エコシステム
### フレームワークとプラットフォーム
|フレームワーク |ドメイン |説明 |
|----------|----------|---------------|
| **ASP.NET コア** |ウェブ | API および Web アプリ用の高性能 Web フレームワーク |
| **ブレザー** |ウェブ（フロントエンド） | JavaScript の代わりに C# を使用してインタラクティブな Web UI を構築する |
| **Entity Framework コア** | ORM | LINQ によるデータベース アクセス。コードファーストの移行 |
| **団結** |ゲーム |世界で最も人気のあるゲーム エンジン (C# スクリプト) |
| **.NET マウイ** |モバイル/デスクトップ | iOS、Android、macOS、Windows 用のクロスプラットフォーム アプリ |
| **アバロニア** |デスクトップ |クロスプラットフォームのデスクトップ UI (すべてのプラットフォームの WPF など) |
### ビルドとパッケージの管理
|ツール |目的 |
|-----|----------|
| **ドットネット CLI** |コマンド ラインからビルド、実行、テスト、公開 |
| **NuGet** |パッケージマネージャー |
| **MSBuild** |基礎となるビルド システム |
| **ビジュアル スタジオ / ライダー** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# 言語のバージョン
|バージョン |年 |主な機能 |
|----------|------|---------------|
| C#7 | 2017年 |パターンマッチング、タプル、`out`変数、ローカル関数 |
| C#8 | 2019年 | Null 許容参照型、`switch` 式、非同期ストリーム |
| C#9 | 2020年 | **レコード**、トップレベルのステートメント、`init` プロパティ |
| C#10 | 2021年 |レコード構造体、グローバル`using`、ファイル スコープの名前空間 |
| C#11 | 2022年 |生の文字列リテラル、リスト パターン、`required` メンバー、一般的な数学 |
| C#12 | 2023年 |プライマリ コンストラクター、コレクション式、インライン配列 |
| C#13 | 2024年 | `params`コレクション、新しいロック タイプ、ファーストクラス スパン |
---

## C# を使用する場合
|シナリオ |なぜ C# |より良い代替案 |
|----------|----------|--------|
|ゲーム開発（Unity） |標準の Unity スクリプト言語 | -- |
|エンタープライズ Web バックエンド | ASP.NET Core は高速で成熟しており、サポートが充実しています | Java (スプリングブート) |
| Windows デスクトップ アプリケーション | WPF、WinForms、WinUI は成熟しています | -- |
|クロスプラットフォームデスクトップ |アバロニアまたはマウイ | Electron (ウェブベース) |
| Web フロントエンド (Blazor) |フルスタック C# — JavaScript は不要 |より充実した SPA エコシステムのための React/Vue/Angular |
|クラウドサービス（Azure） |ディープ Azure 統合 | -- |
|モバイルアプリ (MAUI) | C# によるクロスプラットフォーム | Flutter、React Native、またはネイティブ Swift/Kotlin |
| AI/ML | ML.NET で可能 | Python (圧倒的に推奨) |
| CLI ツール/スクリプト |可能だが冗長 | Go、Rust、Python |
---

## 総合的な Q&A
### Q1: C# における`class`と`record`の違いは何ですか?
**A:**`class`は、デフォルトで可変プロパティを持つ参照型です。2 つの変数が同じオブジェクトを参照できます。`record`(C# 9 以降) は、値ベースの等価性を持つ参照型です。同じデータを持つ 2 つのレコードは等しいとみなされます。レコードには init 専用プロパティ、組み込み`ToString`があり、非破壊的な変更のための`with`式をサポートしています。データ キャリア (DTO、値オブジェクト) のレコードを使用します。アイデンティティを持つ動作豊富なエンティティにはクラスを使用します。
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

### Q2: async/await と`Task`は内部的にどのように動作しますか?
**A:**`async/await`は、コンパイラによって生成されたステート マシン上の糖衣構文です。`await`を`Task`にすると、メソッドは待機ポイントで分割されます。つまり、それまでのすべてが同期的に実行され、残りが継続として登録されます。スレッドは他の作業のために解放されます。 `Task<T>`は将来の値を表します。 `ValueTask<T>`は、結果がすでに利用可能な場合にヒープ割り当てを回避するホット パスの代替構造体です。
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

### Q3: 拡張メソッドとは何ですか?いつ使用する必要がありますか?
**A:** 拡張メソッドは、既存の型を変更せずにメソッドを追加します。これらは静的クラス内の静的メソッドであり、最初のパラメーターに`this`キーワードが付いています。これらにより、流暢でチェーン可能な API が可能になります。これらを使用して、所有していない型 (`string`や`IEnumerable<T>`など) にユーティリティ メソッドを追加します。過度に使用しないでください。コードを発見するのが困難になる可能性があります。
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

### Q4: 最新の C# ではパターン マッチングはどのように機能しますか?
**A:** C# では、より強力なパターン マッチングが徐々に追加されています。 Switch 式 (C# 8)、型パターン、プロパティ パターン、リレーショナル パターン、およびリスト パターン (C# 11) を使用すると、簡潔で表現力豊かな条件付きロジックが可能になります。パターン マッチングは長い if/else チェーンを置き換え、コンパイラによって徹底的にチェックされます。
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

### Q5: .NET の依存関係注入とは何ですか?また、それをどのように使用すればよいですか?
**A:** .NET には、`Microsoft.Extensions.DependencyInjection`を介した DI サポートが組み込まれています。サービスをそのライフタイム (シングルトン、スコープ付き、一時的) とともに登録すると、コンテナーがコンストラクター パラメーターを介してサービスを挿入します。シングルトン: アプリの 1 つのインスタンス。スコープ: HTTP リクエストごとに 1 つ。一時的: 毎回新しいインスタンス。
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

## 思考連鎖による問題解決
### 問題 1: キャッシュを使用した汎用リポジトリの構築
**問題ステートメント:** キャッシュを追加するデコレータを使用して汎用リポジトリ パターンを実装します。リポジトリは CRUD 操作をサポートする必要があり、キャッシュ デコレータは読み取りをキャッシュし、書き込みを無効にする必要があります。
**ステップ 1 — 問題を理解する:**
必要なのは、(1) 汎用`IRepository<T>`インターフェイス、(2) 具体的な実装 (メモリ内など)、(3) 任意のリポジトリをラップするキャッシュ デコレータ、(4) 書き込み操作時のキャッシュの無効化です。デコレータ パターンは、データ アクセス ロジックと直交してキャッシュを維持します。
**ステップ 2 — アプローチを特定する:**
-`IRepository<T>`を`Get`、`GetAll`、`Add`、`Update`、`Delete`で定義します。
-`IRepository<T>`をラップし、`IMemoryCache`を使用する`CachingRepository<T>`を作成します。
- キャッシュキー:`typeof(T).Name:{id}`。
- 書き込み操作では、キャッシュ エントリを無効にします。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- 関心事の分離: キャッシュはデコレータであり、リポジトリに混合されるものではありません。
- DI 登録:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(Scrutor を使用)。
- 運用: マルチサーバー シナリオには`IDistributedCache`(Redis) を使用し、`CacheStampede` 保護を備えたキャッシュ アサイド パターンを追加します。
### 問題 2: ミドルウェア パイプラインの実装
**問題ステートメント:** ASP.NET Core の要求パイプラインと同様のミドルウェア パイプラインを構築します。各ミドルウェアはリクエストを処理し、次のミドルウェアを呼び出し、応答を処理できます。
**ステップ 1 — 問題を理解する:**
(1) パイプラインを表す`RequestDelegate`型、(2) 次のデリゲートをラップするミドルウェア、(3) ミドルウェアを構成するためのビルダー API が必要です。これは、デリゲートで実装される責任の連鎖パターンです。
**ステップ 2 — アプローチを特定する:**
-`RequestDelegate` は`Func<Context, RequestDelegate, Task>`です。
- 各ミドルウェアはコンテキストと`next`関数を受け取ります。
-`Use`はミドルウェアを追加します。 `Build`は、それらを 1 つのデリゲートに合成します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- ミドルウェアの順序は重要です: 最初に追加された = 最も外側 (要求時に最初に実行され、応答時に最後に実行されます)。
- ターミナル ミドルウェア (`next` 呼び出しなし) がパイプラインを短絡します。
- 運用: ASP.NET Core のパイプラインはまさにこのパターンであり、ゼロ割り当て用にコンパイルされた式ツリーで最適化されています。
---

＃＃ まとめ
C# は、優れたツールと強力なエコシステムを備えた、洗練された最新の汎用言語です。エンタープライズ開発、ゲーム開発 (Unity)、クロスプラットフォーム アプリケーションに優れています。この言語は急速に進化しており、最新の C# は簡潔で表現力が豊かで、タイプセーフです。 Java や Python のようなエコシステムの規模はありませんが、.NET の品質と一貫性により、C# は幅広いアプリケーションにとって生産的で楽しい言語となっています。