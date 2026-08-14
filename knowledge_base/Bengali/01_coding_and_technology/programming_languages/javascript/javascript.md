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
# জাভাস্ক্রিপ্ট
জাভাস্ক্রিপ্ট হল একটি গতিশীল, ব্যাখ্যা করা প্রোগ্রামিং ভাষা যা ব্রেন্ডন ইচ 1995 সালে মাত্র 10 দিনের মধ্যে তৈরি করেছিলেন। মূলত ওয়েব পৃষ্ঠাগুলিতে ইন্টারঅ্যাকটিভিটি যোগ করার জন্য ডিজাইন করা হয়েছিল, এটি বিশ্বের সবচেয়ে ব্যাপকভাবে ব্যবহৃত প্রোগ্রামিং ভাষাতে পরিণত হয়েছে। জাভাস্ক্রিপ্ট প্রতিটি ওয়েব ব্রাউজারে, Node.js এর মাধ্যমে সার্ভারে, ডেস্কটপ অ্যাপে (ইলেক্ট্রন), মোবাইল অ্যাপস (প্রতিক্রিয়া নেটিভ), এমনকি এমবেডেড সিস্টেমেও চলে।
ভাষাটি অনন্য যে এটি মূলত ক্লায়েন্ট-সাইড ওয়েব ডেভেলপমেন্টের একমাত্র বিকল্প - প্রতিটি ব্রাউজার এটি স্থানীয়ভাবে সমর্থন করে। এই একচেটিয়া, ফুল-স্ট্যাক জাভাস্ক্রিপ্টের (Node.js, Deno, Bun) উত্থানের সাথে মিলিত, এটিকে অপরিহার্য করে তোলে।
---

## কেন জাভাস্ক্রিপ্ট গুরুত্বপূর্ণ
- **ওয়েবের ভাষা**: একমাত্র ভাষা যা ব্রাউজারে স্থানীয়ভাবে চলে। ফ্রন্টএন্ডের জন্য কোন বিকল্প নেই।
- **ফুল-স্ট্যাক ক্ষমতা**: ফ্রন্টএন্ডে একই ভাষা (প্রতিক্রিয়া, ভিউ, স্বেল্ট) এবং ব্যাকএন্ড (Node.js, Express, Fastify)।
- **ম্যাসিভ ইকোসিস্টেম**: npm-এর 2 মিলিয়নেরও বেশি প্যাকেজ রয়েছে — বিশ্বের বৃহত্তম সফ্টওয়্যার রেজিস্ট্রি।
- **ভার্স্যাটিলিটি**: ওয়েব অ্যাপস, মোবাইল অ্যাপস (নেটিভ রিঅ্যাক্ট), ডেস্কটপ অ্যাপস (ইলেক্ট্রন), আইওটি, সার্ভারহীন ফাংশন।
- **প্রবেশে কম বাধা**: যেকোনো ব্রাউজারে চলে — কোডিং শুরু করার জন্য কোনো ইনস্টলেশনের প্রয়োজন নেই।
- **ডিজাইন অনুসারে অ্যাসিঙ্ক্রোনাস**: ইভেন্ট-চালিত, নন-ব্লকিং I/O এটিকে রিয়েল-টাইম অ্যাপ্লিকেশনের জন্য চমৎকার করে তোলে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **গতিশীল টাইপিং সমস্যা** | কম্পাইল-টাইম টাইপ চেকিং নেই; রানটাইমে বাগ পৃষ্ঠ | টাইপস্ক্রিপ্ট ব্যবহার করুন (জাভাস্ক্রিপ্টের একটি টাইপ করা সুপারসেট) |
| **কলব্যাক জটিলতা** | নেস্টেড কলব্যাক অপঠনযোগ্য হয়ে উঠতে পারে ("কলব্যাক হেল") | প্রতিশ্রুতি ব্যবহার করুন এবং অ্যাসিঙ্ক/অপেক্ষা করুন |
| **অদ্ভুত শব্দার্থবিদ্যা** | `==`বনাম`===`,`this`বাঁধাই, উত্তোলন, টাইপ জবরদস্তি | quirks শিখুন; ESLint ব্যবহার করুন;`var`এর চেয়ে`const`/`let`পছন্দ করুন |
| **একক থ্রেডেড** | CPU-বাউন্ড টাস্ক ইভেন্ট লুপ ব্লক করে | ওয়েব ওয়ার্কার, ওয়ার্কার থ্রেড ব্যবহার করুন বা নেটিভ মডিউলে অফলোড করুন |
| **প্যাকেজের গুণমান** | npm এর উন্মুক্ততা মানে অসামঞ্জস্যপূর্ণ গুণমান এবং নিরাপত্তা ঝুঁকি | অডিট নির্ভরতা; লক ফাইল ব্যবহার করুন; ভালোভাবে রক্ষণাবেক্ষণ করা প্যাকেজ পছন্দ করুন |
---

## সিনট্যাক্স মৌলিক
### ভেরিয়েবল এবং প্রকার
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

### ফাংশন
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

### অবজেক্ট এবং ক্লাস
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

### অ্যাসিঙ্ক প্রোগ্রামিং
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

### মডিউল
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### ধ্বংস এবং বিস্তার/বিশ্রাম (গভীর ডুব)
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

### প্রক্সি এবং প্রতিফলন
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

### প্রতীক, পুনরাবৃত্তিকারী এবং জেনারেটর
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

### কাস্টম ত্রুটি শ্রেণিবিন্যাস
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

## সামঞ্জস্য এবং সমান্তরালতা
জাভাস্ক্রিপ্ট একটি ইভেন্ট লুপ সহ একক-থ্রেডেড। অ্যাসিঙ্ক্রোনাস প্যাটার্ন, ওয়েব ওয়ার্কার এবং (Node.js-এ) worker_threads মডিউলের মাধ্যমে একযোগে অর্জন করা হয়।
### ইভেন্ট লুপ
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

### কর্মী থ্রেড (Node.js — CPU-বাউন্ড টাস্ক)
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

### ওয়েব কর্মী (ব্রাউজার)
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

### অ্যাসিঙ্ক প্যাটার্ন
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রজেক্ট ডাইরেক্টরি স্ট্রাকচার
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

### বিল্ড কনফিগারেশন — `package.json`
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

### লিন্টিং এবং ফরম্যাটিং কনফিগারেশন
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

### CI/CD পাইপলাইন — গিটহাব অ্যাকশন
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

## পরীক্ষা
### জেস্ট দিয়ে পরীক্ষা করা হচ্ছে
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

### মকিং এবং ইন্টিগ্রেশন টেস্ট
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

## ইন্টারঅপারেবিলিটি
### N-API (Node.js) সহ নেটিভ অ্যাডঅন
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

### ওয়েব অ্যাসেম্বলি (ওয়াসম)
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

### ffi-napi সহ সি লাইব্রেরি কল করা হচ্ছে
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

## ডিজাইন প্যাটার্ন
### মডিউল প্যাটার্ন (এনক্যাপসুলেশন)
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

### পর্যবেক্ষক / ইভেন্ট ইমিটার প্যাটার্ন
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

### নির্মাতা প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### ডকারফাইল
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

### প্ল্যাটফর্ম-নির্দিষ্ট স্থাপনা
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

## ইকোসিস্টেম
### ফ্রন্টএন্ড ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | দৃষ্টিভঙ্গি | জন্য সেরা |
|------------|----------|------------|
| **প্রতিক্রিয়া** | কম্পোনেন্ট-ভিত্তিক, ভার্চুয়াল DOM | বড় মাপের এসপিএ; বৃহত্তম বাস্তুতন্ত্র |
| **ভিউ** | প্রগতিশীল, টেমপ্লেট-ভিত্তিক | ধীরে ধীরে গ্রহণ; দুর্দান্ত বিকাশকারী অভিজ্ঞতা |
| **Svelte** | কম্পাইল-টাইম, ভার্চুয়াল DOM নেই | ছোট বান্ডিল, সহজ কোড |
| **কৌণিক** | সম্পূর্ণ ফ্রেমওয়ার্ক, টাইপস্ক্রিপ্ট-প্রথম | এন্টারপ্রাইজ অ্যাপস; মতামতযুক্ত কাঠামো |
| **পরবর্তী.js** | প্রতিক্রিয়া মেটা-ফ্রেমওয়ার্ক (SSR/SSG) | এসইও সহ প্রোডাকশন রিঅ্যাক্ট অ্যাপস |
### ব্যাকএন্ড (Node.js)
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **এক্সপ্রেস** | ন্যূনতম, নমনীয় ওয়েব ফ্রেমওয়ার্ক (সবচেয়ে জনপ্রিয়) |
| **দ্রুত করা** | উচ্চ-পারফরম্যান্স ওয়েব ফ্রেমওয়ার্ক |
| **NestJS** | এন্টারপ্রাইজ-গ্রেড, কৌণিক-অনুপ্রাণিত স্থাপত্য |
| **কোয়া** | লাইটওয়েট, আধুনিক এক্সপ্রেস বিকল্প |
| **হোনো** | অতি-দ্রুত, বহু-রানটাইম (নোড, ডেনো, বান, প্রান্ত) |
### রানটাইম
| রানটাইম | বর্ণনা |
|---------|---------------|
| **Node.js** | আসল সার্ভার-সাইড জাভাস্ক্রিপ্ট রানটাইম (V8 ইঞ্জিন) |
| **ডেনো** | ডিফল্টরূপে সুরক্ষিত; নেটিভ টাইপস্ক্রিপ্ট সমর্থন; নোডের মূল লেখক দ্বারা তৈরি |
| **বন** | অতি দ্রুত অল-ইন-ওয়ান রানটাইম, বান্ডলার এবং প্যাকেজ ম্যানেজার |
### প্রয়োজনীয় সরঞ্জাম
| টুল | উদ্দেশ্য |
|------|---------|
| **এনপিএম / সুতা / পিএনপিএম** | প্যাকেজ ম্যানেজার |
| **টাইপস্ক্রিপ্ট** | জাভাস্ক্রিপ্টের টাইপ করা সুপারসেট |
| **ইএসলিন্ট** | কোড লিন্টিং |
| **সুন্দর** | কোড ফরম্যাটিং |
| **ভিট** | দ্রুত বিল্ড টুল এবং ডেভ সার্ভার |
| **ওয়েবপ্যাক** | মডিউল বান্ডলার (পরিপক্ক, ব্যাপকভাবে ব্যবহৃত) |
| **বিদ্রূপ/বিদ্রূপ** | পরীক্ষার কাঠামো |
---

## কখন জাভাস্ক্রিপ্ট ব্যবহার করবেন
| দৃশ্যকল্প | কেন জাভাস্ক্রিপ্ট | ভাল বিকল্প |
|------------|---------------|---------|
| ওয়েব ফ্রন্টএন্ড | ব্রাউজার-ভিত্তিক UI এর জন্য একমাত্র বিকল্প | — |
| ফুল-স্ট্যাক ওয়েব | সর্বত্র একই ভাষা | টাইপ নিরাপত্তার জন্য TypeScript |
| রিয়েল-টাইম অ্যাপস (চ্যাট, গেম) | ইভেন্ট-চালিত, নন-ব্লকিং I/O | — |
| সার্ভারহীন ফাংশন | দ্রুত লিখতে, যে কোনো জায়গায় স্থাপন করুন | পাইথন, গো |
| মোবাইল অ্যাপস (প্রতিক্রিয়া নেটিভ) | ওয়েবের সাথে কোড শেয়ার করুন | ফ্লটার, নেটিভ সুইফট/কোটলিন |
| ডেস্কটপ অ্যাপস (ইলেক্ট্রন) | ওয়েব প্রযুক্তির সাথে ক্রস-প্ল্যাটফর্ম | C# (WPF), টাউরি (মরিচা) |
| CPU- নিবিড় গণনা | একক-থ্রেডেড সীমাবদ্ধতা | পাইথন (NumPy), C++, মরিচা, WebAssembly |
| সিস্টেম প্রোগ্রামিং | ভুল বিমূর্ততা স্তর | C, C++, Rust, Go |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: `var`, `let`, এবং`const`এর মধ্যে পার্থক্য কী এবং আমার প্রতিটি কখন ব্যবহার করা উচিত?
**A:**`var`ফাংশন-স্কোপড এবং উত্তোলিত — আধুনিক কোডে এটি এড়িয়ে চলুন। `let`ব্লক-স্কোপড এবং পুনরায় নিয়োগের অনুমতি দেয়। `const`ব্লক-স্কোপড এবং পুনরায় অ্যাসাইনমেন্ট প্রতিরোধ করে (কিন্তু অবজেক্ট/অ্যারে এর রেফারেন্স এখনও পরিবর্তনযোগ্য)। সর্বোত্তম অনুশীলন: `const`-এ ডিফল্ট, আপনার পুনরায় নিয়োগের প্রয়োজন হলেই`let`ব্যবহার করুন,`var`কখনই ব্যবহার করবেন না।
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### প্রশ্ন 2: জাভাস্ক্রিপ্টে`this`কীভাবে কাজ করে এবং কেন এটি এত বিভ্রান্তিকর?
**A:**`this`নির্ধারণ করা হয় **কীভাবে একটি ফাংশন বলা হয়** দ্বারা, যেখানে এটি সংজ্ঞায়িত করা হয়েছে তা নয়। একটি পদ্ধতি কলে,`this`হল অবজেক্ট। একটি স্বতন্ত্র কলে, এটি হল`undefined`(কঠোর মোড) বা`global`(অ-কঠোর)৷ তীর ফাংশনগুলি তাদের এনক্লোজিং স্কোপ থেকে`this`উত্তরাধিকারসূত্রে পায় — এই কারণেই তারা কলব্যাকের জন্য পছন্দ করে।`this`স্পষ্টভাবে সেট করতে`.bind()`ব্যবহার করুন৷
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

### প্রশ্ন 3: ইভেন্ট লুপ কি, এবং কিভাবে async/await আসলে কাজ করে?
**A:** জাভাস্ক্রিপ্ট একটি ইভেন্ট লুপের সাথে একক-থ্রেডেড যা একটি সারি প্রক্রিয়া করে। কল স্ট্যাক সিঙ্ক্রোনাস কোড নির্বাহ করে। যখন এটি খালি থাকে, ইভেন্ট লুপ মাইক্রোটাস্ক সারি (প্রতিশ্রুতি) বা ম্যাক্রোটাস্ক সারি (সেটটাইমআউট, I/O) থেকে পরবর্তী কাজটি বেছে নেয়। `async/await`হল প্রতিশ্রুতির উপর সিনট্যাক্টিক সুগার —`await`অ্যাসিঙ্ক ফাংশনকে বিরতি দেয় এবং থ্রেড ব্লক না করেই যখন প্রতিশ্রুতি সমাধান হয় তখন পুনরায় শুরু হয়।
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

### প্রশ্ন 4: আধুনিক জাভাস্ক্রিপ্টে আমি কীভাবে ত্রুটিগুলি পরিচালনা করব?
**A:** সিঙ্ক্রোনাস কোডের জন্য`try/catch`এবং অ্যাসিঙ্ক্রোনাস কোডের জন্য`async/await`এর সাথে`.catch()`বা`try/catch`ব্যবহার করুন। সর্বদা প্রতিশ্রুতি প্রত্যাখ্যানগুলি পরিচালনা করুন — আন-হ্যান্ডেলড প্রত্যাখ্যান ক্র্যাশ Node.js। ডোমেন-নির্দিষ্ট ত্রুটির জন্য কাস্টম ত্রুটি ক্লাস তৈরি করুন। একটি নিরাপত্তা জাল হিসাবে একটি বিশ্বব্যাপী ত্রুটি হ্যান্ডলার ব্যবহার করুন.
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

### প্রশ্ন 5: প্লেইন অবজেক্ট/অ্যারের পরিবর্তে আমার কখন`Map`/`Set`ব্যবহার করা উচিত?
**A:**`Map`ব্যবহার করুন যখন কীগুলি স্ট্রিং না হয়, যখন আপনার সন্নিবেশ-অর্ডার পুনরাবৃত্তির প্রয়োজন হয়, যখন আপনার প্রয়োজন হয়`.size`, বা যখন আপনি ঘন ঘন এন্ট্রি যোগ/সরান (অবজেক্টের চেয়ে ভাল পারফরম্যান্স)। O(1) লুকআপ সহ অনন্য সংগ্রহের জন্য`Set`ব্যবহার করুন — বড় ডেটাসেটের জন্য`array.includes()`থেকে অনেক দ্রুত। সাধারণ JSON-সিরিয়ালাইজেবল ডেটা এবং স্ট্রিং কী সহ ছোট কী-মানের মানচিত্রগুলির জন্য প্লেইন অবজেক্ট ব্যবহার করুন।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি ডিবাউন্স ফাংশন প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি`debounce`ইউটিলিটি প্রয়োগ করুন যা শেষবার কল করার পর থেকে একটি নির্দিষ্ট অপেক্ষার সময় অতিবাহিত না হওয়া পর্যন্ত একটি ফাংশন শুরু করতে বিলম্ব করে। লিডিং এবং ট্রেইলিং এজ ইনভোকেশন উভয়কেই সমর্থন করুন।
**ধাপ 1 — সমস্যাটি বুঝুন:**
একটি ডিবাউন্সড ফাংশন দ্রুত ক্রমাগত কলগুলিকে উপেক্ষা করে এবং অপেক্ষার সময়কালের জন্য কলগুলি বন্ধ হয়ে যাওয়ার পরে শুধুমাত্র ফায়ার করে। "লিডিং এজ" মানে প্রথম কলে অবিলম্বে আগুন। "ট্রেলিং এজ" মানে অপেক্ষার পর আগুন। আমাদের উভয় মোড পরিচালনা করতে হবে এবং বাতিলকরণকে সমর্থন করতে হবে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি বন্ধ একটি টাইমার আইডি সংরক্ষণ করুন.
- প্রতিটি কলে: বিদ্যমান টাইমার সাফ করুন, তারপর একটি নতুন`setTimeout`সেট করুন৷
- অগ্রণী প্রান্তের জন্য: টাইমার সক্রিয় না থাকলে অবিলম্বে কল করুন।
- একটি`.cancel()`পদ্ধতির সাথে একটি ডিবাউন্সড ফাংশন ফেরত দিন৷
- তীর ফাংশন বা`.apply()`ব্যবহার করে`this`প্রসঙ্গ এবং আর্গুমেন্টগুলি সংরক্ষণ করুন৷
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- বন্ধ বিশ্বব্যাপী সুযোগ দূষণ ছাড়া কল জুড়ে রাষ্ট্র সংরক্ষণ করে.
-`setTimeout`এর আগে`clearTimeout`শুধুমাত্র শেষ কল ট্রিগার এক্সিকিউশন নিশ্চিত করে।
-`.cancel()`পরিষ্কারের জন্য গুরুত্বপূর্ণ (যেমন, প্রতিক্রিয়াতে উপাদান আনমাউন্ট)।
- এজ কেস: যদি`wait`0 হয়, ফাংশনটি পরবর্তী ইভেন্ট লুপ টিক-এ ফায়ার করে — DOM আপডেটগুলি ব্যাচ করার জন্য দরকারী৷
### সমস্যা 2: একটি প্রতিশ্রুতি-ভিত্তিক হার লিমিটার তৈরি করুন
**সমস্যা বিবৃতি:** একটি রেট লিমিটার তৈরি করুন যা প্রতি টাইম উইন্ডোতে সর্বাধিক N অনুরোধের অনুমতি দেয়। এটি সেই প্রতিশ্রুতিগুলি ফেরত দেবে যা সমাধান করে যখন কলকারীকে এগিয়ে যাওয়ার অনুমতি দেওয়া হয়, এবং অতিরিক্ত অনুরোধগুলি সারিবদ্ধ করে৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের একটি স্লাইডিং বা স্থির উইন্ডো দরকার যা ট্র্যাক করে কতগুলি কল করা হয়েছে৷ সীমা পৌঁছে গেলে, নতুন কলগুলি সারিবদ্ধ হওয়া উচিত এবং একটি স্লট খোলা হলে সমাধান করা উচিত৷ এটি "টোকেন বাকেট" প্যাটার্ন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি অ্যারেতে সাম্প্রতিক কলগুলির টাইমস্ট্যাম্পগুলি ট্র্যাক করুন৷
- প্রতিটি কলে: উইন্ডোর চেয়ে পুরানো টাইমস্ট্যাম্পগুলি সরান, গণনা < সীমা আছে কিনা তা পরীক্ষা করুন।
- সীমার নিচে থাকলে: অবিলম্বে সমাধান করুন।
- যদি সীমা থাকে: প্রাচীনতম টাইমস্ট্যাম্পের মেয়াদ শেষ হলে গণনা করুন, একটি`setTimeout`সেট করুন, তারপর সমাধান করুন৷
- অপেক্ষমাণ কলারদের জন্য একটি সারি (সমাধান ফাংশনের অ্যারে) ব্যবহার করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- স্লাইডিং উইন্ডো অ্যাপ্রোচ স্থির জানালার চেয়ে ফর্সা (জানালার সীমানায় কোনো বিস্ফোরণ নেই)।
- সারি প্রক্রিয়াকরণ হল FIFO — কলারদের ক্রমানুসারে পরিবেশন করা হয়।
- উৎপাদনের জন্য:`AbortController`সমর্থন যোগ করুন যাতে কলকারীরা অপেক্ষা বাতিল করতে পারে।
- কর্মক্ষমতা:`_cleanOldTimestamps`হল প্রতি কলে O(n) কিন্তু n হল`maxCalls`দ্বারা আবদ্ধ৷
### সমস্যা 3: একটি গভীর ক্লোন ফাংশন প্রয়োগ করুন
**সমস্যা বিবৃতি:** এমন একটি ফাংশন লিখুন যা যেকোনো জাভাস্ক্রিপ্ট মানকে গভীরভাবে ক্লোন করে, হ্যান্ডলিং অবজেক্ট, অ্যারে, তারিখ, RegExps, মানচিত্র, সেট, সার্কুলার রেফারেন্স এবং টাইপ করা অ্যারে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
`JSON.parse(JSON.stringify(obj))`এতে ব্যর্থ হয়:`undefined`, ফাংশন, প্রতীক, তারিখ (স্ট্রিং হয়ে যায়), RegExps (খালি বস্তু হয়ে যায়), মানচিত্র, সেট, সার্কুলার রেফারেন্স (থ্রো), এবং টাইপ করা অ্যারে। আমাদের একটি পুনরাবৃত্তিমূলক সমাধান দরকার যা পরিদর্শন করা বস্তুগুলিকে ট্র্যাক করে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- ইতিমধ্যে-ক্লোন করা বস্তুগুলি ট্র্যাক করতে একটি`Map`ব্যবহার করুন (বৃত্তাকার রেফারেন্স পরিচালনা করে)।
- প্রতিটি প্রকার বিশেষভাবে পরিচালনা করুন: তারিখ → নতুন তারিখ, RegExp → নতুন RegExp, মানচিত্র → ক্লোন করা এন্ট্রি সহ নতুন মানচিত্র, সেট → নতুন ক্লোন মান সহ সেট৷
- আধুনিক অন্তর্নির্মিত বিকল্প হিসাবে`structuredClone()`ব্যবহার করুন (ব্রাউজার এবং Node.js 17+ এ উপলব্ধ)।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- সার্কুলার রেফারেন্স:`seen`মানচিত্র অসীমভাবে পুনরাবৃত্তি করার পরিবর্তে ইতিমধ্যে তৈরি করা ক্লোন ফিরিয়ে দেয়।
- সম্পত্তি বর্ণনাকারী:`Reflect.ownKeys`+`getOwnPropertyDescriptor`গেটার, সেটার্স এবং অ-গণনাযোগ্য বৈশিষ্ট্য সংরক্ষণ করে।
- আধুনিক বিকল্প:`structuredClone(value)`নেটিভভাবে (ফাংশন এবং DOM নোড ব্যতীত) বেশিরভাগ ক্ষেত্রেই পরিচালনা করে। উপলব্ধ হলে এটি পছন্দ করুন।
- কর্মক্ষমতা: সাধারণ বস্তুর জন্য,`JSON.parse(JSON.stringify(obj))`এখনও দ্রুততম। আপনার আসলে এটির প্রয়োজন হলেই ডিপ ক্লোন ব্যবহার করুন।
### সমস্যা 4: একটি সাধারণ ইভেন্ট ইমিটার তৈরি করুন
**সমস্যা বিবৃতি:**`on`,`off`,`emit`, এবং`once`পদ্ধতিগুলিকে সমর্থন করে এমন একটি ইভেন্ট ইমিটার ক্লাস প্রয়োগ করুন৷ শ্রোতাদের রেজিস্ট্রেশন অর্ডারে ডাকতে হবে। `emit`সমস্ত শ্রোতার কাছে আর্গুমেন্ট পাস করা উচিত।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের একটি পাব/সাব সিস্টেম দরকার: নামযুক্ত ইভেন্টগুলির জন্য শ্রোতাদের নিবন্ধন করুন, নির্দিষ্ট শ্রোতাদের সরিয়ে দিন, যুক্তি দিয়ে ইভেন্টগুলি ট্রিগার করুন এবং এককালীন শ্রোতাদের সমর্থন করুন৷ এটি Node.js-এ ব্যাপকভাবে ব্যবহৃত পর্যবেক্ষক প্যাটার্ন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি`Map<string, Array<Function>>`এ শ্রোতাদের সঞ্চয় করুন৷
- `on`: শ্রোতাকে অ্যারেতে ঠেলে দিন।
-`off`: অ্যারে থেকে নির্দিষ্ট শ্রোতাকে ফিল্টার করুন।
-`emit`: অ্যারে পুনরাবৃত্তি করুন এবং স্প্রেড আর্গুমেন্ট সহ প্রতিটি শ্রোতাকে কল করুন।
-`once`: একটি ফাংশনে শ্রোতাকে মোড়ানো যা প্রথম কলের পরে নিজেকে সরিয়ে দেয়।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- `emit`-এ`[...listeners]`অনুলিপি যখন পুনরাবৃত্তির সময় একজন শ্রোতা`off`কল করে তখন সমস্যাগুলি প্রতিরোধ করে৷
-`once``_original` সঞ্চয় করে যাতে কলকারীরা`off(event, originalFn)`এর মাধ্যমে র‍্যাপারটি সরাতে পারে৷
- ব্যক্তিগত ক্ষেত্র (`#listeners`) অভ্যন্তরীণ অবস্থার বাহ্যিক মিউটেশন প্রতিরোধ করে।
- উৎপাদনের জন্য:`maxListeners`সতর্কতা (Node.js এর মত), শ্রোতা প্রতি ত্রুটি পরিচালনা, এবং অগ্রাধিকারের জন্য`prependListener`যোগ করুন।
---

## সারাংশ
জাভাস্ক্রিপ্ট অনিবার্য। এটি একমাত্র ভাষা যা ওয়েব ব্রাউজারে চলে, এটি ফ্রন্টএন্ড বিকাশের জন্য অপরিহার্য করে তোলে। Node.js এর সাথে, এটি সার্ভারের দিকে প্রসারিত হয় এবং রিঅ্যাক্ট নেটিভ এবং ইলেকট্রনের মতো ফ্রেমওয়ার্কের সাথে এটি মোবাইল এবং ডেস্কটপে পৌঁছায়। ইকোসিস্টেম প্রোগ্রামিং এর মধ্যে সবচেয়ে বড়। ভাষার ব্যঙ্গগুলি সুপরিচিত এবং পরিচালনাযোগ্য — এবং টাইপস্ক্রিপ্ট টাইপিং সংক্রান্ত উদ্বেগগুলিকে সমাধান করে৷ একটি ব্রাউজারে চলে এমন যেকোনো কিছুর জন্য, JavaScript শুধুমাত্র সেরা পছন্দ নয় - এটি একমাত্র পছন্দ।