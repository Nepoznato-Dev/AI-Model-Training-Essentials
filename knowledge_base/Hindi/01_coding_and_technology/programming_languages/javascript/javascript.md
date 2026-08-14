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

#जावास्क्रिप्ट
जावास्क्रिप्ट एक गतिशील, व्याख्या की गई प्रोग्रामिंग भाषा है जिसे ब्रेंडन ईच ने 1995 में केवल 10 दिनों में बनाया था। मूल रूप से वेब पेजों में अन्तरक्रियाशीलता जोड़ने के लिए डिज़ाइन किया गया था, यह दुनिया में सबसे व्यापक रूप से उपयोग की जाने वाली प्रोग्रामिंग भाषा बन गई है। जावास्क्रिप्ट प्रत्येक वेब ब्राउज़र में, Node.js के माध्यम से सर्वर पर, डेस्कटॉप ऐप्स (इलेक्ट्रॉन), मोबाइल ऐप्स (रिएक्ट नेटिव) और यहां तक ​​कि एम्बेडेड सिस्टम में भी चलता है।
यह भाषा इस मायने में अद्वितीय है कि यह अनिवार्य रूप से क्लाइंट-साइड वेब विकास के लिए एकमात्र विकल्प है - प्रत्येक ब्राउज़र मूल रूप से इसका समर्थन करता है। फुल-स्टैक जावास्क्रिप्ट (नोड.जेएस, डेनो, बन) के उदय के साथ मिलकर यह एकाधिकार इसे अपरिहार्य बनाता है।
---

## जावास्क्रिप्ट क्यों मायने रखती है
- **वेब की भाषा**: एकमात्र भाषा जो ब्राउज़र में मूल रूप से चलती है। फ्रंटएंड के लिए कोई विकल्प नहीं.
- **पूर्ण-स्टैक क्षमता**: फ्रंटएंड (रिएक्ट, व्यू, स्वेल्ट) और बैकएंड (नोड.जेएस, एक्सप्रेस, फास्टिफ़ाइ) पर समान भाषा।
- **विशाल पारिस्थितिकी तंत्र**: एनपीएम में 2 मिलियन से अधिक पैकेज हैं - दुनिया में सबसे बड़ी सॉफ्टवेयर रजिस्ट्री।
- **बहुमुखी प्रतिभा**: वेब ऐप्स, मोबाइल ऐप्स (रिएक्ट नेटिव), डेस्कटॉप ऐप्स (इलेक्ट्रॉन), IoT, सर्वर रहित फ़ंक्शन।
- **प्रवेश के लिए कम बाधा**: किसी भी ब्राउज़र में चलता है - कोडिंग शुरू करने के लिए किसी इंस्टॉलेशन की आवश्यकता नहीं है।
- **डिज़ाइन द्वारा अतुल्यकालिक**: इवेंट-संचालित, गैर-अवरुद्ध I/O इसे वास्तविक समय के अनुप्रयोगों के लिए उत्कृष्ट बनाता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **डायनेमिक टाइपिंग के नुकसान** | कोई संकलन-समय प्रकार की जाँच नहीं; रनटाइम पर बग सतह पर आते हैं | टाइपस्क्रिप्ट (जावास्क्रिप्ट का एक टाइप किया हुआ सुपरसेट) का उपयोग करें |
| **कॉलबैक जटिलता** | नेस्टेड कॉलबैक अपठनीय हो सकते हैं ("कॉलबैक नरक") | वादों और async/प्रतीक्षा का उपयोग करें |
| **विचित्र शब्दार्थ** | `==`बनाम`===`,`this`बाइंडिंग, उत्थापन, प्रकार जबरदस्ती | विचित्रताएँ सीखें; ESLint का उपयोग करें;`var`की तुलना में`const`/`let`को प्राथमिकता दें |
| **सिंगल-थ्रेडेड** | सीपीयू-बाउंड कार्य इवेंट लूप को ब्लॉक करते हैं | वेब वर्कर्स, वर्कर थ्रेड्स का उपयोग करें, या मूल मॉड्यूल पर ऑफलोड करें |
| **पैकेज गुणवत्ता** | एनपीएम के खुलेपन का मतलब है असंगत गुणवत्ता और सुरक्षा जोखिम | लेखापरीक्षा निर्भरताएँ; लॉक फ़ाइलों का उपयोग करें; सुव्यवस्थित पैकेज को प्राथमिकता दें |
---

## सिंटेक्स बुनियादी बातें
### चर और प्रकार
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

### कार्य
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

### वस्तुएं और कक्षाएं
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

### एसिंक प्रोग्रामिंग
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

### मॉड्यूल
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

## उन्नत सिंटैक्स और पैटर्न
### विध्वंस और फैलाव/विश्राम (गहरा गोता)
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

### प्रॉक्सी और प्रतिबिंबित
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

### प्रतीक, इटरेटर और जेनरेटर
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

### कस्टम त्रुटि पदानुक्रम
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

## समवर्ती एवं समांतरता
जावास्क्रिप्ट इवेंट लूप के साथ सिंगल-थ्रेडेड है। समकालिकता एसिंक्रोनस पैटर्न, वेब वर्कर्स और (Node.js में) वर्कर_थ्रेड्स मॉड्यूल के माध्यम से प्राप्त की जाती है।
### इवेंट लूप
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

### वर्कर थ्रेड्स (नोड.जेएस - सीपीयू-बाउंड कार्य)
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

### वेब वर्कर्स (ब्राउज़र)
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

### एसिंक पैटर्न
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना निर्देशिका संरचना
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

### कॉन्फ़िगरेशन बनाएँ - `package.json`
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

### लिंटिंग और फ़ॉर्मेटिंग कॉन्फ़िगरेशन
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

### सीआई/सीडी पाइपलाइन - गिटहब क्रियाएँ
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

## परीक्षण
### जेस्ट के साथ परीक्षण
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

### मॉकिंग और एकीकरण परीक्षण
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

## अंतरसंचालनीयता
### एन-एपीआई (नोड.जेएस) के साथ नेटिव ऐडऑन
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

### वेबअसेंबली (Wasm)
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

### एफएफआई-नेपी के साथ सी लाइब्रेरीज़ को कॉल करना
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

## डिज़ाइन पैटर्न
### मॉड्यूल पैटर्न (एनकैप्सुलेशन)
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

### प्रेक्षक/घटना उत्सर्जक पैटर्न
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

### बिल्डर पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### अनुकूलन तकनीकें
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

## तैनाती
### डॉकरफ़ाइल
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

### प्लेटफ़ॉर्म-विशिष्ट परिनियोजन
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

## पारिस्थितिकी तंत्र
### फ्रंटएंड फ्रेमवर्क
| ढाँचा | दृष्टिकोण | के लिए सर्वश्रेष्ठ |
|----|---|---|
| **प्रतिक्रिया** | घटक-आधारित, वर्चुअल DOM | बड़े पैमाने पर एसपीए; सबसे बड़ा पारिस्थितिकी तंत्र |
| **व्यू** | प्रगतिशील, टेम्पलेट-आधारित | धीरे-धीरे गोद लेना; बेहतरीन डेवलपर अनुभव |
| **सुंदर** | संकलन-समय, कोई वर्चुअल DOM नहीं | छोटे बंडल, सरल कोड |
| **कोणीय** | पूर्ण रूपरेखा, टाइपस्क्रिप्ट-प्रथम | एंटरप्राइज़ ऐप्स; विचारशील संरचना |
| **अगला.जेएस** | रिएक्ट मेटा-फ्रेमवर्क (एसएसआर/एसएसजी) | एसईओ के साथ प्रोडक्शन रिएक्ट ऐप्स |
### बैकएंड (नोड.जेएस)
| ढाँचा | उद्देश्य |
|----|----|
| **एक्सप्रेस** | न्यूनतम, लचीला वेब ढांचा (सबसे लोकप्रिय) |
| **उपवास** | उच्च-प्रदर्शन वेब ढाँचा |
| **NestJS** | एंटरप्राइज-ग्रेड, कोणीय-प्रेरित वास्तुकला |
| **कोआ** | हल्का, आधुनिक एक्सप्रेस विकल्प |
| **आदरणीय** | अल्ट्रा-फास्ट, मल्टी-रनटाइम (नोड, डेनो, बन, एज) |
### रनटाइम्स
| रनटाइम | विवरण |
|---------|-----------------|
| **नोड.जेएस** | मूल सर्वर-साइड जावास्क्रिप्ट रनटाइम (V8 इंजन) |
| **डेनो** | डिफ़ॉल्ट रूप से सुरक्षित; देशी टाइपस्क्रिप्ट समर्थन; नोड के मूल लेखक द्वारा बनाया गया |
| **बन** | अल्ट्रा-फास्ट ऑल-इन-वन रनटाइम, बंडलर और पैकेज मैनेजर |
### आवश्यक उपकरण
| उपकरण | उद्देश्य |
|------|---------|
| **एनपीएम/यार्न/पीएनपीएम** | पैकेज प्रबंधक |
| **टाइपस्क्रिप्ट** | जावास्क्रिप्ट का टाइप किया गया सुपरसेट |
| **एसलिंट** | कोड लिंटिंग |
| **सुंदर** | कोड फ़ॉर्मेटिंग |
| **विटे** | फास्ट बिल्ड टूल और डेव सर्वर |
| **वेबपैक** | मॉड्यूल बंडलर (परिपक्व, व्यापक रूप से प्रयुक्त) |
| **जेस्ट/विटेस्ट** | परीक्षण ढाँचे |
---

## जावास्क्रिप्ट का उपयोग कब करें
| परिदृश्य | जावास्क्रिप्ट क्यों | बेहतर विकल्प |
|---|----------------------|-----|
| वेब फ्रंटएंड | ब्राउज़र-आधारित यूआई के लिए एकमात्र विकल्प | — |
| फुल-स्टैक वेब | हर जगह एक ही भाषा | प्रकार की सुरक्षा के लिए टाइपस्क्रिप्ट |
| रीयल-टाइम ऐप्स (चैट, गेम) | इवेंट-संचालित, गैर-अवरुद्ध I/O | — |
| सर्वर रहित कार्य | लिखने में तेज, कहीं भी तैनात | अजगर, जाओ |
| मोबाइल ऐप्स (रिएक्ट नेटिव) | वेब के साथ कोड साझा करें | स्पंदन, देशी स्विफ्ट/कोटलिन |
| डेस्कटॉप ऐप्स (इलेक्ट्रॉन) | वेब तकनीक के साथ क्रॉस-प्लेटफ़ॉर्म | सी# (डब्ल्यूपीएफ), तौरी (जंग) |
| सीपीयू-गहन संगणना | सिंगल-थ्रेडेड सीमा | पायथन (NumPy), C++, रस्ट, WebAssembly |
| सिस्टम प्रोग्रामिंग | गलत अमूर्तन स्तर | सी, सी++, रस्ट, गो |
---

## सिंथेटिक प्रश्नोत्तर
### Q1:`var`,`let`और`const`के बीच क्या अंतर है, और मुझे प्रत्येक का उपयोग कब करना चाहिए?
**ए:**`var`फ़ंक्शन-स्कोप्ड और फहराया गया है - आधुनिक कोड में इससे बचें। `let`ब्लॉक-स्कोप्ड है और पुन:असाइनमेंट की अनुमति देता है। `const`ब्लॉक-स्कोप्ड है और पुन:असाइनमेंट को रोकता है (लेकिन इसके द्वारा संदर्भित ऑब्जेक्ट/सरणी अभी भी परिवर्तनशील हैं)। सर्वोत्तम अभ्यास:`const`के लिए डिफ़ॉल्ट,`let`का उपयोग केवल तभी करें जब आपको पुन: असाइनमेंट की आवश्यकता हो, कभी भी`var`का उपयोग न करें।
```javascript
const API_URL = "https://api.example.com";  // Never changes
let retryCount = 0;                          // Needs reassignment
retryCount++;

// const with objects — the binding is const, not the content
const user = { name: "Alice" };
user.name = "Bob";        // OK — property mutation allowed
// user = {};              // TypeError — reassignment not allowed
```

### Q2:`this`जावास्क्रिप्ट में कैसे काम करता है, और यह इतना भ्रमित करने वाला क्यों है?
**ए:**`this`**किसी फ़ंक्शन को कैसे कॉल किया जाता है** से निर्धारित होता है, न कि इसे कहां परिभाषित किया गया है। एक विधि कॉल में,`this`ऑब्जेक्ट है। स्टैंडअलोन कॉल में, यह`undefined`(सख्त मोड) या`global`(गैर-सख्त) है। एरो फ़ंक्शंस को उनके संलग्न दायरे से`this`विरासत में मिलता है - यही कारण है कि उन्हें कॉलबैक के लिए प्राथमिकता दी जाती है।`this`को स्पष्ट रूप से सेट करने के लिए`.bind()`का उपयोग करें।
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

### Q3: इवेंट लूप क्या है, और async/await वास्तव में कैसे काम करता है?
**ए:** जावास्क्रिप्ट एक इवेंट लूप के साथ एकल-थ्रेडेड है जो एक कतार को संसाधित करता है। कॉल स्टैक सिंक्रोनस कोड निष्पादित करता है। जब यह खाली होता है, तो इवेंट लूप माइक्रोटास्क कतार (वादे) या मैक्रोटास्क कतार (सेटटाइमआउट, I/O) से अगला कार्य चुनता है। `async/await`वादों पर वाक्यात्मक चीनी है -`await`async फ़ंक्शन को रोक देता है और जब वादा हल हो जाता है, तो थ्रेड को अवरुद्ध किए बिना फिर से शुरू करता है।
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

### प्रश्न4: मुझे आधुनिक जावास्क्रिप्ट में त्रुटियों को कैसे संभालना चाहिए?
**ए:** सिंक्रोनस कोड के लिए`try/catch`और एसिंक्रोनस कोड के लिए`async/await`के साथ`.catch()`या`try/catch`का उपयोग करें। हमेशा प्रॉमिस अस्वीकृतियों को संभालें - बिना संभाले अस्वीकृतियाँ Node.js को क्रैश कर देती हैं। डोमेन-विशिष्ट त्रुटियों के लिए कस्टम त्रुटि वर्ग बनाएं। सुरक्षा जाल के रूप में वैश्विक त्रुटि हैंडलर का उपयोग करें।
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

### Q5: मुझे सादे ऑब्जेक्ट/सरणी के बजाय`Map`/`Set`का उपयोग कब करना चाहिए?
**ए:** जब कुंजियाँ स्ट्रिंग नहीं होती हैं, जब आपको सम्मिलन-क्रम पुनरावृत्ति की आवश्यकता होती है, जब आपको`.size`की आवश्यकता होती है, या जब आप अक्सर प्रविष्टियाँ जोड़ते/हटाते हैं (ऑब्जेक्ट्स की तुलना में बेहतर प्रदर्शन) तो`Map`का उपयोग करें। O(1) लुकअप के साथ अद्वितीय संग्रह के लिए`Set`का उपयोग करें - बड़े डेटासेट के लिए`array.includes()`की तुलना में बहुत तेज़। सरल JSON-क्रमबद्ध डेटा और स्ट्रिंग कुंजियों के साथ छोटे कुंजी-मूल्य मानचित्रों के लिए सादे ऑब्जेक्ट का उपयोग करें।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: डिबाउंस फ़ंक्शन लागू करें
**समस्या कथन:** एक`debounce`उपयोगिता लागू करें जो किसी फ़ंक्शन को लागू करने में तब तक देरी करती है जब तक कि पिछली बार कॉल किए जाने के बाद एक निर्दिष्ट प्रतीक्षा अवधि समाप्त न हो जाए। अग्रणी और अनुगामी दोनों प्रकार के आह्वान का समर्थन करें।
**चरण 1 - समस्या को समझें:**
एक डिबाउंस्ड फ़ंक्शन तेजी से आने वाली कॉलों को नजरअंदाज कर देता है और प्रतीक्षा अवधि के लिए कॉल रुकने के बाद ही सक्रिय होता है। "अग्रणी धार" का अर्थ है पहली कॉल पर तुरंत फायर करना। "ट्रेलिंग एज" का अर्थ है प्रतीक्षा अवधि के बाद आग। हमें दोनों मोड को संभालने की जरूरत है और कैंसिलेशन का भी समर्थन करना है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- एक क्लोजर में टाइमर आईडी स्टोर करें।
- प्रत्येक कॉल पर: मौजूदा टाइमर साफ़ करें, फिर एक नया`setTimeout`सेट करें।
- अग्रणी बढ़त के लिए: यदि कोई टाइमर सक्रिय नहीं है तो तुरंत कॉल करें।
-`.cancel()`विधि के साथ एक डिबाउंस फ़ंक्शन लौटाएं।
- एरो फ़ंक्शंस या`.apply()`का उपयोग करके`this`संदर्भ और तर्कों को संरक्षित करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- समापन वैश्विक दायरे को प्रदूषित किए बिना सभी कॉलों की स्थिति को सुरक्षित रखता है।
-`setTimeout`से पहले`clearTimeout`केवल अंतिम कॉल ट्रिगर निष्पादन को सुनिश्चित करता है।
-`.cancel()`सफाई के लिए महत्वपूर्ण है (उदाहरण के लिए, रिएक्ट में घटक अनमाउंट)।
- एज केस: यदि`wait`0 है, तो फ़ंक्शन अगले इवेंट लूप टिक पर सक्रिय होता है - DOM अपडेट को बैचने के लिए उपयोगी।
### समस्या 2: वादा-आधारित दर सीमक बनाएं
**समस्या कथन:** एक दर अवरोधक बनाएं जो प्रति समय विंडो में अधिकतम एन अनुरोधों की अनुमति देता है। इसे ऐसे वादे लौटाने चाहिए जो कॉल करने वाले को आगे बढ़ने की अनुमति मिलने पर हल हो जाएं और अतिरिक्त अनुरोधों को कतारबद्ध कर दें।
**चरण 1 - समस्या को समझें:**
हमें एक स्लाइडिंग या फिक्स्ड विंडो की आवश्यकता है जो ट्रैक करे कि कितनी कॉल की गई हैं। जब सीमा पूरी हो जाती है, तो नई कॉलों को कतारबद्ध किया जाना चाहिए और एक स्लॉट खुलने पर हल किया जाना चाहिए। यह "टोकन बकेट" पैटर्न है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- किसी सरणी में हाल की कॉल के टाइमस्टैम्प को ट्रैक करें।
- प्रत्येक कॉल पर: विंडो से पुराने टाइमस्टैम्प हटाएं, जांचें कि क्या गिनती <सीमा है।
- यदि सीमा के अंतर्गत है: तुरंत समाधान करें।
- यदि सीमा पर है: सबसे पुराना टाइमस्टैम्प समाप्त होने पर गणना करें,`setTimeout`सेट करें, फिर हल करें।
- प्रतीक्षारत कॉल करने वालों के लिए एक कतार (समाधान कार्यों की श्रृंखला) का उपयोग करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- स्लाइडिंग विंडो का दृष्टिकोण निश्चित विंडो की तुलना में अधिक उचित है (खिड़की की सीमाओं पर कोई विस्फोट नहीं)।
- कतार प्रसंस्करण फीफो है - कॉल करने वालों को क्रम में सेवा दी जाती है।
- उत्पादन के लिए:`AbortController`समर्थन जोड़ें ताकि कॉल करने वाले प्रतीक्षा रद्द कर सकें।
- प्रदर्शन:`_cleanOldTimestamps`प्रति कॉल O(n) है लेकिन n`maxCalls`से घिरा है।
### समस्या 3: एक डीप क्लोन फ़ंक्शन लागू करें
**समस्या कथन:** एक फ़ंक्शन लिखें जो किसी भी जावास्क्रिप्ट मान को गहराई से क्लोन करता है, वस्तुओं, सरणियों, तिथियों, रेगएक्सप्स, मानचित्रों, सेटों, परिपत्र संदर्भों और टाइप किए गए सरणियों को संभालता है।
**चरण 1 - समस्या को समझें:**
`JSON.parse(JSON.stringify(obj))`विफल रहता है: `undefined`, फ़ंक्शंस, प्रतीक, दिनांक (स्ट्रिंग्स बन जाते हैं), रेगएक्सप्स (खाली ऑब्जेक्ट बन जाते हैं), मैप्स, सेट, परिपत्र संदर्भ (थ्रो), और टाइप किए गए एरे। हमें एक पुनरावर्ती समाधान की आवश्यकता है जो विज़िट की गई वस्तुओं को ट्रैक करता है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- पहले से क्लोन की गई वस्तुओं को ट्रैक करने के लिए`Map`का उपयोग करें (गोलाकार संदर्भों को संभालता है)।
- प्रत्येक प्रकार को विशेष रूप से संभालें: दिनांक → नई तिथि, रेगएक्सपी → नया रेगएक्सपी, मानचित्र → क्लोन प्रविष्टियों के साथ नया मानचित्र, सेट → क्लोन किए गए मानों के साथ नया सेट।
- आधुनिक अंतर्निर्मित विकल्प के रूप में`structuredClone()`का उपयोग करें (ब्राउज़र और Node.js 17+ में उपलब्ध)।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- परिपत्र संदर्भ:`seen`मानचित्र अनंत बार पुनरावृत्ति करने के बजाय पहले से निर्मित क्लोन लौटाता है।
- संपत्ति विवरणक:`Reflect.ownKeys`+`getOwnPropertyDescriptor`गेटर्स, सेटर्स और गैर-गणना योग्य गुणों को संरक्षित करता है।
- आधुनिक विकल्प:`structuredClone(value)`इनमें से अधिकांश मामलों को मूल रूप से संभालता है (फ़ंक्शन और DOM नोड्स को छोड़कर)। उपलब्ध होने पर इसे प्राथमिकता दें।
- प्रदर्शन: साधारण वस्तुओं के लिए,`JSON.parse(JSON.stringify(obj))`अभी भी सबसे तेज़ है। डीप क्लोन का उपयोग तभी करें जब आपको वास्तव में इसकी आवश्यकता हो।
### समस्या 4: एक साधारण इवेंट एमिटर बनाएं
**समस्या कथन:** एक इवेंट एमिटर क्लास लागू करें जो `on`, `off`, `emit`, और`once`विधियों का समर्थन करता है। श्रोताओं को पंजीकरण क्रम में बुलाया जाना चाहिए। `emit`को सभी श्रोताओं को तर्क देना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें एक पब/उप प्रणाली की आवश्यकता है: नामित घटनाओं के लिए श्रोताओं को पंजीकृत करें, विशिष्ट श्रोताओं को हटाएं, तर्कों के साथ घटनाओं को ट्रिगर करें, और एक बार के श्रोताओं का समर्थन करें। यह ऑब्जर्वर पैटर्न है जिसका उपयोग Node.js में बड़े पैमाने पर किया जाता है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- श्रोताओं को`Map<string, Array<Function>>`में संग्रहित करें।
-`on`: श्रोता को सरणी में धकेलें।
-`off`: सरणी से विशिष्ट श्रोता को फ़िल्टर करें।
- `emit`: सरणी को पुनरावृत्त करें और प्रत्येक श्रोता को स्प्रेड तर्कों के साथ कॉल करें।
- `once`: श्रोता को एक फ़ंक्शन में लपेटें जो पहली कॉल के बाद खुद को हटा देता है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
-`emit`में`[...listeners]`कॉपी उन समस्याओं को रोकती है जब कोई श्रोता पुनरावृत्ति के दौरान`off`को कॉल करता है।
- `once`,`_original`को संग्रहीत करता है ताकि कॉल करने वाले`off(event, originalFn)`के माध्यम से रैपर को हटा सकें।
- निजी फ़ील्ड (`#listeners`) आंतरिक स्थिति के बाहरी उत्परिवर्तन को रोकते हैं।
- उत्पादन के लिए: प्राथमिकता के लिए`maxListeners`चेतावनी (जैसे Node.js), प्रति श्रोता त्रुटि प्रबंधन और`prependListener`जोड़ें।
---

## सारांश
जावास्क्रिप्ट अपरिहार्य है. यह एकमात्र भाषा है जो वेब ब्राउज़र में चलती है, जो इसे फ्रंटएंड विकास के लिए आवश्यक बनाती है। Node.js के साथ, यह सर्वर साइड तक विस्तारित होता है, और रिएक्ट नेटिव और इलेक्ट्रॉन जैसे फ्रेमवर्क के साथ, यह मोबाइल और डेस्कटॉप तक पहुंचता है। प्रोग्रामिंग में पारिस्थितिकी तंत्र सबसे बड़ा है। भाषा की विचित्रताएँ सर्वविदित और प्रबंधनीय हैं - और टाइपस्क्रिप्ट टाइपिंग संबंधी चिंताओं का समाधान करता है। ब्राउज़र में चलने वाली किसी भी चीज़ के लिए, जावास्क्रिप्ट न केवल सबसे अच्छा विकल्प है - यह एकमात्र विकल्प है।