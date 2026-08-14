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

#Javascript
JavaScript là ngôn ngữ lập trình động, được diễn giải do Brendan Eich tạo ra chỉ trong 10 ngày vào năm 1995. Ban đầu được thiết kế để thêm tính tương tác vào các trang web, nó đã phát triển thành ngôn ngữ lập trình được sử dụng rộng rãi nhất trên thế giới. JavaScript chạy trong mọi trình duyệt web, trên máy chủ thông qua Node.js, trong ứng dụng máy tính để bàn (Electron), ứng dụng di động (React Native) và thậm chí cả các hệ thống nhúng.
Ngôn ngữ này độc đáo ở chỗ về cơ bản nó là lựa chọn duy nhất để phát triển web phía máy khách - mọi trình duyệt đều hỗ trợ ngôn ngữ này. Sự độc quyền này, kết hợp với sự gia tăng của JavaScript full-stack (Node.js, Deno, Bun), khiến nó trở nên không thể thiếu.
---

## Tại sao JavaScript lại quan trọng
- **Ngôn ngữ của web**: Ngôn ngữ duy nhất chạy tự nhiên trong trình duyệt. Không có sự thay thế cho giao diện người dùng.
- **Khả năng toàn ngăn xếp**: Cùng một ngôn ngữ trên giao diện người dùng (React, Vue, Svelte) và phụ trợ (Node.js, Express, Fastify).
- **Hệ sinh thái khổng lồ**: npm có hơn 2 triệu gói — cơ quan đăng ký phần mềm lớn nhất thế giới.
- **Tính linh hoạt**: Ứng dụng web, ứng dụng di động (React Native), ứng dụng máy tính để bàn (Electron), IoT, chức năng serverless.
- **Rào cản gia nhập thấp**: Chạy trên mọi trình duyệt — không cần cài đặt để bắt đầu viết mã.
- **Không đồng bộ theo thiết kế**: I/O không chặn, hướng sự kiện khiến nó trở nên tuyệt vời cho các ứng dụng thời gian thực.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Cạm bẫy khi gõ động** | Không kiểm tra kiểu thời gian biên dịch; lỗi xuất hiện trong thời gian chạy | Sử dụng TypeScript (một siêu tập hợp JavaScript được gõ) |
| **Độ phức tạp của cuộc gọi lại** | Các lệnh gọi lại lồng nhau có thể trở nên không thể đọc được ("gọi lại địa ngục") | Sử dụng Lời hứa và async/await |
| **Ngữ nghĩa kỳ quặc** | `==`vs`===`,`this`ràng buộc, cẩu, ép kiểu | Tìm hiểu những điều kỳ quặc; sử dụng ESLint; thích`const`/`let`hơn`var`|
| **Đơn luồng** | Các tác vụ liên kết với CPU chặn vòng lặp sự kiện | Sử dụng Web Worker, luồng công việc hoặc giảm tải cho các mô-đun gốc |
| **Chất lượng gói hàng** | tính mở của npm có nghĩa là chất lượng không nhất quán và rủi ro bảo mật | Kiểm toán phụ thuộc; sử dụng tập tin khóa; thích các gói được bảo trì tốt |
---

##Cơ bản về cú pháp
### Biến và kiểu
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

### Chức năng
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

### Đối tượng và lớp
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

### Lập trình không đồng bộ
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

### Mô-đun
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

## Cú pháp & Mẫu nâng cao
### Phá hủy & Lan rộng/Nghỉ ngơi (Lặn sâu)
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

### Proxy và phản ánh
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

### Ký hiệu, Trình vòng lặp và Trình tạo
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

### Phân cấp lỗi tùy chỉnh
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

## Đồng thời & Song song
JavaScript là một luồng đơn với một vòng lặp sự kiện. Tính đồng thời đạt được thông qua các mẫu không đồng bộ, Web Workers và (trong Node.js) mô-đun worker_threads.
### Vòng lặp sự kiện
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

### Luồng công nhân (Node.js — các tác vụ liên quan đến CPU)
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

### Nhân viên web (Trình duyệt)
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

### Mẫu không đồng bộ
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc thư mục dự án
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

### Cấu hình bản dựng — `package.json`
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

### Cấu hình Linting và định dạng
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

### Đường dẫn CI/CD — Hành động GitHub
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

##Thử nghiệm
### Thử nghiệm với Jest
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

### Thử nghiệm mô phỏng và tích hợp
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

## Khả năng tương tác
### Addon gốc có N-API (Node.js)
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

### WebAssugging (Wasm)
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

### Gọi thư viện C bằng ffi-napi
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

## Mẫu thiết kế
### Mẫu mô-đun (Đóng gói)
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

### Mẫu trình quan sát / trình phát sự kiện
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

### Mẫu trình tạo
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
###Tệp Docker
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

### Triển khai theo nền tảng cụ thể
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

## Hệ sinh thái
### Khung giao diện người dùng
| Khung | Tiếp cận | Tốt nhất cho |
|----------|----------|----------|
| **Phản ứng** | DOM ảo, dựa trên thành phần | SPA quy mô lớn; hệ sinh thái lớn nhất |
| **Vue** | Tiến bộ, dựa trên mẫu | Áp dụng dần dần; kinh nghiệm phát triển tuyệt vời |
| **Mảnh dẻ** | Thời gian biên dịch, không có DOM ảo | Gói nhỏ hơn, mã đơn giản hơn |
| **Góc cạnh** | Khung đầy đủ, ưu tiên TypeScript | Ứng dụng doanh nghiệp; cấu trúc có quan điểm |
| **Tiếp theo** | Phản ứng siêu khung (SSR/SSG) | Sản xuất ứng dụng React với SEO |
### Phần cuối (Node.js)
| Khung | Mục đích |
|----------||----------|
| **Nhanh** | Khung web tối giản, linh hoạt (phổ biến nhất) |
| **Nhanh chóng** | Khung web hiệu suất cao |
| **NestJS** | Kiến trúc lấy cảm hứng từ góc cạnh, cấp doanh nghiệp |
| **Koa** | Thay thế Express nhẹ, hiện đại |
| **Xin chào** | Cực nhanh, đa thời gian chạy (Node, Deno, Bun, edge) |
### Thời gian chạy
| Thời gian chạy | Mô tả |
|----------|-------------|
| **Node.js** | Thời gian chạy JavaScript phía máy chủ ban đầu (động cơ V8) |
| **Deno** | Bảo mật theo mặc định; hỗ trợ TypeScript gốc; được tạo bởi tác giả gốc của Node |
| **Bún** | Thời gian chạy, trình đóng gói và trình quản lý gói cực nhanh |
### Công cụ cần thiết
| Công cụ | Mục đích |
|------|----------|
| **npm / sợi / pnpm** | Quản lý gói |
| **TypeScript** | Đã gõ superset của JavaScript |
| **ESLint** | Mã linting |
| **Đẹp hơn** | Định dạng mã |
| **Vite** | Công cụ xây dựng nhanh và máy chủ dev |
| **Gói web** | Bộ đóng gói mô-đun (hoàn thiện, được sử dụng rộng rãi) |
| **Jest / Vitest** | Khung kiểm tra |
---

## Khi nào nên sử dụng JavaScript
| Kịch bản | Tại sao dùng JavaScript | Thay thế tốt hơn |
|----------|--------------|-------------------|
| Giao diện web | Tùy chọn duy nhất cho giao diện người dùng dựa trên trình duyệt | — |
| Web đầy đủ | Cùng một ngôn ngữ ở mọi nơi | TypeScript để đảm bảo an toàn về kiểu chữ |
| Ứng dụng thời gian thực (trò chuyện, trò chơi) | I/O không chặn, hướng sự kiện | — |
| Chức năng không có máy chủ | Viết nhanh, triển khai mọi nơi | Python, Đi |
| Ứng dụng di động (React Native) | Chia sẻ mã với web | Flutter, Swift/Kotlin bản địa |
| Ứng dụng máy tính để bàn (Điện tử) | Đa nền tảng với công nghệ web | C# (WPF), Tauri (Rỉ sét) |
| Tính toán sử dụng nhiều CPU | Giới hạn đơn luồng | Python (NumPy), C++, Rust, WebAssugging |
| Lập trình hệ thống | Mức độ trừu tượng sai | C, C++, Rust, Đi |
---

## Hỏi đáp tổng hợp
### Câu hỏi 1: Sự khác biệt giữa`var`,`let`và`const`là gì và khi nào tôi nên sử dụng từng loại?
**A:**`var`nằm trong phạm vi chức năng và được nâng lên — hãy tránh sử dụng nó trong mã hiện đại. `let`có phạm vi khối và cho phép gán lại. `const`có phạm vi khối và ngăn chặn việc gán lại (nhưng các đối tượng/mảng mà nó tham chiếu vẫn có thể thay đổi). Cách thực hành tốt nhất: mặc định là`const`, chỉ sử dụng`let`khi bạn cần chỉ định lại, không bao giờ sử dụng`var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Câu 2:`this`hoạt động như thế nào trong JavaScript và tại sao nó lại khó hiểu đến vậy?
**A:**`this`được xác định bởi **cách gọi một hàm**, chứ không phải nơi nó được xác định. Trong cuộc gọi phương thức,`this`là đối tượng. Trong cuộc gọi độc lập, đó là`undefined`(chế độ nghiêm ngặt) hoặc`global`(không nghiêm ngặt). Các hàm mũi tên kế thừa`this`từ phạm vi kèm theo của chúng - đây là lý do tại sao chúng được ưu tiên cho các lệnh gọi lại. Sử dụng`.bind()`để đặt rõ ràng`this`.
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

### Câu 3: Vòng lặp sự kiện là gì và async/await thực sự hoạt động như thế nào?
**A:** JavaScript đơn luồng với vòng lặp sự kiện xử lý hàng đợi. Ngăn xếp cuộc gọi thực thi mã đồng bộ. Khi trống, vòng lặp sự kiện sẽ chọn nhiệm vụ tiếp theo từ hàng đợi vi nhiệm vụ (Lời hứa) hoặc hàng đợi nhiệm vụ vĩ mô (setTimeout, I/O). `async/await`là đường cú pháp so với Lời hứa -`await`tạm dừng chức năng không đồng bộ và tiếp tục khi Lời hứa được giải quyết mà không chặn luồng.
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

### Q4: Tôi nên xử lý lỗi trong JavaScript hiện đại như thế nào?
**A:** Sử dụng`try/catch`cho mã đồng bộ và`.catch()`hoặc`try/catch`với`async/await`cho mã không đồng bộ. Luôn xử lý các lời từ chối Promise - những lời từ chối không được xử lý làm hỏng Node.js. Tạo các lớp lỗi tùy chỉnh cho các lỗi theo miền cụ thể. Sử dụng trình xử lý lỗi toàn cầu làm mạng lưới an toàn.
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

### Câu 5: Khi nào tôi nên sử dụng`Map`/`Set`thay vì các đối tượng/mảng đơn giản?
**A:** Sử dụng`Map`khi khóa không phải là chuỗi, khi bạn cần lặp lại thứ tự chèn, khi bạn cần`.size`hoặc khi bạn thường xuyên thêm/xóa các mục nhập (hiệu suất tốt hơn so với đối tượng). Sử dụng`Set`cho các bộ sưu tập độc đáo với tính năng tra cứu O(1) — nhanh hơn nhiều so với`array.includes()`cho các tập dữ liệu lớn. Sử dụng các đối tượng đơn giản cho dữ liệu có thể tuần tự hóa JSON đơn giản và các bản đồ khóa-giá trị nhỏ có khóa chuỗi.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Triển khai hàm Debounce
**Báo cáo sự cố:** Triển khai tiện ích`debounce`giúp trì hoãn việc gọi hàm cho đến khi hết một khoảng thời gian chờ được chỉ định kể từ lần cuối cùng nó được gọi. Hỗ trợ cả lệnh gọi cạnh đầu và cuối.
**Bước 1 — Tìm hiểu vấn đề:**
Hàm bị trả lại sẽ bỏ qua các cuộc gọi liên tiếp nhanh chóng và chỉ kích hoạt sau khi các cuộc gọi dừng trong thời gian chờ. “Dẫn đầu” có nghĩa là khai hỏa ngay từ cuộc gọi đầu tiên. "Trailing edge" có nghĩa là cháy sau thời gian chờ đợi. Chúng tôi cần xử lý cả hai chế độ và hỗ trợ hủy.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Lưu trữ ID hẹn giờ trong một bao đóng.
- Trên mỗi cuộc gọi: xóa bộ hẹn giờ hiện có, sau đó đặt`setTimeout`mới.
- Đối với cạnh đầu: gọi ngay nếu không có hẹn giờ hoạt động.
- Trả về hàm đã được gỡ bỏ bằng phương thức `.cancel()`.
- Bảo toàn bối cảnh và đối số`this`bằng cách sử dụng các hàm mũi tên hoặc`.apply()`.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Việc đóng cửa duy trì trạng thái qua các cuộc gọi mà không gây ô nhiễm phạm vi toàn cầu.
-`clearTimeout`trước`setTimeout`đảm bảo chỉ thực hiện cuộc gọi cuối cùng kích hoạt.
-`.cancel()`rất quan trọng cho việc dọn dẹp (ví dụ: ngắt kết nối thành phần trong React).
- Trường hợp cạnh: nếu`wait`bằng 0, hàm sẽ kích hoạt ở dấu kiểm vòng lặp sự kiện tiếp theo — hữu ích cho việc phân nhóm các bản cập nhật DOM.
### Vấn đề 2: Xây dựng bộ giới hạn tỷ lệ dựa trên lời hứa
**Báo cáo vấn đề:** Tạo bộ giới hạn tốc độ cho phép tối đa N yêu cầu trong mỗi khoảng thời gian. Nó sẽ trả về các Lời hứa sẽ giải quyết khi người gọi được phép tiếp tục và xếp hàng các yêu cầu vượt quá.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần một cửa sổ trượt hoặc cố định để theo dõi số lượng cuộc gọi đã được thực hiện. Khi đạt đến giới hạn, các cuộc gọi mới sẽ được xếp hàng đợi và giải quyết khi có chỗ trống. Đây là mẫu "thùng mã thông báo".
**Bước 2 — Xác định phương pháp tiếp cận:**
- Theo dõi dấu thời gian của các cuộc gọi gần đây trong một mảng.
- Trên mỗi cuộc gọi: xóa dấu thời gian cũ hơn cửa sổ, kiểm tra xem số đếm có < giới hạn không.
- Nếu dưới giới hạn: giải quyết ngay.
- Nếu ở giới hạn: tính toán thời điểm dấu thời gian cũ nhất hết hạn, đặt`setTimeout`, sau đó giải quyết.
- Sử dụng hàng đợi (mảng các hàm phân giải) để chờ người gọi.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Phương pháp cửa sổ trượt công bằng hơn so với cửa sổ cố định (không bị vỡ ở ranh giới cửa sổ).
- Xử lý hàng đợi là FIFO - người gọi được phục vụ theo thứ tự.
- Đối với sản xuất: thêm hỗ trợ`AbortController`để người gọi có thể hủy chờ.
- Hiệu suất:`_cleanOldTimestamps`là O(n) mỗi cuộc gọi nhưng n bị giới hạn bởi`maxCalls`.
### Vấn đề 3: Triển khai chức năng Deep Clone
**Báo cáo vấn đề:** Viết hàm sao chép sâu mọi giá trị JavaScript, xử lý các đối tượng, mảng, Ngày, RegExps, Bản đồ, Bộ, tham chiếu vòng tròn và mảng đã nhập.
**Bước 1 — Tìm hiểu vấn đề:**
`JSON.parse(JSON.stringify(obj))`không thành công trên: `undefined`, hàm, Biểu tượng, Ngày tháng (trở thành chuỗi), RegExps (trở thành đối tượng trống), Bản đồ, Bộ, tham chiếu vòng tròn (ném) và mảng đã nhập. Chúng ta cần một giải pháp đệ quy để theo dõi các đối tượng đã truy cập.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`Map`để theo dõi các đối tượng đã được sao chép (xử lý các tham chiếu vòng tròn).
- Xử lý đặc biệt từng loại: Ngày → Ngày mới, RegExp → RegExp mới, Bản đồ → Bản đồ mới với các mục được sao chép, Bộ → Bộ mới với các giá trị được sao chép.
- Sử dụng`structuredClone()`làm giải pháp thay thế tích hợp hiện đại (có sẵn trong trình duyệt và Node.js 17+).
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Tham chiếu vòng: Bản đồ`seen`trả về bản sao đã được tạo thay vì đệ quy vô hạn.
- Bộ mô tả thuộc tính:`Reflect.ownKeys`+`getOwnPropertyDescriptor`bảo toàn các thuộc tính getters, setters và không thể đếm được.
- Giải pháp thay thế hiện đại:`structuredClone(value)`xử lý nguyên bản hầu hết các trường hợp này (ngoại trừ các hàm và nút DOM). Thích nó khi có sẵn.
- Hiệu suất: đối với các đối tượng đơn giản,`JSON.parse(JSON.stringify(obj))`vẫn nhanh nhất. Chỉ sử dụng bản sao sâu khi bạn thực sự cần nó.
### Bài toán 4: Xây dựng một Event Emitter đơn giản
**Báo cáo sự cố:** Triển khai lớp trình phát sự kiện hỗ trợ các phương thức`on`,`off`,`emit`và `once`. Người nghe nên được gọi theo thứ tự đăng ký. `emit`sẽ chuyển đối số cho tất cả người nghe.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần một hệ thống pub/sub: đăng ký trình nghe cho các sự kiện được đặt tên, xóa trình nghe cụ thể, kích hoạt sự kiện bằng đối số và hỗ trợ trình nghe một lần. Đây là mẫu Observer được sử dụng rộng rãi trong Node.js.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Lưu trữ người nghe trong`Map<string, Array<Function>>`.
-`on`: đẩy người nghe vào mảng.
-`off`: lọc ra người nghe cụ thể khỏi mảng.
-`emit`: lặp mảng và gọi từng người nghe bằng các đối số trải rộng.
-`once`: bọc người nghe trong một chức năng tự loại bỏ sau cuộc gọi đầu tiên.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Bản sao`[...listeners]`trong`emit`ngăn ngừa sự cố khi người nghe gọi`off`trong quá trình lặp.
-`once`lưu trữ`_original`để người gọi có thể xóa trình bao bọc thông qua`off(event, originalFn)`.
- Các trường riêng (`#listeners`) ngăn chặn sự đột biến bên ngoài của trạng thái bên trong.
- Đối với sản xuất: thêm cảnh báo`maxListeners`(như Node.js), xử lý lỗi trên mỗi người nghe và ưu tiên `prependListener`.
---

## Bản tóm tắt
JavaScript là không thể tránh khỏi. Đây là ngôn ngữ duy nhất chạy trên trình duyệt web, khiến nó trở nên cần thiết cho việc phát triển giao diện người dùng. Với Node.js, nó mở rộng sang phía máy chủ và với các framework như React Native và Electron, nó tiếp cận với thiết bị di động và máy tính để bàn. Hệ sinh thái là lớn nhất trong lập trình. Những điểm kỳ quặc của ngôn ngữ này rất nổi tiếng và dễ quản lý - và TypeScript giải quyết các vấn đề về đánh máy. Đối với mọi thứ chạy trên trình duyệt, JavaScript không chỉ là lựa chọn tốt nhất mà còn là lựa chọn duy nhất.