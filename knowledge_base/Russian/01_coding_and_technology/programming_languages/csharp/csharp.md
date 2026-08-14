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
# С#
C# (произносится как «C-sharp») — это современный объектно-ориентированный типобезопасный язык программирования, разработанный Microsoft под руководством Андерса Хейлсберга и впервые выпущенный в 2002 году. Он работает на платформе .NET и был разработан для объединения возможностей C++ с производительностью Visual Basic. Сегодня C# — это универсальный кроссплатформенный язык, используемый для веб-приложений (ASP.NET), настольного программного обеспечения (Windows), разработки игр (Unity), мобильных приложений (MAUI), облачных сервисов (Azure) и многого другого.
C# постепенно вобрал в себя лучшие идеи других языков — LINQ, async/await, записей, сопоставления с образцом — что сделало его одним из наиболее многофункциональных и удобных для разработчиков языков.
---

## Почему C# важен
- **Игровой движок Unity**: основной язык Unity, самого популярного игрового движка в мире по количеству разработчиков.
- **Корпоративная разработка**: ASP.NET Core — одна из самых быстрых доступных веб-платформ (постоянно превосходит результаты тестов TechEmpower).
- **Кроссплатформенность**: .NET 5+ работает в Windows, macOS и Linux. Больше не только для Windows.
- **Производительность**: отличная поддержка IDE (Visual Studio, Rider), строгая система типов и современные функции синтаксиса.
- **Пионер async/await**: C# представил async/await в 2012 году — за несколько лет до того, как другие языки переняли этот шаблон.
- **LINQ**: запросы, интегрированные в язык, позволяют писать SQL-подобные запросы непосредственно на C# к любому источнику данных.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Ассоциация Windows** | Исторически привязан к Windows; восприятие отстает от реальности | .NET 6+ полностью кроссплатформен |
| **Экосистема меньше, чем у Java** | Меньше сторонних библиотек, чем в Maven/PyPI | NuGet растет; многие библиотеки Java имеют эквиваленты на C# |
| **Реже встречается в стартапах** | Более популярен среди предприятий, чем в Кремниевой долине | Go, Rust, Node.js для облачных микросервисов |
| **Мобильный (MAUI)** | Xamarin/MAUI менее зрелый, чем нативный или Flutter | Используйте родной Swift/Kotlin или Flutter для сложных мобильных приложений |
| **Графический интерфейс Linux** | Ограниченные возможности встроенного графического интерфейса в Linux | Используйте веб-интерфейсы (Blazor) или Avalonia |
---

## Основы синтаксиса
### Базовая структура
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

### Объектно-ориентированное программирование
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

### Записи (C# 9+) — неизменяемые типы данных
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

### LINQ — запрос, интегрированный с языком
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

### Асинхронность/ожидание
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

### Сопоставление с образцом (C# 7–13)
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

## Расширенный синтаксис и шаблоны
### Дженерики
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

### Делегаты, события и лямбда-выражения
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

### Пользовательские иерархии исключений
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

### Перегрузка оператора
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

## Параллелизм и параллелизм
### асинхронность/ожидание Внутренние функции
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

### Параллельная библиотека LINQ и параллельных задач
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

## Конфигурация проекта и система сборки
### Структура проекта
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

### Файл .csproj
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

### Тестирование с помощью xUnit
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

### Конвейер CI/CD
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

## Совместимость
### P/Invoke — вызов библиотек C
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

### Взаимодействие C++/CLI
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

## Шаблоны проектирования
### Шаблон строителя (Fluent API)
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

### Шаблон стратегии с делегатами
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

## Производительность и оптимизация
### Инструменты профилирования
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

## Развертывание
### Докер-файл
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

### Развертывание для конкретной платформы
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

## Экосистема .NET
### Фреймворки и платформы
| Рамочная | Домен | Описание |
|-----------|--------|-------------|
| **ASP.NET Core** | Интернет | Высокопроизводительная веб-инфраструктура для API и веб-приложений |
| **Блазор** | Веб (интерфейс) | Создавайте интерактивные веб-интерфейсы с помощью C# вместо JavaScript |
| **Ядро Entity Framework** | ОРМ | Доступ к базе данных с помощью LINQ; миграция с приоритетом кода |
| **Единство** | Игры | Самый популярный в мире игровой движок (скрипты C#) |
| **.NET МАУИ** | Мобильный/Настольный компьютер | Кроссплатформенные приложения для iOS, Android, macOS, Windows |
| **Авалония** | Рабочий стол | Межплатформенный пользовательский интерфейс рабочего стола (например, WPF для всех платформ) |
### Управление сборкой и пакетами
| Инструмент | Цель |
|------|---------|
| **интерфейс командной строки dotnet** | Сборка, запуск, тестирование и публикация из командной строки |
| **НюГет** | Менеджер пакетов |
| **MSBuild** | Базовая система сборки |
| **Визуальная студия/Райдер** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## Версии языка C#
| Версия | Год | Ключевые особенности |
|---------|------|-------------|
| С#7 | 2017 | Сопоставление с образцом, кортежи, переменные `out`, локальные функции |
| С# 8 | 2019 | Ссылочные типы, допускающие значение NULL, выражения `switch`, асинхронные потоки |
| С#9 | 2020 | **Записи**, операторы верхнего уровня, свойства`init`|
| С# 10 | 2021 | Структуры записи, глобальные `using`, пространства имен в области файлов |
| С# 11 | 2022 | Необработанные строковые литералы, шаблоны списков, члены `required`, общие математические вычисления |
| С# 12 | 2023 | Первичные конструкторы, выражения коллекций, встроенные массивы |
| С# 13 | 2024 |  Коллекции `params`, новые типы замков, первоклассные пролеты |
---

## Когда использовать C#
| Сценарий | Почему С# | Лучшая альтернатива |
|----------|--------|-------------------|
| Разработка игр (Unity) | Стандартный язык сценариев Unity | -- |
| Корпоративные веб-серверы | ASP.NET Core — быстрый, зрелый и хорошо поддерживаемый | Java (весенняя загрузка) |
| Настольные приложения для Windows | WPF, WinForms, WinUI являются зрелыми | -- |
| Кроссплатформенный рабочий стол | Авалония или МАУИ | Электрон (через Интернет) |
| Веб-интерфейс (Blazor) | Полнофункциональный C# — JavaScript не требуется | React/Vue/Angular для более богатых SPA-экосистем |
| Облачные сервисы (Azure) | Глубокая интеграция с Azure | -- |
| Мобильные приложения (MAUI) | Кроссплатформенность с C# | Flutter, React Native или нативный Swift/Kotlin |
| ИИ/МО | Возможно с ML.NET | Python (в подавляющем большинстве предпочтительнее) |
| Инструменты/скрипты CLI | Возможно, но многословно | Вперёд, Rust, Python |
---

## Синтетические вопросы и ответы
### Вопрос 1. В чем разница между`class`и`record`в C#?
**A:**`class`— это ссылочный тип с изменяемыми свойствами по умолчанию — две переменные могут ссылаться на один и тот же объект.`record`(C# 9+) — это ссылочный тип с равенством на основе значений — две записи с одинаковыми данными считаются равными. Записи имеют свойства только для инициализации, встроенный`ToString`и поддерживают выражения`with`для неразрушающей мутации. Использовать записи для носителей данных (DTO, объекты-значения); используйте классы для сущностей с богатым поведением и индивидуальностью.
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

### Вопрос 2: Как работают async/await и `Task`?
**A:**`async/await`— это синтаксический сахар над конечным автоматом, созданным компилятором. Когда вы`await`a`Task`, метод разделяется в точке ожидания: все, что было раньше, выполняется синхронно, затем остаток регистрируется как продолжение. Поток освобождается для выполнения другой работы. `Task<T>`представляет собой будущую стоимость. `ValueTask<T>`— это альтернатива структуры для горячих путей, которая позволяет избежать выделения кучи, когда результат уже доступен.
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

### В3: Что такое методы расширения и когда их следует использовать?
**О:** Методы расширения добавляют методы к существующим типам, не изменяя их. Это статические методы статического класса с ключевым словом`this`в первом параметре. Они обеспечивают плавный, цепной API. Используйте их для добавления служебных методов к типам, которыми вы не владеете (например,`string`или `IEnumerable<T>`). Не злоупотребляйте ими — они могут затруднить обнаружение кода.
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

### Вопрос 4. Как сопоставление с образцом работает в современном C#?
**A:** В C# постепенно стали добавляться более мощные возможности сопоставления с образцом. Выражения переключения (C# 8), шаблоны типов, шаблоны свойств, реляционные шаблоны и шаблоны списков (C# 11) обеспечивают краткую и выразительную условную логику. Сопоставление с образцом заменяет длинные цепочки if/else и полностью проверяется компилятором.
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

### Вопрос 5. Что такое внедрение зависимостей в .NET и как его использовать?
**A:** .NET имеет встроенную поддержку DI через `Microsoft.Extensions.DependencyInjection`. Вы регистрируете сервисы с указанием их времени жизни (Singleton, Scoped, Transient), а контейнер внедряет их через параметры конструктора. Синглтон: один экземпляр для приложения. Область действия: один на каждый HTTP-запрос. Переходный: каждый раз новый экземпляр.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создайте универсальный репозиторий с кэшированием
**Постановка задачи.** Реализуйте общий шаблон репозитория с помощью декоратора, добавляющего кеширование. Репозиторий должен поддерживать операции CRUD, а декоратор кэширования должен кэшировать операции чтения и делать недействительными операции записи.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) общий интерфейс `IRepository<T>`, (2) конкретная реализация (например, в памяти), (3) декоратор кэширования, который обертывает любой репозиторий, (4) аннулирование кэша при операциях записи. Шаблон декоратора сохраняет кэширование ортогональным логике доступа к данным.
**Шаг 2. Определите подход:**
- Определите`IRepository<T>`с помощью `Get`, `GetAll`, `Add`, `Update`, `Delete`.
— Создайте `CachingRepository<T>`, который обертывает`IRepository<T>`и использует `IMemoryCache`.
- Ключ кэша: `typeof(T).Name:{id}`.
- При операциях записи сделать недействительной запись в кэше.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Разделение задач: кеширование — это декоратор, не подмешанный к репозиторию.
- Регистрация DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(с помощью Scrutor).
- Производство: используйте`IDistributedCache`(Redis) для сценариев с несколькими серверами и добавляйте шаблоны кэширования с защитой `CacheStampede`.
### Проблема 2: реализация конвейера промежуточного программного обеспечения
**Постановка задачи.** Создайте конвейер промежуточного программного обеспечения, аналогичный конвейеру запросов ASP.NET Core. Каждое промежуточное программное обеспечение может обрабатывать запрос, вызывать следующее промежуточное программное обеспечение и обрабатывать ответ.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) тип `RequestDelegate`, представляющий конвейер, (2) промежуточное программное обеспечение, которое обертывает следующего делегата, (3) API-интерфейс компоновщика для создания промежуточного программного обеспечения. Это шаблон цепочки ответственности, реализованный с помощью делегатов.
**Шаг 2. Определите подход:**
-`RequestDelegate`— это `Func<Context, RequestDelegate, Task>`.
- Каждое промежуточное программное обеспечение получает контекст и функцию `next`.
-`Use`добавляет промежуточное программное обеспечение; `Build`объединяет их в один делегат.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Порядок промежуточного программного обеспечения имеет значение: первое добавленное = самое внешнее (выполняется первым по запросу, последним по ответу).
- Промежуточное ПО терминала (без вызова `next`) закорачивает конвейер.
- Производство: конвейер ASP.NET Core представляет собой именно этот шаблон, оптимизированный с помощью скомпилированных деревьев выражений для нулевого распределения.
---

## Краткое содержание
C# — это совершенный, современный язык общего назначения с отличными инструментами и мощной экосистемой. Он преуспевает в корпоративной разработке, разработке игр (Unity) и кроссплатформенных приложениях. Язык быстро развивался — современный C# лаконичен, выразителен и типобезопасен. Несмотря на то, что он не имеет такого размера экосистемы, как Java или Python, качество и согласованность .NET делают C# продуктивным и приятным языком для широкого спектра приложений.