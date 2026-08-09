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

#พิมพ์สคริปต์
TypeScript เป็นชุด JavaScript ที่พิมพ์แบบคงที่ซึ่งพัฒนาโดย Microsoft (นำโดย Anders Hejlsberg) และเปิดตัวครั้งแรกในปี 2012 โดยจะเพิ่มคำอธิบายประกอบประเภททางเลือก อินเทอร์เฟซ ข้อมูลทั่วไป และคุณสมบัติระบบประเภทขั้นสูงให้กับ JavaScript จากนั้นคอมไพล์ลงไปเป็น JavaScript ธรรมดาที่ทำงานได้ทุกที่ที่ JavaScript รัน TypeScript ไม่ใช่ภาษาหรือรันไทม์แยกต่างหาก มันเป็น JavaScript พร้อมตัวตรวจสอบประเภท
TypeScript ได้กลายเป็นมาตรฐานสำหรับการพัฒนา JavaScript ขนาดใหญ่ React, Angular, VS Code, Deno และโปรเจ็กต์ JavaScript โอเพ่นซอร์สหลักๆ ส่วนใหญ่เขียนด้วย TypeScript หากคุณกำลังเริ่มโปรเจ็กต์ JavaScript ใหม่ที่มีขนาดสำคัญใดๆ TypeScript จะเป็นค่าเริ่มต้นที่แนะนำ
---

## ทำไม TypeScript ถึงมีความสำคัญ
- **จับจุดบกพร่อง ณ เวลาคอมไพล์**: พบข้อผิดพลาดประเภทก่อนที่โค้ดจะทำงาน — ไม่ใช่ในการใช้งานจริง
- **รองรับ IDE ที่ดีกว่า**: การเติมข้อความอัตโนมัติ การป้อนคำนิยาม การรีแฟคเตอร์ และเอกสารประกอบแบบอินไลน์ล้วนได้รับการปรับปรุงอย่างมาก
- **รหัสการจัดทำเอกสารด้วยตนเอง**: ประเภทต่างๆ ทำหน้าที่เป็นเอกสารที่เป็นข้อมูลล่าสุด
- **รองรับ JavaScript ได้ 100%**: JavaScript ที่ถูกต้องใดๆ ก็เป็น TypeScript ที่ถูกต้อง คุณสามารถค่อยๆ นำมาใช้ได้
- **ระบบประเภทขั้นสูง**: ประเภทยูเนี่ยน ประเภททางแยก ประเภทตามเงื่อนไข ประเภทที่แมป ประเภทตัวอักษรเทมเพลต — ระบบประเภทสามารถแสดงออกได้เพียงพอที่จะจำลองลอจิกโดเมนที่ซับซ้อน
- **การยอมรับในอุตสาหกรรม**: Angular ต้องการมัน ระบบนิเวศของปฏิกิริยาใช้มันอย่างท่วมท้น แพ็คเกจ npm ใหม่ส่วนใหญ่มาพร้อมกับคำจำกัดความประเภท
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ขั้นตอนการเรียบเรียง** | ต้องคอมไพล์`.ts`→`.js`ก่อนรัน | ใช้`ts-node`/`tsx`เพื่อการพัฒนา `tsc`สำหรับการผลิต |
| **เส้นโค้งการเรียนรู้** | ระบบประเภทสามารถซับซ้อนได้ (ทั่วไป, ประเภทที่มีเงื่อนไข) | เริ่มต้นด้วยประเภทพื้นฐาน นำคุณสมบัติขั้นสูงมาใช้อย่างค่อยเป็นค่อยไป |
| **ประเภทไฟล์คำจำกัดความ** | แพ็คเกจ npm ไม่ใช่ทุกแพ็คเกจที่จัดส่งด้วยประเภท | ติดตั้ง`@types/package-name`จาก SureTyped |
| **เวลาในการคอมไพล์** | โปรเจ็กต์ขนาดใหญ่อาจพิมพ์ตรวจสอบได้ช้า | ใช้การอ้างอิงโปรเจ็กต์`isolatedModules`หรือ`swc`|
| **ความรู้สึกปลอดภัยอันเป็นเท็จ** | ประเภทไม่รับประกันความถูกต้องของรันไทม์ | รวมกับการตรวจสอบรันไทม์ (Zod, io-ts) |
---

## พื้นฐานไวยากรณ์
### คำอธิบายประกอบประเภทพื้นฐาน
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

### อินเทอร์เฟซและประเภท
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

### ทั่วไป
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

### ประเภทขั้นสูง
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

### Async พร้อมประเภท
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ข้อมูลทั่วไปขั้นสูง
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

### มัณฑนากร (มาตรฐาน TypeScript 5.0+)
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

### ประเภท Guards และ Narrowing
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

## การเห็นพ้องต้องกันและความเท่าเทียม
TypeScript สืบทอดโมเดลการทำงานพร้อมกันของ JavaScript แต่เพิ่มความปลอดภัยของประเภทให้กับรูปแบบอะซิงก์
### รูปแบบ Async ที่พิมพ์
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างไดเรกทอรีโครงการ
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

###`tsconfig.json`— การกำหนดค่า TypeScript
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

### การสร้างและการจัดการแพ็คเกจ
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

### ทดสอบกับ Vitest
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

### ไปป์ไลน์ CI/CD — การดำเนินการ GitHub
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ข้อมูลทั่วไปขั้นสูง
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

### มัณฑนากร (TypeScript 5.0+)
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

### ประเภท Guards และ Narrowing
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

## การกำหนดค่าโครงการและสร้างระบบ
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

### ทดสอบกับ Vitest
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

### การตรวจสอบรันไทม์กับ Zod
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

## การทำงานร่วมกัน
### การใช้ไลบรารี JavaScript
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

## รูปแบบการออกแบบ
### รูปแบบผลลัพธ์
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

### รูปแบบพื้นที่เก็บข้อมูล
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

## การปรับใช้
### ด็อคเกอร์ไฟล์
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

## ระบบนิเวศ
### เครื่องมือสำคัญ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ทีเอสซี** | คอมไพเลอร์ TypeScript (เป็นทางการ) |
| **ts-node / tsx** | เรียกใช้ TypeScript โดยตรงโดยไม่ต้องรวบรวม |
| **swc** | คอมไพเลอร์ TypeScript/JavaScript ที่ใช้สนิมเร็วเป็นพิเศษ |
| **ESLint + typescript-eslint** | Linting ด้วยกฎการรับรู้ประเภท |
| **โซด** | การตรวจสอบประเภทรันไทม์ด้วยการอนุมาน TypeScript |
| **tsconfig.json** | ไฟล์การกำหนดค่า TypeScript |
### กรอบงาน (ทั้งหมด TypeScript-First)
| กรอบ | โดเมน |
|----------|--------|
| **เชิงมุม** | เฟรมเวิร์กส่วนหน้าที่มีคุณสมบัติครบถ้วน (ต้องใช้ TypeScript) |
| **Next.js** | ตอบสนองเมตาเฟรมเวิร์ก (TypeScript-first) |
| **NestJS** | กรอบงานแบ็กเอนด์ขององค์กร (TypeScript-first) |
| **tRPC** | API แบบ end-to-end typesafe (TypeScript เท่านั้น) |
| **ปริซึม** | ORM แบบปลอดภัยสำหรับ Node.js |
---

## เมื่อใดควรใช้ TypeScript
| สถานการณ์ | ทำไมต้องพิมพ์สคริปต์ | ทางเลือกที่ดีกว่า |
|----------|---------------|-------------------|
| โครงการ JavaScript ขนาดใหญ่ | ความปลอดภัยของประเภทจะป้องกันข้อผิดพลาดทั้งหมวดหมู่ | -- |
| โครงการของทีม | ประเภททำหน้าที่เป็นสัญญาที่ใช้ร่วมกัน | -- |
| การพัฒนา API | ความปลอดภัยแบบครบวงจรด้วย tRPC หรือ OpenAPI | ไป Java สำหรับ REST API ที่ง่ายกว่า |
| โครงการ JavaScript ใหม่ใด ๆ | ค่าใช้จ่ายในการเพิ่ม TypeScript ในภายหลังนั้นสูง | JS ธรรมดาสำหรับสคริปต์เล็ก ๆ เท่านั้น |
| แพ็คเกจไลบรารี / npm | ผู้บริโภคจะได้รับการเติมข้อความอัตโนมัติและพิมพ์การตรวจสอบ | -- |
**หลักทั่วไป**: หากโปรเจ็กต์ JavaScript ของคุณมีมากกว่าสองสามร้อยบรรทัด ให้ใช้ TypeScript
---

## สรุป
TypeScript เป็น JavaScript ที่เหมาะกับทุกสิ่งที่นอกเหนือจากสคริปต์เล็กๆ น้อยๆ โดยเพิ่มระบบประเภทที่มีประสิทธิภาพซึ่งสามารถตรวจจับจุดบกพร่องได้ตั้งแต่เนิ่นๆ ปรับปรุงเครื่องมือ และโค้ดเอกสาร ทั้งหมดนี้ในขณะเดียวกันก็คอมไพล์เป็น JavaScript มาตรฐานที่ทำงานได้ทุกที่ เส้นโค้งการเรียนรู้นั้นอ่อนโยน (คุณสามารถเริ่มต้นด้วยประเภทที่น้อยที่สุด) แต่ความลึกนั้นกว้างใหญ่ (ระบบประเภทคือทัวริงที่สมบูรณ์) สำหรับการพัฒนา JavaScript สมัยใหม่ TypeScript ได้กลายเป็นมาตรฐานอุตสาหกรรม