<!--
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

-->
# TypeScript: errori comuni e anti-pattern
Questo documento cataloga gli errori, le trappole e gli anti-pattern più comuni in TypeScript. Ogni voce mostra l'approccio errato, spiega perché fallisce e fornisce la soluzione corretta.
---

## 1. Utilizzo eccessivo di `any`
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

## 2. Digita Asserzioni invece di Type Guards
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

## 3. Abuso di asserzioni non nulle
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

## 4. Confusione tra interfacce e tipi
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

## 5. Enum Anti-Pattern
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

## 6. Non utilizzare la modalità `strict`
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

## 7. Sorprese di tipizzazione strutturale
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

## 8. Errori di tipo Asincrono/Attesa
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

## 9. Anti-Pattern: tipi ripetuti (senza utilizzo di generici)
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

## 10. Concatenamento facoltativo eccessivo
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

## 11. Utilizzo di`namespace`(legacy)
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

## 12. Non sfruttare i sindacati discriminati
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

## Riepilogo
Il sistema di tipi di TypeScript è potente ma richiede disciplina. Il peccato capitale è raggiungere `any`: usa`unknown`quando il tipo è veramente sconosciuto e riduci le protezioni del tipo. Evita asserzioni non nulle (`!`) gestendo correttamente undefinite. Utilizza interfacce per forme di oggetti, tipi per unioni e tipi calcolati. I sindacati discriminati eliminano intere classi di bug. Abilita`strict: true`fin dal primo giorno: aggiornare il rigore è doloroso. L’obiettivo è rendere irrappresentabili gli stati illegali a livello di tipologia.