---
# Metadata
title: "C# — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern C# code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [csharp, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C#: patrones idiomáticos y mejores prácticas
Esta guía cubre patrones idiomáticos y mejores prácticas para escribir código C# (12+) limpio y moderno.
---

## Sintaxis moderna de C#
```csharp
// ✅ Records for data
public record User(string Name, string Email, int Age);

var user = new User("Alice", "alice@example.com", 30);
var (name, email, _) = user;  // deconstruction

// ✅ Pattern matching
string Describe(object obj) => obj switch
{
    int n when n > 0  => $"Positive: {n}",
    int n when n < 0  => $"Negative: {n}",
    int 0             => "Zero",
    string s          => $"String: {s}",
    null              => "Null",
    _                 => "Unknown"
};

// ✅ Property patterns
if (user is { Age: >= 18, Role: "admin" })
{
    GrantAccess(user);
}

// ✅ File-scoped namespaces
namespace MyApp.Services;

// ✅ Global usings
global using System;
global using System.Collections.Generic;

// ✅ Raw string literals
var json = """
    {
        "name": "Alice",
        "email": "alice@example.com"
    }
    """;
```

---

## Seguridad nula
```csharp
// ✅ Nullable reference types
#nullable enable
public string? MiddleName { get; set; }

// ✅ Null-conditional operator
var city = user?.Address?.City;
int length = name?.Length ?? 0;

// ✅ Null-coalescing assignment
config ??= LoadDefaultConfig();

// ✅ ArgumentNullException.ThrowIfNull (C# 10+)
public void Process(string input)
{
    ArgumentNullException.ThrowIfNull(input);
    // use input safely
}
```

---

##LINQ
```csharp
// ✅ LINQ for collection transformations
var adults = users
    .Where(u => u.Age >= 18)
    .OrderBy(u => u.Name)
    .Select(u => u.Name)
    .ToList();

// ✅ Method syntax (preferred for complex queries)
var grouped = users
    .GroupBy(u => u.Role)
    .ToDictionary(g => g.Key, g => g.ToList());

// ✅ Query syntax for SQL-like queries
var result = from u in users
             where u.Age > 18
             orderby u.Name
             select new { u.Name, u.Email };

// ✅ LINQ performance: avoid multiple enumerations
var userList = users.ToList();  // materialize once
```

---

## Asíncrono/Espera
```csharp
// ✅ async/await all the way
public async Task<User> GetUserAsync(int id)
{
    return await _context.Users.FindAsync(id)
        ?? throw new NotFoundException($"User {id} not found");
}

// ✅ ConfigureAwait(false) in libraries
public async Task<byte[]> DownloadAsync(string url)
{
    using var client = new HttpClient();
    return await client.GetByteArrayAsync(url).ConfigureAwait(false);
}

// ✅ Parallel async operations
var (users, posts) = await (FetchUsersAsync(), FetchPostsAsync());

// ✅ ValueTask for hot paths
public async ValueTask<int> GetCountAsync() => await _cache.GetAsync();

// ✅ CancellationToken
public async Task ProcessAsync(CancellationToken ct = default)
{
    while (!ct.IsCancellationRequested)
    {
        await DoWorkAsync(ct);
    }
}
```

---

## Inyección de dependencia
```csharp
// ✅ Constructor injection
public class UserService(IUserRepository repository, ILogger<UserService> logger)
{
    private readonly IUserRepository _repository = repository;
    private readonly ILogger<UserService> _logger = logger;

    public async Task<User?> FindByIdAsync(int id) =>
        await _repository.GetByIdAsync(id);
}

// ✅ Primary constructors (C# 12)
public class UserController(IUserService userService) : ControllerBase
{
    [HttpGet("{id}")]
    public async Task<ActionResult<User>> Get(int id) =>
        await userService.FindByIdAsync(id) is { } user ? user : NotFound();
}
```

---

## Expresiones de colección (C# 12)
```csharp
// ✅ Collection expressions
int[] numbers = [1, 2, 3, 4, 5];
List<string> names = ["Alice", "Bob", "Charlie"];
ReadOnlySpan<int> span = [1, 2, 3];

// ✅ Spread operator
int[] combined = [..array1, ..array2, 99];

// ✅ Collection expression in method calls
ProcessItems([item1, item2, item3]);
```

---

## IDisposable y gestión de recursos
```csharp
// ✅ Implement IDisposable properly
public sealed class DatabaseConnection : IDisposable
{
    private readonly SqlConnection _connection;
    
    public void Dispose()
    {
        _connection.Dispose();
    }
}

// ✅ IAsyncDisposable for async resources
public sealed class StreamProcessor : IAsyncDisposable
{
    public async ValueTask DisposeAsync()
    {
        await _stream.DisposeAsync();
    }
}

// ✅ using declaration
using var file = File.OpenRead("data.txt");
using var connection = new SqlConnection(connectionString);
```

---

## Resumen
Los modismos modernos de C# enfatizan: registros para datos, coincidencia de patrones, seguridad nula (tipos de referencia que aceptan valores NULL), LINQ para colecciones, asíncrono/espera con CancellationToken, inyección de dependencia, constructores primarios, expresiones de colección y declaraciones `using`. Siga las convenciones de codificación de C#, utilice`dotnet format`para formatear y analizadores Roslyn para la calidad del código. El C# moderno (12+) es conciso y expresivo: incluye registros, coincidencia de patrones y constructores primarios.