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
JavaScript — это динамический интерпретируемый язык программирования, созданный Бренданом Эйхом всего за 10 дней в 1995 году. Первоначально созданный для добавления интерактивности веб-страницам, он превратился в наиболее широко используемый язык программирования в мире. JavaScript работает в каждом веб-браузере, на серверах через Node.js, в настольных приложениях (Electron), мобильных приложениях (React Native) и даже во встроенных системах.
Этот язык уникален тем, что это, по сути, единственный вариант веб-разработки на стороне клиента — каждый браузер поддерживает его изначально. Эта монополия в сочетании с развитием полнофункционального JavaScript (Node.js, Deno, Bun) делает его незаменимым.
---

## Почему JavaScript важен
- **Язык Интернета**: единственный язык, который изначально работает в браузерах. Альтернативы фронтенду нет.
- **Возможность полного стека**: один и тот же язык во внешнем интерфейсе (React, Vue, Svelte) и внутреннем интерфейсе (Node.js, Express, Fastify).
- **Огромная экосистема**: npm содержит более 2 миллионов пакетов — крупнейший реестр программного обеспечения в мире.
- **Универсальность**: веб-приложения, мобильные приложения (React Native), настольные приложения (Electron), Интернет вещей, бессерверные функции.
- **Низкий порог входа**: работает в любом браузере — для начала программирования установка не требуется.
- **Асинхронный дизайн**: управляемый событиями неблокирующий ввод-вывод делает его идеальным для приложений реального времени.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Ошибки динамического набора** | Никакой проверки типов во время компиляции; обнаружение ошибок во время выполнения | Используйте TypeScript (типизированный расширенный набор JavaScript) |
| **Сложность обратного вызова** | Вложенные обратные вызовы могут стать нечитаемыми («ад обратных вызовов») | Используйте обещания и async/await |
| **Причудливая семантика** | `==`vs`===`,`this`привязка, подъем, приведение типов | Изучите причуды; используйте ESLint; предпочитаю `const`/`let` вместо`var`|
| **Однопоточный** | Задачи, связанные с процессором, блокируют цикл событий | Используйте веб-воркеры, рабочие потоки или выгружайте их в собственные модули |
| **Качество упаковки** | открытость npm означает нестабильное качество и риски безопасности | Аудит зависимостей; использовать файлы блокировки; предпочитают ухоженные упаковки |
---

## Основы синтаксиса
### Переменные и типы
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

### Функции
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

### Объекты и классы
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

### Асинхронное программирование
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

### Модули
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

## Расширенный синтаксис и шаблоны
### Деструктуризация и распространение/отдых (глубокое погружение)
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

### Прокси и отражение
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

### Символы, итераторы и генераторы
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

### Пользовательские иерархии ошибок
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

## Параллелизм и параллелизм
JavaScript является однопоточным с циклом событий. Параллелизм достигается с помощью асинхронных шаблонов, веб-воркеров и (в Node.js) модуля worker_threads.
### Цикл событий
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

### Рабочие потоки (Node.js — задачи, связанные с ЦП)
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

### Веб-работники (браузер)
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

### Асинхронные шаблоны
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

## Конфигурация проекта и система сборки
### Структура каталога проекта
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

### Конфигурация сборки — `package.json`
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

### Конфигурация линтинга и форматирования
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

### Конвейер CI/CD — Действия GitHub
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

## Тестирование
### Тестирование с помощью Jest
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

### Мокинг и интеграционные тесты
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

## Совместимость
### Собственные дополнения с N-API (Node.js)
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

### Веб-сборка (Wasm)
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

### Вызов библиотек C с помощью ffi-napi
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

## Шаблоны проектирования
### Шаблон модуля (инкапсуляция)
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

### Шаблон наблюдателя/эмиттера событий
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

### Шаблон «Строитель»
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

## Производительность и оптимизация
### Инструменты профилирования
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

### Методы оптимизации
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

## Развертывание
### Докер-файл
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

### Развертывание для конкретной платформы
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

## Экосистема
### Фронтенд-фреймворки
| Рамочная | Подход | Лучшее для |
|-----------|----------|----------|
| **Реагировать** | Виртуальный DOM на основе компонентов | Крупномасштабные СПА; крупнейшая экосистема |
| **Вуэ** | Прогрессивный, на основе шаблонов | Постепенное принятие; отличный опыт разработчика |
| **Стройная** | Время компиляции, без виртуального DOM | Меньшие пакеты, более простой код |
| **Угловой** | Полная структура, прежде всего TypeScript | Корпоративные приложения; самоуверенная структура |
| **Next.js** | Метафреймворк React (SSR/SSG) | Производство приложений React с SEO |
### Бэкэнд (Node.js)
| Рамочная | Цель |
|-----------|---------|
| **Экспресс** | Минимальный, гибкий веб-фреймворк (самый популярный) |
| **Фиксировать** | Высокопроизводительный веб-фреймворк |
| **NestJS** | Архитектура корпоративного уровня, основанная на Angular |
| **Коа** | Легкая, современная альтернатива Express |
| **Честь** | Сверхбыстрый, многоисполняемый (Node, Deno, Bun, Edge) |
### Время выполнения
| Время выполнения | Описание |
|---------|-------------|
| **Node.js** | Исходная среда выполнения серверного JavaScript (движок V8) |
| **Дено** | Безопасно по умолчанию; встроенная поддержка TypeScript; создано оригинальным автором Node |
| **Булочка** | Сверхбыстрая универсальная среда выполнения, сборщик и менеджер пакетов |
### Основные инструменты
| Инструмент | Цель |
|------|---------|
| **npm / пряжа / pnpm** | Менеджеры пакетов |
| **Типскрипт** | Типизированный расширенный набор JavaScript |
| **ESLint** | Линтинг кода |
| **Красивее** | Форматирование кода |
| **Вите** | Инструмент быстрой сборки и сервер разработки |
| **Веб-пакет** | Сборщик модулей (зрелый, широко используемый) |
| **Джест / Витест** | Платформы тестирования |
---

## Когда использовать JavaScript
| Сценарий | Почему JavaScript | Лучшая альтернатива |
|----------|---------------|-------------------|
| Веб-интерфейс | Единственный вариант для пользовательского интерфейса на основе браузера | — |
| Полнофункциональный веб-интерфейс | Везде один и тот же язык | TypeScript для безопасности типов |
| Приложения реального времени (чат, игры) | Управляемый событиями неблокирующий ввод-вывод | — |
| Бессерверные функции | Быстро писать, развертывать где угодно | Питон, Го |
| Мобильные приложения (React Native) | Поделиться кодом с Интернетом | Flutter, родной Swift/Kotlin |
| Настольные приложения (электронные) | Кроссплатформенность с веб-технологиями | C# (WPF), Таури (Rust) |
| Вычисления с интенсивным использованием процессора | Однопоточное ограничение | Python (NumPy), C++, Rust, WebAssembly |
| Системное программирование | Неправильный уровень абстракции | C, C++, Rust, Go |
---

## Синтетические вопросы и ответы
### Вопрос 1: В чем разница между`var`,`let`и`const`и когда мне следует использовать каждый из них?
**A:**`var`ограничен функцией и поднят — избегайте этого в современном коде. `let`имеет блочную область действия и допускает переназначение. `const`имеет блочную область действия и предотвращает переназначение (но объекты/массивы, на которые он ссылается, по-прежнему изменяемы). Рекомендация: по умолчанию используется `const`, используйте`let`только при необходимости переназначения, никогда не используйте `var`.
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Вопрос 2: Как`this`работает в JavaScript и почему это так сбивает с толку?
**A:**`this`определяется **как функция вызывается**, а не тем, где она определена. При вызове метода объектом является `this`. В автономном вызове это`undefined`(строгий режим) или`global`(нестрогий). Стрелочные функции наследуют`this`от своей области видимости — именно поэтому они предпочтительны для обратных вызовов. Используйте `.bind()`, чтобы явно установить `this`.
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

### Вопрос 3. Что такое цикл событий и как на самом деле работают async/await?
**О:** JavaScript является однопоточным с циклом событий, обрабатывающим очередь. Стек вызовов выполняет синхронный код. Когда он пуст, цикл событий выбирает следующую задачу из очереди микрозадач (обещания) или очереди макрозадач (setTimeout, I/O). `async/await`— это синтаксический сахар над промисами:`await`приостанавливает асинхронную функцию и возобновляет ее после разрешения промиса, не блокируя поток.
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

### Вопрос 4: Как обрабатывать ошибки в современном JavaScript?
**A:** Используйте`try/catch`для синхронного кода и`.catch()`или`try/catch`с`async/await`для асинхронного кода. Всегда обрабатывайте отклонения промисов — необработанные отклонения приводят к сбою Node.js. Создавайте собственные классы ошибок для ошибок, специфичных для предметной области. Используйте глобальный обработчик ошибок в качестве страховки.
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

### В5: Когда следует использовать `Map`/`Set` вместо простых объектов/массивов?
**A:** Используйте `Map`, когда ключи не являются строками, когда вам нужна итерация порядка вставки, когда вам нужен`.size`или когда вы часто добавляете или удаляете записи (более высокая производительность, чем у объектов). Используйте`Set`для уникальных коллекций с поиском O(1) — гораздо быстрее, чем`array.includes()`для больших наборов данных. Используйте простые объекты для простых сериализуемых в формате JSON данных и небольших карт «ключ-значение» со строковыми ключами.
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

## Решение проблем с цепочкой мыслей
### Проблема 1: реализация функции устранения дребезга
**Постановка проблемы:** Реализуйте утилиту `debounce`, которая откладывает вызов функции до тех пор, пока не истечет указанный период ожидания с момента последнего ее вызова. Поддержка как ведущего, так и заднего фронта вызова.
**Шаг 1. Поймите проблему:**
Функция с устранением дребезга игнорирует быстрые последовательные вызовы и срабатывает только после того, как вызовы прекращаются на время ожидания. «Передовой» означает огонь сразу по первому вызову. «Задний край» означает пожар после периода ожидания. Нам нужно обрабатывать оба режима, а также поддерживать отмену.
**Шаг 2. Определите подход:**
- Сохраните идентификатор таймера в замыкании.
- При каждом вызове: очистите существующий таймер, затем установите новый `setTimeout`.
- Для переднего фронта: немедленно позвоните, если таймер не активен.
- Верните функцию с устранением дребезга с помощью метода `.cancel()`.
— Сохраняйте контекст и аргументы`this`с помощью стрелочных функций или `.apply()`.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Замыкание сохраняет состояние между вызовами, не загрязняя глобальную область видимости.
-`clearTimeout`перед`setTimeout`гарантирует, что только последний вызов запускает выполнение.
—`.cancel()`важен для очистки (например, отмонтирования компонента в React).
Крайний случай: если`wait`равен 0, функция срабатывает при следующем тике цикла событий — полезно для пакетной обработки обновлений DOM.
### Проблема 2: Создайте ограничитель скорости на основе обещаний
**Постановка задачи:** Создайте ограничитель скорости, который разрешает не более N запросов за временной интервал. Он должен возвращать обещания, которые разрешаются, когда вызывающему разрешено продолжить, и ставить в очередь лишние запросы.
**Шаг 1. Поймите проблему:**
Нам нужно скользящее или фиксированное окно, отслеживающее количество совершенных вызовов. При достижении лимита новые вызовы должны быть поставлены в очередь и разрешены при открытии слота. Это шаблон «ведро токенов».
**Шаг 2. Определите подход:**
- Отслеживание временных меток недавних звонков в массиве.
- При каждом вызове: удалите временные метки старше окна, проверьте, <лимит ли количество.
- Если лимит ниже: решите немедленно.
- Если предел: вычислите, когда истечет срок действия самой старой временной метки, установите`setTimeout`, а затем разрешите.
- Используйте очередь (массив функций разрешения) для ожидающих вызывающих абонентов.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Подход со скользящим окном более справедлив, чем с фиксированными окнами (без разрывов на границах окна).
- Обработка очереди осуществляется по принципу FIFO — звонящие обслуживаются по порядку.
- Для производства: добавьте поддержку `AbortController`, чтобы вызывающие абоненты могли отменить ожидание.
- Производительность:`_cleanOldTimestamps`равен O(n) на вызов, но n ограничено `maxCalls`.
### Проблема 3: реализация функции глубокого клонирования
**Постановка задачи:** Напишите функцию, которая глубоко клонирует любое значение JavaScript, обрабатывая объекты, массивы, даты, регулярные выражения, карты, наборы, циклические ссылки и типизированные массивы.
**Шаг 1. Поймите проблему:**
`JSON.parse(JSON.stringify(obj))`завершается с ошибкой:`undefined`, функции, символы, даты (становятся строками), регулярные выражения (становятся пустыми объектами), карты, наборы, циклические ссылки (выбрасывают) и типизированные массивы. Нам нужно рекурсивное решение, отслеживающее посещенные объекты.
**Шаг 2. Определите подход:**
— Используйте`Map`для отслеживания уже клонированных объектов (обрабатывает циклические ссылки).
- Обрабатывайте каждый тип особым образом: Дата → новая дата, RegExp → новое RegExp, Карта → новая карта с клонированными записями, Set → новый набор с клонированными значениями.
- Используйте`structuredClone()`в качестве современной встроенной альтернативы (доступно в браузерах и Node.js 17+).
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Циклические ссылки: карта`seen`возвращает уже созданный клон вместо бесконечной рекурсии.
— Дескрипторы свойств:`Reflect.ownKeys`+`getOwnPropertyDescriptor`сохраняют методы получения, установки и неперечислимые свойства.
— Современная альтернатива:`structuredClone(value)`изначально обрабатывает большинство этих случаев (кроме функций и узлов DOM). Предпочитаю его, когда он доступен.
- Производительность: для простых объектов`JSON.parse(JSON.stringify(obj))`по-прежнему самый быстрый. Используйте глубокое клонирование только тогда, когда оно вам действительно нужно.
### Проблема 4. Создайте простой генератор событий
**Постановка проблемы:** Реализуйте класс отправителя событий, который поддерживает методы`on`,`off`,`emit`и `once`. Слушателей следует вызывать в порядке регистрации. `emit`должен передавать аргументы всем слушателям.
**Шаг 1. Поймите проблему:**
Нам нужна система публикации/подписки: регистрировать прослушиватели для именованных событий, удалять определенные прослушиватели, запускать события с аргументами и поддерживать одноразовые прослушиватели. Это шаблон Observer, широко используемый в Node.js.
**Шаг 2. Определите подход:**
— Сохраните прослушиватели в `Map<string, Array<Function>>`.
- `on`: отправить прослушиватель в массив.
- `off`: отфильтровать конкретного прослушивателя из массива.
- `emit`: перебирать массив и вызывать каждого прослушивателя с расширенными аргументами.
- `once`: обернуть прослушиватель в функцию, которая удаляется после первого вызова.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Копия`[...listeners]`в`emit`предотвращает проблемы, когда прослушиватель вызывает`off`во время итерации.
-`once`сохраняет `_original`, поэтому вызывающие абоненты могут удалить оболочку через `off(event, originalFn)`.
— Частные поля (`#listeners`) предотвращают внешнюю мутацию внутреннего состояния.
- Для производства: добавьте предупреждение`maxListeners`(например, Node.js), обработку ошибок для каждого прослушивателя и`prependListener`для приоритета.
---

## Краткое содержание
JavaScript неизбежен. Это единственный язык, который работает в веб-браузерах, поэтому он необходим для разработки внешнего интерфейса. С помощью Node.js он распространяется на серверную часть, а с помощью таких фреймворков, как React Native и Electron, — на мобильные и настольные компьютеры. Экосистема является крупнейшей в программировании. Особенности языка хорошо известны и ими можно управлять, а TypeScript решает проблемы типизации. Для всего, что работает в браузере, JavaScript — не просто лучший выбор, это единственный выбор.