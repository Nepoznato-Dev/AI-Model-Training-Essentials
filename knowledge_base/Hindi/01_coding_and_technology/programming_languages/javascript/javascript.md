---
# मेटाडेटा
शीर्षक: "जावास्क्रिप्ट"
विवरण: "जावास्क्रिप्ट प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [जावास्क्रिप्ट, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "44 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
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
| **विचित्र शब्दार्थ** | `==`बनाम`===`,`this`बाइंडिंग, उत्थापन, प्रकार की जबरदस्ती | विचित्रताएँ सीखें; ESLint का उपयोग करें;`var`की तुलना में`const`/`let`को प्राथमिकता दें |
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

### कॉन्फ़िगरेशन बनाएँ — `package.json`
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

## सारांश
जावास्क्रिप्ट अपरिहार्य है. यह एकमात्र भाषा है जो वेब ब्राउज़र में चलती है, जो इसे फ्रंटएंड विकास के लिए आवश्यक बनाती है। Node.js के साथ, यह सर्वर साइड तक विस्तारित होता है, और रिएक्ट नेटिव और इलेक्ट्रॉन जैसे फ्रेमवर्क के साथ, यह मोबाइल और डेस्कटॉप तक पहुंचता है। प्रोग्रामिंग में पारिस्थितिकी तंत्र सबसे बड़ा है। भाषा की विचित्रताएँ सर्वविदित और प्रबंधनीय हैं - और टाइपस्क्रिप्ट टाइपिंग संबंधी चिंताओं का समाधान करता है। ब्राउज़र में चलने वाली किसी भी चीज़ के लिए, जावास्क्रिप्ट न केवल सबसे अच्छा विकल्प है - यह एकमात्र विकल्प है।