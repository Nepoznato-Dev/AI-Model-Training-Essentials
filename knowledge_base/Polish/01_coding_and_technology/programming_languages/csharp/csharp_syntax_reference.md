<!--
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

-->
# C# — Odniesienie do składni
Ten dokument zawiera kompleksowe, uporządkowane informacje o składni nowoczesnego języka C# (C# 10/11/12 na platformie .NET 7/8). Uzupełnia główne odniesienia do języka C#, koncentrując się na wyczerpujących wzorcach składni, LINQ, async/await, dopasowywaniu wzorców i nowoczesnych funkcjach.
---

## Operatory i wyrażenia
### Główni operatorzy
| Operator | Imię | Przykład | Notatki |
|---------|------|---------|-------|
| `+``-``*``/``%`| Arytmetyka | `a + b`| `+`łączy także ciągi znaków |
| `++``--` | Zwiększanie/zmniejszanie | `++i`| Preferuj wstępną inkrementację |
| `==``!=` | Równość | `a == b`| Nadpisane; rekordy używają równości wartości |
| `<``>``<=``>=` | Relacyjny | `a >= b`| |
| `&&``\|\|``!`| Logiczne | `a && b`| Zwarcie |
| `&``\|``^``~` | Bitowe | `a & b`| |
| `<<``>>``>>>`| Przesunięcie | `a << 2`| `>>>`przesunięcie w prawo bez znaku (C# 11) |
| `??`| Połączenie zerowe | `a ?? b`| Zwraca `b`, jeśli`a`ma wartość null |
| `?.`| Warunek zerowy | `a?.B`| Zwraca wartość null, jeśli`a`ma wartość null |
| `!`| Wybaczanie zera | `a!.B`| Pomija ostrzeżenie dopuszczające wartość null |
| `is`| Wpisz wzór | `x is string s`| Dopasowanie wzoru |
| `as`| Bezpieczny odlew | `x as string`| Zwraca wartość null w przypadku niepowodzenia |
| `nameof`| Nazwa dosłowna | `nameof(x)`| `"x"`— czas kompilacji |
| `typeof`| Wpisz obiekt | `typeof(int)`| `System.Int32`|
| `sizeof`| Rozmiar w bajtach | `sizeof(int)`| `4`(niebezpieczny kontekst) |
### Pierwszeństwo operatora (od najwyższego do najniższego)
| Pierwszeństwo | Operatorzy |
|------------|-----------|
| 1 (najwyższy) | Podstawowy:`()``.``?.``[]``()`(wywołanie)`++``--` (postfiks)`new``typeof``sizeof`|
| 2 | Jednoargumentowy:`+``-``!``~``++``--` (przedrostek)`(T)x``await` |
| 3 | Multiplikatyw:`*``/``%`|
| 4 | Dodatek:`+``-` |
| 5 | Przesunięcie:`<<``>>``>>>`|
| 6 | Relacyjne:`<``>``<=``>=``is``as` |
| 7 | Równość:`==``!=` |
| 8 | Bitowe AND:`&`|
| 9 | Bitowy XOR:`^`|
| 10 | Bitowe LUB:`\|`|
| 11 | Warunkowe ORAZ:`&&`|
| 12 | Warunkowe LUB:`\|\|`|
| 13 | Koalescencja zerowa:`??`|
| 14 | Warunkowo:`? :`|
| 15 | Przypisanie:`=``+=``-=``??=` itp. |
---

## Kontroluj przepływ
### Dopasowywanie wzorców (C# 8–12)
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

### Nowoczesne wzory pętli
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

## LINQ
### Składnia zapytania a składnia metody
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

## Asynchronizacja/Oczekiwanie
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

## Klasy, rekordy i struktury
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

## Ogólne i ograniczenia
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

## Wyrażenia kolekcji (C# 12)
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

## Interpolacja i formatowanie ciągów
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

## Streszczenie
Nowoczesny C# to język wieloparadygmatowy, który łączy w sobie to, co najlepsze w programowaniu obiektowym, funkcjonalnym i zorientowanym na komponenty. Jego składnia uległa dramatycznej ewolucji — od szczegółowego kodu przypominającego język Java po zwięzłe wyrażenia z dopasowywaniem wzorców, rekordami, wyrażeniami kolekcji i podstawowymi konstruktorami. LINQ zapewnia jednolity interfejs API zapytań we wszystkich kolekcjach. Async/await sprawia, że ​​programowanie asynchroniczne jest naturalne. System typów równoważy bezpieczeństwo z pragmatyzmem poprzez typy referencyjne dopuszczające wartość null, typy generyczne z ograniczeniami i dopasowywanie wzorców. C# nadal szybko się rozwija, a każda wersja dodaje funkcje, które redukują schematy, zachowując jednocześnie kompatybilność wsteczną.