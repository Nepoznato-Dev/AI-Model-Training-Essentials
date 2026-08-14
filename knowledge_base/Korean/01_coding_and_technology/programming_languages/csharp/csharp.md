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
C#("C-sharp"로 발음)은 Microsoft가 Anders Hejlsberg의 주도 하에 개발하고 2002년에 처음 출시된 현대적인 개체 지향 형식 안전 프로그래밍 언어입니다. 이 언어는 .NET 플랫폼에서 실행되며 C++의 강력한 기능과 Visual Basic의 생산성을 결합하도록 설계되었습니다. 오늘날 C#은 웹 애플리케이션(ASP.NET), 데스크톱 소프트웨어(Windows), 게임 개발(Unity), 모바일 앱(MAUI), 클라우드 서비스(Azure) 등에 사용되는 다목적 크로스 플랫폼 언어입니다.
C#은 LINQ, async/await, 레코드, 패턴 일치 등 다른 언어의 최고의 아이디어를 꾸준히 흡수하여 기능이 가장 풍부하고 개발자 친화적인 언어 중 하나가 되었습니다.
---

## C#이 중요한 이유
- **Unity 게임 엔진**: 개발자 수 기준으로 세계에서 가장 인기 있는 게임 엔진인 Unity의 기본 언어입니다.
- **엔터프라이즈 개발**: ASP.NET Core는 사용 가능한 가장 빠른 웹 프레임워크 중 하나입니다(계속 TechEmpower 벤치마크에서 상위를 차지함).
- **크로스 플랫폼**: .NET 5+는 Windows, macOS 및 Linux에서 실행됩니다. 더 이상 Windows 전용이 아닙니다.
- **생산성**: 탁월한 IDE 지원(Visual Studio, Rider), 강력한 유형 시스템 및 최신 구문 기능.
- **async/await 선구자**: C#은 다른 언어가 이 패턴을 채택하기 몇 년 전인 2012년에 async/await를 도입했습니다.
- **LINQ**: 언어 통합 쿼리를 사용하면 모든 데이터 소스에 대해 C#에서 직접 SQL과 유사한 쿼리를 작성할 수 있습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **Windows 연결** | 역사적으로 Windows와 연결되어 있습니다. 인식이 현실보다 뒤쳐져 있다 | .NET 6+는 완전한 크로스 플랫폼입니다 |
| **Java보다 작은 생태계** | Maven/PyPI보다 적은 수의 타사 라이브러리 | NuGet은 성장하고 있습니다. 많은 Java 라이브러리에는 C#에 해당하는 항목이 있습니다 |
| **스타트업에서는 덜 일반적임** | 실리콘밸리보다 기업에서 더 인기 | 클라우드 기반 마이크로서비스를 위한 Go, Rust, Node.js |
| **모바일(MAUI)** | Xamarin/MAUI는 기본 또는 Flutter보다 덜 성숙합니다 | 복잡한 모바일 앱에 기본 Swift/Kotlin 또는 Flutter 사용 |
| **리눅스 GUI** | Linux의 제한된 기본 GUI 옵션 | 웹 기반 UI(Blazor) 또는 Avalonia 사용 |
---

## 구문 기본 사항
### 기본 구조
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

### 객체 지향 프로그래밍
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

### 레코드(C# 9+) - 불변 데이터 유형
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

### LINQ — 언어 통합 쿼리
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

### 비동기/대기
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

### 패턴 일치(C# 7-13)
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

## 고급 구문 및 패턴
### 제네릭
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

### 대리자, 이벤트 및 람다 표현식
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

### 사용자 정의 예외 계층
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

### 연산자 오버로딩
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

## 동시성 및 병렬성
### 비동기/대기 내부
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

### 병렬 LINQ 및 작업 병렬 라이브러리
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조
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

### .csproj 파일
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

### xUnit으로 테스트하기
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

### CI/CD 파이프라인
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

## 상호 운용성
### P/Invoke - C 라이브러리 호출
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

### C++/CLI 상호 운용성
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

## 디자인 패턴
### 빌더 패턴(Fluent API)
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

### 대리인을 사용한 전략 패턴
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

## 성능 및 최적화
### 프로파일링 도구
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

## 배포
### 도커파일
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

### 플랫폼별 배포
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

## .NET 생태계
### 프레임워크 및 플랫폼
| 프레임워크 | 도메인 | 설명 |
|------------|---------|-------------|
| **ASP.NET 코어** | 웹 | API 및 웹 앱을 위한 고성능 웹 프레임워크 |
| **블레이저** | 웹(프런트엔드) | JavaScript 대신 C#을 사용하여 대화형 웹 UI 구축 |
| **엔티티 프레임워크 코어** | ORM | LINQ를 통한 데이터베이스 액세스 코드 우선 마이그레이션 |
| **유니티** | 게임 | 세계에서 가장 인기 있는 게임 엔진(C# 스크립팅) |
| **.NET 마우이** | 모바일/데스크톱 | iOS, Android, macOS, Windows용 크로스 플랫폼 앱 |
| **아발로니아** | 데스크탑 | 크로스 플랫폼 데스크탑 UI(예: 모든 플랫폼용 WPF) |
### 빌드 및 패키지 관리
| 도구 | 목적 |
|------|---------|
| **닷넷 CLI** | 명령줄에서 빌드, 실행, 테스트, 게시 |
| **누겟** | 패키지 관리자 |
| **MS빌드** | 기본 빌드 시스템 |
| **비주얼 스튜디오/라이더** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## C# 언어 버전
| 버전 | 연도 | 주요 기능 |
|---------|------|-------------|
| C#7 | 2017 | 패턴 일치, 튜플,`out`변수, 로컬 함수 |
| C# 8 | 2019 | Null 허용 참조 유형,`switch`표현식, 비동기 스트림 |
| C#9 | 2020 | **레코드**, 최상위 명령문,`init`속성 |
| C#10 | 2021 | 레코드 구조체, 전역 `using`, 파일 범위 네임스페이스 |
| C#11 | 2022 | 원시 문자열 리터럴, 목록 패턴,`required`멤버, 일반 수학 |
| C#12 | 2023 | 기본 생성자, 컬렉션 표현식, 인라인 배열 |
| C# 13 | 2024년 | `params`컬렉션, 새로운 잠금 유형, 일류 범위 |
---

## C#을 사용해야 하는 경우
| 시나리오 | 왜 C#인가 | 더 나은 대안 |
|----------|---------|------|
| 게임 개발(Unity) | 표준 Unity 스크립팅 언어 | -- |
| 엔터프라이즈 웹 백엔드 | ASP.NET Core는 빠르고, 성숙하며, 잘 지원됩니다 | Java(스프링 부트) |
| Windows 데스크톱 애플리케이션 | WPF, WinForms, WinUI는 성숙해졌습니다 | -- |
| 크로스 플랫폼 데스크탑 | 아발로니아 또는 MAUI | Electron(웹 기반) |
| 웹 프런트엔드(Blazor) | 전체 스택 C# — JavaScript가 필요하지 않음 | 더욱 풍부한 SPA 생태계를 위한 React/Vue/Angular |
| 클라우드 서비스(Azure) | 깊은 Azure 통합 | -- |
| 모바일 앱(MAUI) | C#을 사용한 크로스 플랫폼 | Flutter, React Native 또는 기본 Swift/Kotlin |
| AI/ML | ML.NET으로 가능 | Python(압도적으로 선호됨) |
| CLI 도구/스크립트 | 가능하지만 장황함 | 이동, 러스트, 파이썬 |
---

## 종합 Q&A
### Q1: C#에서 `class`와 `record`의 차이점은 무엇입니까?
**A:** `class`는 기본적으로 변경 가능한 속성이 있는 참조 유형입니다. 두 변수가 동일한 객체를 참조할 수 있습니다. `record`(C# 9+)는 값 기반 동등성을 갖춘 참조 유형입니다. 동일한 데이터가 있는 두 개의 레코드는 동일한 것으로 간주됩니다. 레코드에는 초기화 전용 속성인 `ToString`가 내장되어 있으며 비파괴적 변형을 위한`with`표현식을 지원합니다. 데이터 매체(DTO, 값 개체)에 대한 레코드를 사용합니다. ID가 있는 동작이 풍부한 엔터티에 대한 클래스를 사용합니다.
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

### Q2: async/await 및 `Task`는 내부적으로 어떻게 작동하나요?
**A:** `async/await`는 컴파일러에서 생성된 상태 머신에 대한 구문 설탕입니다.`await`a`Task`를 사용하면 메서드가 대기 지점에서 분할됩니다. 이전의 모든 항목은 동기식으로 실행되고 나머지는 연속으로 등록됩니다. 스레드는 다른 작업을 수행하기 위해 해제됩니다.  `Task<T>`는 미래 가치를 나타냅니다.  `ValueTask<T>`는 결과가 이미 사용 가능한 경우 힙 할당을 방지하는 핫 경로에 대한 구조체 대안입니다.
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

### Q3: 확장 방법이란 무엇이며, 언제 사용해야 합니까?
**답:** 확장 메서드는 수정하지 않고 기존 형식에 메서드를 추가합니다. 이는 첫 번째 매개변수에`this`키워드가 있는 정적 클래스의 정적 메서드입니다. 이는 유창하고 연결 가능한 API를 가능하게 합니다. 이를 사용하여 소유하지 않은 유형(예:`string`또는`IEnumerable<T>`)에 유틸리티 메서드를 추가합니다. 과도하게 사용하지 마십시오. 코드를 발견하기 어렵게 만들 수 있습니다.
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

### 질문 4: 최신 C#에서 패턴 일치는 어떻게 작동합니까?
**답:** C#에는 점점 더 강력한 패턴 일치 기능이 추가되었습니다. 스위치 식(C# 8), 유형 패턴, 속성 패턴, 관계형 패턴 및 목록 패턴(C# 11)은 간결하고 표현력이 풍부한 조건부 논리를 허용합니다. 패턴 일치는 긴 if/else 체인을 대체하고 컴파일러에 의해 철저하게 검사됩니다.
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

### 질문 5: .NET의 종속성 주입이란 무엇이며 어떻게 사용합니까?
**A:** .NET에는`Microsoft.Extensions.DependencyInjection`를 통한 DI 지원이 내장되어 있습니다. 수명(Singleton, Scoped, Transient)으로 서비스를 등록하면 컨테이너가 생성자 매개변수를 통해 서비스를 주입합니다. 싱글톤: 앱에 대한 하나의 인스턴스입니다. 범위: HTTP 요청당 하나. 일시적: 매번 새 인스턴스입니다.
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

## 사고 사슬 문제 해결
### 문제 1: 캐싱을 사용하여 일반 저장소 구축
**문제 설명:** 캐싱을 추가하는 데코레이터를 사용하여 일반 저장소 패턴을 구현합니다. 저장소는 CRUD 작업을 지원해야 하며 캐싱 데코레이터는 읽기를 캐시하고 쓰기 시 무효화해야 합니다.
**1단계 - 문제 이해:**
(1) 일반`IRepository<T>`인터페이스, (2) 구체적인 구현(예: 메모리 내), (3) 모든 저장소를 래핑하는 캐싱 데코레이터, (4) 쓰기 작업 시 캐시 무효화가 필요합니다. 데코레이터 패턴은 데이터 액세스 논리에 직교하는 캐싱을 유지합니다.
**2단계 - 접근 방식 파악:**
-`Get`,`GetAll`,`Add`,`Update`,`Delete`로 `IRepository<T>`를 정의합니다.
- `IRepository<T>`를 래핑하고 `IMemoryCache`를 사용하는 `CachingRepository<T>`를 만듭니다.
- 캐시 키:`typeof(T).Name:{id}`.
- 쓰기 작업 시 캐시 항목을 무효화합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 우려사항 분리: 캐싱은 데코레이터이지 저장소에 혼합되지 않습니다.
- DI 등록:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(Scrutor 사용).
- 프로덕션: 다중 서버 시나리오에는 `IDistributedCache`(Redis)를 사용하고`CacheStampede`보호를 통해 캐시 배제 패턴을 추가합니다.
### 문제 2: 미들웨어 파이프라인 구현
**문제 설명:** ASP.NET Core의 요청 파이프라인과 유사한 미들웨어 파이프라인을 빌드합니다. 각 미들웨어는 요청을 처리하고, 다음 미들웨어를 호출하고, 응답을 처리할 수 있습니다.
**1단계 - 문제 이해:**
(1) 파이프라인을 나타내는`RequestDelegate`유형, (2) 다음 대리자를 래핑하는 미들웨어, (3) 미들웨어 구성을 위한 빌더 API가 필요합니다. 이는 대리인으로 구현된 책임 사슬 패턴입니다.
**2단계 - 접근 방식 파악:**
- `RequestDelegate`는 `Func<Context, RequestDelegate, Task>`입니다.
- 각 미들웨어는 컨텍스트와`next`기능을 받습니다.
- `Use`는 미들웨어를 추가합니다.  `Build`는 이를 단일 대리자로 구성합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 미들웨어 순서 중요: 처음 추가됨 = 가장 바깥쪽(요청 시 먼저 실행되고 응답 시 마지막으로 실행됨)
- 터미널 미들웨어(`next` 호출 없음)는 파이프라인을 단락시킵니다.
- 프로덕션: ASP.NET Core의 파이프라인은 정확히 이 패턴이며, 제로 할당을 위해 컴파일된 식 트리로 최적화되었습니다.
---

## 요약
C#은 뛰어난 도구와 강력한 생태계를 갖춘 세련되고 현대적인 범용 언어입니다. 엔터프라이즈 개발, 게임 개발(Unity) 및 크로스 플랫폼 애플리케이션에 탁월합니다. 언어는 빠르게 발전했습니다. 최신 C#은 간결하고 표현력이 풍부하며 형식이 안전합니다. Java 또는 Python과 같은 생태계 규모는 없지만 .NET의 품질과 일관성 덕분에 C#은 다양한 응용 프로그램에서 생산적이고 즐거운 언어가 됩니다.