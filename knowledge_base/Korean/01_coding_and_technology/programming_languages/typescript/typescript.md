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
# 타입스크립트
TypeScript는 Microsoft(Anders Hejlsberg 주도)에서 개발하고 2012년에 처음 출시된 정적으로 유형이 지정된 JavaScript의 상위 집합입니다. JavaScript에 선택적 유형 주석, 인터페이스, 제네릭 및 고급 유형 시스템 기능을 추가한 다음 JavaScript가 실행되는 모든 곳에서 실행되는 일반 JavaScript로 컴파일됩니다. TypeScript는 별도의 언어나 런타임이 아닙니다. 유형 검사기가 있는 JavaScript입니다.
TypeScript는 대규모 JavaScript 개발의 표준이 되었습니다. React, Angular, VS Code, Deno 및 대부분의 주요 오픈 소스 JavaScript 프로젝트는 TypeScript로 작성되었습니다. 상당한 크기의 새 JavaScript 프로젝트를 시작하는 경우 TypeScript가 권장되는 기본값입니다.
---

## TypeScript가 중요한 이유
- **컴파일 시 버그 잡기**: 유형 오류는 코드가 실행되기 전에 발견되며 프로덕션에서는 발견되지 않습니다.
- **더 나은 IDE 지원**: 자동 완성, 정의로 이동, 리팩토링 및 인라인 문서화가 모두 크게 향상됩니다.
- **자체 문서화 코드**: 유형은 최신 상태로 유지되는 문서 역할을 합니다.
- **100% JavaScript 호환**: 유효한 모든 JavaScript는 유효한 TypeScript입니다. 점차적으로 채택할 수 있습니다.
- **고급 유형 시스템**: 통합 유형, 교차 유형, 조건 유형, 매핑 유형, 템플릿 리터럴 유형 — 유형 시스템은 복잡한 도메인 논리를 모델링하기에 충분히 표현력이 뛰어납니다.
- **업계 채택**: Angular에서는 이를 요구합니다. React 생태계에서는 이를 압도적으로 사용합니다. 대부분의 새로운 npm 패키지는 유형 정의와 함께 제공됩니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **컴파일 단계** | 실행하기 전에`.ts`→ `.js`를 컴파일해야 합니다. 개발에는`ts-node`/ `tsx`를 사용하세요.  생산용`tsc`|
| **학습 곡선** | 유형 시스템은 복잡할 수 있습니다(제네릭, 조건부 유형) | 기본 유형부터 시작하세요. 고급 기능을 점진적으로 채택 |
| **유형 정의 파일** | 모든 npm 패키지가 유형과 함께 제공되는 것은 아닙니다 | DefinedTyped에서`@types/package-name`설치 |
| **컴파일 시간** | 대규모 프로젝트에서는 유형 확인이 느려질 수 있습니다 | 프로젝트 참조,`isolatedModules`또는`swc`사용 |
| **잘못된 안보의식** | 유형은 런타임 정확성을 보장하지 않습니다 | 런타임 유효성 검사와 결합(Zod, io-ts) |
---

## 구문 기본 사항
### 기본 유형 주석
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

### 인터페이스 및 유형
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

### 제네릭
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

### 고급 유형
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

### 유형과 비동기화
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

## 고급 구문 및 패턴
### 고급 제네릭
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

### 데코레이터(TypeScript 5.0+ 표준)
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

### 유형 가드 및 축소
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

## 동시성 및 병렬성
TypeScript는 JavaScript의 동시성 모델을 상속하지만 비동기 패턴에 유형 안전성을 추가합니다.
### 형식화된 비동기 패턴
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 디렉터리 구조
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

###`tsconfig.json`— TypeScript 구성
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

### 빌드 및 패키지 관리
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

### Vitest로 테스트하기
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

### CI/CD 파이프라인 — GitHub Actions
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

## 고급 구문 및 패턴
### 고급 제네릭
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

### 데코레이터(TypeScript 5.0+)
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

### 유형 가드 및 축소
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

## 프로젝트 구성 및 빌드 시스템
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

### Vitest로 테스트하기
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

### Zod를 사용한 런타임 검증
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

## 상호 운용성
### JavaScript 라이브러리 사용
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

## 디자인 패턴
### 결과 패턴
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

### 저장소 패턴
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

## 배포
### 도커파일
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

## 생태계
### 주요 도구
| 도구 | 목적 |
|------|---------|
| **tsc** | TypeScript 컴파일러(공식) |
| **ts-노드 / tsx** | 별도의 컴파일 없이 TypeScript 직접 실행 |
| **swc** | 초고속 Rust 기반 TypeScript/JavaScript 컴파일러 |
| **ESLint + typescript-eslint** | 유형 인식 규칙을 사용한 Linting |
| **조드** | TypeScript 추론을 통한 런타임 유형 검증 |
| **tsconfig.json** | TypeScript 구성 파일 |
### 프레임워크(모든 TypeScript 우선)
| 프레임워크 | 도메인 |
|------------|---------|
| **각도** | 모든 기능을 갖춘 프런트엔드 프레임워크(TypeScript 필요) |
| **다음.js** | React 메타 프레임워크(TypeScript 우선) |
| **NestJS** | 엔터프라이즈 백엔드 프레임워크(TypeScript 우선) |
| **tRPC** | 엔드투엔드 형식 안전 API(TypeScript 전용) |
| **프리즈마** | Node.js용 유형 안전 ORM |
---

## TypeScript를 사용해야 하는 경우
| 시나리오 | TypeScript를 사용해야 하는 이유 | 더 나은 대안 |
|------------|---------------|------|
| 대규모 JavaScript 프로젝트 | 유형 안전성은 전체 버그 범주를 방지합니다 | -- |
| 팀 프로젝트 | 유형은 공유 계약 역할을 합니다 | -- |
| API 개발 | tRPC 또는 OpenAPI를 통한 엔드투엔드 유형의 안전성 | 더 간단한 REST API를 위한 Go, Java |
| 새로운 JavaScript 프로젝트 | 나중에 TypeScript를 추가하는 데 드는 비용이 높습니다 | 작은 스크립트 전용 일반 JS |
| 라이브러리/npm 패키지 | 소비자는 자동 완성 및 유형 검사를 받습니다. | -- |
**경험 법칙**: JavaScript 프로젝트에 수백 줄이 넘는 경우 TypeScript를 사용하세요.
---

## 종합 Q&A
### Q1:`type`와`interface`의 차이점은 무엇이며 언제 사용해야 합니까?
**답변:** 둘 다 객체 모양을 정의하지만 기능이 다릅니다.  `interface`는 선언 병합(동일한 이름 병합을 가진 여러 선언), 상속을 위한 `extends`를 지원하며 공용 API에 대한 관용적 선택입니다.  `type`는 통합 유형, 교차 유형, 매핑 유형, 조건 유형 및 템플릿 리터럴 유형 등 모든 고급 기능을 지원합니다. 모범 사례: 객체 모양 및 공용 API에는 `interface`를 사용합니다. 공용체, 유틸리티 및 복합 유형 작업에는 `type`를 사용하세요.
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

### Q2: 제네릭은 어떻게 작동하며 왜 중요한가요?
**답:** 제네릭을 사용하면 유형 안전성을 유지하면서 모든 유형에서 작동하는 함수, 클래스 및 유형을 작성할 수 있습니다. `any`(유형 정보 손실) 대신 제네릭은 입력 유형과 출력 유형 간의 관계를 유지합니다. 이는 재사용 가능하고 유형이 안전한 코드의 기초입니다.
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

### Q3: 유틸리티 유형은 무엇이며, 어떤 유형을 알아야 합니까?
**A:** TypeScript는 기존 유형을 변환하는 내장 유틸리티 유형을 제공합니다. 가장 중요한 것: `Partial<T>`(모두 선택 사항), `Required<T>`(모두 필수), `Pick<T, K>`(키 선택), `Omit<T, K>`(키 제외), `Record<K, V>`(키-값 맵), `Exclude<T, U>`(결합에서 제거), `ReturnType<T>`(함수 반환 유형 추출), `Awaited<T>`(프라미스 풀기). 이를 배우면 사용자 정의 유형 작업이 거의 필요하지 않습니다.
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

### Q4: 비동기 코드를 입력하고 유형이 안전한 방식으로 오류를 처리하려면 어떻게 해야 하나요?
**A:** 비동기 함수는 자동으로 `Promise<T>`를 반환합니다. 여기서 T는 반환 유형입니다. Promise를 풀려면 `await`를 사용하세요. 오류 처리를 위해 TypeScript에는 유형화된 예외가 없지만 유형 가드 및 결과 유형을 만들 수 있습니다. "결과 패턴"(Rust에서 영감을 얻었음)은 컴파일 시간 오류 처리를 제공합니다.
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

### Q5: 선언 파일(.d.ts)이란 무엇이며 타사 유형을 어떻게 사용합니까?
**A:** 선언 파일은 내장된 TypeScript 유형이 없는 JavaScript 라이브러리의 유형을 설명합니다. 여기에는 유형 정보만 포함됩니다(런타임 코드 없음). DefinedTyped:`npm install --save-dev @types/lodash`에서 커뮤니티가 관리하는 유형을 설치합니다. 자신의 라이브러리의 경우 `package.json`에`types`필드를 추가하거나 소스와 함께`.d.ts`파일을 포함하세요. 앰비언트 선언에는 `declare module`를 사용하세요.
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

## 사고 사슬 문제 해결
### 문제 1: 유형이 안전한 이벤트 이미터 구축
**문제 설명:** 각 이벤트 이름이 특정 페이로드 유형에 매핑되는 TypeScript에서 일반 유형 안전 이벤트 이미터를 만듭니다. 컴파일러는 컴파일 타임에 잘못된 이벤트 이름과 페이로드 유형을 포착해야 합니다.
**1단계 - 문제 이해:**
(1) 이벤트가 페이로드 유형으로 정의되고, (2) `emit`가 올바른 페이로드가 있는 유효한 이벤트 이름만 허용하고, (3) `on`가 올바른 유형의 핸들러가 있는 유효한 이벤트 이름만 허용하는 이벤트 시스템이 필요합니다. 이를 위해서는 이벤트 맵 인터페이스를 통한 매핑된 유형과 제네릭이 필요합니다.
**2단계 - 접근 방식 파악:**
-`EventMap`유형을 정의합니다:`{ [eventName: string]: payloadType }`.
- 이벤트 이름을 제한하려면 `keyof EventMap`를 사용하세요.
- `EventMap[K]`를 사용하여 특정 이벤트에 대한 페이로드 유형을 가져옵니다.
- `Map<string, Function[]>`에 리스너를 저장합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 유형 안전성: 컴파일러는 컴파일 타임에 잘못된 이벤트 이름과 잘못된 페이로드 형태를 포착합니다.
- `on`는 편리한 정리를 위해 구독 취소 기능을 반환합니다.
- `once`는 첫 번째 호출 후 자동 구독 취소를 위해 리스너를 래핑합니다.
- 프로덕션의 경우:`listenerCount`,`removeAllListeners`를 추가하고, 취소하려면`AbortSignal`사용을 고려하세요.
### 문제 2: 유형이 안전한 SQL 쿼리 빌더 구현
**문제 설명:** 열 이름과 유형이 TypeScript 인터페이스에서 파생되는 SQL 쿼리 빌더를 빌드합니다. 빌더는 컴파일 시 잘못된 열 이름과 유형 불일치를 방지해야 합니다.
**1단계 - 문제 이해:**
(1)`keyof T`로 제한된 열 이름, (2) 열에 따라 입력된 WHERE 절 값, (3) 쿼리 작성을 위한 연결 가능한 API가 필요합니다. 이를 위해서는`Record<string, unknown>`로 제한된 제네릭이 필요합니다.
**2단계 - 접근 방식 파악:**
- 열 이름 제약 조건에는 `keyof T`를 사용합니다.
- 값 유형 제약 조건에는 `T[K]`를 사용합니다.
- 매개변수화된 쿼리로 SQL 문자열을 작성합니다(SQL 주입 방지).
- 연결 가능한 메서드는`this`를 반환합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- SQL 주입 방지: 모든 값은 매개변수화된 쿼리(`$1`,`$2`)를 거치며 삽입되지 않습니다.
- 유형 안전성: 열 이름과 값 유형은 컴파일 타임에 확인됩니다.
- 확장성: 동일한 패턴에 따라`join`,`groupBy`,`having`,`insert`,`update`메서드를 추가합니다.
- 프로덕션:`kysely`또는 `drizzle-orm`를 사용합니다. 이는 전체 SQL 적용 범위에서 이러한 유형의 안전성을 제공합니다.
### 문제 3: 유형 안전성을 갖춘 유한 상태 머신 구현
**문제 설명:** 컴파일 타임에 유효한 전환이 적용되는 유형이 안전한 유한 상태 머신을 만듭니다. 각 상태에는 시작/종료 작업이 있을 수 있으며 머신은 현재 상태를 추적해야 합니다.
**1단계 - 문제 이해:**
(1) 유형으로 정의된 상태 및 이벤트, (2) 유형 수준에서 매핑된 유효한 전환, (3) 컴파일러가 잘못된 전환을 방지하고, (4) 콜백을 통한 런타임 상태 추적이 필요합니다. 이를 위해서는 매핑된 유형과 조건부 유형이 필요합니다.
**2단계 - 접근 방식 파악:**
-`TransitionMap`: `{ [State]: { [Event]: NextState } }`를 정의합니다.
- 제네릭을 사용하여 현재 상태를 기반으로 `send(event)`를 제한합니다.
- 변수를 사용하여 런타임 시 상태를 추적합니다.
- 상태별 진입/퇴장 콜백을 지원합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 런타임 안전: `send`는 유효하지 않은 전환을 발생시킵니다.
- 유형 안전성:`EventsFor`유형은 컴파일 타임에 상태별로 유효한 이벤트를 추출합니다.
- 전환 시 진입/종료 콜백이 자동으로 실행됩니다.
- 프로덕션의 경우: `xstate`를 사용하세요. 시각적 디버깅, 계층적 상태, 가드 및 작업이 포함된 전체 상태 머신 라이브러리를 제공합니다.
---

## 요약
TypeScript는 사소한 스크립트 이상의 모든 작업에 적합하게 수행되는 JavaScript입니다. 버그를 조기에 포착하고, 도구를 개선하고, 코드를 문서화하는 강력한 유형 시스템을 추가하는 동시에 어디서나 실행되는 표준 JavaScript로 컴파일합니다. 학습 곡선은 완만하지만(최소 유형으로 시작할 수 있음) 깊이는 넓습니다(유형 시스템은 Turing-complete입니다). 최신 JavaScript 개발에서는 TypeScript가 업계 표준이 되었습니다.