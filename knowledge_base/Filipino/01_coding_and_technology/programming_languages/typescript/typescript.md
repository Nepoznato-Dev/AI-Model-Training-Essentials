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
Ang TypeScript ay isang statically typed superset ng JavaScript na binuo ng Microsoft (pinununahan ni Anders Hejlsberg) at unang inilabas noong 2012. Nagdaragdag ito ng opsyonal na uri ng mga anotasyon, mga interface, generic, at mga advanced na feature ng type-system sa JavaScript — pagkatapos ay nag-compile hanggang sa simpleng JavaScript na tumatakbo saanman tumatakbo ang JavaScript. Ang TypeScript ay hindi isang hiwalay na wika o runtime; ito ay JavaScript na may uri ng checker.
Ang TypeScript ay naging pamantayan para sa malakihang pagbuo ng JavaScript. Ang React, Angular, VS Code, Deno, at karamihan sa mga pangunahing open-source na proyekto ng JavaScript ay nakasulat sa TypeScript. Kung nagsisimula ka ng bagong proyekto ng JavaScript ng anumang makabuluhang laki, TypeScript ang inirerekomendang default.
---

## Bakit Mahalaga ang TypeScript
- **Nakakakuha ng mga bug sa oras ng pag-compile**: Ang mga error sa uri ay matatagpuan bago tumakbo ang code — wala sa produksyon.
- **Mas mahusay na suporta sa IDE**: Ang Autocomplete, go-to-definition, refactoring, at inline na dokumentasyon ay bumuti nang husto.
- **Self-documenting code**: Ang mga uri ay nagsisilbing dokumentasyon na nananatiling napapanahon.
- **100% JavaScript compatible**: Ang anumang wastong JavaScript ay wastong TypeScript. Maaari mo itong i-adopt nang paunti-unti.
- **Advanced na uri ng system**: Mga uri ng unyon, mga uri ng intersection, mga uri ng kondisyon, mga uri ng naka-map, mga literal na uri ng template — ang sistema ng uri ay sapat na nagpapahayag upang magmodelo ng kumplikadong lohika ng domain.
- **Pag-aampon sa industriya**: Kinakailangan ito ng Angular; Gumagamit ito ng react ecosystem; karamihan sa mga bagong npm na pakete ay ipinapadala na may mga kahulugan ng uri.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Hakbang ng compilation** | Dapat i-compile ang`.ts`→`.js`bago tumakbo | Gamitin ang`ts-node`/`tsx`para sa pagpapaunlad; `tsc`para sa produksyon |
| **Learning curve** | Ang uri ng system ay maaaring kumplikado (generics, conditional type) | Magsimula sa mga pangunahing uri; unti-unting gamitin ang mga advanced na feature |
| **I-type ang mga file ng kahulugan** | Hindi lahat ng npm package ay nagpapadala ng mga uri | I-install ang`@types/package-name`mula sa DefinitelyTyped |
| **Mga oras ng pag-compile** | Ang malalaking proyekto ay maaaring mabagal sa pag-type-check | Gumamit ng mga sanggunian sa proyekto,`isolatedModules`, o`swc`|
| **Maling pakiramdam ng seguridad** | Hindi ginagarantiyahan ng mga uri ang kawastuhan ng runtime | Pagsamahin sa pagpapatunay ng runtime (Zod, io-ts) |
---

## Syntax Fundamentals
### Pangunahing Uri ng Anotasyon
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

### Mga Interface at Uri
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

### Generics
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

### Mga Advanced na Uri
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

### Async na may Mga Uri
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

## Advanced na Syntax at Mga Pattern
### Advanced na Generics
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

### Mga Dekorador (TypeScript 5.0+ Standard)
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

### Uri ng Guards at Narrowing
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

## Concurrency at Paralelismo
Nakuha ng TypeScript ang concurrency na modelo ng JavaScript ngunit nagdaragdag ng kaligtasan ng uri sa mga pattern ng async.
### Mga Na-type na Async Pattern
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

## Project Configuration at Build System
### Istraktura ng Direktoryo ng Proyekto
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

###`tsconfig.json`— TypeScript Configuration
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

### Pamamahala ng Build at Package
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

### Pagsubok sa Vitest
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

### CI/CD Pipeline — Mga Pagkilos sa GitHub
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

## Advanced na Syntax at Mga Pattern
### Advanced na Generics
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

### Mga Dekorador (TypeScript 5.0+)
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

### Uri ng Guards at Narrowing
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

## Project Configuration at Build System
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

### Pagsubok sa Vitest
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

### Runtime Validation kasama si Zod
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

## Interoperability
### Paggamit ng JavaScript Libraries
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

## Mga Pattern ng Disenyo
### Pattern ng Resulta
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

### Pattern ng Imbakan
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

## Deployment
### Dockerfile
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

## Ang Ecosystem
### Mga Pangunahing Tool
| Tool | Layunin |
|------|---------|
| **tsc** | Ang TypeScript compiler (opisyal) |
| **ts-node / tsx** | Direktang patakbuhin ang TypeScript nang walang hiwalay na compilation |
| **swc** | Napakabilis na Rust-based TypeScript/JavaScript compiler |
| **ESLint + typescript-eslint** | Linting na may type-aware rules |
| **Zod** | Pagpapatunay ng uri ng runtime na may TypeScript inference |
| **tsconfig.json** | TypeScript configuration file |
### Mga Framework (Lahat ng TypeScript-Una)
| Balangkas | Domain |
|-----------|--------|
| **Angular** | Full-feature na frontend framework (nangangailangan ng TypeScript) |
| **Next.js** | React meta-framework (TypeScript-first) |
| **NestJS** | Enterprise backend framework (TypeScript-first) |
| **tRPC** | End-to-end typesafe API (TypeScript-only) |
| **Prisma** | Uri-safe ORM para sa Node.js |
---

## Kailan Gamitin ang TypeScript
| Sitwasyon | Bakit TypeScript | Mas mahusay na Alternatibo |
|----------|----------------|-------------------|
| Mga malalaking proyekto ng JavaScript | Pinipigilan ng kaligtasan ng uri ang buong kategorya ng mga bug | -- |
| Mga proyekto ng pangkat | Ang mga uri ay nagsisilbing isang nakabahaging kontrata | -- |
| Pag-unlad ng API | End-to-end na uri ng kaligtasan sa tRPC o OpenAPI | Pumunta, Java para sa mas simpleng REST API |
| Anumang bagong proyekto ng JavaScript | Ang halaga ng pagdaragdag ng TypeScript mamaya ay mataas | Plain JS para sa maliliit na script lamang |
| Mga aklatan / npm na pakete | Ang mga mamimili ay nakakakuha ng autocomplete at pagsuri ng uri | -- |
**Rule of thumb**: Kung ang iyong proyekto sa JavaScript ay may higit sa ilang daang linya, gamitin ang TypeScript.
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba ng`type`at`interface`, at kailan ko dapat gamitin ang bawat isa?
**A:** Parehong tumutukoy sa mga hugis ng bagay, ngunit may iba't ibang kakayahan ang mga ito.  Sinusuportahan ng`interface`ang pagsasama-sama ng deklarasyon (maraming deklarasyon na may parehong pagsasama-sama ng pangalan),`extends`para sa mana, at ito ang idiomatic na pagpipilian para sa mga pampublikong API.  Sinusuportahan ng`type`ang mga uri ng unyon, mga uri ng intersection, mga naka-map na uri, mga uri ng kondisyon, at mga literal na uri ng template — anumang advanced. Pinakamahusay na kasanayan: gumamit ng`interface`para sa mga hugis ng bagay at pampublikong API; gamitin ang`type`para sa mga unyon, utility, at kumplikadong uri ng operasyon.
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

### Q2: Paano gumagana ang generics, at bakit mahalaga ang mga ito?
**A:** Hinahayaan ka ng mga generic na magsulat ng mga function, klase, at uri na gumagana sa anumang uri habang pinapanatili ang kaligtasan ng uri. Sa halip na`any`(na nawawalan ng impormasyon sa uri), pinapanatili ng mga generic ang ugnayan sa pagitan ng mga uri ng input at output. Sila ang pundasyon ng reusable, type-safe na code.
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

### Q3: Ano ang mga uri ng utility, at alin ang dapat kong malaman?
**A:** Nagbibigay ang TypeScript ng mga built-in na uri ng utility na nagbabago sa mga kasalukuyang uri. Ang pinakamahalaga:`Partial<T>`(lahat ng opsyonal),`Required<T>`(kinakailangan lahat),`Pick<T, K>`(piliin ang mga key),`Omit<T, K>`(ibukod ang mga key),`Record<K, V>`(key-value na mapa),`Exclude<T, U>`(alisin mula sa unipormeng6XQZ), XQZMARKER na function, XQZMARKER6X (alisin mula sa union6X)`Awaited<T>`(i-unwrap ang Pangako). Alamin ang mga ito — inaalis nila ang karamihan sa pangangailangan para sa mga pasadyang uri ng pagpapatakbo.
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

### Q4: Paano ko ita-type ang async code at pangasiwaan ang mga error sa paraang ligtas sa uri?
**A:** Ang mga function ng Async ay awtomatikong nagbabalik ng`Promise<T>`kung saan ang T ay ang uri ng pagbabalik. Gamitin ang`await`para i-unwrap ang Pangako. Para sa paghawak ng error, ang TypeScript ay walang mga pagbubukod sa pag-type, ngunit maaari kang lumikha ng mga bantay ng uri at mga uri ng resulta. Ang "Result pattern" (inspirasyon ng Rust) ay nagbibigay ng compile-time na paghawak ng error.
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

### Q5: Ano ang mga file ng deklarasyon (.d.ts) at paano ko gagamitin ang mga uri ng third-party?
**A:** Inilalarawan ng mga file ng deklarasyon ang mga uri ng mga library ng JavaScript na walang mga built-in na uri ng TypeScript. Naglalaman lamang ang mga ito ng impormasyon ng uri (walang runtime code). I-install ang mga uri na pinananatili ng komunidad mula sa DefinitelyTyped:`npm install --save-dev @types/lodash`. Para sa sarili mong mga library, magdagdag ng`types`field sa`package.json`o isama ang`.d.ts`file sa tabi ng iyong source. Gamitin ang`declare module`para sa mga deklarasyon sa paligid.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Uri-Ligtas na Event Emitter
**Problem Statement:** Lumikha ng generic, type-safe na event emitter sa TypeScript kung saan ang bawat pangalan ng event ay nagmamapa sa isang partikular na uri ng payload. Dapat mahuli ng compiler ang mga maling pangalan ng kaganapan at mga uri ng payload sa oras ng pag-compile.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng system ng kaganapan kung saan: (1) ang mga kaganapan ay tinukoy sa kanilang mga uri ng payload, (2) ang`emit`ay tumatanggap lamang ng mga wastong pangalan ng kaganapan na may tamang mga payload, (3) ang`on`ay tumatanggap lamang ng mga wastong pangalan ng kaganapan na may wastong na-type na mga humahawak. Nangangailangan ito ng mga naka-map na uri at generic sa isang interface ng mapa ng kaganapan.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Tukuyin ang isang uri ng `EventMap`:`{ [eventName: string]: payloadType }`.
- Gamitin ang`keyof EventMap`upang hadlangan ang mga pangalan ng kaganapan.
- Gamitin ang`EventMap[K]`upang makuha ang uri ng payload para sa isang partikular na kaganapan.
- Mag-imbak ng mga tagapakinig sa isang`Map<string, Function[]>`.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Uri ng kaligtasan: ang compiler ay nakakakuha ng mga maling pangalan ng kaganapan at maling mga hugis ng payload sa oras ng pag-compile.
- Nagbabalik ang`on`ng unsubscribe function para sa maginhawang paglilinis.
- Binabalot ng`once`ang tagapakinig upang awtomatikong mag-unsubscribe pagkatapos ng unang invocation.
- Para sa produksyon: magdagdag ng`listenerCount`,`removeAllListeners`, at isaalang-alang ang paggamit ng`AbortSignal`para sa pagkansela.
### Problema 2: Magpatupad ng Type-Safe SQL Query Builder
**Problem Statement:** Bumuo ng SQL query builder kung saan ang mga pangalan at uri ng column ay hinango mula sa isang TypeScript interface. Dapat pigilan ng tagabuo ang mga di-wastong pangalan ng column at hindi pagkakatugma ng uri sa oras ng pag-compile.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) mga pangalan ng column na nalilimitahan sa`keyof T`, (2) WHERE ang mga value ng clause ay nai-type ayon sa column, (3) chainable API para sa pagbuo ng mga query. Nangangailangan ito ng mga generic na pinipigilan ng`Record<string, unknown>`.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`keyof T`para sa mga hadlang sa pangalan ng column.
- Gamitin ang`T[K]`para sa mga hadlang sa uri ng halaga.
- Bumuo ng SQL string na may mga parameterized na query (iwasan ang SQL injection).
- Ang mga nakaka-chain na pamamaraan ay nagbabalik ng`this`.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Pag-iwas sa SQL injection: lahat ng value ay dumadaan sa mga parameterized na query (`$1`,`$2`), hindi kailanman na-interpolated.
- Kaligtasan ng uri: ang mga pangalan ng column at mga uri ng halaga ay sinusuri sa oras ng pag-compile.
- Extensibility: magdagdag ng`join`,`groupBy`,`having`,`insert`,`update`na mga pamamaraan na sumusunod sa parehong pattern.
- Produksyon: gumamit ng`kysely`o`drizzle-orm`— nagbibigay sila ng ganitong uri ng kaligtasan na may buong saklaw ng SQL.
### Problema 3: Magpatupad ng Finite State Machine na may Uri ng Kaligtasan
**Pahayag ng Problema:** Lumikha ng isang uri-safe na may hangganan na makina ng estado kung saan ipinapatupad ang mga wastong transition sa oras ng pag-compile. Ang bawat estado ay maaaring magkaroon ng mga pagkilos sa pagpasok/paglabas, at dapat na subaybayan ng makina ang kasalukuyang estado.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) mga estado at kaganapan na tinukoy bilang mga uri, (2) wastong mga transition na nakamapa sa antas ng uri, (3) pinipigilan ng compiler ang mga di-wastong transition, (4) runtime state tracking na may mga callback. Nangangailangan ito ng mga naka-map na uri at uri ng kondisyon.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Tukuyin ang isang`TransitionMap`:`{ [State]: { [Event]: NextState } }`.
- Gumamit ng mga generic upang hadlangan ang`send(event)`batay sa kasalukuyang estado.
- Subaybayan ang estado sa runtime na may variable.
- Suportahan ang entry/exit callback bawat estado.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Kaligtasan sa runtime: Ang`send`ay naghagis sa mga di-wastong transition.
- Kaligtasan ng uri: ang uri ng`EventsFor`ay kumukuha ng mga wastong kaganapan sa bawat estado sa oras ng pag-compile.
- Ang pagpasok/paglabas ng mga callback ay awtomatikong gumagana sa mga transition.
- Para sa produksyon: gamitin ang`xstate`— nagbibigay ito ng buong state machine library na may visual debugging, hierarchical states, guards, at actions.
---

## Buod
Ang TypeScript ay JavaScript na ginawa nang tama para sa anumang bagay na lampas sa mga walang kuwentang script. Nagdaragdag ito ng malakas na uri ng system na maagang nakakakuha ng mga bug, nagpapahusay ng tooling, at code ng mga dokumento -- habang nagko-compile sa karaniwang JavaScript na tumatakbo kahit saan. Ang curve ng pag-aaral ay banayad (maaari kang magsimula sa mga kaunting uri) ngunit ang lalim ay malawak (ang uri ng sistema ay Turing-kumpleto). Para sa modernong pag-unlad ng JavaScript, ang TypeScript ay naging pamantayan ng industriya.