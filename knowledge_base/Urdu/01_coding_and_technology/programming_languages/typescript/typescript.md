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
# ٹائپ اسکرپٹ
TypeScript جاوا اسکرپٹ کا ایک جامد ٹائپ شدہ سپر سیٹ ہے جسے Microsoft (Anders Hejlsberg کی قیادت میں) نے تیار کیا تھا اور اسے پہلی بار 2012 میں ریلیز کیا گیا تھا۔ یہ جاوا اسکرپٹ میں اختیاری قسم کی تشریحات، انٹرفیس، جنرکس، اور جدید قسم کے نظام کی خصوصیات کو شامل کرتا ہے — پھر سادہ جاوا اسکرپٹ کو مرتب کرتا ہے جہاں جاوا اسکرپٹ چلتا ہے۔ TypeScript ایک الگ زبان یا رن ٹائم نہیں ہے۔ یہ جاوا اسکرپٹ ہے جس میں ٹائپ چیکر ہے۔
TypeScript بڑے پیمانے پر JavaScript کی ترقی کا معیار بن گیا ہے۔ ری ایکٹ، انگولر، وی ایس کوڈ، ڈینو، اور سب سے بڑے اوپن سورس جاوا اسکرپٹ پروجیکٹس ٹائپ اسکرپٹ میں لکھے گئے ہیں۔ اگر آپ کسی اہم سائز کا نیا JavaScript پروجیکٹ شروع کر رہے ہیں تو TypeScript تجویز کردہ ڈیفالٹ ہے۔
---

## ٹائپ اسکرپٹ کیوں اہمیت رکھتا ہے۔
- **کمپائل کے وقت کیڑے پکڑتا ہے**: کوڈ کے چلنے سے پہلے ٹائپ کی غلطیاں پائی جاتی ہیں — پروڈکشن میں نہیں۔
- **بہتر IDE سپورٹ**: خودکار تکمیل، گو ٹو ڈیفینیشن، ری فیکٹرنگ، اور ان لائن دستاویزات سبھی ڈرامائی طور پر بہتر ہوتے ہیں۔
- **خود دستاویزی کوڈ**: اقسام دستاویزات کے طور پر کام کرتی ہیں جو تازہ ترین رہتی ہیں۔
- **100% JavaScript ہم آہنگ**: کوئی بھی درست JavaScript درست TypeScript ہے۔ آپ اسے آہستہ آہستہ اپنا سکتے ہیں۔
- **ایڈوانسڈ ٹائپ سسٹم**: یونین کی قسمیں، انٹرسیکشن کی قسمیں، مشروط قسمیں، نقشہ بندی کی قسمیں، سانچے کی لغوی قسمیں — ٹائپ سسٹم پیچیدہ ڈومین منطق کو ماڈل کرنے کے لیے کافی اظہار خیال کرتا ہے۔
- **صنعت اپنانا**: کونیی اس کی ضرورت ہے۔ رد عمل کا ماحولیاتی نظام اسے بہت زیادہ استعمال کرتا ہے۔ زیادہ تر نئے npm پیکجز قسم کی تعریفوں کے ساتھ بھیجے جاتے ہیں۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **تالیف کا مرحلہ** | چلانے سے پہلے`.ts`→`.js`مرتب کرنا ضروری ہے | ترقی کے لیے`ts-node`/`tsx`استعمال کریں۔  پیداوار کے لیے`tsc`|
| **سیکھنے کا وکر** | قسم کا نظام پیچیدہ ہو سکتا ہے (عام، مشروط اقسام) | بنیادی اقسام کے ساتھ شروع کریں؛ آہستہ آہستہ اعلی درجے کی خصوصیات کو اپنائیں |
| **ٹائپ ڈیفینیشن فائلز** | تمام npm پیکجز اقسام کے ساتھ نہیں بھیجے جاتے ہیں | DefinitelyTyped | سے`@types/package-name`انسٹال کریں۔
| ** مرتب اوقات** | بڑے پروجیکٹس ٹائپ چیک کرنے میں سست ہو سکتے ہیں۔ پروجیکٹ حوالہ جات استعمال کریں، `isolatedModules`، یا`swc`|
| **سلامتی کا غلط احساس** | قسمیں رن ٹائم کی درستگی کی ضمانت نہیں دیتی ہیں۔ رن ٹائم توثیق کے ساتھ جوڑیں (Zod, io-ts) |
---

## نحوی بنیادی باتیں
### بنیادی قسم کی تشریحات
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

### انٹرفیس اور اقسام
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

### عام
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

### اعلی درجے کی اقسام
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

### اقسام کے ساتھ اسینک
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

## اعلی درجے کی نحو اور نمونے۔
### اعلی درجے کی جنرکس
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

### ڈیکوریٹرز (TypeScript 5.0+ سٹینڈرڈ)
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

### قسم گارڈز اور تنگ کرنا
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

## ہم آہنگی اور ہم آہنگی
TypeScript JavaScript کے کنکرنسی ماڈل کو وراثت میں دیتا ہے لیکن async پیٹرن میں قسم کی حفاظت کا اضافہ کرتا ہے۔
### ٹائپ شدہ Async پیٹرنز
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ ڈائرکٹری کا ڈھانچہ
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

###`tsconfig.json`— ٹائپ اسکرپٹ کنفیگریشن
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

### تعمیر اور پیکیج کا انتظام
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

### Vitest کے ساتھ ٹیسٹنگ
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

### CI/CD پائپ لائن — GitHub ایکشنز
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

## اعلی درجے کی نحو اور نمونے۔
### اعلی درجے کی جنرکس
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

### ڈیکوریٹرز (TypeScript 5.0+)
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

### قسم گارڈز اور تنگ کرنا
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

## پروجیکٹ کنفیگریشن اور بلڈ سسٹم
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

### Vitest کے ساتھ ٹیسٹنگ
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

### Zod کے ساتھ رن ٹائم کی توثیق
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

## انٹرآپریبلٹی
### JavaScript لائبریریوں کا استعمال
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

## ڈیزائن پیٹرن
### رزلٹ پیٹرن
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

### ذخیرہ پیٹرن
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

## تعیناتی۔
### ڈاکر فائل
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

## ماحولیاتی نظام
### کلیدی ٹولز
| ٹول | مقصد |
|------|---------|
| **tsc** | ٹائپ اسکرپٹ کمپائلر (آفیشل) |
| **ts-node / tsx** | علیحدہ تالیف کے بغیر براہ راست ٹائپ اسکرپٹ چلائیں۔
| **swc** | الٹرا فاسٹ زنگ پر مبنی ٹائپ اسکرپٹ/جاوا اسکرپٹ کمپائلر |
| **ESLint + typescript-eslint** | قسم سے آگاہ قواعد کے ساتھ لنٹنگ |
| **زوڈ** | TypeScript inference کے ساتھ رن ٹائم قسم کی توثیق |
| **tsconfig.json** | TypeScript کنفیگریشن فائل |
### فریم ورکس (تمام ٹائپ اسکرپٹ-فرسٹ)
| فریم ورک | ڈومین |
|------------|---------|
| **کونیی** | مکمل خصوصیات والا فرنٹ اینڈ فریم ورک (TypeScript کی ضرورت ہے) |
| **Next.js** | ری ایکٹ میٹا فریم ورک (ٹائپ اسکرپٹ فرسٹ) |
| **NestJS** | انٹرپرائز بیک اینڈ فریم ورک (TypeScript-first) |
| **tRPC** | اینڈ ٹو اینڈ ٹائپ سیف APIs (صرف ٹائپ اسکرپٹ) |
| **پرزم** | Node.js کے لیے ٹائپ سیف ORM |
---

## ٹائپ اسکرپٹ کب استعمال کریں۔
| منظر نامہ | کیوں TypeScript | بہتر متبادل |
|------------|----------------------------|---------|
| بڑے جاوا اسکرپٹ پروجیکٹس | قسم کی حفاظت کیڑے کی پوری اقسام کو روکتی ہے | -- |
| ٹیم پروجیکٹس | اقسام مشترکہ معاہدے کے طور پر کام کرتی ہیں | -- |
| API کی ترقی | tRPC یا OpenAPI کے ساتھ اینڈ ٹو اینڈ ٹائپ سیفٹی | آسان REST APIs کے لیے جاوا جاوا |
| کوئی بھی نیا جاوا اسکرپٹ پروجیکٹ | TypeScript کو بعد میں شامل کرنے کی قیمت زیادہ ہے | سادہ جے ایس صرف چھوٹے اسکرپٹ کے لیے |
| لائبریریاں / این پی ایم پیکجز | صارفین کو خود بخود مکمل اور ٹائپ چیکنگ ملتی ہے | -- |
**انگوٹھے کا اصول**: اگر آپ کے JavaScript پروجیکٹ میں چند سو سے زیادہ لائنیں ہیں تو TypeScript استعمال کریں۔
---

## مصنوعی سوال و جواب
### Q1:`type`اور`interface`میں کیا فرق ہے، اور مجھے ہر ایک کب استعمال کرنا چاہیے؟
**A:** دونوں آبجیکٹ کی شکلوں کی وضاحت کرتے ہیں، لیکن ان میں مختلف صلاحیتیں ہیں۔ `interface`ڈیکلریشن انضمام کی حمایت کرتا ہے (ایک ہی نام کے انضمام کے ساتھ متعدد اعلانات)، وراثت کے لیے `extends`، اور عوامی APIs کے لیے محاوراتی انتخاب ہے۔ `type`یونین کی قسموں، چوراہوں کی اقسام، نقشہ بندی کی اقسام، مشروط اقسام، اور تمثیل کی لغوی قسموں کو سپورٹ کرتا ہے - کچھ بھی جدید۔ بہترین عمل: آبجیکٹ کی شکلوں اور عوامی APIs کے لیے`interface`استعمال کریں۔`type`یونینوں، یوٹیلیٹیز، اور پیچیدہ قسم کے آپریشنز کے لیے استعمال کریں۔
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

### Q2: جنرک کیسے کام کرتے ہیں، اور وہ کیوں اہم ہیں؟
**A:** جنرک آپ کو فنکشنز، کلاسز، اور قسمیں لکھنے دیتے ہیں جو قسم کی حفاظت کو برقرار رکھتے ہوئے کسی بھی قسم کے ساتھ کام کرتے ہیں۔`any`کے بجائے (جو قسم کی معلومات کھو دیتا ہے)، جنرک ان پٹ اور آؤٹ پٹ کی اقسام کے درمیان تعلق کو محفوظ رکھتے ہیں۔ وہ دوبارہ قابل استعمال، ٹائپ سیف کوڈ کی بنیاد ہیں۔
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

### Q3: افادیت کی اقسام کیا ہیں، اور مجھے کون سے جاننا چاہیے؟
**A:** TypeScript بلٹ ان یوٹیلیٹی اقسام فراہم کرتا ہے جو موجودہ اقسام کو تبدیل کرتی ہے۔ سب سے اہم:`Partial<T>`(تمام اختیاری)،`Required<T>`(تمام درکار)،`Pick<T, K>`(کیز کو منتخب کریں)،`Omit<T, K>`(کیز کو خارج کریں)،`Record<K, V>`(کلیدی قدر کا نقشہ)،`Exclude<T, U>`سے واپس کریں قسم)،`Awaited<T>`(اوپریپ وعدہ)۔ یہ سیکھیں - یہ حسب ضرورت قسم کے آپریشنز کی زیادہ تر ضرورت کو ختم کر دیتے ہیں۔
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

### Q4: میں async کوڈ کیسے ٹائپ کروں اور غلطیوں کو ٹائپ سیف طریقے سے کیسے ہینڈل کروں؟
**A:** Async فنکشن خود بخود`Promise<T>`واپس کر دیتے ہیں جہاں T واپسی کی قسم ہے۔ وعدے کو کھولنے کے لیے`await`استعمال کریں۔ غلطی سے نمٹنے کے لیے، TypeScript میں ٹائپ شدہ مستثنیات نہیں ہیں، لیکن آپ ٹائپ گارڈز اور نتائج کی قسمیں بنا سکتے ہیں۔ "رزلٹ پیٹرن" (رسٹ سے متاثر) کمپائل ٹائم ایرر ہینڈلنگ فراہم کرتا ہے۔
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

### Q5: ڈیکلریشن فائلز (.d.ts) کیا ہیں اور میں فریق ثالث کی اقسام کو کیسے استعمال کروں؟
**A:** ڈیکلریشن فائلیں JavaScript لائبریریوں کی ان اقسام کو بیان کرتی ہیں جن میں TypeScript کی قسمیں نہیں ہوتی ہیں۔ ان میں صرف قسم کی معلومات ہوتی ہیں (کوئی رن ٹائم کوڈ نہیں)۔ DefinitelyTyped:`npm install --save-dev @types/lodash`سے کمیونٹی کی دیکھ بھال کی قسمیں انسٹال کریں۔ اپنی لائبریریوں کے لیے،`package.json`میں ایک`types`فیلڈ شامل کریں یا`.d.ts`فائلوں کو اپنے ماخذ کے ساتھ شامل کریں۔ محیطی اعلانات کے لیے`declare module`استعمال کریں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ایک ٹائپ سیف ایونٹ ایمیٹر بنائیں
**مسئلہ کا بیان:** ٹائپ اسکرپٹ میں ایک عام، ٹائپ سیف ایونٹ ایمیٹر بنائیں جہاں ہر ایونٹ کا نام ایک مخصوص پے لوڈ کی قسم سے نقشہ بناتا ہے۔ کمپائلر کو کمپائل کے وقت غلط ایونٹ کے نام اور پے لوڈ کی قسمیں پکڑنی چاہئیں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ایک ایونٹ سسٹم کی ضرورت ہے جہاں: (1) ایونٹس کو ان کے پے لوڈ کی اقسام کے ساتھ بیان کیا گیا ہو، (2)`emit`صرف درست پے لوڈز کے ساتھ درست ایونٹ کے ناموں کو قبول کرتا ہے، (3)`on`صرف درست طریقے سے ٹائپ کیے گئے ہینڈلرز کے ساتھ ایونٹ کے درست ناموں کو قبول کرتا ہے۔ اس کے لیے ایونٹ میپ انٹرفیس پر میپ شدہ اقسام اور جنرک کی ضرورت ہوتی ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ایک`EventMap`قسم کی وضاحت کریں:`{ [eventName: string]: payloadType }`۔
- ایونٹ کے ناموں کو محدود کرنے کے لیے`keyof EventMap`استعمال کریں۔
- کسی مخصوص ایونٹ کے لیے پے لوڈ کی قسم حاصل کرنے کے لیے`EventMap[K]`استعمال کریں۔
- سننے والوں کو`Map<string, Function[]>`میں اسٹور کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- ٹائپ سیفٹی: کمپائلر کمپائل کے وقت غلط ایونٹ کے نام اور پے لوڈ کی غلط شکلیں پکڑتا ہے۔
-`on`آسان صفائی کے لیے ان سبسکرائب فنکشن واپس کرتا ہے۔
-`once`پہلی درخواست کے بعد سننے والے کو خودکار رکنیت ختم کرنے کے لیے لپیٹ دیتا ہے۔
- پیداوار کے لیے: `listenerCount`،`removeAllListeners`شامل کریں، اور منسوخی کے لیے`AbortSignal`استعمال کرنے پر غور کریں۔
### مسئلہ 2: ایک ٹائپ سیف ایس کیو ایل کوئری بلڈر کو لاگو کریں۔
**مسئلہ کا بیان:** ایک SQL استفسار بلڈر بنائیں جہاں کالم کے نام اور اقسام ٹائپ اسکرپٹ انٹرفیس سے اخذ کیے گئے ہوں۔ بلڈر کو کمپائل کے وقت غلط کالم کے ناموں اور ٹائپ کی مماثلتوں کو روکنا چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) کالم کے نام `keyof T`، (2) جہاں کالم کے مطابق شق کی قدریں ٹائپ کی گئی ہیں، (3) سوالات کی تعمیر کے لیے chainable API۔ اس کے لیے`Record<string, unknown>`کے ذریعے محدود جنرک کی ضرورت ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- کالم کے نام کی رکاوٹوں کے لیے`keyof T`استعمال کریں۔
- قدر کی قسم کی رکاوٹوں کے لیے`T[K]`استعمال کریں۔
- پیرامیٹرائزڈ سوالات کے ساتھ ایس کیو ایل سٹرنگ بنائیں (ایس کیو ایل انجیکشن کو روکیں)۔
- زنجیر کے قابل طریقے`this`واپس کرتے ہیں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- ایس کیو ایل انجیکشن کی روک تھام: تمام قدریں پیرامیٹرائزڈ سوالات (`$1`,`$2`) سے گزرتی ہیں، کبھی انٹرپول نہیں ہوتی ہیں۔
- قسم کی حفاظت: کالم کے نام اور قیمت کی اقسام کو مرتب کرنے کے وقت چیک کیا جاتا ہے۔
- توسیع پذیری: اسی پیٹرن پر عمل کرتے ہوئے `join`، `groupBy`، `having`، `insert`،`update`طریقے شامل کریں۔
- پیداوار:`kysely`یا`drizzle-orm`استعمال کریں - وہ اس قسم کی حفاظت کو مکمل SQL کوریج کے ساتھ فراہم کرتے ہیں۔
### مسئلہ 3: قسم کی حفاظت کے ساتھ ایک محدود ریاستی مشین کو لاگو کریں۔
**مسئلہ کا بیان:** ایک ٹائپ سیف فائنائٹ سٹیٹ مشین بنائیں جہاں مرتب وقت پر درست ٹرانزیشنز نافذ ہوں۔ ہر ریاست میں داخلے/خارج کی کارروائیاں ہو سکتی ہیں، اور مشین کو موجودہ حالت کو ٹریک کرنا چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) اقسام کے طور پر بیان کردہ ریاستیں اور واقعات، (2) قسم کی سطح پر درست ٹرانزیشنز، (3) کمپائلر غلط ٹرانزیشن کو روکتا ہے، (4) کال بیکس کے ساتھ رن ٹائم اسٹیٹ ٹریکنگ۔ اس کے لیے میپ شدہ اقسام اور مشروط اقسام درکار ہیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ایک`TransitionMap`:`{ [State]: { [Event]: NextState } }`کی وضاحت کریں۔
- موجودہ حالت کی بنیاد پر`send(event)`کو محدود کرنے کے لیے جنرک استعمال کریں۔
- متغیر کے ساتھ رن ٹائم پر ریاست کو ٹریک کریں۔
- فی ریاست اندراج / خارجی کال بیکس کی حمایت کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- رن ٹائم سیفٹی:`send`غلط ٹرانزیشن پر پھینک دیتا ہے۔
- قسم کی حفاظت:`EventsFor`قسم کمپائل کے وقت فی ریاست درست واقعات کو نکالتی ہے۔
- ٹرانزیشن پر داخلے/باہر نکلنے والے کال بیکس خود بخود فائر ہو جاتے ہیں۔
- پروڈکشن کے لیے:`xstate`استعمال کریں — یہ بصری ڈیبگنگ، درجہ بندی کی حالتوں، محافظوں، اور اعمال کے ساتھ ایک مکمل ریاستی مشین لائبریری فراہم کرتا ہے۔
---

## خلاصہ
TypeScript جاوا اسکرپٹ ہے جو معمولی اسکرپٹ سے ہٹ کر کسی بھی چیز کے لیے درست کیا جاتا ہے۔ یہ ایک طاقتور قسم کا نظام شامل کرتا ہے جو کیڑے کو جلد پکڑتا ہے، ٹولنگ کو بہتر بناتا ہے، اور دستاویزات کے کوڈ -- یہ سب کچھ معیاری JavaScript پر مرتب کرتے ہوئے جو کہیں بھی چلتا ہے۔ سیکھنے کا منحنی خطوط نرم ہے (آپ کم سے کم اقسام سے شروع کر سکتے ہیں) لیکن گہرائی بہت وسیع ہے (ٹائپ سسٹم ٹورنگ مکمل ہے)۔ جدید JavaScript کی ترقی کے لیے، TypeScript صنعت کا معیار بن گیا ہے۔