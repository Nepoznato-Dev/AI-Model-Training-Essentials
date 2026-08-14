---
# Metadata
title: "C# — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in C# that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [csharp, common-mistakes, anti-patterns, pitfalls, best-practices, dotnet, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# C# — Erreurs courantes et anti-modèles
Ce document répertorie les erreurs, pièges et anti-modèles les plus courants en C#. Chaque entrée montre l'approche incorrecte, explique pourquoi elle échoue et fournit la solution correcte.
---

## 1. Ne pas supprimer les objets `IDisposable`
```csharp
// ❌ WRONG — resource leak
var stream = new FileStream("data.txt", FileMode.Open);
var reader = new StreamReader(stream);
string data = reader.ReadToEnd();
reader.Close();  // skipped if ReadToEnd throws

// ✅ CORRECT — using statement (C# 8+ using declaration)
using var stream = new FileStream("data.txt", FileMode.Open);
using var reader = new StreamReader(stream);
string data = reader.ReadToEnd();
// automatically disposed
```

---

## 2.`==`vs`Equals()`pour les chaînes
```csharp
// ❌ WRONG — reference comparison for boxed strings
object a = "hello";
object b = new string("hello".ToCharArray());
a == b       // false (reference comparison)
a.Equals(b)  // true (value comparison)

// ✅ CORRECT — use == for strings (it's overloaded correctly)
string x = "hello";
string y = "hello";
x == y  // true

// ✅ CORRECT — explicit comparison
string.Equals(x, y, StringComparison.OrdinalIgnoreCase)
```

---

## 3. Méthodes Async Void
```csharp
// ❌ WRONG — exceptions can't be caught, fire-and-forget
public async void DoWork() {
    await Task.Delay(1000);
    throw new Exception("oops");  // crashes process!
}

// ✅ CORRECT — always return Task
public async Task DoWork() {
    await Task.Delay(1000);
    // exceptions propagate to caller
}

// Exception: async void is OK for event handlers
private async void OnButtonClick(object sender, EventArgs e) { ... }
```

---

## 4. Allocation inutile LINQ `.ToList()`
```csharp
// ❌ WRONG — materializing when not needed
var result = items
    .Where(x => x.IsActive)
    .ToList()
    .Select(x => x.Name)
    .ToList();  // two unnecessary allocations

// ✅ CORRECT — defer materialization
var result = items
    .Where(x => x.IsActive)
    .Select(x => x.Name)
    .ToList();  // single allocation at the end
```

---

## 5. Capture de la variable de boucle (pré-C# 5.0)
```csharp
// ❌ WRONG — pre-C# 5.0, all delegates share the same variable
var actions = new List<Action>();
for (int i = 0; i < 5; i++) {
    actions.Add(() => Console.WriteLine(i));
}
foreach (var action in actions) action();
// C# 4: prints 5,5,5,5,5
// C# 5+: prints 0,1,2,3,4 (fixed)

// ✅ CORRECT — explicit capture (works in all versions)
for (int i = 0; i < 5; i++) {
    int captured = i;
    actions.Add(() => Console.WriteLine(captured));
}
```

---

## 6. Ne pas utiliser la correspondance de modèles
```csharp
// ❌ WRONG — verbose type checking
object value = GetValue();
if (value is string) {
    string s = (string)value;
    Console.WriteLine(s.Length);
}

// ✅ CORRECT — pattern matching (C# 7+)
if (GetValue() is string s) {
    Console.WriteLine(s.Length);
}

// ✅ CORRECT — switch expression (C# 8+)
string description = shape switch {
    Circle c => $"Circle with radius {c.Radius}",
    Rectangle r => $"Rectangle {r.Width}x{r.Height}",
    _ => "Unknown shape"
};
```

---

## 7. Anti-modèle : classes divines / localisateur de services
```csharp
// ❌ WRONG — service locator anti-pattern
public class UserService {
    public void CreateUser() {
        var db = ServiceLocator.Resolve<IDatabase>();
        var email = ServiceLocator.Resolve<IEmailService>();
        // dependencies hidden, hard to test
    }
}

// ✅ CORRECT — constructor injection
public class UserService {
    private readonly IDatabase _db;
    private readonly IEmailService _email;

    public UserService(IDatabase db, IEmailService email) {
        _db = db;
        _email = email;
    }
}
```

---

## 8. Exceptions de référence nulle
```csharp
// ❌ WRONG — not checking for null
public string GetUserName(User user) {
    return user.Address.City;  // NullReferenceException chain
}

// ✅ CORRECT — null-conditional operator
public string GetUserName(User user) {
    return user?.Address?.City ?? "Unknown";
}

// ✅ CORRECT — nullable reference types (C# 8+)
#nullable enable
public string? FindEmail(string name) { ... }
// Compiler warns on unchecked null access
```

---

## 9. Concaténation de chaînes dans les boucles
```csharp
// ❌ WRONG — creates new string each iteration
string result = "";
foreach (var word in words) {
    result += word + " ";  // O(n²)
}

// ✅ CORRECT — StringBuilder
var sb = new StringBuilder();
foreach (var word in words) {
    sb.Append(word).Append(' ');
}
string result = sb.ToString();

// ✅ CORRECT — string.Join
string result = string.Join(" ", words);
```

---

## 10. Ne pas utiliser d'enregistrements pour les types de données
```csharp
// ❌ WRONG — class for immutable data (lots of boilerplate)
public class Point {
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
    // need to manually implement Equals, GetHashCode, ToString...
}

// ✅ CORRECT — record type (C# 9+)
public record Point(int X, int Y);
// auto-generates Equals, GetHashCode, ToString, deconstruct
```

---

## 11. Abus du filtre d'exception
```csharp
// ❌ WRONG — catching Exception and checking type
try {
    DoWork();
} catch (Exception ex) {
    if (ex is IOException) { /* handle */ }
    else if (ex is SqlException) { /* handle */ }
    else throw;
}

// ✅ CORRECT — catch specific exceptions
try {
    DoWork();
} catch (IOException ex) {
    // handle IO
} catch (SqlException ex) {
    // handle SQL
}
```

---

## Résumé
C# est un langage bien conçu mais il présente des pièges : ne pas supprimer les objets `IDisposable`, les méthodes vides asynchrones, les allocations LINQ inutiles et les exceptions de référence nulle. Le C# moderne (8+) fournit des outils puissants : types de référence nullables, correspondance de modèles, enregistrements, utilisation de déclarations et expressions de commutation. Les principes clés : toujours disposer des ressources, ne jamais utiliser de vide asynchrone (sauf les gestionnaires d'événements), utiliser l'injection de constructeur, privilégier les enregistrements pour les données et activer les types de référence nullables pour détecter les bogues nuls au moment de la compilation.