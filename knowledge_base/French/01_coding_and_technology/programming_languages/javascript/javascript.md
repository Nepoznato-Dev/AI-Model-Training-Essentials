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
JavaScript est un langage de programmation dynamique et interprété créé par Brendan Eich en seulement 10 jours en 1995. Conçu à l'origine pour ajouter de l'interactivité aux pages Web, il est devenu le langage de programmation le plus utilisé au monde. JavaScript s'exécute dans tous les navigateurs Web, sur les serveurs via Node.js, dans les applications de bureau (Electron), les applications mobiles (React Native) et même les systèmes embarqués.
Le langage est unique dans le sens où il constitue essentiellement la seule option de développement Web côté client : chaque navigateur le prend en charge de manière native. Ce monopole, combiné à l’essor du JavaScript full-stack (Node.js, Deno, Bun), le rend indispensable.
---

## Pourquoi JavaScript est important
- **Le langage du web** : Le seul langage qui s'exécute nativement dans les navigateurs. Aucune alternative pour le frontend.
- **Capacité Full-stack** : Même langage sur le frontend (React, Vue, Svelte) et le backend (Node.js, Express, Fastify).
- **Écosystème massif** : npm compte plus de 2 millions de packages, soit le plus grand registre de logiciels au monde.
- **Polyvalence** : Applications Web, applications mobiles (React Native), applications de bureau (Electron), IoT, fonctions sans serveur.
- **Faible barrière à l'entrée** : fonctionne dans n'importe quel navigateur — aucune installation n'est nécessaire pour commencer le codage.
- **Asynchrone par conception** : les E/S non bloquantes et pilotées par événements le rendent excellent pour les applications en temps réel.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Pièges de la saisie dynamique** | Aucune vérification de type au moment de la compilation ; bugs font surface au moment de l'exécution | Utiliser TypeScript (un sur-ensemble typé de JavaScript) |
| **Complexité de rappel** | Les rappels imbriqués peuvent devenir illisibles (« l'enfer des rappels ») | Utilisez les promesses et async/wait |
| **Sémantique originale** | `==`vs`===`, liaison `this`, levage, coercition de type | Apprenez les bizarreries; utilisez ESLint ; préférez`const`/`let`à`var`|
| **Monothread** | Les tâches liées au processeur bloquent la boucle d'événements | Utilisez des Web Workers, des threads de travail ou déchargez-les vers des modules natifs |
| **Qualité du colis** | l'ouverture de npm entraîne des risques de qualité et de sécurité incohérents | Dépendances d'audit ; utiliser des fichiers de verrouillage ; préférez les packages bien entretenus |
---

## Fondamentaux de la syntaxe
### Variables et types
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

### Fonctions
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

### Objets et classes
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

### Programmation asynchrone
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

###Modules
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

## Syntaxe et modèles avancés
### Déstructuration et propagation/repos (immersion approfondie)
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

### Proxies et réflexion
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

### Symboles, itérateurs et générateurs
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

### Hiérarchies d'erreurs personnalisées
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

## Concurrence et parallélisme
JavaScript est monothread avec une boucle d'événements. La concurrence est obtenue grâce à des modèles asynchrones, des Web Workers et (dans Node.js) le module worker_threads.
### La boucle d'événements
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

### Worker Threads (Node.js — tâches liées au processeur)
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

### Web Workers (navigateur)
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

### Modèles asynchrones
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

## Configuration du projet et système de construction
### Structure du répertoire du projet
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

### Configuration de construction — `package.json`
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

### Configuration du peluchage et du formatage
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

### Pipeline CI/CD — Actions GitHub
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

## Tests
### Test avec Jest
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

### Tests de moquerie et d'intégration
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

## Interopérabilité
### Addons natifs avec N-API (Node.js)
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

### Appel des bibliothèques C avec ffi-napi
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

## Modèles de conception
### Modèle de module (encapsulation)
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

### Modèle d'observateur/émetteur d'événement
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

### Modèle de constructeur
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

## Performances et optimisation
### Outils de profilage
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

### Techniques d'optimisation
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

## Déploiement
### Fichier Docker
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

### Déploiement spécifique à la plate-forme
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

## L'écosystème
### Cadres frontaux
| Cadre | Approche | Idéal pour |
|-----------|----------|---------------|
| **Réagir** | DOM virtuel basé sur des composants | SPA à grande échelle ; le plus grand écosystème |
| **Vue** | Progressif, basé sur un modèle | Adoption progressive; grande expérience de développeur |
| **Svelte** | Au moment de la compilation, pas de DOM virtuel | Des bundles plus petits, un code plus simple |
| **Angulaire** | Framework complet, TypeScript-first | Applications d'entreprise ; structure opiniâtre |
| **Suivant.js** | Méta-framework React (SSR/SSG) | Applications Production React avec SEO |
### Back-end (Node.js)
| Cadre | Objectif |
|-----------|---------|
| **Express** | Framework Web minimal et flexible (le plus populaire) |
| **Fastifier** | Framework Web haute performance |
| **NestJS** | Architecture d'entreprise d'inspiration angulaire |
| **Koa** | Alternative Express légère et moderne |
| **Hon** | Ultra-rapide, multi-exécution (Node, Deno, Bun, edge) |
### Durées d'exécution
| Durée d'exécution | Descriptif |
|---------|-------------|
| **Node.js** | Le runtime JavaScript original côté serveur (moteur V8) |
| **Déno** | Sécurisé par défaut ; prise en charge native de TypeScript ; créé par l'auteur original de Node |
| **Chignon** | Runtime, bundler et gestionnaire de packages tout-en-un ultra-rapides |
### Outils essentiels
| Outil | Objectif |
|------|--------------|
| **npm / fil / pnpm** | Gestionnaires de paquets |
| **TypeScript** | Sur-ensemble typé de JavaScript |
| **ESLint** | Pelucheux de code |
| **Plus joli** | Formatage des codes |
| **Vite** | Outil de construction rapide et serveur de développement |
| **Webpack** | Bundleur de modules (mature, largement utilisé) |
| ** Blague / Vitest ** | Cadres de test |
---

## Quand utiliser JavaScript
| Scénario | Pourquoi JavaScript | Meilleure alternative |
|--------------|---------------|-------------------|
| Interface Web | Seule option pour l'interface utilisateur basée sur un navigateur | — |
| Web complet | Même langue partout | TypeScript pour la sécurité des types |
| Applications en temps réel (chat, jeux) | E/S non bloquantes pilotées par événements | — |
| Fonctions sans serveur | Rapide à écrire, à déployer n'importe où | Python, allez |
| Applications mobiles (React Native) | Partager du code avec le Web | Flutter, natif Swift/Kotlin |
| Applications de bureau (Electron) | Multiplateforme avec la technologie Web | C# (WPF), Tauri (Rouille) |
| Calcul gourmand en CPU | Limitation monothread | Python (NumPy), C++, Rust, WebAssembly |
| Programmation systèmes | Mauvais niveau d'abstraction | C, C++, Rust, Go |
---

## Questions et réponses synthétiques
### Q1 : Quelle est la différence entre`var`,`let`et`const`, et quand dois-je les utiliser ?
**R :**`var`est limité à une fonction et hissé – évitez-le dans le code moderne. `let`a une portée de bloc et permet la réaffectation. `const`a une portée de bloc et empêche la réaffectation (mais les objets/tableaux auxquels il fait référence sont toujours mutables). Bonne pratique : valeur par défaut`const`, utilisez`let`uniquement lorsque vous avez besoin d'une réaffectation, n'utilisez jamais`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2 : Comment`this`fonctionne-t-il en JavaScript et pourquoi est-il si déroutant ?
**R :**`this`est déterminé par **la façon dont une fonction est appelée**, et non par l'endroit où elle est définie. Dans un appel de méthode,`this`est l'objet. Dans un appel autonome, il s'agit de`undefined`(mode strict) ou`global`(non strict). Les fonctions fléchées héritent de`this`de leur portée englobante — c'est pourquoi elles sont préférées pour les rappels. Utilisez`.bind()`pour définir explicitement`this`.
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

### Q3 : Qu'est-ce que la boucle d'événements et comment fonctionnent réellement async/await ?
**R :** JavaScript est monothread avec une boucle d'événements qui traite une file d'attente. La pile d'appels exécute du code synchrone. Lorsqu'elle est vide, la boucle d'événements sélectionne la tâche suivante dans la file d'attente des microtâches (Promises) ou la file d'attente des macrotâches (setTimeout, I/O). `async/await`est un sucre syntaxique par rapport aux promesses -`await`met en pause la fonction asynchrone et reprend lorsque la promesse est résolue, sans bloquer le thread.
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

### Q4 : Comment dois-je gérer les erreurs dans le JavaScript moderne ?
**R :** Utilisez`try/catch`pour le code synchrone et`.catch()`ou`try/catch`avec`async/await`pour le code asynchrone. Gérez toujours les rejets de promesse – les rejets non gérés font planter Node.js. Créez des classes d'erreurs personnalisées pour les erreurs spécifiques au domaine. Utilisez un gestionnaire d’erreurs global comme filet de sécurité.
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

### Q5 : Quand dois-je utiliser`Map`/`Set`au lieu d'objets/tableaux simples ?
**R :** Utilisez`Map`lorsque les clés ne sont pas des chaînes, lorsque vous avez besoin d'une itération par ordre d'insertion, lorsque vous avez besoin de`.size`ou lorsque vous ajoutez/supprimez fréquemment des entrées (meilleures performances que les objets). Utilisez`Set`pour des collections uniques avec recherche O(1) — beaucoup plus rapide que`array.includes()`pour les grands ensembles de données. Utilisez des objets simples pour des données simples sérialisables JSON et de petites cartes clé-valeur avec des clés de chaîne.
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : implémenter une fonction anti-rebond
**Énoncé du problème :** Implémentez un utilitaire`debounce`qui retarde l'appel d'une fonction jusqu'à ce qu'une période d'attente spécifiée se soit écoulée depuis le dernier appel. Prend en charge les invocations de bord avant et arrière.
**Étape 1 — Comprendre le problème :**
Une fonction anti-rebond ignore les appels successifs rapides et ne se déclenche qu'après l'arrêt des appels pendant la durée d'attente. « bord d'attaque » signifie tirer immédiatement au premier appel. « Bord de fuite » signifie un incendie après la période d'attente. Nous devons gérer les deux modes et également prendre en charge l'annulation.
**Étape 2 — Identifiez l'approche :**
- Stockez un identifiant de minuterie dans une fermeture.
- A chaque appel : effacez le timer existant, puis définissez un nouveau`setTimeout`.
- Pour front montant : appeler immédiatement si aucun temporisateur n'est actif.
- Renvoie une fonction anti-rebond avec une méthode `.cancel()`.
- Préservez le contexte et les arguments`this`à l'aide des fonctions fléchées ou `.apply()`.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- La fermeture préserve l'état entre les appels sans polluer la portée globale.
-`clearTimeout`avant`setTimeout`assure que seul le dernier appel déclenche l'exécution.
-`.cancel()`est important pour le nettoyage (par exemple, démontage de composant dans React).
- Cas limite : si`wait`vaut 0, la fonction se déclenche au prochain tick de boucle d'événement - utile pour regrouper les mises à jour du DOM.
### Problème 2 : Créer un limiteur de débit basé sur des promesses
**Énoncé du problème :** Créez un limiteur de débit qui autorise au plus N requêtes par fenêtre horaire. Il doit renvoyer des promesses qui se résolvent lorsque l'appelant est autorisé à continuer et mettre en file d'attente les demandes excédentaires.
**Étape 1 — Comprendre le problème :**
Nous avons besoin d'une fenêtre coulissante ou fixe qui suit le nombre d'appels passés. Lorsque la limite est atteinte, les nouveaux appels doivent être mis en file d'attente et résolus lorsqu'un créneau se libère. Il s’agit du modèle « seau à jetons ».
**Étape 2 — Identifiez l'approche :**
- Suivez les horodatages des appels récents dans un tableau.
- A chaque appel : supprimez les horodatages plus anciens que la fenêtre, vérifiez si le nombre < limite.
- En cas de dépassement de limite : résoudre immédiatement.
- Si la limite est atteinte : calculez quand l'horodatage le plus ancien expire, définissez un`setTimeout`, puis résolvez.
- Utilisez une file d'attente (un tableau de fonctions de résolution) pour les appelants en attente.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- L'approche par fenêtre glissante est plus juste que les fenêtres fixes (pas d'éclatement aux limites de la fenêtre).
- Le traitement de la file d'attente est FIFO — les appelants sont servis dans l'ordre.
- Pour la production : ajoutez le support`AbortController`afin que les appelants puissent annuler l'attente.
- Performance :`_cleanOldTimestamps`est O(n) par appel mais n est délimité par`maxCalls`.
### Problème 3 : implémenter une fonction de clone profond
**Énoncé du problème :** Écrivez une fonction qui clone en profondeur toute valeur JavaScript, en gérant les objets, les tableaux, les dates, les expressions régulières, les cartes, les ensembles, les références circulaires et les tableaux typés.
**Étape 1 — Comprendre le problème :**
`JSON.parse(JSON.stringify(obj))`échoue sur :`undefined`, fonctions, symboles, dates (deviennent des chaînes), RegExps (deviennent des objets vides), cartes, ensembles, références circulaires (lancements) et tableaux typés. Nous avons besoin d'une solution récursive qui suit les objets visités.
**Étape 2 — Identifiez l'approche :**
- Utilisez un`Map`pour suivre les objets déjà clonés (gère les références circulaires).
- Gérer chaque type spécialement : Date → nouvelle Date, RegExp → nouvelle RegExp, Carte → nouvelle Carte avec entrées clonées, Set → nouvel Set avec valeurs clonées.
- Utilisez`structuredClone()`comme alternative intégrée moderne (disponible dans les navigateurs et Node.js 17+).
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Références circulaires : la Map`seen`renvoie le clone déjà créé au lieu de récurer à l'infini.
- Descripteurs de propriété :`Reflect.ownKeys`+`getOwnPropertyDescriptor`préserve les getters, les setters et les propriétés non énumérables.
- Alternative moderne :`structuredClone(value)`gère nativement la plupart de ces cas (sauf fonctions et nœuds DOM). Préférez-le lorsqu'il est disponible.
- Performance : pour les objets simples,`JSON.parse(JSON.stringify(obj))`est toujours le plus rapide. Utilisez le clonage profond uniquement lorsque vous en avez réellement besoin.
### Problème 4 : Créer un émetteur d'événements simple
**Énoncé du problème :** Implémentez une classe d'émetteur d'événements qui prend en charge les méthodes`on`,`off`,`emit`et`once`. Les auditeurs doivent être appelés dans l'ordre d'inscription. `emit`doit transmettre des arguments à tous les écouteurs.
**Étape 1 — Comprendre le problème :**
Nous avons besoin d'un système pub/sub : enregistrer les auditeurs pour les événements nommés, supprimer des auditeurs spécifiques, déclencher des événements avec des arguments et prendre en charge les auditeurs ponctuels. Il s'agit du modèle Observer largement utilisé dans Node.js.
**Étape 2 — Identifiez l'approche :**
- Stockez les auditeurs dans un`Map<string, Array<Function>>`.
-`on`: pousse l'écouteur vers le tableau.
-`off`: filtre l'écouteur spécifique du tableau.
- `emit` : itérer le tableau et appeler chaque écouteur avec des arguments répartis.
-`once`: enveloppe l'écouteur dans une fonction qui se supprime après le premier appel.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- La copie`[...listeners]`dans`emit`évite les problèmes lorsqu'un écouteur appelle`off`pendant l'itération.
-`once`stocke`_original`afin que les appelants puissent supprimer le wrapper via`off(event, originalFn)`.
- Les champs privés (`#listeners`) empêchent la mutation externe de l'état interne.
- Pour la production : ajoutez l'avertissement`maxListeners`(comme Node.js), la gestion des erreurs par écouteur et`prependListener`pour la priorité.
---

## Résumé
JavaScript est incontournable. C'est le seul langage qui s'exécute dans les navigateurs Web, ce qui le rend essentiel pour le développement front-end. Avec Node.js, il s'étend côté serveur, et avec des frameworks comme React Native et Electron, il atteint les mobiles et les ordinateurs de bureau. L'écosystème est le plus grand en programmation. Les bizarreries du langage sont bien connues et gérables – et TypeScript répond aux problèmes de frappe. Pour tout ce qui s'exécute dans un navigateur, JavaScript n'est pas seulement le meilleur choix : c'est le seul choix.