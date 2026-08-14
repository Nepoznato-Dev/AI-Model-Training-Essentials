---
# Metadata
title: "JavaScript — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern JavaScript code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [javascript, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# জাভাস্ক্রিপ্ট — ইডিওম্যাটিক প্যাটার্নস এবং সর্বোত্তম অনুশীলন
এই নির্দেশিকাটি পরিচ্ছন্ন, আধুনিক জাভাস্ক্রিপ্ট (ES2024+) কোড লেখার জন্য বাহাদুরি প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## আধুনিক ঘোষণা
```javascript
// ❌ Avoid var
var name = "Alice";

// ✅ Use const by default, let when reassignment needed
const name = "Alice";
let count = 0;

// ✅ Destructuring
const { name, email, age } = user;
const [first, second, ...rest] = items;

// ✅ Destructuring with defaults
const { name = "Anonymous", role = "user" } = userData;

// ✅ Nested destructuring
const { address: { city, zip } } = user;
```

---

## তীর ফাংশন
```javascript
// ✅ Arrow for short functions
const double = (x) => x * 2;
const greet = (name) => `Hello, ${name}!`;

// ✅ Arrow for callbacks
const adults = users.filter((u) => u.age >= 18);
const names = users.map((u) => u.name);

// ❌ Don't use arrow for methods that need `this`
class Counter {
  constructor() { this.count = 0; }
  increment() { this.count++; }  // not arrow
}

// ✅ Use class fields with arrow for event handlers
class Button {
  handleClick = () => {
    this.count++;
  };
}
```

---

## টেমপ্লেট আক্ষরিক
```javascript
// ❌ String concatenation
const msg = "Hello, " + name + "! You are " + age + " years old.";

// ✅ Template literals
const msg = `Hello, ${name}! You are ${age} years old.`;

// ✅ Multi-line strings
const html = `
  <div class="card">
    <h2>${title}</h2>
    <p>${description}</p>
  </div>
`;

// ✅ Tagged templates
const highlight = (strings, ...values) =>
  strings.reduce((result, str, i) =>
    `${result}${str}<mark>${values[i] || ""}</mark>`, "");
```

---

## ছড়িয়ে দিন এবং বিশ্রাম করুন
```javascript
// ✅ Spread for arrays
const combined = [...arr1, ...arr2];
const copy = [...original];
const withExtra = [...items, "new"];

// ✅ Spread for objects
const updated = { ...user, name: "Bob", age: 31 };
const merged = { ...defaults, ...overrides };

// ✅ Rest parameters
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

// ✅ Rest in destructuring
const { name, ...rest } = user;
const [first, ...others] = items;
```

---

## অ্যাসিঙ্ক/অপেক্ষা করুন
```javascript
// ❌ Callback hell
getData((a) => {
  getMoreData(a, (b) => {
    getEvenMoreData(b, (c) => {
      console.log(c);
    });
  });
});

// ✅ async/await
async function processData() {
  try {
    const a = await getData();
    const b = await getMoreData(a);
    const c = await getEvenMoreData(b);
    return c;
  } catch (error) {
    console.error("Failed:", error);
  }
}

// ✅ Concurrent execution
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
]);

// ✅ Promise.allSettled for independent operations
const results = await Promise.allSettled([
  fetch("/api/users"),
  fetch("/api/posts"),
  fetch("/api/comments"),
]);
const successes = results.filter((r) => r.status === "fulfilled");
```

---

## অ্যারে পদ্ধতি
```javascript
// ✅ Functional array methods
const total = prices.reduce((sum, price) => sum + price, 0);
const names = users.filter((u) => u.active).map((u) => u.name);
const found = users.find((u) => u.id === 1);
const exists = users.some((u) => u.role === "admin");
const allActive = users.every((u) => u.active);
const first = items.at(0);
const last = items.at(-1);

// ✅ flat / flatMap
const nested = [[1, 2], [3, 4], [5]];
const flat = nested.flat();          // [1, 2, 3, 4, 5]
const flatMapped = users.flatMap((u) => u.roles);

// ✅ Grouping (ES2024)
const grouped = Object.groupBy(users, (u) => u.role);

// ✅ Chaining
const result = items
  .filter((item) => item.active)
  .map((item) => item.name)
  .sort()
  .join(", ");
```

---

## মডিউল
```javascript
// ✅ Named exports
export function add(a, b) { return a + b; }
export const PI = 3.14159;

// ✅ Default export (one per module)
export default class UserService { }

// ✅ Import
import UserService, { add, PI } from "./module.js";

// ✅ Re-export
export { default as UserService } from "./UserService.js";
export * from "./utils.js";

// ✅ Dynamic import
const module = await import("./heavy-module.js");
```

---

## ত্রুটি হ্যান্ডলিং
```javascript
// ✅ Custom error classes
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

// ✅ Try/catch with async
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    if (error instanceof ValidationError) throw error;
    console.error("Failed to fetch user:", error);
    throw error;
  }
}

// ✅ Global error handling
window.addEventListener("unhandledrejection", (event) => {
  console.error("Unhandled rejection:", event.reason);
});
```

---

## ক্লাস
```javascript
// ✅ Modern class syntax
class User {
  #name;  // private field
  
  constructor(name, email) {
    this.#name = name;
    this.email = email;
  }
  
  get name() { return this.#name; }
  
  greet() { return `Hello, I'm ${this.#name}`; }
  
  static create(data) {
    return new User(data.name, data.email);
  }
}

// ✅ Private methods
class Counter {
  #count = 0;
  
  increment() { this.#count++; }
  #validate(n) { return Number.isInteger(n) && n >= 0; }
}

// ✅ Inheritance
class Admin extends User {
  #permissions;
  
  constructor(name, email, permissions) {
    super(name, email);
    this.#permissions = permissions;
  }
}
```

---

## অবজেক্ট প্যাটার্ন
```javascript
// ✅ Object shorthand
const name = "Alice";
const user = { name, email: "alice@example.com" };

// ✅ Computed properties
const key = "dynamic";
const obj = { [key]: "value" };

// ✅ Optional chaining
const city = user?.address?.city;
const result = obj?.method?.();

// ✅ Nullish coalescing
const value = obj.prop ?? "default";
const count = arr?.length ?? 0;

// ✅ Object.fromEntries
const entries = [["a", 1], ["b", 2]];
const obj = Object.fromEntries(entries);

// ✅ StructuredClone for deep copy
const copy = structuredClone(original);
```

---

## সারাংশ
আধুনিক জাভাস্ক্রিপ্ট ইডিয়মগুলি জোর দেয়:`const`/`let`ওভার`var`, ধ্বংস, তীর ফাংশন, টেমপ্লেট লিটারাল, অ্যাসিঙ্ক/ওয়েট, স্প্রেড/রেস্ট অপারেটর, অ্যারে পদ্ধতি ( XQZMARKER3XZQZQZ/XQZMARKER3XZQZERK4`reduce`), ES মডিউল, ঐচ্ছিক চেইনিং (`?.`), নালিশ কোলেসিং (`??`), এবং ব্যক্তিগত সদস্যদের সাথে ক্লাস ক্ষেত্র। কোড মানের জন্য ESLint অনুসরণ করুন, ফরম্যাটিং এর জন্য সুন্দর, এবং পরিবর্তনযোগ্য অবস্থার চেয়ে কার্যকরী নিদর্শন পছন্দ করুন। জাভাস্ক্রিপ্ট সম্প্রদায় সংক্ষিপ্ততা, সংমিশ্রণযোগ্যতা এবং আধুনিক ES2024+ বৈশিষ্ট্যকে মূল্য দেয়।