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

# جاوا اسکرپٹ
JavaScript ایک متحرک، تشریح شدہ پروگرامنگ زبان ہے جسے Brendan Eich نے 1995 میں صرف 10 دنوں میں تخلیق کیا تھا۔ اصل میں ویب صفحات میں انٹرایکٹیویٹی کو شامل کرنے کے لیے ڈیزائن کیا گیا تھا، یہ دنیا میں سب سے زیادہ استعمال ہونے والی پروگرامنگ زبان بن گئی ہے۔ JavaScript ہر ویب براؤزر میں، سرورز پر Node.js کے ذریعے، ڈیسک ٹاپ ایپس (الیکٹران)، موبائل ایپس (رییکٹ مقامی)، اور یہاں تک کہ ایمبیڈڈ سسٹمز میں چلتا ہے۔
زبان اس لحاظ سے منفرد ہے کہ یہ کلائنٹ سائڈ ویب ڈویلپمنٹ کے لیے بنیادی طور پر واحد آپشن ہے — ہر براؤزر اسے مقامی طور پر سپورٹ کرتا ہے۔ یہ اجارہ داری، فل اسٹیک جاوا اسکرپٹ (Node.js، Deno، Bun) کے عروج کے ساتھ مل کر اسے ناگزیر بناتی ہے۔
---

## جاوا اسکرپٹ کیوں اہمیت رکھتا ہے۔
- **ویب کی زبان**: واحد زبان جو مقامی طور پر براؤزرز میں چلتی ہے۔ فرنٹ اینڈ کے لیے کوئی متبادل نہیں۔
- **مکمل اسٹیک کی اہلیت**: فرنٹ اینڈ پر ایک ہی زبان (ری ایکٹ، ویو، سویلٹ) اور بیک اینڈ (Node.js، Express، Fastify)۔
- **بڑے پیمانے پر ماحولیاتی نظام**: npm کے پاس 2 ملین سے زیادہ پیکجز ہیں — جو دنیا کی سب سے بڑی سافٹ ویئر رجسٹری ہے۔
- **استعمال**: ویب ایپس، موبائل ایپس (ری ایکٹ نیٹیو)، ڈیسک ٹاپ ایپس (الیکٹران)، آئی او ٹی، سرور لیس فنکشنز۔
- **داخلے میں کم رکاوٹ**: کسی بھی براؤزر میں چلتا ہے - کوڈنگ شروع کرنے کے لیے کسی انسٹالیشن کی ضرورت نہیں ہے۔
- **ڈیزائن کے لحاظ سے غیر مطابقت پذیر**: ایونٹ سے چلنے والا، غیر مسدود I/O اسے ریئل ٹائم ایپلی کیشنز کے لیے بہترین بناتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **متحرک ٹائپنگ کے نقصانات** | کوئی کمپائل ٹائم ٹائپ چیکنگ نہیں ہے۔ رن ٹائم پر کیڑے کی سطح | TypeScript (جاوا اسکرپٹ کا ٹائپ شدہ سپر سیٹ) استعمال کریں۔
| **کال بیک پیچیدگی** | نیسٹڈ کال بیکس ناقابل پڑھ سکتے ہیں ("کال بیک جہنم") | وعدوں کا استعمال کریں اور async/await |
| **نرالا الفاظ** | `==`بمقابلہ`===`,`this`بائنڈنگ، لہرانا، قسم جبر | نرالا جانیں؛ ESLint استعمال کریں؛`const`/`let`کو`var`پر ترجیح دیں |
| **سنگل تھریڈڈ** | سی پی یو کے پابند کام ایونٹ لوپ کو بلاک کر دیتے ہیں | ویب ورکرز، ورکر تھریڈز استعمال کریں یا مقامی ماڈیولز پر آف لوڈ کریں |
| **پیکیج کا معیار** | npm کے کھلے پن کا مطلب ہے متضاد معیار اور سیکورٹی کے خطرات | آڈٹ انحصار؛ لاک فائلوں کا استعمال کریں؛ اچھی طرح سے برقرار رکھنے والے پیکجوں کو ترجیح دیں |
---

## نحوی بنیادی باتیں
### متغیرات اور اقسام
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

### افعال
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

### آبجیکٹ اور کلاسز
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

### Async پروگرامنگ
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

### ماڈیولز
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

## اعلی درجے کی نحو اور نمونے۔
### تباہی اور پھیلاؤ/آرام (گہرا غوطہ)
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

### پراکسی اور ریفلیکٹ
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

### علامات، تکرار کرنے والے، اور جنریٹر
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

### حسب ضرورت خرابی کے درجہ بندی
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

## ہم آہنگی اور ہم آہنگی
JavaScript ایونٹ لوپ کے ساتھ سنگل تھریڈڈ ہے۔ ہم آہنگی غیر مطابقت پذیر پیٹرن، ویب ورکرز، اور (Node.js میں) worker_threads ماڈیول کے ذریعے حاصل کی جاتی ہے۔
### ایونٹ لوپ
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

### ورکر تھریڈز (Node.js — CPU کے پابند کام)
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

### ویب ورکرز (براؤزر)
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

### Async پیٹرنز
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ ڈائرکٹری کا ڈھانچہ
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

### تشکیل کنفیگریشن — `package.json`
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

### لنٹنگ اور فارمیٹنگ کنفیگریشن
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

### CI/CD پائپ لائن — GitHub ایکشنز
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

## ٹیسٹنگ
### مذاق کے ساتھ ٹیسٹنگ
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

### مذاق اور انٹیگریشن ٹیسٹ
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

## انٹرآپریبلٹی
### N-API (Node.js) کے ساتھ مقامی ایڈونز
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

### ffi-napi کے ساتھ C لائبریریوں کو کال کرنا
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

## ڈیزائن پیٹرن
### ماڈیول پیٹرن (انکیپسولیشن)
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

### مبصر/ایونٹ ایمیٹر پیٹرن
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

### بلڈر پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### ڈاکر فائل
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

### پلیٹ فارم کے لیے مخصوص تعیناتی۔
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

## ماحولیاتی نظام
### فرنٹ اینڈ فریم ورک
| فریم ورک | نقطہ نظر | کے لیے بہترین |
|------------|---------|------------|
| **ردعمل** | اجزاء پر مبنی، ورچوئل DOM | بڑے پیمانے پر SPAs؛ سب سے بڑا ماحولیاتی نظام |
| **ویو** | ترقی پسند، ٹیمپلیٹ پر مبنی | بتدریج اپنانے؛ عظیم ڈویلپر کا تجربہ |
| **Svelte** | کمپائل ٹائم، کوئی ورچوئل DOM نہیں | چھوٹے بنڈل، آسان کوڈ |
| **کونیی** | مکمل فریم ورک، TypeScript-first | انٹرپرائز ایپس؛ نظریاتی ڈھانچہ |
| **Next.js** | ری ایکٹ میٹا فریم ورک (SSR/SSG) | SEO کے ساتھ پروڈکشن ری ایکٹ ایپس |
### بیک اینڈ (Node.js)
| فریم ورک | مقصد |
|------------|---------|
| **ایکسپریس** | کم سے کم، لچکدار ویب فریم ورک (سب سے زیادہ مقبول) |
| **تیز بنائیں** | اعلی کارکردگی کا ویب فریم ورک |
| **NestJS** | انٹرپرائز گریڈ، کونیی سے متاثر فن تعمیر |
| **Koa** | ہلکا پھلکا، جدید ایکسپریس متبادل |
| **ہونو** | انتہائی تیز، کثیر رن ٹائم (نوڈ، ڈینو، بن، کنارے) |
### رن ٹائمز
| رن ٹائم | تفصیل |
|---------|---------------|
| **Node.js** | اصل سرور سائیڈ JavaScript رن ٹائم (V8 انجن) |
| **ڈینو** | پہلے سے طے شدہ طور پر محفوظ؛ مقامی ٹائپ اسکرپٹ سپورٹ؛ نوڈ کے اصل مصنف کے ذریعہ تخلیق کردہ |
| **بن** | الٹرا فاسٹ آل ان ون رن ٹائم، بنڈلر، اور پیکیج مینیجر |
### ضروری ٹولز
| ٹول | مقصد |
|------|---------|
| **npm / سوت / pnpm** | پیکیج مینیجرز |
| **TypeScript** | جاوا اسکرپٹ کا ٹائپ شدہ سپر سیٹ |
| **ESLint** | کوڈ linting |
| **خوبصورت** | کوڈ فارمیٹنگ |
| **وائٹ** | فاسٹ بلڈ ٹول اور دیو سرور |
| **ویب پیک** | ماڈیول بنڈلر (بالغ، وسیع پیمانے پر استعمال) |
| **مذاق/مذاق** | جانچ کے فریم ورک |
---

## جاوا اسکرپٹ کب استعمال کریں۔
| منظر نامہ | جاوا اسکرپٹ کیوں | بہتر متبادل |
|------------|----------------------------|---------|
| ویب فرنٹ اینڈ | براؤزر پر مبنی UI کے لیے واحد آپشن | - |
| مکمل اسٹیک ویب | ہر جگہ ایک ہی زبان | قسم کی حفاظت کے لیے TypeScript |
| ریئل ٹائم ایپس (چیٹ، گیمز) | ایونٹ پر مبنی، غیر مسدود I/O | - |
| سرور کے بغیر افعال | لکھنے میں جلدی، کہیں بھی تعینات کریں | ازگر، جاؤ |
| موبائل ایپس (رییکٹ مقامی) | ویب کے ساتھ کوڈ کا اشتراک کریں | پھڑپھڑاہٹ، مقامی سوئفٹ/کوٹلن |
| ڈیسک ٹاپ ایپس (الیکٹران) | ویب ٹیک کے ساتھ کراس پلیٹ فارم | C# (WPF)، توری (زنگ) |
| CPU-انتہائی حساب | سنگل تھریڈڈ حد | Python (NumPy)، C++، Rust، WebAssembly |
| سسٹمز پروگرامنگ | غلط تجریدی سطح | C, C++, Rust, Go |
---

## مصنوعی سوال و جواب
### Q1: `var`، `let`، اور`const`میں کیا فرق ہے، اور مجھے ہر ایک کب استعمال کرنا چاہیے؟
**A:**`var`فنکشن کا دائرہ کار اور لہرایا ہوا ہے — جدید کوڈ میں اس سے گریز کریں۔ `let`بلاک دائرہ کار ہے اور دوبارہ تفویض کی اجازت دیتا ہے۔ `const`بلاک اسکوپڈ ہے اور دوبارہ تفویض کو روکتا ہے (لیکن اس کے حوالے سے آبجیکٹ/ایرے اب بھی متغیر ہیں)۔ بہترین عمل: پہلے سے طے شدہ `const`،`let`صرف اس وقت استعمال کریں جب آپ کو دوبارہ تفویض کی ضرورت ہو، کبھی بھی`var`استعمال نہ کریں۔
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2:`this`JavaScript میں کیسے کام کرتا ہے، اور یہ اتنا الجھا ہوا کیوں ہے؟
**A:**`this`کا تعین **کسی فنکشن کو کیسے کہا جاتا ہے** سے ہوتا ہے، نہ کہ اس کی تعریف کہاں کی گئی ہے۔ میتھڈ کال میں،`this`آبجیکٹ ہے۔ ایک اسٹینڈ کال میں، یہ`undefined`(سخت موڈ) یا`global`(غیر سخت) ہے۔ تیر کے فنکشنز`this`کو ان کے منسلک دائرہ کار سے وراثت میں ملاتے ہیں - یہی وجہ ہے کہ انہیں کال بیکس کے لیے ترجیح دی جاتی ہے۔`this`کو واضح طور پر سیٹ کرنے کے لیے`.bind()`استعمال کریں۔
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

### Q3: ایونٹ لوپ کیا ہے، اور async/await دراصل کیسے کام کرتا ہے؟
**A:** JavaScript ایک ایونٹ لوپ کے ساتھ واحد تھریڈڈ ہے جو قطار پر کارروائی کرتا ہے۔ کال اسٹیک مطابقت پذیر کوڈ پر عمل درآمد کرتا ہے۔ جب یہ خالی ہوتا ہے، ایونٹ لوپ مائیکرو ٹاسک قطار (وعدے) یا میکروٹاسک قطار (سیٹ ٹائم آؤٹ، I/O) سے اگلا کام چنتا ہے۔ `async/await`وعدوں پر مصنوعی شوگر ہے —`await`async فنکشن کو روکتا ہے اور جب وعدہ حل ہو جاتا ہے تو تھریڈ کو بلاک کیے بغیر دوبارہ شروع ہوتا ہے۔
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

### Q4: مجھے جدید JavaScript میں غلطیوں کو کیسے ہینڈل کرنا چاہیے؟
**A:** مطابقت پذیر کوڈ کے لیے`try/catch`اور غیر مطابقت پذیر کوڈ کے لیے`async/await`کے ساتھ`.catch()`یا`try/catch`استعمال کریں۔ ہمیشہ وعدے کے مسترد ہونے کو ہینڈل کریں — غیر ہینڈل شدہ مسترد کریش Node.js۔ ڈومین کی مخصوص غلطیوں کے لیے حسب ضرورت غلطی کی کلاسز بنائیں۔ عالمی ایرر ہینڈلر کو حفاظتی جال کے طور پر استعمال کریں۔
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

### Q5: مجھے سادہ اشیاء/ارے کی بجائے`Map`/`Set`کب استعمال کرنا چاہئے؟
**A:**`Map`استعمال کریں جب چابیاں تار نہ ہوں، جب آپ کو داخل کرنے کے آرڈر کی تکرار کی ضرورت ہو، جب آپ کو`.size`کی ضرورت ہو، یا جب آپ بار بار اندراجات کو شامل / ہٹاتے ہوں (آجیکٹ سے بہتر کارکردگی)۔ O(1) تلاش کے ساتھ منفرد مجموعوں کے لیے`Set`استعمال کریں — بڑے ڈیٹا سیٹس کے لیے`array.includes()`سے کہیں زیادہ تیز۔ سادہ JSON-Serializable ڈیٹا اور سٹرنگ کیز کے ساتھ چھوٹے کلیدی قدر کے نقشوں کے لیے سادہ اشیاء کا استعمال کریں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ڈیباؤنس فنکشن کو نافذ کریں۔
**مسئلہ کا بیان:** ایک`debounce`یوٹیلیٹی کو لاگو کریں جو کسی فنکشن کو شروع کرنے میں اس وقت تک تاخیر کرتی ہے جب تک کہ آخری بار کال کیے جانے کے بعد ایک مخصوص انتظار کی مدت ختم نہ ہو جائے۔ سرکردہ اور پچھلے دونوں کنارے کی درخواست کی حمایت کریں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ڈیباؤنس شدہ فنکشن تیزی سے آنے والی کالوں کو نظر انداز کرتا ہے اور انتظار کی مدت کے لیے کال بند ہونے کے بعد ہی فائر ہوتا ہے۔ "لیڈنگ ایج" کا مطلب ہے پہلی کال پر فوراً فائر۔ "ٹریلنگ ایج" کا مطلب ہے انتظار کی مدت کے بعد آگ۔ ہمیں دونوں طریقوں کو سنبھالنے اور منسوخی کی حمایت کرنے کی ضرورت ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- بندش میں ٹائمر آئی ڈی اسٹور کریں۔
- ہر کال پر: موجودہ ٹائمر کو صاف کریں، پھر ایک نیا`setTimeout`سیٹ کریں۔
- معروف کنارے کے لیے: اگر کوئی ٹائمر فعال نہیں ہے تو فوراً کال کریں۔
-`.cancel()`طریقہ کے ساتھ ڈیباؤنس شدہ فنکشن واپس کریں۔
- تیر کے فنکشن یا`.apply()`کا استعمال کرتے ہوئے`this`سیاق و سباق اور دلائل کو محفوظ کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- بندش عالمی دائرہ کار کو آلودہ کیے بغیر کالوں میں ریاست کو محفوظ رکھتی ہے۔
-`clearTimeout`سے پہلے`setTimeout`صرف آخری کال کو متحرک کرتا ہے۔
-`.cancel()`صفائی کے لیے اہم ہے (مثال کے طور پر، ری ایکٹ میں اجزاء کا ان ماؤنٹ)۔
- ایج کیس: اگر`wait`0 ہے، تو فنکشن اگلے ایونٹ لوپ ٹک پر فائر کرتا ہے — بیچنگ DOM اپ ڈیٹس کے لیے مفید ہے۔
### مسئلہ 2: وعدے پر مبنی شرح کی حد بنائیں
**مسئلہ کا بیان:** ایک ریٹ لمیٹر بنائیں جو فی ٹائم ونڈو میں زیادہ سے زیادہ N درخواستوں کی اجازت دے۔ اسے وہ وعدے واپس کرنے چاہئیں جو کال کرنے والے کو آگے بڑھنے کی اجازت دینے پر حل کرتے ہیں، اور ضرورت سے زیادہ درخواستوں کی قطار لگاتے ہیں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ایک سلائیڈنگ یا فکسڈ ونڈو کی ضرورت ہے جو ٹریک کرے کہ کتنی کالیں کی گئی ہیں۔ جب حد تک پہنچ جاتی ہے، نئی کالوں کو قطار میں لگانا چاہیے اور سلاٹ کھلنے پر حل کیا جانا چاہیے۔ یہ "ٹوکن بالٹی" پیٹرن ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ایک صف میں حالیہ کالوں کے ٹائم اسٹیمپ کو ٹریک کریں۔
- ہر کال پر: ونڈو سے پرانے ٹائم اسٹیمپ کو ہٹا دیں، چیک کریں کہ گنتی < حد ہے۔
- اگر حد کے تحت: فوری طور پر حل کریں۔
- اگر حد ہے: حساب لگائیں کہ کب سب سے پرانا ٹائم اسٹیمپ ختم ہو جائے، ایک`setTimeout`سیٹ کریں، پھر حل کریں۔
- انتظار کرنے والے کال کرنے والوں کے لیے ایک قطار (حل کے افعال کی صف) کا استعمال کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- سلائیڈنگ ونڈو اپروچ فکسڈ کھڑکیوں سے بہتر ہے (کھڑکی کی حدود پر کوئی پھٹ نہیں)۔
- قطار پروسیسنگ FIFO ہے - کال کرنے والوں کو ترتیب سے پیش کیا جاتا ہے۔
- پیداوار کے لیے:`AbortController`سپورٹ شامل کریں تاکہ کال کرنے والے انتظار کو منسوخ کر سکیں۔
- کارکردگی:`_cleanOldTimestamps`فی کال O(n) ہے لیکن n`maxCalls`سے منسلک ہے۔
### مسئلہ 3: ڈیپ کلون فنکشن لاگو کریں۔
**مسئلہ کا بیان:** ایک ایسا فنکشن لکھیں جو جاوا اسکرپٹ کی کسی بھی قدر کو گہرائی سے کلون کرتا ہو، آبجیکٹس، ارے، تاریخیں، RegExps، نقشے، سیٹس، سرکلر حوالہ جات، اور ٹائپ کردہ صفوں کو ہینڈل کرتا ہو۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
`JSON.parse(JSON.stringify(obj))`اس پر ناکام ہو جاتا ہے:`undefined`, فنکشنز، سمبلز، تاریخیں (سٹرنگز بن جاتے ہیں)، RegExps (خالی اشیاء بن جاتے ہیں)، نقشے، سیٹ، سرکلر حوالہ جات (تھرو)، اور ٹائپ کردہ ارے۔ ہمیں ایک تکراری حل کی ضرورت ہے جو ملاحظہ کی گئی اشیاء کو ٹریک کرے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- پہلے سے کلون شدہ اشیاء کو ٹریک کرنے کے لیے ایک`Map`استعمال کریں (سرکلر حوالوں کو ہینڈل کرتا ہے)۔
- ہر قسم کو خاص طور پر ہینڈل کریں: تاریخ → نئی تاریخ، RegExp → نئی RegExp، نقشہ → نیا نقشہ کلون شدہ اندراجات کے ساتھ، سیٹ → کلون شدہ اقدار کے ساتھ نیا سیٹ۔
-`structuredClone()`کو جدید بلٹ ان متبادل کے طور پر استعمال کریں (براؤزرز اور Node.js 17+ میں دستیاب)۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- سرکلر حوالہ جات:`seen`نقشہ لامحدود تکرار کرنے کے بجائے پہلے سے بنائے گئے کلون کو واپس کرتا ہے۔
- پراپرٹی کی وضاحت کنندگان:`Reflect.ownKeys`+`getOwnPropertyDescriptor`حاصل کرنے والوں، سیٹرز اور غیر گنتی کی خصوصیات کو محفوظ رکھتا ہے۔
- جدید متبادل:`structuredClone(value)`ان میں سے زیادہ تر معاملات کو مقامی طور پر ہینڈل کرتا ہے (سوائے فنکشنز اور DOM نوڈس کے)۔ دستیاب ہونے پر اسے ترجیح دیں۔
- کارکردگی: سادہ اشیاء کے لیے،`JSON.parse(JSON.stringify(obj))`اب بھی تیز ترین ہے۔ ڈیپ کلون صرف اس وقت استعمال کریں جب آپ کو درحقیقت اس کی ضرورت ہو۔
### مسئلہ 4: ایک سادہ ایونٹ ایمیٹر بنائیں
**مسئلہ کا بیان:** ایک ایونٹ ایمیٹر کلاس نافذ کریں جو `on`، `off`، `emit`، اور`once`طریقوں کو سپورٹ کرتی ہو۔ سننے والوں کو رجسٹریشن آرڈر میں بلایا جائے۔ `emit`کو تمام سننے والوں کو دلائل دینا چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ایک پب/سب سسٹم کی ضرورت ہے: سامعین کو نامزد واقعات کے لیے رجسٹر کریں، مخصوص سننے والوں کو ہٹائیں، واقعات کو دلائل کے ساتھ متحرک کریں، اور ایک بار سننے والوں کی حمایت کریں۔ یہ مبصر پیٹرن ہے جو Node.js میں بڑے پیمانے پر استعمال ہوتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- سننے والوں کو`Map<string, Array<Function>>`میں اسٹور کریں۔
-`on`: سننے والے کو صف کی طرف دھکیلیں۔
-`off`: مخصوص سننے والے کو صف سے فلٹر کریں۔
-`emit`: سرنی کو اعادہ کریں اور ہر سننے والے کو پھیلاؤ کے دلائل کے ساتھ کال کریں۔
-`once`: سننے والے کو ایک فنکشن میں لپیٹیں جو پہلی کال کے بعد خود کو ہٹا دیتا ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
-`emit`میں`[...listeners]`کاپی مسائل کو روکتی ہے جب سننے والا تکرار کے دوران`off`کو کال کرتا ہے۔
-`once``_original` کو اسٹور کرتا ہے تاکہ کال کرنے والے`off(event, originalFn)`کے ذریعے ریپر کو ہٹا سکیں۔
- پرائیویٹ فیلڈز (`#listeners`) اندرونی حالت کے بیرونی تغیر کو روکتے ہیں۔
- پروڈکشن کے لیے:`maxListeners`وارننگ شامل کریں (جیسے Node.js)، فی سننے والا ایرر ہینڈلنگ، اور ترجیح کے لیے `prependListener`۔
---

## خلاصہ
جاوا اسکرپٹ ناگزیر ہے۔ یہ واحد زبان ہے جو ویب براؤزرز میں چلتی ہے، جو اسے فرنٹ اینڈ ڈیولپمنٹ کے لیے ضروری بناتی ہے۔ Node.js کے ساتھ، یہ سرور سائیڈ تک پھیلا ہوا ہے، اور React Native اور Electron جیسے فریم ورک کے ساتھ، یہ موبائل اور ڈیسک ٹاپ تک پہنچتا ہے۔ پروگرامنگ میں ماحولیاتی نظام سب سے بڑا ہے۔ زبان کی نرالی باتیں معروف اور قابل انتظام ہیں — اور TypeScript ٹائپنگ کے خدشات کو دور کرتا ہے۔ براؤزر میں چلنے والی کسی بھی چیز کے لیے، JavaScript صرف بہترین انتخاب نہیں ہے - یہ واحد انتخاب ہے۔