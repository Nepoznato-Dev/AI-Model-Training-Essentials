---
# Metadata
title: "TypeScript — Cheat Sheet"
description: "Quick-reference cheat sheet for TypeScript types, generics, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [typescript, types, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# تايب سكريبت - ورقة الغش
## الأنواع الأساسية
```typescript
// Primitives
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;
let nothing: null = null;
let undef: undefined = undefined;

// Arrays
let nums: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// Tuples
let pair: [string, number] = ["age", 30];
let triple: [string, number, boolean] = ["test", 1, true];

// Enums
enum Direction { Up, Down, Left, Right }
enum Status { Active = "ACTIVE", Inactive = "INACTIVE" }

// Any (avoid)
let x: any = "anything";

// Unknown (type-safe alternative to any)
let u: unknown = "hello";
if (typeof u === "string") {
    u.toUpperCase();  // narrowed to string
}

// Void & Never
function log(msg: string): void { console.log(msg); }
function fail(msg: string): never { throw new Error(msg); }
```

## الواجهات والأنواع
```typescript
// Interface
interface User {
    name: string;
    age: number;
    email?: string;  // optional
    readonly id: number;
}

// Type alias
type Point = { x: number; y: number };
type ID = string | number;

// Extending
interface Admin extends User {
    permissions: string[];
}

// Intersection
type AdminUser = User & { permissions: string[] };

// Index signature
interface Dictionary {
    [key: string]: number;
}

// Mapped types
type Readonly<T> = { readonly [K in keyof T]: T[K] };
type Partial<T> = { [K in keyof T]?: T[K] };
type Pick<T, K extends keyof T> = { [P in K]: T[P] };
type Record<K extends string, V> = { [P in K]: V };
```

## النقابات التمييزية
```typescript
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "rectangle"; width: number; height: number }
    | { kind: "point" };

function area(s: Shape): number {
    switch (s.kind) {
        case "circle": return Math.PI * s.radius ** 2;
        case "rectangle": return s.width * s.height;
        case "point": return 0;
    }
}

// Exhaustiveness check
function assertNever(x: never): never {
    throw new Error("Unexpected: " + x);
}
```

## الأدوية العامة
```typescript
// Generic function
function first<T>(arr: T[]): T | undefined {
    return arr[0];
}

// Generic interface
interface Result<T, E = Error> {
    ok: boolean;
    data?: T;
    error?: E;
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
}

// Utility types
type Partial<T> = { [K in keyof T]?: T[K] };
type Required<T> = { [K in keyof T]: T[K] };
type Nullable<T> = { [K in keyof T]: T[K] | null };
type Awaited<T> = T extends Promise<infer U> ? U : T;
```

## الوظائف
```typescript
// Typed function
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
const greet = (name: string): string => `Hello, ${name}!`;

// Optional & default params
function create(name: string, role: string = "user"): User { ... }
function search(query?: string): Results { ... }

// Rest parameters
function log(...args: any[]): void { console.log(...args); }

// Overloads
function parse(input: string): Date;
function parse(input: number): Date;
function parse(input: string | number): Date {
    return new Date(typeof input === "string" ? input : input * 1000);
}

// Type guards as return types
function isString(val: unknown): val is string {
    return typeof val === "string";
}
```

## غير متزامن
```typescript
// Promise
async function fetchUser(id: number): Promise<User> {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json() as Promise<User>;
}

// Async generator
async function* paginate(url: string): AsyncGenerator<Item[]> {
    let page = 1;
    while (true) {
        const items = await fetchPage(url, page++);
        if (items.length === 0) break;
        yield items;
    }
}

// Promise utilities
const results: [User, Post[]] = await Promise.all([
    fetchUser(1),
    fetchPosts()
]);
```

## أنماط المنفعة
```typescript
// Type narrowing
if (typeof x === "string") { ... }
if (x instanceof Error) { ... }
if ("name" in obj) { ... }

// Satisfies operator (TS 4.9+)
const config = {
    host: "localhost",
    port: 3000,
} satisfies Record<string, string | number>;

// const assertions
const colors = ["red", "green", "blue"] as const;
// type: readonly ["red", "green", "blue"]

// Template literal types
type EventName = `on${Capitalize<string>}`;
type Route = `/${string}`;

// Conditional types
type IsString<T> = T extends string ? true : false;
type NonNullable<T> = T extends null | undefined ? never : T;

// Branded types
type UserId = string & { readonly __brand: "UserId" };
const toUserId = (s: string): UserId => s as UserId;
```
