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

# تايب سكريبت
TypeScript عبارة عن مجموعة شاملة من JavaScript مكتوبة بشكل ثابت تم تطويرها بواسطة Microsoft (بقيادة Anders Hejlsberg) وتم إصدارها لأول مرة في عام 2012. وهي تضيف تعليقات توضيحية اختيارية للنوع، وواجهات، وأدوية عامة، وميزات نظام الكتابة المتقدمة إلى JavaScript - ثم يتم تجميعها إلى JavaScript عادي يتم تشغيله في أي مكان يتم تشغيل JavaScript فيه. TypeScript ليست لغة منفصلة أو وقت تشغيل منفصل؛ إنها JavaScript مع مدقق النوع.
أصبح TypeScript هو المعيار لتطوير JavaScript على نطاق واسع. تتم كتابة React وAngular وVS Code وDeno ومعظم مشاريع JavaScript مفتوحة المصدر باستخدام TypeScript. إذا كنت تبدأ مشروع JavaScript جديدًا بأي حجم كبير، فإن TypeScript هو الخيار الافتراضي الموصى به.
---

## لماذا تعتبر TypeScript مهمة
- **اكتشاف الأخطاء في وقت الترجمة**: يتم العثور على أخطاء الكتابة قبل تشغيل التعليمات البرمجية - وليس أثناء الإنتاج.
- **دعم أفضل لـ IDE**: يتم تحسين الإكمال التلقائي والانتقال إلى التعريف وإعادة البناء والوثائق المضمنة بشكل كبير.
- **رمز التوثيق الذاتي**: تعمل الأنواع بمثابة وثائق تظل محدثة.
- **متوافق مع JavaScript بنسبة 100%**: أي JavaScript صالح يعد TypeScript صالحًا. يمكنك اعتماده تدريجياً.
- **نظام الكتابة المتقدم**: أنواع الاتحاد، وأنواع التقاطع، والأنواع الشرطية، والأنواع المعينة، والأنواع الحرفية للقالب - نظام الكتابة معبر بدرجة كافية لصياغة منطق المجال المعقد.
- **اعتماد الصناعة**: تتطلب Angular ذلك؛ يستخدمه نظام React البيئي بأغلبية ساحقة؛ تأتي معظم حزم npm الجديدة مع تعريفات النوع.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **خطوة التجميع** | يجب ترجمة`.ts`→`.js`قبل تشغيل | استخدم`ts-node`/`tsx`للتطوير؛ `tsc`للإنتاج |
| **منحنى التعلم** | يمكن أن يكون نظام الكتابة معقدًا (أسماء عامة، أنواع شرطية) | ابدأ بالأنواع الأساسية؛ اعتماد الميزات المتقدمة تدريجيا |
| ** ملفات تعريف النوع ** | لا يتم شحن جميع حزم npm بالأنواع | قم بتثبيت`@types/package-name`من DefinitelyTyped |
| ** تجميع الأوقات ** | قد تكون المشاريع الكبيرة بطيئة في التحقق من النوع | استخدم مراجع المشروع،`isolatedModules`أو`swc`|
| **شعور زائف بالأمان** | لا تضمن الأنواع صحة وقت التشغيل | ادمجها مع التحقق من صحة وقت التشغيل (Zod، io-ts) |
---

## أساسيات بناء الجملة
### التعليقات التوضيحية للنوع الأساسي
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

### الواجهات والأنواع
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

### الأدوية العامة
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

### الأنواع المتقدمة
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

### غير متزامن مع الأنواع
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة المتقدمة
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

### أدوات الديكور (TypeScript 5.0+ Standard)
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

### اكتب الحراس والتضييق
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

## التزامن والتوازي
يرث TypeScript نموذج التزامن الخاص بـ JavaScript ولكنه يضيف أمان الكتابة إلى الأنماط غير المتزامنة.
### الأنماط غير المتزامنة المكتوبة
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

## تكوين المشروع ونظام البناء
### هيكل دليل المشروع
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

###`tsconfig.json`— تكوين TypeScript
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

### إدارة البناء والحزم
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

### الاختبار باستخدام Vitest
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

### خط أنابيب CI/CD — إجراءات GitHub
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة المتقدمة
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

### أدوات الديكور (TypeScript 5.0+)
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

### اكتب الحراس والتضييق
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

## تكوين المشروع ونظام البناء
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

### الاختبار باستخدام Vitest
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

### التحقق من صحة وقت التشغيل باستخدام Zod
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

## إمكانية التشغيل البيني
### استخدام مكتبات جافا سكريبت
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

## أنماط التصميم
### نمط النتيجة
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

### نمط المستودع
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

## النشر
### ملف دوكر
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

## النظام البيئي
### الأدوات الرئيسية
| أداة | الغرض |
|------|---------|
| **تسك** | مترجم TypeScript (رسمي) |
| ** عقدة ts / tsx ** | قم بتشغيل TypeScript مباشرة بدون تجميع منفصل |
| **سوك** | مترجم TypeScript/JavaScript فائق السرعة قائم على الصدأ |
| **ESLint + typescript-eslint** | البطانة بقواعد مدركة للنوع |
| **زود** | التحقق من صحة نوع وقت التشغيل باستخدام استنتاج TypeScript |
| **tsconfig.json** | ملف تكوين TypeScript |
### الأطر (كل TypeScript-أولاً)
| الإطار | المجال |
|-----------|--------|
| ** الزاوي ** | إطار عمل كامل المواصفات للواجهة الأمامية (يتطلب TypeScript) |
| **Next.js** | رد فعل إطار التعريف (TypeScript-first) |
| **نيست جي إس** | إطار عمل الواجهة الخلفية للمؤسسة (TypeScript-first) |
| **tRPC** | واجهات برمجة التطبيقات الآمنة من طرف إلى طرف (TypeScript فقط) |
| **بريزما** | ORM من النوع الآمن لـ Node.js |
---

## متى يجب استخدام TypeScript
| السيناريو | لماذا تايب سكريبت | البديل الأفضل |
|----------|-------------|------------------|
| مشاريع جافا سكريبت الكبيرة | أمان النوع يمنع فئات كاملة من الأخطاء | -- |
| مشاريع الفريق | الأنواع بمثابة عقد مشترك | -- |
| تطوير API | أمان شامل من خلال tRPC أو OpenAPI | اذهب، جافا للحصول على واجهات برمجة تطبيقات REST أبسط |
| أي مشروع جافا سكريبت جديد | تكلفة إضافة TypeScript لاحقًا مرتفعة | JS عادي للنصوص الصغيرة فقط |
| المكتبات / حزم npm | يحصل المستهلكون على الإكمال التلقائي والتحقق من النوع | -- |
**القاعدة الأساسية**: إذا كان مشروع JavaScript الخاص بك يحتوي على أكثر من بضع مئات من الأسطر، فاستخدم TypeScript.
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين`type`و`interface` ومتى يجب أن أستخدم كل منهما؟
**أ:** كلاهما يحددان أشكال الكائنات، لكن لهما قدرات مختلفة.  يدعم`interface`دمج الإعلانات (إعلانات متعددة بنفس الاسم المدمج)، و`extends` للميراث، وهو الاختيار الاصطلاحي لواجهات برمجة التطبيقات العامة.  يدعم`type`أنواع الاتحاد وأنواع التقاطع والأنواع المعينة والأنواع الشرطية والأنواع الحرفية للقالب - أي شيء متقدم. أفضل الممارسات: استخدم`interface`لأشكال الكائنات وواجهات برمجة التطبيقات العامة؛ استخدم`type`للاتحادات والأدوات المساعدة وعمليات النوع المعقدة.
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

### السؤال الثاني: كيف تعمل الأدوية الجنيسة، وما سبب أهميتها؟
**أ:** تتيح لك الأدوية العامة كتابة الوظائف والفئات والأنواع التي تعمل مع أي نوع مع الحفاظ على أمان النوع. بدلاً من`any`(الذي يفقد معلومات النوع)، تحافظ الأدوية العامة على العلاقة بين أنواع الإدخال والإخراج. إنها أساس التعليمات البرمجية الآمنة والقابلة لإعادة الاستخدام.
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

### س3: ما هي أنواع المرافق، وما هي تلك التي يجب أن أعرفها؟
**أ:** يوفر TypeScript أنواع أدوات مساعدة مضمنة تعمل على تحويل الأنواع الموجودة. الأكثر أهمية:`Partial<T>`(جميعها اختيارية)،`Required<T>`(جميعها مطلوبة)،`Pick<T, K>`(مفاتيح محددة)،`Omit<T, K>`(استبعاد المفاتيح)،`Record<K, V>`(خريطة قيمة المفتاح)،`Exclude<T, U>`(إزالة من الاتحاد)،`ReturnType<T>`(استخراج نوع إرجاع الوظيفة)،`Awaited<T>`(فتح الوعد). تعرف على هذه الأشياء — فهي تلغي معظم الحاجة إلى عمليات الكتابة المخصصة.
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

### Q4: كيف يمكنني كتابة التعليمات البرمجية غير المتزامنة والتعامل مع الأخطاء بطريقة آمنة للكتابة؟
**A:** تقوم وظائف المزامنة تلقائيًا بإرجاع`Promise<T>`حيث T هو نوع الإرجاع. استخدم`await`لإلغاء الوعد. لمعالجة الأخطاء، لا يحتوي TypeScript على استثناءات مكتوبة، ولكن يمكنك إنشاء حراس الكتابة وأنواع النتائج. يوفر "نمط النتيجة" (المستوحى من Rust) معالجة الأخطاء في وقت الترجمة.
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

### س5: ما هي ملفات التصريح (.d.ts) وكيف يمكنني استخدام أنواع الجهات الخارجية؟
**ج:** تصف ملفات الإقرار أنواع مكتبات JavaScript التي لا تحتوي على أنواع TypeScript مضمنة. أنها تحتوي على معلومات النوع فقط (لا يوجد رمز وقت التشغيل). قم بتثبيت الأنواع التي يحتفظ بها المجتمع من DefinitelyTyped:`npm install --save-dev @types/lodash`. بالنسبة لمكتباتك الخاصة، أضف حقل`types`في`package.json`أو قم بتضمين ملفات`.d.ts`إلى جانب المصدر الخاص بك. استخدم`declare module`للإعلانات المحيطة.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: إنشاء باعث حدث آمن النوع
**بيان المشكلة:** قم بإنشاء باعث حدث عام وآمن من النوع في TypeScript حيث يتم تعيين كل اسم حدث إلى نوع حمولة محدد. يجب أن يلتقط المترجم أسماء الأحداث وأنواع الحمولة غير الصحيحة في وقت الترجمة.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى نظام أحداث حيث: (1) يتم تعريف الأحداث بأنواع الحمولات الخاصة بها، (2) يقبل`emit`فقط أسماء الأحداث الصالحة ذات الحمولات الصحيحة، (3) يقبل`on`فقط أسماء الأحداث الصالحة مع المعالجات المكتوبة بشكل صحيح. يتطلب هذا أنواعًا وأسماء عامة معينة عبر واجهة خريطة الحدث.
**الخطوة الثانية — تحديد النهج:**
- تحديد نوع `EventMap`:`{ [eventName: string]: payloadType }`.
- استخدم`keyof EventMap`لتقييد أسماء الأحداث.
- استخدم`EventMap[K]`للحصول على نوع الحمولة لحدث معين.
- تخزين المستمعين في`Map<string, Function[]>`.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- أمان النوع: يلتقط المترجم أسماء أحداث خاطئة وأشكال حمولة خاطئة في وقت الترجمة.
- يقوم`on`بإرجاع وظيفة إلغاء الاشتراك للتنظيف المريح.
- يُلزم`once`المستمع بإلغاء الاشتراك تلقائيًا بعد الاستدعاء الأول.
- للإنتاج: أضف`listenerCount`و`removeAllListeners`وفكر في استخدام`AbortSignal`للإلغاء.
### المشكلة الثانية: تنفيذ منشئ استعلام SQL آمن النوع
**بيان المشكلة:** قم بإنشاء منشئ استعلام SQL حيث يتم اشتقاق أسماء الأعمدة وأنواعها من واجهة TypeScript. يجب أن يمنع المنشئ أسماء الأعمدة غير الصالحة ويكتب عدم التطابق في وقت الترجمة.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) أسماء الأعمدة مقيدة بـ `keyof T`، (2) قيم جملة WHERE مكتوبة وفقًا للعمود، (3) واجهة برمجة تطبيقات قابلة للتسلسل لبناء الاستعلامات. وهذا يتطلب أدوية عامة مقيدة بـ`Record<string, unknown>`.
**الخطوة الثانية — تحديد النهج:**
- استخدم`keyof T`لقيود اسم العمود.
- استخدم`T[K]`لقيود نوع القيمة.
- بناء سلسلة SQL مع استعلامات ذات معلمات (منع حقن SQL).
- الأساليب القابلة للتسلسل ترجع`this`.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- منع حقن SQL: تمر جميع القيم عبر استعلامات ذات معلمات (`$1`، `$2`)، ولا يتم تحريفها أبدًا.
- سلامة الكتابة: يتم التحقق من أسماء الأعمدة وأنواع القيم في وقت الترجمة.
- القابلية للتوسعة: أضف أساليب`join`و`groupBy`و`having`و`insert`و`update`باتباع نفس النمط.
- الإنتاج: استخدم`kysely`أو`drizzle-orm`- فهي توفر هذا النوع من الأمان مع تغطية SQL كاملة.
### المشكلة 3: تنفيذ آلة الحالة المحدودة مع أمان النوع
**بيان المشكلة:** قم بإنشاء جهاز حالة محدودة آمن من النوع حيث يتم فرض التحولات الصالحة في وقت الترجمة. يمكن أن يكون لكل حالة إجراءات دخول/خروج، ويجب أن يتتبع الجهاز الحالة الحالية.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) حالات وأحداث محددة كأنواع، (2) انتقالات صالحة تم تعيينها على مستوى النوع، (3) يمنع المترجم التحولات غير الصالحة، (4) تتبع حالة وقت التشغيل من خلال عمليات الاسترجاعات. وهذا يتطلب الأنواع المعينة والأنواع الشرطية.
**الخطوة الثانية — تحديد النهج:**
- تحديد`TransitionMap`:`{ [State]: { [Event]: NextState } }`.
- استخدم الأدوية العامة لتقييد`send(event)`بناءً على الحالة الحالية.
- تتبع الحالة في وقت التشغيل باستخدام متغير.
- دعم عمليات الاسترجاعات الدخول / الخروج لكل دولة.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- أمان وقت التشغيل: يؤدي`send`إلى حدوث انتقالات غير صالحة.
- أمان النوع: يستخرج النوع`EventsFor`الأحداث الصالحة لكل حالة في وقت الترجمة.
- يتم إطلاق عمليات رد الاتصال للدخول/الخروج تلقائيًا عند التحولات.
- بالنسبة للإنتاج: استخدم`xstate`- فهو يوفر مكتبة أجهزة كاملة الحالة مع تصحيح الأخطاء المرئية والحالات الهرمية والحراس والإجراءات.
---

## ملخص
TypeScript هو JavaScript يتم تنفيذه بشكل صحيح لأي شيء يتجاوز النصوص التافهة. فهو يضيف نظام كتابة قويًا يرصد الأخطاء مبكرًا، ويحسن الأدوات، ويوثق التعليمات البرمجية - كل ذلك أثناء التحويل البرمجي إلى JavaScript القياسي الذي يعمل في أي مكان. منحنى التعلم لطيف (يمكنك البدء بالحد الأدنى من الأنواع) ولكن العمق واسع (نظام الكتابة مكتمل من خلال تورينج). بالنسبة لتطوير JavaScript الحديث، أصبح TypeScript هو المعيار الصناعي.