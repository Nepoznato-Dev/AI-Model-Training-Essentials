---
# Metadata
title: "C# — Cheat Sheet"
description: "Quick-reference cheat sheet for C# syntax, LINQ, and .NET patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [csharp, dotnet, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C# — Bảng tính gian lận
## Cơ bản
```csharp
// Variables
int x = 42;
double pi = 3.14159;
string name = "Alice";
bool active = true;
var inferred = "hello";  // type inferred
const int MAX = 100;

// Nullable types
int? nullableInt = null;
string? nullableString = null;
int value = nullableInt ?? 0;  // null coalescing

// String interpolation
$"Hello, {name}! Age: {age}"
$"{pi:F2}"                     // "3.14"
$"{value,10}"                  // right-align, width 10

// String methods
name.Length
name.ToUpper()
name.Contains("lic")
name.Substring(0, 3)
name.Trim()
string.Join(", ", items)
"hello".Split(' ')
```

## Bộ sưu tập
```csharp
// List<T>
var list = new List<string> { "Alice", "Bob" };
list.Add("Charlie");
list[0];
list.Count;
list.Remove("Bob");
list.Where(x => x.Length > 3).ToList();

// Dictionary<K,V>
var dict = new Dictionary<string, int>
{
    ["alice"] = 90,
    ["bob"] = 85
};
dict["charlie"] = 78;
dict.TryGetValue("alice", out int score);
dict.GetValueOrDefault("unknown", 0);

// Array
int[] arr = { 1, 2, 3 };
int[] sized = new int[10];
Array.Sort(arr);
Array.BinarySearch(arr, 2);

// HashSet<T>
var set = new HashSet<int> { 1, 2, 3 };
set.Add(4);
set.Contains(2);

// Immutable collections
using System.Collections.Immutable;
var imm = ImmutableList.Create(1, 2, 3);

// Span<T> (high-performance)
Span<int> span = stackalloc int[] { 1, 2, 3 };
ReadOnlySpan<char> chars = "hello".AsSpan();
```

## Luồng điều khiển
```csharp
if (condition) { ... }
else if (other) { ... }
else { ... }

// Ternary
string result = condition ? "yes" : "no";

// Switch expression (C# 8+)
string label = day switch
{
    DayOfWeek.Monday or DayOfWeek.Tuesday => "early week",
    DayOfWeek.Wednesday                   => "midweek",
    _                                     => "later"
};

// Pattern matching
if (obj is string s && s.Length > 5) { ... }
if (obj is int n and > 0) { ... }  // C# 9+

// Loops
foreach (var item in collection) { ... }
for (int i = 0; i < 10; i++) { ... }
while (condition) { ... }
```

## Lớp học & Hồ sơ
```csharp
// Record (C# 9+)
public record Point(double X, double Y);
var p = new Point(1.0, 2.0);
var p2 = p with { Y = 3.0 };  // with-expression

// Record struct (C# 10+)
public readonly record struct Color(byte R, byte G, byte B);

// Class
public class User
{
    public string Name { get; init; }  // init-only setter
    public int Age { get; set; }
    public required string Email { get; set; }  // C# 11

    public User(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

// Sealed
public sealed class FinalClass { }

// Partial methods & classes
public partial class Service { }
```

##LINQ
```csharp
using System.Linq;

// Query syntax
var adults = from u in users
             where u.Age >= 18
             orderby u.Name
             select u.Name;

// Method syntax
var names = users
    .Where(u => u.Age >= 18)
    .OrderBy(u => u.Name)
    .Select(u => u.Name)
    .ToList();

// Aggregation
int total = items.Sum(i => i.Price);
double avg = items.Average(i => i.Rating);
var groups = items.GroupBy(i => i.Category);
var dict = items.ToDictionary(i => i.Id);
bool any = items.Any(i => i.Active);
var first = items.First(i => i.Active);

// Group join
var result = from dept in departments
             join emp in employees on dept.Id equals emp.DeptId into group
             select new { Department = dept.Name, Employees = group };
```

## Không đồng bộ/Đang chờ
```csharp
// Async method
public async Task<User> GetUserAsync(int id)
{
    using var client = new HttpClient();
    var response = await client.GetAsync($"/api/users/{id}");
    response.EnsureSuccessStatusCode();
    return await response.Content.ReadFromJsonAsync<User>();
}

// Parallel async
var tasks = new[] { FetchUsers(), FetchPosts() };
var (users, posts) = await Task.WhenAll(tasks);  // C# with deconstruct

// ValueTask for hot paths
public async ValueTask<int> FastOpAsync() { ... }

// Cancellation
public async Task ProcessAsync(CancellationToken ct = default)
{
    while (!ct.IsCancellationRequested)
    {
        await Task.Delay(100, ct);
    }
}
```

## Xử lý lỗi
```csharp
try
{
    var result = RiskyOperation();
}
catch (InvalidOperationException ex)
{
    Log.Error(ex, "Operation failed");
}
catch (Exception ex) when (ex.Message.Contains("timeout"))
{
    // Exception filter
}
finally
{
    Cleanup();
}

// Throw expressions
int Value => x ?? throw new ArgumentNullException(nameof(x));
```

## Tính năng C# hiện đại
```csharp
// Pattern matching (C# 9+)
string Classify(object obj) => obj switch
{
    int n when n > 0  => "positive int",
    string { Length: 0 } => "empty string",
    null => "null",
    _ => "other"
};

// Raw string literals (C# 11+)
var json = """
    {
        "name": "Alice",
        "age": 30
    }
    """;

// Collection expressions (C# 12)
int[] arr = [1, 2, 3];
List<string> list = ["a", "b", "c"];

// Primary constructors (C# 12)
public class User(string name, int age)
{
    public string Name => name;
}
```
