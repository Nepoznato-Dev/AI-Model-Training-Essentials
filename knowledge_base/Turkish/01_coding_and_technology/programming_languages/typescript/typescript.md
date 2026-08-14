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
TypeScript, Microsoft (Anders Hejlsberg öncülüğünde) tarafından geliştirilen ve ilk kez 2012'de piyasaya sürülen, statik olarak yazılan bir JavaScript üst kümesidir. JavaScript'e isteğe bağlı tür açıklamaları, arayüzler, jenerikler ve gelişmiş tür sistemi özellikleri ekler ve ardından JavaScript'in çalıştığı her yerde çalışan düz JavaScript'e derler. TypeScript ayrı bir dil veya çalışma zamanı değildir; tür denetleyicili JavaScript'tir.
TypeScript, büyük ölçekli JavaScript geliştirmenin standardı haline geldi. React, Angular, VS Code, Deno ve çoğu büyük açık kaynaklı JavaScript projesi TypeScript'te yazılmıştır. Önemli boyutta yeni bir JavaScript projesi başlatıyorsanız TypeScript önerilen varsayılandır.
---

## TypeScript Neden Önemlidir
- **Hataları derleme sırasında yakalar**: Tür hataları, üretim sırasında değil, kod çalıştırılmadan önce bulunur.
- **Daha iyi IDE desteği**: Otomatik tamamlama, tanıma gitme, yeniden düzenleme ve satır içi belgelemenin tümü önemli ölçüde iyileşir.
- **Kendi kendini belgeleyen kod**: Türler, güncel kalan belgeler görevi görür.
- **%100 JavaScript uyumlu**: Geçerli herhangi bir JavaScript, geçerli TypeScript'tir. Yavaş yavaş benimseyebilirsiniz.
- **Gelişmiş tür sistemi**: Birleşim türleri, kesişim türleri, koşullu türler, eşlenen türler, şablon değişmez türleri — tür sistemi, karmaşık alan mantığını modellemek için yeterince anlamlıdır.
- **Sektörün benimsenmesi**: Angular bunu gerektirir; React ekosistemi bunu büyük oranda kullanıyor; Yeni npm paketlerinin çoğu tür tanımlarıyla birlikte gelir.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Derleme adımı** | Çalıştırmadan önce`.ts`→`.js`derlenmelidir | Geliştirme için`ts-node`/`tsx`kullanın;  üretim için`tsc`|
| **Öğrenme eğrisi** | Tip sistemi karmaşık olabilir (jenerikler, koşullu tipler) | Temel türlerle başlayın; gelişmiş özellikleri kademeli olarak benimseyin |
| **Tür tanımı dosyaları** | Tüm npm paketleri türlerle birlikte gönderilmez | `@types/package-name`'yi KesinlikleTyped'dan yükleyin |
| **Derleme zamanları** | Büyük projelerin yazım denetimi yavaş olabilir | Proje referanslarını kullanın,`isolatedModules`veya`swc`|
| **Yanlış güvenlik duygusu** | Türler çalışma zamanının doğruluğunu garanti etmez | Çalışma zamanı doğrulamasıyla birleştirme (Zod, io-ts) |
---

## Söz Diziminin Temelleri
### Temel Tür Ek Açıklamaları
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

### Arayüzler ve Türler
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

### Jenerikler
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

### Gelişmiş Türler
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

### Türlerle Eşzamansız
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

## Gelişmiş Sözdizimi ve Desenler
### Gelişmiş Jenerikler
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

### Dekoratörler (TypeScript 5.0+ Standardı)
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

### Tip Korumalar ve Daraltma
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

## Eşzamanlılık ve Paralellik
TypeScript, JavaScript'in eşzamanlılık modelini devralır ancak eşzamansız kalıplara tür güvenliği ekler.
### Yazılan Eşzamansız Desenler
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Rehberi Yapısı
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

###`tsconfig.json`— TypeScript Yapılandırması
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

### Derleme ve Paket Yönetimi
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

### Vitest ile test etme
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

### CI/CD İşlem Hattı — GitHub Eylemleri
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

## Gelişmiş Sözdizimi ve Desenler
### Gelişmiş Jenerikler
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

### Dekoratörler (TypeScript 5.0+)
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

### Tip Korumalar ve Daraltma
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

## Proje Yapılandırması ve Oluşturma Sistemi
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

### Vitest ile test etme
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

### Zod ile Çalışma Zamanı Doğrulaması
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

## Birlikte Çalışabilirlik
### JavaScript Kitaplıklarını Kullanma
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

## Tasarım Desenleri
### Sonuç Modeli
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

### Depo Modeli
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

## Dağıtım
### Docker dosyası
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

## Ekosistem
### Temel Araçlar
| Araç | Amaç |
|------|------------|
| **tsc** | TypeScript derleyicisi (resmi) |
| **ts düğümü / tsx** | TypeScript'i ayrı bir derleme olmadan doğrudan çalıştırın |
| **swc** | Ultra hızlı Rust tabanlı TypeScript/JavaScript derleyicisi |
| **ESLint + typescript-eslint** | Tipe duyarlı kurallarla Linting |
| **Zod** | TypeScript çıkarımıyla çalışma zamanı tür doğrulaması |
| **tsconfig.json** | TypeScript yapılandırma dosyası |
### Çerçeveler (Tüm TypeScript-First)
| Çerçeve | Etki Alanı |
|-----------|-----------|
| **Açısal** | Tam özellikli ön uç çerçevesi (TypeScript gerektirir) |
| **Sonraki.js** | Meta çerçeveye tepki verme (önce TypeScript) |
| **NestJS** | Kurumsal arka uç çerçevesi (önce TypeScript) |
| **tRPC** | Uçtan uca yazım uyumlu API'ler (yalnızca TypeScript) |
| **Prizma** | Node.js için tür açısından güvenli ORM |
---

## TypeScript Ne Zaman Kullanılmalı
| Senaryo | Neden TypeScript | Daha İyi Alternatif |
|----------|---------------|----------|
| Büyük JavaScript projeleri | Tip güvenliği tüm hata kategorilerini önler | -- |
| Takım projeleri | Türler paylaşılan bir sözleşme görevi görür | -- |
| API geliştirme | tRPC veya OpenAPI ile uçtan uca güvenlik | Daha basit REST API'leri için Go, Java |
| Herhangi bir yeni JavaScript projesi | TypeScript'i sonradan eklemenin maliyeti yüksektir | Yalnızca küçük komut dosyaları için düz JS |
| Kütüphaneler / npm paketleri | Tüketiciler otomatik tamamlama ve yazım denetiminden yararlanıyor | -- |
**Genel kural**: JavaScript projenizde birkaç yüzden fazla satır varsa TypeScript kullanın.
---

## Sentetik Soru-Cevap
### S1:`type`ile`interface`arasındaki fark nedir ve her birini ne zaman kullanmalıyım?
**C:** Her ikisi de nesne şekillerini tanımlar ancak farklı yeteneklere sahiptirler. `interface`bildirim birleştirmeyi (aynı ad birleştirmeyle birden çok bildirim),`extends`devralmayı destekler ve genel API'ler için deyimsel seçimdir.  `type`, birleşim türlerini, kesişim türlerini, eşlenen türleri, koşullu türleri ve şablon değişmez türlerini (gelişmiş olan her şeyi) destekler. En iyi uygulama: Nesne şekilleri ve genel API'ler için `interface`'yi kullanın; Birleşimler, yardımcı programlar ve karmaşık türdeki işlemler için `type`'yi kullanın.
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

### S2: Jenerikler nasıl çalışır ve neden önemlidirler?
**C:** Jenerikler, tür güvenliğini korurken herhangi bir türle çalışan işlevler, sınıflar ve türler yazmanıza olanak tanır.`any`(tür bilgilerini kaybeder) yerine jenerikler, giriş ve çıkış türleri arasındaki ilişkiyi korur. Bunlar yeniden kullanılabilir, tür açısından güvenli kodun temelidir.
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

### S3: Yardımcı program türleri nelerdir ve hangilerini bilmeliyim?
**C:** TypeScript, mevcut türleri dönüştüren yerleşik yardımcı program türleri sağlar. En önemlileri:`Partial<T>`(hepsi isteğe bağlı),`Required<T>`(tümü gerekli),`Pick<T, K>`(anahtarları seç),`Omit<T, K>`(anahtarları hariç tut),`Record<K, V>`(anahtar-değer haritası),`Exclude<T, U>`(birleşimden kaldır),`ReturnType<T>`(işlev dönüş türünü çıkar),`Awaited<T>`(Söz paketini aç). Bunları öğrenin; özel türde işlemlere olan ihtiyacın çoğunu ortadan kaldırırlar.
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

### S4: Zaman uyumsuz kodu nasıl yazarım ve hataları tür açısından güvenli bir şekilde nasıl ele alırım?
**A:** Zaman uyumsuz işlevler otomatik olarak`Promise<T>`değerini döndürür; burada T dönüş türüdür. Promise paketini açmak için`await`kullanın. Hata işleme için TypeScript'in yazılı istisnaları yoktur, ancak tür korumaları ve sonuç türleri oluşturabilirsiniz. "Sonuç modeli" (Rust'tan esinlenilmiştir) derleme zamanı hata yönetimini sağlar.
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

### S5: Bildirim dosyaları (.d.ts) nedir ve üçüncü taraf türlerini nasıl kullanırım?
**C:** Bildirim dosyaları, yerleşik TypeScript türlerine sahip olmayan JavaScript kitaplıklarının türlerini açıklar. Yalnızca tür bilgilerini içerirler (çalışma zamanı kodu yoktur). KesinlikleTyped'dan topluluk tarafından korunan türleri yükleyin: `npm install --save-dev @types/lodash`. Kendi kitaplıklarınız için `package.json`'ye bir`types`alanı ekleyin veya kaynağınızın yanına`.d.ts`dosyalarını ekleyin. Ortam bildirimleri için`declare module`kullanın.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Güvenli Tip Olay Yayıcı Oluşturma
**Sorun Açıklaması:** TypeScript'te her olay adının belirli bir veri yükü türüyle eşleştiği genel, tür açısından güvenli bir olay yayıcı oluşturun. Derleyicinin derleme zamanında yanlış olay adlarını ve veri yükü türlerini yakalaması gerekir.
**1. Adım — Sorunu Anlayın:**
Şunları içeren bir olay sistemine ihtiyacımız var: (1) olaylar yük türleriyle tanımlanır, (2)`emit`yalnızca doğru yüklere sahip geçerli olay adlarını kabul eder, (3)`on`yalnızca doğru yazılmış işleyicilere sahip geçerli olay adlarını kabul eder. Bu, bir olay haritası arayüzü üzerinden eşlenen türler ve jenerikler gerektirir.
**2. Adım — Yaklaşımı Belirleyin:**
- Bir`EventMap`türü tanımlayın:`{ [eventName: string]: payloadType }`.
- Etkinlik adlarını kısıtlamak için`keyof EventMap`kullanın.
- Belirli bir olayın yük türünü almak için `EventMap[K]`'yi kullanın.
- Dinleyicileri bir `Map<string, Function[]>`'de saklayın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Tür güvenliği: derleyici, derleme sırasında yanlış olay adlarını ve yanlış yük şekillerini yakalar.
- `on`, uygun temizlik için bir abonelikten çıkma işlevi döndürür.
- `once`, ilk çağrıdan sonra dinleyiciyi otomatik olarak abonelikten çıkmaya sarar.
- Üretim için:`listenerCount`,`removeAllListeners`ekleyin ve iptal için`AbortSignal`kullanmayı düşünün.
### Sorun 2: Tür Güvenli SQL Sorgu Oluşturucusunun Uygulanması
**Sorun Açıklaması:** Sütun adlarının ve türlerinin TypeScript arayüzünden türetildiği bir SQL sorgu oluşturucusu oluşturun. Oluşturucunun derleme zamanında geçersiz sütun adlarını ve tür uyuşmazlıklarını önlemesi gerekir.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1)`keyof T`ile sınırlandırılmış sütun adları, (2) sütuna göre yazılan WHERE yan tümcesi değerleri, (3) sorgu oluşturmak için zincirlenebilir API. Bu,`Record<string, unknown>`tarafından kısıtlanan jenerikleri gerektirir.
**2. Adım — Yaklaşımı Belirleyin:**
- Sütun adı kısıtlamaları için`keyof T`kullanın.
- Değer türü kısıtlamaları için`T[K]`kullanın.
- Parametreli sorgularla SQL dizesi oluşturun (SQL enjeksiyonunu önleyin).
- Zincirlenebilir yöntemler`this`değerini döndürür.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- SQL enjeksiyon önleme: tüm değerler parametreli sorgulardan (`$1`,`$2`) geçer, hiçbir zaman enterpolasyon yapılmaz.
- Tür güvenliği: sütun adları ve değer türleri derleme zamanında kontrol edilir.
- Genişletilebilirlik: aynı modeli izleyerek`join`,`groupBy`,`having`,`insert`,`update`yöntemlerini ekleyin.
- Üretim:`kysely`veya`drizzle-orm`kullanın — tam SQL kapsamıyla bu tür güvenliği sağlarlar.
### Sorun 3: Tip Güvenlikli Sonlu Durum Makinesinin Uygulanması
**Sorun Açıklaması:** Derleme zamanında geçerli geçişlerin uygulandığı, tür açısından güvenli bir sonlu durum makinesi oluşturun. Her durumun giriş/çıkış eylemleri olabilir ve makinenin mevcut durumu izlemesi gerekir.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) tür olarak tanımlanan durumlar ve olaylar, (2) tür düzeyinde eşlenen geçerli geçişler, (3) derleyici geçersiz geçişleri önler, (4) geri çağrılarla çalışma zamanı durum takibi. Bu, eşlenen türleri ve koşullu türleri gerektirir.
**2. Adım — Yaklaşımı Belirleyin:**
- Bir`TransitionMap`:`{ [State]: { [Event]: NextState } }`tanımlayın.
- `send(event)`'yi mevcut duruma göre sınırlamak için jenerikleri kullanın.
- Bir değişkenle çalışma zamanındaki durumu izleyin.
- Durum başına giriş/çıkış geri aramalarını destekleyin.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Çalışma zamanı güvenliği:`send`geçersiz geçişlere neden olur.
- Tür güvenliği:`EventsFor`türü, derleme zamanında durum başına geçerli olayları çıkarır.
- Giriş/çıkış geri aramaları geçişlerde otomatik olarak tetiklenir.
- Üretim için:`xstate`kullanın — görsel hata ayıklama, hiyerarşik durumlar, korumalar ve eylemlerle tam durumlu bir makine kitaplığı sağlar.
---

## Özet
TypeScript, önemsiz komut dosyalarının ötesinde her şey için doğru şekilde yapılmış bir JavaScript'tir. Hataları erkenden yakalayan, araçları geliştiren ve kodu belgeleyen güçlü bir tür sistemi eklerken aynı zamanda her yerde çalışan standart JavaScript'i derler. Öğrenme eğrisi yumuşaktır (minimal türlerle başlayabilirsiniz) ancak derinlik çok büyüktür (tip sistemi Turing-tamamlanmıştır). Modern JavaScript geliştirmede TypeScript endüstri standardı haline geldi.