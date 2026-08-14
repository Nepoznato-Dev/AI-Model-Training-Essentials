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

# Типскрипт
TypeScript — это статически типизированный расширенный набор JavaScript, разработанный Microsoft (под руководством Андерса Хейлсберга) и впервые выпущенный в 2012 году. Он добавляет в JavaScript необязательные аннотации типов, интерфейсы, дженерики и расширенные функции системы типов, а затем компилируется в простой JavaScript, который запускается везде, где работает JavaScript. TypeScript не является отдельным языком или средой выполнения; это JavaScript с проверкой типов.
TypeScript стал стандартом для крупномасштабной разработки JavaScript. React, Angular, VS Code, Deno и большинство крупных проектов JavaScript с открытым исходным кодом написаны на TypeScript. Если вы начинаете новый проект JavaScript значительного размера, TypeScript рекомендуется использовать по умолчанию.
---

## Почему TypeScript важен
- **Отлавливает ошибки во время компиляции**: ошибки типов обнаруживаются до запуска кода, а не в рабочей среде.
- **Улучшенная поддержка IDE**: автозаполнение, переход к определению, рефакторинг и встроенная документация значительно улучшены.
- **Самодокументируемый код**: типы служат в качестве документации, которая постоянно обновляется.
- **100% совместимость с JavaScript**: любой допустимый JavaScript является допустимым TypeScript. Вы можете принять его постепенно.
- **Расширенная система типов**: типы объединения, типы пересечений, условные типы, сопоставленные типы, литеральные типы шаблонов — система типов достаточно выразительна для моделирования сложной логики предметной области.
- **Промышленное внедрение**: этого требует Angular; Экосистема React в подавляющем большинстве использует его; большинство новых пакетов npm поставляются с определениями типов.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Этап компиляции** | Перед запуском необходимо скомпилировать`.ts`→`.js`| Используйте `ts-node`/`tsx` для разработки; `tsc`для производства |
| **Кривая обучения** | Система типов может быть сложной (обобщенные, условные типы) | Начните с базовых типов; постепенно внедрять расширенные функции |
| **Файлы определения типа** | Не все пакеты npm поставляются с типами | Установите`@types/package-name`из DefinitelyTyped |
| **Время компиляции** | Проверка типа больших проектов может быть медленной | Используйте ссылки на проект`isolatedModules`или`swc`|
| **Ложное чувство безопасности** | Типы не гарантируют корректность во время выполнения | В сочетании с проверкой времени выполнения (Zod, io-ts) |
---

## Основы синтаксиса
### Аннотации базового типа
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

### Интерфейсы и типы
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

### Дженерики
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

### Расширенные типы
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

### Асинхронность с типами
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

## Расширенный синтаксис и шаблоны
### Расширенные дженерики
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

### Декораторы (стандарт TypeScript 5.0+)
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

### Типовые ограждения и сужение
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

## Параллелизм и параллелизм
TypeScript наследует модель параллелизма JavaScript, но добавляет безопасность типов в асинхронные шаблоны.
### Типизированные асинхронные шаблоны
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

## Конфигурация проекта и система сборки
### Структура каталога проекта
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

###`tsconfig.json`— конфигурация TypeScript
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

### Управление сборкой и пакетами
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

### Тестирование с помощью Vitest
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

### Конвейер CI/CD — Действия GitHub
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

## Расширенный синтаксис и шаблоны
### Расширенные дженерики
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

### Декораторы (TypeScript 5.0+)
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

### Типовые ограждения и сужение
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

## Конфигурация проекта и система сборки
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

### Тестирование с помощью Vitest
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

### Проверка времени выполнения с помощью Zod
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

## Совместимость
### Использование библиотек JavaScript
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

## Шаблоны проектирования
### Шаблон результата
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

### Шаблон репозитория
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

## Развертывание
### Докер-файл
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

## Экосистема
### Ключевые инструменты
| Инструмент | Цель |
|------|---------|
| **тск** | Компилятор TypeScript (официальный) |
| **ts-узел / tsx** | Запуск TypeScript напрямую без отдельной компиляции |
| **свк** | Сверхбыстрый компилятор TypeScript/JavaScript на основе Rust |
| **ESLint + typescript-eslint** | Линтинг с учетом типов правил |
| **Зод** | Проверка типа во время выполнения с выводом TypeScript |
| **tsconfig.json** | Файл конфигурации TypeScript |
### Фреймворки (все сначала TypeScript)
| Рамочная | Домен |
|-----------|--------|
| **Угловой** | Полнофункциональная интерфейсная платформа (требуется TypeScript) |
| **Next.js** | Метафреймворк React (в первую очередь TypeScript) |
| **NestJS** | Корпоративная серверная среда (в первую очередь TypeScript) |
| **тРПК** | Сквозные типобезопасные API (только TypeScript) |
| **Призма** | Типобезопасный ORM для Node.js |
---

## Когда использовать TypeScript
| Сценарий | Почему TypeScript | Лучшая альтернатива |
|----------|---------------|-------------------|
| Крупные проекты JavaScript | Типовая безопасность предотвращает целые категории ошибок | -- |
| Командные проекты | Типы служат общим контрактом | -- |
| Разработка API | Сквозная безопасность типов с помощью tRPC или OpenAPI | Go, Java для более простых REST API |
| Любой новый проект JavaScript | Стоимость добавления TypeScript позже высока | Обычный JS только для крошечных скриптов |
| Библиотеки/пакеты npm | Потребители получают автозаполнение и проверку типа | -- |
**Правило**: если ваш проект JavaScript содержит более нескольких сотен строк, используйте TypeScript.
---

## Синтетические вопросы и ответы
### Q1: В чем разница между`type`и`interface`и когда мне следует использовать каждый из них?
**О:** Оба определяют формы объектов, но имеют разные возможности. `interface`поддерживает слияние объявлений (слияние нескольких объявлений с одинаковыми именами),`extends`для наследования и является идиоматическим выбором для общедоступных API. `type`поддерживает типы объединения, типы пересечений, отображаемые типы, условные типы и литеральные типы шаблонов — все, что является продвинутым. Рекомендации: используйте`interface`для фигур объектов и общедоступных API; используйте`type`для объединений, утилит и операций со сложными типами.
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

### Вопрос 2. Как работают дженерики и почему они важны?
**О:** Обобщенные шаблоны позволяют писать функции, классы и типы, которые работают с любыми типами, сохраняя при этом безопасность типов. Вместо`any`(который теряет информацию о типе) дженерики сохраняют связь между входными и выходными типами. Они являются основой многоразового, типобезопасного кода.
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

### Q3: Что такое типы утилит и какие из них мне следует знать?
**A:** TypeScript предоставляет встроенные служебные типы, преобразующие существующие типы. Наиболее важные:`Partial<T>`(все необязательные),`Required<T>`(все обязательные),`Pick<T, K>`(выбрать ключи),`Omit<T, K>`(исключить ключи),`Record<K, V>`(сопоставление ключ-значение),`Exclude<T, U>`(удалить из объединения),`ReturnType<T>`(извлечь тип возвращаемого значения функции),`Awaited<T>`(развернуть обещание). Изучите их — они устраняют большую часть необходимости в операциях с пользовательскими типами.
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

### Вопрос 4. Как вводить асинхронный код и обрабатывать ошибки типобезопасным способом?
**A:** Асинхронные функции автоматически возвращают `Promise<T>`, где T — тип возвращаемого значения. Используйте `await`, чтобы развернуть обещание. Для обработки ошибок TypeScript не имеет типизированных исключений, но вы можете создавать средства защиты типов и типы результатов. «Шаблон результата» (вдохновленный Rust) обеспечивает обработку ошибок во время компиляции.
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

### Вопрос 5. Что такое файлы объявлений (.d.ts) и как использовать сторонние типы?
**A:** Файлы объявлений описывают типы библиотек JavaScript, которые не имеют встроенных типов TypeScript. Они содержат только информацию о типе (без кода времени выполнения). Установите поддерживаемые сообществом типы из DefinitelyTyped: `npm install --save-dev @types/lodash`. Для ваших собственных библиотек добавьте поле`types`в`package.json`или включите файлы`.d.ts`вместе с исходным кодом. Используйте`declare module`для внешних объявлений.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создайте типобезопасный генератор событий
**Постановка задачи.** Создайте универсальный типобезопасный источник событий в TypeScript, где каждое имя события сопоставляется с конкретным типом полезных данных. Компилятор должен обнаруживать неверные имена событий и типы полезных данных во время компиляции.
**Шаг 1. Поймите проблему:**
Нам нужна система событий, в которой: (1) события определяются с помощью их типов полезных данных, (2)`emit`принимает только действительные имена событий с правильными полезными данными, (3)`on`принимает только действительные имена событий с правильно типизированными обработчиками. Для этого требуются сопоставленные типы и дженерики через интерфейс карты событий.
**Шаг 2. Определите подход:**
- Определите тип `EventMap`:`{ [eventName: string]: payloadType }`.
- Используйте `keyof EventMap`, чтобы ограничить имена событий.
– Используйте `EventMap[K]`, чтобы получить тип полезной нагрузки для определенного события.
— Сохраните прослушиватели в `Map<string, Function[]>`.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Типовая безопасность: компилятор распознает неправильные имена событий и неправильные формы полезных данных во время компиляции.
-`on`возвращает функцию отказа от подписки для удобной очистки.
-`once`переносит прослушиватель на автоматическую отмену подписки после первого вызова.
- Для производства: добавьте`listenerCount`,`removeAllListeners`и рассмотрите возможность использования`AbortSignal`для отмены.
### Проблема 2. Реализация типобезопасного построителя SQL-запросов
**Постановка задачи.** Создайте построитель SQL-запросов, в котором имена и типы столбцов будут получены из интерфейса TypeScript. Разработчик должен предотвратить недопустимые имена столбцов и несоответствия типов во время компиляции.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) имена столбцов, ограниченные`keyof T`, (2) значения предложения WHERE, введенные в соответствии со столбцом, (3) API для построения цепочек для построения запросов. Для этого требуются дженерики, ограниченные`Record<string, unknown>`.
**Шаг 2. Определите подход:**
- Используйте`keyof T`для ограничений имени столбца.
- Используйте`T[K]`для ограничений типа значения.
- Создайте строку SQL с параметризованными запросами (предотвратите внедрение SQL).
— Цепные методы возвращают `this`.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Предотвращение SQL-инъекций: все значения проходят через параметризованные запросы (`$1`,`$2`) и никогда не интерполируются.
— Безопасность типов: имена столбцов и типы значений проверяются во время компиляции.
- Расширяемость: добавьте методы `join`, `groupBy`, `having`, `insert`,`update`по тому же шаблону.
- Производство: используйте`kysely`или`drizzle-orm`— они обеспечивают безопасность этого типа с полным покрытием SQL.
### Проблема 3: реализация конечного автомата с типобезопасностью
**Постановка задачи:** Создайте типобезопасный конечный автомат, в котором допустимые переходы реализуются во время компиляции. Каждое состояние может иметь действия входа/выхода, и машина должна отслеживать текущее состояние.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) состояния и события, определенные как типы, (2) допустимые переходы, отображаемые на уровне типа, (3) компилятор предотвращает недопустимые переходы, (4) отслеживание состояний во время выполнения с помощью обратных вызовов. Для этого требуются отображаемые типы и условные типы.
**Шаг 2. Определите подход:**
- Определите `TransitionMap`: `{ [State]: { [Event]: NextState } }`.
— Используйте дженерики для ограничения`send(event)`на основе текущего состояния.
- Отслеживание состояния во время выполнения с помощью переменной.
- Поддержка обратных вызовов входа/выхода для каждого состояния.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Безопасность во время выполнения:`send`выдает ошибку при недопустимых переходах.
- Типовая безопасность: тип`EventsFor`извлекает допустимые события для каждого состояния во время компиляции.
- Обратные вызовы входа/выхода срабатывают автоматически при переходах.
- Для производства: используйте`xstate`— он предоставляет полную библиотеку конечных автоматов с визуальной отладкой, иерархическими состояниями, средствами защиты и действиями.
---

## Краткое содержание
TypeScript — это JavaScript, созданный специально для всего, что выходит за рамки тривиальных сценариев. Он добавляет мощную систему типов, которая рано выявляет ошибки, улучшает инструменты и документирует код — и все это при компиляции в стандартный JavaScript, который работает где угодно. Кривая обучения невелика (вы можете начать с минимальных типов), но глубина огромна (система типов является полной по Тьюрингу). Для современной разработки JavaScript TypeScript стал отраслевым стандартом.