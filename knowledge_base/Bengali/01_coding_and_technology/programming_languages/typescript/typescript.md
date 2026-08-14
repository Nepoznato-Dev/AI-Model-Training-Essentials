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

# টাইপস্ক্রিপ্ট
টাইপস্ক্রিপ্ট হল জাভাস্ক্রিপ্টের একটি স্ট্যাটিক্যালি টাইপ করা সুপারসেট যা মাইক্রোসফ্ট (অ্যান্ডার্স হেজলবার্গের নেতৃত্বে) দ্বারা তৈরি করা হয়েছিল এবং প্রথম 2012 সালে প্রকাশিত হয়েছিল। এটি জাভাস্ক্রিপ্টে ঐচ্ছিক টাইপ টীকা, ইন্টারফেস, জেনেরিক এবং উন্নত টাইপ-সিস্টেম বৈশিষ্ট্যগুলি যোগ করে — তারপর প্লেইন জাভাস্ক্রিপ্ট যেখানে চালায় সেখানে কম্পাইল করে। TypeScript একটি পৃথক ভাষা বা রানটাইম নয়; এটি একটি টাইপ চেকার সহ জাভাস্ক্রিপ্ট।
টাইপস্ক্রিপ্ট বড় আকারের জাভাস্ক্রিপ্ট বিকাশের জন্য আদর্শ হয়ে উঠেছে। প্রতিক্রিয়া, কৌণিক, ভিএস কোড, ডেনো এবং বেশিরভাগ প্রধান ওপেন-সোর্স জাভাস্ক্রিপ্ট প্রকল্পগুলি টাইপস্ক্রিপ্টে লেখা হয়। আপনি যদি কোনো উল্লেখযোগ্য আকারের একটি নতুন জাভাস্ক্রিপ্ট প্রকল্প শুরু করেন, টাইপস্ক্রিপ্ট প্রস্তাবিত ডিফল্ট।
---

## টাইপস্ক্রিপ্ট কেন গুরুত্বপূর্ণ
- **সংকলনের সময় বাগ ধরা পড়ে**: কোড চলার আগে টাইপ ত্রুটি পাওয়া যায় — উৎপাদনে নয়।
- **আরো ভালো আইডিই সমর্থন**: স্বয়ংসম্পূর্ণ, গো-টু-ডেফিনিশন, রিফ্যাক্টরিং এবং ইনলাইন ডকুমেন্টেশন সবই নাটকীয়ভাবে উন্নতি করে।
- **স্ব-ডকুমেন্টিং কোড**: প্রকারগুলি ডকুমেন্টেশন হিসাবে কাজ করে যা আপ টু ডেট থাকে।
- **100% জাভাস্ক্রিপ্ট সামঞ্জস্যপূর্ণ**: যেকোনো বৈধ জাভাস্ক্রিপ্ট বৈধ টাইপস্ক্রিপ্ট। আপনি ধীরে ধীরে এটি গ্রহণ করতে পারেন।
- **অ্যাডভান্সড টাইপ সিস্টেম**: ইউনিয়নের ধরন, ইন্টারসেকশন প্রকার, কন্ডিশনাল টাইপ, ম্যাপ করা প্রকার, টেমপ্লেট আক্ষরিক প্রকার — টাইপ সিস্টেমটি জটিল ডোমেন লজিক মডেল করার জন্য যথেষ্ট অভিব্যক্তিপূর্ণ।
- **শিল্প গ্রহণ**: কৌণিক এটি প্রয়োজন; প্রতিক্রিয়া ইকোসিস্টেম অপ্রতিরোধ্যভাবে এটি ব্যবহার করে; বেশিরভাগ নতুন এনপিএম প্যাকেজ টাইপ সংজ্ঞা সহ পাঠানো হয়।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **সংকলন ধাপ** | চালানোর আগে অবশ্যই`.ts`→`.js`কম্পাইল করতে হবে | উন্নয়নের জন্য`ts-node`/`tsx`ব্যবহার করুন;  উৎপাদনের জন্য`tsc`|
| **লার্নিং কার্ভ** | টাইপ সিস্টেম জটিল হতে পারে (জেনারিক, শর্তাধীন প্রকার) | মৌলিক ধরনের দিয়ে শুরু করুন; ধীরে ধীরে উন্নত বৈশিষ্ট্য গ্রহণ করুন |
| **টাইপ সংজ্ঞা ফাইল** | সব এনপিএম প্যাকেজ টাইপের সাথে পাঠানো হয় না DefinitelyTyped থেকে`@types/package-name`ইনস্টল করুন |
| **সময় কম্পাইল** | বড় প্রকল্প টাইপ-চেক করতে ধীর হতে পারে | প্রকল্পের রেফারেন্স ব্যবহার করুন,`isolatedModules`, বা`swc`|
| **মিথ্যা নিরাপত্তাবোধ** | প্রকারগুলি রানটাইম সঠিকতার গ্যারান্টি দেয় না | রানটাইম যাচাইকরণের সাথে একত্রিত করুন (Zod, io-ts) |
---

## সিনট্যাক্স মৌলিক
### বেসিক টাইপ টীকা
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

### ইন্টারফেস এবং প্রকার
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

### জেনেরিক
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

### উন্নত প্রকার
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

### প্রকারের সাথে অ্যাসিঙ্ক করুন
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### উন্নত জেনেরিক
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

### ডেকোরেটর (টাইপস্ক্রিপ্ট 5.0+ স্ট্যান্ডার্ড)
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

### টাইপ গার্ড এবং সংকীর্ণ
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

## সামঞ্জস্য এবং সমান্তরালতা
TypeScript JavaScript-এর একযোগে মডেলের উত্তরাধিকারী হয় কিন্তু অ্যাসিঙ্ক প্যাটার্নে টাইপ নিরাপত্তা যোগ করে।
### টাইপ করা অ্যাসিঙ্ক প্যাটার্ন
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রজেক্ট ডাইরেক্টরি স্ট্রাকচার
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

###`tsconfig.json`— টাইপস্ক্রিপ্ট কনফিগারেশন
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

### বিল্ড এবং প্যাকেজ ব্যবস্থাপনা
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

### ভিটেস্ট দিয়ে পরীক্ষা করা হচ্ছে
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

### CI/CD পাইপলাইন — গিটহাব অ্যাকশন
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### উন্নত জেনেরিক
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

### ডেকোরেটর (TypeScript 5.0+)
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

### টাইপ গার্ড এবং সংকীর্ণ
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
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

### ভিটেস্ট দিয়ে পরীক্ষা করা হচ্ছে
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

### Zod এর সাথে রানটাইম বৈধতা
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

## ইন্টারঅপারেবিলিটি
### জাভাস্ক্রিপ্ট লাইব্রেরি ব্যবহার করা
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

## ডিজাইন প্যাটার্ন
### ফলাফল প্যাটার্ন
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

### ভান্ডার প্যাটার্ন
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

## স্থাপনা
### ডকারফাইল
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

## ইকোসিস্টেম
### মূল টুল
| টুল | উদ্দেশ্য |
|------|---------|
| **tsc** | টাইপস্ক্রিপ্ট কম্পাইলার (অফিসিয়াল) |
| **ts-নোড / tsx** | পৃথক সংকলন ছাড়াই সরাসরি TypeScript চালান |
| **swc** | অতি-দ্রুত মরিচা-ভিত্তিক টাইপস্ক্রিপ্ট/জাভাস্ক্রিপ্ট কম্পাইলার |
| **ESLint + typescript-eslint** | টাইপ-সচেতন নিয়মের সাথে লিন্টিং |
| **জোড** | TypeScript অনুমান সহ রানটাইম প্রকারের বৈধতা |
| **tsconfig.json** | টাইপস্ক্রিপ্ট কনফিগারেশন ফাইল |
### ফ্রেমওয়ার্ক (সমস্ত টাইপস্ক্রিপ্ট-প্রথম)
| ফ্রেমওয়ার্ক | ডোমেন |
|------------|---------|
| **কৌণিক** | সম্পূর্ণ বৈশিষ্ট্যযুক্ত ফ্রন্টএন্ড ফ্রেমওয়ার্ক (টাইপস্ক্রিপ্ট প্রয়োজন) |
| **পরবর্তী.js** | প্রতিক্রিয়া মেটা-ফ্রেমওয়ার্ক (টাইপস্ক্রিপ্ট-প্রথম) |
| **NestJS** | এন্টারপ্রাইজ ব্যাকএন্ড ফ্রেমওয়ার্ক (টাইপস্ক্রিপ্ট-প্রথম) |
| **tRPC** | এন্ড-টু-এন্ড টাইপসেফ API (শুধুমাত্র টাইপস্ক্রিপ্ট) |
| **প্রিজমা** | Node.js এর জন্য টাইপ-সেফ ORM |
---

## কখন টাইপস্ক্রিপ্ট ব্যবহার করবেন
| দৃশ্যকল্প | কেন টাইপস্ক্রিপ্ট | ভাল বিকল্প |
|------------|---------------|---------|
| বড় জাভাস্ক্রিপ্ট প্রকল্প | টাইপ নিরাপত্তা বাগগুলির সম্পূর্ণ বিভাগকে বাধা দেয় | -- |
| দল প্রকল্প | প্রকারগুলি একটি ভাগ করা চুক্তি হিসাবে পরিবেশন করে | -- |
| API উন্নয়ন | tRPC বা OpenAPI এর সাথে এন্ড-টু-এন্ড টাইপ নিরাপত্তা | সহজ REST API-এর জন্য যান, জাভা |
| যেকোনো নতুন জাভাস্ক্রিপ্ট প্রকল্প | পরে TypeScript যোগ করার খরচ বেশি | শুধুমাত্র ছোট স্ক্রিপ্টের জন্য প্লেইন JS |
| লাইব্রেরি / npm প্যাকেজ | ভোক্তারা স্বয়ংসম্পূর্ণ এবং টাইপ চেকিং পান | -- |
**আঙুলের নিয়ম**: যদি আপনার জাভাস্ক্রিপ্ট প্রজেক্টে কয়েকশোর বেশি লাইন থাকে, তাহলে TypeScript ব্যবহার করুন।
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1:`type`এবং`interface`এর মধ্যে পার্থক্য কী এবং আমার প্রতিটি কখন ব্যবহার করা উচিত?
**A:** উভয়ই বস্তুর আকারকে সংজ্ঞায়িত করে, কিন্তু তাদের বিভিন্ন ক্ষমতা রয়েছে। `interface`ঘোষণা একত্রীকরণ সমর্থন করে (একই নামের একত্রীকরণের একাধিক ঘোষণা), উত্তরাধিকারের জন্য `extends`, এবং সর্বজনীন API-এর জন্য মূর্তিপূর্ণ পছন্দ। `type`ইউনিয়ন প্রকার, ছেদ প্রকার, ম্যাপ করা প্রকার, শর্তাধীন প্রকার, এবং টেমপ্লেট আক্ষরিক প্রকারগুলিকে সমর্থন করে — যেকোনও উন্নত। সর্বোত্তম অনুশীলন: বস্তুর আকার এবং সর্বজনীন API-এর জন্য`interface`ব্যবহার করুন; ইউনিয়ন, ইউটিলিটি এবং জটিল ধরনের অপারেশনের জন্য`type`ব্যবহার করুন।
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

### প্রশ্ন 2: জেনেরিক কীভাবে কাজ করে এবং কেন তারা গুরুত্বপূর্ণ?
**A:** জেনেরিক আপনাকে ফাংশন, ক্লাস এবং প্রকারগুলি লিখতে দেয় যা টাইপ নিরাপত্তা বজায় রেখে যেকোন ধরণের সাথে কাজ করে।`any`(যা টাইপ তথ্য হারায়) এর পরিবর্তে জেনেরিক ইনপুট এবং আউটপুট প্রকারের মধ্যে সম্পর্ক রক্ষা করে। তারা পুনঃব্যবহারযোগ্য, টাইপ-নিরাপদ কোডের ভিত্তি।
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

### প্রশ্ন 3: ইউটিলিটি কি কি এবং কোনটি আমার জানা উচিত?
**A:** TypeScript বিল্ট-ইন ইউটিলিটি প্রকার সরবরাহ করে যা বিদ্যমান প্রকারগুলিকে রূপান্তরিত করে। সবচেয়ে গুরুত্বপূর্ণ:`Partial<T>`(সমস্ত ঐচ্ছিক),`Required<T>`(সমস্ত প্রয়োজনীয়),`Pick<T, K>`(কীগুলি নির্বাচন করুন),`Omit<T, K>`(কীগুলি বাদ দিন),`Record<K, V>`(কী-মান মানচিত্র),`Exclude<T, U>`থেকে আনুন (`Exclude<T, U>`) ফাংশন আনুন (`Exclude<T, U>`) টাইপ),`Awaited<T>`(আনর্যাপ প্রমিস)। এগুলি শিখুন - এগুলি কাস্টম টাইপ অপারেশনের জন্য সবচেয়ে বেশি প্রয়োজন বাদ দেয়।
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

### প্রশ্ন 4: আমি কীভাবে অ্যাসিঙ্ক কোড টাইপ করব এবং টাইপ-নিরাপদ উপায়ে ত্রুটিগুলি পরিচালনা করব?
**A:** Async ফাংশন স্বয়ংক্রিয়ভাবে`Promise<T>`রিটার্ন করে যেখানে T হল রিটার্ন টাইপ। প্রতিশ্রুতি খুলতে`await`ব্যবহার করুন। ত্রুটি পরিচালনার জন্য, টাইপস্ক্রিপ্টে টাইপ করা ব্যতিক্রম নেই, তবে আপনি টাইপ গার্ড এবং ফলাফলের ধরন তৈরি করতে পারেন। "ফলাফল প্যাটার্ন" (মরিচা দ্বারা অনুপ্রাণিত) কম্পাইল-টাইম ত্রুটি হ্যান্ডলিং প্রদান করে।
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

### প্রশ্ন 5: ঘোষণা ফাইল (.d.ts) কি এবং কিভাবে আমি তৃতীয় পক্ষের ধরন ব্যবহার করব?
**A:** ঘোষণা ফাইলগুলি জাভাস্ক্রিপ্ট লাইব্রেরির প্রকারগুলি বর্ণনা করে যেগুলিতে অন্তর্নির্মিত টাইপস্ক্রিপ্ট প্রকার নেই৷ তারা শুধুমাত্র টাইপ তথ্য ধারণ করে (কোন রানটাইম কোড নেই)। DefinitelyTyped:`npm install --save-dev @types/lodash`থেকে সম্প্রদায়-রক্ষণাবেক্ষণ করা প্রকারগুলি ইনস্টল করুন। আপনার নিজের লাইব্রেরির জন্য, `package.json`-এ একটি`types`ক্ষেত্র যোগ করুন বা আপনার উত্সের পাশাপাশি`.d.ts`ফাইলগুলি অন্তর্ভুক্ত করুন৷ পরিবেষ্টিত ঘোষণার জন্য`declare module`ব্যবহার করুন।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি টাইপ-সেফ ইভেন্ট ইমিটার তৈরি করুন
**সমস্যা বিবৃতি:** TypeScript-এ একটি জেনেরিক, টাইপ-সেফ ইভেন্ট ইমিটার তৈরি করুন যেখানে প্রতিটি ইভেন্টের নাম একটি নির্দিষ্ট পেলোড টাইপের সাথে ম্যাপ করে। কম্পাইলারকে কম্পাইলের সময় ভুল ইভেন্টের নাম এবং পেলোডের ধরন ধরতে হবে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের একটি ইভেন্ট সিস্টেম দরকার যেখানে: (1) ইভেন্টগুলি তাদের পেলোডের ধরন দিয়ে সংজ্ঞায়িত করা হয়, (2)`emit`শুধুমাত্র সঠিক পেলোড সহ বৈধ ইভেন্টের নাম গ্রহণ করে, (3)`on`শুধুমাত্র সঠিকভাবে টাইপ করা হ্যান্ডলারের সাথে বৈধ ইভেন্টের নাম গ্রহণ করে৷ এর জন্য একটি ইভেন্ট ম্যাপ ইন্টারফেসে ম্যাপ করা প্রকার এবং জেনেরিক প্রয়োজন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি`EventMap`প্রকার সংজ্ঞায়িত করুন: `{ [eventName: string]: payloadType }`।
- ইভেন্টের নাম সীমাবদ্ধ করতে`keyof EventMap`ব্যবহার করুন।
- একটি নির্দিষ্ট ইভেন্টের জন্য পেলোড টাইপ পেতে`EventMap[K]`ব্যবহার করুন।
- একটি`Map<string, Function[]>`এ শ্রোতাদের সঞ্চয় করুন৷
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- টাইপ নিরাপত্তা: কম্পাইলার কম্পাইলের সময় ভুল ইভেন্টের নাম এবং ভুল পেলোড আকারগুলি ধরে।
-`on`সুবিধাজনক ক্লিনআপের জন্য একটি আনসাবস্ক্রাইব ফাংশন প্রদান করে।
-`once`প্রথম আহ্বানের পরে শ্রোতাকে স্বতঃ-আনসাবস্ক্রাইব করার জন্য আবৃত করে৷
- উৎপাদনের জন্য:`listenerCount`,`removeAllListeners`যোগ করুন এবং বাতিল করার জন্য`AbortSignal`ব্যবহার করার কথা বিবেচনা করুন৷
### সমস্যা 2: একটি টাইপ-সেফ এসকিউএল কোয়েরি বিল্ডার প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি এসকিউএল কোয়েরি বিল্ডার তৈরি করুন যেখানে কলামের নাম এবং প্রকারগুলি একটি টাইপস্ক্রিপ্ট ইন্টারফেস থেকে উদ্ভূত হয়। নির্মাতার উচিত কম্পাইলের সময় অবৈধ কলামের নাম এবং টাইপের অমিল প্রতিরোধ করা।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) কলামের নামগুলি`keyof T`তে সীমাবদ্ধ, (2) যেখানে কলাম অনুসারে ক্লজের মান টাইপ করা হয়েছে, (3) বিল্ডিং কোয়েরির জন্য চেইনেবল API। এর জন্য`Record<string, unknown>`দ্বারা সীমাবদ্ধ জেনেরিক প্রয়োজন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- কলাম নামের সীমাবদ্ধতার জন্য`keyof T`ব্যবহার করুন।
- মান প্রকারের সীমাবদ্ধতার জন্য`T[K]`ব্যবহার করুন।
- প্যারামিটারাইজড প্রশ্নগুলির সাথে SQL স্ট্রিং তৈরি করুন (এসকিউএল ইনজেকশন প্রতিরোধ করুন)।
- চেইনযোগ্য পদ্ধতি`this`ফেরত দেয়।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- এসকিউএল ইনজেকশন প্রতিরোধ: সমস্ত মান প্যারামিটারাইজড কোয়েরির মধ্য দিয়ে যায় (`$1`,`$2`), কখনও ইন্টারপোলেটেড নয়৷
- টাইপ নিরাপত্তা: কলামের নাম এবং মানের প্রকারগুলি কম্পাইলের সময় চেক করা হয়।
- এক্সটেনসিবিলিটি: একই প্যাটার্ন অনুসরণ করে`join`,`groupBy`,`having`,`insert`,`update`পদ্ধতি যোগ করুন৷
- উত্পাদন:`kysely`বা`drizzle-orm`ব্যবহার করুন — তারা সম্পূর্ণ SQL কভারেজ সহ এই ধরনের নিরাপত্তা প্রদান করে।
### সমস্যা 3: প্রকার নিরাপত্তা সহ একটি সীমাবদ্ধ স্টেট মেশিন প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি টাইপ-সেফ ফিনিট স্টেট মেশিন তৈরি করুন যেখানে কম্পাইলের সময় বৈধ ট্রানজিশন প্রয়োগ করা হয়। প্রতিটি রাজ্যে প্রবেশ/প্রস্থান ক্রিয়া থাকতে পারে এবং মেশিনের বর্তমান অবস্থা ট্র্যাক করা উচিত।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) প্রকার হিসাবে সংজ্ঞায়িত অবস্থা এবং ঘটনা, (2) টাইপ স্তরে ম্যাপ করা বৈধ ট্রানজিশন, (3) কম্পাইলার অবৈধ রূপান্তর প্রতিরোধ করে, (4) কলব্যাকের সাথে রানটাইম স্টেট ট্র্যাকিং। এর জন্য ম্যাপ করা প্রকার এবং শর্তসাপেক্ষ প্রকারের প্রয়োজন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি`TransitionMap`:`{ [State]: { [Event]: NextState } }`সংজ্ঞায়িত করুন।
- বর্তমান অবস্থার উপর ভিত্তি করে`send(event)`সীমাবদ্ধ করতে জেনেরিক ব্যবহার করুন।
- একটি ভেরিয়েবল দিয়ে রানটাইমে ট্র্যাক স্টেট।
- রাজ্য প্রতি এন্ট্রি/প্রস্থান কলব্যাক সমর্থন করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- রানটাইম নিরাপত্তা:`send`অবৈধ ট্রানজিশন নিক্ষেপ করে।
- টাইপ নিরাপত্তা:`EventsFor`টাইপ কম্পাইল সময়ে রাজ্য প্রতি বৈধ ইভেন্ট বের করে।
- ট্রানজিশনে প্রবেশ/প্রস্থান কলব্যাক স্বয়ংক্রিয়ভাবে চালু হয়।
- উৎপাদনের জন্য:`xstate`ব্যবহার করুন — এটি ভিজ্যুয়াল ডিবাগিং, শ্রেণীবদ্ধ অবস্থা, গার্ড এবং অ্যাকশন সহ একটি সম্পূর্ণ স্টেট মেশিন লাইব্রেরি প্রদান করে।
---

## সারাংশ
TypeScript হল জাভাস্ক্রিপ্ট যা তুচ্ছ স্ক্রিপ্টের বাইরে যেকোনো কিছুর জন্য করা হয়। এটি একটি শক্তিশালী টাইপ সিস্টেম যুক্ত করে যা বাগগুলিকে তাড়াতাড়ি ধরতে পারে, টুলিংকে উন্নত করে এবং নথির কোডগুলিকে উন্নত করে -- সবই স্ট্যান্ডার্ড জাভাস্ক্রিপ্টে কম্পাইল করার সময় যা কোথাও চলে। শেখার বক্ররেখাটি মৃদু (আপনি ন্যূনতম ধরনের দিয়ে শুরু করতে পারেন) কিন্তু গভীরতা বিশাল (টাইপ সিস্টেমটি টুরিং-সম্পূর্ণ)। আধুনিক জাভাস্ক্রিপ্ট বিকাশের জন্য, টাইপস্ক্রিপ্ট শিল্পের মান হয়ে উঠেছে।