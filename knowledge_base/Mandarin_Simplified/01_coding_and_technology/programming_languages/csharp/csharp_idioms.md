---
# Metadata
title: "C# — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern C# code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C# — 惯用模式和最佳实践
本指南涵盖了编写简洁的现代 C# (12+) 代码的惯用模式和最佳实践。
---

## 现代 C# 语法
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

## 空安全
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

## LINQ
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

## 异步/等待
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

## 依赖注入
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

## 集合表达式 (C# 12)
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

## IDisposable 和资源管理
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

＃＃ 概括
现代 C# 习惯用法强调：数据记录、模式匹配、空安全（可为空引用类型）、集合 LINQ、使用 CancellationToken 进行异步/等待、依赖项注入、主构造函数、集合表达式和`using`声明。遵循 C# 编码约定，使用`dotnet format`进行格式化，并使用 Roslyn 分析器确保代码质量。现代 C# (12+) 简洁且富有表现力 — 包含记录、模式匹配和主构造函数。