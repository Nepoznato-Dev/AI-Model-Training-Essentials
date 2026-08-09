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

#จาวาสคริปต์
JavaScript เป็นภาษาโปรแกรมที่มีการตีความแบบไดนามิก สร้างขึ้นโดย Brendan Eich ภายในเวลาเพียง 10 วันในปี 1995 เดิมทีออกแบบมาเพื่อเพิ่มการโต้ตอบให้กับหน้าเว็บ และได้เติบโตขึ้นเป็นภาษาโปรแกรมที่ใช้กันอย่างแพร่หลายมากที่สุดในโลก JavaScript ทำงานในทุกเว็บเบราว์เซอร์ บนเซิร์ฟเวอร์ผ่าน Node.js ในแอปเดสก์ท็อป (Electron) แอปมือถือ (React Native) และแม้แต่ระบบฝังตัว
ภาษามีความพิเศษตรงที่เป็นตัวเลือกเดียวสำหรับการพัฒนาเว็บฝั่งไคลเอ็นต์ — ทุกเบราว์เซอร์รองรับภาษานี้โดยกำเนิด การผูกขาดนี้เมื่อรวมกับการเพิ่มขึ้นของ JavaScript แบบเต็มสแต็ก (Node.js, Deno, Bun) ทำให้เป็นสิ่งที่ขาดไม่ได้
---

## ทำไม JavaScript ถึงมีความสำคัญ
- **ภาษาของเว็บ**: ภาษาเดียวที่ทำงานในเบราว์เซอร์ ไม่มีทางเลือกอื่นสำหรับส่วนหน้า
- **ความสามารถเต็มสแต็ก**: ภาษาเดียวกันบนส่วนหน้า (React, Vue, Svelte) และแบ็กเอนด์ (Node.js, Express, Fastify)
- **ระบบนิเวศขนาดใหญ่**: npm มีแพ็คเกจมากกว่า 2 ล้านแพ็คเกจ ซึ่งเป็นการลงทะเบียนซอฟต์แวร์ที่ใหญ่ที่สุดในโลก
- **ความอเนกประสงค์**: เว็บแอป แอปมือถือ (React Native) แอปเดสก์ท็อป (Electron) IoT ฟังก์ชันไร้เซิร์ฟเวอร์
- **อุปสรรคในการเข้าต่ำ**: ทำงานได้ในทุกเบราว์เซอร์ — ไม่จำเป็นต้องติดตั้งเพื่อเริ่มเขียนโค้ด
- **อะซิงโครนัสตามการออกแบบ**: I/O ที่ขับเคลื่อนด้วยเหตุการณ์และไม่มีการบล็อกทำให้เป็นเลิศสำหรับแอปพลิเคชันแบบเรียลไทม์
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ข้อผิดพลาดในการพิมพ์แบบไดนามิก** | ไม่มีการตรวจสอบประเภทเวลาคอมไพล์ ข้อบกพร่องปรากฏขึ้นที่รันไทม์ | ใช้ TypeScript (ซูเปอร์เซ็ตที่พิมพ์ของ JavaScript) |
| **ความซับซ้อนในการโทรกลับ** | การโทรกลับที่ซ้อนกันอาจไม่สามารถอ่านได้ ("callback hell") | ใช้ Promises และ async/await |
| **ความหมายที่แปลก** | `==`กับ `===`,`this`การเชื่อมโยง, การยก, การบีบบังคับประเภท | เรียนรู้นิสัยใจคอ; ใช้ ESLint; ชอบ`const`/`let`มากกว่า`var`|
| **เธรดเดียว** | งานที่เชื่อมโยงกับ CPU จะบล็อกเหตุการณ์วนซ้ำ | ใช้ Web Workers, เธรดของผู้ปฏิบัติงาน หรือออฟโหลดไปยังโมดูลดั้งเดิม |
| **คุณภาพแพ็คเกจ** | การเปิดกว้างของ npm หมายถึงคุณภาพที่ไม่สอดคล้องกันและความเสี่ยงด้านความปลอดภัย | การพึ่งพาการตรวจสอบ ใช้ไฟล์ล็อค ชอบแพ็คเกจที่ได้รับการดูแลอย่างดี |
---

## พื้นฐานไวยากรณ์
### ตัวแปรและประเภท
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

### ฟังก์ชั่น
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

### วัตถุและคลาส
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

### การเขียนโปรแกรมแบบอะซิงโครนัส
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

### โมดูล
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

## ไวยากรณ์และรูปแบบขั้นสูง
### การทำลายล้าง & การแพร่กระจาย/การพักผ่อน (เจาะลึก)
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

### ผู้รับมอบฉันทะและการไตร่ตรอง
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

### สัญลักษณ์ ตัววนซ้ำ และเครื่องกำเนิดไฟฟ้า
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

### ลำดับชั้นข้อผิดพลาดที่กำหนดเอง
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

## การเห็นพ้องต้องกันและความเท่าเทียม
JavaScript เป็นแบบเธรดเดียวพร้อมลูปเหตุการณ์ การทำงานพร้อมกันทำได้ผ่านรูปแบบอะซิงโครนัส Web Workers และ (ใน Node.js) โมดูล worker_threads
### ห่วงเหตุการณ์
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

### เธรดผู้ปฏิบัติงาน (Node.js — งานที่เชื่อมโยงกับ CPU)
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

### พนักงานเว็บ (เบราว์เซอร์)
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

### รูปแบบอะซิงก์
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างไดเรกทอรีโครงการ
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

### การกำหนดค่าบิวด์ — `package.json`
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

### การกำหนดค่า Linting และการจัดรูปแบบ
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

### ไปป์ไลน์ CI/CD — การดำเนินการ GitHub
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

## การทดสอบ
### ทดสอบกับเจสท์
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

### การทดสอบการเยาะเย้ยและบูรณาการ
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

## การทำงานร่วมกัน
### ส่วนเสริมดั้งเดิมพร้อม N-API (Node.js)
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

### การเรียกไลบรารี C ด้วย ffi-napi
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

## รูปแบบการออกแบบ
### รูปแบบโมดูล (การห่อหุ้ม)
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

### รูปแบบผู้สังเกตการณ์ / ตัวส่งสัญญาณเหตุการณ์
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

### รูปแบบตัวสร้าง
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### ด็อคเกอร์ไฟล์
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

### การใช้งานเฉพาะแพลตฟอร์ม
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

## ระบบนิเวศ
### กรอบการทำงานส่วนหน้า
| กรอบ | วิธีการ | ดีที่สุดสำหรับ |
|----------|----------|----------|
| **โต้ตอบ** | DOM เสมือนแบบอิงคอมโพเนนต์ | สปาขนาดใหญ่ ระบบนิเวศที่ใหญ่ที่สุด |
| **วิว** | แบบก้าวหน้าตามเทมเพลต | การยอมรับอย่างค่อยเป็นค่อยไป; ประสบการณ์นักพัฒนาที่ยอดเยี่ยม |
| **เรียบหรู** | เวลาคอมไพล์ ไม่มี DOM เสมือน | บันเดิลเล็กกว่า, โค้ดง่ายกว่า |
| **เชิงมุม** | กรอบงานแบบเต็ม TypeScript-first | แอพระดับองค์กร โครงสร้างดื้อดึง |
| **Next.js** | ตอบสนองเมตาเฟรมเวิร์ก (SSR / SSG) | แอป Production React พร้อม SEO |
### แบ็กเอนด์ (Node.js)
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **ด่วน** | กรอบงานเว็บขั้นต่ำและยืดหยุ่น (ยอดนิยมที่สุด) |
| **อดอาหาร** | กรอบงานเว็บประสิทธิภาพสูง |
| **NestJS** | สถาปัตยกรรมระดับองค์กรที่ได้แรงบันดาลใจเชิงมุม |
| **โคอา** | ทางเลือก Express น้ำหนักเบา ทันสมัย ​​|
| **โฮโน** | รันไทม์หลายรันไทม์ที่รวดเร็วเป็นพิเศษ (Node, Deno, Bun, edge) |
### รันไทม์
| รันไทม์ | คำอธิบาย |
|---------|-------------|
| **Node.js** | รันไทม์ JavaScript ฝั่งเซิร์ฟเวอร์ดั้งเดิม (เอ็นจิ้น V8) |
| **ดีโน่** | ปลอดภัยตามค่าเริ่มต้น รองรับ TypeScript ดั้งเดิม สร้างโดยผู้เขียนดั้งเดิมของ Node |
| **บุญ** | รันไทม์, Bundler และตัวจัดการแพ็คเกจแบบออลอินวันที่รวดเร็วเป็นพิเศษ |
### เครื่องมือสำคัญ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **npm / เส้นด้าย / pnpm** | ผู้จัดการแพ็คเกจ |
| **TypeScript** | พิมพ์ superset ของ JavaScript |
| **ESLint** | รหัสขุย |
| **สวยกว่า** | การจัดรูปแบบโค้ด |
| **เยี่ยม** | เครื่องมือสร้างที่รวดเร็วและเซิร์ฟเวอร์ dev |
| **เว็บแพ็ค** | Bundler โมดูล (แก่แล้ว ใช้กันอย่างแพร่หลาย) |
| **Jest / Vitest** | กรอบการทดสอบ |
---

## เมื่อใดจึงควรใช้ JavaScript
| สถานการณ์ | ทำไมต้องจาวาสคริปต์ | ทางเลือกที่ดีกว่า |
|----------|---------------|-------------------|
| ส่วนหน้าของเว็บ | ตัวเลือกเดียวสำหรับ UI ที่ใช้เบราว์เซอร์ | — |
| เว็บเต็มกอง | ภาษาเดียวกันทุกที่ | TypeScript เพื่อความปลอดภัยประเภท |
| แอพแบบเรียลไทม์ (แชท, เกม) | I/O | ที่ขับเคลื่อนด้วยเหตุการณ์และไม่ปิดกั้น — |
| ฟังก์ชั่นไร้เซิร์ฟเวอร์ | เขียนเร็ว ปรับใช้ได้ทุกที่ | Python ไป |
| แอพมือถือ (React Native) | แชร์โค้ดกับเว็บ | Flutter, Swift/Kotlin |
| แอพเดสก์ท็อป (อิเล็กตรอน) | ข้ามแพลตฟอร์มด้วยเทคโนโลยีเว็บ | C# (WPF), Tauri (สนิม) |
| การคำนวณที่เน้น CPU | ข้อจำกัดแบบเธรดเดียว | Python (NumPy), C++, Rust, WebAssembly |
| การเขียนโปรแกรมระบบ | ระดับนามธรรมผิด | C, C++, สนิม, ไป |
---

## สรุป
จาวาสคริปต์เป็นสิ่งที่หลีกเลี่ยงไม่ได้ มันเป็นภาษาเดียวที่ทำงานบนเว็บเบราว์เซอร์ ทำให้จำเป็นสำหรับการพัฒนาส่วนหน้า ด้วย Node.js มันขยายไปถึงฝั่งเซิร์ฟเวอร์ และด้วยเฟรมเวิร์ก เช่น React Native และ Electron มันเข้าถึงมือถือและเดสก์ท็อป ระบบนิเวศเป็นระบบนิเวศที่ใหญ่ที่สุดในการเขียนโปรแกรม นิสัยใจคอของภาษานั้นเป็นที่รู้จักและจัดการได้ และ TypeScript จัดการกับปัญหาการพิมพ์ สำหรับทุกสิ่งที่ทำงานในเบราว์เซอร์ JavaScript ไม่ได้เป็นเพียงตัวเลือกที่ดีที่สุดเท่านั้น แต่ยังเป็นทางเลือกเดียวอีกด้วย