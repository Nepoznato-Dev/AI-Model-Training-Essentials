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
#جافا سكريبت
JavaScript هي لغة برمجة ديناميكية ومفسرة أنشأها Brendan Eich في 10 أيام فقط في عام 1995. وقد تم تصميمها في الأصل لإضافة التفاعل إلى صفحات الويب، وقد تطورت لتصبح لغة البرمجة الأكثر استخدامًا في العالم. يتم تشغيل JavaScript في كل متصفح ويب، وعلى الخوادم عبر Node.js، وفي تطبيقات سطح المكتب (Electron)، وتطبيقات الهاتف المحمول (React Native)، وحتى الأنظمة المدمجة.
تعتبر اللغة فريدة من نوعها من حيث أنها الخيار الوحيد لتطوير الويب من جانب العميل - حيث يدعمها كل متصفح محليًا. هذا الاحتكار، جنبًا إلى جنب مع ظهور JavaScript الكامل (Node.js، وDeno، وBun)، يجعله أمرًا لا غنى عنه.
---

## لماذا يهم جافا سكريبت
- **لغة الويب**: اللغة الوحيدة التي تعمل أصلاً في المتصفحات. لا يوجد بديل للواجهة الأمامية.
- **إمكانية التكديس الكامل**: نفس اللغة على الواجهة الأمامية (React وVue وSvelte) والواجهة الخلفية (Node.js وExpress وFastify).
- **نظام بيئي ضخم**: يحتوي npm على أكثر من 2 مليون حزمة — وهو أكبر سجل برامج في العالم.
- **التنوع**: تطبيقات الويب، وتطبيقات الهاتف المحمول (React Native)، وتطبيقات سطح المكتب (Electron)، وإنترنت الأشياء، والوظائف بدون خادم.
- **عائق دخول منخفض**: يعمل في أي متصفح — لا يلزم التثبيت لبدء البرمجة.
- **غير متزامن حسب التصميم**: الإدخال/الإخراج المبني على الأحداث وغير المحظور يجعله ممتازًا للتطبيقات في الوقت الفعلي.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **مزالق الكتابة الديناميكية** | لا يوجد فحص نوع وقت الترجمة؛ ظهور الأخطاء في وقت التشغيل | استخدم TypeScript (مجموعة شاملة مكتوبة من JavaScript) |
| **تعقيد رد الاتصال** | يمكن أن تصبح عمليات الاسترجاعات المتداخلة غير قابلة للقراءة ("جحيم رد الاتصال") | استخدم الوعود والمزامنة/الانتظار |
| ** دلالات ملتوية ** | `==`vs `===`،`this`ربط، رفع، نوع الإكراه | تعلم المراوغات. استخدم ESLint؛ تفضل`const`/`let`على`var`|
| ** خيط واحد ** | المهام المرتبطة بوحدة المعالجة المركزية تحظر حلقة الحدث | استخدم عمال الويب، أو سلاسل العمليات، أو قم بإلغاء التحميل إلى الوحدات النمطية الأصلية |
| **جودة العبوة** | إن انفتاح npm يعني عدم تناسق الجودة والمخاطر الأمنية | تبعيات التدقيق؛ استخدام ملفات القفل. تفضل الحزم التي يتم صيانتها جيدًا |
---

## أساسيات بناء الجملة
### المتغيرات والأنواع
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

### الوظائف
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

### الكائنات والفئات
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

### البرمجة غير المتزامنة
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

### الوحدات
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

## بناء الجملة والأنماط المتقدمة
### التدمير والانتشار/الراحة (الغوص العميق)
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

### الوكلاء والانعكاس
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

### الرموز والمكررات والمولدات
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

### التسلسل الهرمي للأخطاء المخصصة
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

## التزامن والتوازي
JavaScript عبارة عن خيط واحد مع حلقة حدث. يتم تحقيق التزامن من خلال الأنماط غير المتزامنة، وعمال الويب، و(في Node.js) وحدةworker_threads.
### حلقة الحدث
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

### سلاسل العمليات (Node.js — المهام المرتبطة بوحدة المعالجة المركزية)
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

### عمال الويب (المتصفح)
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

### أنماط غير متزامنة
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

## تكوين المشروع ونظام البناء
### هيكل دليل المشروع
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

### تكوين التكوين — `package.json`
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

### تكوين الفحص والتنسيق
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

### خط أنابيب CI/CD — إجراءات GitHub
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

## الاختبار
### الاختبار مع Jest
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

### اختبارات السخرية والتكامل
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

## إمكانية التشغيل البيني
### الإضافات الأصلية مع N-API (Node.js)
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

### الاتصال بمكتبات C باستخدام ffi-napi
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

## أنماط التصميم
### نمط الوحدة (التغليف)
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

### نمط باعث المراقب / الحدث
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

### نمط البناء
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

## الأداء والتحسين
### أدوات التنميط
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

### تقنيات التحسين
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

## النشر
### ملف دوكر
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

### النشر الخاص بالمنصة
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

## النظام البيئي
### أطر الواجهة الأمامية
| الإطار | النهج | الأفضل لـ |
|-----------|---------|----------|
| **رد** | DOM الظاهري القائم على المكونات | المنتجعات الصحية واسعة النطاق؛ أكبر نظام بيئي |
| **النظرة** | تقدمية، قائمة على القالب | التبني التدريجي تجربة مطور رائعة |
| **رشيق** | وقت الترجمة، لا يوجد DOM افتراضي | حزم أصغر، رمز أبسط |
| ** الزاوي ** | الإطار الكامل، TypeScript-first | تطبيقات المؤسسات؛ بنية رأي |
| **Next.js** | رد فعل إطار التعريف (SSR/SSG) | تطبيقات رد فعل الإنتاج مع SEO |
### الواجهة الخلفية (Node.js)
| الإطار | الغرض |
|-----------|--------|
| **اكسبرس** | إطار ويب بسيط ومرن (الأكثر شيوعًا) |
| **أصم** | إطار ويب عالي الأداء |
| **نيست جي إس** | بنية مستوحاة من الطراز المؤسسي |
| **كوا** | بديل سريع خفيف الوزن وحديث |
| **هونو** | سريع للغاية، متعدد أوقات التشغيل (Node، Deno، Bun، edge) |
### أوقات التشغيل
| وقت التشغيل | الوصف |
|---------|------------|
| **Node.js** | وقت تشغيل JavaScript الأصلي من جانب الخادم (محرك V8) |
| **دينو** | آمن بشكل افتراضي؛ دعم TypeScript الأصلي؛ تم إنشاؤها بواسطة المؤلف الأصلي لـ Node |
| ** كعكة ** | وقت تشغيل الكل في واحد، ومجمع حزم، ومدير حزم سريع للغاية |
### الأدوات الأساسية
| أداة | الغرض |
|------|---------|
| **npm/غزل/pnpm** | مدراء الحزم |
| ** تايب سكريبت ** | مجموعة شاملة مكتوبة من جافا سكريبت |
| ** إي إس لينت ** | فحص الكود |
| **أجمل** | تنسيق الكود |
| **فيت** | أداة بناء سريعة وخادم تطوير |
| **حزمة الويب** | وحدة تجميع الوحدات (ناضجة، مستخدمة على نطاق واسع) |
| ** الدعابة / فيتيست ** | أطر الاختبار |
---

## متى يجب استخدام جافا سكريبت
| السيناريو | لماذا جافا سكريبت | البديل الأفضل |
|----------|-------------|------------------|
| الواجهة الأمامية للويب | الخيار الوحيد لواجهة المستخدم المستندة إلى المتصفح | — |
| ويب مكدس كامل | نفس اللغة في كل مكان | TypeScript لسلامة النوع |
| تطبيقات الوقت الحقيقي (الدردشة والألعاب) | الإدخال/الإخراج | يحركه الحدث، وغير محظور — |
| وظائف بدون خادم | سريع الكتابة والنشر في أي مكان | بايثون، اذهب |
| تطبيقات الجوال (React Native) | مشاركة الكود مع الويب | رفرفة، لغة سويفت/كوتلين الأصلية |
| تطبيقات سطح المكتب (الكترون) | منصة مشتركة مع تكنولوجيا الويب | C# (WPF)، تاوري (الصدأ) |
| حساب مكثف لوحدة المعالجة المركزية | الحد من الخيوط المفردة | بايثون (NumPy)، C++، Rust، WebAssembly |
| برمجة النظم | مستوى تجريد خاطئ | C، C++، الصدأ، الذهاب |
---

## أسئلة وأجوبة اصطناعية
### Q1: ما الفرق بين`var`و`let`و`const`ومتى يجب أن أستخدم كلاً منهما؟
**أ:**`var`محدد ومرفوع على نطاق وظيفي — تجنبه في التعليمات البرمجية الحديثة. `let`محدد النطاق ويسمح بإعادة التعيين. `const`محدد النطاق ويمنع إعادة التعيين (لكن الكائنات/المصفوفات التي تشير إليها لا تزال قابلة للتغيير). أفضل الممارسات: الإعداد الافتراضي هو `const`، استخدم`let`فقط عندما تحتاج إلى إعادة التعيين، ولا تستخدم`var`مطلقًا.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### السؤال الثاني: كيف يعمل`this`في JavaScript، ولماذا يكون الأمر محيرًا جدًا؟
**A:** يتم تحديد`this`من خلال **كيفية استدعاء الدالة**، وليس من خلال مكان تعريفها. في استدعاء الأسلوب، يكون`this`هو الكائن. في المكالمة المستقلة، تكون`undefined`(الوضع الصارم) أو`global`(غير مقيد). ترث دوال السهم`this`من النطاق المحيط بها، ولهذا السبب يتم تفضيلها لعمليات الاسترجاعات. استخدم`.bind()`لتعيين`this`بشكل صريح.
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

### س3: ما هي حلقة الحدث، وكيف يعمل المزامنة/الانتظار فعليًا؟
**أ:** جافا سكريبت عبارة عن خيط واحد مع حلقة حدث تعالج قائمة الانتظار. يقوم مكدس الاستدعاءات بتنفيذ تعليمات برمجية متزامنة. عندما تكون فارغة، تختار حلقة الحدث المهمة التالية من قائمة انتظار المهام الدقيقة (الوعود) أو قائمة انتظار المهام الكبيرة (setTimeout، I/O). `async/await`عبارة عن السكر النحوي فوق الوعود - يقوم`await`بإيقاف وظيفة المزامنة مؤقتًا واستئنافها عندما يتم حل الوعد، دون حظر سلسلة الرسائل.
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

### Q4: كيف يجب أن أتعامل مع الأخطاء في JavaScript الحديثة؟
**أ:** استخدم`try/catch`للتعليمات البرمجية المتزامنة و`.catch()` أو`try/catch`مع`async/await`للتعليمات البرمجية غير المتزامنة. تعامل دائمًا مع حالات رفض الوعد - تؤدي حالات الرفض غير المعالجة إلى تعطل Node.js. إنشاء فئات خطأ مخصصة للأخطاء الخاصة بالمجال. استخدم معالج الأخطاء العالمي كشبكة أمان.
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

### س5: متى يجب علي استخدام`Map`/`Set`بدلاً من الكائنات/المصفوفات العادية؟
**أ:** استخدم`Map`عندما لا تكون المفاتيح عبارة عن سلاسل، أو عندما تحتاج إلى تكرار ترتيب الإدراج، أو عندما تحتاج إلى `.size`، أو عندما تقوم بإضافة/إزالة إدخالات بشكل متكرر (أداء أفضل من الكائنات). استخدم`Set`للمجموعات الفريدة باستخدام بحث O(1) - أسرع بكثير من`array.includes()`لمجموعات البيانات الكبيرة. استخدم كائنات عادية لبيانات JSON البسيطة القابلة للتسلسل وخرائط القيمة الرئيسية الصغيرة مع مفاتيح السلسلة.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة 1: تنفيذ وظيفة الارتداد
**بيان المشكلة:** قم بتنفيذ الأداة المساعدة`debounce`التي تؤخر استدعاء دالة حتى بعد انقضاء فترة انتظار محددة منذ آخر مرة تم استدعاؤها. دعم كل من استدعاء الحافة الأمامية والزائدة.
**الخطوة الأولى — فهم المشكلة:**
تتجاهل الوظيفة المرتدة المكالمات المتعاقبة السريعة ولا يتم تشغيلها إلا بعد توقف المكالمات طوال مدة الانتظار. "الحافة الأمامية" تعني إطلاق النار فورًا عند المكالمة الأولى. "الحافة الخلفية" تعني الحريق بعد فترة الانتظار. نحن بحاجة إلى التعامل مع كلا الوضعين وكذلك دعم الإلغاء.
**الخطوة الثانية — تحديد النهج:**
- تخزين معرف الموقت في الإغلاق.
- في كل مكالمة: امسح المؤقت الحالي، ثم قم بتعيين`setTimeout`جديد.
- بالنسبة للحافة الأمامية: اتصل فورًا إذا لم يكن هناك مؤقت نشط.
- إرجاع دالة مرتجعة بطريقة `.cancel()`.
- الحفاظ على سياق ووسائط`this`باستخدام وظائف الأسهم أو`.apply()`.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- يحافظ الإغلاق على الحالة عبر المكالمات دون تلويث النطاق العالمي.
- يضمن`clearTimeout`قبل`setTimeout`تنفيذ المكالمة الأخيرة فقط.
-`.cancel()`مهم للتنظيف (على سبيل المثال، إلغاء تحميل المكون في React).
- حالة الحافة: إذا كانت قيمة`wait`تساوي 0، فسيتم تشغيل الوظيفة عند علامة حلقة الحدث التالية - وهي مفيدة لتجميع تحديثات DOM.
### المشكلة الثانية: إنشاء محدد للمعدل على أساس الوعد
**بيان المشكلة:** قم بإنشاء محدد معدل يسمح بحد أقصى N من الطلبات لكل نافذة زمنية. يجب أن يُرجع الوعود التي يتم حلها عندما يُسمح للمتصل بالمتابعة، ويضع الطلبات الزائدة في قائمة الانتظار.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى نافذة منزلقة أو ثابتة تتتبع عدد المكالمات التي تم إجراؤها. عند الوصول إلى الحد الأقصى، يجب وضع المكالمات الجديدة في قائمة الانتظار وحلها عند فتح الفتحة. هذا هو نمط "دلو الرمز المميز".
**الخطوة الثانية — تحديد النهج:**
- تتبع الطوابع الزمنية للمكالمات الأخيرة في المصفوفة.
- في كل مكالمة: قم بإزالة الطوابع الزمنية الأقدم من النافذة، وتحقق مما إذا كان العدد < الحد.
- إذا كان تحت الحد: حل على الفور.
- إذا كان عند الحد: احسب متى تنتهي صلاحية الطابع الزمني الأقدم، وقم بتعيين `setTimeout`، ثم قم بالحل.
- استخدم قائمة الانتظار (مجموعة من وظائف الحل) لانتظار المتصلين.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- تعتبر طريقة النافذة المنزلقة أكثر عدلاً من النوافذ الثابتة (لا يوجد انفجار عند حدود النافذة).
- معالجة قائمة الانتظار هي FIFO - يتم تقديم المتصلين بالترتيب.
- بالنسبة للإنتاج: أضف دعم`AbortController`حتى يتمكن المتصلون من إلغاء الانتظار.
- الأداء:`_cleanOldTimestamps`هو O(n) لكل مكالمة ولكن n يحده`maxCalls`.
### المشكلة 3: تنفيذ وظيفة الاستنساخ العميق
**بيان المشكلة:** اكتب دالة تستنسخ بشكل عميق أي قيمة JavaScript، وتتعامل مع الكائنات، والمصفوفات، والتواريخ، وRegExps، والخرائط، والمجموعات، والمراجع الدائرية، والمصفوفات المكتوبة.
**الخطوة الأولى — فهم المشكلة:**
 يفشل`JSON.parse(JSON.stringify(obj))`في:`undefined`والوظائف والرموز والتواريخ (تصبح سلاسل) وRegExps (تصبح كائنات فارغة) والخرائط والمجموعات والمراجع الدائرية (رميات) والمصفوفات المكتوبة. نحن بحاجة إلى حل عودي يتتبع الكائنات التي تمت زيارتها.
**الخطوة الثانية — تحديد النهج:**
- استخدم`Map`لتتبع الكائنات المستنسخة بالفعل (يتعامل مع المراجع الدائرية).
- التعامل مع كل نوع بشكل خاص: التاريخ → تاريخ جديد، RegExp → RegExp الجديد، خريطة → خريطة جديدة مع إدخالات مستنسخة، تعيين → مجموعة جديدة مع القيم المستنسخة.
- استخدم`structuredClone()`كبديل حديث مدمج (متوفر في المتصفحات وNode.js 17+).
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- المراجع الدائرية: تُرجع خريطة`seen`النسخة التي تم إنشاؤها بالفعل بدلاً من التكرار بلا حدود.
- واصفات الخاصية:`Reflect.ownKeys`+`getOwnPropertyDescriptor`يحافظ على الحروف، والمحددات، والخصائص غير القابلة للإحصاء.
- البديل الحديث: يتعامل`structuredClone(value)`مع معظم هذه الحالات محليًا (باستثناء الوظائف وعقد DOM). يفضل ذلك عند توفره.
- الأداء: بالنسبة للكائنات البسيطة، لا يزال`JSON.parse(JSON.stringify(obj))`هو الأسرع. استخدم الاستنساخ العميق فقط عندما تحتاج إليه بالفعل.
### المشكلة الرابعة: إنشاء باعث حدث بسيط
**بيان المشكلة:** تنفيذ فئة باعث الحدث التي تدعم الأساليب`on`و`off` و`emit` و`once`. وينبغي استدعاء المستمعين في أمر التسجيل.  يجب أن يقوم`emit`بتمرير الوسائط إلى جميع المستمعين.
**الخطوة الأولى — فهم المشكلة:**
نحن بحاجة إلى نظام نشر/فرعي: تسجيل المستمعين للأحداث المسماة، وإزالة مستمعين محددين، وتشغيل الأحداث باستخدام الوسائط، ودعم المستمعين لمرة واحدة. هذا هو نمط المراقب المستخدم على نطاق واسع في Node.js.
**الخطوة الثانية — تحديد النهج:**
- تخزين المستمعين في`Map<string, Array<Function>>`.
- `on`: دفع المستمع إلى المصفوفة.
- `off`: تصفية المستمع المحدد من المصفوفة.
- `emit`: قم بتكرار المصفوفة واستدعاء كل مستمع باستخدام وسائط الانتشار.
- `once`: التفاف المستمع في وظيفة تزيل نفسها بعد المكالمة الأولى.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- تمنع نسخة`[...listeners]`في`emit`حدوث مشكلات عندما يستدعي المستمع`off`أثناء التكرار.
- يقوم`once`بتخزين`_original`حتى يتمكن المتصلون من إزالة الغلاف عبر `off(event, originalFn)`.
- الحقول الخاصة (`#listeners`) تمنع التحول الخارجي للحالة الداخلية.
- بالنسبة للإنتاج: أضف تحذير`maxListeners`(مثل Node.js)، ومعالجة الأخطاء لكل مستمع، و`prependListener` للأولوية.
---

## ملخص
جافا سكريبت لا مفر منه. إنها اللغة الوحيدة التي تعمل في متصفحات الويب، مما يجعلها ضرورية لتطوير الواجهة الأمامية. مع Node.js، يمتد إلى جانب الخادم، ومع أطر عمل مثل React Native وElectron، يصل إلى الهاتف المحمول وسطح المكتب. النظام البيئي هو الأكبر في البرمجة. إن خصوصيات اللغة معروفة ويمكن التحكم فيها، ويعالج TypeScript مشكلات الكتابة. بالنسبة لأي شيء يتم تشغيله في المتصفح، فإن JavaScript ليس الخيار الأفضل فحسب، بل هو الخيار الوحيد.