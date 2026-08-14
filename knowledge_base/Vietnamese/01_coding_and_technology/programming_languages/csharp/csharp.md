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
C# (phát âm là "C-sharp") là ngôn ngữ lập trình hiện đại, hướng đối tượng, an toàn kiểu được phát triển bởi Microsoft dưới sự lãnh đạo của Anders Hejlsberg và phát hành lần đầu tiên vào năm 2002. Nó chạy trên nền tảng .NET và được thiết kế để kết hợp sức mạnh của C++ với năng suất của Visual Basic. Ngày nay, C# là ngôn ngữ đa nền tảng, linh hoạt được sử dụng cho các ứng dụng web (ASP.NET), phần mềm máy tính để bàn (Windows), phát triển trò chơi (Unity), ứng dụng di động (MAUI), dịch vụ đám mây (Azure), v.v.
C# đã dần dần tiếp thu những ý tưởng hay nhất từ ​​các ngôn ngữ khác — LINQ, async/await, record, samplematch — khiến nó trở thành một trong những ngôn ngữ giàu tính năng và thân thiện với nhà phát triển nhất hiện có.
---

## Tại sao C# lại quan trọng
- **Công cụ trò chơi Unity**: Ngôn ngữ chính của Unity, công cụ trò chơi phổ biến nhất thế giới tính theo số lượng nhà phát triển.
- **Phát triển doanh nghiệp**: ASP.NET Core là một trong những khung web nhanh nhất hiện có (luôn đứng đầu các điểm chuẩn của TechEmpower).
- **Đa nền tảng**: .NET 5+ chạy trên Windows, macOS và Linux. Không còn chỉ dành cho Windows nữa.
- **Năng suất**: Hỗ trợ IDE tuyệt vời (Visual Studio, Rider), hệ thống kiểu mạnh mẽ và các tính năng cú pháp hiện đại.
- **tiên phong về async/await**: C# đã giới thiệu async/await vào năm 2012 — nhiều năm trước khi các ngôn ngữ khác áp dụng mô hình này.
- **LINQ**: Truy vấn tích hợp ngôn ngữ cho phép bạn viết các truy vấn giống SQL trực tiếp trong C# dựa trên bất kỳ nguồn dữ liệu nào.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Hiệp hội Windows** | Về mặt lịch sử gắn liền với Windows; nhận thức tụt hậu so với thực tế | .NET 6+ hoàn toàn đa nền tảng |
| **Hệ sinh thái nhỏ hơn Java** | Ít thư viện của bên thứ ba hơn Maven/PyPI | NuGet đang phát triển; nhiều thư viện Java có tương đương với C# |
| **Ít phổ biến hơn ở các công ty khởi nghiệp** | Phổ biến trong doanh nghiệp hơn ở Thung lũng Silicon | Go, Rust, Node.js cho các dịch vụ vi mô gốc đám mây |
| **Di động (MAUI)** | Xamarin/MAUI kém trưởng thành hơn bản địa hoặc Flutter | Sử dụng Swift/Kotlin hoặc Flutter gốc cho các ứng dụng di động phức tạp |
| **Giao diện Linux** | Tùy chọn GUI gốc hạn chế trên Linux | Sử dụng giao diện người dùng dựa trên web (Blazor) hoặc Avalonia |
---

##Cơ bản về cú pháp
###Cấu trúc cơ bản
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

### Lập trình hướng đối tượng
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

### Bản ghi (C# 9+) - Kiểu dữ liệu bất biến
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

### LINQ — Truy vấn tích hợp ngôn ngữ
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

### Không đồng bộ/Đang chờ
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

### Khớp mẫu (C# 7-13)
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

## Cú pháp & Mẫu nâng cao
### Thuốc gốc
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

### Đại biểu, Sự kiện và Biểu thức Lambda
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

### Phân cấp ngoại lệ tùy chỉnh
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

### Quá tải toán tử
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

## Đồng thời & Song song
### async/await Nội bộ
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

### LINQ song song và thư viện song song tác vụ
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
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

### Tệp .csproj
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

### Thử nghiệm với xUnit
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

### Đường ống CI/CD
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

## Khả năng tương tác
### P/Invoke — Gọi thư viện C
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

### Tương tác C++/CLI
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

## Mẫu thiết kế
### Mẫu trình tạo (API thông thạo)
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

### Mẫu chiến lược với đại biểu
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

## Triển khai
###Tệp Docker
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

### Triển khai theo nền tảng cụ thể
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

## Hệ sinh thái .NET
### Khung và Nền tảng
| Khung | Tên miền | Mô tả |
|----------|----------|-------------|
| **Lõi ASP.NET** | Web | Khung web hiệu suất cao cho API và ứng dụng web |
| **Blazor** | Web (giao diện người dùng) | Xây dựng giao diện người dùng web tương tác bằng C# thay vì JavaScript |
| **Lõi khung thực thể** | ORM | Truy cập cơ sở dữ liệu bằng LINQ; di chuyển mã đầu tiên |
| **Đoàn kết** | Trò chơi | Công cụ trò chơi phổ biến nhất thế giới (kịch bản C#) |
| **.NET MAUI** | Điện thoại di động/Máy tính để bàn | Ứng dụng đa nền tảng cho iOS, Android, macOS, Windows |
| **Avalonia** | Máy tính để bàn | Giao diện người dùng máy tính để bàn đa nền tảng (như WPF cho tất cả các nền tảng) |
### Quản lý bản dựng và gói
| Công cụ | Mục đích |
|------|----------|
| **dotnet CLI** | Xây dựng, chạy, kiểm tra, xuất bản từ dòng lệnh |
| **NuGet** | Quản lý gói |
| **MSBuild** | Hệ thống xây dựng cơ bản |
| **Visual Studio / Rider** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## Phiên bản ngôn ngữ C#
| Phiên bản | Năm | Các tính năng chính |
|----------|------|-------------|
| C#7 | 2017 | Khớp mẫu, bộ dữ liệu, biến `out`, hàm cục bộ |
| C # 8 | 2019 | Các loại tham chiếu có thể rỗng, biểu thức `switch`, luồng không đồng bộ |
| C#9 | 2020 | **Bản ghi**, tuyên bố cấp cao nhất, thuộc tính`init`|
| C # 10 | 2021 | Cấu trúc bản ghi,`using`toàn cầu, không gian tên trong phạm vi tệp |
| C # 11 | 2022 | Chuỗi ký tự thô, mẫu danh sách, thành viên `required`, toán học chung |
| C # 12 | 2023 | Hàm tạo chính, biểu thức tập hợp, mảng nội tuyến |
| C# 13 | 2024 |  Bộ sưu tập `params`, loại khóa mới, nhịp hạng nhất |
---

## Khi nào nên sử dụng C#
| Kịch bản | Tại sao C# | Thay thế tốt hơn |
|----------|--------|-------------------|
| Phát triển trò chơi (Unity) | Ngôn ngữ kịch bản Unity tiêu chuẩn | -- |
| Phần mềm hỗ trợ web doanh nghiệp | ASP.NET Core nhanh, hoàn thiện, được hỗ trợ tốt | Java (Khởi động mùa xuân) |
| Ứng dụng máy tính để bàn Windows | WPF, WinForms, WinUI đã trưởng thành | -- |
| Máy tính để bàn đa nền tảng | Avalonia hoặc MAUI | Điện tử (dựa trên web) |
| Giao diện web (Blazor) | C# đầy đủ — không cần JavaScript | React/Vue/Angular cho hệ sinh thái SPA phong phú hơn |
| Dịch vụ đám mây (Azure) | Tích hợp Azure sâu | -- |
| Ứng dụng di động (MAUI) | Đa nền tảng với C# | Flutter, React Native hoặc Swift/Kotlin bản địa |
| AI/ML | Có thể với ML.NET | Python (được ưu tiên áp đảo) |
| Công cụ/tập lệnh CLI | Có thể nhưng dài dòng | Đi, Rust, Python |
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`class`và`record`trong C# là gì?
**A:**`class`là loại tham chiếu có các thuộc tính có thể thay đổi theo mặc định — hai biến có thể tham chiếu cùng một đối tượng.`record`(C# 9+) là loại tham chiếu có sự bằng nhau dựa trên giá trị - hai bản ghi có cùng dữ liệu được coi là bằng nhau. Các bản ghi chỉ có thuộc tính init,`ToString`tích hợp sẵn và hỗ trợ các biểu thức`with`cho đột biến không phá hủy. Sử dụng bản ghi cho vật mang dữ liệu (DTO, đối tượng giá trị); sử dụng các lớp cho các thực thể giàu hành vi có nhận dạng.
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

### Câu 2: Async/await và`Task`hoạt động nội bộ như thế nào?
**A:**`async/await`là đường cú pháp trên máy trạng thái do trình biên dịch tạo ra. Khi bạn`await`a`Task`, phương thức được phân chia tại điểm chờ: mọi thứ trước đó được thực thi đồng bộ, sau đó phần còn lại được đăng ký làm phần tiếp theo. Chủ đề được giải phóng để làm công việc khác. `Task<T>`đại diện cho một giá trị trong tương lai. `ValueTask<T>`là một giải pháp thay thế cấu trúc cho các đường dẫn nóng giúp tránh phân bổ đống khi đã có sẵn kết quả.
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

### Câu 3: Phương pháp mở rộng là gì và khi nào tôi nên sử dụng chúng?
**A:** Phương thức mở rộng thêm phương thức vào các loại hiện có mà không sửa đổi chúng. Chúng là các phương thức tĩnh trong một lớp tĩnh, với từ khóa`this`ở tham số đầu tiên. Chúng kích hoạt một API thông thạo, có thể kết nối được. Sử dụng chúng để thêm các phương thức tiện ích vào các loại bạn không sở hữu (như`string`hoặc`IEnumerable<T>`). Tránh lạm dụng chúng - chúng có thể khiến mã khó bị phát hiện.
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

### Q4: Việc khớp mẫu hoạt động như thế nào trong C# hiện đại?
**A:** C# đã dần dần bổ sung thêm tính năng khớp mẫu mạnh mẽ hơn. Biểu thức chuyển đổi (C# 8), mẫu kiểu, mẫu thuộc tính, mẫu quan hệ và mẫu danh sách (C# 11) cho phép logic có điều kiện ngắn gọn, biểu cảm. So khớp mẫu thay thế các chuỗi if/else dài và được trình biên dịch kiểm tra toàn diện.
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

### Câu hỏi 5: Nội dung phụ thuộc trong .NET là gì và tôi sử dụng nó như thế nào?
**A:** .NET có hỗ trợ DI tích hợp thông qua`Microsoft.Extensions.DependencyInjection`. Bạn đăng ký các dịch vụ theo thời gian tồn tại của chúng (Singleton, Scoped, Transient) và vùng chứa sẽ chèn chúng thông qua các tham số của hàm tạo. Singleton: một phiên bản cho ứng dụng. Phạm vi: một cho mỗi yêu cầu HTTP. Tạm thời: phiên bản mới mỗi lần.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xây dựng kho lưu trữ chung bằng bộ nhớ đệm
**Báo cáo vấn đề:** Triển khai mẫu kho lưu trữ chung bằng trình trang trí có thêm bộ nhớ đệm. Kho lưu trữ phải hỗ trợ các hoạt động CRUD và trình trang trí bộ nhớ đệm sẽ đọc và vô hiệu hóa hoạt động ghi vào bộ nhớ đệm.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) giao diện`IRepository<T>`chung, (2) triển khai cụ thể (ví dụ: trong bộ nhớ), (3) trình trang trí bộ nhớ đệm bao bọc bất kỳ kho lưu trữ nào, (4) vô hiệu hóa bộ đệm trong các hoạt động ghi. Mẫu trang trí giữ cho bộ đệm ẩn trực giao với logic truy cập dữ liệu.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Xác định`IRepository<T>`với`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Tạo`CachingRepository<T>`bao bọc`IRepository<T>`và sử dụng`IMemoryCache`.
- Khóa bộ đệm:`typeof(T).Name:{id}`.
- Khi thực hiện thao tác ghi, vô hiệu hóa mục nhập bộ đệm.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Tách biệt mối quan tâm: bộ nhớ đệm là vật trang trí, không trộn lẫn vào kho lưu trữ.
- Đăng ký DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(sử dụng Scrutor).
- Sản xuất: sử dụng`IDistributedCache`(Redis) cho các kịch bản nhiều máy chủ và thêm các mẫu dành riêng cho bộ đệm với tính năng bảo vệ `CacheStampede`.
### Vấn đề 2: Triển khai Middleware Pipeline
**Báo cáo vấn đề:** Xây dựng đường dẫn phần mềm trung gian tương tự như đường dẫn yêu cầu của ASP.NET Core. Mỗi phần mềm trung gian có thể xử lý yêu cầu, gọi phần mềm trung gian tiếp theo và xử lý phản hồi.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) loại`RequestDelegate`đại diện cho đường dẫn, (2) phần mềm trung gian bao bọc đại biểu tiếp theo, (3) API trình xây dựng để soạn phần mềm trung gian. Đây là mẫu Chuỗi trách nhiệm được triển khai với các đại biểu.
**Bước 2 — Xác định phương pháp tiếp cận:**
-`RequestDelegate`là `Func<Context, RequestDelegate, Task>`.
- Mỗi phần mềm trung gian nhận được ngữ cảnh và chức năng `next`.
-`Use`bổ sung phần mềm trung gian; `Build`kết hợp chúng thành một đại biểu duy nhất.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Vấn đề thứ tự phần mềm trung gian: được thêm đầu tiên = ngoài cùng (thực thi đầu tiên theo yêu cầu, cuối cùng khi phản hồi).
- Phần mềm trung gian đầu cuối (không có lệnh gọi `next`) làm đoản mạch đường ống.
- Sản xuất: Đường dẫn của ASP.NET Core chính xác là mẫu này, được tối ưu hóa với các cây biểu thức được biên dịch để phân bổ bằng 0.
---

## Bản tóm tắt
C# là một ngôn ngữ có mục đích chung, hiện đại, bóng bẩy với công cụ tuyệt vời và hệ sinh thái mạnh mẽ. Nó vượt trội trong phát triển doanh nghiệp, phát triển trò chơi (Unity) và các ứng dụng đa nền tảng. Ngôn ngữ đã phát triển nhanh chóng - C# hiện đại ngắn gọn, biểu cảm và an toàn về kiểu. Mặc dù nó không có quy mô hệ sinh thái như Java hoặc Python, nhưng chất lượng và tính nhất quán của .NET khiến C# trở thành ngôn ngữ hiệu quả và thú vị cho nhiều ứng dụng.