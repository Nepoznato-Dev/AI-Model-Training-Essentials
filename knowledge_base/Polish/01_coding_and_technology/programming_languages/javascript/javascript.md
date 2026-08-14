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
JavaScript to dynamiczny, interpretowany język programowania stworzony przez Brendana Eicha w zaledwie 10 dni w 1995 roku. Pierwotnie zaprojektowany w celu dodania interaktywności do stron internetowych, stał się najpopularniejszym językiem programowania na świecie. JavaScript działa w każdej przeglądarce internetowej, na serwerach poprzez Node.js, w aplikacjach desktopowych (Electron), aplikacjach mobilnych (React Native), a nawet systemach wbudowanych.
Język ten jest wyjątkowy, ponieważ jest w zasadzie jedyną opcją tworzenia stron internetowych po stronie klienta — każda przeglądarka obsługuje go natywnie. Ten monopol w połączeniu z rozwojem pełnego stosu JavaScript (Node.js, Deno, Bun) sprawia, że ​​jest on niezbędny.
---

## Dlaczego JavaScript jest ważny
- **Język sieci**: Jedyny język, który działa natywnie w przeglądarkach. Brak alternatywy dla frontendu.
- **Możliwość pełnego stosu**: Ten sam język na interfejsie (React, Vue, Svelte) i backendie (Node.js, Express, Fastify).
- **Ogromny ekosystem**: npm ma ponad 2 miliony pakietów — największy rejestr oprogramowania na świecie.
- **Wszechstronność**: aplikacje internetowe, aplikacje mobilne (React Native), aplikacje komputerowe (Electron), IoT, funkcje bezserwerowe.
- **Niski próg wejścia**: Działa w dowolnej przeglądarce — nie jest wymagana instalacja, aby rozpocząć kodowanie.
- **Z założenia asynchroniczny**: Sterowane zdarzeniami, nieblokujące wejścia/wyjścia sprawiają, że doskonale nadają się do zastosowań w czasie rzeczywistym.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Pułapki podczas pisania dynamicznego** | Brak sprawdzania typu w czasie kompilacji; błędy pojawiają się w czasie wykonywania | Użyj TypeScript (nadzbiór JavaScriptu z typem) |
| **Złożoność wywołania zwrotnego** | Zagnieżdżone wywołania zwrotne mogą stać się nieczytelne („piekło wywołań zwrotnych”) | Użyj obietnic i async/await |
| **Dziwaczna semantyka** | `==`vs`===`,`this`wiązanie, podnoszenie, wymuszenie typu | Naucz się dziwactw; użyj ESLint; wolisz`const`/`let`zamiast`var`|
| **Jednowątkowy** | Zadania związane z procesorem blokują pętlę zdarzeń | Użyj procesów roboczych sieci Web, wątków roboczych lub przenieś do modułów natywnych |
| **Jakość opakowania** | otwartość npm oznacza niespójne ryzyko jakości i bezpieczeństwa | Zależności audytowe; użyj plików blokujących; preferują dobrze utrzymane pakiety |
---

## Podstawy składni
### Zmienne i typy
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

### Funkcje
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

### Obiekty i klasy
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

### Programowanie asynchroniczne
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

### Moduły
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

## Zaawansowana składnia i wzorce
### Destrukturyzacja i rozprzestrzenianie/odpoczynek (głębokie nurkowanie)
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

### Serwery proxy i refleksja
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

### Symbole, iteratory i generatory
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

### Niestandardowe hierarchie błędów
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

## Współbieżność i równoległość
JavaScript jest jednowątkowy z pętlą zdarzeń. Współbieżność osiąga się poprzez wzorce asynchroniczne, procesy robocze sieci Web i (w Node.js) moduł worker_threads.
### Pętla zdarzeń
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

### Wątki robocze (Node.js — zadania związane z procesorem)
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

### Pracownicy sieciowi (przeglądarka)
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

### Wzorce asynchroniczne
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

## Konfiguracja projektu i budowanie systemu
### Struktura katalogu projektu
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

### Konfiguracja kompilacji — `package.json`
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

### Konfiguracja lintingu i formatowania
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

### Potok CI/CD — akcje w GitHubie
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

## Testowanie
### Testowanie z Jest
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

### Testy drwiące i integracyjne
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

## Interoperacyjność
### Natywne dodatki z N-API (Node.js)
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

### Zespół sieciowy (Wasm)
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

### Wywoływanie bibliotek C za pomocą ffi-napi
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

## Wzorce projektowe
### Wzorzec modułu (hermetyzacja)
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

### Wzór obserwatora/emitera zdarzenia
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

### Wzór konstruktora
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

## Wydajność i optymalizacja
### Narzędzia do profilowania
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

### Techniki optymalizacji
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

## Zastosowanie
### Plik Dockera
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

### Wdrożenie specyficzne dla platformy
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

## Ekosystem
### Frameworki frontendowe
| Ramy | Podejście | Najlepsze dla |
|----------|----------|---------|
| **Reaguj** | Oparte na komponentach, wirtualne DOM | SPA na dużą skalę; największy ekosystem |
| **Vue** | Progresywne, oparte na szablonach | Stopniowe przyjęcie; świetne doświadczenie programistyczne |
| **Smukły** | Czas kompilacji, brak wirtualnego DOM | Mniejsze pakiety, prostszy kod |
| **Kątowy** | Pełna platforma, najpierw TypeScript | aplikacje korporacyjne; uparty struktura |
| **Następny.js** | Metarama reakcji (SSR/SSG) | Aplikacje Production React z SEO |
### Backend (Node.js)
| Ramy | Cel |
|---------------|--------|
| **Ekspres** | Minimalny, elastyczny framework sieciowy (najpopularniejszy) |
| **Przymocuj** | Wysokowydajna platforma internetowa |
| **NestJS** | Architektura klasy korporacyjnej inspirowana Angularem |
| **Koa** | Lekka, nowoczesna alternatywa Express |
| **Cześć** | Ultraszybki, wieloetapowy (Node, Deno, Bun, Edge) |
### Czasy działania
| Czas wykonania | Opis |
|--------|------------|
| **Node.js** | Oryginalne środowisko wykonawcze JavaScript po stronie serwera (silnik V8) |
| **Deno** | Domyślnie bezpieczne; natywna obsługa TypeScriptu; stworzony przez oryginalnego autora Node'a |
| **Kok** | Ultraszybkie, wszechstronne środowisko wykonawcze, program pakujący i menedżer pakietów |
### Niezbędne narzędzia
| Narzędzie | Cel |
|------|-------------|
| **npm / przędza / pnpm** | Menedżerowie pakietów |
| **Maszynopis** | Wpisany nadzbiór JavaScript |
| **ESLint** | Linting kodu |
| **Ładniej** | Formatowanie kodu |
| **Witaj** | Narzędzie do szybkiego budowania i serwer deweloperski |
| **Pakiet internetowy** | Pakiet modułów (dojrzały, szeroko stosowany) |
| **Jest / Odwiedza** | Frameworki testowe |
---

## Kiedy używać JavaScript
| Scenariusz | Dlaczego JavaScript | Lepsza alternatywa |
|---------|---------------|--------------------------------|
| Interfejs WWW | Jedyna opcja dla interfejsu użytkownika opartego na przeglądarce | — |
| Sieć z pełnym stosem | Wszędzie ten sam język | TypeScript dla bezpieczeństwa typów |
| Aplikacje czasu rzeczywistego (czat, gry) | Sterowane zdarzeniami, nieblokujące wejścia/wyjścia | — |
| Funkcje bezserwerowe | Szybkie pisanie, wdrażanie w dowolnym miejscu | Pythonie, idź |
| Aplikacje mobilne (React Native) | Udostępnij kod w sieci | Flutter, natywny Swift/Kotlin |
| Aplikacje komputerowe (elektron) | Wieloplatformowy z technologią internetową | C# (WPF), Tauri (Rdza) |
| Obliczenia intensywnie obciążające procesor | Ograniczenie jednowątkowe | Python (NumPy), C++, Rust, WebAssembly |
| Programowanie systemów | Zły poziom abstrakcji | C, C++, Rust, Przejdź |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między`var`,`let`i`const`i kiedy należy używać każdego z nich?
**A:**`var`ma zakres funkcji i jest podnoszony — unikaj tego we współczesnym kodzie. `let`ma zasięg blokowy i umożliwia ponowne przypisanie. `const`ma zasięg blokowy i zapobiega ponownemu przypisaniu (ale obiekty/tablice, do których się odwołuje, nadal można modyfikować). Najlepsza praktyka: domyślnie`const`, używaj`let`tylko wtedy, gdy potrzebujesz ponownego przypisania, nigdy nie używaj`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### P2: Jak działa`this`w JavaScript i dlaczego jest to tak zagmatwane?
**A:**`this`jest określany przez **sposób wywołania funkcji**, a nie miejsce jej zdefiniowania. W wywołaniu metody obiektem jest `this`. W przypadku połączenia samodzielnego jest to`undefined`(tryb ścisły) lub`global`(nieścisły). Funkcje strzałkowe dziedziczą`this`ze swojego zakresu — dlatego są preferowane w przypadku wywołań zwrotnych. Użyj `.bind()`, aby jawnie ustawić`this`.
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

### P3: Co to jest pętla zdarzeń i jak właściwie działa funkcja asynchronizacji/oczekiwania?
**O:** JavaScript jest jednowątkowy z pętlą zdarzeń, która przetwarza kolejkę. Stos wywołań wykonuje kod synchroniczny. Gdy jest pusta, pętla zdarzeń wybiera następne zadanie z kolejki mikrozadań (Promises) lub kolejki makrozadań (setTimeout, I/O). `async/await`to cukier syntaktyczny w przypadku obietnic —`await`wstrzymuje funkcję asynchroniczną i wznawia ją po rozwiązaniu obietnicy, bez blokowania wątku.
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

### P4: Jak mam postępować z błędami we współczesnym JavaScript?
**A:** Użyj`try/catch`dla kodu synchronicznego i`.catch()`lub`try/catch`z`async/await`dla kodu asynchronicznego. Zawsze obsługuj odrzucenia obietnic — nieobsłużone odrzucenia powodują awarię Node.js. Utwórz niestandardowe klasy błędów dla błędów specyficznych dla domeny. Użyj globalnej procedury obsługi błędów jako siatki bezpieczeństwa.
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

### P5: Kiedy powinienem używać`Map`/`Set`zamiast zwykłych obiektów/tablic?
**A:** Użyj `Map`, gdy klucze nie są ciągami znaków, gdy potrzebujesz iteracji kolejności wstawiania, gdy potrzebujesz`.size`lub gdy często dodajesz/usuwasz wpisy (lepsza wydajność niż obiekty). Użyj`Set`dla unikalnych kolekcji z wyszukiwaniem O(1) — znacznie szybciej niż`array.includes()`dla dużych zbiorów danych. Używaj zwykłych obiektów do prostych danych, które można serializować w formacie JSON i małych map klucz-wartość z kluczami łańcuchowymi.
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

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zaimplementuj funkcję odrzucenia
**Opis problemu:** Zaimplementuj narzędzie `debounce`, które opóźnia wywołanie funkcji do czasu, aż upłynie określony czas oczekiwania od ostatniego wywołania. Obsługa wywołań krawędzi wiodącej i końcowej.
**Krok 1 — Zrozum problem:**
Odrzucona funkcja ignoruje szybkie, kolejne wywołania i uruchamia się dopiero po zatrzymaniu wywołań na czas oczekiwania. „Przewaga” oznacza ogień natychmiast po pierwszym wezwaniu. „Zbocze opadające” oznacza pożar po okresie oczekiwania. Musimy obsługiwać oba tryby, a także obsługiwać anulowanie.
**Krok 2 — Zidentyfikuj podejście:**
- Przechowuj identyfikator timera w zamknięciu.
- Przy każdym połączeniu: wyczyść istniejący timer, a następnie ustaw nowy `setTimeout`.
- W przypadku krawędzi natarcia: zadzwoń natychmiast, jeśli żaden timer nie jest aktywny.
- Zwróć odrzuconą funkcję za pomocą metody `.cancel()`.
- Zachowaj kontekst i argumenty`this`za pomocą funkcji strzałek lub`.apply()`.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
— Zamknięcie zachowuje stan we wszystkich połączeniach bez zanieczyszczania zasięgu globalnego.
-`clearTimeout`przed`setTimeout`zapewnia, że ​​tylko ostatnie wywołanie wyzwala wykonanie.
-`.cancel()`jest ważny przy czyszczeniu (np. odmontowaniu komponentu w React).
- Przypadek brzegowy: jeśli`wait`wynosi 0, funkcja uruchamia się przy następnym zaznaczeniu pętli zdarzeń — przydatne przy grupowaniu aktualizacji DOM.
### Problem 2: Stwórz ogranicznik stawki oparty na obietnicach
**Opis problemu:** Utwórz ogranicznik szybkości, który dopuszcza maksymalnie N żądań w oknie czasowym. Powinien zwracać obietnice, które zostaną rozpatrzone, gdy osoba wywołująca będzie mogła kontynuować, i kolejkować nadmiarowe żądania.
**Krok 1 — Zrozum problem:**
Potrzebujemy przesuwanego lub stałego okna, które śledzi liczbę wykonanych połączeń. Po osiągnięciu limitu nowe połączenia powinny być umieszczane w kolejce i rozwiązywane, gdy zwolni się miejsce. To jest wzór „wiadra tokenów”.
**Krok 2 — Zidentyfikuj podejście:**
- Śledź znaczniki czasu ostatnich połączeń w tablicy.
- Przy każdym wywołaniu: usuń znaczniki czasu starsze niż okno, sprawdź, czy liczba < limit.
- Jeśli poniżej limitu: natychmiast rozwiąż problem.
- Jeśli na granicy: oblicz, kiedy wygaśnie najstarszy znacznik czasu, ustaw`setTimeout`, a następnie rozwiąż.
- Użyj kolejki (tablicy funkcji rozwiązywania) dla oczekujących rozmówców.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Podejście do okien przesuwnych jest bardziej sprawiedliwe niż okna stałe (brak pęknięć na granicach okien).
- Przetwarzanie kolejki odbywa się w trybie FIFO — osoby dzwoniące są obsługiwane w kolejności.
- W przypadku produkcji: dodaj obsługę `AbortController`, aby dzwoniący mogli anulować oczekiwanie.
- Wydajność:`_cleanOldTimestamps`wynosi O(n) na wywołanie, ale n jest ograniczone przez `maxCalls`.
### Problem 3: Zaimplementuj funkcję głębokiego klonowania
**Opis problemu:** Napisz funkcję, która głęboko klonuje dowolną wartość JavaScript, obsługując obiekty, tablice, daty, wyrażenia regularne, mapy, zbiory, odniesienia cykliczne i tablice z określonym typem.
**Krok 1 — Zrozum problem:**
`JSON.parse(JSON.stringify(obj))`kończy się niepowodzeniem w przypadku:`undefined`, funkcji, symboli, dat (stają się ciągami znaków), RegExps (stają się pustymi obiektami), map, zestawów, odwołań cyklicznych (rzutów) i tablic z określonym typem. Potrzebujemy rozwiązania rekurencyjnego, które śledzi odwiedzane obiekty.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`Map`do śledzenia już sklonowanych obiektów (obsługuje odniesienia cykliczne).
- Obsługuj każdy typ specjalnie: Data → nowa Data, RegExp → nowa RegExp, Mapa → nowa Mapa ze sklonowanymi wpisami, Ustaw → nowy Zestaw ze sklonowanymi wartościami.
- Użyj`structuredClone()`jako nowoczesnej wbudowanej alternatywy (dostępnej w przeglądarkach i Node.js 17+).
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Odniesienia cykliczne: mapa`seen`zwraca już utworzony klon zamiast powtarzać się w nieskończoność.
- Deskryptory właściwości:`Reflect.ownKeys`+`getOwnPropertyDescriptor`zachowują metody pobierające, ustawiające i nieprzeliczalne właściwości.
- Nowoczesna alternatywa:`structuredClone(value)`obsługuje większość tych przypadków natywnie (z wyjątkiem funkcji i węzłów DOM). Preferuj, gdy jest dostępny.
- Wydajność: w przypadku prostych obiektów`JSON.parse(JSON.stringify(obj))`jest nadal najszybszy. Używaj głębokiego klonowania tylko wtedy, gdy naprawdę tego potrzebujesz.
### Problem 4: Zbuduj prosty emiter zdarzeń
**Opis problemu:** Zaimplementuj klasę emitera zdarzeń obsługującą metody`on`,`off`,`emit`i `once`. Słuchaczy należy wywoływać według kolejności rejestracji. `emit`powinien przekazywać argumenty wszystkim słuchaczom.
**Krok 1 — Zrozum problem:**
Potrzebujemy systemu pub/sub: rejestruj słuchacze dla nazwanych zdarzeń, usuwaj określonych słuchaczy, wyzwalaj zdarzenia za pomocą argumentów i obsługuj słuchacze jednorazowe. Jest to wzorzec Observer szeroko używany w Node.js.
**Krok 2 — Zidentyfikuj podejście:**
- Przechowuj słuchaczy w`Map<string, Array<Function>>`.
- `on`: wypychanie słuchacza do tablicy.
- `off`: odfiltruj konkretnego słuchacza z tablicy.
- `emit`: iteracja tablicy i wywołanie każdego słuchacza z argumentami rozproszonymi.
-`once`: zawija słuchacza w funkcję, która usuwa się po pierwszym wywołaniu.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
— Kopia`[...listeners]`w`emit`zapobiega problemom, gdy słuchacz wywołuje`off`podczas iteracji.
-`once`przechowuje `_original`, więc osoby wywołujące mogą usunąć opakowanie poprzez`off(event, originalFn)`.
- Pola prywatne (`#listeners`) zapobiegają zewnętrznym mutacjom stanu wewnętrznego.
- W przypadku produkcji: dodaj ostrzeżenie`maxListeners`(jak Node.js), obsługę błędów na słuchacza i`prependListener`dla priorytetu.
---

## Streszczenie
JavaScript jest nieunikniony. Jest to jedyny język, który działa w przeglądarkach internetowych, co czyni go niezbędnym do tworzenia frontendu. Dzięki Node.js rozciąga się na stronę serwerową, a dzięki frameworkom takim jak React Native i Electron dociera do urządzeń mobilnych i komputerów stacjonarnych. Ekosystem jest największy w programowaniu. Dziwactwa tego języka są dobrze znane i łatwe do opanowania, a TypeScript rozwiązuje problemy związane z pisaniem. W przypadku wszystkiego, co działa w przeglądarce, JavaScript jest nie tylko najlepszym wyborem — to jedyny wybór.