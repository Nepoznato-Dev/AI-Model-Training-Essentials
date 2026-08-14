<!--
---
# Metadata
title: "JavaScript — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in JavaScript that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [javascript, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# JavaScript: errores comunes y antipatrones
Este documento cataloga los errores, trampas y antipatrones más comunes en JavaScript. Cada entrada muestra el enfoque incorrecto, explica por qué falla y proporciona la solución correcta.
---

## 1. Confusión de vinculación `this`
```javascript
// ❌ WRONG — `this` is lost in callback
class Button {
  constructor() {
    this.count = 0;
  }
  handleClick() {
    setTimeout(function() {
      this.count++;  // TypeError: Cannot read property 'count' of undefined
    }, 1000);
  }
}

// ✅ CORRECT — arrow function preserves `this`
handleClick() {
  setTimeout(() => {
    this.count++;
  }, 1000);
}

// ✅ CORRECT — explicit bind
setTimeout(function() {
  this.count++;
}.bind(this), 1000);
```

---

## 2. Aritmética de coma flotante
```javascript
// ❌ WRONG — expecting exact decimal math
0.1 + 0.2 === 0.3  // false! (0.30000000000000004)

// ✅ CORRECT — use epsilon comparison
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON  // true

// ✅ CORRECT — for money, use integer cents
const priceInCents = 1099;  // $10.99
const totalCents = priceInCents + 500;  // $15.99
```

---

## 3.`var`Problemas de elevación y alcance
```javascript
// ❌ WRONG — var is function-scoped, not block-scoped
for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 5, 5, 5, 5, 5 (not 0, 1, 2, 3, 4)

// ✅ CORRECT — use let (block-scoped)
for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 0, 1, 2, 3, 4

// ✅ CORRECT — var declarations are hoisted
console.log(x);  // undefined (not ReferenceError)
var x = 10;
// Equivalent to: var x; console.log(x); x = 10;
```

---

## 4. Comparando`==`con `===`
```javascript
// ❌ WRONG — loose equality performs type coercion
0 == ""        // true
0 == "0"       // true
"" == "0"      // true (not transitive!)
null == undefined  // true
false == 0     // true

// ✅ CORRECT — always use strict equality
0 === ""       // false
0 === "0"      // false
null === undefined  // false
```

---

## 5. No gestionar los rechazos de promesas
```javascript
// ❌ WRONG — unhandled rejection
async function fetchData() {
  const response = await fetch("/api/data");
  const data = await response.json();
  return data;
}
fetchData();  // If fetch fails: UnhandledPromiseRejection

// ✅ CORRECT — always handle errors
async function fetchData() {
  try {
    const response = await fetch("/api/data");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error("Fetch failed:", error);
    throw error;  // re-throw or handle
  }
}

// ✅ CORRECT — global handler as safety net
window.addEventListener("unhandledrejection", event => {
  console.error("Unhandled rejection:", event.reason);
});
```

---

## 6. Modificación de objetos durante la iteración
```javascript
// ❌ WRONG — deleting properties during for...in
const obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
  if (obj[key] < 2) delete obj[key];
}
// Unpredictable behavior

// ✅ CORRECT — collect keys first, then delete
const keysToDelete = Object.entries(obj)
  .filter(([_, v]) => v < 2)
  .map(([k]) => k);
keysToDelete.forEach(k => delete obj[k]);

// ✅ CORRECT — create a new object
const filtered = Object.fromEntries(
  Object.entries(obj).filter(([_, v]) => v >= 2)
);
```

---

## 7. Antipatrón: Infierno de devolución de llamada
```javascript
// ❌ WRONG — deeply nested callbacks
getUser(id, function(user) {
  getPosts(user, function(posts) {
    getComments(posts[0], function(comments) {
      getReplies(comments[0], function(replies) {
        console.log(replies);  // pyramid of doom
      });
    });
  });
});

// ✅ CORRECT — use async/await
async function getDiscussion(id) {
  const user = await getUser(id);
  const posts = await getPosts(user);
  const comments = await getComments(posts[0]);
  const replies = await getReplies(comments[0]);
  return replies;
}
```

---

## 8. Malentendido `typeof null`
```javascript
// ❌ WRONG — trusting typeof for null checks
typeof null   // "object" (historic bug, never fixed)
typeof undefined  // "undefined"

// ✅ CORRECT — use direct comparison
if (value === null) { ... }
if (value == null) { ... }  // catches both null and undefined
```

---

## 9. Los objetos similares a matrices no son matrices
```javascript
// ❌ WRONG — calling array methods on array-like objects
const nodeList = document.querySelectorAll("div");
nodeList.map(el => el.textContent);  // TypeError!

// ✅ CORRECT — convert to array first
const nodes = Array.from(nodeList);
const texts = nodes.map(el => el.textContent);

// ✅ CORRECT — spread syntax
const texts = [...document.querySelectorAll("div")]
  .map(el => el.textContent);
```

---

## 10. Antipatrón: parámetros de función mutante
```javascript
// ❌ WRONG — mutating the passed object
function updateUser(user) {
  user.lastModified = Date.now();  // mutates caller's object
  user.version++;
  return save(user);
}

// ✅ CORRECT — create a new object
function updateUser(user) {
  const updated = {
    ...user,
    lastModified: Date.now(),
    version: user.version + 1
  };
  return save(updated);
}
```

---

## 11. No entender el bucle de eventos y las microtareas
```javascript
// ❌ WRONG — expecting synchronous execution
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// Output: 1, 4, 3, 2 (not 1, 2, 3, 4)
// Microtasks (Promise) run before macrotasks (setTimeout)
```

---

## 12. Antipatrón: uso de `eval()`
```javascript
// ❌ WRONG — security risk and performance nightmare
const result = eval("2 + 3");
const fn = eval("(" + fnString + ")");

// ✅ CORRECT — use Function constructor (still risky) or JSON.parse
const result = 2 + 3;
const data = JSON.parse(jsonString);
```

---

## 13. Olvidarse de limpiar los oyentes de eventos
```javascript
// ❌ WRONG — memory leak
class Component {
  mount() {
    window.addEventListener("resize", this.handleResize);
  }
  // no unmount — listener persists after component is destroyed
}

// ✅ CORRECT — always clean up
class Component {
  mount() {
    window.addEventListener("resize", this.handleResize);
  }
  unmount() {
    window.removeEventListener("resize", this.handleResize);
  }
}
```

---

## 14. Copia superficial versus copia profunda
```javascript
// ❌ WRONG — spread creates shallow copy
const original = { nested: { value: 1 } };
const copy = { ...original };
copy.nested.value = 999;
original.nested.value  // 999 — original is modified!

// ✅ CORRECT — deep copy for nested objects
const copy = structuredClone(original);

// ✅ CORRECT — manual deep copy
const copy = JSON.parse(JSON.stringify(original));
// Warning: loses functions, undefined, Date, RegExp, etc.
```

---

## Resumen
La flexibilidad de JavaScript viene con trampas: el enlace`this`depende del sitio de llamada,`==`realiza coerción, las promesas requieren manejo de errores y el orden del bucle de eventos (microtareas antes que macrotareas) no es obvio. Las reglas modernas son simples: use`const`/`let`nunca `var`, prefiera`===`sobre `==`, maneje siempre los rechazos de promesas, use funciones de flecha para devoluciones de llamadas, evite mutaciones y limpie los detectores de eventos. Seguir estas reglas elimina la mayoría de los errores de JavaScript.