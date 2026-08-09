---
# البيانات الوصفية
العنوان: "TypeScript"
الوصف: "مرجع شامل للغة برمجة TypeScript يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [الآلة الكاتبة، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "34 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
# تايب سكريبت
TypeScript عبارة عن مجموعة شاملة من JavaScript مكتوبة بشكل ثابت تم تطويرها بواسطة Microsoft (بقيادة Anders Hejlsberg) وتم إصدارها لأول مرة في عام 2012. وهي تضيف تعليقات توضيحية اختيارية للنوع وواجهات وأسماء عامة وميزات نظام الكتابة المتقدمة إلى JavaScript - ثم يتم تجميعها إلى JavaScript عادي يتم تشغيله في أي مكان يتم تشغيل JavaScript فيه. TypeScript ليست لغة منفصلة أو وقت تشغيل منفصل؛ إنها JavaScript مع مدقق النوع.
أصبح TypeScript هو المعيار لتطوير JavaScript على نطاق واسع. تتم كتابة React وAngular وVS Code وDeno ومعظم مشاريع JavaScript مفتوحة المصدر باستخدام TypeScript. إذا كنت تبدأ مشروع JavaScript جديدًا بأي حجم كبير، فإن TypeScript هو الخيار الافتراضي الموصى به.
---

## لماذا تعتبر TypeScript مهمة
- **اكتشاف الأخطاء في وقت الترجمة**: يتم العثور على أخطاء الكتابة قبل تشغيل التعليمات البرمجية - وليس أثناء الإنتاج.
- **دعم أفضل لـ IDE**: يتم تحسين الإكمال التلقائي والانتقال إلى التعريف وإعادة البناء والوثائق المضمنة بشكل كبير.
- **رمز التوثيق الذاتي**: تعمل الأنواع بمثابة وثائق تظل محدثة.
- **متوافق مع JavaScript بنسبة 100%**: أي JavaScript صالح هو TypeScript صالح. يمكنك اعتماده تدريجياً.
- **نظام الكتابة المتقدم**: أنواع الاتحاد، وأنواع التقاطع، والأنواع الشرطية، والأنواع المعينة، والأنواع الحرفية للقالب - نظام الكتابة معبر بما يكفي لصياغة منطق المجال المعقد.
- **اعتماد الصناعة**: تتطلب Angular ذلك؛ يستخدمه نظام React البيئي بأغلبية ساحقة؛ تأتي معظم حزم npm الجديدة مع تعريفات النوع.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **خطوة التجميع** | يجب ترجمة`.ts`→`.js`قبل تشغيل | استخدم`ts-node`/`tsx`للتطوير؛  __محمي_4__ للإنتاج |
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

### __محمي_0__ — تكوين TypeScript
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

## ملخص
TypeScript هو JavaScript يتم تنفيذه بشكل صحيح لأي شيء يتجاوز النصوص التافهة. فهو يضيف نظام كتابة قويًا يرصد الأخطاء مبكرًا، ويحسن الأدوات، ويوثق التعليمات البرمجية - كل ذلك أثناء التحويل البرمجي إلى JavaScript القياسي الذي يعمل في أي مكان. منحنى التعلم لطيف (يمكنك البدء بالحد الأدنى من الأنواع) ولكن العمق واسع (نظام الكتابة مكتمل من خلال تورينج). بالنسبة لتطوير JavaScript الحديث، أصبح TypeScript هو المعيار الصناعي.