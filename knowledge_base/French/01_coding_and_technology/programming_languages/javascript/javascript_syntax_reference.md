<!--
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

-->
# JavaScript — Référence de syntaxe
Ce document fournit une référence de syntaxe complète et structurée pour JavaScript. Il complète la principale référence JavaScript en se concentrant sur des modèles de syntaxe exhaustifs, des tables d'opérateurs et des mécanismes internes.
---

## Opérateurs et expressions
### Opérateurs arithmétiques
| Opérateur | Nom | Exemple | Résultat | Remarques |
|--------------|------|---------|--------|-------|
| `+`| Ajout | `3 + 2`| `5`| Également la concaténation de chaînes |
| `-`| Soustraction | `3 - 2`| `1`| |
| `*`| Multiplications | `3 * 2`| `6`| |
| `/`| Division | `7 / 2`| `3.5`| |
| `%`| Reste | `7 % 2`| `1`| |
| `**`| Exponentiation | `2 ** 10`| `1024`| ES2016 |
| `++`| Incrément | `x++`/`++x`| | Post- et pré-incrémentation |
| `--`| Décrémentation | `x--`/`--x`| | Post- et pré-décrémentation |
| `+x`,`-x`| Unaire | `+"42"`→`42`| Tapez la coercition au numéro |
### Comparaison et égalité
| Opérateur | Nom | Exemple | Remarques |
|--------------|------|---------|-------|
| `===`| Égalité stricte | `1 === 1`| Aucune coercition de type – préférez toujours ceci |
| `!==`| Inégalités strictes | `1 !== "1"`| `true`— différents types |
| `==`| Égalité abstraite | `1 == "1"`| Tapez la coercition – éviter |
| `!=`| Inégalités abstraites | `1 != "1"`| `false`— éviter |
| `<`,`>`,`<=`,`>=`| Relationnel | `"b" > "a"`| Lexicographique pour cordes |
### Opérateurs logiques et nuls
| Opérateur | Nom | Exemple | Remarques |
|--------------|------|---------|-------|
| `&&`| ET logique | `a && b`| Renvoie la première valeur fausse ou la dernière valeur |
| `\|\|`| OU logique | `a \|\| b`| Renvoie la première ou la dernière valeur vraie |
| `!`| NON logique | `!true`| `false`|
| `??`| Coalescence nulle | `a ?? b`| Renvoie`b`uniquement si`a`est`null`/`undefined`|
| `?.`| Chaînage optionnel | `obj?.prop?.method()`| Courts-circuits vers`undefined`|
### Opérateurs au niveau du bit
| Opérateur | Nom | Exemple | Remarques |
|--------------|------|---------|-------|
| `&`| ET | `5 & 3`| `1`|
| `\|`| OU | `5 \| 3`| `7`|
| `^`| XOR | `5 ^ 3`| `6`|
| `~`| PAS | `~5`| `-6`|
| `<<`| Maj gauche | `5 << 1`| `10`|
| `>>`| Signé Maj droite | `-5 >> 1`| `-3`|
| `>>>`| Maj droite non signé | `-1 >>> 0`| `4294967295`|
### Cession & Déstructuration
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

### Priorité des opérateurs (de la plus élevée à la plus basse)
| Priorité | Opérateurs | Associativité |
|------------|-----------|--------------|
| 1 (le plus élevé) | `()``[]``.``?.` | Gauche |
| 2 | `new`(sans arguments) | Droite |
| 3 | `++``--` (postfix) | N/A |
| 4 | `!``~``+x``-x``typeof``void``delete``++``--`(préfixe) | Droite |
| 5 | `**`| Droite |
| 6 | `*``/``%`| Gauche |
| 7 | `+``-` | Gauche |
| 8 | `<<``>>``>>>`| Gauche |
| 9 | `<``<=``>``>=``in``instanceof` | Gauche |
| 10 | `===``!==``==``!=` | Gauche |
| 11 | `&`| Gauche |
| 12 | `^`| Gauche |
| 13 | `\|`| Gauche |
| 14 | `&&`| Gauche |
| 15 | `\|\|`| Gauche |
| 16 | `??`| Gauche |
| 17 | `=``+=``-=`etc. | Droite |
| 18 (le plus bas) | `=>`(fonction flèche) | Droite |
---

## Flux de contrôle
### Déclarations conditionnelles
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

### Boucles
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

## Fonctions
### Déclarations et expressions de fonctions
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

### Fermetures et fonctions d'ordre supérieur
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

### Générateurs
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

## Structures de données
### Présentation des collections intégrées
| Collecte | Commandé | Mutable | Doublons | Type de clé | Recherche |
|------------|---------|---------|------------|--------------|--------|
| `Array`| Oui | Oui | Oui | Indice (numéro) | O(n) |
| `Object`| Oui (insertion) | Oui | Clés : Non | Chaîne/Symbole | O(1) moyenne |
| `Map`| Oui (insertion) | Oui | Clés : Non | N'importe quel | O(1) moyenne |
| `Set`| Oui (insertion) | Oui | Non | — | O(1) moyenne |
| `WeakMap`| Non | Oui | Clés : Non | Objet uniquement | O(1) moyenne |
| `WeakSet`| Non | Oui | Non | Objet uniquement | O(1) moyenne |
### Tableaux
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

### Objets
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

### Carte et ensemble
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

## Programmation orientée objet
### Classes et héritage
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

### Mixins & Composition
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

## Gestion des erreurs
### Modèles d'exceptions
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

##Modules et forfaits
### Modules ES (ESM)
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

### CommonJS (héritage Node.js)
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

## Modèles asynchrones
### Promesses
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

### Asynchrone/Attendre
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

## Fonctionnalités avancées
### Proxy et réflexion
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

### Symboles
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

### WeakRef et finalisationRegistry
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

## Résumé
La syntaxe de JavaScript est d'une simplicité trompeuse en apparence, mais contient une profondeur significative. Le langage a évolué d'un simple outil de script à un langage multi-paradigme avec des classes, des modules, des générateurs, des proxys et un modèle asynchrone sophistiqué. Comprendre la priorité des opérateurs, la boucle d'événements, les chaînes de prototypes et les nuances de la liaison`this`sépare les développeurs compétents des experts. JavaScript moderne (ES2020+) avec chaînage facultatif, fusion nulle,`Promise.allSettled`et attente de niveau supérieur continue de réduire le passe-partout tout en maintenant la rétrocompatibilité.