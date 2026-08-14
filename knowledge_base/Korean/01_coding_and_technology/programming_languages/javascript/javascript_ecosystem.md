<!--
---
# Metadata
title: "JavaScript — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the JavaScript ecosystem including package managers, build tools, testing frameworks, linters, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [javascript, ecosystem, tooling, npm, node, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# JavaScript — 생태계 및 도구 가이드
이 가이드에서는 JavaScript 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 런타임
| 런타임 | 환경 | 최고의 대상 |
|---------|-------------|----------|
| **Node.js** | 서버/CLI | 백엔드, API, 도구 |
| **데노** | 서버/CLI | 기본적으로 안전함, TypeScript 네이티브 |
| **빵** | 서버/CLI | 빠른 내장 번들러/테스트 실행기 |
| **브라우저** | 클라이언트 측 | 웹 애플리케이션 |
---

## 패키지 관리
| 도구 | 레지스트리 | 특징 |
|------|----------|----------|
| **npm** | npmjs.com | Node.js의 기본값 |
| **실** | npmjs.com | 작업 공간, PnP 모드 |
| **pnpm** | npmjs.com | 빠르고 디스크 효율적이며 엄격함 |
| **빵** | npmjs.com | 초고속 내장 |
```bash
npm init -y                   # initialize project
npm install express           # add dependency
npm install -D typescript     # add dev dependency
npm run build                 # run script from package.json
```

---

## 빌드 도구 및 번들러
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **비테** | 번들러 | 빠른 개발 서버, 현대적 |
| **건축** | 번들러 | 초고속, Go 기반 |
| **웹팩** | 번들러 | 성숙하고 고도로 구성 가능 |
| **롤업** | 번들러 | 도서관, 나무 흔들기 |
| **소포** | 번들러 | 제로 구성 |
| **터보팩** | 번들러 | Next.js, Rust 기반 |
| **SWC** | 컴파일러 | 빠른 TypeScript/JSX |
| **바벨** | 컴파일러 | 번역, 플러그인 |
---

## 프레임워크
### 프론트엔드
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **반응** | UI 라이브러리 | 컴포넌트 기반 UI, 생태계 |
| **뷰** | 프로그레시브 | 접근하기 쉽고 훌륭한 DX |
| **날씬한** | 컴파일러 | 최소한의 런타임, 빠른 |
| **각도** | 전체 프레임워크 | Enterprise, TypeScript 우선 |
| **단단한** | 반응성 | 세분화된 반응성 |
| **아스트로** | 정적/SSR | 콘텐츠 사이트, 섬 |
### 백엔드
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **익스프레스** | 마이크로 | 간단한 API, 미들웨어 |
| **확인** | 성과 | 처리량이 높은 API |
| **NestJS** | 기업 | 구조화, DI, TypeScript |
| **호노** | 엣지 | 경량, 다중 런타임 |
| **코아** | 현대 | 익스프레스 후계자 |
---

## 테스트
| 프레임워크 | 유형 |
|------------|------|
| **비테스트** | 빠른 Vite 기반 |
| **농담** | 성숙한 스냅샷 테스트 |
| **극작가** | E2E, 멀티 브라우저 |
| **사이프러스** | E2E, 개발자 경험 |
| **테스트 라이브러리** | 구성 요소 테스트 |
| **모카** | 유연한 플러그인 기반 |
```bash
vitest                        # run tests
vitest --coverage             # with coverage
playwright test               # E2E tests
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **ESLint** | Linter(구성 가능한 규칙) |
| **더 예쁘다** | 코드 포맷터 |
| **생물군계** | 빠른 린터 + 포맷터(Rust) |
| **타입스크립트** | 정적 유형 검사 |
| **ts-패턴** | TS에 대한 패턴 일치 |
```json
// eslint.config.js (flat config)
export default [
  { rules: { "no-unused-vars": "warn" } }
];
```

---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드** | 지배적이고 우수한 JS/TS 지원 |
| **웹스톰** | 모든 기능을 갖춘 JetBrains IDE |
| **커서** | AI 기반 VS Code 포크 |
| **네오빔** | LSP를 사용한 터미널 기반 |
---

## 배포
| 플랫폼 | 유형 |
|------------|------|
| **베르셀** | 프런트엔드/서버리스(Next.js) |
| **넷티파이** | 프론트엔드/잼스택 |
| **Cloudflare 작업자** | 엣지 컴퓨팅 |
| **철도** | 풀스택 PaaS |
| **플라이.io** | 앱 호스팅, 글로벌 |
| **AWS 람다** | 서버리스 |
| **도커** | 컨테이너화 |
---

## 요약
JavaScript의 생태계는 프로그래밍 분야에서 가장 큽니다. 최신 스택은 빌드용 **Vite**, 패키지용 **pnpm**, 테스트용 **Vitest**, 코드 품질용 **ESLint + Prettier**, 프런트엔드용 **React/Next.js** 또는 **Vue/Nuxt**, 배포용 **Vercel** 또는 **Cloudflare**입니다. TypeScript는 이제 모든 심각한 프로젝트에 필수적입니다. 생태계는 빠르게 움직입니다. 최신 상태를 유지하되 프레임워크 이탈을 방지하세요.