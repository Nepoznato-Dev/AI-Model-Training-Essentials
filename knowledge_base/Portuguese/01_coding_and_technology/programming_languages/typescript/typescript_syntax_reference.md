---
# Metadata
title: "TypeScript — Syntax Reference"
description: "Detailed syntax reference for TypeScript covering type system, generics, utility types, control flow, classes, modules, decorators, and advanced type operations."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [typescript, syntax-reference, type-system, generics, utility-types, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# TypeScript — Referência de sintaxe
Este documento fornece uma referência de sintaxe estruturada e abrangente para TypeScript. Ele complementa a referência principal do TypeScript, concentrando-se no sistema de tipos, genéricos, tipos de utilitários e programação avançada em nível de tipo.
---

## Digite Fundamentos do Sistema
### Tipos primitivos e integrados
```typescript
// Primitives
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;
let nothing: null = null;
let undef: undefined = undefined;
let big: bigint = 9007199254740991n;
let sym: symbol = Symbol("id");

// Special types
let anyVal: any = "anything";      // Opts out of type checking — avoid
let unknownVal: unknown = 42;      // Type-safe alternative to any
let neverVal: never = (() => { throw new Error(); })();  // Never returns
let voidVal: void = undefined;     // No return value
```

### Tipos literais e uniões
```typescript
// Literal types
const direction: "north" | "south" | "east" | "west" = "north";
const statusCode: 200 | 404 | 500 = 200;
const pi: 3.14159 = 3.14159;

// Union types
type StringOrNumber = string | number;
type Result = Success | Error;

// Narrowing with type guards
function process(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase();  // TypeScript knows: string
  }
  return value.toFixed(2);       // TypeScript knows: number
}

// Discriminated unions (tagged unions)
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle": return Math.PI * shape.radius ** 2;
    case "rectangle": return shape.width * shape.height;
    case "triangle": return 0.5 * shape.base * shape.height;
  }
}
```

### Interfaces e aliases de tipo
```typescript
// Interface — best for object shapes
interface User {
  readonly id: string;          // Cannot be reassigned
  name: string;
  email?: string;               // Optional property
  readonly tags: readonly string[];  // Immutable array
}

// Extending interfaces
interface Admin extends User {
  permissions: string[];
}

// Type alias — more flexible
type ID = string | number;
type Callback<T> = (data: T) => void;
type Pair<T, U> = [T, U];

// Index signatures
interface Dictionary<T> {
  [key: string]: T;
}

// Intersection types
type Timestamped = { createdAt: Date; updatedAt: Date };
type UserRecord = User & Timestamped;  // Has all fields from both
```

---

## Genéricos
### Funções e classes genéricas
```typescript
// Generic function
function identity<T>(value: T): T { return value; }
const num = identity(42);        // T inferred as number
const str = identity("hello");   // T inferred as string

// Multiple type parameters
function pair<A, B>(first: A, second: B): [A, B] {
  return [first, second];
}

// Generic constraints
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}

// Generic class
class Stack<T> {
  private items: T[] = [];
  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
  peek(): T | undefined { return this.items[this.items.length - 1]; }
  get size(): number { return this.items.length; }
}

// Generic constraints with keyof
function pluck<T, K extends keyof T>(objects: T[], key: K): T[K][] {
  return objects.map(obj => obj[key]);
}
const users = [{ name: "Alice", age: 30 }, { name: "Bob", age: 25 }];
const names = pluck(users, "name");  // string[]
```

### Tipos Condicionais
```typescript
// Conditional type — type-level if/else
type IsString<T> = T extends string ? true : false;
type A = IsString<"hello">;  // true
type B = IsString<42>;       // false

// Distributive conditional types
type ToArray<T> = T extends any ? T[] : never;
type C = ToArray<string | number>;  // string[] | number[]

// infer keyword — extract types
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type D = ReturnType<() => string>;  // string

type ElementType<T> = T extends (infer U)[] ? U : T;
type E = ElementType<string[]>;     // string

// Template literal types
type EventName<T extends string> = `on${Capitalize<T>}`;
type F = EventName<"click">;        // "onClick"

type PathSegment = `/${string}`;
type G = PathSegment;               // `/${string}`
```

---

## Tipos de utilitários
### Tipos de utilitários integrados
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

// Partial<T> — all properties optional
type UpdateUser = Partial<User>;
// { id?: string; name?: string; email?: string; age?: number }

// Required<T> — all properties required
type FullUser = Required<Partial<User>>;

// Readonly<T> — all properties readonly
type FrozenUser = Readonly<User>;

// Pick<T, K> — select specific properties
type UserBasic = Pick<User, "id" | "name">;
// { id: string; name: string }

// Omit<T, K> — exclude specific properties
type UserNoEmail = Omit<User, "email">;
// { id: string; name: string; age: number }

// Record<K, V> — object with key type K and value type V
type UserMap = Record<string, User>;
type StatusCodes = Record<"ok" | "error" | "pending", number>;

// Exclude<T, U> — remove U from union T
type NonStatus = Exclude<"active" | "inactive" | "pending", "pending">;
// "active" | "inactive"

// Extract<T, U> — keep only U from union T
type StatusStrings = Extract<"active" | 42 | "pending", string>;
// "active" | "pending"

// NonNullable<T> — remove null and undefined
type NonNull = NonNullable<string | null | undefined>;  // string

// ReturnType<T> — extract return type of function
type R = ReturnType<() => Promise<string>>;  // Promise<string>

// Parameters<T> — extract function parameters as tuple
type P = Parameters<(name: string, age: number) => void>;
// [name: string, age: number]

// Awaited<T> — unwrap Promise
type A = Awaited<Promise<Promise<string>>>;  // string
```

### Tipos de utilitários personalizados
```typescript
// Deep partial — recursively make all properties optional
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

// Deep readonly
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

// Mutable — remove readonly
type Mutable<T> = { -readonly [K in keyof T]: T[K] };

// Nullable — make all properties nullable
type Nullable<T> = { [K in keyof T]: T[K] | null };

// Type-safe event handler
type EventHandler<T extends string> = T extends `${infer E}Changed`
  ? (newValue: E) => void
  : never;

// Branded types — nominal typing
type Brand<T, B extends string> = T & { __brand: B };
type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;

function getUser(id: UserId): User { /* ... */ }
// getUser("abc");           // Error: string not assignable to UserId
// getUser("abc" as UserId); // OK — explicit cast
```

---

## Classes e OOP
```typescript
// Abstract class
abstract class Animal {
  constructor(
    protected readonly name: string,
    private readonly sound: string
  ) {}

  abstract speak(): string;

  describe(): string {
    return `${this.name} says ${this.speak()}`;
  }
}

// Concrete class with access modifiers
class Dog extends Animal {
  private tricks: string[] = [];

  constructor(name: string) {
    super(name, "Woof");
  }

  speak(): string { return `${this.name} says Woof!`; }

  learn(trick: string): this {
    this.tricks.push(trick);
    return this;  // Enable chaining
  }

  get trickCount(): number { return this.tricks.length; }
}

// Implements interface
interface Serializable<T> {
  serialize(): string;
  deserialize(data: string): T;
}

class UserRecord implements Serializable<UserRecord> {
  constructor(public name: string, public email: string) {}

  serialize(): string {
    return JSON.stringify({ name: this.name, email: this.email });
  }

  deserialize(data: string): UserRecord {
    const { name, email } = JSON.parse(data);
    return new UserRecord(name, email);
  }
}

// Parameter properties (shorthand)
class Point {
  constructor(
    public readonly x: number,
    public readonly y: number,
  ) {}
}
// Equivalent to declaring x, y as properties and assigning in constructor
```

---

## Módulos e importações
```typescript
// Named exports
export const API_URL = "https://api.example.com";
export function fetchUser(id: string): Promise<User> { /* ... */ }
export class UserService { /* ... */ }

// Default export
export default class Config { /* ... */ }

// Re-exports
export { default as Button } from "./Button";
export * from "./types";
export { type User, type Admin } from "./models";

// Importing
import Config from "./config";
import { fetchUser, type User } from "./api";
import * as Utils from "./utils";

// Type-only imports (erased at compile time)
import type { User, Admin } from "./models";

// Dynamic imports
const module = await import("./heavy-module");

// Import attributes
import data from "./config.json" with { type: "json" };
```

---

## Decoradores (TC39 Estágio 3 / TypeScript 5.0+)
```typescript
// Class decorator
function sealed<T extends new (...args: any[]) => any>(constructor: T) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

@sealed
class User {
  constructor(public name: string) {}
}

// Method decorator
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

// Property decorator
function required(target: any, key: string) {
  let value: any = target[key];
  const getter = () => value;
  const setter = (newVal: any) => {
    if (newVal === null || newVal === undefined) {
      throw new Error(`${key} is required`);
    }
    value = newVal;
  };
  Object.defineProperty(target, key, { get: getter, set: setter });
}

class Form {
  @required name: string = "";
  @required email: string = "";
}
```

---

## Padrões Avançados
### Verificação exaustiva
```typescript
// Using never for exhaustive switch
function assertNever(x: never): never {
  throw new Error(`Unexpected value: ${x}`);
}

type Color = "red" | "green" | "blue";

function hexFor(color: Color): string {
  switch (color) {
    case "red": return "#ff0000";
    case "green": return "#00ff00";
    case "blue": return "#0000ff";
    default: return assertNever(color);
    // If a new color is added to the union,
    // this line will error — catching the missing case
  }
}
```

### Const Asserções e Estreitamento
```typescript
// const assertion — deepest readonly literal type
const config = {
  api: {
    baseUrl: "https://api.example.com",
    timeout: 5000,
    retries: 3,
  },
} as const;

// Type of config.api.baseUrl is "https://api.example.com" (literal)
// Type of config.api.timeout is 5000 (literal)

// satisfies — validate type without widening
const palette = {
  red: [255, 0, 0],
  green: [0, 255, 0],
  blue: [0, 0, 255],
} satisfies Record<string, [number, number, number]>;

// palette.red is still [255, 0, 0] (tuple), not number[]
```

### Tipos literais de modelo
```typescript
// CSS-in-JS type safety
type CSSProperty = "color" | "background" | "margin" | "padding";
type CSSValue = string | number;
type CSSRule = `${CSSProperty}: ${CSSValue}`;

const rule: CSSRule = "color: red";       // OK
// const bad: CSSRule = "invalid: red";   // Error

// Event names
type DOMEvent = `${"click" | "focus" | "blur"}Handler`;
// "clickHandler" | "focusHandler" | "blurHandler"

// Path types
type Route = `/api/${"users" | "posts"}/${string}`;
const r1: Route = "/api/users/123";     // OK
const r2: Route = "/api/posts/abc";     // OK
// const r3: Route = "/api/admin/123";  // Error
```

---

## Resumo
O sistema de tipos do TypeScript é seu recurso definidor e é notavelmente profundo. Desde anotações básicas até genéricos, tipos condicionais, tipos mapeados, tipos literais de modelo e`infer`, o sistema de tipos é essencialmente uma linguagem funcional operando em tempo de compilação. Compreender a interação entre`interface`vs`type`, genéricos vs tipos de utilitários e tipagem estrutural vs nominal suporta a escrita de TypeScript que é seguro e ergonômico. A linguagem continua a evoluir, com cada versão adicionando mais poder expressivo, mantendo total compatibilidade retroativa com JavaScript.