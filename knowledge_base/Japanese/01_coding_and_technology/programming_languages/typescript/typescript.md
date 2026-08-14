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
TypeScript は、Microsoft (Anders Hejlsberg 率いる) によって開発され、2012 年に初めてリリースされた JavaScript の静的に型付けされたスーパーセットです。TypeScript は、オプションの型アノテーション、インターフェイス、ジェネリックス、高度な型システム機能を JavaScript に追加し、JavaScript が実行される場所ならどこでも実行できるプレーンな JavaScript にコンパイルします。 TypeScript は別個の言語やランタイムではありません。それは型チェッカーを備えた JavaScript です。
TypeScript は、大規模な JavaScript 開発の標準となっています。 React、Angular、VS Code、Deno、およびほとんどの主要なオープンソース JavaScript プロジェクトは TypeScript で書かれています。何らかの大きなサイズの新しい JavaScript プロジェクトを開始する場合は、TypeScript がデフォルトとして推奨されます。
---

## TypeScript が重要な理由
- **コンパイル時にバグを検出**: 型エラーはコードが実行される前に検出されます (運用環境では検出されません)。
- **IDE サポートの向上**: オートコンプリート、定義への移動、リファクタリング、およびインライン ドキュメントのすべてが大幅に改善されました。
- **自己文書化コード**: 型は最新の状態を保つドキュメントとして機能します。
- **100% JavaScript 互換**: 有効な JavaScript はすべて有効な TypeScript です。徐々に取り入れていくことも可能です。
- **高度な型システム**: 共用型、交差型、条件付き型、マップされた型、テンプレート リテラル型 - 型システムは、複雑なドメイン ロジックをモデル化するのに十分な表現力を持っています。
- **業界での採用**: Angular ではこれが必要です。 React エコシステムでは圧倒的にこれが使用されています。ほとんどの新しい npm パッケージには型定義が付属しています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **コンパイル手順** |実行する前に`.ts`→`.js`をコンパイルする必要があります。開発には`ts-node`/`tsx`を使用します。  実稼働用`tsc`|
| **学習曲線** |型システムは複雑になる可能性があります (ジェネリック、条件付き型)。基本的なタイプから始めます。高度な機能を段階的に採用 |
| **タイプ定義ファイル** |すべての npm パッケージにタイプが付属しているわけではありません。 DefinitelyTyped から`@types/package-name`をインストールする |
| **コンパイル時間** |大規模なプロジェクトでは型チェックが遅くなる可能性があります。プロジェクト参照`isolatedModules`または`swc`を使用します。
| **誤った安心感** |型は実行時の正確性を保証しません。ランタイム検証と組み合わせる (Zod、io-ts) |
---

## 構文の基礎
### 基本的な型の注釈
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

### インターフェースとタイプ
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

### ジェネリック医薬品
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

### 高度なタイプ
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

### 型との非同期
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

## 高度な構文とパターン
### 高度なジェネリックス
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

### デコレータ (TypeScript 5.0+ 標準)
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

### タイプガードとナローイング
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

## 同時実行性と並列処理
TypeScript は JavaScript の同時実行モデルを継承していますが、非同期パターンにタイプ セーフティを追加します。
### 型付き非同期パターン
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

## プロジェクトの構成とシステムの構築
### プロジェクトのディレクトリ構造
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

###`tsconfig.json`— TypeScript の構成
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

### ビルドとパッケージの管理
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

### Vitest を使用したテスト
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

### CI/CD パイプライン — GitHub アクション
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

## 高度な構文とパターン
### 高度なジェネリックス
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

### デコレータ (TypeScript 5.0 以降)
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

### タイプガードとナローイング
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

## プロジェクト構成とビルドシステム
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

### Vitest を使用したテスト
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

### Zod を使用したランタイム検証
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

## 相互運用性
### JavaScript ライブラリの使用
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

## デザインパターン
### 結果パターン
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

### リポジトリ パターン
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

## デプロイメント
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

## エコシステム
### 主要なツール
|ツール |目的 |
|-----|----------|
| **tsc** | TypeScript コンパイラ (公式) |
| **ts-node / tsx** |別途コンパイルせずに TypeScript を直接実行します。
| **SWC** |超高速 Rust ベースの TypeScript/JavaScript コンパイラ |
| **ESLint + typescript-eslint** |型認識ルールによるリンティング |
| **ゾッド** | TypeScript 推論によるランタイム型検証 |
| **tsconfig.json** | TypeScript 設定ファイル |
### フレームワーク (すべて TypeScript ファースト)
|フレームワーク |ドメイン |
|----------|----------|
| **角度** |フル機能のフロントエンド フレームワーク (TypeScript が必要) |
| **Next.js** | React メタフレームワーク (TypeScript ファースト) |
| **NestJS** |エンタープライズ バックエンド フレームワーク (TypeScript ファースト) |
| **tRPC** |エンドツーエンドのタイプセーフ API (TypeScript のみ) |
| **プリズマ** | Node.js のタイプセーフ ORM |
---

## TypeScript を使用する場合
|シナリオ | TypeScript を選ぶ理由 |より良い代替案 |
|----------|------|--------|
|大規模な JavaScript プロジェクト |型安全性は、あらゆるカテゴリーのバグを防止します。 -- |
|チームプロジェクト |タイプは共有コントラクトとして機能します。 -- |
| API開発 | tRPC または OpenAPI によるエンドツーエンドのタイプ セーフティ |より単純な REST API には Java を使用してください |
|新しい JavaScript プロジェクト | TypeScript を後から追加するとコストが高くなります。小さなスクリプトのみのプレーン JS |
|ライブラリ / npm パッケージ |コンシューマーはオートコンプリートと型チェックを取得します。 -- |
**経験則**: JavaScript プロジェクトに数百行を超える場合は、TypeScript を使用してください。
---

## 総合的な Q&A
### Q1:`type`と`interface`の違いは何ですか?それぞれをいつ使用する必要がありますか?
**A:** どちらもオブジェクトの形状を定義しますが、機能が異なります。 `interface`は宣言のマージ (同じ名前の複数の宣言のマージ)、`extends` の継承をサポートしており、パブリック API の慣用的な選択肢です。 `type`は、共用体タイプ、交差タイプ、マップされたタイプ、条件付きタイプ、およびテンプレート リテラル タイプなど、あらゆる高度なタイプをサポートします。ベスト プラクティス: オブジェクト シェイプとパブリック API には`interface`を使用します。共用体、ユーティリティ、複合型の演算には`type`を使用します。
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

### Q2: ジェネリック医薬品はどのように機能し、なぜ重要ですか?
**A:** ジェネリックを使用すると、型の安全性を維持しながら、任意の型で動作する関数、クラス、および型を作成できます。`any`(型情報が失われます) の代わりに、ジェネリックは入力型と出力型の間の関係を保持します。これらは、再利用可能でタ​​イプセーフなコードの基礎です。
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

### Q3: ユーティリティ タイプとは何ですか?どれについて知っておくべきですか?
**A:** TypeScript は、既存の型を変換する組み込みのユーティリティ型を提供します。最も重要なもの:`Partial<T>`(すべてオプション)、`Required<T>` (すべて必須)、`Pick<T, K>` (キーの選択)、`Omit<T, K>` (キーの除外)、`Record<K, V>` (キーと値のマップ)、`Exclude<T, U>` (共用体からの削除)、`ReturnType<T>` (関数の戻り値の抽出)タイプ)、`Awaited<T>` (Promise のラップ解除)。これらを学習すると、カスタム タイプの操作のほとんどが不要になります。
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

### Q4: 非同期コードを入力し、タイプセーフな方法でエラーを処理するにはどうすればよいですか?
**A:** 非同期関数は自動的に`Promise<T>`を返します。T は戻り値の型です。`await`を使用して Promise をアンラップします。エラー処理については、TypeScript には型指定された例外がありませんが、タイプ ガードと結果の型を作成できます。 「結果パターン」(Rust からインスピレーションを得た) は、コンパイル時のエラー処理を提供します。
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

### Q5: 宣言ファイル (.d.ts) とは何ですか?また、サードパーティのタイプを使用するにはどうすればよいですか?
**A:** 宣言ファイルには、TypeScript 型が組み込まれていない JavaScript ライブラリの種類が記述されています。これらには型情報のみが含まれます (ランタイム コードは含まれません)。 DefinitelyTyped:`npm install --save-dev @types/lodash`からコミュニティが管理するタイプをインストールします。独自のライブラリの場合は、`package.json` に`types`フィールドを追加するか、ソースと一緒に`.d.ts`ファイルを含めます。アンビエント宣言には`declare module`を使用します。
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

## 思考連鎖による問題解決
### 問題 1: タイプセーフなイベント エミッターを構築する
**問題ステートメント:** TypeScript で、各イベント名が特定のペイロード タイプにマップされる汎用のタイプセーフ イベント エミッターを作成します。コンパイラは、コンパイル時に間違ったイベント名とペイロード タイプを検出する必要があります。
**ステップ 1 — 問題を理解する:**
イベント システムが必要です。(1) イベントはペイロード タイプで定義され、(2)`emit`は正しいペイロードを持つ有効なイベント名のみを受け入れます。(3)`on`は正しく型指定されたハンドラーを持つ有効なイベント名のみを受け入れます。これには、イベント マップ インターフェイスを介してマップされた型とジェネリックスが必要です。
**ステップ 2 — アプローチを特定する:**
-`EventMap`タイプを定義します:`{ [eventName: string]: payloadType }`。
- イベント名を制約するには、`keyof EventMap` を使用します。
-`EventMap[K]`を使用して、特定のイベントのペイロード タイプを取得します。
- リスナーを`Map<string, Function[]>`に保存します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- タイプ セーフティ: コンパイラは、コンパイル時に間違ったイベント名と間違ったペイロード形状を検出します。
-`on`は、便利なクリーンアップのために購読解除関数を返します。
-`once`は、最初の呼び出し後に自動サブスクライブ解除するようにリスナーをラップします。
- 本番環境の場合:`listenerCount`、`removeAllListeners`を追加し、キャンセルには`AbortSignal`の使用を検討してください。
### 問題 2: タイプセーフな SQL クエリ ビルダーを実装する
**問題ステートメント:** 列名と型が TypeScript インターフェイスから派生する SQL クエリ ビルダーを構築します。ビルダーは、コンパイル時に無効な列名と型の不一致を防ぐ必要があります。
**ステップ 1 — 問題を理解する:**
(1)`keyof T`に制約された列名、(2) 列に従って型指定された WHERE 句の値、(3) クエリを構築するためのチェーン可能な API が必要です。これには、`Record<string, unknown>`によって制約されたジェネリックスが必要です。
**ステップ 2 — アプローチを特定する:**
- 列名の制約には`keyof T`を使用します。
- 値型制約には`T[K]`を使用します。
- パラメータ化されたクエリを使用して SQL 文字列を構築します (SQL インジェクションを防止します)。
- チェーン可能なメソッドは`this`を返します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- SQL インジェクション防止: すべての値はパラメータ化されたクエリ (`$1`、`$2`) を通過し、補間されることはありません。
- 型安全性: 列名と値の型はコンパイル時にチェックされます。
- 拡張性: 同じパターンに従って`join`、`groupBy`、`having`、`insert`、`update`メソッドを追加します。
- 本番環境:`kysely`または`drizzle-orm`を使用します。これらは、完全な SQL カバレッジでこの型安全性を提供します。
### 問題 3: タイプ セーフティを備えた有限ステート マシンを実装する
**問題ステートメント:** コンパイル時に有効な遷移が強制される、タイプセーフな有限状態マシンを作成します。各状態には開始/終了アクションを持つことができ、マシンは現在の状態を追跡する必要があります。
**ステップ 1 — 問題を理解する:**
(1) 型として定義された状態とイベント、(2) 型レベルでマップされた有効な遷移、(3) コンパイラによる無効な遷移の防止、(4) コールバックによるランタイム状態の追跡が必要です。これには、マップされた型と条件付き型が必要です。
**ステップ 2 — アプローチを特定する:**
-`TransitionMap`:`{ [State]: { [Event]: NextState } }`を定義します。
- ジェネリックスを使用して、現在の状態に基づいて`send(event)`を制約します。
- 実行時に変数を使用して状態を追跡します。
- 状態ごとの入口/出口コールバックをサポートします。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- ランタイムの安全性: 無効な遷移では`send`がスローされます。
- タイプ セーフティ:`EventsFor`タイプは、コンパイル時に状態ごとに有効なイベントを抽出します。
- 開始/終了コールバックは遷移時に自動的に起動されます。
- 運用環境の場合:`xstate`を使用します。これは、視覚的なデバッグ、階層状態、ガード、およびアクションを備えた完全なステート マシン ライブラリを提供します。
---

＃＃ まとめ
TypeScript は、単純なスクリプトを超えてあらゆる用途に適した JavaScript です。どこでも実行できる標準 JavaScript にコンパイルしながら、バグを早期に検出し、ツールを改善し、コードを文書化する強力な型システムが追加されます。学習曲線は緩やかですが (最小限の型から始めることができます)、その奥深さは広大です (型システムはチューリング完全です)。最新の JavaScript 開発では、TypeScript が業界標準になっています。