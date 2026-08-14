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
# Naskah Ketik
TypeScript adalah superset JavaScript yang diketik secara statis yang dikembangkan oleh Microsoft (dipimpin oleh Anders Hejlsberg) dan pertama kali dirilis pada tahun 2012. TypeScript menambahkan anotasi tipe opsional, antarmuka, generik, dan fitur sistem tipe lanjutan ke JavaScript — lalu dikompilasi menjadi JavaScript biasa yang berjalan di mana pun JavaScript dijalankan. TypeScript bukanlah bahasa atau runtime yang terpisah; itu adalah JavaScript dengan pemeriksa tipe.
TypeScript telah menjadi standar untuk pengembangan JavaScript skala besar. React, Angular, VS Code, Deno, dan sebagian besar proyek JavaScript sumber terbuka utama ditulis dalam TypeScript. Jika Anda memulai proyek JavaScript baru dengan ukuran signifikan apa pun, TypeScript adalah default yang disarankan.
---

## Mengapa TypeScript Penting
- **Menangkap bug pada waktu kompilasi**: Kesalahan jenis ditemukan sebelum kode dijalankan — bukan dalam produksi.
- **Dukungan IDE yang lebih baik**: Pelengkapan otomatis, masuk ke definisi, pemfaktoran ulang, dan dokumentasi sebaris semuanya meningkat secara dramatis.
- **Kode yang mendokumentasikan mandiri**: Jenis berfungsi sebagai dokumentasi yang selalu diperbarui.
- **100% kompatibel dengan JavaScript**: Semua JavaScript yang valid adalah TypeScript yang valid. Anda bisa menerapkannya secara bertahap.
- **Sistem tipe lanjutan**: Tipe gabungan, tipe persimpangan, tipe kondisional, tipe yang dipetakan, tipe literal templat — sistem tipe cukup ekspresif untuk memodelkan logika domain yang kompleks.
- **Adopsi industri**: Angular memerlukannya; Ekosistem React sebagian besar menggunakannya; sebagian besar paket npm baru dikirimkan dengan definisi tipe.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Langkah kompilasi** | Harus mengkompilasi`.ts`→`.js`sebelum menjalankan | Gunakan`ts-node`/`tsx`untuk pengembangan; `tsc`untuk produksi |
| **Kurva pembelajaran** | Sistem tipenya bisa rumit (generik, tipe bersyarat) | Mulailah dengan tipe dasar; mengadopsi fitur-fitur canggih secara bertahap |
| **Ketik file definisi** | Tidak semua paket npm dikirimkan dengan tipe | Instal`@types/package-name`dari PastiDiketik |
| **Waktu kompilasi** | Proyek besar bisa jadi lambat untuk diketik | Gunakan referensi proyek,`isolatedModules`, atau`swc`|
| **Rasa aman yang salah** | Jenis tidak menjamin kebenaran runtime | Kombinasikan dengan validasi runtime (Zod, io-ts) |
---

## Dasar Sintaks
### Anotasi Tipe Dasar
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

### Antarmuka dan Tipe
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

### Generik
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

### Tipe Lanjutan
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

### Asinkron dengan Tipe
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

## Sintaks & Pola Tingkat Lanjut
### Generik Tingkat Lanjut
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

### Dekorator (Standar TypeScript 5.0+)
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

### Ketik Penjaga dan Penyempitan
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

## Konkurensi & Paralelisme
TypeScript mewarisi model konkurensi JavaScript tetapi menambahkan keamanan tipe ke pola asinkron.
### Pola Asinkron yang Diketik
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Direktori Proyek
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

###`tsconfig.json`— Konfigurasi TypeScript
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

### Pembuatan dan Manajemen Paket
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

### Menguji dengan Vitest
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

### Saluran CI/CD — Tindakan GitHub
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

## Sintaks & Pola Tingkat Lanjut
### Generik Tingkat Lanjut
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

### Dekorator (TypeScript 5.0+)
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

### Ketik Penjaga dan Penyempitan
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

## Konfigurasi Proyek dan Sistem Pembangunan
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

### Menguji dengan Vitest
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

### Validasi Waktu Proses dengan Zod
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

## Interoperabilitas
### Menggunakan Perpustakaan JavaScript
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

## Pola Desain
### Pola Hasil
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

### Pola Repositori
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

## Penerapan
### File Docker
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
### Alat Utama
| Alat | Tujuan |
|------|---------|
| **tsc** | Kompiler TypeScript (resmi) |
| **simpul-ts / tsx** | Jalankan TypeScript secara langsung tanpa kompilasi terpisah |
| **swc** | Kompiler TypeScript/JavaScript berbasis Rust yang sangat cepat |
| **ESLint + TypeScript-eslint** | Linting dengan aturan sadar tipe |
| **Zod** | Validasi tipe runtime dengan inferensi TypeScript |
| **tsconfig.json** | File konfigurasi TypeScript |
### Kerangka Kerja (Semua TypeScript-Pertama)
| Kerangka | Domain |
|-----------|--------|
| **Sudut** | Kerangka kerja frontend berfitur lengkap (memerlukan TypeScript) |
| **Berikutnya.js** | Bereaksi meta-framework (TypeScript-first) |
| **NestJS** | Kerangka kerja backend perusahaan (mengutamakan TypeScript) |
| **tRPC** | API typesafe ujung ke ujung (khusus TypeScript) |
| **Prisma** | ORM yang aman untuk tipe untuk Node.js |
---

## Kapan Menggunakan TypeScript
| Skenario | Mengapa TypeScript | Alternatif Lebih Baik |
|----------|---------------|-------------------|
| Proyek JavaScript besar | Keamanan jenis mencegah seluruh kategori bug | -- |
| Proyek tim | Jenis berfungsi sebagai kontrak bersama | -- |
| Pengembangan API | Keamanan tipe ujung ke ujung dengan tRPC atau OpenAPI | Gunakan Java untuk REST API yang lebih sederhana |
| Setiap proyek JavaScript baru | Biaya penambahan TypeScript nanti tinggi | JS biasa hanya untuk skrip kecil |
| Perpustakaan / paket npm | Konsumen mendapatkan pelengkapan otomatis dan pengecekan tipe | -- |
**Aturan praktis**: Jika proyek JavaScript Anda memiliki lebih dari beberapa ratus baris, gunakan TypeScript.
---

## Tanya Jawab Sintetis
### Q1: Apa perbedaan antara`type`dan`interface`, dan kapan saya harus menggunakannya?
**A:** Keduanya mendefinisikan bentuk objek, namun memiliki kemampuan yang berbeda. `interface`mendukung penggabungan deklarasi (beberapa deklarasi dengan nama yang sama digabungkan),`extends`untuk pewarisan, dan merupakan pilihan idiomatis untuk API publik. `type`mendukung tipe gabungan, tipe persimpangan, tipe yang dipetakan, tipe kondisional, dan tipe literal templat — semuanya tingkat lanjut. Praktik terbaik: gunakan`interface`untuk bentuk objek dan API publik; gunakan`type`untuk serikat pekerja, utilitas, dan operasi tipe kompleks.
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

### Q2: Bagaimana cara kerja obat generik, dan mengapa obat generik itu penting?
**A:** Generik memungkinkan Anda menulis fungsi, kelas, dan tipe yang berfungsi dengan tipe apa pun sambil menjaga keamanan tipe. Daripada`any`(yang kehilangan informasi tipe), obat generik mempertahankan hubungan antara tipe input dan output. Ini adalah dasar dari kode yang dapat digunakan kembali dan aman untuk diketik.
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

### Q3: Apa saja jenis utilitasnya, dan mana yang harus saya ketahui?
**A:** TypeScript menyediakan tipe utilitas bawaan yang mengubah tipe yang sudah ada. Yang paling penting:`Partial<T>`(semua opsional),`Required<T>`(semua diperlukan),`Pick<T, K>`(pilih tombol),`Omit<T, K>`(tidak termasuk kunci),`Record<K, V>`(peta nilai kunci),`Exclude<T, U>`(hapus dari gabungan),`ReturnType<T>`(tipe pengembalian fungsi ekstrak),`Awaited<T>`(membuka bungkusnya Janji). Pelajari hal ini — hal ini menghilangkan sebagian besar kebutuhan akan operasi tipe kustom.
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

### Q4: Bagaimana cara mengetik kode asinkron dan menangani kesalahan dengan cara yang aman untuk mengetik?
**A:** Fungsi async secara otomatis mengembalikan`Promise<T>`dengan T adalah tipe kembaliannya. Gunakan`await`untuk membuka Janji tersebut. Untuk penanganan kesalahan, TypeScript tidak memiliki pengecualian pengetikan, namun Anda dapat membuat pelindung tipe dan tipe hasil. "Pola hasil" (terinspirasi oleh Rust) menyediakan penanganan kesalahan pada waktu kompilasi.
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

### Q5: Apa itu file deklarasi (.d.ts) dan bagaimana cara menggunakan tipe pihak ketiga?
**A:** File deklarasi menjelaskan tipe pustaka JavaScript yang tidak memiliki tipe TypeScript bawaan. Mereka hanya berisi informasi tipe (tidak ada kode runtime). Instal tipe yang dikelola komunitas dari PastiTyped:`npm install --save-dev @types/lodash`. Untuk perpustakaan Anda sendiri, tambahkan bidang`types`di`package.json`atau sertakan file`.d.ts`di samping sumber Anda. Gunakan`declare module`untuk deklarasi ambien.
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

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membangun Pemancar Peristiwa yang Aman untuk Tipe
**Pernyataan Masalah:** Buat pemancar peristiwa generik yang aman untuk tipe di TypeScript tempat setiap nama peristiwa dipetakan ke jenis payload tertentu. Kompiler harus menangkap nama peristiwa dan jenis muatan yang salah pada waktu kompilasi.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan sistem kejadian di mana: (1) kejadian didefinisikan dengan jenis muatannya, (2)`emit`hanya menerima nama kejadian yang valid dengan muatan yang benar, (3)`on`hanya menerima nama kejadian yang valid dengan penangan yang diketik dengan benar. Ini memerlukan tipe dan generik yang dipetakan melalui antarmuka peta peristiwa.
**Langkah 2 — Identifikasi Pendekatannya:**
- Tentukan tipe `EventMap`:`{ [eventName: string]: payloadType }`.
- Gunakan`keyof EventMap`untuk membatasi nama acara.
- Gunakan`EventMap[K]`untuk mendapatkan jenis muatan untuk peristiwa tertentu.
- Simpan pendengar di`Map<string, Function[]>`.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Keamanan jenis: kompiler menangkap nama peristiwa yang salah dan bentuk muatan yang salah pada waktu kompilasi.
-`on`mengembalikan fungsi berhenti berlangganan untuk pembersihan yang nyaman.
-`once`membungkus pendengar untuk berhenti berlangganan otomatis setelah pemanggilan pertama.
- Untuk produksi: tambahkan`listenerCount`,`removeAllListeners`, dan pertimbangkan untuk menggunakan`AbortSignal`untuk pembatalan.
### Masalah 2: Menerapkan Pembuat Kueri SQL yang Aman untuk Tipe
**Pernyataan Masalah:** Buat pembuat kueri SQL yang nama dan tipe kolomnya berasal dari antarmuka TypeScript. Pembuatnya harus mencegah nama kolom yang tidak valid dan ketidakcocokan tipe pada waktu kompilasi.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) nama kolom dibatasi hingga`keyof T`, (2) nilai klausa WHERE diketik sesuai kolom, (3) API yang dapat dirantai untuk membuat kueri. Ini memerlukan obat generik yang dibatasi oleh`Record<string, unknown>`.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`keyof T`untuk batasan nama kolom.
- Gunakan`T[K]`untuk batasan tipe nilai.
- Bangun string SQL dengan kueri berparameter (mencegah injeksi SQL).
- Metode yang dapat dirantai mengembalikan`this`.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Pencegahan injeksi SQL: semua nilai melewati kueri berparameter (`$1`,`$2`), tidak pernah diinterpolasi.
- Keamanan jenis: nama kolom dan tipe nilai diperiksa pada waktu kompilasi.
- Ekstensibilitas: tambahkan metode`join`,`groupBy`,`having`,`insert`,`update`mengikuti pola yang sama.
- Produksi: gunakan`kysely`atau`drizzle-orm`— keduanya memberikan keamanan jenis ini dengan cakupan SQL penuh.
### Masalah 3: Menerapkan Mesin Keadaan Hingga dengan Keamanan Tipe
**Pernyataan Masalah:** Membuat mesin status terbatas yang aman untuk tipe tempat transisi yang valid diterapkan pada waktu kompilasi. Setiap negara bagian dapat memiliki tindakan masuk/keluar, dan mesin harus melacak keadaan saat ini.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) status dan peristiwa yang didefinisikan sebagai tipe, (2) transisi valid yang dipetakan pada tingkat tipe, (3) kompiler mencegah transisi yang tidak valid, (4) pelacakan status runtime dengan callback. Ini memerlukan tipe yang dipetakan dan tipe bersyarat.
**Langkah 2 — Identifikasi Pendekatannya:**
- Tentukan`TransitionMap`:`{ [State]: { [Event]: NextState } }`.
- Gunakan obat generik untuk membatasi`send(event)`berdasarkan kondisi saat ini.
- Lacak status saat runtime dengan variabel.
- Mendukung panggilan balik masuk/keluar per negara bagian.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Keamanan runtime:`send`melakukan transisi yang tidak valid.
- Keamanan tipe: tipe`EventsFor`mengekstrak kejadian valid per status pada waktu kompilasi.
- Panggilan balik masuk/keluar diaktifkan secara otomatis pada transisi.
- Untuk produksi: gunakan`xstate`— ini menyediakan perpustakaan mesin status lengkap dengan debugging visual, status hierarki, penjaga, dan tindakan.
---

## Ringkasan
TypeScript adalah JavaScript yang dilakukan dengan benar untuk apa pun selain skrip sepele. Ia menambahkan sistem tipe yang kuat yang menangkap bug lebih awal, meningkatkan perkakas, dan mendokumentasikan kode -- semuanya sambil mengkompilasi ke JavaScript standar yang berjalan di mana saja. Kurva pembelajarannya lembut (Anda bisa memulai dengan tipe minimal) tetapi kedalamannya sangat luas (sistem tipenya adalah Turing-complete). Untuk pengembangan JavaScript modern, TypeScript telah menjadi standar industri.