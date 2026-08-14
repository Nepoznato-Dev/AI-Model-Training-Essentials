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
JavaScript は、1995 年にブレンダン・アイヒによってわずか 10 日間で作成された動的インタープリタ型プログラミング言語です。元々は Web ページにインタラクティブ性を追加するために設計されましたが、世界で最も広く使用されているプログラミング言語に成長しました。 JavaScript は、あらゆる Web ブラウザー、Node.js 経由のサーバー、デスクトップ アプリ (Electron)、モバイル アプリ (React Native)、さらには組み込みシステムでも実行されます。
この言語は、基本的にクライアント側 Web 開発の唯一のオプションであるという点で独特です。すべてのブラウザーがこの言語をネイティブにサポートしています。この独占は、フルスタック JavaScript (Node.js、Deno、Bun) の台頭と相まって、不可欠なものとなっています。
---

## JavaScript が重要な理由
- **Web の言語**: ブラウザーでネイティブに実行される唯一の言語。フロントエンドの代替手段はありません。
- **フルスタック機能**: フロントエンド (React、Vue、Svelte) とバックエンド (Node.js、Express、Fastify) で同じ言語を使用します。
- **大規模なエコシステム**: npm には 200 万を超えるパッケージがあり、これは世界最大のソフトウェア レジストリです。
- **汎用性**: Web アプリ、モバイル アプリ (React Native)、デスクトップ アプリ (Electron)、IoT、サーバーレス機能。
- **参入障壁が低い**: どのブラウザでも実行でき、コーディングを開始するためにインストールする必要はありません。
- **設計による非同期**: イベント駆動型のノンブロッキング I/O は、リアルタイム アプリケーションに最適です。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **動的タイピングの落とし穴** |コンパイル時の型チェックはありません。バグは実行時に表面化します。 TypeScript (JavaScript の型付きスーパーセット) を使用する |
| **コールバックの複雑さ** |ネストされたコールバックが読み取れなくなる場合があります (「コールバック地獄」)。 Promise と async/await を使用する |
| **風変わりなセマンティクス** | `==`と`===`、`this`のバインディング、ホイスティング、型強制 |癖を学びましょう。 ESLint を使用します。`var`よりも`const`/`let`を優先します |
| **シングルスレッド** | CPU に依存するタスクがイベント ループをブロックする | Web ワーカー、ワーカー スレッドを使用するか、ネイティブ モジュールにオフロードする |
| **パッケージの品質** | npm のオープン性は、一貫性のない品質とセキュリティのリスクを意味します。依存関係を監査します。ロックファイルを使用します。よく管理されたパッケージを好む |
---

## 構文の基礎
### 変数と型
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

### 関数
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

### オブジェクトとクラス
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

### 非同期プログラミング
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

### モジュール
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

## 高度な構文とパターン
### 構造の分割と拡散/休止 (詳細)
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

### プロキシとリフレクト
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

### シンボル、イテレータ、およびジェネレータ
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

### カスタムエラー階層
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

## 同時実行性と並列処理
JavaScript はイベント ループを備えたシングルスレッドです。同時実行性は、非同期パターン、Web ワーカー、および (Node.js の)worker_threads モジュールを通じて実現されます。
### イベントループ
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

### ワーカー スレッド (Node.js — CPU バウンドのタスク)
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

### Web ワーカー (ブラウザ)
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

### 非同期パターン
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

## プロジェクトの構成とシステムの構築
### プロジェクトのディレクトリ構造
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

### ビルド構成 — `package.json`
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

### リンティングとフォーマットの構成
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

### CI/CD パイプライン — GitHub アクション
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

## テスト
### Jest を使用したテスト
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

### モックテストと統合テスト
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

## 相互運用性
### N-API を使用したネイティブ アドオン (Node.js)
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

### ffi-napi を使用した C ライブラリの呼び出し
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

## デザインパターン
### モジュールパターン (カプセル化)
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

### オブザーバー/イベント エミッター パターン
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

### ビルダーパターン
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

## パフォーマンスと最適化
### プロファイリングツール
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

### 最適化手法
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

## デプロイメント
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

### プラットフォーム固有の展開
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

## エコシステム
### フロントエンド フレームワーク
|フレームワーク |アプローチ |最適な用途 |
|----------|----------|----------|
| **反応** |コンポーネントベースの仮想 DOM |大規模SPA;最大のエコシステム |
| **ビュー** |プログレッシブ、テンプレートベース |段階的な採用。素晴らしい開発者エクスペリエンス |
| **洗練された** |コンパイル時、仮想 DOM なし |より小さなバンドル、よりシンプルなコード |
| **角度** |完全なフレームワーク、TypeScript ファースト |エンタープライズアプリ。独自の構造 |
| **Next.js** | React メタフレームワーク (SSR/SSG) | SEO を備えた製品版 React アプリ |
### バックエンド (Node.js)
|フレームワーク |目的 |
|----------|----------|
| **エクスプレス** |最小限で柔軟な Web フレームワーク (最も人気のある) |
| **高速化** |高性能Webフレームワーク |
| **NestJS** |エンタープライズ グレードの Angular にインスピレーションを得たアーキテクチャ |
| **コア** |軽量で最新の Express の代替品 |
| **ほの** |超高速、マルチランタイム (Node、Deno、Bun、edge) |
### ランタイム
|ランタイム |説明 |
|----------|---------------|
| **Node.js** |オリジナルのサーバーサイド JavaScript ランタイム (V8 エンジン) |
| **デノ** |デフォルトで安全。ネイティブ TypeScript サポート。 Node のオリジナルの作者によって作成されました |
| **ブン** |超高速のオールインワン ランタイム、バンドラー、パッケージ マネージャー |
### 必須ツール
|ツール |目的 |
|-----|----------|
| **npm / 糸 / pnpm** |パッケージマネージャー |
| **TypeScript** | JavaScript の型付きスーパーセット |
| **ESLint** |コードリンティング |
| **より美しく** |コードのフォーマット |
| **ヴィート** |高速ビルドツールと開発サーバー |
| **ウェブパック** |モジュール バンドラー (成熟した、広く使用されている) |
| **ジェスト / ヴィテスト** |テストフレームワーク |
---

## JavaScript を使用する場合
|シナリオ | JavaScript を使用する理由 |より良い代替案 |
|----------|------|--------|
|ウェブフロントエンド |ブラウザベースの UI の唯一のオプション | — |
|フルスタックウェブ |どこでも同じ言語 |タイプ セーフティのための TypeScript |
|リアルタイム アプリ (チャット、ゲーム) |イベント駆動型のノンブロッキング I/O | — |
|サーバーレス機能 |素早く作成してどこにでも展開 | Python、ゴー |
|モバイル アプリ (React Native) | Web とコードを共有する | Flutter、ネイティブ Swift/Kotlin |
|デスクトップ アプリ (Electron) | Web テクノロジーによるクロスプラットフォーム | C# (WPF)、Tauri (Rust) |
| CPU を大量に使用する計算 |シングルスレッドの制限 | Python (NumPy)、C++、Rust、WebAssembly |
|システムプログラミング |間違った抽象化レベル | C、C++、Rust、Go |
---

## 総合的な Q&A
### Q1:`var`、`let`、および`const`の違いは何ですか?それぞれをいつ使用する必要がありますか?
**A:**`var`は関数スコープでホイストされています。最新のコードでは避けてください。 `let`はブロックスコープであり、再割り当てが可能です。 `const`はブロック スコープであり、再割り当てが禁止されています (ただし、`const` が参照するオブジェクト/配列は変更可能です)。ベスト プラクティス: デフォルトは`const`で、再割り当てが必要な場合にのみ`let`を使用し、`var`は決して使用しないでください。
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2:`this`は JavaScript でどのように機能しますか?また、なぜ非常にわかりにくいのですか?
**A:**`this`は、関数がどこで定義されているかではなく、**関数の呼び出し方法**によって決まります。メソッド呼び出しでは、`this` がオブジェクトです。スタンドアロン呼び出しでは、`undefined` (厳密モード) または`global`(非厳密モード) です。アロー関数は、それを囲んでいるスコープから`this`を継承します。これが、アロー関数がコールバックに好まれる理由です。`.bind()`を使用して、`this`を明示的に設定します。
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

### Q3: イベント ループとは何ですか?また、async/await は実際にどのように機能しますか?
**A:** JavaScript はシングルスレッドであり、キューを処理するイベント ループを備えています。コールスタックは同期コードを実行します。空の場合、イベント ループはマイクロタスク キュー (Promises) またはマクロタスク キュー (setTimeout、I/O) から次のタスクを選択します。 `async/await`は Promise に対する糖衣構文です。`await` は非同期関数を一時停止し、Promise が解決されるとスレッドをブロックせずに再開します。
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

### Q4: 最新の JavaScript でエラーを処理するにはどうすればよいですか?
**A:** 同期コードには`try/catch`を使用し、非同期コードには`.catch()`または`try/catch`を`async/await`とともに使用します。 Promise の拒否は常に処理します。処理されない拒否は Node.js をクラッシュさせます。ドメイン固有のエラー用のカスタム エラー クラスを作成します。グローバル エラー ハンドラーをセーフティ ネットとして使用します。
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

### Q5: プレーン オブジェクト/配列の代わりに`Map`/`Set`を使用する必要があるのはどのような場合ですか?
**A:** キーが文字列ではない場合、挿入順序の反復が必要な場合、`.size`が必要な場合、またはエントリを頻繁に追加/削除する場合 (オブジェクトよりもパフォーマンスが高い場合)、`Map`を使用します。 O(1) ルックアップによる一意のコレクションには`Set`を使用します。大規模なデータセットの場合は`array.includes()`よりもはるかに高速です。単純な JSON シリアル化可能なデータと、文字列キーを含む小さなキーと値のマップには、プレーン オブジェクトを使用します。
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

## 思考連鎖による問題解決
### 問題 1: デバウンス関数を実装する
**問題ステートメント:** 最後に呼び出されてから指定された待機期間が経過するまで関数の呼び出しを遅らせる`debounce`ユーティリティを実装します。リーディング エッジとトレーリング エッジの両方の呼び出しをサポートします。
**ステップ 1 — 問題を理解する:**
デバウンス関数は、急速に連続する呼び出しを無視し、待機期間中に呼び出しが停止した後にのみ起動します。 「最先端」とは、最初の呼び出しですぐに発射することを意味します。 「トレーリングエッジ」とは、待機期間後の発射を意味します。両方のモードを処理し、キャンセルもサポートする必要があります。
**ステップ 2 — アプローチを特定する:**
- タイマー ID をクロージャに格納します。
- 呼び出しごとに、既存のタイマーをクリアしてから、新しい`setTimeout`を設定します。
- リーディングエッジの場合: アクティブなタイマーがない場合は、すぐに呼び出します。
-`.cancel()`メソッドを使用してデバウンスされた関数を返します。
- アロー関数または`.apply()`を使用して、`this` コンテキストと引数を保持します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- クロージャは、グローバル スコープを汚染することなく、呼び出し全体で状態を保持します。
-`setTimeout`の前に`clearTimeout`を指定すると、最後の呼び出しのみが実行をトリガーします。
-`.cancel()`はクリーンアップ (React でのコンポーネントのアンマウントなど) に重要です。
- エッジ ケース:`wait`が 0 の場合、関数は次のイベント ループ ティックで起動します。これは、DOM 更新のバッチ処理に役立ちます。
### 問題 2: Promise ベースのレート リミッターを構築する
**問題ステートメント:** 時間枠ごとに最大 N 個のリクエストを許可するレート リミッターを作成します。呼び出し元が続行を許可され、過剰なリクエストがキューに追加されたときに解決される Promise を返す必要があります。
**ステップ 1 — 問題を理解する:**
行われた通話の数を追跡するスライド ウィンドウまたは固定ウィンドウが必要です。制限に達すると、新しい呼び出しはキューに入れられ、スロットが空いたときに解決される必要があります。これは「トークンバケット」パターンです。
**ステップ 2 — アプローチを特定する:**
- 最近の呼び出しのタイムスタンプを配列で追跡します。
- 各呼び出し時: ウィンドウより古いタイムスタンプを削除し、カウント < 制限かどうかを確認します。
- 制限を下回っている場合: 直ちに解決します。
- 制限に達した場合: 最も古いタイムスタンプがいつ期限切れになるかを計算し、`setTimeout`を設定してから解決します。
- 待機中の呼び出し元にはキュー (解決関数の配列) を使用します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- スライディング ウィンドウ アプローチは、固定ウィンドウよりも公平です (ウィンドウ境界でのバーストがありません)。
- キュー処理は FIFO です。呼び出し元は順番に処理されます。
- 運用環境の場合:`AbortController`サポートを追加して、呼び出し側が待機をキャンセルできるようにします。
- パフォーマンス:`_cleanOldTimestamps`は呼び出しごとに O(n) ですが、n は`maxCalls`によって制限されます。
### 問題 3: ディープ クローン機能の実装
**問題ステートメント:** オブジェクト、配列、日付、RegExp、マップ、セット、循環参照、および型付き配列を処理して、任意の JavaScript 値を詳細に複製する関数を作成します。
**ステップ 1 — 問題を理解する:**
`JSON.parse(JSON.stringify(obj))`は、`undefined`、関数、シンボル、日付 (文字列になる)、RegExp (空のオブジェクトになる)、マップ、セット、循環参照 (スロー)、および型付き配列で失敗します。訪問したオブジェクトを追跡する再帰的なソリューションが必要です。
**ステップ 2 — アプローチを特定する:**
-`Map`を使用して、すでに複製されたオブジェクトを追跡します (循環参照を処理します)。
- 各タイプを特別に処理します: Date → 新しい Date、RegExp → 新しい RegExp、Map → クローンされたエントリを持つ新しい Map、Set → クローンされた値を持つ新しい Set。
-`structuredClone()`を最新の組み込み代替手段として使用します (ブラウザーおよび Node.js 17 以降で利用可能)。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- 循環参照:`seen`マップは、無限に再帰するのではなく、作成済みのクローンを返します。
- プロパティ記述子:`Reflect.ownKeys`+`getOwnPropertyDescriptor`は、ゲッター、セッター、および列挙不可能なプロパティを保持します。
- 最新の代替案:`structuredClone(value)`は、これらのケースのほとんどをネイティブに処理します (関数と DOM ノードを除く)。利用可能な場合はそれを優先します。
- パフォーマンス: 単純なオブジェクトの場合は、依然として`JSON.parse(JSON.stringify(obj))`が最速です。ディープ クローンは、実際に必要な場合にのみ使用してください。
### 問題 4: 単純なイベント エミッターを構築する
**問題ステートメント:**`on`、`off`、`emit`、および`once`メソッドをサポートするイベント エミッター クラスを実装します。リスナーは登録順に呼び出す必要があります。 `emit`はすべてのリスナーに引数を渡す必要があります。
**ステップ 1 — 問題を理解する:**
パブリッシュ/サブシステムが必要です。名前付きイベントのリスナーを登録し、特定のリスナーを削除し、引数を使用してイベントをトリガーし、ワンタイム リスナーをサポートします。これは、Node.js で広く使用されている Observer パターンです。
**ステップ 2 — アプローチを特定する:**
- リスナーを`Map<string, Array<Function>>`に保存します。
-`on`: リスナーを配列にプッシュします。
-`off`: 配列から特定のリスナーをフィルタリングします。
-`emit`: 配列を反復し、スプレッド引数を使用して各リスナーを呼び出します。
-`once`: 最初の呼び出し後にリスナー自体を削除する関数でリスナーをラップします。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
-`emit`内の`[...listeners]`コピーは、リスナーが反復中に`off`を呼び出すときの問題を防ぎます。
-`once`は`_original`を保存するため、呼び出し元は`off(event, originalFn)`を介してラッパーを削除できます。
- プライベート フィールド (`#listeners`) は、内部状態の外部からの突然変異を防ぎます。
- 運用環境の場合:`maxListeners`警告 (Node.js など)、リスナーごとのエラー処理、および優先度の`prependListener`を追加します。
---

＃＃ まとめ
JavaScript は避けられません。 Web ブラウザーで実行される唯一の言語であるため、フロントエンド開発には不可欠です。 Node.js を使用するとサーバー側にまで拡張され、React Native や Electron などのフレームワークを使用するとモバイルとデスクトップにまで拡張されます。エコシステムはプログラミングにおいて最大です。この言語の癖はよく知られており、対処しやすいものであり、TypeScript は入力の問題に対処します。ブラウザーで実行されるものであれば、JavaScript が最良の選択であるだけでなく、それが唯一の選択肢です。