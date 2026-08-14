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

# JavaScript — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔하고 현대적인 JavaScript(ES2024+) 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 현대 선언
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

## 화살표 기능
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

## 템플릿 리터럴
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

## 확산 및 휴식
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

## 비동기/대기
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

## 배열 방법
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

## 모듈
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

## 오류 처리
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

## 수업
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

## 객체 패턴
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

## 요약
최신 JavaScript 관용구는 `var`에 대한`const`/ `let`, 구조 분해, 화살표 함수, 템플릿 리터럴, 비동기/대기, 확산/휴식 연산자, 배열 메서드(`map`/`filter`/`reduce`), ES 모듈, 선택적 체이닝(`?.`), nullish 병합(`??`) 및 전용 멤버가 있는 클래스 필드. 코드 품질을 위해서는 ESLint를 따르고, 형식화를 위해서는 Prettier를 따르며, 변경 가능한 상태보다 기능적 패턴을 선호합니다. JavaScript 커뮤니티는 간결함, 구성 가능성 및 최신 ES2024+ 기능을 중요하게 생각합니다.