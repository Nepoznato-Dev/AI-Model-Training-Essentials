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
# Dattiloscritto
TypeScript è un superset di JavaScript tipizzato staticamente sviluppato da Microsoft (guidato da Anders Hejlsberg) e rilasciato per la prima volta nel 2012. Aggiunge annotazioni di tipo opzionali, interfacce, generici e funzionalità avanzate del sistema di tipo a JavaScript, quindi compila in JavaScript semplice che viene eseguito ovunque venga eseguito JavaScript. TypeScript non è un linguaggio o un runtime separato; è JavaScript con un controllo del tipo.
TypeScript è diventato lo standard per lo sviluppo JavaScript su larga scala. React, Angular, VS Code, Deno e la maggior parte dei principali progetti JavaScript open source sono scritti in TypeScript. Se stai avviando un nuovo progetto JavaScript di dimensioni significative, TypeScript è l'impostazione predefinita consigliata.
---

## Perché TypeScript è importante
- **Rileva i bug in fase di compilazione**: gli errori di tipo vengono rilevati prima dell'esecuzione del codice, non in produzione.
- **Migliore supporto IDE**: completamento automatico, go-to-definition, refactoring e documentazione in linea migliorano notevolmente.
- **Codice autodocumentante**: i tipi servono come documentazione che rimane aggiornata.
- **Compatibile con JavaScript al 100%**: qualsiasi JavaScript valido è TypeScript valido. Puoi adottarlo gradualmente.
- **Sistema di tipi avanzato**: tipi di unione, tipi di intersezione, tipi condizionali, tipi mappati, tipi letterali di modello: il sistema di tipi è sufficientemente espressivo per modellare la logica di dominio complessa.
- **Adozione da parte del settore**: Angular lo richiede; L'ecosistema React lo utilizza in modo schiacciante; la maggior parte dei nuovi pacchetti npm vengono forniti con definizioni di tipo.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Passaggio di compilazione** | È necessario compilare`.ts`→`.js`prima di eseguire | Utilizzare`ts-node`/`tsx`per lo sviluppo; `tsc`per la produzione |
| **Curva di apprendimento** | Il sistema di tipi può essere complesso (generici, tipi condizionali) | Inizia con i tipi di base; adottare gradualmente funzionalità avanzate |
| **File di definizione del tipo** | Non tutti i pacchetti npm vengono forniti con i tipi | Installa`@types/package-name`da SicuramenteTyped |
| **Tempi di compilazione** | I progetti di grandi dimensioni possono essere lenti nel controllo del tipo | Utilizzare i riferimenti al progetto,`isolatedModules`o`swc`|
| **Falso senso di sicurezza** | I tipi non garantiscono la correttezza del runtime | Combinalo con la convalida del runtime (Zod, io-ts) |
---

## Fondamenti di sintassi
### Annotazioni di tipo base
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

### Interfacce e tipi
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

### Generici
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

### Tipi avanzati
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

### Asincrono con i tipi
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

## Sintassi e modelli avanzati
### Generici avanzati
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

### Decoratori (TypeScript 5.0+ standard)
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

### Tipo Protezioni e Restrizioni
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

## Concorrenza e parallelismo
TypeScript eredita il modello di concorrenza di JavaScript ma aggiunge l'indipendenza dai tipi ai modelli asincroni.
### Modelli asincroni digitati
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

## Configurazione del progetto e sistema di creazione
### Struttura delle directory del progetto
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

### `tsconfig.json`: configurazione TypeScript
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

### Gestione di build e pacchetti
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

### Test con Vitest
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

### Pipeline CI/CD: azioni GitHub
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

## Sintassi e modelli avanzati
### Generici avanzati
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

### Decoratori (TypeScript 5.0+)
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

### Tipo Protezioni e Restrizioni
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

## Configurazione del progetto e sistema di creazione
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

### Test con Vitest
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

### Convalida runtime con Zod
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

## Interoperabilità
### Utilizzo delle librerie JavaScript
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

## Modelli di progettazione
### Modello di risultato
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

### Modello di archivio
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

## Distribuzione
###Dockerfile
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

## L'ecosistema
### Strumenti chiave
| Strumento | Scopo |
|------|---------|
| **tsc** | Il compilatore TypeScript (ufficiale) |
| **nodo ts / tsx** | Esegui TypeScript direttamente senza compilazione separata |
| **swc** | Compilatore TypeScript/JavaScript ultraveloce basato su Rust |
| **ESLint + dattiloscritto-eslint** | Linting con regole basate sul tipo |
| **Zod** | Convalida del tipo di runtime con inferenza TypeScript |
| **tsconfig.json** | File di configurazione TypeScript |
### Framework (tutti TypeScript-First)
| Quadro | Dominio |
|-----------|--------|
| **Angolare** | Framework frontend completo (richiede TypeScript) |
| **Next.js** | Meta-framework React (prima TypeScript) |
| **NestJS** | Framework backend aziendale (prima TypeScript) |
| **tRPC** | API typesafe end-to-end (solo TypeScript) |
| **Prisma** | ORM indipendente dai tipi per Node.js |
---

## Quando utilizzare TypeScript
| Scenario | Perché TypeScript | Alternativa migliore |
|----------|--------------|-------------|
| Grandi progetti JavaScript | L'indipendenza dai tipi previene intere categorie di bug | -- |
| Progetti di squadra | I tipi fungono da contratto condiviso | -- |
| Sviluppo API | Sicurezza dei tipi end-to-end con tRPC o OpenAPI | Vai, Java per API REST più semplici |
| Qualsiasi nuovo progetto JavaScript | Il costo per aggiungere TypeScript in un secondo momento è elevato | JS semplice solo per script piccoli |
| Librerie/pacchetti npm | I consumatori ricevono il completamento automatico e il controllo del tipo | -- |
**Regola pratica**: se il tuo progetto JavaScript ha più di qualche centinaio di righe, utilizza TypeScript.
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra`type`e`interface`e quando dovrei utilizzarli entrambi?
**R:** Entrambi definiscono le forme degli oggetti, ma hanno capacità diverse. `interface`supporta l'unione delle dichiarazioni (unione di più dichiarazioni con lo stesso nome),`extends`per l'ereditarietà ed è la scelta idiomatica per le API pubbliche. `type`supporta tipi di unione, tipi di intersezione, tipi mappati, tipi condizionali e tipi letterali modello: qualsiasi cosa avanzata. Procedura consigliata: utilizzare`interface`per forme di oggetti e API pubbliche; utilizzare`type`per unioni, servizi pubblici e operazioni di tipo complesso.
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

### D2: Come funzionano i farmaci generici e perché sono importanti?
**R:** I generici ti consentono di scrivere funzioni, classi e tipi che funzionano con qualsiasi tipo mantenendo l'indipendenza dai tipi. Invece di`any`(che perde le informazioni sul tipo), i generici preservano la relazione tra i tipi di input e output. Costituiscono la base del codice riutilizzabile e indipendente dai tipi.
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

### D3: Cosa sono i tipi di utilità e quali dovrei conoscere?
**R:** TypeScript fornisce tipi di utilità incorporati che trasformano i tipi esistenti. I più importanti:`Partial<T>`(tutto opzionale),`Required<T>`(tutto obbligatorio),`Pick<T, K>`(seleziona chiavi),`Omit<T, K>`(escludi chiavi),`Record<K, V>`(mappa valori-chiave),`Exclude<T, U>`(rimuovi dall'unione),`ReturnType<T>`(estrai tipo di ritorno funzione),`Awaited<T>`(unwrap Promessa). Imparateli: eliminano la maggior parte della necessità di operazioni di tipo personalizzato.
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

### D4: Come posso digitare codice asincrono e gestire gli errori in modo indipendente dai tipi?
**R:** Le funzioni asincrone restituiscono automaticamente`Promise<T>`dove T è il tipo restituito. Usa`await`per scartare la Promessa. Per la gestione degli errori, TypeScript non dispone di eccezioni tipizzate, ma è possibile creare protezioni di tipo e tipi di risultati. Il "modello di risultato" (ispirato da Rust) fornisce la gestione degli errori in fase di compilazione.
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

### D5: Cosa sono i file di dichiarazione (.d.ts) e come posso utilizzare tipi di terze parti?
**R:** I file di dichiarazione descrivono i tipi di librerie JavaScript che non dispongono di tipi TypeScript incorporati. Contengono solo informazioni sul tipo (nessun codice runtime). Installa i tipi gestiti dalla community da SicuramenteTyped:`npm install --save-dev @types/lodash`. Per le tue librerie, aggiungi un campo`types`in`package.json`o includi i file`.d.ts`insieme alla tua fonte. Utilizzare`declare module`per le dichiarazioni ambientali.
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

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: creare un emettitore di eventi type-safe
**Dichiarazione del problema:** crea un emettitore di eventi generico e indipendente dai tipi in TypeScript in cui ciascun nome di evento è mappato a un tipo di payload specifico. Il compilatore dovrebbe rilevare nomi di eventi e tipi di payload errati in fase di compilazione.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di un sistema di eventi in cui: (1) gli eventi sono definiti con i relativi tipi di payload, (2)`emit`accetta solo nomi di eventi validi con payload corretti, (3)`on`accetta solo nomi di eventi validi con gestori digitati correttamente. Ciò richiede tipi mappati e generici su un'interfaccia della mappa eventi.
**Passaggio 2: identificare l'approccio:**
- Definire un tipo `EventMap`:`{ [eventName: string]: payloadType }`.
- Utilizza`keyof EventMap`per vincolare i nomi degli eventi.
- Utilizza`EventMap[K]`per ottenere il tipo di carico utile per un evento specifico.
- Memorizza gli ascoltatori in un `Map<string, Function[]>`.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Sicurezza del tipo: il compilatore rileva nomi di eventi errati e forme di payload errate in fase di compilazione.
-`on`restituisce una funzione di annullamento dell'iscrizione per una comoda pulizia.
-`once`avvolge l'ascoltatore per annullare automaticamente l'iscrizione dopo la prima invocazione.
- Per la produzione: aggiungi`listenerCount`,`removeAllListeners`e considera l'utilizzo di`AbortSignal`per l'annullamento.
### Problema 2: implementare un generatore di query SQL type-safe
**Dichiarazione del problema:** crea un generatore di query SQL in cui i nomi e i tipi di colonna derivano da un'interfaccia TypeScript. Il builder dovrebbe impedire nomi di colonne non validi e tipi non corrispondenti in fase di compilazione.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) nomi di colonna vincolati a`keyof T`, (2) valori della clausola WHERE digitati in base alla colonna, (3) API concatenabile per la creazione di query. Ciò richiede farmaci generici vincolati da`Record<string, unknown>`.
**Passaggio 2: identificare l'approccio:**
- Utilizzare`keyof T`per i vincoli sui nomi delle colonne.
- Utilizzare`T[K]`per i vincoli sul tipo di valore.
- Crea una stringa SQL con query parametrizzate (previene l'iniezione SQL).
- I metodi concatenabili restituiscono`this`.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Prevenzione SQL injection: tutti i valori passano attraverso query parametrizzate (`$1`,`$2`), mai interpolate.
- Sicurezza del tipo: i nomi delle colonne e i tipi di valore vengono controllati in fase di compilazione.
- Estendibilità: aggiungi i metodi`join`,`groupBy`,`having`,`insert`,`update`seguendo lo stesso schema.
- Produzione: utilizza`kysely`o `drizzle-orm`: forniscono questo tipo di sicurezza con copertura SQL completa.
### Problema 3: implementare una macchina a stati finiti con sicurezza dei tipi
**Dichiarazione del problema:** creare una macchina a stati finiti indipendente dai tipi in cui vengono applicate transizioni valide in fase di compilazione. Ogni stato può avere azioni di entrata/uscita e la macchina dovrebbe tenere traccia dello stato corrente.
**Passaggio 1: comprendere il problema:**
Sono necessari: (1) stati ed eventi definiti come tipi, (2) transizioni valide mappate a livello di tipo, (3) il compilatore impedisce transizioni non valide, (4) tracciamento dello stato di runtime con callback. Ciò richiede tipi mappati e tipi condizionali.
**Passaggio 2: identificare l'approccio:**
- Definire un`TransitionMap`:`{ [State]: { [Event]: NextState } }`.
- Utilizza i generici per vincolare`send(event)`in base allo stato corrente.
- Tieni traccia dello stato in fase di esecuzione con una variabile.
- Supporta richiamate di entrata/uscita per stato.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Sicurezza di runtime:`send`genera transizioni non valide.
- Sicurezza del tipo: il tipo`EventsFor`estrae eventi validi per stato in fase di compilazione.
- Le richiamate di entrata/uscita si attivano automaticamente durante le transizioni.
- Per la produzione: utilizza `xstate`: fornisce una libreria completa di macchine a stati con debug visivo, stati gerarchici, protezioni e azioni.
---

## Riepilogo
TypeScript è JavaScript fatto bene per qualsiasi cosa oltre gli script banali. Aggiunge un potente sistema di tipi che rileva tempestivamente i bug, migliora gli strumenti e documenta il codice, il tutto durante la compilazione in JavaScript standard che funziona ovunque. La curva di apprendimento è delicata (puoi iniziare con tipi minimi) ma la profondità è vasta (il sistema di tipi è completo di Turing). Per lo sviluppo JavaScript moderno, TypeScript è diventato lo standard del settore.