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

# TypeScript
TypeScript là một siêu tập hợp JavaScript được gõ tĩnh do Microsoft (do Anders Hejlsberg đứng đầu) phát triển và phát hành lần đầu tiên vào năm 2012. Nó bổ sung các chú thích loại tùy chọn, giao diện, khái quát và các tính năng hệ thống loại nâng cao vào JavaScript — sau đó biên dịch thành JavaScript đơn giản chạy ở mọi nơi JavaScript chạy. TypeScript không phải là ngôn ngữ hoặc thời gian chạy riêng biệt; đó là JavaScript với trình kiểm tra loại.
TypeScript đã trở thành tiêu chuẩn để phát triển JavaScript quy mô lớn. React, Angular, VS Code, Deno và hầu hết các dự án JavaScript nguồn mở lớn đều được viết bằng TypeScript. Nếu bạn đang bắt đầu một dự án JavaScript mới có kích thước đáng kể, thì TypeScript là mặc định được đề xuất.
---

## Tại sao TypeScript lại quan trọng
- **Bắt lỗi tại thời điểm biên dịch**: Lỗi loại được tìm thấy trước khi mã chạy — không có trong quá trình sản xuất.
- **Hỗ trợ IDE tốt hơn**: Tự động hoàn thành, chuyển sang định nghĩa, tái cấu trúc và tài liệu nội tuyến đều cải thiện đáng kể.
- **Mã tự ghi chép**: Các loại đóng vai trò là tài liệu luôn được cập nhật.
- **Tương thích 100% với JavaScript**: Mọi JavaScript hợp lệ đều là TypeScript hợp lệ. Bạn có thể áp dụng nó dần dần.
- **Hệ thống loại nâng cao**: Loại kết hợp, loại giao lộ, loại có điều kiện, loại được ánh xạ, loại chữ mẫu — hệ thống loại đủ biểu cảm để mô hình hóa logic miền phức tạp.
- **Áp dụng trong ngành**: Angular yêu cầu điều đó; Hệ sinh thái React sử dụng nó một cách áp đảo; hầu hết các gói npm mới đều có định nghĩa kiểu.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Bước tổng hợp** | Phải biên dịch`.ts`→`.js`trước khi chạy | Sử dụng`ts-node`/`tsx`để phát triển; `tsc`dành cho sản xuất |
| **Đường cong học tập** | Hệ thống loại có thể phức tạp (loại chung, loại có điều kiện) | Bắt đầu với các loại cơ bản; áp dụng dần dần các tính năng nâng cao |
| **Gõ tệp định nghĩa** | Không phải tất cả các gói npm đều có loại | Cài đặt`@types/package-name`từ DefiniteTyped |
| **Số lần biên dịch** | Các dự án lớn có thể chậm kiểm tra kiểu | Sử dụng tài liệu tham khảo dự án,`isolatedModules`hoặc`swc`|
| **Cảm giác an toàn sai lầm** | Các loại không đảm bảo tính chính xác của thời gian chạy | Kết hợp với xác thực thời gian chạy (Zod, io-ts) |
---

##Cơ bản về cú pháp
### Chú thích kiểu cơ bản
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

### Giao diện và loại
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

### Thuốc gốc
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

### Các loại nâng cao
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

### Không đồng bộ với các loại
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

## Cú pháp & Mẫu nâng cao
### Generics nâng cao
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

### Công cụ trang trí (Tiêu chuẩn TypeScript 5.0+)
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

### Loại bảo vệ và thu hẹp
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

## Đồng thời & Song song
TypeScript kế thừa mô hình đồng thời của JavaScript nhưng bổ sung tính an toàn về loại cho các mẫu không đồng bộ.
### Các mẫu không đồng bộ được nhập
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc thư mục dự án
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

###`tsconfig.json`- Cấu hình TypeScript
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

### Quản lý bản dựng và gói
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

###Thử nghiệm với Vitest
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

### Đường dẫn CI/CD — Hành động GitHub
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

## Cú pháp & Mẫu nâng cao
### Generics nâng cao
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

### Công cụ trang trí (TypeScript 5.0+)
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

### Loại bảo vệ và thu hẹp
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

## Cấu hình dự án và xây dựng hệ thống
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

###Thử nghiệm với Vitest
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

### Xác thực thời gian chạy với Zod
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

## Khả năng tương tác
### Sử dụng Thư viện JavaScript
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

## Mẫu thiết kế
### Mẫu kết quả
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

### Mẫu kho lưu trữ
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

## Triển khai
###Tệp Docker
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

## Hệ sinh thái
### Công cụ chính
| Công cụ | Mục đích |
|------|----------|
| **tsc** | Trình biên dịch TypeScript (chính thức) |
| **ts-nút / tsx** | Chạy trực tiếp TypeScript mà không cần biên dịch riêng |
| **swc** | Trình biên dịch TypeScript/JavaScript dựa trên Rust cực nhanh |
| **ESLint + TypeScript-eslint** | Linting với các quy tắc nhận biết kiểu |
| **Zod** | Xác thực loại thời gian chạy bằng suy luận TypeScript |
| **tsconfig.json** | Tệp cấu hình TypeScript |
### Khung (Tất cả TypeScript-First)
| Khung | Tên miền |
|----------||--------|
| **Góc cạnh** | Khung giao diện người dùng đầy đủ tính năng (yêu cầu TypeScript) |
| **Tiếp theo** | Phản ứng siêu khung (TypeScript-first) |
| **NestJS** | Khung phụ trợ doanh nghiệp (TypeScript-first) |
| **tRPC** | API an toàn loại đầu cuối (chỉ dành cho TypeScript) |
| **Prisma** | ORM loại an toàn cho Node.js |
---

## Khi nào nên sử dụng TypeScript
| Kịch bản | Tại sao TypeScript | Thay thế tốt hơn |
|----------|--------------|-------------------|
| Các dự án JavaScript lớn | Loại an toàn ngăn chặn toàn bộ loại lỗi | -- |
| Dự án nhóm | Các loại phục vụ như một hợp đồng chung | -- |
| Phát triển API | An toàn loại đầu cuối với tRPC hoặc OpenAPI | Đi, Java để có API REST đơn giản hơn |
| Bất kỳ dự án JavaScript mới nào | Chi phí thêm TypeScript sau này cao | JS thuần túy chỉ dành cho các tập lệnh nhỏ |
| Thư viện/gói npm | Người tiêu dùng nhận được tính năng tự động hoàn thành và kiểm tra kiểu | -- |
**Quy tắc chung**: Nếu dự án JavaScript của bạn có hơn vài trăm dòng, hãy sử dụng TypeScript.
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`type`và`interface`là gì và khi nào tôi nên sử dụng từng loại?
**A:** Cả hai đều xác định hình dạng đối tượng nhưng có các khả năng khác nhau. `interface`hỗ trợ hợp nhất khai báo (hợp nhất nhiều khai báo có cùng tên),`extends`để kế thừa và là lựa chọn thông thường cho các API công khai. `type`hỗ trợ các loại kết hợp, loại giao lộ, loại được ánh xạ, loại có điều kiện và loại chữ mẫu - mọi thứ nâng cao. Cách thực hành tốt nhất: sử dụng`interface`cho hình dạng đối tượng và API công khai; sử dụng`type`cho các công đoàn, tiện ích và các hoạt động loại phức tạp.
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

### Câu 2: Thuốc generic hoạt động như thế nào và tại sao chúng lại quan trọng?
**A:** Generics cho phép bạn viết các hàm, lớp và kiểu hoạt động với bất kỳ kiểu nào trong khi vẫn duy trì sự an toàn về kiểu. Thay vì`any`(làm mất thông tin loại), generics duy trì mối quan hệ giữa loại đầu vào và đầu ra. Chúng là nền tảng của mã an toàn loại, có thể tái sử dụng.
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

### Câu 3: Các loại tiện ích là gì và tôi nên biết những loại nào?
**A:** TypeScript cung cấp các loại tiện ích tích hợp sẵn để chuyển đổi các loại hiện có. Quan trọng nhất:`Partial<T>`(tất cả tùy chọn),`Required<T>`(tất cả bắt buộc),`Pick<T, K>`(chọn khóa),`Omit<T, K>`(loại trừ khóa),`Record<K, V>`(bản đồ khóa-giá trị),`Exclude<T, U>`(xóa khỏi liên kết),`ReturnType<T>`(loại trả về hàm trích xuất),`Awaited<T>`(Lời hứa mở ra). Tìm hiểu những điều này - chúng loại bỏ hầu hết nhu cầu về các hoạt động loại tùy chỉnh.
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

### Q4: Làm cách nào để nhập mã không đồng bộ và xử lý lỗi theo cách an toàn?
**A:** Hàm không đồng bộ tự động trả về`Promise<T>`trong đó T là loại trả về. Sử dụng`await`để mở khóa Lời hứa. Để xử lý lỗi, TypeScript không có ngoại lệ được gõ, nhưng bạn có thể tạo bộ bảo vệ kiểu và loại kết quả. "Mẫu kết quả" (lấy cảm hứng từ Rust) cung cấp khả năng xử lý lỗi thời gian biên dịch.
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

### Câu hỏi 5: Tệp khai báo (.d.ts) là gì và làm cách nào để sử dụng loại của bên thứ ba?
**A:** Tệp khai báo mô tả các loại thư viện JavaScript không có loại TypeScript tích hợp. Chúng chỉ chứa thông tin loại (không có mã thời gian chạy). Cài đặt các loại do cộng đồng duy trì từ DefiniteTyped:`npm install --save-dev @types/lodash`. Đối với thư viện của riêng bạn, hãy thêm trường`types`trong`package.json`hoặc bao gồm các tệp`.d.ts`cùng với nguồn của bạn. Sử dụng`declare module`để khai báo môi trường xung quanh.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xây dựng Trình phát sự kiện loại an toàn
**Báo cáo sự cố:** Tạo trình phát sự kiện chung, loại an toàn trong TypeScript trong đó mỗi tên sự kiện ánh xạ tới một loại tải trọng cụ thể. Trình biên dịch sẽ phát hiện tên sự kiện và loại tải trọng không chính xác tại thời điểm biên dịch.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần một hệ thống sự kiện trong đó: (1) sự kiện được xác định bằng loại tải trọng của chúng, (2)`emit`chỉ chấp nhận tên sự kiện hợp lệ với tải trọng chính xác, (3)`on`chỉ chấp nhận tên sự kiện hợp lệ với trình xử lý được nhập chính xác. Điều này yêu cầu các loại và khái quát được ánh xạ trên giao diện bản đồ sự kiện.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Xác định một loại `EventMap`: `{ [eventName: string]: payloadType }`.
- Sử dụng`keyof EventMap`để hạn chế tên sự kiện.
- Sử dụng`EventMap[K]`để lấy loại tải trọng cho một sự kiện cụ thể.
- Lưu trữ người nghe trong`Map<string, Function[]>`.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- An toàn về kiểu: trình biên dịch bắt sai tên sự kiện và hình dạng tải trọng sai tại thời điểm biên dịch.
-`on`trả về chức năng hủy đăng ký để dọn dẹp thuận tiện.
-`once`bao bọc người nghe để tự động hủy đăng ký sau lần gọi đầu tiên.
- Đối với sản xuất: thêm`listenerCount`,`removeAllListeners`và cân nhắc sử dụng`AbortSignal`để hủy.
### Vấn đề 2: Triển khai Trình tạo truy vấn SQL an toàn kiểu
**Báo cáo vấn đề:** Xây dựng trình tạo truy vấn SQL trong đó tên và loại cột được lấy từ giao diện TypeScript. Trình xây dựng phải ngăn chặn các tên cột không hợp lệ và kiểu nhập không khớp tại thời điểm biên dịch.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) tên cột bị ràng buộc ở `keyof T`, (2) các giá trị mệnh đề WHERE được nhập theo cột, (3) API có thể tạo chuỗi để xây dựng truy vấn. Điều này đòi hỏi thuốc generic bị ràng buộc bởi`Record<string, unknown>`.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`keyof T`cho các ràng buộc về tên cột.
- Sử dụng`T[K]`cho các ràng buộc về loại giá trị.
- Xây dựng chuỗi SQL với các truy vấn được tham số hóa (ngăn chặn việc tiêm SQL).
- Các phương thức có thể xâu chuỗi trả về`this`.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Ngăn chặn việc tiêm SQL: tất cả các giá trị đều trải qua các truy vấn được tham số hóa (`$1`,`$2`), không bao giờ được nội suy.
- An toàn kiểu: tên cột và kiểu giá trị được kiểm tra tại thời điểm biên dịch.
- Khả năng mở rộng: thêm các phương thức`join`,`groupBy`,`having`,`insert`,`update`theo cùng một mẫu.
- Sản xuất: sử dụng`kysely`hoặc`drizzle-orm`- chúng cung cấp sự an toàn cho loại này với phạm vi bảo hiểm SQL đầy đủ.
### Bài toán 3: Triển khai máy trạng thái hữu hạn với kiểu an toàn
**Báo cáo vấn đề:** Tạo một máy trạng thái hữu hạn an toàn về loại trong đó các chuyển đổi hợp lệ được thực thi tại thời điểm biên dịch. Mỗi trạng thái có thể có các hành động vào/ra và máy sẽ theo dõi trạng thái hiện tại.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng ta cần: (1) các trạng thái và sự kiện được xác định theo loại, (2) các chuyển đổi hợp lệ được ánh xạ ở cấp loại, (3) trình biên dịch ngăn chặn các chuyển đổi không hợp lệ, (4) theo dõi trạng thái thời gian chạy bằng các lệnh gọi lại. Điều này đòi hỏi các loại ánh xạ và các loại có điều kiện.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Xác định một`TransitionMap`:`{ [State]: { [Event]: NextState } }`.
- Sử dụng thuốc generic để hạn chế`send(event)`dựa trên trạng thái hiện tại.
- Theo dõi trạng thái khi chạy bằng một biến.
- Hỗ trợ gọi lại vào/ra theo từng trạng thái.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- An toàn trong thời gian chạy:`send`ném vào các chuyển tiếp không hợp lệ.
- An toàn loại: loại`EventsFor`trích xuất các sự kiện hợp lệ trên mỗi trạng thái tại thời điểm biên dịch.
- Lệnh gọi lại vào/ra tự động kích hoạt khi chuyển đổi.
- Đối với sản xuất: sử dụng`xstate`— nó cung cấp thư viện máy trạng thái đầy đủ với tính năng gỡ lỗi trực quan, trạng thái phân cấp, bảo vệ và hành động.
---

## Bản tóm tắt
TypeScript là JavaScript được thực hiện phù hợp cho mọi thứ ngoài các tập lệnh tầm thường. Nó bổ sung một hệ thống loại mạnh mẽ giúp phát hiện lỗi sớm, cải thiện công cụ và mã tài liệu -- tất cả trong khi biên dịch sang JavaScript tiêu chuẩn chạy ở mọi nơi. Quá trình học tập nhẹ nhàng (bạn có thể bắt đầu với các loại tối thiểu) nhưng có chiều sâu rất lớn (hệ thống loại là Turing-complete). Để phát triển JavaScript hiện đại, TypeScript đã trở thành tiêu chuẩn công nghiệp.