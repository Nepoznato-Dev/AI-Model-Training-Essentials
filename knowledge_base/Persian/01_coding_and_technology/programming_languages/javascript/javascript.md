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
# جاوا اسکریپت
جاوا اسکریپت یک زبان برنامه نویسی پویا و تفسیر شده است که توسط Brendan Eich تنها در 10 روز در سال 1995 ایجاد شد. این زبان که در اصل برای افزودن تعامل به صفحات وب طراحی شده بود، به پرکاربردترین زبان برنامه نویسی در جهان تبدیل شده است. جاوا اسکریپت در هر مرورگر وب، روی سرورها از طریق Node.js، در برنامه های دسکتاپ (الکترون)، برنامه های موبایل (React Native) و حتی سیستم های جاسازی شده اجرا می شود.
این زبان از این نظر منحصر به فرد است که اساساً تنها گزینه برای توسعه وب سمت مشتری است - هر مرورگر به طور بومی از آن پشتیبانی می کند. این انحصار، همراه با ظهور جاوا اسکریپت تمام پشته (Node.js، Deno، Bun)، آن را ضروری می کند.
---

## چرا جاوا اسکریپت مهم است
- **زبان وب**: تنها زبانی که به صورت بومی در مرورگرها اجرا می شود. جایگزینی برای frontend وجود ندارد.
- **قابلیت فول پشته**: زبان یکسان در فرانت اند (React، Vue، Svelte) و باطن (Node.js، Express، Fastify).
- **اکوسیستم عظیم**: npm دارای بیش از 2 میلیون بسته است - بزرگترین رجیستری نرم افزار در جهان.
- **تطبیق پذیری**: برنامه های وب، برنامه های تلفن همراه (React Native)، برنامه های دسکتاپ (الکترون)، اینترنت اشیا، عملکردهای بدون سرور.
- ** مانع ورود کم **: در هر مرورگری اجرا می شود - برای شروع کدنویسی نیازی به نصب نیست.
- **ناهمزمان بر اساس طراحی**: I/O مبتنی بر رویداد، بدون مسدود کردن، آن را برای برنامه های بلادرنگ عالی می کند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **مشکلات تایپ پویا** | بدون بررسی نوع زمان کامپایل. سطح اشکالات در زمان اجرا | از TypeScript (یک ابر مجموعه تایپ شده جاوا اسکریپت) |
| **پیچیدگی پاسخ به تماس** | تماس‌های تودرتو می‌توانند ناخوانا شوند ("جهنم پاسخ به تماس") | از Promises و async/wait | استفاده کنید
| **معناشناسی عجیب و غریب** | `==`vs`===`,`this`اتصال، بالا بردن، نوع اجبار | چیزهای عجیب و غریب را بیاموزید؛ از ESLint استفاده کنید. ترجیح دادن`const`/`let`بر`var`|
| **تک نخ** | وظایف محدود به CPU حلقه رویداد | از Web Workers، worker thread ها یا بارگذاری به ماژول های بومی استفاده کنید |
| **کیفیت بسته** | باز بودن npm به معنای ناسازگاری کیفیت و خطرات امنیتی است | وابستگی حسابرسی؛ استفاده از فایل های قفل؛ ترجیح می دهند بسته های به خوبی نگهداری شده |
---

## اصول نحو
### متغیرها و انواع
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

### توابع
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

### اشیاء و کلاس ها
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

### برنامه نویسی همگام
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

### ماژول ها
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

## نحو و الگوهای پیشرفته
### تخریب و گسترش/استراحت (شیرجه عمیق)
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

### پراکسی و Reflect
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

### نمادها، تکرار کننده ها و مولدها
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

### سلسله مراتب خطای سفارشی
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

## همزمانی و موازی
جاوا اسکریپت تک رشته ای با یک حلقه رویداد است. همزمانی از طریق الگوهای ناهمزمان، Web Workers و (در Node.js) ماژول worker_threads به دست می آید.
### حلقه رویداد
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

### Worker Threads (Node.js - وظایف محدود به CPU)
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

### کارگران وب (مرورگر)
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

### الگوهای همگام
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

## پیکربندی پروژه و سیستم ساخت
### ساختار فهرست پروژه
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

### پیکربندی ساخت — `package.json`
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

### لینتینگ و پیکربندی قالب بندی
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

### خط لوله CI/CD — اقدامات GitHub
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

## تست
### تست با Jest
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

### تست های تمسخر و ادغام
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

## قابلیت همکاری
### افزونه های بومی با N-API (Node.js)
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

### تماس با کتابخانه های C با ffi-napi
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

## الگوهای طراحی
### الگوی ماژول (کپسولاسیون)
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

### الگوی ناظر / انتشار دهنده رویداد
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

### الگوی سازنده
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### تکنیک های بهینه سازی
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

## استقرار
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

### استقرار ویژه پلتفرم
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

## اکوسیستم
### فریم ورک های فرانت اند
| چارچوب | رویکرد | بهترین برای |
|-----------|----------|----------|
| **واکنش** | DOM مجازی مبتنی بر مؤلفه | آبگرم در مقیاس بزرگ؛ بزرگترین اکوسیستم |
| **Vue** | پیشرو، مبتنی بر الگو | پذیرش تدریجی؛ تجربه توسعه دهنده عالی |
| **Svelte** | زمان کامپایل، بدون DOM مجازی | بسته های کوچکتر، کد ساده تر |
| **زاویه** | چارچوب کامل، TypeScript-first | برنامه های سازمانی؛ ساختار نظری |
| **Next.js** | متا چارچوب واکنش (SSR/SSG) | تولید برنامه های React با SEO |
### Backend (Node.js)
| چارچوب | هدف |
|-----------|---------|
| **اکسپرس** | چارچوب وب حداقلی و انعطاف پذیر (محبوب ترین) |
| **تعطیف** | چارچوب وب با کارایی بالا |
| **NestJS** | معماری با درجه سازمانی، الهام گرفته از Angular |
| **کوآ** | جایگزین اکسپرس سبک و مدرن |
| **هنو** | فوق العاده سریع، چند اجرا (Node، Deno، Bun، Edge) |
### زمان اجرا
| زمان اجرا | توضیحات |
|---------|-------------|
| **Node.js** | زمان اجرا جاوا اسکریپت سمت سرور اصلی (موتور V8) |
| **دنو** | ایمن به طور پیش فرض؛ پشتیبانی از TypeScript بومی؛ ایجاد شده توسط نویسنده اصلی Node |
| **نان** | زمان اجرا، بسته‌کننده و مدیریت بسته همه‌کاره فوق‌العاده سریع |
### ابزارهای ضروری
| ابزار | هدف |
|------|---------|
| **npm / نخ / pnpm ** | مدیران بسته |
| **TypeScript** | ابرمجموعه تایپ شده جاوا اسکریپت |
| **ESLint** | کد لینتینگ |
| **زیباتر** | قالب بندی کد |
| **Vite** | ابزار ساخت سریع و سرور توسعه دهنده |
| **وبک** | باندلر ماژول (بالغ، پرکاربرد) |
| **Jest / Vitest** | تست چارچوب |
---

## چه زمانی از جاوا اسکریپت استفاده کنیم
| سناریو | چرا جاوا اسکریپت | جایگزین بهتر |
|----------|--------------|-------------------|
| وب سایت | تنها گزینه برای UI مبتنی بر مرورگر | — |
| وب تمام پشته | همه جا یک زبان | TypeScript برای ایمنی نوع |
| برنامه های بلادرنگ (چت، بازی) | I/O مبتنی بر رویداد، غیر مسدود کننده | — |
| توابع بدون سرور | نوشتن سریع، استقرار در هر کجا | پایتون، برو |
| برنامه های موبایل (React Native) | اشتراک گذاری کد با وب | فلاتر، بومی سوئیفت/کاتلین |
| برنامه های دسکتاپ (الکترون) | کراس پلتفرم با فناوری وب | C# (WPF)، Tauri (Rust) |
| محاسبات فشرده CPU | محدودیت تک رشته ای | پایتون (NumPy)، C++، Rust، WebAssembly |
| برنامه نویسی سیستم ها | سطح انتزاع اشتباه | C، C++، Rust، Go |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین`var`،`let`و`const`چیست و چه زمانی باید از هر کدام استفاده کنم؟
**A:**`var`دارای محدوده عملکردی و بلند شده است - در کدهای مدرن از آن اجتناب کنید. `let`دارای محدوده بلوک است و امکان تخصیص مجدد را می دهد. `const`دارای محدوده بلوکی است و از تخصیص مجدد جلوگیری می کند (اما اشیا/آرایه هایی که به آن ارجاع می دهد هنوز قابل تغییر هستند). بهترین روش: به طور پیش فرض روی `const`، از`let`فقط زمانی که نیاز به تخصیص مجدد دارید استفاده کنید، هرگز از`var`استفاده نکنید.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2:`this`چگونه در جاوا اسکریپت کار می کند و چرا اینقدر گیج کننده است؟
**A:**`this`با **نحوه فراخوانی یک تابع** تعیین می شود، نه جایی که تعریف شده است. در فراخوانی متد،`this`شی است. در یک تماس مستقل،`undefined`(حالت دقیق) یا`global`(غیر دقیق) است. توابع پیکان`this`را از محدوده محصور خود به ارث می برند - به همین دلیل است که آنها برای تماس های برگشتی ترجیح داده می شوند. برای تنظیم صریح`this`از`.bind()`استفاده کنید.
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

### Q3: حلقه رویداد چیست و در واقع async/wait چگونه کار می‌کند؟
**A:** جاوا اسکریپت تک رشته ای با یک حلقه رویداد است که یک صف را پردازش می کند. پشته تماس کدهای همزمان را اجرا می کند. وقتی خالی است، حلقه رویداد وظیفه بعدی را از صف میکرووظیفه (Promises) یا صف macrotask (setTimeout، I/O) انتخاب می کند. `async/await`قند نحوی بر روی Promises است -`await`عملکرد async را متوقف می کند و هنگامی که Promise حل شد، بدون مسدود کردن رشته، از سر می گیرد.
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

### Q4: چگونه باید خطاها را در جاوا اسکریپت مدرن مدیریت کنم؟
**A:** از`try/catch`برای کد همزمان و`.catch()`یا`try/catch`با`async/await`برای کد ناهمزمان استفاده کنید. همیشه ردهای Promise را مدیریت کنید - ردهای کنترل نشده Node.js را خراب می کنند. کلاس های خطای سفارشی برای خطاهای دامنه خاص ایجاد کنید. از یک کنترل کننده خطای جهانی به عنوان یک شبکه ایمنی استفاده کنید.
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

### Q5: چه زمانی باید به جای اشیاء/آرایه های ساده از`Map`/`Set`استفاده کنم؟
**A:** از`Map`زمانی که کلیدها رشته ای نیستند، زمانی که به تکرار مرتبه درج نیاز دارید، زمانی که به`.size`نیاز دارید، یا زمانی که مدخل ها را اضافه/حذف می کنید (عملکرد بهتر از اشیا) از`Map`استفاده کنید. از`Set`برای مجموعه‌های منحصربه‌فرد با جستجوی O(1) استفاده کنید — بسیار سریع‌تر از`array.includes()`برای مجموعه‌های داده بزرگ. از اشیاء ساده برای داده‌های قابل سریال‌سازی با JSON و نقشه‌های کوچک کلید-مقدار با کلیدهای رشته‌ای استفاده کنید.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک تابع Debounce را اجرا کنید
**بیانیه مشکل:** یک ابزار`debounce`را اجرا کنید که فراخوانی یک تابع را تا زمانی که یک دوره انتظار مشخص از آخرین باری که فراخوانی شده است سپری شود به تاخیر می اندازد. از فراخوانی لبه های پیشرو و انتهایی پشتیبانی کنید.
** مرحله 1 - مشکل را درک کنید:**
یک تابع بازگردانده شده تماس‌های متوالی سریع را نادیده می‌گیرد و تنها پس از توقف تماس‌ها برای مدت زمان انتظار فعال می‌شود. "لبه پیشرو" به معنای آتش زدن بلافاصله در اولین تماس است. "لبه دنباله" یعنی آتش پس از مدت انتظار. ما باید هر دو حالت را مدیریت کنیم و از لغو نیز پشتیبانی کنیم.
** مرحله 2 - شناسایی رویکرد: **
- شناسه تایمر را در یک بسته ذخیره کنید.
- در هر تماس: تایمر موجود را پاک کنید، سپس یک`setTimeout`جدید تنظیم کنید.
- برای لبه اصلی: اگر تایمر فعال نیست، فوراً تماس بگیرید.
- یک تابع بازگردانده شده را با روش`.cancel()`برگردانید.
- با استفاده از توابع پیکان یا`.apply()`زمینه و آرگومان های`this`را حفظ کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- بسته شدن وضعیت را در سراسر تماس ها بدون ایجاد آلودگی جهانی حفظ می کند.
-`clearTimeout`قبل از`setTimeout`تضمین می کند که فقط آخرین تماس باعث اجرا می شود.
-`.cancel()`برای پاکسازی مهم است (به عنوان مثال، جدا کردن مؤلفه در React).
- Edge case: اگر`wait`0 باشد، تابع در تیک حلقه رویداد بعدی فعال می شود - برای به روز رسانی دسته ای DOM مفید است.
### مشکل 2: یک محدود کننده نرخ مبتنی بر وعده بسازید
**بیانیه مشکل:** یک محدود کننده نرخ ایجاد کنید که حداکثر N درخواست را در هر پنجره زمانی ایجاد کنید. باید وعده‌هایی را برگرداند که زمانی که تماس‌گیرنده مجاز به ادامه است، حل می‌شود و درخواست‌های اضافی را در صف قرار می‌دهد.
** مرحله 1 - مشکل را درک کنید:**
ما به یک پنجره کشویی یا ثابت نیاز داریم که تعداد تماس های برقرار شده را ردیابی کند. وقتی به حد مجاز رسید، تماس‌های جدید باید در صف قرار گیرند و وقتی شکافی باز می‌شود، حل شود. این الگوی "سطل نشانه" است.
** مرحله 2 - شناسایی رویکرد: **
- مُهر زمانی تماس‌های اخیر را در یک آرایه پیگیری کنید.
- در هر تماس: مُهرهای زمانی قدیمی‌تر از پنجره را حذف کنید، بررسی کنید که آیا تعداد < محدود است.
- اگر تحت محدودیت: فورا حل کنید.
- اگر در حد مجاز است: محاسبه کنید چه زمانی قدیمی‌ترین مُهر زمانی منقضی می‌شود، یک`setTimeout`تنظیم کنید، سپس حل کنید.
- از یک صف (آرایه ای از توابع حل) برای تماس گیرندگان در انتظار استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- رویکرد پنجره کشویی منصفانه تر از پنجره های ثابت است (بدون ترکیدگی در مرزهای پنجره).
- پردازش صف FIFO است - تماس گیرندگان به ترتیب ارائه می شوند.
- برای تولید: پشتیبانی`AbortController`را اضافه کنید تا تماس گیرندگان بتوانند انتظار را لغو کنند.
- عملکرد:`_cleanOldTimestamps`O(n) در هر تماس است اما n توسط`maxCalls`محدود می شود.
### مشکل 3: یک تابع کلون عمیق را اجرا کنید
**بیانیه مشکل:** تابعی بنویسید که هر مقدار جاوا اسکریپت، مدیریت اشیا، آرایه ها، تاریخ ها، RegExps، نقشه ها، مجموعه ها، ارجاعات دایره ای و آرایه های تایپ شده را عمیقاً شبیه سازی کند.
** مرحله 1 - مشکل را درک کنید:**
`JSON.parse(JSON.stringify(obj))`در: `undefined`، توابع، نمادها، تاریخ ها (رشته تبدیل می شوند)، RegExps (تبدیل به اشیاء خالی)، نقشه ها، مجموعه ها، ارجاعات دایره ای (پرتاب ها)، و آرایه های تایپ شده با شکست مواجه می شود. ما به یک راه حل بازگشتی نیاز داریم که اشیاء بازدید شده را ردیابی کند.
** مرحله 2 - شناسایی رویکرد: **
- از`Map`برای ردیابی اشیاء شبیه سازی شده استفاده کنید (مرجع دایره ای را کنترل می کند).
- هر نوع را به طور خاص مدیریت کنید: تاریخ → تاریخ جدید، RegExp → RegExp جدید، نقشه → نقشه جدید با ورودی های کلون شده، تنظیم → مجموعه جدید با مقادیر کلون شده.
- از`structuredClone()`به عنوان جایگزین داخلی مدرن (موجود در مرورگرها و Node.js 17+) استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- مراجع دایره ای: نقشه`seen`به جای تکرار بی نهایت، کلون از قبل ایجاد شده را برمی گرداند.
- توصیف کننده های ویژگی:`Reflect.ownKeys`+`getOwnPropertyDescriptor`گیرنده ها، تنظیم کننده ها و ویژگی های غیرقابل شمارش را حفظ می کند.
- جایگزین مدرن:`structuredClone(value)`اکثر این موارد را به صورت بومی (به جز توابع و گره های DOM) مدیریت می کند. در صورت موجود بودن آن را ترجیح دهید.
- عملکرد: برای اشیاء ساده،`JSON.parse(JSON.stringify(obj))`هنوز سریع‌ترین است. از کلون عمیق فقط زمانی استفاده کنید که واقعاً به آن نیاز دارید.
### مسئله 4: یک امیتر رویداد ساده بسازید
**بیانیه مشکل:** یک کلاس Emitter رویداد را پیاده سازی کنید که از روش های `on`، `off`، `emit`، و`once`پشتیبانی می کند. شنوندگان باید به ترتیب ثبت نام فراخوانی شوند. `emit`باید آرگومان ها را به همه شنوندگان ارسال کند.
** مرحله 1 - مشکل را درک کنید:**
ما به یک سیستم میخانه/فرعی نیاز داریم: شنوندگان را برای رویدادهای نام‌گذاری شده ثبت کنید، شنوندگان خاص را حذف کنید، رویدادها را با آرگومان‌ها آغاز کنید و از شنوندگان یک‌باره پشتیبانی کنید. این الگوی Observer است که به طور گسترده در Node.js استفاده می شود.
** مرحله 2 - شناسایی رویکرد: **
- شنوندگان را در`Map<string, Array<Function>>`ذخیره کنید.
- `on`: شنونده را به آرایه فشار دهید.
- `off`: شنونده خاص را از آرایه فیلتر کنید.
- `emit`: آرایه را تکرار کنید و هر شنونده را با آرگومان های گسترده فراخوانی کنید.
- `once`: شنونده را در تابعی بپیچید که پس از اولین تماس خود را حذف می کند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- کپی`[...listeners]`در`emit`هنگامی که شنونده`off`را در حین تکرار فرا می خواند، از بروز مشکلات جلوگیری می کند.
-`once``_original` را ذخیره می کند تا تماس گیرندگان بتوانند از طریق`off(event, originalFn)`لفاف را جدا کنند.
- زمینه های خصوصی (`#listeners`) از جهش خارجی حالت داخلی جلوگیری می کند.
- برای تولید: هشدار`maxListeners`(مانند Node.js)، مدیریت خطا به ازای هر شنونده و`prependListener`را برای اولویت اضافه کنید.
---

## خلاصه
جاوا اسکریپت اجتناب ناپذیر است. این تنها زبانی است که در مرورگرهای وب اجرا می‌شود و آن را برای توسعه frontend ضروری می‌کند. با Node.js به سمت سرور گسترش می یابد و با فریم ورک هایی مانند React Native و Electron به موبایل و دسکتاپ می رسد. اکوسیستم بزرگترین در برنامه نویسی است. ویژگی‌های این زبان به خوبی شناخته شده و قابل مدیریت هستند - و TypeScript به نگرانی‌های تایپ کردن پاسخ می‌دهد. برای هر چیزی که در مرورگر اجرا می شود، جاوا اسکریپت تنها بهترین انتخاب نیست، بلکه تنها انتخاب است.