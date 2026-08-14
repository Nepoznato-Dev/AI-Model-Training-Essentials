---
# Metadata
title: "TypeScript — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in TypeScript that catch even experienced developers, with explanations and corrections."
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
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [typescript, common-mistakes, anti-patterns, pitfalls, best-practices, type-system, coding-and-technology]
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
# TypeScript – Häufige Fehler und Anti-Patterns
Dieses Dokument katalogisiert die häufigsten Fehler, Fallen und Anti-Patterns in TypeScript. Jeder Eintrag zeigt den falschen Ansatz, erklärt, warum er fehlschlägt, und bietet die richtige Lösung.
---

## 1. Überbeanspruchung von `any`
```typescript
// ❌ WRONG — defeats the purpose of TypeScript
function processData(data: any): any {
    return data.value;
}

// ❌ WRONG — implicit any from JSON
const config = JSON.parse(jsonString);  // type: any

// ✅ CORRECT — use proper types
function processData(data: { value: number }): number {
    return data.value;
}

// ✅ CORRECT — type assertion after validation
const config = JSON.parse(jsonString) as Config;

// ✅ CORRECT — use unknown when type is truly unknown
function safeProcess(data: unknown): string {
    if (typeof data === "object" && data !== null && "value" in data) {
        return String((data as { value: unknown }).value);
    }
    throw new Error("Invalid data");
}
```

---

## 2. Typzusicherungen anstelle von Typwächtern
```typescript
// ❌ WRONG — lying to the compiler
const element = document.getElementById("app") as HTMLDivElement;
element.innerHTML = "Hello";  // runtime error if element is not a div

// ✅ CORRECT — use type guards
const element = document.getElementById("app");
if (element instanceof HTMLDivElement) {
    element.innerHTML = "Hello";  // type-safe
}

// ✅ CORRECT — custom type guard
function isUser(obj: unknown): obj is User {
    return typeof obj === "object" && obj !== null
        && "name" in obj && "email" in obj;
}
```

---

## 3. Missbrauch von Nicht-Null-Behauptungen
```typescript
// ❌ WRONG — suppresses null checks
function getUser(id: number): User {
    return userMap.get(id)!;  // throws if id not found
}

// ✅ CORRECT — handle the undefined case
function getUser(id: number): User | undefined {
    return userMap.get(id);
}

// ✅ CORRECT — provide a default
function getUser(id: number): User {
    return userMap.get(id) ?? defaultUser;
}
```

---

## 4. Verwirrung zwischen Schnittstellen und Typen
```typescript
// ❌ WRONG — using type for object shapes that should use interface
type User = {
    name: string;
    email: string;
};

// ✅ CORRECT — interfaces for object shapes (extendable, better errors)
interface User {
    name: string;
    email: string;
}

// ✅ CORRECT — use type for unions, intersections, and computed types
type Status = "active" | "inactive" | "pending";
type UserOrAdmin = User | Admin;
type Readonly<T> = { readonly [K in keyof T]: T[K] };
```

---

## 5. Enum Anti-Patterns
```typescript
// ❌ WRONG — numeric enums are fragile
enum Direction {
    Up,    // 0
    Down,  // 1
    Left,  // 2
    Right  // 3
}
// Adding a value in the middle breaks everything

// ✅ CORRECT — use string enums for clarity
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT"
}

// ✅ BEST — use const assertions (TypeScript 5.0+)
const DIRECTIONS = {
    Up: "UP",
    Down: "DOWN",
    Left: "LEFT",
    Right: "RIGHT"
} as const;
type Direction = typeof DIRECTIONS[keyof typeof DIRECTIONS];
```

---

## 6. Der `strict`-Modus wird nicht verwendet
```json
// ❌ WRONG — loose compiler options
{
    "compilerOptions": {
        "strict": false
    }
}

// ✅ CORRECT — enable strict mode
{
    "compilerOptions": {
        "strict": true,
        "noImplicitAny": true,
        "strictNullChecks": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true
    }
}
```

---

## 7. Überraschungen bei der strukturellen Typisierung
```typescript
// ❌ WRONG — assuming nominal typing (like Java/C#)
class Dog {
    name: string;
    bark(): void { console.log("Woof!"); }
}
class Cat {
    name: string;
    bark(): void { console.log("..."); }  // same shape!
}

const dog: Dog = new Cat();  // compiles! (structural typing)

// ✅ CORRECT — use branding for nominal-like behavior
type Brand<T, B extends string> = T & { __brand: B };
type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;

const userId = "123" as UserId;
const orderId = "123" as OrderId;
// userId and orderId are not interchangeable
```

---

## 8. Async/Await-Typfehler
```typescript
// ❌ WRONG — not awaiting a Promise
async function getUsers(): Promise<User[]> {
    const users = fetch("/api/users");  // Promise<User[]>, not User[]!
    return users.map(u => u.name);  // Error: Property 'map' does not exist
}

// ✅ CORRECT — await the Promise
async function getUsers(): Promise<string[]> {
    const response = await fetch("/api/users");
    const users: User[] = await response.json();
    return users.map(u => u.name);
}
```

---

## 9. Anti-Pattern: Wiederholte Typen (keine Verwendung von Generics)
```typescript
// ❌ WRONG — duplicated code for each type
function getFirstString(arr: string[]): string | undefined {
    return arr[0];
}
function getFirstNumber(arr: number[]): number | undefined {
    return arr[0];
}

// ✅ CORRECT — use generics
function getFirst<T>(arr: T[]): T | undefined {
    return arr[0];
}
```

---

## 10. Übermäßige optionale Verkettung
```typescript
// ❌ WRONG — masking data model issues
const city = response?.data?.user?.address?.city;
// If this chain breaks, you don't know where

// ✅ CORRECT — validate at boundaries, use types
interface UserResponse {
    data: {
        user: {
            address: {
                city: string;
            };
        };
    };
}

function parseUserResponse(response: unknown): UserResponse {
    // validate once at the boundary
    if (!isValidUserResponse(response)) {
        throw new Error("Invalid user response");
    }
    return response;
}

// Now safe to access without chaining
const { city } = parseUserResponse(raw).data.user.address;
```

---

## 11. Verwendung von`namespace`(Legacy)
```typescript
// ❌ WRONG — namespace is legacy
namespace Utils {
    export function format() { ... }
}

// ✅ CORRECT — use ES modules
// utils.ts
export function format() { ... }

// main.ts
import { format } from "./utils";
```

---

## 12. Diskriminierte Gewerkschaften nicht ausnutzen
```typescript
// ❌ WRONG — using optional properties for different shapes
interface Shape {
    type: string;
    radius?: number;
    width?: number;
    height?: number;
}
function area(s: Shape): number {
    if (s.type === "circle") return Math.PI * s.radius! ** 2;
    if (s.type === "rectangle") return s.width! * s.height!;
    return 0;
}

// ✅ CORRECT — discriminated unions
type Shape =
    | { type: "circle"; radius: number }
    | { type: "rectangle"; width: number; height: number };

function area(s: Shape): number {
    switch (s.type) {
        case "circle": return Math.PI * s.radius ** 2;
        case "rectangle": return s.width * s.height;
    }
}
```

---

## Zusammenfassung
Das Typsystem von TypeScript ist leistungsstark, erfordert jedoch Disziplin. Die Todsünde besteht darin, nach`any`zu greifen – verwenden Sie `unknown`, wenn der Typ wirklich unbekannt ist, und grenzen Sie ihn mit Typschutz ein. Vermeiden Sie Nicht-Null-Behauptungen (`!`), indem Sie undefiniert richtig behandeln. Verwenden Sie Schnittstellen für Objektformen, Typen für Vereinigungen und berechnete Typen. Diskriminierte Gewerkschaften beseitigen ganze Klassen von Fehlern. Aktivieren Sie`strict: true`vom ersten Tag an – das Nachrüsten der Strenge ist mühsam. Ziel ist es, illegale Zustände auf Typebene nicht darstellbar zu machen.