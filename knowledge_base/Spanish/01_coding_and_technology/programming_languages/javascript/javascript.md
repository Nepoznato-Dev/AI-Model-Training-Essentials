---
# Metadata
title: "JavaScript"
description: "Comprehensive reference for the JavaScript programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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
JavaScript es un lenguaje de programación interpretado dinámico creado por Brendan Eich en sólo 10 días en 1995. Originalmente diseñado para agregar interactividad a las páginas web, se ha convertido en el lenguaje de programación más utilizado en el mundo. JavaScript se ejecuta en todos los navegadores web, en servidores a través de Node.js, en aplicaciones de escritorio (Electron), aplicaciones móviles (React Native) e incluso sistemas integrados.
El lenguaje es único porque es esencialmente la única opción para el desarrollo web del lado del cliente: todos los navegadores lo admiten de forma nativa. Este monopolio, combinado con el auge del JavaScript completo (Node.js, Deno, Bun), lo hace indispensable.
---

## Por qué es importante JavaScript
- **El idioma de la web**: El único idioma que se ejecuta de forma nativa en los navegadores. No hay alternativa para la interfaz.
- **Capacidad de pila completa**: Mismo lenguaje en el frontend (React, Vue, Svelte) y el backend (Node.js, Express, Fastify).
- **Ecosistema masivo**: npm tiene más de 2 millones de paquetes, el registro de software más grande del mundo.
- **Versatilidad**: aplicaciones web, aplicaciones móviles (React Native), aplicaciones de escritorio (Electron), IoT, funciones sin servidor.
- **Baja barrera de entrada**: se ejecuta en cualquier navegador; no se necesita instalación para comenzar a codificar.
- **Asíncrono por diseño**: la E/S sin bloqueo y controlada por eventos lo hace excelente para aplicaciones en tiempo real.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Errores de la escritura dinámica** | Sin verificación de tipos en tiempo de compilación; errores aparecen en tiempo de ejecución | Utilice TypeScript (un superconjunto escrito de JavaScript) |
| **Complejidad de devolución de llamada** | Las devoluciones de llamadas anidadas pueden volverse ilegibles ("infierno de las devoluciones de llamadas") | Utilice promesas y async/await |
| **Semántica peculiar** | `==`vs `===`,`this`vinculación, elevación, coerción de tipo | Aprenda las peculiaridades; utilizar ESLint; prefiera`const`/`let`sobre`var`|
| **Un solo subproceso** | Las tareas vinculadas a la CPU bloquean el bucle de eventos | Utilice Web Workers, subprocesos de trabajo o descargue a módulos nativos |
| **Calidad del paquete** | la apertura de npm significa riesgos de calidad y seguridad inconsistentes | Dependencias de auditoría; utilizar archivos de bloqueo; prefieren paquetes bien mantenidos |
---

## Fundamentos de sintaxis
### Variables y tipos
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

### Funciones
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

### Objetos y clases
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

### Programación asíncrona
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

### Módulos
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

## Sintaxis y patrones avanzados
### Desestructuración y extensión/descanso (inmersión profunda)
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

### Proxys y Reflexión
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

### Símbolos, iteradores y generadores
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

### Jerarquías de errores personalizadas
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

## Concurrencia y paralelismo
JavaScript tiene un solo subproceso con un bucle de eventos. La simultaneidad se logra mediante patrones asincrónicos, Web Workers y (en Node.js) el módulo trabajador_threads.
### El bucle de eventos
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

### Subprocesos de trabajo (Node.js: tareas vinculadas a la CPU)
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

### Trabajadores web (navegador)
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

### Patrones asíncronos
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

## Configuración del proyecto y sistema de construcción
### Estructura del directorio del proyecto
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

### Configuración de compilación: `package.json`
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

### Configuración de linting y formato
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

### Canalización de CI/CD: Acciones de GitHub
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

## Pruebas
### Pruebas con Jest
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

### Pruebas de burla e integración
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

## Interoperabilidad
### Complementos nativos con N-API (Node.js)
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

### Asamblea web (Wasm)
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

### Llamar a bibliotecas C con ffi-napi
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

## Patrones de diseño
### Patrón de módulo (encapsulación)
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

### Patrón de observador/emisor de eventos
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

### Patrón de constructor
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
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

### Técnicas de optimización
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

## Implementación
### Archivo Docker
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

### Implementación específica de la plataforma
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

## El ecosistema
### Marcos de interfaz de usuario
| Marco | Enfoque | Mejor para |
|-----------|----------|----------|
| **Reaccionar** | DOM virtual basado en componentes | SPA de gran escala; ecosistema más grande |
| **Vista** | Progresivo, basado en plantillas | Adopción gradual; gran experiencia de desarrollador |
| **Esbelto** | Tiempo de compilación, sin DOM virtual | Paquetes más pequeños, código más simple |
| **Angulosos** | Marco completo, TypeScript primero | aplicaciones empresariales; estructura obstinada |
| **Siguiente.js** | Reaccionar metamarco (SSR/SSG) | Producción de aplicaciones React con SEO |
### Backend (Node.js)
| Marco | Propósito |
|-----------|------------------|
| **Expreso** | Marco web mínimo y flexible (el más popular) |
| **Acelerar** | Marco web de alto rendimiento |
| **NestJS** | Arquitectura de nivel empresarial inspirada en Angular |
| **Koa** | Alternativa Express ligera y moderna |
| **Hono** | Ultrarrápido, multiejecución (Node, Deno, Bun, edge) |
### Tiempos de ejecución
| Tiempo de ejecución | Descripción |
|---------|-------------|
| **Nodo.js** | El tiempo de ejecución original de JavaScript del lado del servidor (motor V8) |
| **Deno** | Seguro por defecto; soporte nativo de TypeScript; creado por el autor original de Node |
| **Bollo** | Administrador de paquetes, empaquetador y tiempo de ejecución todo en uno ultrarrápido |
### Herramientas esenciales
| Herramienta | Propósito |
|------|---------|
| **npm / hilo / pnpm** | Gestores de paquetes |
| **Mecanografiado** | Superconjunto escrito de JavaScript |
| **ESLint** | Eliminación de código |
| **Más bonita** | Formato de código |
| **Vita** | Herramienta de construcción rápida y servidor de desarrollo |
| **Paquete web** | Paquete de módulos (maduro, ampliamente utilizado) |
| **Broma / Vitest** | Marcos de prueba |
---

## Cuándo utilizar JavaScript
| Escenario | ¿Por qué JavaScript? Mejor alternativa |
|----------|---------------|-------------------|
| Interfaz web | Única opción para UI basada en navegador | — |
| Web de pila completa | Mismo idioma en todas partes | TypeScript para seguridad de tipos |
| Aplicaciones en tiempo real (chat, juegos) | E/S sin bloqueo y controladas por eventos | — |
| Funciones sin servidor | Rápido de escribir, implementar en cualquier lugar | Pitón, vamos |
| Aplicaciones móviles (React Native) | Compartir código con web | Flutter, Swift/Kotlin nativo |
| Aplicaciones de escritorio (Electron) | Multiplataforma con tecnología web | C# (WPF), Tauri (óxido) |
| Computación intensiva en CPU | Limitación de un solo subproceso | Python (NumPy), C++, Rust, WebAssembly |
| Programación de sistemas | Nivel de abstracción incorrecto | C, C++, óxido, listo |
---

## Preguntas y respuestas sintéticas
### P1: ¿Cuál es la diferencia entre `var`,`let`y`const`y cuándo debo usar cada uno?
**R:**`var`tiene un alcance funcional y elevado; evítelo en el código moderno. `let`tiene un alcance de bloque y permite la reasignación. `const`tiene un alcance de bloque y evita la reasignación (pero los objetos/matrices a las que hace referencia siguen siendo mutables). Mejores prácticas: use de forma predeterminada `const`, use`let`solo cuando necesite una reasignación, nunca use `var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### P2: ¿Cómo funciona`this`en JavaScript y por qué es tan confuso?
**R:**`this`está determinado por **cómo se llama una función**, no por dónde está definida. En una llamada a un método,`this`es el objeto. En una llamada independiente, es`undefined`(modo estricto) o`global`(no estricto). Las funciones de flecha heredan`this`de su alcance circundante; es por eso que se prefieren para las devoluciones de llamada. Utilice`.bind()`para configurar explícitamente `this`.
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

### P3: ¿Qué es el bucle de eventos y cómo funciona realmente async/await?
**R:** JavaScript tiene un solo subproceso con un bucle de eventos que procesa una cola. La pila de llamadas ejecuta código sincrónico. Cuando está vacío, el bucle de eventos selecciona la siguiente tarea de la cola de microtask (Promises) o de la cola de macrotask (setTimeout, I/O). `async/await`es azúcar sintáctico sobre Promesas:`await`pausa la función asíncrona y la reanuda cuando la Promesa se resuelve, sin bloquear el hilo.
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

### P4: ¿Cómo debo manejar los errores en JavaScript moderno?
**R:** Utilice`try/catch`para código sincrónico y`.catch()`o`try/catch`con`async/await`para código asincrónico. Maneje siempre los rechazos de promesas: los rechazos no controlados bloquean Node.js. Cree clases de error personalizadas para errores específicos del dominio. Utilice un controlador de errores global como red de seguridad.
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

### P5: ¿Cuándo debo usar`Map`/`Set`en lugar de objetos/matrices simples?
**R:** Utilice`Map`cuando las claves no sean cadenas, cuando necesite una iteración del orden de inserción, cuando necesite`.size`o cuando agregue o elimine entradas con frecuencia (mejor rendimiento que los objetos). Utilice`Set`para colecciones únicas con búsqueda O(1), mucho más rápido que`array.includes()`para conjuntos de datos grandes. Utilice objetos simples para datos serializables JSON simples y pequeños mapas clave-valor con claves de cadena.
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

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: implementar una función antirrebote
**Declaración del problema:** Implemente una utilidad`debounce`que retrase la invocación de una función hasta que haya transcurrido un período de espera específico desde la última vez que se llamó. Admite invocación de borde inicial y final.
**Paso 1: comprenda el problema:**
Una función antirrebote ignora las llamadas sucesivas rápidas y solo se activa después de que las llamadas se detienen durante el tiempo de espera. "Borde de ataque" significa disparar inmediatamente a la primera llamada. "Borde de salida" significa fuego después del período de espera. Necesitamos manejar ambos modos y también admitir la cancelación.
**Paso 2: Identifique el enfoque:**
- Almacenar un ID de temporizador en un cierre.
- En cada llamada: borre el temporizador existente y luego configure un nuevo `setTimeout`.
- Para borde de ataque: llame inmediatamente si no hay ningún temporizador activo.
- Devuelve una función antirrebote con un método `.cancel()`.
- Preservar el contexto y los argumentos de`this`usando funciones de flecha o `.apply()`.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- El cierre preserva el estado en todas las llamadas sin contaminar el alcance global.
-`clearTimeout`antes de`setTimeout`garantiza que solo la última llamada desencadene la ejecución.
-`.cancel()`es importante para la limpieza (por ejemplo, desmontaje de componentes en React).
- Caso extremo: si`wait`es 0, la función se activa en el siguiente tic del bucle de eventos, lo que resulta útil para realizar actualizaciones de DOM por lotes.
### Problema 2: crear un limitador de tarifas basado en promesas
**Declaración del problema:** Cree un limitador de velocidad que permita como máximo N solicitudes por ventana de tiempo. Debería devolver promesas que resuelvan cuándo se le permite continuar a la persona que llama y poner en cola el exceso de solicitudes.
**Paso 1: comprenda el problema:**
Necesitamos una ventana corrediza o fija que rastree cuántas llamadas se han realizado. Cuando se alcanza el límite, las nuevas llamadas deben ponerse en cola y resolverse cuando se abre un espacio. Este es el patrón del "cubo de fichas".
**Paso 2: Identifique el enfoque:**
- Seguimiento de marcas de tiempo de llamadas recientes en una matriz.
- En cada llamada: elimine las marcas de tiempo anteriores a la ventana, verifique si el recuento <límite.
- Si está por debajo del límite: resolver inmediatamente.
- Si está en el límite: calcule cuándo caduca la marca de tiempo más antigua, establezca un`setTimeout`y luego resuelva.
- Utilice una cola (conjunto de funciones de resolución) para las personas que llaman en espera.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- El enfoque de la ventana corredera es más justo que el de las ventanas fijas (sin roturas en los límites de las ventanas).
- El procesamiento de cola es FIFO: las personas que llaman son atendidas en orden.
- Para producción: agregue soporte`AbortController`para que las personas que llaman puedan cancelar la espera.
- Rendimiento:`_cleanOldTimestamps`es O(n) por llamada pero n está limitado por `maxCalls`.
### Problema 3: implementar una función de clonación profunda
**Declaración del problema:** Escriba una función que clone profundamente cualquier valor de JavaScript, manejando objetos, matrices, fechas, expresiones regulares, mapas, conjuntos, referencias circulares y matrices escritas.
**Paso 1: comprenda el problema:**
`JSON.parse(JSON.stringify(obj))`falla en: `undefined`, funciones, símbolos, fechas (se convierten en cadenas), expresiones regulares (se convierten en objetos vacíos), mapas, conjuntos, referencias circulares (lanzamientos) y matrices escritas. Necesitamos una solución recursiva que rastree los objetos visitados.
**Paso 2: Identifique el enfoque:**
- Utilice un`Map`para rastrear objetos ya clonados (maneja referencias circulares).
- Manejar cada tipo de forma especial: Fecha → nueva fecha, RegExp → nueva RegExp, Mapa → nuevo mapa con entradas clonadas, Conjunto → nuevo conjunto con valores clonados.
- Utilice`structuredClone()`como la alternativa moderna integrada (disponible en navegadores y Node.js 17+).
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Referencias circulares: el mapa`seen`devuelve el clon ya creado en lugar de repetirse infinitamente.
- Descriptores de propiedades:`Reflect.ownKeys`+`getOwnPropertyDescriptor`conserva captadores, definidores y propiedades no enumerables.
- Alternativa moderna:`structuredClone(value)`maneja la mayoría de estos casos de forma nativa (excepto funciones y nodos DOM). Prefiere cuando esté disponible.
- Rendimiento: para objetos simples,`JSON.parse(JSON.stringify(obj))`sigue siendo el más rápido. Utilice la clonación profunda sólo cuando realmente la necesite.
### Problema 4: construir un emisor de eventos simple
**Declaración del problema:** Implemente una clase de emisor de eventos que admita los métodos `on`, `off`,`emit`y `once`. Los oyentes deben ser llamados por orden de registro. `emit`debería pasar argumentos a todos los oyentes.
**Paso 1: comprenda el problema:**
Necesitamos un sistema de publicación/subscripción: registre oyentes para eventos con nombre, elimine oyentes específicos, active eventos con argumentos y admita oyentes únicos. Este es el patrón Observer que se usa ampliamente en Node.js.
**Paso 2: Identifique el enfoque:**
- Almacenar oyentes en un `Map<string, Array<Function>>`.
- `on`: envía el oyente a la matriz.
- `off`: filtra el oyente específico de la matriz.
- `emit`: itera la matriz y llama a cada oyente con argumentos extendidos.
- `once`: envuelve el oyente en una función que se elimina después de la primera llamada.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- La copia`[...listeners]`en`emit`evita problemas cuando un oyente llama a`off`durante la iteración.
-`once`almacena`_original`para que las personas que llaman puedan eliminar el contenedor a través de `off(event, originalFn)`.
- Los campos privados (`#listeners`) evitan la mutación externa del estado interno.
- Para producción: agregue la advertencia`maxListeners`(como Node.js), manejo de errores por oyente y`prependListener`como prioridad.
---

## Resumen
JavaScript es ineludible. Es el único lenguaje que se ejecuta en los navegadores web, lo que lo hace esencial para el desarrollo frontend. Con Node.js, se extiende al lado del servidor y con marcos como React Native y Electron, llega a dispositivos móviles y de escritorio. El ecosistema es el más grande en programación. Las peculiaridades del lenguaje son bien conocidas y manejables, y TypeScript aborda los problemas de mecanografía. Para cualquier cosa que se ejecute en un navegador, JavaScript no es sólo la mejor opción: es la única opción.