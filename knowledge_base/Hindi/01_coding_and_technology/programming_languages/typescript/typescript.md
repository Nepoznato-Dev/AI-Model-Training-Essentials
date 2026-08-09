---
# मेटाडेटा
शीर्षक: "टाइपस्क्रिप्ट"
विवरण: "टाइपस्क्रिप्ट प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
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
टैग: [टाइपस्क्रिप्ट, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "34 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# टाइपस्क्रिप्ट
टाइपस्क्रिप्ट जावास्क्रिप्ट का एक स्थिर रूप से टाइप किया गया सुपरसेट है जिसे माइक्रोसॉफ्ट (एंडर्स हेजल्सबर्ग के नेतृत्व में) द्वारा विकसित किया गया है और पहली बार 2012 में जारी किया गया है। यह जावास्क्रिप्ट में वैकल्पिक प्रकार के एनोटेशन, इंटरफेस, जेनरिक और उन्नत टाइप-सिस्टम सुविधाओं को जोड़ता है - फिर सादे जावास्क्रिप्ट में संकलित होता है जो जावास्क्रिप्ट चलाने पर कहीं भी चलता है। टाइपस्क्रिप्ट कोई अलग भाषा या रनटाइम नहीं है; यह एक टाइप चेकर वाला जावास्क्रिप्ट है।
टाइपस्क्रिप्ट बड़े पैमाने पर जावास्क्रिप्ट विकास के लिए मानक बन गया है। रिएक्ट, एंगुलर, वीएस कोड, डेनो और अधिकांश प्रमुख ओपन-सोर्स जावास्क्रिप्ट प्रोजेक्ट टाइपस्क्रिप्ट में लिखे गए हैं। यदि आप किसी भी महत्वपूर्ण आकार का एक नया जावास्क्रिप्ट प्रोजेक्ट शुरू कर रहे हैं, तो टाइपस्क्रिप्ट अनुशंसित डिफ़ॉल्ट है।
---

## टाइपस्क्रिप्ट क्यों मायने रखती है
- **संकलन समय पर बग पकड़ता है**: कोड चलने से पहले प्रकार की त्रुटियां पाई जाती हैं - उत्पादन में नहीं।
- **बेहतर आईडीई समर्थन**: स्वत: पूर्ण, गो-टू-डेफिनिशन, रीफैक्टरिंग और इनलाइन दस्तावेज़ीकरण सभी में नाटकीय रूप से सुधार होता है।
- **स्वयं-दस्तावेजीकरण कोड**: प्रकार दस्तावेज़ीकरण के रूप में कार्य करते हैं जो अद्यतित रहते हैं।
- **100% जावास्क्रिप्ट संगत**: कोई भी वैध जावास्क्रिप्ट वैध टाइपस्क्रिप्ट है। इसे आप धीरे-धीरे अपना सकते हैं.
- **उन्नत प्रकार प्रणाली**: संघ प्रकार, प्रतिच्छेदन प्रकार, सशर्त प्रकार, मैप किए गए प्रकार, टेम्पलेट शाब्दिक प्रकार - जटिल डोमेन तर्क को मॉडल करने के लिए प्रकार प्रणाली पर्याप्त रूप से अभिव्यंजक है।
- **उद्योग अपनाना**: एंगुलर को इसकी आवश्यकता है; रिएक्ट पारिस्थितिकी तंत्र इसका अत्यधिक उपयोग करता है; अधिकांश नए एनपीएम पैकेज टाइप परिभाषाओं के साथ भेजे जाते हैं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **संकलन चरण** | चलाने से पहले`.ts`→`.js`अवश्य संकलित करें | विकास के लिए`ts-node`/`tsx`का उपयोग करें;  उत्पादन के लिए __संरक्षित_4__ |
| **सीखने की अवस्था** | प्रकार प्रणाली जटिल हो सकती है (जेनेरिक, सशर्त प्रकार) | बुनियादी प्रकारों से प्रारंभ करें; उन्नत सुविधाओं को धीरे-धीरे अपनाएं |
| **प्रकार परिभाषा फ़ाइलें** | सभी एनपीएम पैकेज प्रकारों के साथ नहीं भेजे जाते | DefinitelyTyped | से`@types/package-name`इंस्टॉल करें
| **संकलन समय** | बड़े प्रोजेक्ट टाइप-चेक करने में धीमे हो सकते हैं | प्रोजेक्ट संदर्भ, `isolatedModules`, या`swc`| का उपयोग करें
| **सुरक्षा की झूठी भावना** | प्रकार रनटाइम शुद्धता की गारंटी नहीं देते | रनटाइम सत्यापन (ज़ोड, आईओ-टीएस) के साथ संयोजित करें |
---

## सिंटेक्स बुनियादी बातें
### मूल प्रकार की टिप्पणियाँ
```typescript
// Primitives
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;

// Arrays
let scores: number[] = [9.5, 8.0, 7.5];
let names: Array<string> = ["Alice", "Bob"];  // Alternative syntax

// Functions
function add(a: number, b: number): number {
    return a + b;
}

const greet = (name: string): string => `Hello, ${name}!`;

// Return type void (no return value)
function log(message: string): void {
    console.log(message);
}
```

### इंटरफ़ेस और प्रकार
```typescript
// Interface — defines the shape of an object
interface User {
    id: number;
    name: string;
    email: string;
    role: "admin" | "editor" | "viewer";  // Union type (string literal)
    createdAt: Date;
}

// Optional and readonly properties
interface Config {
    readonly apiUrl: string;
    timeout: number;
    retries?: number;  // Optional property
}

// Type alias — can represent any type (including unions, intersections)
type Status = "pending" | "active" | "inactive";
type ID = string | number;

// Extending interfaces
interface Admin extends User {
    permissions: string[];
    lastLogin: Date;
}

// Using them
const user: User = {
    id: 1,
    name: "Alice",
    email: "alice@example.com",
    role: "admin",
    createdAt: new Date(),
};
```

### जेनेरिक
```typescript
// Generic function — works with any type while preserving type safety
function first<T>(arr: T[]): T | undefined {
    return arr[0];
}

const num = first([1, 2, 3]);       // Type: number | undefined
const str = first(["a", "b", "c"]); // Type: string | undefined

// Generic interface
interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}

// Generic constraint
function getLength<T extends { length: number }>(item: T): number {
    return item.length;
}

getLength("hello");     // OK — string has .length
getLength([1, 2, 3]);   // OK — array has .length
// getLength(42);        // Error — number doesn't have .length

// Generic class
class Stack<T> {
    private items: T[] = [];
    
    push(item: T): void { this.items.push(item); }
    pop(): T | undefined { return this.items.pop(); }
    peek(): T | undefined { return this.items[this.items.length - 1]; }
    get size(): number { return this.items.length; }
}

const numbers = new Stack<number>();
numbers.push(1);
numbers.push(2);
const top = numbers.pop();  // Type: number | undefined
```

### उन्नत प्रकार
```typescript
// Union types
type Result = Success | Error;
interface Success { ok: true; data: string; }
interface Error { ok: false; error: string; }

function handle(result: Result) {
    if (result.ok) {
        console.log(result.data);   // TypeScript narrows to Success
    } else {
        console.log(result.error);  // TypeScript narrows to Error
    }
}

// Discriminated unions (pattern matching)
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "rectangle"; width: number; height: number }
    | { kind: "triangle"; base: number; height: number };

function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2;
        case "rectangle":
            return shape.width * shape.height;
        case "triangle":
            return 0.5 * shape.base * shape.height;
    }
}

// Utility types (built-in)
interface Todo {
    title: string;
    description: string;
    completed: boolean;
}

type ReadonlyTodo = Readonly<Todo>;          // All properties readonly
type PartialTodo = Partial<Todo>;             // All properties optional
type TodoPreview = Pick<Todo, "title" | "completed">;  // Only selected properties
type TodoWithoutTitle = Omit<Todo, "title">;  // All except selected

// Template literal types
type EventName = `on${Capitalize<"click" | "hover" | "focus">}`;
// Result: "onClick" | "onHover" | "onFocus"

// Conditional types
type IsString<T> = T extends string ? true : false;
type A = IsString<"hello">;  // true
type B = IsString<42>;       // false
```

### प्रकारों के साथ एसिंक
```typescript
// Typed async functions
async function fetchUser(id: number): Promise<User> {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error("User not found");
    return response.json();
}

// Typed error handling
async function safeFetch(url: string): Promise<[User, null] | [null, Error]> {
    try {
        const user = await fetchUser(1);
        return [user, null];
    } catch (error) {
        return [null, error instanceof Error ? error : new Error("Unknown")];
    }
}
```

---

## उन्नत सिंटैक्स और पैटर्न
### उन्नत जेनरिक
```typescript
// Multiple type parameters
function zip<A, B>(as: A[], bs: B[]): [A, B][] {
    const length = Math.min(as.length, bs.length);
    return Array.from({ length }, (_, i) => [as[i], bs[i]]);
}

const zipped = zip([1, 2, 3], ["a", "b", "c"]);
// Type: [number, string][]

// Generic constraints with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

const user = { name: "Alice", age: 30 };
const nameVal = getProperty(user, "name");  // Type: string
// getProperty(user, "email");  // Error: "email" is not a key of user

// Mapped types — transform existing types
type Nullable<T> = { [K in keyof T]: T[K] | null };
type Readonly2<T> = { readonly [K in keyof T]: T[K] };

// Custom utility: make specific keys required
type WithRequired<T, K extends keyof T> = T & { [P in K]-?: T[P] };
interface Form { name?: string; email?: string; age?: number; }
type RequiredName = WithRequired<Form, "name">;
// { name: string; email?: string; age?: number; }

// Infer keyword — extract types from patterns
type ReturnType2<T> = T extends (...args: any[]) => infer R ? R : never;
type UnpackPromise<T> = T extends Promise<infer U> ? U : T;

type A = ReturnType2<() => string>;  // string
type B = UnpackPromise<Promise<number>>;  // number
```

### डेकोरेटर्स (टाइपस्क्रिप्ट 5.0+ मानक)
```typescript
// Method decorator — logging
function log(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${key} with`, args);
        const result = original.apply(this, args);
        console.log(`${key} returned`, result);
        return result;
    };
    return descriptor;
}

class Calculator {
    @log
    add(a: number, b: number): number {
        return a + b;
    }
}

// Property decorator — validation
function MinLength(min: number) {
    return function (target: any, key: string) {
        let value: string = target[key];
        const getter = () => value;
        const setter = (newVal: string) => {
            if (newVal.length < min) {
                throw new Error(`${key} must be at least ${min} characters`);
            }
            value = newVal;
        };
        Object.defineProperty(target, key, { get: getter, set: setter });
    };
}

class UserDto {
    @MinLength(3)
    username!: string;
}

// Class decorator — auto-register
const registry: Function[] = [];
function register(target: Function) {
    registry.push(target);
}

@register
class UserService {
    findAll() { return []; }
}
```

### टाइप गार्ड और नैरोइंग
```typescript
// Custom type guard with "is"
function isString(value: unknown): value is string {
    return typeof value === "string";
}

function isUser(obj: unknown): obj is User {
    return (
        typeof obj === "object" &&
        obj !== null &&
        "id" in obj &&
        "name" in obj &&
        "email" in obj
    );
}

// Exhaustive checking with never
function assertNever(x: never): never {
    throw new Error(`Unexpected value: ${x}`);
}

type PaymentStatus = "pending" | "completed" | "failed" | "refunded";

function describeStatus(status: PaymentStatus): string {
    switch (status) {
        case "pending": return "Awaiting payment";
        case "completed": return "Payment received";
        case "failed": return "Payment failed";
        case "refunded": return "Payment refunded";
        default: return assertNever(status);  // Compile error if a case is missing
    }
}

// Satisfies operator (TS 4.9+) — validate without widening
const palette = {
    red: [255, 0, 0],
    green: [0, 128, 0],
    blue: [0, 0, 255],
} satisfies Record<string, [number, number, number]>;

palette.red[0] = 200;   // OK — knows it's a number array
// palette.yellow;       // Error — "yellow" not in palette
```

---

## समवर्ती एवं समांतरता
टाइपस्क्रिप्ट को जावास्क्रिप्ट का समवर्ती मॉडल विरासत में मिला है लेकिन यह एसिंक पैटर्न में प्रकार की सुरक्षा जोड़ता है।
### टाइप किए गए Async पैटर्न
```typescript
// Typed event emitter
interface EventMap {
    "user.login": { userId: number; timestamp: Date };
    "user.logout": { userId: number };
    "error": { message: string; code: number };
}

class TypedEmitter {
    private handlers: Map<string, Function[]> = new Map();

    on<K extends keyof EventMap>(event: K, handler: (data: EventMap[K]) => void) {
        const list = this.handlers.get(event as string) || [];
        list.push(handler);
        this.handlers.set(event as string, list);
    }

    emit<K extends keyof EventMap>(event: K, data: EventMap[K]) {
        const list = this.handlers.get(event as string) || [];
        list.forEach(h => h(data));
    }
}

const emitter = new TypedEmitter();
emitter.on("user.login", (data) => {
    console.log(data.userId, data.timestamp);  // Fully typed!
});

// Typed async queue
class AsyncQueue<T> {
    private queue: T[] = [];
    private resolve: ((value: T) => void) | null = null;

    push(item: T) {
        if (this.resolve) {
            this.resolve(item);
            this.resolve = null;
        } else {
            this.queue.push(item);
        }
    }

    async pop(): Promise<T> {
        if (this.queue.length > 0) {
            return this.queue.shift()!;
        }
        return new Promise<T>(resolve => { this.resolve = resolve; });
    }
}
```

---

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना निर्देशिका संरचना
```
my-ts-project/
├── src/
│   ├── index.ts
│   ├── types/
│   │   ├── user.ts
│   │   └── api.ts
│   ├── services/
│   │   └── userService.ts
│   └── utils/
│       └── validators.ts
├── tests/
│   └── services/
│       └── userService.test.ts
├── tsconfig.json
├── tsconfig.build.json
├── package.json
├── vitest.config.ts
├── .eslintrc.js
└── .github/workflows/ci.yml
```

###`tsconfig.json`- टाइपस्क्रिप्ट कॉन्फ़िगरेशन
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

### निर्माण और पैकेज प्रबंधन
```bash
# Initialize project
npm init -y
npm install typescript --save-dev
npx tsc --init

# Development (with hot reload)
npx tsx watch src/index.ts

# Build for production
npx tsc -p tsconfig.build.json

# Alternative: use esbuild for faster builds
npx esbuild src/index.ts --bundle --platform=node --outdir=dist
```

### विटेस्ट के साथ परीक्षण
```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
    test: {
        globals: true,
        coverage: {
            provider: "v8",
            reporter: ["text", "json", "html"],
        },
    },
});

// tests/services/userService.test.ts
import { describe, it, expect, vi } from "vitest";
import { UserService } from "../../src/services/userService";

describe("UserService", () => {
    it("creates a user with valid data", () => {
        const service = new UserService();
        const user = service.create({ name: "Alice", email: "alice@example.com" });
        expect(user.id).toBeDefined();
        expect(user.name).toBe("Alice");
    });

    it("throws on invalid email", () => {
        const service = new UserService();
        expect(() => service.create({ name: "Bob", email: "invalid" }))
            .toThrowError("Invalid email format");
    });

    it("calls repository with correct data", async () => {
        const mockRepo = { save: vi.fn().mockResolvedValue({ id: 1 }) };
        const service = new UserService(mockRepo);
        await service.create({ name: "Alice", email: "a@b.com" });
        expect(mockRepo.save).toHaveBeenCalledWith({
            name: "Alice",
            email: "a@b.com",
        });
    });
});
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
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"
      - run: npm ci
      - run: npm run lint
      - run: npx tsc --noEmit
      - run: npm test -- --coverage
      - run: npm run build
```

---

## उन्नत सिंटैक्स और पैटर्न
### उन्नत जेनरिक
```typescript
// Multiple type parameters
function zip<A, B>(as: A[], bs: B[]): [A, B][] {
    const length = Math.min(as.length, bs.length);
    return Array.from({ length }, (_, i) => [as[i], bs[i]]);
}

// Generic constraints with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

// Infer keyword — extract types from patterns
type ReturnType2<T> = T extends (...args: any[]) => infer R ? R : never;
type UnpackPromise<T> = T extends Promise<infer U> ? U : T;

// Mapped types
type Nullable<T> = { [K in keyof T]: T[K] | null };
type WithRequired<T, K extends keyof T> = T & { [P in K]-?: T[P] };
```

### डेकोरेटर्स (टाइपस्क्रिप्ट 5.0+)
```typescript
function log(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${key} with`, args);
        return original.apply(this, args);
    };
}

class Calculator {
    @log
    add(a: number, b: number): number { return a + b; }
}
```

### टाइप गार्ड और नैरोइंग
```typescript
function isUser(obj: unknown): obj is User {
    return typeof obj === "object" && obj !== null && "id" in obj && "name" in obj;
}

// Exhaustive checking with never
function assertNever(x: never): never { throw new Error(`Unexpected: ${x}`); }

type Status = "pending" | "active" | "done";
function handle(s: Status): string {
    switch (s) {
        case "pending": return "waiting";
        case "active": return "running";
        case "done": return "finished";
        default: return assertNever(s);
    }
}

// Satisfies operator (TS 4.9+)
const palette = { red: [255, 0, 0], green: [0, 128, 0] } satisfies Record<string, number[]>;
```

---

## प्रोजेक्ट कॉन्फ़िगरेशन और बिल्ड सिस्टम
### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### विटेस्ट के साथ परीक्षण
```typescript
import { describe, it, expect, vi } from "vitest";
import { UserService } from "../src/services/userService";

describe("UserService", () => {
    it("creates a user with valid data", () => {
        const service = new UserService();
        const user = service.create({ name: "Alice", email: "alice@example.com" });
        expect(user.name).toBe("Alice");
    });

    it("calls repository with correct data", async () => {
        const mockRepo = { save: vi.fn().mockResolvedValue({ id: 1 }) };
        const service = new UserService(mockRepo);
        await service.create({ name: "Alice", email: "a@b.com" });
        expect(mockRepo.save).toHaveBeenCalled();
    });
});
```

### राशि चक्र के साथ रनटाइम सत्यापन
```typescript
import { z } from "zod";

const UserSchema = z.object({
    id: z.number().positive(),
    name: z.string().min(1).max(100),
    email: z.string().email(),
    role: z.enum(["admin", "editor", "viewer"]),
});

type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse(unknownData);
if (result.success) {
    console.log(result.data.name);
} else {
    console.error(result.error.issues);
}
```

---

## अंतरसंचालनीयता
### जावास्क्रिप्ट लाइब्रेरीज़ का उपयोग करना
```typescript
// Installing type definitions
// npm install @types/express @types/lodash

// Declare a module for untyped packages
declare module "untyped-library" {
    export function doSomething(input: string): void;
}

// Branded types for type safety at boundaries
type UserId = string & { readonly __brand: "UserId" };
function toUserId(id: string): UserId { return id as UserId; }
```

---

## डिज़ाइन पैटर्न
### परिणाम पैटर्न
```typescript
type Result<T, E = Error> =
    | { ok: true; value: T }
    | { ok: false; error: E };

function ok<T>(value: T): Result<T, never> { return { ok: true, value }; }
function err<E>(error: E): Result<never, E> { return { ok: false, error }; }

function divide(a: number, b: number): Result<number, string> {
    if (b === 0) return err("Division by zero");
    return ok(a / b);
}
```

### रिपॉजिटरी पैटर्न
```typescript
interface Repository<T extends { id: number }> {
    findById(id: number): Promise<T | null>;
    findAll(): Promise<T[]>;
    save(entity: Omit<T, "id">): Promise<T>;
}

class UserRepository implements Repository<User> {
    async findById(id: number): Promise<User | null> { return null; }
    async findAll(): Promise<User[]> { return []; }
    async save(data: Omit<User, "id">): Promise<User> { return { ...data, id: 1 }; }
}
```

---

## तैनाती
### डॉकरफ़ाइल
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json tsconfig.json ./
RUN npm ci
COPY src/ src/
RUN npx tsc -p tsconfig.build.json

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --production
CMD ["node", "dist/index.js"]
```

---

## पारिस्थितिकी तंत्र
### प्रमुख उपकरण
| उपकरण | उद्देश्य |
|------|---------|
| **tsc** | टाइपस्क्रिप्ट कंपाइलर (आधिकारिक) |
| **ts-नोड / tsx** | अलग संकलन के बिना सीधे टाइपस्क्रिप्ट चलाएँ |
| **एसडब्ल्यूसी** | अल्ट्रा-फास्ट रस्ट-आधारित टाइपस्क्रिप्ट/जावास्क्रिप्ट कंपाइलर |
| **ESlint + टाइपस्क्रिप्ट-eslint** | प्रकार-जागरूक नियमों के साथ लिंटिंग |
| **ज़ोड** | टाइपस्क्रिप्ट अनुमान के साथ रनटाइम प्रकार सत्यापन |
| **tsconfig.json** | टाइपस्क्रिप्ट कॉन्फ़िगरेशन फ़ाइल |
### फ्रेमवर्क (सभी टाइपस्क्रिप्ट-प्रथम)
| ढाँचा | डोमेन |
|--------|-------|
| **कोणीय** | पूर्ण विशेषताओं वाला फ्रंटएंड फ्रेमवर्क (टाइपस्क्रिप्ट की आवश्यकता है) |
| **अगला.जेएस** | रिएक्ट मेटा-फ्रेमवर्क (टाइपस्क्रिप्ट-प्रथम) |
| **NestJS** | एंटरप्राइज बैकएंड फ्रेमवर्क (टाइपस्क्रिप्ट-प्रथम) |
| **टीआरपीसी** | एंड-टू-एंड टाइपसेफ एपीआई (केवल टाइपस्क्रिप्ट) |
| **प्रिज्मा** | Node.js के लिए टाइप-सुरक्षित ORM |
---

## टाइपस्क्रिप्ट का उपयोग कब करें
| परिदृश्य | टाइपस्क्रिप्ट क्यों | बेहतर विकल्प |
|---|----------------------|-----|
| बड़े जावास्क्रिप्ट प्रोजेक्ट | प्रकार की सुरक्षा बग की संपूर्ण श्रेणियों को रोकती है | -- |
| टीम प्रोजेक्ट्स | प्रकार एक साझा अनुबंध के रूप में कार्य करते हैं | -- |
| एपीआई विकास | टीआरपीसी या ओपनएपीआई के साथ एंड-टू-एंड प्रकार की सुरक्षा | सरल REST API के लिए जावा पर जाएँ |
| कोई भी नया जावास्क्रिप्ट प्रोजेक्ट | बाद में टाइपस्क्रिप्ट जोड़ने की लागत अधिक है | केवल छोटी स्क्रिप्ट के लिए सादा जेएस |
| पुस्तकालय / एनपीएम पैकेज | उपभोक्ताओं को स्वत: पूर्ण और टाइप चेकिंग मिलती है | -- |
**सामान्य नियम**: यदि आपके जावास्क्रिप्ट प्रोजेक्ट में कुछ सौ से अधिक पंक्तियाँ हैं, तो टाइपस्क्रिप्ट का उपयोग करें।
---

## सारांश
टाइपस्क्रिप्ट वह जावास्क्रिप्ट है जो सामान्य लिपियों से परे किसी भी चीज़ के लिए सही ढंग से बनाई गई है। यह एक शक्तिशाली प्रकार की प्रणाली जोड़ता है जो बग को जल्दी पकड़ता है, टूलींग में सुधार करता है, और दस्तावेज़ कोड - मानक जावास्क्रिप्ट को संकलित करते समय कहीं भी चलता है। सीखने की अवस्था धीमी है (आप न्यूनतम प्रकारों से शुरू कर सकते हैं) लेकिन गहराई विशाल है (प्रकार प्रणाली ट्यूरिंग-पूर्ण है)। आधुनिक जावास्क्रिप्ट विकास के लिए, टाइपस्क्रिप्ट उद्योग मानक बन गया है।