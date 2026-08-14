---
# Metadata
title: "TypeScript"
description: "Comprehensive reference for the TypeScript programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [typescript, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "34 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Maszynopis
TypeScript to statycznie typowany nadzbiór języka JavaScript opracowany przez firmę Microsoft (pod przewodnictwem Andersa Hejlsberga) i wydany po raz pierwszy w 2012 r. Dodaje do JavaScript opcjonalne adnotacje typów, interfejsy, typy generyczne i zaawansowane funkcje systemu typów, a następnie kompiluje się do zwykłego kodu JavaScript, który działa w dowolnym miejscu, w którym działa JavaScript. TypeScript nie jest oddzielnym językiem ani środowiskiem wykonawczym; jest to JavaScript ze sprawdzaniem typów.
TypeScript stał się standardem dla programowania JavaScript na dużą skalę. React, Angular, VS Code, Deno i większość głównych projektów JavaScript typu open source są napisane w TypeScript. Jeśli rozpoczynasz nowy projekt JavaScript o znacznych rozmiarach, zalecanym domyślnym rozwiązaniem jest TypeScript.
---

## Dlaczego TypeScript ma znaczenie
- **Wychwytuje błędy w czasie kompilacji**: Błędy typu są wykrywane przed uruchomieniem kodu — nie w środowisku produkcyjnym.
- **Lepsza obsługa IDE**: Autouzupełnianie, przejście do definicji, refaktoryzacja i dokumentacja wbudowana znacznie się poprawiają.
- **Kod samodokumentujący**: Typy służą jako dokumentacja, która jest zawsze aktualna.
- **W 100% kompatybilny z JavaScript**: Każdy prawidłowy JavaScript jest prawidłowym TypeScriptem. Można to adoptować stopniowo.
- **Zaawansowany system typów**: typy Unii, typy skrzyżowań, typy warunkowe, typy mapowane, typy literałów szablonowych — system typów jest wystarczająco wyrazisty, aby modelować złożoną logikę domeny.
- **Przyjęcie w branży**: Angular tego wymaga; Ekosystem React w przeważającej mierze z niego korzysta; większość nowych pakietów npm jest dostarczana z definicjami typów.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Etap kompilacji** | Należy skompilować`.ts`→`.js`przed uruchomieniem | Użyj`ts-node`/`tsx`do programowania; `tsc`do produkcji |
| **Krzywa uczenia się** | System typów może być złożony (typy ogólne, typy warunkowe) | Zacznij od typów podstawowych; stopniowo wprowadzaj zaawansowane funkcje |
| **Pliki definicji typów** | Nie wszystkie pakiety npm są dostarczane z typami | Zainstaluj`@types/package-name`z SureTyped |
| **Czasy kompilacji** | Duże projekty mogą powoli sprawdzać typ | Użyj referencji projektu,`isolatedModules`lub`swc`|
| **Fałszywe poczucie bezpieczeństwa** | Typy nie gwarantują poprawności środowiska wykonawczego | Połącz z walidacją środowiska wykonawczego (Zod, io-ts) |
---

## Podstawy składni
### Adnotacje typów podstawowych
```typescript
// Primitives
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;

// Arrays
let scores: number[] = [9.5, 8.0, 7.5];
let names: Array<string> = ["Alice", "Bob"];  // Alternative syntax

// Functions
function add(a: number, b: number): number {
    return a + b;
}

const greet = (name: string): string => `Hello, ${name}!`;

// Return type void (no return value)
function log(message: string): void {
    console.log(message);
}
```

### Interfejsy i typy
```typescript
// Interface — defines the shape of an object
interface User {
    id: number;
    name: string;
    email: string;
    role: "admin" | "editor" | "viewer";  // Union type (string literal)
    createdAt: Date;
}

// Optional and readonly properties
interface Config {
    readonly apiUrl: string;
    timeout: number;
    retries?: number;  // Optional property
}

// Type alias — can represent any type (including unions, intersections)
type Status = "pending" | "active" | "inactive";
type ID = string | number;

// Extending interfaces
interface Admin extends User {
    permissions: string[];
    lastLogin: Date;
}

// Using them
const user: User = {
    id: 1,
    name: "Alice",
    email: "alice@example.com",
    role: "admin",
    createdAt: new Date(),
};
```

### Ogólne
```typescript
// Generic function — works with any type while preserving type safety
function first<T>(arr: T[]): T | undefined {
    return arr[0];
}

const num = first([1, 2, 3]);       // Type: number | undefined
const str = first(["a", "b", "c"]); // Type: string | undefined

// Generic interface
interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}

// Generic constraint
function getLength<T extends { length: number }>(item: T): number {
    return item.length;
}

getLength("hello");     // OK — string has .length
getLength([1, 2, 3]);   // OK — array has .length
// getLength(42);        // Error — number doesn't have .length

// Generic class
class Stack<T> {
    private items: T[] = [];
    
    push(item: T): void { this.items.push(item); }
    pop(): T | undefined { return this.items.pop(); }
    peek(): T | undefined { return this.items[this.items.length - 1]; }
    get size(): number { return this.items.length; }
}

const numbers = new Stack<number>();
numbers.push(1);
numbers.push(2);
const top = numbers.pop();  // Type: number | undefined
```

### Typy zaawansowane
```typescript
// Union types
type Result = Success | Error;
interface Success { ok: true; data: string; }
interface Error { ok: false; error: string; }

function handle(result: Result) {
    if (result.ok) {
        console.log(result.data);   // TypeScript narrows to Success
    } else {
        console.log(result.error);  // TypeScript narrows to Error
    }
}

// Discriminated unions (pattern matching)
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "rectangle"; width: number; height: number }
    | { kind: "triangle"; base: number; height: number };

function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2;
        case "rectangle":
            return shape.width * shape.height;
        case "triangle":
            return 0.5 * shape.base * shape.height;
    }
}

// Utility types (built-in)
interface Todo {
    title: string;
    description: string;
    completed: boolean;
}

type ReadonlyTodo = Readonly<Todo>;          // All properties readonly
type PartialTodo = Partial<Todo>;             // All properties optional
type TodoPreview = Pick<Todo, "title" | "completed">;  // Only selected properties
type TodoWithoutTitle = Omit<Todo, "title">;  // All except selected

// Template literal types
type EventName = `on${Capitalize<"click" | "hover" | "focus">}`;
// Result: "onClick" | "onHover" | "onFocus"

// Conditional types
type IsString<T> = T extends string ? true : false;
type A = IsString<"hello">;  // true
type B = IsString<42>;       // false
```

### Asynchronizacja z typami
```typescript
// Typed async functions
async function fetchUser(id: number): Promise<User> {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error("User not found");
    return response.json();
}

// Typed error handling
async function safeFetch(url: string): Promise<[User, null] | [null, Error]> {
    try {
        const user = await fetchUser(1);
        return [user, null];
    } catch (error) {
        return [null, error instanceof Error ? error : new Error("Unknown")];
    }
}
```

---

## Zaawansowana składnia i wzorce
### Zaawansowane typy ogólne
```typescript
// Multiple type parameters
function zip<A, B>(as: A[], bs: B[]): [A, B][] {
    const length = Math.min(as.length, bs.length);
    return Array.from({ length }, (_, i) => [as[i], bs[i]]);
}

const zipped = zip([1, 2, 3], ["a", "b", "c"]);
// Type: [number, string][]

// Generic constraints with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

const user = { name: "Alice", age: 30 };
const nameVal = getProperty(user, "name");  // Type: string
// getProperty(user, "email");  // Error: "email" is not a key of user

// Mapped types — transform existing types
type Nullable<T> = { [K in keyof T]: T[K] | null };
type Readonly2<T> = { readonly [K in keyof T]: T[K] };

// Custom utility: make specific keys required
type WithRequired<T, K extends keyof T> = T & { [P in K]-?: T[P] };
interface Form { name?: string; email?: string; age?: number; }
type RequiredName = WithRequired<Form, "name">;
// { name: string; email?: string; age?: number; }

// Infer keyword — extract types from patterns
type ReturnType2<T> = T extends (...args: any[]) => infer R ? R : never;
type UnpackPromise<T> = T extends Promise<infer U> ? U : T;

type A = ReturnType2<() => string>;  // string
type B = UnpackPromise<Promise<number>>;  // number
```

### Dekoratory (standard TypeScript 5.0 lub nowszy)
```typescript
// Method decorator — logging
function log(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${key} with`, args);
        const result = original.apply(this, args);
        console.log(`${key} returned`, result);
        return result;
    };
    return descriptor;
}

class Calculator {
    @log
    add(a: number, b: number): number {
        return a + b;
    }
}

// Property decorator — validation
function MinLength(min: number) {
    return function (target: any, key: string) {
        let value: string = target[key];
        const getter = () => value;
        const setter = (newVal: string) => {
            if (newVal.length < min) {
                throw new Error(`${key} must be at least ${min} characters`);
            }
            value = newVal;
        };
        Object.defineProperty(target, key, { get: getter, set: setter });
    };
}

class UserDto {
    @MinLength(3)
    username!: string;
}

// Class decorator — auto-register
const registry: Function[] = [];
function register(target: Function) {
    registry.push(target);
}

@register
class UserService {
    findAll() { return []; }
}
```

### Osłony typu i zwężanie
```typescript
// Custom type guard with "is"
function isString(value: unknown): value is string {
    return typeof value === "string";
}

function isUser(obj: unknown): obj is User {
    return (
        typeof obj === "object" &&
        obj !== null &&
        "id" in obj &&
        "name" in obj &&
        "email" in obj
    );
}

// Exhaustive checking with never
function assertNever(x: never): never {
    throw new Error(`Unexpected value: ${x}`);
}

type PaymentStatus = "pending" | "completed" | "failed" | "refunded";

function describeStatus(status: PaymentStatus): string {
    switch (status) {
        case "pending": return "Awaiting payment";
        case "completed": return "Payment received";
        case "failed": return "Payment failed";
        case "refunded": return "Payment refunded";
        default: return assertNever(status);  // Compile error if a case is missing
    }
}

// Satisfies operator (TS 4.9+) — validate without widening
const palette = {
    red: [255, 0, 0],
    green: [0, 128, 0],
    blue: [0, 0, 255],
} satisfies Record<string, [number, number, number]>;

palette.red[0] = 200;   // OK — knows it's a number array
// palette.yellow;       // Error — "yellow" not in palette
```

---

## Współbieżność i równoległość
TypeScript dziedziczy model współbieżności JavaScript, ale dodaje bezpieczeństwo typów do wzorców asynchronicznych.
### Wpisane wzorce asynchroniczne
```typescript
// Typed event emitter
interface EventMap {
    "user.login": { userId: number; timestamp: Date };
    "user.logout": { userId: number };
    "error": { message: string; code: number };
}

class TypedEmitter {
    private handlers: Map<string, Function[]> = new Map();

    on<K extends keyof EventMap>(event: K, handler: (data: EventMap[K]) => void) {
        const list = this.handlers.get(event as string) || [];
        list.push(handler);
        this.handlers.set(event as string, list);
    }

    emit<K extends keyof EventMap>(event: K, data: EventMap[K]) {
        const list = this.handlers.get(event as string) || [];
        list.forEach(h => h(data));
    }
}

const emitter = new TypedEmitter();
emitter.on("user.login", (data) => {
    console.log(data.userId, data.timestamp);  // Fully typed!
});

// Typed async queue
class AsyncQueue<T> {
    private queue: T[] = [];
    private resolve: ((value: T) => void) | null = null;

    push(item: T) {
        if (this.resolve) {
            this.resolve(item);
            this.resolve = null;
        } else {
            this.queue.push(item);
        }
    }

    async pop(): Promise<T> {
        if (this.queue.length > 0) {
            return this.queue.shift()!;
        }
        return new Promise<T>(resolve => { this.resolve = resolve; });
    }
}
```

---

## Konfiguracja projektu i budowanie systemu
### Struktura katalogu projektu
```
my-ts-project/
├── src/
│   ├── index.ts
│   ├── types/
│   │   ├── user.ts
│   │   └── api.ts
│   ├── services/
│   │   └── userService.ts
│   └── utils/
│       └── validators.ts
├── tests/
│   └── services/
│       └── userService.test.ts
├── tsconfig.json
├── tsconfig.build.json
├── package.json
├── vitest.config.ts
├── .eslintrc.js
└── .github/workflows/ci.yml
```

###`tsconfig.json`— konfiguracja TypeScriptu
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

### Zarządzanie kompilacją i pakietami
```bash
# Initialize project
npm init -y
npm install typescript --save-dev
npx tsc --init

# Development (with hot reload)
npx tsx watch src/index.ts

# Build for production
npx tsc -p tsconfig.build.json

# Alternative: use esbuild for faster builds
npx esbuild src/index.ts --bundle --platform=node --outdir=dist
```

### Testowanie za pomocą Vitest
```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
    test: {
        globals: true,
        coverage: {
            provider: "v8",
            reporter: ["text", "json", "html"],
        },
    },
});

// tests/services/userService.test.ts
import { describe, it, expect, vi } from "vitest";
import { UserService } from "../../src/services/userService";

describe("UserService", () => {
    it("creates a user with valid data", () => {
        const service = new UserService();
        const user = service.create({ name: "Alice", email: "alice@example.com" });
        expect(user.id).toBeDefined();
        expect(user.name).toBe("Alice");
    });

    it("throws on invalid email", () => {
        const service = new UserService();
        expect(() => service.create({ name: "Bob", email: "invalid" }))
            .toThrowError("Invalid email format");
    });

    it("calls repository with correct data", async () => {
        const mockRepo = { save: vi.fn().mockResolvedValue({ id: 1 }) };
        const service = new UserService(mockRepo);
        await service.create({ name: "Alice", email: "a@b.com" });
        expect(mockRepo.save).toHaveBeenCalledWith({
            name: "Alice",
            email: "a@b.com",
        });
    });
});
```

### Potok CI/CD — akcje w GitHubie
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"
      - run: npm ci
      - run: npm run lint
      - run: npx tsc --noEmit
      - run: npm test -- --coverage
      - run: npm run build
```

---

## Zaawansowana składnia i wzorce
### Zaawansowane typy ogólne
```typescript
// Multiple type parameters
function zip<A, B>(as: A[], bs: B[]): [A, B][] {
    const length = Math.min(as.length, bs.length);
    return Array.from({ length }, (_, i) => [as[i], bs[i]]);
}

// Generic constraints with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

// Infer keyword — extract types from patterns
type ReturnType2<T> = T extends (...args: any[]) => infer R ? R : never;
type UnpackPromise<T> = T extends Promise<infer U> ? U : T;

// Mapped types
type Nullable<T> = { [K in keyof T]: T[K] | null };
type WithRequired<T, K extends keyof T> = T & { [P in K]-?: T[P] };
```

### Dekoratory (TypeScript 5.0+)
```typescript
function log(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${key} with`, args);
        return original.apply(this, args);
    };
}

class Calculator {
    @log
    add(a: number, b: number): number { return a + b; }
}
```

### Osłony typu i zwężanie
```typescript
function isUser(obj: unknown): obj is User {
    return typeof obj === "object" && obj !== null && "id" in obj && "name" in obj;
}

// Exhaustive checking with never
function assertNever(x: never): never { throw new Error(`Unexpected: ${x}`); }

type Status = "pending" | "active" | "done";
function handle(s: Status): string {
    switch (s) {
        case "pending": return "waiting";
        case "active": return "running";
        case "done": return "finished";
        default: return assertNever(s);
    }
}

// Satisfies operator (TS 4.9+)
const palette = { red: [255, 0, 0], green: [0, 128, 0] } satisfies Record<string, number[]>;
```

---

## Konfiguracja projektu i zbudowanie systemu
### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Testowanie za pomocą Vitest
```typescript
import { describe, it, expect, vi } from "vitest";
import { UserService } from "../src/services/userService";

describe("UserService", () => {
    it("creates a user with valid data", () => {
        const service = new UserService();
        const user = service.create({ name: "Alice", email: "alice@example.com" });
        expect(user.name).toBe("Alice");
    });

    it("calls repository with correct data", async () => {
        const mockRepo = { save: vi.fn().mockResolvedValue({ id: 1 }) };
        const service = new UserService(mockRepo);
        await service.create({ name: "Alice", email: "a@b.com" });
        expect(mockRepo.save).toHaveBeenCalled();
    });
});
```

### Walidacja środowiska wykonawczego za pomocą Zoda
```typescript
import { z } from "zod";

const UserSchema = z.object({
    id: z.number().positive(),
    name: z.string().min(1).max(100),
    email: z.string().email(),
    role: z.enum(["admin", "editor", "viewer"]),
});

type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse(unknownData);
if (result.success) {
    console.log(result.data.name);
} else {
    console.error(result.error.issues);
}
```

---

## Interoperacyjność
### Korzystanie z bibliotek JavaScript
```typescript
// Installing type definitions
// npm install @types/express @types/lodash

// Declare a module for untyped packages
declare module "untyped-library" {
    export function doSomething(input: string): void;
}

// Branded types for type safety at boundaries
type UserId = string & { readonly __brand: "UserId" };
function toUserId(id: string): UserId { return id as UserId; }
```

---

## Wzorce projektowe
### Wzorzec wyników
```typescript
type Result<T, E = Error> =
    | { ok: true; value: T }
    | { ok: false; error: E };

function ok<T>(value: T): Result<T, never> { return { ok: true, value }; }
function err<E>(error: E): Result<never, E> { return { ok: false, error }; }

function divide(a: number, b: number): Result<number, string> {
    if (b === 0) return err("Division by zero");
    return ok(a / b);
}
```

### Wzorzec repozytorium
```typescript
interface Repository<T extends { id: number }> {
    findById(id: number): Promise<T | null>;
    findAll(): Promise<T[]>;
    save(entity: Omit<T, "id">): Promise<T>;
}

class UserRepository implements Repository<User> {
    async findById(id: number): Promise<User | null> { return null; }
    async findAll(): Promise<User[]> { return []; }
    async save(data: Omit<User, "id">): Promise<User> { return { ...data, id: 1 }; }
}
```

---

## Zastosowanie
### Plik Dockera
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json tsconfig.json ./
RUN npm ci
COPY src/ src/
RUN npx tsc -p tsconfig.build.json

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --production
CMD ["node", "dist/index.js"]
```

---

## Ekosystem
### Kluczowe narzędzia
| Narzędzie | Cel |
|------|-------------|
| **tsc** | Kompilator TypeScript (oficjalny) |
| **węzeł ts / tsx** | Uruchom TypeScript bezpośrednio, bez osobnej kompilacji |
| **swc** | Ultraszybki kompilator TypeScript/JavaScript oparty na Rust |
| **ESLint + maszynopis-eslint** | Linting z regułami uwzględniającymi typy |
| **Zoda** | Sprawdzanie poprawności typu w środowisku wykonawczym z wnioskowaniem TypeScript |
| **tsconfig.json** | Plik konfiguracyjny TypeScriptu |
### Frameworki (wszystkie oparte na TypeScript)
| Ramy | Domena |
|----------|--------|
| **Kątowy** | W pełni funkcjonalny framework frontendowy (wymaga TypeScriptu) |
| **Następny.js** | Meta-framework reakcji (najpierw TypeScript) |
| **NestJS** | Struktura zaplecza korporacyjnego (najpierw TypeScript) |
| **tRPC** | Kompleksowe interfejsy API bezpiecznego typu (tylko TypeScript) |
| **Prisma** | Bezpieczny typ ORM dla Node.js |
---

## Kiedy używać TypeScriptu
| Scenariusz | Dlaczego TypeScript | Lepsza alternatywa |
|---------|---------------|--------------------------------|
| Duże projekty JavaScript | Bezpieczeństwo typu zapobiega całym kategoriom błędów | -- |
| Projekty zespołowe | Typy służą jako wspólny kontrakt | -- |
| Rozwój API | Kompleksowe bezpieczeństwo z tRPC lub OpenAPI | Przejdź na Java, aby uzyskać prostsze interfejsy API REST |
| Dowolny nowy projekt JavaScript | Koszt późniejszego dodania TypeScriptu jest wysoki | Zwykły JS tylko dla małych skryptów |
| Biblioteki / pakiety npm | Konsumenci otrzymują autouzupełnianie i sprawdzanie typu | -- |
**Ogólna zasada**: Jeśli Twój projekt JavaScript ma więcej niż kilkaset linii, użyj TypeScript.
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między`type`i`interface`i kiedy należy używać każdego z nich?
**O:** Obydwa definiują kształty obiektów, ale mają różne możliwości. `interface`obsługuje łączenie deklaracji (scalanie wielu deklaracji o tej samej nazwie),`extends`w przypadku dziedziczenia i jest idiomatycznym wyborem dla publicznych interfejsów API. `type`obsługuje typy unii, typy skrzyżowań, typy mapowane, typy warunkowe i typy literałów szablonowych — wszystko, co jest zaawansowane. Najlepsza praktyka: używaj`interface`dla kształtów obiektów i publicznych interfejsów API; użyj`type`dla związków, narzędzi i operacji typu złożonego.
```typescript
// interface — declaration merging, extends
interface User {
  id: string;
  name: string;
}
interface User {
  email: string;  // Merges with the above
}
interface Admin extends User {
  permissions: string[];
}

// type — unions, mapped types, conditional types
type Status = "active" | "inactive" | "pending";
type Readonly<T> = { readonly [K in keyof T]: T[K] };
type NonNullable<T> = T extends null | undefined ? never : T;

// When they overlap — prefer interface for objects
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}
```

### P2: Jak działają leki generyczne i dlaczego są ważne?
**O:** Typy generyczne umożliwiają pisanie funkcji, klas i typów, które działają z dowolnym typem, przy jednoczesnym zachowaniu bezpieczeństwa typów. Zamiast`any`(który traci informacje o typie), typy generyczne zachowują relację między typami wejściowymi i wyjściowymi. Stanowią podstawę kodu wielokrotnego użytku, bezpiecznego typu.
```typescript
// Generic function — preserves type relationship
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
const num = first([1, 2, 3]);       // Type: number | undefined
const str = first(["a", "b"]);       // Type: string | undefined

// Generic constraints
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user = { name: "Alice", age: 30 };
const name = getProperty(user, "name");   // Type: string
// getProperty(user, "email");            // Error: "email" is not keyof typeof user

// Generic utility — the real power of TypeScript's type system
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};
```

### P3: Jakie są typy narzędzi i które warto znać?
**O:** TypeScript udostępnia wbudowane typy narzędzi, które przekształcają istniejące typy. Najważniejsze:`Partial<T>`(wszystkie opcjonalne),`Required<T>`(wszystkie wymagane),`Pick<T, K>`(wybierz klucze),`Omit<T, K>`(wyklucz klucze),`Record<K, V>`(mapa klucz-wartość),`Exclude<T, U>`(usuń z unii),`ReturnType<T>`(wyodrębnij typ powrotu funkcji),`Awaited<T>`(rozwiń obietnicę). Naucz się ich — eliminują one większość potrzeb wykonywania operacji na typach niestandardowych.
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  password: string;
  createdAt: Date;
}

// Common transformations
type CreateUser = Omit<User, "id" | "createdAt">;     // For POST requests
type UpdateUser = Partial<Omit<User, "id">>;            // For PATCH requests
type UserSummary = Pick<User, "id" | "name">;           // For list views
type UserMap = Record<string, User>;                    // Dictionary

// Extracting types
type UserReturn = ReturnType<typeof getUser>;           // What getUser returns
type UserKeys = keyof User;                              // "id" | "name" | "email" | ...

// Custom utility
type Nullable<T> = { [K in keyof T]: T[K] | null };
type NullableUser = Nullable<User>;  // All fields can be null
```

### P4: Jak wpisać kod asynchroniczny i obsłużyć błędy w sposób bezpieczny dla typu?
**A:** Funkcje asynchroniczne automatycznie zwracają wartość `Promise<T>`, gdzie T jest typem zwracanej wartości. Użyj `await`, aby rozpakować obietnicę. Do obsługi błędów TypeScript nie ma wyjątków wpisywanych, ale można tworzyć osłony typów i typy wyników. „Wzorzec wyników” (inspirowany Rustem) zapewnia obsługę błędów w czasie kompilacji.
```typescript
// Async typing
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json() as Promise<User>;
}

// Result pattern — type-safe error handling
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function safeFetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await fetchUser(id);
    return { ok: true, value: user };
  } catch (error) {
    return { ok: false, error: error as Error };
  }
}

// Usage — compiler forces you to check 'ok'
const result = await safeFetchUser("123");
if (result.ok) {
  console.log(result.value.name);  // TypeScript knows value exists
} else {
  console.error(result.error.message);
}
```

### P5: Co to są pliki deklaracji (.d.ts) i jak używać typów innych firm?
**O:** Pliki deklaracji opisują typy bibliotek JavaScript, które nie mają wbudowanych typów TypeScript. Zawierają tylko informacje o typie (bez kodu wykonawczego). Zainstaluj typy obsługiwane przez społeczność z SureTyped:`npm install --save-dev @types/lodash`. W przypadku własnych bibliotek dodaj pole`types`w`package.json`lub dołącz pliki`.d.ts`do źródła. Użyj`declare module`dla deklaracji otoczenia.
```typescript
// Installing third-party types
// npm install --save-dev @types/express @types/node

// Custom declaration file (global.d.ts)
declare module "*.svg" {
  const content: string;
  export default content;
}

declare module "legacy-library" {
  export function processData(input: string): number;
  export class LegacyClient {
    constructor(config: { host: string; port: number });
    connect(): Promise<void>;
  }
}

// Augmenting existing modules
declare module "express" {
  interface Request {
    user?: import("./models").User;
  }
}
```

---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zbuduj emiter zdarzeń bezpieczny dla typu
**Opis problemu:** Utwórz ogólny, bezpieczny dla typów emiter zdarzeń w TypeScript, w którym każda nazwa zdarzenia jest odwzorowywana na określony typ ładunku. Kompilator powinien wychwycić nieprawidłowe nazwy zdarzeń i typy ładunku w czasie kompilacji.
**Krok 1 — Zrozum problem:**
Potrzebujemy systemu zdarzeń, w którym: (1) zdarzenia są zdefiniowane wraz z ich typami ładunku, (2)`emit`akceptuje tylko prawidłowe nazwy zdarzeń z poprawnymi ładunkami, (3)`on`akceptuje tylko prawidłowe nazwy zdarzeń z poprawnie wpisanymi procedurami obsługi. Wymaga to mapowanych typów i typów ogólnych za pośrednictwem interfejsu mapy zdarzeń.
**Krok 2 — Zidentyfikuj podejście:**
- Zdefiniuj typ `EventMap`:`{ [eventName: string]: payloadType }`.
- Użyj `keyof EventMap`, aby ograniczyć nazwy zdarzeń.
- Użyj `EventMap[K]`, aby uzyskać typ ładunku dla określonego zdarzenia.
- Przechowuj słuchaczy w`Map<string, Function[]>`.
**Krok 3 — Wdróż rozwiązanie:**
```typescript
type EventMap = Record<string, unknown>;

class TypedEmitter<Events extends EventMap> {
  private listeners = new Map<string, Set<Function>>();

  on<K extends keyof Events>(
    event: K,
    listener: (payload: Events[K]) => void
  ): () => void {
    if (!this.listeners.has(event as string)) {
      this.listeners.set(event as string, new Set());
    }
    this.listeners.get(event as string)!.add(listener);

    // Return unsubscribe function
    return () => this.off(event, listener);
  }

  off<K extends keyof Events>(
    event: K,
    listener: (payload: Events[K]) => void
  ): void {
    this.listeners.get(event as string)?.delete(listener);
  }

  emit<K extends keyof Events>(event: K, payload: Events[K]): void {
    this.listeners.get(event as string)?.forEach(fn => fn(payload));
  }

  once<K extends keyof Events>(
    event: K,
    listener: (payload: Events[K]) => void
  ): void {
    const unsubscribe = this.on(event, (payload: Events[K]) => {
      listener(payload);
      unsubscribe();
    });
  }
}

// Usage — fully type-safe
interface AppEvents {
  "user:login": { userId: string; timestamp: Date };
  "user:logout": { userId: string };
  "data:update": { key: string; value: unknown };
  "error": { message: string; code: number };
}

const emitter = new TypedEmitter<AppEvents>();

emitter.on("user:login", ({ userId, timestamp }) => {
  console.log(`${userId} logged in at ${timestamp}`);
});

emitter.emit("user:login", { userId: "abc", timestamp: new Date() });
// emitter.emit("user:login", { userId: "abc" });  // Error: missing timestamp
// emitter.emit("unknown", {});                     // Error: "unknown" not in AppEvents
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Bezpieczeństwo typu: kompilator wychwytuje błędne nazwy zdarzeń i nieprawidłowe kształty ładunku w czasie kompilacji.
-`on`zwraca funkcję anulowania subskrypcji w celu wygodnego czyszczenia.
-`once`otacza słuchacza, aby automatycznie anulował subskrypcję po pierwszym wywołaniu.
- W przypadku produkcji: dodaj`listenerCount`,`removeAllListeners`i rozważ użycie`AbortSignal`do anulowania.
### Problem 2: Zaimplementuj konstruktor zapytań SQL bezpieczny dla typu
**Opis problemu:** Zbuduj narzędzie do tworzenia zapytań SQL, w którym nazwy i typy kolumn pochodzą z interfejsu TypeScript. Konstruktor powinien zapobiegać nieprawidłowym nazwom kolumn i niezgodnościom typów w czasie kompilacji.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) nazw kolumn ograniczonych do`keyof T`, (2) wartości klauzuli WHERE wpisanych zgodnie z kolumną, (3) API z możliwością tworzenia łańcuchów do budowania zapytań. Wymaga to typów ogólnych ograniczonych przez`Record<string, unknown>`.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`keyof T`dla ograniczeń nazw kolumn.
- Użyj`T[K]`dla ograniczeń typu wartości.
- Zbuduj ciąg SQL ze sparametryzowanymi zapytaniami (zapobiegaj wstrzykiwaniu SQL).
- Metody łańcuchowe zwracają`this`.
**Krok 3 — Wdróż rozwiązanie:**
```typescript
interface QueryBuilder<T extends Record<string, unknown>> {
  select(...columns: (keyof T)[]): QueryBuilder<T>;
  where<K extends keyof T>(column: K, value: T[K]): QueryBuilder<T>;
  orderBy(column: keyof T, direction?: "ASC" | "DESC"): QueryBuilder<T>;
  limit(n: number): QueryBuilder<T>;
  build(): { sql: string; params: unknown[] };
}

function createQuery<T extends Record<string, unknown>>(
  table: string
): QueryBuilder<T> {
  let columns: string[] = ["*"];
  let conditions: string[] = [];
  let params: unknown[] = [];
  let orderClause = "";
  let limitClause = "";

  return {
    select(...cols: (keyof T)[]) {
      columns = cols.map(String);
      return this;
    },
    where<K extends keyof T>(column: K, value: T[K]) {
      conditions.push(`${String(column)} = $${params.length + 1}`);
      params.push(value);
      return this;
    },
    orderBy(column: keyof T, direction: "ASC" | "DESC" = "ASC") {
      orderClause = ` ORDER BY ${String(column)} ${direction}`;
      return this;
    },
    limit(n: number) {
      limitClause = ` LIMIT ${n}`;
      return this;
    },
    build() {
      const sql = `SELECT ${columns.join(", ")} FROM ${table}`
        + (conditions.length ? ` WHERE ${conditions.join(" AND ")}` : "")
        + orderClause + limitClause;
      return { sql, params };
    },
  };
}

// Usage — fully type-safe
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

const { sql, params } = createQuery<User>("users")
  .select("name", "email")
  .where("age", 25)           // Type: number
  .where("name", "Alice")     // Type: string
  .orderBy("name")
  .limit(10)
  .build();

console.log(sql);
// SELECT name, email FROM users WHERE age = $1 AND name = $2 ORDER BY name ASC LIMIT 10
console.log(params);  // [25, "Alice"]

// .where("age", "not a number");  // Error: string not assignable to number
// .select("nonexistent");          // Error: "nonexistent" not in keyof User
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Zapobieganie wstrzykiwaniu SQL: wszystkie wartości przechodzą przez sparametryzowane zapytania (`$1`,`$2`), nigdy nie są interpolowane.
- Bezpieczeństwo typu: nazwy kolumn i typy wartości są sprawdzane w czasie kompilacji.
- Rozszerzalność: dodaj metody`join`,`groupBy`,`having`,`insert`,`update`według tego samego wzorca.
- Produkcja: użyj`kysely`lub`drizzle-orm`— zapewniają tego typu bezpieczeństwo przy pełnym pokryciu SQL.
### Problem 3: Zaimplementuj maszynę o skończonych stanach z bezpieczeństwem typu
**Opis problemu:** Utwórz bezpieczną maszynę o skończonych stanach, w której wymuszane są prawidłowe przejścia w czasie kompilacji. Każdy stan może mieć akcje wejścia/wyjścia, a maszyna powinna śledzić bieżący stan.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) stanów i zdarzeń zdefiniowanych jako typy, (2) prawidłowych przejść mapowanych na poziomie typu, (3) kompilator zapobiega nieprawidłowym przejść, (4) śledzenia stanu w czasie wykonywania za pomocą wywołań zwrotnych. Wymaga to typów mapowanych i typów warunkowych.
**Krok 2 — Zidentyfikuj podejście:**
- Zdefiniuj `TransitionMap`:`{ [State]: { [Event]: NextState } }`.
- Użyj typów ogólnych, aby ograniczyć`send(event)`w oparciu o bieżący stan.
- Stan śledzenia w czasie wykonywania ze zmienną.
- Obsługa wywołań zwrotnych wejścia/wyjścia dla każdego stanu.
**Krok 3 — Wdróż rozwiązanie:**
```typescript
type TransitionMap = Record<string, Record<string, string>>;

interface StateMachineConfig<T extends TransitionMap> {
  initial: keyof T & string;
  transitions: T;
  onEnter?: Partial<Record<keyof T & string, () => void>>;
  onExit?: Partial<Record<keyof T & string, () => void>>;
}

// Extract valid events for a given state
type EventsFor<S extends string, T extends TransitionMap> =
  S extends keyof T ? keyof T[S] & string : never;

// Extract target state for a given state + event
type TargetState<S extends string, E extends string, T extends TransitionMap> =
  S extends keyof T ? (E extends keyof T[S] ? T[S][E] : never) : never;

class StateMachine<T extends TransitionMap> {
  private current: string;
  private config: StateMachineConfig<T>;

  constructor(config: StateMachineConfig<T>) {
    this.config = config;
    this.current = config.initial;
    config.onEnter?.[config.initial]?.();
  }

  getState(): keyof T & string {
    return this.current as keyof T & string;
  }

  can(event: EventsFor<keyof T & string, T>): boolean {
    const transitions = this.config.transitions[this.current];
    return transitions != null && event in transitions;
  }

  send(event: EventsFor<keyof T & string, T>): void {
    const transitions = this.config.transitions[this.current];
    if (!transitions || !(event in transitions)) {
      throw new Error(
        `Invalid transition: cannot send '${event}' from state '${this.current}'`
      );
    }

    const nextState = transitions[event];
    this.config.onExit?.[this.current]?.();
    this.current = nextState;
    this.config.onEnter?.[nextState]?.();
  }
}

// Usage — type-safe state machine
const trafficLight = new StateMachine({
  initial: "red",
  transitions: {
    red:    { next: "green" },
    green:  { next: "yellow" },
    yellow: { next: "red" },
  } as const,
  onEnter: {
    red: () => console.log("🔴 Stop"),
    green: () => console.log("🟢 Go"),
    yellow: () => console.log("🟡 Caution"),
  },
});

trafficLight.getState();  // "red"
trafficLight.send("next"); // → green, prints "🟢 Go"
trafficLight.send("next"); // → yellow, prints "🟡 Caution"
trafficLight.send("next"); // → red, prints "🔴 Stop"
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Bezpieczeństwo w czasie wykonywania:`send`zgłasza nieprawidłowe przejścia.
- Bezpieczeństwo typu: typ`EventsFor`wyodrębnia prawidłowe zdarzenia dla każdego stanu w czasie kompilacji.
- Wywołania zwrotne wejścia/wyjścia uruchamiają się automatycznie przy przejściach.
- Do celów produkcyjnych: użyj`xstate`— zapewnia pełną bibliotekę maszyn stanowych z wizualnym debugowaniem, stanami hierarchicznymi, osłonami i akcjami.
---

## Streszczenie
TypeScript to JavaScript stworzony do wszystkiego, co wykracza poza trywialne skrypty. Dodaje potężny system typów, który wcześnie wychwytuje błędy, ulepsza narzędzia i dokumentuje kod - a wszystko to podczas kompilacji do standardowego kodu JavaScript, który działa w dowolnym miejscu. Krzywa uczenia się jest łagodna (można zacząć od typów minimalnych), ale głębokość jest ogromna (system typów jest kompletny według Turinga). W przypadku nowoczesnego programowania JavaScript TypeScript stał się standardem branżowym.