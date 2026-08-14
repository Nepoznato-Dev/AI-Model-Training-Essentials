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
#Javascript
JavaScript ni lugha ya programu inayobadilika, iliyotafsiriwa iliyoundwa na Brendan Eich katika muda wa siku 10 tu mwaka wa 1995. Hapo awali iliundwa ili kuongeza mwingiliano kwenye kurasa za wavuti, imekua na kuwa lugha ya programu inayotumiwa zaidi ulimwenguni. JavaScript hutumika katika kila kivinjari, kwenye seva kupitia Node.js, katika programu za kompyuta za mezani (Elektroni), programu za simu (React Native), na hata mifumo iliyopachikwa.
Lugha ni ya kipekee kwa kuwa kimsingi ndiyo chaguo pekee kwa ukuzaji wa wavuti wa upande wa mteja - kila kivinjari kinaitumia asili. Ukiritimba huu, pamoja na kuongezeka kwa JavaScript yenye rundo kamili (Node.js, Deno, Bun), huifanya iwe ya lazima.
---

## Kwa Nini JavaScript Ni Muhimu
- **Lugha ya wavuti**: Lugha pekee inayotumika kienyeji katika vivinjari. Hakuna mbadala kwa frontend.
- **Uwezo wa mrundikano kamili**: Lugha sawa kwenye mandhari ya mbele (React, Vue, Svelte) na mandharinyuma (Node.js, Express, Fastify).
- **Mfumo mkubwa wa ikolojia**: npm ina zaidi ya vifurushi milioni 2 - sajili kubwa zaidi ya programu ulimwenguni.
- ** Utangamano**: Programu za Wavuti, programu za rununu (React Native), programu za kompyuta za mezani (Elektroni), IoT, vitendaji visivyo na seva.
- **Kizuizi kidogo cha kuingia**: Hutumika katika kivinjari chochote — hakuna usakinishaji unaohitajika ili kuanza kusimba.
- **Inayolingana na muundo**: I/O inayoendeshwa na tukio, isiyozuia huifanya kuwa bora kwa programu za wakati halisi.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Mitego Inayobadilika ya kuandika** | Hakuna ukaguzi wa aina ya wakati; mende huonekana wakati wa kukimbia | Tumia TypeScript (seti kuu iliyochapwa ya JavaScript) |
| **Utata wa kupiga simu** | Nambari za simu zilizowekwa kwenye simu zinaweza kutosomeka ("kuzimu ya kupiga simu") | Tumia Ahadi na async/ngoja |
| **Semantiki za ajabu** | `==`vs`===`,`this`kufunga, kuinua, aina ya kulazimisha | Jifunze mambo ya ajabu; tumia ESLint; napendelea`const`/`let`kuliko`var`|
| **Nyezi moja** | Kazi zinazofungamana na CPU huzuia kitanzi cha tukio | Tumia Wafanyakazi wa Wavuti, nyuzi za wafanyakazi, au pakua kwa moduli asili |
| **Ubora wa kifurushi** | uwazi wa npm unamaanisha hatari zisizolingana za ubora na usalama | Utegemezi wa ukaguzi; tumia faili za kufuli; pendelea vifurushi vilivyotunzwa vizuri |
---

## Misingi ya Sintaksia
### Vigezo na Aina
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

### Kazi
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

### Vitu na Madarasa
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

Upangaji wa ### Async
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

## Sintaksia na Miundo ya Kina
### Kuharibu & Kueneza/Kupumzika (Kupiga mbizi kwa kina)
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

### Wakala na Tafakari
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

### Alama, Viigaji, na Jenereta
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

### Daraja Maalum za Hitilafu
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

## Concurrency & Usambamba
JavaScript imeunganishwa kwa nyuzi moja na kitanzi cha tukio. Upatanisho hupatikana kupitia mifumo isiyolingana, Wafanyakazi wa Wavuti, na (katika Node.js) moduli ya worker_threads.
### Kitanzi cha Tukio
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

### Nyuzi za Wafanyakazi (Node.js — Kazi zinazofungamana na CPU)
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

### Wafanyakazi wa Wavuti (Kivinjari)
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

### Miundo ya Async
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Saraka ya Mradi
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

### Usanidi wa Kuunda — `package.json`
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

### Uwekaji na Uumbizaji wa Uumbizaji
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

### CI/CD Bomba - Vitendo vya GitHub
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

##Upimaji
### Kujaribu na Jest
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

### Vipimo vya Kejeli na Muunganisho
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

## Kuingiliana
### Native Addons na N-API (Node.js)
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

### Kuita Maktaba za C kwa kutumia ffi-napi
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

## Miundo ya Kubuni
### Muundo wa Moduli (Encapsulation)
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

### Muundo wa Mwangalizi / Tukio la Mwigizaji
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

### Muundo wa Wajenzi
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
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

### Mbinu za Kuboresha
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

## Usambazaji
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

### Usambazaji Mahususi wa Mfumo
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

## Mfumo wa Ikolojia
### Mifumo ya Mbele
| Mfumo | Mbinu | Bora Kwa |
|-----------|----------|-----------|
| **Jibu** | Kulingana na vipengele, DOM pepe | SPA za kiwango kikubwa; mfumo mkubwa wa ikolojia |
| **Vue** | Inayoendelea, kulingana na kiolezo | Kupitishwa kwa taratibu; uzoefu mkubwa wa msanidi |
| **Svelte** | Muda wa kukusanya, hakuna DOM pepe | Vifurushi vidogo, msimbo rahisi zaidi |
| **Angular** | Mfumo kamili, TypeScript-kwanza | Programu za biashara; muundo wa maoni |
| **Inayofuata.js** | React meta-framework (SSR/SSG) | Programu za Uzalishaji wa React na SEO |
### Nyuma (Node.js)
| Mfumo | Kusudi |
|-----------|---------|
| **Express** | Mfumo mdogo wa wavuti unaonyumbulika (maarufu zaidi) |
| **Fastify** | Mfumo wa wavuti wenye utendaji wa juu |
| **NestJS** | Usanifu wa daraja la biashara, Angular-inspired |
| **Koa** | Nyepesi, mbadala ya kisasa ya Express |
| **Heshima** | Kasi ya juu zaidi, wakati mwingi wa kukimbia (Njia, Deno, Bun, ukingo) |
### Nyakati za utekelezaji
| Muda wa kukimbia | Maelezo |
|---------|-------------|
| **Node.js** | Muda halisi wa utekelezaji wa JavaScript wa upande wa seva (injini ya V8) |
| **Deno** | Salama kwa chaguo-msingi; usaidizi wa asili wa TypeScript; imeundwa na mwandishi asilia wa Node |
| **Bun** | Muda wa utekelezaji wa haraka sana wa kila mmoja, kifurushi na kidhibiti kifurushi |
### Zana Muhimu
| Zana | Kusudi |
|------|----------|
| **npm / uzi / pnpm** | Wasimamizi wa vifurushi |
| **TypeScript** | Aina kuu ya JavaScript |
| **ESLint** | Kuweka kanuni |
| **Mrembo zaidi** | Uumbizaji wa msimbo |
| **Vite** | Chombo cha kujenga haraka na seva ya dev |
| **Kifurushi cha wavuti** | Kifurushi cha moduli (iliyokomaa, inatumika sana) |
| **Jest / Vitest** | Mifumo ya majaribio |
---

## Wakati wa Kutumia JavaScript
| Hali | Kwa nini JavaScript | Mbadala Bora |
|----------|----------------------------------|
| Mbele ya wavuti | Chaguo pekee kwa UI inayotegemea kivinjari | - |
| Wavuti kamili | Lugha sawa kila mahali | TypeScript kwa usalama wa aina |
| Programu za wakati halisi (soga, michezo) | I/O inayoendeshwa na tukio | - |
| Vitendaji visivyo na seva | Haraka kuandika, peleka popote | Python, Nenda |
| Programu za rununu (React Asili) | Shiriki msimbo na wavuti | Flutter, mzaliwa wa Swift/Kotlin |
| Programu za Kompyuta ya mezani (Elektroni) | Jukwaa mtambuka na teknolojia ya wavuti | C# (WPF), Tauri (Kutu) |
| Uhesabuji wa kina wa CPU | Kizuizi cha nyuzi moja | Python (NumPy), C++, Rust, WebAssembly |
| Upangaji wa mifumo | Kiwango kibaya cha uondoaji | C, C++, Rust, Nenda |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`var`,`let`, na`const`, na ni lini ninapaswa kutumia kila moja?
**J:**`var`imewekewa utendakazi na kuinuliwa - iepuke katika msimbo wa kisasa. `let`imewekewa mipaka na inaruhusu kukabidhiwa upya. `const`imewekewa kizuizi na inazuia kukabidhiwa upya (lakini marejeleo ya vitu/mikusanyiko bado yanaweza kubadilika). Mbinu bora zaidi: chaguo-msingi kwa`const`, tumia`let`wakati tu unahitaji kukabidhiwa upya, kamwe usitumie`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2: Je,`this`inafanyaje kazi katika JavaScript, na kwa nini inachanganya sana?
**J:**`this`inabainishwa na **jinsi chaguo la kukokotoa linavyoitwa**, si pale inapofafanuliwa. Katika simu ya mbinu,`this`ndio kitu. Katika simu ya pekee, ni`undefined`(hali madhubuti) au`global`(isiyo kali). Vitendaji vya mshale hurithi`this`kutoka kwa upeo wao wa kuambatanisha - hii ndiyo sababu vinapendelewa kwa mirudisho ya simu. Tumia`.bind()`kuweka kwa uwazi`this`.
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

### Q3: Kitanzi cha tukio ni nini, na async/kungoja hufanya kazi vipi haswa?
**J:** JavaScript ina nyuzi moja na kitanzi cha tukio ambacho huchakata foleni. Rafu ya simu hutekeleza msimbo unaosawazishwa. Wakati ni tupu, kitanzi cha tukio huchagua kazi inayofuata kutoka kwa foleni ya microtask (Ahadi) au foleni ya makrotask (setTimeout, I/O). `async/await`ni sukari ya kisintaksia juu ya Ahadi —`await`husitisha utendakazi wa kusawazisha na kuanza tena Ahadi inapotatuliwa, bila kuzuia mazungumzo.
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

### Q4: Ninapaswa kushughulikia vipi makosa katika JavaScript ya kisasa?
**J:** Tumia`try/catch`kwa msimbo ulandanishi na`.catch()`au`try/catch`na`async/await`kwa msimbo usiolandanishwa. Shikilia kukataliwa kwa Ahadi kila wakati - kukataliwa bila kushughulikiwa kunaharibu Node.js. Unda madarasa maalum ya makosa kwa hitilafu maalum za kikoa. Tumia kidhibiti makosa cha kimataifa kama wavu wa usalama.
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

### Q5: Je, ni lini ninapaswa kutumia`Map`/`Set`badala ya vitu/safu wazi?
**A:** Tumia`Map`wakati funguo si kamba, unapohitaji marudio ya agizo la kuingiza, unapohitaji`.size`, au unapoongeza/kuondoa maingizo mara kwa mara (utendaji bora kuliko vitu). Tumia`Set`kwa mikusanyo ya kipekee yenye utafutaji wa O(1) — haraka zaidi kuliko`array.includes()`kwa seti kubwa za data. Tumia vitu wazi kwa data rahisi ya JSON-serializable na ramani ndogo za thamani ya vitufe zilizo na vitufe vya kamba.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tekeleza Kazi ya Kutatua
**Taarifa ya Tatizo:** Tekeleza matumizi ya`debounce`ambayo huchelewesha kutuma chaguo za kukokotoa hadi baada ya muda maalum wa kusubiri kukamilika tangu mara ya mwisho ilipoitwa. Saidia ombi linaloongoza na linalofuata.
**Hatua ya 1 - Elewa Tatizo:**
Chaguo za kukokotoa zilizokatishwa hupuuza simu zinazofuatana za haraka na huwaka tu baada ya simu kusimama kwa muda wa kusubiri. "Makali ya mbele" inamaanisha moto mara moja kwenye simu ya kwanza. "Makali yanayofuata" inamaanisha moto baada ya muda wa kusubiri. Tunahitaji kushughulikia hali zote mbili na pia kusaidia kughairi.
**Hatua ya 2 — Tambua Mbinu:**
- Hifadhi kitambulisho cha saa wakati wa kufungwa.
- Kwa kila simu: futa kipima saa kilichopo, kisha weka`setTimeout`mpya.
- Kwa makali ya mbele: piga simu mara moja ikiwa hakuna kipima saa kinachotumika.
- Rudisha kitendakazi kilichotenguliwa kwa mbinu ya `.cancel()`.
- Hifadhi muktadha na hoja za`this`kwa kutumia vitendaji vya mshale au`.apply()`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Kufungwa huhifadhi hali katika simu zote bila kuchafua wigo wa kimataifa.
-`clearTimeout`kabla ya`setTimeout`huhakikisha tu simu ya mwisho inaanzisha utekelezaji.
-`.cancel()`ni muhimu kwa usafishaji (k.m., kijenzi shushwe kwenye React).
- Kesi ya ukingo: ikiwa`wait`ni 0, chaguo la kukokotoa litawaka kwenye tiki ya kitanzi cha tukio linalofuata - ni muhimu kwa kuunganisha masasisho ya DOM.
### Tatizo la 2: Tengeneza Kikomo cha Kiwango cha Ahadi
**Taarifa ya Tatizo:** Unda kikomo cha viwango kinachoruhusu maombi mengi ya N kwa kila dirisha la wakati. Inapaswa kurudisha Ahadi zinazosuluhisha wakati mpigaji simu anaruhusiwa kuendelea, na kupanga foleni maombi ya ziada.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji dirisha la kuteleza au lisilobadilika ambalo hufuatilia ni simu ngapi zimepigwa. Wakati kikomo kinapofikiwa, simu mpya zinapaswa kupangwa na kutatuliwa wakati slot inafunguliwa. Huu ndio muundo wa "ndoo ya ishara".
**Hatua ya 2 — Tambua Mbinu:**
- Fuatilia mihuri ya muda ya simu za hivi majuzi katika safu.
- Kwa kila simu: ondoa mihuri ya muda ya zamani kuliko dirisha, angalia ikiwa hesabu <kikomo.
- Ikiwa chini ya kikomo: suluhisha mara moja.
- Ikiwa iko kikomo: hesabu wakati muhuri wa muda wa zamani zaidi unaisha, weka`setTimeout`, kisha suluhisha.
- Tumia foleni (safu ya kazi za kutatua) kwa wapigaji wanaosubiri.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Mbinu ya dirisha la kuteleza ni nzuri zaidi kuliko madirisha yaliyowekwa (hakuna kupasuka kwenye mipaka ya dirisha).
- Uchakataji wa foleni ni FIFO - wapigaji simu wanahudumiwa kwa mpangilio.
- Kwa uzalishaji: ongeza usaidizi wa`AbortController`ili wapigaji waweze kughairi kusubiri.
- Utendaji:`_cleanOldTimestamps`ni O(n) kwa kila simu lakini n inafungwa na`maxCalls`.
### Tatizo la 3: Tekeleza Kazi ya Ulinganifu wa Kina
**Taarifa ya Tatizo:** Andika chaguo la kukokotoa ambalo huiga kwa kina thamani yoyote ya JavaScript, kushughulikia vitu, safu, Tarehe, RegExps, Ramani, Seti, marejeleo ya duara na safu zilizochapwa.
**Hatua ya 1 - Elewa Tatizo:**
`JSON.parse(JSON.stringify(obj))`haifaulu kwenye:`undefined`, chaguo za kukokotoa, Alama, Tarehe (kuwa mifuatano), RegExps (kuwa vitu tupu), Ramani, Seti, marejeleo ya duara (kutupwa), na safu zilizochapwa. Tunahitaji suluhisho la kujirudia ambalo hufuatilia vitu vilivyotembelewa.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`Map`kufuatilia vitu ambavyo tayari vimeundwa (hushughulikia marejeleo ya duara).
- Hushughulikia kila aina haswa: Tarehe → Tarehe mpya, RegExp → RegExp mpya, Ramani → Ramani mpya iliyo na maingizo yaliyopangwa, Weka → Seti mpya yenye thamani zilizoundwa.
- Tumia`structuredClone()`kama njia mbadala ya kisasa iliyojengewa ndani (inapatikana katika vivinjari na Node.js 17+).
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Marejeleo ya mduara: Ramani ya`seen`hurejesha kisanii kilichoundwa tayari badala ya kujirudia kabisa.
- Vielezi vya mali:`Reflect.ownKeys`+`getOwnPropertyDescriptor`huhifadhi wapataji, wawekaji, na mali zisizohesabika.
- Mbadala wa kisasa:`structuredClone(value)`hushughulikia visa hivi kienyeji (isipokuwa vitendaji na nodi za DOM). Pendelea inapopatikana.
- Utendaji: kwa vitu rahisi,`JSON.parse(JSON.stringify(obj))`bado ni ya haraka zaidi. Tumia clone ya kina wakati tu unahitaji.
### Tatizo la 4: Tengeneza Emitter Rahisi ya Tukio
**Taarifa ya Tatizo:** Tekeleza darasa la mtoaji tukio ambalo linaauni mbinu za`on`,`off`,`emit`, na `once`. Wasikilizaji wanapaswa kuitwa kwa utaratibu wa usajili. `emit`inapaswa kupitisha hoja kwa wasikilizaji wote.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji mfumo wa baa/ndogo: sajili wasikilizaji kwa matukio yaliyotajwa, ondoa wasikilizaji mahususi, anzisha matukio kwa hoja, na usaidie wasikilizaji wa mara moja. Huu ni muundo wa Observer unaotumika sana katika Node.js.
**Hatua ya 2 — Tambua Mbinu:**
- Hifadhi wasikilizaji katika `Map<string, Array<Function>>`.
-`on`: msukuma msikilizaji kupanga.
-`off`: chuja msikilizaji maalum kutoka kwa safu.
-`emit`: rudia safu na upige simu kila msikilizaji kwa hoja zilizoenea.
-`once`: funika msikilizaji katika utendaji unaojiondoa baada ya simu ya kwanza.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Nakala ya`[...listeners]`katika`emit`huzuia matatizo wakati msikilizaji anapopigia simu`off`wakati wa marudio.
-`once`maduka`_original`ili wapiga simu waweze kuondoa kanga kupitia`off(event, originalFn)`.
- Sehemu za kibinafsi (`#listeners`) huzuia mabadiliko ya nje ya hali ya ndani.
- Kwa uzalishaji: ongeza onyo la`maxListeners`(kama Node.js), kushughulikia makosa kwa kila msikilizaji, na`prependListener`kwa kipaumbele.
---

## Muhtasari
JavaScript haiwezi kuepukika. Ndiyo lugha pekee inayotumika katika vivinjari vya wavuti, na kuifanya kuwa muhimu kwa maendeleo ya mbele. Kwa Node.js, inaenea hadi upande wa seva, na ikiwa na mifumo kama React Native na Electron, inafikia simu ya mkononi na kompyuta ya mezani. Mfumo ikolojia ndio mkubwa zaidi katika upangaji programu. Sifa za lugha zinajulikana na zinaweza kudhibitiwa - na TypeScript inashughulikia maswala ya kuandika. Kwa chochote kinachoendeshwa kwenye kivinjari, JavaScript sio chaguo bora tu - ni chaguo pekee.