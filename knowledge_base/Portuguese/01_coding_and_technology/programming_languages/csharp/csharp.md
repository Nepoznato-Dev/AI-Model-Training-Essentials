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
C# (pronuncia-se "C-sharp") é uma linguagem de programação moderna, orientada a objetos e com segurança de tipo, desenvolvida pela Microsoft sob a liderança de Anders Hejlsberg e lançada pela primeira vez em 2002. Ela roda na plataforma .NET e foi projetada para combinar o poder do C++ com a produtividade do Visual Basic. Hoje, C# é uma linguagem versátil e multiplataforma usada para aplicativos web (ASP.NET), software de desktop (Windows), desenvolvimento de jogos (Unity), aplicativos móveis (MAUI), serviços em nuvem (Azure) e muito mais.
C# tem absorvido constantemente as melhores ideias de outras linguagens — LINQ, async/await, records, correspondência de padrões — tornando-a uma das linguagens mais ricas em recursos e fáceis de desenvolver disponíveis.
---

## Por que C# é importante
- **Mecanismo de jogo Unity**: o idioma principal do Unity, o mecanismo de jogo mais popular do mundo por contagem de desenvolvedores.
- **Desenvolvimento empresarial**: ASP.NET Core é uma das estruturas web mais rápidas disponíveis (supera consistentemente os benchmarks da TechEmpower).
- **Plataforma cruzada**: .NET 5+ é executado em Windows, macOS e Linux. Não é mais apenas Windows.
- **Produtividade**: Excelente suporte IDE (Visual Studio, Rider), sistema de tipo forte e recursos de sintaxe modernos.
- **pioneiro do async/await**: C# introduziu o async/await em 2012 — anos antes de outras linguagens adotarem o padrão.
- **LINQ**: a consulta integrada à linguagem permite escrever consultas semelhantes a SQL diretamente em C# em qualquer fonte de dados.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Associação do Windows** | Historicamente vinculado ao Windows; percepção fica aquém da realidade | .NET 6+ é totalmente multiplataforma |
| **Ecossistema menor que Java** | Menos bibliotecas de terceiros que Maven/PyPI | NuGet está crescendo; muitas bibliotecas Java possuem equivalentes em C# |
| **Menos comum em startups** | Mais popular nas empresas do que no Vale do Silício | Go, Rust, Node.js para microsserviços nativos da nuvem |
| **Celular (MAUI)** | Xamarin/MAUI é menos maduro que nativo ou Flutter | Use Swift/Kotlin ou Flutter nativos para aplicativos móveis complexos |
| **GUI Linux** | Opções limitadas de GUI nativa no Linux | Use UIs baseadas na web (Blazor) ou Avalonia |
---

## Fundamentos de sintaxe
### Estrutura Básica
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

### Programação Orientada a Objetos
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

### Registros (C# 9+) — Tipos de dados imutáveis
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

### LINQ — Consulta integrada à linguagem
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

### Assíncrono/Aguardar
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

### Correspondência de padrões (C# 7-13)
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

## Sintaxe e padrões avançados
### Genéricos
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

### Delegados, eventos e expressões lambda
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

### Hierarquias de exceções personalizadas
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

### Sobrecarga do Operador
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

## Simultaneidade e paralelismo
### async/await Internos
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

### LINQ Paralelo e Biblioteca Paralela de Tarefas
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

## Configuração do projeto e sistema de construção
### Estrutura do Projeto
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

Arquivo ### .csproj
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

### Testando com xUnit
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

### Pipeline de CI/CD
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

## Interoperabilidade
### P/Invoke — Chamando bibliotecas C
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

### Interoperabilidade C++/CLI
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

## Padrões de Projeto
### Padrão Builder (API Fluente)
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

### Padrão de Estratégia com Delegados
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

## Desempenho e otimização
### Ferramentas de criação de perfil
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

## Implantação
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

### Implantação específica da plataforma
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

## O ecossistema .NET
### Frameworks e plataformas
| Estrutura | Domínio | Descrição |
|-----------|--------|-------------|
| **ASP.NET Core** | Rede | Estrutura web de alto desempenho para APIs e aplicativos web |
| **Blazor** | Web (front-end) | Crie UIs web interativas com C# em vez de JavaScript |
| **Núcleo do Entity Framework** | ORM | Acesso a banco de dados com LINQ; migrações que priorizam o código |
| **Unidade** | Jogos | O mecanismo de jogo mais popular do mundo (script C#) |
| **.NET MAUI** | Móvel/Desktop | Aplicativos multiplataforma para iOS, Android, macOS, Windows |
| **Avalônia** | Área de trabalho | UI de desktop multiplataforma (como WPF para todas as plataformas) |
### Gerenciamento de compilação e pacotes
| Ferramenta | Finalidade |
|------|---------|
| **CLI dotnet** | Construa, execute, teste, publique na linha de comando |
| **NuGet** | Gerenciador de pacotes |
| **MSBuild** | Sistema de construção subjacente |
| **Visual Studio/Rider** | IDEs |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## Versões da linguagem C#
| Versão | Ano | Principais recursos |
|--------|------|---------|
| C#7 | 2017 | Correspondência de padrões, tuplas, variáveis ​​`out`, funções locais |
| C#8 | 2019 | Tipos de referência anuláveis, expressões `switch`, fluxos assíncronos |
| C#9 | 2020 | **Registros**, instruções de nível superior, propriedades`init`|
| C#10 | 2021 | Estruturas de registro,`using`globais, namespaces com escopo de arquivo |
| C#11 | 2022 | Literais de string bruta, padrões de lista, membros `required`, matemática genérica |
| C#12 | 2023 | Construtores primários, expressões de coleção, matrizes embutidas |
| C#13 | 2024 |  Coleções `params`, novos tipos de bloqueio, extensões de primeira classe |
---

## Quando usar C#
| Cenário | Por que C# | Melhor Alternativa |
|----------|--------|-------------------|
| Desenvolvimento de jogos (Unity) | A linguagem de script padrão do Unity | -- |
| Back-ends da web corporativos | ASP.NET Core é rápido, maduro e bem suportado | Java (inicialização Spring) |
| Aplicativos de área de trabalho do Windows | WPF, WinForms, WinUI estão maduros | -- |
| Desktop multiplataforma | Avalônia ou MAUI | Elétron (baseado na web) |
| Front-end da Web (Blazor) | C# full-stack — sem necessidade de JavaScript | React/Vue/Angular para ecossistemas SPA mais ricos |
| Serviços em nuvem (Azure) | Integração profunda com o Azure | -- |
| Aplicativos móveis (MAUI) | Plataforma cruzada com C# | Flutter, React Native ou Swift/Kotlin nativo |
| IA/ML | Possível com ML.NET | Python (preferencialmente preferido) |
| Ferramentas/scripts CLI | Possível, mas detalhado | Vá, Ferrugem, Python |
---

## Perguntas e respostas sintéticas
### Q1: Qual é a diferença entre`class`e`record`em C#?
**R:** Um`class`é um tipo de referência com propriedades mutáveis ​​por padrão — duas variáveis ​​podem fazer referência ao mesmo objeto. Um`record`(C# 9+) é um tipo de referência com igualdade baseada em valor — dois registros com os mesmos dados são considerados iguais. Os registros têm propriedades somente de inicialização, um`ToString`integrado e suportam expressões`with`para mutação não destrutiva. Utilizar registros para suportes de dados (DTOs, objetos de valor); use classes para entidades ricas em comportamento com identidade.
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

### Q2: Como async/await e`Task`funcionam internamente?
**R:**`async/await`é um açúcar sintático sobre uma máquina de estado gerada pelo compilador. Quando você usa`await`a`Task`, o método é dividido no ponto de espera: tudo antes é executado de forma síncrona e o restante é registrado como uma continuação. O thread é liberado para fazer outro trabalho. `Task<T>`representa um valor futuro. `ValueTask<T>`é uma alternativa de estrutura para caminhos ativos que evita a alocação de heap quando o resultado já está disponível.
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

### Q3: O que são métodos de extensão e quando devo usá-los?
**R:** Os métodos de extensão adicionam métodos aos tipos existentes sem modificá-los. São métodos estáticos em uma classe estática, com a palavra-chave`this`no primeiro parâmetro. Eles permitem uma API fluente e encadeada. Use-os para adicionar métodos utilitários a tipos que você não possui (como`string`ou`IEnumerable<T>`). Evite usá-los excessivamente – eles podem dificultar a descoberta do código.
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

### Q4: Como funciona a correspondência de padrões no C# moderno?
**R:** C# adicionou progressivamente correspondência de padrões mais poderosa. Expressões de alternância (C# 8), padrões de tipo, padrões de propriedade, padrões relacionais e padrões de lista (C# 11) permitem lógica condicional concisa e expressiva. A correspondência de padrões substitui longas cadeias if/else e é verificada exaustivamente pelo compilador.
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

### Q5: O que é injeção de dependência no .NET e como posso usá-la?
**R:** .NET tem suporte DI integrado via`Microsoft.Extensions.DependencyInjection`. Você registra serviços com seus tempos de vida (Singleton, Scoped, Transient) e o contêiner os injeta por meio de parâmetros do construtor. Singleton: uma instância para o aplicativo. Escopo: um por solicitação HTTP. Transitório: nova instância a cada vez.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construa um Repositório Genérico com Cache
**Declaração do problema:** Implemente um padrão de repositório genérico com um decorador que adicione cache. O repositório deve suportar operações CRUD, e o decorador de cache deve armazenar em cache as leituras e invalidar as gravações.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) uma interface genérica `IRepository<T>`, (2) uma implementação concreta (por exemplo, na memória), (3) um decorador de cache que envolva qualquer repositório, (4) invalidação de cache em operações de gravação. O padrão decorador mantém o cache ortogonal à lógica de acesso a dados.
**Etapa 2 — Identifique a abordagem:**
- Defina`IRepository<T>`com`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Crie`CachingRepository<T>`que envolve`IRepository<T>`e usa`IMemoryCache`.
- Chave de cache: `typeof(T).Name:{id}`.
- Nas operações de gravação, invalide a entrada do cache.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Separação de interesses: o cache é um decorador, não misturado ao repositório.
- Cadastro DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(usando Scrutor).
- Produção: use`IDistributedCache`(Redis) para cenários de vários servidores e adicione padrões de cache-aside com proteção `CacheStampede`.
### Problema 2: Implementar um pipeline de middleware
**Declaração do problema:** Crie um pipeline de middleware semelhante ao pipeline de solicitação do ASP.NET Core. Cada middleware pode processar a solicitação, chamar o próximo middleware e processar a resposta.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) um tipo`RequestDelegate`representando o pipeline, (2) middleware que envolve o próximo delegado, (3) uma API construtora para compor o middleware. Este é o padrão de Cadeia de Responsabilidade implementado com delegados.
**Etapa 2 — Identifique a abordagem:**
-`RequestDelegate`é`Func<Context, RequestDelegate, Task>`.
- Cada middleware recebe o contexto e uma função `next`.
-`Use`adiciona middleware; `Build`os compõe em um único delegado.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- A ordem do middleware é importante: primeiro adicionado = mais externo (executado primeiro na solicitação, último na resposta).
- O middleware do terminal (sem chamada `next`) causa curto-circuito no pipeline.
- Produção: o pipeline do ASP.NET Core segue exatamente esse padrão, otimizado com árvores de expressão compiladas para alocação zero.
---

## Resumo
C# é uma linguagem polida, moderna e de uso geral, com excelentes ferramentas e um ecossistema forte. É excelente em desenvolvimento empresarial, desenvolvimento de jogos (Unity) e aplicativos multiplataforma. A linguagem evoluiu rapidamente – o C# moderno é conciso, expressivo e de tipo seguro. Embora não tenha o tamanho do ecossistema de Java ou Python, a qualidade e a consistência do .NET tornam o C# uma linguagem produtiva e agradável para uma ampla variedade de aplicativos.