---
# البيانات الوصفية
العنوان: "جافا سكريبت"
description: "مرجع شامل للغة برمجة JavaScript يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [جافا سكريبت، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "44 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
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
| ** دلالات ملتوية ** |  __محمي_0__ مقابل __محمي_1__، __محمي_2__ ربط، رفع، نوع الإكراه | تعلم المراوغات. استخدم ESLint؛ تفضل`const`/`let`على`var`|
| ** خيط واحد ** | المهام المرتبطة بوحدة المعالجة المركزية تحظر حلقة الحدث | استخدم عمال الويب أو سلاسل العمليات أو قم بإلغاء التحميل إلى الوحدات النمطية الأصلية |
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

### تكوين التكوين — __محمي_0__
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
| برمجة الأنظمة | مستوى تجريد خاطئ | C، C++، الصدأ، الذهاب |
---

## ملخص
جافا سكريبت لا مفر منه. إنها اللغة الوحيدة التي تعمل في متصفحات الويب، مما يجعلها ضرورية لتطوير الواجهة الأمامية. مع Node.js، يمتد الأمر إلى جانب الخادم، ومع أطر عمل مثل React Native وElectron، يصل إلى الهاتف المحمول وسطح المكتب. النظام البيئي هو الأكبر في البرمجة. إن خصوصيات اللغة معروفة ويمكن التحكم فيها، ويعالج TypeScript مشكلات الكتابة. بالنسبة لأي شيء يتم تشغيله في المتصفح، فإن JavaScript ليس الخيار الأفضل فحسب، بل هو الخيار الوحيد.