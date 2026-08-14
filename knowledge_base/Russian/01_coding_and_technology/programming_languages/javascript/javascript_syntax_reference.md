---
# Metadata
title: "JavaScript — Syntax Reference"
description: "Detailed syntax reference for JavaScript covering operators, control flow, functions, data structures, OOP, error handling, modules, async patterns, and advanced features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [javascript, syntax-reference, operators, control-flow, functions, oop, async, coding-and-technology]
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
# JavaScript — Справочник по синтаксису
Этот документ предоставляет исчерпывающий структурированный справочник по синтаксису JavaScript. Он дополняет основной справочник по JavaScript, уделяя особое внимание исчерпывающим синтаксическим шаблонам, таблицам операторов и внутренней механике.
---

## Операторы и выражения
### Арифметические операторы
| Оператор | Имя | Пример | Результат | Заметки |
|----------|------|---------|--------|-------|
| `+`| Дополнение | `3 + 2`| `5`| Также конкатенация строк |
| `-`| Вычитание | `3 - 2`| `1`| |
| `*`| Умножение | `3 * 2`| `6`| |
| `/`| Отдел | `7 / 2`| `3.5`| |
| `%`| Остаток | `7 % 2`| `1`| |
| `**`| Возведение в степень | `2 ** 10`| `1024`| ES2016 |
| `++`| Приращение | `x++`/`++x`| | Пост- и предварительный прирост |
| `--`| Декремент | `x--`/`--x`| | Пост- и предварительный декремент |
| `+x`,`-x`| Унарный | `+"42"`→`42`| Приведение типа к номеру |
### Сравнение и равенство
| Оператор | Имя | Пример | Заметки |
|----------|------|---------|-------|
| `===`| Строгое равенство | `1 === 1`| Никакого приведения типов — всегда предпочитайте это |
| `!==`| Строгое неравенство | `1 !== "1"`| `true`— разные типы |
| `==`| Абстрактное равенство | `1 == "1"`| Приведение типа — избегать |
| `!=`| Абстрактное неравенство | `1 != "1"`| `false`— избегать |
| `<`,`>`,`<=`,`>=`| Реляционный | `"b" > "a"`| Лексикографика для строк |
### Логические и нулевые операторы
| Оператор | Имя | Пример | Заметки |
|----------|------|---------|-------|
| `&&`| Логическое И | `a && b`| Возвращает первое ложное или последнее значение |
| `\|\|`| Логическое ИЛИ | `a \|\| b`| Возвращает первое истинное или последнее значение |
| `!`| Логическое НЕ | `!true`| `false`|
| `??`| Нулевое объединение | `a ?? b`| Возвращает `b`, только если`a`равен`null`/`undefined`|
| `?.`| Дополнительное связывание | `obj?.prop?.method()`| Короткое замыкание на`undefined`|
### Побитовые операторы
| Оператор | Имя | Пример | Заметки |
|----------|------|---------|-------|
| `&`| И | `5 & 3`| `1`|
| `\|`| ИЛИ | `5 \| 3`| `7`|
| `^`| ИСКЛЮЧАЮЩЕЕ ИЛИ | `5 ^ 3`| `6`|
| `~`| НЕ | `~5`| `-6`|
| `<<`| Левый сдвиг | `5 << 1`| `10`|
| `>>`| Подписанный правый сдвиг | `-5 >> 1`| `-3`|
| `>>>`| Беззнаковый правый сдвиг | `-1 >>> 0`| `4294967295`|
### Присвоение и деструктуризация
```javascript
// Basic assignment
let x = 10;

// Compound assignment
x += 5;     // x = x + 5
x -= 3;     // x = x - 3
x *= 2;     // x = x * 2
x /= 4;     // x = x / 4
x %= 7;     // x = x % 7
x **= 2;    // x = x ** 2
x &= 0xFF;  // Bitwise AND
x |= 0x0F;  // Bitwise OR
x ^= 0xFF;  // Bitwise XOR
x <<= 2;    // Left shift
x >>= 1;    // Right shift
x >>>= 1;   // Unsigned right shift

// Logical assignment (ES2021)
x ||= "default";       // x = x || "default"
x &&= validate(x);     // x = x && validate(x)
x ??= fallback;        // x = x ?? fallback (only if null/undefined)

// Destructuring assignment
const { name, age, ...rest } = user;
const [first, , third] = array;
const { a: x, b: y } = { a: 1, b: 2 };  // Rename while destructuring

// Nested destructuring
const { address: { city, zip } } = user;
const [[a, b], [c, d]] = [[1, 2], [3, 4]];

// Swap variables
[a, b] = [b, a];
```

### Приоритет оператора (от самого высокого к самому низкому)
| Приоритет | Операторы | Ассоциативность |
|------------|-----------|---------------|
| 1 (самый высокий) | `()``[]``.``?.` | Левый |
| 2 | `new`(без аргументов) | Правильно |
| 3 | `++``--` (постфикс) | Н/Д |
| 4 | `!``~``+x``-x``typeof``void``delete``++``--`(префикс) | Правильно |
| 5 | `**`| Правильно |
| 6 | `*``/``%`| Левый |
| 7 | `+``-` | Левый |
| 8 | `<<``>>``>>>`| Левый |
| 9 | `<``<=``>``>=``in``instanceof` | Левый |
| 10 | `===``!==``==``!=` | Левый |
| 11 | `&`| Левый |
| 12 | `^`| Левый |
| 13 | `\|`| Левый |
| 14 | `&&`| Левый |
| 15 | `\|\|`| Левый |
| 16 | `??`| Левый |
| 17 | `=``+=``-=`и т. д. | Правильно |
| 18 (самый низкий) | `=>`(функция стрелки) | Правильно |
---

## Поток управления
### Условные операторы
```javascript
// if / else if / else
if (score >= 90) {
  grade = "A";
} else if (score >= 80) {
  grade = "B";
} else {
  grade = "F";
}

// Ternary operator
const status = age >= 18 ? "adult" : "minor";

// Nested ternary (use sparingly — hard to read)
const category = score >= 90 ? "excellent"
                : score >= 70 ? "good"
                : "needs work";

// Switch statement
switch (action) {
  case "start":
    engine.start();
    break;
  case "stop":
    engine.stop();
    break;
  case "pause":
  case "hold":                    // Fall-through (intentional)
    engine.pause();
    break;
  default:
    console.warn(`Unknown action: ${action}`);
}

// Switch with expression (using IIFE)
const result = ((action) => {
  switch (action) {
    case "add": return a + b;
    case "sub": return a - b;
    default: return 0;
  }
})(op);
```

### Циклы
```javascript
// for loop
for (let i = 0; i < 10; i++) {
  if (i === 5) continue;   // Skip iteration
  if (i === 8) break;       // Exit loop
  console.log(i);
}

// for...of — iterate values (arrays, strings, Maps, Sets, iterables)
for (const item of [10, 20, 30]) {
  console.log(item);
}
for (const [index, value] of ["a", "b", "c"].entries()) {
  console.log(`${index}: ${value}`);
}

// for...in — iterate keys (objects) — do NOT use for arrays
for (const key in user) {
  if (Object.hasOwn(user, key)) {
    console.log(`${key}: ${user[key]}`);
  }
}

// while loop
let count = 0;
while (count < 5) {
  console.log(count++);
}

// do...while — always executes at least once
do {
  const input = prompt("Enter 'quit' to exit:");
} while (input !== "quit");

// Labeled loops (for breaking out of nested loops)
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) break outer;
    console.log(`i=${i}, j=${j}`);
  }
}
```

---

## Функции
### Объявления функций и выражения
```javascript
// Function declaration (hoisted)
function add(a, b) {
  return a + b;
}

// Function expression (not hoisted)
const multiply = function(a, b) {
  return a * b;
};

// Arrow function (lexical 'this', no 'arguments')
const divide = (a, b) => a / b;
const square = x => x * x;            // Single param: no parens needed
const greet = () => "Hello!";          // No params: empty parens
const createObj = () => ({ x: 1 });   // Return object literal: wrap in ()

// Default parameters
function connect(host, port = 8080, timeout = 30000) {
  // ...
}

// Rest parameters
function log(...messages) {
  messages.forEach(msg => console.log(msg));
}

function merge(base, ...overrides) {
  return Object.assign({}, base, ...overrides);
}

// IIFE (Immediately Invoked Function Expression)
const result = (() => {
  const secret = 42;
  return secret * 2;
})();
```

### Замыкания и функции высшего порядка
```javascript
// Closure — function retains access to outer scope
function makeCounter(initial = 0) {
  let count = initial;
  return {
    increment: () => ++count,
    decrement: () => --count,
    getCount: () => count,
  };
}

const counter = makeCounter(10);
counter.increment();   // 11
counter.increment();   // 12
counter.getCount();    // 12

// Higher-order functions
const numbers = [1, 2, 3, 4, 5];

// map
const doubled = numbers.map(n => n * 2);

// filter
const evens = numbers.filter(n => n % 2 === 0);

// reduce
const sum = numbers.reduce((acc, n) => acc + n, 0);

// Chaining
const result = numbers
  .filter(n => n > 2)
  .map(n => n * 10)
  .reduce((sum, n) => sum + n, 0);

// Function composition
const pipe = (...fns) => (x) => fns.reduce((acc, fn) => fn(acc), x);
const process = pipe(
  x => x * 2,
  x => x + 1,
  x => `Result: ${x}`
);
process(5);  // "Result: 11"
```

### Генераторы
```javascript
// Generator function
function* fibonacci() {
  let a = 0, b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
fib.next().value;   // 0
fib.next().value;   // 1
fib.next().value;   // 1
fib.next().value;   // 2

// Generator with bidirectional communication
function* accumulator() {
  let total = 0;
  while (true) {
    const value = yield total;
    total += value;
  }
}

const acc = accumulator();
acc.next();          // Prime: { value: 0, done: false }
acc.next(10);        // { value: 10, done: false }
acc.next(20);        // { value: 30, done: false }

// Async generator
async function* fetchPages(url) {
  let page = 1;
  while (true) {
    const response = await fetch(`${url}?page=${page}`);
    const data = await response.json();
    if (data.length === 0) return;
    yield data;
    page++;
  }
}

// Consume async generator
for await (const page of fetchPages("/api/items")) {
  processItems(page);
}
```

---

## Структуры данных
### Обзор встроенных коллекций
| Коллекция | Заказал | Изменяемый | Дубликаты | Тип ключа | Поиск |
|------------|---------|---------|------------|----------|--------|
| `Array`| Да | Да | Да | Индекс (номер) | О(п) |
| `Object`| Да (вставка) | Да | Ключи: Нет | Строка/Символ | O(1) среднее |
| `Map`| Да (вставка) | Да | Ключи: Нет | Любой | O(1) среднее |
| `Set`| Да (вставка) | Да | Нет | — | O(1) среднее |
| `WeakMap`| Нет | Да | Ключи: Нет | Только объект | O(1) среднее |
| `WeakSet`| Нет | Да | Нет | Только объект | O(1) среднее |
### Массивы
```javascript
// Creation
const nums = [1, 2, 3, 4, 5];
const fromRange = Array.from({ length: 5 }, (_, i) => i + 1);  // [1,2,3,4,5]
const filled = Array(3).fill(0);                                  // [0, 0, 0]
const flat = [[1, 2], [3, 4]].flat();                            // [1, 2, 3, 4]
const deep = [[1, [2]], [3]].flat(Infinity);                     // [1, 2, 3]

// Access
const first = nums[0];
const last = nums.at(-1);                  // Array.at() — ES2022
const slice = nums.slice(1, 4);            // [2, 3, 4] — non-mutating

// Mutation
nums.push(6);                              // Add to end
nums.unshift(0);                           // Add to beginning
nums.pop();                                // Remove from end
nums.shift();                              // Remove from beginning
nums.splice(2, 1, 99);                     // Remove 1 at index 2, insert 99
nums.reverse();                            // In-place reverse
nums.sort((a, b) => a - b);               // In-place numeric sort

// Search
const idx = nums.indexOf(3);               // First occurrence (-1 if not found)
const lastIdx = nums.lastIndexOf(3);       // Last occurrence
const hasThree = nums.includes(3);         // Boolean check
const found = nums.find(n => n > 3);       // First matching element
const foundIdx = nums.findIndex(n => n > 3);
const allEven = nums.every(n => n % 2 === 0);
const anyEven = nums.some(n => n % 2 === 0);

// Transformation (non-mutating)
const mapped = nums.map(n => n * 2);
const filtered = nums.filter(n => n > 2);
const reduced = nums.reduce((sum, n) => sum + n, 0);
const grouped = nums.reduce((groups, n) => {
  const key = n % 2 === 0 ? "even" : "odd";
  (groups[key] ??= []).push(n);
  return groups;
}, {});

// Iteration
nums.forEach((n, i) => console.log(`${i}: ${n}`));
for (const [i, n] of nums.entries()) {
  console.log(`${i}: ${n}`);
}
```

### Объекты
```javascript
// Creation
const user = { name: "Alice", age: 30 };
const dynamic = { [keyName]: value };            // Computed property
const shorthand = { name, age };                  // Property shorthand
const method = {
  greet() { return `Hi, I'm ${this.name}`; },    // Method shorthand
  get fullName() { return `${this.first} ${this.last}`; },  // Getter
  set fullName(v) { [this.first, this.last] = v.split(" "); }  // Setter
};

// Access
const name = user.name;
const age = user["age"];
const optional = user?.address?.city;             // Optional chaining
const fallback = user.email ?? "none";            // Nullish coalescing

// Mutation
user.email = "alice@example.com";
delete user.age;
Object.assign(user, { role: "admin", active: true });  // Merge

// Inspection
Object.keys(user);       // ["name", "email", "role", "active"]
Object.values(user);     // ["Alice", "alice@...", "admin", true]
Object.entries(user);    // [["name","Alice"], ["email","alice@..."], ...]
Object.hasOwn(user, "name");  // true (replaces hasOwnProperty)

// Immutability patterns
const frozen = Object.freeze({ x: 1, y: 2 });     // Shallow freeze
const sealed = Object.seal({ x: 1 });              // Can't add/remove props
const descriptor = Object.getOwnPropertyDescriptor(user, "name");
Object.defineProperty(user, "id", {
  value: 123,
  writable: false,
  enumerable: true,
  configurable: false
});
```

### Карта и набор
```javascript
// Map — any key type, ordered, iterable
const map = new Map();
const objKey = { id: 1 };
map.set("string", 1);
map.set(objKey, 2);           // Object as key
map.set(Symbol("sym"), 3);

map.get("string");             // 1
map.get(objKey);               // 2
map.has("string");             // true
map.size;                      // 3
map.delete("string");
map.clear();

// Iteration
for (const [key, value] of map) {
  console.log(`${key} => ${value}`);
}
map.forEach((value, key) => console.log(key, value));

// Map from / to object
const fromObj = new Map(Object.entries({ a: 1, b: 2 }));
const toObj = Object.fromEntries(map);

// Set — unique values, ordered
const set = new Set([1, 2, 2, 3, 3]);  // Set(3) {1, 2, 3}
set.add(4);
set.has(3);                            // true
set.size;                              // 4
set.delete(1);

// Set operations (using spread)
const a = new Set([1, 2, 3, 4]);
const b = new Set([3, 4, 5, 6]);
const union = new Set([...a, ...b]);                    // {1,2,3,4,5,6}
const intersection = new Set([...a].filter(x => b.has(x)));  // {3,4}
const difference = new Set([...a].filter(x => !b.has(x)));   // {1,2}

// WeakMap — garbage-collectible keys (objects only)
const cache = new WeakMap();
function process(obj) {
  if (cache.has(obj)) return cache.get(obj);
  const result = /* expensive computation */ obj.value * 2;
  cache.set(obj, result);
  return result;
}
// When 'obj' is no longer referenced elsewhere, it's GC'd along with cache entry
```

---

## Объектно-ориентированное программирование
### Классы и наследование
```javascript
// Base class with constructor
class Animal {
  #sound;   // Private field

  constructor(name, sound) {
    this.name = name;        // Public field
    this.#sound = sound;     // Private field
  }

  // Instance method
  speak() {
    return `${this.name} says ${this.#sound}`;
  }

  // Getter
  get info() {
    return `${this.name} (${this.constructor.name})`;
  }

  // Static method
  static create(type, name) {
    const sounds = { dog: "Woof", cat: "Meow", bird: "Tweet" };
    return new Animal(name, sounds[type]);
  }

  // Private method
  #validate() {
    if (!this.name) throw new Error("Name required");
  }
}

// Subclass
class Dog extends Animal {
  #tricks = [];

  constructor(name) {
    super(name, "Woof");     // Must call super() before using 'this'
  }

  learn(trick) {
    this.#tricks.push(trick);
    return this;             // Enable chaining
  }

  showTricks() {
    return `${this.name} knows: ${this.#tricks.join(", ")}`;
  }

  // Override parent method
  speak() {
    return `${super.speak()}!`;
  }
}

const rex = new Dog("Rex");
rex.learn("sit").learn("shake");
console.log(rex.speak());       // "Rex says Woof!"
console.log(rex.showTricks());  // "Rex knows: sit, shake"
```

### Миксины и композиция
```javascript
// Mixin pattern (JavaScript has single inheritance only)
const Serializable = (Base) => class extends Base {
  toJSON() {
    return JSON.stringify(this);
  }
  static fromJSON(json) {
    return Object.assign(new this(), JSON.parse(json));
  }
};

const Validatable = (Base) => class extends Base {
  validate() {
    const errors = [];
    for (const [key, rules] of Object.entries(this.constructor.rules || {})) {
      if (rules.required && !this[key]) errors.push(`${key} is required`);
    }
    return errors;
  }
};

// Compose multiple mixins
class User extends Validatable(Serializable(Animal)) {
  static rules = { name: { required: true } };
  constructor(name, email) {
    super(name, "Hello");
    this.email = email;
  }
}

const user = new User("Alice", "alice@example.com");
user.toJSON();      // '{"name":"Alice","email":"alice@example.com"}'
user.validate();    // []
```

---

## Обработка ошибок
### Шаблоны исключений
```javascript
// try / catch / finally
try {
  const data = JSON.parse(input);
  processData(data);
} catch (error) {
  if (error instanceof SyntaxError) {
    console.error("Invalid JSON:", error.message);
  } else if (error instanceof TypeError) {
    console.error("Type error:", error.message);
  } else {
    throw error;   // Re-throw unknown errors
  }
} finally {
  cleanup();       // Always executes
}

// Custom error classes
class AppError extends Error {
  constructor(message, code, details = {}) {
    super(message);
    this.name = "AppError";
    this.code = code;
    this.details = details;
    Error.captureStackTrace(this, this.constructor);  // V8 only
  }
}

class NotFoundError extends AppError {
  constructor(resource, id) {
    super(`${resource} not found: ${id}`, "NOT_FOUND", { resource, id });
  }
}

// Async error handling
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new NotFoundError("User", id);
    }
    return await response.json();
  } catch (error) {
    if (error instanceof AppError) throw error;
    throw new AppError("Failed to fetch user", "NETWORK_ERROR", { cause: error });
  }
}

// Global error handlers
window.addEventListener("error", (event) => {
  console.error("Uncaught:", event.error);
});
window.addEventListener("unhandledrejection", (event) => {
  console.error("Unhandled rejection:", event.reason);
});

// Assert pattern (no built-in assert in browsers)
function assert(condition, message) {
  if (!condition) throw new Error(`Assertion failed: ${message}`);
}
```

---

## Модули и пакеты
### ES-модули (ESM)
```javascript
// Named exports
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export class Vector { /* ... */ }

// Default export
export default class Calculator { /* ... */ }

// Re-export
export { default as Button } from "./Button.js";
export * from "./utils.js";
export { formatDate, parseDate } from "./dates.js";

// Importing
import Calculator from "./calculator.js";                     // Default
import { add, PI } from "./math.js";                          // Named
import { add as mathAdd } from "./math.js";                   // Rename
import Calculator, { add, PI } from "./calculator.js";        // Both
import * as MathUtils from "./math.js";                       // Namespace
MathUtils.add(1, 2);

// Dynamic import (code splitting)
const module = await import("./heavy-module.js");
module.doSomething();

// Import attributes (ES2025)
import data from "./config.json" with { type: "json" };
```

### CommonJS (устаревший Node.js)
```javascript
// Export
module.exports = { add, subtract };
module.exports = class Calculator { /* ... */ };
exports.helper = function() { /* ... */ };

// Import
const { add, subtract } = require("./math");
const Calculator = require("./calculator");
const fs = require("fs");
```

---

## Асинхронные шаблоны
### Обещания
```javascript
// Creating a Promise
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    if (success) resolve(data);
    else reject(new Error("Failed"));
  }, 1000);
});

// Consuming
promise
  .then(data => process(data))
  .then(result => save(result))
  .catch(error => handleError(error))
  .finally(() => cleanup());

// Promise combinators
const all = await Promise.all([p1, p2, p3]);           // All resolve (or first rejects)
const settled = await Promise.allSettled([p1, p2]);     // All results (resolve or reject)
const first = await Promise.race([p1, p2, timeout]);    // First to settle
const any = await Promise.any([p1, p2, p3]);            // First to resolve

// Promise utilities
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
await delay(1000);  // Sleep for 1 second

// Promise.resolve / Promise.reject
const resolved = Promise.resolve(42);       // Immediately resolved
const rejected = Promise.reject(new Error("fail"));

// Converting callback to Promise (promisification)
const readFile = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, "utf-8", (err, data) => {
    if (err) reject(err);
    else resolve(data);
  });
});
```

### Асинхронность/ожидание
```javascript
// Basic async function
async function fetchUserData(userId) {
  const user = await getUser(userId);
  const posts = await getPosts(user.id);
  return { user, posts };
}

// Parallel execution
async function loadDashboard(userId) {
  const [user, posts, notifications] = await Promise.all([
    fetchUser(userId),
    fetchPosts(userId),
    fetchNotifications(userId),
  ]);
  return { user, posts, notifications };
}

// Error handling
async function safeFetch(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error(`Fetch failed: ${error.message}`);
    return null;
  }
}

// Async iteration
async function* paginatedFetch(url) {
  let nextUrl = url;
  while (nextUrl) {
    const response = await fetch(nextUrl);
    const data = await response.json();
    yield data.results;
    nextUrl = data.next;
  }
}

// Top-level await (ESM modules)
const config = await import("./config.json", { with: { type: "json" } });
```

---

## Расширенные функции
### Прокси и отражение
```javascript
// Proxy — intercept operations on an object
const handler = {
  get(target, prop, receiver) {
    if (!(prop in target)) {
      throw new ReferenceError(`Property '${prop}' does not exist`);
    }
    return Reflect.get(target, prop, receiver);
  },
  set(target, prop, value, receiver) {
    if (prop === "age" && (typeof value !== "number" || value < 0)) {
      throw new TypeError("Age must be a positive number");
    }
    return Reflect.set(target, prop, value, receiver);
  },
  has(target, prop) {
    return prop.startsWith("_") ? false : Reflect.has(target, prop);
  }
};

const user = new Proxy({ name: "Alice", age: 30, _secret: "hidden" }, handler);
user.age = 31;              // OK
// user.age = "thirty";     // TypeError
// console.log(user.email); // ReferenceError
// "secret" in user;        // false (hidden by 'has' trap)

// Use cases: validation, logging, reactive data, virtual properties
function createValidator(schema) {
  return new Proxy({}, {
    set(target, prop, value) {
      if (schema[prop] && !schema[prop](value)) {
        throw new Error(`Validation failed for '${prop}'`);
      }
      target[prop] = value;
      return true;
    }
  });
}
```

### Символы
```javascript
// Built-in symbols
const obj = {
  [Symbol.iterator]() {       // Make object iterable
    let i = 0;
    const items = this.items || [];
    return {
      next: () => ({
        value: items[i],
        done: i++ >= items.length
      })
    };
  },
  [Symbol.toPrimitive](hint) {  // Custom type coercion
    if (hint === "number") return this.value;
    if (hint === "string") return String(this.value);
    return this.value;
  },
  items: [10, 20, 30],
  value: 42
};

for (const item of obj) console.log(item);  // 10, 20, 30
Number(obj);   // 42
String(obj);   // "42"

// Custom symbols — guaranteed unique identifiers
const ID = Symbol("id");
const user = { [ID]: 12345, name: "Alice" };
console.log(user[ID]);          // 12345
// Symbols are not enumerable in for...in or Object.keys()
```

### WeakRef и реестр финализации
```javascript
// WeakRef — hold a weak reference to an object
const weakRef = new WeakRef(largeObject);
const obj = weakRef.deref();   // Get reference or undefined if GC'd
if (obj) {
  obj.doSomething();
}

// FinalizationRegistry — run cleanup when object is GC'd
const registry = new FinalizationRegistry((key) => {
  console.log(`Object with key ${key} was garbage collected`);
  // Clean up external resources (close file handles, etc.)
});

function createResource(id) {
  const resource = { id, data: new ArrayBuffer(1024 * 1024) };
  registry.register(resource, id, resource);
  return resource;
}
```

---

## Краткое содержание
Синтаксис JavaScript на первый взгляд обманчиво прост, но содержит значительную глубину. Язык превратился из простого инструмента создания сценариев в многопарадигмальный язык с классами, модулями, генераторами, прокси и сложной асинхронной моделью. Понимание приоритета операторов, цикла событий, цепочек прототипов и нюансов привязки`this`отличает компетентных разработчиков от экспертов. Современный JavaScript (ES2020+) с необязательным связыванием, нулевым объединением,`Promise.allSettled`и ожиданием верхнего уровня продолжает сокращать шаблонный код, сохраняя при этом обратную совместимость.