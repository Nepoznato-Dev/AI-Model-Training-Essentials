<!--
---
# Metadata
title: "TypeScript"
description: "Comprehensive reference for the TypeScript programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# TypeScript
TypeScript ist eine statisch typisierte Obermenge von JavaScript, die von Microsoft (unter der Leitung von Anders Hejlsberg) entwickelt und erstmals 2012 veröffentlicht wurde. Es fügt JavaScript optionale Typanmerkungen, Schnittstellen, Generika und erweiterte Typsystemfunktionen hinzu und wird dann zu einfachem JavaScript kompiliert, das überall dort ausgeführt werden kann, wo JavaScript ausgeführt wird. TypeScript ist keine separate Sprache oder Laufzeit; es ist JavaScript mit einem Typprüfer.
TypeScript ist zum Standard für die groß angelegte JavaScript-Entwicklung geworden. React, Angular, VS Code, Deno und die meisten großen Open-Source-JavaScript-Projekte sind in TypeScript geschrieben. Wenn Sie ein neues JavaScript-Projekt von beträchtlicher Größe starten, ist TypeScript die empfohlene Standardeinstellung.
---

## Warum TypeScript wichtig ist
- **Fängt Fehler zur Kompilierzeit ab**: Typfehler werden gefunden, bevor der Code ausgeführt wird – nicht in der Produktion.
- **Bessere IDE-Unterstützung**: Autovervollständigung, Go-to-Definition, Refactoring und Inline-Dokumentation verbessern sich erheblich.
- **Selbstdokumentierender Code**: Typen dienen als Dokumentation, die aktuell bleibt.
- **100 % JavaScript-kompatibel**: Jedes gültige JavaScript ist gültiges TypeScript. Sie können es schrittweise übernehmen.
- **Erweitertes Typsystem**: Union-Typen, Schnittmengentypen, bedingte Typen, zugeordnete Typen, Vorlagenliteraltypen – das Typsystem ist ausdrucksstark genug, um komplexe Domänenlogik zu modellieren.
- **Branchenakzeptanz**: Angular erfordert es; Das React-Ökosystem nutzt es überwiegend; Die meisten neuen NPM-Pakete werden mit Typdefinitionen ausgeliefert.
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Kompilierungsschritt** | Vor dem Ausführen | muss`.ts`→`.js`kompiliert werden Verwenden Sie`ts-node`/`tsx`für die Entwicklung. `tsc`für die Produktion |
| **Lernkurve** | Das Typsystem kann komplex sein (Generika, bedingte Typen) | Beginnen Sie mit den Grundtypen; Erweiterte Funktionen schrittweise übernehmen |
| **Typdefinitionsdateien** | Nicht alle NPM-Pakete werden mit den Typen | ausgeliefert Installieren Sie`@types/package-name`von DefinitelyTyped |
| **Kompilierungszeiten** | Bei großen Projekten kann die Typprüfung langsam sein | Verwenden Sie Projektverweise,`isolatedModules`oder`swc`|
| **Falsches Sicherheitsgefühl** | Typen garantieren keine Laufzeitkorrektheit | Kombinieren mit Laufzeitvalidierung (Zod, io-ts) |
---

## Syntax-Grundlagen
### Grundlegende Typanmerkungen
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

### Schnittstellen und Typen
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

### Generika
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

### Erweiterte Typen
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

### Asynchron mit Typen
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

## Erweiterte Syntax und Muster
### Erweiterte Generika
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

### Dekorateure (TypeScript 5.0+ Standard)
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

### Geben Sie Guards und Narrowing ein
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

## Parallelität und Parallelität
TypeScript erbt das Parallelitätsmodell von JavaScript, fügt aber Typsicherheit zu asynchronen Mustern hinzu.
### Typisierte asynchrone Muster
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

## Projektkonfiguration und Build-System
### Struktur des Projektverzeichnisses
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

###`tsconfig.json`– TypeScript-Konfiguration
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

### Build- und Paketverwaltung
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

### Testen mit Vitest
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

### CI/CD-Pipeline – GitHub-Aktionen
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

## Erweiterte Syntax und Muster
### Erweiterte Generika
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

### Dekorateure (TypeScript 5.0+)
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

### Geben Sie Guards und Narrowing ein
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

## Projektkonfiguration und Build-System
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

### Testen mit Vitest
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

### Laufzeitvalidierung mit Zod
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

## Interoperabilität
### Verwendung von JavaScript-Bibliotheken
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

## Designmuster
### Ergebnismuster
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

### Repository-Muster
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

## Bereitstellung
### Docker-Datei
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

## Das Ökosystem
### Schlüsselwerkzeuge
| Werkzeug | Zweck |
|------|---------|
| **tsc** | Der TypeScript-Compiler (offiziell) |
| **ts-node / tsx** | TypeScript direkt ohne separate Kompilierung ausführen |
| **swc** | Ultraschneller Rust-basierter TypeScript/JavaScript-Compiler |
| **ESLint + typescript-eslint** | Linting mit typbewussten Regeln |
| **Zod** | Laufzeittypvalidierung mit TypeScript-Inferenz |
| **tsconfig.json** | TypeScript-Konfigurationsdatei |
### Frameworks (alle TypeScript-First)
| Rahmen | Domäne |
|-----------|--------|
| **Winkel** | Voll ausgestattetes Frontend-Framework (erfordert TypeScript) |
| **Next.js** | Reagieren Sie auf das Meta-Framework (TypeScript-first) |
| **NestJS** | Enterprise-Backend-Framework (TypeScript-first) |
| **tRPC** | Durchgängige typsichere APIs (nur TypeScript) |
| **Prisma** | Typsicheres ORM für Node.js |
---

## Wann TypeScript verwendet werden sollte
| Szenario | Warum TypeScript | Bessere Alternative |
|----------|---------------|-------------------|
| Große JavaScript-Projekte | Typensicherheit verhindert ganze Kategorien von Fehlern | -- |
| Teamprojekte | Typen dienen als gemeinsamer Vertrag | -- |
| API-Entwicklung | Durchgängige Typensicherheit mit tRPC oder OpenAPI | Go, Java für einfachere REST-APIs |
| Jedes neue JavaScript-Projekt | Die Kosten für das spätere Hinzufügen von TypeScript sind hoch | Einfaches JS nur für kleine Skripte |
| Bibliotheken/npm-Pakete | Verbraucher erhalten automatische Vervollständigung und Typprüfung | -- |
**Faustregel**: Wenn Ihr JavaScript-Projekt mehr als ein paar hundert Zeilen umfasst, verwenden Sie TypeScript.
---

## Synthetische Fragen und Antworten
### F1: Was ist der Unterschied zwischen`type`und`interface`und wann sollte ich sie jeweils verwenden?
**A:** Beide definieren Objektformen, haben jedoch unterschiedliche Fähigkeiten. `interface`unterstützt die Zusammenführung von Deklarationen (Zusammenführung mehrerer Deklarationen mit demselben Namen),`extends`für die Vererbung und ist die idiomatische Wahl für öffentliche APIs. `type`unterstützt Union-Typen, Schnittmengentypen, zugeordnete Typen, bedingte Typen und Vorlagenliteraltypen – alles Fortgeschrittene. Best Practice: Verwenden Sie`interface`für Objektformen und öffentliche APIs; Verwenden Sie`type`für Unions, Dienstprogramme und komplexe Typoperationen.
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

### F2: Wie funktionieren Generika und warum sind sie wichtig?
**A:** Mit Generics können Sie Funktionen, Klassen und Typen schreiben, die mit jedem Typ funktionieren und gleichzeitig die Typsicherheit wahren. Anstelle von`any`(wodurch Typinformationen verloren gehen) behalten Generika die Beziehung zwischen Eingabe- und Ausgabetypen bei. Sie bilden die Grundlage für wiederverwendbaren, typsicheren Code.
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

### F3: Was sind Versorgungstypen und welche sollte ich kennen?
**A:** TypeScript bietet integrierte Dienstprogrammtypen, die vorhandene Typen umwandeln. Die wichtigsten:`Partial<T>`(alle optional),`Required<T>`(alle erforderlich),`Pick<T, K>`(Schlüssel auswählen),`Omit<T, K>`(Schlüssel ausschließen), (Versprechen auspacken). Lernen Sie diese kennen – sie machen die meisten benutzerdefinierten Typoperationen überflüssig.
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

### F4: Wie gebe ich asynchronen Code ein und gehe mit Fehlern typsicher um?
**A:** Asynchrone Funktionen geben automatisch`Promise<T>`zurück, wobei T der Rückgabetyp ist. Verwenden Sie `await`, um das Versprechen auszupacken. Für die Fehlerbehandlung verfügt TypeScript nicht über typisierte Ausnahmen, Sie können jedoch Typschutz und Ergebnistypen erstellen. Das „Ergebnismuster“ (inspiriert von Rust) bietet eine Fehlerbehandlung zur Kompilierungszeit.
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

### F5: Was sind Deklarationsdateien (.d.ts) und wie verwende ich Typen von Drittanbietern?
**A:** Deklarationsdateien beschreiben die Typen von JavaScript-Bibliotheken, die nicht über integrierte TypeScript-Typen verfügen. Sie enthalten nur Typinformationen (keinen Laufzeitcode). Installieren Sie von der Community verwaltete Typen von DefinitelyTyped:`npm install --save-dev @types/lodash`. Fügen Sie für Ihre eigenen Bibliotheken ein `types`-Feld in`package.json`hinzu oder fügen Sie `.d.ts`-Dateien neben Ihrer Quelle ein. Verwenden Sie`declare module`für Umgebungsdeklarationen.
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

## Problemlösung in der Gedankenkette
### Problem 1: Erstellen Sie einen typsicheren Ereignisemitter
**Problemstellung:** Erstellen Sie einen generischen, typsicheren Ereignisemitter in TypeScript, bei dem jeder Ereignisname einem bestimmten Nutzlasttyp zugeordnet ist. Der Compiler sollte zur Kompilierungszeit falsche Ereignisnamen und Nutzlasttypen erkennen.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen ein Ereignissystem, in dem: (1) Ereignisse mit ihren Nutzlasttypen definiert werden, (2)`emit`nur gültige Ereignisnamen mit korrekten Nutzlasten akzeptiert, (3)`on`nur gültige Ereignisnamen mit korrekt typisierten Handlern akzeptiert. Dies erfordert zugeordnete Typen und Generika über eine Ereigniszuordnungsschnittstelle.
**Schritt 2 – Identifizieren Sie den Ansatz:**
- Definieren Sie einen `EventMap`-Typ: `{ [eventName: string]: payloadType }`.
– Verwenden Sie `keyof EventMap`, um Ereignisnamen einzuschränken.
– Verwenden Sie `EventMap[K]`, um den Nutzlasttyp für ein bestimmtes Ereignis abzurufen.
- Speichern Sie Listener in einem`Map<string, Function[]>`.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
- Typensicherheit: Der Compiler erkennt beim Kompilieren falsche Ereignisnamen und falsche Nutzlastformen.
-`on`gibt eine Abmeldefunktion zur bequemen Bereinigung zurück.
–`once`umschließt den Listener so, dass er sich nach dem ersten Aufruf automatisch abmeldet.
– Für die Produktion: Fügen Sie`listenerCount`und`removeAllListeners`hinzu und erwägen Sie die Verwendung von`AbortSignal`zur Stornierung.
### Problem 2: Implementieren Sie einen typsicheren SQL Query Builder
**Problemstellung:** Erstellen Sie einen SQL-Abfrage-Builder, bei dem die Spaltennamen und -typen von einer TypeScript-Schnittstelle abgeleitet werden. Der Builder sollte ungültige Spaltennamen und Typkonflikte zur Kompilierungszeit verhindern.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) Spaltennamen, die auf`keyof T`beschränkt sind, (2) WHERE-Klauselwerte, die entsprechend der Spalte typisiert sind, (3) eine verkettbare API zum Erstellen von Abfragen. Dies erfordert durch`Record<string, unknown>`eingeschränkte Generika.
**Schritt 2 – Identifizieren Sie den Ansatz:**
– Verwenden Sie`keyof T`für Spaltennamenbeschränkungen.
– Verwenden Sie`T[K]`für Werttypbeschränkungen.
- SQL-String mit parametrisierten Abfragen erstellen (SQL-Injection verhindern).
- Verkettbare Methoden geben`this`zurück.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
- Verhinderung von SQL-Injection: Alle Werte durchlaufen parametrisierte Abfragen (`$1`, `$2`), niemals interpoliert.
- Typsicherheit: Spaltennamen und Werttypen werden zur Kompilierzeit überprüft.
- Erweiterbarkeit: Fügen Sie die Methoden `join`, `groupBy`, `having`,`insert`und`update`nach demselben Muster hinzu.
- Produktion: Verwenden Sie`kysely`oder`drizzle-orm`– sie bieten diese Typsicherheit mit vollständiger SQL-Abdeckung.
### Problem 3: Implementieren Sie eine Finite-State-Maschine mit Typsicherheit
**Problemstellung:** Erstellen Sie eine typsichere Finite-State-Maschine, in der gültige Übergänge zur Kompilierungszeit erzwungen werden. Jeder Zustand kann Ein-/Austrittsaktionen haben und die Maschine sollte den aktuellen Zustand verfolgen.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) als Typen definierte Zustände und Ereignisse, (2) gültige Übergänge, die auf Typebene abgebildet werden, (3) der Compiler verhindert ungültige Übergänge, (4) Laufzeitverfolgung mit Rückrufen. Dies erfordert zugeordnete Typen und bedingte Typen.
**Schritt 2 – Identifizieren Sie den Ansatz:**
- Definieren Sie einen `TransitionMap`: `{ [State]: { [Event]: NextState } }`.
– Verwenden Sie Generika, um`send(event)`basierend auf dem aktuellen Status einzuschränken.
- Verfolgen Sie den Status zur Laufzeit mit einer Variablen.
- Unterstützen Sie Ein-/Ausstiegsrückrufe pro Bundesstaat.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
- Laufzeitsicherheit:`send`löst ungültige Übergänge aus.
- Typsicherheit: Der Typ`EventsFor`extrahiert zur Kompilierungszeit gültige Ereignisse pro Status.
- Ein-/Ausstiegsrückrufe werden bei Übergängen automatisch ausgelöst.
- Für die Produktion: Verwenden Sie`xstate`– es bietet eine vollständige Zustandsmaschinenbibliothek mit visuellem Debugging, hierarchischen Zuständen, Schutzvorrichtungen und Aktionen.
---

## Zusammenfassung
TypeScript ist JavaScript, das sich für alles eignet, was über triviale Skripte hinausgeht. Es fügt ein leistungsstarkes Typsystem hinzu, das Fehler frühzeitig erkennt, die Tools verbessert und Code dokumentiert – und das alles bei gleichzeitiger Kompilierung in Standard-JavaScript, das überall ausgeführt werden kann. Die Lernkurve ist sanft (Sie können mit minimalen Typen beginnen), aber die Tiefe ist enorm (das Typensystem ist Turing-vollständig). Für die moderne JavaScript-Entwicklung ist TypeScript zum Industriestandard geworden.