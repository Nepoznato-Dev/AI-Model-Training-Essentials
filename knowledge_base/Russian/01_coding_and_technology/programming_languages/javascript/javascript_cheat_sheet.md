---
# Metadata
title: "JavaScript — Cheat Sheet"
description: "Quick-reference cheat sheet for JavaScript (ES2024+) syntax and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [javascript, es6, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# JavaScript — шпаргалка
## Основы
```javascript
// Variables
const name = "Alice";    // immutable binding
let age = 30;            // mutable binding
var legacy = "avoid";    // function-scoped — avoid

// Types
typeof name       // "string"
typeof 42         // "number"
typeof true       // "boolean"
typeof undefined  // "undefined"
typeof null       // "object" (historic bug)
typeof []         // "object"
Array.isArray([]) // true

// Template literals
`Hello, ${name}! You are ${age}.`
`Multi
line
string`

// String methods
name.toUpperCase()
name.includes("lic")
name.slice(0, 3)
name.replace("Alice", "Bob")
"  hi  ".trim()
"a,b,c".split(",")
```

## Структуры данных
```javascript
// Array
const arr = [1, 2, 3];
arr.push(4);
arr.map(x => x * 2);       // [2, 4, 6, 8]
arr.filter(x => x > 2);    // [3, 4]
arr.reduce((sum, x) => sum + x, 0);
arr.find(x => x > 2);      // 3
arr.some(x => x > 2);      // true
arr.flat();                 // flatten nested
arr.flatMap(x => [x, x*2]); // map + flatten
[...arr, 5, 6];             // spread

// Object
const user = { name: "Alice", age: 30 };
const { name, age } = user; // destructuring
const copy = { ...user, email: "a@b.com" }; // spread
Object.keys(user);    // ["name", "age"]
Object.values(user);  // ["Alice", 30]
Object.entries(user); // [["name","Alice"],["age",30]]

// Map & Set
const map = new Map();
map.set("key", "value");
map.get("key");

const set = new Set([1, 2, 3]);
set.add(4);
set.has(2); // true
```

## Поток управления
```javascript
if (condition) { ... }
else if (other) { ... }
else { ... }

// Ternary
const result = condition ? "yes" : "no";

// Nullish coalescing
const value = maybeNull ?? "default";

// Optional chaining
const len = user?.address?.street?.length;

// Loops
for (const item of iterable) { ... }
for (const [i, val] of arr.entries()) { ... }
for (const key in object) { ... }  // enumerable keys

// Switch
switch (action) {
  case "start": run(); break;
  case "stop": halt(); break;
  default: idle();
}
```

## Функции
```javascript
// Arrow function
const add = (a, b) => a + b;
const greet = name => `Hello, ${name}!`;

// Default params
function create(name, role = "user") { ... }

// Rest parameters
function log(...args) { console.log(args); }

// Destructuring params
function render({ title, count = 0 }) { ... }

// Closures
function counter() {
  let n = 0;
  return { increment: () => ++n, value: () => n };
}

// IIFE
(() => { console.log("runs immediately"); })();
```

## Асинхронный
```javascript
// Promise
fetch(url)
  .then(res => res.json())
  .then(data => process(data))
  .catch(err => console.error(err));

// Async/Await
async function loadUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    const user = await res.json();
    return user;
  } catch (err) {
    console.error("Failed:", err);
  }
}

// Parallel
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts()
]);

// Promise.allSettled
const results = await Promise.allSettled([p1, p2, p3]);
```

## Классы
```javascript
class Animal {
  #name;  // private field
  constructor(name) { this.#name = name; }
  speak() { return `${this.#name} makes a sound`; }
  get name() { return this.#name; }
}

class Dog extends Animal {
  speak() { return `${this.#name} barks`; }
}

// Static
class Math {
  static add(a, b) { return a + b; }
}
Math.add(1, 2);
```

## Модули
```javascript
// ESM
export const PI = 3.14;
export default class Calculator { ... }
import Calculator, { PI } from './calc.js';

// Dynamic import
const mod = await import('./heavy-module.js');
```

## Общие шаблоны
```javascript
// Spread & destructuring
const [first, ...rest] = arr;
const { name, ...others } = user;

// Short-circuit
condition && doSomething();
error || fallback();

// Array from
Array.from({ length: 5 }, (_, i) => i * 2);
[...new Set(items)];  // unique values

// Object.fromEntries
const obj = Object.fromEntries(map);
```
