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
# TypeScript
TypeScript ni seti kuu ya JavaScript iliyochapwa kwa takwimu iliyotengenezwa na Microsoft (inayoongozwa na Anders Hejlsberg) na ilitolewa kwa mara ya kwanza mwaka wa 2012. Inaongeza maelezo ya hiari ya aina, violesura, jenereta na vipengele vya mfumo wa aina ya juu kwenye JavaScript - kisha inajumlisha hadi JavaScript wazi inayofanya kazi popote JavaScript. TypeScript si lugha tofauti au wakati wa utekelezaji; ni JavaScript iliyo na kikagua aina.
TypeScript imekuwa kiwango cha ukuzaji wa JavaScript kwa kiwango kikubwa. React, Angular, VS Code, Deno, na miradi mingi mikuu ya programu huria ya JavaScript imeandikwa katika TypeScript. Ikiwa unaanza mradi mpya wa JavaScript wa ukubwa wowote muhimu, TypeScript ndiyo chaguomsingi inayopendekezwa.
---

## Kwa nini TypeScript ni muhimu
- **Hupata hitilafu kwa wakati wa kukusanya**: Hitilafu za aina hupatikana kabla ya msimbo kutekelezwa - sio katika toleo la umma.
- **Usaidizi bora wa IDE**: Kamilisha kiotomatiki, nenda-kwa-ufafanuzi, urekebishaji upya, na uwekaji wa hati ulio ndani yote unaboresha sana.
- **Msimbo wa kujiandikisha**: Aina hutumika kama hati ambazo husasishwa.
- **100% JavaScript inaoana**: JavaScript yoyote halali ni TypeScript halali. Unaweza kupitisha hatua kwa hatua.
- **Mfumo wa aina ya hali ya juu**: Aina za muungano, aina za makutano, aina za masharti, aina zilizochorwa, aina halisi za violezo - mfumo wa aina unajieleza vya kutosha kuiga mantiki changamano ya kikoa.
- **Kupitishwa kwa sekta **: Angular inahitaji; Mfumo wa ikolojia wa React huitumia kwa wingi; vifurushi vingi vipya vya npm husafirishwa na ufafanuzi wa aina.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Hatua ya mkusanyiko** | Lazima ikusanye`.ts`→`.js`kabla ya kukimbia | Tumia`ts-node`/`tsx`kwa maendeleo; `tsc`kwa ajili ya uzalishaji |
| **Mwingo wa kujifunza** | Mfumo wa aina unaweza kuwa mgumu (generics, aina za masharti) | Anza na aina za msingi; kupitisha vipengele vya juu hatua kwa hatua |
| **Aina faili za ufafanuzi** | Sio vifurushi vyote vya npm vinavyosafirishwa na aina | Sakinisha`@types/package-name`kutoka DefinitelyTyped |
| **Kukusanya nyakati** | Miradi mikubwa inaweza kuwa polepole kuandika-angalia | Tumia marejeleo ya mradi,`isolatedModules`, au`swc`|
| **Hisia potofu za usalama** | Aina hazihakikishi usahihi wa wakati wa kukimbia | Changanya na uthibitishaji wa wakati wa kukimbia (Zod, io-ts) |
---

## Misingi ya Sintaksia
### Vidokezo vya Aina ya Msingi
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

### Violesura na Aina
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

### Jenerali
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

### Aina za Kina
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

### Async na Aina
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

## Sintaksia na Miundo ya Kina
### Jeni za Kina
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

### Vipamba (TypeScript 5.0+ Standard)
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

### Aina ya Walinzi na Kupunguza
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

## Concurrency & Usambamba
TypeScript hurithi muundo wa upatanishi wa JavaScript lakini huongeza usalama wa aina kwenye mifumo isiyosawazisha.
### Miundo ya Async Imechapishwa
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Saraka ya Mradi
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

###`tsconfig.json`— Usanidi wa Hati ya Aina
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

### Kuunda na Usimamizi wa Kifurushi
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

### Jaribio na Vitest
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

### CI/CD Bomba - Vitendo vya GitHub
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

## Sintaksia na Miundo ya Kina
### Jeni za Kina
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

### Vipamba (TypeScript 5.0+)
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

### Aina ya Walinzi na Kupunguza
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

## Usanidi wa Mradi na Mfumo wa Kuunda
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

### Jaribio na Vitest
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

### Uthibitishaji wa Muda wa Kuendesha na Zod
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

## Kuingiliana
### Kwa kutumia JavaScript Maktaba
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

## Miundo ya Kubuni
### Muundo wa Matokeo
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

### Muundo wa Hifadhi
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

## Usambazaji
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

## Mfumo wa Ikolojia
### Zana Muhimu
| Zana | Kusudi |
|------|----------|
| **tsc** | Mkusanyaji wa TypeScript (rasmi) |
| **ts-nodi / tsx** | Endesha TypeScript moja kwa moja bila mkusanyiko tofauti |
| **swc** | Kikusanyaji cha TypeScript/JavaScript chenye kasi ya juu zaidi |
| **ESLint + typescript-eslint** | Linting na aina-aware sheria |
| **Zodi** | Uthibitishaji wa aina ya wakati wa kukimbia na marejeleo ya TypeScript |
| **tsconfig.json** | Faili ya usanidi wa TypeScript |
### Mifumo (TypeScript Yote-Kwanza)
| Mfumo | Kikoa |
|-----------|--------|
| **Angular** | Mfumo wa mandhari ya mbele ulio na kipengele kamili (inahitaji TypeScript) |
| **Inayofuata.js** | React meta-framework (TypeScript-first) |
| **NestJS** | Mfumo wa nyuma wa biashara (TypeScript-first) |
| **tRPC** | End-to-end typesafe APIs (TypeScript-pekee) |
| **Prisma** | Aina-salama ya ORM ya Node.js |
---

## Wakati wa Kutumia TypeScript
| Hali | Kwa nini TypeScript | Mbadala Bora |
|----------|----------------------------------|
| Miradi mikubwa ya JavaScript | Usalama wa aina huzuia aina zote za hitilafu | -- |
| Miradi ya timu | Aina hutumika kama mkataba wa pamoja | -- |
| Maendeleo ya API | Usalama wa aina ya mwisho hadi mwisho na tRPC au OpenAPI | Nenda, Java kwa API rahisi za REST |
| Mradi wowote mpya wa JavaScript | Gharama ya kuongeza TypeScript baadaye ni kubwa | Plain JS kwa hati ndogo pekee |
| Maktaba / vifurushi vya npm | Wateja hukamilishwa kiotomatiki na kuandika kuangalia | -- |
**Kanuni ya kidole gumba**: Ikiwa mradi wako wa JavaScript una zaidi ya mistari mia chache, tumia TypeScript.
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`type`na`interface`, na ninapaswa kutumia kila moja lini?
**J:** Zote zinafafanua maumbo ya kitu, lakini zina uwezo tofauti. `interface`inaauni ujumuishaji wa tamko (matangazo mengi yenye jina sawa kuunganisha),`extends`kwa urithi, na ni chaguo la nahau kwa API za umma. `type`hutumia aina za miungano, aina za makutano, aina za ramani, aina za masharti na aina halisi za violezo - chochote cha juu. Mbinu bora: tumia`interface`kwa maumbo ya kitu na API za umma; tumia`type`kwa vyama vya wafanyakazi, huduma, na shughuli za aina changamano.
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

### Q2: Je, jeneriki hufanya kazi vipi, na kwa nini ni muhimu?
**J:** Jenerili hukuruhusu kuandika vipengele, madarasa na aina zinazofanya kazi na aina yoyote huku ukidumisha usalama wa aina. Badala ya`any`(ambayo hupoteza maelezo ya aina), jenetiki huhifadhi uhusiano kati ya aina za ingizo na pato. Ndio msingi wa nambari inayoweza kutumika tena, salama ya aina.
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

### Q3: Ni aina gani za matumizi, na ni zipi ninapaswa kujua?
**J:** TypeScript hutoa aina za matumizi zilizojengewa ndani zinazobadilisha aina zilizopo. Muhimu zaidi:`Partial<T>`(yote ni hiari),`Required<T>`(zote zinahitajika),`Pick<T, K>`(chagua funguo),`Omit<T, K>`(ondoa funguo),`Record<K, V>`(ramani ya thamani-muhimu),`Pick<T, K>`(chagua tena funguo ZRKERX kutoka kwa muungano wa XQERX) aina),`Awaited<T>`(fungua Ahadi). Jifunze haya - yanaondoa hitaji kubwa la shughuli za aina maalum.
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

### Q4: Ninawezaje kuandika msimbo wa async na kushughulikia makosa kwa njia salama ya aina?
**J:** Vitendaji vya Async hurejesha kiotomatiki`Promise<T>`ambapo T ni aina ya kurejesha. Tumia`await`kufungua Ahadi. Kwa kushughulikia makosa, TypeScript haina vighairi vilivyoandikwa, lakini unaweza kuunda walinzi wa aina na aina za matokeo. "Mchoro wa matokeo" (ulioongozwa na Rust) hutoa utunzaji wa makosa ya wakati.
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

### Q5: Faili za tamko (.d.ts) ni nini na ninawezaje kutumia aina za watu wengine?
**J:** Faili za tamko zinaelezea aina za maktaba za JavaScript ambazo hazina aina za TypeScript zilizojengewa ndani. Zina maelezo ya aina pekee (hakuna msimbo wa wakati wa kukimbia). Sakinisha aina zinazodumishwa na jumuiya kutoka DefinitelyTyped:`npm install --save-dev @types/lodash`. Kwa maktaba zako mwenyewe, ongeza sehemu ya`types`katika`package.json`au ujumuishe faili za`.d.ts`pamoja na chanzo chako. Tumia`declare module`kwa tamko la mazingira.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tengeneza Kitoa Tukio cha Aina-salama
**Taarifa ya Tatizo:** Unda mtoaji wa tukio la kawaida, aina-salama katika TypeScript ambapo kila jina la tukio linaonyesha aina mahususi ya upakiaji. Mkusanyaji anapaswa kupata majina ya matukio na aina zisizo sahihi za upakiaji kwa wakati wa kukusanya.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji mfumo wa matukio ambapo: (1) matukio yamebainishwa kwa aina zake za upakiaji, (2)`emit`inakubali tu majina halali ya matukio yenye mizigo sahihi, (3)`on`inakubali tu majina halali ya matukio yenye vishikilizi vilivyoandikwa kwa usahihi. Hii inahitaji aina zilizochorwa na jenetiki kwenye kiolesura cha ramani ya tukio.
**Hatua ya 2 — Tambua Mbinu:**
- Bainisha aina ya `EventMap`:`{ [eventName: string]: payloadType }`.
- Tumia`keyof EventMap`kulazimisha majina ya hafla.
- Tumia`EventMap[K]`kupata aina ya malipo kwa tukio maalum.
- Hifadhi wasikilizaji katika `Map<string, Function[]>`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa aina: mkusanyaji hushika majina ya matukio yasiyo sahihi na maumbo yasiyo sahihi ya upakiaji kwa wakati wa kukusanya.
-`on`hurejesha kitendakazi cha kujiondoa kwa usafishaji rahisi.
-`once`hufunga msikilizaji kujiondoa kiotomatiki baada ya ombi la kwanza.
- Kwa uzalishaji: ongeza`listenerCount`,`removeAllListeners`, na uzingatie kutumia`AbortSignal`kwa kughairi.
### Tatizo la 2: Tekeleza Kiunda Hoji cha Aina-salama cha SQL
**Taarifa ya Tatizo:** Tengeneza kiunda hoja cha SQL ambapo majina na aina za safu wima zimetolewa kutoka kwa kiolesura cha TypeScript. Mjenzi anapaswa kuzuia majina ya safu wima batili na aina zisizolingana wakati wa kukusanya.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) majina ya safu wima yaliyobanwa kuwa`keyof T`, (2) AMBAPO thamani za vifungu zimechapwa kulingana na safu wima, (3) API inayoweza kuunganishwa kwa hoja za ujenzi. Hii inahitaji jenetiki zinazodhibitiwa na`Record<string, unknown>`.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`keyof T`kwa vikwazo vya jina la safu.
- Tumia`T[K]`kwa vikwazo vya aina ya thamani.
- Jenga kamba ya SQL na maswali yenye vigezo (zuia sindano ya SQL).
- Njia zinazoweza kurudishwa`this`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Uzuiaji wa sindano ya SQL: maadili yote hupitia maswali yaliyo na vigezo (`$1`,`$2`), kamwe hayajaingiliwa.
- Usalama wa aina: majina ya safu wima na aina za thamani huangaliwa kwa wakati wa kukusanya.
- Upanuzi: ongeza`join`,`groupBy`,`having`,`insert`,`update`mbinu zinazofuata muundo sawa.
- Uzalishaji: tumia`kysely`au`drizzle-orm`- zinatoa usalama wa aina hii kwa ufunikaji kamili wa SQL.
### Tatizo la 3: Tekeleza Mashine ya Hali Filamu yenye Usalama wa Aina
**Taarifa ya Tatizo:** Unda mashine ya hali ya ukomo ya aina-salama ambapo mageuzi halali yanatekelezwa wakati wa kukusanya. Kila jimbo linaweza kuwa na vitendo vya kuingia/kutoka, na mashine inapaswa kufuatilia hali ya sasa.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) hali na matukio yanayofafanuliwa kama aina, (2) mageuzi halali yaliyopangwa katika kiwango cha aina, (3) kikusanyaji huzuia mabadiliko yasiyo sahihi, (4) ufuatiliaji wa hali ya wakati wa utekelezaji kwa kupiga simu tena. Hii inahitaji aina zilizopangwa na aina za masharti.
**Hatua ya 2 — Tambua Mbinu:**
- Fafanua `TransitionMap`: `{ [State]: { [Event]: NextState } }`.
- Tumia jenetiki kulazimisha`send(event)`kulingana na hali ya sasa.
- Fuatilia hali wakati wa kukimbia na mabadiliko.
- Ingizo la usaidizi/toka kwa kurudi nyuma kwa kila jimbo.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa wakati wa kukimbia:`send`inarusha kwenye mipito isiyo sahihi.
- Usalama wa aina: aina ya`EventsFor`hutoa matukio halali kwa kila hali kwa wakati wa kukusanya.
- Kuingia/kutoka kwa callbacks moto moja kwa moja juu ya mabadiliko.
- Kwa uzalishaji: tumia`xstate`- hutoa maktaba ya mashine ya hali kamili yenye utatuzi wa kuona, hali ya mada, walinzi na vitendo.
---

## Muhtasari
TypeScript ni JavaScript iliyofanywa kwa haki kwa chochote zaidi ya hati ndogo. Inaongeza mfumo wa aina wenye nguvu ambao hunasa hitilafu mapema, inaboresha zana, na msimbo wa hati -- yote huku ikijumuisha JavaScript ya kawaida inayotumika popote. Curve ya kujifunza ni mpole (unaweza kuanza na aina ndogo) lakini kina ni kikubwa (mfumo wa aina ni Turing-kamili). Kwa maendeleo ya kisasa ya JavaScript, TypeScript imekuwa kiwango cha tasnia.