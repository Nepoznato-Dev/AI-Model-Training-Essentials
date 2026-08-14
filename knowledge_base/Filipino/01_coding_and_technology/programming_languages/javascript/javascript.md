---
# Metadata
title: "JavaScript"
description: "Comprehensive reference for the JavaScript programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [javascript, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "44 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# JavaScript
Ang JavaScript ay isang pabago-bago, binibigyang kahulugan na programming language na nilikha ni Brendan Eich sa loob lamang ng 10 araw noong 1995. Orihinal na idinisenyo upang magdagdag ng interaktibidad sa mga web page, ito ay lumago sa pinakamalawak na ginagamit na programming language sa mundo. Gumagana ang JavaScript sa bawat web browser, sa mga server sa pamamagitan ng Node.js, sa mga desktop app (Electron), mga mobile app (React Native), at maging sa mga naka-embed na system.
Ang wika ay natatangi dahil ito ay mahalagang ang tanging opsyon para sa client-side web development — bawat browser ay sumusuporta dito sa katutubong. Ang monopolyong ito, na sinamahan ng pagtaas ng full-stack na JavaScript (Node.js, Deno, Bun), ay ginagawa itong kailangang-kailangan.
---

## Bakit Mahalaga ang JavaScript
- **Ang wika ng web**: Ang tanging wika na katutubong tumatakbo sa mga browser. Walang alternatibo para sa frontend.
- **Kakayahang full-stack**: Parehong wika sa frontend (React, Vue, Svelte) at backend (Node.js, Express, Fastify).
- **Massive ecosystem**: Ang npm ay mayroong mahigit 2 milyong package — ang pinakamalaking software registry sa mundo.
- **Versatility**: Mga web app, mobile app (React Native), desktop app (Electron), IoT, mga walang server na function.
- **Mababang hadlang sa pagpasok**: Tumatakbo sa anumang browser — walang kinakailangang pag-install upang simulan ang coding.
- **Asynchronous ayon sa disenyo**: Ang I/O na hinimok ng kaganapan, hindi nakaharang ay ginagawa itong mahusay para sa mga real-time na application.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Mga dynamic na typing pitfalls** | Walang pagsusuri sa uri ng oras ng pag-compile; lumalabas ang mga bug sa runtime | Gumamit ng TypeScript (isang naka-type na superset ng JavaScript) |
| **Pagiging kumplikado ng callback** | Ang mga nested callback ay maaaring maging hindi nababasa ("callback hell") | Gumamit ng Mga Pangako at mag-async/maghintay |
| **Mga kakaibang semantika** | `==`kumpara sa`===`,`this`na nagbubuklod, pagtaas, uri ng pamimilit | Alamin ang mga quirks; gumamit ng ESLint; mas gusto ang`const`/`let`kaysa`var`|
| **Single-threaded** | Hinaharangan ng mga gawaing nakatali sa CPU ang loop ng kaganapan | Gumamit ng Mga Manggagawa sa Web, mga thread ng manggagawa, o nag-offload sa mga native na module |
| **Kalidad ng package** | Ang pagiging bukas ng npm ay nangangahulugan ng hindi pantay na kalidad at mga panganib sa seguridad | Mga dependency sa pag-audit; gumamit ng mga lock file; mas gusto ang well-maintained packages |
---

## Syntax Fundamentals
### Mga Variable at Uri
```javascript
// Modern variable declarations
const name = "Alice";       // Cannot be reassigned
let age = 30;               // Can be reassigned
// var active = true;       // Legacy — avoid in modern code (function-scoped, hoisted)

// JavaScript has 7 primitive types and 1 structural type
typeof "hello"     // "string"
typeof 42          // "number"
typeof 3.14        // "number" (no separate integer type)
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object" (historical bug, kept for compatibility)
typeof Symbol()    // "symbol"
typeof 42n         // "bigint"
typeof {}          // "object"
```

### Mga Pag-andar
```javascript
// Function declaration (hoisted)
function add(a, b) {
    return a + b;
}

// Arrow function (modern, concise)
const multiply = (a, b) => a * b;

// Default parameters
function greet(name = "World", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}

// Higher-order functions
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);          // [2, 4, 6, 8, 10]
const evens = numbers.filter(n => n % 2 === 0);   // [2, 4]
const total = numbers.reduce((sum, n) => sum + n, 0); // 15
```

### Mga Bagay at Klase
```javascript
// Object literal
const user = {
    name: "Alice",
    age: 30,
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};

// Destructuring
const { name, age } = user;

// Class (ES6+)
class Animal {
    #name;  // Private field (# prefix)
    
    constructor(name) {
        this.#name = name;
    }
    
    speak() {
        return `${this.#name} makes a sound`;
    }
    
    get name() {
        return this.#name;
    }
}

class Dog extends Animal {
    speak() {
        return `${this.name} says woof`;
    }
}

const dog = new Dog("Rex");
console.log(dog.speak());  // "Rex says woof"
```

### Async Programming
```javascript
// Promises
function fetchUser(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id > 0) resolve({ id, name: "Alice" });
            else reject(new Error("Invalid ID"));
        }, 1000);
    });
}

// Async/await (modern approach)
async function getUser(id) {
    try {
        const user = await fetchUser(id);
        console.log(user);
        return user;
    } catch (error) {
        console.error("Failed:", error.message);
    }
}

// Parallel execution
async function fetchAll() {
    const [users, posts] = await Promise.all([
        fetch("/api/users").then(r => r.json()),
        fetch("/api/posts").then(r => r.json()),
    ]);
    return { users, posts };
}
```

### Mga Module
```javascript
// ES Modules (modern standard)
// math.js
export function add(a, b) { return a + b; }
export const PI = 3.14159;
export default class Calculator { /* ... */ }

// app.js
import Calculator, { add, PI } from './math.js';

// CommonJS (Node.js legacy — still widely used)
// math.js
module.exports = { add: (a, b) => a + b, PI: 3.14159 };

// app.js
const { add, PI } = require('./math');
```

---

## Advanced na Syntax at Mga Pattern
### Pagsira at Pagkalat/Pahinga (Deep Dive)
```javascript
// Nested destructuring
const response = {
    data: {
        user: { name: "Alice", address: { city: "London" } },
        posts: [{ id: 1, title: "Hello" }],
    },
    status: 200,
};

const { data: { user: { name, address: { city } }, posts: [firstPost] }, status } = response;
console.log(name, city, firstPost.title);  // "Alice" "London" "Hello"

// Spread operator — clone and merge
const defaults = { theme: "light", lang: "en", fontSize: 14 };
const userPrefs = { theme: "dark", fontSize: 16 };
const config = { ...defaults, ...userPrefs };  // { theme: "dark", lang: "en", fontSize: 16 }

// Rest in function parameters
function logEvent(level, ...messages) {
    console[level](`[${level.toUpperCase()}]`, ...messages);
}

// Computed property names
const key = "color";
const obj = { [key]: "blue", [`_${key}Dark`]: "navy" };
// { color: "blue", _colorDark: "navy" }
```

### Proxies at Reflect
```javascript
// Proxy — intercept operations on objects
const handler = {
    get(target, prop) {
        if (!(prop in target)) {
            throw new ReferenceError(`Property "${prop}" does not exist`);
        }
        return Reflect.get(target, prop);
    },
    set(target, prop, value) {
        if (prop === "age" && (typeof value !== "number" || value < 0)) {
            throw new TypeError("Age must be a positive number");
        }
        return Reflect.set(target, prop, value);
    },
};

const user = new Proxy({ name: "Alice", age: 30 }, handler);
user.age = 31;           // OK
// user.age = -5;         // TypeError: Age must be a positive number
// console.log(user.email); // ReferenceError: Property "email" does not exist

// Practical use: reactive state (simplified Vue-like reactivity)
function reactive(obj, onChange) {
    return new Proxy(obj, {
        set(target, prop, value) {
            target[prop] = value;
            onChange(prop, value);
            return true;
        },
    });
}

const state = reactive({ count: 0 }, (key, val) => {
    console.log(`State changed: ${key} = ${val}`);
});
state.count = 1;  // logs: "State changed: count = 1"
```

### Mga Simbolo, Iterator, at Generator
```javascript
// Symbol — unique, immutable primitive (used for hidden object properties)
const ID = Symbol("id");
const user = { [ID]: 12345, name: "Alice" };
console.log(Object.keys(user));  // ["name"] — Symbol keys are hidden
console.log(user[ID]);           // 12345

// Custom iterator
class Range {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }
    [Symbol.iterator]() {
        let current = this.start;
        return {
            next: () => {
                return current <= this.end
                    ? { value: current++, done: false }
                    : { done: true };
            },
        };
    }
}

for (const num of new Range(1, 5)) {
    console.log(num);  // 1, 2, 3, 4, 5
}

// Generator functions — produce iterable sequences
function* fibonacci() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

const fib = fibonacci();
console.log(fib.next().value);  // 0
console.log(fib.next().value);  // 1
console.log(fib.next().value);  // 1
console.log(fib.next().value);  // 2

// Async generator
async function* fetchPages(baseUrl) {
    let page = 1;
    while (true) {
        const response = await fetch(`${baseUrl}?page=${page}`);
        const data = await response.json();
        if (data.length === 0) return;
        yield data;
        page++;
    }
}
```

### Mga Custom na Hierarchy ng Error
```javascript
class AppError extends Error {
    constructor(message, code) {
        super(message);
        this.name = this.constructor.name;
        this.code = code;
        Error.captureStackTrace(this, this.constructor);
    }
}

class ValidationError extends AppError {
    constructor(field, message) {
        super(`Validation failed for '${field}': ${message}`, "VALIDATION");
        this.field = field;
    }
}

class NotFoundError extends AppError {
    constructor(resource, id) {
        super(`${resource} not found: ${id}`, "NOT_FOUND");
        this.resource = resource;
        this.resourceId = id;
    }
}

class AuthenticationError extends AppError {
    constructor(message = "Authentication required") {
        super(message, "AUTH");
    }
}

// Usage
function findUser(id) {
    if (!id) throw new ValidationError("id", "cannot be empty");
    throw new NotFoundError("User", id);
}

try {
    findUser("");
} catch (e) {
    if (e instanceof ValidationError) {
        console.log(`Bad input: ${e.field}`);
    } else if (e instanceof NotFoundError) {
        console.log(`Missing: ${e.resource} #${e.resourceId}`);
    }
}
```

---

## Concurrency at Paralelismo
Ang JavaScript ay single-threaded na may loop ng kaganapan. Nakakamit ang concurrency sa pamamagitan ng mga asynchronous na pattern, Web Workers, at (sa Node.js) ang worker_threads module.
### Ang Loop ng Kaganapan
```javascript
// Understanding execution order
console.log("1: sync");

setTimeout(() => console.log("2: macrotask (setTimeout)"), 0);

Promise.resolve().then(() => console.log("3: microtask (Promise)"));

queueMicrotask(() => console.log("4: microtask (queueMicrotask)"));

console.log("5: sync");

// Output order: 1, 5, 3, 4, 2
// Sync code runs first, then microtasks, then macrotasks
```

### Worker Threads (Node.js — CPU-bound na mga gawain)
```javascript
// worker.js — runs in a separate thread
const { parentPort, workerData } = require("worker_threads");

function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

const result = workerData.numbers.map(isPrime);
parentPort.postMessage(result);

// main.js — spawns workers
const { Worker } = require("worker_threads");

function runWorker(numbers) {
    return new Promise((resolve, reject) => {
        const worker = new Worker("./worker.js", { workerData: { numbers } });
        worker.on("message", resolve);
        worker.on("error", reject);
    });
}

async function main() {
    const numbers = [1000000007, 1000000009, 1000000021, 999999999989];
    const result = await runWorker(numbers);
    console.log(result);  // [true, true, false, true]
}
```

### Mga Manggagawa sa Web (Browser)
```javascript
// worker.js (runs in background thread)
self.onmessage = function (e) {
    const { data } = e.data;
    // Heavy computation...
    const result = data.map(x => x * x);
    self.postMessage(result);
};

// main.js (browser)
const worker = new Worker("worker.js");
worker.postMessage({ data: [1, 2, 3, 4, 5] });
worker.onmessage = (e) => {
    console.log("Result from worker:", e.data);
};
```

### Mga Pattern ng Async
```javascript
// Rate-limited concurrent requests
async function mapConcurrent(items, maxConcurrency, fn) {
    const results = [];
    const executing = new Set();

    for (const [index, item] of items.entries()) {
        const p = Promise.resolve().then(() => fn(item, index));
        executing.add(p);
        p.then(() => executing.delete(p));

        if (executing.size >= maxConcurrency) {
            await Promise.race(executing);
        }
    }

    return Promise.all(
        items.map((item, i) =>
            results[i] !== undefined ? results[i] : fn(item, i)
        )
    );
}

// Debounce — delay execution until input stops
function debounce(fn, delay) {
    let timer;
    return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
    };
}

// Throttle — limit execution frequency
function throttle(fn, limit) {
    let inThrottle = false;
    return function (...args) {
        if (!inThrottle) {
            fn.apply(this, args);
            inThrottle = true;
            setTimeout(() => (inThrottle = false), limit);
        }
    };
}
```

---

## Project Configuration at Build System
### Istraktura ng Direktoryo ng Proyekto
```
my-js-project/
├── src/
│   ├── index.js
│   ├── modules/
│   │   ├── auth.js
│   │   ├── api.js
│   │   └── utils.js
│   └── middleware/
│       └── logger.js
├── tests/
│   ├── unit/
│   │   └── auth.test.js
│   └── integration/
│       └── api.test.js
├── .github/
│   └── workflows/
│       └── ci.yml
├── package.json
├── .eslintrc.json
├── .prettierrc
├── jest.config.js
├── .env.example
├── README.md
└── .gitignore
```

### Build Configuration — `package.json`
```json
{
  "name": "my-js-project",
  "version": "1.0.0",
  "type": "module",
  "description": "A sample JavaScript project",
  "main": "dist/index.js",
  "scripts": {
    "dev": "node --watch src/index.js",
    "build": "esbuild src/index.js --bundle --outdir=dist --minify",
    "start": "node dist/index.js",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src/ --fix",
    "format": "prettier --write 'src/**/*.js'"
  },
  "dependencies": {
    "express": "^4.18.0",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "eslint": "^8.50.0",
    "prettier": "^3.0.0",
    "jest": "^29.7.0",
    "esbuild": "^0.19.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

### Linting at Formatting Configuration
```json
// .eslintrc.json
{
  "env": { "node": true, "es2023": true, "jest": true },
  "parserOptions": { "ecmaVersion": "latest", "sourceType": "module" },
  "extends": ["eslint:recommended"],
  "rules": {
    "no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
    "no-console": "warn",
    "prefer-const": "error",
    "eqeqeq": ["error", "always"],
    "no-var": "error"
  }
}
```

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 4,
  "trailingComma": "es5",
  "printWidth": 100
}
```

### CI/CD Pipeline — Mga Pagkilos sa GitHub
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Test
        run: npm test -- --coverage

      - name: Build
        run: npm run build
```

---

## Pagsubok
### Pagsubok kasama si Jest
```javascript
// tests/unit/auth.test.js
import { createUser, validateEmail, authenticate } from "../src/modules/auth.js";

describe("validateEmail", () => {
    test("accepts valid email", () => {
        expect(validateEmail("alice@example.com")).toBe(true);
    });

    test("rejects invalid email", () => {
        expect(validateEmail("not-an-email")).toBe(false);
        expect(validateEmail("")).toBe(false);
    });
});

describe("createUser", () => {
    test("creates user with valid data", () => {
        const user = createUser("Alice", "alice@example.com");
        expect(user).toEqual({
            name: "Alice",
            email: "alice@example.com",
            createdAt: expect.any(Date),
        });
    });

    test("throws on empty name", () => {
        expect(() => createUser("", "a@b.com")).toThrow("Name is required");
    });
});

describe("authenticate", () => {
    test("returns token for valid credentials", async () => {
        const result = await authenticate("alice", "password123");
        expect(result).toHaveProperty("token");
        expect(typeof result.token).toBe("string");
    });

    test("throws for invalid credentials", async () => {
        await expect(authenticate("alice", "wrong")).rejects.toThrow("Invalid credentials");
    });
});
```

### Mapanukso at Pagsasama-sama ng Pagsusulit
```javascript
// Mocking external dependencies
jest.mock("../src/modules/api.js");
import { fetchData } from "../src/modules/api.js";
import { processData } from "../src/modules/utils.js";

test("processData uses fetched data", async () => {
    fetchData.mockResolvedValue({ items: [1, 2, 3] });

    const result = await processData();

    expect(fetchData).toHaveBeenCalledTimes(1);
    expect(result).toEqual({ count: 3, items: [1, 2, 3] });
});

// Timer mocking
test("debounce delays execution", () => {
    jest.useFakeTimers();
    const fn = jest.fn();
    const debounced = debounce(fn, 300);

    debounced();
    debounced();
    debounced();

    expect(fn).not.toHaveBeenCalled();
    jest.advanceTimersByTime(300);
    expect(fn).toHaveBeenCalledTimes(1);
    jest.useRealTimers();
});

// Integration test with real HTTP
describe("API integration", () => {
    test("GET /api/users returns user list", async () => {
        const response = await fetch("http://localhost:3000/api/users");
        expect(response.status).toBe(200);
        const data = await response.json();
        expect(Array.isArray(data)).toBe(true);
    });
});
```

---

## Interoperability
### Native Addons na may N-API (Node.js)
```javascript
// Using native C++ addons via node-addon-api
// binding.cc (C++ code)
// #include <napi.h>
//
// Napi::String Hello(const Napi::CallbackInfo& info) {
//     return Napi::String::New(info.Env(), "Hello from C++!");
// }
//
// Napi::Object Init(Napi::Env env, Napi::Object exports) {
//     exports.Set("hello", Napi::Function::New(env, Hello));
//     return exports;
// }
//
// NODE_API_MODULE(addon, Init)

// Usage in JavaScript:
// const addon = require("./build/Release/addon");
// console.log(addon.hello());  // "Hello from C++!"
```

### WebAssembly (Wasm)
```javascript
// Load and run a WebAssembly module
async function runWasm() {
    const wasmBytes = await fetch("module.wasm").then(r => r.arrayBuffer());
    const { instance } = await WebAssembly.instantiate(wasmBytes);

    // Call exported function
    const result = instance.exports.add(3, 5);
    console.log(result);  // 8
}

// Compile WAT (WebAssembly Text) inline
const wasmCode = new Uint8Array([
    0x00, 0x61, 0x73, 0x6d, // magic number
    0x01, 0x00, 0x00, 0x00, // version 1
]);
WebAssembly.instantiate(wasmCode).then(({ instance }) => {
    console.log("Wasm loaded");
});
```

### Tinatawagan ang C Libraries gamit ang ffi-napi
```javascript
import ffi from "ffi-napi";

// Load the C math library
const libm = ffi.Library("libm", {
    ceil: ["double", ["double"]],
    floor: ["double", ["double"]],
    sqrt: ["double", ["double"]],
});

console.log(libm.ceil(3.2));   // 4
console.log(libm.floor(3.8));  // 3
console.log(libm.sqrt(16));    // 4
```

---

## Mga Pattern ng Disenyo
### Pattern ng Module (Encapsulation)
```javascript
// The module pattern — closure-based encapsulation
const UserModule = (() => {
    const users = [];  // Private state

    function addUser(name, email) {
        const user = { id: users.length + 1, name, email };
        users.push(user);
        return user;
    }

    function findUser(id) {
        return users.find(u => u.id === id) || null;
    }

    function getAll() {
        return [...users];  // Return a copy
    }

    return { addUser, findUser, getAll };
})();

UserModule.addUser("Alice", "alice@example.com");
console.log(UserModule.getAll());  // [{ id: 1, name: "Alice", ... }]
// console.log(UserModule.users);  // undefined — private
```

### Pattern ng Tagamasid / Emitter ng Kaganapan
```javascript
class EventEmitter {
    #listeners = new Map();

    on(event, callback) {
        if (!this.#listeners.has(event)) {
            this.#listeners.set(event, []);
        }
        this.#listeners.get(event).push(callback);
        return this;  // Enable chaining
    }

    off(event, callback) {
        const listeners = this.#listeners.get(event);
        if (listeners) {
            this.#listeners.set(event, listeners.filter(cb => cb !== callback));
        }
        return this;
    }

    emit(event, ...args) {
        const listeners = this.#listeners.get(event);
        if (listeners) {
            listeners.forEach(cb => cb(...args));
        }
        return this;
    }
}

// Usage
const bus = new EventEmitter();
bus.on("user.login", (user) => console.log(`Welcome, ${user.name}!`));
bus.on("user.login", (user) => console.log(`Logging in ${user.name}...`));
bus.emit("user.login", { name: "Alice" });
```

### Pattern ng Tagabuo
```javascript
class QueryBuilder {
    #table = "";
    #conditions = [];
    #orderFields = [];
    #limitValue = null;

    from(table) {
        this.#table = table;
        return this;
    }

    where(condition) {
        this.#conditions.push(condition);
        return this;
    }

    orderBy(field, direction = "ASC") {
        this.#orderFields.push(`${field} ${direction}`);
        return this;
    }

    limit(n) {
        this.#limitValue = n;
        return this;
    }

    build() {
        let sql = `SELECT * FROM ${this.#table}`;
        if (this.#conditions.length > 0) {
            sql += ` WHERE ${this.#conditions.join(" AND ")}`;
        }
        if (this.#orderFields.length > 0) {
            sql += ` ORDER BY ${this.#orderFields.join(", ")}`;
        }
        if (this.#limitValue !== null) {
            sql += ` LIMIT ${this.#limitValue}`;
        }
        return sql;
    }
}

const query = new QueryBuilder()
    .from("users")
    .where("age > 18")
    .where("active = true")
    .orderBy("name")
    .limit(10)
    .build();

console.log(query);
// SELECT * FROM users WHERE age > 18 AND active = true ORDER BY name ASC LIMIT 10
```

---

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
```bash
# Node.js built-in profiler
node --prof app.js
node --prof-process isolate-*.log > profile.txt

# Chrome DevTools — inspect Node.js processes
node --inspect app.js
# Then open chrome://inspect in Chrome

# Benchmark with benchmark.js
npm install benchmark
```

### Mga Teknik sa Pag-optimize
```javascript
// 1. Use Map/Set instead of objects/arrays for lookups
// BAD — O(n) lookup in array
const validNames = ["alice", "bob", "charlie"];
if (validNames.includes(name)) { }

// GOOD — O(1) lookup in Set
const validNamesSet = new Set(["alice", "bob", "charlie"]);
if (validNamesSet.has(name)) { }

// 2. Object pooling for frequently created objects
const bufferPool = {
    _pool: [],
    acquire(size) {
        return this._pool.pop() || Buffer.alloc(size);
    },
    release(buffer) {
        buffer.fill(0);
        this._pool.push(buffer);
    },
};

// 3. Avoid memory leaks — clear intervals and event listeners
const intervalId = setInterval(() => { /* ... */ }, 1000);
// Don't forget to clear:
clearInterval(intervalId);

// 4. Use streams for large data processing
import { createReadStream } from "fs";
import { createInterface } from "readline";

const stream = createReadStream("large-file.csv");
const rl = createInterface({ input: stream });

for await (const line of rl) {
    processLine(line);  // Process one line at a time
}
```

---

## Deployment
### Dockerfile
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Deployment na Partikular sa Platform
```bash
# Vercel (frontend / serverless)
npm i -g vercel
vercel --prod

# AWS Lambda (serverless)
# Use the Serverless Framework or AWS SAM
npx serverless deploy

# Docker deployment
docker build -t my-app .
docker run -p 3000:3000 my-app

# PM2 (process manager for Node.js)
npm install -g pm2
pm2 start dist/index.js --name "my-app" -i max  # Cluster mode
pm2 save
pm2 startup
```

---

## Ang Ecosystem
### Frontend Frameworks
| Balangkas | Diskarte | Pinakamahusay Para sa |
|-----------|----------|----------|
| **React** | Nakabatay sa bahagi, virtual na DOM | Mga malalaking SPA; pinakamalaking ecosystem |
| **Vue** | Progressive, batay sa template | Unti-unting pag-aampon; mahusay na karanasan sa developer |
| **Svelte** | Oras ng pag-compile, walang virtual na DOM | Mas maliliit na bundle, mas simpleng code |
| **Angular** | Buong balangkas, TypeScript-una | Enterprise apps; istraktura ng opinyon |
| **Next.js** | React meta-framework (SSR/SSG) | Production React apps na may SEO |
### Backend (Node.js)
| Balangkas | Layunin |
|-----------|---------|
| **Express** | Minimal, nababaluktot na web framework (pinakatanyag) |
| **Mag-fastify** | Mataas na pagganap ng web framework |
| **NestJS** | Enterprise-grade, Angular-inspired na arkitektura |
| **Koa** | Magaan, modernong Express alternatibo |
| **Hono** | Napakabilis, multi-runtime (Node, Deno, Bun, edge) |
### Mga Runtime
| Runtime | Paglalarawan |
|---------|-------------|
| **Node.js** | Ang orihinal na server-side JavaScript runtime (V8 engine) |
| **Deno** | Secure bilang default; katutubong TypeScript na suporta; nilikha ng orihinal na may-akda ng Node |
| **Bun** | Napakabilis na all-in-one na runtime, bundler, at manager ng package |
### Mahahalagang Tool
| Tool | Layunin |
|------|---------|
| **npm / sinulid / pnpm** | Mga manager ng package |
| **TypeScript** | Nag-type ng superset ng JavaScript |
| **ESLint** | Code linting |
| **Mas maganda** | Pag-format ng code |
| **Vite** | Mabilis na build tool at dev server |
| **Webpack** | Module bundler (mature, malawakang ginagamit) |
| **Jest / Vitest** | Mga balangkas ng pagsubok |
---

## Kailan Gamitin ang JavaScript
| Sitwasyon | Bakit JavaScript | Mas mahusay na Alternatibo |
|----------|----------------|-------------------|
| Web frontend | Tanging opsyon para sa browser-based na UI | — |
| Full-stack na web | Parehong wika sa lahat ng dako | TypeScript para sa kaligtasan ng uri |
| Mga real-time na app (chat, laro) | I/O na hinimok ng kaganapan, hindi humaharang | — |
| Mga function na walang server | Mabilis na magsulat, i-deploy kahit saan | Python, Pumunta |
| Mga mobile app (React Native) | Ibahagi ang code sa web | Flutter, katutubong Swift/Kotlin |
| Mga desktop app (Electron) | Cross-platform na may web tech | C# (WPF), Tauri (Rust) |
| CPU-intensive computation | Single-threaded na limitasyon | Python (NumPy), C++, Rust, WebAssembly |
| System programming | Maling abstraction level | C, C++, Rust, Go |
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba sa pagitan ng`var`,`let`, at`const`, at kailan ko dapat gamitin ang bawat isa?
**A:** Ang`var`ay nasasakupan ng pag-andar at nakataas — iwasan ito sa modernong code.  Ang`let`ay block-scoped at nagbibigay-daan sa muling pagtatalaga.  Ang`const`ay block-scoped at pinipigilan ang muling pagtatalaga (ngunit ang mga object/arrays na tinutukoy nito ay nababago pa rin). Pinakamahusay na kasanayan: default sa`const`, gamitin lang ang`let`kapag kailangan mo ng muling pagtatalaga, huwag gumamit ng`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2: Paano gumagana ang`this`sa JavaScript, at bakit ito nakakalito?
**A:** Ang`this`ay tinutukoy ng **kung paano tinatawag ang isang function**, hindi kung saan ito tinukoy. Sa isang method call,`this`ang object. Sa isang standalone na tawag, ito ay`undefined`(strict mode) o`global`(non-strict). Ang mga function ng arrow ay namamana ng`this`mula sa kanilang kalakip na saklaw — ito ang dahilan kung bakit mas gusto ang mga ito para sa mga callback. Gamitin ang`.bind()`para tahasang itakda ang`this`.
```javascript
// Arrow function inherits 'this' from class scope
class Timer {
  constructor() { this.seconds = 0; }
  start() {
    // WRONG: regular function — 'this' is undefined
    // setInterval(function() { this.seconds++; }, 1000);

    // RIGHT: arrow function — 'this' is the Timer instance
    setInterval(() => { this.seconds++; }, 1000);
  }
}
```

### Q3: Ano ang event loop, at paano gumagana ang async/wait?
**A:** Ang JavaScript ay single-threaded na may loop ng kaganapan na nagpoproseso ng queue. Ang call stack ay nagpapatupad ng synchronous code. Kapag ito ay walang laman, pipiliin ng event loop ang susunod na gawain mula sa microtask queue (Promises) o macrotask queue (setTimeout, I/O).  Ang`async/await`ay syntactic sugar sa mga Pangako — Ipo-pause ng`await`ang async function at magpapatuloy kapag nalutas ang Pangako, nang hindi hinaharangan ang thread.
```javascript
// Execution order demonstrates the event loop
console.log("1: sync");                    // Runs first (synchronous)

setTimeout(() => console.log("2: macrotask"), 0);  // Runs fourth

Promise.resolve().then(() => {
  console.log("3: microtask");             // Runs second
}).then(() => {
  console.log("4: microtask chain");       // Runs third
});

console.log("5: sync");                    // Runs first (after "1")

// Output: 1, 5, 3, 4, 2
```

### Q4: Paano ko dapat pangasiwaan ang mga error sa modernong JavaScript?
**A:** Gamitin ang`try/catch`para sa kasabay na code at`.catch()`o`try/catch`na may`async/await`para sa asynchronous na code. Palaging pangasiwaan ang mga pagtanggi sa Pangako — ang mga hindi nahawakang pagtanggi ay bumagsak sa Node.js. Gumawa ng mga custom na klase ng error para sa mga error na partikular sa domain. Gumamit ng pandaigdigang tagapangasiwa ng error bilang isang safety net.
```javascript
// Custom error class
class ApiError extends Error {
  constructor(message, statusCode, endpoint) {
    super(message);
    this.name = "ApiError";
    this.statusCode = statusCode;
    this.endpoint = endpoint;
  }
}

// Async error handling
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new ApiError(
        `Failed to fetch user ${id}`,
        response.status,
        `/api/users/${id}`
      );
    }
    return await response.json();
  } catch (error) {
    if (error instanceof ApiError) throw error;  // Re-throw known errors
    throw new Error(`Network error: ${error.message}`);  // Wrap unknown
  }
}

// Global safety net (Node.js)
process.on("unhandledRejection", (reason, promise) => {
  console.error("Unhandled rejection:", reason);
});
```

### Q5: Kailan ko dapat gamitin ang`Map`/`Set`sa halip na mga simpleng bagay/array?
**A:** Gamitin ang`Map`kapag ang mga key ay hindi mga string, kapag kailangan mo ng insertion-order iteration, kapag kailangan mo ng`.size`, o kapag madalas kang magdagdag/mag-alis ng mga entry (mas mahusay na performance kaysa sa mga object). Gamitin ang`Set`para sa mga natatanging koleksyon na may O(1) lookup — mas mabilis kaysa`array.includes()`para sa malalaking dataset. Gumamit ng mga plain object para sa simpleng JSON-serializable na data at maliliit na key-value na mga mapa na may mga string key.
```javascript
// Map — non-string keys, ordered, fast mutations
const userRoles = new Map();
const admin = { id: 1, name: "Alice" };
userRoles.set(admin, "admin");      // Object as key!
userRoles.set({ id: 2 }, "editor");
console.log(userRoles.size);         // 2
console.log(userRoles.get(admin));   // "admin"

// Set — fast membership testing
const allowedIds = new Set([101, 205, 310, 422]);
// O(1) lookup vs O(n) for Array.includes()
if (allowedIds.has(requestId)) {
  processRequest(requestId);
}
```

---

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Magpatupad ng Debounce Function
**Pahayag ng Problema:** Magpatupad ng`debounce`na utility na nagde-delay sa pag-invoke ng isang function hanggang matapos ang isang tinukoy na panahon ng paghihintay mula noong huling beses itong tinawag. Suportahan ang parehong leading at trailing edge invocation.
**Hakbang 1 — Unawain ang Problema:**
Binabalewala ng isang na-debounce na function ang mabilis na sunud-sunod na mga tawag at magpapagana lamang pagkatapos huminto ang mga tawag sa tagal ng paghihintay. Ang ibig sabihin ng "nangungunang gilid" ay sunog kaagad sa unang tawag. Ang ibig sabihin ng "trailing edge" ay sunog pagkatapos ng panahon ng paghihintay. Kailangan nating pangasiwaan ang parehong mga mode at suportahan din ang pagkansela.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Mag-imbak ng timer ID sa isang pagsasara.
- Sa bawat tawag: i-clear ang kasalukuyang timer, pagkatapos ay magtakda ng bagong`setTimeout`.
- Para sa nangungunang gilid: tumawag kaagad kung walang timer na aktibo.
- Ibalik ang isang na-debounce na function na may`.cancel()`na paraan.
- Panatilihin ang`this`na konteksto at mga argumento gamit ang mga arrow function o`.apply()`.
**Hakbang 3 — Ipatupad ang Solusyon:**
```javascript
function debounce(fn, wait, { leading = false } = {}) {
  let timeoutId = null;
  let lastArgs = null;
  let lastThis = null;

  function debounced(...args) {
    lastArgs = args;
    lastThis = this;

    if (leading && timeoutId === null) {
      fn.apply(lastThis, lastArgs);  // Fire immediately on leading edge
    }

    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      if (!leading) {
        fn.apply(lastThis, lastArgs);  // Fire after wait on trailing edge
      }
      timeoutId = null;
      lastArgs = null;
      lastThis = null;
    }, wait);
  }

  debounced.cancel = () => {
    clearTimeout(timeoutId);
    timeoutId = null;
    lastArgs = null;
    lastThis = null;
  };

  return debounced;
}

// Usage — search input that fires API call 300ms after typing stops
const searchInput = document.querySelector("#search");
const handleSearch = debounce((query) => {
  fetch(`/api/search?q=${encodeURIComponent(query)}`)
    .then(res => res.json())
    .then(results => renderResults(results));
}, 300);

searchInput.addEventListener("input", (e) => {
  handleSearch(e.target.value);
});
```

**Hakbang 4 — I-verify at I-optimize:**
- Ang pagsasara ay nagpapanatili ng estado sa lahat ng mga tawag nang hindi nagpaparumi sa pandaigdigang saklaw.
- Tinitiyak ng`clearTimeout`bago ang`setTimeout`na ang huling tawag lang ang magti-trigger ng pagpapatupad.
- Mahalaga ang`.cancel()`para sa paglilinis (hal., i-unmount ang component sa React).
- Edge case: kung ang`wait`ay 0, gagana ang function sa susunod na event loop tick — kapaki-pakinabang para sa pag-batch ng mga update sa DOM.
### Problema 2: Bumuo ng Limiter ng Rate na Nakabatay sa Pangako
**Pahayag ng Problema:** Lumikha ng isang limiter ng rate na nagbibigay-daan sa hindi hihigit sa N kahilingan sa bawat palugit ng oras. Dapat nitong ibalik ang Mga Pangakong naresolba kapag pinahintulutan ang tumatawag na magpatuloy, at mag-queue ng mga labis na kahilingan.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng sliding o fixed window na sumusubaybay kung gaano karaming mga tawag ang ginawa. Kapag naabot na ang limitasyon, ang mga bagong tawag ay dapat na nakapila at lutasin kapag may nagbubukas na puwang. Ito ang pattern na "token bucket".
**Hakbang 2 — Tukuyin ang Diskarte:**
- Subaybayan ang mga timestamp ng mga kamakailang tawag sa isang array.
- Sa bawat tawag: alisin ang mga timestamp na mas luma sa window, tingnan kung count < limit.
- Kung nasa ilalim ng limitasyon: lutasin kaagad.
- Kung nasa limitasyon: kalkulahin kung kailan mag-e-expire ang pinakalumang timestamp, magtakda ng`setTimeout`, pagkatapos ay lutasin.
- Gumamit ng pila (array ng mga function ng paglutas) para sa mga naghihintay na tumatawag.
**Hakbang 3 — Ipatupad ang Solusyon:**
```javascript
class RateLimiter {
  constructor(maxCalls, windowMs) {
    this.maxCalls = maxCalls;
    this.windowMs = windowMs;
    this.timestamps = [];
    this.queue = [];
  }

  async acquire() {
    this._cleanOldTimestamps();

    if (this.timestamps.length < this.maxCalls) {
      this.timestamps.push(Date.now());
      return;
    }

    // Calculate wait time until the oldest call exits the window
    const waitTime = this.timestamps[0] + this.windowMs - Date.now();

    return new Promise((resolve) => {
      this.queue.push(resolve);
      setTimeout(() => {
        this._cleanOldTimestamps();
        this.timestamps.push(Date.now());
        const nextResolve = this.queue.shift();
        if (nextResolve) nextResolve();
      }, Math.max(waitTime, 0));
    });
  }

  _cleanOldTimestamps() {
    const cutoff = Date.now() - this.windowMs;
    this.timestamps = this.timestamps.filter(t => t > cutoff);
  }
}

// Usage — limit API calls to 5 per second
const limiter = new RateLimiter(5, 1000);

async function callApi(url) {
  await limiter.acquire();
  const response = await fetch(url);
  return response.json();
}

// All 20 calls will be spread across ~4 seconds (5 per second)
const urls = Array.from({ length: 20 }, (_, i) => `/api/item/${i}`);
Promise.all(urls.map(callApi)).then(results => {
  console.log(`Fetched ${results.length} items`);
});
```

**Hakbang 4 — I-verify at I-optimize:**
- Ang diskarte sa sliding window ay mas patas kaysa sa mga nakapirming bintana (walang pagsabog sa mga hangganan ng bintana).
- Ang pagpoproseso ng pila ay FIFO — ang mga tumatawag ay inihahatid sa pagkakasunud-sunod.
- Para sa produksyon: magdagdag ng suporta sa`AbortController`upang makansela ng mga tumatawag ang paghihintay.
- Pagganap: Ang`_cleanOldTimestamps`ay O(n) bawat tawag ngunit ang n ay nililimitahan ng`maxCalls`.
### Problema 3: Magpatupad ng Deep Clone Function
**Pahayag ng Problema:** Sumulat ng isang function na malalim na nagko-clone ng anumang halaga ng JavaScript, pangangasiwa ng mga object, array, Petsa, RegExps, Maps, Sets, circular reference, at typed array.
**Hakbang 1 — Unawain ang Problema:**
 Nabigo ang`JSON.parse(JSON.stringify(obj))`sa:`undefined`, mga function, Mga Simbolo, Mga Petsa (naging mga string), RegExps (naging mga walang laman na bagay), Mga Mapa, Mga Set, mga pabilog na sanggunian (mga throw), at mga na-type na array. Kailangan namin ng recursive na solusyon na sumusubaybay sa mga binisita na bagay.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng`Map`upang subaybayan ang mga na-clone na bagay (pangasiwaan ang mga pabilog na sanggunian).
- Pangasiwaan ang bawat uri lalo na: Petsa → bagong Petsa, RegExp → bagong RegExp, Map → bagong Map na may mga naka-clone na entry, Itakda → bagong Set na may mga naka-clone na halaga.
- Gamitin ang`structuredClone()`bilang modernong built-in na alternatibo (available sa mga browser at Node.js 17+).
**Hakbang 3 — Ipatupad ang Solusyon:**
```javascript
function deepClone(value, seen = new Map()) {
  // Primitives and null — returned as-is
  if (value === null || typeof value !== "object") {
    return value;
  }

  // Circular reference check
  if (seen.has(value)) {
    return seen.get(value);
  }

  // Date
  if (value instanceof Date) {
    return new Date(value.getTime());
  }

  // RegExp
  if (value instanceof RegExp) {
    return new RegExp(value.source, value.flags);
  }

  // Typed Arrays (Uint8Array, Float32Array, etc.)
  if (ArrayBuffer.isView(value)) {
    return new value.constructor(value);
  }

  // Map
  if (value instanceof Map) {
    const clone = new Map();
    seen.set(value, clone);
    for (const [k, v] of value) {
      clone.set(deepClone(k, seen), deepClone(v, seen));
    }
    return clone;
  }

  // Set
  if (value instanceof Set) {
    const clone = new Set();
    seen.set(value, clone);
    for (const v of value) {
      clone.add(deepClone(v, seen));
    }
    return clone;
  }

  // Array
  if (Array.isArray(value)) {
    const clone = [];
    seen.set(value, clone);
    for (const item of value) {
      clone.push(deepClone(item, seen));
    }
    return clone;
  }

  // Plain Object
  const clone = Object.create(Object.getPrototypeOf(value));
  seen.set(value, clone);
  for (const key of Reflect.ownKeys(value)) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if ("value" in descriptor) {
      clone[key] = deepClone(value[key], seen);
    } else {
      Object.defineProperty(clone, key, descriptor);
    }
  }
  return clone;
}

// Usage
const original = { a: 1, b: { c: [2, 3] }, d: new Date(), e: new Map([["k", "v"]]) };
original.self = original;  // Circular reference

const cloned = deepClone(original);
console.log(cloned.self === cloned);  // true — circular ref preserved
console.log(cloned.b !== original.b); // true — deep clone, not reference
```

**Hakbang 4 — I-verify at I-optimize:**
- Mga pabilog na sanggunian: ibinabalik ng`seen`Map ang nagawa nang clone sa halip na umulit nang walang hanggan.
- Mga deskriptor ng property: Ang`Reflect.ownKeys`+`getOwnPropertyDescriptor`ay nagpapanatili ng mga getter, setter, at hindi mabilang na mga katangian.
- Modernong alternatibo: Ang`structuredClone(value)`ay pinangangasiwaan ang karamihan sa mga kasong ito nang katutubong (maliban sa mga function at DOM node). Mas gusto ito kapag available.
- Pagganap: para sa mga simpleng bagay, ang`JSON.parse(JSON.stringify(obj))`ay pinakamabilis pa rin. Gumamit lamang ng malalim na clone kapag talagang kailangan mo ito.
### Problema 4: Bumuo ng Simpleng Event Emitter
**Problem Statement:** Magpatupad ng event emitter class na sumusuporta sa`on`,`off`,`emit`, at`once`na pamamaraan. Dapat tawagan ang mga tagapakinig sa pagkakasunud-sunod ng pagpaparehistro.  Ang`emit`ay dapat magpasa ng mga argumento sa lahat ng mga tagapakinig.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng isang pub/sub system: magrehistro ng mga tagapakinig para sa mga pinangalanang kaganapan, mag-alis ng mga partikular na tagapakinig, mag-trigger ng mga kaganapan na may mga argumento, at suportahan ang isang beses na tagapakinig. Ito ang pattern ng Observer na malawakang ginagamit sa Node.js.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Mag-imbak ng mga tagapakinig sa isang`Map<string, Array<Function>>`.
-`on`: itulak ang tagapakinig sa array.
-`off`: i-filter ang partikular na tagapakinig mula sa array.
-`emit`: ulitin ang array at tawagan ang bawat tagapakinig na may mga spread na argumento.
-`once`: balutin ang tagapakinig sa isang function na nag-aalis ng sarili pagkatapos ng unang tawag.
**Hakbang 3 — Ipatupad ang Solusyon:**
```javascript
class EventEmitter {
  #listeners = new Map();

  on(event, listener) {
    if (!this.#listeners.has(event)) {
      this.#listeners.set(event, []);
    }
    this.#listeners.get(event).push(listener);
    return this;  // Enable chaining
  }

  off(event, listener) {
    const listeners = this.#listeners.get(event);
    if (!listeners) return this;
    const index = listeners.indexOf(listener);
    if (index !== -1) {
      listeners.splice(index, 1);
    }
    if (listeners.length === 0) {
      this.#listeners.delete(event);
    }
    return this;
  }

  emit(event, ...args) {
    const listeners = this.#listeners.get(event);
    if (!listeners) return false;
    // Copy array to avoid issues if listeners modify the list during iteration
    for (const listener of [...listeners]) {
      listener(...args);
    }
    return true;
  }

  once(event, listener) {
    const wrapper = (...args) => {
      this.off(event, wrapper);
      listener(...args);
    };
    wrapper._original = listener;  // Allow off() with original reference
    return this.on(event, wrapper);
  }

  listenerCount(event) {
    return this.#listeners.get(event)?.length ?? 0;
  }
}

// Usage
const emitter = new EventEmitter();

emitter.on("data", (msg) => console.log(`Received: ${msg}`));
emitter.once("connected", () => console.log("First connection only"));

emitter.emit("connected");           // "First connection only"
emitter.emit("connected");           // (nothing — listener removed)
emitter.emit("data", "hello");       // "Received: hello"
```

**Hakbang 4 — I-verify at I-optimize:**
- Ang`[...listeners]`na kopya sa`emit`ay pumipigil sa mga isyu kapag ang isang tagapakinig ay tumawag sa`off`sa panahon ng pag-ulit.
- Iniimbak ng`once`ang`_original`upang maalis ng mga tumatawag ang wrapper sa pamamagitan ng`off(event, originalFn)`.
- Ang mga pribadong field (`#listeners`) ay pumipigil sa panlabas na mutation ng panloob na estado.
- Para sa produksyon: magdagdag ng`maxListeners`na babala (tulad ng Node.js), paghawak ng error sa bawat tagapakinig, at`prependListener`para sa priyoridad.
---

## Buod
Ang JavaScript ay hindi maiiwasan. Ito ang tanging wika na tumatakbo sa mga web browser, na ginagawa itong mahalaga para sa pag-unlad ng frontend. Sa Node.js, umaabot ito sa gilid ng server, at sa mga frameworks tulad ng React Native at Electron, umaabot ito sa mobile at desktop. Ang ecosystem ang pinakamalaki sa programming. Ang mga quirks ng wika ay kilala at mapapamahalaan — at tinutugunan ng TypeScript ang mga alalahanin sa pag-type. Para sa anumang bagay na tumatakbo sa isang browser, ang JavaScript ay hindi lamang ang pinakamahusay na pagpipilian - ito ang tanging pagpipilian.