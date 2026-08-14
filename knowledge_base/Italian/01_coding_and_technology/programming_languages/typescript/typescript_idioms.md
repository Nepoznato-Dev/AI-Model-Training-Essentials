<!--
---
# Metadata
title: "TypeScript — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, type-safe TypeScript code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [typescript, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# TypeScript: modelli idiomatici e migliori pratiche
Questa guida illustra i modelli idiomatici e le migliori pratiche per scrivere codice TypeScript pulito e sicuro per i tipi.
---

## Digita Sistema
```typescript
// ✅ Prefer interfaces for object shapes
interface User {
  readonly id: number;
  name: string;
  email: string;
  role: UserRole;
}

// ✅ Use type for unions, intersections, utilities
type UserRole = "admin" | "user" | "guest";
type UserWithPosts = User & { posts: Post[] };
type UserPreview = Pick<User, "id" | "name">;
type UserInput = Omit<User, "id">;

// ✅ const assertions for literal types
const ROLES = ["admin", "user", "guest"] as const;
type Role = typeof ROLES[number]; // "admin" | "user" | "guest"

// ✅ Discriminated unions
type Result<T> =
  | { status: "ok"; data: T }
  | { status: "error"; error: string };

function handle<T>(result: Result<T>): T {
  if (result.status === "ok") return result.data;
  throw new Error(result.error);
}
```

---

## Configurazione rigorosa
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "moduleResolution": "bundler",
    "target": "ES2022",
    "module": "ES2022"
  }
}
```

---

## Tipo Protezioni e restringimento
```typescript
// ✅ User-defined type guards
function isUser(obj: unknown): obj is User {
  return typeof obj === "object" && obj !== null &&
    "name" in obj && "email" in obj;
}

// ✅ Discriminated union narrowing
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "rectangle":
      return shape.width * shape.height;
  }
}

// ✅ Exhaustive checking
function assertNever(x: never): never {
  throw new Error(`Unexpected value: ${x}`);
}

// ✅ in operator for narrowing
if ("radius" in shape) {
  // shape is Circle
}

// ✅ satisfies operator (TS 4.9+)
const config = {
  host: "localhost",
  port: 8080,
} satisfies ServerConfig;
```

---

##Generici
```typescript
// ✅ Constrained generics
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// ✅ Generic with defaults
interface Repository<T, ID = number> {
  findById(id: ID): Promise<T | null>;
  findAll(): Promise<T[]>;
  save(entity: T): Promise<T>;
}

// ✅ Generic constraints with extends
function merge<T extends object, U extends object>(a: T, b: U): T & U {
  return { ...a, ...b };
}

// ✅ Conditional types
type IsString<T> = T extends string ? true : false;
type NonNullable<T> = T extends null | undefined ? never : T;
```

---

## Modelli moderni
```typescript
// ✅ Destructuring with types
const { name, email, age }: User = userData;
const [first, ...rest]: number[] = numbers;

// ✅ Optional chaining + nullish coalescing
const city = user?.address?.city ?? "Unknown";
const count = items?.length ?? 0;

// ✅ Template literal types
type EventName = `on${Capitalize<string>}`;
type HTTPMethod = "GET" | "POST" | "PUT" | "DELETE";
type Endpoint = `/${string}`;

// ✅ as const for config objects
const ROUTES = {
  HOME: "/",
  USERS: "/users",
  USER_DETAIL: "/users/:id",
} as const;

// ✅ Branded types for type safety
type UserId = number & { readonly __brand: "UserId" };
type OrderId = number & { readonly __brand: "OrderId" };

function toUserId(id: number): UserId { return id as UserId; }
```

---

## Modelli asincroni
```typescript
// ✅ async/await with proper types
async function fetchUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json() as Promise<User>;
}

// ✅ Promise.all with typed results
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
]);
// users: User[], posts: Post[]

// ✅ AsyncGenerator
async function* streamData(): AsyncGenerator<Item> {
  for (const chunk of chunks) {
    yield chunk;
  }
}
```

---

## Modelli di moduli
```typescript
// ✅ Named exports
export interface User { name: string; email: string; }
export function createUser(data: UserInput): User { }
export const MAX_USERS = 100;

// ✅ Barrel exports (index.ts)
export * from "./User.js";
export * from "./UserService.js";

// ✅ Type-only imports/exports
import type { User } from "./types.js";
export type { User } from "./types.js";
```

---

## Gestione degli errori
```typescript
// ✅ Custom error classes
class ValidationError extends Error {
  constructor(
    readonly field: string,
    message: string,
  ) {
    super(message);
    this.name = "ValidationError";
  }
}

// ✅ Result type pattern
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function parse(input: string): Result<number, ValidationError> {
  const n = Number(input);
  if (Number.isNaN(n)) {
    return { ok: false, error: new ValidationError("input", "not a number") };
  }
  return { ok: true, value: n };
}
```

---

## Riepilogo
Gli idiomi TypeScript enfatizzano: controllo rigoroso del tipo, interfacce per forme di oggetti, unioni discriminate per lo stato, protezioni dei tipi per il restringimento, generici con vincoli,`readonly`per l'immutabilità e`as const`per i tipi letterali. Segui ESLint con`typescript-eslint`, Più carino per la formattazione e abilita sempre`strict: true`. La comunità TypeScript valorizza la sicurezza del tipo: se viene compilato, probabilmente funziona. Preferisci`interface`per le forme degli oggetti,`type`per unioni e utenze ed evita`any`a tutti i costi.