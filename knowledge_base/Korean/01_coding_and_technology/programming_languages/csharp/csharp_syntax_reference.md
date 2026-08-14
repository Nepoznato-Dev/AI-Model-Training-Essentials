---
# Metadata
title: "C# — Syntax Reference"
description: "Detailed syntax reference for C# covering operators, control flow, classes, LINQ, async, generics, pattern matching, records, and modern C# features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [csharp, syntax-reference, operators, linq, async, generics, pattern-matching, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# C# — 구문 참조
이 문서는 최신 C#(.NET 7/8의 C# 10/11/12)에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, LINQ, 비동기/대기, 패턴 일치 및 최신 기능에 중점을 두어 기본 C# 참조를 보완합니다.
---

## 연산자 및 표현식
### 핵심 운영자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `+``-``*``/``%`| 산술 | `a + b`|  `+`는 또한 문자열을 연결합니다 |
| `++``--` | 증가/감소 | `++i`| 사전 증분 선호 |
| `==``!=` | 평등 | `a == b`| 재정의 가능; 기록은 가치 평등을 사용합니다 |
| `<``>``<=``>=` | 관계형 | `a >= b`| |
| `&&``\|\|``!`| 논리적 | `a && b`| 단락 |
| `&``\|``^``~` | 비트별 | `a & b`| |
| `<<``>>``>>>`| 교대 | `a << 2`| `>>>`부호 없는 오른쪽 시프트(C# 11) |
| `??`| Null 병합 | `a ?? b`| `a`가 null인 경우 `b`를 반환합니다. |
| `?.`| Null 조건부 | `a?.B`| `a`가 null인 경우 null을 반환합니다. |
| `!`| Null 허용 | `a!.B`| 널 입력 가능 경고를 억제합니다 |
| `is`| 유형 패턴 | `x is string s`| 패턴 매칭 |
| `as`| 안전한 캐스트 | `x as string`| 실패 시 null을 반환합니다. |
| `nameof`| 이름 리터럴 | `nameof(x)`| `"x"`— 컴파일 타임 |
| `typeof`| 유형 개체 | `typeof(int)`| `System.Int32`|
| `sizeof`| 크기(바이트) | `sizeof(int)`|  `4`(안전하지 않은 컨텍스트) |
### 연산자 우선 순위(가장 높은 것에서 가장 낮은 것까지)
| 우선순위 | 운영자 |
|------------|------------|
| 1(가장 높음) | 기본:`()``.``?.``[]` `()`(호출)`++``--`(접미사)`new``typeof``sizeof`|
| 2 | 단항:`+``-``!``~``++``--`(접두사)`(T)x``await` |
| 3 | 곱셈:`*``/``%`|
| 4 | 첨가제:`+``-` |
| 5 | 시프트:`<<``>>``>>>`|
| 6 | 관계형:`<``>``<=``>=``is``as` |
| 7 | 같음:`==``!=` |
| 8 | 비트 AND:`&`|
| 9 | 비트별 XOR:`^`|
| 10 | 비트 OR:`\|`|
| 11 | 조건부 AND:`&&`|
| 12 | 조건부 OR:`\|\|`|
| 13 | Null 병합:`??`|
| 14 | 조건부:`? :`|
| 15 | 과제:`=``+=``-=``??=` 등 |
---

## 제어 흐름
### 패턴 일치(C# 8–12)
```csharp
// Switch expression
string GetStatus(HttpStatusCode code) => code switch
{
    >= 200 and < 300 => "Success",
    >= 300 and < 400 => "Redirect",
    >= 400 and < 500 => "Client Error",
    >= 500 => "Server Error",
    _ => "Unknown"
};

// Type patterns
object Describe(object obj) => obj switch
{
    null => "null",
    int n => $"integer: {n}",
    string { Length: 0 } => "empty string",
    string s => $"string({s.Length}): \"{s}\"",
    IList<int> { Count: > 10 } list => $"large int list with {list.Count} items",
    (int x, int y) => $"tuple: ({x}, {y})",
    _ => $"other: {obj.GetType().Name}"
};

// if with patterns
if (obj is Person { Age: >= 18, Name: not null } adult)
{
    Console.WriteLine($"Adult: {adult.Name}");
}

// List patterns (C# 11)
int[] numbers = { 1, 2, 3, 4, 5 };
string desc = numbers switch
{
    [] => "empty",
    [var single] => $"single: {single}",
    [var first, .., var last] => $"first: {first}, last: {last}",
    [_, _, ..] => "at least two elements"
};
```

### 현대적인 루프 패턴
```csharp
// foreach with deconstruction
foreach (var (key, value) in dictionary) { }
foreach (var (index, item) in list.Select((item, i) => (i, item))) { }

// Range and indices (C# 8)
int[] arr = { 0, 1, 2, 3, 4, 5 };
var slice = arr[1..4];      // { 1, 2, 3 }
var last = arr[^1];          // 5 (last element)
var tail = arr[^3..];        // { 3, 4, 5 }
```

---

## 링크
### 쿼리 구문과 메서드 구문
```csharp
// Method syntax (most common)
var adults = people
    .Where(p => p.Age >= 18)
    .OrderByDescending(p => p.Age)
    .Select(p => p.Name)
    .ToList();

// Query syntax (SQL-like)
var adults2 = from p in people
              where p.Age >= 18
              orderby p.Age descending
              select p.Name;

// Group by
var byCity = people.GroupBy(p => p.City);
foreach (var group in byCity)
{
    Console.WriteLine($"{group.Key}: {group.Count()} people");
}

// Aggregate
int total = numbers.Aggregate(0, (acc, n) => acc + n);
string csv = names.Aggregate("", (acc, name) => acc == "" ? name : $\"{acc}, {name}\");

// Common operations
var distinct = items.Distinct().ToList();
var union = list1.Union(list2);
var intersection = list1.Intersect(list2);
var difference = list1.Except(list2);
var zipped = names.Zip(scores, (n, s) => $\"{n}: {s}\");
bool any = people.Any(p => p.Age > 60);
bool all = people.All(p => p.Age >= 0);
int count = people.Count(p => p.IsActive);
```

---

## 비동기/대기
```csharp
// Basic async method
public async Task<string> FetchAsync(string url)
{
    using var client = new HttpClient();
    var response = await client.GetAsync(url);
    response.EnsureSuccessStatusCode();
    return await response.Content.ReadAsStringAsync();
}

// Concurrent execution
var task1 = FetchAsync(url1);
var task2 = FetchAsync(url2);
var (result1, result2) = (await task1, await task2);

// Task.WhenAll — true parallel await
var results = await Task.WhenAll(
    urls.Select(url => FetchAsync(url))
);

// CancellationToken support
public async Task<string> FetchAsync(string url, CancellationToken ct)
{
    using var client = new HttpClient();
    var response = await client.GetAsync(url, ct);
    return await response.Content.ReadAsStringAsync(ct);
}

// IAsyncEnumerable — async streaming
public async IAsyncEnumerable<int> GenerateNumbers(
    [EnumeratorCancellation] CancellationToken ct = default)
{
    for (int i = 0; ; i++)
    {
        ct.ThrowIfCancellationRequested();
        await Task.Delay(100, ct);
        yield return i;
    }
}

// Consume async stream
await foreach (var number in GenerateNumbers(ct))
{
    Console.WriteLine(number);
}
```

---

## 클래스, 레코드 및 구조체
```csharp
// Record — value equality, immutable
public record Person(string FirstName, string LastName, int Age)
{
    public string FullName => $\"{FirstName} {LastName}\";
}

var p1 = new Person(\"Alice\", \"Smith\", 30);
var p2 = p1 with { LastName = \"Jones\" };  // Non-destructive mutation

// Record struct (C# 10) — value type with value equality
public record struct Point(double X, double Y);

// Primary constructor (C# 12)
public class UserController(IUserRepository repo, ILogger logger) : ControllerBase
{
    [HttpGet(\"{id}\")]
    public async Task<User> Get(string id) => await repo.GetByIdAsync(id);
}

// Sealed class — cannot be inherited
public sealed class Singleton { /* ... */ }

// Abstract class with abstract members
public abstract class Shape
{
    public abstract double Area { get; }
    public virtual string Describe() => $\"Shape with area {Area:F2}\";
}

// Interface with default implementation
public interface ILogger
{
    void Log(string message);
    void LogError(Exception ex) => Log($\"ERROR: {ex.Message}\");  // Default impl
}

// Partial methods and classes (source generators)
public partial class GeneratedService
{
    partial void ValidateInput(CreateDto dto);  // Implemented by source generator
}
```

---

## 제네릭 및 제약 조건
```csharp
// Generic class with constraints
public class Repository<T> where T : class, IEntity, new()
{
    private readonly Dictionary<string, T> _store = new();

    public T? Get(string id) => _store.GetValueOrDefault(id);
    public void Save(T entity) => _store[entity.Id] = entity;
}

// Generic method
public T Max<T>(T a, T b) where T : IComparable<T> =>
    a.CompareTo(b) >= 0 ? a : b;

// Covariance and contravariance
IEnumerable<out T>    // Covariant — can use derived type
IComparer<in T>       // Contravariant — can use base type

// Generic constraints reference
// where T : struct        — value type
// where T : class         — reference type
// where T : notnull       — non-nullable
// where T : unmanaged     — unmanaged type
// where T : new()         — parameterless constructor
// where T : BaseType      — must inherit
// where T : IInterface    — must implement
```

---

## 컬렉션 표현식(C# 12)
```csharp
// Collection expressions
int[] arr = [1, 2, 3, 4, 5];
List<string> names = [\"Alice\", \"Bob\", \"Charlie\"];
Span<int> span = [10, 20, 30];

// Spread operator
int[] combined = [..arr, 6, 7, ..new[] { 8, 9 }];

// With LINQ
var squares = [..Enumerable.Range(1, 10).Select(x => x * x)];
```

---

## 문자열 보간 및 서식 지정
```csharp
// Raw string literals (C# 11)
var json = \"\"\"
    {
        \"name\": \"Alice\",
        \"age\": 30
    }
    \"\"\";

// Interpolated raw strings
var name = \"Alice\";
var greeting = \"\"\"
    Hello, {name}!
    Welcome to the system.
    \"\"\";

// Format strings
Console.WriteLine($\"{price:C2}\");     // $1,234.56
Console.WriteLine($\"{ratio:P1}\");     // 45.6%
Console.WriteLine($\"{value,10:F2}\");  // Right-aligned, 2 decimals
```

---

## 요약
최신 C#은 객체 지향, 기능적, 구성 요소 지향 프로그래밍의 장점을 결합한 다중 패러다임 언어입니다. 구문은 Java와 유사한 장황한 코드에서 패턴 일치, 레코드, 컬렉션 표현식 및 기본 생성자가 포함된 간결한 표현식에 이르기까지 극적으로 발전했습니다. LINQ는 모든 컬렉션에 걸쳐 균일한 쿼리 API를 제공합니다. Async/await는 비동기 프로그래밍을 자연스럽게 만듭니다. 유형 시스템은 null 허용 참조 유형, 제약 조건이 있는 제네릭 및 패턴 일치를 통해 안전성과 실용주의의 균형을 유지합니다. C#은 이전 버전과의 호환성을 유지하면서 상용구를 줄이는 기능을 각 릴리스에 추가하면서 계속 빠르게 발전하고 있습니다.