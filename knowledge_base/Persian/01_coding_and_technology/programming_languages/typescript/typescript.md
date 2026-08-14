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
TypeScript یک ابرمجموعه جاوا اسکریپت تایپ شده است که توسط مایکروسافت (به رهبری آندرس هیلسبرگ) توسعه یافته و اولین بار در سال 2012 منتشر شد. این نوع حاشیه نویسی اختیاری، رابط ها، ژنریک ها و ویژگی های سیستم نوع پیشرفته را به جاوا اسکریپت اضافه می کند - سپس به جاوا اسکریپت ساده که در هر جایی که جاوا اسکریپت اجرا می شود، کامپایل می شود. TypeScript یک زبان یا زمان اجرا جداگانه نیست. این جاوا اسکریپت با جستجوگر نوع است.
TypeScript به استانداردی برای توسعه جاوا اسکریپت در مقیاس بزرگ تبدیل شده است. React، Angular، VS Code، Deno و اکثر پروژه های اصلی جاوا اسکریپت منبع باز با TypeScript نوشته شده اند. اگر یک پروژه جاوا اسکریپت جدید با هر اندازه قابل توجهی را شروع می کنید، TypeScript پیش فرض توصیه شده است.
---

## چرا TypeScript مهم است
- ** اشکالات را در زمان کامپایل پیدا می کند **: خطاهای نوع قبل از اجرای کد پیدا می شود - در حال تولید نیست.
- **پشتیبانی بهتر از IDE**: تکمیل خودکار، رفتن به تعریف، refactoring و مستندات درون خطی همه به طور چشمگیری بهبود می یابند.
- **کد خود مستندسازی**: انواع به عنوان اسنادی عمل می کنند که به روز می مانند.
- ** 100% جاوا اسکریپت سازگار **: هر جاوا اسکریپت معتبر TypeScript معتبر است. می توانید آن را به تدریج اتخاذ کنید.
- **سیستم نوع پیشرفته**: انواع اتحادیه، انواع تقاطع، انواع شرطی، انواع نقشه برداری، انواع تحت اللفظی الگو - سیستم نوع به اندازه کافی گویا برای مدل سازی منطق دامنه پیچیده است.
- ** پذیرش صنعت **: Angular به آن نیاز دارد. اکوسیستم React به طور قاطع از آن استفاده می کند. اکثر بسته های جدید npm با تعاریف نوع ارسال می شوند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **مرحله تالیف** | قبل از اجرا باید`.ts`→`.js`را کامپایل کنید | برای توسعه از`ts-node`/`tsx`استفاده کنید. `tsc`برای تولید |
| **منحنی یادگیری** | سیستم نوع می تواند پیچیده باشد (عمومی، انواع مشروط) | با انواع پایه شروع کنید. به تدریج ویژگی های پیشرفته را اتخاذ کنید |
| **فایل های تعریف تایپ** | همه بسته‌های npm با انواع | ارسال نمی‌شوند`@types/package-name`را از DefinitelyTyped | نصب کنید
| **زمان کامپایل** | بررسی تایپ پروژه های بزرگ می تواند کند باشد | استفاده از منابع پروژه، `isolatedModules`، یا`swc`|
| **احساس امنیت کاذب** | انواع صحت زمان اجرا را تضمین نمی کنند | ترکیب با اعتبار سنجی زمان اجرا (Zod، io-ts) |
---

## اصول نحو
### حاشیه نویسی نوع پایه
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

### رابط ها و انواع
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

### ژنریک
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

### انواع پیشرفته
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

### همگام با انواع
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

## نحو و الگوهای پیشرفته
### ژنریک پیشرفته
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

### دکوراتورها (TypeScript 5.0+ استاندارد)
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

### نوع محافظ و باریک کردن
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

## همزمانی و موازی
TypeScript مدل همزمانی جاوا اسکریپت را به ارث می برد اما ایمنی نوع را به الگوهای همگام اضافه می کند.
### تایپ الگوهای همگام
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

## پیکربندی پروژه و سیستم ساخت
### ساختار فهرست پروژه
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

###`tsconfig.json`- پیکربندی TypeScript
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

### مدیریت ساخت و بسته
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

### تست با Vitest
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

### خط لوله CI/CD — اقدامات GitHub
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

## نحو و الگوهای پیشرفته
### ژنریک پیشرفته
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

### دکوراتورها (TypeScript 5.0+)
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

### نوع محافظ و باریک کردن
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

## پیکربندی پروژه و ساخت سیستم
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

### تست با Vitest
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

### اعتبار سنجی زمان اجرا با Zod
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

## قابلیت همکاری
### با استفاده از کتابخانه های جاوا اسکریپت
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

## الگوهای طراحی
### الگوی نتیجه
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

### الگوی مخزن
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

## استقرار
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

## اکوسیستم
### ابزارهای کلیدی
| ابزار | هدف |
|------|---------|
| **tsc** | کامپایلر TypeScript (رسمی) |
| **ts-node / tsx** | TypeScript را مستقیماً بدون کامپایل جداگانه | اجرا کنید
| **swc** | کامپایلر TypeScript/JavaScript بسیار سریع مبتنی بر Rust |
| **ESLint + typescript-eslint** | پرده زدن با قوانین نوع آگاه |
| **زود** | اعتبار سنجی نوع زمان اجرا با استنتاج TypeScript |
| **tsconfig.json** | فایل پیکربندی TypeScript |
### چارچوب (همه TypeScript-First)
| چارچوب | دامنه |
|-----------|--------|
| **زاویه** | فریمورک ظاهری با امکانات کامل (نیاز به TypeScript دارد) |
| **Next.js** | متا فریمورک React (TypeScript-first) |
| **NestJS** | چارچوب باطن سازمانی (TypeScript-first) |
| **tRPC** | API های سرتاسر typeafe (فقط تایپ اسکریپت) |
| **پریسما** | نوع ایمن ORM برای Node.js |
---

## چه زمانی از TypeScript استفاده کنیم
| سناریو | چرا TypeScript | جایگزین بهتر |
|----------|--------------|-------------------|
| پروژه های بزرگ جاوا اسکریپت | ایمنی نوع از کل دسته بندی اشکالات جلوگیری می کند | -- |
| پروژه های تیمی | انواع به عنوان یک قرارداد مشترک خدمت می کنند | -- |
| توسعه API | ایمنی از نوع سرتاسر با tRPC یا OpenAPI | برو، جاوا برای REST API های ساده تر |
| هر پروژه جاوا اسکریپت جدید | هزینه اضافه کردن TypeScript بعداً زیاد است | JS ساده فقط برای اسکریپت های کوچک |
| کتابخانه ها / بسته های npm | مصرف کنندگان تکمیل خودکار و بررسی تایپ | -- |
**قاعده سرانگشتی**: اگر پروژه جاوا اسکریپت شما بیش از چند صد خط دارد، از TypeScript استفاده کنید.
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین`type`و`interface`چیست و چه زمانی باید از هر کدام استفاده کنم؟
**A:** هر دو شکل شی را تعریف می کنند، اما قابلیت های متفاوتی دارند. `interface`از ادغام اعلامیه ها (ادغام چند اعلان با همین نام)،`extends`برای ارث بردن، و انتخاب اصطلاحی برای API های عمومی است. `type`از انواع اتحاد، انواع تقاطع، انواع نقشه‌برداری شده، انواع شرطی و انواع تحت اللفظی الگو پشتیبانی می‌کند - هر چیزی پیشرفته. بهترین روش: از`interface`برای اشکال شی و APIهای عمومی استفاده کنید. از`type`برای اتحادیه ها، برنامه های کاربردی و عملیات نوع پیچیده استفاده کنید.
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

### Q2: ژنریک ها چگونه کار می کنند و چرا مهم هستند؟
**A:** Generics به شما امکان می دهد توابع، کلاس ها و انواعی را بنویسید که با هر نوع کار می کنند و در عین حال ایمنی نوع را حفظ می کنند. به جای`any`(که اطلاعات نوع را از دست می دهد)، ژنریک ها رابطه بین انواع ورودی و خروجی را حفظ می کنند. آنها پایه و اساس کد قابل استفاده مجدد و ایمن هستند.
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

### Q3: انواع ابزار چیست، و کدام یک را باید بدانم؟
**A:** TypeScript انواع ابزار داخلی را فراهم می کند که انواع موجود را تغییر می دهد. مهمترین آنها:`Partial<T>`(همه اختیاری)،`Required<T>`(همه موارد مورد نیاز)،`Pick<T, K>`(کلیدهای انتخاب)،`Omit<T, K>`(کلیدها حذف می‌شوند)،`Record<K, V>`(نقشه کلید-مقدار)، `Exclude<T, U>`،`Exclude<T, U>`(عملکرد بازگرداندن)`Awaited<T>`(وعده را باز کنید). اینها را بیاموزید - آنها بیشتر نیاز به عملیات نوع سفارشی را از بین می برند.
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

### Q4: چگونه می توانم کد async را تایپ کنم و خطاها را به روش ایمن تایپ کنم؟
**A:** توابع Async به طور خودکار`Promise<T>`را برمی گرداند که در آن T نوع برگشتی است. برای باز کردن Promise از`await`استفاده کنید. برای رسیدگی به خطا، TypeScript استثناهای تایپ شده ندارد، اما می توانید محافظ نوع و انواع نتیجه ایجاد کنید. "الگوی نتیجه" (الهام گرفته شده از Rust) مدیریت خطا در زمان کامپایل را ارائه می دهد.
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

### Q5: فایل های اعلامیه (.d.ts) چیست و چگونه از انواع شخص ثالث استفاده کنم؟
**A:** فایل های اعلامیه انواع کتابخانه های جاوا اسکریپت را که دارای انواع TypeScript داخلی نیستند، توصیف می کنند. آنها فقط حاوی اطلاعات نوع هستند (بدون کد زمان اجرا). انواع نگهداری شده توسط انجمن را از DefinitelyTyped نصب کنید: `npm install --save-dev @types/lodash`. برای کتابخانه های خود، یک فیلد`types`در`package.json`اضافه کنید یا فایل های`.d.ts`را در کنار منبع خود قرار دهید. از`declare module`برای اعلان های محیطی استفاده کنید.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک Emitter رویداد نوع ایمن بسازید
**بیانیه مشکل:** یک انتشار دهنده رویداد عمومی و ایمن در TypeScript ایجاد کنید که در آن نام هر رویداد به یک نوع بار خاص نگاشت می شود. کامپایلر باید در زمان کامپایل نام رویدادها و انواع بارگذاری نادرست را بگیرد.
** مرحله 1 - مشکل را درک کنید:**
ما به یک سیستم رویداد نیاز داریم که در آن: (1) رویدادها با انواع بارگذاری خود تعریف شوند، (2)`emit`فقط نام رویدادهای معتبر را با بارهای صحیح بپذیرد، (3)`on`فقط نام رویدادهای معتبر را با کنترل‌کننده‌های درست تایپ شده بپذیرد. این نیاز به انواع نقشه‌برداری شده و کلیات روی رابط نقشه رویداد دارد.
** مرحله 2 - شناسایی رویکرد: **
- نوع`EventMap`را تعریف کنید: `{ [eventName: string]: payloadType }`.
- از`keyof EventMap`برای محدود کردن نام رویدادها استفاده کنید.
- از`EventMap[K]`برای دریافت نوع بار برای یک رویداد خاص استفاده کنید.
- شنوندگان را در`Map<string, Function[]>`ذخیره کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی نوع: کامپایلر در زمان کامپایل نام رویدادها و اشکال اشتباه بار بار را می گیرد.
-`on`یک تابع لغو اشتراک را برای پاکسازی راحت برمی گرداند.
-`once`شنونده را می‌پیچد تا پس از اولین فراخوان، اشتراک خود را لغو کند.
- برای تولید: `listenerCount`،`removeAllListeners`را اضافه کنید و از`AbortSignal`برای لغو استفاده کنید.
### مشکل 2: یک Type-Safe Query Builder SQL را پیاده سازی کنید
**بیانیه مشکل:** یک سازنده کوئری SQL بسازید که در آن نام و انواع ستون ها از یک رابط TypeScript مشتق شده باشد. سازنده باید از نام‌های ستون نامعتبر جلوگیری کند و از عدم تطابق نوع در زمان کامپایل جلوگیری کند.
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) نام ستون‌ها محدود به `keyof T`، (2) WHERE مقادیر بند طبق ستون تایپ شوند، (3) API زنجیره‌ای برای ساخت کوئری‌ها. این به ژنریک های محدود شده توسط`Record<string, unknown>`نیاز دارد.
** مرحله 2 - شناسایی رویکرد: **
- از`keyof T`برای محدودیت های نام ستون استفاده کنید.
- از`T[K]`برای محدودیت های نوع مقدار استفاده کنید.
- ساخت رشته SQL با پرس و جوهای پارامتری (جلوگیری از تزریق SQL).
- روش های زنجیره ای`this`را برمی گرداند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- جلوگیری از تزریق SQL: همه مقادیر از طریق پرس و جوهای پارامتری (`$1`، `$2`)، هرگز درون یابی نمی شوند.
- ایمنی نوع: نام ستون ها و انواع مقادیر در زمان کامپایل بررسی می شوند.
- توسعه پذیری: روش های `join`، `groupBy`، `having`، `insert`،`update`را با همان الگو اضافه کنید.
- تولید: از`kysely`یا`drizzle-orm`استفاده کنید - آنها این نوع ایمنی را با پوشش کامل SQL ارائه می کنند.
### مشکل 3: یک ماشین حالت محدود با نوع ایمنی پیاده سازی کنید
**بیانیه مشکل:** یک ماشین حالت محدود با نوع ایمن ایجاد کنید که در آن انتقال های معتبر در زمان کامپایل اجرا شوند. هر حالت می تواند اقدامات ورود/خروج داشته باشد و ماشین باید وضعیت فعلی را ردیابی کند.
** مرحله 1 - مشکل را درک کنید:**
ما به موارد زیر نیاز داریم: (1) حالت ها و رویدادهایی که به عنوان انواع تعریف شده اند، (2) انتقال های معتبر که در سطح نوع نگاشت شده اند، (3) کامپایلر از انتقال نامعتبر جلوگیری می کند، (4) ردیابی وضعیت زمان اجرا با تماس های برگشتی. این به انواع نقشه‌برداری شده و انواع مشروط نیاز دارد.
** مرحله 2 - شناسایی رویکرد: **
-`TransitionMap`را تعریف کنید: `{ [State]: { [Event]: NextState } }`.
- از ژنریک برای محدود کردن`send(event)`بر اساس وضعیت فعلی استفاده کنید.
- وضعیت را در زمان اجرا با یک متغیر پیگیری کنید.
- پشتیبانی از تماس های ورودی/خروجی در هر ایالت.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی در زمان اجرا:`send`روی انتقال های نامعتبر پرتاب می کند.
- ایمنی نوع: نوع`EventsFor`رویدادهای معتبر را در هر حالت در زمان کامپایل استخراج می کند.
- تماس های ورودی/خروجی به طور خودکار در انتقال ها شلیک می شوند.
- برای تولید: از`xstate`استفاده کنید - یک کتابخانه ماشین حالت کامل با اشکال زدایی بصری، حالت های سلسله مراتبی، محافظ ها و اقدامات ارائه می دهد.
---

## خلاصه
TypeScript جاوا اسکریپتی است که برای هر چیزی فراتر از اسکریپت های بی اهمیت درست انجام می شود. این سیستم یک نوع قدرتمند را اضافه می کند که اشکالات را زود تشخیص می دهد، ابزارها و کد اسناد را بهبود می بخشد - همه اینها در حالی که به جاوا اسکریپت استانداردی که در هر جایی اجرا می شود کامپایل می شود. منحنی یادگیری ملایم است (شما می توانید با حداقل انواع شروع کنید) اما عمق آن بسیار زیاد است (سیستم نوع کاملاً تورینگ است). برای توسعه مدرن جاوا اسکریپت، TypeScript به استاندارد صنعتی تبدیل شده است.