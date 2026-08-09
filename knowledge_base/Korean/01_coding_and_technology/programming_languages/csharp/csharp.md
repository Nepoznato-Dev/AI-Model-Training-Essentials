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

### 레코드(C# 9+) — 불변 데이터 유형
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
| **.NET 마우이** | 모바일/데스크탑 | iOS, Android, macOS, Windows용 크로스 플랫폼 앱 |
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
| C#9 | 2020 | **레코드**, 최상위 명령문,`init`속성 ​​|
| C#10 | 2021 | 레코드 구조체, 전역 `using`, 파일 범위 네임스페이스 |
| C#11 | 2022 | 원시 문자열 리터럴, 목록 패턴,`required`멤버, 일반 수학 |
| C#12 | 2023 | 기본 생성자, 컬렉션 표현식, 인라인 배열 |
| C# 13 | 2024년 | `params`컬렉션, 새로운 잠금 유형, 최고 수준 범위 |
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

## 요약
C#은 뛰어난 도구와 강력한 생태계를 갖춘 세련되고 현대적인 범용 언어입니다. 엔터프라이즈 개발, 게임 개발(Unity) 및 크로스 플랫폼 애플리케이션에 탁월합니다. 언어는 빠르게 발전했습니다. 최신 C#은 간결하고 표현력이 풍부하며 형식이 안전합니다. Java 또는 Python과 같은 생태계 규모는 없지만 .NET의 품질과 일관성 덕분에 C#은 다양한 응용 프로그램에서 생산적이고 즐거운 언어가 됩니다.