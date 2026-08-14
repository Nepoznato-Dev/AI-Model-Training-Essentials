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
JavaScript 是一種動態的解釋性程式語言，由 Brendan Eich 在 1995 年僅用 10 天就創建了。它最初旨在為網頁添加互動性，現已發展成為世界上使用最廣泛的程式語言。 JavaScript 在每個 Web 瀏覽器中運行，透過 Node.js 在伺服器上運行，在桌面應用程式 (Electron)、行動應用程式 (React Native) 甚至嵌入式系統中運行。
語言的獨特之處在於它本質上是客戶端 Web 開發的唯一選擇——每個瀏覽器都原生支援它。這種壟斷，再加上全端 JavaScript（Node.js、Deno、Bun）的興起，使其變得不可或缺。
---

## 為什麼 JavaScript 很重要
- **網頁語言**：唯一在瀏覽器中本地運行的語言。前端別無選擇。
- **全端功能**：前端（React、Vue、Svelte）和後端（Node.js、Express、Fastify）使用相同的語言。
- **龐大的生態系統**：npm 擁有超過 200 萬個軟體包——世界上最大的軟體註冊表。
- **多功能性**：Web 應用程式、行動應用程式 (React Native)、桌面應用程式 (Electron)、物聯網、無伺服器功能。
- **進入門檻低**：在任何瀏覽器中運行 - 無需安裝即可開始編碼。
- **設計非同步**：事件驅動、非阻塞 I/O 使其非常適合即時應用程式。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **動態類型陷阱** |沒有編譯時類型檢查；運行時出現錯誤|使用 TypeScript（JavaScript 的類型化超集）|
| **回調複雜度** |嵌套回呼可能變得不可讀（“回調地獄”）|使用 Promise 和 async/await |
| **古怪的語意** |`==`與`===`、`this`綁定、提升、類型強制 |了解怪癖；使用 ESLint；與`var`相比，更喜歡`const`/`let`|
| **單執行緒** | CPU 密集型任務會阻塞事件循環 |使用 Web Workers、工作執行緒或卸載到本機模組 |
| **包裝品質** | npm 的開放性意味著品質不一致和安全風險 |審核依賴性；使用鎖定檔案；偏好維護良好的套件 |
---

## 文法基礎知識
### 變數和類型
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

### 函數
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

### 物件和類別
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

### 非同步編程
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

### 模組
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

## 進階語法和模式
### 解構與傳播/休息（深入探討）
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

### 代理和反映
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

### 符號、迭代器和生成器
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

### 自訂錯誤層次結構
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

## 並發與平行
JavaScript 是帶有事件循環的單線程。並發性是透過非同步模式、Web Workers 和（在 Node.js 中）worker_threads 模組實現的。
### 事件循環
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

### 工作執行緒（Node.js — CPU 密集型任務）
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

### Web Worker（瀏覽器）
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

### 非同步模式
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

## 專案配置與建置系統
### 專案目錄結構
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

### 建置配置 — `package.json`
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

### Linting 和格式配置
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

### CI/CD 管道 — GitHub Actions
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

## 測試
### 使用 Jest 進行測試
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

### 模擬和整合測試
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

## 互通性
### 具有 N-API 的本機外掛程式 (Node.js)
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

### 使用 ffi-napi 呼叫 C 函式庫
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

## 設計模式
### 模組模式（封裝）
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

### 觀察者/事件發射器模式
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

### 建構器模式
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

## 效能與最佳化
### 分析工具
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

### 優化技術
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

## 部署
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

### 特定於平台的部署
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

## 生態系統
### 前端框架
|框架|方法|最適合 |
|------------|----------|----------|
| **反應** |基於組件的虛擬 DOM |大型SPA；最大的生態系|
| **Vue** |漸進式、基於模板 |逐步採用；優秀的開發者體驗 |
| **苗條** |編譯時，無虛擬 DOM |更小的包，更簡單的程式碼 |
| **角度** |完整框架，TypeScript 優先 |企業應用程式；固執己見的結構|
| **Next.js** | React 元框架 (SSR/SSG) |帶有 SEO 的生產 React 應用程式 |
### 後端 (Node.js)
|框架|目的|
|------------|---------|
| **快遞** |最小、靈活的 Web 框架（最受歡迎）|
| **快點** |高效能Web框架|
| **NestJS** |企業級、受 Angular 啟發的架構 |
| **相思木** |輕量級、現代的 Express 替代品 |
| **榮譽** |超快、多運行時（Node、Deno、Bun、edge）|
### 運行時
|運行時|描述 |
|---------|-------------|
| **Node.js** |原始伺服器端 JavaScript 執行階段（V8 引擎）|
| **德諾** |預設安全；原生 TypeScript 支援；由 Node 原作者建立 |
| **髮髻** |超快一體化運行時間、捆綁器和套件管理器 |
### 基本工具
|工具|目的|
|------|---------|
| **npm / 紗線 / pnpm** |套件管理器 |
| **打字稿** | JavaScript 的類型化超集 |
| **ESLint** |程式碼檢查 |
| **更漂亮** |程式碼格式化 |
| **投票** |快速建立工具和開發伺服器|
| **Webpack** |模組捆綁器（成熟、廣泛使用）|
| **開玩笑/維斯特** |測試框架|
---

## 何時使用 JavaScript
|場景|為什麼選擇 JavaScript |更好的選擇|
|----------|--------------|--------------------|
|網頁前端 |基於瀏覽器的 UI 的唯一選項 | — |
|全端網路|到處都是同一種語言 |用於型別安全的 TypeScript |
|即時應用程式（聊天、遊戲）|事件驅動、非阻塞 I/O | — |
|無伺服器功能 |快速編寫，隨處部署 | Python、Go |
|行動應用程式（React Native）|與網路共用程式碼 | Flutter，原生 Swift/Kotlin |
|桌面應用程式（Electron）|跨平台網路技術 | C# (WPF)、Tauri (Rust) |
| CPU 密集型運算 |單執行緒限制 | Python (NumPy)、C++、Rust、WebAssembly |
|系統程式設計|錯誤的抽象層次 | C、C++、Rust、Go |
---

## 綜合問答
### Q1：`var`、`let`和`const`之間有什麼區別，什麼時候應該使用它們？
**A:**`var`是函數作用域和提升的 - 在現代程式碼中避免它。 `let`具有區塊作用域並允許重新指派。 `const`是區塊範圍的並防止重新分配（但它引用的物件/陣列仍然是可變的）。最佳實務：預設為`const`，僅在需要重新分配時使用`let`，切勿使用`var`。
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2：`this` 在 JavaScript 中如何運作，為什麼如此令人困惑？
**答：**`this`由**如何呼叫函數**決定，而不是由其定義位置決定。在方法呼叫中，`this` 是物件。在獨立呼叫中，它是 `undefined`（嚴格模式）或 `global`（非嚴格模式）。箭頭函數從其封閉範圍繼承`this`— 這就是為什麼它們是回調的首選。使用`.bind()`明確設定`this`。
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

### Q3：什麼是事件循環，async/await 實際上如何運作？
**答：** JavaScript 是單線程的，帶有處理隊列的事件循環。呼叫堆疊執行同步程式碼。當它為空時，事件循環會從微任務佇列（Promises）或巨集任務佇列（setTimeout，I/O）中選擇下一個任務。 `async/await`是 Promise 的語法糖 —`await`暫停非同步函數，並在 Promise 解析時恢復，而不會阻塞線程。
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

### Q4：我該如何處理現代 JavaScript 中的錯誤？
**A:** 對於同步程式碼使用 `try/catch`，對於非同步程式碼使用`.catch()`或`try/catch`與 `async/await`。始終處理 Promise 拒絕——未處理的拒絕會導致 Node.js 崩潰。為特定於網域的錯誤建立自訂錯誤類別。使用全域錯誤處理程序作為安全網。
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

### Q5：什麼時候應該使用`Map`/`Set`而不是普通物件/陣列？
**A:** 當鍵不是字串時，當您需要插入順序迭代時，當您需要`.size`時，或當您頻繁新增/刪除條目時（比物件更好的效能），請使用`Map`。使用`Set`進行 O(1) 尋找的唯一集合 — 比大型資料集的`array.includes()`快得多。將普通物件用於簡單的 JSON 可序列化資料和帶有字串鍵的小型鍵值映射。
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

## 解決問題的思路
### 問題 1：實現去抖動功能
**問題陳述：** 實作一個`debounce`實用程序，該實用程式延遲呼叫函數，直到自上次呼叫以來經過指定的等待時間後。支援前緣和後緣調用。
**第 1 步 — 了解問題：**
去抖函數會忽略快速的連續調用，並且僅在調用停止等待一段時間後觸發。 「前沿」是指在第一次呼叫後立即開火。 「後緣」是指在等待期之後發生火災。我們需要處理這兩種模式並支援取消。
**第 2 步 — 確定方法：**
- 將計時器 ID 儲存在閉包中。
- 每次呼叫時：清除現有計時器，然後設定新的`setTimeout`。
- 對於前緣：如果沒有定時器處於活動狀態，則立即呼叫。
- 使用`.cancel()`方法傳回去抖函數。
- 使用箭頭函數或`.apply()`保留`this`上下文和參數。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 閉包保留呼叫之間的狀態，而不會污染全域範圍。
-`setTimeout`之前的`clearTimeout`確保只有最後一個呼叫才會觸發執行。
-`.cancel()`對於清理很重要（例如，React 中的元件卸載）。
- 邊緣情況：如果`wait`為 0，則函數在下一個事件循環標記時觸發 - 對於批次 DOM 更新非常有用。
### 問題 2：建立基於 Promise 的速率限制器
**問題陳述：** 建立一個速率限制器，每個時間視窗最多允許 N 個請求。它應該會傳回在允許呼叫者繼續操作時解析的 Promise，並對多餘的請求進行排隊。
**第 1 步 — 了解問題：**
我們需要一個滑動或固定視窗來追蹤已撥打的電話數量。當達到限制時，新的呼叫應該排隊並在空位打開時解決。這就是「令牌桶」模式。
**第 2 步 — 確定方法：**
- 追蹤數組中最近調用的時間戳記。
- 每次呼叫時：刪除早於視窗的時間戳，檢查計數是否<限制。
- 如果低於限制：立即解決。
- 如果達到限制：計算最舊的時間戳何時到期，設定`setTimeout`，然後解析。
- 使用佇列（解析函數陣列）來等待呼叫者。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 滑動視窗方法比固定視窗更公平（視窗邊界處沒有突發）。
- 佇列處理採用先進先出 (FIFO) 方式 — 依序為呼叫者提供服務。
- 對於生產：新增`AbortController`支持，以便呼叫者可以取消等待。
- 效能：`_cleanOldTimestamps`每次呼叫的複雜度為 O(n)，但 n 受`maxCalls`限制。
### 問題3：實現深度克隆功能
**問題陳述：** 寫一個深度複製任何 JavaScript 值的函數，處理物件、陣列、日期、正規表示式、映射、集合、循環參考和類型化陣列。
**第 1 步 — 了解問題：**
`JSON.parse(JSON.stringify(obj))`失敗：`undefined`、函數、符號、日期（成為字串）、正規表示式（成為空物件）、映射、集合、循環引用（拋出）和類型化陣列。我們需要一個遞歸解決方案來追蹤存取的物件。
**第 2 步 — 確定方法：**
- 使用`Map`跟踪已克隆的对象（处理循环引用）。
- 特別處理每種類型：日期→新日期、正規表示式→新正規表示式、映射→帶有克隆條目的新映射、集合→帶有克隆值的新集合。
- 使用`structuredClone()`作为现代内置替代方案（在浏览器和 Node.js 17+ 中可用）。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 循環引用：`seen` 映射傳回已建立的克隆，而不是無限遞歸。
- 屬性描述子：`Reflect.ownKeys` +`getOwnPropertyDescriptor`保留 getter、setter 和不可枚舉屬性。
- 現代替代方案：`structuredClone(value)` 原生處理大多數此類情況（函數和 DOM 節點除外）。當可用時更喜歡它。
- 效能：對於簡單對象，`JSON.parse(JSON.stringify(obj))` 仍然是最快的。僅當您確實需要時才使用深度克隆。
### 問題 4：建造一個簡單的事件發射器
**問題陳述：** 實作一個支援`on`、`off`、`emit`和`once`方法的事件發射器類別。應依登記順序召集聽眾。 `emit`應將參數傳遞給所有偵聽器。
**第 1 步 — 了解問題：**
我們需要一個發布/訂閱系統：為命名事件註冊偵聽器，刪除特定偵聽器，使用參數觸發事件，並支援一次性偵聽器。這是 Node.js 中廣泛使用的觀察者模式。
**第 2 步 — 確定方法：**
- 將偵聽器儲存在`Map<string, Array<Function>>`中。
-`on`：將監聽器推送到陣列。
-`off`：從陣列中過濾掉特定的監聽器。
-`emit`：迭代陣列並使用擴充參數呼叫每個偵聽器。
-`once`：將偵聽器包裝在函數中，該函數在第一次呼叫後會自行刪除。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
-`emit`中的`[...listeners]`副本可防止偵聽器在迭代期間呼叫`off`時出現問題。
-`once`儲存`_original`，以便呼叫者可以透過`off(event, originalFn)`刪除包裝器。
- 私有欄位（`#listeners`）防止內部狀態的外部突變。
- 對於生產：新增`maxListeners`警告（如 Node.js）、每個偵聽器的錯誤處理以及`prependListener`優先權。
---

＃＃ 概括
JavaScript 是不可避免的。它是唯一在網頁瀏覽器中運行的語言，這使得它對於前端開發至關重要。透過 Node.js，它可以擴展到伺服器端，而透過 React Native 和 Electron 等框架，它可以擴展到行動和桌面。生態系統是程式設計領域最大的。該語言的怪癖眾所周知且易於管理——TypeScript 解決了打字問題。對於在瀏覽器中運行的任何東西，JavaScript 不僅是最好的選擇，也是唯一的選擇。