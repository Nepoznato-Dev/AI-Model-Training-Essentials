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
# TypeScript — 생태계 및 도구 가이드
이 가이드에서는 TypeScript 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다. TypeScript는 JavaScript와 생태계의 대부분을 공유하지만 자체적으로 특화된 도구를 가지고 있습니다.
---

## 컴파일러 및 유형 검사
| 도구 | 목적 |
|------|---------|
| **tsc** | 공식 TypeScript 컴파일러 |
| **ts-노드** | TS 직접 실행(개발자) |
| **쯧쯧** | 빠른 TS 실행(esbuild) |
| **SWC** | Rust 기반 컴파일러 |
| **건축** | TS를 지원하는 초고속 번들러 |
| **타입스크립트 SDK** | IDE 통합 |
```bash
tsc --init                      # create tsconfig.json
tsc --noEmit                    # type-check only
tsc --watch                     # watch mode
tsx src/index.ts                # run TypeScript directly
```

---

## 패키지 관리
JavaScript와 동일: **npm**, **pnpm**, **yarn**, **bun**. TypeScript는 npm 레지스트리(유형 정의를 위한`@types/*`패키지)를 사용합니다.
```bash
npm install -D @types/node @types/express  # type definitions
npx typesync                               # auto-install missing types
```

---

## 유형 정의 소스
| 소스 | 목적 |
|---------|---------|
| **확실히 유형이 지정됨** | 커뮤니티가 관리하는`@types/*`패키지 |
| **번들 유형** | 라이브러리는 자체 `.d.ts`를 제공합니다 |
| **유형 과제** | TypeScript 유형 연습 |
| **유형 축제** | 유틸리티 유형 모음 |
---

## 빌드 도구
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **비테** | 번들러 | 빠른 개발, HMR |
| **쯧** | TS 번들러 | 도서관 건물(esbuild 기반) |
| **롤업 + 플러그인** | 번들러 | 도서관 |
| **웹팩 + TS-로더** | 번들러 | 복잡한 앱 |
| **tsc** | 컴파일러 | 간단한 프로젝트 |
| **pkgroll** | 패키지 번들러 | npm 패키지 |
---

## 프레임워크(TypeScript 우선)
### 프론트엔드
| 프레임워크 | TS 지원 |
|------------|------------|
| **다음.js** | 내장형, 일류 |
| **누스트 3** | 내장 |
| **SvelteKit** | 내장 |
| **각도** | TypeScript 필요 |
| **리믹스** | 내장 |
| **아스트로** | 내장 |
### 백엔드
| 프레임워크 | TS 지원 |
|------------|------------|
| **tRPC** | 엔드투엔드형 안전 |
| **NestJS** | TypeScript 우선 |
| **호노** | TypeScript 우선 |
| **확인** | 좋은 유형 지원 |
| **익스프레스** | @types/express를 통해 |
---

## 테스트
| 프레임워크 | TS 지원 |
|------------|------------|
| **비테스트** | 네이티브 TypeScript |
| **농담 + ts-jest** | 변압기를 통해 |
| **극작가** | 네이티브 TypeScript |
| **사이프러스** | 네이티브 TypeScript |
---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **ESLint + typescript-eslint** | 유형 인식 규칙을 사용한 Linting |
| **더 예쁘다** | 서식 |
| **생물군계** | 빠른 린트 + 형식 |
| **ts-prune** | 미사용 수출품 찾기 |
| **심층검사** | 사용되지 않는 종속성 찾기 |
| **마지** | 종속성 시각화 |
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

## IDE 및 편집기
| IDE | TS 지원 |
|------|------------|
| **VS 코드** | TS 팀이 구축한 최고의 지원 |
| **웹스톰** | 뛰어난 리팩토링 |
| **커서** | AI 기반 |
---

## 풀스택형 안전성
| 도구 | 목적 |
|------|---------|
| **tRPC** | Codegen이 없는 엔드투엔드 유형 |
| **조드** | 런타임 유효성 검사 + 유형 추론 |
| **프리즈마** | 유형이 안전한 ORM |
| **이슬비** | 유형이 안전한 SQL |
| **OpenAPI + 코드 생성** | API 유형 생성 |
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

## 배포
JavaScript와 동일: **Vercel**, **Netlify**, **Cloudflare Workers**, **Docker**, **AWS Lambda** 등. TypeScript는 JavaScript로 컴파일되므로 모든 JS 배포 옵션이 작동합니다.
---

## 요약
TypeScript의 생태계는 유형 안전성을 추가하면서 JavaScript의 방대한 라이브러리를 활용합니다. 최신 스택은 빌드용 **Vite**, 테스트용 **Vitest**, Linting용 **typescript-eslint**, 런타임 검증용 **Zod**, 엔드투엔드 유형 안전성용 **tRPC**, 유형 안전 데이터베이스 액세스용 **Prisma** 또는 **Drizzle**, 전체 스택 프레임워크용 **Next.js** 또는 **Nuxt**입니다. TypeScript의 강력한 기능은 JavaScript 생태계의 폭을 유지하면서 컴파일 타임에 버그를 잡는 것입니다.