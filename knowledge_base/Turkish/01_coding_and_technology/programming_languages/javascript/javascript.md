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

#JavaScript
JavaScript, Brendan Eich tarafından 1995 yılında yalnızca 10 günde oluşturulan dinamik, yorumlanan bir programlama dilidir. Başlangıçta web sayfalarına etkileşim eklemek için tasarlanan bu dil, bugün dünyada en yaygın kullanılan programlama dili haline geldi. JavaScript her web tarayıcısında, Node.js aracılığıyla sunucularda, masaüstü uygulamalarında (Electron), mobil uygulamalarda (React Native) ve hatta gömülü sistemlerde çalışır.
Dil, istemci tarafı web geliştirme için esasen tek seçenek olması açısından benzersizdir; her tarayıcı onu yerel olarak destekler. Bu tekel, tam yığın JavaScript'in (Node.js, Deno, Bun) yükselişiyle birleştiğinde onu vazgeçilmez kılıyor.
---

## JavaScript Neden Önemlidir
- **Web'in dili**: Tarayıcılarda yerel olarak çalışan tek dil. Ön uç için alternatif yok.
- **Tam yığın yeteneği**: Ön uçta (React, Vue, Svelte) ve arka uçta (Node.js, Express, Fastify) aynı dil.
- **Devasa ekosistem**: npm'nin 2 milyondan fazla paketi vardır; bu, dünyadaki en büyük yazılım kaydıdır.
- **Çok yönlülük**: Web uygulamaları, mobil uygulamalar (React Native), masaüstü uygulamaları (Electron), IoT, sunucusuz işlevler.
- **Giriş engeli düşük**: Her tarayıcıda çalışır; kodlamaya başlamak için kurulum gerekmez.
- **Tasarım gereği eşzamansız**: Olay odaklı, engellemeyen G/Ç, onu gerçek zamanlı uygulamalar için mükemmel kılar.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Dinamik yazmanın zorlukları** | Derleme zamanı tür denetimi yok; çalışma zamanında hatalar ortaya çıkıyor | TypeScript (JavaScript'in yazılı bir üst kümesi) kullanın |
| **Geri arama karmaşıklığı** | İç içe geçmiş geri aramalar okunamaz hale gelebilir ("geri arama cehennemi") | Promises ve async/await kullanın |
| **İlginç anlambilim** | `==`vs`===`,`this`bağlama, kaldırma, tip zorlama | Tuhaflıkları öğrenin; ESLint'i kullanın;`var`yerine`const`/ `let`'yi tercih edin |
| **Tek iş parçacıklı** | CPU'ya bağlı görevler olay döngüsünü engeller | Web Çalışanlarını, çalışan iş parçacıklarını kullanın veya yerel modüllere yükleme yapın |
| **Paket kalitesi** | npm'nin açıklığı tutarsız kalite ve güvenlik riskleri anlamına gelir | Denetim bağımlılıkları; kilit dosyalarını kullanın; bakımlı paketleri tercih edin |
---

## Söz Diziminin Temelleri
### Değişkenler ve Türler
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

### İşlevler
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

### Nesneler ve Sınıflar
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

### Eşzamansız Programlama
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

### Modüller
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

## Gelişmiş Sözdizimi ve Desenler
### Yıkım ve Yayılma/Dinlenme (Derin Dalış)
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

### Proxy'ler ve Yansıtma
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

### Semboller, Yineleyiciler ve Oluşturucular
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

### Özel Hata Hiyerarşileri
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

## Eşzamanlılık ve Paralellik
JavaScript, bir olay döngüsüne sahip tek iş parçacıklıdır. Eşzamanlılık, eş zamanlı olmayan kalıplar, Web Çalışanları ve (Node.js'de) Worker_threads modülü aracılığıyla sağlanır.
### Olay Döngüsü
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

### Çalışan Konuları (Node.js — CPU'ya bağlı görevler)
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

### Web Çalışanları (Tarayıcı)
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

### Eşzamansız Desenler
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Rehberi Yapısı
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

### Yapı Yapılandırması — `package.json`
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

### Linting ve Formatlama Yapılandırması
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

### CI/CD İşlem Hattı — GitHub Eylemleri
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

## Test etme
### Jest ile test etme
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

### Alay ve Entegrasyon Testleri
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

## Birlikte Çalışabilirlik
### N-API'li Yerel Eklentiler (Node.js)
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

### ffi-napi ile C Kütüphanelerini çağırmak
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

## Tasarım Desenleri
### Modül Deseni (Kapsülleme)
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

### Gözlemci / Olay Yayıcı Modeli
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

### Oluşturucu Deseni
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
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

### Optimizasyon Teknikleri
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

## Dağıtım
### Docker dosyası
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

### Platforma Özel Dağıtım
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

## Ekosistem
### Ön Uç Çerçeveleri
| Çerçeve | Yaklaşım | En İyisi |
|-----------|----------|----------|
| **Tepki** | Bileşen tabanlı, sanal DOM | Büyük ölçekli SPA'lar; en büyük ekosistem |
| **Vue** | Aşamalı, şablon tabanlı | Kademeli evlat edinme; harika geliştirici deneyimi |
| **İnce** | Derleme zamanı, sanal DOM yok | Daha küçük paketler, daha basit kod |
| **Açısal** | Tam çerçeve, TypeScript öncelikli | Kurumsal uygulamalar; inatçı yapı |
| **Sonraki.js** | Tepki meta çerçevesi (SSR/SSG) | SEO ile Üretim React uygulamaları |
### Arka uç (Node.js)
| Çerçeve | Amaç |
|-----------|------------|
| **Ekspres** | Minimal, esnek web çerçevesi (en popüler) |
| **Hızlandır** | Yüksek performanslı web çerçevesi |
| **NestJS** | Kurumsal düzeyde, Angular'dan ilham alan mimari |
| **Koa** | Hafif, modern Ekspres alternatifi |
| **Hono** | Ultra hızlı, çoklu çalışma süresi (Düğüm, Deno, Bun, kenar) |
### Çalışma Zamanları
| Çalışma zamanı | Açıklama |
|-----------|------------|
| **Node.js** | Orijinal sunucu tarafı JavaScript çalışma zamanı (V8 motoru) |
| **Deno** | Varsayılan olarak güvenlidir; yerel TypeScript desteği; Node'un orijinal yazarı tarafından oluşturulmuştur |
| **Çörek** | Ultra hızlı hepsi bir arada çalışma zamanı, paketleyici ve paket yöneticisi |
### Temel Araçlar
| Araç | Amaç |
|------|------------|
| **npm / iplik / pnpm** | Paket yöneticileri |
| **TypeScript** | JavaScript'in yazılan üst kümesi |
| **ESLint** | Kod astarlama |
| **Daha güzel** | Kod biçimlendirme |
| **Vite** | Hızlı oluşturma aracı ve geliştirme sunucusu |
| **Web paketi** | Modül paketleyici (olgun, yaygın olarak kullanılan) |
| **Şaka / Şaka** | Çerçevelerin test edilmesi |
---

## JavaScript Ne Zaman Kullanılmalı
| Senaryo | Neden JavaScript | Daha İyi Alternatif |
|----------|---------------|----------|
| Web arayüzü | Tarayıcı tabanlı kullanıcı arayüzü için tek seçenek | — |
| Tam yığın web | Her yerde aynı dil | Yazım güvenliği için TypeScript |
| Gerçek zamanlı uygulamalar (sohbet, oyunlar) | Olay odaklı, engellemesiz G/Ç | — |
| Sunucusuz işlevler | Hızlı yazma, her yere dağıtma | Python, Git |
| Mobil uygulamalar (React Native) | Kodu web ile paylaşın | Flutter, yerli Swift/Kotlin |
| Masaüstü uygulamaları (Electron) | Web teknolojisiyle çapraz platform | C# (WPF), Tauri (Pas) |
| CPU yoğun hesaplama | Tek iş parçacıklı sınırlama | Python (NumPy), C++, Rust, WebAssembly |
| Sistem programlama | Yanlış soyutlama düzeyi | C, C++, Pas, Git |
---

## Sentetik Soru-Cevap
### S1: `var`,`let`ve`const`arasındaki fark nedir ve her birini ne zaman kullanmalıyım?
**C:**`var`işlev kapsamlıdır ve kaldırılmıştır; modern kodlarda bundan kaçının. `let`blok kapsamlıdır ve yeniden atamaya izin verir. `const`blok kapsamlıdır ve yeniden atamayı önler (ancak başvurduğu nesneler/diziler hala değiştirilebilir). En iyi uygulama: varsayılan olarak`const`kullanın, `let`'yi yalnızca yeniden atamaya ihtiyacınız olduğunda kullanın, asla`var`kullanmayın.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### S2: `this`, JavaScript'te nasıl çalışır ve neden bu kadar kafa karıştırıcıdır?
**C:** `this`, tanımlandığı yere değil, **bir fonksiyonun nasıl çağrıldığına** göre belirlenir. Bir yöntem çağrısında`this`nesnedir. Bağımsız bir çağrıda bu,`undefined`(katı mod) veya `global`'dir (katı olmayan). Ok işlevleri, `this`'yi kendi kapsamlarından devralır; bu nedenle geri aramalar için tercih edilirler.`this`öğesini açıkça ayarlamak için`.bind()`öğesini kullanın.
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

### S3: Olay döngüsü nedir ve eşzamansız/beklemede gerçekte nasıl çalışır?
**C:** JavaScript, bir kuyruğu işleyen bir olay döngüsüne sahip tek iş parçacıklı bir yapıya sahiptir. Çağrı yığını senkronize kodu yürütür. Boş olduğunda, olay döngüsü bir sonraki görevi mikro görev kuyruğundan (Vaatler) veya makro görev kuyruğundan (setTimeout, I/O) seçer.  `async/await`, Promises üzerindeki sözdizimsel şekerdir — `await`, zaman uyumsuz işlevi duraklatır ve Promise çözümlendiğinde iş parçacığını engellemeden devam eder.
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

### S4: Modern JavaScript'teki hataları nasıl ele almalıyım?
**C:** Eşzamanlı kod için `try/catch`'yi ve eşzamansız kod için`.catch()`veya`async/await`ile `try/catch`'yi kullanın. Promise retlerini her zaman ele alın; işlenmeyen retler Node.js'yi çökertir. Etki alanına özgü hatalar için özel hata sınıfları oluşturun. Güvenlik ağı olarak genel bir hata işleyicisi kullanın.
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

### S5: Düz nesneler/diziler yerine ne zaman`Map`/`Set`kullanmalıyım?
**C:** Anahtarlar dize olmadığında, kampanya siparişi yinelemeye ihtiyaç duyduğunuzda, `.size`'ye ihtiyaç duyduğunuzda veya girişleri sık sık eklediğinizde/kaldırdığınızda (nesnelerden daha iyi performans)`Map`kullanın. O(1) aramalı benzersiz koleksiyonlar için `Set`'yi kullanın; büyük veri kümeleri için `array.includes()`'den çok daha hızlıdır. JSON ile serileştirilebilir basit veriler ve dize anahtarlarıyla küçük anahtar/değer eşlemeleri için düz nesneler kullanın.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Geri Dönme İşlevini Uygulama
**Sorun Açıklaması:** Bir işlevin çağrılmasını, son çağrılmasından bu yana belirli bir bekleme süresi geçene kadar erteleyen bir`debounce`yardımcı programı uygulayın. Hem ön hem de arka kenar çağrısını destekleyin.
**1. Adım — Sorunu Anlayın:**
Geri dönen bir işlev, birbirini izleyen hızlı çağrıları yok sayar ve yalnızca çağrıların bekleme süresi boyunca durmasının ardından etkinleşir. "Ön kenar", ilk çağrıda hemen ateş etmek anlamına gelir. "Arka kenar", bekleme süresinden sonra yangın anlamına gelir. Her iki modu da ele almamız ve iptali de desteklememiz gerekiyor.
**2. Adım — Yaklaşımı Belirleyin:**
- Bir zamanlayıcı kimliğini bir kapakta saklayın.
- Her aramada: mevcut zamanlayıcıyı silin, ardından yeni bir`setTimeout`ayarlayın.
- Ön uç için: herhangi bir zamanlayıcı etkin değilse hemen arayın.
-`.cancel()`yöntemiyle geri dönen bir işlevi döndürün.
- Ok işlevlerini veya`.apply()`kullanarak`this`bağlamını ve bağımsız değişkenlerini koruyun.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Kapatma, küresel kapsamı kirletmeden çağrılar genelinde durumu korur.
- `setTimeout`'den önceki `clearTimeout`, yalnızca son çağrının yürütülmesini tetiklediğini garanti eder.
-`.cancel()`temizleme için önemlidir (örneğin, React'te bileşenin çıkarılması).
- Edge durumu:`wait`0 ise, işlev bir sonraki olay döngüsü işaretinde etkinleşir; DOM güncellemelerini toplu olarak işlemek için kullanışlıdır.
### Sorun 2: Söze Dayalı Bir Oran Sınırlayıcı Oluşturun
**Sorun Açıklaması:** Zaman aralığı başına en fazla N isteğe izin veren bir hız sınırlayıcı oluşturun. Arayanın devam etmesine izin verildiğinde çözülen Promise'ları döndürmeli ve fazla istekleri sıraya koymalıdır.
**1. Adım — Sorunu Anlayın:**
Kaç aramanın yapıldığını takip eden kayan veya sabit bir pencereye ihtiyacımız var. Limite ulaşıldığında, yeni aramalar sıraya alınmalı ve bir slot açıldığında çözümlenmelidir. Bu "jeton kovası" modelidir.
**2. Adım — Yaklaşımı Belirleyin:**
- Bir dizideki son aramaların zaman damgalarını izleyin.
- Her aramada: pencereden daha eski zaman damgalarını kaldırın, sayım < limit olup olmadığını kontrol edin.
- Limitin altındaysa: derhal çözümleyin.
- Sınırdaysa: en eski zaman damgasının süresinin ne zaman dolacağını hesaplayın, bir`setTimeout`ayarlayın ve ardından çözümleyin.
- Bekleyen arayanlar için bir sıra (çözümleme işlevleri dizisi) kullanın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Kayan pencere yaklaşımı sabit pencerelerden daha adildir (pencere sınırlarında patlama olmaz).
- Kuyruk işleme FIFO'dur; arayanlara sırayla hizmet verilir.
- Üretim için: arayanların beklemeyi iptal edebilmesi için`AbortController`desteğini ekleyin.
- Performans:`_cleanOldTimestamps`çağrı başına O(n)'dir ancak n,`maxCalls`tarafından sınırlanmıştır.
### Sorun 3: Derin Klonlama İşlevinin Uygulanması
**Sorun Açıklaması:** Herhangi bir JavaScript değerini derinlemesine kopyalayan, nesneleri, dizileri, Tarihleri, RegExps'i, Haritaları, Kümeleri, döngüsel başvuruları ve yazılan dizileri işleyen bir işlev yazın.
**1. Adım — Sorunu Anlayın:**
`JSON.parse(JSON.stringify(obj))`şu durumlarda başarısız olur:`undefined`, işlevler, Semboller, Tarihler (dize haline gelir), RegExps (boş nesneler haline gelir), Haritalar, Kümeler, dairesel referanslar (atarlar) ve yazılan diziler. Ziyaret edilen nesneleri izleyen özyinelemeli bir çözüme ihtiyacımız var.
**2. Adım — Yaklaşımı Belirleyin:**
- Zaten klonlanmış nesneleri izlemek için bir`Map`kullanın (dairesel referansları yönetir).
- Her türü özel olarak ele alın: Tarih → yeni Tarih, RegExp → yeni RegExp, Harita → klonlanmış girişlerle yeni Harita, Ayarla → klonlanmış değerlerle yeni Ayarla.
- Modern yerleşik alternatif olarak `structuredClone()`'yi kullanın (tarayıcılarda ve Node.js 17+ sürümlerinde mevcuttur).
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Döngüsel referanslar:`seen`Haritası, sonsuz şekilde yinelenmek yerine önceden oluşturulmuş klonu döndürür.
- Özellik tanımlayıcıları:`Reflect.ownKeys`+`getOwnPropertyDescriptor`alıcıları, ayarlayıcıları ve numaralandırılamayan özellikleri korur.
- Modern alternatif:`structuredClone(value)`bu durumların çoğunu yerel olarak ele alır (işlevler ve DOM düğümleri hariç). Mümkün olduğunda tercih edin.
- Performans: Basit nesneler için`JSON.parse(JSON.stringify(obj))`hâlâ en hızlıdır. Deep clone'u yalnızca gerçekten ihtiyacınız olduğunda kullanın.
### Sorun 4: Basit Bir Olay Yayıcı Oluşturun
**Sorun Açıklaması:** `on`, `off`,`emit`ve`once`yöntemlerini destekleyen bir olay yayıcı sınıfı uygulayın. Dinleyiciler kayıt sırasına göre çağrılmalıdır. `emit`argümanları tüm dinleyicilere iletmelidir.
**1. Adım — Sorunu Anlayın:**
Bir pub/sub sistemine ihtiyacımız var: adlandırılmış olaylar için dinleyicileri kaydedin, belirli dinleyicileri kaldırın, olayları argümanlarla tetikleyin ve tek seferlik dinleyicileri destekleyin. Bu, Node.js'de yaygın olarak kullanılan Observer modelidir.
**2. Adım — Yaklaşımı Belirleyin:**
- Dinleyicileri bir `Map<string, Array<Function>>`'de saklayın.
-`on`: dinleyiciyi diziye aktarır.
-`off`: diziden belirli dinleyiciyi filtreler.
-`emit`: diziyi yineleyin ve her dinleyiciyi yayılmış argümanlarla çağırın.
-`once`: dinleyiciyi ilk çağrıdan sonra kendisini kaldıran bir işleve sarın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- `emit`'deki`[...listeners]`kopyası, yineleme sırasında bir dinleyicinin `off`'yi çağırması durumunda sorunları önler.
- `once`, `_original`'yi saklar, böylece arayanlar ambalajı`off(event, originalFn)`aracılığıyla kaldırabilir.
- Özel alanlar (`#listeners`) dahili durumun harici değişimini önler.
- Üretim için:`maxListeners`uyarısını (Node.js gibi), dinleyici başına hata işlemeyi ve öncelik için `prependListener`'yi ekleyin.
---

## Özet
JavaScript kaçınılmazdır. Web tarayıcılarında çalışan tek dildir ve bu da onu ön uç geliştirme için gerekli kılar. Node.js ile sunucu tarafına uzanır, React Native ve Electron gibi frameworkler ile mobil ve masaüstüne ulaşır. Ekosistem programlamadaki en büyüğüdür. Dilin tuhaflıkları iyi biliniyor ve yönetilebilir; TypeScript yazma sorunlarına çözüm getiriyor. Tarayıcıda çalışan her şey için JavaScript yalnızca en iyi seçim değil aynı zamanda tek seçimdir.