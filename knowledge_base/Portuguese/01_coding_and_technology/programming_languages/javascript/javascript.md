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
# JavaScript
JavaScript é uma linguagem de programação dinâmica e interpretada criada por Brendan Eich em apenas 10 dias em 1995. Originalmente projetada para adicionar interatividade às páginas da web, tornou-se a linguagem de programação mais utilizada no mundo. O JavaScript é executado em todos os navegadores da web, em servidores via Node.js, em aplicativos de desktop (Electron), aplicativos móveis (React Native) e até mesmo em sistemas embarcados.
A linguagem é única porque é essencialmente a única opção para desenvolvimento web do lado do cliente – cada navegador oferece suporte nativo. Este monopólio, combinado com o surgimento do JavaScript full-stack (Node.js, Deno, Bun), torna-o indispensável.
---

## Por que o JavaScript é importante
- **A linguagem da web**: A única linguagem executada nativamente nos navegadores. Nenhuma alternativa para frontend.
- **Capacidade full-stack**: Mesma linguagem no frontend (React, Vue, Svelte) e backend (Node.js, Express, Fastify).
- **Ecossistema massivo**: o npm tem mais de 2 milhões de pacotes — o maior registro de software do mundo.
- **Versatilidade**: aplicativos Web, aplicativos móveis (React Native), aplicativos de desktop (Electron), IoT, funções sem servidor.
- **Baixa barreira de entrada**: funciona em qualquer navegador — não é necessária instalação para iniciar a codificação.
- **Assíncrono por design**: E/S sem bloqueio e orientada a eventos o torna excelente para aplicativos em tempo real.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Armadilhas da digitação dinâmica** | Nenhuma verificação de tipo em tempo de compilação; bugs surgem em tempo de execução | Use TypeScript (um superconjunto digitado de JavaScript) |
| **Complexidade de retorno de chamada** | Retornos de chamada aninhados podem se tornar ilegíveis ("inferno de retorno de chamada") | Use Promessas e async/await |
| **Semântica peculiar** | `==`vs`===`, ligação `this`, içamento, coerção de tipo | Aprenda as peculiaridades; use ESLint; prefira`const`/`let`em vez de`var`|
| **Encadeamento único** | Tarefas vinculadas à CPU bloqueiam o loop de eventos | Use Web Workers, threads de trabalho ou transfira para módulos nativos |
| **Qualidade do pacote** | a abertura do npm significa riscos inconsistentes de qualidade e segurança | Dependências de auditoria; use arquivos de bloqueio; prefira pacotes bem conservados |
---

## Fundamentos de sintaxe
### Variáveis ​​e tipos
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

### Funções
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

### Objetos e Classes
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

### Programação Assíncrona
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

## Sintaxe e padrões avançados
### Desestruturação e propagação/descanso (mergulho profundo)
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

### Proxies e Refletir
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

### Símbolos, Iteradores e Geradores
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

### Hierarquias de erros personalizadas
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

## Simultaneidade e paralelismo
JavaScript é de thread único com um loop de eventos. A simultaneidade é alcançada por meio de padrões assíncronos, Web Workers e (em Node.js) o módulo worker_threads.
### O ciclo de eventos
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

### Worker Threads (Node.js — tarefas vinculadas à CPU)
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

### Trabalhadores da Web (navegador)
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

### Padrões assíncronos
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

## Configuração do projeto e sistema de construção
### Estrutura do diretório do projeto
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

### Configuração de compilação — `package.json`
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

### Configuração de linting e formatação
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

### Pipeline de CI/CD — Ações do GitHub
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

## Teste
### Testando com Jest
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

### Testes de simulação e integração
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

## Interoperabilidade
### Complementos nativos com N-API (Node.js)
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

### Chamando bibliotecas C com ffi-napi
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

## Padrões de Projeto
### Padrão de Módulo (Encapsulamento)
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

### Observador/Padrão Emissor de Evento
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

### Padrão do Construtor
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

## Desempenho e otimização
### Ferramentas de criação de perfil
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

### Técnicas de otimização
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

## Implantação
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

### Implantação específica da plataforma
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

## O Ecossistema
### Estruturas de front-end
| Estrutura | Abordagem | Melhor para |
|----------|----------|----------|
| **Reaja** | DOM virtual baseado em componentes | SPAs de grande porte; maior ecossistema |
| **Vue** | Progressivo, baseado em modelo | Adoção gradual; ótima experiência de desenvolvedor |
| **Esbelto** | Tempo de compilação, sem DOM virtual | Pacotes menores, código mais simples |
| **Angular** | Estrutura completa, TypeScript primeiro | Aplicativos empresariais; estrutura opinativa |
| **Próximo.js** | Metaestrutura React (SSR/SSG) | Produção de aplicativos React com SEO |
### Back-end (Node.js)
| Estrutura | Finalidade |
|-----------|---------|
| **Expresso** | Estrutura web mínima e flexível (mais popular) |
| **Rápido** | Estrutura web de alto desempenho |
| **NestJS** | Arquitetura de nível empresarial com inspiração Angular |
| **Koa** | Alternativa Express leve e moderna |
| **Hono** | Ultrarrápido, multi-tempo de execução (Node, Deno, Bun, edge) |
### Tempos de execução
| Tempo de execução | Descrição |
|--------|-------------|
| **Node.js** | O tempo de execução JavaScript original do lado do servidor (mecanismo V8) |
| **Deno** | Seguro por padrão; suporte nativo a TypeScript; criado pelo autor original do Node |
| **Pão** | Tempo de execução, empacotador e gerenciador de pacotes tudo-em-um ultrarrápido |
### Ferramentas Essenciais
| Ferramenta | Finalidade |
|------|---------|
| **npm / fio / pnpm** | Gerenciadores de pacotes |
| **TypeScript** | Superconjunto digitado de JavaScript |
| **ESLint** | Linting de código |
| **Mais bonito** | Formatação de código |
| **Visite** | Ferramenta de construção rápida e servidor de desenvolvimento |
| **Webpack** | Empacotador de módulos (maduro, amplamente utilizado) |
| **Jest / Vitest** | Estruturas de teste |
---

## Quando usar JavaScript
| Cenário | Por que JavaScript | Melhor Alternativa |
|----------|---------------|-------------------|
| Front-end da Web | Única opção para UI baseada em navegador | — |
| Web full-stack | A mesma língua em todos os lugares | TypeScript para segurança de tipo |
| Aplicativos em tempo real (chat, jogos) | E/S sem bloqueio e orientada a eventos | — |
| Funções sem servidor | Rápido para escrever, implantar em qualquer lugar | Python, vá |
| Aplicativos móveis (React Native) | Compartilhe código com a web | Flutter, Swift/Kotlin nativo |
| Aplicativos de desktop (Elétron) | Plataforma cruzada com tecnologia web | C# (WPF), Tauri (Rust) |
| Computação com uso intensivo de CPU | Limitação de thread único | Python (NumPy), C++, Rust, WebAssembly |
| Programação de sistemas | Nível de abstração errado | C, C++, Ferrugem, Go |
---

## Perguntas e respostas sintéticas
### Q1: Qual é a diferença entre`var`,`let`e`const`e quando devo usar cada um?
**R:**`var`tem escopo de função e é elevado – evite-o no código moderno. `let`tem escopo de bloco e permite reatribuição. `const`tem escopo de bloco e evita a reatribuição (mas os objetos/matrizes aos quais ele faz referência ainda são mutáveis). Prática recomendada: padrão para`const`, use`let`somente quando precisar de reatribuição, nunca use`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2: Como`this`funciona em JavaScript e por que é tão confuso?
**R:**`this`é determinado por **como uma função é chamada**, e não por onde ela é definida. Em uma chamada de método,`this`é o objeto. Em uma chamada independente, é`undefined`(modo estrito) ou`global`(não estrito). As funções de seta herdam`this`de seu escopo envolvente - é por isso que são preferidas para retornos de chamada. Use`.bind()`para definir explicitamente`this`.
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

### Q3: O que é o loop de eventos e como o async/await realmente funciona?
**R:** JavaScript é de thread único com um loop de eventos que processa uma fila. A pilha de chamadas executa código síncrono. Quando está vazio, o loop de eventos escolhe a próxima tarefa da fila de microtarefas (Promises) ou da fila de macrotarefas (setTimeout, I/O). `async/await`é um açúcar sintático sobre Promises -`await`pausa a função assíncrona e retoma quando a Promise é resolvida, sem bloquear o thread.
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

### Q4: Como devo lidar com erros no JavaScript moderno?
**R:** Use`try/catch`para código síncrono e`.catch()`ou`try/catch`com`async/await`para código assíncrono. Sempre lide com rejeições de promessas – rejeições não tratadas travam o Node.js. Crie classes de erro personalizadas para erros específicos do domínio. Use um manipulador de erros global como rede de segurança.
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

### Q5: Quando devo usar`Map`/`Set`em vez de objetos/matrizes simples?
**R:** Use`Map`quando as chaves não forem strings, quando você precisar de iteração de pedido de inserção, quando precisar de`.size`ou quando você adicionar/remover entradas com frequência (melhor desempenho do que objetos). Use`Set`para coleções exclusivas com pesquisa O(1) — muito mais rápido que`array.includes()`para grandes conjuntos de dados. Use objetos simples para dados serializáveis ​​JSON simples e pequenos mapas de valores-chave com chaves de string.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Implementar uma função Debounce
**Declaração do problema:** Implemente um utilitário`debounce`que atrase a invocação de uma função até que um período de espera especificado tenha decorrido desde a última vez que ela foi chamada. Suporta invocação de borda inicial e final.
**Etapa 1 — Entenda o problema:**
Uma função debounce ignora chamadas sucessivas rápidas e só é acionada depois que as chamadas param durante o período de espera. "Vista de ataque" significa disparar imediatamente na primeira chamada. "Borda de fuga" significa incêndio após o período de espera. Precisamos lidar com os dois modos e também oferecer suporte ao cancelamento.
**Etapa 2 — Identifique a abordagem:**
- Armazene um ID de temporizador em um fechamento.
- Em cada chamada: limpe o cronômetro existente e defina um novo`setTimeout`.
- Para borda principal: ligue imediatamente se nenhum temporizador estiver ativo.
- Retorna uma função debounce com um método `.cancel()`.
- Preserve o contexto e os argumentos de`this`usando funções de seta ou`.apply()`.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- O fechamento preserva o estado nas chamadas sem poluir o escopo global.
-`clearTimeout`antes de`setTimeout`garante que apenas a última chamada acione a execução.
-`.cancel()`é importante para limpeza (por exemplo, desmontagem de componente no React).
- Caso extremo: se`wait`for 0, a função é acionada no próximo tique do loop de evento - útil para atualizações de DOM em lote.
### Problema 2: Construa um Limitador de Taxa Baseado em Promessas
**Declaração do problema:** Crie um limitador de taxa que permita no máximo N solicitações por intervalo de tempo. Ele deve retornar promessas que serão resolvidas quando o chamador tiver permissão para prosseguir e enfileirar solicitações em excesso.
**Etapa 1 — Entenda o problema:**
Precisamos de uma janela deslizante ou fixa que monitore quantas chamadas foram feitas. Quando o limite for atingido, novas chamadas deverão ser enfileiradas e resolvidas quando uma vaga for aberta. Este é o padrão "balde de tokens".
**Etapa 2 — Identifique a abordagem:**
- Acompanhe carimbos de data/hora de chamadas recentes em uma matriz.
- Em cada chamada: remova carimbos de data e hora mais antigos que a janela, verifique se contagem <limite.
- Se estiver abaixo do limite: resolva imediatamente.
- Se estiver no limite: calcule quando o carimbo de data/hora mais antigo expira, defina um`setTimeout`e resolva.
- Use uma fila (matriz de funções de resolução) para chamadores em espera.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- A abordagem da janela deslizante é mais justa do que as janelas fixas (sem ruptura nos limites da janela).
- O processamento da fila é FIFO – os chamadores são atendidos em ordem.
- Para produção: adicione suporte`AbortController`para que os chamadores possam cancelar a espera.
- Desempenho:`_cleanOldTimestamps`é O(n) por chamada, mas n é limitado por`maxCalls`.
### Problema 3: Implementar uma função de clone profundo
**Declaração do problema:** Escreva uma função que clone profundamente qualquer valor JavaScript, manipulando objetos, matrizes, datas, RegExps, mapas, conjuntos, referências circulares e matrizes digitadas.
**Etapa 1 — Entenda o problema:**
`JSON.parse(JSON.stringify(obj))`falha em:`undefined`, funções, símbolos, datas (tornam-se strings), RegExps (tornam-se objetos vazios), mapas, conjuntos, referências circulares (lançamentos) e matrizes digitadas. Precisamos de uma solução recursiva que rastreie os objetos visitados.
**Etapa 2 — Identifique a abordagem:**
- Use um`Map`para rastrear objetos já clonados (lida com referências circulares).
- Lide com cada tipo especialmente: Data → nova Data, RegExp → novo RegExp, Mapa → novo Mapa com entradas clonadas, Conjunto → novo Conjunto com valores clonados.
- Use`structuredClone()`como alternativa integrada moderna (disponível em navegadores e Node.js 17+).
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Referências circulares: o Mapa`seen`retorna o clone já criado em vez de recorrer infinitamente.
- Descritores de propriedades:`Reflect.ownKeys`+`getOwnPropertyDescriptor`preserva getters, setters e propriedades não enumeráveis.
- Alternativa moderna:`structuredClone(value)`lida nativamente com a maioria desses casos (exceto funções e nós DOM). Prefira quando disponível.
- Desempenho: para objetos simples,`JSON.parse(JSON.stringify(obj))`ainda é o mais rápido. Use o clone profundo somente quando realmente precisar dele.
### Problema 4: Construa um Emissor de Evento Simples
**Declaração do problema:** Implemente uma classe emissora de eventos que suporte os métodos`on`,`off`,`emit`e`once`. Os ouvintes deverão ser chamados por ordem de inscrição. `emit`deve passar argumentos para todos os ouvintes.
**Etapa 1 — Entenda o problema:**
Precisamos de um sistema pub/sub: registrar ouvintes para eventos nomeados, remover ouvintes específicos, acionar eventos com argumentos e oferecer suporte a ouvintes únicos. Este é o padrão Observer usado extensivamente em Node.js.
**Etapa 2 — Identifique a abordagem:**
- Armazene ouvintes em um`Map<string, Array<Function>>`.
- `on`: envia o ouvinte para o array.
- `off`: filtre o ouvinte específico do array.
- `emit`: itera o array e chama cada ouvinte com argumentos de propagação.
- `once`: envolve o ouvinte em uma função que se remove após a primeira chamada.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- A cópia`[...listeners]`em`emit`evita problemas quando um ouvinte chama`off`durante a iteração.
-`once`armazena`_original`para que os chamadores possam remover o wrapper por meio de`off(event, originalFn)`.
- Campos privados (`#listeners`) evitam mutação externa do estado interno.
- Para produção: adicione aviso`maxListeners`(como Node.js), tratamento de erros por ouvinte e`prependListener`para prioridade.
---

## Resumo
JavaScript é inevitável. É a única linguagem que roda em navegadores web, o que a torna essencial para o desenvolvimento frontend. Com o Node.js, ele se estende ao lado do servidor, e com frameworks como React Native e Electron, chega a dispositivos móveis e desktops. O ecossistema é o maior em programação. As peculiaridades da linguagem são bem conhecidas e gerenciáveis ​​– e o TypeScript aborda as questões de digitação. Para qualquer coisa que rode em um navegador, JavaScript não é apenas a melhor escolha – é a única escolha.