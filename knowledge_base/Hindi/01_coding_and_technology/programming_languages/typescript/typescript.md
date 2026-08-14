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
# टाइपस्क्रिप्ट
टाइपस्क्रिप्ट जावास्क्रिप्ट का एक स्थिर रूप से टाइप किया गया सुपरसेट है जिसे माइक्रोसॉफ्ट (एंडर्स हेजल्सबर्ग के नेतृत्व में) द्वारा विकसित किया गया है और पहली बार 2012 में जारी किया गया है। यह जावास्क्रिप्ट में वैकल्पिक प्रकार के एनोटेशन, इंटरफेस, जेनरिक और उन्नत टाइप-सिस्टम सुविधाओं को जोड़ता है - फिर सादे जावास्क्रिप्ट में संकलित होता है जो जावास्क्रिप्ट चलाने पर कहीं भी चलता है। टाइपस्क्रिप्ट कोई अलग भाषा या रनटाइम नहीं है; यह एक टाइप चेकर वाला जावास्क्रिप्ट है।
टाइपस्क्रिप्ट बड़े पैमाने पर जावास्क्रिप्ट विकास के लिए मानक बन गया है। रिएक्ट, एंगुलर, वीएस कोड, डेनो और अधिकांश प्रमुख ओपन-सोर्स जावास्क्रिप्ट प्रोजेक्ट टाइपस्क्रिप्ट में लिखे गए हैं। यदि आप किसी भी महत्वपूर्ण आकार का एक नया जावास्क्रिप्ट प्रोजेक्ट शुरू कर रहे हैं, तो टाइपस्क्रिप्ट अनुशंसित डिफ़ॉल्ट है।
---

## टाइपस्क्रिप्ट क्यों मायने रखती है
- **संकलन समय पर बग पकड़ता है**: कोड चलने से पहले प्रकार की त्रुटियां पाई जाती हैं - उत्पादन में नहीं।
- **बेहतर आईडीई समर्थन**: स्वत: पूर्ण, गो-टू-डेफिनिशन, रीफैक्टरिंग और इनलाइन दस्तावेज़ीकरण सभी में नाटकीय रूप से सुधार होता है।
- **स्वयं-दस्तावेजीकरण कोड**: प्रकार दस्तावेज़ीकरण के रूप में कार्य करते हैं जो अद्यतित रहते हैं।
- **100% जावास्क्रिप्ट संगत**: कोई भी वैध जावास्क्रिप्ट वैध टाइपस्क्रिप्ट है। इसे आप धीरे-धीरे अपना सकते हैं.
- **उन्नत प्रकार प्रणाली**: संघ प्रकार, प्रतिच्छेदन प्रकार, सशर्त प्रकार, मैप किए गए प्रकार, टेम्पलेट शाब्दिक प्रकार - जटिल डोमेन तर्क को मॉडल करने के लिए प्रकार प्रणाली पर्याप्त रूप से अभिव्यंजक है।
- **उद्योग अपनाना**: एंगुलर को इसकी आवश्यकता है; रिएक्ट पारिस्थितिकी तंत्र इसका अत्यधिक उपयोग करता है; अधिकांश नए एनपीएम पैकेज टाइप परिभाषाओं के साथ भेजे जाते हैं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **संकलन चरण** | चलने से पहले`.ts`→`.js`अवश्य संकलित करें | विकास के लिए`ts-node`/`tsx`का उपयोग करें;  उत्पादन के लिए`tsc`|
| **सीखने की अवस्था** | प्रकार प्रणाली जटिल हो सकती है (जेनेरिक, सशर्त प्रकार) | बुनियादी प्रकारों से प्रारंभ करें; उन्नत सुविधाओं को धीरे-धीरे अपनाएं |
| **प्रकार परिभाषा फ़ाइलें** | सभी एनपीएम पैकेज प्रकारों के साथ नहीं भेजे जाते | DefinitelyTyped | से`@types/package-name`इंस्टॉल करें
| **संकलन समय** | बड़े प्रोजेक्ट टाइप-चेक करने में धीमे हो सकते हैं | प्रोजेक्ट संदर्भ, `isolatedModules`, या`swc`का उपयोग करें |
| **सुरक्षा की झूठी भावना** | प्रकार रनटाइम शुद्धता की गारंटी नहीं देते | रनटाइम सत्यापन (ज़ोड, आईओ-टीएस) के साथ संयोजित करें |
---

## सिंटेक्स बुनियादी बातें
### मूल प्रकार की टिप्पणियाँ
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

### इंटरफ़ेस और प्रकार
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

### जेनेरिक
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

### उन्नत प्रकार
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

### प्रकारों के साथ एसिंक
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

## उन्नत सिंटैक्स और पैटर्न
### उन्नत जेनरिक
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

### डेकोरेटर्स (टाइपस्क्रिप्ट 5.0+ मानक)
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

### टाइप गार्ड और नैरोइंग
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

## समवर्ती एवं समांतरता
टाइपस्क्रिप्ट को जावास्क्रिप्ट का समवर्ती मॉडल विरासत में मिला है लेकिन यह एसिंक पैटर्न में प्रकार की सुरक्षा जोड़ता है।
### टाइप किए गए Async पैटर्न
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना निर्देशिका संरचना
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

###`tsconfig.json`- टाइपस्क्रिप्ट कॉन्फ़िगरेशन
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

### निर्माण और पैकेज प्रबंधन
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

### विटेस्ट के साथ परीक्षण
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

### सीआई/सीडी पाइपलाइन - गिटहब क्रियाएँ
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

## उन्नत सिंटैक्स और पैटर्न
### उन्नत जेनरिक
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

### डेकोरेटर्स (टाइपस्क्रिप्ट 5.0+)
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

### टाइप गार्ड और नैरोइंग
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

## प्रोजेक्ट कॉन्फ़िगरेशन और बिल्ड सिस्टम
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

### विटेस्ट के साथ परीक्षण
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

### राशि चक्र के साथ रनटाइम सत्यापन
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

## अंतरसंचालनीयता
### जावास्क्रिप्ट लाइब्रेरीज़ का उपयोग करना
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

## डिज़ाइन पैटर्न
### परिणाम पैटर्न
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

### रिपॉजिटरी पैटर्न
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

## तैनाती
### डॉकरफ़ाइल
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

## पारिस्थितिकी तंत्र
### प्रमुख उपकरण
| उपकरण | उद्देश्य |
|------|---------|
| **tsc** | टाइपस्क्रिप्ट कंपाइलर (आधिकारिक) |
| **ts-नोड / tsx** | अलग संकलन के बिना सीधे टाइपस्क्रिप्ट चलाएँ |
| **एसडब्ल्यूसी** | अल्ट्रा-फास्ट रस्ट-आधारित टाइपस्क्रिप्ट/जावास्क्रिप्ट कंपाइलर |
| **ESlint + टाइपस्क्रिप्ट-eslint** | प्रकार-जागरूक नियमों के साथ लिंटिंग |
| **ज़ोड** | टाइपस्क्रिप्ट अनुमान के साथ रनटाइम प्रकार सत्यापन |
| **tsconfig.json** | टाइपस्क्रिप्ट कॉन्फ़िगरेशन फ़ाइल |
### फ्रेमवर्क (सभी टाइपस्क्रिप्ट-प्रथम)
| ढाँचा | डोमेन |
|--------|-------|
| **कोणीय** | पूर्ण विशेषताओं वाला फ्रंटएंड फ्रेमवर्क (टाइपस्क्रिप्ट की आवश्यकता है) |
| **अगला.जेएस** | रिएक्ट मेटा-फ्रेमवर्क (टाइपस्क्रिप्ट-प्रथम) |
| **NestJS** | एंटरप्राइज बैकएंड फ्रेमवर्क (टाइपस्क्रिप्ट-प्रथम) |
| **टीआरपीसी** | एंड-टू-एंड टाइपसेफ एपीआई (केवल टाइपस्क्रिप्ट) |
| **प्रिज्मा** | Node.js के लिए टाइप-सुरक्षित ORM |
---

## टाइपस्क्रिप्ट का उपयोग कब करें
| परिदृश्य | टाइपस्क्रिप्ट क्यों | बेहतर विकल्प |
|---|----------------------|-----|
| बड़े जावास्क्रिप्ट प्रोजेक्ट | प्रकार की सुरक्षा बग की संपूर्ण श्रेणियों को रोकती है | -- |
| टीम प्रोजेक्ट्स | प्रकार एक साझा अनुबंध के रूप में कार्य करते हैं | -- |
| एपीआई विकास | टीआरपीसी या ओपनएपीआई के साथ एंड-टू-एंड प्रकार की सुरक्षा | सरल REST API के लिए जावा पर जाएँ |
| कोई भी नया जावास्क्रिप्ट प्रोजेक्ट | बाद में टाइपस्क्रिप्ट जोड़ने की लागत अधिक है | केवल छोटी स्क्रिप्ट के लिए सादा जेएस |
| पुस्तकालय / एनपीएम पैकेज | उपभोक्ताओं को स्वत: पूर्ण और टाइप चेकिंग मिलती है | -- |
**सामान्य नियम**: यदि आपके जावास्क्रिप्ट प्रोजेक्ट में कुछ सौ से अधिक पंक्तियाँ हैं, तो टाइपस्क्रिप्ट का उपयोग करें।
---

## सिंथेटिक प्रश्नोत्तर
### Q1:`type`और`interface`के बीच क्या अंतर है, और मुझे प्रत्येक का उपयोग कब करना चाहिए?
**ए:** दोनों वस्तु आकार को परिभाषित करते हैं, लेकिन उनकी क्षमताएं अलग-अलग होती हैं। `interface`डिक्लेरेशन मर्जिंग (एक ही नाम मर्ज के साथ कई घोषणाएं), इनहेरिटेंस के लिए`extends`का समर्थन करता है, और सार्वजनिक एपीआई के लिए मुहावरेदार विकल्प है। `type`यूनियन प्रकार, प्रतिच्छेदन प्रकार, मैप किए गए प्रकार, सशर्त प्रकार और टेम्पलेट शाब्दिक प्रकार - कुछ भी उन्नत का समर्थन करता है। सर्वोत्तम अभ्यास: ऑब्जेक्ट आकृतियों और सार्वजनिक एपीआई के लिए`interface`का उपयोग करें; यूनियनों, उपयोगिताओं और जटिल प्रकार के संचालन के लिए`type`का उपयोग करें।
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

### प्रश्न2: जेनेरिक कैसे काम करते हैं, और वे महत्वपूर्ण क्यों हैं?
**ए:** जेनरिक आपको फ़ंक्शन, कक्षाएं और प्रकार लिखने देता है जो प्रकार की सुरक्षा बनाए रखते हुए किसी भी प्रकार के साथ काम करते हैं।`any`(जो प्रकार की जानकारी खो देता है) के बजाय, जेनरिक इनपुट और आउटपुट प्रकारों के बीच संबंध को संरक्षित करते हैं। वे पुन: प्रयोज्य, प्रकार-सुरक्षित कोड की नींव हैं।
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

### Q3: उपयोगिता प्रकार क्या हैं, और मुझे किनके बारे में जानना चाहिए?
**ए:** टाइपस्क्रिप्ट अंतर्निहित उपयोगिता प्रकार प्रदान करता है जो मौजूदा प्रकारों को बदल देता है। सबसे महत्वपूर्ण:`Partial<T>`(सभी वैकल्पिक),`Required<T>`(सभी आवश्यक),`Pick<T, K>`(कुंजियाँ चुनें),`Awaited<T>`(वादा खोलो)। इन्हें सीखें - वे कस्टम प्रकार के संचालन की अधिकांश आवश्यकता को समाप्त कर देते हैं।
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

### Q4: मैं एसिंक कोड कैसे टाइप करूं और टाइप-सुरक्षित तरीके से त्रुटियों को कैसे संभालूं?
**ए:** Async फ़ंक्शन स्वचालित रूप से`Promise<T>`लौटाते हैं जहां T रिटर्न प्रकार है। वादे को पूरा करने के लिए`await`का उपयोग करें। त्रुटि प्रबंधन के लिए, टाइपस्क्रिप्ट में टाइप किए गए अपवाद नहीं हैं, लेकिन आप टाइप गार्ड और परिणाम प्रकार बना सकते हैं। "परिणाम पैटर्न" (रस्ट से प्रेरित) संकलन-समय त्रुटि प्रबंधन प्रदान करता है।
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

### Q5: घोषणा फ़ाइलें (.d.ts) क्या हैं और मैं तृतीय-पक्ष प्रकारों का उपयोग कैसे करूँ?
**ए:** घोषणा फ़ाइलें उन जावास्क्रिप्ट पुस्तकालयों के प्रकारों का वर्णन करती हैं जिनमें अंतर्निहित टाइपस्क्रिप्ट प्रकार नहीं होते हैं। उनमें केवल प्रकार की जानकारी होती है (कोई रनटाइम कोड नहीं)। DefinitelyTyped:`npm install --save-dev @types/lodash`से समुदाय-रखरखाव प्रकार स्थापित करें। अपने स्वयं के पुस्तकालयों के लिए,`package.json`में एक`types`फ़ील्ड जोड़ें या अपने स्रोत के साथ`.d.ts`फ़ाइलें शामिल करें। व्यापक घोषणाओं के लिए`declare module`का उपयोग करें।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक प्रकार-सुरक्षित इवेंट एमिटर बनाएं
**समस्या कथन:** टाइपस्क्रिप्ट में एक सामान्य, टाइप-सुरक्षित इवेंट एमिटर बनाएं जहां प्रत्येक इवेंट का नाम एक विशिष्ट पेलोड प्रकार पर मैप होता है। कंपाइलर को कंपाइल समय पर गलत इवेंट नाम और पेलोड प्रकार को पकड़ना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें एक इवेंट सिस्टम की आवश्यकता है जहां: (1) इवेंट को उनके पेलोड प्रकारों के साथ परिभाषित किया जाता है, (2)`emit`केवल सही पेलोड के साथ वैध इवेंट नाम स्वीकार करता है, (3)`on`केवल सही टाइप किए गए हैंडलर के साथ वैध इवेंट नाम स्वीकार करता है। इसके लिए इवेंट मैप इंटरफ़ेस पर मैप किए गए प्रकारों और जेनेरिक की आवश्यकता होती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- एक`EventMap`प्रकार परिभाषित करें: `{ [eventName: string]: payloadType }`।
- इवेंट के नाम सीमित करने के लिए`keyof EventMap`का उपयोग करें।
- किसी विशिष्ट घटना के लिए पेलोड प्रकार प्राप्त करने के लिए`EventMap[K]`का उपयोग करें।
- श्रोताओं को`Map<string, Function[]>`में संग्रहित करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- प्रकार की सुरक्षा: कंपाइलर कंपाइल समय पर गलत ईवेंट नाम और गलत पेलोड आकार पकड़ता है।
-`on`सुविधाजनक सफ़ाई के लिए एक अनसब्सक्राइब फ़ंक्शन लौटाता है।
-`once`पहले आह्वान के बाद श्रोता को स्वतः-सदस्यता समाप्त करने के लिए बाध्य करता है।
- उत्पादन के लिए:`listenerCount`,`removeAllListeners`जोड़ें, और रद्दीकरण के लिए`AbortSignal`का उपयोग करने पर विचार करें।
### समस्या 2: एक प्रकार-सुरक्षित SQL क्वेरी बिल्डर लागू करें
**समस्या कथन:** एक SQL क्वेरी बिल्डर बनाएं जहां कॉलम नाम और प्रकार टाइपस्क्रिप्ट इंटरफ़ेस से प्राप्त होते हैं। बिल्डर को संकलन समय पर अमान्य कॉलम नामों और प्रकार के बेमेल को रोकना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) कॉलम नाम`keyof T`तक सीमित, (2) जहां क्लॉज मान कॉलम के अनुसार टाइप किए गए, (3) बिल्डिंग क्वेरी के लिए चेनेबल एपीआई। इसके लिए`Record<string, unknown>`द्वारा प्रतिबंधित जेनेरिक की आवश्यकता होती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- कॉलम नाम की बाधाओं के लिए`keyof T`का उपयोग करें।
- मूल्य प्रकार की बाधाओं के लिए`T[K]`का उपयोग करें।
- पैरामीटरयुक्त प्रश्नों के साथ SQL स्ट्रिंग बनाएं (SQL इंजेक्शन को रोकें)।
- चेनेबल विधियाँ`this`लौटाती हैं।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- एसक्यूएल इंजेक्शन रोकथाम: सभी मान पैरामीटरयुक्त प्रश्नों (`$1`, `$2`) से गुजरते हैं, कभी भी प्रक्षेपित नहीं होते।
- प्रकार सुरक्षा: संकलन समय पर कॉलम नाम और मान प्रकार की जाँच की जाती है।
- विस्तारशीलता: समान पैटर्न का अनुसरण करते हुए`join`,`groupBy`,`having`,`insert`,`update`विधियां जोड़ें।
- उत्पादन:`kysely`या`drizzle-orm`का उपयोग करें - वे पूर्ण SQL कवरेज के साथ इस प्रकार की सुरक्षा प्रदान करते हैं।
### समस्या 3: प्रकार की सुरक्षा के साथ एक परिमित राज्य मशीन लागू करें
**समस्या कथन:** एक प्रकार-सुरक्षित परिमित राज्य मशीन बनाएं जहां संकलन समय पर वैध बदलाव लागू किए जाते हैं। प्रत्येक राज्य में प्रवेश/निकास क्रियाएं हो सकती हैं, और मशीन को वर्तमान स्थिति को ट्रैक करना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) राज्यों और घटनाओं को प्रकारों के रूप में परिभाषित किया गया है, (2) प्रकार के स्तर पर वैध बदलावों को मैप किया गया है, (3) कंपाइलर अमान्य बदलावों को रोकता है, (4) कॉलबैक के साथ रनटाइम स्थिति ट्रैकिंग। इसके लिए मैप किए गए प्रकार और सशर्त प्रकार की आवश्यकता होती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- एक`TransitionMap`:`{ [State]: { [Event]: NextState } }`को परिभाषित करें।
- वर्तमान स्थिति के आधार पर`send(event)`को बाधित करने के लिए जेनेरिक का उपयोग करें।
- एक वेरिएबल के साथ रनटाइम पर स्थिति को ट्रैक करें।
- प्रति राज्य समर्थन प्रवेश/निकास कॉलबैक।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- रनटाइम सुरक्षा:`send`अमान्य ट्रांज़िशन पर फेंकता है।
- प्रकार सुरक्षा:`EventsFor`प्रकार संकलन समय पर प्रति राज्य वैध घटनाओं को निकालता है।
- प्रवेश/निकास कॉलबैक संक्रमण पर स्वचालित रूप से सक्रिय हो जाते हैं।
- उत्पादन के लिए:`xstate`का उपयोग करें - यह विज़ुअल डिबगिंग, पदानुक्रमित स्थिति, गार्ड और क्रियाओं के साथ एक पूर्ण राज्य मशीन लाइब्रेरी प्रदान करता है।
---

## सारांश
टाइपस्क्रिप्ट वह जावास्क्रिप्ट है जो सामान्य लिपियों से परे किसी भी चीज़ के लिए सही ढंग से बनाई गई है। यह एक शक्तिशाली प्रकार की प्रणाली जोड़ता है जो बग को जल्दी पकड़ता है, टूलींग में सुधार करता है, और दस्तावेज़ कोड - मानक जावास्क्रिप्ट को संकलित करते समय कहीं भी चलता है। सीखने की अवस्था धीमी है (आप न्यूनतम प्रकारों से शुरू कर सकते हैं) लेकिन गहराई विशाल है (प्रकार प्रणाली ट्यूरिंग-पूर्ण है)। आधुनिक जावास्क्रिप्ट विकास के लिए, टाइपस्क्रिप्ट उद्योग मानक बन गया है।