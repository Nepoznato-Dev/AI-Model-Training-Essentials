<!--
---
# Metadata
title: "TypeScript — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the TypeScript ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [typescript, ecosystem, tooling, npm, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# TypeScript — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the TypeScript ecosystem. TypeScript shares much of its ecosystem with JavaScript but has its own specialized tools.

---

## Compiler & Type Checking

| Tool | Purpose |
|------|---------|
| **tsc** | Official TypeScript compiler |
| **ts-node** | Run TS directly (dev) |
| **tsx** | Fast TS execution (esbuild) |
| **SWC** | Rust-based compiler |
| **esbuild** | Ultra-fast bundler with TS support |
| **TypeScript SDK** | IDE integration |

```bash
tsc --init                      # create tsconfig.json
tsc --noEmit                    # type-check only
tsc --watch                     # watch mode
tsx src/index.ts                # run TypeScript directly
```

---

## Package Management

Same as JavaScript: **npm**, **pnpm**, **yarn**, **bun**. TypeScript uses the npm registry (`@types/*` packages for type definitions).

```bash
npm install -D @types/node @types/express  # type definitions
npx typesync                               # auto-install missing types
```

---

## Type Definition Sources

| Source | Purpose |
|--------|---------|
| **DefinitelyTyped** | Community-maintained `@types/*` packages |
| **Bundled types** | Libraries ship their own `.d.ts` |
| **Type Challenges** | Practice TypeScript types |
| **type-fest** | Utility types collection |

---

## Build Tools

| Tool | Type | Best For |
|------|------|----------|
| **Vite** | Bundler | Fast dev, HMR |
| **tsup** | TS bundler | Library building (esbuild-based) |
| **Rollup + plugin** | Bundler | Libraries |
| **webpack + ts-loader** | Bundler | Complex apps |
| **tsc** | Compiler | Simple projects |
| **pkgroll** | Package bundler | npm packages |

---

## Frameworks (TypeScript-First)

### Frontend

| Framework | TS Support |
|-----------|-----------|
| **Next.js** | Built-in, first-class |
| **Nuxt 3** | Built-in |
| **SvelteKit** | Built-in |
| **Angular** | TypeScript required |
| **Remix** | Built-in |
| **Astro** | Built-in |

### Backend

| Framework | TS Support |
|-----------|-----------|
| **tRPC** | End-to-end type safety |
| **NestJS** | TypeScript-first |
| **Hono** | TypeScript-first |
| **Fastify** | Good type support |
| **Express** | Via @types/express |

---

## Testing

| Framework | TS Support |
|-----------|-----------|
| **Vitest** | Native TypeScript |
| **Jest + ts-jest** | Via transformer |
| **Playwright** | Native TypeScript |
| **Cypress** | Native TypeScript |

---

## Code Quality

| Tool | Purpose |
|------|---------|
| **ESLint + typescript-eslint** | Linting with type-aware rules |
| **Prettier** | Formatting |
| **Biome** | Fast lint + format |
| **ts-prune** | Find unused exports |
| **depcheck** | Find unused dependencies |
| **madge** | Dependency visualization |

```json
// tsconfig.json (strict)
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "moduleResolution": "bundler",
    "target": "ES2022",
    "module": "ES2022"
  }
}
```

---

## IDEs & Editors

| IDE | TS Support |
|-----|-----------|
| **VS Code** | Built by the TS team, best support |
| **WebStorm** | Excellent refactoring |
| **Cursor** | AI-powered |

---

## Full-Stack Type Safety

| Tool | Purpose |
|------|---------|
| **tRPC** | End-to-end types without codegen |
| **Zod** | Runtime validation + type inference |
| **Prisma** | Type-safe ORM |
| **Drizzle** | Type-safe SQL |
| **OpenAPI + codegen** | API type generation |

```typescript
// Zod: runtime validation with type inference
import { z } from "zod";

const UserSchema = z.object({
  name: z.string().min(2),
  email: z.string().email(),
  age: z.number().int().positive(),
});

type User = z.infer<typeof UserSchema>;
// { name: string; email: string; age: number; }

const user = UserSchema.parse(data); // throws if invalid
```

---

## Deployment

Same as JavaScript: **Vercel**, **Netlify**, **Cloudflare Workers**, **Docker**, **AWS Lambda**, etc. TypeScript compiles to JavaScript, so all JS deployment options work.

---

## Summary

TypeScript's ecosystem leverages JavaScript's vast library while adding type safety. The modern stack is: **Vite** for building, **Vitest** for testing, **typescript-eslint** for linting, **Zod** for runtime validation, **tRPC** for end-to-end type safety, **Prisma** or **Drizzle** for type-safe database access, and **Next.js** or **Nuxt** for full-stack frameworks. TypeScript's superpower is catching bugs at compile time while maintaining the JavaScript ecosystem's breadth.
