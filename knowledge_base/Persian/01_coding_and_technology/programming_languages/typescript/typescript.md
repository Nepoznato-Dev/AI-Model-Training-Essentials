---
# فراداده
عنوان: "TypeScript"
توضیحات: "مرجع جامع برای زبان برنامه نویسی TypeScript شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [تایپ، زبان برنامه نویسی، نحو، اکوسیستم، کدنویسی و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "34 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
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
| **مرحله تالیف** | قبل از اجرا باید`.ts`→`.js`را کامپایل کند | برای توسعه از`ts-node`/`tsx`استفاده کنید. `tsc`برای تولید |
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

###`tsconfig.json`— پیکربندی TypeScript
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

## خلاصه
TypeScript جاوا اسکریپتی است که برای هر چیزی فراتر از اسکریپت های بی اهمیت درست انجام می شود. این سیستم یک نوع قدرتمند را اضافه می کند که اشکالات را زود تشخیص می دهد، ابزارها و کد اسناد را بهبود می بخشد - همه اینها در حالی که به جاوا اسکریپت استانداردی که در هر جایی اجرا می شود کامپایل می شود. منحنی یادگیری ملایم است (شما می توانید با حداقل انواع شروع کنید) اما عمق آن بسیار زیاد است (سیستم نوع کاملاً تورینگ است). برای توسعه مدرن جاوا اسکریپت، TypeScript به استاندارد صنعتی تبدیل شده است.