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

# Datilografado
TypeScript é um superconjunto de JavaScript digitado estaticamente desenvolvido pela Microsoft (liderado por Anders Hejlsberg) e lançado pela primeira vez em 2012. Ele adiciona anotações de tipo opcionais, interfaces, genéricos e recursos avançados de sistema de tipos ao JavaScript - e então compila em JavaScript simples que é executado em qualquer lugar que o JavaScript seja executado. TypeScript não é uma linguagem ou tempo de execução separado; é JavaScript com um verificador de tipo.
TypeScript se tornou o padrão para desenvolvimento de JavaScript em larga escala. React, Angular, VS Code, Deno e a maioria dos principais projetos JavaScript de código aberto são escritos em TypeScript. Se você estiver iniciando um novo projeto JavaScript de qualquer tamanho significativo, TypeScript é o padrão recomendado.
---

## Por que o TypeScript é importante
- **Captura bugs em tempo de compilação**: erros de tipo são encontrados antes da execução do código — não em produção.
- **Melhor suporte IDE**: preenchimento automático, definição, refatoração e documentação in-line melhoraram drasticamente.
- **Código autodocumentado**: os tipos servem como documentação que se mantém atualizada.
- **100% compatível com JavaScript**: Qualquer JavaScript válido é TypeScript válido. Você pode adotá-lo gradualmente.
- **Sistema de tipos avançado**: tipos de união, tipos de interseção, tipos condicionais, tipos mapeados, tipos literais de modelo — o sistema de tipos é expressivo o suficiente para modelar lógica de domínio complexa.
- **Adoção pela indústria**: Angular exige isso; O ecossistema React o utiliza de forma esmagadora; a maioria dos novos pacotes npm vem com definições de tipo.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Etapa de compilação** | Deve compilar`.ts`→`.js`antes de executar | Use `ts-node`/`tsx` para desenvolvimento; `tsc`para produção |
| **Curva de aprendizado** | O sistema de tipos pode ser complexo (genéricos, tipos condicionais) | Comece com tipos básicos; adotar recursos avançados gradualmente |
| **Arquivos de definição de tipo** | Nem todos os pacotes npm são fornecidos com tipos | Instale`@types/package-name`de DefinitelyTyped |
| **Tempos de compilação** | Grandes projetos podem demorar para verificar o tipo | Use referências de projeto,`isolatedModules`ou`swc`|
| **Falsa sensação de segurança** | Os tipos não garantem a correção do tempo de execução | Combine com validação em tempo de execução (Zod, io-ts) |
---

## Fundamentos de sintaxe
### Anotações de tipo básico
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

### Interfaces e Tipos
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

### Genéricos
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

### Tipos Avançados
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

### Assíncrono com Tipos
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

## Sintaxe e padrões avançados
### Genéricos Avançados
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

### Decoradores (Padrão TypeScript 5.0+)
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

### Tipo Guardas e Estreitamento
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

## Simultaneidade e paralelismo
TypeScript herda o modelo de simultaneidade do JavaScript, mas adiciona segurança de tipo aos padrões assíncronos.
### Padrões assíncronos digitados
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

## Configuração do projeto e sistema de construção
### Estrutura do diretório do projeto
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

###`tsconfig.json`— Configuração TypeScript
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

### Gerenciamento de compilação e pacotes
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

### Testando com Vitest
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

### Pipeline de CI/CD — Ações do GitHub
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

## Sintaxe e padrões avançados
### Genéricos Avançados
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

### Decoradores (TypeScript 5.0+)
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

### Tipo Guardas e Estreitamento
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

## Configuração do projeto e sistema de construção
###tsconfig.json
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

### Testando com Vitest
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

### Validação de tempo de execução com Zod
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

## Interoperabilidade
### Usando bibliotecas JavaScript
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

## Padrões de Projeto
### Padrão de resultado
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

### Padrão de repositório
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

## Implantação
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

## O Ecossistema
### Ferramentas principais
| Ferramenta | Finalidade |
|------|---------|
| **tsc** | O compilador TypeScript (oficial) |
| **ts-nó /tsx** | Execute o TypeScript diretamente sem compilação separada |
| **swc** | Compilador TypeScript/JavaScript ultrarrápido baseado em Rust |
| **ESLint + texto digitado-eslint** | Linting com regras de reconhecimento de tipo |
| **Zod** | Validação de tipo de tempo de execução com inferência TypeScript |
| **tsconfig.json** | Arquivo de configuração TypeScript |
### Frameworks (todos TypeScript primeiro)
| Estrutura | Domínio |
|-----------|--------|
| **Angular** | Estrutura de front-end completa (requer TypeScript) |
| **Próximo.js** | Metaestrutura React (Primeiro TypeScript) |
| **NestJS** | Estrutura de back-end empresarial (primeiro TypeScript) |
| **tRPC** | APIs typesafe de ponta a ponta (somente TypeScript) |
| **Prisma** | ORM de tipo seguro para Node.js |
---

## Quando usar TypeScript
| Cenário | Por que TypeScript | Melhor Alternativa |
|----------|---------------|-------------------|
| Grandes projetos JavaScript | A segurança de tipo evita categorias inteiras de bugs | -- |
| Projetos de equipe | Tipos servem como contrato compartilhado | -- |
| Desenvolvimento de APIs | Segurança de ponta a ponta com tRPC ou OpenAPI | Vá, Java para APIs REST mais simples |
| Qualquer novo projeto JavaScript | O custo de adicionar TypeScript posteriormente é alto | JS simples apenas para scripts pequenos |
| Bibliotecas/pacotes npm | Os consumidores obtêm preenchimento automático e verificação de tipo | -- |
**Regra geral**: se o seu projeto JavaScript tiver mais de algumas centenas de linhas, use TypeScript.
---

## Perguntas e respostas sintéticas
### Q1: Qual é a diferença entre`type`e`interface`e quando devo usar cada um?
**R:** Ambos definem formas de objetos, mas têm capacidades diferentes. `interface`oferece suporte à mesclagem de declarações (múltiplas declarações com o mesmo nome mesclado),`extends`para herança e é a escolha idiomática para APIs públicas. `type`oferece suporte a tipos de união, tipos de interseção, tipos mapeados, tipos condicionais e tipos literais de modelo – qualquer coisa avançada. Prática recomendada: use`interface`para formas de objetos e APIs públicas; use`type`para uniões, utilitários e operações de tipo complexo.
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

### Q2: Como funcionam os genéricos e por que são importantes?
**R:** Os genéricos permitem escrever funções, classes e tipos que funcionam com qualquer tipo, mantendo a segurança do tipo. Em vez de`any`(que perde informações de tipo), os genéricos preservam o relacionamento entre os tipos de entrada e saída. Eles são a base do código reutilizável e de tipo seguro.
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

### Q3: O que são tipos de utilitários e quais devo saber?
**R:** O TypeScript fornece tipos de utilitários integrados que transformam os tipos existentes. O mais importante:`Partial<T>`(todos opcionais),`Required<T>`(todos obrigatórios),`Pick<T, K>`(selecionar chaves),`Omit<T, K>`(excluir chaves),`Record<K, V>`(mapa de valor-chave),`Exclude<T, U>`(remover da união),`ReturnType<T>`(tipo de retorno da função de extração),`Awaited<T>`(desembrulhar promessa). Aprenda-os – eles eliminam a maior parte da necessidade de operações de tipo personalizado.
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

### Q4: Como digito código assíncrono e trato erros de maneira segura?
**R:** As funções assíncronas retornam automaticamente`Promise<T>`onde T é o tipo de retorno. Use`await`para desembrulhar a promessa. Para tratamento de erros, o TypeScript não possui exceções digitadas, mas você pode criar protetores de tipo e tipos de resultados. O "padrão de resultado" (inspirado em Rust) fornece tratamento de erros em tempo de compilação.
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

### Q5: O que são arquivos de declaração (.d.ts) e como posso usar tipos de terceiros?
**R:** Os arquivos de declaração descrevem os tipos de bibliotecas JavaScript que não possuem tipos TypeScript integrados. Eles contêm apenas informações de tipo (sem código de tempo de execução). Instale tipos mantidos pela comunidade de DefinitelyTyped:`npm install --save-dev @types/lodash`. Para suas próprias bibliotecas, adicione um campo`types`em`package.json`ou inclua arquivos`.d.ts`junto com sua fonte. Use`declare module`para declarações de ambiente.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construir um emissor de eventos com segurança de tipo
**Declaração do problema:** Crie um emissor de evento genérico e de tipo seguro no TypeScript, onde cada nome de evento é mapeado para um tipo de carga útil específico. O compilador deve capturar nomes de eventos e tipos de carga incorretos em tempo de compilação.
**Etapa 1 — Entenda o problema:**
Precisamos de um sistema de eventos onde: (1) os eventos sejam definidos com seus tipos de carga útil, (2)`emit`aceita apenas nomes de eventos válidos com cargas corretas, (3)`on`aceita apenas nomes de eventos válidos com manipuladores digitados corretamente. Isso requer tipos mapeados e genéricos em uma interface de mapa de eventos.
**Etapa 2 — Identifique a abordagem:**
- Defina um tipo `EventMap`:`{ [eventName: string]: payloadType }`.
- Use`keyof EventMap`para restringir nomes de eventos.
- Use`EventMap[K]`para obter o tipo de carga útil para um evento específico.
- Armazene ouvintes em um`Map<string, Function[]>`.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Segurança de tipo: o compilador detecta nomes de eventos errados e formas de carga erradas em tempo de compilação.
-`on`retorna uma função de cancelamento de assinatura para limpeza conveniente.
-`once`envolve o ouvinte para cancelar a assinatura automaticamente após a primeira invocação.
- Para produção: adicione`listenerCount`,`removeAllListeners`e considere usar`AbortSignal`para cancelamento.
### Problema 2: implementar um construtor de consultas SQL com segurança de tipo
**Declaração do problema:** Crie um construtor de consultas SQL em que os nomes e tipos de colunas sejam derivados de uma interface TypeScript. O construtor deve evitar nomes de coluna inválidos e incompatibilidades de tipo em tempo de compilação.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) nomes de colunas restritos a`keyof T`, (2) valores da cláusula WHERE digitados de acordo com a coluna, (3) API encadeada para construção de consultas. Isso requer genéricos restritos por`Record<string, unknown>`.
**Etapa 2 — Identifique a abordagem:**
- Use`keyof T`para restrições de nome de coluna.
- Use`T[K]`para restrições de tipo de valor.
- Construir string SQL com consultas parametrizadas (evitar injeção de SQL).
- Métodos encadeados retornam`this`.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Prevenção de injeção de SQL: todos os valores passam por consultas parametrizadas (`$1`,`$2`), nunca interpoladas.
- Segurança de tipo: nomes de colunas e tipos de valores são verificados em tempo de compilação.
- Extensibilidade: adicione os métodos`join`,`groupBy`,`having`,`insert`,`update`seguindo o mesmo padrão.
- Produção: use`kysely`ou`drizzle-orm`— eles fornecem segurança a esse tipo com cobertura SQL completa.
### Problema 3: Implementar uma máquina de estados finitos com segurança de tipo
**Declaração do problema:** Crie uma máquina de estado finito com segurança de tipo onde transições válidas são impostas em tempo de compilação. Cada estado pode ter ações de entrada/saída e a máquina deve rastrear o estado atual.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) estados e eventos definidos como tipos, (2) transições válidas mapeadas no nível de tipo, (3) o compilador evita transições inválidas, (4) rastreamento de estado de tempo de execução com retornos de chamada. Isso requer tipos mapeados e tipos condicionais.
**Etapa 2 — Identifique a abordagem:**
- Defina um `TransitionMap`: `{ [State]: { [Event]: NextState } }`.
- Use genéricos para restringir`send(event)`com base no estado atual.
- Acompanhe o estado em tempo de execução com uma variável.
- Suporte a retornos de chamada de entrada/saída por estado.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Segurança em tempo de execução:`send`lança transições inválidas.
- Segurança de tipo: o tipo`EventsFor`extrai eventos válidos por estado em tempo de compilação.
- Retornos de chamada de entrada/saída são acionados automaticamente nas transições.
- Para produção: use`xstate`— ele fornece uma biblioteca completa de máquinas de estado com depuração visual, estados hierárquicos, guardas e ações.
---

## Resumo
TypeScript é JavaScript feito corretamente para qualquer coisa além de scripts triviais. Ele adiciona um poderoso sistema de tipos que detecta bugs antecipadamente, melhora as ferramentas e documenta o código - tudo isso enquanto compila para JavaScript padrão que pode ser executado em qualquer lugar. A curva de aprendizado é suave (você pode começar com tipos mínimos), mas a profundidade é vasta (o sistema de tipos é Turing-completo). Para o desenvolvimento moderno de JavaScript, o TypeScript se tornou o padrão da indústria.