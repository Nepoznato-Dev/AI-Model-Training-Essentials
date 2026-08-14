<!--
---
# Metadata
title: "JavaScript — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern JavaScript code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# JavaScript - Miundo ya Idiomatic & Mazoezi Bora
Mwongozo huu unashughulikia ruwaza za nahau na mbinu bora za kuandika msimbo safi wa kisasa wa JavaScript (ES2024+).
---

## Matamko ya Kisasa
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

## Kazi za Mshale
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

## Vielelezo halisi
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

## Eneza & Upumzike
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

## Async/Subiri
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

## Mbinu za Mpangilio
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

##Moduli
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

## Kushughulikia Hitilafu
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

## Madarasa
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

## Miundo ya Kitu
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

## Muhtasari
Nahau za kisasa za JavaScript zinasisitiza:`const`/`let`juu ya`var`, uundaji, vitendaji vya mshale, maandishi halisi ya kiolezo, async/await, waendeshaji wa kueneza/pumzika, njia za safu (`map`/ XQZMARKER4ZZZZQZ) chaguo la XQZMARKER4QZZQZ RKZ, XQZMARKER4QZZQZ RKZ, XQZMARKER4QZZZQZ, XQZMARKER4XZQZ RKZ,`map`/ XQZ. (`?.`), kubatilisha kuunganisha (`??`), na nyanja za darasa na wanachama binafsi. Fuata ESLint kwa ubora wa msimbo, Nzuri zaidi kwa uumbizaji, na upendeze mifumo ya utendakazi kuliko hali inayoweza kubadilika. Jumuiya ya JavaScript inathamini ufupi, utunzi, na vipengele vya kisasa vya ES2024+.