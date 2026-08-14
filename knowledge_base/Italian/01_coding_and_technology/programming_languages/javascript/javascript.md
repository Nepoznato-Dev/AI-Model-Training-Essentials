<!--
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

-->
#JavaScript
JavaScript è un linguaggio di programmazione dinamico e interpretato creato da Brendan Eich in soli 10 giorni nel 1995. Originariamente progettato per aggiungere interattività alle pagine web, è diventato il linguaggio di programmazione più utilizzato al mondo. JavaScript viene eseguito in ogni browser Web, sui server tramite Node.js, nelle app desktop (Electron), nelle app mobili (React Native) e persino nei sistemi embedded.
Il linguaggio è unico in quanto è essenzialmente l'unica opzione per lo sviluppo web lato client: ogni browser lo supporta in modo nativo. Questo monopolio, combinato con l’ascesa del JavaScript full-stack (Node.js, Deno, Bun), lo rende indispensabile.
---

## Perché JavaScript è importante
- **Il linguaggio del web**: l'unico linguaggio che viene eseguito in modo nativo nei browser. Nessuna alternativa per il frontend.
- **Funzionalità full-stack**: stesso linguaggio sul frontend (React, Vue, Svelte) e sul backend (Node.js, Express, Fastify).
- **Ecosistema enorme**: npm ha oltre 2 milioni di pacchetti: il più grande registro software del mondo.
- **Versatilità**: app Web, app mobili (React Native), app desktop (Electron), IoT, funzioni serverless.
- **Bassa barriera all'accesso**: funziona con qualsiasi browser: non è necessaria alcuna installazione per iniziare a scrivere codice.
- **Design asincrono**: l'I/O non bloccante e guidato dagli eventi lo rende eccellente per le applicazioni in tempo reale.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Insidie ​​della digitazione dinamica** | Nessun controllo del tipo in fase di compilazione; i bug emergono in fase di esecuzione | Utilizza TypeScript (un superset digitato di JavaScript) |
| **Complessità della richiamata** | Le richiamate nidificate possono diventare illeggibili ("inferno delle richiamate") | Utilizza Promises e async/await |
| **Semantica bizzarra** | `==`vs`===`,`this`vincolo, sollevamento, tipo coercizione | Impara le stranezze; utilizzare ESLint; preferisci`const`/`let`rispetto a`var`|
| **A thread singolo** | Le attività legate alla CPU bloccano il ciclo di eventi | Utilizza Web Worker, thread di lavoro o scarica su moduli nativi |
| **Qualità della confezione** | L'apertura di npm implica qualità incoerente e rischi per la sicurezza | Dipendenze di controllo; utilizzare file di blocco; preferiscono pacchetti ben mantenuti |
---

## Fondamenti di sintassi
### Variabili e tipi
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

### Funzioni
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

### Oggetti e classi
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

### Programmazione asincrona
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

### Moduli
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

## Sintassi e modelli avanzati
### Destrutturazione e diffusione/riposo (immersione profonda)
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

### Proxy e riflessione
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

### Simboli, iteratori e generatori
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

### Gerarchie di errori personalizzate
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

## Concorrenza e parallelismo
JavaScript è a thread singolo con un loop di eventi. La concorrenza viene raggiunta tramite modelli asincroni, Web Worker e (in Node.js) il modulo lavoratore_threads.
### Il ciclo degli eventi
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

### Thread di lavoro (Node.js: attività legate alla CPU)
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

### Lavoratori Web (browser)
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

### Modelli asincroni
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

## Configurazione del progetto e sistema di creazione
### Struttura delle directory del progetto
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

### Configurazione della creazione: `package.json`
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

### Configurazione dell'linting e della formattazione
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

## Test
### Test con Jest
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

### Test simulati e di integrazione
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

## Interoperabilità
### Componenti aggiuntivi nativi con N-API (Node.js)
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

### Chiamare le librerie C con ffi-napi
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

## Modelli di progettazione
### Modello del modulo (incapsulamento)
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

### Modello osservatore/emettitore di eventi
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

### Modello di creazione
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

## Prestazioni e ottimizzazione
### Strumenti di profilazione
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

### Tecniche di ottimizzazione
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

## Distribuzione
###Dockerfile
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

### Distribuzione specifica della piattaforma
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

## L'ecosistema
### Framework frontend
| Quadro | Avvicinamento | Ideale per |
|-----------|----------|----------|
| **Reagire** | DOM virtuale basato su componenti | SPA di grandi dimensioni; il più grande ecosistema |
| **Veduta** | Progressivo, basato su modelli | Adozione graduale; ottima esperienza da sviluppatore |
| **Svelto** | In fase di compilazione, nessun DOM virtuale | Pacchetti più piccoli, codice più semplice |
| **Angolare** | Framework completo, prima TypeScript | App aziendali; struttura supponente |
| **Next.js** | Meta-framework React (SSR/SSG) | App React di produzione con SEO |
### Back-end (Node.js)
| Quadro | Scopo |
|-----------|---------|
| **Espresso** | Framework web minimo e flessibile (il più popolare) |
| **Fastificare** | Framework web ad alte prestazioni |
| **NestJS** | Architettura di livello aziendale, ispirata ad Angular |
| **Koa** | Alternativa Express leggera e moderna |
| **Ono** | Ultraveloce, multi-runtime (Node, Deno, Bun, edge) |
### Tempi di esecuzione
| Durata | Descrizione |
|---------|-----|
| **Node.js** | Il runtime JavaScript lato server originale (motore V8) |
| **Deno** | Sicuro per impostazione predefinita; supporto nativo di TypeScript; creato dall'autore originale di Node |
| **Panino** | Runtime, bundler e gestore pacchetti all-in-one ultraveloci |
### Strumenti essenziali
| Strumento | Scopo |
|------|---------|
| **npm / filato / pnpm** | Gestori di pacchetti |
| **Script dattiloscritto** | Superset digitato di JavaScript |
| **ESLint** | Linting del codice |
| **Più carino** | Formattazione del codice |
| **Vite** | Strumento di creazione rapida e server di sviluppo |
| **Pacchetto web** | Bundler di moduli (maturo, ampiamente utilizzato) |
| **Jest / Vitest** | Strutture di test |
---

## Quando utilizzare JavaScript
| Scenario | Perché JavaScript | Alternativa migliore |
|----------|--------------|-------------|
| Frontend Web | Unica opzione per l'interfaccia utente basata su browser | — |
| Web a stack completo | Stessa lingua ovunque | TypeScript per l'indipendenza dal tipo |
| App in tempo reale (chat, giochi) | I/O guidato dagli eventi e non bloccante | — |
| Funzioni serverless | Veloce da scrivere, distribuito ovunque | Pitone, vai |
| App mobili (React Native) | Condividi il codice con il web | Flutter, nativo di Swift/Kotlin |
| App desktop (Electron) | Multipiattaforma con tecnologia web | C# (WPF), Tauri (Ruggine) |
| Calcolo ad uso intensivo della CPU | Limitazione a thread singolo | Python (NumPy), C++, Rust, WebAssembly |
| Programmazione dei sistemi | Livello di astrazione errato | C, C++, Ruggine, Go |
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra`var`,`let`e`const`e quando dovrei utilizzarli ciascuno?
**R:**`var`ha un ambito di funzione ed è issato: evitalo nel codice moderno. `let`ha ambito a blocchi e consente la riassegnazione. `const`ha un ambito di blocco e impedisce la riassegnazione (ma gli oggetti/matrici a cui fa riferimento sono ancora modificabili). Procedura consigliata: impostazione predefinita su`const`, utilizzare`let`solo quando è necessaria una riassegnazione, non utilizzare mai`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### D2: Come funziona`this`in JavaScript e perché crea così confusione?
**R:**`this`è determinato da **come viene chiamata una funzione**, non da dove è definita. In una chiamata al metodo,`this`è l'oggetto. In una chiamata autonoma, è`undefined`(modalità rigorosa) o`global`(non rigorosa). Le funzioni freccia ereditano`this`dall'ambito che le racchiude: ecco perché sono preferite per i callback. Utilizzare`.bind()`per impostare esplicitamente`this`.
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

### D3: Cos'è il ciclo di eventi e come funziona effettivamente async/await?
**R:** JavaScript è a thread singolo con un loop di eventi che elabora una coda. Lo stack di chiamate esegue codice sincrono. Quando è vuoto, il ciclo degli eventi seleziona l'attività successiva dalla coda dei microtask (Promises) o dalla coda dei macrotask (setTimeout, I/O). `async/await`è zucchero sintattico su Promises:`await`mette in pausa la funzione asincrona e la riprende quando Promise si risolve, senza bloccare il thread.
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

### D4: Come dovrei gestire gli errori nel JavaScript moderno?
**R:** Utilizzare`try/catch`per codice sincrono e`.catch()`o`try/catch`con`async/await`per codice asincrono. Gestisci sempre i rifiuti Promise: i rifiuti non gestiti bloccano Node.js. Crea classi di errore personalizzate per errori specifici del dominio. Utilizzare un gestore errori globale come rete di sicurezza.
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

### D5: Quando dovrei utilizzare`Map`/`Set`invece di semplici oggetti/array?
**R:** Utilizza`Map`quando le chiavi non sono stringhe, quando hai bisogno dell'iterazione dell'ordine di inserimento, quando hai bisogno di`.size`o quando aggiungi/rimuovi frequentemente voci (prestazioni migliori rispetto agli oggetti). Utilizza`Set`per raccolte univoche con ricerca O(1), molto più veloce di`array.includes()`per set di dati di grandi dimensioni. Utilizza oggetti semplici per semplici dati serializzabili JSON e piccole mappe chiave-valore con chiavi stringa.
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

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: implementare una funzione antirimbalzo
**Dichiarazione del problema:** Implementa un'utilità`debounce`che ritarda il richiamo di una funzione fino allo scadere di un periodo di attesa specificato dall'ultima volta che è stata chiamata. Supporta sia l'invocazione del bordo iniziale che di quello finale.
**Passaggio 1: comprendere il problema:**
Una funzione antirimbalzo ignora le chiamate successive rapide e si attiva solo dopo che le chiamate si interrompono per la durata dell'attesa. "Leading edge" significa sparare immediatamente alla prima chiamata. "Bordo d'uscita" significa fuoco dopo il periodo di attesa. Dobbiamo gestire entrambe le modalità e supportare anche la cancellazione.
**Passaggio 2: identificare l'approccio:**
- Memorizza un ID timer in una chiusura.
- Ad ogni chiamata: cancella il timer esistente, quindi imposta un nuovo`setTimeout`.
- Per il fronte ascendente: chiamare immediatamente se nessun timer è attivo.
- Restituisce una funzione antirimbalzo con un metodo `.cancel()`.
- Conserva il contesto e gli argomenti`this`utilizzando le funzioni freccia o`.apply()`.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- La chiusura preserva lo stato tra le chiamate senza inquinare l'ambito globale.
-`clearTimeout`prima di`setTimeout`garantisce che solo l'ultima chiamata attivi l'esecuzione.
-`.cancel()`è importante per la pulizia (ad esempio, lo smontaggio del componente in React).
- Caso limite: se`wait`è 0, la funzione si attiva al successivo tick del ciclo di eventi: utile per raggruppare gli aggiornamenti DOM.
### Problema 2: costruire un limitatore di velocità basato su promesse
**Dichiarazione del problema:** Crea un limitatore di velocità che consenta al massimo N richieste per intervallo di tempo. Dovrebbe restituire Promesse che risolvono quando al chiamante è consentito procedere e mettere in coda le richieste in eccesso.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di una finestra scorrevole o fissa che tenga traccia di quante chiamate sono state effettuate. Quando viene raggiunto il limite, le nuove chiamate dovrebbero essere messe in coda e risolte quando si libera uno slot. Questo è il modello "secchio di token".
**Passaggio 2: identificare l'approccio:**
- Tieni traccia dei timestamp delle chiamate recenti in un array.
- Ad ogni chiamata: rimuovi i timestamp più vecchi della finestra, controlla se conteggio < limite.
- Se sotto limite: risolvere immediatamente.
- Se al limite: calcola quando scade il timestamp più vecchio, imposta un `setTimeout`, quindi risolvi.
- Utilizzare una coda (array di funzioni di risoluzione) per i chiamanti in attesa.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- L'approccio con finestre scorrevoli è più equo rispetto a quello con finestre fisse (nessuna esplosione ai bordi delle finestre).
- L'elaborazione della coda è FIFO: i chiamanti vengono serviti in ordine.
- Per la produzione: aggiunto il supporto`AbortController`in modo che i chiamanti possano annullare l'attesa.
- Prestazioni:`_cleanOldTimestamps`è O(n) per chiamata ma n è delimitato da`maxCalls`.
### Problema 3: implementare una funzione Deep Clone
**Dichiarazione del problema:** Scrivi una funzione che cloni profondamente qualsiasi valore JavaScript, gestendo oggetti, array, date, espressioni regolari, mappe, set, riferimenti circolari e array tipizzati.
**Passaggio 1: comprendere il problema:**
`JSON.parse(JSON.stringify(obj))`fallisce su:`undefined`, funzioni, simboli, date (diventano stringhe), RegExps (diventano oggetti vuoti), mappe, set, riferimenti circolari (lancia) e matrici tipizzate. Abbiamo bisogno di una soluzione ricorsiva che tenga traccia degli oggetti visitati.
**Passaggio 2: identificare l'approccio:**
- Utilizza`Map`per tracciare oggetti già clonati (gestisce i riferimenti circolari).
- Gestisci ogni tipo in modo speciale: Data → nuova data, RegExp → nuova RegExp, Mappa → nuova mappa con voci clonate, Set → nuovo Set con valori clonati.
- Utilizza`structuredClone()`come moderna alternativa integrata (disponibile nei browser e Node.js 17+).
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Riferimenti circolari: la mappa`seen`restituisce il clone già creato invece di ricorrere all'infinito.
- Descrittori di proprietà:`Reflect.ownKeys`+`getOwnPropertyDescriptor`preserva getter, setter e proprietà non enumerabili.
- Alternativa moderna:`structuredClone(value)`gestisce la maggior parte di questi casi in modo nativo (eccetto funzioni e nodi DOM). Preferirlo quando disponibile.
- Prestazioni: per oggetti semplici,`JSON.parse(JSON.stringify(obj))`è ancora il più veloce. Usa il deep clone solo quando ne hai effettivamente bisogno.
### Problema 4: costruire un semplice emettitore di eventi
**Dichiarazione del problema:** Implementa una classe emettitore di eventi che supporti i metodi`on`,`off`,`emit`e `once`. Gli ascoltatori dovranno essere chiamati in ordine di registrazione. `emit`dovrebbe passare argomenti a tutti gli ascoltatori.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di un sistema pub/sub: registri gli ascoltatori per eventi denominati, rimuova ascoltatori specifici, attivi eventi con argomenti e supporti ascoltatori occasionali. Questo è il pattern Observer ampiamente utilizzato in Node.js.
**Passaggio 2: identificare l'approccio:**
- Memorizza gli ascoltatori in un`Map<string, Array<Function>>`.
- `on`: invia l'ascoltatore all'array.
- `off`: filtra l'ascoltatore specifico dall'array.
- `emit`: esegue l'iterazione dell'array e chiama ciascun ascoltatore con argomenti diffusi.
- `once`: avvolge l'ascoltatore in una funzione che si rimuove dopo la prima chiamata.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- La copia`[...listeners]`in`emit`previene problemi quando un ascoltatore chiama`off`durante l'iterazione.
-`once`memorizza`_original`in modo che i chiamanti possano rimuovere il wrapper tramite`off(event, originalFn)`.
- I campi privati ​​(`#listeners`) impediscono la mutazione esterna dello stato interno.
- Per la produzione: aggiungi l'avviso`maxListeners`(come Node.js), la gestione degli errori per ascoltatore e`prependListener`per la priorità.
---

## Riepilogo
JavaScript è inevitabile. È l'unico linguaggio che funziona nei browser Web, rendendolo essenziale per lo sviluppo del frontend. Con Node.js si estende al lato server e con framework come React Native ed Electron raggiunge dispositivi mobili e desktop. L'ecosistema è il più grande nella programmazione. Le peculiarità del linguaggio sono ben note e gestibili e TypeScript risolve i problemi di digitazione. Per tutto ciò che viene eseguito in un browser, JavaScript non è solo la scelta migliore, è l'unica scelta.