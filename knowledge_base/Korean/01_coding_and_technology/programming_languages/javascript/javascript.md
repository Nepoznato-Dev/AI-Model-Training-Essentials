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
# 자바스크립트
JavaScript는 Brendan Eich가 1995년 단 10일 만에 만든 동적 해석 프로그래밍 언어입니다. 원래 웹 페이지에 상호 작용 기능을 추가하도록 설계되었으나 세계에서 가장 널리 사용되는 프로그래밍 언어로 성장했습니다. JavaScript는 모든 웹 브라우저, Node.js를 통한 서버, 데스크톱 앱(Electron), 모바일 앱(React Native) 및 임베디드 시스템에서 실행됩니다.
이 언어는 본질적으로 클라이언트 측 웹 개발을 위한 유일한 옵션이라는 점에서 독특합니다. 모든 브라우저는 기본적으로 이를 지원합니다. 풀스택 JavaScript(Node.js, Deno, Bun)의 등장과 결합된 이러한 독점은 이를 필수불가결하게 만듭니다.
---

## 자바스크립트가 중요한 이유
- **웹 언어**: 브라우저에서 기본적으로 실행되는 유일한 언어입니다. 프론트엔드에 대한 대안이 없습니다.
- **풀 스택 기능**: 프런트엔드(React, Vue, Svelte)와 백엔드(Node.js, Express, Fastify)에서 동일한 언어입니다.
- **거대한 생태계**: npm은 200만 개 이상의 패키지를 보유하고 있으며 이는 세계 최대 규모의 소프트웨어 레지스트리입니다.
- **다용성**: 웹 앱, 모바일 앱(React Native), 데스크톱 앱(Electron), IoT, 서버리스 기능.
- **낮은 진입 장벽**: 모든 브라우저에서 실행됩니다. 코딩을 시작하는 데 설치가 필요하지 않습니다.
- **비동기식 설계**: 이벤트 중심의 비차단 I/O는 실시간 애플리케이션에 탁월합니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **동적 타이핑의 함정** | 컴파일 타임 유형 검사가 없습니다. 런타임 시 버그 표면 | TypeScript 사용(JavaScript의 형식화된 상위 집합) |
| **콜백 복잡성** | 중첩된 콜백을 읽을 수 없게 될 수 있음("콜백 지옥") | 약속 및 async/await 사용 |
| **기발한 의미** | `==`대`===`,`this`바인딩, 호이스팅, 유형 강제 | 단점을 배우십시오. ESLint를 사용하십시오. `var`보다`const`/ `let`를 선호합니다 |
| **단일 스레드** | CPU 바인딩된 작업이 이벤트 루프를 차단합니다. | 웹 작업자, 작업자 스레드를 사용하거나 기본 모듈로 오프로드 |
| **패키지 품질** | npm의 개방성은 일관되지 않은 품질 및 보안 위험을 의미합니다 | 종속성을 감사합니다. 잠금 파일을 사용하십시오. 잘 관리된 패키지를 선호함 |
---

## 구문 기본 사항
### 변수 및 유형
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

### 기능
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

### 객체 및 클래스
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

### 비동기 프로그래밍
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

### 모듈
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

## 고급 구문 및 패턴
### 구조화 및 확산/휴식(심층 분석)
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

### 프록시 및 반사
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

### 기호, 반복자 및 생성기
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

### 사용자 정의 오류 계층 구조
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

## 동시성 및 병렬성
JavaScript는 이벤트 루프가 있는 단일 스레드입니다. 동시성은 비동기 패턴, 웹 작업자 및 (Node.js의) Worker_threads 모듈을 통해 달성됩니다.
### 이벤트 루프
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

### 작업자 스레드(Node.js — CPU 바인딩 작업)
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

### 웹 워커(브라우저)
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

### 비동기 패턴
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 디렉터리 구조
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

### 빌드 구성 — `package.json`
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

### 린팅 및 서식 지정 구성
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

### CI/CD 파이프라인 — GitHub Actions
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

## 테스트
### Jest로 테스트하기
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

### 모의 및 통합 테스트
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

## 상호 운용성
### N-API(Node.js)를 사용한 네이티브 애드온
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

### 웹어셈블리(Wasm)
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

### ffi-napi로 C 라이브러리 호출하기
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

## 디자인 패턴
### 모듈 패턴(캡슐화)
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

### 관찰자/이벤트 이미터 패턴
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

### 빌더 패턴
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

## 성능 및 최적화
### 프로파일링 도구
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

### 최적화 기술
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

## 배포
### 도커파일
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

### 플랫폼별 배포
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

## 생태계
### 프런트엔드 프레임워크
| 프레임워크 | 접근 | 최고의 대상 |
|------------|----------|----------|
| **반응** | 컴포넌트 기반, 가상 DOM | 대규모 SPA; 가장 큰 생태계 |
| **뷰** | 프로그레시브, 템플릿 기반 | 점진적인 채택; 훌륭한 개발자 경험 |
| **날씬한** | 컴파일 타임, 가상 DOM 없음 | 더 작은 번들, 더 간단한 코드 |
| **각도** | 전체 프레임워크, TypeScript 우선 | 기업용 앱 독선적인 구조 |
| **다음.js** | React 메타 프레임워크(SSR/SSG) | SEO를 사용한 프로덕션 React 앱 |
### 백엔드(Node.js)
| 프레임워크 | 목적 |
|------------|---------|
| **익스프레스** | 최소한의 유연한 웹 프레임워크(가장 인기 있음) |
| **고정** | 고성능 웹 프레임워크 |
| **NestJS** | 엔터프라이즈급, Angular 기반 아키텍처 |
| **코아** | 가볍고 현대적인 Express 대안 |
| **호노** | 초고속 멀티 런타임(Node, Deno, Bun, edge) |
### 런타임
| 런타임 | 설명 |
|---------|-------------|
| **Node.js** | 원래의 서버측 JavaScript 런타임(V8 엔진) |
| **데노** | 기본적으로 안전합니다. 기본 TypeScript 지원; Node의 원저작자가 만든 |
| **빵** | 초고속 올인원 런타임, 번들러 및 패키지 관리자 |
### 필수 도구
| 도구 | 목적 |
|------|---------|
| **npm / 원사 / pnpm** | 패키지 관리자 |
| **타입스크립트** | JavaScript의 유형화된 상위 집합 |
| **ESLint** | 코드 린팅 |
| **더 예쁘다** | 코드 서식 |
| **비테** | 빠른 빌드 도구 및 개발 서버 |
| **웹팩** | 모듈 번들러(성숙하고 널리 사용됨) |
| **Jest / Vitest** | 테스트 프레임워크 |
---

## JavaScript를 사용해야 하는 경우
| 시나리오 | 왜 자바스크립트인가 | 더 나은 대안 |
|------------|---------------|------|
| 웹 프론트엔드 | 브라우저 기반 UI 전용 옵션 | — |
| 풀스택 웹 | 어디서나 같은 언어 | 유형 안전성을 위한 TypeScript |
| 실시간 앱(채팅, 게임) | 이벤트 기반, 비차단 I/O | — |
| 서버리스 기능 | 빠른 작성, 어디서나 배포 | 파이썬, 바둑 |
| 모바일 앱(React Native) | 웹으로 코드 공유 | Flutter, 기본 Swift/Kotlin |
| 데스크탑 앱(Electron) | 웹 기술을 사용한 크로스 플랫폼 | C#(WPF), 타우리(Rust) |
| CPU 집약적인 계산 | 단일 스레드 제한 | Python(NumPy), C++, Rust, WebAssembly |
| 시스템 프로그래밍 | 잘못된 추상화 수준 | C, C++, 러스트, Go |
---

## 종합 Q&A
### Q1:`var`,`let`,`const`의 차이점은 무엇이며 언제 사용해야 하나요?
**A:** `var`는 함수 범위 및 호이스트이므로 최신 코드에서는 사용하지 마세요.  `let`는 블록 범위이며 재할당을 허용합니다.  `const`는 블록 범위이며 재할당을 방지합니다(그러나 참조하는 객체/배열은 여전히 ​​변경 가능합니다). 모범 사례: 기본값은`const`입니다. 재할당이 필요한 경우에만`let`를 사용하고`var`는 사용하지 마세요.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2: `this`는 JavaScript에서 어떻게 작동하며 왜 그렇게 혼란스럽습니까?
**A:** `this`는 함수가 정의된 위치가 아니라 **함수가 호출되는 방식**에 따라 결정됩니다. 메서드 호출에서는 `this`가 개체입니다. 독립형 호출에서는 `undefined`(엄격 모드) 또는 `global`(비엄격)입니다. 화살표 함수는 바깥쪽 범위에서 `this`를 상속합니다. 이것이 콜백에 선호되는 이유입니다. `.bind()`를 사용하여 `this`를 명시적으로 설정합니다.
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

### Q3: 이벤트 루프란 무엇이며, 비동기/대기는 실제로 어떻게 작동합니까?
**답:** JavaScript는 대기열을 처리하는 이벤트 루프가 있는 단일 스레드입니다. 호출 스택은 동기 코드를 실행합니다. 비어 있으면 이벤트 루프는 마이크로태스크 대기열(Promises) 또는 매크로태스크 대기열(setTimeout, I/O)에서 다음 작업을 선택합니다.  `async/await`는 Promise에 대한 구문 설탕입니다. `await`는 비동기 기능을 일시 중지하고 Promise가 해결되면 스레드를 차단하지 않고 다시 시작합니다.
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

### Q4: 최신 JavaScript의 오류를 어떻게 처리해야 합니까?
**A:** 동기 코드에는 `try/catch`를 사용하고 비동기 코드에는`.catch()`또는 `try/catch`를 `async/await`와 함께 사용하세요. 항상 Promise 거부를 처리하십시오. 처리되지 않은 거부는 Node.js를 충돌시킵니다. 도메인별 오류에 대한 사용자 정의 오류 클래스를 만듭니다. 전역 오류 처리기를 안전망으로 사용하십시오.
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

### Q5: 일반 개체/배열 대신`Map`/ `Set`를 사용해야 하는 경우는 언제인가요?
**A:** 키가 문자열이 아닐 때, 삽입 순서 반복이 필요할 때,`.size`가 필요할 때 또는 항목을 자주 추가/제거할 때(객체보다 성능이 더 좋음) `Map`를 사용하세요. O(1) 조회가 포함된 고유 컬렉션의 경우 `Set`를 사용하세요. 대규모 데이터 세트의 경우 `array.includes()`보다 훨씬 빠릅니다. 간단한 JSON 직렬화 가능 데이터와 문자열 키가 있는 작은 키-값 맵에는 일반 객체를 사용하세요.
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

## 사고 사슬 문제 해결
### 문제 1: 디바운스 기능 구현
**문제 설명:** 마지막 호출 이후 지정된 대기 기간이 경과할 때까지 함수 호출을 지연하는`debounce`유틸리티를 구현하십시오. 선행 및 후행 가장자리 호출을 모두 지원합니다.
**1단계 - 문제 이해:**
디바운스된 함수는 빠른 연속 호출을 무시하고 대기 시간 동안 호출이 중지된 후에만 실행됩니다. "리딩 에지(Leading edge)"는 첫 번째 호출 시 즉시 발사되는 것을 의미합니다. "트레일링 에지(Trailing Edge)"는 대기 기간 이후의 화재를 의미합니다. 두 가지 모드를 모두 처리하고 취소도 지원해야 합니다.
**2단계 - 접근 방식 파악:**
- 클로저에 타이머 ID를 저장합니다.
- 각 호출 시: 기존 타이머를 지운 다음 새 `setTimeout`를 설정합니다.
- 리딩 엣지의 경우: 활성화된 타이머가 없으면 즉시 호출합니다.
-`.cancel()`메서드를 사용하여 디바운싱된 함수를 반환합니다.
- 화살표 함수 또는 `.apply()`를 사용하여`this`컨텍스트 및 인수를 유지합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 클로저는 전역 범위를 오염시키지 않고 호출 전반에 걸쳐 상태를 유지합니다.
-`setTimeout`이전의 `clearTimeout`는 마지막 호출만 실행을 트리거하도록 보장합니다.
- `.cancel()`는 정리(예: React에서 구성 요소 마운트 해제)에 중요합니다.
- 엣지 케이스: `wait`가 0이면 함수는 다음 이벤트 루프 틱에서 실행됩니다. DOM 업데이트를 일괄 처리하는 데 유용합니다.
### 문제 2: 약속 기반 비율 제한기 구축
**문제 설명:** 시간 창당 최대 N개의 요청을 허용하는 속도 제한기를 만듭니다. 호출자가 계속 진행할 수 있는 시기를 확인하고 초과 요청을 대기열에 추가하는 약속을 반환해야 합니다.
**1단계 - 문제 이해:**
호출 횟수를 추적하는 슬라이딩 또는 고정 창이 필요합니다. 한도에 도달하면 새 통화가 대기열에 추가되고 슬롯이 열리면 해결되어야 합니다. 이것이 "토큰 버킷" 패턴입니다.
**2단계 - 접근 방식 파악:**
- 최근 호출의 타임스탬프를 배열로 추적합니다.
- 각 호출에서: 창보다 오래된 타임스탬프를 제거하고 개수 < 제한인지 확인합니다.
- 한도 미만인 경우: 즉시 해결합니다.
- 제한에 있는 경우: 가장 오래된 타임스탬프가 만료되는 시기를 계산하고`setTimeout`를 설정한 다음 해결합니다.
- 대기 중인 호출자를 위해 대기열(해결 함수 배열)을 사용합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 슬라이딩 창 접근 방식은 고정 창보다 공정합니다(창 경계에서 버스트 없음).
- 대기열 처리는 FIFO입니다. 발신자에게 순서대로 서비스가 제공됩니다.
- 프로덕션의 경우: 발신자가 대기를 취소할 수 있도록`AbortController`지원을 추가합니다.
- 성능: `_cleanOldTimestamps`는 호출당 O(n)이지만 n은 `maxCalls`로 제한됩니다.
### 문제 3: 딥 클론 기능 구현
**문제 설명:** 객체, 배열, 날짜, RegExps, 지도, 세트, ​​순환 참조 및 형식화된 배열을 처리하여 JavaScript 값을 심층적으로 복제하는 함수를 작성합니다.
**1단계 - 문제 이해:**
 `JSON.parse(JSON.stringify(obj))`는 다음에서 실패합니다.`undefined`, 함수, 기호, 날짜(문자열이 됨), RegExps(빈 객체가 됨), 맵, 세트, 순환 참조(던지기) 및 형식화된 배열. 방문한 객체를 추적하는 재귀적 솔루션이 필요합니다.
**2단계 - 접근 방식 파악:**
- `Map`를 사용하여 이미 복제된 개체를 추적합니다(순환 참조 처리).
- 각 유형을 특별하게 처리합니다: 날짜 → 새 날짜, RegExp → 새 RegExp, 지도 → 복제된 항목이 있는 새 맵, 설정 → 복제된 값이 있는 새 세트.
- `structuredClone()`를 최신 내장 대안으로 사용하세요(브라우저 및 Node.js 17+에서 사용 가능).
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 순환 참조:`seen`맵은 무한 반복 대신 이미 생성된 복제본을 반환합니다.
- 속성 설명자:`Reflect.ownKeys`+ `getOwnPropertyDescriptor`는 getter, setter 및 열거할 수 없는 속성을 유지합니다.
- 최신 대안: `structuredClone(value)`는 이러한 경우의 대부분을 기본적으로 처리합니다(함수 및 DOM 노드 제외). 가능하다면 선호하세요.
- 성능: 간단한 개체의 경우 `JSON.parse(JSON.stringify(obj))`가 여전히 가장 빠릅니다. 실제로 필요할 때만 딥클론을 사용하세요.
### 문제 4: 간단한 이벤트 이미터 구축
**문제 설명:**`on`,`off`,`emit`및`once`메서드를 지원하는 이벤트 이미터 클래스를 구현합니다. 청취자는 등록 순서대로 호출되어야 합니다.  `emit`는 모든 리스너에게 인수를 전달해야 합니다.
**1단계 - 문제 이해:**
게시/구독 시스템이 필요합니다. 명명된 이벤트에 대한 리스너를 등록하고, 특정 리스너를 제거하고, 인수를 사용하여 이벤트를 트리거하고, 일회성 리스너를 지원합니다. 이는 Node.js에서 광범위하게 사용되는 Observer 패턴입니다.
**2단계 - 접근 방식 파악:**
-`Map<string, Array<Function>>`에 리스너를 저장합니다.
-`on`: 리스너를 배열로 푸시합니다.
-`off`: 배열에서 특정 리스너를 필터링합니다.
-`emit`: 배열을 반복하고 스프레드 인수를 사용하여 각 리스너를 호출합니다.
- `once`: 첫 번째 호출 후 자신을 제거하는 함수에 리스너를 래핑합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- `emit`의`[...listeners]`복사본은 반복 중에 수신기가 `off`를 호출할 때 발생하는 문제를 방지합니다.
- `once`는 `_original`를 저장하므로 호출자는 `off(event, originalFn)`를 통해 래퍼를 제거할 수 있습니다.
- 비공개 필드(`#listeners`)는 내부 상태의 외부 변경을 방지합니다.
- 프로덕션의 경우:`maxListeners`경고(예: Node.js), 리스너별 오류 처리 및 우선순위를 위한 `prependListener`를 추가합니다.
---

## 요약
자바스크립트는 피할 수 없습니다. 웹 브라우저에서 실행되는 유일한 언어이므로 프런트엔드 개발에 필수적입니다. Node.js를 사용하면 서버 측으로 확장되고 React Native 및 Electron과 같은 프레임워크를 사용하면 모바일 및 데스크톱에 도달합니다. 생태계는 프로그래밍 분야에서 가장 크다. 언어의 특징은 잘 알려져 있고 관리하기 쉬우며 TypeScript는 타이핑 문제를 해결합니다. 브라우저에서 실행되는 모든 것에 대해 JavaScript는 최선의 선택일 뿐만 아니라 유일한 선택입니다.